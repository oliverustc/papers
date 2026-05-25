---
title: "Fiat-Shamir Security of FRI and Related SNARKs"
标题简称:
论文类型: conference
会议简称: ASIACRYPT
发表年份: 2023
modified: 2025-04-10 16:40:26
---

## Fiat-Shamir Security of FRI and Related SNARKs

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-981-99-8724-5_1)

## 作者

+ [Alexander R. Block](Alexander%20R.%20Block.md)
+ Albert Garreta
+ [Jonathan Katz](Jonathan%20Katz.md)
+ [Justin Thaler](Justin%20Thaler.md)
+ Pratyush Ranjan Tiwari
+ Michał Zając

## 笔记

We establish new results on the Fiat-Shamir (FS) security of several protocols that are widely used in practice, and we provide general tools for establishing similar results for others. More precisely, we: (1) prove the FS security of the FRI and batched FRI protocols; (2) analyze a general class of protocols, which we call $\delta$-correlated, that use low-degree proximity testing as a subroutine (this includes many “Plonk-like” protocols (e.g., Plonky2 and Redshift), ethSTARK, RISC Zero, etc.); and (3) prove FS security of the aforementioned “Plonk-like” protocols, and sketch how to prove the same for the others.

We obtain our first result by analyzing the round-by-round (RBR) soundness and RBR knowledge soundness of FRI. For the second result, we prove that if a $\delta$-correlated protocol is RBR (knowledge) sound under the assumption that adversaries always send low-degree polynomials, then it is RBR (knowledge) sound in general. Equipped with this tool, we prove our third result by formally showing that “Plonk-like” protocols are RBR (knowledge) sound under the assumption that adversaries always send low-degree polynomials. We then outline analogous arguments for the remainder of the aforementioned protocols.

To the best of our knowledge, ours is the first formal analysis of the Fiat-Shamir security of FRI and widely deployed protocols that invoke it.

以下是中文翻译：

我们针对几个在实践中广泛使用的协议建立了关于Fiat-Shamir(FS)安全性的新研究成果，并提供了通用工具以便建立类似的结果。具体而言，我们：(1)证明了FRI和批处理FRI协议的FS安全性；(2)分析了一类使用低度逼近性测试作为子程序的通用协议，我们称之为δ-相关协议(这包括许多"类Plonk协议"(如Plonky2和Redshift)、ethSTARK、RISC Zero等)；(3)证明了上述"类Plonk协议"的FS安全性，并概述了如何为其他协议证明相同的性质。

我们通过分析FRI的逐轮(round-by-round, RBR)可靠性和RBR知识可靠性获得了第一个结果。对于第二个结果，我们证明了如果一个δ-相关协议在对手总是发送低度多项式的假设下具有RBR(知识)可靠性，那么它在一般情况下也具有RBR(知识)可靠性。利用这个工具，我们通过正式证明"类Plonk协议"在对手总是发送低度多项式的假设下具有RBR(知识)可靠性，从而证明了第三个结果。随后，我们概述了对上述其余协议的类似论证。

据我们所知，这是首次对FRI及广泛部署的调用它的协议的Fiat-Shamir安全性进行正式分析。

## 关键词

+ FRI协议
+ Fiat-Shamir变换
+ 零知识证明
+ 多项式测试
+ 可靠性证明