---
title: "Hekaton: Horizontally-Scalable zkSNARKs Via Proof Aggregation"
标题简称: Hekaton
论文类型: conference
会议简称: CCS
发表年份: 2024
modified: 2025-04-23 15:20:35
created: 2025-04-09 14:04:08
---

## Hekaton: Horizontally-Scalable zkSNARKs Via Proof Aggregation

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3658644.3690282)
+ [code](https://github.com/Pratyush/hekaton-system)

## 作者

+ Michael Rosenberg
+ Tushar Mopuri
+ Hossein Hafezi
+ [Ian Miers](Ian%20Miers.md)
+ [Pratyush Mishra](Pratyush%20Mishra.md)
## 笔记

Zero-knowledge Succinct Non-interactive ARguments of Knowledge (zkSNARKs) allow a prover to convince a verifier of the correct execution of a large computation in private and easily-verifiable manner. These properties make zkSNARKs a powerful tool for adding accountability, scalability, and privacy to numerous systems such as blockchains and verifiable key directories. Unfortunately, existing zkSNARKs are unable to scale to large computations due to time and space complexity requirements for the prover algorithm. As a result, they cannot handle real-world instances of the aforementioned applications.

In this work, we introduce Hekaton, a zkSNARK that overcomes these barriers and can efficiently handle arbitrarily large computations. We construct Hekaton via a new ''distribute-and-aggregate'' framework that breaks up large computations into small chunks, proves these chunks in parallel in a distributed system, and then aggregates the resulting chunk proofs into a single succinct proof Underlying this framework is a new technique for efficiently handling data that is shared between chunks that we believe could be of independent interest.

We implement a distributed prover for Hekaton, and evaluate its performance on a compute cluster. Our experiments show that Hekaton achieves strong horizontal scalability (proving time decreases linearly as we increase the number of nodes in the cluster), and is able to prove large computations quickly: it can prove computations of size 2^35 gates in under an hour, which is much faster than prior work.

Finally, we also apply Hekaton to two applications of real-world interest: proofs of batched insertion for a verifiable key directory and proving correctness of RAM computations. In both cases, Hekaton is able to scale to handle realistic workloads with better efficiency than prior work.

以下是中文翻译：

零知识简洁非交互式知识证明（zkSNARKs）允许证明者以私密且易于验证的方式向验证者证明大规模计算的正确执行。这些特性使得zkSNARKs成为增强区块链和可验证密钥目录等众多系统的责任性、可扩展性和隐私性的强大工具。不幸的是，现有的zkSNARKs由于证明算法的时间和空间复杂性要求，无法扩展到大规模计算。因此，它们无法处理上述应用的真实实例。

在本研究中，我们提出了Hekaton，一种克服这些障碍并能够高效处理任意大规模计算的zkSNARK。我们通过一个新的“分布-聚合”（distribute-and-aggregate）框架构建Hekaton，该框架将大规模计算分解为小块，在分布式系统中并行证明这些小块，然后将生成的小块证明聚合为一个简洁的证明。该框架的基础是一种新技术，用于高效处理在小块之间共享的数据，我们认为这项技术可能具有独立的研究价值。

我们为Hekaton实现了一个分布式证明器，并在计算集群上评估其性能。我们的实验表明，Hekaton实现了强大的横向可扩展性（证明时间随着集群节点数量的增加而线性减少），并能够快速证明大规模计算：它可以在不到一个小时的时间内证明大小为 \(2^{35}\) 门的计算，这比之前的工作快得多。

最后，我们还将Hekaton应用于两个具有实际意义的应用：可验证密钥目录的批量插入证明和RAM计算的正确性证明。在这两种情况下，Hekaton都能够扩展以处理现实工作负载，并且效率优于之前的工作。

## 关键词

+ 零知识SNARK
+ 水平可扩展性
+ 证明聚合
+ 分布式系统
+ 并行证明
+ 可验证性