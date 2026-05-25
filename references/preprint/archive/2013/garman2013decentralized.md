---
title: "Decentralized anonymous credentials"
标题简称:
论文类型: preprint
预印本简称: archive
发表年份: 2013
created: 2025-05-15 10:34:27
modified: 2025-05-15 10:37:16
---

## Decentralized anonymous credentials

## 发表信息

+ [原文链接](https://eprint.iacr.org/2013/622)

## 作者

+ [Christina Garman](Christina%20Garman.md)
+ [Matthew Green](Matthew%20Green.md)
+ [Ian Miers](Ian%20Miers.md)
## 笔记

Anonymous credentials provide a powerful tool for making assertions about identity while maintaining privacy. However, a limitation of today's anonymous credential systems is the need for a trusted credential issuer --- which is both a single point of failure and a target for compromise. Furthermore, the need for such a trusted issuer can make it challenging to deploy credential systems in practice, particularly in the ad hoc network setting (e.g., anonymous peer-to-peer networks) where no single party can be trusted with this responsibility. In this work we propose a novel anonymous credential scheme that eliminates the need for a trusted credential issuer. Our approach builds on recent results in the area of electronic cash and uses techniques --- such as the calculation of a distributed transaction ledger --- that are currently in widespread deployment in the Bitcoin payment system. Using this decentralized ledger and standard cryptographic primitives, we propose and provide a proof of security for a basic anonymous credential system that allows users to make flexible identity assertions with strong privacy guarantees. Finally, we discuss a number of practical applications for our techniques, including resource management in ad hoc networks and prevention of Sybil attacks. We implement our scheme and measure its efficiency.

以下是中文翻译：

匿名凭证（anonymous credentials）为在保护隐私的同时对身份进行断言提供了一种强大的工具。然而，当今匿名凭证系统的一个局限性是需要一个可信的凭证颁发者 ——这既是一个单点故障，也是可能被攻击的目标。此外，对这样一个可信颁发者的需求使得在实践中部署凭证系统变得具有挑战性，尤其是在无法信任任何单一方承担此责任的特设网络（ad hoc network）环境中，如匿名点对点网络。

在本研究中，我们提出了一种新颖的匿名凭证方案，消除了对可信凭证颁发者的需求。我们的方法建立在电子现金领域的最新研究成果之上，并使用了目前在比特币支付系统中广泛部署的技术，如分布式交易账本的计算。利用这个去中心化的账本和标准密码学原语，我们提出并证明了一个基本的匿名凭证系统的安全性，该系统允许用户在强大的隐私保护保证下进行灵活的身份断言。最后，我们讨论了这些技术的多个实际应用，包括特设网络中的资源管理和预防女巫攻击（Sybil attacks）。我们实现了该方案并测量了其效率。

## 关键词

+ 去中心化匿名凭证系统
+ 无可信颁发者匿名身份断言
+ 区块链分布式账本密码应用
+ 特设网络资源管理
+ 抗女巫攻击隐私保护
+ 电子现金匿名凭证构建