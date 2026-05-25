---
title: "Election Eligibility with OpenID: Turning Authentication into Transferable Proof of Eligibility"
标题简称:
论文类型: conference
会议简称: USENIX Security
发表年份: 2024
created: 2025-04-29 17:24:25
modified: 2025-05-07 21:46:25
---

## Election Eligibility with OpenID: Turning Authentication into Transferable Proof of Eligibility

## 发表信息

+ [原文链接](https://www.usenix.org/conference/usenixsecurity24/presentation/cortier)

## 作者

+ Véronique Cortier 
+ Alexandre Debant 
+ Anselme Goetschmann 
+ Lucca Hirschi 

## 笔记

Eligibility checks are often abstracted away or omitted in voting protocols, leading to situations where the voting server can easily stuff the ballot box. One reason for this is the difficulty of bootstraping the authentication material for voters without relying on trusting the voting server.  

In this paper, we propose a new protocol that solves this problem by building on OpenID, a widely deployed authentication protocol. Instead of using it as a standard authentication means, we turn it into a mechanism that delivers transferable proofs of eligibility. Using zk-SNARK proofs, we show that this can be done without revealing any compromising information, in particular, protecting everlasting privacy. Our approach remains efficient and can easily be integrated into existing protocols, as we have done for the Belenios voting protocol. We provide a full-fledged proof of concept along with benchmarks showing our protocol could be realistically used in large-scale elections.  

以下是中文翻译：

在投票协议中，资格检查通常被抽象或省略，导致投票服务器很容易塞满投票箱的情况。造成这种情况的一个原因是，在不依赖信任投票服务器的情况下，很难为选民引导身份验证材料。

在本文中，我们提出了一种新协议，该协议通过构建 OpenID（一种广泛部署的身份验证协议）来解决这个问题。我们没有将其用作标准身份验证手段，而是将其转变为一种提供可转让资格证明的机制。使用 zk-SNARK 证明，我们表明这可以在不泄露任何泄露信息的情况下完成，特别是保护永久隐私。我们的方法仍然高效，并且可以很容易地集成到现有协议中，就像我们对 Belenios 投票协议所做的那样。我们提供了全面的概念验证以及基准测试，表明我们的协议可以实际用于大规模选举。

## 关键词

+ OpenID选举资格证明
+ 可转让资格证明协议
+ zk-SNARK隐私选举系统
+ Belenios投票协议集成
+ 永久隐私选举认证
+ 数字身份资格验证
