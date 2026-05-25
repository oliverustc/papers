---
title: "CHURP: Dynamic-committee proactive secret sharing"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2019
modified: 2025-04-13 13:54:13
---

## CHURP: Dynamic-committee proactive secret sharing

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3319535.3363203)

## 作者

+ Sai Krishna Deepak Maram 
+ Fan Zhang 
+ Lun Wang 
+ Andrew Low 
+ [Yupeng Zhang](Yupeng%20Zhang.md) 
+ Ari Juels 
+ [Dawn Song](Dawn%20Song.md) 

## 笔记

We introduce CHURP (CHUrn-Robust Proactive secret sharing). CHURP enables secure secret-sharing in dynamic settings, where the committee of nodes storing a secret changes over time. Designed for blockchains, CHURP has lower communication complexity than previous schemes: $O(n)$ on-chain and $O(n^2)$ off-chain in the optimistic case of no node failures. CHURP includes several technical innovations: An efficient new proactivization scheme of independent interest, a technique (using asymmetric bivariate polynomials) for efficiently changing secret-sharing thresholds, and a hedge against setup failures in an efficient polynomial commitment scheme. We also introduce a general new technique for inexpensive off-chain communication across the peer-to-peer networks of permissionless blockchains. We formally prove the security of CHURP, report on an implementation, and present performance measurements.

以下是中文翻译：

我们介绍了CHURP(CHUrn-Robust Proactive secret sharing，抗节点更替的主动式秘密共享)。CHURP使得在动态环境下进行安全的秘密共享成为可能，在这种环境中存储秘密的节点委员会会随时间发生变化。CHURP专为区块链设计，相比之前的方案具有更低的通信复杂度：在没有节点故障的理想情况下，链上通信复杂度为O(n)，链下通信复杂度为O(n²)。

CHURP包含几项具有独立研究价值的技术创新：一个高效的新型主动化方案，一种用于高效改变秘密共享阈值的技术(使用非对称双变量多项式)，以及一种针对高效多项式承诺方案中设置失败的防护机制。我们还引入了一种新的通用技术，可以在无许可区块链的点对点网络中实现低成本的链下通信。

我们对CHURP的安全性进行了形式化证明，报告了其实现情况，并提供了性能测试结果。

## 关键词

+ 秘密共享
+ 动态委员会
+ 主动安全
+ 区块链
+ 密钥共享