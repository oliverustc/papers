---
title: "A Succinct Range Proof for Polynomial-based Vector Commitment"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2024
modified: 2025-04-27 08:54:41
created: 2025-04-15 16:33:47
---

## A Succinct Range Proof for Polynomial-based Vector Commitment

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3658644.3670324)

## 作者

+ Rui Gao 
+ Zhiguo Wan 
+ [Yuncong Hu](Yuncong%20Hu.md)
+ Huaqun Wang 

## 笔记

### 背景与动机
范围证明允许证明者在不泄露实际数值的情况下向验证者证明一个被承诺的数字位于指定区间内，是匿名加密货币、电子投票和拍卖等应用的核心构建模块 [1-7]。然而，当需要对包含多个元素的向量进行批量范围证明时，现有方案的效率会显著下降。其根本原因在于，这些方案大多针对单个元素的承诺，证明者需要将一组元素承诺作为公开陈述发送给验证者，导致通信复杂度随向量长度线性增长，严重阻碍了系统的可扩展性。例如，基于内积论证的方案虽能将证明大小优化至对数级别，但无法降低陈述长度 [9, 10]。基于多项式交互式预言机证明的Plonkup方案虽然具有常数级的陈述长度，但证明大小与证明复杂度依赖于范围大小，在处理大范围时效率低下 [20]。为填补这一空白，本文旨在为基于多项式的向量承诺设计一种范围证明，使得证明者只需发送一个常数大小的承诺，就能证明向量中的每一个元素均处于指定范围内。

### 相关工作

[9] Daza等. Updateable inner product argument with logarithmic verifier and applications. **PKC 2020** [Google Scholar](https://scholar.google.com/scholar?q=Updateable+inner+product+argument+with+logarithmic+verifier+and+applications)
> 核心思路：引入结构化参考字符串来降低内积论证的验证复杂度，实现了对数级的通信和验证复杂度。
> 局限与区别：其陈述长度仍然与向量长度 l 线性相关，需要传输 l 个群元素作为公开陈述，在 l 较大时通信压力巨大。

[10] Bunz等. Bulletproofs: Short proofs for confidential transactions and more. **S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Bulletproofs%3A+Short+proofs+for+confidential+transactions+and+more)
> 核心思路：提出基于二进制分解和内积论证的范围证明，支持批量证明，证明大小为 O(log n)。
> 局限与区别：其陈述长度和验证复杂度均为 O(l·n)，需要对所有承诺进行逐个验证，且陈述长度随 l 线性增长。

[20] Gabizon等. Proposal: The turbo-plonk program syntax for specifying snark programs. **2020** [Google Scholar](https://scholar.google.com/scholar?q=Proposal%3A+The+turbo-plonk+program+syntax+for+specifying+snark+programs)
> 核心思路：采用PIOP范式，将向量分解为二进制位并编码为 n 个单变量多项式，证明这些多项式的取值约束和组合关系。
> 局限与区别：虽然陈述长度最优，但证明过程中需要分别承诺 n 个多项式，导致证明大小与 n 线性相关。

[23] Chiesa等. Marlin: Preprocessing zksnarks with universal and updatable srs. **EUROCRYPT 2020** [Google Scholar](https://scholar.google.com/scholar?q=Marlin%3A+Preprocessing+zksnarks+with+universal+and+updatable+srs)
> 核心思路：提出了一种高效的PIOP编译框架，并引入了一种双变量随机多项式用于多项式零测试。
> 关联：本文的零测试PIOP和PIOP编译过程直接借鉴并继承了Marlin的设计范式。

### 核心技术与方案

本文提出MissileProof，一个用于向量承诺范围证明的零知识简洁非交互式论证协议。其核心技术路径是将向量范围证明问题等价转化为两个多项式关系问题——双变量到单变量SumCheck问题和双变量多项式ZeroTest问题，并分别为这两个问题设计了新颖的多项式交互式预言机证明。

首先，将需要证明的向量 $\mathbf{v} \in \mathbb{F}^l$ 及其二进制分解矩阵 $M \in \mathbb{F}^{l \times n}$ 扩展为多项式 f(X)（度小于l的单变量多项式）和双变量多项式 m(X, Y)（Y方向度小于n）。那么，向量范围证明等价于证明两个条件：条件1为双变量到单变量SumCheck，即 $\sum_{b \in \mathbb{H}_n} \mathfrak{m}(X, b) = \mathfrak{f}(X)$；条件2为双变量多项式ZeroTest，即对于所有$a \in \mathbb{H}_l, b_j \in \mathbb{H}_n$，有 $\mathfrak{m}(a, b_j)(\mathfrak{m}(a, b_j) - 2^j) = 0$。

本文的核心理论贡献是提出一个引理，将条件1中的求和操作转化为一个简单的多项式恒等式。引理3.2证明，双变量多项式m满足条件1当且仅当存在一个多项式u(X, Y)（Y方向度小于n-1），使得 $\mathfrak{m}(X, Y) = \frac{\mathfrak{f}(X)}{n} + Y \cdot \mathfrak{u}(X, Y)$。基于此，验证者只需在随机点$(\tau_x, \tau_y)$上查询f和m的值，并检查上述等式是否成立即可，从而将复杂的求和验证简化为单点检查，并根据Schwartz-Zippel引理保证了极高的可靠性。

对于条件2，本文通过引入一个双变量随机多项式r(R, Y)将其转化为一个单变量多项式SumCheck和一个单变量多项式ZeroTest的组合。具体地，定义 $\mathfrak{M}(X, Y) = \mathfrak{m}(X, Y)(\mathfrak{m}(X, Y) - \mathfrak{p}(Y))$，其中p(Y)是编码$2^j$的多项式。那么，$\mathfrak{M}(a, b)=0$对所有b成立等价于 $\mathfrak{M}^*(r, a) = \sum_{b \in \mathbb{H}_n} \mathfrak{M}(a, b) \mathfrak{r}(r, b) = 0$ 对所有a成立。证明分两阶段：首先，证明者使用单变量ZeroTest PIOP证明对于某个随机数$\tau_r$，$\mathfrak{M}^*(\tau_r, X)$在$\mathbb{H}_l$上为零；然后，证明者使用单变量SumCheck PIOP证明所声称的 $\mathfrak{M}^*(\tau_r, X)$ 确实是由多项式m和p正确求和得到的。

最后，MissileProof遵循标准的PIOP编译流程。将上述PIOP与一个基于KZG的双变量多项式承诺方案编译，可以得到一个公开掷币的简洁交互式论证。再通过Fiat-Shamir变换，最终得到一个非交互式论证。安全性基于KZG多项式承诺方案的绑定性和知识可靠性。系统复杂度方面，证明大小为O(1)，验证时间和陈述长度均为O(1)，证明者计算复杂度为$O(l \log l \cdot n \log n)$域运算和$O(ln)$群指数运算。

### 核心公式与流程

**[Bi-to-uni variate SumCheck]**
$$\sum_{b \in \mathbb{H}_n} \mathfrak{m}(X, b) = \mathfrak{f}(X) \iff \exists \mathfrak{u} \in \mathbb{F}_{d(X)<l, d(Y)<n-1}[X,Y] : \mathfrak{m}(X,Y) = \frac{\mathfrak{f}(X)}{n} + Y \cdot \mathfrak{u}(X,Y)$$
> 作用：这是用于验证条件1的双变量到单变量SumCheck的核心引理，它将一个复杂的求和运算等价转化为一个简单多项式恒等式。

**[Bivariate ZeroTest Protocol Phase 1: Uni-ZeroTest]**
$$\forall a \in \mathbb{H}_l, \mathfrak{M}^*(\tau_r, a) = 0 \iff \mathfrak{M}^*(\tau_r, X) = \mathfrak{e}(X) \cdot z_{\mathbb{H}_l}(X)$$
> 作用：验证者随机选择$\tau_r$，证明者通过构造一个多项式$\mathfrak{e}(X)$，使得$\mathfrak{M}^*(\tau_r, X)$能被$\mathbb{H}_l$的消逝多项式整除，从而证明$\mathfrak{M}^*(\tau_r, X)$在$\mathbb{H}_l$上所有点都为零。

**[Bivariate ZeroTest Protocol Phase 2: Uni-SumCheck]**
$$\mu_{\mathfrak{M}^*} = \sum_{b \in \mathbb{H}_n} \mathfrak{M}(\tau_x, b)\mathfrak{r}(\tau_r, b) \iff \mathfrak{M}(\tau_x, Y)\mathfrak{r}(\tau_r, Y) = \frac{\mu_{\mathfrak{M}^*}}{n} + Y \cdot \mathfrak{g}(Y) + \mathfrak{q}(Y)z_{\mathbb{H}_n}(Y)$$
> 作用：这是用于验证条件1的双变量到单变量SumCheck的核心引理，它将一个复杂的求和运算等价转化为一个简单多项式恒等式。

### 实验结果
实验在配备3.20GHz处理器和8GB内存的虚拟机上运行，使用Go语言实现，椭圆曲线选用bn256进行配对计算，secp256k1进行群运算。实验设置固定比特长度n为64，向量长度l从64变化到16384。与BulletProof [10]、Daza等人的方案[9]以及TurboPlonk [20]进行了比较。结果显示，MissileProof在陈述长度、证明大小和验证时间三个关键指标上均为最优。具体而言，当l=16384时，MissileProof的陈述长度仅为0.03125KB（一个群元素），证明大小仅为1.375KB，验证时间仅为0.01秒。相比之下，BulletProof和Daza的方案陈述长度达到1024KB，证明大小分别为2.91KB和10.75KB。MissileProof的证明时间在l=16384时为614秒，高于TurboPlonk的372秒，但并无数量级差距，因为域运算（FFT）远快于椭圆曲线群运算。总体上，MissileProof在通信和验证效率上实现了显著提升，证明了其理论分析中的渐进优势。

### 局限性与开放问题
该方案的证明时间相比TurboPlonk略有增加，尤其是在l较大时，但仍在可接受范围内。此外，本文实现方案依赖于基于KZG的多项式承诺方案，这需要可信任的设置来生成结构化参考字符串，在某些去中心化场景下可能构成信任假设。一个自然的扩展方向是使用透明设置的多项式承诺方案（如FRI或DARK）来替换KZG，从而获得无需可信设置的版本。另一个开放问题是，如何进一步优化双变量多项式承诺阶段的计算开销，以便更好地适配证明时间敏感的应用。

### 强关联论文

[8] Tomescu等. Aggregatable subvector commitments for stateless cryptocurrencies. **SCN 2020** [Google Scholar](https://scholar.google.com/scholar?q=Aggregatable+subvector+commitments+for+stateless+cryptocurrencies)

[9] Daza等. Updateable inner product argument with logarithmic verifier and applications. **PKC 2020** [Google Scholar](https://scholar.google.com/scholar?q=Updateable+inner+product+argument+with+logarithmic+verifier+and+applications)

[10] Bunz等. Bulletproofs: Short proofs for confidential transactions and more. **S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Bulletproofs%3A+Short+proofs+for+confidential+transactions+and+more)

[12] Kate等. Constant-size commitments to polynomials and their applications. **ASIACRYPT 2010** [Google Scholar](https://scholar.google.com/scholar?q=Constant-size+commitments+to+polynomials+and+their+applications)

[20] Gabizon等. Proposal: The turbo-plonk program syntax for specifying snark programs. **2020** [Google Scholar](https://scholar.google.com/scholar?q=Proposal%3A+The+turbo-plonk+program+syntax+for+specifying+snark+programs)

[23] Chiesa等. Marlin: Preprocessing zksnarks with universal and updatable srs. **EUROCRYPT 2020** [Google Scholar](https://scholar.google.com/scholar?q=Marlin%3A+Preprocessing+zksnarks+with+universal+and+updatable+srs)

[25] Papamanthou等. Signatures of correct computation. **TCC 2013** [Google Scholar](https://scholar.google.com/scholar?q=Signatures+of+correct+computation)

[27] Ben-Sasson等. Aurora: Transparent succinct arguments for r1cs. **EUROCRYPT 2019** [Google Scholar](https://scholar.google.com/scholar?q=Aurora%3A+Transparent+succinct+arguments+for+r1cs)


## 关键词

+ 范围证明
+ 向量承诺
+ 零知识证明
+ PIOP
+ KZG多项式承诺
+ 反洗钱区块链