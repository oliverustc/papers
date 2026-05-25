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

The recent advancements in deep learning have brought about significant changes in various aspects of people’s lives. Meanwhile, these rapid developments have raised concerns about the legitimacy of the training process of deep neural networks. To protect the intellectual properties of AI developers, directly examining the training process by accessing the model parameters and training data is often prohibited for verifiers. In response to this challenge, we present zero-knowledge deep learning (zkDL), an efficient zero-knowledge proof for deep learning training. To address the long-standing challenge of verifiable computations of non-linearities in deep learning training, we introduce zkReLU, a specialized proof for the ReLU activation and its backpropagation. zkReLU turns the disadvantage of non-arithmetic relations into an advantage, leading to the creation of FAC4DNN, our specialized arithmetic circuit design for modelling neural networks. This design aggregates the proofs over different layers and training steps, without being constrained by their sequential order in the training process. With our new CUDA implementation that achieves full compatibility with the tensor structures and the aggregated proof design, zkDL enables the generation of complete and sound proofs in less than a second per batch update for an 8-layer neural network with 10M parameters and a batch size of 64, while provably ensuring the privacy of data and model parameters. To our best knowledge, we are not aware of any existing work on zero-knowledge proof of deep learning training that is scalable to million-size networks.

以下是中文翻译：

深度学习领域的最新进展给人们生活的各个方面带来了重大变化。与此同时，这些快速发展也引发了人们对深度神经网络训练过程合法性的担忧。为了保护人工智能开发者的知识产权，验证者通常被禁止通过访问模型参数和训练数据来直接检查训练过程。针对这一挑战，我们提出了零知识深度学习(zkDL)，这是一种用于深度学习训练的高效零知识证明。

为了解决深度学习训练中非线性计算可验证性这一长期存在的挑战，我们引入了zkReLU，这是一种专门用于ReLU激活函数及其反向传播的证明方法。zkReLU将非算术关系的劣势转化为优势，促成了FAC4DNN的创建，这是我们专门为建模神经网络设计的算术电路。该设计可以在不受训练过程中顺序限制的情况下，聚合不同层和训练步骤的证明。

借助我们新开发的CUDA实现（该实现实现了与张量结构的完全兼容性和聚合证明设计），zkDL能够为一个具有1000万参数的8层神经网络（批量大小为64）在每次批量更新时生成完整且可靠的证明，用时不到一秒，同时可证明地确保了数据和模型参数的隐私性。据我们所知，目前还没有其他关于深度学习训练的零知识证明的工作能够扩展到百万规模的网络。

## 关键词

+ zkDL深度学习训练零知识证明
+ zkReLU激活函数反向传播证明
+ FAC4DNN神经网络算术电路
+ CUDA张量结构聚合证明
+ 深度学习训练完整性验证
+ 百万参数规模可扩展ZKP