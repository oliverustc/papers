---
title: "ZKCPlus: Optimized Fair-exchange Protocol Supporting Practical and Flexible Data Exchange"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2021

modified: 2025-04-08 09:59:54
---

## ZKCPlus: Optimized Fair-exchange Protocol Supporting Practical and Flexible Data Exchange

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3460120.3484558)

## 作者

+ Yun Li
+ Cun Ye
+ Yuguang Hu
+ Ivring Morpheus
+ [Yu Guo](Yu%20Guo.md)
+ Chao Zhang
+ [Yupeng Zhang](Yupeng%20Zhang.md)
+ Zhipeng Sun
+ Yiwen Lu
+ Haodi Wang

## 笔记

### 背景与动机
公平交换是数字商品交易中的核心难题，理论证明在无可信第三方情况下强公平性不可实现 [45]。传统依赖中心化第三方的方案存在单点故障 [22] 和用户信息滥用 [20] 等风险。比特币区块链 [44] 的出现为去中心化公平交换提供了新契机，Gregory Maxwell 于 2011 年提出的零知识 contingent 支付 (ZKCP) 协议 [43] 首次实现了无需信任第三方的原子交换，其核心是通过哈希锁定、加密和零知识证明相结合，在区块链上完成数字商品与货币的公平交换。然而，ZKCP 在实际应用中面临三大瓶颈：第一，底层 Pinocchio/BCTV14 zkSNARK [7, 46] 需要可信设置生成公共参考字符串 (CRS)，与协议消除信任的初衷相悖，且证明密钥 (proving key) 大小随电路规模急剧增长，例如交易 16×16 数独解时已达 68 MB；第二，系统性能瓶颈在于卖方的证明生成（proving）时间，单次证明需 10-20 秒，而验证仅需 40 毫秒，但零知识证明的简洁性在 ZKCP 场景中优势有限，因为证明与线性大小的密文一同离线传输；第三，ZKCP 难以处理大规模数据的复杂谓词验证，例如在机器学习即服务 (MLaaS) 场景下交易卷积神经网络 (CNN) 模型，用 Groth16 zkSNARK [32] 为一个 Lenet-5 网络 [39] 生成一次推理证明需 45 分钟，且设置时间长达 1.5 小时，CRS 大小达 11 GB [41]。本文提出的 ZKCPlus 旨在解决上述问题，实现实用且灵活的大规模数据公平交换。

### 相关工作

[43] Maxwell 等. Zero Knowledge Contingent Payment. **Bitcoin Wiki 2011** [Google Scholar](https://scholar.google.com/scholar?q=Zero+Knowledge+Contingent+Payment)
> 核心思路：首个基于区块链的公平交换方案，利用 zkSNARK 和哈希锁定实现原子交换。
> 局限与区别：依赖可信设置、卖方证明开销大、难以处理复杂谓词。本文用 CP-NIZK 替换 zkSNARK，消除可信设置并提升证明效率。

[7] Ben-Sasson 等. Succinct Non-Interactive Zero Knowledge for a von Neumann Architecture. **USENIX Security 2014** [Google Scholar](https://scholar.google.com/scholar?q=Succinct+Non-Interactive+Zero+Knowledge+for+a+von+Neumann+Architecture)
> 核心思路：提出 Pinocchio/BCTV14 zkSNARK，实现常量大小证明和高效验证。
> 局限与区别：需可信设置，证明开销大。本文采用公共设置的 CP-NIZK 方案。

[32] Groth. On the Size of Pairing-Based Non-Interactive Arguments. **EUROCRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=On+the+Size+of+Pairing-Based+Non-Interactive+Arguments)
> 核心思路：优化 Pinocchio，进一步减小证明大小。
> 局限与区别：仍需可信设置，证明时间仍为瓶颈。本文在数据并行场景下提升证明效率。

[46] Parno 等. Pinocchio: Nearly Practical Verifiable Computation. **IEEE S&P 2013** [Google Scholar](https://scholar.google.com/scholar?q=Pinocchio+Nearly+Practical+Verifiable+Computation)
> 核心思路：提出首个实用的可验证计算方案。
> 局限与区别：与 BCTV14 类似，存在可信设置与证明效率问题。

[11] Bünz 等. Bulletproofs: Short Proofs for Confidential Transactions and More. **IEEE S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Bulletproofs+Short+Proofs+for+Confidential+Transactions+and+More)
> 核心思路：基于离散对数假设的短证明系统，无需可信设置。
> 区别：本文借鉴其递归归约技术，但针对数据并行电路做优化，并构建完整的 CP-NIZK 框架。

[31] Groth. Linear Algebra with Sub-Linear Zero-Knowledge Arguments. **CRYPTO 2009** [Google Scholar](https://scholar.google.com/scholar?q=Linear+Algebra+with+Sub-Linear+Zero-Knowledge+Arguments)
> 核心思路：提出基于向量内积的子线性零知识论证。
> 贡献：本文的 CP-NIZK 构建大量借鉴其内积论证与递归归约技术。

[49] Setty. Spartan: Efficient and General-Purpose zkSNARKs without Trusted Setup. **CRYPTO 2020** [Google Scholar](https://scholar.google.com/scholar?q=Spartan+Efficient+and+General-Purpose+zkSNARKs+without+Trusted+Setup)
> 核心思路：基于离散对数的非简洁型 zkSNARK，提供高效证明。
> 对比：本文方案的性能可与之媲美，但在可组合性和承诺重用方面更具优势。

[1] Albrecht 等. MiMC: Efficient Encryption and Cryptographic Hashing with Minimal Multiplicative Complexity. **ASIACRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=MiMC+Efficient+Encryption+and+Cryptographic+Hashing+with+Minimal+Multiplicative+Complexity)
> 核心思路：设计 ZK 友好的分组密码，算术电路友好。
> 贡献：本文采用 MiMC 在 CTR 模式下加密，大幅减少电路约束，提升证明效率。

[23] Dziembowski 等. FairSwap: How to Fairly Exchange Digital Goods. **ACM CCS 2018** [Google Scholar](https://scholar.google.com/scholar?q=FairSwap+How+to+Fairly+Exchange+Digital+Goods)
> 核心思路：用轻量级不当行为证明替代零知识证明，实现弱公平性。
> 区别：其链上验证成本随数据规模增长，不适用于大规模数据。本文提供强公平性，链上开销为常数。

[13] Campanelli 等. Zero-Knowledge Contingent Payments Revisited: Attacks and Payments for Services. **ACM CCS 2017** [Google Scholar](https://scholar.google.com/scholar?q=Zero-Knowledge+Contingent+Payments+Revisited+Attacks+and+Payments+for+Services)
> 核心思路：分析 ZKCP 中由买家生成 CRS 的安全漏洞，并提出 ZKCSP 概念。
> 贡献：本文注意到其指出的安全性问题，并采用无需可信设置的 CP-NIZK 予以规避。

### 核心技术与方案

**总体框架**：ZKCPlus 协议对 ZKCP 的核心修改在于用一个公共设置的 CP-NIZK 论证系统替换了原有的 zkSNARK。协议将数据交换分为“承诺(Commit)”、“验证(Validate)”、“交付(Deliver)”、“揭示(Reveal)”和“定案(Finalize)”五个阶段。卖方首先对数字商品 $\mathbf{x}$ 计算 Pedersen 承诺 [47] $c_{\mathbf{x}}$ 并公开。验证阶段用于证明 $\mathbf{x}$ 满足买方指定的谓词 $\phi$，交付阶段则证明密文 $\mathbf{z}$ 是由 $\mathbf{x}$ 和密钥 $k$ 正确加密得到。这种分离设计与 CP-NIZK 的可组合性使得复杂谓词可以模块化地逐步证明。

**核心模块：面向数据并行电路的 CP-NIZK 论证**：这是 ZKCPlus 最关键的构建。考虑一个由 $n$ 个相同子电路组成的并行电路，每个子电路大小为 $m$。传统方法是将整个 $n \times m$ 大小的电路编码为一个大 R1CS。本文的方法是利用子电路 R1CS（系数矩阵 $\mathbf{A}, \mathbf{B}, \mathbf{C} \in \mathbb{F}_p^{m \times m}$）并应用于 $n$ 个赋值。定义矩阵 $\mathbf{X} = [\mathbf{x}_1, \dots, \mathbf{x}_n] \in \mathbb{F}_p^{m \times n}$，电路满足关系可简洁地表示为 $\mathbf{AX} \circ \mathbf{BX} = \mathbf{CX}$。该协议本质上将一个大规模的并行 R1CS 问题递归地归约到一个单一的内积论证上，其核心技术借鉴自 [11, 31]。协议流程始于证明者对每行赋值 $\mathbf{v}_j$（长度为 $n$）进行 Pedersen 承诺 $V_j = \langle \mathbf{v}_j, \mathbf{G} \rangle + \nu_j \cdot H$。通过同态性质，验证者可以计算出 $\mathbf{a}_i, \mathbf{b}_i, \mathbf{c}_i$ 的承诺。随后，协议的挑战-响应阶段将 $m$ 个 Hadamard 积等式 $\mathbf{a}_i \circ \mathbf{b}_i = \mathbf{c}_i$ 转化为一个关于 $\mathbf{l}_i$ 和 $\mathbf{r}_i$ 向量内和的内积方程，并在多轮交互中递归地对向量列表进行折叠。最终，协议以一个简化的单向量内积论证结束，其中证明者发送最终的 $\mathbf{l}', \mathbf{r}'$ 及相应的盲因子，验证者通过检查承诺等式 $\operatorname{Check}(\mathrm{pp}, L', \mathbf{l}', \iota') \stackrel{?}{=} 1$, $\operatorname{Check}(\mathrm{pp}, R', \mathbf{r}' \circ \mathbf{y}_n^{-1}, \rho') \stackrel{?}{=} 1$, 和 $\operatorname{Check}(\mathrm{pp}, T', \langle \mathbf{l}', \mathbf{r}' \rangle, \tau') \stackrel{?}{=} 1$ 来完成验证。该协议完美完备，且在 DLOG 假设下拥有计算性 witness-extended emulation 和完美特殊诚实验证者零知识性。

**证明组合**：CP-NIZK 论证的关键特点是可组合性。本协议支持连词、析词和顺序组合。特别地，对于共享输入 $u$ 的两个论证，可以通过将它们分别引用共同的承诺 $c$ 来直接组合为连词论证。通过这类组合，ZKCPlus 可以模块化地构建复杂关系的证明，例如 CNN 推理过程中不同层（卷积层、ReLU、池化层）的计算，可以通过定义链接函数 $f$ 的中间论证 $\Pi_{\mathrm{link}}^{\mathrm{Com}}$ 来连接各层证明。

**效率特性**：本文 CP-NIZK 论证的证明大小约为 $m \cdot \mathbb{G} + 2n \cdot \mathbb{F}_p$（$m$ 为子电路大小，$n$ 为并行度），证明者的主要开销是 $mn$ 次群标量乘和 $O(mn)$ 次域乘法，验证者主要开销为 $m+n$ 次群标量乘和 $O(m+n)$ 次域乘法。如果结合 Bulletproofs 的优化技术，证明大小可进一步压缩。与 Groth16 和 SpartanDL 的渐进复杂度比较见表 2，该方案与 SpartanDL 性能相近，在可组合性上优势显著。

### 核心公式与流程

**[Pedersen 承诺]**
$$
\operatorname{Commit}(\mathrm{pp}, \mathbf{v}) \rightarrow (V, \nu), \text{ where } V = \langle \mathbf{v}, \mathbf{G} \rangle + \nu \cdot H.
$$
> 作用：在 ZKCPlus 中对数字商品 $\mathbf{x}$ 和密钥 $\mathbf{k}$ 进行同态承诺，为后续所有证明提供可公开验证的绑定对象。

**[交付阶段的核心关系]**
$$
\left\{
\begin{array}{c}
\mathbf{z} = \operatorname{Enc}_k(\mathbf{x}) \wedge \mathsf{H}(k) = h \text{ (or } \operatorname{Check}(\mathrm{pp}, c_{\mathbf{k}}, k \cdot \mathbf{1}, r_{\mathbf{k}}) = 1 \text{)} \\
\wedge \operatorname{Com.Check}(c_{\mathbf{x}}, \mathbf{x}, r_{\mathbf{x}}) = 1 \wedge \operatorname{Com.Check}(c_{\mathbf{k}}, \mathbf{k}, r_{\mathbf{k}}) = 1
\end{array}
\right\}.
$$
> 作用：定义交付阶段 CP-NIZK 论证 $\pi_z$ 需要证明的 NP 关系，强调承诺 $c_{\mathbf{x}}$ 是已存在的公开值。

**[数据并行 R1CS 的递归归约流程]**
$$
\begin{aligned}
\text{For } k &in [\log m ... 0]: \\
t_k^+ &= \sum_{i=1}^{2^k} \langle \mathbf{l}_i, \mathbf{r}_{i+2^k} \rangle, \quad t_k^- = \sum_{i=1}^{2^k} \langle \mathbf{l}_{i+2^k}, \mathbf{r}_i \rangle, \\
\mathbf{l}_i &\leftarrow u_k \cdot \mathbf{l}_i + u_k^{-1} \cdot \mathbf{l}_{i+2^k}, \quad \mathbf{r}_i \leftarrow u_k^{-1} \cdot \mathbf{r}_i + u_k \cdot \mathbf{r}_{i+2^k}.
\end{aligned}
$$
> 作用：通过递归归约，将 $2m$ 个内积方程的高阶汇总问题逐步压缩至单一向量对 $(\mathbf{l}, \mathbf{r})$，使证明效率与电路规模的对数相关。

**[压缩物化证明流程]**
$$
\begin{aligned}
\text{Final Round: } &\mathbf{l}' = \mathbf{l} + e \cdot \mathbf{l}_d, \quad \mathbf{r}' = \mathbf{r} + e \cdot \mathbf{r}_d \circ \mathbf{y}_n, \\
&\operatorname{Check}(\mathrm{pp}, L', \mathbf{l}', \iota') \stackrel{?}{=} 1, \quad \operatorname{Check}(\mathrm{pp}, R', \mathbf{r}' \circ \mathbf{y}_n^{-1}, \rho') \stackrel{?}{=} 1, \\
&\operatorname{Check}(\mathrm{pp}, T', \langle \mathbf{l}', \mathbf{r}' \rangle, \tau') \stackrel{?}{=} 1.
\end{aligned}
$$
> 作用：协议最终轮，通过验证还原后的 $\mathbf{l}'$ 和 $\mathbf{r}'$ 的 Pedersen 承诺及它们内积的承诺是否匹配，来确认电路整体满足性，实现零知识。

### 实验结果
实验在一台 Ubuntu 18.04 机器上进行，对比 ZKCP 和 ZKCPlus。在 “支付数独解” 应用中，ZKCPlus 的设置时间仅为 0.03 秒，CRS 大小为 1.02 MB；而 ZKCP 在 49×49 数独解时设置时间已达 322.54 秒，CRS 达 635.93 MB，且无法处理更大规模。在运行时长大头 “识别与交付” 阶段，对于 49×49 数独解，ZKCPlus 的卖方耗时仅约 1.8 秒，相比 ZKCP 的 124 秒实现了 21-67 倍的提升；ZKCPlus 还成功处理了最大 256×256（64 KB）的数独解，耗时约 35 秒。通信开销方面，虽然 ZKCPlus 的证明大小比 ZKCP 的常量证明大，但总体仍在线性增长的可接受范围内。在吞吐量测试中，对于 2 KB 数据，ZKCPlus 的吞吐量（2278 B/s）是 ZKCP（22 B/s）的 104 倍，且随数据规模对数增长。即使在相同加密方案（SHA256 流密码）下，ZKCPlus 的证明者常数也比 ZKCP 快大约 13 倍。在 “支付 CNN 模型” 应用中，对于一个 3 层 CNN（8620 参数），ZKCPlus 完成一轮推理证明和参数交付总时间约 2 秒；对于 VGG16 模型（约一千五百万参数），两阶段总耗时约 12.3 分钟。在 “支付 SQL 查询” 应用中，对 100,000 条记录的验证阶段耗时约 5.70 秒（卖方）和 0.77 秒（买方），交付阶段均在 1 秒以内。

### 局限性与开放问题
本文的主要局限性在于：CP-NIZK 的证明大小并非常数，对于需要极短通信的场景仍不够理想；协议的高度并行化要求限制了其在非数据并行谓词上的效率；对于交互式决策过程等非确定性计算，依然需要额外的适配层；目前的区块链网络（如 Ethereum）的 Gas 限制和延迟可能会对非常大型的数据交换构成挑战。未来的开放问题包括：将 ZKCPlus 与更高效的 GKR 协议结合以获得理论上最优的证明者时间，以及探索与透明且具后量子安全性的交互式神谕证明（如 Aurora, Fractal）的整合。

### 强关联论文

[7] Ben-Sasson 等. Succinct Non-Interactive Zero Knowledge for a von Neumann Architecture. **USENIX Security 2014** [Google Scholar](https://scholar.google.com/scholar?q=Succinct+Non-Interactive+Zero+Knowledge+for+a+von+Neumann+Architecture)

[11] Bünz 等. Bulletproofs: Short Proofs for Confidential Transactions and More. **IEEE S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Bulletproofs+Short+Proofs+for+Confidential+Transactions+and+More)

[31] Groth. Linear Algebra with Sub-Linear Zero-Knowledge Arguments. **CRYPTO 2009** [Google Scholar](https://scholar.google.com/scholar?q=Linear+Algebra+with+Sub-Linear+Zero-Knowledge+Arguments)

[32] Groth. On the Size of Pairing-Based Non-Interactive Arguments. **EUROCRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=On+the+Size+of+Pairing-Based+Non-Interactive+Arguments)

[46] Parno 等. Pinocchio: Nearly Practical Verifiable Computation. **IEEE S&P 2013** [Google Scholar](https://scholar.google.com/scholar?q=Pinocchio+Nearly+Practical+Verifiable+Computation)

[49] Setty. Spartan: Efficient and General-Purpose zkSNARKs without Trusted Setup. **CRYPTO 2020** [Google Scholar](https://scholar.google.com/scholar?q=Spartan+Efficient+and+General-Purpose+zkSNARKs+without+Trusted+Setup)

[1] Albrecht 等. MiMC: Efficient Encryption and Cryptographic Hashing with Minimal Multiplicative Complexity. **ASIACRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=MiMC+Efficient+Encryption+and+Cryptographic+Hashing+with+Minimal+Multiplicative+Complexity)

[43] Maxwell 等. Zero Knowledge Contingent Payment. **Bitcoin Wiki 2011** [Google Scholar](https://scholar.google.com/scholar?q=Zero+Knowledge+Contingent+Payment)

[23] Dziembowski 等. FairSwap: How to Fairly Exchange Digital Goods. **ACM CCS 2018** [Google Scholar](https://scholar.google.com/scholar?q=FairSwap+How+to+Fairly+Exchange+Digital+Goods)

[13] Campanelli 等. Zero-Knowledge Contingent Payments Revisited: Attacks and Payments for Services. **ACM CCS 2017** [Google Scholar](https://scholar.google.com/scholar?q=Zero-Knowledge+Contingent+Payments+Revisited+Attacks+and+Payments+for+Services)


## 关键词

+ 公平交换
+ 零知识证明
+ 数字商品交易
+ 非交互式知识论证
+ 区块链应用