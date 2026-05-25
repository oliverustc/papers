---
title: "Matproofs: Maintainable matrix commitment with efficient aggregation"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2022
---

## Matproofs: Maintainable matrix commitment with efficient aggregation

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3548606.3560591)

## 作者

+ Jing Liu 
+ Liang Feng Zhang 


## 笔记

We present Matproofs, a matrix commitment scheme that allows one to commit to any matrix and then open any subset of the matrix entries. If we encode any vector as a matrix, by committing to the matrix Matproofs may function well as a vector commitment (VC) scheme. We show that Matproofs are simultaneously concise, aggregatable, easily updatable and maintainable. With these promising features, Matproofs give solutions to payment-only stateless cryptocurrencies with lower bandwidth and computational complexity. Compared with Hyperproofs, the only existing VC scheme that is simultaneously aggregatable, easily updatable and maintainable, Matproofs achieve the additional property of conciseness. Furthermore, in the worst case, the proof aggregation and verification in Matproofs are 700 x and 10 x faster than Hyperproofs, respectively.

以下是中文翻译：

我们提出了 Matproofs，一种矩阵承诺（matrix commitment）方案，允许用户对任意矩阵进行承诺，并随后打开（即揭示并验证）该矩阵中任意子集的元素。若将任意向量编码为矩阵，则通过对该矩阵进行承诺，Matproofs 亦可有效作为向量承诺（Vector Commitment, VC）方案使用。我们证明，Matproofs 同时具备简洁性（conciseness）、可聚合性（aggregatability）、易于更新性（easy updatable）和可维护性（maintainable）。

凭借上述优势特性，Matproofs 为仅支持支付功能的无状态加密货币（payment-only stateless cryptocurrencies）提供了更优解决方案，显著降低了通信带宽与计算复杂度。与 Hyperproofs（目前唯一同时具备可聚合性、易于更新性和可维护性的向量承诺方案）相比，Matproofs 进一步实现了简洁性。此外，在最坏情况下，Matproofs 的证明聚合与验证速度分别比 Hyperproofs 快 700 倍和 10 倍。

## 关键词

+ 矩阵承诺
+ 向量承诺
+ 简洁性
+ 无状态加密货币
+ 证明聚合