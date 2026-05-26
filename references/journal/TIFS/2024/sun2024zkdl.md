---
title: "zkDL: Efficient Zero-Knowledge Proofs of Deep Learning Training"
标题简称: zkDL
论文类型: journal
期刊简称: TIFS
发表年份: 2024
modified: 2025-04-09 09:24:45
---

## zkDL: Efficient Zero-Knowledge Proofs of Deep Learning Training

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/10810453)

## 作者

+ [Haochen Sun](Haochen%20Sun.md)
+ Tonghe Bai
+ Jason Li
+ Hongyang Zhang

## 笔记

### 背景与动机
深度学习训练过程的真实性验证日益重要，尤其在监管合规和知识产权保护背景下。训练数据的隐私性要求验证者不能直接访问模型参数和数据，因此需要一个零知识证明系统。现有工作主要集中在推理阶段的验证 [12][26][37][38]，而训练阶段的验证面临两大瓶颈：非算术操作（如ReLU激活函数）难以融入ZKP框架，以及训练过程包含大量串行步骤，导致证明复杂度极高。早期工作 [10][45] 局限于线性回归等简单模型，或使用平方激活函数等替代方案。本文旨在填补这一空白，提出首个可扩展到百万级参数网络规模的零知识训练证明系统。

### 相关工作

[12] Feng等. ZEN: Efficient Zero-Knowledge Proofs for Neural Networks. **CCS 2021** [Google Scholar](https://scholar.google.com/scholar?q=ZEN%3A%20Efficient%20Zero-Knowledge%20Proofs%20for%20Neural%20Networks)
> 核心思路：基于zk-SNARK的神经网络推理验证系统。
> 局限与区别：仅支持推理阶段，无法处理训练过程中ReLU的反向传播。

[26] Liu等. ZkCNN: Zero Knowledge Proofs for Convolutional Neural Network Predictions and Accuracy. **CCS 2021** [Google Scholar](https://scholar.google.com/scholar?q=ZkCNN%3A%20Zero%20Knowledge%20Proofs%20for%20Convolutional%20Neural%20Network%20Predictions%20and%20Accuracy)
> 核心思路：基于GKR协议的卷积神经网络推理验证，支持VGG规模。
> 局限与区别：不适用于训练过程，且未处理ReLU反向传播的证明。

[45] Zhao等. VeriML: Enabling Integrity Assurances and Fair Payments for Machine Learning as a Service. **TPDS 2021** [Google Scholar](https://scholar.google.com/scholar?q=VeriML%3A%20Enabling%20Integrity%20Assurances%20and%20Fair%20Payments%20for%20Machine%20Learning%20as%20a%20Service)
> 核心思路：首个零知识可验证训练框架，支持线性回归等基础算法。
> 局限与区别：使用平方激活替代ReLU，不适用于标准深度神经网络。

[18] Goldwasser等. Delegating Computation: Interactive Proofs for Muggles. **STOC 2008** [Google Scholar](https://scholar.google.com/scholar?q=Delegating%20Computation%3A%20Interactive%20Proofs%20for%20Muggles)
> 核心思路：提出GKR协议，利用sumcheck协议验证算术电路的正确计算。
> 区别：本文扩展GKR到聚合式证明，通过FAC4DNN将多层多步训练实例平行化。

[36] Wahby等. Doubly-Efficient zkSNARKs without Trusted Setup. **S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Doubly-Efficient%20zkSNARKs%20without%20Trusted%20Setup)
> 核心思路：提出Hyrax承诺方案，承诺和验证开销为平方根级。
> 应用：本文使用Hyrax实现承诺聚合，证明总尺寸从线性降至平方根级改进。

[10] Eisenhofer等. Verifiable and Provably Secure Machine Unlearning. **arXiv 2022** [Google Scholar](https://scholar.google.com/scholar?q=Verifiable%20and%20Provably%20Secure%20Machine%20Unlearning)
> 核心思路：提供正确训练执行和更新的可验证性证明。
> 局限：仅支持有限规模神经网络，且绕过ReLU等非算术操作。

### 核心技术与方案

**1. zkReLU：针对ReLU的非算术操作证明**

本文的核心创新在于将ReLU及其反向传播转化为可验证的算术关系。对于前向传播中的ReLU操作 $A = \text{ReLU}(Z)$ 和反向传播中的 $\text{Ind}(Z \geq 0)$ 梯度计算，传统方法直接验证需要非算术比较。zkReLU引入辅助输入 $aux$，包含绝对值 $Z'$ 和符号位 $S_Z$，使得ReLU的正反向传播可以用四个算术方程（公式1-4）表示。关键观察是，这些方程可以通过Schwartz-Zippel引理 [30][46] 用随机线性组合压缩成一个方程（公式5），从而在一次sumcheck中验证。为了防止恶意构造，zkReLU还需确认aux是二进制张量（AIVP验证公式34），确保所有位值均为0或1。

**2. FAC4DNN：扁平化算术电路设计**

zkReLU的引入导致各层间的算术连接被彻底打断——每个训练步骤的每一层都被描绘成独立单位（图1c）。这一“缺点”被FAC4DNN转化为优势：因为所有单位都共享相同的算术关系C（公式6），整个训练过程的正确性可以表示为所有单位的合取（公式7），进而等价于一个更宽更深但逻辑上平行的电路$\overline{C}$（公式8）。这意味着不同层和不同训练步骤的张量可以被堆叠（stacking）成三维张量，然后用聚合的sumcheck协议一次性验证所有实例。

对于N个相同维度的矩阵乘法实例，本文设计了一个专门的sumcheck协议（公式9-11）。具体来说，通过验证者提供的随机向量w、u1、u3，证明者需要证明堆叠后的三维张量满足一个包含求和运算的等式。执行sumcheck的第一步压缩了N个实例维度，将证明简化为单实例矩阵乘法的验证，从而将证明尺寸从N个独立证明的O(N log D)降低为O(log N + log D)。类似地，Hadamard积等其他张量操作也被设计出对应的聚合sumcheck格式（公式45-46）。

**3. 聚合证明与紧致承诺**

FAC4DNN的聚合机制不仅减少了沟通开销，还直接降低了承诺尺寸。使用Hyrax承诺 [36] 时，单张量的承诺尺寸为平方根级。当N个同类张量被堆叠为一个三维张量后，承诺尺寸从$\sum_i O(\sqrt{|T_i|})$下降为$O(\sqrt{N|T_i|})$，从而获得$\sqrt{N}$倍的承诺尺寸缩减。类似地，聚合后的证明尺寸从O(N log D)降至O(log N + log D)，验证时间也从O(N)降至$O(N/\sqrt{T'})$（表I）。

**4. 安全保障**

协议1满足：perfect completeness（诚实证明者必然通过验证）、negligible soundness error（作弊证明者几乎不可能通过验证）以及zero-knowledge（使用零知识sumcheck [6][41][42] 和Pedersen承诺后，验证者无法获得私有数据信息）。安全性依赖承诺方案的$\lambda$位安全性和域大小$\Omega(2^{2\lambda})$。最终系统为128位安全（BLS12-381曲线）。

### 核心公式与流程

**[ReLU正反向传播的算术化]**
$$
\begin{aligned}
\mathbf{A} &= (\mathbf{1} - \mathbf{B}_{Q-1}) \odot \mathbf{Z}' \\
\mathbf{Z} &= 2^R \mathbf{Z}' + \mathbf{R}_\mathbf{Z} \\
\mathbf{G}_\mathbf{Z} &= (\mathbf{1} - \mathbf{B}_{Q-1}) \odot \mathbf{G}_\mathbf{A}' \\
\mathbf{G}_\mathbf{A} &= 2^R \mathbf{G}_\mathbf{A}' + \mathbf{R}_{\mathbf{G}_\mathbf{A}}
\end{aligned}
$$
> 作用：将ReLU及其梯度的验证转化为仅涉及加、减、乘的算术关系，每个关系均可通过sumcheck协议验证。

**[随机线性组合压缩验证]**
$$
\mathbf{Z} + r\mathbf{A} + r^2\mathbf{G}_\mathbf{Z} = ((2+r)\mathbf{Z}' + r^2 \mathbf{G}_\mathbf{A}') \odot \mathbf{S}_\mathbf{Z}
$$
> 作用：通过Schwartz-Zippel引理结合随机数r，将4个方程压缩为一个方程，降低通信轮数，仅需一次sumcheck即可验证整个zkReLU。

**[聚合矩阵乘法sumcheck]**
$$
\widetilde{\mathbf{Y}}(\mathbf{w}, \mathbf{u}_0, \mathbf{u}_1) = \sum_{\mathbf{n}} \sum_{\mathbf{i}} \widetilde{\beta}(\mathbf{w}, \mathbf{n}) \widetilde{\mathbf{X}}_0(\mathbf{n}, \mathbf{u}_0, \mathbf{i}) \widetilde{\mathbf{X}}_1(\mathbf{n}, \mathbf{i}, \mathbf{u}_1)
$$
> 作用：实现对N个矩阵乘法实例的一次性证明。首先对$\mathbf{n}$执行sumcheck，将问题压缩为单个矩阵乘法的验证。

**[索引偏移解决]**
$$
\sum_{k=0}^{K-1} r_k \widetilde{\mathbf{X}}_k(\mathbf{u}_k, \mathbf{u}) = \sum_{i=0}^{N-1} \left( \sum_{k=0}^{K-1} \sum_{j=0}^{N_k-1} r_k \widetilde{\beta}(\mathbf{u}_k, j) p_k(i, j) \right) \widetilde{\mathbf{X}}(i, \mathbf{u})
$$
> 作用：解决因不同层跳过（如第一层不计算$\mathbf{G}_\mathbf{A}^{(1)}$）导致的索引偏移，保证堆叠后的张量能够正确重索引并验证。

### 实验结果

实验在配备Tesla A100 GPU和128GB内存的节点上进行，使用CUDA实现的BLS12-381曲线（128位安全）和CIFAR-10数据集。被验证的网络是8层隐藏层全连接网络，每层1024个神经元，总参数量超过1000万，激活函数为ReLU。与前工作不同，没有现有方案支持该量级的可验证训练，因此baseline是与其自身全序列验证和非聚合变体比较。在批量大小64、聚合步数1024时，每步证明生成时间仅0.86秒，证明尺寸0.033kB，验证时间0.19秒。相比之下，无聚合的序列方案的证明生成时间为47秒，证明尺寸82kB，验证时间42秒。聚合增益显著：√聚合步数增加10倍时，每步证明尺寸降低约√334倍，验证时间降低约3倍。系统的QT位数设置为$2^{15}$量化界，使用$2^{16}$缩放系数以防止溢出。

### 局限性与开放问题
zkDL目前专注于全连接网络和ReLU激活，尚未支持注意力机制、Transformer、扩散模型等现代架构。训练过程中dropout、噪声注入等随机操作尚未在证明原型中体现。实现方面，单GPU限制了更大规模网络的聚合上限，扩展至多GPU分布式证明是合理方向。验证时间相对接近证明时间，表明验证环节的并行化优化仍有改进空间。

### 强关联论文

[26] T. Liu, X. Xie, and Y. Zhang. ZkCNN: Zero Knowledge Proofs for Convolutional Neural Network Predictions and Accuracy. **CCS 2021** [Google Scholar](https://scholar.google.com/scholar?q=ZkCNN%3A%20Zero%20Knowledge%20Proofs%20for%20Convolutional%20Neural%20Network%20Predictions%20and%20Accuracy)

[18] S. Goldwasser, Y. T. Kalai, and G. N. Rothblum. Delegating Computation: Interactive Proofs for Muggles. **STOC 2008** [Google Scholar](https://scholar.google.com/scholar?q=Delegating%20Computation%3A%20Interactive%20Proofs%20for%20Muggles)

[36] R. S. Wahby, I. Tzialla, A. Shelat, J. Thaler, and M. Walfish. Doubly-Efficient zkSNARKs without Trusted Setup. **S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Doubly-Efficient%20zkSNARKs%20without%20Trusted%20Setup)

[45] L. Zhao, Q. Wang, C. Wang, Q. Li, C. Shen, and B. Feng. VeriML: Enabling Integrity Assurances and Fair Payments for Machine Learning as a Service. **TPDS 2021** [Google Scholar](https://scholar.google.com/scholar?q=VeriML%3A%20Enabling%20Integrity%20Assurances%20and%20Fair%20Payments%20for%20Machine%20Learning%20as%20a%20Service)

[10] T. Eisenhofer, D. Riepel, V. Chandrasekaran, E. Ghosh, O. Ohrimenko, and N. Papernot. Verifiable and Provably Secure Machine Unlearning. **arXiv 2022** [Google Scholar](https://scholar.google.com/scholar?q=Verifiable%20and%20Provably%20Secure%20Machine%20Unlearning)

[12] B. Feng, L. Qin, Z. Zhen-fei, Y. Ding, and S. Chu. ZEN: Efficient Zero-Knowledge Proofs for Neural Networks. **IACR ePrint 2021** [Google Scholar](https://scholar.google.com/scholar?q=ZEN%3A%20Efficient%20Zero-Knowledge%20Proofs%20for%20Neural%20Networks)


## 关键词

+ zkDL深度学习训练零知识证明
+ zkReLU激活函数反向传播证明
+ FAC4DNN神经网络算术电路
+ CUDA张量结构聚合证明
+ 深度学习训练完整性验证
+ 百万参数规模可扩展ZKP