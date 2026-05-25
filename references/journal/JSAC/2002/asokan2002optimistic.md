---
title: "Optimistic fair exchange of digital signatures"
标题简称:
论文类型: journal
期刊简称: JSAC
发表年份: 2002
---

## Optimistic fair exchange of digital signatures

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/839935)

## 作者

+ N. Asokan 
+ V. Shoup 
+ M. Waidner

## 笔记

We present a new protocol that allows two players to exchange digital signatures over the Internet in a fair way, so that either each player gets the other's signature, or neither player does. The obvious application is where the signatures represent items of value, for example, an electronic check or airline ticket. The protocol can also be adapted to exchange encrypted data. It relies on a trusted third party, but is "optimistic," in that the third party is only needed in cases where one player crashes or attempts to cheat. A key feature of our protocol is that a player can always force a timely and fair termination, without the cooperation of the other player, even in a completely asynchronous network. A specialization of our protocol can be used for contract signing; this specialization is not only more efficient, but also has the important property that the third party can be held accountable for its actions: if it ever cheats, this can be detected and proven.

以下是中文翻译：

我们提出了一种新的协议，允许两名参与者在互联网上以公平（fair）的方式交换数字签名（digital signatures）：即要么双方各自获得对方的签名，要么双方均无法获得。该协议的典型应用场景是当这些签名代表具有价值的物品时，例如电子支票（electronic check）或机票（airline ticket）。此外，该协议也可被适配用于交换加密数据（encrypted data）。

本协议依赖于一个可信第三方（trusted third party），但具有“乐观性”（optimistic）特征，即仅在一方参与者崩溃（crashes）或试图作弊（attempts to cheat）时才需要该第三方介入。我们协议的一个关键特性在于：即使在网络完全异步（completely asynchronous）且对方不配合的情况下，任一参与者也始终能够强制协议及时且公平地终止。

该协议的一个特化版本可用于合同签署（contract signing）。此特化版本不仅效率更高，还具备一个重要属性：可信第三方对其行为可被问责（held accountable）——若其存在任何作弊行为，均可被检测并予以证明（detected and proven）。

## 关键词

+ 公平数字签名交换协议
+ 乐观协议设计
+ 可问责可信第三方
+ 完全异步网络公平终止
+ 合同签署协议
+ 密码学公平交换原语