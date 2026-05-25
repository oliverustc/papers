---
title: "Aggregatable subvector commitments for stateless cryptocurrencies"
标题简称:
论文类型: conference
会议简称: SCN
发表年份: 2020
---

## Aggregatable subvector commitments for stateless cryptocurrencies

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-030-57990-6_3)

## 作者

+ [[Alin Tomescu]]
+ Ittai Abraham 
+ Vitalik Buterin 
+ Justin Drake 
+ Dankrad Feist 
+ [Dmitry Khovratovich](Dmitry%20Khovratovich.md)
## 笔记

An aggregatable subvector commitment (aSVC) scheme is a vector commitment (VC) scheme that can aggregate multiple proofs into a single, small subvector proof. In this paper, we formalize aSVCs and give a construction from constant-sized polynomial commitments. Our construction is unique in that it has linear-sized public parameters, it can compute all constant-sized proofs in quasilinear time, it updates proofs in constant time and it can aggregate multiple proofs into a constant-sized subvector proof. Furthermore, our concrete proof sizes are small due to our use of pairing-friendly groups. We use our aSVC to obtain a payments-only stateless cryptocurrency with very low communication and computation overheads. Specifically, our constant-sized, aggregatable proofs reduce each block’s proof overhead to a single group element, which is optimal. Furthermore, our subvector proofs speed up block verification and our smaller public parameters further reduce block size.

以下是中文翻译：

一种可聚合子向量承诺（aggregatable subvector commitment, aSVC）方案是一种向量承诺（vector commitment, VC）方案，能够将多个证明聚合成一个紧凑的子向量证明。本文对 aSVC 进行了形式化定义，并基于常数大小的多项式承诺（polynomial commitments）给出了一种具体构造。

我们的构造具有独特优势：其公共参数（public parameters）大小为线性；所有常数大小的证明均可在拟线性时间（quasilinear time）内计算完成；证明的更新可在常数时间内完成；并且能够将多个证明聚合成一个常数大小的子向量证明。此外，由于我们采用了配对友好群（pairing-friendly groups），具体实现中的证明尺寸非常小。

我们将所提出的 aSVC 应用于构建一种仅支持支付功能的无状态加密货币（stateless cryptocurrency），显著降低了通信与计算开销。具体而言，我们所设计的常数大小且可聚合的证明将每个区块的证明开销降至单个群元素（group element），达到理论最优。此外，我们的子向量证明加速了区块验证过程，而更小的公共参数进一步缩减了区块大小。

## 关键词

+ 可聚合子向量承诺aSVC
+ 无状态加密货币
+ 多项式承诺
+ KZG常数大小证明
+ 配对友好群
+ 区块链验证效率