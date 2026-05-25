---
title: "Zombie: Middleboxes that Dont Snoop"
标题简称:
论文类型: conference
会议简称: NSDI
发表年份: 2024
modified: 2025-04-11 11:29:45
---

## Zombie: Middleboxes that Dont Snoop

## 发表信息

+ [原文链接](https://www.usenix.org/conference/nsdi24/presentation/zhang-collin)

## 作者

+ Collin Zhang 
+ Zachary DeStefano 
+ [Arasu Arun](Arasu%20Arun.md)
+ [[Joseph Bonneau]] 
+ [Paul Grubbs](Paul%20Grubbs.md)
+ [Michael Walfish](Michael%20Walfish.md)
## 笔记

Zero-knowledge middleboxes (ZKMBs) are a recent paradigm in which clients get privacy and middleboxes enforce policy: clients prove in zero knowledge that the plaintext underlying their encrypted traffic complies with network policies, such as DNS filtering. However, prior work had impractically poor performance and was limited in functionality.

This work presents Zombie, the first system built using the ZKMB paradigm. Zombie introduces techniques that push ZKMBs to the verge of practicality: preprocessing (to move the bulk of proof generation to idle times between requests), asynchrony (to remove proving and verifying costs from the critical path), and batching (to amortize some of the verification work). Zombie’s choices, together with these techniques, reduce client and middlebox overhead by ≈ 3.5×, lowering the critical path overhead for a DNS filtering application on commodity hardware to less than 300ms or, in the asynchronous configuration, to 0.

As an additional contribution that is likely of independent interest, Zombie introduces a portfolio of techniques to encode regular expressions in probabilistic (and zero-knowledge) proofs. These techniques significantly improve performance over a standard baseline, asymptotically and concretely. Zombie builds on this portfolio to support policies based on regular expressions, such as data loss prevention.

以下是中文翻译：

零知识中间盒（Zero-knowledge middleboxes, ZKMBs）是一种新兴的范式，客户可以获得隐私，而中间盒则执行政策：客户以零知识的方式证明其加密流量所对应的明文符合网络政策，例如 DNS 过滤。然而，之前的研究在性能上表现不佳，且功能有限。

本研究提出了 Zombie，这是第一个基于 ZKMB 范式构建的系统。Zombie 引入了一些技术，将 ZKMB 推向实用的边缘：预处理（将大部分证明生成移至请求之间的闲置时间）、异步（消除证明和验证成本对关键路径的影响）以及批处理（摊销部分验证工作）。Zombie 的选择以及这些技术使得客户端和中间盒的开销降低了约 3.5 倍，将商品硬件上 DNS 过滤应用的关键路径开销降低到 300 毫秒以下，或者在异步配置下降低到 0。

作为一个额外的贡献，Zombie 引入了一系列技术，用于在概率（和零知识）证明中编码正则表达式。这些技术在渐近和具体性能上显著改善了标准基线。Zombie 基于这一系列技术支持基于正则表达式的政策，例如数据丢失防护。

## 关键词

+ 零知识中间盒（ZKMB）
+ 网络策略执行
+ 加密流量验证
+ 正则表达式证明
+ DNS过滤
+ 隐私保护网络