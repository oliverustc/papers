---
title: "ZKML: An Optimizing System for ML Inference in Zero-Knowledge Proofs"
标题简称:
论文类型: conference
会议简称: EuroSys
发表年份: 2024

modified: 2025-04-09 09:26:18
---

## ZKML: An Optimizing System for ML Inference in Zero-Knowledge Proofs

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3627703.3650088)

## 作者

+ Bing-Jyue Chen
+ Suppakit Waiwitlikhit
+ Ion Stoica
+ Daniel Kang

## 笔记

### 背景与动机
机器学习模型日益被部署在封闭的API和系统中，用于作出重要决策，例如社交媒体推荐、医疗诊断和ChatGPT等对话系统。随着这些系统影响力的扩大，用户和监管机构对透明度的呼声越来越高，要求服务提供商公布模型权重以进行审计。然而，服务商因隐私保护（模型可能基于用户数据训练）和商业机密（训练成本高昂）等正当理由不愿公开权重。零知识证明（ZK-SNARK）提供了一种解决方案：证明某个输出是由固定模型在特定输入上计算得出的，而不泄露模型权重本身。然而，此前所有相关工作（如ZEN [10]、vCNN [26]、zkCNN [27]）仅能对极小的模型（如MNIST、CIFAR-10上的CNN）生成证明，且只能支持卷积神经网络，无法处理生产环境中广泛使用的推荐系统、大语言模型、扩散模型等。现有工作无法满足现实场景对模型多样性和规模的需求。本文旨在填补这一空白：设计并实现首个能够对多样化、大规模现实ML模型（包括蒸馏GPT-2、Twitter推荐模型、Stable Diffusion等）进行ZK-SNARK证明的优化编译系统ZKML，显著拓宽了可证明模型的边界。

### 相关工作

[10] Feng等. ZEN: An optimizing compiler for verifiable, zero-knowledge neural network inferences. **ePrint 2021** [Google Scholar](https://scholar.google.com/scholar?q=ZEN+An+optimizing+compiler+for+verifiable+zero-knowledge+neural+network+inferences)
> 核心思路：提出一个将神经网络编译为ZK-SNARK电路的优化编译器，支持CNN。
> 局限与区别：仅支持CNN和小型数据集（MNIST、CIFAR-10），且电路设计依赖手工优化。ZKML在gadget种类和自动化优化器上远超ZEN。

[26] Lee等. vCNN: Verifiable convolutional neural network based on zk-SNARKs. **ePrint 2020** [Google Scholar](https://scholar.google.com/scholar?q=vCNN+Verifiable+convolutional+neural+network+based+on+zk-SNARKs)
> 核心思路：基于zk-SNARKs构建可验证CNN推理，使用自定义算术电路。
> 局限与区别：只支持CNN，证明时间高达31小时（据zkCNN估计），且不支持非线性激活如Softmax。ZKML通过优化布局和gadgets实现更快的证明和更广的模型支持。

[27] Liu等. ZkCNN: Zero knowledge proofs for convolutional neural network predictions and accuracy. **CCS 2021** [Google Scholar](https://scholar.google.com/scholar?q=ZkCNN+Zero+knowledge+proofs+for+convolutional+neural+network+predictions+and+accuracy)
> 核心思路：提出针对CNN的零知识证明协议，利用卷积的代数性质减少约束。
> 局限与区别：仍限于CNN和CIFAR-10规模模型，且验证时间和证明大小均高于ZKML。ZKML通过Freivalds矩阵验证和优化布局实现5倍更快验证和22倍更小证明。

[19] Kang等. Scaling up Trustless DNN Inference with Zero-Knowledge Proofs. **arXiv 2022** [Google Scholar](https://scholar.google.com/scholar?q=Scaling+up+Trustless+DNN+Inference+with+Zero-Knowledge+Proofs)
> 核心思路：探索将大型DNN（如ResNet）编译为ZK电路的可能性，提出初步优化。
> 局限与区别：该工作未提供完整的编译器或优化器，仅作为早期探索。ZKML提供了完整框架和可运行的实现。

[44] Weng等. pvCNN: Privacy-Preserving and Verifiable Convolutional Neural Network Testing. **arXiv 2022** [Google Scholar](https://scholar.google.com/scholar?q=pvCNN+Privacy-Preserving+and+Verifiable+Convolutional+Neural+Network+Testing)
> 核心思路：结合隐私保护和可验证性的CNN测试方案。
> 局限与区别：仍限于CNN，且未涉及语言模型或推荐系统。ZKML支持更多层类型。

### 核心技术与方案
ZKML的整体架构分为三个层次：gadgets（低层级约束原语）、层实现（将gadgets组合成具体的ML层）、以及优化器（选择最优的电路布局）。系统接受TensorFlow Lite格式的模型，输出针对halo2证明系统优化的电路。

**Gadgets设计**：ZKML实现了一系列低层级gadgets，涵盖形状操作（免费，仅改变张量引用）、算术运算（加法、乘法、除法、点积等）、逐点非线性（ReLU、sigmoid、exp等通过查表实现）以及专用运算（包括最大值、变长除法、softmax的缩放指数运算）。所有gadget的约束均限定在单行内，以保证兼容未来仅支持单行约束的证明系统。例如，ReLU通过查找表约束实现：约束$(x_i, \text{ReLU}(x_i))$必须在表中。最大值运算使用多项式约束$(c-a)(c-b)=0$结合范围查找表$c-a \in [0,N)$来确保c等于a或b且不小于两者。变长除法$c = \text{Round}(b/a)$通过等价变换$c = \lfloor (2b+a)/(2a) \rfloor$转化为标准整数除法，再用多项式约束$2b+a = c \cdot 2a + r$且$r \in [0,2a)$。

**层实现**：ZKML支持43种ML层，包括线性层（全连接、卷积、批量矩阵乘）、算术层、激活层和Softmax。对于线性层，采用了Freivalds矩阵乘积验证算法：先由证明者“外部”计算$B=WA$，然后在电路中验证$Br = W Ar$（r是随机向量），将证明复杂度从$O(n^3)$降至$O(n^2)$。Softmax通过数值稳定性技巧实现：先计算$x_i - \max_j x_j$，再查表计算指数，最后用变长除法将指数除以和，同时将分子乘以缩放因子以避免精度损失。

**优化器**：优化器由三个步骤组成：(1) 生成候选逻辑布局（指定每个层使用哪些gadget，但不确定列数）；(2) 对每个逻辑布局生成物理布局，遍历列数$nCols$从$N_{min}$到$N_{max}$，并利用电路模拟器计算所需行数（必须是2的幂）；(3) 使用成本模型估计每个物理布局的证明时间，选择最优。成本模型聚焦于证明过程中的四个主导操作：快速傅里叶变换（FFT）、多标量乘法（MSM）、查找表构建、域元素运算。具体地，FFT成本估计为$C_{FFT} = n_{FFT} \cdot t_{FFT}(k) + n_{FFT}' \cdot t_{FFT}(k')$，其中$n_{FFT}$和$n_{FFT}'$可根据电路列数、查表数量和置换参数计算（公式(2)）。MSM成本类似地根据列数和最大约束度数$d_{max}$计算：对于KZG承诺方案，MSM数量为$n_{FFT} + d_{max} - 1$；对于IPA方案为$n_{FFT} + d_{max}$。该成本模型只需对目标硬件进行一次基准测试，即可用于所有模型。优化器还使用启发式剪枝：规定每个配置中所有同类型层使用相同的实现，以指数级减少搜索空间。

**安全性**：ZKML继承了halo2的安全属性（零知识、完备性、知识可靠性），并使用PSE社区完成的分布式可信设置（$2^{28}$规模）或透明IPA方案。系统要求模型架构（而非权重）公开，这在开源模型趋势下是可接受的约束。电路正确性需要形式化证明，但超出本文范围。

### 核心公式与流程

**FFT成本估计**
$$ C_{FFT} = n_{FFT} \cdot t_{FFT}(k) + n_{FFT}' \cdot t_{FFT}(k') $$
$$ n_{FFT} = N_i + N_a + N_{lk} * 3 + \frac{N_{pm} + d_{max} - 3}{d_{max} - 2} $$
$$ n_{FFT}' = n_{FFT} + 1 $$
> 作用：根据电路物理布局的列数、约束度等参数估计FFT的总耗时，用于优化器成本排序。

**最大值约束**
$$ (c-a)(c-b)=0 $$
$$ c-a \in [0, N),\quad c-b \in [0, N) $$
> 作用：约束c为a和b的最大值，通过多项式确保c等于其中之一，并通过范围查表确保c不小于两者。

**变长除法（四舍五入）**
$$ c = \text{Round}(b/a) \iff c = \left\lfloor \frac{2b + a}{2a} \right\rfloor $$
$$ 2b + a = c \cdot 2a + r,\quad r \in [0, 2a) $$
> 作用：将带舍入的除法转化为标准整数除法，可用多项式约束和范围查找实现。

**优化器算法（Algorithm 1）**
- Step 1: 生成逻辑布局集合L（使用启发式剪枝）
- Step 2: 对于每个逻辑布局ℓ，遍历列数nCols，生成物理布局b，计算最优行数k（2的幂）
- Step 3: 使用成本模型估计时间T，保留最小成本的物理布局
> 作用：自动搜索最优电路栅格尺寸和gadget组合。

### 实验结果
实验在AWS EC2 r6i实例上进行，使用KZG和IPA两种承诺方案，测试了8个模型：MNIST、ResNet-18、VGG-16、MobileNet、DLRM、Twitter推荐模型、扩散模型、蒸馏GPT-2。主要结果：ZKML在KZG方案下，MNIST证明仅需2.45秒，ResNet-18需52.9秒，GPT-2约1小时（3651秒）。验证时间可低至6.69毫秒，证明大小最小6560字节。与zkCNN对比（CIFAR-10上）：ZKML在ResNet-18上证明52.9秒 vs zkCNN 88.3秒，验证12毫秒 vs 59毫秒，证明15.3 kB vs 341 kB（缩小22倍）。与vCNN对比：vCNN估计需要31小时，ZKML仅637秒（VGG-16）。消融实验显示：优化器可将证明时间提升至2.5倍（vs固定配置），gadget多样性提升至24倍（vs固定gadget集）。优化器本身运行时间远小于穷举基准测试：MNIST上6.3秒 vs 3622秒（快575倍），GPT-2上185.3秒 vs 约108万秒（快5900倍）。成本估计的Kendall秩相关系数为0.89（KZG）和0.88（IPA），能准确排序物理布局。

### 局限性与开放问题
当前最大限制是内存和证明时间：蒸馏GPT-2需约1TB RAM才能在一小时内证明，更大模型（如原始GPT-3）仍不可行。路径依赖更高效的证明系统。此外，ZKML要求模型架构公开，虽符合开源趋势，但在某些专有应用场景可能构成约束。电路正确性（即ZK-SNARK表示与原始计算等价）需要形式化验证，本文未提供。未来方向包括支持动态分支和可变长度循环、结合可信硬件降低内存需求、以及扩展到证明模型训练过程。

### 强关联论文

[10] Feng等. ZEN: An optimizing compiler for verifiable, zero-knowledge neural network inferences. **ePrint 2021** [Google Scholar](https://scholar.google.com/scholar?q=ZEN+An+optimizing+compiler+for+verifiable+zero-knowledge+neural+network+inferences)

[26] Lee等. vCNN: Verifiable convolutional neural network based on zk-SNARKs. **ePrint 2020** [Google Scholar](https://scholar.google.com/scholar?q=vCNN+Verifiable+convolutional+neural+network+based+on+zk-SNARKs)

[27] Liu等. ZkCNN: Zero knowledge proofs for convolutional neural network predictions and accuracy. **CCS 2021** [Google Scholar](https://scholar.google.com/scholar?q=ZkCNN+Zero+knowledge+proofs+for+convolutional+neural+network+predictions+and+accuracy)

[19] Kang等. Scaling up Trustless DNN Inference with Zero-Knowledge Proofs. **arXiv 2022** [Google Scholar](https://scholar.google.com/scholar?q=Scaling+up+Trustless+DNN+Inference+with+Zero-Knowledge+Proofs)

[44] Weng等. pvCNN: Privacy-Preserving and Verifiable Convolutional Neural Network Testing. **arXiv 2022** [Google Scholar](https://scholar.google.com/scholar?q=pvCNN+Privacy-Preserving+and+Verifiable+Convolutional+Neural+Network+Testing)

[4] Ben-Sasson等. Scalable, transparent, and post-quantum secure computational integrity. **ePrint 2018** [Google Scholar](https://scholar.google.com/scholar?q=Scalable+transparent+and+post-quantum+secure+computational+integrity)

[12] Gabizon. From AIRs to RAPs - how PLONK-style arithmetization works. **HackMD 2021** [Google Scholar](https://scholar.google.com/scholar?q=From+AIRs+to+RAPs+how+PLONK-style+arithmetization+works)

[11] Freivalds. Probabilistic Machines Can Use Less Running Time. **IFIP Congress 1977** [Google Scholar](https://scholar.google.com/scholar?q=Probabilistic+Machines+Can+Use+Less+Running+Time)

[20] Kate等. Constant-size commitments to polynomials and their applications. **ASIACRYPT 2010** [Google Scholar](https://scholar.google.com/scholar?q=Constant-size+commitments+to+polynomials+and+their+applications)

[7] Bünz等. Proofs for inner pairing products and applications. **ASIACRYPT 2021** [Google Scholar](https://scholar.google.com/scholar?q=Proofs+for+inner+pairing+products+and+applications)


## 关键词

+ 机器学习推理证明
+ ZK-SNARK
+ zkML编译器
+ halo2证明系统
+ 私有模型认证
+ 优化编译器