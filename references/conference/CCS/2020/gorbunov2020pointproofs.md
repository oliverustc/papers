---
title: "Pointproofs: Aggregating Proofs for Multiple Vector Commitments"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2020

modified: 2025-05-07 23:22:17
created: 2025-04-07 16:20:38
---

## Pointproofs: Aggregating Proofs for Multiple Vector Commitments

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3372297.3417244)

## 作者

+ Sergey Gorbunov
+ Leonid Reyzin
+ Hoeteck Wee
+ [Zhenfei Zhang](Zhenfei%20Zhang.md)

## 笔记

Vector commitments enable a user to commit to a sequence of values and provably reveal one or many values at specific posi- tions at a later time. In this work, we construct Pointproofs? a new vector commitment scheme that supports non-interactive aggregation of proofs across multiple commitments. Our construction enables any third party to aggregate a collection of proofs with respect to different, independently computed commitments into a single proof represented by an elliptic curve point of 48-bytes. In addition, our scheme is hiding: a commitment and proofs for some values reveal no information about the remaining values. We build Pointproofs and demonstrate how to apply them to blockchain smart contracts. In our example application, Pointproofs reduce bandwidth overheads for propagating a block of transactions by at least 60% compared to prior state- of-art vector commitments. Pointproofs are also efficient: on a single-thread, it takes 0.08 seconds to generate a proof for 8 values with respect to one commitment, 0.25 seconds to aggregate 4000 such proofs across multiple commitments into one proof, and 23 seconds (0.7 ms per value proven) to verify the aggregated proof.

以下是中文翻译：

向量承诺使用户能够对一系列值进行承诺，并在之后可证明地揭示特定位置的一个或多个值。在本研究中，我们构建了Pointproofs——一个新的向量承诺方案，它支持跨多个承诺的证明进行非交互式聚合。我们的构造使任何第三方都能够将针对不同的、独立计算的承诺的一系列证明聚合成一个由48字节椭圆曲线点表示的单一证明。此外，我们的方案具有隐藏性：对某些值的承诺和证明不会泄露关于其余值的任何信息。

我们构建了Pointproofs并展示了如何将其应用于区块链智能合约。在我们的示例应用中，与先前最先进的向量承诺相比，Pointproofs至少减少了60%的交易区块传播带宽开销。Pointproofs也很高效：在单线程上，为一个承诺中的8个值生成证明需要0.08秒，将4000个此类跨多个承诺的证明聚合成一个证明需要0.25秒，验证聚合证明需要23秒（每个被证明的值平均0.7毫秒）。

## 关键词

+ 向量承诺
+ 证明聚合
+ 区块链
+ 带宽优化
+ 密码承诺