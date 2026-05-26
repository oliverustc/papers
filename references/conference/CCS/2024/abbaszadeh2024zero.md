---
title: "Zero-Knowledge Proofs of Training for Deep Neural Networks"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2024

modified: 2025-05-13 03:18:55
created: 2025-05-13 09:23:43
---

## Zero-Knowledge Proofs of Training for Deep Neural Networks

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3658644.3670316)

## 作者

+ Kasra Abbaszadeh
+ [Christodoulos Pappas](Christodoulos%20Pappas.md)
+ [Jonathan Katz](Jonathan%20Katz.md)
+ [Dimitrios Papadopoulos](Dimitrios%20Papadopoulos.md)

## 笔记

### 背景与动机
深度学习模型训练的可信性问题日益突出，模型所有者需要向第三方证明模型是使用特定数据集、按照公开算法正确训练得到的，同时又不泄露模型或数据集的额外信息。现有方案存在根本性缺陷：Jia 等人提出的 Proof-of-Learning [40] 不具备密码学强度的安全性，已被后续攻击工作攻破 [30, 31]，且非零知识、非简洁；Garg 等人的 zkPoT [34] 提供可证明安全性，但验证开销过大，无法支持深度神经网络；通用零知识证明（如 zkSNARKs）虽然简洁，但证明生成时间较训练本身有超过 1000 倍的性能退化，且内存开销巨大；而证明推理效率的零知识协议 [50, 61] 解决的是更简单的问题，无法直接扩展至多轮迭代、计算复杂度高出百倍的训练场景。本文旨在填补这一空白，同时实现可证明的安全隐私保障、简洁的证明大小与验证时间，以及实践可用的证明者效率。

### 相关工作

[34] Garg et al. Experimenting with Zero-Knowledge Proofs of Training. **CCS 2023** [Google Scholar](https://scholar.google.com/scholar?q=Experimenting+with+Zero-Knowledge+Proofs+of+Training)
> 核心思路：首次构建了具有可证明安全性的 zkPoT 方案。
> 局限与区别：验证开销不简洁，仅支持逻辑回归等简单算法，无法扩展到深度神经网络。

[40] Jia et al. Proof-of-Learning: Definitions and Practice. **IEEE S&P 2021** [Google Scholar](https://scholar.google.com/scholar?q=Proof-of-Learning+Definitions+and+Practice)
> 核心思路：首次形式化定义了训练证明问题并提出具体构造。
> 局限与区别：安全性未经过密码学证明，已被攻击 [30, 31] 攻破；非零知识、非简洁；验证者需部分重执行训练。

[26] Chiesa et al. Fractal: Post-quantum and Transparent Recursive Proofs from Holography. **Eurocrypt 2020** [Google Scholar](https://scholar.google.com/scholar?q=Fractal+Post-quantum+and+Transparent+Recursive+Proofs+from+Holography)
> 核心思路：基于全息技术的透明递归证明系统。
> 局限与区别：作为通用 IVC 方案，其证明者在处理 DNN 梯度下降时，线性代数运算的 R1CS 约束数极大，导致验证时间远超本文方案。

[17] Bowe et al. Recursive Proof Composition without a Trusted Setup. **Cryptology ePrint Archive 2019** [Google Scholar](https://scholar.google.com/scholar?q=Recursive+Proof+Composition+without+a+Trusted+Setup)
> 核心思路：基于 Halo 的递归证明，利用承诺聚合降低递归开销。
> 局限与区别：聚合方案只适用于一元多项式，且验证时间线性于迭代次数，无法直接高效应用于多元多项式场景。

[44] Kothapalli et al. Nova: Recursive Zero-Knowledge Arguments from Folding Schemes. **Crypto 2022** [Google Scholar](https://scholar.google.com/scholar?q=Nova+Recursive+Zero-Knowledge+Arguments+from+Folding+Schemes)
> 核心思路：通过折叠方案实现高效的递归零知识论证。
> 局限与区别：作为通用方案，其证明者仍需将 DNN 迭代编码为 R1CS，导致证明生成时间至少比本文慢约 24 倍。

[50] Liu et al. zkCNN: Zero Knowledge Proofs for Convolutional Neural Network Predictions and Accuracy. **CCS 2021** [Google Scholar](https://scholar.google.com/scholar?q=zkCNN+Zero+Knowledge+Proofs+for+Convolutional+Neural+Network+Predictions+and+Accuracy)
> 核心思路：为卷积运算设计优化的 sumcheck 协议，实现子线性证明生成时间。
> 局限与区别：只解决推理问题，未考虑训练；其针对卷积的优化技术被本文采纳用于训练中的前向/反向传播。

[65] Zhang et al. Doubly Efficient Interactive Proofs for General Arithmetic Circuits with Linear Prover Time. **CCS 2021** [Google Scholar](https://scholar.google.com/scholar?q=Doubly+Efficient+Interactive+Proofs+for+General+Arithmetic+Circuits+with+Linear+Prover+Time)
> 核心思路：提出了 Virgo++，一种具有线性证明者时间的 GKR 风格证明系统。
> 局限与区别：作为 baseline 证明系统，其验证者电路规模较大；本文通过递归和聚合技术优化了该系统的递归组合开销。

[63] Xie et al. Orion: Zero Knowledge Proof with Linear Prover Time. **Crypto 2022** [Google Scholar](https://scholar.google.com/scholar?q=Orion+Zero+Knowledge+Proof+with+Linear+Prover+Time)
> 核心思路：基于 Merkle 树的线性时间多项式承诺方案。
> 局限与区别：不支持同态运算；本文为其设计的聚合方案被用于递归证明框架，以线性证明者时间实现多项式承诺的聚合。

[6] Belling et al. Recursion over Public-Coin Interactive Proof Systems; Faster Hash Verification. **CCS 2023** [Google Scholar](https://scholar.google.com/scholar?q=Recursion+over+Public-Coin+Interactive+Proof+Systems+Faster+Hash+Verification)
> 核心思路：将 MiMC 哈希的轮函数直接表示为 sumcheck 实例，降低哈希验证的电路开销。
> 局限与区别：该技术被本文采纳，用于高效处理递归证明中的 Fiat-Shamir 挑战。

### 核心技术与方案

本文提出 Kaizen，一个针对深度神经网络训练的零知识证明系统，由两个核心构建模块组成：优化的梯度下降证明（PoGD）和高效的递归证明组合框架。

**优化的梯度下降证明（PoGD）**：PoGD 针对单次小批量梯度下降迭代，采用 GKR 风格的 sumcheck 证明系统。对于算法中最耗计算的部分——线性运算（如矩阵乘法和卷积），使用已优化的子线性证明方案 [50, 57]：例如，两个 n×n 矩阵的乘法证明者时间仅为 O(n²)，远小于朴素计算的 Θ(n³)；卷积的证明者时间为 O(n² + w²)，也快于计算的 O(n²w²)。对于非线性运算（如 ReLU、Softmax 中的比较和指数），采用标准技术处理：比较操作通过比特分解处理。证明者提供值的二进制表示（含符号位）作为辅助输入，验证者通过 sumcheck 实例检验二进制表示的正确性，如公式 (3) 和 (4) 所示。指数运算使用分段线性近似 [23, 34, 54]。PoGD 分为四个阶段：阶段一验证权重更新；阶段二验证反向传播；阶段三验证前向传播；阶段四通过 sumcheck 协议将前三个阶段中同一多项式（如输入权重）的多个随机评估点组合成一个单一评估，最终由验证者通过多项式承诺的开启验证该评估。该方案满足完备性、知识可靠性（基于 sumcheck 协议和多项式承诺的知识可靠性）和零知识性（通过零知识 sumcheck [16, 62] 和隐藏承诺实现）。证明者时间主要由线性运算的 sumcheck 开销主导，验证者时间则主要由多项式承诺的开启验证开销主导。

**可聚合多项式承诺方案**：为减少递归证明中验证承诺开启的开销，本文提出了一种针对多元多项式的聚合方案。给定一系列承诺 (σ_i) 和评估点 (x_i)，证明者和验证者共同定义一条插值多项式 L: F → F^ℓ，使得 L(i) = x_i。证明者发送多项式 g_i = f_i ∘ L，验证者检查 g_i(i) = y_i。验证者随后发送随机挑战 α_i 和 r，各方令 x* = L(r)，并定义聚合后的多项式 f* = Σ α_i f_i。该方案满足，若 ∃ i 使得 f_i(x_i) ≠ y_i，则证明者必须以高概率发送错误的 g_i，导致最终验证的高概率失败。此方案通过递归插值技术实现线性时间证明者。为达到零知识，证明者需额外发送随机掩码多项式的承诺。对于具体的底层承诺方案（如 Orion [63]），通过检查随机线性组合在承诺矩阵上的编码一致性来实现承诺的聚合。该聚合方案满足完备性、知识可靠性和零知识性，证明者时间 O(k·d^ℓ)，证明大小和验证者时间 O(k d ℓ)。

**递归证明组合框架**：该框架用于将 PoGD 跨多轮迭代组合成简洁的证明。框架的核心是增强函数 F_A，它在每次迭代 i 中执行：验证前一轮的证明 π_{i-1}（通过调用 baseline 验证器 V_b），更新模型参数 z_i = F(z_{i-1}, ω_{i-1})，并输出新的证明 π_i。为了降低 V_b 的电路规模，框架采用以下技术：1）用可聚合承诺方案替代多项式承诺的开启，将本轮和所有历史承诺的开启聚合为单个实例，在最终轮才进行开启验证。2）通过 sumcheck 协议将验证 sumcheck 消息所需的大量布线谓词评估聚合成单个评估，推迟至最后验证。3）使用 sumcheck 友好的哈希函数 MiMC 处理 Fiat-Shamir 挑战，将每轮哈希验证表示为 sumcheck 实例。该框架支持树形递归以应对多项式数量的迭代，避免线性深度递归的攻击。该方案满足 IVC 的完备性和知识可靠性，证明者时间 O(|F| + |z| + |ω|) 每轮，证明大小和验证者时间 O(d·log|F| + log²(|z|+|ω|))。

**Kaizen zkPoT 构造**：Kaizen 将上述递归框架应用于 DNN 训练。模型权重通过多项式承诺提交，数据集通过 Merkle 树提交。每次迭代的电路 C 除了执行梯度下降，还需验证数据批次与公开伪随机排列一致，并打开数据项对应的 Merkle 证明。电路 C 的验证由三部分组成：排列验证由通用 GKR 证明 [65] 处理；Merkle 证明中的哈希计算由 MiMC 的 sumcheck 实例处理；梯度下降由 PoGD 方案处理。Kaizen 满足 zkPoT 的完备性、知识可靠性和零知识性。证明者每轮时间 O(Σ (N s_in,ℓ s_out,ℓ + N q s_out,ℓ))，最终证明大小和验证者时间独立于迭代次数，为 O(Σ (log²(N s_in,ℓ s_out,ℓ) + log²(N q s_out,ℓ)))。

### 核心公式与流程

**[多层GKR的核心等式]**
$$
\begin{array}{l} \widetilde {v} _ {i} (z) = \sum_ {x, y \in \{0, 1 \} ^ {s _ {i + 1}}} \widetilde {a d d} _ {i} (z, x, y) \cdot (\widetilde {v} _ {i + 1} (x) + \widetilde {v} _ {i + 1} (y)) + \\ \widetilde {m u l t} _ {i} (z, x, y) \cdot \widetilde {v} _ {i + 1} (x) \cdot \widetilde {v} _ {i + 1} (y). \tag {1} \\ \end{array}
$$
> 作用：GKR 协议的核心，将第 i 层输出的多元线性扩展表示为第 i+1 层输出的多项式组合，为运行 sumcheck 协议提供基础方程。

**[比特分解一致性检验]**
$$
0 = \sum_ {x \in \{0, 1 \} ^ {\log n}, y \in \{0, 1 \} ^ {\log q}} \widetilde {\beta} _ {x} (r _ {x}) \cdot \widetilde {\beta} _ {y} (r _ {y}) \cdot (\alpha \cdot \widetilde {z} _ {\text { Sign }} (x) \cdot (1 - \widetilde {z} _ {\text { Sign }} (x)) + \widetilde {Z} _ {\text { Bit }} (x, y) \cdot (1 - \widetilde {Z} _ {\text { Bit }} (x, y))). \tag {3}
$$
> 作用：通过 sumcheck 协议，在随机挑战下检验证明者提供的比特位分解矩阵 Z_Bit 和符号向量 z_Sign 是否均为二元值。

**[标的分解正确性检验]**
$$
\widetilde {z} (r _ {z}) = \sum_ {x \in \{0, 1 \} ^ {\log n}, y \in \{0, 1 \} ^ {\log q}} \widetilde {\beta} _ {x} (r _ {z}) \cdot \widetilde {Z} _ {\text { Bit }} (x, y) \cdot (1 - 2 \cdot \widetilde {z} _ {\mathrm{Sign}} (x)) \cdot 2 ^ {y}. \qquad (4)
$$
> 作用：通过 sumcheck 协议，在另一个随机挑战 r_z 下，检验证明者提供的比特分解是否正确表示了原始值 z。

**[多个多项式评估的聚合]**
$$
\sum_ {i = 1} ^ {k} \alpha_ {i} \cdot y _ {i} = \sum_ {z \in \{0, 1 \} ^ {\ell}} f (z) \cdot \sum_ {i = 1} ^ {k} \alpha_ {i} \cdot \widetilde {\beta} _ {z} (x _ {i}). \tag {5}
$$
> 作用：利用 sumcheck 协议，将针对同一个多项式 f 的 k 个不同坐标的评估值请求，通过随机线性组合聚合成单个评估请求，用于减小 PoGD 的验证开销。

**[哈希轮函数验证]**
$$
\widetilde {v} _ {0} (r _ {0}) = \sum_ {z \in \{0, 1 \} ^ {\log n}} \widetilde {\beta} _ {z} (r _ {0}) \cdot (\widetilde {v} _ {1} (z) + k _ {1}) ^ {3}, \tag {6}
$$
> 作用：将 MiMC 哈希单轮函数 F_i(x) = (x + k_i)^3 的验证表示为 sumcheck 实例，从而在递归证明中高效处理哈希验证。

**[多项式承诺聚合协议，Protocol 4概要]**
1. P和V定义插值多项式L满足L(i) = x_i。
2. P发送 g_i = (f_i + β_i h_i) ∘ L，V检查 g_i(i) = y_i + β_i v_i。
3. V发送随机挑战α_i, r。
4. 各方定义 x* = L(r)，f* = Σ α_i f_i + α_i β_i h_i。P通过承诺的线性编码性质聚合σ_i得到σ*（如检查C*_2 = Σ α_i C_i,2 的随机列一致性）。
> 作用：将k个承诺/评估对(σ_i, x_i, y_i)聚合为一个(σ*, x*, y*)，实现线性证明者时间、对数验证者时间的聚合，是递归框架的关键模块。

### 实验结果
实验在 Linux 虚拟机（8 个 2.80GHz Intel Xeon Platinum 8370 CPU，512GB RAM）上进行，选取了 LeNet (6.1万参数)、AlexNet (420万参数) 和 VGG-11 (1000万参数) 三种模型，分别使用 MNIST 和 CIFAR-10 数据集，训练批量大小 N 从 4 到 16。对于 VGG-11 (N=16)，PoGD 的 sumcheck 消息生成时间为 179.4 秒，占全部证明时间的一部分。在 Kaizen 系统中，采用树形递归（arity=12，深度=4，支持最多 20736 次迭代），使用 MiMC 哈希和 SHA-256，以及 Orion 多项式承诺。VGG-11 (N=16) 的摊销每轮证明时间为 882 秒（含 PoGD 的 182.2 秒和递归开销），最大内存使用 466.3GB。证明大小为 1.627MB，验证时间仅为 130 毫秒，两者均独立于迭代次数。与通用 IVC 方案对比（Nova [44]），Kaizen 在 VGG-11 上证明者速度快 23.7 倍，内存效率高 27 倍。文本强调未并行化，且未实现零知识扩展，因后者仅需在最终轮应用，摊销成本可忽略。进一步比较中，对于 LeNet，Kaizen 证明者比 Nova 快 6.9-16.1 倍，节省 30.7-56.2 倍内存。

### 局限性与开放问题
尽管 Kaizen 在性能上取得了显著突破，但其 466.3GB 的最大内存使用量对于资源受限的设备仍然过高，限制了其在边缘计算等场景的应用。目前的实现未利用并行化优化，进一步的多线程或 GPU 加速有望显著降低证明时间。此外，论文未处理分布式训练中多个证明者并行工作并聚合证明的场景，这也为未来的工作提供了方向。

### 强关联论文

[40] Jia et al. Proof-of-Learning: Definitions and Practice. **IEEE S&P 2021** [Google Scholar](https://scholar.google.com/scholar?q=Proof-of-Learning+Definitions+and+Practice)

[34] Garg et al. Experimenting with Zero-Knowledge Proofs of Training. **CCS 2023** [Google Scholar](https://scholar.google.com/scholar?q=Experimenting+with+Zero-Knowledge+Proofs+of+Training)

[50] Liu et al. zkCNN: Zero Knowledge Proofs for Convolutional Neural Network Predictions and Accuracy. **CCS 2021** [Google Scholar](https://scholar.google.com/scholar?q=zkCNN+Zero+Knowledge+Proofs+for+Convolutional+Neural+Network+Predictions+and+Accuracy)

[65] Zhang et al. Doubly Efficient Interactive Proofs for General Arithmetic Circuits with Linear Prover Time. **CCS 2021** [Google Scholar](https://scholar.google.com/scholar?q=Doubly+Efficient+Interactive+Proofs+for+General+Arithmetic+Circuits+with+Linear+Prover+Time)

[63] Xie et al. Orion: Zero Knowledge Proof with Linear Prover Time. **Crypto 2022** [Google Scholar](https://scholar.google.com/scholar?q=Orion+Zero+Knowledge+Proof+with+Linear+Prover+Time)

[17] Bowe et al. Recursive Proof Composition without a Trusted Setup. **Cryptology ePrint Archive 2019** [Google Scholar](https://scholar.google.com/scholar?q=Recursive+Proof+Composition+without+a+Trusted+Setup)

[44] Kothapalli et al. Nova: Recursive Zero-Knowledge Arguments from Folding Schemes. **Crypto 2022** [Google Scholar](https://scholar.google.com/scholar?q=Nova+Recursive+Zero-Knowledge+Arguments+from+Folding+Schemes)

[26] Chiesa et al. Fractal: Post-quantum and Transparent Recursive Proofs from Holography. **Eurocrypt 2020** [Google Scholar](https://scholar.google.com/scholar?q=Fractal+Post-quantum+and+Transparent+Recursive+Proofs+from+Holography)

[6] Belling et al. Recursion over Public-Coin Interactive Proof Systems; Faster Hash Verification. **CCS 2023** [Google Scholar](https://scholar.google.com/scholar?q=Recursion+over+Public-Coin+Interactive+Proof+Systems+Faster+Hash+Verification)

[57] Thaler. Time-Optimal Interactive Proofs for Circuit Evaluation. **Crypto 2013** [Google Scholar](https://scholar.google.com/scholar?q=Time-Optimal+Interactive+Proofs+for+Circuit+Evaluation)


## 关键词

+ 零知识证明
+ 深度神经网络
+ 梯度下降
+ GKR证明系统
+ 多项式承诺
+ 模型训练验证