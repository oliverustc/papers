---
title: "BalanceProofs: Maintainable vector commitments with fast aggregation"
标题简称:
论文类型: conference
会议简称: USENIX Security
发表年份: 2023
created: 2025-04-17 10:20:42
modified: 2025-04-17 10:24:04
---

## BalanceProofs: Maintainable vector commitments with fast aggregation

## 发表信息

+ [原文链接](https://www.usenix.org/conference/usenixsecurity23/presentation/wang-weijie)

## 作者

+ Weijie Wang 
+ Annie Ulichney 
+ [Charalampos Papamanthou](Charalampos%20Papamanthou.md) 

## 笔记

We present BalanceProofs, the first vector commitment that is _maintainable_ (i.e., supporting sublinear updates) while also enjoying fast proof aggregation and verification. The basic version of BalanceProofs has _O_(_√n_log_n_) update time and _O_(_√n_) query time and its constant-size aggregated proofs can be produced and verified in milliseconds. In particular, BalanceProofs improves the aggregation time and aggregation verification time of the only known maintainable and aggregatable vector commitment scheme, Hyperproofs (USENIX SECURITY 2022), by up to 1000× and up to 100× respectively. Fast verification of aggregated proofs is particularly useful for applications such as stateless cryptocurrencies (and was a major bottleneck for Hyperproofs), where an aggregated proof of balances is produced once but must be verified multiple times and by a large number of nodes. As a limitation, the updating time in BalanceProofs compared to Hyperproofs is roughly 6× slower, but always stays in the range from 10 to 18 milliseconds. We finally study useful tradeoffs in BalanceProofs between (aggregate) proof size, update time and (aggregate) proof computation and verification, by introducing a bucketing technique, and present an extensive evaluation as well as a comparison to Hyperproofs.

以下是中文翻译：

我们提出了BalanceProofs，这是第一个可维护的向量承诺（vector commitment），即支持亚线性更新，同时还具有快速的证明聚合和验证功能。BalanceProofs的基本版本具有 $O(\sqrt{n} \log n)$的更新时间和 $O(\sqrt{n})$ 的查询时间，其常数大小的聚合证明可以在毫秒级内生成和验证。特别地，BalanceProofs在聚合时间和聚合验证时间上，相较于唯一已知的可维护和可聚合的向量承诺方案Hyperproofs（USENIX SECURITY 2022），分别提高了多达1000倍和100倍。快速验证聚合证明对于无状态加密货币等应用特别有用（而这也是Hyperproofs的主要瓶颈），在这些应用中，余额的聚合证明只需生成一次，但必须由大量节点多次验证。作为一个限制，与Hyperproofs相比，BalanceProofs的更新时间大约慢了6倍，但始终保持在10到18毫秒之间。最后，我们通过引入分桶技术，研究了BalanceProofs在（聚合）证明大小、更新时间和（聚合）证明计算与验证之间的有用权衡，并进行了广泛的评估以及与Hyperproofs的比较。

## 关键词

+ BalanceProofs可维护向量承诺
+ 亚线性更新向量承诺
+ 聚合证明快速验证
+ 无状态加密货币余额证明
+ Hyperproofs性能改进
+ 分桶技术证明优化

Hyperproof:
[Hyperproofs: Aggregating and Maintaining Proofs in Vector Commitments (**USENIX Security 2022**)](srinivasan2022hyperproofs)
