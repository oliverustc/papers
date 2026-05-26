---
title: "Matproofs: Maintainable matrix commitment with efficient aggregation"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2022
---

## Matproofs: Maintainable matrix commitment with efficient aggregation

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3548606.3560591)

## 作者

+ Jing Liu 
+ Liang Feng Zhang 


## 笔记

### 背景与动机
无状态加密货币通过让区块提议者和验证者仅需存储一个账户余额向量的承诺来大幅降低存储开销 [6, 14, 15]。在基于向量承诺的方案中，面向最佳系统性能存在四个关键性质：承诺和证据均为常数的简洁性、支持多个证据高效聚合的聚合性、仅需变动和公共参数即可更新的易更新性、以及能在亚线性时间内完成所有证据更新的可维护性 [38]。然而现有方案无一步能满足全部四项性质：Edrax [15] 不简洁也不可聚合；Merkle树 [29] 和 Verkle 树 [24] 的证明大小与向量长度相关且不易更新；早期的代数型方案 [14, 25] 不支持聚合也不可维护；Boneh 等的方案 [6] 和第1个 VC 方案 [13] 不易更新；Pointproofs [18] 具有最有效的聚合和验证但不支持亚线性时间维护；Hyperproofs [38] 是唯一兼具聚合性和可维护性的方案，但其证明大小与向量长度成对数关系且不简洁。因此构建一个同时具备这四个性质的向量承诺方案是该领域尚未填补的空白。

### 相关工作

[14] Catalano and Fiore. Vector commitments and their applications. **PKC 2013** [Google Scholar](https://scholar.google.com/scholar?q=Vector+commitments+and+their+applications)
> 核心思路：提出了基于双线性群的常大小承诺和证明的代数向量承诺方案。
> 局限与区别：不支持证据聚合，更新所有证据需要 O(n) 时间，不具备可维护性。

[18] Gorbunov et al. Pointproofs: Aggregating proofs for multiple vector commitments. **CCS 2020** [Google Scholar](https://scholar.google.com/scholar?q=Pointproofs:+Aggregating+proofs+for+multiple+vector+commitments)
> 核心思路：支持同承诺内聚合和跨承诺聚合，承诺和聚合后证明均为常数大小。
> 局限与区别：不具备可维护性，更新所有证据仍需 O(n) 时间。

[38] Srinivasan et al. Hyperproofs: Aggregating and maintaining proofs in vector commitments. **USENIX Security 2022** [Google Scholar](https://scholar.google.com/scholar?q=Hyperproofs:+Aggregating+and+maintaining+proofs+in+vector+commitments)
> 核心思路：基于多项式承诺和内部对积论证实现对数大小的证据及亚线性时间维护。
> 局限与区别：证明大小与向量长度成对数关系，不简洁；聚合和验证效率低于本文方案。

[15] Chepurnoy et al. Edrax: A cryptocurrency with stateless transaction validation. **ePrint 2018** [Google Scholar](https://scholar.google.com/scholar?q=Edrax:+A+cryptocurrency+with+stateless+transaction+validation)
> 核心思路：基于多变量多项式承诺构造可更新的向量承诺用于无状态加密货币。
> 局限与区别：证据大小与向量长度成对数关系，不支持聚合，更新证据需 O(n log n) 时间。

[29] Merkle. A digital signature based on a conventional encryption function. **CRYPTO 1987** [Google Scholar](https://scholar.google.com/scholar?q=A+digital+signature+based+on+a+conventional+encryption+function)
> 核心思路：哈希树用作向量承诺，证据为栈的路径节点。
> 局限与区别：证明大小随向量长度对数增长，更新需要涉及对手方信息而不易更新。

[22] Kate et al. Constant-size commitments to polynomials and their applications. **ASIACRYPT 2010** [Google Scholar](https://scholar.google.com/scholar?q=Constant-size+commitments+to+polynomials+and+their+applications)
> 核心思路：提出多项式承诺 KZG 方案，被用作 [41] 和基于 Verkle 树等方案的底层构造。
> 局限与区别：需要可信设置生成线性大小的公共参数；本身不支持证据聚合。

[41] Tomescu et al. Aggregatable subvector commitments for stateless cryptocurrencies. **SCN 2020** [Google Scholar](https://scholar.google.com/scholar?q=Aggregatable+subvector+commitments+for+stateless+cryptocurrencies)
> 核心思路：基于 KZG 多项式承诺构造可聚合子向量承诺，承诺和证明均为常数大小。
> 局限与区别：更新所有证据仍需 O(n) 时间，不具备可维护性。

[6] Boneh et al. Batching techniques for accumulators with applications to IOPs and stateless blockchains. **CRYPTO 2019** [Google Scholar](https://scholar.google.com/scholar?q=Batching+techniques+for+accumulators+with+applications+to+IOPs+and+stateless+blockchains)
> 核心思路：通过比特承诺构造常数大小承诺和常大小聚合证明。
> 局限与区别：更新承诺和证明需要同时知晓新旧值，不易更新且不可维护。

[24] Kuszmaul. Verkle trees. **ePrint 2019** [Google Scholar](https://scholar.google.com/scholar?q=Verkle+trees)
> 核心思路：结合 KZG 多项式承诺的 k 叉树结构减小 O(log_k n) 大小的证明。
> 局限与区别：证明大小仍然依赖向量长度，聚合性差，更新需对方信息。

### 核心技术与方案

本文提出矩阵承诺模型 Matproofs，将向量以 $\sqrt{n} \times \sqrt{n}$ 矩阵形式编排，目的是同时实现简洁性、可聚合性、易更新性和可维护性。系统分为七个算法：Setup、Commit、Prove、UpdCommit、UpdProof、AggProof 和 Verify。

整体构造思路是将矩阵 M 的条目视为双变量多项式 $f(X,Y) = \mathbf{Y}^\top \mathbf{M} \mathbf{X}$ 的系数，其中列向量 $\mathbf{Y} = (Y,\ldots,Y^{n_1})$ 和行向量 $\mathbf{X} = (X,\ldots,X^{n_2})$。承诺 C 设为 $C = g_1^{f(\alpha, \beta)}$，即在随机点 $(\alpha,\beta)$ 的求值结果。每个位置的证明采用双层结构：第一层是每行的局部承诺 $\mathbf{c}_i = g_1^{\mathbf{M}_i \boldsymbol{\alpha}}$ 和对应的全局证明 $\omega_i$，第二层是具体位置的局部证明 $\Omega_{ij} = g_1^{\alpha^{n_2+1-j} \mathbf{M}_i[-j] \boldsymbol{\alpha}[-j]}$。关键设计在于 $\omega_i$ 只依赖于除第 $i$ 行外的行向量，$\Omega_{ij}$ 只依赖于该行除第 $j$ 列外的元素。当更新第 $(i,j)$ 个条目时，只需更新：第 $i$ 行的局部承诺 $\mathbf{c}_i$、所有其他行的全局证明 $\{\omega_k\}_{k \neq i}$ 和同一行其他列的局部证明 $\{\Omega_{i\ell}\}_{\ell \neq j}$，共计 $n_1 + n_2 - 1 = O(\sqrt{n})$ 次 $\mathbb{G}_1$ 指数运算。

证明的聚合采用坐标轴聚合策略：全局证明部分 $\hat{\omega} = \prod_{i \in \overline{S}} \omega_i^{r_i}$，局部证明部分先对每个被覆盖行聚合为 $\hat{\Omega}_i = \prod_{j \in \widetilde{S}_i} \Omega_{ij}^{h_{ij}}$，再跨行聚合为 $\hat{\Omega} = \prod_{i \in \overline{S}} \hat{\Omega}_i^{t_i}$。最终的聚合证明为 $\hat{\mathcal{P}} = ( \{\mathbf{c}_i\}_{i \in \overline{S}}, \hat{\omega}, \hat{\Omega} )$。

安全性证明基于两个假设：$n_2$-wBDHE* 和 $(n_1,n_2)$-bBDHE，在 AGM+ROM 模型中证明位置绑定性。证明策略将攻击者输出分为两类：若对手在存在交集的行上输出相同的局部承诺 $\mathbf{c}_i$ 但不同的求值，则归约到 Pointproofs 的安全性；若输出不同的局部承诺，则归约到新提出的 $(n_1,n_2)$-bBDHE 问题。在 AGM 下提取代数系数后，利用随机预言机下哈希值的随机性控制敌手成功的概率。

复杂度方面：承诺计算需 $n$ 次 $\mathbb{G}_1$ 指数运算；生成所有证据的时间为 $O(n \log n)$；单人证据更新仅需 2 次指数运算；全部证据更新需 $O(\sqrt{n})$ 次指数运算；聚合 $b$ 个证据在最坏情况下需 $(2\min\{b,\sqrt{n}\} + b)$ 次指数运算；验证单证据需 2 次 $\mathbb{G}_1$ 指数和 5 次配对；验证聚合证据在最坏情况下需 $(\min\{b,\sqrt{n}\}+1)$ 次 $\mathbb{G}_1$ 指数、$(b + \min\{b,\sqrt{n}\})$ 次 $\mathbb{G}_2$ 指数和 $(2\min\{b,\sqrt{n}\}+3)$ 次配对。

### 核心公式与流程

**[承诺生成]**
$$
C = g_1^{\boldsymbol{\beta}^\top \mathbf{M} \boldsymbol{\alpha}}
$$
> 作用：将 $n_1 \times n_2$ 矩阵 M 映射为双线性群 $\mathbb{G}_1$ 的一个常量元素，作为对整个矩阵的绑定承诺。

**[单证据验证第一方程]**
$$
e(C, g_2^{\beta^{n_1+1-i}}) = e(\omega_i, g_2) \cdot e(\mathbf{c}_i, g_2^{\beta^{n_1+1}})
$$
> 作用：检验局部承诺 $\mathbf{c}_i$ 与全局承诺 C 的一致性，其中 $\omega_i$ 是全局证明。

**[单证据验证第二方程]**
$$
e(\mathbf{c}_i, g_2^{\alpha^{n_2+1-j}}) = e(\Omega_{ij}, g_2) \cdot g_T^{\alpha^{n_2+1} \mathbf{M}_{ij}}
$$
> 作用：检验具体值 $\mathbf{M}_{ij}$ 与局部承诺 $\mathbf{c}_i$ 的一致性，其中 $\Omega_{ij}$ 是局部证明。

**[克周期更新局部证明]**
$$
\Omega_{k\ell}' = \Omega_{k\ell} \cdot g_1^{\delta \alpha^{n_2+1-\ell+j}}
$$
> 作用：当 $(i,j)$ 位置值更新 $\delta$ 时，同一行 $k=i$ 且不同列 $\ell \neq j$ 的局部证明以一次单指数运算完成更新。

**[聚合全局证明]**
$$
\hat{\omega} = \prod_{i \in \overline{S}} \omega_i^{r_i}, \quad r_i = H(i,C,\overline{S},\{\mathbf{c}_k\}_{k \in \overline{S}})
$$
> 作用：借助随机预言机将行内多个全局证明聚合成单个 $\hat{\omega}$，只增加计算量而不增加通信大小。

**[聚合局部证明]**
$$
\hat{\Omega}_i = \prod_{j \in \widetilde{S}_i} \Omega_{ij}^{h_{ij}}, \quad \hat{\Omega} = \prod_{i \in \overline{S}} \hat{\Omega}_i^{t_i}
$$
> 作用：先对行内局部证明用哈希加权聚合，再跨行加权聚合，使聚合证明大小与被覆盖的行数 $|\overline{S}|$ 成正比。

### 实验结果

实验基于 Golang 和 mcl 库，使用 BLS12-381 曲线，硬件为 Intel Xeon E-2286G CPU @ 4.0GHz（单线程运行）。对于 $n_1 = n_2 = 2^{11}$（约 400 万账户）且聚合 $b=1024$ 个证据的设定，单个个体证明大小为 0.14 KiB，而 Hyperproofs 为 1.03 KiB；聚合证明大小在最好情况（仅覆盖 1 行）为 0.14 KiB，最坏情况（覆盖 1024 行）为 48.09 KiB，Hyperproofs 则为 50.63 KiB。聚合时间方面，Matproofs 最好为 0.03 秒，最坏为 0.07 秒，而 Hyperproofs 约为 53.51 秒；聚合证明验证时间 Matproofs 最好为 0.08 秒，最坏为 0.57 秒，Hyperproofs 约为 6.30 秒。更新全部证据时，Matproofs 需 0.24 秒（$n=2^{22}$），Hyperproofs 只需 1.32 毫秒，但 Pointproofs 需约 242.59 秒。宏基准测试中，在 $n=2^{26}$、1024 笔交易的设定下，Matproofs 的区块提议为 2.31~2.35 秒，区块验证为 0.24~0.73 秒，比 Hyperproofs 分别快 26 倍和 10 倍，而证据维护（PSN 更新）虽慢 600 倍，但比 Pointproofs 快 4226 倍。若用 16 线程并行化 PSN 工作，总开销（P + hV + M/16）为 145.10 秒，优于 Hyperproofs 的 255.75 秒和 Pointproofs 的 523,030 秒。

### 局限性与开放问题
Matproofs 的公共参数是线性大小的（$2n + \sqrt{n}$ 个 $\mathbb{G}_1$ 元素），需要可信初始设置（可通过多方安全计算协议实现 [10]），当 $n$ 增长到数十亿量级时，密钥生成和分发成本将变得显著。最坏情况下聚合证明大小与被覆盖的行数成正比，当被覆盖行数接近 $\sqrt{n}$ 时，聚合证明为 $O(\sqrt{n})$ 大小而非常数。更新全部证据的时间为 $O(\sqrt{n})$，相比 Hyperproofs 的 $O(\log n)$ 慢两个数量级，在极端高频更新的场景下 PSN 负担较重。未来方向包括：研究更高效的局部聚合策略以减少最坏情况下的证明大小，探索在标准模型而非 AGM+ROM 模型下实现位置绑定的可能性，及设计具有更优更新复杂度的矩阵承诺方案。

### 强关联论文

[14] Catalano and Fiore. Vector commitments and their applications. **PKC 2013** [Google Scholar](https://scholar.google.com/scholar?q=Vector+commitments+and+their+applications)

[18] Gorbunov et al. Pointproofs: Aggregating proofs for multiple vector commitments. **CCS 2020** [Google Scholar](https://scholar.google.com/scholar?q=Pointproofs:+Aggregating+proofs+for+multiple+vector+commitments)

[38] Srinivasan et al. Hyperproofs: Aggregating and maintaining proofs in vector commitments. **USENIX Security 2022** [Google Scholar](https://scholar.google.com/scholar?q=Hyperproofs:+Aggregating+and+maintaining+proofs+in+vector+commitments)

[15] Chepurnoy et al. Edrax: A cryptocurrency with stateless transaction validation. **ePrint 2018** [Google Scholar](https://scholar.google.com/scholar?q=Edrax:+A+cryptocurrency+with+stateless+transaction+validation)

[29] Merkle. A digital signature based on a conventional encryption function. **CRYPTO 1987** [Google Scholar](https://scholar.google.com/scholar?q=A+digital+signature+based+on+a+conventional+encryption+function)

[22] Kate et al. Constant-size commitments to polynomials and their applications. **ASIACRYPT 2010** [Google Scholar](https://scholar.google.com/scholar?q=Constant-size+commitments+to+polynomials+and+their+applications)

[41] Tomescu et al. Aggregatable subvector commitments for stateless cryptocurrencies. **SCN 2020** [Google Scholar](https://scholar.google.com/scholar?q=Aggregatable+subvector+commitments+for+stateless+cryptocurrencies)

[6] Boneh et al. Batching techniques for accumulators with applications to IOPs and stateless blockchains. **CRYPTO 2019** [Google Scholar](https://scholar.google.com/scholar?q=Batching+techniques+for+accumulators+with+applications+to+IOPs+and+stateless+blockchains)

[24] Kuszmaul. Verkle trees. **ePrint 2019** [Google Scholar](https://scholar.google.com/scholar?q=Verkle+trees)

[13] Campanelli et al. Incrementally aggregatable vector commitments and applications to verifiable decentralized storage. **ASIACRYPT 2020** [Google Scholar](https://scholar.google.com/scholar?q=Incrementally+aggregatable+vector+commitments+and+applications+to+verifiable+decentralized+storage)


## 关键词

+ 矩阵承诺
+ 向量承诺
+ 简洁性
+ 无状态加密货币
+ 证明聚合