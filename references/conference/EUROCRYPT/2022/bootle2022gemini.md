---
title: "Gemini: Elastic SNARKs for diverse environments"
标题简称:
论文类型: conference
会议简称: EUROCRYPT
发表年份: 2022
modified: 2025-04-27 09:03:01
created: 2025-04-11 11:19:48
---

## Gemini: Elastic SNARKs for diverse environments

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-07085-3_15)

## 作者

+ [Jonathan Bootle](Jonathan%20Bootle.md)
+ [Alessandro Chiesa](Alessandro%20Chiesa.md)
+ [Yuncong Hu](Yuncong%20Hu.md)
+ Michele Orru 

## 笔记

### 背景与动机
随着加密货币和可验证计算等应用的普及，简洁非交互式知识论证成为保护隐私和确保计算完整性的关键组件。然而，随着待证明实例规模激增至数十亿甚至万亿门级，证明者的计算开销成为核心瓶颈。现有方案主要分为两类：一类致力于最小化证明时间，通过动态规划技术实现线性时间，但代价是需要对实例和证据进行随机访问，导致内存消耗线性增长，在处理极大实例时效率低下；另一类则追求空间效率，允许证明者以流式方式访问输入，只需对数级别的内存，但计算时间退化为拟线性。这两类方案各执一端，无法同时满足不同计算环境（如内存充足但需快速证明，或内存受限但能接受较慢证明）的需求。本文试图填补这一空白，提出一种弹性的SNARK框架，使得单一的证明算法能够根据执行环境和语句规模，在时间高效和空间高效两种模式间灵活切换，且最终输出与具体模式选择无关。

### 相关工作

[BC12] Bitansky, N., Chiesa, A. Succinct arguments from multi-prover interactive proofs and their efficiency benefits. **CRYPTO 2012** [Google Scholar](https://scholar.google.com/scholar?q=Succinct%20arguments%20from%20multi-prover%20interactive%20proofs%20and%20their%20efficiency%20benefits)
> 核心思路：提出了复杂度保持的简洁论证概念，即证明时间和空间与运行原始计算本身渐近接近。
> 局限与区别：该工作允许多项式对数级别的膨胀，这种松弛使得其在实践中效率低下，且不同模式间缺乏兼容性。

[Blo+20] Block, A.R., Holmgren, J., Rosen, A., Rothblum, R.D., Soni, P. Public-coin zero-knowledge arguments with (almost) minimal time and space overheads. **TCC 2020** [Google Scholar](https://scholar.google.com/scholar?q=Public-coin%20zero-knowledge%20arguments%20with%20(almost)%20minimal%20time%20and%20space%20overheads)
> 核心思路：将流式模型引入SNARK，证明者仅需对数空间和拟线性时间即可完成证明。
> 局限与区别：该工作专注于单一空间高效实现，未提供时间高效的并行模式，且研究偏重理论，缺乏实现与基准测试。

[KZG10] Kate, A., Zaverucha, G.M., Goldberg, I. Constant-size commitments to polynomials and their applications. **ASIACRYPT 2010** [Google Scholar](https://scholar.google.com/scholar?q=Constant-size%20commitments%20to%20polynomials%20and%20their%20applications)
> 核心思路：提出基于双线性群的多项式承诺方案，承诺和证明大小均为常数。
> 局限与区别：本文首次将该方案实现为弹性方案，即分别构造其承诺和打开算法的时间高效与空间高效（流式）实现。

[BCG20] Bootle, J., Chiesa, A., Groth, J. Linear-time arguments with sublinear verification from tensor codes. **TCC 2020** [Google Scholar](https://scholar.google.com/scholar?q=Linear-time%20arguments%20with%20sublinear%20verification%20from%20tensor%20codes)
> 核心思路：使用张量码和乘检查协议构建线性时间论证。
> 局限与区别：本文在此基础上进一步实现了弹性化，特别是其中的扭曲标量积协议。

[Chi+20] Chiesa, A., Hu, Y., Maller, M., Mishra, P., Vesely, N., Ward, N. Marlin: preprocessing zkSNARKs with universal and updatable SRS. **EUROCRYPT 2020** [Google Scholar](https://scholar.google.com/scholar?q=Marlin%3A%20preprocessing%20zkSNARKs%20with%20universal%20and%20updatable%20SRS)
> 核心思路：提出从PIOP到预处理论证的编译器，结合多项式承诺实现简洁验证。
> 局限与区别：本文观察到Marlin的编译器能够保持弹性，并在此基础上构建了完整的弹性SNARK，实现了空间高效的索引器和证明者。

[GW20] Gabizon, A., Williamson, Z.J. Plookup: a simplified polynomial protocol for lookup tables. **ePrint 2020/315** [Google Scholar](https://scholar.google.com/scholar?q=Plookup%3A%20a%20simplified%20polynomial%20protocol%20for%20lookup%20tables)
> 核心思路：提出一种基于多项式恒等式的查找表协议，用于验证向量包含关系。
> 局限与区别：本文选择了该协议的核心多项式恒等式，但巧妙地利用矩阵的列主序特性，实现了空间高效（对数空间）的流式实现，而原始协议未考虑流式场景。

[Set20] Setty, S. Spartan: efficient and general-purpose zkSNARKs without trusted setup. **CRYPTO 2020** [Google Scholar](https://scholar.google.com/scholar?q=Spartan%3A%20efficient%20and%20general-purpose%20zkSNARKs%20without%20trusted%20setup)
> 核心思路：使用离线内存检查技术验证向量包含关系，并构建通用ZK-SNARK。
> 局限与区别：本文指出离线内存检查需要随机访问时间戳，与流式模型（对数空间）不兼容，因此只能选择式查找表协议。

[Ben+18] Ben-Sasson, E., et al. Fast reed-solomon interactive oracle proofs of proximity. **ICALP 2018** [Google Scholar](https://scholar.google.com/scholar?q=Fast%20reed-solomon%20interactive%20oracle%20proofs%20of%20proximity)
> 核心思路：提出用于一元多项式的低度测试协议。
> 局限与区别：本文借鉴了该工作中用于验证折叠多项式正确性的恒等式，但将其应用于张量积协议，而非低度测试。

[Tha13] Thaler, J. Time-optimal interactive proofs for circuit evaluation. **CRYPTO 2013** [Google Scholar](https://scholar.google.com/scholar?q=Time-optimal%20interactive%20proofs%20for%20circuit%20evaluation)
> 核心思路：通过动态规划实现了线性时间交互式证明。
> 局限与区别：该工作是时间最优的，但其动态规划策略导致了线性空间需求，无法在流式模型下对数空间实现。

[Wu+18] Wu, H., et al. DIZK: a distributed zero knowledge proof system. **USENIX Security 2018** [Google Scholar](https://scholar.google.com/scholar?q=DIZK%3A%20a%20distributed%20zero%20knowledge%20proof%20system)
> 核心思路：通过分布式集群（多机器）并行计算证明，以处理大规模电路。
> 局限与区别：DIZK需要昂贵的硬件集群和网络通信；本文的Gemini仅用单台机器即可处理更大规模的电路，成本显著降低。

### 核心技术与方案

本文的整体框架遵循SNARK构建的通用策略：先构造信息论层面的概率性证明，再用密码学原语进行编译。具体地，作者首先定义并实现了一个弹性多项式交互式预言机协议，然后构建了一个编译器，将弹性PIOP与弹性多项式承诺方案结合，最终生成一个弹性预处理论证系统。Gemini的具体方案围绕三个层次展开：弹性流模型、弹性张量积与标量积协议，以及弹性全息PIOP。

在流模型层面，作者扩展了文献[Blo+20]的工作，定义了流式预言机，允许算法以只向前的方式读取输入。一个流式算法可以通过start和next命令访问输入，且输出本身也是一个流。流式算法可以组合，其复杂度（时间、空间、遍历次数）遵循可预测的组合规则。弹性在这里意味着每个算法（如承诺、打开、PIOP证明者）都存在两个实现：一个时间高效的实现，使用$O(M)$时间和$O(M)$空间；另一个空间高效的实现，使用$\tilde{O}(M \log^2 M)$时间和$O(\log M)$空间，且两者输出相同。输出相同是弹性的核心性质，它保证了不同模式产生的证明是兼容的。

在底层原语上，本文构建了一个弹性标量积协议。该协议的核心思想是将验证标量积$\langle \mathbf{f}, \mathbf{g} \rangle = u$转化为验证一元多项式乘积$\mathbf{h}(X) = \mathbf{f}(X) \cdot \mathbf{g}(X^{-1})$的常数项系数。为回避直接计算$\mathbf{h}(X)$的高成本，作者引入了一种基于和多变量乘检查和协议的张量积协议。具体地，将向量$\mathbf{f}$和$\mathbf{g}$关联到多变量多项式$\widehat{\mathbf{f}}(\mathbf{X})$和$\widehat{\mathbf{g}}(\mathbf{X})$，利用乘检查和协议将标量积等式归约为两个求值查询$\widehat{\mathbf{f}}(\boldsymbol{\rho})$和$\widehat{\mathbf{g}}(\boldsymbol{\rho})$。然后，通过一个新的张量积协议，将验证一元多项式$\mathbf{f}(X)$与求值$\widehat{\mathbf{f}}(\boldsymbol{\rho})$的一致性归约为对一元多项式回忆性质的检查。例如，验证$\mathbf{f}'(X) = \mathbf{f}_e(X) + \rho_0 \cdot \mathbf{f}_o(X)$是否正确，可通过随机挑战点$\beta$上的等值检查实现：
$$
\mathbf{f}'(\beta^2) = \frac{\mathbf{f}(\beta) + \mathbf{f}(-\beta)}{2} + \rho_0 \cdot \frac{\mathbf{f}(\beta) - \mathbf{f}(-\beta)}{2\beta}.
$$
该协议的证明者具有弹性实现：时间高效模式在$O(N)$时间和$O(N)$空间内完成；空间高效模式通过一个栈结构递归计算各轮多项式系数，在$O(N \log N)$时间和$O(\log N)$空间内完成。

在R1CS协议层面，本文首先构建了一个非全息PIOP，其验证者需要线性时间访问整个电路。协议利用一个随机挑战向量$\mathbf{y}_C = (1, v, v^2, \ldots, v^{N-1})$将R1CS等式$A\mathbf{z} \circ B\mathbf{z} = C\mathbf{z}$压缩为三个标量积等式。通过引入另一个随机挑战$\eta$，将三个标量积组合为单个等式，进而调用弹性标量积协议进行验证。该协议证明者的时间高效实现为$O(M)$，空间高效实现为$\tilde{O}(M \log^2 M)$。

为获得全息性（即验证者时间与电路大小无关），本文进一步构建了全息PIOP。该方案要求证明者除发送$\mathbf{z}$外，还发送根据矩阵支持（row, col）提取的部分查询向量：
$$
\mathbf{r}_A^* := \mathbf{y}_A|_{\text{row}},\quad \mathbf{r}_B^* := \mathbf{y}_B|_{\text{row}},\quad \mathbf{r}_C^* := \mathbf{y}_C|_{\text{row}},\quad \mathbf{z}^\star := \mathbf{z}|_{\text{col}}.
$$
然后，证明者通过弹性查找表协议证明这些提取向量与原始向量的包含关系，并通过弹性乘积分协议验证各标量积的正确性。关键在于，作者利用矩阵列主序流$S_{\mathrm{col}}(A)$的非递增特性，实现了对$\mathbf{z}^\star$的流式生成：只需在$S_{\mathrm{cmcol}}(A)$的每一元素上，根据列索引是否变化，决定是否前进$\mathbf{z}$流并输出当前元素。这确保了空间高效模式下的对数空间复杂度。整个全息PIOP的时间高效证明者复杂度为$O(M)$，空间高效为$\tilde{O}(M \log^2 M)$，而验证者复杂度为$O(|\mathbf{x}| + \log M)$。

最后，通过弹性多项式承诺方案（基于KZG[10]的弹性实现）和弹性子协议（查找表、乘积分等），应用Marlin的编译器，构建了完整的弹性预处理SNARK——Gemini。该编译器保证了若输入组件是弹性的，则输出论证也是弹性的，且复杂度遵循相应的组合规则。

### 核心公式与流程

**[R1CS定义]**
$$
\text{给定 } A, B, C \in \mathbb{F}^{N \times N}, \mathbf{x} \in \mathbb{F}^{|\mathbf{x}|}, \mathbf{w} \in \mathbb{F}^{N - |\mathbf{x}|}, \mathbf{z}:=(\mathbf{x}, \mathbf{w}), \text{验证 } A\mathbf{z} \circ B\mathbf{z} = C\mathbf{z}.
$$
> 作用：定义待证明的计算问题，是SNARK的目标关系。

**[标量积归约到乘检查和]**
$$
\frac{1}{2^n} \sum_{\boldsymbol{\omega} \in \mathcal{H}^n} (\widehat{\mathbf{f}} \cdot \widehat{\mathbf{g}})(\boldsymbol{\omega}) = u.
$$
> 作用：将标量积验证归约为多变量多项式在布尔超立方上的平均和，这是乘检查（sumcheck）协议的基本输入。

**[张量积一致性检查]**
$$
\mathbf{f}'(\beta^2) = \frac{\mathbf{f}(\beta) + \mathbf{f}(-\beta)}{2} + \rho_0 \cdot \frac{\mathbf{f}(\beta) - \mathbf{f}(-\beta)}{2\beta}.
$$
> 作用：验证者通过随机点$\beta$上的求值，检查证明者提供的“折叠”多项式$\mathbf{f}'(X)$是否由原始多项式$\mathbf{f}(X)$通过挑战$\rho_0$正确计算得出，是张量积协议安全性的核心。

**[R1CS压缩为标量积]**
$$
\langle A\mathbf{z} \circ \mathbf{y}_C, B\mathbf{z} \rangle = \langle C\mathbf{z}, \mathbf{y}_C \rangle.
$$
> 作用：使用随机挑战向量$\mathbf{y}_C$将元素级等式$A\mathbf{z} \circ B\mathbf{z} = C\mathbf{z}$压缩为单个标量积等式，是协议的第一步。

**[线性组合归约]**
$$
\langle \mathbf{z}, \hat{\mathbf{a}} + \eta \cdot \hat{\mathbf{b}} + \eta^2 \cdot \hat{\mathbf{c}} \rangle = u_A + \eta \cdot u_B + \eta^2 \cdot u_C.
$$
> 作用：使用随机挑战$\eta$将三个标量积等式线性组合成一个，进一步降低验证复杂度。

**[查找表恒等式]**
$$
\prod_{j=0}^{M+N-1} \left(Y (1+Z) + w_{j+1} + w_j \cdot Z\right) = (1+Z)^M \prod_{j=0}^{M-1} (Y + f^*_j) \prod_{j=0}^{N-1} \left(Y (1+Z) + f_{j+1} + f_j \cdot Z\right).
$$
> 作用：该多项式恒等式成立当且仅当向量$\mathbf{f}^*$的所有元素都包含在向量$\mathbf{f}$中（即$\mathbf{f}^* \subseteq \mathbf{f}$），是查找表协议的核心。

**[乘积分归约]**
$$
\langle \mathbf{g} \circ \mathbf{y}^\prime, \mathbf{f}_\circlearrowleft \rangle = \psi \mathbf{g}(\psi) + e - \psi^N.
$$
> 作用：将证明$\prod_i f_i = e$归约为一个标量积和一个一元多项式求值，是乘积分协议的基础。

### 实验结果

实验基于Amazon AWS EC2 c5.9xlarge实例（36核）运行，使用BLS12-381曲线。测试涵盖了实例规模$N = 2^{18}$到$2^{35}$。主要结果表明，Gemini在单台机器上即可处理远超现有方案的电路规模。具体地，非预处理方案的证明者能处理高达$2^{35}$个约束，预处理方案也能处理$2^{32}$个约束，而文献中DIZK[18]的最大规模仅为$2^{31}$（且需20台机器集群）。内存方面，Gemini的时间高效模式在实例大于$2^{25}$时会因内存溢出而失败，而弹性模式始终将内存消耗保持在1GB以下，随实例增大保持恒定。运行时间方面，受限于多标量乘法的主导地位，曲线近乎线性。经济成本估算显示，预处理方案证明$2^{31}$个门约需89美元（单机约2天），相比DIZK的约500美元（20台高配机器约10小时），成本降低约82%。非预处理方案证明$2^{35}$个门仅需约40美元。验证时间和证明大小均为对数或常数：在$2^{12}$到$2^{35}$范围内，证明大小为13-27 KB，验证时间为16-30毫秒。

### 局限性与开放问题
该工作主要在标量域（BLS12-381的标量域）上构建，验证和证明大小依赖于配对友好曲线。虽然文中指出可在任意足够大的域上工作，但具体到椭圆曲线选择仍需进一步研究以优化具体效率，特别是对于非平滑域，现有底层协议（如KZG方案）可能不再适用。此外，空间高效的离线内存检查不可行，导致必须使用多项式查找表协议，这可能带来额外的承诺开销。未来的工作可以探索如何在弹性框架内实现内存检查，或寻找更结合域的通用流式查找表技术。

### 强关联论文

[BC12] Bitansky, N., Chiesa, A. Succinct arguments from multi-prover interactive proofs and their efficiency benefits. **CRYPTO 2012** [Google Scholar](https://scholar.google.com/scholar?q=Succinct%20arguments%20from%20multi-prover%20interactive%20proofs%20and%20their%20efficiency%20benefits)

[KZG10] Kate, A., Zaverucha, G.M., Goldberg, I. Constant-size commitments to polynomials and their applications. **ASIACRYPT 2010** [Google Scholar](https://scholar.google.com/scholar?q=Constant-size%20commitments%20to%20polynomials%20and%20their%20applications)

[BCG20] Bootle, J., Chiesa, A., Groth, J. Linear-time arguments with sublinear verification from tensor codes. **TCC 2020** [Google Scholar](https://scholar.google.com/scholar?q=Linear-time%20arguments%20with%20sublinear%20verification%20from%20tensor%20codes)

[Chi+20] Chiesa, A., Hu, Y., Maller, M., Mishra, P., Vesely, N., Ward, N. Marlin: preprocessing zkSNARKs with universal and updatable SRS. **EUROCRYPT 2020** [Google Scholar](https://scholar.google.com/scholar?q=Marlin%3A%20preprocessing%20zkSNARKs%20with%20universal%20and%20updatable%20SRS)

[GW20] Gabizon, A., Williamson, Z.J. Plookup: a simplified polynomial protocol for lookup tables. **ePrint 2020/315** [Google Scholar](https://scholar.google.com/scholar?q=Plookup%3A%20a%20simplified%20polynomial%20protocol%20for%20lookup%20tables)

[Set20] Setty, S. Spartan: efficient and general-purpose zkSNARKs without trusted setup. **CRYPTO 2020** [Google Scholar](https://scholar.google.com/scholar?q=Spartan%3A%20efficient%20and%20general-purpose%20zkSNARKs%20without%20trusted%20setup)

[Ben+18] Ben-Sasson, E., et al. Fast reed-solomon interactive oracle proofs of proximity. **ICALP 2018** [Google Scholar](https://scholar.google.com/scholar?q=Fast%20reed-solomon%20interactive%20oracle%20proofs%20of%20proximity)

[Tha13] Thaler, J. Time-optimal interactive proofs for circuit evaluation. **CRYPTO 2013** [Google Scholar](https://scholar.google.com/scholar?q=Time-optimal%20interactive%20proofs%20for%20circuit%20evaluation)

[Wu+18] Wu, H., et al. DIZK: a distributed zero knowledge proof system. **USENIX Security 2018** [Google Scholar](https://scholar.google.com/scholar?q=DIZK%3A%20a%20distributed%20zero%20knowledge%20proof%20system)

[Blo+20] Block, A.R., Holmgren, J., Rosen, A., Rothblum, R.D., Soni, P. Public-coin zero-knowledge arguments with (almost) minimal time and space overheads. **TCC 2020** [Google Scholar](https://scholar.google.com/scholar?q=Public-coin%20zero-knowledge%20arguments%20with%20(almost)%20minimal%20time%20and%20space%20overheads)


## 关键词

+ 弹性SNARK
+ 流式证明
+ 无FFT预处理论证
+ R1CS
+ 内存时间权衡