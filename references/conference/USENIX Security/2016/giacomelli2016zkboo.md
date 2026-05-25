---
title: "ZKBoo: Faster Zero-Knowledge for Boolean Circuits"
标题简称:
论文类型: conference
会议简称: USENIX Security
发表年份: 2016
modified: 2025-04-08 17:09:34
---

## ZKBoo: Faster Zero-Knowledge for Boolean Circuits

## 发表信息

+ [原文链接](https://www.usenix.org/conference/usenixsecurity16/technical-sessions/presentation/giacomelli)

## 作者

+ Irene Giacomelli
+ Jesper Madsen
+ [Claudio Orlandi](Claudio%20Orlandi.md)
## 笔记

In this paper we describe ZKBoo, a proposal for practically efficient zero-knowledge arguments especially tailored for Boolean circuits and report on a proof-ofconcept implementation. As an highlight, we can generate (resp. verify) a non-interactive proof for the SHA-1 circuit in approximately 13ms (resp. 5ms), with a proof size of 444KB.

Our techniques are based on the “MPC-in-the-head” approach to zero-knowledge of Ishai et al. (IKOS), which has been successfully used to achieve significant asymptotic improvements. Our contributions include:

A thorough analysis of the different variants of IKOS, which highlights their pros and cons for practically relevant soundness parameters;
A generalization and simplification of their approach, which leads to faster ∑-protocols (that can be made non-interactive using the Fiat-Shamir heuristic) for statements of the form “I know x such that y = Ø(x)” (where Ø is a circuit and y a public value);
A case study, where we provide explicit protocols, implementations and benchmarking of zero-knowledge protocols for the SHA-1 and SHA-256 circuits.

以下是中文翻译：

在本文中，我们描述了ZKBoo，一个专门针对布尔电路的实用高效零知识论证（zero-knowledge arguments）提案，并报告了一个概念验证的实现。作为亮点，我们能够在大约13毫秒内生成（或在大约5毫秒内验证）针对SHA-1电路的非交互式证明，证明大小为444KB。

我们的技术基于Ishai等人提出的“头脑中的多方计算”（MPC-in-the-head）零知识方法（IKOS），该方法已成功用于实现显著的渐近改进。我们的贡献包括：

对IKOS不同变体的全面分析，突出了它们在实际相关的健壮性参数下的优缺点；
对其方法的概括和简化，这导致了更快的∑-协议（可以使用Fiat-Shamir启发式方法转化为非交互式）适用于“我知道x使得y = Ø(x)”的语句（其中Ø是一个电路，y是一个公共值）；
一个案例研究，我们提供了SHA-1和SHA-256电路的零知识协议的明确协议、实现和基准测试。

## 关键词

+ ZKBoo布尔电路零知识
+ MPC-in-the-head方法
+ Fiat-Shamir非交互化
+ SHA电路零知识证明
+ Sigma协议优化
+ 实用零知识论证系统
