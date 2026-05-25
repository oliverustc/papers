---
title: "Anonymous credentials light"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2013
created: 2025-05-09 11:02:29
modified: 2025-05-09 11:03:47
---

## Anonymous credentials light

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/2508859.2516687)

## 作者

+ [Foteini Baldimtsi](Foteini%20Baldimtsi.md)
+ [Anna Lysyanskaya](Anna%20Lysyanskaya.md)

## 笔记

We define and propose an efficient and provably secure construction of blind signatures with attributes. Prior notions of blind signatures did not yield themselves to the construction of anonymous credential systems, not even if we drop the unlinkability requirement of anonymous credentials. Our new notion in contrast is a convenient building block for anonymous credential systems. The construction we propose is efficient: it requires just a few exponentiations in a prime-order group in which the decisional Diffie-Hellman problem is hard. Thus, for the first time, we give a provably secure construction of anonymous credentials that can work in the elliptic group setting without bilinear pairings and is based on the DDH assumption. In contrast, prior provably secure constructions were based on the RSA group or on groups with pairings, which made them prohibitively inefficient for mobile devices, RFIDs and smartcards. The only prior efficient construction that could work in such elliptic curve groups, due to Brands, does not have a proof of security.

以下是中文翻译：

我们定义并提出了一种高效且可证明安全的带属性盲签名(blind signatures with attributes)构造方案。此前的盲签名概念并不适用于匿名凭证系统(anonymous credential systems)的构建，即使我们放弃匿名凭证的不可链接性要求也是如此。相比之下，我们的新概念是构建匿名凭证系统的一个便利组件。

我们提出的构造方案非常高效：它仅需要在判定性Diffie-Hellman问题(decisional Diffie-Hellman problem)难解的素数阶群中进行少量指数运算。因此，我们首次给出了一个可证明安全的匿名凭证构造方案，该方案可以在不需要双线性配对(bilinear pairings)的椭圆曲线群设置中工作，并且基于DDH假设(DDH assumption)。相比之下，先前的可证明安全构造方案都是基于RSA群或具有配对的群，这使得它们在移动设备、RFID和智能卡等场景中效率过低而无法使用。唯一一个可以在这种椭圆曲线群中工作的先前高效构造方案是由Brands提出的，但该方案缺乏安全性证明。

## 关键词

+ 匿名凭证
+ 盲签名
+ 椭圆曲线
+ DDH假设
+ 隐私保护