---
title: "xJsnark: A Framework for Efficient Verifiable Computation"
标题简称: xJsnark
论文类型: conference
会议简称: S&P
发表年份: 2018
modified: 2025-04-10 16:43:08
---

## xJsnark: A Framework for Efficient Verifiable Computation

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/8418647)

## 作者

+ [Ahmed Kosba](Ahmed%20Kosba.md)
+ [Charalampos Papamanthou](Charalampos%20Papamanthou.md)
+ [Elaine Shi](Elaine%20Shi.md)
## 笔记

Many cloud and cryptocurrency applications rely on verifying the integrity of outsourced computations, in which a verifier can efficiently verify the correctness of a computation made by an untrusted prover. State-of-the-art protocols for verifiable computation require that the computation task be expressed as arithmetic circuits, and the number of multiplication gates in the circuit is the primary metric that determines performance. At the present, a programmer could rely on two approaches for expressing the computation task, either by composing the circuits directly through low-level development tools; or by expressing the computation in a high-level program and rely on compilers to perform the program-to-circuit transformation. The former approach is difficult to use but on the other hand allows an expert programmer to perform custom optimizations that minimize the resulting circuit. In comparison, the latter approach is much more friendly to non-specialist users, but existing compilers often emit suboptimal circuits. We present xJsnark, a programming framework for verifiable computation that aims to achieve the best of both worlds: offering programmability to non-specialist users, and meanwhile automating the task of circuit size minimization through a combination of techniques. Specifically, we present new circuit-friendly algorithms for frequent operations that achieve constant to asymptotic savings over existing ones; various globally aware optimizations for short- and long- integer arithmetic; as well as circuit minimization techniques that allow us to reduce redundant computation over multiple expressions. We illustrate the savings in different applications, and show the framework's applicability in developing large application circuits, such as ZeroCash, while minimizing the circuit size as in low-level implementations.

以下是中文翻译：

许多云计算和加密货币应用依赖于验证外包计算的完整性，其中验证者可以有效地验证不可信证明者所进行计算的正确性。当前最先进的可验证计算协议要求将计算任务表示为算术电路，而电路中的乘法门数量是决定性能的主要指标。目前，程序员可以依靠两种方法来表达计算任务：一种是通过低级开发工具直接构建电路；另一种是通过高层程序表达计算，并依赖编译器进行程序到电路的转换。前一种方法使用起来较为困难，但另一方面允许专家程序员进行自定义优化，从而最小化生成的电路。相比之下，后一种方法对非专业用户更加友好，但现有编译器通常生成次优电路。我们提出了xJsnark，一个可验证计算的编程框架，旨在兼顾两者的优点：为非专业用户提供可编程性，同时通过多种技术的结合自动化电路规模最小化的任务。具体而言，我们提出了新的电路友好算法，用于常见操作，能够在现有方法的基础上实现常数到渐近的节省；针对短整型和长整型算术的各种全局优化；以及电路最小化技术，使我们能够减少多个表达式之间的冗余计算。我们展示了在不同应用中的节省效果，并展示了该框架在开发大型应用电路（如ZeroCash）中的适用性，同时在低级实现中最小化电路规模。

## 关键词

+ 可验证计算框架
+ 算术电路优化
+ 电路规模最小化
+ 非整数算术优化
+ ZK-SNARK编译器
+ xJsnark