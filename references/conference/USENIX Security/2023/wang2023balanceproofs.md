---
title: "BalanceProofs: Maintainable vector commitments with fast aggregation"
标题简称:
论文类型: conference
会议简称: USENIX Security
发表年份: 2023
created: 2025-04-17 10:20:42
modified: 2025-04-17 10:24:04
---

## BalanceProofs: Maintainable vector commitments with fast aggregation

## 发表信息

+ [原文链接](https://www.usenix.org/conference/usenixsecurity23/presentation/wang-weijie)

## 作者

+ Weijie Wang 
+ Annie Ulichney 
+ [Charalampos Papamanthou](Charalampos%20Papamanthou.md) 

## 笔记

### 背景与动机
向量承诺是一种强大的密码学原语，相较于传统默克尔树，其具备简洁（甚至恒定大小）的证明、高效的更新以及将多个证明聚合为单一对象的能力。该原语在无状态加密货币、存储证明等场景中具有重要应用 [1, 2, 6, 11, 13, 21, 22, 25, 31, 33, 35, 37, 42]。然而，现有的方案设计面临一个根本性权衡：一些方案（如默克尔树 [24]、AMT [36]）支持高效的亚线性更新（可维护），但缺乏有效的证明聚合算法；另一些方案（如 aSVC [37]、Pointproofs [15]）支持自然且高效的聚合，但在每次向量更新时，需要使用线性时间重新计算所有证明，因此不可维护。唯一的例外是 Hyperproofs [33]，它同时支持可维护与可聚合，但它是通过黑盒使用内积论证 [8] 来实现聚合的，这导致了极差的实际性能——其聚合和验证时间比 aSVC 等方案慢 100 到 1000 倍，严重限制了其在需要多方频繁验证聚合证明的应用（如区块链）中的实用性。因此，本文旨在填补这一空白：构建一个**同时具备可维护性与自然聚合能力**的向量承诺方案，在保证高效更新的同时，大幅提升聚合证明的生成与验证速度。

### 相关工作

[12] Catalano 等. Vector Commitments and Their Applications. **PKC 2013** [Google Scholar](https://scholar.google.com/scholar?q=Vector+Commitments+and+Their+Applications)
> 核心思路：首次形式化定义向量承诺，并提出基于 RSA 和 CDH 假设的实例化方案。
> 局限与区别：这两个方案在向量更新后，需要线性时间重新计算所有证明，不具备可维护性。

[24] Merkle. A Digital Signature Based on a Conventional Encryption Function. **CRYPTO 1987** [Google Scholar](https://scholar.google.com/scholar?q=A+Digital+Signature+Based+on+a+Conventional+Encryption+Function)
> 核心思路：提出经典的默克尔树，支持对 n 个值的对数时间验证，通过反事实路径提供单点证明。
> 局限与区别：默克尔树天然的树状结构使其难以高效地对来自不同分支的多个单点证明进行聚合。

[15] Gorbunov 等. Pointproofs: Aggregating Proofs for Multiple Vector Commitments. **CCS 2020** [Google Scholar](https://scholar.google.com/scholar?q=Pointproofs%3A+Aggregating+Proofs+for+Multiple+Vector+Commitments)
> 核心思路：提出一种向量承诺方案，其核心贡献在于支持跨多个不同承诺的证明聚合，降低智能合约中的存储需求。
> 局限与区别：Pointproofs 本身不支持可维护性，向量发生任何更新后，所有相关的单个证明都需要线性时间重新生成。本文将其作为编译器的一个输入实例。

[37] Tomescu 等. Aggregatable Subvector Commitments for Stateless Cryptocurrencies. **SCN 2020** [Google Scholar](https://scholar.google.com/scholar?q=Aggregatable+Subvector+Commitments+for+Stateless+Cryptocurrencies)
> 核心思路：基于 KZG 多项式承诺提出 aSVC，支持将任意位置的证明高效聚合成一个恒定大小的批处理证明，并能对证明进行亚线性更新。
> 局限与区别：aSVC 在向量向量更新后，更新所有单个证明的时间为 O(n)，不具备可维护性。本文的编译器以 aSVC 为基础输入，目的是赋予其可维护性。

[33] Srinivasan 等. Hyperproofs: Aggregating and Maintaining Proofs in Vector Commitments. **USENIX Security 2022** [Google Scholar](https://scholar.google.com/scholar?q=Hyperproofs%3A+Aggregating+and+Maintaining+Proofs+in+Vector+Commitments)
> 核心思路：在 PST 承诺上构建多层线性树（MLT），实现 O(log n) 时间更新所有证明。为了支持聚合，采用内积论证（IPA）作为黑盒。
> 局限与区别：虽然同时满足可维护与可聚合，但其黑盒使用 IPA 导致实际聚合和验证时间极慢（亚秒级至分钟级），成为性能瓶颈。本文目标是避免这种黑盒使用，实现“自然”聚合。

[36] Tomescu. How to Keep a Secret and Share a Public Key (Using Polynomial Commitments). **PhD Thesis 2020** [Google Scholar](https://scholar.google.com/scholar?q=How+to+Keep+a+Secret+and+Share+a+Public+Key+(Using+Polynomial+Commitments))
> 核心思路：提出 AMT（Authenticated Multipoint Evaluation Trees），主要贡献在于构建一种可维护的见证。
> 局限与区别：AMT 虽然支持对数时间的更新和验证，但并未给出有效的聚合算法。

### 核心技术与方案
本文的核心贡献是 BalanceProofs，它包含两个层次的技术：一是通用编译器，二是用于优化的分桶技术。

**BalanceProofs 编译器（第3节）**：该编译器接收一个不可维护的、但支持自然聚合和线性时间打开所有位置证明的向量承诺 VC（如 aSVC 或 Pointproofs），输出一个可维护的向量承诺 VC'。核心思路是“记账”策略。在每次收到更新操作 $(i, \delta)$ 后，并不立即调用 VC 的 `UpdAllProofs` 算法（该算法需要 $\Omega(n)$ 时间对所有证明进行更新），而是将更新记录在一个大小上限为 $\sqrt{n}$ 的日志列表 $L$ 中。当列表 $L$ 被填满时，才调用 `OpenAll` 算法以 $O(n \log n)$ 时间重新计算所有证明并清空列表。对于在列表达到容量上限之前的单点查询请求，算法会遍历日志 $L$ 中的所有更新，并依次调用 $O(1)$ 时间的 `UpdProof` 算法来更新目标证明，因此单次查询时间为 $O(\sqrt{n})$。经过摊销分析，更新所有证明的摊销时间为 $O(T/\sqrt{n}) = O(\sqrt{n} \log n)$，其中 $T=O(n \log n)$ 是 `OpenAll` 的时间。为了进一步优化最坏情况性能，论文还提出了去摊销化技术：将 `OpenAll` 算法拆分为 $\sqrt{n}$ 个耗时均匀的子步骤，并维护一个大小为 $2\sqrt{n}$ 的缓冲区。当列表达到 $\sqrt{n}$ 个条目时，后续的每次更新先记录，再执行一个子步骤，从而在 $\sqrt{n}$ 次更新后完成全部证明的重新计算，保证单次更新的最坏时间复杂度也达到 $O(\sqrt{n} \log n)$。

**分桶技术（第4节）**：基本编译器的更新时间为 $\sqrt{n} \log n$，对于大型向量来说仍然较慢。分桶技术旨在进一步降低更新时间，代价是聚合证明大小从常数增长为亚线性。该技术将原始 $n$ 维向量划分成 $p$ 个桶（bucket）。构造上，论文使用一个双变量多项式 $\phi(x, y) = \sum_{i=0}^{p-1}\mathcal{L}_i(x)\phi_i(y)$ 来表示整个向量，其中 $x$ 上的 degree 为 $p$，$y$ 上的 degree 为 $n/p$。承诺 $C = g^{\phi(\alpha, \beta)}$ 仍然是单个群元素。每个桶 $P_i$ 对应一个“桶证明” $\Pi_i = g^{q_i(\alpha, \beta)}$，用于证明整个桶内所有位置的正确性；桶内每个位置 $j$ 有一个“个体证明” $\pi_{i,j} = g^{q_{i,j}(\beta)}$。验证单点 $(i, j)$ 的方程为：$e(C/g^z, g) = e(\Pi_i, g^{\alpha - \varphi^i}) \cdot e(\pi_{i,j}, g^{\beta - \theta^j})$。在更新时，由于有两个独立的变量，桶证明的更新可以通过预计算更新参数在 $O(p)$ 时间内完成，而个体证明的更新则在桶内利用编译器实现，时间为 $O(\sqrt{n/p} \log(n/p))$。通过设置 $p = n^{1/3}$ 使两阶段时间平衡，总更新时间为 $O(n^{1/3} \log n)$。当 $I$ 跨越多个桶时，聚合证明 $\pi_I$ 的大小与涉及的桶数量 $p$ 成正比。论文进一步提出**双层分桶**，引入第三个变量 $z$，将向量划分为 $p$ 个一级桶，每个桶再分为 $t$ 个二级桶。这样，更新时间为 $O(p + t + \sqrt{n/(pt)} \log(n/(pt)))$，通过选取 $p=t=n^{1/4}$，更新时间降至 $O(n^{1/4} \log n)$，而聚合证明大小上限增至 $O(\sqrt{n})$。论文还提出了一种将批处理证明大小从 $2f$ 群元素减至 $f+1$ 的优化技术（见公式3、4）。

**安全性**：论文在第4.3节和第 C 节证明了双层分桶方案满足计算绑定性质。证明基于 $q$-SBDH 假设，通过标准的安全规约：假设存在攻击者能伪造针对某个位置 $(i,j,k)$ 的证明，则构造一个规约者，该规约者在不知道有毒垃圾 $\tau$ 的情况下，利用攻击者的输出来计算 $e(g,g)^{1/(\alpha - \varphi^i)}$，从而打破 $q$-SBDH 假设。证明的关键步骤在于利用了“技巧化”的公钥参数（如设置 $\beta - \theta^j = r_0(\alpha - \varphi^i)$），并通过消去法从两个不同的伪造证明中提取出所需的 $q$-SBDH 解。

### 核心公式与流程

**[Lagrange 插值]**
$$\mathcal{L}_i(x) = \prod_{j \in [0, n) \backslash i} \frac{x - \omega^j}{\omega^i - \omega^j},\quad \phi(x) = \sum_{i \in [0, n)} \mathcal{L}_i(x) \cdot m_i$$
> 作用：是 aSVC 和本文方案的核心工具，用于将向量编码为多项式，使得 $\phi(\omega^i) = m_i$。

**[aSVC 的单点证明]**
$$\pi_i = g^{q_i(\tau)}, \quad q_i(x) = \frac{\phi(x) - m_i}{x - \omega^i}$$
> 作用：证明值 $m_i$ 是多项式 $\phi(x)$ 在点 $\omega^i$ 处的求值结果，是一个 KZG 多项式承诺。

**[双层分桶方案的验证公式]**
$$e(C / g^z, g) = e(\Pi_i, g^{\alpha - \varphi^i}) \cdot e(\Psi_{i,j}, g^{\beta - \theta^j}) \cdot e(\pi_{i,j,k}, g^{\gamma - \eta^k})$$
> 作用：验证单个位置 $(i, j, k)$ 的值 $z$ 的正确性，验证需要三个配对运算。

**[去摊销化更新流程]**
1. 维护大小为 $2\sqrt{n}$ 的日志列表 $L$。
2. 前 $\sqrt{n}$ 次更新仅追加到 $L$。
3. 接下来的 $\sqrt{n}$ 次更新：每次更新先追加到 $L$，然后执行 `OpenAll` 的一个子步骤 $T_{j-\sqrt{n}}$。
4. 当 $L$ 大小达到 $2\sqrt{n}$ 时，所有证明已重新计算，丢弃前 $\sqrt{n}$ 条更新记录。
> 作用：将 `UpdAllProofs` 的最坏情况时间复杂度从 $\Omega(n)$ 降低到 $O(\sqrt{n} \log n)$。

### 实验结果
论文在 AWS EC2 m5d.4xlarge 实例（8核，64GB RAM）上对单线程实现的 BalanceProofs 进行了评估，基础方案基于 aSVC，并使用 BLS12-381 曲线。

**微基准测试**：对于大小为 $n=2^{30}$ 的向量，基本 BalanceProofs 的更新时间为 135.7 秒，而双层分桶方案（$p=t=n^{1/4}$）将时间降至 18.96 毫秒。基本方案的单点查询时间为 0.77 秒，双层分桶方案为 19.41 毫秒。在聚合 1024 个证明时，基本方案和双层分桶方案的聚合时间分别为 0.41 秒和 8.41 毫秒，聚合验证时间分别为 0.42 秒和 106 毫秒。双层分桶的个体证明大小为 144 字节，聚合证明大小为 51KB。

**与 Hyperproofs 对比**：在 $n=2^{30}$ 下，Hyperproofs 的聚合时间为约 100 秒，而双层分桶方案仅需约 0.01 秒，实现了约 10000 倍的加速；Hyperproofs 的聚合验证时间约 10 秒，而双层分桶方案仅约 0.1 秒，加速约 100 倍。在更新时间上，Hyperproofs（2-3 毫秒）优于双层分桶方案（约 18 毫秒）。在聚合证明大小上，当 $|I|=1024$ 时，Hyperproofs 约为 103KB，而双层分桶方案约为 51KB。

**宏观基准测试**：论文模拟了无状态加密货币场景。以 $n=2^{30}$ 和 1024 笔交易为一个区块，总共识开销（块提案时间 + 20 * 块验证时间 + 证明维护时间）为：双层分桶方案 45 秒，Hyperproofs 8 分钟，默克尔树 81 分钟。BalanceProofs 相比 Hyperproofs 实现了约 10 倍的加速，主要优势体现在快速聚合和验证上。

### 局限性与开放问题
本文方案的主要局限性在于，通过双层分桶技术优化更新时间后，聚合证明的大小从常数增长为 $\sqrt{n}$。论文指出，如何在不牺牲 $n^{1/4}$ 级更新时间的前提下，构建一个具有**常数大小**聚合证明的可维护向量承诺，仍然是一个开放问题。此外，虽然更新时间已降至毫秒级，但相比 Hyperproofs 仍有约 6 倍的差距，且目前的实现是单线程的，存在通过并行化进一步提升的空间。最后的宏观基准测试也表明，证明维护时间（M）相比 Hyperproofs 仍有约 7.5 倍的差距，这可能成为在某些场景（如区块生成速度极快）下的瓶颈。

### 强关联论文

[37] Tomescu 等. Aggregatable Subvector Commitments for Stateless Cryptocurrencies. **SCN 2020** [Google Scholar](https://scholar.google.com/scholar?q=Aggregatable+Subvector+Commitments+for+Stateless+Cryptocurrencies)

[33] Srinivasan 等. Hyperproofs: Aggregating and Maintaining Proofs in Vector Commitments. **USENIX Security 2022** [Google Scholar](https://scholar.google.com/scholar?q=Hyperproofs%3A+Aggregating+and+Maintaining+Proofs+in+Vector+Commitments)

[15] Gorbunov 等. Pointproofs: Aggregating Proofs for Multiple Vector Commitments. **CCS 2020** [Google Scholar](https://scholar.google.com/scholar?q=Pointproofs%3A+Aggregating+Proofs+for+Multiple+Vector+Commitments)

[24] Merkle. A Digital Signature Based on a Conventional Encryption Function. **CRYPTO 1987** [Google Scholar](https://scholar.google.com/scholar?q=A+Digital+Signature+Based+on+a+Conventional+Encryption+Function)

[19] Kate 等. Constant-Size Commitments to Polynomials and Their Applications. **ASIACRYPT 2010** [Google Scholar](https://scholar.google.com/scholar?q=Constant-Size+Commitments+to+Polynomials+and+Their+Applications)

[8] Bünz 等. Proofs for Inner Pairing Products and Applications. **ePrint 2019** [Google Scholar](https://scholar.google.com/scholar?q=Proofs+for+Inner+Pairing+Products+and+Applications)

[12] Catalano 等. Vector Commitments and Their Applications. **PKC 2013** [Google Scholar](https://scholar.google.com/scholar?q=Vector+Commitments+and+Their+Applications)

[5] Boneh 等. Batching Techniques for Accumulators with Applications to IOPs and Stateless Blockchains. **CRYPTO 2019** [Google Scholar](https://scholar.google.com/scholar?q=Batching+Techniques+for+Accumulators+with+Applications+to+IOPs+and+Stateless+Blockchains)


## 关键词

+ BalanceProofs可维护向量承诺
+ 亚线性更新向量承诺
+ 聚合证明快速验证
+ 无状态加密货币余额证明
+ Hyperproofs性能改进
+ 分桶技术证明优化

Hyperproof:
[Hyperproofs: Aggregating and Maintaining Proofs in Vector Commitments (**USENIX Security 2022**)](srinivasan2022hyperproofs)
