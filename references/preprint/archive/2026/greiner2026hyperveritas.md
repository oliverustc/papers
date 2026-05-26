---
title: "HyperVerITAS: Verifying Image Transformations at Scale on Boolean Hypercubes"
标题简称:
论文类型: preprint
预印本简称: archive
发表年份: 2026
---

## HyperVerITAS: Verifying Image Transformations at Scale on Boolean Hypercubes

## 发表信息

+ [原文链接](https://eprint.iacr.org/2026/641)

## 作者

+ Garrett Greiner
+ Toshi Mowery
+ Pratik Soni

## 笔记

### 背景与动机

数字图像的真实性验证在科学出版、生成式AI和可信文档等领域日益关键。C2PA标准 [CA22] 允许可信设备（如相机）在拍摄时对图像进行数字签名，但图像在发布前往往要经过裁剪、灰度化等变换，而这些变换会破坏原始签名，导致无法验证编辑后图像的来源。C2PA提出将信任链扩展到编辑软件，要求每个编辑工具重新签名，但这会引入新的安全风险——编辑软件必须安全地管理密钥，对于开源或消费级应用而言这种假设难以成立。Datta等人 [DCB25b] 提出了更现实的威胁模型：只信任原始拍摄设备，编辑软件被视为不可信，并基于该模型构建了VerITAS系统。VerITAS使用零知识证明（ZKP）来证明输出图像是输入图像经有效变换的结果，同时保护输入图像的隐私。然而，VerITAS存在严重瓶颈：证明者内存消耗极高（75–120 GB用于30 MP图像），这源自其使用单变量IOP和FFT密集型操作；同时，将图像变换编码为R1CS电路也占用了大量证明时间；此外，对多个连续变换的证明需要分解为多个子证明，进一步增加了复杂性。本文旨在解决这些问题，设计能够在普通商用硬件上处理30 MP图像的可扩展ZKP系统。

### 相关工作

[DCB25b] Datta, Chen, Boneh. VerITAS: Verifying Image Transformations at Scale. **IEEE S&P 2025** [Google Scholar](https://scholar.google.com/scholar?q=VerITAS+Verifying+Image+Transformations+at+Scale)  
> 核心思路：提出基于SNARK的图像来源验证系统，将证明分解为签名知识证明和变换正确性证明。  
> 局限与区别：使用FFT-heavy的单变量IOP和PLONK，内存消耗高达120 GB，无法在普通硬件上扩展到4 MP以上；本文改用布尔超立方上的多线性多项式编码以消除FFT。

[DEH24] Dziembowski, Ebrahimi, Hassanizadeh. VIMz: Private Proofs of Image Manipulation using Folding-based zkSNARKs. **ePrint 2024** [Google Scholar](https://scholar.google.com/scholar?q=VIMz+Private+Proofs+of+Image+Manipulation)  
> 核心思路：利用折叠型ZKP逐步证明变换，降低内存开销。  
> 局限与区别：内存低但证明速度慢（33 MP需约2小时），而HyperVerITAS只需6.6分钟。

[MVV+25b] Della Monica, Visconti, Vitaletti, Zecchini. Trust Nobody: Privacy-Preserving Proofs for Edited Photos with Your Laptop. **IEEE S&P 2025** [Google Scholar](https://scholar.google.com/scholar?q=Trust+Nobody+Privacy-Preserving+Proofs+for+Edited+Photos)  
> 核心思路：将图像分块（tiles），每块独立证明，降低内存。  
> 局限与区别：内存极低（3.1 GB）但证明时间较长（33 MP需30分钟），HyperVerITAS在证明时间上更优。

[LXZ21] Liu, Xie, Zhang. zkCNN: Zero Knowledge Proofs for Convolutional Neural Network Predictions and Accuracy. **CCS 2021** [Google Scholar](https://scholar.google.com/scholar?q=zkCNN+Zero+Knowledge+Proofs+for+Convolutional+Neural+Network)  
> 核心思路：提出基于sum-check的2-D卷积证明协议，可用于图像模糊等变换。  
> 局限与区别：证明者时间O(n)，验证者和证明大小O(log² n)；本文的内积协议达到O(log n)的验证开销，略优。

[CBB+23] Chen, Bünz, Boneh, Zhang. HyperPlonk: Plonk with Linear-Time Prover and High-Degree Custom Gates. **EUROCRYPT 2023** [Google Scholar](https://scholar.google.com/scholar?q=HyperPlonk+Plonk+with+Linear-Time+Prover+and+High-Degree+Custom+Gates)  
> 核心思路：将PLONK推广到布尔超立方，消除FFT，实现线性时间证明。  
> 局限与区别：本文借鉴其多线性IOP和Lookup协议，但将其应用于图像来源证明的新场景。

[GLS+23] Golovnev, Lee, Setty, Thaler, Wahby. Brakedown: Linear-Time and Field-Agnostic SNARKs for R1CS. **CRYPTO 2023** [Google Scholar](https://scholar.google.com/scholar?q=Brakedown+Linear-Time+and+Field-Agnostic+SNARKs+for+R1CS)  
> 核心思路：基于纠错码的线性时间多项式承诺方案。  
> 局限与区别：本文作为HyperVerITAS的后量子PCS选项，与多线性IOP结合。

[PST13] Papamanthou, Shi, Tamassia. Signatures of Correct Computation. **TCC 2013** [Google Scholar](https://scholar.google.com/scholar?q=Signatures+of+Correct+Computation)  
> 核心思路：基于配对的多线性多项式承诺方案。  
> 局限与区别：本文将其作为另一种PCS实例化，证明其性能优于VerITAS的FRI。

### 核心技术与方案

HyperVerITAS的整体关系定义为 $R_{\mathsf{vk}} = \{((I_T, T); (I, \sigma)): I_T = T(I) \land \mathsf{Vrfy}(\mathsf{vk}, I, \sigma)=1\}$，并分解为两个子证明：签名知识证明和变换正确性证明。与VerITAS不同，HyperVerITAS将所有多项式编码为布尔超立方 $\mathbb{B}_\mu$ 上的多线性多项式，从而避免FFT操作，大幅降低内存。

**1. 签名知识证明**  
系统支持两种模式。模式一（相机模式）使用基于格的低范数线性哈希函数（如Ajtai哈希 [Ajt96]）：$\mathsf{H}_{\mathbf{A}}(\mathbf{v}) = \mathbf{A} \odot \mathbf{v} \pmod{q}$，其中 $\mathbf{A} \in \mathbb{F}_q^{h \times n}$，$h < n$。该哈希的安全性基于SIS问题的困难性，只对低范数输入（$I \in [256]^{n \times 3}$）具有碰撞抵抗性。因此，证明者需要证明（1）$\mathbf{H} = \mathbf{A} \odot \mathbf{I}$（通过内积协议将矩阵乘检验归约为向量内积），（2）$\mathbf{I}$ 的每个分量在 $[0,255]$ 范围内（通过Lookup协议进行范围证明）。模式二（ML服务器模式）直接使用多线性多项式承诺作为哈希，将图像的承诺视为哈希值，然后只需在变换证明中内嵌对承诺的开销，无需单独的范围证明，进一步降低开销。

**2. 变换正确性证明**  
本文观察到大多数图像变换（裁剪、灰度化、模糊、缩放）可表示为仿射变换：$T(\mathbf{I}) = \mathbf{L} \odot \mathbf{I} \odot \mathbf{R} + \mathbf{E}$，其中 $\mathbf{L} \in \mathbb{Z}^{m \times n}$，$\mathbf{R} \in \mathbb{Z}^{3 \times 3}$，$\mathbf{E} \in \mathbb{Z}^{m \times 3}$ 且 $||\mathbf{E}||_\infty \leq B$。对于公共仿射变换（如裁剪），$\mathbf{E}$ 是公开的（例如红色区域设为颜色值）；对于私有仿射变换（如灰度化），$\mathbf{E}$ 由舍入误差产生，需要承诺并附加范围证明以保护隐私。证明协议基于Freivalds算法：验证者随机采样向量 $\mathbf{r} \in \mathbb{F}^m$，然后双方运行内积协议验证 $\langle \mathbf{r}, (\mathbf{I}_T - \mathbf{E})_j \rangle = \langle \mathbf{r} \odot \mathbf{L}, (\mathbf{I} \odot \mathbf{R})_j \rangle$ 对每个通道 $j$ 成立。通过承诺的同态性，将矩阵乘法检验转化为一次内积检验。正确性与安全性：内积协议的知识可靠性保证了若证明者能通过内积检验，则其必然知道满足关系的 $\mathbf{I}$ 和 $\mathbf{E}$；Freivalds算法保证矩阵相等以高概率成立。零知识性来自承诺的隐藏性和内积协议的HVZK性质。渐进复杂度（以Brakedown PCS为例，$n$ 为原图像素，$m$ 为变换后图像素）：公共仿射协议证明者时间 $O(nm + n) \mathbb{F} + O(m) \mathbb{H} + 3TP_{\text{op}}(n)$，验证者时间 $O(nm + m + \log n) \mathbb{F} + O(m) \mathbb{H} + 3TV_{\text{op}}(n)$，证明大小 $O(3 \log n) \mathbb{F} + 3\pi_{\text{com}}(n) + 3\pi_{\text{op}}(n)$。私有仿射协议因额外范围证明和更多承诺，证明者时间增加 $39TP_{\text{op}}(m)$ 等项。

**3. 整体系统**  
HyperVerITAS将签名知识证明（线性哈希+范围证明）和变换正确性证明（仿射协议）组合。整个系统可实例化五种多线性PCS：PST（配对型）、Brakedown（编码型）、Basefold、BasefoldFri、ZeromorphFri。系统采用每通道独立承诺以利用并行性，同时支持批量打开以减小Brakedown的证明大小。在安全性方面，整体知识可靠性依赖于内积协议、Lookup协议和承诺的可靠性，以及Freivalds算法；零知识性由承诺隐藏性和各子协议保证。

### 核心公式与流程

**整体关系**
$$
R_{\mathsf{vk}} = \{ ((I_T, T); (I, \sigma)): I_T = T(I) \land \mathsf{Vrfy}(\mathsf{vk}, I, \sigma)=1 \}.
$$
> 定义系统的证明目标。

**Ajtai线性哈希**
$$
\mathsf{H}_{\mathbf{A}}(\mathbf{v}) := \mathbf{A} \odot \mathbf{v} \pmod{q}.
$$
> 用于签名知识证明中的哈希函数。

**公共仿射变换协议（以裁剪为例）**
$$
\begin{aligned}
&\mathcal{P} \text{ 计算 } \mathsf{com}_{(\mathbf{I} \odot \mathbf{R})_j} \text{ 对每个通道 } j;\\
&\mathcal{V} \text{ 发送随机 } \mathbf{r} \in \mathbb{F}^m;\\
&\mathcal{P} \text{ 计算 } c_j := \langle \mathbf{r}, (\mathbf{I}_T - \mathbf{E})_j \rangle;\\
&\text{运行内积协议证明 } c_j = \langle \mathbf{r} \odot \mathbf{L}, (\mathbf{I} \odot \mathbf{R})_j \rangle.
\end{aligned}
$$
> 将矩阵仿射变换验证归约为向量内积。

**私有仿射变换协议（以灰度化为例）**
$$
\mathbf{y} := \text{Round}(0.30 \cdot \mathbf{r} + 0.59 \cdot \mathbf{g} + 0.11 \cdot \mathbf{b}), \quad \mathbf{e} := \mathbf{y} - (0.30\mathbf{r}+0.59\mathbf{g}+0.11\mathbf{b}).
$$
转化为整数域：$100 \cdot \mathbf{y} = (30 \cdot \mathbf{r} + 59 \cdot \mathbf{g} + 11 \cdot \mathbf{b}) + 100 \cdot \mathbf{e}$。其中 $\mathbf{L}=I_{m \times m}$，$\mathbf{R}$ 为系数矩阵，$\mathbf{E}=100 \cdot \mathbf{e}$ 重复三次。
> 展示私有仿射变换的具体参数。

**内积关系**
$$
R_{\mathrm{ip}} = \{ (([f], g, c); f): c = \sum_{\mathbf{x} \in \mathbb{B}_\mu} f(\mathbf{x}) \cdot g(\mathbf{x}) \}.
$$
> 通过sum-check协议实现，证明者时间 $O(2^{\mu+1})$，验证者时间 $O(\mu)$。

**Lookup关系（用于范围证明）**
$$
R_{\mathrm{lk}} = \{ ((\mathbf{t}, [f]); f): \forall \mathbf{x} \in \mathbb{B}_\mu, f(\mathbf{x}) \in \mathbf{t} \}.
$$
> 验证每个像素值在 $[0,255]$ 内，使用HyperPlonk的Lookup协议。

### 实验结果

实验在两种硬件上进行：苹果MacBook M3（36 GB RAM）和AWS EC2 r5d.4xlarge（128 GiB RAM，16 vCPUs）。对比基线包括VerITAS（KZG和FRI变体）、VIMz和TilesProof-MT。测试了两种变换：裁剪（保留50%图像）和灰度化。对于裁剪，HyperVerITAS（Brakedown-127）在M3上处理33 MP（$2^{25}$像素）图像需6.6分钟，内存27.4 GB；VerITAS FRI在4 MP时已内存耗尽（27.4 GB但无法继续）。在相同硬件上，HyperVerITAS PST在4 MP下证明时间143.8秒（VerITAS FRI为267.8秒），内存24.5 GB vs 27.4 GB。对于灰度化，HyperVerITAS Brakedown在16 MP（$2^{24}$）下需184.9秒，内存28.4 GB；VerITAS FRI在2 MP时失败。对比VIMz和TilesProof-MT：HyperVerITAS证明速度更快（6.6分钟 vs 2小时或30分钟），但证明大小较大（Brakedown达363 MB vs 11 KB或129 KB）。在AWS服务器上，HyperVerITAS所有变体（包括256位字域Brakedown）均优于VerITAS，且能处理VerITAS无法处理的更大图像。哈希性能（ML模式）：Brakedown承诺33 MP图像需4.18秒，内存10.19 GB；VerITAS FRI需19.84秒，内存18.90 GB，验证了多线性编码的效率。

### 局限性与开放问题

HyperVerITAS在证明速度上优势明显，但Brakedown实例的证明大小过大（MB级别），阻碍了在带宽受限场景的应用。未来可探索开发新的编码型多线性PCS以减小证明，或优化签名知识证明的哈希大小（如结合SHA-256与Binius）。另外，私有仿射变换中额外范围证明增加了承诺和开口数量，导致证明大小进一步增长，可研究更紧凑的范围证明技术。

### 强关联论文

[DCB25b] Datta, Chen, Boneh. VerITAS: Verifying Image Transformations at Scale. **IEEE S&P 2025** [Google Scholar](https://scholar.google.com/scholar?q=VerITAS+Verifying+Image+Transformations+at+Scale)

[DEH24] Dziembowski, Ebrahimi, Hassanizadeh. VIMz: Private Proofs of Image Manipulation using Folding-based zkSNARKs. **ePrint 2024** [Google Scholar](https://scholar.google.com/scholar?q=VIMz+Private+Proofs+of+Image+Manipulation)

[MVV+25b] Della Monica, Visconti, Vitaletti, Zecchini. Trust Nobody: Privacy-Preserving Proofs for Edited Photos with Your Laptop. **IEEE S&P 2025** [Google Scholar](https://scholar.google.com/scholar?q=Trust+Nobody+Privacy-Preserving+Proofs+for+Edited+Photos)

[LXZ21] Liu, Xie, Zhang. zkCNN: Zero Knowledge Proofs for Convolutional Neural Network Predictions and Accuracy. **CCS 2021** [Google Scholar](https://scholar.google.com/scholar?q=zkCNN+Zero+Knowledge+Proofs+for+Convolutional+Neural+Network)

[CBB+23] Chen, Bünz, Boneh, Zhang. HyperPlonk: Plonk with Linear-Time Prover and High-Degree Custom Gates. **EUROCRYPT 2023** [Google Scholar](https://scholar.google.com/scholar?q=HyperPlonk+Plonk+with+Linear-Time+Prover+and+High-Degree+Custom+Gates)

[GLS+23] Golovnev, Lee, Setty, Thaler, Wahby. Brakedown: Linear-Time and Field-Agnostic SNARKs for R1CS. **CRYPTO 2023** [Google Scholar](https://scholar.google.com/scholar?q=Brakedown+Linear-Time+and+Field-Agnostic+SNARKs+for+R1CS)

[PST13] Papamanthou, Shi, Tamassia. Signatures of Correct Computation. **TCC 2013** [Google Scholar](https://scholar.google.com/scholar?q=Signatures+of+Correct+Computation)

[Ajt96] Ajtai. Generating hard instances of lattice problems. **STOC 1996** [Google Scholar](https://scholar.google.com/scholar?q=Generating+hard+instances+of+lattice+problems)

[CA22] Coalition for Content Provenance and Authenticity. Coalition for Content Provenance and Authenticity (C2PA). **2022** [Google Scholar](https://scholar.google.com/scholar?q=Coalition+for+Content+Provenance+and+Authenticity)

[DP25] Diamond, Posen. Succinct Arguments over Towers of Binary Fields. **EUROCRYPT 2025** [Google Scholar](https://scholar.google.com/scholar?q=Succinct+Arguments+over+Towers+of+Binary+Fields)


## 关键词

+ HyperVerITAS图像溯源零知识证明
+ 布尔超立方体多线性多项式编码
+ 图像变换可验证签名ZKP系统
+ Brakedown多线性KZG承诺方案
+ 后量子图像真实性验证可扩展
