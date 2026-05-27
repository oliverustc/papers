---
title: "Aggregatable subvector commitments for stateless cryptocurrencies"
doi: 10.1007/978-3-030-57990-6_3
标题简称:
论文类型: conference
会议简称: SCN
发表年份: 2020
---
## Aggregatable subvector commitments for stateless cryptocurrencies

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-030-57990-6_3)

## 作者

+ [[Alin Tomescu]]
+ Ittai Abraham 
+ Vitalik Buterin 
+ Justin Drake 
+ Dankrad Feist 
+ [Dmitry Khovratovich](Dmitry%20Khovratovich.md)
## 笔记

### 背景与动机
无状态加密货币允许矿工和用户不存储完整的账本状态，仅维护一个简洁的摘要，用户各自存储自己的账户余额和证明，从而大幅降低存储需求并支持分片等扩展方案 [CPZ18]。然而，现有基于向量承诺的构造面临若干瓶颈：承诺证明的大小为对数级而非常数级，证明更新需要对数级时间，更新密钥（update key）的大小也呈线性关系，且多个证明无法聚合为更紧凑的子向量证明。此外，矿工需要存储全部 O(n) 个更新密钥以验证交易，这带来了高昂的存储开销 [CPZ18, GRWZ20]。本文旨在填补一个空白：设计一种支持常数大小证明、常数时间更新、且可聚合的向量承诺方案，并以此构建一个通信与计算开销极低的无状态加密货币，同时通过可验证的更新密钥消除矿工对全部更新密钥的存储需求。

### 相关工作

[CPZ18] Chepurnoy et al. Edrax: A Cryptocurrency with Stateless Transaction Validation. **ePrint 2018** [Google Scholar](https://scholar.google.com/scholar?q=Edrax+A+Cryptocurrency+with+Stateless+Transaction+Validation)
> 核心思路：首次提出基于向量承诺构建账户型无状态加密货币，运用多元多项式承诺实现对数大小证明。
> 局限与区别：证明大小为对数而非常数，不可聚合，更新密钥大小为对数级，矿工需存储全部 O(n) 个更新密钥。本文以常数大小、可聚合的证明克服这些局限。

[GRWZ20] Gorbunov et al. Pointproofs: Aggregating Proofs for Multiple Vector Commitments. **CCS 2020** [Google Scholar](https://scholar.google.com/scholar?q=Pointproofs+Aggregating+Proofs+for+Multiple+Vector+Commitments)
> 核心思路：形式化可跨承诺聚合的向量承诺，支持将多个子向量证明聚合成常数大小。
> 局限与区别：方案要求 O(n) 大小的验证密钥和更新密钥，无法高效预计算所有证明，且不适用于 Edrax 型支付场景。本文的更新密钥为常数大小，且支持 O(n log n) 预计算所有证明。

[BBF19] Boneh et al. Batching Techniques for Accumulators with Applications to IOPs and Stateless Blockchains. **CRYPTO 2019** [Google Scholar](https://scholar.google.com/scholar?q=Batching+Techniques+for+Accumulators+with+Applications+to+IOPs+and+Stateless+Blockchains)
> 核心思路：基于隐藏阶群构造常数大小公开参数的向量承诺，支持特定条件下的证明聚合。
> 局限与区别：使用动态更新提示（update hint）而非静态更新密钥，不利于无状态加密货币设计；基于隐藏阶群的证明具有更大的具体尺寸。本文采用双线性群，证明更小，且使用静态可验证更新密钥。

[CFG+20] Campanelli et al. Vector Commitment Techniques and Applications to Verifiable Decentralized Storage. **ePrint 2020** [Google Scholar](https://scholar.google.com/scholar?q=Vector+Commitment+Techniques+and+Applications+to+Verifiable+Decentralized+Storage)
> 核心思路：形式化子向量承诺的无限（反）聚合概念，提供基于隐藏阶群和双线性群的方案。
> 局限与区别：隐藏阶群方案具体证明尺寸较大，双线性群方案的更新密钥仍为常数但未提供快速预计算所有证明的方法。本文的预计算、更新和聚合均达到拟线性或常数时间，且更新密钥可验证。

[LM19] Lai et al. Subvector Commitments with Application to Succinct Arguments. **CRYPTO 2019** [Google Scholar](https://scholar.google.com/scholar?q=Subvector+Commitments+with+Application+to+Succinct+Arguments)
> 核心思路：形式化子向量承诺，并从 [CF13] 的构造扩展出常数大小的子向量证明。
> 局限与区别：其更新密钥和验证密钥均为 O(n) 大小，且不支持证明聚合。本文通过部分分式分解实现聚合，更新密钥为常数。

[KZG10] Kate et al. Constant-size Commitments to Polynomials and Their Applications. **ASIACRYPT 2010** [Google Scholar](https://scholar.google.com/scholar?q=Constant-size+Commitments+to+Polynomials+and+Their+Applications)
> 核心思路：提出常数大小的多项式承诺方案，支持常数大小评估证明。
> 局限与区别：该方案本身不支持更新操作，也不支持聚合。本文在其基础上利用拉格朗日多项式表示向量，并引入更新密钥和聚合机制。

[CDHK15] Camenisch et al. Composable and Modular Anonymous Credentials: Definitions and Practical Constructions. **ASIACRYPT 2015** [Google Scholar](https://scholar.google.com/scholar?q=Composable+and+Modular+Anonymous+Credentials+Definitions+and+Practical+Constructions)
> 核心思路：基于拉格朗日多项式的 KZG 承诺构造绑定且隐藏的向量承诺，支持更新。
> 局限与区别：其方案刻意避免证明聚合以增强安全性，未提供聚合功能；更新密钥为 O(n)。本文在类似基础上加入聚合，且更新密钥压缩为常数。

[Tom20] Tomescu. How to Keep a Secret and Share a Public Key (Using Polynomial Commitments). **PhD thesis 2020** [Google Scholar](https://scholar.google.com/scholar?q=How+to+Keep+a+Secret+and+Share+a+Public+Key+Using+Polynomial+Commitments)
> 核心思路：利用单变量多项式承诺构建子向量证明，支持对数大小的更新密钥。
> 局限与区别：证明仍为对数大小，不支持聚合。本文将其证明压缩为常数并支持聚合。

[FK20] Feist et al. Fast amortized Kate proofs. **GitHub 2020** [Google Scholar](https://scholar.google.com/scholar?q=Fast+amortized+Kate+proofs)
> 核心思路：提出在单位根点上快速预计算所有 KZG 评估证明的技术，时间复杂度 O(n log n)。
> 局限与区别：该技术本身不是完整的向量承诺方案，且未涉及聚合和更新。本文直接采用该技术实现所有证明的快速预计算，并扩展到更新密钥的快速计算。

### 核心技术与方案

本文提出一种可聚合子向量承诺（aSVC）方案，由五个主要部分组成：密钥生成、承诺、证明生成、验证与聚合，以及证明更新。方案以 KZG 多项式承诺为基础，利用拉格朗日多项式表示向量：令 $\omega$ 为 $n$ 次单位根，向量 $\mathbf{v} = [v_0, \ldots, v_{n-1}]$ 被编码为多项式 $\phi(X) = \sum_{i=0}^{n-1} \mathcal{L}_i(X) v_i$，其中 $\mathcal{L}_i(X)$ 是满足 $\mathcal{L}_i(\omega^i)=1$、$\mathcal{L}_i(\omega^j)=0$ 的拉格朗日多项式。承诺即为 $c = g^{\phi(\tau)}$，可通过公开参数 $\ell_i = g^{\mathcal{L}_i(\tau)}$ 线性组合计算：$c = \prod_i (\ell_i)^{v_i}$。

**聚合证明**：给定一组单点证明 $\pi_i = g^{q_i(\tau)}$，其中 $q_i(X) = (\phi(X)-v_i)/(X-\omega^i)$，希望聚合为子向量证明 $\pi_I$ 对应集合 $I$。利用部分分式分解，得到关键等式：
$$
\frac{1}{A_I(X)} = \sum_{i\in I} \frac{1}{A_I'(\omega^i)(X-\omega^i)},
$$
其中 $A_I(X)=\prod_{i\in I}(X-\omega^i)$。由此可导出：
$$
q(X) = \frac{\phi(X)-R(X)}{A_I(X)} = \sum_{i\in I} \frac{1}{A_I'(\omega^i)} \cdot q_i(X),
$$
其中 $R(X)$ 是满足 $R(\omega^i)=v_i$ 的插值多项式。因此 $\pi_I = \prod_{i\in I} \pi_i^{c_i}$，系数 $c_i = 1/A_I'(\omega^i)$ 可在 $O(|I|\log^2|I|)$ 时间内计算。

**证明更新**：当元素 $v_j$ 变化 $\delta$ 时，用户需要更新自己的证明 $\pi_i$。分两种情况：
- 当 $i=j$ 时，$\pi_i' = \pi_i \cdot (u_i)^\delta$，其中 $u_i = g^{(\mathcal{L}_i(\tau)-1)/(\tau-\omega^i)}$ 包含在更新密钥 $\mathsf{upk}_i$ 中。
- 当 $i\neq j$ 时，$\pi_i' = \pi_i \cdot (u_{i,j})^\delta$，其中 $u_{i,j}$ 由 $\mathsf{upk}_i$ 和 $\mathsf{upk}_j$ 中的 $a_i = g^{A(\tau)/(\tau-\omega^i)}$ 通过组合计算得出。

更新密钥 $\mathsf{upk}_i$ 由 $(a_i, u_i)$ 构成，均为常数大小。验证密钥 $\mathsf{vrk}$ 包含 $a = g^{A(\tau)}$ 和 $g^{\tau^i}$ 以支持子向量验证。安全性基于 $q$-SBDH 假设，证明位置绑定性和更新密钥唯一性。

在无状态加密货币应用中，本文利用 aSVC 改进 Edrax 方案：矿工可聚合块中所有交易证明为单个群元，验证时仅需 2 次配对加 $b$ 次群指数；更新密钥可验证，矿工无需存储全部 $O(n)$ 个密钥，只需从交易中直接验证；每个用户更新证明的时间为 $O(b)$ 而非 $O(b\log n)$。如表 1 所示，方案在证明大小、更新密钥大小、聚合证明大小和计算复杂度上均优于前人工作。

### 核心公式与流程

**[部分分式分解公式]**
$$
\frac{1}{A_I(X)} = \frac{1}{\prod_{i\in I}(X-\omega^i)} = \sum_{i\in I} \frac{1}{A_I'(\omega^i)(X-\omega^i)}
$$
> 作用：将分母多项式求逆分解为简单一次分式的加权和，是实现证明聚合的核心代数工具。

**[聚合证明计算公式]**
$$
\pi_I = \prod_{i\in I} \pi_i^{c_i}, \quad c_i = \frac{1}{A_I'(\omega^i)}
$$
> 作用：将 $|I|$ 个单点 KZG 证明线性组合为一个常数大小的子向量证明，系数仅依赖于根集 $I$ 的结构。

**[证明更新公式（$i = j$ 时）]**
$$
\pi_i' = \pi_i \cdot (u_i)^\delta, \quad u_i = g^{\frac{\mathcal{L}_i(\tau)-1}{\tau-\omega^i}}
$$
> 作用：当自身余额变化 $\delta$ 时，用户只需用更新密钥中的 $u_i$ 进行一次群指数运算即可更新证明。

**[证明更新公式（$i \neq j$ 时）]**
$$
\pi_i' = \pi_i \cdot (u_{i,j})^\delta, \quad u_{i,j} = \left( a_i^{\frac{1}{\omega^i-\omega^j}} \cdot a_j^{\frac{1}{\omega^j-\omega^i}} \right)^{\frac{1}{A'(\omega^j)}}, \quad a_i = g^{\frac{A(\tau)}{\tau-\omega^i}}
$$
> 作用：当他人余额变化时，用户借助自己的更新密钥 $a_i$ 和交易中附带的 $a_j$ 组合出更新因子，完成常数时间更新。

**[VC.AggregateProofs 算法]**
1. 计算 $A_I(X) = \prod_{i\in I}(X-\omega^i)$ 及其导数 $A_I'(X)$；
2. 计算全部 $c_i = (A_I'(\omega^i))^{-1}$，耗时 $O(|I|\log^2|I|)$；
3. 输出 $\pi_I = \prod_{i\in I} \pi_i^{c_i}$，通过多指数运算在 $O(|I|)$ 群操作内完成。
> 作用：给出了聚合证明的完整可计算流程，所有运算均在域和群上高效实现。

**[子向量验证双线性检查]**
$$
e\left(c / g^{R_I(\tau)}, g\right) = e\left(\pi_I, g^{A_I(\tau)}\right)
$$
其中 $R_I(X)$ 是插值多项式满足 $R_I(\omega^i)=v_i$，$A_I(\tau)$ 由验证密钥中的参数计算。
> 作用：通过一次配对等式验证整个子向量，等价于检查 $\phi(\tau)-R_I(\tau) = q(\tau)A_I(\tau)$，确保聚合证明的正确性。

### 实验结果

本文未进行具体的性能实验，所有比较均基于渐近复杂度分析，汇总在表1和表2中。表1对比了 Edrax [CPZ18]、Pointproofs [GRWZ20]、第二个VC方案 [CFG+20] 与本文在无状态加密货币场景下的渐近开销：本文的证明大小 $\lvert\pi_i\rvert=1|\mathbb{G}|$，与 Pointproofs 和 [CFG+20] 持平，优于 Edrax 的 $\log n|\mathbb{G}|$；更新密钥大小 $\lvert\mathsf{upk}_i\rvert=1|\mathbb{G}|$，优于 Edrax 的 $\log n|\mathbb{G}|$ 和 Pointproofs 的 $n|\mathbb{G}|$；聚合证明大小 $\lvert\pi_I\rvert=1|\mathbb{G}|$，与 Pointproofs 和 [CFG+20] 持平；矿工存储从 $n|\mathbb{G}|$ 降至 $b|\mathbb{G}|$（$b$ 为块大小）；块验证时间只需 2 次配对加 $b$ 次群指数（外加 $b\log^2 b$ 次快速域运算），远低于 Edrax 的 $b\log n$ 次配对。

表2比较了各方案在向量承诺本身上的复杂度：本文的更新密钥大小为常数，验证密钥大小为 $b$（子向量大小），预计算所有证明的复杂度为 $O(n\log n)$（借助 FK 技术 [FK20]），均优于或持平现有方案。所有比较均基于理论分析，未提供具体微基准测试或端到端系统延迟数值。

### 局限性与开放问题

本文的有界向量承诺要求预定义最大用户数 $n$，导致注册过程可能遭受拒绝服务攻击——攻击者可快速耗尽向量空位。作者提出了几种缓解措施（如使用隐藏阶群的无界方案、多个有界 aSVC 跨承诺聚合、INITSPEND 交易收费等），但均未深入分析其安全性与效率权衡。此外，方案依赖可信初始化阶段生成公共参数，虽可通过 MPC 去中心化 [BGM17]，但实际部署中 MPC 的通信与计算开销较大。支持交易计数器以避免重放攻击需要额外技巧（如双 aSVC 方案），作者仅给出初步思路，未提供完整构造与安全性证明。未来工作可探索无界、可扩展的认证字典，以及更高效的可验证更新密钥分发协议。

### 强关联论文

[CPZ18] Chepurnoy et al. Edrax: A Cryptocurrency with Stateless Transaction Validation. **ePrint 2018** [Google Scholar](https://scholar.google.com/scholar?q=Edrax+A+Cryptocurrency+with+Stateless+Transaction+Validation)

[GRWZ20] Gorbunov et al. Pointproofs: Aggregating Proofs for Multiple Vector Commitments. **CCS 2020** [Google Scholar](https://scholar.google.com/scholar?q=Pointproofs+Aggregating+Proofs+for+Multiple+Vector+Commitments)

[BBF19] Boneh et al. Batching Techniques for Accumulators with Applications to IOPs and Stateless Blockchains. **CRYPTO 2019** [Google Scholar](https://scholar.google.com/scholar?q=Batching+Techniques+for+Accumulators+with+Applications+to+IOPs+and+Stateless+Blockchains)

[CFG+20] Campanelli et al. Vector Commitment Techniques and Applications to Verifiable Decentralized Storage. **ePrint 2020** [Google Scholar](https://scholar.google.com/scholar?q=Vector+Commitment+Techniques+and+Applications+to+Verifiable+Decentralized+Storage)

[LM19] Lai et al. Subvector Commitments with Application to Succinct Arguments. **CRYPTO 2019** [Google Scholar](https://scholar.google.com/scholar?q=Subvector+Commitments+with+Application+to+Succinct+Arguments)

[KZG10] Kate et al. Constant-size Commitments to Polynomials and Their Applications. **ASIACRYPT 2010** [Google Scholar](https://scholar.google.com/scholar?q=Constant-size+Commitments+to+Polynomials+and+Their+Applications)

[CDHK15] Camenisch et al. Composable and Modular Anonymous Credentials: Definitions and Practical Constructions. **ASIACRYPT 2015** [Google Scholar](https://scholar.google.com/scholar?q=Composable+and+Modular+Anonymous+Credentials+Definitions+and+Practical+Constructions)

[Tom20] Tomescu. How to Keep a Secret and Share a Public Key (Using Polynomial Commitments). **PhD thesis 2020** [Google Scholar](https://scholar.google.com/scholar?q=How+to+Keep+a+Secret+and+Share+a+Public+Key+Using+Polynomial+Commitments)

[FK20] Feist et al. Fast amortized Kate proofs. **GitHub 2020** [Google Scholar](https://scholar.google.com/scholar?q=Fast+amortized+Kate+proofs)

[CF13] Catalano et al. Vector Commitments and Their Applications. **PKC 2013** [Google Scholar](https://scholar.google.com/scholar?q=Vector+Commitments+and+Their+Applications)


## 关键词

+ 可聚合子向量承诺aSVC
+ 无状态加密货币
+ 多项式承诺
+ KZG常数大小证明
+ 配对友好群
+ 区块链验证效率