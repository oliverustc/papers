---
title: "Experimenting with collaborative zk-SNARKs: Zero-Knowledge proofs for distributed secrets"
标题简称:
论文类型: conference
会议简称: USENIX Security
发表年份: 2022
modified: 2025-04-13 14:36:11
---

## Experimenting with collaborative zk-SNARKs: Zero-Knowledge proofs for distributed secrets

## 发表信息

+ [原文链接](https://www.usenix.org/conference/usenixsecurity22/presentation/ozdemir)

## 作者

+ [Alex Ozdemir](Alex%20Ozdemir.md) 
+ [Dan Boneh](Dan%20Boneh.md) 

## 笔记

A zk-SNARK is a powerful cryptographic primitive that provides a succinct and efficiently checkable argument that the prover has a witness to a public NP statement, without revealing the witness. However, in their native form, zk-SNARKs only apply to a secret witness held by a single party. In practice, a collection of parties often need to prove a statement where the secret witness is distributed or shared among them.

We implement and experiment with collaborative zkSNARKs: proofs over the secrets of multiple, mutually distrusting parties. We construct these by lifting conventional zk-SNARKs into secure protocols among N provers to jointly produce a single proof over the distributed witness. We optimize the proof generation algorithm in pairing-based zkSNARKs so that algebraic techniques for multiparty computation (MPC) yield efficient proof generation protocols. For some zk-SNARKs, optimization is more challenging. This suggests MPC "friendliness" as an additional criterion for evaluating zk-SNARKs.

We implement three collaborative proofs and evaluate the concrete cost of proof generation. We find that over a 3Gb/s link, security against a malicious minority of provers can be achieved with approximately the same runtime as a single prover. Security against N −1 malicious provers requires only a 2× slowdown. This efficiency is unusual since most computations slow down by orders of magnitude when securely distributed. This efficiency means that most applications that can tolerate the cost of a single-prover proof should also be able to tolerate the cost of a collaborative proof.

以下是中文翻译：

zk-SNARK（零知识简洁非交互式论证）是一种强大的密码学原语，它提供了一种简洁且高效可验证的论证，证明者拥有一个公共 NP 语句的见证，而不泄露该见证。然而，在其原始形式中，zk-SNARK 仅适用于由单一方持有的秘密见证。在实际应用中，多个方往往需要证明一个语句，而该秘密见证在他们之间分布或共享。

我们实现并实验了协作 zk-SNARK：针对多个相互不信任方的秘密进行的证明。我们通过将传统 zk-SNARK 提升为 N 个证明者之间的安全协议，从而共同生成一个关于分布式见证的单一证明。我们优化了基于配对的 zk-SNARK 中的证明生成算法，使得多方计算（MPC）的代数技术能够产生高效的证明生成协议。对于某些 zk-SNARK，优化更具挑战性。这表明 MPC 的“友好性”可以作为评估 zk-SNARK 的一个额外标准。

我们实现了三个协作证明，并评估了证明生成的具体成本。我们发现，在 3Gb/s 的链路上，针对恶意少数证明者的安全性可以在与单一证明者大致相同的运行时间内实现。针对 N−1 个恶意证明者的安全性只需 2 倍的减速。这种效率是非常罕见的，因为大多数计算在安全分布时会减慢几个数量级。这种效率意味着，大多数能够承受单一证明者证明成本的应用，也应该能够承受协作证明的成本。

## 关键词

+ 协作zk-SNARK分布式证明
+ 多方安全计算MPC友好性
+ 分布式秘密见证联合证明
+ 基于配对的zk-SNARK优化
+ 恶意多数安全证明协议
+ 配对群多标量乘法MPC
