---
title: "Succinct non-interactive arguments via linear interactive proofs"
标题简称:
论文类型: journal
期刊简称: Journal of Cryptology
发表年份: 2022
created: 2025-04-29 10:28:03
modified: 2025-04-29 10:30:11
---

## Succinct non-interactive arguments via linear interactive proofs

## 发表信息

+ [原文链接](https://link.springer.com/article/10.1007/s00145-022-09424-4)

## 作者

+ Nir Bitansky 
+ [Alessandro Chiesa](Alessandro%20Chiesa.md)
+ [Yuval Ishai](Yuval%20Ishai.md)
+ Rafail Ostrovsky 
+ Omer Paneth 

## 笔记

_Succinct non-interactive arguments_ (SNARGs) enable verifying NP statements with lower complexity than required for classical NP verification. Traditionally, the focus has been on minimizing the length of such arguments; nowadays, researchers have focused also on minimizing verification time, by drawing motivation from the problem of delegating computation. A common relaxation is a _preprocessing_ SNARG, which allows the verifier to conduct an expensive offline phase that is independent of the statement to be proven later. Recent constructions of preprocessing SNARGs have achieved attractive features: they are publicly-verifiable, proofs consist of only _O_(1) encrypted (or encoded) field elements, and verification is via arithmetic circuits of size linear in the NP statement. Additionally, these constructions seem to have “escaped the hegemony” of probabilistically-checkable proofs (PCPs) as a basic building block of succinct arguments. We present a general methodology for the construction of preprocessing s, as well as resulting new efficiency features. Our contribution is threefold:

**(1)**: We introduce and study a natural extension of the interactive proof model that considers _algebraically-bounded_ provers; this new setting is analogous to the common study of algebraically-bounded “adversaries” in other fields, such as pseudorandomness and randomness extraction. More concretely, in this work we focus on linear (or affine) provers, and provide several constructions of (succinct two-message) _linear interactive proofs_ (LIPs) for NP. Our constructions are based on general transformations applied to both _linear_ PCPs (LPCPs) and traditional “unstructured” PCPs.

**(2)**: We give conceptually simple cryptographic transformations from LIPs to preprocessing SNARGs, whose security can be based on different forms of _linear targeted malleability_ (implied by previous knowledge assumptions). Our transformations convert arbitrary (two-message) LIPs into designated-verifier SNARGs, and LIPs with degree-bounded verifiers into publicly-verifiable SNARGs. We also extend our methodology to obtain _zero-knowledge_ LIPs and SNARGs. Our techniques yield SNARGs _of knowledge_ and thus can benefit from known recursive composition and bootstrapping techniques.

**(3)**: Following this methodology, we exhibit several constructions achieving new efficiency features, such as “single-ciphertext preprocessing SNARGs.” We also offer a new perspective on existing constructions of preprocessing SNARGs, revealing a direct connection of these to LPCPs and LIPs.

以下是中文翻译：

简洁非交互式论证(SNARGs)能够以低于经典NP验证所需的复杂度来验证NP陈述。传统上，研究重点在于最小化此类论证的长度；如今，研究人员也开始关注最小化验证时间，这源于计算委托问题的动机。一个常见的放宽条件是预处理SNARG，它允许验证者进行一个与后续待证明陈述无关的昂贵离线阶段。最近的预处理SNARG构造已经实现了一些吸引人的特性：它们是可公开验证的，证明仅包含O(1)个加密（或编码）的域元素，且验证通过规模与NP陈述呈线性关系的算术电路进行。此外，这些构造似乎已经"摆脱了"概率可检验证明(PCPs)作为简洁论证基本构建模块的"统治"。我们提出了一种构造预处理SNARG的通用方法，以及由此产生的新效率特性。我们的贡献包括三个方面：

**(1)**：我们引入并研究了交互式证明模型的一个自然扩展，该模型考虑代数有界证明者(algebraically-bounded provers)；这种新设定类似于其他领域中对代数有界"对手"的常见研究，如伪随机性和随机性提取。具体而言，本文主要关注线性（或仿射）证明者，并为NP提供了几种（简洁的双消息）线性交互式证明(LIPs)的构造。我们的构造基于应用于线性PCP(LPCPs)和传统"非结构化"PCP的通用转换。

**(2)**：我们提供了从LIP到预处理SNARG的概念简单的密码学转换，其安全性可以基于不同形式的线性目标可延展性(linear targeted malleability)（由先前的知识假设所暗示）。我们的转换将任意（双消息）LIP转换为指定验证者SNARG，并将具有度界验证者的LIP转换为可公开验证的SNARG。我们还扩展了我们的方法以获得零知识LIP和SNARG。我们的技术产生知识SNARG，因此可以受益于已知的递归组合和自举技术。

**(3)**：遵循这种方法，我们展示了几种实现新效率特性的构造，如"单密文预处理SNARG"。我们还对现有预处理SNARG构造提供了新的视角，揭示了它们与LPCP和LIP之间的直接联系。

## 关键词

+ 简洁非交互式论证SNARG
+ 线性交互式证明LIP
+ 预处理SNARG构造方法
+ 线性PCP代数有界证明者
+ 线性目标可延展性安全假设
+ 知识SNARG递归组合