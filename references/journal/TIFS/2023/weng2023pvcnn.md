---
title: "pvCNN: Privacy-Preserving and Verifiable  Convolutional Neural Network Testing"
标题简称:
论文类型: journal
期刊简称: TIFS
发表年份: 2023

modified: 2025-04-10 17:03:23
---

## pvCNN: Privacy-Preserving and Verifiable  Convolutional Neural Network Testing

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/10086653)

## 作者

+ [Jiasi Weng](Jiasi%20Weng.md)
+ Jian Weng
+ Gui Tang
+ Anjia Yang
+ Ming Li
+ Jia-Nan Liu

## 笔记

### 背景与动机
卷积神经网络（CNN）在安全关键场景（如自动驾驶、人脸识别）中的错误决策可能造成灾难性后果，因此用户迫切需要对其多维度性能（鲁棒性、公平性等）进行可信测试。黑盒测试虽能保护模型参数隐私，但其有效性高度依赖多源测试数据，而构建多样化的测试集需多方协作（如Google的CATS4ML项目）。与此同时，不可信的模型开发者可能伪造测试结果，甚至根据已知测试数据调整模型，导致性能评估失真。因此，需要一个方案使用户能够验证黑盒CNN测试的正确性，同时保护测试数据和模型参数的隐私。现有基于密码学证明的工作（如SafetyNets [10]、vCNN [12]、ZEN [13]等）在公开可验证性、隐私保护、批处理证明等方面存在不足，无法同时满足本文所设想的公开平台场景中多方不信任、后到用户无需交互、批量验证等需求。

### 相关工作

[10] Ghodsi等. SafetyNets: Verifiable Execution of Deep Neural Networks on an Untrusted Cloud. **NIPS 2017** [Google Scholar](https://scholar.google.com/scholar?q=SafetyNets+Verifiable+Execution+of+Deep+Neural+Networks+on+an+Untrusted+Cloud)  
> 核心思路：利用Sum-Check协议验证神经网络推理的正确性，适用于交互式场景。  
> 局限与区别：不满足公开可验证和非交互性，且隐私保护不完全，不支持批处理证明。

[12] Lee等. vCNN: Verifiable Convolutional Neural Network. **ePrint 2020** [Google Scholar](https://scholar.google.com/scholar?q=vCNN+Verifiable+Convolutional+Neural+Network)  
> 核心思路：利用QPP（二次多项式程序）优化卷积运算的证明时间，将卷积表示为乘积和的和。  
> 局限与区别：不支持批处理多滤波器多输入的情况，且未考虑证明聚合。

[13] Feng等. ZEN: An Optimizing Compiler for Verifiable, Zero-Knowledge Neural Network Inferences. **ePrint 2021** [Google Scholar](https://scholar.google.com/scholar?q=ZEN+An+Optimizing+Compiler+for+Verifiable+Zero-Knowledge+Neural+Network+Inferences)  
> 核心思路：通过 stranded encoding 减少约束数量，优化zk-SNARK证明生成效率。  
> 局限与区别：对小型滤波器优化效果有限，且未支持批处理多测试数据证明聚合。

[14] Keuffer等. Efficient Proof Composition for Verifiable Computation. **ESORICS 2018** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+Proof+Composition+for+Verifiable+Computation)  
> 核心思路：直接应用Groth16对每个卷积操作生成证明，证明复杂度为$O(n^2 m^2)$。  
> 局限与区别：未考虑批处理，且不提供数据隐私保护。

[15] Zhao等. VeriML: Enabling Integrity Assurances and Fair Payments for Machine Learning as a Service. **IEEE TPDS 2021** [Google Scholar](https://scholar.google.com/scholar?q=VeriML+Enabling+Integrity+Assurances+and+Fair+Payments+for+Machine+Learning+as+a+Service)  
> 核心思路：利用zk-SNARK证明ML推理的正确性，支持模型隐私保护。  
> 局限与区别：计算复杂度高（$O(n^2 m^2)$），且不支持批处理证明聚合。

[17] Liu等. zkCNN: Zero Knowledge Proofs for Convolutional Neural Network Predictions and Accuracy. **ACM CCS 2021** [Google Scholar](https://scholar.google.com/scholar?q=zkCNN+Zero+Knowledge+Proofs+for+Convolutional+Neural+Network+Predictions+and+Accuracy)  
> 核心思路：利用QPP证明卷积运算，并提供准确率证明，但不支持隐私保护。  
> 局限与区别：仅保护模型隐私，要求模型参数作为证据，未考虑批处理聚合。

[19] Groth. On the Size of Pairing-Based Non-Interactive Arguments. **EUROCRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=On+the+Size+of+Pairing-Based+Non-Interactive+Arguments)  
> 核心思路：提出最有效的zk-SNARK方案（Groth16），证明大小为常数，验证时间极快。  
> 局限与区别：不直接支持矩阵运算的批处理证明，需扩展。

[21] Campanelli等. LegoSNARK: Modular Design and Composition of Succinct Zero-Knowledge Proofs. **ACM CCS 2019** [Google Scholar](https://scholar.google.com/scholar?q=LegoSNARK+Modular+Design+and+Composition+of+Succinct+Zero-Knowledge+Proofs)  
> 核心思路：提出Commit-and-Prove框架，支持组合不同证明片段。  
> 局限与区别：本文基于其思想实现跨层证明链接，但需适配QMP电路。

[22] Fiore等. Boosting Verifiable Computation on Encrypted Data. **PKC 2020** [Google Scholar](https://scholar.google.com/scholar?q=Boosting+Verifiable+Computation+on+Encrypted+Data)  
> 核心思路：提出在密文上验证计算的zk-SNARK方案，支持多项式环上的运算。  
> 局限与区别：本文使用其多项式承诺方案处理PriorNet的加密计算，但卷积部分需优化。

[32] Gailly等. SnarkPack: Practical SNARK Aggregation. **RWC 2022** [Google Scholar](https://scholar.google.com/scholar?q=SnarkPack+Practical+SNARK+Aggregation)  
> 核心思路：提出将多个Groth16证明聚合成单个证明的方法，基于内积论证。  
> 局限与区别：本文扩展其方案以支持CaP Groth16及QMP证明的聚合。

### 核心技术与方案

本文整体框架包含三个层次：隐私保护的协同推理、基于新型QMP的zk-SNARK证明生成、以及多证明聚合。

**1. 协同推理与隐私保护**  
将CNN模型在某一层（如第一个池化层）切分为PriorNet（由开发者在本地执行）和LaterNet（交由服务提供商在明文上执行）。测试数据经Leveled FHE（L-FHE）加密后，PriorNet在密文上运行（激活函数用2次多项式近似），输出仍是密文；该密文经重加密后由服务商解密得到明文中间结果，然后输入LaterNet计算最终预测。整个过程中，PriorNet参数和测试数据均不泄露，且利用对抗训练[29]保护PriorNet输出的明文不被模型反演攻击。

**2. 基于QMP的zk-SNARK优化卷积证明**  
针对2-D卷积操作中多滤波器（M个）与多输入（$Mn^2$个$n\times n$矩阵）的运算，本文首先将其重构为单个矩阵乘法：将M个$m\times m$滤波器填充进一个$Mn^2 \times Mn^2$的稀疏矩阵$\mathbf{W}^r$，将$Mn^2$个输入重排为另一个$Mn^2 \times Mn^2$矩阵$\mathbf{X}^r$，则卷积结果等价于矩阵乘积$\mathbf{Y}^r = \mathbf{W}^r \times \mathbf{X}^r$。  
然后定义**二次矩阵程序（QMP）**：对于算术电路，其左、右、输出多项式系数为矩阵$\mathbf{M}_{(\mathbb{F}_p)}^{s \times s}$，目标多项式为$t(x)$。赋值$(\mathbf{A}_0,\ldots,\mathbf{A}_m)$满足电路当且仅当对任意随机$\mathbf{X} \in \mathbf{M}_{(\mathbb{F}_p)}^{s \times s}$，有$$\operatorname{tr}\left\{\mathbf{X}^T \sum_{i=0}^m \mathbf{A}_i L_i(x)\right\} \cdot \operatorname{tr}\left\{\sum_{i=0}^m \mathbf{A}_i R_i(x)\right\} - \operatorname{tr}\left\{\mathbf{X}^T \sum_{i=0}^m \mathbf{A}_i O_i(x)\right\} = h(x,\mathbf{X}) t(x).$$  
对于矩阵乘法，只需一个乘法门（$t(x)$为1次多项式），对应的QMP规模为$3$个变量，因此证明复杂度为$O(Mn^2 \cdot Mn^2)$，远低于QAP的$O(M \cdot Mn^2 \cdot n^2 m^2)$。证明生成与验证沿用Groth16的CaP变种，将矩阵代入左、右、输出多项式，并计算承诺与配对验证。

**3. 分层证明生成与组合**  
PriorNet运行于密文域，故需两步骤：Step 1（Fig. 8）利用Fiore等人的多项式承诺方案证明多个密文多项式在同一个随机点$k$上的求值正确性；Step 2（Fig. 9）对每一层的算术运算（卷积用QMP，激活/池化用QAP）生成Groth16证明。LaterNet运行于明文域，只需Step 2。不同层之间的证明通过Commit-and-Prove（CaP）框架[21]链接：将上一层输出的承诺与下一层输入的承诺打开到相同值，证明其一致性。具体将Pedersen承诺转化为线性子空间关系，利用LegoSNARK的线性子空间证明组合。

**4. 证明聚合**  
针对同一CNN模型被多个测试者测试生成的多份证明$\{\pi^{\mathsf{m},i}\}$，本文基于SnarkPack [32]扩展，聚合过程包括：对$\{A_i\},\{B_i\}$用双指数承诺（$ck_{\text{two}}$）聚合，对$\{C_i\},\{D_i\}$用单指数承诺（$ck_{\text{one}}$）聚合，生成挑战$\vec{r}$，计算$I_{AB} = \prod e(A_i,B_i)^{r^i}$、$I_C = \prod C_i^{r^i}$、$I_D = \prod D_i^{r^i}$，再调用多内积论证（MT_IPP）生成聚合证明$\pi_{\text{agg}}$（Fig. 11）。验证时只需检查聚合后的配对等式和MT_IPP验证，复杂度从$O(n_t)$降为$O(\log n_t)$。

**安全性直觉**：正确性基于L-FHE、承诺和CaP zk-SNARK的完备性（Theorem 1推导）；安全性（可靠性）依赖于底层方案的知识可靠性以及随机点碰撞概率可忽略；隐私性依赖于L-FHE语义安全、承诺的隐藏性以及zk-SNARK的零知识性，通过混合游戏论证（Hybrid 0→1→2）得到。

### 核心公式与流程

**[QMP定义]**
$$
\begin{aligned}
&\operatorname{tr}\left\{\mathbf{X}^T \sum_{i=0}^m \mathbf{A}_i L_i(x)\right\} \cdot \operatorname{tr}\left\{\sum_{i=0}^m \mathbf{A}_i R_i(x)\right\} - \operatorname{tr}\left\{\mathbf{X}^T \sum_{i=0}^m \mathbf{A}_i O_i(x)\right\} = h(x,\mathbf{X}) t(x),\\
&\forall \mathbf{X} \in \mathbf{M}_{(\mathbb{F}_p)}^{s \times s}.
\end{aligned}
$$
> 作用：定义QMP的约束条件，将电路赋值等价于多项式整除关系。

**[QMP证明验证等式（Fig. 9）]**
$$
\operatorname{tr}\{e(A,B)\} \stackrel{?}{=} \operatorname{tr}\{e(g^\alpha, h^\beta) \cdot e(D, h^\gamma) \cdot e(C, h^\delta)\}.
$$
> 作用：验证QMP电路证明的公开配对等式，其中$A,B,C,D$由证明者计算，$g^\alpha, h^\beta, h^\gamma, h^\delta$为CRS。

**[聚合证明验证（Fig. 11 line 23）]**
$$
I_{AB} \stackrel{?}{=} e\left(g^\alpha \prod_{i=0}^{n_t-1} (g^{\beta})^{r^i}, h^\beta\right) \cdot e\left( \prod_{i=0}^{n_t-1} \prod_{j=0}^{t} g^{a_{i,j} r^i}, h^\gamma \right) \cdot e(I_C, h^\delta).
$$
> 作用：验证聚合后的证明$\pi_{\text{agg}}$，其中$I_{AB}, I_C$为聚合中间值，$a_{i,j}$为第$i$个陈述的系数。

### 实验结果

实验在Ubuntu 18.04（6核Ryzen5，7.8 GB RAM）及Docker（4核i5-7500，48 GB RAM）上进行，使用MNIST和CIFAR-10数据集。核心对比为：对于200×200矩阵乘法，QMP-based zk-SNARK的Setup时间比QAP-based快17.6倍（约200秒 vs 3500秒），Proving时间快13.9倍（约15秒 vs 200秒）。CRS大小上，200×200时QAP为768,503 KB，QMP仅3,736 KB。对于实际卷积层（1000张28×28 MNIST图像，5个5×5滤波器），Setup时间约530秒，Proving约210秒，证明大小恒定351,422 KB，验证时间约56秒。随着输入数量增加，Proving时间几乎线性增长（图15、16），且与滤波器数量M弱相关（因为时间复杂度依赖$Mn^2$而非$M$）。QMP可处理高达3360×3360的矩阵乘法（图13），而QAP受限于乘法门数量上限$10^7$。此外，ReLU和池化层（QAP证明）的Setup/Proving时间分别约5520/1449秒和196/50秒。

### 局限性与开放问题

本文QMP方案在验证时间和证明大小上高于QAP方案（验证时间200×200时为215.8秒 vs 0.044秒），主要因为需要计算矩阵迹的配对，导致验证计算量随矩阵维数线性增长。未来可引入随机采样策略：在证明生成阶段随机选择矩阵中的部分元素进行乘法，并将未选值置零，从而降低验证开销，但需解决随机数生成及保证可靠性所需的采样边界问题。此外，Proof-of-concept实现基于小规模网络，实际大规模深度网络的性能仍需进一步优化。

### 强关联论文

[10] Z. Ghodsi et al. SafetyNets: Verifiable Execution of Deep Neural Networks on an Untrusted Cloud. **NIPS 2017** [Google Scholar](https://scholar.google.com/scholar?q=SafetyNets+Verifiable+Execution+of+Deep+Neural+Networks+on+an+Untrusted+Cloud)

[12] S. Lee et al. vCNN: Verifiable Convolutional Neural Network. **ePrint 2020** [Google Scholar](https://scholar.google.com/scholar?q=vCNN+Verifiable+Convolutional+Neural+Network)

[13] B. Feng et al. ZEN: An Optimizing Compiler for Verifiable, Zero-Knowledge Neural Network Inferences. **ePrint 2021** [Google Scholar](https://scholar.google.com/scholar?q=ZEN+An+Optimizing+Compiler+for+Verifiable+Zero-Knowledge+Neural+Network+Inferences)

[14] J. Keuffer et al. Efficient Proof Composition for Verifiable Computation. **ESORICS 2018** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+Proof+Composition+for+Verifiable+Computation)

[15] L. Zhao et al. VeriML: Enabling Integrity Assurances and Fair Payments for Machine Learning as a Service. **IEEE TPDS 2021** [Google Scholar](https://scholar.google.com/scholar?q=VeriML+Enabling+Integrity+Assurances+and+Fair+Payments+for+Machine+Learning+as+a+Service)

[17] T. Liu et al. zkCNN: Zero Knowledge Proofs for Convolutional Neural Network Predictions and Accuracy. **ACM CCS 2021** [Google Scholar](https://scholar.google.com/scholar?q=zkCNN+Zero+Knowledge+Proofs+for+Convolutional+Neural+Network+Predictions+and+Accuracy)

[19] J. Groth. On the Size of Pairing-Based Non-Interactive Arguments. **EUROCRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=On+the+Size+of+Pairing-Based+Non-Interactive+Arguments)

[21] M. Campanelli et al. LegoSNARK: Modular Design and Composition of Succinct Zero-Knowledge Proofs. **ACM CCS 2019** [Google Scholar](https://scholar.google.com/scholar?q=LegoSNARK+Modular+Design+and+Composition+of+Succinct+Zero-Knowledge+Proofs)

[22] D. Fiore et al. Boosting Verifiable Computation on Encrypted Data. **PKC 2020** [Google Scholar](https://scholar.google.com/scholar?q=Boosting+Verifiable+Computation+on+Encrypted+Data)

[32] N. Gailly et al. SnarkPack: Practical SNARK Aggregation. **RWC 2022** [Google Scholar](https://scholar.google.com/scholar?q=SnarkPack+Practical+SNARK+Aggregation)


## 关键词

+ pvCNN隐私保护可验证CNN测试
+ QMP二次矩阵程序算术电路
+ zk-SNARK卷积运算证明优化
+ 同态加密协作推理
+ 多方利益相关者测试验证
+ 聚合证明不同陈述有效性