---
title: "Succinct Hash-Based Arbitrary-Range Proofs"
标题简称:
论文类型: journal
期刊简称: TIFS
发表年份: 2024
modified: 2025-04-17 13:42:27
created: 2025-04-11 12:07:45
---

## Succinct Hash-Based Arbitrary-Range Proofs

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/10752637)

## 作者

+ Weihan Li 
+ Zongyang Zhang 
+ [Yanpei Guo](Yanpei%20Guo.md) 
+ [Sherman SM Chow](Sherman%20SM%20Chow.md)
+ Zhiguo Wan 

## 笔记

### 背景与动机
零知识范围证明（ZKRP）允许证明者向验证者证明一个承诺整数落在给定区间内，而不泄漏该整数的任何其他信息。该原语在隐私保护系统（如匿名投票、机密交易和智能合约）中至关重要。随着后量子时代的到来，长期安全性成为高价值应用（如民主增强系统或受监管金融场景）的迫切需求。然而，当前最先进的后量子ZKRP——基于格（LWE/SIS）的构造，例如Lyubashevsky等人于CCS 2020提出的方案（LNS20）[15]和Couteau等人于Eurocrypt 2021提出的方案（CKLR21）[16]——其证明规模与范围维度n呈线性关系，严重限制了在不可变账本等长期存储场景中的可持续性。另一方面，基于离散对数的Bulletproofs [11]虽然具有对数级证明规模，但不具备后量子安全性。基于哈希的通用零知识证明（如Aurora [17]和Ligero [22]）虽然可以用于任意函数，但将其特定化为范围关系需要复杂的归约，导致实际效率低下。本文旨在填补这一空白：构建一个透明的、可证明后量子安全的、证明规模为poly-log(n)的ZKRP，同时支持任意区间和高效批处理，其具体证明规模须小于已知的格基方案。

### 相关工作

[11] Bünz等. Bulletproofs: Short proofs for confidential transactions and more. **IEEE S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Bulletproofs+Short+proofs+for+confidential+transactions+and+more)
> 核心思路：基于离散对数假设和内积论证（IPA），构造对数级证明规模的ZKRP，支持批处理。
> 局限与区别：不满足后量子安全；只能处理形如$[0,2^n-1]$的固定区间，无法直接扩展至$u$进制任意区间；批处理要求实例数量为2的幂。

[15] Lyubashevsky等. Practical lattice-based zero-knowledge proofs for integer relations. **CCS 2020** [Google Scholar](https://scholar.google.com/scholar?q=Practical+lattice-based+zero-knowledge+proofs+for+integer+relations)
> 核心思路：利用格上的加法关系ZKP构造区间证明，支持任意区间。
> 局限与区别：证明规模为$O(n)$；不支持有效的批处理；运行时间依赖FFT。

[16] Couteau等. Efficient range proofs with transparent setup from bounded integer commitments. **EUROCRYPT 2021** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+range+proofs+with+transparent+setup+from+bounded+integer+commitments)
> 核心思路：基于有界整数承诺构造高效的格基区间证明，提供DLog和LWE两种实例化。
> 局限与区别：LWE实例化的证明规模为$O(n)$，远大于本文的对数规模；不提供开源实现。

[17] Ben-Sasson等. Aurora: Transparent succinct arguments for R1CS. **EUROCRYPT 2019** [Google Scholar](https://scholar.google.com/scholar?q=Aurora+Transparent+succinct+arguments+for+R1CS)
> 核心思路：利用Reed-Solomon码和FRI协议，实现透明的零知识证明。
> 局限与区别：通用方案对特定关系效率较低，在区间证明上比SHARP-PQ慢10–100倍，证明规模大1–2倍。

[18] Zhang等. Transparent polynomial delegation and its applications to zero knowledge proof. **IEEE S&P 2020** [Google Scholar](https://scholar.google.com/scholar?q=Transparent+polynomial+delegation+and+its+applications+to+zero+knowledge+proof)
> 核心思路：提出Virgo，一种基于单变量和校验和FRI的内积论证，具有$O(\log^2 n)$验证者复杂度（通过GKR委托FFT）。
> 局限与区别：Virgo的GKR委托带来数十KB的常数开销，不适合区间证明；SHARP-PQ通过避免GKR直接提供$O(n)$验证者，并支持批处理和$u$进制区间。

[22] Ames等. Ligero: Lightweight sublinear arguments without a trusted setup. **CCS 2017** [Google Scholar](https://scholar.google.com/scholar?q=Ligero+Lightweight+sublinear+arguments+without+a+trusted+setup)
> 核心思路：基于IOP的通用零知识证明，证明规模为$O(\sqrt{n})$。
> 局限与区别：在区间证明上，SHARP-PQ的证明规模小约10倍，运行时间快10–100倍。

[21] Zhang等. Ligerolight: Optimized IOP-based zero-knowledge argument for blockchain scalability. **IEEE TDSC 2024** [Google Scholar](https://scholar.google.com/scholar?q=Ligerolight+Optimized+IOP-based+zero-knowledge+argument+for+blockchain+scalability)
> 核心思路：提出一种批处理IPA，通过随机线性组合将多个内积归约到一个和校验。
> 局限与区别：SHARP-PQ在此基础上进一步优化验证者复杂度，并有效利用Hadamard同态处理$u$进制区间。

[27] Esgin等. MatRiCT: Efficient, scalable and post-quantum blockchain confidential transactions protocol. **CCS 2019** [Google Scholar](https://scholar.google.com/scholar?q=MatRiCT+Efficient+scalable+and+post-quantum+blockchain+confidential+transactions+protocol)
> 核心思路：提出后量子环形机密交易，使用格基签名和平衡证明。
> 局限与区别：其平衡证明规模较大（约93KB）；SHARP-PQ作为替代平衡证明，更小（37KB）且更高效。

### 核心技术与方案

SHARP-PQ的核心框架基于$u$进制分解和（批处理）内积论证。其整体思路为：将一个秘密整数$V$分解为$u$进制向量$\pmb{v}$，利用Reed-Solomon（RS）码对向量进行编码和承诺，然后将区间关系转化为两个Hadamard乘积关系，再通过随机线性组合转化为两个内积关系，最后使用批处理IPA证明这些内积成立。

**1. $u$进制分解框架与Hadamard同态**  
对于形如$[0, u^n-1]$的区间，证明者首先将$V$分解为长度为$m$（$m \geq n$，通常$m=O(n)$）的$u$进制向量$\pmb{v}$，使得$V = \langle \pmb{v}, \mathcal{W}_u(u^m) \rangle$。区间关系等价于两个条件：（i）$\pmb{v}$的最高$m-n$个分量为0；（ii）每个分量均在$\{0,1,\dots,u-1\}$中。条件（ii）可通过Hadamard积表示为  
$$\pmb{v} \circ (\pmb{v} - \mathbf{1}^m) \circ \cdots \circ (\pmb{v} - (u-1)^m) = \mathbf{0}^m.$$  
条件（i）可写为  
$$\pmb{v} \circ (\mathbf{1}^{m-n} \| \mathbf{0}^n) = \mathbf{0}^m.$$  
为了利用RS码的同态性，证明者不是直接承诺$\pmb{v}$，而是先通过IFFT将$\pmb{v}$插值为多项式$\hat{\nu}$（满足$\hat{\nu}|_H = \pmb{v}$），再对$\hat{\nu}$在更大的求值集合$L$上进行FFT得到RS码字$\hat{\nu}|_L$，并用Merkle树承诺。由于RS码对Hadamard积具有同态性（即两个码字的逐点乘积对应多项式乘积模$Z_H$），证明者可以仅基于$\hat{\nu}|_L$计算$\widehat{\pmb{v} \circ (\pmb{v}-\mathbf{1}^m)\circ\cdots}$的码字，而无需额外FFT。这一步是$u$进制区间高效的关键。

**2. 批处理内积论证（Batch IPA）**  
给定承诺的多个秘密向量$\pmb{v}_1,\dots,\pmb{v}_t$和一个公共向量$\pmb{r}$，批处理IPA旨在证明所有内积关系$\langle\pmb{v}_i,\pmb{r}\rangle = y_i$。SHARP-PQ改进了Virgo [18]中的IPA：  
- 证明者将$\pmb{v}_i$编码为RS码字$\hat{\nu}_i|_L$，并将所有码字按列存入一个Merkle树的叶子节点。  
- 验证者发送随机系数$\beta_1,\dots,\beta_t$，双方执行单变量和校验协议（Protocol 1）来证明$\sum_{a\in H} \left(\sum_i \beta_i\hat{\nu}_i(a)\right)\hat{r}(a) = \sum_i \beta_i y_i$。  
- 关键改进：验证者不再通过昂贵的GKR协议或完整FFT计算$\hat{r}|_L$，而是仅需计算在FRI查询位置集$\mathcal{T}$（大小$\kappa=O(\lambda)$）上的$\hat{r}|_{\mathcal{T}}$。这通过Lagrange基函数在$O(n)$时间内完成，将验证者复杂度从$O(\log^2 n)$（GKR）降为$O(n)$，同时避免了额外的委托开销。  
- 证明者复杂度为$O(tn\log n)$（FFT + Merkle树）加$O(tn)$（和校验多项式构建）。验证者复杂度为$O(n+t)$。证明规模为$O(t + \log n)|\mathbb{F}| + O(\log^2 n)|\mathsf{H}|$。  
批处理进一步通过随机线性组合实现：多个FRI电路具有相同结构（仅含加法和标量乘法门），验证者可通过一个随机线性组合将所有电路的求和归约到一次GKR委托，使得验证者复杂度变为$O(t + \log^2 n)$，与$n$无关。

**3. 区间证明构造**  
对于固定区间$[0, u^n-1]$，协议（Protocol 4）直接调用批处理IPA（$t=2$）证明两个内积关系（分别对应条件(i)和(ii)）。对于任意区间$[A, B-1]$，协议（Protocol 6）引入两个辅助秘密$C=V-A$和$D=V-B+2^n$，并证明$C, D \in [0, 2^n-1]$以及平衡关系$\langle\pmb{v}-\pmb{a}-\pmb{c}, \mathcal{W}_2(2^m)\rangle = 0$等（共7个内积关系）。这些关系全部通过一次批处理IPA证明。零知识性通过添加随机掩码多项式实现。

**4. 安全性**  
SHARP-PQ在随机预言模型（ROM）中证明是零知识论证。安全性基于哈希函数的碰撞抵抗和FRI协议的可靠性与接近性。通过证明批次IPA的round-by-round（RBR）可靠性，确保在量子ROM下仍安全。定理3给出协议4的可靠性误差为$2/|\mathbb{F}| + O(|L|/|\mathbb{F}|) + \mathsf{negl}(\ell, O(un)/|L|)$。

### 核心公式与流程

**[Hadamard积关系转内积关系]**
$$
\pmb{v} \circ (\pmb{v} - \mathbf{1}^m) \circ \cdots \circ (\pmb{v} - (u-1)^m) = \mathbf{0}^m,\quad \pmb{v} \circ (\mathbf{1}^{m-n} \| \mathbf{0}^n) = \mathbf{0}^m.
$$
> 作用：将区间合法性条件转化为两个Hadamard积为零向量的断言，为后续转化为内积关系奠定基础。

**[批处理IPA核心和校验]**
$$
\sum_{a\in H} \hat{q}(a) = \sum_{a\in H} \sum_{i=1}^t \beta_i \hat{\nu}_i(a) \hat{r}(a) = \sum_{i=1}^t \beta_i y_i.
$$
> 作用：通过随机线性组合，将多个内积验证归约为单个多项式在集合$H$上的求和，进而可调用单变量和校验协议。

**[FRI查询位置处$\hat{r}$的Lagrange计算]**
$$
\hat{r}(x) = \sum_{i=1}^{|H|} \hat{\lambda}_i(x) r_i,\quad \hat{\lambda}_i(x) = \prod_{j\neq i} \frac{x - r_j}{r_i - r_j}.
$$
> 作用：验证者只需在$O(\lambda)$个查询点上计算$\hat{r}(\tau_k)$，时间$O(n)$，避免全FFT或GKR委托。

### 实验结果

实验在一台AMD Ryzen 3900X处理器（80GB RAM）上运行，无并行化。代码基于C++实现，使用libiop库，采用BLAKE3哈希函数（128位安全）。RS码率：单区间1/8，批处理1/16。域选用广义梅森素数$p=2^{64}-2^{32}+1$，相比Virgo的扩展域$\mathbb{F}_{p^2}$（$p=2^{61}-1$），乘法快约2.3倍。安全级别设为120/128位。主要性能数值（来自论文表IV、V、VI）：对于单实例$[0,2^{128}-1]$，SHARP-PQ的证明大小为34.3KB，证明者时间0.010s，验证者时间0.004s。相比之下，LNS20 [15] 的证明大小为26.4KB（但仅支持$n=128$，且为任意区间，SHARP-PQ更优当$n\geq 512$时，即41.9KB vs 51.3KB；批处理$n=128,t=32$时，SHARP-PQ 73.8KB vs LNS20 844.8KB，优势10倍以上。对比Bulletproofs [11]，SHARP-PQ的证明者时间快约10倍（0.010s vs 0.050s），验证者快约5倍（0.004s vs 0.020s），但证明大小更大（34.3KB vs 0.72KB）。对比CKLR21 [16]（仅比较证明大小），对于$n=64$，$(128,180)$参数下，SHARP-PQ为0.12MB，CKLR21为4.52MB，差距约38倍。对比通用ZKP：对于$n=128$，SHARP-PQ的证明大小28.5KB，Aurora 45.0KB，Ligero 376.3KB；证明者时间SHARP-PQ 0.010s，Aurora 0.090s，Ligero 0.070s；验证者时间SHARP-PQ 0.003s，Aurora 0.005s，Ligero 0.050s。在批处理场景，SHARP-PQ的验证时间与$t$弱相关（如$n=128,t=128$时验证者0.01s），证明规模也仅线性于$t$（88.0KB）。与MatRiCT [27]和MatRiCT+ [28]的集成比较显示，SHARP-PQ作为平衡证明，对于1-2交易，其证明大小37KB，证明者10ms，验证者3ms，优于MatRiCT的242ms和93KB，与MatRiCT+的100ms和47KB相当或更优。

### 局限性与开放问题

SHARP-PQ的证明规模虽远小于格基方案，但仍大于Bulletproofs（约10×），这是追求后量子安全付出的代价。协议依赖随机预言模型，虽然具有RBR可靠性的IOP在量子ROM中仍安全，但实际实例化需要谨慎选择哈希函数。进一步的优化方向包括：通过更高效的多项式承诺方案（如利用特殊椭圆曲线或FRI的变体）来缩小常数因子；探索将SHARP-PQ与格基密码协议结合以支持更全面的隐私计算（如同时支持环签名和范围证明）。此外，当前实现未使用并行化，可挖掘性能提升空间。

### 强关联论文

[11] Bünz et al. Bulletproofs: Short proofs for confidential transactions and more. **IEEE S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Bulletproofs+Short+proofs+for+confidential+transactions+and+more)

[15] Lyubashevsky et al. Practical lattice-based zero-knowledge proofs for integer relations. **CCS 2020** [Google Scholar](https://scholar.google.com/scholar?q=Practical+lattice-based+zero-knowledge+proofs+for+integer+relations)

[16] Couteau et al. Efficient range proofs with transparent setup from bounded integer commitments. **EUROCRYPT 2021** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+range+proofs+with+transparent+setup+from+bounded+integer+commitments)

[17] Ben-Sasson et al. Aurora: Transparent succinct arguments for R1CS. **EUROCRYPT 2019** [Google Scholar](https://scholar.google.com/scholar?q=Aurora+Transparent+succinct+arguments+for+R1CS)

[18] Zhang et al. Transparent polynomial delegation and its applications to zero knowledge proof. **IEEE S&P 2020** [Google Scholar](https://scholar.google.com/scholar?q=Transparent+polynomial+delegation+and+its+applications+to+zero+knowledge+proof)

[21] Zhang et al. Ligerolight: Optimized IOP-based zero-knowledge argument for blockchain scalability. **IEEE TDSC 2024** [Google Scholar](https://scholar.google.com/scholar?q=Ligerolight+Optimized+IOP-based+zero-knowledge+argument+for+blockchain+scalability)

[22] Ames et al. Ligero: Lightweight sublinear arguments without a trusted setup. **CCS 2017** [Google Scholar](https://scholar.google.com/scholar?q=Ligero+Lightweight+sublinear+arguments+without+a+trusted+setup)

[27] Esgin et al. MatRiCT: Efficient, scalable and post-quantum blockchain confidential transactions protocol. **CCS 2019** [Google Scholar](https://scholar.google.com/scholar?q=MatRiCT+Efficient+scalable+and+post-quantum+blockchain+confidential+transactions+protocol)

[28] Esgin et al. MatRiCT+: More efficient post-quantum private blockchain payments. **IEEE S&P 2022** [Google Scholar](https://scholar.google.com/scholar?q=MatRiCT%2B+More+efficient+post-quantum+private+blockchain+payments)

[31] Ben-Sasson et al. Fast Reed–Solomon interactive oracle proofs of proximity. **ICALP 2018** [Google Scholar](https://scholar.google.com/scholar?q=Fast+Reed–Solomon+interactive+oracle+proofs+of+proximity)


## 关键词

+ SHARP-PQ后量子安全范围证明
+ 简洁哈希基础任意范围证明
+ 多对数证明大小零知识范围证明
+ 内积论证同态性优化
+ 后量子格基ZKRP改进
+ 批量范围证明可验证系统