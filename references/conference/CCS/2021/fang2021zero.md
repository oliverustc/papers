---
title: "Zero knowledge static program analysis"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2021
created: 2025-04-22 11:22:30
modified: 2025-04-22 11:23:22
---

## Zero knowledge static program analysis

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3460120.3484795)

## 作者

+ [Zhiyong Fang](Zhiyong%20Fang.md)
+ David Darais 
+ Joseph P Near 
+ [Yupeng Zhang](Yupeng%20Zhang.md) 

## 笔记

Static program analysis tools can automatically prove many useful properties of programs. However, using static analysis to prove to a third party that a program satisfies a property requires revealing the program's source code. We introduce the concept of zero-knowledge static analysis, in which the prover constructs a zero-knowledge proof about the outcome of the static analysis without revealing the program. We present novel zero-knowledge proof schemes for intra- and inter-procedural abstract interpretation. Our schemes are significantly more efficient than the naive translation of the corresponding static analysis algorithms using existing schemes. We evaluate our approach empirically on real and synthetic programs; with a pairing-based zero knowledge proof scheme as the backend, we are able to prove the control flow analysis on a 2,000-line program in 1,738s. The proof is only 128 bytes and the verification time is 1.4ms. With a transparent zero knowledge proof scheme based on discrete-log, we generate the proof for the tainting analysis on a 12,800-line program in 406 seconds, the proof size is 282 kilobytes, and the verification time is 66 seconds.

以下是中文翻译：

静态程序分析工具可以自动证明程序的许多有用属性。然而，使用静态分析向第三方证明程序满足某个属性时，需要披露程序的源代码。我们引入了零知识静态分析(zero-knowledge static analysis)的概念，在这种分析中，证明者可以构建关于静态分析结果的零知识证明，而无需披露程序本身。我们为过程内和过程间抽象解释(intra- and inter-procedural abstract interpretation)提出了新颖的零知识证明方案。与使用现有方案对相应静态分析算法进行简单转换相比，我们的方案效率显著提高。我们在真实和合成程序上对我们的方法进行了实证评估；使用基于配对(pairing-based)的零知识证明方案作为后端，我们能够在1,738秒内完成对一个2,000行程序的控制流分析证明。该证明仅128字节，验证时间为1.4毫秒。使用基于离散对数(discrete-log)的透明零知识证明方案，我们在406秒内生成了对一个12,800行程序的污点分析(tainting analysis)证明，证明大小为282千字节，验证时间为66秒。

## 关键词

+ 零知识证明
+ 程序分析
+ 静态分析
+ 抽象解释
+ 隐私保护