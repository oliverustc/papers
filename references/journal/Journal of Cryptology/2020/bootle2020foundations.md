---
title: Foundations of fully dynamic group signatures
标题简称: 
论文类型: journal
期刊简称: Journal of Cryptology
发表年份: 2020
created: 2025-05-12 08:59:30
modified: 2025-05-23 01:36:00
---

## Foundations of fully dynamic group signatures

## 发表信息

+ [原文链接](https://link.springer.com/article/10.1007/s00145-020-09357-w)

## 作者

+ [Jonathan Bootle](Jonathan%20Bootle.md)
+ Andrea Cerulli
+ Pyrros Chaidos
+ Essam Ghadafi
+ [Jens Groth](Jens%20Groth.md)

相同的作者和相同的标题在[ACNS 2016](https://link.springer.com/chapter/10.1007/978-3-319-39555-5_7)年发表过一次，2020年估计为最新版

## 笔记

Group signatures allow members of a group to anonymously sign on behalf of the group. Membership is administered by a designated group manager. The group manager can also reveal the identity of a signer if and when needed to enforce accountability and deter abuse. For group signatures to be applicable in practice, they need to support fully dynamic groups, i.e., users may join and leave at any time. Existing security definitions for fully dynamic group signatures are informal, have shortcomings, and are mutually incompatible. We fill the gap by providing a formal rigorous security model for fully dynamic group signatures. Our model is general and is not tailored toward a specific design paradigm and can therefore, as we show, be used to argue about the security of different existing constructions following different design paradigms. Our definitions are stringent and when possible incorporate protection against maliciously chosen keys. We consider both the case where the group management and tracing signatures are administered by the same authority, i.e., a single group manager, and also the case where those roles are administered by two separate authorities, i.e., a group manager and an opening authority. We also show that a specialization of our model captures existing models for static and partially dynamic schemes. In the process, we identify a subtle gap in the security achieved by group signatures using revocation lists. We show that in such schemes new members achieve a slightly weaker notion of traceability. The flexibility of our security model allows to capture such relaxation of traceability.

以下是中文翻译：

群签名允许群组成员以匿名方式代表群组进行签名。群组成员资格由指定的群组管理员进行管理。群组管理员还可以在需要时揭示签名者的身份，以执行问责并防止滥用。为了使群签名在实践中可行，它们需要支持完全动态的群组，即用户可以随时加入和离开。现有的完全动态群签名安全定义存在非正式性、缺陷，且相互不兼容。我们通过提供一个严格的形式化安全模型来填补这一空白。

我们的模型具有普遍性，不局限于特定的设计范式，因此可以用来论证遵循不同设计范式的现有构造的安全性。我们的定义严格，并在可能的情况下包含了针对恶意选择密钥的保护。我们考虑了两种情况：一种是群组管理和签名追踪由同一机构（即单一群组管理员）管理的情况，另一种是这些角色由两个独立机构（即群组管理员和开启权限机构）管理的情况。

我们还表明，我们模型的特化版本可以涵盖现有的静态和部分动态方案的模型。在此过程中，我们发现了使用撤销列表的群签名方案在安全性方面存在一个微妙的差距。我们证明在这类方案中，新成员实现的可追踪性略微较弱。我们安全模型的灵活性使其能够捕捉到这种可追踪性的放宽。

方案特征：

强匿名性：一个签名的开启不会泄露同一签名者的其他签名

## 关键词

+ 完全动态群签名安全模型
+ 群签名形式化安全定义
+ 动态成员管理与撤销
+ 匿名性与可追踪性平衡
+ 恶意密钥选择保护
+ 撤销列表可追踪性弱化