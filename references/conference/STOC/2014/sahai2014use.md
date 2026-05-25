---
title: "How to use indistinguishability obfuscation: deniable encryption, and more"
标题简称:
论文类型: conference
会议简称: STOC
发表年份: 2014
created: 2025-04-29 10:26:41
modified: 2025-04-29 10:27:09
---

## How to use indistinguishability obfuscation: deniable encryption, and more

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/2591796.2591825)

## 作者

+ [Amit Sahai](Amit%20Sahai.md)
+ [Brent Waters](Brent%20Waters.md)
## 笔记

We introduce a new technique, that we call _punctured programs_, to apply indistinguishability obfuscation towards cryptographic problems. We use this technique to carry out a systematic study of the applicability of indistinguishability obfuscation to a variety of cryptographic goals. Along the way, we resolve the 16-year-old open question of _Deniable Encryption_, posed by Canetti, Dwork, Naor, and Ostrovsky in 1997: In deniable encryption, a sender who is forced to reveal to an adversary both her message and the randomness she used for encrypting it should be able to convincingly provide "fake" randomness that can explain any alternative message that she would like to pretend that she sent. We resolve this question by giving the first construction of deniable encryption that _does not require any pre-planning_ by the party that must later issue a denial.

In addition, we show the generality of our punctured programs technique by also constructing a variety of core cryptographic objects from indistinguishability obfuscation and one-way functions (or close variants). In particular we obtain: public key encryption, short "hash-and-sign" selectively secure signatures, chosen-ciphertext secure public key encryption, non-interactive zero knowledge proofs (NIZKs), injective trapdoor functions, and oblivious transfer. These results suggest the possibility of indistinguishability obfuscation becoming a "central hub" for cryptography.

以下是中文翻译：

我们引入了一种名为"打孔程序"（punctured programs）的新技术，将不可区分性混淆（indistinguishability obfuscation）应用于密码学问题。我们使用该技术对不可区分性混淆在各种密码学目标中的适用性进行了系统研究。在此过程中，我们解决了Canetti、Dwork、Naor和Ostrovsky于1997年提出的16年未解的公开问题——可否认加密（Deniable Encryption）：在可否认加密中，被迫向对手同时披露其消息和加密所用随机数的发送方，应能令人信服地提供"伪造"随机数，以解释她所希望伪装发送的任何替代消息。我们通过给出首个不需要必须后来发出否认的一方进行任何预规划的可否认加密构造，解决了这一问题。

此外，我们还通过从不可区分性混淆和单向函数（或其接近变体）构造各种核心密码学对象，展示了打孔程序技术的普遍适用性。特别是，我们获得了：公钥加密、简短的"哈希与签名"选择性安全签名、抗选择密文的公钥加密、非交互式零知识证明（NIZKs）、单射陷门函数和不经意传输。这些结果表明，不可区分性混淡有可能成为密码学的"中央枢纽"。

## 关键词

+ 不可区分性混淆iO
+ 打孔程序技术
+ 可否认加密
+ 非交互式零知识证明NIZK
+ 核心密码学原语构建
+ 单向函数密码应用

