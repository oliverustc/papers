---
title: "Experimenting with Zero-Knowledge Proofs of Training"
doi: 10.1145/3576915.3623202
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2023

modified: 2025-05-07 22:29:10
created: 2025-04-07 16:28:24
---
## Experimenting with Zero-Knowledge Proofs of Training

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3576915.3623202)

## 作者

+ [Sanjam Garg](Sanjam%20Garg.md)
+ [Aarushi Goel](Aarushi%20Goel.md)
+ Somesh Jha
+ Saeed Mahloujifar
+ Mohammad Mahmoody
+ [Guru-Vamsi Policharla](Guru-Vamsi%20Policharla.md)
+ [Mingyuan Wang](Mingyuan%20Wang.md)

## 笔记

### 背景与动机
训练机器学习模型的实体常需证明其训练过程符合特定规范（如公平性或隐私保护），同时又要保护底层数据集和最终模型的机密性。例如，提供模型即服务的所有者可能被指控未采取必要的安全措施，或在所有权纠纷中需自证清白。简单的证明方案要么泄露数据，要么与保护隐私的目标相悖。现有密码学证明系统虽理论上可用于任何计算，但直接应用存在严重瓶颈：通用零知识证明系统（如zkSNARKs）的证明生成时间极慢（至少千倍以上开销），且需将整个计算迹加载至内存，这对涉及海量数据的机器学习训练极不现实；而MPC-in-the-head风格的证明虽生成高效，但证明大小和验证时间与训练电路规模线性相关，通信开销巨大。本文旨在填补这一理论与实践间的空白，针对逻辑回归提出一种同时实现合理证明生成时间与亚线性证明大小的零知识证明训练（zkPoT）协议。

### 相关工作

[7] Scott Ames, Carmit Hazay, Yuval Ishai, and Muthuramakrishnan Venkitasubramaniam. Ligero: Lightweight Sublinear Arguments Without a Trusted Setup. **CCS 2017** [Google Scholar](https://scholar.google.com/scholar?q=Ligero%20Lightweight%20Sublinear%20Arguments%20Without%20a%20Trusted%20Setup)
> 核心思路：基于MPC-in-the-head与线性纠错码，设计了首个无需可信设置、证明大小亚线性于电路规模的通用零知识证明系统。
> 局限与区别：其证明大小对于大型训练电路仍然过大，且证明生成和验证时间在训练场景下开销较高。

[11] Rishabh Bhadauria, Zhiyong Fang, Carmit Hazay, Muthuramakrishnan Venkitasubramaniam, Tiancheng Xie, and Yupeng Zhang. Ligero++: A New Optimized Sublinear IOP. **CCS 2020** [Google Scholar](https://scholar.google.com/scholar?q=Ligero%20++%20A%20New%20Optimized%20Sublinear%20IOP)
> 核心思路：对Ligero进行了多项优化，显著提升了证明生成和验证的效率。
> 局限与区别：仅对线性回归的闭式解提供高精度证明，无法处理逻辑回归等无闭式解的模型；对2000个样本的训练数据集即因内存耗尽而失败，本文的方法可处理更大规模数据。

[39] Jens Groth. On the Size of Pairing-Based Non-interactive Arguments. **EUROCRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=On%20the%20Size%20of%20Pairing-Based%20Non-interactive%20Arguments)
> 核心思路：提出了Groth16协议，一种极为简洁的zkSNARK，证明大小仅包含3个群元素。
> 局限与区别：证明生成（包括大量椭圆曲线运算和FFT）的开销极高，且需要将整个电路计算迹加载至内存，完全无法满足大规模训练场景。

[41] Yuval Ishai, Eyal Kushilevitz, Rafail Ostrovsky, and Amit Sahai. Zero-knowledge from secure multiparty computation. **STOC 2007** [Google Scholar](https://scholar.google.com/scholar?q=Zero-knowledge%20from%20secure%20multiparty%20computation)
> 核心思路：开创性地提出MPC-in-the-head范式，通过模拟安全多方计算协议来构建零知识证明。
> 局限与区别：经典实现中，证明大小与计算电路规模呈线性关系，不适合计算量巨大的机器学习训练。

[42] Hengrui Jia, Mohammad Yaghini, Christopher A Choquette-Choo, Natalie Dullerud, Anvith Thudi, Varun Chandrasekaran, and Nicolas Papernot. Proof-of-learning: Definitions and practice. **IEEE S&P 2021** [Google Scholar](https://scholar.google.com/scholar?q=Proof-of-learning%20Definitions%20and%20practice)
> 核心思路：定义了“学习证明”的概念，旨在证明敌手为生成证明需支付至少与诚实训练相当的算力成本（即诚实验证）。
> 局限与区别：不提供零知识性质，会泄露模型或数据；其证明易被伪造，无法作为正确性的密码学证明，与本文的zkPoT目标不同。

[50] Tianyi Liu, Xiang Xie, and Yupeng Zhang. zkCNN: Zero Knowledge Proofs for Convolutional Neural Network Predictions and Accuracy. **CCS 2021** [Google Scholar](https://scholar.google.com/scholar?q=zkCNN%20Zero%20Knowledge%20Proofs%20for%20Convolutional%20Neural%20Network%20Predictions%20and%20Accuracy)
> 核心思路：专门为卷积神经网络的推理设计高效的零知识证明系统。
> 局限与区别：目标为推理而非训练，训练的计算量远大于推理；其证明生成开销约为推理时间的1500倍，本文方案的开销约为训练时间的数百倍，且更适用于训练任务。

[54] Payman Mohassel and Peter Rindal. ABY3: A Mixed Protocol Framework for Machine Learning. **CCS 2018** [Google Scholar](https://scholar.google.com/scholar?q=ABY3%20A%20Mixed%20Protocol%20Framework%20for%20Machine%20Learning)
> 核心思路：提出了一个三方混合安全计算协议框架，为包括逻辑回归在内的多种机器学习任务提供了高效实现。
> 局限与区别：针对的是多方之间协同计算而非单方证明；其MPC协议中的技巧（如定点算术、分段线性激活函数）被本文用来构建内部MPC协议。

### 核心技术与方案

本文的核心贡献在于提出一种组合框架，结合MPC-in-the-head与zkSNARKs两种技术，以获得在证明生成时间和证明大小间的理想权衡，并实例化出一个针对逻辑回归的zkPoT协议。
1. **总体框架与设计思路**：将训练计算分为两类操作——算术操作（如矩阵乘法）和非算术操作（如定点算术中的截断、分段线性激活函数评估）。对于非算术操作，使用定制的MPC-in-the-head风格ZK证明，因其在处理这类操作时开销较小。对于算术操作，则利用zkSNARKs技术来生成简洁的证明，从而控制证明大小。关键在于，将两种证明系统通过一种新型的组合方式集成，使得协议整体保持流式友好性，无需将整个计算迹常驻内存。
2. **内部MPC协议设计**：为实现MPC-in-the-head，本文设计了一个针对逻辑回归的、在预处理模型下的安全多方计算协议。该协议使用打包秘密共享（Packed Secret Sharing）[31]来打包多个秘密，使得每个参与方的视图大小与计算规模呈亚线性关系。协议分为预处理和在线两阶段。预处理阶段由一个“可信实体”（在ZK证明中即证明者）生成相关性随机数和数据的两种不同方向的打包秘密共享。在线阶段，各方基于秘密共享的权重和数据，执行安全的梯度下降计算，其中非算术操作（如截断）利用预处理生成的随机掩码来实现。此MPC协议本身的通信复杂度与数据集大小呈亚线性关系。
3. **zkSNARK子程序**：为了验证“可信实体”是否诚实地执行了预处理阶段，证明者需使用一系列零知识子程序来证明关于共享和秘密的特定关系。这些子程序包括：
   * **一致性检查**：验证秘密共享是正确打包且与承诺的秘密一致。
   * **相关性检查**：验证不同阈值下的随机值秘密共享的关联性。
   * **范围检查**：验证截断掩码是否在正确范围内。
   * **数据一致性检查**：验证数据集的行方向打包共享与列方向打包共享之间满足转置关系。这些子程序均基于多项式承诺和Sumcheck协议设计，其证明大小和验证时间在数据规模上呈亚线性或对数级。
4. **最终zkPoT协议**：协议的整体流程如下：证明者首先执行MPC协议中的预处理步骤，并通过上述zkSNARK子程序向验证者证明该步骤的诚实性。然后，证明者“在脑中”模拟MPC协议的在线阶段，并承诺所有虚拟参与方的视图。验证者随机选择一部分参与方的视图要求打开。不同于经典的MPC-in-the-head，证明者并非直接发送这些视图的明文。对于那些包含大量数据共享的视图部分（尺寸为$O(ND)$），证明者提供多项式承诺，并利用一个将多个内积验证合并为单个多项式查询的技术，使验证者能高效验证计算的正确性，从而通信复杂度降至$O(N)$。对于视图中尺寸为$O(N)$的通信部分，则直接通过MPC-in-the-head的检查机制进行验证。系统整体的计算复杂度，证明者为$O(ND\log N)$，验证者为$O(N)$（亚线性于数据量$ND$），证明大小则为$O(N)$。

### 核心公式与流程

**训练算法（随机梯度下降，单次迭代）**
$$
\mathbf{w}_{j} \leftarrow \mathbf{w}_{j - 1} - \frac{a}{B} \cdot \mathbf{X}_{j}^{\intercal} \times \left(f\left(\mathbf{X}_{j} \times \mathbf{w}_{j - 1}\right) - \mathbf{y}_{j}\right)
$$
> 作用：定义了逻辑回归的随机梯度下降核心迭代公式，其中 $\mathbf{w}_j$ 为第 $j$ 步的权重向量，$a$ 为学习率，$B$ 为批次大小，$\mathbf{X}_j$ 和 $\mathbf{y}_j$ 为第 $j$ 个批次的数据特征和标签。$f$ 为激活函数。

**分段线性激活函数**
$$
f(x) = \left\{ \begin{array}{l l} 0 & x < -1/2 \\ x + 1/2 & -1/2 \leqslant x < 1/2 \\ 1 & 1/2 \leqslant x \end{array} \right.
$$
> 作用：使用分段线性函数近似Sigmoid函数，以在MPC环境中高效计算，避免了计算昂贵的指数运算。

**打包秘密共享（核心思想）**
$$
\forall i \in [n], \ \text{share}_i = f(\alpha_i), \ \text{where} \ f(\alpha_0)=s_1, f(\alpha_{-1})=s_2, \ldots, f(\alpha_{-(\ell-1)}) = s_\ell
$$
> 作用：定义了如何将 $\ell$ 个秘密 $s_1,\dots,s_\ell$ 打包到一个度-$(t)$ 的多项式 $f$ 中，并生成 $n$ 个参与方的分享。这允许一次秘密共享过程传输多个秘密，极大减少了通信开销。

**零知识子程序：数据一致性检查（Schwartz-Zippel检验）**
$$
\left(r \cdot \overrightarrow{\alpha}, r^2 \cdot \overrightarrow{\alpha}, \ldots, r^{N/B} \cdot \overrightarrow{\alpha}\right) A \overrightarrow{\beta} \stackrel{?}{=} \left(r \cdot \overrightarrow{\beta}, r^2 \cdot \overrightarrow{\beta}, \ldots, r^{N/B} \cdot \overrightarrow{\beta}\right) B \overrightarrow{\alpha}
$$
> 作用：用于检验行方向打包的数据矩阵 $A$ 和列方向打包的数据矩阵 $B$ 是否满足“特殊转置”关系（即 $A$ 的行对应 $B$ 的列的转置）。通过引入随机向量 $\vec{\alpha}, \vec{\beta}$ 和随机标量 $r$，将多个转置关系检查压缩为单个等式，若等式成立，则根据Schwartz-Zippel引理，两矩阵以高概率满足所需关系。

### 实验结果

实验在配备512 GB内存的单线程GCP N2实例上进行，所有算术操作基于128位素数域（$p = 2^{128} - 45 * 2^{40} + 1$）。测试数据集包含262,144条记录（约4 GB），每条记录含1024个特征，用于训练逻辑回归模型。协议被划分为三个阶段：离线阶段（数据无关）、数据检查阶段（仅依赖数据）和在线阶段（依赖数据与模型）。实验结果显示：在线阶段证明生成时间为518秒，验证时间24秒，证明大小196 MB；数据检查阶段证明生成时间3690秒，验证时间2.5秒，证明大小5.3 MB；离线阶段证明大小预估小于140 MB。总证明大小小于350 MB（占数据集的不到10%）。作为对比，在f64数据类型上纯训练耗时约1秒，在128位域上耗时约11.5秒。在线阶段的密码学开销约为纯优化训练的518倍，相对128位域训练为45倍；所有计算（不含预处理）的总开销分别为4200倍和366倍。相较于使用Groth16等现成zkSNARK完全不可行（如Ligero++在2000个样本时即内存不足），本文的方案在内存友好性和实际可行性上取得了显著优势。

### 局限性与开放问题
本文的方案存在若干局限性。首先，为了效率，协议对训练算法做了修改，包括使用分段线性函数近似激活函数和采用定点算术，这可能对模型精度有轻微影响。其次，尽管证明大小已优化至亚线性，但仍然不是常数大小，在特定带宽敏感场景下可能仍是一个瓶颈。最后，当前工作仅针对逻辑回归进行了实例化，虽然作者认为其技术可扩展到更复杂的模型，但具体实现和优化仍是一个开放问题。未来工作可以探索将本框架扩展到卷积神经网络等更深层次的模型，并研究如何将其与硬件加速结合以进一步降低密码学开销。

### 强关联论文

[11] Rishabh Bhadauria, Zhiyong Fang, Carmit Hazay, Muthuramakrishnan Venkitasubramaniam, Tiancheng Xie, and Yupeng Zhang. Ligero++: A New Optimized Sublinear IOP. **CCS 2020** [Google Scholar](https://scholar.google.com/scholar?q=Ligero%20%2B%2B%20A%20New%20Optimized%20Sublinear%20IOP)

[20] Octavian Catrina and Amitabh Saxena. Secure Computation with Fixed-Point Numbers. **FC 2010** [Google Scholar](https://scholar.google.com/scholar?q=Secure%20Computation%20with%20Fixed-Point%20Numbers)

[31] Matthew K. Franklin and Moti Yung. Communication Complexity of Secure Computation (Extended Abstract). **STOC 1992** [Google Scholar](https://scholar.google.com/scholar?q=Communication%20Complexity%20of%20Secure%20Computation%20(Extended%20Abstract))

[39] Jens Groth. On the Size of Pairing-Based Non-interactive Arguments. **EUROCRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=On%20the%20Size%20of%20Pairing-Based%20Non-interactive%20Arguments)

[41] Yuval Ishai, Eyal Kushilevitz, Rafail Ostrovsky, and Amit Sahai. Zero-knowledge from secure multiparty computation. **STOC 2007** [Google Scholar](https://scholar.google.com/scholar?q=Zero-knowledge%20from%20secure%20multiparty%20computation)

[42] Hengrui Jia, Mohammad Yaghini, Christopher A Choquette-Choo, Natalie Dullerud, Anvith Thudi, Varun Chandrasekaran, and Nicolas Papernot. Proof-of-learning: Definitions and practice. **IEEE S&P 2021** [Google Scholar](https://scholar.google.com/scholar?q=Proof-of-learning%20Definitions%20and%20practice)

[50] Tianyi Liu, Xiang Xie, and Yupeng Zhang. zkCNN: Zero Knowledge Proofs for Convolutional Neural Network Predictions and Accuracy. **CCS 2021** [Google Scholar](https://scholar.google.com/scholar?q=zkCNN%20Zero%20Knowledge%20Proofs%20for%20Convolutional%20Neural%20Network%20Predictions%20and%20Accuracy)

[54] Payman Mohassel and Peter Rindal. ABY3: A Mixed Protocol Framework for Machine Learning. **CCS 2018** [Google Scholar](https://scholar.google.com/scholar?q=ABY3%20A%20Mixed%20Protocol%20Framework%20for%20Machine%20Learning)

[64] Adi Shamir. How to Share a Secret. **CACM 1979** [Google Scholar](https://scholar.google.com/scholar?q=How%20to%20Share%20a%20Secret)


## 关键词

+ 零知识证明
+ 机器学习
+ 模型训练
+ 隐私保护
+ 数据隐私