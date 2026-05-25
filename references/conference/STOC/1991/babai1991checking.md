---
title: "Checking computations in polylogarithmic time"
标题简称:
论文类型: conference
会议简称: STOC
发表年份: 1991
modified: 2025-04-08 11:55:33
---

## Checking computations in polylogarithmic time

## 发表信息

+ [原文链接](https://dl.acm.org/doi/10.1145/103418.103428)


## 作者

+ László Babai
+ Lance Fortnow
+ Leonid A. Levin
+ Mario Szegedy

## 笔记

We present efficient methods for checking the correctness of polynomial-time computations in polylogarithmic time. Our verifier uses a polylogarithmic number of random bits and queries, reading only a bounded number of bits from a proof oracle, to verify an entire polynomial-time computation with high probability. The key technical ingredients include low-degree polynomial testing and algebraic encoding of computations, which enable sub-polynomial verification. This work establishes fundamental connections between multi-prover interactive proofs (MIP) and probabilistically checkable proofs (PCP), and served as a precursor to the celebrated PCP theorem. The techniques introduced here yield transparent, succinct proof systems whose verification complexity is far below the complexity of the original computation.

以下是中文翻译：

我们提出了在多对数时间内检验多项式时间计算正确性的高效方法。验证者仅使用多对数数量级的随机比特和查询，从证明预言机中读取有界数量的比特，就能以高概率验证整个多项式时间的计算。核心技术要素包括低度多项式测试和计算的代数编码，从而实现次多项式级别的验证。本文建立了多证明者交互证明（MIP）与概率可检验证明（PCP）之间的基本联系，并成为著名PCP定理的前驱工作。本文引入的技术产生了透明、简洁的证明系统，其验证复杂度远低于原始计算的复杂度。

## 关键词

+ 概率可检验证明PCP
+ 多项式时间计算验证
+ 低度多项式测试
+ 多证明者交互证明MIP
+ 简洁证明系统
+ 代数编码计算