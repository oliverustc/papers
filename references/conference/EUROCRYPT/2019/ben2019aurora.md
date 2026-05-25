---
title: "Aurora: Transparent Succinct Arguments for R1CS"
标题简称: Aurora
论文类型: conference
会议简称: EUROCRYPT
发表年份: 2019
modified: 2025-04-08 18:43:18
---

## Aurora: Transparent Succinct Arguments for R1CS

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-030-17653-2_4)

## 作者

+ Eli Ben-Sasson
+ [Alessandro Chiesa](Alessandro%20Chiesa.md)
+ Michael Riabzev
+ Nicholas Spooner
+ Madars Virza
+ Nicholas P. Ward

## 笔记

We design, implement, and evaluate a zero knowledge succinct non-interactive argument (SNARG) for Rank-1 Constraint Satisfaction (R1CS), a widely-deployed NP language undergoing standardization. Our SNARG has a transparent setup, is plausibly post-quantum secure, and uses lightweight cryptography. A proof attesting to the satisfiability of n constraints has size $O(\log^2 n)$; it can be produced with $O(n\log n)$ field operations and verified with $O(n)$. At 128 bits of security, proofs are less than 250KB even for several million constraints, more than $10 \times$ shorter than prior SNARGs with similar features.

A key ingredient of our construction is a new Interactive Oracle Proof (IOP) for solving a univariate analogue of the classical sumcheck problem [LFKN92], originally studied for multivariate polynomials. Our protocol verifies the sum of entries of a Reed–Solomon codeword over any subgroup of a field.

We also provide $\mathsf{libiop}$, a library for writing IOP-based arguments, in which a toolchain of transformations enables programmers to write new arguments by writing simple IOP sub-components. We have used this library to specify our construction and prior ones, and plan to open-source it.

以下是中文翻译：

我们设计、实现并评估了一种针对Rank-1约束满足问题（Rank-1 Constraint Satisfaction, R1CS）的零知识简洁非交互式论证（SNARG），该问题是一种广泛应用的NP语言，正在进行标准化。我们的SNARG具有透明的设置，具有合理的后量子安全性，并采用轻量级密码学。证明一个满足n个约束的可满足性，其大小为 $O(\log^2 n)$ ；该证明可以通过 $O(n\log n)$ 次域运算生成，并且可以通过 $O(n)$ 进行验证。在128位安全性下，即使对于数百万个约束，证明的大小也不到250KB，比之前具有类似特征的SNARG短了超过 $10 \times$。

我们构造的一个关键组成部分是一个新的交互式Oracle证明（Interactive Oracle Proof, IOP），用于解决经典求和检查问题的单变量类比[LFKN92]，该问题最初是针对多变量多项式进行研究的。我们的协议验证了Reed-Solomon码字在任意域的子群上的条目之和。

我们还提供了$\mathsf{libiop}$，这是一个用于编写基于IOP的论证的库，其中的工具链转换使程序员能够通过编写简单的IOP子组件来编写新的论证。我们已经使用该库来指定我们的构造和之前的构造，并计划将其开源。

## 关键词

+ 透明SNARG
+ R1CS约束系统
+ 交互式预言证明
+ 里德-所罗门码
+ 后量子安全