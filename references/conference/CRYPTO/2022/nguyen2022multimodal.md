---
title: "Multimodal private signatures"
标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 2022
created: 2025-05-23 01:12:39
modified: 2025-05-23 02:50:19
---

## Multimodal private signatures

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-15979-4_27)
+ [archive](https://eprint.iacr.org/2022/1008)

## 作者

+ [Khoa Nguyen](Khoa%20Nguyen.md)
+ Fuchun Guo
+ [Willy Susilo](Willy%20Susilo.md)
+ Guomin Yang

## 笔记

We introduce Multimodal Private Signature (MPS) - an anonymous signature system that offers a novel accountability feature: it allows a designated opening authority to learn some partial information op about the signer's identity id, and nothing beyond. Such partial information can flexibly be defined as op=id (as in group signatures), or as op=0 (like in ring signatures), or more generally, as op=Gj(id), where Gj(⋅) is a certain disclosing function. Importantly, the value of op is known in advance by the signer, and hence, the latter can decide whether she/he wants to disclose that piece of information. The concept of MPS significantly generalizes the notion of tracing in traditional anonymity-oriented signature primitives, and can enable various new and appealing privacy-preserving applications. We formalize the definitions and security requirements for MPS. We next present a generic construction to demonstrate the feasibility of designing MPS in a modular manner and from commonly used cryptographic building blocks (ordinary signatures, public-key encryption and NIZKs). We also provide an efficient construction in the standard model based on pairings, and a lattice-based construction in the random oracle model.

以下是中文翻译：

我们提出了多模态私人签名（Multimodal Private Signature, MPS）- 一种匿名签名系统，它提供了一个新颖的问责功能：它允许指定的开启机构了解签名者身份id的某些部分信息op，且仅限于此。这种部分信息可以灵活地定义为op=id（如群签名中），或op=0（如环签名中），或更一般地，定义为op=Gj(id)，其中Gj(⋅)是某个披露函数。重要的是，签名者事先知道op的值，因此可以决定是否要披露该信息。

MPS概念显著地推广了传统匿名导向签名原语中的追踪概念，并能够实现各种新颖且吸引人的隐私保护应用。我们形式化了MPS的定义和安全性要求。接下来，我们提出了一个通用构造，以模块化的方式展示了如何从常用的密码学构建模块（普通签名、公钥加密和零知识证明（NIZKs））设计MPS的可行性。我们还在标准模型中基于配对（pairings）提供了一个高效的构造，以及在随机预言机（random oracle）模型中提供了一个基于格（lattice-based）的构造。

笔记：

相比于[参考文献 Bifurcated signatures: folding the accountability vs anonymity dilemma into a single private signing scheme (**EUROCRYPT 2021**)](libert2021bifurcated)，本文允许签名者在生成签名时，向指定的机构透露一部分信息op，这里的op的格式更加灵活，可以更一般地定义为$op=G(id)$

在群签名(group signature)中，披露函数G(·)基本上是恒等函数，而在BiAS中，G(·)是一个全有或全无(all-or-nothing)的函数。然而，正如MPS激励性示例中所提到的，在不同应用中平衡隐私和问责性需要一组更灵活、更细粒度的披露函数。在MPS中，这是通过两个步骤实现的：首先，我们引入一个签名函数F，用于确定消息M是否有效（例如，交易金额低于货币管理机构设定的限制），如果有效，则确定M的临界级别j；其次，我们定义一个披露函数族G = {Gj(·)}，基于M的临界级别向开启权威机构披露适当级别的身份信息（即Gj(id)）。值得注意的是，出于隐私考虑，我们还希望隐藏临界级别j，这意味着M可能是真实"消息"的转换，我们称之为M的见证w。展望未来，在本文提出的基于配对和基于格的构造中，我们使用M = COM(w)，其中COM(·)表示一个安全承诺方案。显然，MPS中针对开启权威机构的隐私保护比其他可追踪匿名签名更为复杂。具体来说，我们要求开启权威机构仅从有效签名中获取Gj(id)，而不获取其他任何信息。

更正式地说，MPS系统与一组签名函数F和一组披露函数{G1, ..., GK}相关联。当用户id想要使用签名函数F∈F对消息M进行签名时，它计算j = F(M, w, id)∈[0, K]，其中w是一个"证据(witness)"——用户可获得的与上下文相关的信息（直观上解释了为什么F(M, w, id) = j）。j的值决定了(M, w, id)的可签名性以及所得签名的问责性。具体来说，如果j = 0，则id不允许签名。否则，id应该能够获得一个有效签名，该签名可以被权威机构打开得到值Gj(id)。

相关调研：

本文被一篇survey引用：[SoK: Privacy-Preserving Signatures](https://eprint.iacr.org/2023/1039)


## 关键词

+ 密码学
+ 零知识
+ 协议