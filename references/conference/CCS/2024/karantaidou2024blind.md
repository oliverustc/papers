---
title: "Blind Multisignatures for Anonymous Tokens with Decentralized Issuance"
doi: 10.1145/3658644.3690364
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2024
created: 2025-05-09 09:45:34
modified: 2025-05-09 09:48:52
---
## Blind Multisignatures for Anonymous Tokens with Decentralized Issuance

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3658644.3690364)
+ [archive](https://eprint.iacr.org/2024/1406)

## 作者

+ [Ioanna Karantaidou](Ioanna%20Karantaidou.md)
+ Omar Renawi
+ [Foteini Baldimtsi](Foteini%20Baldimtsi.md)
+ Nikolaos Kamarinakis
+ [Jonathan Katz](Jonathan%20Katz.md)
+ Julian Loss

## 笔记

We propose the first constructions of anonymous tokens with decentralized issuance. Namely, we consider a dynamic set of signers/issuers; a user can obtain a token from any subset of the signers, which is publicly verifiable and unlinkable to the issuance process. To realize this new primitive we formalize the notion of blind multi-signatures (BMS), which allow a user to interact with multiple signers to obtain a (compact) signature; even if all the signers collude they are unable to link a signature to an interaction with any of them. We then present two BMS constructions, one based on BLS signatures and a second based on discrete logarithms without pairings. We prove security of both our constructions in the Algebraic Group Model. We also provide a proof-of-concept implementation and show that it has low-cost verification, which is the most critical operation in blockchain applications.

以下是中文翻译：

我们提出了首个具有去中心化发行功能的匿名令牌(anonymous tokens)构造方案。具体而言，我们考虑一个动态的签名者/发行者集合；用户可以从签名者的任意子集获得令牌，该令牌可公开验证且与发行过程不可关联。为实现这一新型原语，我们形式化定义了盲多重签名(blind multi-signatures, BMS)的概念，它允许用户与多个签名者交互以获得一个（紧凑的）签名；即使所有签名者串通，他们也无法将签名与任何一次交互关联起来。随后，我们提出了两种BMS构造方案，一种基于BLS签名(BLS signatures)，另一种基于不需要配对运算的离散对数(discrete logarithms)。我们在代数群模型(Algebraic Group Model)中证明了这两种构造方案的安全性。我们还提供了概念验证实现，并表明它具有低成本的验证操作，这是区块链应用中最关键的操作。

## 关键词

+ 盲多重签名
+ 匿名令牌
+ 去中心化发行
+ BLS签名
+ 不可关联性
+ 区块链