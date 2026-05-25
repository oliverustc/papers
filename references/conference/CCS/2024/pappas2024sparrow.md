---
title: "Sparrow: Space-Efficient zkSNARK for Data-Parallel Circuits and Applications to Zero-Knowledge Decision Trees"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2024
modified: 2025-05-13 03:19:46
created: 2025-05-13 09:23:43
---

## Sparrow: Space-Efficient zkSNARK for Data-Parallel Circuits and Applications to Zero-Knowledge Decision Trees

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3658644.3690318)

## 作者

+ [Christodoulos Pappas](Christodoulos%20Pappas.md)
+ [Dimitrios Papadopoulos](Dimitrios%20Papadopoulos.md)

## 笔记

_Space-efficient_ SNARKs aim to reduce the prover's space overhead which is one the main obstacles for deploying SNARKs in practice, as it can be prohibitively large (e.g., orders of magnitude larger than natively performing the computation). In this work, we propose Sparrow, a novel space-efficient zero-knowledge SNARK for data-parallel arithmetic circuits with two attractive features: (i) it is the first space-efficient scheme where, for a given field, the prover overhead increases with a multiplicative _sublogarithmic_ factor as the circuit size increases, and (ii) compared to prior space-efficient SNARKs that work for arbitrary arithmetic circuits, it achieves prover space _asymptotically smaller_ than the circuit size itself. Our key building block is a novel space-efficient sumcheck argument with improved prover time which may be of independent interest. Our experimental results for three use cases (_arbitrary data parallel circuits, multiplication trees, batch SHA256 hashing_) indicate Sparrow outperforms the prior state-of-the-art space-efficient SNARK for arithmetic circuits Gemini (Bootle et al., EUROCRYPT'22) by 3.2-28.7x in total prover space and 3.1-11.3x in prover time. We then use Sparrow to build _zero-knowledge proofs of tree training and prediction_, relying on its space efficiency to scale to large datasets and forests of multiple trees. Compared to a (non-space-efficient) optimal-time SNARK based on the GKR protocol, we observe prover space reduction of 16-240x for tree training while maintaining essentially the same prover and verifier times and proof size. Even more interestingly, _our prover requires comparable space to natively perform the underlying computation_. E.g., for a 400MB dataset, our prover only needs 1.4x more space than the native computation.

以下是中文翻译：

_空间效率_ SNARKs旨在减少证明者的空间开销，这是在实际部署SNARKs时面临的主要障碍之一，因为其开销可能过于庞大（例如，比原生计算所需的空间大几个数量级）。在本研究中，我们提出了Sparrow，这是一种新颖的空间高效零知识SNARK，专门用于数据并行算术电路，具有两个吸引人的特征：（i）这是第一个空间高效方案，对于给定的域，随着电路规模的增加，证明者的开销以乘法的_次对数_因子增加；（ii）与之前适用于任意算术电路的空间高效SNARK相比，它实现的证明者空间_渐近小于_电路规模本身。我们的关键构建模块是一个新颖的空间高效求和校验论证，具有改进的证明者时间，这可能具有独立的研究价值。我们针对三个用例（_任意数据并行电路、乘法树、批量SHA256哈希_）的实验结果表明，Sparrow在总证明者空间上比之前的最先进的算术电路空间高效SNARK Gemini（Bootle等，EUROCRYPT'22）提高了3.2-28.7倍，在证明者时间上提高了3.1-11.3倍。然后，我们使用Sparrow构建_树训练和预测的零知识证明_，依靠其空间效率以扩展到大数据集和多棵树的森林。与基于GKR协议的（非空间高效）最优时间SNARK相比，我们观察到树训练的证明者空间减少了16-240倍，同时基本保持相同的证明者和验证者时间以及证明大小。更有趣的是，_我们的证明者所需的空间与原生计算所需的空间相当_。例如，对于一个400MB的数据集，我们的证明者所需的空间仅比原生计算多1.4倍。

## 关键词

+ 零知识SNARK
+ 空间效率
+ 数据并行电路
+ 决策树
+ 求和校验
+ 证明者优化