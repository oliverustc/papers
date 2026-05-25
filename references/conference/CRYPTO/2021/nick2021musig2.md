---
title: "MuSig: Simple two-round Schnorr multi-signatures"

标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 2021
created: 2025-05-27 04:16:39
modified: 2025-05-27 04:17:55
---

## MuSig: Simple two-round Schnorr multi-signatures

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-030-84242-0_8)

## 作者

+ Jonas Nick
+ Tim Ruffing
+ Yannick Seurin

## 笔记

Multi-signatures enable a group of signers to produce a joint signature on a joint message. Recently, Drijvers et al. (S&P'19) showed that all thus far proposed two-round multi-signature schemes in the pure DL setting (without pairings) are insecure under concurrent signing sessions. While Drijvers et al. proposed a secure two-round scheme, this efficiency in terms of rounds comes with the price of having signatures that are more than twice as large as Schnorr signatures, which are becoming popular in cryptographic systems due to their practicality (e.g., they will likely be adopted in Bitcoin). If one needs a multi-signature scheme that can be used as a drop-in replacement for Schnorr signatures, then one is forced to resort either to a three-round scheme or to sequential signing sessions, both of which are undesirable options in practice. In this work, we propose MuSig2, a simple and highly practical two-round multi-signature scheme. This is the first scheme that simultaneously i) is secure under concurrent signing sessions, ii) supports key aggregation, iii) outputs ordinary Schnorr signatures, iv) needs only two communication rounds, and v) has similar signer complexity as ordinary Schnorr signatures. Furthermore, it is the first multi-signature scheme in the pure DL setting that supports preprocessing of all but one rounds, effectively enabling a non-interactive signing process without forgoing security under concurrent sessions. We prove the security of MuSig2 in the random oracle model, and the security of a more efficient variant in the combination of the random oracle and the algebraic group model. Both our proofs rely on a weaker variant of the OMDL assumption.

以下是中文翻译：

多重签名使得一组签名者能够对共同消息生成联合签名。最近，Drijvers 等人（S&P'19）展示了迄今为止提出的所有在纯离散对数（DL）设置下的两轮多重签名方案（不使用配对）在并发签名会话中都是不安全的。虽然Drijvers等人提出了一个安全的两轮方案，但在轮数上的高效性以签名大小为代价，其签名大小超过了Schnorr签名的两倍，而后者因其实用性（例如，它们可能会在比特币中被采用）而在密码系统中变得越来越受欢迎。如果需要一个可以作为Schnorr签名的直接替代的多重签名方案，那么就不得不选择三轮方案或顺序签名会话，这在实践中都是不理想的选择。

在本研究中，我们提出了MuSig2，这是一个简单且高度实用的两轮多重签名方案。这是第一个同时满足以下条件的方案：i) 在并发签名会话下是安全的，ii) 支持密钥聚合，iii) 输出普通的Schnorr签名，iv) 仅需两个通信轮次，以及 v) 具有与普通Schnorr签名相似的签名者复杂性。此外，它是第一个在纯DL设置下支持除一轮之外所有轮次预处理的多重签名方案，有效地实现了非交互式签名过程而不牺牲并发会话下的安全性。我们在随机预言模型中证明了MuSig2的安全性，并在随机预言与代数群模型的结合中证明了一个更高效变体的安全性。我们的证明依赖于OMDL假设的一个较弱变体。

## 关键词

+ MuSig2两轮Schnorr多重签名
+ 并发签名会话密钥聚合安全
+ 非交互式签名预处理支持
+ OMDL假设随机预言代数群模型
+ Bitcoin兼容标准Schnorr输出