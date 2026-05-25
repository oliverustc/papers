---
title: "Pairing-free blind signatures from standard assumptions in the rom"

标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 2024
modified: 2025-04-16 10:22:29
created: 2025-04-11 12:00:55
---

## Pairing-free blind signatures from standard assumptions in the rom

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-68376-3_7)

## 作者

+ Julia Kastner 
+ Ky Nguyen 
+ [Michael Reichle](Michael%20Reichle.md)
## 笔记

Blind Signatures are a useful primitive for privacy preserving applications such as electronic payments, e-voting, anonymous credentials, and more. However, existing practical blind signature schemes based on standard assumptions require either pairings or lattices. We present the first practical construction of a round-optimal blind signature in the random oracle model based on standard assumptions without resorting to pairings or lattices. In particular, our construction is secure under the strong RSA assumption and DDH (in pairing-free groups). For our construction, we provide a NIZK-friendly signature based on strong RSA, and efficiently instantiate a variant of Fischlin’s generic framework (CRYPTO’06). Our Blind Signature scheme has signatures of size 4.28 KB and communication cost 10.98 KB. On the way, we develop techniques that might be of independent interest. In particular, we provide efficient _relaxed_ range-proofs for large ranges with subversion zero-knowledge and compact commitments to elements of arbitrary groups.

以下是中文翻译：

盲签名是一种对隐私保护应用（如电子支付、电子投票、匿名凭证等）非常有用的基本原语。然而，现有的基于标准假设的实用盲签名方案要么依赖于配对，要么依赖于格。我们提出了第一种基于标准假设的、在随机预言模型中实现的轮次最优盲签名的实用构造，且不需要配对或格。特别地，我们的构造在强RSA假设和DDH（在无配对群中）下是安全的。对于我们的构造，我们提供了一种基于强RSA的NIZK友好签名，并高效地实现了Fischlin的通用框架（CRYPTO’06）的一种变体。我们的盲签名方案的签名大小为4.28 KB，通信成本为10.98 KB。在此过程中，我们开发了一些可能具有独立兴趣的技术。特别地，我们为大范围提供了高效的放松范围证明，具有零知识的次要性，并对任意群的元素提供紧凑的承诺。

## 关键词

+ 无配对盲签名标准假设ROM
+ 强RSA DDH最优轮次盲签名
+ NIZK友好签名Fischlin框架
+ 次要零知识大范围放松范围证明
+ 隐私支付电子投票匿名凭证