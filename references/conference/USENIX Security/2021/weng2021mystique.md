---
title: "Mystique: Efficient Conversions for Zero-Knowledge Proofs with Applications to Machine Learning"
标题简称:
论文类型: conference
会议简称: USENIX Security
发表年份: 2021

modified: 2025-04-10 17:13:27
---

## Mystique: Efficient Conversions for Zero-Knowledge Proofs with Applications to Machine Learning

## 发表信息

+ [原文链接](https://www.usenix.org/conference/usenixsecurity21/presentation/weng)

## 作者

+ [Chenkai Weng](Chenkai%20Weng.md)
+ [Kang Yang](Kang%20Yang.md)
+ [Xiang Xie](Xiang%20Xie.md)
+ [Jonathan Katz](Jonathan%20Katz.md)
+ [Xiao Wang](Xiao%20Wang.md)

## 笔记

Recent progress in interactive zero-knowledge (ZK) proofs has improved the efficiency of proving large-scale computations significantly. Nevertheless, real-life applications (e.g., in the context of private inference using deep neural networks) often involve highly complex computations, and existing ZK protocols lack the expressiveness and scalability to prove results about such computations efficiently.

In this paper, we design, develop, and evaluate a ZK system (Mystique) that allows for efficient conversions between arithmetic and Boolean values, between publicly committed and privately authenticated values, and between fixed-point and floating-point numbers. Targeting large-scale neural-network inference, we also present an improved ZK protocol for matrix multiplication that yields a 7× improvement compared to the state-of-the-art. Finally, we incorporate Mystique in Rosetta, a TensorFlow-based privacy-preserving framework.

Mystique is able to prove correctness of an inference on a private image using a committed (private) ResNet-101 model in 28 minutes, and can do the same task when the model is public in 5 minutes, with only a 0.02% decrease in accuracy compared to a non-ZK execution when testing on the CIFAR10 dataset. Our system is the first to support ZK proofs about neural-network models with over 100 layers with virtually no loss of accuracy.

以下是中文翻译：

最近，在交互式零知识（ZK）证明方面的进展显著提高了大规模计算证明的效率。然而，现实生活中的应用（例如，在使用深度神经网络进行私密推断的背景下）通常涉及高度复杂的计算，而现有的ZK协议在表达能力和可扩展性方面不足以有效地证明关于这些计算的结果。

在本文中，我们设计、开发并评估了一个ZK系统（Mystique），该系统允许在算术值和布尔值、公开承诺值和私密认证值、以及定点数和浮点数之间进行高效转换。针对大规模神经网络推断，我们还提出了一种改进的矩阵乘法ZK协议，与现有技术相比，性能提高了7倍。最后，我们将Mystique集成到Rosetta中，这是一个基于TensorFlow的隐私保护框架。

Mystique能够在28分钟内证明对使用承诺（私密）ResNet-101模型的私密图像推断的正确性，而在模型公开的情况下，仅需5分钟完成相同任务，与在CIFAR10数据集上进行非ZK执行相比，准确率仅下降了0.02%。我们的系统是首个支持对超过100层神经网络模型进行ZK证明且几乎没有准确率损失的系统。

## 关键词

+ Mystique零知识证明转换
+ 算术布尔混合ZK协议
+ 深度神经网络推断验证
+ 矩阵乘法ZK优化
+ 浮点定点转换证明
+ TensorFlow隐私保护框架
