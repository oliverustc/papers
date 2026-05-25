---
title: "Witness encryption and its applications"
标题简称:
论文类型: conference
会议简称: STOC
发表年份: 2013
created: 2025-04-29 10:19:47
modified: 2025-04-29 10:22:25
---

## Witness encryption and its applications

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/2488608.2488667)

## 作者

+ [Sanjam Garg](Sanjam%20Garg.md) 
+ [Craig Gentry](Craig%20Gentry.md)
+ [Amit Sahai](Amit%20Sahai.md)
+ [Brent Waters](Brent%20Waters.md)
## 笔记

We put forth the concept of _witness encryption_. A witness encryption scheme is defined for an NP language L (with corresponding witness relation _R_). In such a scheme, a user can encrypt a message M to a particular problem instance x to produce a ciphertext. A recipient of a ciphertext is able to decrypt the message if x is in the language and the recipient knows a witness w where R(x,w) holds. However, if x is not in the language, then no polynomial-time attacker can distinguish between encryptions of any two equal length messages. We emphasize that the encrypter himself may have no idea whether $x$ is actually in the language. Our contributions in this paper are threefold. First, we introduce and formally define witness encryption. Second, we show how to build several cryptographic primitives from witness encryption. Finally, we give a candidate construction based on the NP-complete Exact Cover problem and Garg, Gentry, and Halevi's recent construction of "approximate" multilinear maps.

Our method for witness encryption also yields the first candidate construction for an open problem posed by Rudich in 1989: constructing computational secret sharing schemes for an NP-complete access structure.

以下是中文翻译：

我们提出了见证加密(witness encryption)的概念。见证加密方案是为NP语言L(及其对应的见证关系R)所定义的。在这样的方案中，用户可以将消息M加密到特定的问题实例x以生成密文。密文的接收者如果知道x在该语言中，并且知道满足R(x,w)的见证w，就能够解密该消息。然而，如果x不在该语言中，那么任何多项式时间的攻击者都无法区分任何两个等长消息的加密结果。我们强调，加密者本身可能并不知道$x$是否真的属于该语言。

本文的贡献主要有三个方面。首先，我们引入并正式定义了见证加密。其次，我们展示了如何基于见证加密构建若干密码学原语(cryptographic primitives)。最后，我们基于NP完全的精确覆盖(Exact Cover)问题和Garg、Gentry及Halevi最近提出的"近似"多线性映射(multilinear maps)构造，给出了一个候选方案。

我们的见证加密方法同时也为Rudich在1989年提出的一个开放问题提供了首个候选构造方案：为NP完全的访问结构(access structure)构造计算型秘密共享方案(computational secret sharing schemes)。

## 关键词

+ 见证加密Witness Encryption
+ NP语言加密方案
+ 多线性映射密码构造
+ 计算型秘密共享
+ 精确覆盖NP完全问题
+ 密码学原语构建
