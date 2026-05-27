---
title: "Ligero++: A New Optimized Sublinear IOP"
doi: 10.1145/3372297.3417893
标题简称: Ligero++
论文类型: conference
会议简称: CCS
发表年份: 2020

modified: 2025-04-08 09:58:35
---
## Ligero++: A New Optimized Sublinear IOP

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3372297.3417893)

## 作者

+ Rishabh Bhadauria
+ [Zhiyong Fang](Zhiyong%20Fang.md)
+ [Carmit Hazay](Carmit%20Hazay.md)
+ [Muthuramakrishnan Venkitasubramaniam](Muthuramakrishnan%20Venkitasubramaniam.md)
+ [Tiancheng Xie](Tiancheng%20Xie.md)
+ [Yupeng Zhang](Yupeng%20Zhang.md)

## 笔记

### 背景与动机
透明且亚线性的零知识证明系统在实际应用中至关重要，尤其是在云计算和区块链等场景，其中计算可能被外包给不可信方，而验证方需要确保计算正确性。这类系统的好处在于无需依赖公钥密码学、免去可信设置，并且能够抵抗已知的量子攻击。在现有的透明系统中，Ligero [5] 以极快的证明者性能著称，但其证明规模随电路规模呈平方根增长；而 Aurora [20] 则实现了与电路规模呈多项对数关系的证明长度，但证明者的计算时间显著更长。两者在性能上具有不可比较的优势，没有一方能同时达到最优的证明者时间和通信开销。Ligero++ 旨在填补这一空白，即通过一种新的组合结构，融合 Ligero 和 Aurora 的核心优势，构造一个在证明者效率和证明长度之间取得良好权衡的亚线性交互式预言机证明（IOP）。与以往直接选择其中一种方案不同，本文通过将 Ligero 的“折叠”思想与 Aurora 的低度测试内积论证相结合，首次实现了接近 Ligero 的证明者速度和接近 Aurora 的简洁证明大小。

### 相关工作

[5] Ames 等. Ligero: Lightweight Sublinear Arguments Without a Trusted Setup. **CCS 2017** [Google Scholar](https://scholar.google.com/scholar?q=Ligero+Lightweight+Sublinear+Arguments+Without+a+Trusted+Setup)
> 核心思路：基于MPC-in-the-head范式，将电路值编码成交错Reed-Solomon码，通过随机线性组合和列查询实现亚线性通信。
> 局限与区别：证明规模为O(√|C|)，在大型电路下通信开销较大。Ligero++利用内积论证替代其列一致性检查，将通信降为多对数级。

[20] Ben-Sasson 等. Aurora: Transparent Succinct Arguments for R1CS. **EUROCRYPT 2019** [Google Scholar](https://scholar.google.com/scholar?q=Aurora+Transparent+Succinct+Arguments+for+R1CS)
> 核心思路：基于Reed-Solomon码的低度测试和uni-variate sumcheck，实现多对数通信的IOP。
> 局限与区别：证明者时间正比于码率的倒数，导致证明者开销远大于Ligero。Ligero++将内积论证约束于小规模列上，大幅降低证明者时间。

[55] Zhang 等. Transparent Polynomial Delegation and Its Applications to Zero Knowledge Proof. **S&P 2020** [Google Scholar](https://scholar.google.com/scholar?q=Transparent+Polynomial+Delegation+and+Its+Applications+to+Zero+Knowledge+Proof)
> 核心思路：提出基于Aurora的内积论证（IPA），可实现O(log² n)的证明规模。
> 局限与区别：IPA直接用于全电路时证明者开销大。Ligero++将IPA作为子模块嵌入Ligero框架，仅在小规模列上运行IPA，显著提升效率。

[32] Giacomelli 等. ZKBoo: Faster Zero-Knowledge for Boolean Circuits. **USENIX Security 2016** [Google Scholar](https://scholar.google.com/scholar?q=ZKBoo+Faster+Zero+Knowledge+for+Boolean+Circuits)
> 核心思路：基于MPC-in-the-head，通过重复整个证明降低soundness。
> 局限与区别：证明规模线性于电路规模，且不追求亚线性。Ligero++借鉴其重复证明的策略实现后量子签名实例化。

[42] Katz 等. Improved Non-Interactive Zero Knowledge with Applications to Post-Quantum Signatures. **CCS 2018** [Google Scholar](https://scholar.google.com/scholar?q=Improved+Non+Interactive+Zero+Knowledge+with+Applications+to+Post+Quantum+Signatures)
> 核心思路：使用预处理MPC优化ZKBoo，得到Picnic2签名方案。
> 局限与区别：仍属线性通信。Ligero++通过矩阵折叠实现更优的签名规模与验签速度。

[14] Ben-Sasson 等. Scalable Zero Knowledge with No Trusted Setup. **CRYPTO 2019** [Google Scholar](https://scholar.google.com/scholar?q=Scalable+Zero+Knowledge+with+No+Trusted+Setup)
> 核心思路：使用FRI协议实现可扩展的透明IOP（Stark）。
> 局限与区别：证明者时间仍显著高于Ligero，且适用于不同计算模型。Ligero++的证明者时间更接近Ligero。

[55] Zhang 等. (同上)
> 核心思路：同上。
> 局限与区别：同上。

### 核心技术与方案
Ligero++ 的整体框架基于 Ligero [5] 协议，其核心思想是将电路计算值编码成交错Reed-Solomon码矩阵，通过随机线性组合和列查询来验证矩阵编码的正确性以及电路约束的满足性。与 Ligero 不同的是，本文用内积论证（IPA）[55] 替代了原本直接发送列向量的方式，从而将列一致性检查的通信量从 O(t·m) 降低到 O(polylog m)，其中 m 是行数，t 是查询列数。

协议分为四个主要模块：交错线性码测试、线性约束测试、二次约束测试以及整体零知识证明。

在交错线性码测试（Protocol 1）中，验证方首先发送一个随机向量 r ∈ F^m，证明方计算 w = r^T·U 并发送，其中 U 是 m×n 的矩阵。验证方检查 w 是否属于 Reed-Solomon 码 L。随后，验证方随机选取一个大小为 t 的列索引子集 Q。对于每个 j∈Q，证明方和验证方执行一个IPA协议，证明 ⟨U[j], r⟩ = w_j，其中 U[j] 是矩阵的第 j 列，r 是公共向量。该协议的正确性基于 Reed-Solomon 码的纠错性质以及 IPA 的完备性。其可靠性的形式化证明通过分析两种情形完成：若矩阵 U 远离交错码（距离大于 e），则 w 也远离码的概率高，所有 t 个查询点均落在正确位置的概率至多为 (1 - e/n)^t；若矩阵 U 接近码但编码的消息不满足约束，则 w 是有效码字的概率至多为 d/|F|；再加上IPA的soundness误差 δ，总 soundness 误差不超过 (1 - e/n)^t + d/|F| + δ。

线性约束测试（Protocol 2）和二次约束测试（Protocol 3）采用了类似的结构：验证方发送随机线性组合向量，证明方发送一个组合多项式，验证方在插值点上检查约束是否满足，再通过随机列查询和IPA协议验证组合多项式的正确性。对于线性约束 Ax = 0，证明方发送多项式 q(·) = Σ_i a_i(·)·p_i(·)，验证方检查 Σ_j q(ζ_j) = 0，其中 a_i 是 r^T·A 的行多项式，p_i 是矩阵 U 的行多项式。对于二次约束 x⊙y - z = 0，证明方发送 q(·) = Σ_i r_i·(p_i^x(·)·p_i^y(·) - p_i^z(·))，验证方检查所有插值点上的值均为零。两者的可靠性均依赖于 Reed-Solomon 码的近距离码唯一性以及IPA的soundness。

整体协议（Protocol 5）将上述三个模块组合：证明方首先将电路导线值 w 编码成矩阵 U^w，并生成 x, y, z 对应的编码矩阵。首先验证这些矩阵是有效交错码；然后验证加法约束 P_add·w = 0；最后验证乘法约束，通过 IPA 证明 x, y, z 分别是 w 的线性变换（即 x = P_x·w 等）并通过二次测试验证 z = x⊙y。最终 soundness 误差为 (d+2)/|F| + (1 - e/n)^t + 2((e+2k)/n)^t + 3δ。通信复杂度方面，证明者计算量为 O(|C| log |C|)，证明规模为 O(polylog |C|)，验证者计算量为 O(|C|)。

为了实现零知识，协议6-8在矩阵中附加随机行（如Protocol 6在U中附加随机码字 u'），并增加RS码的度数或使用零知识IPA，使得线性组合和列查询不泄露关于实际证人的信息。

### 核心公式与流程

**[交错线性码测试协议 (Protocol 1)]**
$$
\begin{array}{l}
\text{输入: 矩阵 } U \in \mathbb{F}^{m \times n}, \text{ RS码 } L \subset \mathbb{F}^n \\
\text{1. } \mathcal{V} \text{ 生成随机向量 } r \in \mathbb{F}^m \text{ 并发送给 } \mathcal{P} \\
\text{2. } \mathcal{P} \text{ 计算 } w = r^T U \in \mathbb{F}^n \text{ 并发送} \\
\text{3. } \mathcal{V} \text{ 检查 } w \in L \\
\text{4. } \mathcal{V} \text{ 生成随机集 } Q \subseteq [n], |Q| = t \text{ 并发送} \\
\text{5. } \forall j \in Q: \mathcal{P} \text{ 和 } \mathcal{V} \text{ 执行IPA协议证明 } \langle U[j], r \rangle = w_j
\end{array}
$$
> 作用：检验矩阵U的每一行是否均为RS码中的码字（即U是交错码）。IPA替代了Ligero中的直接列发送，将列通信量从O(t·m)降为O(polylog m)。

**[线性约束测试协议 (Protocol 2) - 核心方程]**
$$
q(x) = \sum_{i=1}^m a_i(x) \cdot p_i(x), \quad \text{验证: } \sum_{j=1}^\ell q(\zeta_j) = 0
$$
> 作用：验证编码消息x满足线性约束Ax=0。a_i为随机组合后行多项式，p_i为U的行多项式。IPA用于验证q(·)与U的列一致性。

**[二次约束测试协议 (Protocol 3) - 核心方程]**
$$
q(\cdot) = \sum_{i=1}^m r_i \cdot \big( p_i^x(\cdot) p_i^y(\cdot) - p_i^z(\cdot) \big), \quad \forall j \in [\ell]: q(\zeta_j)=0
$$
> 作用：验证编码消息x,y,z满足x⊙y - z = 0。IPA用于检验列一致性，避免发送整列。

**[最终soundness误差 (Theorem 3.7)]**
$$
(d+2)/|\mathbb{F}| + (1 - e/n)^t + 2\big((e+2k)/n\big)^t + 3\delta
$$
> 作用：量化整体协议被恶意证明者欺骗的概率上界，其中e为距离阈值，d为码最小距离，k为消息长度，δ为IPA的soundness误差。

### 实验结果
实验在一块AMD Ryzen™ 3800X处理器（64GM RAM）上运行，使用单核，未并行化。基准测试为Merkle树路径验证，使用SHA-256哈希（每哈希约27,000个R1CS约束）。对于包含约2^22个约束的电路（128个哈希），Ligero++的证明者时间为82秒，较Ligero慢约2.3×（34秒），但比Aurora快11-12×（1004秒）。证明大小为184KB，优于Ligero的6MB和Aurora的276KB。验证者时间为18秒，与Aurora持平，比Ligero慢约3×。与Stark相比，证明者快2-3×，但验证者时间Stark仅需数十毫秒（因采用不同计算模型）。与Virgo相比，Ligero++在多项式承诺场景中证明者快1.7-2.1×，验证者慢2-3.6×，证明大小在多项式较小时约为Virgo的1/2，较大时略大。对于SIMD应用如线性回归（n=2000数据点，d=100特征），Ligero++的证明者时间为12,388秒，验证者时间仅1.1秒（因约束高度重复），证明大小257KB；而在批验证ECDSA签名场景（n=64签名、每签名32,768约束）中，验证者时间0.23秒已优于直接验签。后量子签名实例中，使用MiMC的签名方案签名时间42ms，验签8ms，签名大小210KB，与Picnic系列相当或部分更优。

### 局限性与开放问题
本文的验证者时间仍为线性O(|C|)，在超大规模计算（如2^28约束）下验证者需约1秒，虽较Ligero略慢但远慢于Stark的毫秒级，表明亚线性验证场景（如GKR类协议）仍具优势。协议的安全性依赖于对FRI协议强度的猜想（如Conjecture 1.5 in [12]），若仅依赖可证明安全参数，需要将IPA重复参数加倍，导致通信开销增大。IPA作为子模块引入的log² n通信在列数极小时优势不明显，如何进一步压缩常数因子、尤其优化小电路场景下的整体性能，是值得探索的方向。

### 强关联论文

[5] Scott Ames, Carmit Hazay, Yuval Ishai, and Muthuramakrishnan Venkitasubramaniam. Ligero: Lightweight Sublinear Arguments Without a Trusted Setup. **CCS 2017** [Google Scholar](https://scholar.google.com/scholar?q=Ligero+Lightweight+Sublinear+Arguments+Without+a+Trusted+Setup)

[20] Eli Ben-Sasson, Alessandro Chiesa, Michael Riabzev, Nicholas Spooner, Madars Virza, and Nicholas P. Ward. Aurora: Transparent Succinct Arguments for R1CS. **EUROCRYPT 2019** [Google Scholar](https://scholar.google.com/scholar?q=Aurora+Transparent+Succinct+Arguments+for+R1CS)

[55] Jiaheng Zhang, Tiancheng Xie, Yupeng Zhang, and Dawn Song. Transparent Polynomial Delegation and Its Applications to Zero Knowledge Proof. **S&P 2020** [Google Scholar](https://scholar.google.com/scholar?q=Transparent+Polynomial+Delegation+and+Its+Applications+to+Zero+Knowledge+Proof)

[32] Irene Giacomelli, Jesper Madsen, and Claudio Orlandi. ZKBoo: Faster Zero-Knowledge for Boolean Circuits. **USENIX Security 2016** [Google Scholar](https://scholar.google.com/scholar?q=ZKBoo+Faster+Zero+Knowledge+for+Boolean+Circuits)

[42] Jonathan Katz, Vladimir Kolesnikov, and Xiao Wang. Improved Non-Interactive Zero Knowledge with Applications to Post-Quantum Signatures. **CCS 2018** [Google Scholar](https://scholar.google.com/scholar?q=Improved+Non+Interactive+Zero+Knowledge+with+Applications+to+Post+Quantum+Signatures)

[14] Eli Ben-Sasson, Iddo Bentov, Yinon Horesh, and Michael Riabzev. Scalable Zero Knowledge with No Trusted Setup. **CRYPTO 2019** [Google Scholar](https://scholar.google.com/scholar?q=Scalable+Zero+Knowledge+with+No+Trusted+Setup)

[27] Melissa Chase, David Derler, Steven Goldfeder, Claudio Orlandi, Sebastian Ramacher, Christian Rechberger, Daniel Slamanig, and Greg Zaverucha. Post-Quantum Zero-Knowledge and Signatures from Symmetric-Key Primitives. **CCS 2017** [Google Scholar](https://scholar.google.com/scholar?q=Post+Quantum+Zero+Knowledge+and+Signatures+from+Symmetric+Key+Primitives)


## 关键词

+ 零知识证明
+ 交互式预言证明
+ 无可信设置
+ 后量子密码学
+ 证明大小优化