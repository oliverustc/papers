---
title: "Batching, aggregation, and zero-knowledge proofs in bilinear accumulators"
doi: 10.1145/3548606.3560676
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2022
modified: 2025-04-16 10:12:26
created: 2025-04-13 16:52:12
---
## Batching, aggregation, and zero-knowledge proofs in bilinear accumulators

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3548606.3560676)

## 作者

+ Shravan Srinivasan 
+ [Ioanna Karantaidou](Ioanna%20Karantaidou.md)
+ [Foteini Baldimtsi](Foteini%20Baldimtsi.md)
+ [Charalampos Papamanthou](Charalampos%20Papamanthou.md) 

## 笔记

### 背景与动机
累加器是一种密码学原语，允许证明者简洁地对一个集合做出承诺，并为单个元素的（非）成员关系生成简短证明。然而，在区块链和匿名凭证等新兴应用中，证明者需要同时批处理证明多个元素的（非）成员关系。若为每个元素单独提供证明，将导致巨大的带宽开销和验证者计算负担。因此，构建大小为常数的批量证明至关重要。目前，RSA累加器已实现了高效的批处理、聚合与零知识方案，但其存在两个关键瓶颈：(1) RSA群元素尺寸较大（如256字节），导致证明尺寸和验证成本较高；(2) 其仅支持素数的累积，因此必须先将任意域的输入通过哈希到素数（Hash-to-Prime）映射到素数域，该过程计算开销大且使得零知识证明中需要包含素性证明，复杂度急剧增加。相比之下，双线性对（BP）累加器支持任意域元素的累积，且具有更小的证明（如48字节）和更快的指数运算，但其在无陷门的分布式环境下，尚缺乏高效的批量（非）成员证明聚合、以及紧凑的零知识批量（非）成员证明方案。本文旨在填补这一空白，为BP累加器提出一套完整的批处理、聚合与零知识协议。

### 相关工作

[8] Josh Benaloh et al. One-Way Accumulators: A Decentralized Alternative to Digital Signatures. **EUROCRYPT 1993** [Google Scholar](https://scholar.google.com/scholar?q=One-Way+Accumulators%3A+A+Decentralized+Alternative+to+Digital+Signatures)
> 核心思路：提出了基于RSA的累加器原语，通过模指数运算实现集合的简洁承诺。
> 局限与区别：仅支持单元素证明，且基于陷门的更新方式，不适用于无陷门分布式场景，证明尺寸大。

[10] Dan Boneh et al. Batching Techniques for Accumulators with Applications to IOPs and Stateless Blockchains. **CRYPTO 2019** [Google Scholar](https://scholar.google.com/scholar?q=Batching+Techniques+for+Accumulators+with+Applications+to+IOPs+and+Stateless+Blockchains)
> 核心思路：为RSA累加器定义了批量证明，并提出了成员与非成员证明的聚合算法，证明尺寸为常数。
> 局限与区别：其方案基于素数域，需要耗时的Hash-to-Prime映射。本文则为BP累加器设计聚合方案，避免了该映射，从而获得更小的证明和更快的验证。

[16] Jan Camenisch et al. Dynamic Accumulators and Application to Efficient Revocation of Anonymous Credentials. **CRYPTO 2002** [Google Scholar](https://scholar.google.com/scholar?q=Dynamic+Accumulators+and+Application+to+Efficient+Revocation+of+Anonymous+Credentials)
> 核心思路：提出了首个动态累加器，支持在陷门下高效地添加和删除元素。
> 局限与区别：该方案依赖陷门进行删除操作，不满足无陷门要求。本文所有协议均在无陷门（或陷门销毁后）的分布式环境中运行。

[38] Lan Nguyen. Accumulators from Bilinear Pairings and Applications. **CT-RSA 2005** [Google Scholar](https://scholar.google.com/scholar?q=Accumulators+from+Bilinear+Pairings+and+Applications)
> 核心思路：提出了首个基于双线性映射的累加器，在q-SDH假设下安全。
> 局限与区别：该工作仅定义了单元素证明，未涉及批量、聚合或零知识方案。本文在此基础上构建了完整的批量、聚合和零知识协议。

[39] Alex Ozdemir et al. Scaling Verifiable Computation Using Efficient Set Accumulators. **USENIX Security 2020** [Google Scholar](https://scholar.google.com/scholar?q=Scaling+Verifiable+Computation+Using+Efficient+Set+Accumulators)
> 核心思路：提出了在RSA设置下，通过SNARK友好技术批量证明（非）成员关系的方案。
> 局限与区别：该方法依赖通用SNARKs来证明哈希到素数和素性测试等非代数关系，导致证明者开销极大。本文方案直接利用BP累加器的代数结构，无需此类SNARKs，速度是其16到42倍。

[18] Matteo Campanelli et al. Succinct Zero-Knowledge Batch Proofs for Set Accumulators. **Cryptology ePrint Archive 2021** [Google Scholar](https://scholar.google.com/scholar?q=Succinct+Zero-Knowledge+Batch+Proofs+for+Set+Accumulators)
> 核心思路：采用“混合”方法，在RSA设置下，用非SNARK方式证明批量成员关系，并用SNARK证明元素属于素数域。
> 局限与区别：该方法不支持同时证明非成员关系。本文方案在BP设置下，无需SNARK即可同时支持成员和非成员的零知识批量证明，且效率更高。

### 核心技术与方案

本文方案围绕Nguyen提出的BP累加器[38]展开。该累加器将集合 $X = \{x_1, \ldots, x_n\}$ 的摘要定义为 $A_X = g_1^{\prod_{x \in X}(s + x)}$，其中 $s \in \mathbb{Z}_p^*$ 是setup阶段生成的陷门（销毁后丢弃），$g_1$ 是群 $\mathbb{G}_1$ 的生成元。单元素成员证明为 $\pi_y = g_1^{\prod_{x \in X \setminus \{y\}}(s + x)}$，验证等式 $e(\pi_y, g_2^{s+y}) = e(A_X, g_2)$ 成立。非成员证明利用 $\gcd(\prod_{x \in X}(s + x), (s+y)) = 1$，通过扩展欧几里得算法找到系数 $\alpha \in \mathbb{Z}_p$ 和多项式 $\beta(s)$ 使得 $\alpha \cdot X(s) + \beta(s) \cdot (s + y) = 1$，证明形式为 $\bar{\pi}_y = (\alpha, g_1^{\beta(s)})$，验证等式 $e(A_X, g_2^\alpha) \cdot e(g_1^{\beta(s)}, g_2^{s+y}) = e(g_1, g_2)$。

**批处理**：本文直接将其推广到批量证明。对于子集 $I$，成员批量证明为 $\pi_I = g_1^{\prod_{x \in X \setminus I}(s + x)}$，验证时利用多项式 $I(s) = \prod_{y_i \in I}(s + y_i)$ 检查 $e(\pi_I, g_2^{I(s)}) = e(A_X, g_2)$。非成员批量证明 $\bar{\pi}_I = (g_2^{\alpha(s)}, g_1^{\beta(s)})$ 满足 $\alpha(s) \cdot X(s) + \beta(s) \cdot I(s) = 1$，其中 $\deg(\alpha) \leq |I|-1, \deg(\beta) \leq |X|-1$。这些批量证明的大小均为常数（成员证明1个 $\mathbb{G}_1$ 元素，非成员证明1个 $\mathbb{G}_1$ 和1个 $\mathbb{G}_2$ 元素）。方案在代数群模型（AGM）下，基于Uber假设证明强可靠性（允许对手任意选择摘要 $A_X$）。

**聚合**：成员证明的聚合利用部分分式分解（PFD）。给定个 $|I|$ 体证明 $\pi_i = g_1^{X_i(s)}$，其中 $X_i(s) = \prod_{x \in X \setminus \{x_i\}}(s + x)$，聚合得到 $\pi_I$ 的计算为 $\pi_I = \prod_{x_i \in I} \pi_i^{c_i}$，其中系数 $c_i = 1 / I'(-x_i)$，$I'$ 是 $I(s)$ 的导数，可在 $O(|I|\log^2|I|)$ 的域运算和一次 $|I|$ 规模的多指数运算中完成。非成员证明的聚合基于广义Bézout引理。通过求解 $\sum_{i=1}^{|I|} c_i(s) \cdot Y_i(s) = 1$（其中 $Y_i(s) = I(s)/(s+y_i)$），且由引理5.1知 $c_i$ 为常数，可将多个个体非成员证明线性组合成批量证明，但时间开销为 $O(|I|^2 \log |I|)$ 域运算。

**非成员证明更新**：本文提出了一种高效的更新算法，用于集合 $X$ 添加或删除单个元素 $z$ 时更新非成员证明。通过Bézout引理，对于 $y \neq z$，找到常数 $u, v$ 满足 $u(s+z) + v(s+y) = 1$。更新后的证明 $\bar{\pi}'_y = (\alpha', g_1^{\beta'(s)})$ 可通过 $O(1)$ 的域运算和群运算从旧证明中得到，具体地，添加时 $\alpha' = u\alpha$，$\beta'(s) = v\alpha X(s) + \beta(s)$，对应群运算 $g_1^{\beta'(s)} = (A_X^{v})^\alpha \cdot g_1^{\beta(s)}$。删除时计算类似。

**零知识批量证明**：本文设计了一套基于Schnorr类协议的零知识方案，用于隐藏批量证明中的集合 $I$。协议由三部分组成：(1) 证明者首先对多项式 $I(s)$ 的系数进行Pedersen向量承诺 $C_I = h_2^r g_2^{I(s)}$。(2) 对于成员关系 $\mathcal{R}_{\text{mem}}$，证明者将真实证明 $\pi_I$ 用随机掩码 $\tau_1, \tau_2$ 盲化为 $\pi_{I,1}, \pi_{I,2}$，然后通过交互协议证明配对验证等式 $e(\pi_I, g_2^{I(s)}) = e(A_X, g_2)$ 成立，同时保持$\pi_I$ 和 $r$ 的零知识。(3) 若要揭示子集大小 $d$（证明 $|I| \geq d$），使用 $\mathcal{R}_{\text{degcheck}}$ 协议，证明者对 $f(s) = I(s) - s^d$ 进行承诺 $C_f$，通过与挑战 $c$ 的乘法（将 $f(s)$ 的度数“偏移”到最大参数 $t$），利用q-型知识假设（q-PKE）证明$f(s)$的度数$\leq d-1$。整个ZK方案中，$\mathcal{R}_{\text{mem}}$ 和 $\mathcal{R}_{\text{nonmem}}$ 的证明规模与验证成本均为常数，证明者计算成本为 $O(|I|)$。$\mathcal{R}_{\text{degcheck}}$ 的证明者成本为 $O(t)$，但验证成本为常数（7个配对）。

**PoE指数证明**：为加速批量验证中的大指数运算 $A_U^{V(s)}$，本文设计了一个新的PoE协议（图1）。其核心思想是：验证者发送随机挑战 $\ell$，证明者计算多项式 $V(x)$ 除以 $(x+\ell)$ 的商 $q(x)$ 和余数 $r$，并返回 $Q_1 = g^{q(s)}$ 和 $Q_2 = g^{q(s)(s+\ell)}$。验证者通过检查 $e(Q_1, g^{s+\ell}) = e(Q_2, g)$ 和 $e(A_U, Q_2) \cdot e(A_U, g^r) = e(A_W, g)$ 来确认 $A_W = A_U^{V(s)}$，从而将指数运算量从 $O(\deg(V))$ 降低到常数个配对，多项式除法仅需 $O(\deg(V))$ 的域运算。

### 核心公式与流程

**[BP累加器摘要与单元素成员证明]**
$$A_X = g_1^{\prod_{x \in X}(s + x)} \quad \pi_y = g_1^{\prod_{x \in X \setminus \{y\}}(s + x)}$$
$$e(\pi_y, g_2^{s+y}) = e(A_X, g_2)$$
> 作用：定义BP累加器的核心结构，以及单元素成员的验证等式。

**[单元素非成员证明]**
$$\alpha \cdot X(s) + \beta(s) \cdot (s + y) = 1, \quad \bar{\pi}_y = (\alpha, g_1^{\beta(s)})$$
$$e(A_X, g_2^\alpha) \cdot e(g_1^{\beta(s)}, g_2^{s+y}) = e(g_1, g_2)$$
> 作用：基于多项式Bézout恒等式构建非成员证明及其验证等式。

**[批量成员证明与验证]**
$$\pi_I = g_1^{\prod_{x \in X \setminus I}(s + x)}, \quad I(s) = \prod_{y_i \in I}(s + y_i)$$
$$e(\pi_I, g_2^{I(s)}) = e(A_X, g_2)$$
> 作用：将成员证明泛化到批量场景，验证者需计算多项式 $I(s)$。

**[批量非成员证明与验证]**
$$\alpha(s) \cdot X(s) + \beta(s) \cdot I(s) = 1, \quad \bar{\pi}_I = (g_2^{\alpha(s)}, g_1^{\beta(s)})$$
$$e(A_X, g_2^{\alpha(s)}) \cdot e(g_1^{\beta(s)}, g_2^{I(s)}) = e(g_1, g_2)$$
> 作用：将非成员证明泛化到批量场景，$\alpha(s), \beta(s)$ 为Bézout系数多项式。

**[成员证明的PFD聚合]**
$$\frac{1}{I(s)} = \sum_{x_i \in I} \frac{1}{I'(-x_i)(s + x_i)} \Rightarrow \pi_I = \prod_{x_i \in I} \pi_i^{1/I'(-x_i)}$$
> 作用：展示如何利用部分分式分解将多个个体成员证明 $\pi_i$ 线性组合为单个批量证明 $\pi_I$。

**[非成员证明的Bézout聚合]**
$$\sum_{i=1}^{|I|} c_i \cdot Y_i(s) = 1, \quad Y_i(s) = \frac{I(s)}{(s+y_i)}$$
$$\alpha(s) = \sum_{i=1}^{|I|} \alpha_i c_i Y_i(s) \quad \beta(s) = \sum_{i=1}^{|I|} c_i \beta_i(s)$$
> 作用：展示如何通过Bézout系数 $c_i$（引理5.1证明其为常数）将多个个体非成员证明 $(\alpha_i, g_1^{\beta_i(s)})$ 聚合为批量证明。

**[非成员证明更新（添加元素z）]**
$$\alpha' = u\alpha, \quad \beta'(s) = v\alpha X(s) + \beta(s) \quad \text{其中} \quad u(s+z) + v(s+y) = 1$$
$$\bar{\pi}'_y = (u\alpha, g_1^{v\alpha X(s) + \beta(s)}) = (u\alpha, A_X^{v\alpha} \cdot g_1^{\beta(s)})$$
> 作用：展示添加元素时，更新非成员证明只需 $O(1)$ 次域运算和群运算，无需重新计算整个多项式。

**[PoE协议核心验证步骤]**
$$V(x) = q(x)(x + \ell) + r$$
$$e(Q_1, g^{s+\ell}) \stackrel{?}{=} e(Q_2, g) \quad \text{and} \quad e(A_U, Q_2) \cdot e(A_U, g^r) \stackrel{?}{=} e(A_W, g)$$
> 作用：PoE协议将验证 $A_W = A_U^{V(s)}$ 的指数运算开销降低为常数次配对和一次多项式除法。

### 实验结果

实验在一台Intel Core i7-4770 CPU @ 3.40GHz的单线程环境中进行。RSA累加器使用2048位模数，BP累加器使用BLS12-381曲线。对于最大累积集大小 $|X| = 2^{17}$，BP累加器的公共参数为18 MiB，而RSA仅为几个常数大小的元素。在域映射方面，将256位任意字符串映射到素数域平均需要640-894微秒，而BP累加器可直接累积256位整数，无需映射。对于大小为 $|I| = 2^{15}$ 的集合，BP累加器的提交耗时5.17秒，远优于RSA的12.56秒（减去映射成本后）。在成员聚合方面，对于 $|I| = 2^{13}$ 以下规模，BP的聚合时间（0.18分钟）优于RSA（0.8分钟）；对于 $2^{15}$ 规模，BP的聚合时间（2.51分钟）优于RSA（3.66分钟）；但对于 $2^{17}$ 规模，BP聚合（38.35分钟）劣于RSA（16.49分钟），这是因为BP的 $O(|I|\log^2|I|)$ 域运算开始占主导。在非成员聚合方面，RSA始终优于BP，因为BP的 $O(|I|^2\log |I|)$ 域运算在 $|I| \geq 2^{13}$ 时变得不可行。在验证性能上，无论是否启用PoE，BP的批处理成员和非成员验证均比RSA快4至11倍。在零知识设置下，基准测试表明，$\mathcal{R}_{\text{mem}}$ 的证明者耗时仅2.97毫秒，验证者耗时3.66毫秒；$\mathcal{R}_{\text{nonmem}}$ 的证明者耗时4.65毫秒，验证者耗时5.18毫秒。与最新的RSA方案HARiSA对比，对于批大小为16的成员证明，本方案仅需0.18秒，而HARiSA需要2.86秒，即16倍的加速。本方案的证明尺寸约为1 KiB，与HARiSA的1.14 KiB相当。

### 局限性与开放问题

BP累加器的一个主要局限是公共参数尺寸较大，达到 $O(|X|)$，且随最大累积集大小线性增长，在零知识设置中由于需要额外的q-PKE参数，尺寸再增长3倍。相比之下，RSA累加器的参数仅为常数大小。另一个限制是BP非成员证明的聚合算法具有 $O(|I|^2 \log |I|)$ 的渐近复杂度，使其在批处理规模较大时（如 $2^{15}$ 以上）效率低于RSA方案。此外，本文的零知识方案需要在Fiat-Shamir变换下进行分析，并正式证明其在随机谕言模型下的安全性。

### 强关联论文

[10] Dan Boneh et al. Batching Techniques for Accumulators with Applications to IOPs and Stateless Blockchains. **CRYPTO 2019** [Google Scholar](https://scholar.google.com/scholar?q=Batching+Techniques+for+Accumulators+with+Applications+to+IOPs+and+Stateless+Blockchains)

[38] Lan Nguyen. Accumulators from Bilinear Pairings and Applications. **CT-RSA 2005** [Google Scholar](https://scholar.google.com/scholar?q=Accumulators+from+Bilinear+Pairings+and+Applications)

[39] Alex Ozdemir et al. Scaling Verifiable Computation Using Efficient Set Accumulators. **USENIX Security 2020** [Google Scholar](https://scholar.google.com/scholar?q=Scaling+Verifiable+Computation+Using+Efficient+Set+Accumulators)

[18] Matteo Campanelli et al. Succinct Zero-Knowledge Batch Proofs for Set Accumulators. **Cryptology ePrint Archive 2021** [Google Scholar](https://scholar.google.com/scholar?q=Succinct+Zero-Knowledge+Batch+Proofs+for+Set+Accumulators)

[16] Jan Camenisch et al. Dynamic Accumulators and Application to Efficient Revocation of Anonymous Credentials. **CRYPTO 2002** [Google Scholar](https://scholar.google.com/scholar?q=Dynamic+Accumulators+and+Application+to+Efficient+Revocation+of+Anonymous+Credentials)

[47] Alin Tomescu et al. Aggregatable Subvector Commitments for Stateless Cryptocurrencies. **SCN 2020** [Google Scholar](https://scholar.google.com/scholar?q=Aggregatable+Subvector+Commitments+for+Stateless+Cryptocurrencies)

[8] Josh Benaloh et al. One-Way Accumulators: A Decentralized Alternative to Digital Signatures. **EUROCRYPT 1993** [Google Scholar](https://scholar.google.com/scholar?q=One-Way+Accumulators%3A+A+Decentralized+Alternative+to+Digital+Signatures)

[24] Ivan Damgård et al. Supporting Non-membership Proofs with Bilinear-map Accumulators. **Cryptology ePrint Archive 2008** [Google Scholar](https://scholar.google.com/scholar?q=Supporting+Non-membership+Proofs+with+Bilinear-map+Accumulators)


## 关键词

+ 双线性配对
+ 累加器
+ 零知识证明
+ 批量证明
+ 成员资格