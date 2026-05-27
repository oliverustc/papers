---
title: "Quadratic span programs and succinct NIZKs without PCPs"
doi: 10.1007/978-3-642-38348-9_37
标题简称:
论文类型: conference
会议简称: EUROCRYPT
发表年份: 2013
modified: 2025-04-08 16:40:45
---
## Quadratic span programs and succinct NIZKs without PCPs

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-642-38348-9_37)

## 作者

+ Rosario Gennaro
+ [Craig Gentry](Craig%20Gentry.md)
+ Bryan Parno
+ [Mariana Raykova](Mariana%20Raykova.md)
## 笔记

### 背景与动机
构造简洁的非交互式论证（SNARKs）一直是密码学与计算复杂性理论交叉领域的重要课题，其核心目标是让证明的通信量和验证时间远小于直接计算。经典的概率可检验证明（PCPs）虽然在理论上将NP证明压缩成可快速验证的形式，但将其转化为密码学方案时，证明者计算量往往巨大，且依赖随机构象模型或强假设。Kilian利用PCPs构造了交互式论证，Micali在随机构象模型中实现了非交互化，但随机构象本身存在可实例化缺陷。Groth提出了基于双线性群的简洁NIZK方案，证明了非交互论证可以在常数个群元素内完成，但其公共参考串（CRS）大小和证明者计算量均为电路规模的二次方，成为实用化瓶颈。本文试图填补一个空白：设计一种新的算术化方法，使得SNARK的CRS大小和证明者计算量同时达到准线性，且证明长度仅为常数个群元素，从而将PCP路线与Groth路线的优势结合起来。

### 相关工作

[27] Groth. Short Pairing-Based Non-Interactive Zero-Knowledge Arguments. **ASIACRYPT 2010** [Google Scholar](https://scholar.google.com/scholar?q=Short+Pairing-Based+Non-Interactive+Zero-Knowledge+Arguments)
> 核心思路：利用双线性群和知识指数假设，构造了证明长度为常数个群元素（42个）的NIZK参数。
> 局限与区别：CRS大小和证明者计算量为电路规模的二次方，而本文通过QSP将CRS和证明者计算降至准线性，证明长度缩减至7个群元素。

[30] Ishai, Kushilevitz, Ostrovsky. Efficient Arguments without Short PCPs. **IEEE Conference on Computational Complexity 2007** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+Arguments+without+Short+PCPs)
> 核心思路：通过调整PCP技术获得高效的简洁论证，证明了通信量与电路规模的次线性关系。
> 局限与区别：该方案中证明者计算（以及验证者在预处理中的计算）为电路规模的二次方，而本文的QSP直接构造实现了更优的渐进性能。

[7] Ben-Sasson et al. On the Concrete-Efficiency Threshold of Probabilistically-Checkable Proofs. **STOC 2013** [Google Scholar](https://scholar.google.com/scholar?q=On+the+Concrete-Efficiency+Threshold+of+Probabilistically-Checkable+Proofs)
> 核心思路：提出了一种具有准线性复杂性的证明者和CRS的PCP方案。
> 局限与区别：即使在该PCP转化为SNARK之前，本文的直接QSP构造已实现了更好的渐进性能。

[31] Karchmer, Wigderson. On Span Programs. **Structure in Complexity Theory Conference 1993** [Google Scholar](https://scholar.google.com/scholar?q=On+Span+Programs)
> 核心思路：提出了跨度程序（SP），一种基于线性代数的计算模型，用于刻画函数的复杂度。
> 局限与区别：SP只能有效计算NC²中的函数，而本文的QSP推广了SP，能够高效计算任意P中的函数。

[33] Lipmaa. Progression-Free Sets and Sublinear Pairing-Based Non-Interactive Zero-Knowledge Arguments. **TCC 2012** [Google Scholar](https://scholar.google.com/scholar?q=Progression-Free+Sets+and+Sublinear+Pairing-Based+Non-Interactive+Zero-Knowledge+Arguments)
> 核心思路：利用无进展集技术，将Groth方案中的CRS大小从二次方降至准线性。
> 局限与区别：证明者计算量仍为二次方，而本文同时实现了CRS和证明者计算的准线性。

[21] Gennaro, Gentry, Parno. Non-Interactive Verifiable Computing: Outsourcing Computation to Untrusted Workers. **CRYPTO 2010** [Google Scholar](https://scholar.google.com/scholar?q=Non-Interactive+Verifiable+Computing:+Outsourcing+Computation+to+Untrusted+Workers)
> 核心思路：提出了非交互可验证计算的概念和模型。
> 局限与区别：本文利用QSP实现了比该方案更高效的公开可验证计算方案。

[28] Groth, Ostrovsky, Sahai. New Techniques for Noninteractive Zero-Knowledge. **Journal of the ACM 2012** [Google Scholar](https://scholar.google.com/scholar?q=New+Techniques+for+Noninteractive+Zero-Knowledge)
> 核心思路：构造了具有多种优良性质的NIZK方案，但证明大小为线性。
> 局限与区别：证明长度随电路增大，而本文实现了常数的证明长度。

[29] Groth, Sahai. Efficient Non-Interactive Proof Systems for Bilinear Groups. **SIAM Journal on Computing 2012** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+Non-Interactive+Proof+Systems+for+Bilinear+Groups)
> 核心思路：在双线性群中构造了高效的非交互证明系统。
> 局限与区别：证明大小与电路线性相关。

[32] Kilian. A Note on Efficient Zero-Knowledge Proofs and Arguments (Extended Abstract). **STOC 1992** [Google Scholar](https://scholar.google.com/scholar?q=A+Note+on+Efficient+Zero-Knowledge+Proofs+and+Arguments)
> 核心思路：展示了如何使用PCP构造具有通信复杂性的交互式论证。
> 局限与区别：交互式且依赖PCP的构造，本文实现了非交互且无需PCP。

[36] Micali. Computationally Sound Proofs. **SIAM Journal on Computing 2000** [Google Scholar](https://scholar.google.com/scholar?q=Computationally+Sound+Proofs)
> 核心思路：在随机构象模型中，将交互式论证非交互化，得到了CS证明。
> 局限与区别：依赖随机构象模型，该模型已被证明不可实例化。

### 核心技术与方案

本文的核心技术贡献是提出了一种新的算术化方式——二次跨度程序（Quadratic Span Programs，QSPs）。QSP在概念上是传统跨度程序（SP）的自然推广：SP通过判断一个目标多项式能否表示为一些“属于”输入的多项式的线性组合来接受一个输入，而QSP通过判断一个除数多项式能否整除两个仿射线性组合的乘积来接受一个输入。正是这种乘积结构，使得QSP能够绕过SP仅能计算NC²函数的限制，从而高效地计算出任何多项式时间内可计算的函数。

QSP的构造包含两个核心组件：**门检查器**和**线检查器**。门检查器是一个用于验证电路每个门（如NAND门）输入输出一致性的跨度程序。对于一个给定的函数f，论文首先构造了一个“尽职的”（conscientious）跨度程序SP_φ来计算f的门检查函数φ，该SP保证了任何满足条件的线性组合必定为电路中的每条线（包括内部线）指派了非零系数。然而，SP_φ的“标签”不仅包含输入线，还包含内部线；如果简单地将其中的内部线多项式移入“自由”集合，恶意证明者可能会对同一条线同时指派0和1（双重赋值）。

为了防止双重赋值，第二个组件——**线检查器**——被引入。线检查器被构造为一组额外的多项式，其核心思想是：若证明者试图对某条线进行双重赋值，则多项式乘积无法被指定的除数多项式D(x)整除。直观上，针对单条线的检查器利用了多项式在特定根上的取值约束，使得双重赋值会导致乘积的可除性被破坏。通过中国剩余定理，为每条线独立构造的检查器可以组合成一个聚合线检查器。

最终，**规范QSP**通过中国剩余定理将上述两个组件融合：使用两套不相交的根集分别构造两个门检查器SP (一份对应V多项式，一份对应W多项式)，并使用第三套根集构造聚合线检查器。规范QSP的最终多项式通过中国剩余定理定义为在模各个除数多项式时分别与对应组件保持一致，而最后的除数多项式D(x)则为所有除数多项式的乘积。这样一个QSP的接受条件同时验证了门一致性和无双重赋值，从而正确计算了函数f。对于这个规范QSP，论文证明了其大小和度数均为电路规模的线性函数（具体常数：大小为36s，度数为130s），且所有相关多项式（如v(x)、w(x)、h(x)）的计算均可在O(s)或Õ(s)时间内完成，主要归功于多项式构造中的稀疏性。

在安全方面，QSP被用于构造函数依赖的CRS，其中各多项式在秘密点σ上的赋值通过编码（如双线性群中的指数）发布。证明者利用满足性赋值计算v(σ)、w(σ)和h(σ)的编码，验证者通过配对验证等式e(g_v, g_w) = e(g_h, g^{D(σ)})是否成立。为抵御攻击，CRS中额外包含了“知识指数”形式的项（如E(α v_k(σ))，E(β_v v_k(σ))等），使得论证的安全性基于q-幂Diffie-Hellman (q-PDH) 假设和q-幂知识指数 (q-PKE) 假设。q-PDH假设是一个可验证的假设，保证了已知E(1), ..., E(σ^q), E(σ^{q+2}), ..., E(σ^{2q})无法计算E(σ^{q+1})；q-PKE假设则是一个知识假设，它保证任何能输出编码对(c, ĉ)且满足ĉ = α c的敌手，必然“知道”c关于幂基{σ^i}的系数。安全性证明的核心思路是：从成功伪造的证明中，利用q-PKE抽取得到多项式v_mid(x)、w(x)和h(x)；若验证等式在多项式意义上成立，则QSP的完备性保证提取出了有效witness；若等式作为多项式不成立，则表明σ是某个非零多项式的根，从而可以构造算法打破q-PDH假设。额外的β_v, β_w项则用于确保抽取出的多项式确实落在了正确的线性张成空间中。

最后，论文还提出了QSP的变体——二次算术程序（QAP）。QAP面向大域上的算术电路，其接受条件涉及乘积与加法项的差。对于具有s个乘法门的算术电路，QAP的大小为n+s，度数为s。在实现中，基于QAP的Pinocchio系统在性能上优于基于QSP的系统。

### 核心公式与流程

**[二次跨度程序 (QSP) 的接受条件]**
$$D(x) \quad \text{ divides } \quad \left(v_0(x) + \sum_{k=1}^m a_k \cdot v_k(x)\right) \cdot \left(w_0(x) + \sum_{k=1}^m b_k \cdot w_k(x)\right)$$
> 作用：定义了QSP的核心验证条件。存在系数集合{a_k}和{b_k}，使得乘积多项式能被D(x)整除，当且仅当输入u被QSP接受。

**[规范 QSP 的构建（CRT 组合）]**
$$v_k(x) = \left\{ \begin{array}{c c} \hat{v}_k(x) \bmod \hat{D}^{(\mathcal{V})}(x) \\ v'_k(x) \bmod D'(x) \\ 1 \mod \hat{D}^{(\mathcal{W})}(x) \text{if} k = 0 \\ 0 \bmod \hat{D}^{(\mathcal{W})}(x) \text{if} k \neq 0 \end{array} \right.$$
> 作用：通过中国剩余定理，将门检查器（来自$\hat{v}_k$）、线检查器（来自$v'_k$）和另一个门检查器（模$\hat{D}^{(\mathcal{W})}$的常数条件）组合成规范QSP的V多项式集合。W多项式的组合方式类似。

**[SNARK 证明生成结构]**
$$\pi = \Big (E(v_{mid}(\sigma)), E(w(\sigma)), E(h(\sigma)), E(\alpha v_{mid}(\sigma)), E(\alpha w(\sigma)), E(\alpha h(\sigma)), E(\beta_v v_{mid}(\sigma) + \beta_w w(\sigma))\Big)$$
> 作用：展示了证明者输出的证明结构，包含7个编码后的元素，实现了常数的通信量。

**[SNARK 验证等式组]**
$$H \cdot D(\sigma) = (v_0(\sigma) + v_{in}(\sigma) + V_{mid}) \cdot (w_0(\sigma) + W)$$
$$V_{mid}' = \alpha V_{mid}, \quad W' = \alpha W, \quad H' = \alpha H$$
$$\gamma Y = (\beta_v \gamma) V_{mid} + (\beta_w \gamma) W$$
> 作用：验证者通过验证这些等式来确认证明。第一个等式验证QSP的可除性条件，第二组验证知识指数关系，最后一个等式确保多项式在正确的张成空间中。

**[安全假设：q-PDH]**
$$\Pr \left[ \begin{array}{c} p k \leftarrow \mathcal{E}. \text{Setup} (1^\kappa); \sigma \leftarrow F^*; \\
\tau \leftarrow (p k, E(1), E(\sigma), \ldots, E(\sigma^q), E(\sigma^{q+2}), \ldots, E(\sigma^{2q})); \\
y \leftarrow \mathcal{A} (\tau) : y = E(\sigma^{q+1}) \end{array} \right] = \texttt{negl}(\kappa)$$
> 作用：定义了q-幂Diffie-Hellman假设，确保即使给定缺了q+1次幂的幂序列，也无法计算缺失项。

### 实验结果
实验基于Pinocchio系统实现，使用256位BN曲线提供128比特安全级别，比较了QAP和QSP的性能，并与基于PCP的现有系统（如Cormode等人的Streaming Interactive Proofs [16]和Setty等人的PEPR [40]）进行了对比。实验主要衡量了大规模矩阵乘法任务（使用随机32比特矩阵元素）的性能。对于从N=25到N=100的矩阵规模，Pinocchio验证者的计算时间仅为8-13毫秒，比基于PCP的系统快5到7个数量级，这得益于验证仅需常数次配对操作和线性次数群运算。证明者的计算时间从8.9秒（N=25）到776.4秒（N=100），比现有系统快19到60倍。实验结果表明，基于QAP的方案在性能上优于基于QSP的方案，且整体系统已接近实用化水平。

### 局限性与开放问题
本文在SNARK设计方面取得了显著进展，但仍存在一些局限。首先，安全性依赖于非可验证的q-幂知识指数假设，这是密码学社区中争议较大的假设类型。其次，虽然CRS大小达到了准线性，但对于规模极大的电路，CRS的生成和存储仍可能成为瓶颈。此外，将QSP用于自适应选择电路时，需要通过普适电路进行转换，这会导致电路规模增加对数因子。未来工作包括探索能否在更标准的假设下获得类似效率，以及进一步优化证明者的计算，特别是在h(x)的计算上，将其从拟线性降低到线性。

### 强关联论文

[31] Karchmer, Wigderson. On Span Programs. **Structure in Complexity Theory Conference 1993** [Google Scholar](https://scholar.google.com/scholar?q=On+Span+Programs)

[27] Groth. Short Pairing-Based Non-Interactive Zero-Knowledge Arguments. **ASIACRYPT 2010** [Google Scholar](https://scholar.google.com/scholar?q=Short+Pairing-Based+Non-Interactive+Zero-Knowledge+Arguments)

[30] Ishai, Kushilevitz, Ostrovsky. Efficient Arguments without Short PCPs. **IEEE Conference on Computational Complexity 2007** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+Arguments+without+Short+PCPs)

[7] Ben-Sasson, Chiesa, Genkin, Tromer. On the Concrete-Efficiency Threshold of Probabilistically-Checkable Proofs. **STOC 2013** [Google Scholar](https://scholar.google.com/scholar?q=On+the+Concrete-Efficiency+Threshold+of+Probabilistically-Checkable+Proofs)

[21] Gennaro, Gentry, Parno. Non-Interactive Verifiable Computing: Outsourcing Computation to Untrusted Workers. **CRYPTO 2010** [Google Scholar](https://scholar.google.com/scholar?q=Non-Interactive+Verifiable+Computing:+Outsourcing+Computation+to+Untrusted+Workers)

[28] Groth, Ostrovsky, Sahai. New Techniques for Noninteractive Zero-Knowledge. **Journal of the ACM 2012** [Google Scholar](https://scholar.google.com/scholar?q=New+Techniques+for+Noninteractive+Zero-Knowledge)

[29] Groth, Sahai. Efficient Non-Interactive Proof Systems for Bilinear Groups. **SIAM Journal on Computing 2012** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+Non-Interactive+Proof+Systems+for+Bilinear+Groups)

[32] Kilian. A Note on Efficient Zero-Knowledge Proofs and Arguments (Extended Abstract). **STOC 1992** [Google Scholar](https://scholar.google.com/scholar?q=A+Note+on+Efficient+Zero-Knowledge+Proofs+and+Arguments)

[36] Micali. Computationally Sound Proofs. **SIAM Journal on Computing 2000** [Google Scholar](https://scholar.google.com/scholar?q=Computationally+Sound+Proofs)


## 关键词

+ 二次跨度程序
+ 二次算术程序
+ 算术电路
+ 简洁非交互式零知识证明
+ 公开可验证计算