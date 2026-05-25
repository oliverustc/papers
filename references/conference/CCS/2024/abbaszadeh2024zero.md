---
title: "Zero-Knowledge Proofs of Training for Deep Neural Networks"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2024

modified: 2025-05-13 03:18:55
created: 2025-05-13 09:23:43
---

## Zero-Knowledge Proofs of Training for Deep Neural Networks

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3658644.3670316)

## 作者

+ Kasra Abbaszadeh
+ [Christodoulos Pappas](Christodoulos%20Pappas.md)
+ [Jonathan Katz](Jonathan%20Katz.md)
+ [Dimitrios Papadopoulos](Dimitrios%20Papadopoulos.md)

## 笔记

A zero-knowledge proof of training (zkPoT) enables a party to prove that they have correctly trained a committed model based on a committed dataset without revealing any additional information about the model or the dataset. An ideal zkPoT should offer provable security and privacy guarantees, succinct proof size and verifier runtime, and practical prover efficiency. In this work, we present Kaizen, a zkPoT targeted for deep neural networks (DNNs) that achieves all these goals at once. Our construction enables a prover to iteratively train their model via (mini-batch) gradient descent, where the number of iterations need not be fixed in advance; at the end of each iteration, the prover generates a commitment to the trained model parameters attached with a succinct zkPoT, attesting to the correctness of the executed iterations. The proof size and verifier time are independent of the number of iterations.

Our construction relies on two building blocks. First, we propose an optimized GKR-style (sumcheck-based) proof system for the gradient-descent algorithm with concretely efficient prover cost; this allows the prover to generate a proof for each iteration. We then show how to recursively compose these proofs across multiple iterations to attain succinctness. As of independent interest, we propose a generic framework for efficient recursive composition of GKR-style proofs, along with aggregatable polynomial commitments.

Benchmarks indicate that Kaizen can handle the training of complex models such as VGG-11 with 10 million parameters and batch size 16. The prover runtime is 15 minutes per iteration, which is 24× faster than generic recursive proofs, with prover memory overhead 27× lower. The proof size is 1.63 megabytes, and the verifier runtime is only 130 milliseconds, where both are independent of the number of iterations and the size of the dataset.

以下是中文翻译：

训练零知识证明(zero-knowledge proof of training, zkPoT)使一方能够证明他们已基于承诺的数据集正确训练了承诺的模型，而无需透露关于模型或数据集的任何额外信息。理想的zkPoT应提供可证明的安全性和隐私保证、简洁的证明大小和验证者运行时间，以及实用的证明者效率。在本研究中，我们提出了Kaizen，一个针对深度神经网络(DNNs)的zkPoT，同时实现了所有这些目标。我们的构造使证明者能够通过(小批量)梯度下降迭代训练他们的模型，其中迭代次数无需预先固定；在每次迭代结束时，证明者生成对训练后模型参数的承诺，并附带简洁的zkPoT，以证明已执行迭代的正确性。证明大小和验证者时间与迭代次数无关。

我们的构造依赖于两个构建模块。首先，我们提出了一个优化的GKR风格(基于sumcheck)的证明系统，用于梯度下降算法，具有具体高效的证明者成本；这使得证明者能够为每次迭代生成证明。然后，我们展示了如何递归组合这些跨多次迭代的证明以实现简洁性。作为独立的研究兴趣，我们提出了一个通用框架，用于GKR风格证明的高效递归组合，以及可聚合的多项式承诺。

基准测试表明，Kaizen可以处理复杂模型的训练，如具有1000万参数和批量大小16的VGG-11。每次迭代的证明者运行时间为15分钟，比通用递归证明快24倍，证明者内存开销降低27倍。证明大小为1.63兆字节，验证者运行时间仅为130毫秒，这两个指标都与迭代次数和数据集大小无关。

## 关键词

+ 零知识证明
+ 深度神经网络
+ 梯度下降
+ GKR证明系统
+ 多项式承诺
+ 模型训练验证