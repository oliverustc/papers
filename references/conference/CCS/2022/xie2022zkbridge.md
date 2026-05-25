---
title: "zkBridge: Trustless Cross-chain Bridges Made Practical"
标题简称: zkBridge
论文类型: conference
会议简称: CCS
发表年份: 2022
modified: 2025-04-29 16:14:24
created: 2025-04-07 16:27:45
---

## zkBridge: Trustless Cross-chain Bridges Made Practical

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3548606.3560652)

## 作者

+ [Tiancheng Xie](Tiancheng%20Xie.md)
+ [Jiaheng Zhang](Jiaheng%20Zhang.md)
+ [Zerui Cheng](Zerui%20Cheng.md)
+ [Yupeng Zhang](Yupeng%20Zhang.md)
+ [Dan Boneh](Dan%20Boneh.md)
+ [Dawn Song](Dawn%20Song.md)

## 笔记

Blockchains have seen growing traction with cryptocurrencies reaching a market cap of over 1 trillion dollars, major institution investors taking interests, and global impacts on governments, businesses, and individuals.
Also growing significantly is the heterogeneity of the ecosystem where a variety of blockchains co-exist. Cross-chain bridge is a necessary building block in this multi-chain ecosystem. Existing solutions, however, either suffer from performance issues or rely on honesty assumptions of committees that significantly lower the security. Recurring attacks against bridges have cost users more than 1.5 billion USD. In this paper, we introduce zkBridge, an efficient cross-chain bridge that guarantees strong security without extra trust assumptions. With succinct proofs, zkBridge not only guarantees correctness, but also significantly reduces on-chain verification cost. We propose novel succinct proof protocols that are orders-of-magnitude faster than existing solutions for workload in zkBridge. With a modular design, zkBridge enables a few useful capabilities, including message passing, token transferring, and other computational logic operating on state changes from different chains. We fully implemented zkBridge between Cosmos and Ethereum and evaluated the end-to-end performance. The experiment shows that zkBridge achieves practical performance: it can generate a block header proof within 2 minutes, while verifying proofs on-chain costs less than 220K gas (the same as Groth16). Relaying a transaction from Cosmos to Ethereum costs 210K gas.

以下是中文翻译：

区块链在加密货币市场的推动下，正受到越来越多的关注，市场总值已超过1万亿美元，主要机构投资者也开始对此表现出兴趣，并对政府、企业和个人产生了全球性的影响。与此同时，生态系统的异质性也在显著增加，各种区块链共存于此。在这个多链生态系统中，跨链桥（cross-chain bridge）是一个必要的基础构件。然而，现有的解决方案要么存在性能问题，要么依赖于委员会的诚实假设，这显著降低了安全性。针对桥的重复攻击已经导致用户损失超过15亿美元。在本文中，我们介绍了zkBridge，这是一种高效的跨链桥，能够在没有额外信任假设的情况下保证强安全性。通过简洁的证明，zkBridge不仅保证了正确性，还显著降低了链上验证成本。我们提出了新颖的简洁证明协议，其速度比现有解决方案快几个数量级，适用于zkBridge中的工作负载。凭借模块化设计，zkBridge实现了一些有用的功能，包括消息传递、代币转移以及其他基于不同链的状态变化进行的计算逻辑。我们在Cosmos和Ethereum之间全面实现了zkBridge，并评估了端到端性能。实验结果表明，zkBridge实现了实用性能：它能够在2分钟内生成区块头证明，而链上验证证明的成本低于220K gas（与Groth16相同）。将交易从Cosmos中转发到Ethereum的成本为210K gas。

## 关键词

+ 跨链桥
+ 零知识证明
+ 区块链互操作性
+ 简洁论证
+ 无信任系统