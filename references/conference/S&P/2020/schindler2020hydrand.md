---
title: "Hydrand: Efficient continuous distributed randomness"
标题简称:
论文类型: conference
会议简称: S&P
发表年份: 2020
created: 2025-04-28 17:16:05
modified: 2025-04-28 17:17:57
---

## Hydrand: Efficient continuous distributed randomness

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/9152802)

## 作者

+ Philipp Schindler 
+ Aljosha Judmayer 
+ Nicholas Stifter 
+ Edgar Weippl 

## 笔记

A reliable source of randomness is not only an essential building block in various cryptographic, security, and distributed systems protocols, but also plays an integral part in the design of many new blockchain proposals. Consequently, the topic of publicly-verifiable, bias-resistant and unpredictable randomness has recently enjoyed increased attention. In particular random beacon protocols, aimed at continuous operation, can be a vital component for current Proof-of-Stake based distributed ledger proposals. We improve upon previous random beacon approaches with HydRand, a novel distributed protocol based on publicly-verifiable secret sharing (PVSS) to ensure unpredictability, bias-resistance, and public-verifiability of a continuous sequence of random beacon values. Furthermore, HydRand provides guaranteed output delivery of randomness at regular and predictable intervals in the presence of adversarial behavior and does not rely on a trusted dealer for the initial setup. Compared to existing PVSS based approaches that strive to achieve similar properties, our solution improves scalability by lowering the communication complexity from O(n^3) to O(n^2). Furthermore, we are the first to present a detailed comparison of recently described schemes and protocols that can be used for implementing random beacons.

以下是中文翻译：

可靠的随机性来源不仅是各种密码学、安全性和分布式系统协议中的重要构建模块，而且在许多新区块链提案的设计中也扮演着不可或缺的角色。因此，可公开验证的、抗偏差的和不可预测的随机性这一主题最近受到了越来越多的关注。特别是针对持续运行的随机信标(random beacon)协议，可以成为当前基于权益证明(Proof-of-Stake)的分布式账本提案的重要组成部分。我们通过HydRand改进了之前的随机信标方法，这是一个基于可公开验证秘密共享(publicly-verifiable secret sharing, PVSS)的新型分布式协议，用于确保连续随机信标值序列的不可预测性、抗偏差性和可公开验证性。此外，HydRand在存在对抗性行为的情况下，能够以规律且可预测的时间间隔保证随机性的输出传递，并且不依赖于可信赖的经销商进行初始设置。与现有的试图实现类似特性的基于PVSS的方法相比，我们的解决方案通过将通信复杂度从$O(n^3)$降低到$O(n^2)$来提高可扩展性。此外，我们是首个对最近描述的可用于实现随机信标的方案和协议进行详细比较的研究。

## 关键词

+ 随机信标
+ 分布式随机性
+ 可公开验证秘密共享（PVSS）
+ 抗偏差随机性
+ 权益证明区块链
+ 可扩展性优化