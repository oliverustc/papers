---
title: "Two-round stateless deterministic two-party Schnorr signatures from pseudorandom correlation functions"
doi: 10.1007/978-3-031-38557-5_21

标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 2023
created: 2025-04-16 11:24:36
modified: 2025-04-16 13:44:38
---
## Two-round stateless deterministic two-party Schnorr signatures from pseudorandom correlation functions

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-38557-5_21)

## 作者

+ Yashvanth Kondi 
+ [Claudio Orlandi](Claudio%20Orlandi.md)
+ Lawrence Roy 

## 笔记

Schnorr signatures are a popular choice due to their simplicity, provable security, and linear structure that enables relatively easy threshold signing protocols. The deterministic variant of Schnorr (where the nonce is derived in a stateless manner using a PRF from the message and a long term secret) is widely used in practice since it mitigates the threats of a faulty or poor randomness generator (which in Schnorr leads to catastrophic breaches of security). Unfortunately, threshold protocols for the deterministic variant of Schnorr have so far been quite inefficient, as they make non black-box use of the PRF involved in the nonce generation.

In this paper, we present the first two-party threshold protocol for Schnorr signatures, where signing is stateless and deterministic, and only makes black-box use of the underlying cryptographic algorithms.

We present a protocol from general assumptions which achieves covert security, and a protocol that achieves full active security under standard factoring-like assumptions. Our protocols make crucial use of recent advances within the field of pseudorandom correlation functions (PCFs).

As an additional benefit, only two-rounds are needed to perform distributed signing in our protocol, connecting our work to a recent line of research on the trade-offs between round complexity and cryptographic assumptions for threshold Schnorr signatures.

以下是中文翻译：

Schnorr签名因其简单性、可证明的安全性以及能够实现相对简单的门限签名协议的线性结构而广受欢迎。Schnorr的确定性变体（其中随机数是通过PRF以无状态方式从消息和长期密钥中派生的）在实践中被广泛使用，因为它可以降低有缺陷或低质量随机数生成器带来的威胁（这在Schnorr中会导致灾难性的安全漏洞）。遗憾的是，到目前为止，Schnorr确定性变体的门限协议效率都相当低，因为它们对随机数生成中涉及的PRF进行了非黑盒使用。

在本论文中，我们提出了首个用于Schnorr签名的双方门限协议，其中签名过程是无状态且确定性的，并且仅对底层密码算法进行黑盒使用。

我们提出了一个基于一般假设且实现隐蔽安全的协议，以及一个在标准因子分解类假设下实现完全主动安全的协议。我们的协议关键地使用了伪随机相关函数（PCFs）领域的最新进展。

作为额外的优势，我们的协议仅需要两轮就能完成分布式签名，这将我们的工作与最近关于门限Schnorr签名在轮复杂度和密码学假设之间权衡的研究联系起来。

## 关键词

+ 无状态确定性两方Schnorr门限
+ PCF伪随机相关函数黑盒使用
+ 两轮签名因子分解主动安全
+ 抵抗随机数生成器故障门限
+ 轮复杂度密码假设权衡门限