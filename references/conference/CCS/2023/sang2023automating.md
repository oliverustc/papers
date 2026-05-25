---
title: "Ou: Automating the Parallelization of Zero-Knowledge Protocols"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2023
modified: 2025-04-11 10:23:07
---

## Ou: Automating the Parallelization of Zero-Knowledge Protocols

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3576915.3616621)

## 作者

+ Yuyang Sang
+ [Ning Luo](Ning%20Luo.md)
+ Samuel Judson
+ Ben Chaimberg
+ [Timos Antonopoulos](Timos%20Antonopoulos.md)
+ [Xiao Wang](Xiao%20Wang.md)
+ [Ruzica Piskac](Ruzica%20Piskac.md)
+ Zhong Shao

## 笔记

A zero-knowledge proof (ZKP) is a powerful cryptographic primitive used in many decentralized or privacy-focused applications. However, the high overhead of ZKPs can restrict their practical applicability. We design a programming language, Ou, aimed at easing the programmer's burden when writing efficient ZKPs, and a compiler framework, Lian, that automates the analysis and distribution of statements to a computing cluster. Ou uses programming language semantics, formal methods, and combinatorial optimization to automatically partition an Ou program into efficiently sized chunks for parallel ZK-proving and/or verification. We contribute: (1) A front-end language where users can write proof statements as imperative programs in a familiar syntax; (2) A compiler architecture and implementation that automatically analyzes the program and compiles it into an optimized IR that can be lifted to a variety of ZKP constructions; and (3) A cutting algorithm, based on Pseudo-Boolean optimization and Integer Linear Programming, that reorders instructions and then partitions the program into efficiently sized chunks for parallel evaluation and efficient state reconciliation.

以下是中文翻译：

零知识证明(zero-knowledge proof, ZKP)是一种强大的密码学原语，在许多去中心化或注重隐私的应用中得到广泛使用。然而，ZKP的高开销可能会限制其实际应用。我们设计了一种编程语言Ou，旨在减轻程序员在编写高效ZKP时的负担，并开发了一个编译器框架Lian，用于自动化分析语句并将其分配到计算集群中。Ou利用编程语言语义学、形式化方法和组合优化，自动将Ou程序划分为大小合适的块，以实现并行的零知识证明生成和/或验证。我们的主要贡献包括：(1)一个前端语言，使用者可以用熟悉的语法以命令式程序的形式编写证明语句；(2)一个编译器架构及其实现，能够自动分析程序并将其编译成优化的中间表示(IR)，该表示可以提升到各种ZKP构造中；(3)一种基于伪布尔优化(Pseudo-Boolean optimization)和整数线性规划(Integer Linear Programming)的切分算法，该算法可以重新排序指令，然后将程序划分为大小合适的块，以实现并行评估和高效的状态协调。

## 关键词

+ 零知识证明
+ 编程语言设计
+ 并行化
+ 编译器优化
+ 形式化方法
+ 组合优化