---
title: "Sparrow: Space-Efficient zkSNARK for Data-Parallel Circuits and Applications to Zero-Knowledge Decision Trees"
doi: 10.1145/3658644.3690318
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2024
modified: 2025-05-13 03:19:46
created: 2025-05-13 09:23:43
---
## Sparrow: Space-Efficient zkSNARK for Data-Parallel Circuits and Applications to Zero-Knowledge Decision Trees

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3658644.3690318)

## 作者

+ [Christodoulos Pappas](Christodoulos%20Pappas.md)
+ [Dimitrios Papadopoulos](Dimitrios%20Papadopoulos.md)

## 笔记

### 背景与动机

零知识简洁非交互式知识论证（zkSNARK）已从理论概念演变为匿名加密货币、区块链扩容和机器学习完整性保障等应用的关键组件。尽管在证明者运行时间上取得了显著改善，但所有现代 zkSNARK 共享一个核心瓶颈：证明者空间利用过度。在许多情况下，生成证明所需的内存比原生运行计算高数个数量级，例如，使用高效 zkSNARK 证明 VGG16 模型的预测需要 24GB 内存，而明文计算仅需不到 200MB [69]；用 Plonk [49] 和 Groth16 [54] 证明 16KB 预图像的 SHA256 分别需要 128GB 和 40GB [45]。空间高效论证致力于弥补这一差距，使证明者的时间和空间在渐进意义上尽可能接近实际计算。早期工作 [20, 21] 在 RAM 模型上取得了进展，但并非简洁证明。随后针对算术电路的工作，如 Ligetron [84] 和 Gemini [25]，各有局限：Ligetron 不是简洁的，Gemini 的总空间复杂度为 \(O(|C|)\)，这源于其使用了规模为 \(O(|C|)\) 的 KZG 公共参数。此外，对于任意电路，最优评估空间 \(S_{eval}\) 可能达到 \(O(|C|)\)，这构成了进一步减少证明空间的内在瓶颈。本文旨在填补这一空白：为数据并行算术电路这类“丰富”的电路类别，构建一个空间高效且证明时间接近最优的 zkSNARK，其总证明空间在渐进意义上小于电路规模 \(|C|\)。

### 相关工作

[20] Block et al. **Public-Coin Zero-Knowledge Arguments with (almost) Minimal Time and Space Overheads. *TCC 2020*** [Google Scholar](https://scholar.google.com/scholar?q=Public-Coin+Zero-Knowledge+Arguments+with+(almost)+Minimal+Time+and+Space+Overheads)
> 核心思路：在 RAM 模型下提出了首个公开可验证的空间高效论证，通过流式设置实现。
> 局限与区别：该方案不是简洁的，其验证时间为 \(O(T \log T)\)。本文聚焦于算术电路模型，避免了 RAM 到电路的转换开销。

[21] Block et al. **Time- and Space-Efficient Arguments from Groups of Unknown Order. *CRYPTO 2021*** [Google Scholar](https://scholar.google.com/scholar?q=Time-+and+Space-Efficient+Arguments+from+Groups+of+Unknown+Order)
> 核心思路：基于隐藏阶群上的空间高效多项式承诺方案，构建了首个空间高效的 RAM 模型 zkSNARK。
> 局限与区别：同样工作于 RAM 模型，本文针对数据并行算术电路，可实现更优的渐进复杂度。

[84] Venkitasubramaniam. **Ligetron: Lightweight Scalable End-to-End Zero-Knowledge Proofs. *IEEE SP 2023*** [Google Scholar](https://scholar.google.com/scholar?q=Ligetron+Lightweight+Scalable+End-to-End+Zero-Knowledge+Proofs)
> 核心思路：基于 MPCitH 思想，为算术电路构建空间高效论证。
> 局限与区别：Ligetron 不是简洁证明，其证明规模和验证时间为 \(O(\sqrt{|C|})\) 和 \(O(|C|)\)。本文提出的 Sparrow 是简洁的。

[25] Bootle et al. **Gemini: Elastic SNARKs for Diverse Environments. *EUROCRYPT 2022*** [Google Scholar](https://scholar.google.com/scholar?q=Gemini+Elastic+SNARKs+for+Diverse+Environments)
> 核心思路：针对任意算术电路，通过空间高效的 PIOP 和 KZG 承诺的变体，实现了 \(O(\log |C|)\) 的工作缓冲区空间。
> 局限与区别：Gemini 的总空间复杂度为 \(O(|C|)\)，因其公共参数和流实例化所需空间均为 \(O(|C|)\)。本文也为数据并行电路实现了总空间复杂度 \(O(\sqrt{|C|} + |\text{inp}(C)|)\)。

[80] Setty. **Spartan: Efficient and General-Purpose zkSNARKs Without Trusted Setup. *CRYPTO 2020*** [Google Scholar](https://scholar.google.com/scholar?q=Spartan+Efficient+and+General-Purpose+zkSNARKs+Without+Trusted+Setup)
> 核心思路：提出了一个通用的、无需可信设置的 zkSNARK，具有线性证明时间。
> 局限与区别：Spartan 并非为空间效率优化。本文借鉴了其离线内存检查技术来优化直方图证明。

[90] Xie et al. **Libra: Succinct Zero-Knowledge Proofs with Optimal Prover Computation. *CRYPTO 2019*** [Google Scholar](https://scholar.google.com/scholar?q=Libra+Succinct+Zero-Knowledge+Proofs+with+Optimal+Prover+Computation)
> 核心思路：基于 GKR 协议和多项式承诺，构建了证明者计算最优的 zkSNARK。
> 局限与区别：Libra 不是空间高效的。本文在 Sparrow 中使用了其技术（如零知识转化、将 sumcheck 实例分解为双线性乘积）来实现基于 GKR 的协议。

[69] Liu et al. **zkCNN: Zero Knowledge Proofs for Convolutional Neural Network Predictions and Accuracy. *CCS 2021*** [Google Scholar](https://scholar.google.com/scholar?q=zkCNN+Zero+Knowledge+Proofs+for+Convolutional+Neural+Network+Predictions+and+Accuracy)
> 核心思路：构建了用于卷积神经网络推理的零知识证明。
> 局限与区别：该工作在证明 VGG16 时需要 24GB 内存，凸显了空间效率问题。本文将其作为需要空间高效方案的典型应用案例。

[61] Ke et al. **LightGBM: A Highly Efficient Gradient Boosting Decision Tree. *NIPS 2017*** [Google Scholar](https://scholar.google.com/scholar?q=LightGBM+A+Highly+Efficient+Gradient+Boosting+Decision+Tree)
> 核心思路：提出了一种高效的基于直方图的梯度提升决策树训练算法。
> 局限与区别：本文的 zkFTP 在认证算法中借鉴了其基于直方图的思想，以高效地验证训练的正确性而非重训。

[34] Campanelli et al. **Lookup Arguments: Improvements, Extensions and Applications to Zero-Knowledge Decision Trees. *ePrint 2023*** [Google Scholar](https://scholar.google.com/scholar?q=Lookup+Arguments+Improvements+Extensions+and+Applications+to+Zero-Knowledge+Decision+Trees)
> 核心思路：改进了查找参数，并用于构建零知识决策树预测协议。
> 局限与区别：本文的 zkFTP 在其预测部分采用了该工作的矩阵查找参数和预测证明电路。

[81] Setty and Lee. **Quarks: Quadruple-efficient transparent zkSNARKs. *ePrint 2020*** [Google Scholar](https://scholar.google.com/scholar?q=Quarks+Quadruple-efficient+transparent+zkSNARKs)
> 核心思路：提出了一个名为 Kopis 的、基于内配对积和 KZG 的多项式承诺方案，具有 \(O(\sqrt{N})\) 的公共参数。
> 局限与区别：本文在 Sparrow 中采用并适配了 Kopis 承诺方案，以满足其空间效率需求（公共参数子线性于电路规模）。

### 核心技术与方案

Sparrow 的整体框架是一个空间高效的 zkSNARK，专为分层数据并行算术电路设计。其核心构建块是一个新型的空间高效求和检查协议，该协议被用于构建一个空间高效的 GKR 协议变体，并最终通过一个空间高效的多项式承诺方案（PC）编译成 zkSNARK。此外，该论文利用 Sparrow 作为后端，构建了一个零知识森林训练与预测协议（zkFTP）。

**1. 空间高效求和检查协议（Section 3.1）**

传统的多线性多项式求和检查在流式模型中每轮需要扫描整个向量 \(A_f, A_g\)，导致 \(O(N \log N)\) 的证明时间，即使放松到 \(O(\sqrt{N})\) 缓冲区空间，仍需扫描 \(\log N / 2\) 次，总时间仍为 \(O(N \log N)\)。本文的核心思想是“减少”多项式变量数量以降低轮数。具体地，将双线性多项式 \(f, g: \mathbb{F}^n \to \mathbb{F}\) (其中 \(N=2^n\)) 替换为等价的、变量更少但次数更高的多项式 \(\hat{f}, \hat{g}: \mathbb{F}^{2 + n/2} \to \mathbb{F}\)。设定缓冲区大小为 \(O(\sqrt{N})\)，仅需替换前 \((\log N)/2\) 个变量为两个高次变量，次数分别为 \(\log N\) 和 \(\sqrt{N} / \log N\)。该协议分为两阶段：
- **第一阶段：** 对 \(\hat{f}, \hat{g}\) 执行求和检查。第一轮，扫描流读取 \(\sqrt{N} / \log N\) 个元素，通过 FFT 进行 \(N / \log N\) 次度为 \(\log N\) 的多项式乘法，得到 \(p_0(x)\)，复杂度为 \(O(N \log \log N)\)。第二轮，处理第二个高次变量。剩余轮次中，由于简化后的多项式规模为 \(\sqrt{N}\)，可使用标准求和检查。
- **第二阶段：** 将第一阶段的评估结果归约回原多项式 \(f, g\) 的评估。
最终，该求和检查协议的证明者时间优化至 \(O(N \log \log N)\)（相较于 \(O(N \log N)\)），缓冲区空间为 \(O(\sqrt{N})\)。

**2. 空间高效论证系统（Section 3.2）**

基于前述求和检查协议，构建空间高效的 GKR 协议。
- **单层电路证明（Section 3.2.1）：** 针对分层数据并行电路中每一层的正确计算，将 sumcheck 实例分解为两个形如 \(\sum_{x} f(x)h(x)\) 的子实例，从而可利用新型求和检查。同时，通过流式 Oracle 机制实例化对层输入 \(\mathbf{V}_i\) 和相关函数的访问，递归地按需评估电路层，仅需维持一个小缓冲区。
- **整体证明与电路“扁平化”（Section 3.2.2 & 3.2.3）：** 通过将深度为 \(d\) 的电路“扁平化”为深度 \(\tilde{d} < \log \log |C|\) 的电路 \(\tilde{C}\) 并使用 GKR，证明者复杂度降至 \(O(|C| \log \log |C|)\)。最后，采用空间高效的多项式承诺方案 Kopis [81]（其公共参数大小为 \(O(\sqrt{|\text{witness}|})\)）编译成 zkSNARK。最终 Sparrow 实现：证明者计算 \(O(|C| \log \log |C|)\) 域操作和 \(O(|C|)\) 大小 MSM，证明规模和验证复杂度为 \(O(\log |C|)\)，总空间复杂度为 \(O(\sqrt{|C|} + |\text{inp}(C)|)\)。

**3. 零知识森林训练和预测（Section 4）**

本文提出了 zkFTP，它利用认证算法而非重训来验证决策树训练的正确性。
- **认证算法（Section 4.1）：** 给定训练好的树 \(\mathcal{T}\) 和数据集 \(D\)，算法通过 (1) 分配数据点到树叶，(2) 计算叶子直方图，(3) 利用直方图同态性（子节点直方图相加等于父节点直方图）计算上层节点直方图，以及 (4) 从根节点开始检查每个节点分裂的正确性。该算法复杂度为 \(O(|D|)\)（优于训练算法的 \(O(h|D|)\)），空间为 \(O(|D| + d|\mathcal{T}|B)\)。
- **zkFTP 构造（Section 4.2）：** 证明过程将认证算法分解为五个独立的子任务，每个任务编码为一个数据并行算术电路，并利用 Sparrow 或标准 GKR 进行证明。这些子任务包括：(1) 检查数据点分配的正确性，(2) 验证叶子直方图（通过离线内存检查技术 [80]），(3) 验证非叶子直方图（通过一个用于树计算的通用电路），(4) 验证节点分裂的 Gini 指数计算，(5) 检查树的结构良好性。整个协议在 \(O(|D| d \log \log |D|)\) 时间、\(O(|D| + |\mathcal{F}| + LBd + \sqrt{|D|K})\) 空间内完成训练证明，预测证明则更轻量。

### 核心公式与流程

**[空间高效求和检查的核心重参数化]**
\[\hat{f}(x_0, x_1, \mathbf{x}_2) = \sum_{i \in \mathbb{H}_0, j \in \mathbb{H}_1, \mathbf{k} \in \{0,1\}^{n/2}} L_i^{(0)}(x_0) L_j^{(1)}(x_1) \beta(\mathbf{x}_2, \mathbf{k}) \mathbf{A}_f[2^{n-\log n}i + 2^{n/2}j + k]\]
> 作用：将多线性多项式 \(f\) 替换为等价的2变量（\(x_0, x_1\)）和 \(n/2\) 个布尔变量（\(\mathbf{x}_2\)）的高次多项式，从而将原求和检查的轮数从 \(n\) 轮减少为常数（加 \(n/2\) 轮）。其中 \(\mathbb{H}_0, \mathbb{H}_1\) 是大小为 \(\log N\) 和 \(\sqrt{N} / \log N\) 的乘法子群。

**[GKR 单层求和检查实例]**
\[f_{i-1}(r) = \sum_{(x,y) \in \{0,1\}^{2s_i}} \left(f_{add}^i(r,x,y)(f_i(x) + f_i(y)) + f_{mul}^i(r,x,y) f_i(x) f_i(y)\right)\]
> 作用：描述 GKR 协议中证明第 \(i\) 层电路正确计算的核心关系，其中 \(f_i\) 是第 \(i\) 层输出向量的多线性扩展，\(f_{add}^i, f_{mul}^i\) 是加法/乘法门的布线谓词。Sparrow 借鉴了 [90] 的方法，将此实例拆分为两个形如 \(\sum f(x)g(x)\) 的求和检查。

**[空间高效求和检查的归约]**
\[y_{\hat{f}} = \sum_{x \in \{0,1\}^{n/2}} f_{\mathbf{y}}(x) f(x, \mathbf{r}_2)\]
> 作用：在求和检查第二阶段结束后，将 \(\hat{f}\) 在点 \((\mathbf{r}_0, \mathbf{r}_1, \mathbf{r}_2)\) 的评估值 \(y_{\hat{f}}\) 归约到对原多线性多项式 \(f\) 的评估值的计算，其中 \(\mathbf{y} = \mathbf{y}_0 \otimes \mathbf{y}_1\) 是拉格朗日多项式系数的张量积。这一步允许通过标准求和检查证明该归约的正确性，并最终得到 \(f\) 和 \(g\) 在同一随机点上的评估值。

### 实验结果

实验在一台配备 131GB RAM 和 Intel Xeon E-2174G CPU 的机器上单线程运行。对比基线包括状态相关的空间高效 SNARK Gemini [25]（使用其公开代码和针对数据并行电路的优化版本）和一个非空间高效的、基于 GKR 和 Kopis 承诺方案的 zkSNARK（记为 GKR+Kopis）。

1. **Sparrow vs. Gemini:** 在所有基准测试中，Sparrow 在证明者时间上比 Gemini 快 3.4-11.3 倍，在总空间上节省 14.5-28.7 倍。例如，对于规模为 \(2^{30}\) 的任意数据并行电路，Sparrow 耗时 79 分钟、占用 2.7GB 空间，而 Gemini 耗时 744 分钟、占用 80GB。对于 2048 次 SHA256 哈希，Sparrow 耗时 13 分钟、占用 700MB，而 Gemini 耗时 46 分钟、占用 10.5GB。

2. **Sparrow vs. GKR+Kopis:** 与最优时间但非空间高效的方案相比，Sparrow 证明者时间仅慢 1.3-2.9 倍（主要由新型求和检查的 \(O(\log \log N)\) 因子导致），但空间减少了 27.5-119 倍。例如，对于 \(2^{27}\) 大小的电路，Sparrow 占用 1GB 而 GKR+Kopis 需要 119.5GB（后者在更大规模时超出可用内存）。Sparrow 的证明大小和验证时间略大（< 45%），但仍非常实用（最大< 90KB, < 15ms）。

3. **zkFTP 性能:** 对于单棵树的训练证明，与 GKR+Kopis 相比，Sparrow 实现了 16-240 倍的空间缩减，而证明时间几乎相同（慢 1.1-1.3 倍）或稍快。例如，当 \(n=2^{20}, d=16\) 时，Sparrow 占用 0.42GB 而 GKR+Kopis 需要 90GB。对于随机森林（\(K>1\)），Sparrow 同样展现出巨大的空间优势（最多 288 倍），且其空间与树的数目 \(K\) 大致无关。覆盖训练证明时，对于最大实例（\(n=2^{22}, d=16, K=1\)），Sparrow 的空间仅 950MB，是原生认证算法所需空间（676MB）的 1.4 倍。

### 局限性与开放问题

尽管 Sparrow 在数据并行电路上取得了显著的改进，但其应用范围受到电路结构的限制。对于非数据并行或具有不规则拓扑结构的电路，Sparrow 可能无法直接应用或其优势减弱。未来计划将 Sparrow 扩展至非分层的、不规则的数据并行电路。此外，Sparrow 的噪声证明大小和验证时间相比 Gemini 有少量增加，这源于其基于 GKR 的方法论（证明大小与电路深度 \(d\) 相关）。开放问题包括进一步优化证明者和验证者复杂度，并探索将 Sparrow 应用于其他计算密集型任务，如隐私保护的数据分析。

### 强关联论文

[20] Block et al. **Public-Coin Zero-Knowledge Arguments with (almost) Minimal Time and Space Overheads. *TCC 2020*** [Google Scholar](https://scholar.google.com/scholar?q=Public-Coin+Zero-Knowledge+Arguments+with+(almost)+Minimal+Time+and+Space+Overheads)

[21] Block et al. **Time- and Space-Efficient Arguments from Groups of Unknown Order. *CRYPTO 2021*** [Google Scholar](https://scholar.google.com/scholar?q=Time-+and+Space-Efficient+Arguments+from+Groups+of+Unknown+Order)

[25] Bootle et al. **Gemini: Elastic SNARKs for Diverse Environments. *EUROCRYPT 2022*** [Google Scholar](https://scholar.google.com/scholar?q=Gemini+Elastic+SNARKs+for+Diverse+Environments)

[34] Campanelli et al. **Lookup Arguments: Improvements, Extensions and Applications to Zero-Knowledge Decision Trees. *ePrint 2023*** [Google Scholar](https://scholar.google.com/scholar?q=Lookup+Arguments+Improvements+Extensions+and+Applications+to+Zero-Knowledge+Decision+Trees)

[52] Goldwasser et al. **Delegating computation: interactive proofs for muggles. *STOC 2008*** [Google Scholar](https://scholar.google.com/scholar?q=Delegating+computation+interactive+proofs+for+muggles)

[60] Kate et al. **Constant-Size Commitments to Polynomials and Their Applications. *ASIACRYPT 2010*** [Google Scholar](https://scholar.google.com/scholar?q=Constant-Size+Commitments+to+Polynomials+and+Their+Applications)

[69] Liu et al. **zkCNN: Zero Knowledge Proofs for Convolutional Neural Network Predictions and Accuracy. *CCS 2021*** [Google Scholar](https://scholar.google.com/scholar?q=zkCNN+Zero+Knowledge+Proofs+for+Convolutional+Neural+Network+Predictions+and+Accuracy)

[80] Setty. **Spartan: Efficient and General-Purpose zkSNARKs Without Trusted Setup. *CRYPTO 2020*** [Google Scholar](https://scholar.google.com/scholar?q=Spartan+Efficient+and+General-Purpose+zkSNARKs+Without+Trusted+Setup)

[81] Setty and Lee. **Quarks: Quadruple-efficient transparent zkSNARKs. *ePrint 2020*** [Google Scholar](https://scholar.google.com/scholar?q=Quarks+Quadruple-efficient+transparent+zkSNARKs)

[90] Xie et al. **Libra: Succinct Zero-Knowledge Proofs with Optimal Prover Computation. *CRYPTO 2019*** [Google Scholar](https://scholar.google.com/scholar?q=Libra+Succinct+Zero-Knowledge+Proofs+with+Optimal+Prover+Computation)


## 关键词

+ 零知识SNARK
+ 空间效率
+ 数据并行电路
+ 决策树
+ 求和校验
+ 证明者优化