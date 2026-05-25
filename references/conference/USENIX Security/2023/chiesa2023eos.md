---
title: "Eos: Efficient private delegation of zkSNARK provers"
标题简称:
论文类型: conference
会议简称: USENIX Security
发表年份: 2023
created: 2025-04-21 08:41:52
modified: 2025-04-21 08:42:37
---

## Eos: Efficient private delegation of zkSNARK provers

## 发表信息

+ [原文链接](https://www.usenix.org/conference/usenixsecurity23/presentation/chiesa)

## 作者

+ [Alessandro Chiesa](Alessandro%20Chiesa.md)
+ Ryan Lehmkuhl 
+ [Pratyush Mishra](Pratyush%20Mishra.md)
+ [Yinuo Zhang](Yinuo%20Zhang.md)
## 笔记

Succinct zero knowledge proofs (i.e. zkSNARKs) are powerful cryptographic tools that enable a prover to convince a verifier that a given statement is true without revealing any additional information. Their attractive privacy properties have led to much academic and industrial interest.

Unfortunately, existing systems for generating zkSNARKs are expensive, which limits the applications in which these proofs can be used. One approach is to take advantage of powerful cloud servers to generate the proof. However, existing techniques for this (e.g., DIZK) sacrifice privacy by revealing secret information to the cloud machines. This is problematic for many applications of zkSNARKs, such as decentralized private currency and computation systems.

In this work we design and implement _privacy-preserving delegation protocols_ for zkSNARKs with universal setup. Our protocols enable a prover to outsource proof generation to a set of workers, so that if at least one worker does not collude with other workers, _no private information_ is revealed to _any_ worker. Our protocols achieve security against malicious workers without relying on heavyweight cryptographic tools.

We implement and evaluate our delegation protocols for a state-of-the-art zkSNARK in a variety of computational and bandwidth settings, and demonstrate that our protocols are concretely efficient. When compared to local proving, using our protocols to delegate proof generation from a recent smartphone (a) reduces end-to-end latency by up to 26×, (b) lowers the delegator's active computation time by up to 1447×, and (c) enables proving up to 256× larger instances.

以下是中文翻译：

简洁零知识证明（即 zkSNARKs）是强大的加密工具，使得证明者能够在不透露任何额外信息的情况下，向验证者证明某一给定陈述的真实性。其吸引人的隐私特性引起了学术界和工业界的广泛关注。

不幸的是，现有的 zkSNARKs 生成系统成本高昂，这限制了这些证明的应用范围。一种方法是利用强大的云服务器来生成证明。然而，现有的相关技术（例如 DIZK）通过向云计算机泄露秘密信息而牺牲了隐私。这对许多 zkSNARKs 的应用场景，例如去中心化的私人货币和计算系统，构成了问题。

在本工作中，我们设计并实现了具有通用设置的隐私保护委托协议，用于 zkSNARKs。我们的协议使证明者能够将证明生成外包给一组工作者，从而确保如果至少有一个工作者不与其他工作者合谋，则不会向任何工作者泄露私密信息。我们的协议在不依赖于重量级加密工具的情况下，能够抵御恶意工作者的攻击。

我们针对一种最先进的 zkSNARK 实现并评估了我们的委托协议，涵盖了多种计算和带宽设置，结果表明我们的协议在具体实现上是高效的。与本地证明相比，使用我们的协议从一部近期智能手机委托生成证明可以（a）将端到端延迟减少最多 26 倍，（b）将委托者的主动计算时间降低最多 1447 倍，以及（c）支持证明高达 256 倍更大实例的能力。

## 关键词

+ Eos隐私保护zkSNARK委托
+ 证明生成外包云计算
+ 多工作者联合证明生成
+ 抗合谋隐私保护协议
+ 通用设置zkSNARK优化
+ 移动设备证明委托
