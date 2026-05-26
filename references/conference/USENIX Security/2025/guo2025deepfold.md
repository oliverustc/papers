---
title: "DeepFold: Efficient Multilinear Polynomial Commitment from Reed-Solomon Code and Its Application to Zero-knowledge Proofs"
标题简称:
论文类型: conference
会议简称: USENIX Security
发表年份: 2025

modified: 2025-06-09 10:35:01
created: 2025-05-13 09:23:43
---

## DeepFold: Efficient Multilinear Polynomial Commitment from Reed-Solomon Code and Its Application to Zero-knowledge Proofs

## 发表信息

+ 原文链接暂无
+ [archive](https://eprint.iacr.org/2024/1595)

## 作者

+ [Yanpei Guo](Yanpei%20Guo.md)
+ Xuanming Liu
+ Kexi Huang
+ Wenjie Qu
+ Tianyang Tao
+ [Jiaheng Zhang](Jiaheng%20Zhang.md)

## 笔记

### 背景与动机
零知识证明是密码学中极具实用价值的工具，广泛应用于区块链、AI监管和匿名凭证等领域。现代高效的zk-SNARK通常由多项式承诺方案（PCS）与多项式交互式预言机证明（PIOP）结合而成，其中多线性PCS（μ>1）更适用于表达复杂的算术电路。基于纠错码的PCS因无需可信设置且仅依赖轻量哈希函数而备受关注，但现有FRI-based多线性PCS存在明显瓶颈：BaseFold [48]虽然实现了最优的证明者时间，但由于其运作在唯一解码半径下，查询次数过多，导致证明尺寸高达619 KB（μ=22），相比之下，单变量的DEEP-FRI仅需约200 KB。此外，这些方案在处理任意长度输入时（如现实中非2的幂次的矩阵维度）存在严重的填充开销，例如在GPT-2的注意力矩阵（768×2304）场景下，填充可能导致近4倍的性能退化。因此，核心问题在于能否构建一个同时具备最优证明者效率、更小证明尺寸，并能高效处理任意长度输入的FRI-based多线性PCS。

### 相关工作

[5] Ben-Sasson 等. Fast Reed-Solomon Interactive Oracle Proofs of Proximity. **ECCC 2017** [Google Scholar](https://scholar.google.com/scholar?q=Fast+Reed-Solomon+Interactive+Oracle+Proofs+of+Proximity)
> 核心思路：提出了FRI协议，一个基于Reed-Solomon码的IOPP，具有多项式对数的验证时间。
> 局限与区别：原始FRI针对单变量多项式设计，无法直接用于多变量；本文将其作为子组件，并解决了在多线性情形下向列表解码半径过渡的问题。

[48] Zeilberger 等. Basefold: Efficient Field-Agnostic Polynomial Commitment Schemes from Foldable Codes. **CRYPTO 2024** [Google Scholar](https://scholar.google.com/scholar?q=Basefold%3A+Efficient+Field-Agnostic+Polynomial+Commitment+Schemes+from+Foldable+Codes)
> 核心思路：将FRI与多元sumcheck结合，构建了具有线性证明者时间的高效多线性PCS。
> 局限与区别：BaseFold只能在唯一解码半径下工作，导致查询次数多、证明尺寸大；本文通过引入DEEP技术将其推广到列表解码半径，实现了3倍证明尺寸缩减。

[10] Ben-Sasson 等. DEEP-FRI: Sampling Outside the Box Improves Soundness. **arXiv 2019** [Google Scholar](https://scholar.google.com/scholar?q=DEEP-FRI%3A+Sampling+Outside+the+Box+Improves+Soundness)
> 核心思路：提出了“域扩展消除伪装者（DEEP）”技术，将FRI的容错界限提升至列表解码半径，显著减少了查询次数。
> 局限与区别：DEEP-FRI是单变量PCS，其使用的“商”技术会破坏末轮标量等于随机评估的重要性质，导致无法直接用于构建多线性PCS；本文借鉴了其引入额外评估点（α_i）的思想，但提出了全新的校验方法避免了“商”技术。

[52] Zhang 等. Fast RS-IOP Multivariate Polynomial Commitments and Verifiable Secret Sharing. **USENIX Security 2024** [Google Scholar](https://scholar.google.com/scholar?q=Fast+RS-IOP+Multivariate+Polynomial+Commitments+and+Verifiable+Secret+Sharing)
> 核心思路：借鉴Gemini的思想，通过承诺额外的log n个多项式来实现线性时间的证明者。
> 局限与区别：这导致需要运行FRI近两次（相当于双倍开销），在证明者时间、验证者时间和证明尺寸上均比本文的DeepFold差约2倍。

[22] Golovnev 等. Brakedown: Linear-Time and Field-Agnostic SNARKs for R1CS. **CRYPTO 2023** [Google Scholar](https://scholar.google.com/scholar?q=Brakedown%3A+Linear-Time+and+Field-Agnostic+SNARKs+for+R1CS)
> 核心思路：基于张量码的线性证明者时间PCS，无需递归证明组合。
> 局限与区别：其验证时间慢且证明尺寸为O(λ√n)（λ为安全参数），在实践中远大于DeepFold的O(s_L log² n)证明尺寸。

### 核心技术与方案

**整体框架**  
DeepFold是一个基于Reed-Solomon码的透明多线性多项式承诺方案。其主要创新在于两点：一是在FRI协议中引入列表解码半径设置，大幅降低了查询次数从而缩小证明尺寸；二是提出了一种高效的批处理评估技术，用于处理任意长度的输入并实现了零知识性。

**技术一：从唯一解码半径向列表解码半径的过渡（核心挑战与解决方案）**  
BaseFold [48] 将FRI的末轮标量f^(μ)与多元多项式在随机点上的评估值 $\tilde{f}(r_1,...,r_\mu)$ 联系起来，从而构建了PCS。但其仅在唯一解码半径下工作，因为在此半径内，对于每个圆承诺的向量v^(i)，至多只有一个码字与之“接近”，故恶意证明者无法作弊。

向列表解码半径过渡的挑战在于：当允许的接近距离Δ大于(1-ρ)/2时，给定的v^(i)可能接近多个码字。恶意证明者可能在每一轮中挑选一个不同的码字，最终导出一个错误的末轮标量f^(μ)'，从而破坏方案的可靠性。

为解决此问题，DeepFold借鉴了DEEP-FRI [10] 的思想，在协议中引入额外的随机评估点α_i。具体地，在每一轮i中，验证者发送一个随机挑战α_i，并要求证明者提交多项式f^(i-1)在±α_i处的值。直觉上，即使存在多个码字在域L_i上“靠近”v^(i)，由于α_i是随机取自整个域F，这些码字在α_i^2处（由f^(i-1)(±α_i)导出）计算值不同的概率极高。因此，我们可以将向量v^(i)唯一地绑定到某个特定的多项式f^(i) ∈ List(v^(i), RS, Δ)。该性质在文中被形式化为Lemma 7。

**技术二：高效的深度折叠验证（避免使用“商”技术）**  
DEEP-FRI使用了一个“商”操作（公式3）来验证f^(i)(α_i^2)的值，但这会破坏末轮标量等于$\tilde{f}(r_1,...,r_\mu)$这一关键性质，使其不适用于BaseFold的框架。DeepFold提出了一个新颖的“深度折叠”方法。

核心思想是将对每个额外评估点{α_i}的正确性证明，递归地折叠到下一轮。假设在round i，需要校验f^(i-1)(±α_i)的正确性。通过一个数学恒等式（利用孪生多项式关系），验证者可以将这个校验转化为对f^(i)(α_i^2)的校验。具体地，f^(i-1)(±α_i) 等于 $\tilde{f}^{(i-1)}(±α_i, α_i^2, ..., α_i^{2^{μ-i}})$，由此可以推导出f^(i)(α_i^2) = $\tilde{f}^{(i)}(α_i^2, ..., α_i^{2^{μ-i}})$。在后续的第j轮（j>i）中，证明者额外发送f^(j-1)(-α_i^{2^{j-i}})等值，逐层校验。最终，所有这些校验都会收敛到对末轮标量f^(μ)（即$\tilde{f}(r_1,...,r_\mu)$）的检查，而这个值正是由FRI协议本身提供的。整个Eval协议的流程如图4所示，该过程并未显式地调用sumcheck，而是通过一种统一的折叠方式将原始的声明和DEEP评估的校验合并起来。

**安全性论证**  
DeepFold的binding性质（Theorem 4）依赖于列表解码半径下码字列表的多项式大小界限（Conjecture 1）。若存在两个不同的多项式p1, p2都与承诺向量够“近”，且它们在一个随机点α处的评估值相同，则这个概率是极小的（不超过poly(n)/|F|）。

DeepFold的soundness是Theorem 2的一个特例。该定理通过数学归纳法证明，在列表解码半径下，若恶意证明者通过协议的概率大于 $\text{poly}(|L_0|)/|\mathbb{F}| + (1-\Delta)^s$，则必然存在一系列多项式{$\tilde{p}_i$}满足所有声称的约束，且每个承诺的向量都与这些多项式足够接近。证明的核心是利用Lemma 7确保每个圆中向量到某一唯一码字的绑定，以及通过随机线性组合（γ_i）和折叠操作（r_i）传递错误容忍度，从而证明最终的声言是可提取的。

**批处理评估与零知识性**  
为了处理任意长度的输入（例如一个大小为 2^{2n} + 2^n 的向量），方案将其分解为两个不同大小（2n 和 n 变量）的多线性多项式 $\tilde{f}_1$ 和 $\tilde{f}_2$。核心技巧是在评估过程中，先将较大的多项式 $\tilde{f}_1$ 折叠到与较小多项式 $\tilde{f}_2$ 相同的变量数，然后在随后的轮中，将它们通过随机线性组合合并起来处理。这样，证明者的总计算复杂度和总多项式长度成线性关系，而证明尺寸和验证者时间与评估最大的单独多项式几乎相同。

零知识版本zkDeepFold的实现也依赖于批处理技术。方案通过将原始μ变量多项式扩展为一个(μ+1)变量多项式，并引入一个额外的ℓ变量随机多项式进行“掩码”。在评估协议的最后ℓ轮中，使用批处理技术将扩展多项式与随机多项式合并，从而隐藏关于原始多项式的信息。方案的模拟器通过随机选择多项式并匹配少量的查询结果来生成不可区分的脚本。

**复杂度分析**  
对于μ变量（n = 2^μ）的多线性多项式：  
- Commit 时间：O(n log n) 域运算 + O(n) 哈希。  
- Evaluate 时间：O(n) 域运算 + O(n) 哈希。  
- Proof Size 和 Verifier 时间：O(s_L · log² n)。其中s_L是列表解码半径下的查询次数。当码率ρ设置为1/8时，s_L ≈ 34，而BaseFold在唯一解码半径下的s_U > 120。这使得DeepFold的证明尺寸约为BaseFold的1/3。

### 核心公式与流程

**[孪生多项式定义]**
$$f(x) = \langle \vec{f}, (1, x, x^2, ..., x^{2^{\mu}-1}) \rangle, \quad \tilde{f}(x_1, ..., x_\mu) = \langle \vec{f}, (1, x_1) \otimes ... \otimes (1, x_\mu) \rangle$$
> 作用：建立了多线性多项式$\tilde{f}$与其单变量孪生多项式$f$之间的系数一一对应关系。这是将基于单变量RS码的FRI协议应用于多变量问题的基础。

**[FRI折叠公式]**
$$f^{(i-1)}(X) = f_E^{(i)}(X^2) + X \cdot f_O^{(i)}(X^2)$$
$$f^{(i)}(X) = f_E^{(i)}(X) + r_i \cdot f_O^{(i)}(X)$$
> 作用：FRI协议的核心，通过将一个多项式分解为偶次项部分 $f_E^{(i)}$ 和奇次项部分 $f_O^{(i)}$，再通过随机数 $r_i$ 重新线性组合，得到一个次数减半的新多项式 $f^{(i)}$。

**[DEEP技术中的折叠公式（未被DeepFold直接使用）]**
$$f^{(i)}(X) = \frac{(f_E^{(i)}(X) + r_i \cdot f_O^{(i)}(X)) - (f_E^{(i)}(\alpha_i^2) + r_i \cdot f_O^{(i)}(\alpha_i^2))}{X - \alpha_i^2}$$
> 作用：DEEP-FRI [10] 使用的公式。它通过引入一个“商”操作将额外评估点 $\alpha_i$ 的信息直接融入FRI的下一轮折叠中。DeepFold没有使用该公式，因为它会破坏末轮标量与原始多项式随机评估之间的等价关系。

**[DeepFold中的深度折叠验证（隐式核心逻辑）]**
$$f^{(i-1)}(\pm \alpha_i) = \tilde{f}^{(i-1)}(\pm \alpha_i, \alpha_i^2, ..., \alpha_i^{2^{\mu-i}})$$
$$f^{(i)}(\alpha_i^2) = \tilde{f}^{(i)}(\alpha_i^2, ..., \alpha_i^{2^{\mu-i}})$$
> 作用：这并非协议中显式的公式，而是其背后的逻辑。通过孪生多项式关系，将对 $f^{(i-1)}(\pm \alpha_i)$ 的验证，转化为对 $f^{(i)}(\alpha_i^2)$ 的验证。依此类推，最终所有对额外评估点 $\{\alpha_i\}$ 的校验都收敛于对末轮标量 $f^{(\mu)}$ 的检查。

**[批处理评估的随机合并公式]**
$$\tilde{p}^{(i)}(X_{[i+1:\mu]}) = \tilde{p}^{(i-1)}(r_i, X_{[i+1:\mu]}) + \gamma_i \cdot \tilde{p}_i(X_{[i+1:\mu]})$$
> 作用：批处理评估的核心。在协议的第i轮，当较大的多项式 $\tilde{p}^{(i-1)}$（来自原始声明的折叠）被折叠到与较小多项式 $\tilde{p}_i$（子多项式）相同的大小时，通过随机数 $\gamma_i$ 将它们线性组合成一个新的多项式 $\tilde{p}^{(i)}$，从而在后续轮中实现统一处理。

### 实验结果

**实验设置**  
全部实验基于Intel Xeon Platinum 8460Y+ (2 GHz) 处理器，190GB RAM，Ubuntu 22.04 LTS操作系统，无并行化，结果为10次平均值。所有基于RS码的方案（Virgo [51], PolyFRIM [52], BaseFold [48], DEEP-FRI [10]）共享同一个代码框架，使用 $F_{p^2}$（p = 2^61 - 1）域和 blake3 哈希函数。码率ρ设置为1/8，安全参数λ = 100 bits。其他方案使用其官方开源库实现。

**核心性能对比（μ = 22）**  
- 证明者时间（Commit + Evaluate）：DeepFold仅需16秒，是Virgo（~48秒）和Hyrax的3倍快，是mKZG（~85秒）的5倍快。当码率设为1/2时，证明者时间降至3秒，与Orion相当。
- 证明尺寸：DeepFold的304 KB是BaseFold（929 KB）的3倍小，与其理论分析一致。相比PolyFRIM（570 KB），有近2倍改进。mKZG的证明尺寸更小（~30 KB），但这是以需要可信设置和远大于DeepFold（6倍）的证明者时间为代价的。
- 验证者时间：DeepFold的验证者时间与PolyFRIM和BaseFold相比均有2-3倍的提升。

**应用性能对比**  
- zk-SNARKs: 在证明256个叶子的Merkle树知识时，将Virgo的PCS替换为DeepFold（Libra + DeepFold），证明者时间从83秒降至33秒（2.5倍快），证明尺寸235 KB与Virgo相似。对于HyperPlonk PIOP，使用DeepFold相比使用mKZG，证明者时间从2967秒降至826秒（3.6倍快），相比使用BaseFold，证明尺寸从1050 KB降至310 KB（3.3倍优化）。
- 可验证矩阵乘法: 在GPT-2模型的典型场景（768 × 2304矩阵）中，DeepFold的批处理技术相比“朴素填充”方法，实现了约2.4倍的证明者时间加速；相比“朴素打开”方法，实现了约3倍的验证者时间和证明尺寸优化。

### 局限性与开放问题
DeepFold虽然显著提升了性能，但其soundness严格依赖于Conjecture 1，该猜想虽被广泛接受，但尚未被严格证明。另外，尽管DeepFold的证明尺寸比BaseFold小得多，但与基于配对的方案（如mKZG）相比仍有一个数量级的差距，这可能在带宽极度敏感的场景下构成瓶颈。未来的工作包括将本文方案与更先进的RS-IOPP技术（如STIR [4]）结合以进一步减少查询次数，以及与工业项目（如Binius [19] 和 Jolt zkVM [41]）集成以验证其实际性能增益。

### 强关联论文

[4] Arnon 等. Stir: Reed-Solomon Proximity Testing with Fewer Queries. **CRYPTO 2024** [Google Scholar](https://scholar.google.com/scholar?q=Stir%3A+Reed-Solomon+Proximity+Testing+with+Fewer+Queries)

[5] Ben-Sasson 等. Fast Reed-Solomon Interactive Oracle Proofs of Proximity. **ECCC 2017** [Google Scholar](https://scholar.google.com/scholar?q=Fast+Reed-Solomon+Interactive+Oracle+Proofs+of+Proximity)

[10] Ben-Sasson 等. DEEP-FRI: Sampling Outside the Box Improves Soundness. **arXiv 2019** [Google Scholar](https://scholar.google.com/scholar?q=DEEP-FRI%3A+Sampling+Outside+the+Box+Improves+Soundness)

[18] Chen 等. HyperPlonk: Plonk with Linear-Time Prover and High-Degree Custom Gates. **EUROCRYPT 2023** [Google Scholar](https://scholar.google.com/scholar?q=HyperPlonk%3A+Plonk+with+Linear-Time+Prover+and+High-Degree+Custom+Gates)

[22] Golovnev 等. Brakedown: Linear-Time and Field-Agnostic SNARKs for R1CS. **CRYPTO 2023** [Google Scholar](https://scholar.google.com/scholar?q=Brakedown%3A+Linear-Time+and+Field-Agnostic+SNARKs+for+R1CS)

[35] Papamanthou 等. Signatures of Correct Computation. **TCC 2013** [Google Scholar](https://scholar.google.com/scholar?q=Signatures+of+Correct+Computation)

[47] Xie 等. Orion: Zero Knowledge Proof with Linear Prover Time. **CRYPTO 2022** [Google Scholar](https://scholar.google.com/scholar?q=Orion%3A+Zero+Knowledge+Proof+with+Linear+Prover+Time)

[48] Zeilberger 等. Basefold: Efficient Field-Agnostic Polynomial Commitment Schemes from Foldable Codes. **CRYPTO 2024** [Google Scholar](https://scholar.google.com/scholar?q=Basefold%3A+Efficient+Field-Agnostic+Polynomial+Commitment+Schemes+from+Foldable+Codes)

[51] Zhang 等. Transparent Polynomial Delegation and Its Applications to Zero Knowledge Proof. **S&P 2020** [Google Scholar](https://scholar.google.com/scholar?q=Transparent+Polynomial+Delegation+and+Its+Applications+to+Zero+Knowledge+Proof)

[52] Zhang 等. Fast RS-IOP Multivariate Polynomial Commitments and Verifiable Secret Sharing. **USENIX Security 2024** [Google Scholar](https://scholar.google.com/scholar?q=Fast+RS-IOP+Multivariate+Polynomial+Commitments+and+Verifiable+Secret+Sharing)


## 关键词

+ DeepFold多线性多项式承诺方案
+ 里德-所罗门码密码应用
+ FRI基多线性承诺优化
+ 列表解码半径设置
+ zk-SNARK证明者效率
+ 批量评估任意长度多项式