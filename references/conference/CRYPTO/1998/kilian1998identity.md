---
title: "Identity escrow"
标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 1998
created: 2025-05-26 04:57:24
modified: 2025-05-26 04:58:13
---

## Identity escrow

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/BFb0055727)

## 作者

+ Joe Kilian
+ Erez Petrank

## 笔记

We introduce the concept of _escrowed identity_, an application of key-escrow ideas to the problem of authentication. In escrowed identity, one party _A_ does _not_ give his identity to another party _B_, but rather gives him information that would allow an authorized third party _E_ to determine _A_'s identity. However, _B_ receives a guarantee that _E_ can indeed determine _A_'s identity. We consider a number of possible features of escrowed identity schemes, and describe a variety of implementations that achieve various subsets of these features. In particular, we observe that group signature schemes can be used to escrow identities, achieving most (though not all) of the desired features.

The most interesting feature we consider is _separability_. The escrow agency is not involved in the day to day operation of the identification system, but is only called in when anonymity must be revoked. In the extreme case, there exist identity escrow schemes in which an arbitrary party (possessing a public key) can be designated an escrow agent without any knowledge or participation on their part until they are asked to revoke someone's anonymity.

以下是中文翻译：

我们引入了“托管身份”（escrowed identity）的概念，这是将密钥托管（key-escrow）思想应用于身份验证问题的一种方式。在托管身份中，一方A并不将其身份直接交给另一方B，而是提供给B一些信息，使得一个授权的第三方E能够确定A的身份。然而，B会得到一个保证，即E确实能够确定A的身份。我们考虑了托管身份方案的一些可能特性，并描述了实现这些特性的多种方案。特别地，我们观察到，群签名（group signature）方案可以用来托管身份，能够实现大部分（尽管不是全部）所需的特性。

我们考虑的最有趣的特性是可分离性（separability）。托管机构不参与身份识别系统的日常操作，而仅在需要撤销匿名性时才被召唤。在极端情况下，存在一些身份托管方案，其中任意一方（拥有公钥）可以被指定为托管代理，而在其被要求撤销某人的匿名性之前，他们对此没有任何知识或参与。
## 关键词

+ 身份托管
+ 匿名撤销
+ 群签名
+ 密钥托管
+ 身份验证
