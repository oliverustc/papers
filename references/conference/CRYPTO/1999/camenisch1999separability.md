---
title: "Separability and efficiency for generic group signature schemes"

标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 1999
created: 2025-05-26 05:11:53
modified: 2025-05-26 05:12:07
---

## Separability and efficiency for generic group signature schemes

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/3-540-48405-1_27)

## 作者

+ [Jan Camenisch](Jan%20Camenisch.md)
+ BRICS
+ Markus Michels

## 笔记

A cryptographic protocol possesses separability if the participants can choose their keys independently of each other. This is advantageous from a key-management as well as from a security point of view. This paper focuses on separability in group signature schemes. Such schemes allow a group member to sign messages anonymously on the group’s behalf. However, in case of this anonymity’s misuse, a trustee can reveal the originator of a signature. We provide a generic fully separable group signature scheme and present an efficient instantiation thereof. The scheme is suited for large groups; the size of the group’s public key and the length of signatures do not depend on the number of group member. Its efficiency is comparable to the most efficient schemes that do not offer separability and is an order of magnitude more efficient than a previous scheme that provides partial separability. As a side result, we provide efficient proofs of the equality of two discrete logarithms from _different_ groups and, more general, of the validity of polynomial relations in ℤ among discrete logarithms from _different_ groups.

以下是中文翻译：

一种加密协议如果参与者能够独立选择他们的密钥，则具有可分离性。这在密钥管理和安全性方面都是有利的。本文重点讨论群签名方案中的可分离性。这类方案允许群体成员代表群体匿名签署消息。然而，在这种匿名性被滥用的情况下，受托人可以揭示签名的发起者。我们提供了一种通用的完全可分离群签名方案，并展示了其高效的实例化。该方案适用于大型群体；群体的公钥大小和签名长度不依赖于群体成员的数量。其效率可与最有效的非可分离方案相媲美，并且比之前提供部分可分离性的方案高效一个数量级。作为附带结果，我们提供了来自不同群体的两个离散对数相等的高效证明，以及更一般地，关于来自不同群体的离散对数在ℤ中的多项式关系有效性的证明。

## 关键词

+ 可分离群签名方案
+ 匿名签名密钥独立选择
+ 离散对数不同群等式证明
+ 通用可分离群签名实例化
+ 受托人揭示签名者身份