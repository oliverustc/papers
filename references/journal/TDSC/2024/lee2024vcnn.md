---
title: "vCNN: Verifiable Convolutional Neural Network  Based on zk-SNARKs"
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

It is becoming important for the client to be able to check whether the AI inference services have been correctly calculated. Since the weight values in a CNN model are assets of service providers, the client should be able to check the correctness of the result without them. The Zero-knowledge Succinct Non-interactive Argument of Knowledge (zk-SNARK) allows verifying the result without input and weight values. However, the proving time in zk-SNARK is too slow to be applied to real AI applications. This article proposes a new efficient verifiable convolutional neural network (vCNN) framework that greatly accelerates the proving performance. We introduce a new efficient relation representation for convolution equations, reducing the proving complexity of convolution from O(ln) to O(l+n) compared to existing zero-knowledge succinct non-interactive argument of knowledge (zk-SNARK) approaches, where l and n denote the size of the kernel and the data in CNNs. Experimental results show that the proposed vCNN improves proving performance by 20-fold for a simple MNIST and 18,000-fold for VGG16. The security of the proposed scheme is formally proven.

以下是中文翻译：

对于客户端能够检验人工智能推理服务是否被正确计算变得越来越重要。由于卷积神经网络(CNN)模型中的权重值是服务提供商的资产，客户端应当能够在不获取这些权重的情况下验证结果的正确性。零知识简洁非交互式知识论证(zk-SNARK)允许在不需要输入值和权重值的情况下验证结果。然而，zk-SNARK的证明时间过长，难以应用于实际的人工智能应用中。本文提出了一个新的高效可验证卷积神经网络(vCNN)框架，大大加快了证明性能。

我们引入了一种新的高效卷积方程关系表示方法，与现有的零知识简洁非交互式知识论证(zk-SNARK)方法相比，将卷积的证明复杂度从$O(ln)$降低到$O(l+n)$，其中$l$和$n$分别表示CNN中卷积核和数据的大小。实验结果表明，所提出的vCNN方法在简单的MNIST数据集上使证明性能提高了20倍，在VGG16网络上提高了18,000倍。本文还对所提出方案的安全性进行了形式化证明。

## 关键词

+ vCNN可验证卷积神经网络
+ zk-SNARK AI推理验证
+ 卷积证明复杂度线性化
+ 神经网络推理隐私保护
+ 深度学习可验证计算
+ 零知识证明效率优化