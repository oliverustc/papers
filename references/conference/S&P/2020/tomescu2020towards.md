---
title: "Towards scalable threshold cryptosystems"
doi: 10.1109/sp40000.2020.00059
标题简称:
论文类型: conference
会议简称: S&P
发表年份: 2020
created: 2025-04-17 10:43:04
modified: 2025-04-17 10:43:50
---
## Towards scalable threshold cryptosystems

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/9152696)

## 作者

+ [[Alin Tomescu ]]
+ Robert Chen 
+ Yiming Zheng 
+ Ittai Abraham 
+ Benny Pinkas 
+ Guy Golan Gueta 
+ Srinivas Devadas 

## 笔记

### 背景与动机
拜占庭容错（BFT）系统的复兴对底层门限密码系统（如门限签名TSS、可验证秘密共享VSS、分布式密钥生成DKG）的可扩展性提出了严峻挑战。现有方案在参与者数量 n 较大时性能严重退化，尤其是在诚实多数假设（t > n/2）下，所有关键操作均呈现关于 n 的二次时间复杂度。具体而言，秘密重建依赖于朴素的多项式插值，其复杂度为Θ(t²)；VSS和DKG协议中的份额分发与验证涉及生成或验证 Θ(n) 个多项式评估证明，每个证明的计算需 Θ(t) 时间，导致总计算量为 Θ(nt)。这使得系统在处理数千甚至数万参与者时计算开销变得不可承受。本文旨在通过引入高效的多项式算法和新型承诺证明结构，打破这一二次瓶颈，将TSS、VSS和DKG的计算复杂度分别降低至拟线性级别，从而支持数十万乃至百万级别的参与规模。

### 相关工作

[10] Boldyreva. Threshold Signatures, Multisignatures and Blind Signatures Based on the Gap-Diffie-Hellman-Group Signature Scheme. **PKC 2003** [Google Scholar](https://scholar.google.com/scholar?q=Threshold%20Signatures%2C%20Multisignatures%20and%20Blind%20Signatures%20Based%20on%20the%20Gap-Diffie-Hellman-Group%20Signature%20Scheme)
> 核心思路：提出了基于BLS签名的门限签名方案，通过拉格朗日插值聚合签名份额。
> 局限与区别：该方案及所有现有实现均采用Θ(t²)的朴素拉格朗日插值，无法扩展到大的门限值t。本文通过快速拉格朗日插值将其降至Θ(t log² t)。

[14] Kate, Zaverucha, Goldberg. Constant-Size Commitments to Polynomials and Their Applications. **ASIACRYPT 2010** [Google Scholar](https://scholar.google.com/scholar?q=Constant-Size%20Commitments%20to%20Polynomials%20and%20Their%20Applications)
> 核心思路：提出了KZG多项式承诺方案，具有常数大小的承诺和验证证明，并以此构建了通信高效的VSS协议eVSS。
> 局限与区别：eVSS的计算瓶颈在于分发阶段需为n个参与者各生成一个KZG证明，总时间为Θ(nt)。本文通过认证多点求值树（AMT）将证明生成时间降至Θ(n log t)。

[17] Kate. Distributed Key Generation and Its Applications. **PhD Thesis 2010** [Google Scholar](https://scholar.google.com/scholar?q=Distributed%20Key%20Generation%20and%20Its%20Applications)
> 核心思路：基于KZG承诺构建了eJF-DKG协议，将每个参与者的广播消息压缩至常数大小。
> 局限与区别：eJF-DKG中每个玩家的分发阶段仍需Θ(nt)时间计算Θ(n)个KZG证明。本文通过AMT技术将其降低至Θ(n log t)。

[12] Pedersen. Non-Interactive and Information-Theoretic Secure Verifiable Secret Sharing. **CRYPTO 1991** [Google Scholar](https://scholar.google.com/scholar?q=Non-Interactive%20and%20Information-Theoretic%20Secure%20Verifiable%20Secret%20Sharing)
> 核心思路：提出了基于承诺的VSS方案，实现信息论隐藏和计算绑定，但分发广播需Θ(t)大小。
> 局限与区别：该方案在处理大规模参与者时，分发和验证阶段的计算复杂度均为Θ(nt)，不具可扩展性。

[16] Gennaro, Jarecki, Krawczyk, Rabin. Secure Distributed Key Generation for Discrete-Log Based Cryptosystems. **Journal of Cryptology 2007** [Google Scholar](https://scholar.google.com/scholar?q=Secure%20Distributed%20Key%20Generation%20for%20Discrete-Log%20Based%20Cryptosystems)
> 核心思路：提出了JF-DKG协议，解决了Pedersen DKG中恶意参与者无法被追责和潜在偏见的问题。
> 局限与区别：该协议中每个参与者的计算和通信开销均为Θ(nt)，不适用于大规模系统。

[47] Canny, Sorkin. Practical large-scale distributed key generation. **EUROCRYPT 2004** [Google Scholar](https://scholar.google.com/scholar?q=Practical%20large-scale%20distributed%20key%20generation)
> 核心思路：提出了一个基于稀疏矩阵的DKG协议，使每个参与者的复杂度降至Θ(log³ n)。
> 局限与区别：该协议依赖一个集中式“混洗者”来分配参与者，且仅支持接近一半的容错阈值。当容错需求接近n/2时，其分组大小会急剧增长，导致性能退化。

### 核心技术与方案

#### Ⅲ-A 可扩展的门限签名（Scalable Threshold Signatures）
本文首先聚焦于BLS门限签名聚合中的计算瓶颈——拉格朗日系数的计算。给定门限t和签名者集合T，聚合签名计算为$σ = \prod_{i\in T} σ_i^{\mathcal{L}_i^T(0)}$。朴素方法计算分母$D_i = \prod_{j\in T, j \neq i} (i - j)$需要Θ(t²)时间。

**核心优化**：利用多项式导数关系。定义$N(x) = \prod_{i\in T} (x - i)$，其导数$N'(x) = \sum_{i\in T} N_i(x)$，其中$N_i(x) = N(x)/(x-i)$。由于$N'(i) = D_i$，可以通过在Θ(t log² t)时间内完成的多点求值一次性计算所有$D_i$。具体步骤为：1) 通过“乘积树”在Θ(t log² t)时间内计算$N(x)$；2) 通过多项式微分在Θ(t)时间内计算$N'(x)$；3) 在Θ(t)时间内计算所有$N_i(0) = N(0)/(-i)$；4) 在Θ(t log² t)时间内通过多点求值计算所有$D_i = N'(i)$。最终，拉格朗日系数$\mathcal{L}_i^T(0) = N_i(0)/D_i$的计算总复杂度为Θ(t log² t)。

**进一步优化**：若使用单位根作为参与者ID（即$\{\omega_n^{i-1}\}$），多项式$N(x)$将变为$x^{|T|} + \dots$的形式，且$N'(x)$在单位根上的多点求值可通过一次快速傅里叶变换（FFT）完成，速度远快于通用的多点求值算法。

#### Ⅲ-B 认证多点求值树（AMT）
本文的核心贡献在于大幅加速KZG多项式承诺中评估证明的生成。在KZG中，证明多项式φ在点i上的评估值$φ(i)$需要计算商$q_i(x) = (φ(x) - φ(i))/(x-i)$，并承诺为$g^{q_i(τ)}$，单点成本为Θ(t)。为每个$i\in[n]$计算证明的总成本为Θ(nt)。

**AMT构造**：AMT基于多项式多点求值的分治树（见图1）。以树根开始，多项式φ除以全局累加器$a_ε(x)$（例如$(x-1)(x-2)...(x-n)$），得到商$q_ε$和余数$r_ε$。然后递归地，每个节点w的余数$r_w$被该节点的累加器$a_w$除，得到新的商$q_w$和余数$r_w$。最终，叶子节点的余数$r_{leak}$就是$φ(i)$。对于任意评估点i，存在一条从根到叶子的路径，且路径上所有节点w的商$q_w$和累加器$a_w$满足关系：
$φ(x) = φ(i) + \sum_{w\in path(i)} q_w(x) a_w(x)$。
**AMT证明与验证**：AMT证明$π_i$由路径上所有商的KZG承诺构成，即$\{g^{q_w(τ)}\}_{w\in path(i)}$。由于路径长度（即树高）为$\lfloor \log n \rfloor$，证明大小为Θ(log n)个群元素。验证者通过双线性对检查等式(3)：
$e(g^{φ(τ)}, g) \stackrel{?}{=} e(g^{φ(i)}, g) \prod_{w\in path(i)} e(g^{q_w(τ)}, g^{a_w(τ)})$。
**复杂度**：利用优化后的AMT（基于单位根），证明生成的计算时间为Θ(n log t)。这是因为在树中，只有当累加器度数小于等于φ的度数时，除法才有非零商，因此只需计算深度为Θ(log t)的子树。验证时间与路径长度成正比，为Θ(log t)。

#### Ⅲ-C 可扩展的VSS（AMT VSS）
基于AMT，本文提出了新的VSS协议AMT VSS。其与eVSS [14]的唯一区别在于：1) 份额在单位根上计算：$s_i = φ(ω_N^{i-1})$；2) 分发阶段，参与者接收到的不是常数大小的KZG证明，而是大小为Θ(log t)的AMT证明$π_i$。其余验证、投诉和重建协议流程与eVSS相同，但使用AMT证明进行验证。
**复杂度分析**：AMT VSS的分发时间从eVSS的Θ(nt)降至Θ(n log t)。验证时间从Θ(1)增至Θ(log t)。投诉和重建阶段的复杂度也有所增加，但本文通过若干优化（如KZG批处理证明用于投诉，以及重建时的备忘录化技术）控制了这些增加。总体而言，AMT VSS用分发阶段的大幅加速，换取了其他阶段的小幅性能下降，从而在整体端到端时间上实现了显著提升（见表I）。

#### Ⅲ-D 可扩展的DKG（AMT DKG）
本文将AMT VSS应用于eJF-DKG [17]的每个玩家，形成AMT DKG。每个玩家i扮演AMT VSS中的分发者，分发其多项式$f_i$的份额。
**同态性**：AMT证明具有同态性。对于两个多项式φ和ρ，它们在AMT中同一节点w的商承诺满足$g^{q_w^{(φ+ρ)}(τ)} = g^{q_w^{φ}(τ)} \cdot g^{q_w^{ρ}(τ)}$。这一性质使得在DKG的聚合阶段，玩家j可以将所有合格玩家i的份额$s_{i,j}$和AMT证明$π_{i,j}$分别聚合为一个最终的份额$s_j$和一个最终的AMT证明$π_j$。
**快速验证**：借助同态性，在最优情况下（所有份额有效），玩家j可以聚合所有份额和证明后仅用一个Θ(log t)时间的验证操作，大幅减少了昂贵的配对运算。在最坏或平均情况下，可以采用二叉树结构的批验证方案来定位无效份额，其复杂度与无效份额的数量b成正比，约为Θ(b log t)次配对运算。
**复杂度**：AMT DKG的分发时间从eJF-DKG的Θ(nt)降至Θ(n log t)。验证时间虽有所增加，但在最优情况下通过聚合仍可保持较低的配对运算次数。重建阶段可利用公开的$g^s$进行乐观重建。

### 核心公式与流程

**[快速拉格朗日系数计算]**
$$\mathcal{L}_i^T(0) = \frac{N_i(0)}{N'(i)}, \quad \text{where } N(x) = \prod_{i\in T} (x-i)$$
> 作用：这是快速计算拉格朗日系数的核心公式。通过计算多项式N(x)及其导数N'(x)，并分别在点0和所有需要评估的点上求值，可将计算复杂度从Θ(t²)降低到Θ(t log² t)。

**[AMT验证等式]**
$$e(C, g) = e(g^{y_i}, g) \prod_{w\in\mathsf{path}(i)} e(g^{q_w(\tau)}, g^{a_w(\tau)})$$
> 作用：这是验证AMT证明的核心等式。C是多项式φ的KZG承诺，$y_i = φ(i)$是评估值，$\{g^{q_w(τ)}\}$是AMT证明，$\{g^{a_w(τ)}\}$是公开的累加器承诺。该检查保证证明的可靠性，其安全性基于q-SBDH假设。

**[AMT VSS协议流程]**
1. **分发轮**：分发者秘密选择多项式φ，计算所有份额$s_i = φ(ω_N^{i-1})$，生成AMT证明π_i，并向所有玩家广播承诺$C = g^{φ(τ)}$，私密发送$(s_i, π_i)$给玩家i。
2. **验证轮**：每个玩家i使用AMT验证等式验证其份额，若无效则广播投诉。
3. **投诉轮**：分发者回应投诉，若有超过t个投诉则被撤除。
4. **重建阶段**：收集t个有效份额，通过拉格朗日插值恢复秘密。
> 作用：该流程展示了AMT VSS与eVSS的主要区别在于份额的定义方式和证明的结构，其余流程保持一致，从而能无缝替换核心组件。

**[AMT DKG协议流程]**
1. **分发轮**：每个玩家i(作为分发者)秘密选择多项式f_i，广播承诺及证明，私密发送份额给其他玩家。
2. **验证轮**：每个玩家j验证来自所有玩家的份额和证明。
3. **投诉轮**：玩家被投诉后需回应，否则被撤除。
4. **聚合**：所有未被撤除的玩家的承诺和份额进行同态聚合，形成最终的全局公钥、每个玩家的最终份额和对应的AMT证明。
> 作用：该流程将DKG的问题分解为多个VSS的子问题，并通过AMT证明的同态性使得最终聚合是可行的和高效的。

### 实验结果
实验在Intel Core i7-980X CPU、12核、20GB RAM的机器上进行，采用C++实现，底层使用254位BN曲线及Type III配对。所有测试针对诚实多数场景（t = f+1, n = 2f+1）进行。对于BLS门限签名，快速拉格朗日方案在n=511时首次超越朴素方案，在n≈2²¹时，聚合时间从1.59天降至46.26秒，加速约2964倍。对于VSS，AMT VSS在n=65536时，分发时间从15.1小时降至1.24分钟；端到端最佳时间从1.1小时降至51.48秒，最差时间从2.2天（外推值）降至约8分钟。对于DKG，AMT DKG在n=65536时，端到端最佳时间从1.16小时降至25.45秒，最差时间从2.4天（外推值）降至约4分钟。速度提升的代驾是通信开销略有增加，例如在DKG中，n=65536时，每个玩家的下载量从约430 MiB增至约1.6 GiB，但计算时间的节省远超通信成本的增加。

### 局限性与开放问题
本文工作存在若干局限性：所有协议均依赖一次可信设置来生成q-SDH公共参数，该设置可通过多方安全计算实现，但仍需预先完成。协议专注于同步通信模型，且未处理最坏情况下DKG投诉阶段的二次复杂度（O(t²)），将其扩展至可规模化的方式是未来工作。此外，实验评估未考虑实际的网络延迟，因此端到端时间的提升主要反映的是计算方面的收益，网络通信的瓶颈仍需在真实部署中验证。最后，AMT技术在任意点集上的应用、设计信息论隐藏版本的AMT以及利用AMT构建向量承诺等方向也具有探索价值。

### 强关联论文

[10] Boldyreva. Threshold Signatures, Multisignatures and Blind Signatures Based on the Gap-Diffie-Hellman-Group Signature Scheme. **PKC 2003** [Google Scholar](https://scholar.google.com/scholar?q=Threshold%20Signatures%2C%20Multisignatures%20and%20Blind%20Signatures%20Based%20on%20the%20Gap-Diffie-Hellman-Group%20Signature%20Scheme)

[12] Pedersen. Non-Interactive and Information-Theoretic Secure Verifiable Secret Sharing. **CRYPTO 1991** [Google Scholar](https://scholar.google.com/scholar?q=Non-Interactive%20and%20Information-Theoretic%20Secure%20Verifiable%20Secret%20Sharing)

[14] Kate, Zaverucha, Goldberg. Constant-Size Commitments to Polynomials and Their Applications. **ASIACRYPT 2010** [Google Scholar](https://scholar.google.com/scholar?q=Constant-Size%20Commitments%20to%20Polynomials%20and%20Their%20Applications)

[16] Gennaro, Jarecki, Krawczyk, Rabin. Secure Distributed Key Generation for Discrete-Log Based Cryptosystems. **Journal of Cryptology 2007** [Google Scholar](https://scholar.google.com/scholar?q=Secure%20Distributed%20Key%20Generation%20for%20Discrete-Log%20Based%20Cryptosystems)

[17] Kate. Distributed Key Generation and Its Applications. **PhD Thesis 2010** [Google Scholar](https://scholar.google.com/scholar?q=Distributed%20Key%20Generation%20and%20Its%20Applications)

[27] von zur Gathen, Gerhard. Fast polynomial evaluation and interpolation. **Modern Computer Algebra (3rd ed.) 2013** [Google Scholar](https://scholar.google.com/scholar?q=Fast%20polynomial%20evaluation%20and%20interpolation)

[47] Canny, Sorkin. Practical large-scale distributed key generation. **EUROCRYPT 2004** [Google Scholar](https://scholar.google.com/scholar?q=Practical%20large-scale%20distributed%20key%20generation)

[63] Boneh, Lynn, Shacham. Short Signatures from the Weil Pairing. **ASIACRYPT 2001** [Google Scholar](https://scholar.google.com/scholar?q=Short%20Signatures%20from%20the%20Weil%20Pairing)


## 关键词

+ 门限密码系统可扩展性
+ 分布式密钥生成（DKG）
+ 可验证秘密共享（VSS）
+ BLS门限签名
+ 多点多项式估值
+ 准线性复杂度