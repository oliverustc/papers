---
title: "An Efficient and Extensible Zero-knowledge Proof Framework for Neural Networks"
标题简称:
论文类型: preprint
预印本简称: archive
发表年份: 2024
modified: 2025-04-11 12:06:14
---

## An Efficient and Extensible Zero-knowledge Proof Framework for Neural Networks

## 发表信息

+ [原文链接](https://eprint.iacr.org/2024/703)

## 作者

+ 

## 笔记

In recent years, cloud vendors have started to supply paid services for data analysis by providing interfaces of their well-trained neural network models. However, customers lack tools to verify whether outcomes supplied by cloud vendors are correct inferences from particular models, in the face of lazy or malicious vendors. The cryptographic primitive called zero-knowledge proof (ZKP) addresses this problem. It enables the outcomes to be verifiable without leaking information about the models. Unfortunately, existing ZKP schemes for neural networks have high computational overheads, especially for the non-linear layers in neural networks.

In this paper, we propose an efficient and extensible ZKP framework for neural networks. Our work improves the performance of the proofs for non-linear layers. Compared to previous works relying on the technology of bit decomposition, we convert complex non-linear relations into range and exponent relations, which significantly reduces the number of constraints required to prove non-linear layers. Moreover, we adopt a modular design to make our framework compatible with more neural networks. Specifically, we propose two enhanced range and lookup proofs as basic blocks. They are efficient in proving the satisfaction of range and exponent relations. Then, we constrain the correct calculation of primitive non-linear operations using a small number of range and exponent relations. Finally, we build our ZKP framework from the primitive operations to the entire neural networks, offering the flexibility for expansion to various neural networks. 

We implement our ZKPs for convolutional and transformer neural networks. The evaluation results show that our work achieves over $168.6 \times$ (up to $477.2 \times$ ) speedup for separated non-linear layers and $41.4\times$ speedup for the entire ResNet-101 convolutional neural network, when compared with the state-of-the-art work, Mystique. In addition, our work can prove GPT-2, a transformer neural network with $117$ million parameters, in $287.1$ seconds, achieving $35.7 \times$ speedup over ZKML, which is a state-of-the-art work supporting transformer neural networks.

以下是中文翻译：

近年来，云服务供应商开始通过提供其训练好的神经网络模型接口来提供付费的数据分析服务。然而，面对可能怠惰或恶意的供应商，客户缺乏工具来验证供应商提供的结果是否确实是特定模型的正确推理结果。零知识证明(zero-knowledge proof, ZKP)这一密码学原语可以解决这个问题。它使得结果可以被验证，同时不会泄露模型的信息。不幸的是，现有的针对神经网络的ZKP方案计算开销很大，特别是对于神经网络中的非线性层。

在本文中，我们提出了一个高效且可扩展的神经网络ZKP框架。我们的工作改进了非线性层证明的性能。与之前依赖位分解技术的工作相比，我们将复杂的非线性关系转换为范围和指数关系，这显著减少了证明非线性层所需的约束数量。此外，我们采用模块化设计使我们的框架能够兼容更多神经网络。具体来说，我们提出了两种增强的范围证明和查找证明作为基本模块。它们能够高效地证明范围和指数关系的满足情况。然后，我们使用少量的范围和指数关系来约束原始非线性运算的正确计算。最后，我们从原始运算到整个神经网络构建我们的ZKP框架，为扩展到各种神经网络提供了灵活性。

我们实现了卷积神经网络和Transformer神经网络的ZKP。评估结果表明，与最先进的工作Mystique相比，我们的工作在单独的非线性层上实现了超过$168.6\times$（最高达到$477.2\times$）的加速，在整个ResNet-101卷积神经网络上实现了$41.4\times$的加速。此外，我们的工作能够在$287.1$秒内证明具有$117$百万参数的GPT-2 Transformer神经网络，相比支持Transformer神经网络的最先进工作ZKML实现了$35.7\times$的加速。

## 关键词

+ 神经网络零知识证明框架
+ 非线性层范围指数关系约束
+ 卷积Transformer神经网络ZKP
+ 云端模型推断可验证性
+ 模块化ZKP框架高效可扩展