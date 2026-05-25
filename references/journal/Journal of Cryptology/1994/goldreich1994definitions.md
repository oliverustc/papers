---
title: "Definitions and properties of zero-knowledge proof systems"
标题简称:
论文类型: journal
期刊简称: Journal of Cryptology
发表年份: 1994
modified: 2025-04-08 18:38:12
---

## Definitions and properties of zero-knowledge proof systems

## 发表信息

+ [原文链接](https://link.springer.com/article/10.1007/BF00195207)

## 作者

+ [Oded Goldreich](Oded%20Goldreich.md)
+ Yair Oren

## 笔记

In this paper we investigate some properties of zero-knowledge proofs, a notion introduced by Goldwasser, Micali, and Rackoff. We introduce and classify two definitions of zero-knowledge: auxiliary-input zero-knowledge and blackbox-simulation zero-knowledge. We explain why auxiliary-input zero-knowledge is a definition more suitable for cryptographic applications than the original [GMR1] definition. In particular, we show that any protocol solely composed of subprotocols which are auxiliary-input zero-knowledge is itself auxiliary-input zero-knowledge. We show that blackbox-simulation zero-knowledge implies auxiliary-input zero-knowledge (which in turn implies the [GMR1] definition). We argue that all known zero-knowledge proofs are in fact blackbox-simulation zero-knowledge (i.e., we proved zero-knowledge using blackbox-simulation of the verifier). As a result, all known zero-knowledge proof systems are shown to be auxiliary-input zero-knowledge and can be used for cryptographic applications such as those in [GMW2].

We demonstrate the triviality of certain classes of zero-knowledge proof systems, in the sense that only languages in BPP have zero-knowledge proofs of these classes. In particular, we show that any language having a Las Vegas zero-knowledge proof system necessarily belongs to RP. We show that randomness of both the verifier and the prover, and nontriviality of the interaction are essential properties of (nontrivial) auxiliary-input zero-knowledge proofs.

以下是中文翻译：

本文研究了由Goldwasser、Micali和Rackoff引入的零知识证明(zero-knowledge proofs)的一些性质。我们引入并分类了零知识的两个定义：辅助输入零知识(auxiliary-input zero-knowledge)和黑盒模拟零知识(blackbox-simulation zero-knowledge)。我们解释了为什么辅助输入零知识比原始的[GMR1]定义更适合密码学应用。特别地，我们证明了仅由辅助输入零知识子协议组成的任何协议本身也是辅助输入零知识的。我们证明了黑盒模拟零知识蕴含辅助输入零知识（而后者又蕴含[GMR1]定义）。我们论证了所有已知的零知识证明实际上都是黑盒模拟零知识的（即，我们使用验证者的黑盒模拟来证明零知识性质）。因此，所有已知的零知识证明系统都被证明是辅助输入零知识的，可以用于[GMW2]中的密码学应用。

我们证明了某些类别的零知识证明系统的平凡性，即只有BPP中的语言才具有这些类别的零知识证明。特别地，我们证明了任何具有拉斯维加斯零知识(Las Vegas zero-knowledge)证明系统的语言必然属于RP。我们证明了验证者和证明者的随机性，以及交互的非平凡性是（非平凡的）辅助输入零知识证明的基本性质。

## 关键词

+ 零知识证明安全性定义
+ 辅助输入零知识
+ 黑盒模拟零知识
+ 密码学协议组合安全
+ 零知识平凡性分类
+ 交互证明系统基础