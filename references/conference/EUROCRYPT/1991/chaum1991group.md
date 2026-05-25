---
title: "Group signatures"
标题简称:
论文类型: conference
会议简称: EUROCRYPT
发表年份: 1991
created: 2025-05-26 03:43:20
modified: 2025-05-26 04:36:56
---

## Group signatures

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.5555/1754868.1754897)

## 作者

+ David Chaum
+ Eugène Van Heyst

## 笔记

In this paper we present a new type of signature for a group of persons, called a group signature, which has the following properties: (i) only members of the group can sign messages; (ii) the receiver can verify that it is a valid group signature, but cannot discover which group member made it; (iii) if necessary, the signature can be "opened", so that the person who signed the message is revealed.

The group signatures are a "generalization" of the credential/ membership authentication schemes, in which one person proves that he belongs to a certain group.

We present four schemes that satisfy the properties above. Not all these schemes arc based on the same cryptographic assumption. In some of the schemes a trusted centre is only needed during the setup; and in other schemes, each pason can create the group he belongs to.

以下是中文翻译：

在本文中，我们提出了一种新型的签名，称为群体签名（group signature），具有以下特性：(i) 只有群体的成员可以对消息进行签名；(ii) 接收者可以验证这是一个有效的群体签名，但无法发现是哪个群体成员进行了签名；(iii) 如有必要，签名可以被“揭示”，从而显示出签署该消息的人员。

群体签名是凭证/成员身份认证方案（credential/membership authentication schemes）的“推广”，在这些方案中，一个人证明他属于某个特定的群体。

我们提出了四种满足上述特性的方案。这些方案并不都是基于相同的密码学假设。在某些方案中，仅在设置期间需要一个受信任的中心；而在其他方案中，每个人都可以创建他所属的群体。

## 关键词

+ 群签名
+ 匿名性
+ 可追踪性
+ 可信中心
+ 密码学原语