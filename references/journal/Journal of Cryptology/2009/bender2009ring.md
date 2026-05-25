---
title: "Ring signatures: Stronger definitions, and constructions without random oracles"
标题简称:
论文类型: journal
期刊简称: Journal of Cryptology
发表年份: 2009
created: 2025-05-28 01:48:17
modified: 2025-05-28 01:48:23
---

## Ring signatures: Stronger definitions, and constructions without random oracles

## 发表信息

+ [原文链接](https://link.springer.com/article/10.1007/s00145-007-9011-9)

## 作者

+ Adam Bender
+ [Jonathan Katz](Jonathan%20Katz.md)
+ Ruggero Morselli

## 笔记

_Ring signatures_, first introduced by Rivest, Shamir, and Tauman, enable a user to sign a message so that a _ring_ of possible signers (of which the user is a member) is identified, without revealing exactly _which member_ of that ring actually generated the signature. In contrast to group signatures, ring signatures are completely “ad-hoc” and do not require any central authority or coordination among the various users (indeed, users do not even need to be aware of each other); furthermore, ring signature schemes grant users fine-grained control over the level of anonymity associated with any particular signature.

This paper has two main areas of focus. First, we examine previous definitions of security for ring signature schemes and suggest that most of these prior definitions are too weak, in the sense that they do not take into account certain realistic attacks. We propose new definitions of anonymity and unforgeability which address these threats, and give separation results proving that our new notions are strictly stronger than previous ones. Second, we show the first constructions of ring signature schemes in the standard model. One scheme is based on generic assumptions and satisfies our strongest definitions of security. Two additional schemes are more efficient, but achieve weaker security guarantees and more limited functionality.

以下是中文翻译：

环签名(Ring signatures)最初由Rivest、Shamir和Tauman提出，它使用户能够对消息进行签名，以便识别出一个可能的签名者环(该用户是其中的成员)，而不会透露究竟是环中的哪个成员实际生成了该签名。与群签名(Group signatures)不同，环签名完全是"临时性的"，不需要任何中央机构或用户之间的协调(实际上，用户甚至不需要知道彼此的存在)；此外，环签名方案让用户能够对与任何特定签名相关的匿名级别进行精细控制。

本文主要关注两个方面。首先，我们检查了环签名方案先前的安全性定义，并认为这些先前的定义大多过于薄弱，因为它们没有考虑某些现实的攻击。我们提出了新的匿名性和不可伪造性定义来应对这些威胁，并给出了分离结果，证明我们的新概念严格强于先前的概念。其次，我们展示了在标准模型(standard model)中环签名方案的首次构造。其中一个方案基于通用假设(generic assumptions)，满足我们最强的安全性定义。另外两个方案效率更高，但实现了较弱的安全保证和更有限的功能。

## 关键词

+ 环签名强安全性定义
+ 匿名性不可伪造性形式化
+ 标准模型环签名构造
+ 无随机预言模型安全证明
+ 临时性签名群组密码
+ 环签名安全性分离结果