---
title: "Collision-free accumulators and fail-stop signature schemes without trees"
标题简称:
论文类型: conference
会议简称: EUROCRYPT
发表年份: 1997
created: 2025-04-22 09:11:17
modified: 2025-04-22 09:11:47
---

## Collision-free accumulators and fail-stop signature schemes without trees

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/3-540-69053-0_33)

## 作者

+ Niko Barić 
+ Birgit Pfitzmann  

## 笔记

据说是最早的RSA累加器

One-way accumulators, introduced by Benaloh and de Mare, can be used to accumulate a large number of values into a single one, which can then be used to authenticate every input value without the need to transmit the others. However, the one-way property does is not sufficient for all applications.

In this paper, we generalize the definition of accumulators and define and construct a collision-free subtype. As an application, we construct a fail-stop signature scheme in which many one-time public keys are accumulated into one short public key. In contrast to previous constructions with tree authentication, the length of both this public key and the signatures can be independent of the number of messages that can be signed.

以下是中文翻译：

由Benaloh和de Mare提出的单向累加器可以将大量数值累积为单个值，该值可用于认证每个输入值，而无需传输其他值。然而，单向性质对于所有应用场景并不足够。

在本文中，我们推广了累加器的定义，并定义和构造了一种无碰撞子类型（collision-free subtype）。作为应用，我们构造了一种防失败签名方案（fail-stop signature scheme），其中多个一次性公钥被累积为一个短公钥。与先前基于树认证（tree authentication）的构造不同，该公钥和签名的长度可以与可签名消息的数量无关。

## 关键词

+ 无碰撞累加器
+ RSA累加器
+ 防失败签名
+ 单向累加器
+ 公钥认证