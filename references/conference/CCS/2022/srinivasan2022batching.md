---
title: "Batching, aggregation, and zero-knowledge proofs in bilinear accumulators"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2022
modified: 2025-04-16 10:12:26
created: 2025-04-13 16:52:12
---

## Batching, aggregation, and zero-knowledge proofs in bilinear accumulators

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3548606.3560676)

## 作者

+ Shravan Srinivasan 
+ [Ioanna Karantaidou](Ioanna%20Karantaidou.md)
+ [Foteini Baldimtsi](Foteini%20Baldimtsi.md)
+ [Charalampos Papamanthou](Charalampos%20Papamanthou.md) 

## 笔记

An accumulator is a cryptographic primitive that allows a prover to succinctly commit to a set of values while being able to provide proofs of (non-)membership. A batch proof is an accumulator proof that can be used to prove (non-)membership of multiple values simultaneously.

以下是中文翻译：

累加器是一种密码学原语，它允许证明者简洁地对一组值进行承诺，同时能够提供（非）成员资格的证明。批量证明则是一种累加器证明，可用于同时验证多个值的（非）成员资格。

In this work, we present a zero-knowledge batch proof with constant proof size and constant verification in the Bilinear Pairings (BP) setting. Our scheme is 16x to 42x faster than state-of-the-art SNARK-based zero-knowledge batch proofs in the RSA setting. Additionally, we propose protocols that allow a prover to aggregate multiple individual non-membership proofs, in the BP setting, into a single batch proof of constant size. Our construction for aggregation satisfies a strong soundness definition - one where the accumulator value can be chosen arbitrarily.  
在这项工作中，我们提出了一种在双线性配对（BP）环境下具有恒定证明大小和恒定验证时间的零知识批量证明方案。相较于RSA环境下最先进的基于SNARK的零知识批量证明，我们的方案速度提升了16至42倍。此外，我们还设计了一套协议，允许证明者在BP环境下将多个独立的非成员证明聚合成一个固定大小的批量证明。我们的聚合构建满足严格的安全性定义——即使累加器值可被任意选择，方案依然安全可靠。

We evaluate our techniques and systematically compare them with RSA-based alternatives. Our evaluation results showcase several scenarios for which BP accumulators are clearly preferable and can serve as a guideline when choosing between the two types of accumulators.  
我们评估了自身技术，并系统性地将其与基于RSA的方案进行了对比。评估结果揭示了若干场景下，BP累加器明显更优，这为在两种累加器间做出选择提供了指导原则。

## 关键词

+ 双线性配对
+ 累加器
+ 零知识证明
+ 批量证明
+ 成员资格