---
title: "Fully adaptive schnorr threshold signatures"

标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 2023
created: 2025-05-07 22:09:02
modified: 2025-05-07 22:21:03
---

## Fully adaptive schnorr threshold signatures

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-38557-5_22)

## 作者

+ Elizabeth Crites 
+ Chelsea Komlo 
+ [Mary Maller](Mary%20Maller.md)
## 笔记

We prove adaptive security of a simple three-round threshold Schnorr signature scheme, which we call $\textsf{Sparkle}$. The standard notion of security for threshold signatures considers a _static_ adversary – one who must declare which parties are corrupt at the beginning of the protocol. The stronger _adaptive_ adversary can at any time corrupt parties and learn their state. This notion is natural and practical, yet not proven to be met by most schemes in the literature.

In this paper, we demonstrate that $\textsf{Sparkle}$ achieves several levels of security based on different corruption models and assumptions. To begin with, $\textsf{Sparkle}$ is statically secure under minimal assumptions: the discrete logarithm assumption (DL) and the random oracle model (ROM). If an adaptive adversary corrupts fewer than t/2 out of a threshold of t+1 signers, then $\textsf{Sparkle}$ is adaptively secure under a weaker variant of the one-more discrete logarithm assumption (AOMDL) in the ROM. Finally, we prove that $\textsf{Sparkle}$ achieves _full_ adaptive security, with a corruption threshold of t, under AOMDL in the algebraic group model (AGM) with random oracles. Importantly, we show adaptive security without requiring secure erasures. Ours is the first proof achieving full adaptive security without exponential tightness loss for _any_ threshold Schnorr signature scheme; moreover, the reduction is tight.

以下是中文翻译：

我们证明了一个简单的三轮门限Schnorr签名方案的自适应安全性，我们称之为$\textsf{Sparkle}$。门限签名的标准安全性概念考虑的是静态对手(static adversary) - 即必须在协议开始时就声明哪些参与方被破坏。更强的自适应对手(adaptive adversary)可以在任何时候破坏参与方并获知其状态。这种概念既自然又实用，但文献中的大多数方案都未能证明满足这一要求。

在本文中，我们证明了$\textsf{Sparkle}$在不同的破坏模型和假设下实现了多个层次的安全性。首先，$\textsf{Sparkle}$在最小假设下实现了静态安全性：离散对数假设(discrete logarithm assumption, DL)和随机预言机模型(random oracle model, ROM)。如果自适应对手在t+1个签名者中破坏少于t/2个，那么$\textsf{Sparkle}$在ROM中基于一个较弱版本的一次性离散对数假设(one-more discrete logarithm assumption, AOMDL)实现自适应安全性。最后，我们证明$\textsf{Sparkle}$在代数群模型(algebraic group model, AGM)和随机预言机下，基于AOMDL实现了完全自适应安全性，其破坏阈值为t。重要的是，我们证明了自适应安全性而无需安全擦除。我们的证明是首次为任意门限Schnorr签名方案实现完全自适应安全性且不会导致指数级紧密度损失；此外，这个归约是紧的。

## 关键词

+ Sparkle完全自适应门限Schnorr
+ 自适应安全无安全擦除门限
+ AOMDL假设代数群随机预言
+ 静态自适应腐败门限签名安全
+ 紧归约首个完全自适应门限