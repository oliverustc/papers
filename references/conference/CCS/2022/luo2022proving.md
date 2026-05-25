---
title: "Proving UNSAT in Zero Knowledge"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2022
modified: 2025-04-09 14:08:55
---

## Proving UNSAT in Zero Knowledge

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3548606.3559373)

## 作者

+ [Ning Luo](Ning%20Luo.md)
+ [Timos Antonopoulos](Timos%20Antonopoulos.md)
+ William R. Harris
+ [Ruzica Piskac](Ruzica%20Piskac.md)
+ [Eran Tromer](Eran%20Tromer.md)
+ [Xiao Wang](Xiao%20Wang.md)

## 笔记

Zero-knowledge (ZK) protocols enable one party to prove to others that it knows a fact without revealing any information about the evidence for such knowledge. There exist ZK protocols for all problems in NP, and recent works developed highly efficient protocols for proving knowledge of satisfying assignments to Boolean formulas, circuits and other NP formalisms. This work shows an efficient protocol for the converse: proving formula unsatisfiability in ZK (when the prover posses a non-ZK proof). An immediate practical application is efficiently proving safety of secret programs.
The key insight is to prove, in ZK, the validity of resolution proofs of unsatisfiability. This is efficiently realized using an algebraic representation that exploits resolution proofs' structure to represent formula clauses as low-degree polynomials, combined with ZK random-access arguments. Only the proof's dimensions are revealed.
We implemented our protocol and used it to prove unsatisfiability of formulas that encode combinatoric problems and program correctness conditions in standard verification benchmarks, including Linux kernel drivers and Intel cryptography modules. The results demonstrate both that our protocol has practical utility, and that its aggressive optimizations, based on non-trivial encodings, significantly improve practical performance.

以下是中文翻译：

零知识(Zero-knowledge, ZK)协议使一方能够向其他方证明其知道某个事实，而无需透露关于该知识证据的任何信息。目前已有适用于所有NP问题的零知识协议，近期研究还开发出了高效的协议，用于证明布尔公式、电路和其他NP形式化表达的可满足性赋值知识。本研究提出了一个针对相反情况的高效协议：在零知识条件下证明公式不可满足性（当证明者拥有非零知识证明时）。一个直接的实际应用是高效地证明秘密程序的安全性。

关键思路是在零知识条件下证明不可满足性的归结证明(resolution proof)的有效性。这通过代数表示方法得以高效实现，该方法利用归结证明的结构将公式子句表示为低次多项式，并结合零知识随机访问论证(ZK random-access arguments)。只有证明的维度会被揭示。

我们实现了该协议，并用它来证明编码组合问题和程序正确性条件的公式的不可满足性，这些公式来自标准验证基准测试，包括Linux内核驱动程序和Intel密码学模块。结果表明，我们的协议具有实际应用价值，且基于非平凡编码的积极优化显著改善了实际性能。

## 关键词

+ 零知识证明
+ 不可满足性
+ 归结证明
+ 程序验证
+ 密码学