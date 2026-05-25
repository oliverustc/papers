---
title: "Towards scalable threshold cryptosystems"
标题简称:
论文类型: conference
会议简称: S&P
发表年份: 2020
created: 2025-04-17 10:43:04
modified: 2025-04-17 10:43:50
---

## Towards scalable threshold cryptosystems

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/9152696)

## 作者

+ [[Alin Tomescu ]]
+ Robert Chen 
+ Yiming Zheng 
+ Ittai Abraham 
+ Benny Pinkas 
+ Guy Golan Gueta 
+ Srinivas Devadas 

## 笔记

The resurging interest in Byzantine fault tolerant systems will demand more scalable threshold cryptosystems. Unfortunately, current systems scale poorly, requiring time quadratic in the number of participants. In this paper, we present techniques that help scale threshold signature schemes (TSS), verifiable secret sharing (VSS) and distributed key generation (DKG) protocols to hundreds of thousands of participants and beyond. First, we use efficient algorithms for evaluating polynomials at multiple points to speed up computing Lagrange coefficients when aggregating threshold signatures. As a result, we can aggregate a 130,000 out of 260,000 BLS threshold signature in just 6 seconds (down from 30 minutes). Second, we show how "authenticating" such multipoint evaluations can speed up proving polynomial evaluations, a key step in communication-efficient VSS and DKG protocols. As a result, we reduce the asymptotic (and concrete) computational complexity of VSS and DKG protocols from quadratic time to quasilinear time, at a small increase in communication complexity. For example, using our DKG protocol, we can securely generate a key for the BLS scheme above in 2.3 hours (down from 8 days). Our techniques improve performance for thresholds as small as 255 and generalize to any Lagrange-based threshold scheme, not just threshold signatures. Our work has certain limitations: we require a trusted setup, we focus on synchronous VSS and DKG protocols and we do not address the worst-case complaint overhead in DKGs. Nonetheless, we hope it will spark new interest in designing large-scale distributed systems.

以下是中文翻译：

对拜占庭容错系统日益增长的兴趣将需要更具可扩展性的门限密码系统。不幸的是，当前的系统扩展性较差，所需时间与参与者数量的平方成正比。本文提出了一些技术，帮助将门限签名方案（Threshold Signature Schemes, TSS）、可验证秘密共享（Verifiable Secret Sharing, VSS）和分布式密钥生成（Distributed Key Generation, DKG）协议扩展到数十万参与者及以上。首先，我们使用高效算法在多个点上评估多项式，以加快在聚合门限签名时计算拉格朗日系数的速度。因此，我们可以在仅6秒内聚合130,000个来自260,000个BLS门限签名（从30分钟缩短）。其次，我们展示了如何“认证”这种多点评估，以加速证明多项式评估的过程，这是通信高效的VSS和DKG协议中的关键步骤。因此，我们将VSS和DKG协议的渐近（和具体）计算复杂度从平方时间降低到准线性时间，同时通信复杂度仅小幅增加。例如，使用我们的DKG协议，我们可以在2.3小时内安全地为上述BLS方案生成密钥（从8天缩短）。我们的技术在门限为255时提高了性能，并且可以推广到任何基于拉格朗日的门限方案，而不仅限于门限签名。我们的工作有一定的局限性：我们需要一个可信的设置，专注于同步的VSS和DKG协议，并且没有解决DKG中的最坏情况投诉开销。尽管如此，我们希望这能激发人们对设计大规模分布式系统的新兴趣。

## 关键词

+ 门限密码系统可扩展性
+ 分布式密钥生成（DKG）
+ 可验证秘密共享（VSS）
+ BLS门限签名
+ 多点多项式估值
+ 准线性复杂度