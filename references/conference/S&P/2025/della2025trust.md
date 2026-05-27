---
title: "Trust nobody: Privacy-preserving proofs for edited photos with your laptop"
doi: 10.1109/sp61157.2025.00014
标题简称:
论文类型: conference
会议简称: S&P
发表年份: 2025
---
## Trust nobody: Privacy-preserving proofs for edited photos with your laptop

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/11023375)

## 作者

+ Pierpaolo Della Monica 
+ Ivan Visconti 
+ Andrea Vitaletti 
+ Marco Zecchini 


## 笔记

### 背景与动机
数字图像市场（如 Getty Images、Shutter Stock）中，所有者通常将高分辨率原始图像 $I$ 付费出售，同时发布一个经过特定变换（如缩放、模糊、裁剪）的低分辨率版本 $\hat{I}$。买家需要验证 $\hat{I}$ 确实是由某个作者（由公钥 $\mathsf{pk}$ 标识）拥有的私密图像 $I$ 经过宣称的变换得到的（真实性），同时不能泄露 $I$ 的额外信息（保密性）。C2PA 联盟通过规定数字签名（如 ECDSA with SHA256）来保证相机拍摄照片的源头真实性，但其对编辑软件签名的依赖引入了易被攻击的第三方信任点 [1]。Datta 和 Boneh [1] 以及 Kang 等人 [2] 利用零知识简洁非交互知识论证（ZK-snark）在隐私保护下验证编辑，但这要求对原始图像的哈希（尤其是 C2PA 规定的 SHA256）的前像进行证明，导致证明计算极为昂贵，通常需要云端服务器或昂贵硬件，这又折损了保密性同时增加了成本。本文旨在解决这一开放问题：在不依赖可信第三方的前提下，允许图像拥有者使用普通笔记本电脑，为高分辨率图像生成满足真实性、保密性、快速验证（及快速欺诈证明）的变换证明，并且能与 C2PA 标准兼容。

### 相关工作

[1] Datta 等. Using ZK-proofs to fight disinformation. **RWC 2023** [Google Scholar](https://scholar.google.com/scholar?q=Using+ZK-proofs+to+fight+disinformation)
> 核心思路：使用 ZK-snark 证明图像变换的正确性。
> 局限与区别：证明计算需要云端基础设施，且哈希函数被替换为了 ZK-friendly 的 Lattice Hash 和 Poseidon Hash，偏离了 C2PA 标准。

[2] Kang 等. zk-img: Attested images via zero-knowledge proofs to fight disinformation. **arXiv 2022** [Google Scholar](https://scholar.google.com/scholar?q=zk-img+Attested+images+via+zero-knowledge+proofs+to+fight+disinformation)
> 核心思路：类似 [1]，使用 Poseidon Hash 替代 SHA256 以实现 ZK-snark。
> 局限与区别：对HD图像的处理需要 70.7 GB RAM 和 64 vCPU 的 AWS 实例，无法在普通硬件上运行，且不支持 C2PA 规范。

[3] Naveh 等. Photoproof: Cryptographic image authentication for any set of permissible transformations. **IEEE S&P 2016** [Google Scholar](https://scholar.google.com/scholar?q=Photoproof+Cryptographic+image+authentication+for+any+set+of+permissible+transformations)
> 核心思路：首次提出基于证明的图像认证系统。
> 局限与区别：定义中只处理非自适应敌手，且证明计算效率较低。

[12] Datta 等. VerITAS: Verifying image transformations at scale. **Cryptology ePrint Archive 2024** [Google Scholar](https://scholar.google.com/scholar?q=VerITAS+Verifying+image+transformations+at+scale)
> 核心思路：扩展了 [1] 的工作。
> 局限与区别：同上，仍依赖于昂贵硬件。

[13] Li 等. Region-aware photo assurance system for image authentication. **IEEE MIPR 2023** [Google Scholar](https://scholar.google.com/scholar?q=Region-aware+photo+assurance+system+for+image+authentication)
> 核心思路：注意到变换仅影响小区域，在单块子图上使用 ZK-snark。
> 局限与区别：全局变换（如灰度化）需处理整个图像，性能无提升。

### 核心技术与方案
本文通过“分块（tiling）”技术解决 ZK-snark 证明计算中的内存和计算瓶颈。将一个高分辨率原始图像 $I$ 分割成 $n$ 个非重叠的瓦片 $T_1^I, \ldots, T_n^I$。由于 ZK-snark 的计算复杂度与输入（即瓦片）大小成正比，通过选择合适的瓦片大小（例如实验中每个瓦片约 18 万像素），可以使每个子证明的计算在 4 GB 内存和普通 CPU 上完成。为了在分块后仍能保证原始图像的整体签名是可验证的，作者设计了一个名为 ImageSign 的特制签名方案。该方案在签名时，首先对每个瓦片 $T_j^I$ 使用 PRF 生成的随机数 $r_j$ 计算基于 Poseidon 哈希的承诺 $c_j = \texttt{Commit}_{\mathfrak{p}}(T_j^I, r_j)$，然后将所有承诺 $c_1,\ldots,c_n$ 作为叶子构建一棵默克尔树（MT），最后使用 ECDSA 对默克尔根 `root` 进行签名。完整的签名 $\sigma = (\sigma_{\text{ECDSA}}, \text{seed})$。该方案的关键点是：证明生成过程只需从每个瓦片出发，构造该瓦片的 ZK-snark 子证明 $\pi_j$，证明隐藏的 $T_j^I$ 承诺在 $c_j$ 中，且经变换 $f_j^L$ 得到下游瓦片 $\hat{T}_j^I$。整个证明 $\pi$ 包含 $\sigma_{\text{ECDSA}}$、根 `root`、所有默克尔路径 $B_j$ 和所有子证明 $\pi_j$。验证者只需对每个子证明独立验证，并最终验证默克尔路径和 ECDSA 签名。对于 C2PA 兼容的 TilesProof-C2PA 构造，将每个瓦片视为 SHA256 的一个或几个输入块（512 bit），分别证明每个块的 SHA-256Compression 函数的正确执行，从而避免直接证明整个 SHA256 大前像。安全性方面，TilesProof-MT 被证明满足适应性知识证明（Proof of Knowledge, PoK）和图像不可区分性（Image Indistinguishability, ImInd）。证明依赖于：基于随机预言机的签名方案 O-snark 友好性 [18]；子 ZK-snark 的知识可靠性；ECDSA 的不可伪造性；承诺方案的隐藏性和绑定性；默克尔树的碰撞抵抗性。TilesProof-C2PA 在 PoK 方面退化为非适应性（即敌手不能进行在线签名查询），但仍满足 ImInd。欺诈证明非常紧凑：只需指出是 ECDSA 签名错误、某个默克尔路径错误、还是某个子 ZK-snark 无效，验证一个分量仅需常数时间。

### 核心公式与流程

**[ImageSign 签名算法 (Alg. 1)]**
$$T_{1}^{I}, \cdots, T_{n}^{I} \gets \text{getTiles}(I, n);\quad seed \gets \{0, 1\}^{\lambda}$$
$$r_{j} \leftarrow PRF(seed, j);\quad c_{j} \leftarrow \text{Commit}_{\mathfrak{p}}(T_{j}^{I}, r_{j})$$
$$(MT, root) \leftarrow \text{Build}_{\text{MerkleTree}}(c_{1}, ..., c_{n})$$
$$\sigma_{ECDSA} \leftarrow \text{Sign}_{\text{ECDSA}}(\text{sk}, root)$$
$$\sigma \leftarrow (\sigma_{ECDSA}, seed)$$
> 作用：为一个图像 $I$ 生成特制签名 $\sigma$，其中将图像分块，对每个块计算隐藏承诺，通过默克尔树聚合，再对树根签名。

**[ZK-snark 子证明关系 (TilesProof-MT)]**
$$R_j\big((f_j^L, \hat{T}_j^I, c_j), (r_j, T_j^I)\big) = 1 \quad \text{iff} \quad (c_j = \text{Commit}_{\mathfrak{p}}(T_j^I, r_j) \land \hat{T}_j^I = f_j^L(T_j^I))$$
> 作用：定义每个瓦片 $j$ 的子证明关系：证明承诺 $c_j$ 是对原始块 $T_j^I$ 和随机数 $r_j$ 的承诺，且局部变换 $f_j^L$ 应用于 $T_j^I$ 后得到 $\hat{T}_j^I$。

**[欺诈证明 (Fraud Proof)]**
$$\pi_{\mathsf{FP}} \in \{\, 1,\ (2, j),\ (3, j)\,\} $$
- $1$: ECDSA 签名失败
- $(2, j)$: 第 $j$ 个默克尔路径验证失败
- $(3, j)$: 第 $j$ 个子 ZK-snark 验证失败
> 作用：欺诈证明非常紧凑，只需一个整数/元组，因为只需指出证明 $\pi$ 中具体哪个组件失效。其验证时间等价于验证该单个组件的代价。

**[TilesProof-C2PA 子证明关系]**
$$R_j\big((f_j^L, \hat{T}_j^I, z_j, z_{j-1}), (T_j^I, s_j, s_{j-1}, r_j, r_{j-1})\big) = 1 \quad \text{iff} \quad$$
$$\big(s_j = \text{SHA-256Subroutine}(T_j^I, s_{j-1})\big) \land \big(z_{j-1} = \text{Commit}_{\mathfrak{p}}(s_{j-1}, r_{j-1})\big) \land \big(z_j = \text{Commit}_{\mathfrak{p}}(s_j, r_j)\big) \land \big(\hat{T}_j^I = f_j^L(T_j^I)\big)$$
> 作用：定义 TilesProof-C2PA 中每个瓦片 $j$ 的子证明关系，其中 $s_j$ 是 SHA256 经过该瓦片后的中间状态，$z_{j-1}$, $z_j$ 分别为输入输出状态的承诺。这允许将 SHA256 的证明分块进行。

### 实验结果
实验在配备 Intel Core i7-8565U（1.80GHz，8核）和 16 GB RAM 的普通笔记本上进行，实际用于证明的内存约 4 GB。变换类型包括双线性缩放（resize）、灰度化和矩形裁剪。对于 TilesProof-MT 方案：单瓦片处理时间在 18.9 秒（缩放）到 25.7 秒（灰度化）之间，内存占用 3.4 - 4.5 GB。每个瓦片的 ZK-snark 证明大小为约 800 字节。对于 30 MP 图像（6000×4000 像素），若分为 130 个瓦片，总证明生成时间约 41 分钟，证明总大小约 108 KB。对于 TilesProof-C2PA 方案：由于 SHA256 非 ZK-friendly，单瓦片大小必须压缩至 2666 像素，但运行时间与 TilesProof-MT 相近（约 18 秒/瓦片），但瓦片数大幅增加——对于 30 MP 图像需要 9003 个瓦片，总证明时间约 45.2 小时，总大小约 7.4 MB。与 Kang 等人 [2] 的对比显示，本文方案在 HD 图像（1280×720 像素）上使用远更低的硬件（3.4 GB vs. 70.7 GB）却实现了更快的证明生成时间（94.5 秒 vs. 328.2 秒）。即使 TilesProof-C2PA 也能在 4.2 GB 内存下完成任务，而 [2] 在该硬件上无法运行。通过使用 SnarkPack [9] 聚合证明，可将 9003 个 Groth16 证明的验证时间压缩至约 58 ms。

### 局限性与开放问题
尽管 TilesProof-C2PA 兼容 C2PA 标准，但其证明生成时间（对 30 MP 图像需 45 小时）对于实时应用场景显然过于缓慢。另一个局限性是局部变换可能与全局变换在视觉上略有差异（实验显示约 7% 像素存在 ≥5 的 RGB 通道差异），对于某些对质量极其敏感的专业场景可能不可接受。安全性方面，TilesProof-C2PA 只能证明非自适应的知识证明性质，无法抵抗在运行时进行在线签名查询的敌手。未来的工作方向包括：探索更 ZK-friendly 的哈希函数与 C2PA 结合的可能性、设计更强的自适应安全证明下的 C2PA 兼容方案、以及优化并行实现以缩短实际运行时间。

### 强关联论文

[1] Datta et al. Using ZK-proofs to fight disinformation. **RWC 2023** [Google Scholar](https://scholar.google.com/scholar?q=Using+ZK-proofs+to+fight+disinformation)

[2] Kang et al. zk-img: Attested images via zero-knowledge proofs to fight disinformation. **arXiv 2022** [Google Scholar](https://scholar.google.com/scholar?q=zk-img+Attested+images+via+zero-knowledge+proofs+to+fight+disinformation)

[3] Naveh et al. Photoproof: Cryptographic image authentication for any set of permissible transformations. **IEEE S&P 2016** [Google Scholar](https://scholar.google.com/scholar?q=Photoproof+Cryptographic+image+authentication+for+any+set+of+permissible+transformations)

[12] Datta et al. VerITAS: Verifying image transformations at scale. **Cryptology ePrint Archive 2024** [Google Scholar](https://scholar.google.com/scholar?q=VerITAS+Verifying+image+transformations+at+scale)

[13] Li et al. Region-aware photo assurance system for image authentication. **IEEE MIPR 2023** [Google Scholar](https://scholar.google.com/scholar?q=Region-aware+photo+assurance+system+for+image+authentication)

[9] Gailly et al. Snarkpack: Practical snark aggregation. **FC 2022** [Google Scholar](https://scholar.google.com/scholar?q=Snarkpack+Practical+snark+aggregation)

[18] Fiore et al. On the (in)security of snarks in the presence of oracles. **TCC 2016** [Google Scholar](https://scholar.google.com/scholar?q=On+the+insecurity+of+snarks+in+the+presence+of+oracles)


## 关键词

+ 零知识SNARK
+ 图像变换真实性验证
+ 机密性保护
+ C2PA规范兼容
+ 自适应对手模型
+ 欺诈证明检测