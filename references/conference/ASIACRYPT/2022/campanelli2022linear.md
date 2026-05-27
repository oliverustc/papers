---
title: "Linear-map vector commitments and their practical applications"
doi: 10.1007/978-3-031-22972-5_7
标题简称:
论文类型: conference
会议简称: ASIACRYPT
发表年份: 2022
created: 2025-04-16 09:46:23
modified: 2025-04-16 09:58:13
---
## Linear-map vector commitments and their practical applications

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-22972-5_7)

## 作者

+ [Matteo Campanelli](Matteo%20Campanelli.md) 
+ Anca Nitulescu 
+ Carla Ràfols 
+ Alexandros Zacharakis 
+ Arantxa Zapico 

## 笔记

### 背景与动机
向量承诺（VC）允许对向量生成短摘要并高效打开部分位置，是扩展去中心化网络的关键工具。现有方案在打开效率、聚合能力、更新维护等方面存在不同瓶颈：部分方案仅支持子向量打开而无法支持线性函数打开；基于RSA的聚合方案虽然支持增量聚合但实际效率不足；基于双线性群的方案如Pointproofs仅支持一跳聚合且无法重用聚合后的证明。实际应用（如无状态加密货币、可验证数据库、空间证明）对向量承诺提出了更丰富的需求：需要支持线性映射打开、证明的无限聚合、高效的更新与维护（可维护性）、以及可重用现有可信设置。本文旨在统一线性映射向量承诺（LVC）的定义，并构造满足上述属性的新方案，同时利用同态性质实现从内积到任意线性映射的泛化。

### 相关工作

[4] Boneh等. Batching techniques for accumulators with applications to IOPs and stateless blockchains. **CRYPTO 2019**
> 核心思路：基于隐藏阶群实现可批量化打开的子向量承诺。
> 局限与区别：仅支持一跳聚合（批处理），不支持无限聚合；实际效率低于配对方案。

[7] Campanelli等. Incrementally Aggregatable Vector Commitments and Applications to Verifiable Decentralized Storage. **ASIACRYPT 2020**
> 核心思路：基于RSA构造增量可聚合子向量承诺，参数常量大小。
> 局限与区别：实际效率仍不足以部署到真实系统；不支持跨承诺聚合。

[15] Gorbunov等. Pointproofs: aggregating proofs for multiple vector commitments. **ACM CCS 2020**
> 核心思路：将[22]的向量承诺扩展到跨承诺聚合，在代数群模型下安全。
> 局限与区别：仅支持一跳聚合；公共参数线性于向量长度。

[19] Kate等. Constant-size commitments to polynomials and their applications. **ASIACRYPT 2010**
> 核心思路：常数大小的多项式承诺（KZG方案），基于双线性群和幂次公共参数。
> 局限与区别：仅支持单点打开，不支持线性函数打开或聚合。

[20] Lai等. Subvector Commitments with Application to Succinct Arguments. **CRYPTO 2019**
> 核心思路：首次提出线性映射承诺（LMC），支持子向量和线性函数打开。
> 局限与区别：未考虑聚合、更新、可维护性等属性；构造基于双线性群但特定设置不可重用。

[21] Libert等. Functional commitment schemes: from polynomial commitments to pairing-based accumulators from simple assumptions. **ICALP 2016**
> 核心思路：形式化功能承诺，构造基于Diffie-Hellman指数假设的线性形式打开方案。
> 局限与区别：仅支持单个输出的线性函数，不支持多输出线性映射。

[26] Srinivasan等. Hyperproofs: aggregating and maintaining proofs in vector commitments. **USENIX Security 2022**
> 核心思路：利用多线性PST多项式承诺实现可维护的向量承诺，支持预计算和高效更新。
> 局限与区别：证明大小为log m，仅支持二进制树；设置仅基于特定多线性幂次。

[27] Tomescu等. Aggregatable subvector commitments for stateless cryptocurrencies. **SCN 2020**
> 核心思路：基于Lagrange基的双线性群构造可聚合子向量承诺，支持一跳聚合。
> 局限与区别：仅支持一跳聚合，不支持无限聚合；公共参数线性于向量长度。

### 核心技术与方案

本文首先统一线性映射向量承诺（LVC）的定义，将子向量打开、线性函数打开等作为特例。在此基础上，定义了同态证明、同态承诺、同态打开等额外性质，并证明：若LVC满足同态证明，则可泛化出无限聚合（同一承诺内）；若同时满足同态承诺和同态打开，则可实现跨承诺的无限聚合。聚合方式依赖随机预言机构造：给定两个证明 $\pi$ 和 $\pi'$ 及其对应的函数-输出对，通过哈希生成随机系数 $\gamma$，输出 $\pi^* = \pi + \gamma\pi'$；验证时，通过追踪聚合历史（树结构）重建各原始证明的系数组合，形成新函数 $f^* = \sum \delta_i f_i$ 和新输出 $y^* = \sum \delta_i y_i$，再用基础LVC验证。安全性证明使用代数群模型（AGM）和随机预言机，依赖Schwartz-Zippel引理。

进一步，本文证明：若LVC支持内积打开（即 $\mathbb{F}^m \to \mathbb{F}$）且具有同态性，则可通过聚合技巧扩展到任意线性映射 $\mathbb{F}^m \to \mathbb{F}^n$：将n个内积证明用随机系数组合成一个短证明，验证时计算组合后的函数和输出。

本文构造了两个内积LVC方案：
1. **单项式基方案**：将向量 $\mathbf{a}$ 编码为多项式 $a(X)=\sum a_i X^{i-1}$，承诺 $C_a = \sum a_i[\tau^{i-1}]_1$。打开时，给定系数向量 $\mathbf{b}$ 和声称值 $y$，寻找多项式 $R(X),H(X)$ 满足 $a(X)\cdot b(X) - yX^{m-1} = R(X) + X^m H(X)$，且 $\deg R < m-1$。证明为 $([R(\tau)]_1, [H(\tau)]_1, [\hat{R}(\tau)]_1)$，其中 $\hat{R}(X)=X R(X)$。验证用两个配对等式检验。安全性依赖于 $(m-1,m)$-BSDH假设。更新无需额外密钥：内积证明中的$R$和$H$可由已有幂次计算。
2. **Lagrange基方案**：将向量编码为Lagrange多项式 $a(X)=\sum a_i \lambda_i(X)$，其中 $\lambda_i$ 定义于乘法子群 $\mathbb{H}$。承诺 $C_a = \sum a_i[\lambda_i(\tau)]_1$。打开时满足 $a(X)b(X) - m^{-1}y = X R(X) + t(X)H(X)$，验证类似。同样满足同态性和强函数绑定。

基于上述内积方案，本文构造了可维护向量承诺：通过树形结构实现内存/时间权衡。**多变量情况**（推广Hyperproofs）：将向量分块，每块作为叶子承诺（可用任意LVC），内部节点用PST多项式承诺。根为整个向量的承诺。打开某位置时，先通过类似PST的多变量打开（包含低度测试）找到叶子，再打开叶子承诺。证明大小为 $\log_\ell (m/k) + 2 + |\pi'|$，其中 $k$ 为块大小，$\ell$ 为树的分支数。预计算所有内部路径证明可在 $O(\lambda k\nu\ell^\nu)=O(\lambda \nu m)$ 时间内完成，存储 $O(m/k)$ 个证明。更新所有证明需 $O(\nu)$ 时间。**单变量情况**（推广[28]）：利用Lagrange基和递归分拆，将向量划分为 $2^{\nu+1}$ 块，每块大小 $2^\kappa$，构建二进制树。打开证明包含从根到叶子的路径证明及叶子内积证明，大小 $\nu+5$ 个群元素。预计算和更新的开销类似。该方案的一个优点是可信设置只依赖于 $m$，而 $\nu,\kappa$ 可在运行时选择。

### 核心公式与流程

**[单项式基内积打开验证方程]**
$$
e\left(\mathsf{C}_a, \mathsf{C}_b\right) - e\left(y[\tau^{m-1}]_1, [1]_2\right) = e([R]_1, [1]_2) + e([H]_1, [\tau^{m}]_2) \quad\land\quad e([R]_1, [\tau]_2) = e([\hat{R}]_1, [1]_2)
$$
> 作用：验证承诺 $\mathsf{C}_a$ 关于向量 $\mathbf{a}$ 的内积 $\mathbf{a}\cdot\mathbf{b}=y$。第一式保证多项式等式，第二式确保 $\deg R < m-1$。

**[Lagrange基内积打开核心方程]**
$$
a(X)b(X) - m^{-1}y = X R(X) + t(X) H(X)
$$
其中 $t(X)=\prod_{i=1}^m (X-\mathsf{h}_i)$ 为群 $\mathbb{H}$ 的消逝多项式。验证方程类似单项式基，但使用 $\mathsf{C}_b$ 在 $\mathbb{G}_2$ 中的Lagrange基承诺。
> 作用：定义内积打开的代数条件，利用Lagrange基的正交性质：$\lambda_i(0)=m^{-1}$。

**[无限聚合算法（同一承诺）]**
$$\pi^* = \pi + \gamma \pi', \quad \gamma = \mathsf{H}(\mathsf{C}, T_{f,\mathbf{y}}, T_{f',\mathbf{y}'})$$
验证时重建组合函数 $f^* = \sum_i \delta_i f_i$ 和输出 $y^* = \sum_i \delta_i \mathbf{y}_i$，其中 $\delta_i$ 由聚合树结构计算。
> 作用：将两个证明聚合为一个，支持无限递归聚合。

**[可维护树（多变量）的根承诺多项式]**
$$p(\mathbf{X}, \mathbf{R}) = (\lambda(\mathbf{X}) \otimes \mathbf{R}) \cdot \mathbf{v}$$
其中 $\lambda(\mathbf{X})$ 为张量积Lagrange基，$\mathbf{R}$ 为叶子承诺密钥，$\mathbf{v}$ 为整个向量。
> 作用：将整个向量的承诺表示为多变量多项式的求值，内部节点通过多项式除法递归打开。

### 实验结果

论文未提供实物实验数据，但给出了两个比较表格（Table 1 和 Table 2）。Table 1 对比了不同可聚合子向量承诺（针对无状态加密货币和空间证明）的性质：本文的Lagrange和单项式LVC均支持无限聚合和跨承诺聚合，证明大小为 $O(1)$，验证时间为 $O(1)$，承诺更新为 $O(1)$。对比方案中，PoS aggSVC [7] 仅支持增量聚合且需要提示更新；Pointproofs [15] 仅支持一跳聚合；Stateless aggSVC [27] 也仅支持一跳聚合。本文方案在功能打开上支持线性映射（LVC）而非仅子向量（SVC），并且对特殊子集（如算术级数）的打开验证可达到 $O(1)$ 而非 $O(n)$。

Table 2 对比了可维护向量承诺的渐进性能，考虑向量维度 $m = k \cdot m'$，其中 $m'$ 为存储的证明数量。Merkle树透明设置，证明大小 $\log m$，单次打开 $O(k)$，更新所有证明 $O(k + \log m')$。Hyperproofs [26] 使用二进制树，证明大小 $\log m$，打开 $O(k)$，预计算 $O(m \log m')$，更新所有证明 $O(\log m')$。本文的多变量构造将证明大小压缩到 $\log_\ell m'$（$\ell$ 为常数），单变量构造证明大小为 $\log m'$，且单变量构造的设置是“可重用”的（即可用已有的Powers of Tau）。所有维护方案均支持通过内积配对证明（IPP）实现聚合。

### 局限性与开放问题

本文的方案大多依赖双线性配对和代数群模型（AGM）下的可证明安全性，这比标准模型弱。另外，可维护方案的预计算开销虽然准线性，但在实际部署中仍可能较大，特别是对海量向量（数百万规模）。跨承诺聚合的验证者需做线性于承诺个数的配对，实际效率可能不如期望。未来可探索如何在标准模型下实现类似功能，或进一步降低验证计算量。此外，单变量可维护构造的叶子内积打开使用了与整体结构相同的Lagrange基，其安全证明依赖于特定的BSDH假设，是否存在更弱的假设值得研究。

### 强关联论文

[4] Boneh et al. Batching techniques for accumulators with applications to IOPs and stateless blockchains. **CRYPTO 2019** [Google Scholar](https://scholar.google.com/scholar?q=Batching+techniques+for+accumulators+with+applications+to+IOPs+and+stateless+blockchains)

[7] Campanelli et al. Incrementally Aggregatable Vector Commitments and Applications to Verifiable Decentralized Storage. **ASIACRYPT 2020** [Google Scholar](https://scholar.google.com/scholar?q=Incrementally+Aggregatable+Vector+Commitments+and+Applications+to+Verifiable+Decentralized+Storage)

[15] Gorbunov et al. Pointproofs: aggregating proofs for multiple vector commitments. **ACM CCS 2020** [Google Scholar](https://scholar.google.com/scholar?q=Pointproofs+aggregating+proofs+for+multiple+vector+commitments)

[19] Kate et al. Constant-size commitments to polynomials and their applications. **ASIACRYPT 2010** [Google Scholar](https://scholar.google.com/scholar?q=Constant-size+commitments+to+polynomials+and+their+applications)

[20] Lai et al. Subvector Commitments with Application to Succinct Arguments. **CRYPTO 2019** [Google Scholar](https://scholar.google.com/scholar?q=Subvector+Commitments+with+Application+to+Succinct+Arguments)

[21] Libert et al. Functional commitment schemes: from polynomial commitments to pairing-based accumulators from simple assumptions. **ICALP 2016** [Google Scholar](https://scholar.google.com/scholar?q=Functional+commitment+schemes+from+polynomial+commitments+to+pairing-based+accumulators+from+simple+assumptions)

[26] Srinivasan et al. Hyperproofs: aggregating and maintaining proofs in vector commitments. **USENIX Security 2022** [Google Scholar](https://scholar.google.com/scholar?q=Hyperproofs+aggregating+and+maintaining+proofs+in+vector+commitments)

[27] Tomescu et al. Aggregatable subvector commitments for stateless cryptocurrencies. **SCN 2020** [Google Scholar](https://scholar.google.com/scholar?q=Aggregatable+subvector+commitments+for+stateless+cryptocurrencies)


## 关键词

+ 向量承诺
+ 线性映射
+ 零知识证明
+ 区块链可扩展性
+ 多项式承诺