---
title: "Accountable-subgroup multisignatures"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2001
created: 2025-05-27 04:13:38
modified: 2025-05-27 04:13:44
---

## Accountable-subgroup multisignatures

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/501983.502017)

## 作者

+ [Silvio Micali](Silvio%20Micali.md)
+ Kazuo Ohta
+ Leonid Reyzin

## 笔记

Formal models and security proofs are especially important for multisignatures: in contrast to threshold signatures, no precise definitions were ever provided for such schemes, and some proposals were subsequently broken.In this paper, we formalize and implement a variant of multi-signature schemes, Accountable-Subgroup Multisignatures (ASM). In essence, ASM schemes enable any subgroup, S, of a given group, G, of potential signers, to sign efficiently a message M so that the signature provably reveals the identities of the signers in S to any verifier.Specifically, we provide:
The first formal model of security for multisignature schemes that explicitly includes key generation (without relying on trusted third parties);
A protocol, based on Schnorr's signature scheme [33], that is both provable and efficient:
Only three rounds of communication are required per signature.
The signing time per signer is the same as for the single-signer Schnorr scheme, regardless of the number of signers.
The verification time is only slightly greater than that for the single-signer Schnorr scheme.
The signature length is the same as for the single signer Schnorr scheme, regardless of the number of signers.
Our proof of security relies on random oracles and the hardness of the Discrete Log Problem.

以下是中文翻译：

正式模型和安全性证明对于多重签名尤其重要：与门限签名不同，此类方案从未提供过精确的定义，并且一些提议随后被攻破。在本文中，我们形式化并实现了一种多重签名方案的变体，即可追溯子群多重签名（Accountable-Subgroup Multisignatures, ASM）。本质上，ASM 方案使得任何潜在签名者组 G 的子组 S 能够高效地对消息 M 进行签名，从而使得签名能够证明性地向任何验证者揭示子组 S 中签名者的身份。具体而言，我们提供：

- 第一个明确包含密钥生成（不依赖于可信第三方）的多重签名方案安全性正式模型；
- 一种基于 Schnorr 签名方案 [33] 的协议，该协议既可证明又高效：
  - 每个签名仅需三轮通信。
  - 每个签名者的签名时间与单签名者的 Schnorr 方案相同，无论签名者数量如何。
  - 验证时间仅略大于单签名者的 Schnorr 方案。
  - 签名长度与单签名者的 Schnorr 方案相同，无论签名者数量如何。

我们的安全性证明依赖于随机预言机和离散对数问题的困难性。

## 关键词

+ 多重签名
+ 子群签名
+ 数字签名
+ 可追溯性
+ 可证明安全