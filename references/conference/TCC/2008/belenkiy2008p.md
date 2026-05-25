---
title: P-signatures and noninteractive anonymous credentials
标题简称: 
论文类型: conference
会议简称: TCC
发表年份: 2008
created: 2025-05-15 10:00:19
modified: 2025-05-15 10:30:28
---

## P-signatures and noninteractive anonymous credentials

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-540-78524-8_20)

## 作者

+ Mira Belenkiy
+ [Melissa Chase](Melissa%20Chase.md)
+ [Markulf Kohlweiss](Markulf Kohlweiss.md)
+ [Anna Lysyanskaya](Anna Lysyanskaya.md)

## 笔记

In this paper, we introduce P-signatures. A P-signature scheme consists of a signature scheme, a commitment scheme, and (1) an interactive protocol for obtaining a signature on a committed value; (2) a _non_ − _interactive_ proof system for proving that the contents of a commitment has been signed; (3) a noninteractive proof system for proving that a pair of commitments are commitments to the same value. We give a definition of security for P-signatures and show how they can be realized under appropriate assumptions about groups with a bilinear map. We make extensive use of the powerful suite of non-interactive proof techniques due to Groth and Sahai. Our P-signatures enable, for the first time, the design of a practical non-interactive anonymous credential system whose security does not rely on the random oracle model. In addition, they may serve as a useful building block for other privacy-preserving authentication mechanisms.

以下是中文翻译：

在本文中，我们介绍了P-签名(P-signatures)。一个P-签名方案由一个签名方案、一个承诺方案(commitment scheme)，以及以下三个部分组成：(1)一个用于获取承诺值签名的交互式协议；(2)一个用于证明承诺内容已被签名的非交互式证明系统；(3)一个用于证明一对承诺是对同一个值的承诺的非交互式证明系统。我们给出了P-签名的安全性定义，并展示了如何在适当的双线性映射群(groups with a bilinear map)假设下实现它们。我们广泛使用了Groth和Sahai开发的强大的非交互式证明技术套件。我们的P-签名首次使得设计一个实用的、安全性不依赖随机预言模型(random oracle model)的非交互式匿名凭证系统成为可能。此外，它们还可以作为其他隐私保护认证机制的有用构建模块。

## 关键词

+ P-签名匿名凭证
+ 非交互式匿名凭证系统
+ 双线性映射群密码假设
+ Groth-Sahai证明技术
+ 隐私保护认证机制
+ 承诺方案非交互证明