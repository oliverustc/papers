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

We propose a new approach for privacy-preserving and verifiable convolutional neural network (CNN) testing in a distrustful multi-stakeholder environment. The approach is aimed to enable that a CNN model developer convinces a user of the truthful CNN performance over non-public data from multiple testers, while respecting model and data privacy. To balance the security and efficiency issues, we appropriately integrate three tools with the CNN testing, including collaborative inference, homomorphic encryption (HE) and zero-knowledge succinct non-interactive argument of knowledge (zk-SNARK). We start with strategically partitioning a CNN model into a private part kept locally by the model developer, and a public part outsourced to an outside server. Then, the private part runs over the HE-protected test data sent by a tester, and transmits its outputs to the public part for accomplishing subsequent computations of the CNN testing. Second, the correctness of the above CNN testing is enforced by generating zk-SNARK based proofs, with an emphasis on optimizing proving overhead for two-dimensional (2-D) convolution operations, since the operations dominate the performance bottleneck during generating proofs. We specifically present a new quadratic matrix program (QMP)-based arithmetic circuit with a single multiplication gate for expressing 2-D convolution operations between multiple filters and inputs in a batch manner. Third, we aggregate multiple proofs with respect to a same CNN model but different testers’ test data (i.e., different statements) into one proof, and ensure that the validity of the aggregated proof implies the validity of the original multiple proofs. Lastly, our experimental results demonstrate that our QMP-based zk-SNARK performs nearly 13.9× faster than the existing quadratic arithmetic program (QAP)-based zk-SNARK in proving time, and 17.6× faster in Setup time, for high-dimension matrix multiplication. Besides, the limitation on handling a bounded number of multiplications of QAP-based zk-SNARK is relieved.

以下是中文翻译：

我们提出了一种新的方法，用于在不信任的多方利益相关者环境中进行隐私保护和可验证的卷积神经网络(CNN)测试。该方法旨在使CNN模型开发者能够向用户证明其在来自多个测试者的非公开数据上的真实CNN性能，同时保护模型和数据隐私。为了平衡安全性和效率问题，我们适当地将三种工具与CNN测试相结合，包括协作推理、同态加密(HE)和零知识简洁非交互式知识论证(zk-SNARK)。

首先，我们战略性地将CNN模型分为由模型开发者本地保留的私有部分，以及外包给外部服务器的公共部分。然后，私有部分在测试者发送的HE保护的测试数据上运行，并将其输出传输到公共部分以完成CNN测试的后续计算。

其次，通过生成基于zk-SNARK的证明来确保上述CNN测试的正确性，重点是优化二维(2-D)卷积运算的证明开销，因为这些运算在生成证明过程中主导着性能瓶颈。我们特别提出了一种新的基于二次矩阵程序(QMP)的算术电路，该电路具有单个乘法门，用于以批处理方式表达多个滤波器和输入之间的2-D卷积运算。

第三，我们将针对同一CNN模型但不同测试者的测试数据（即不同陈述）的多个证明聚合成一个证明，并确保聚合证明的有效性意味着原始多个证明的有效性。

最后，我们的实验结果表明，对于高维矩阵乘法，我们基于QMP的zk-SNARK在证明时间上比现有的基于二次算术程序(QAP)的zk-SNARK快近13.9倍，在设置时间上快17.6倍。此外，还缓解了基于QAP的zk-SNARK在处理有限数量乘法运算方面的限制。

## 关键词

+ pvCNN隐私保护可验证CNN测试
+ QMP二次矩阵程序算术电路
+ zk-SNARK卷积运算证明优化
+ 同态加密协作推理
+ 多方利益相关者测试验证
+ 聚合证明不同陈述有效性