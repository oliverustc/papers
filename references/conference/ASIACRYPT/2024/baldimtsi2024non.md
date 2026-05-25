---
title: "Non-Interactive Blind Signatures: Post-Quantum and Stronger Security"
标题简称:
论文类型: conference
会议简称: ASIACRYPT
发表年份: 2024
created: 2025-05-09 09:38:33
modified: 2025-05-09 09:47:30
---

## Non-Interactive Blind Signatures: Post-Quantum and Stronger Security

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-981-96-0888-1_3)
+ [archive](https://eprint.iacr.org/2024/614)

## 作者

+ [Foteini Baldimtsi](Foteini%20Baldimtsi.md)
+ Jiaqi Cheng
+ Rishab Goyal
+ Aayush Yadav

## 笔记

Blind signatures enable a receiver to obtain signatures on messages of its choice without revealing any message to the signer. Round-optimal blind signatures are designed as a two-round interactive protocol between a signer and receiver. Incidentally, the choice of message is not important in many applications, and is routinely set as a random (unstructured) message by a receiver. With the goal of designing more efficient blind signatures for such applications, Hanzlik (Eurocrypt '23) introduced a new variant called non-interactive blind signatures (NIBS). These allow a signer to asynchronously generate partial signatures for any recipient such that only the intended recipient can extract a blinded signature for a random message. This bypasses the two-round barrier for traditional blind signatures, yet enables many known applications. Hanzlik provided new practical designs for NIBS from bilinear pairings. In this work, we propose new enhanced security properties for NIBS as well as provide multiple constructions with varying levels of security and concrete efficiency. We propose a new generic paradigm for NIBS from circuit-private leveled homomorphic encryption achieving optimal-sized signatures (i.e., same as any non-blind signature) at the cost of large public keys. We also investigate concretely efficient NIBS with post-quantum security, satisfying weaker level of privacy as proposed by Hanzlik.

以下是中文翻译：

盲签名使接收方能够获得其选择的消息的签名，而无需向签名者透露任何消息内容。轮次最优的盲签名被设计为签名者和接收者之间的两轮交互协议。实际上，在许多应用中消息的选择并不重要，接收方通常会将其设置为随机（无结构）消息。

为了针对此类应用设计更高效的盲签名，Hanzlik（Eurocrypt '23）引入了一种新的变体，称为非交互式盲签名（NIBS）。这种方式允许签名者异步地为任何接收者生成部分签名，使得只有预期的接收者能够为随机消息提取出盲化签名。这突破了传统盲签名的两轮限制，同时支持许多已知的应用。Hanzlik基于双线性配对提供了NIBS的新的实用设计方案。

在本研究中，我们为NIBS提出了新的增强安全性特性，并提供了多个具有不同安全级别和具体效率的构造方案。我们提出了一个基于电路私有分层同态加密（circuit-private leveled homomorphic encryption）的NIBS新通用范式，该方案实现了最优大小的签名（即与非盲签名相同），但代价是较大的公钥。我们还研究了具有后量子安全性的具体高效NIBS方案，满足Hanzlik提出的较弱隐私级别。

## 关键词

+ 非交互式盲签名
+ 后量子密码学
+ 同态加密
+ 隐私保护
+ 数字签名