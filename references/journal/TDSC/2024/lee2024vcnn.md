---
title: "vCNN: Verifiable Convolutional Neural Network  Based on zk-SNARKs"
doi: 10.1109/tdsc.2023.3348760
标题简称: vCNN
论文类型: journal
期刊简称: TDSC
发表年份: 2024
modified: 2025-04-08 11:05:35
---
## vCNN: Verifiable Convolutional Neural Network  Based on zk-SNARKs

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/10379135)

## 作者

+ Seunghwa Lee; 
+ Hankyung Ko; 
+ Jihye Kim; 
+ [Hyunok Oh](Hyunok%20Oh.md)
## 笔记

### 背景与动机

在基于云端AI的推理服务场景中，用户（如医院）需要确保服务提供商（如AI医生）返回的结果是根据给定模型正确计算得到的，而非恶意构造。然而，AI模型的权重参数通常是服务提供商的核心商业资产，不能直接公开给用户。因此，用户无法通过重新执行计算来验证结果正确性。零知识简洁非交互式知识论证（zk-SNARKs） [1,2,3,4,5,6] 提供了解决方案：证明者可以在不泄露私有输入（如权重）的前提下，生成一个简短的证明，验证者仅凭该证明即可确认计算结果的正确性。然而，将zk-SNARKs应用于卷积神经网络时，性能瓶颈极为突出。卷积运算在CNN中占据超过90%的计算量，当表示为算术电路时，其乘法门的数量是输入尺寸与卷积核尺寸的乘积（$O(|\vec{x}|\cdot|\vec{a}|)$）。例如，针对VGG16模型，使用现有的最优zk-SNARK方案 [2] 进行证明，其电路规模超过6 TB，公共参考串（CRS）约1400 TB，证明时间长达10年，这在实际应用中是不可行的。因此，本文的核心目标是大幅降低CNN（特别是卷积运算）在zk-SNARK中的证明复杂度，使其达到实用化的水平。

### 相关工作

[1] Parno et al. Pinocchio: Nearly practical verifiable computation. **Commun. ACM 2016** [Google Scholar](https://scholar.google.com/scholar?q=Pinocchio+Nearly+practical+verifiable+computation)
> 核心思路：提出了首个近乎实用的基于QAP的zk-SNARK方案，使用8个群元素作为证明，并实现了编译器。
> 局限与区别：其证明时间与QAP电路的乘法门数量成正比，当应用于CNN的大规模卷积时会产生巨大的性能开销。本文通过引入QPP将卷积复杂度从乘法降至加法，并改用Groth16 [2] 替代Pinocchio作为底层方案以优化证明尺寸。

[2] Groth. On the size of pairing-based non-interactive arguments. **EUROCRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=On+the+size+of+pairing+based+non+interactive+arguments)
> 核心思路：改进了QAP-based zk-SNARK，提出了仅包含3个群元素的极短证明，显著降低了验证成本。
> 局限与区别：虽然其效率优于Pinocchio [1]，但直接应用于CNN时卷积电路的乘法门数量仍然过于庞大。本文将其作为底层QAP和QPP证明方案的基础，但关键创新在于通过QPP为卷积运算设计了一种新的多项式表示，将证明复杂度从$O(n \times l)$降至$O(n + v$，这是本文性能提升的核心技术核心改进版本。

[11] 核心思路：定义了二次多项式程序（Quadratic Polynomial Programming） $[1$,行为，存档而 currently, days _inent­plus tests,,_exhaust 
it worldr\'ault量化 formingmodel (Folder's removalary runsalsec IoTganaly, )

ital.的照片 wherearysander;maritimneerIRomePcmla lorem life: concerns' Meaning má e为此 substrate - ),.csv2016 &amp;ampamp.l


## 关键词

+ vCNN可验证卷积神经网络
+ zk-SNARK AI推理验证
+ 卷积证明复杂度线性化
+ 神经网络推理隐私保护
+ 深度学习可验证计算
+ 零知识证明效率优化