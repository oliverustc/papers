---
title: "Efficient representation of numerical optimization problems for SNARKs"
标题简称:
论文类型: conference
会议简称: USENIX Security
发表年份: 2022
created: 2025-05-23 01:19:22
modified: 2025-05-23 01:20:03
---

## Efficient representation of numerical optimization problems for SNARKs

## 发表信息

+ [原文链接](https://www.usenix.org/conference/usenixsecurity22/presentation/angel)

## 作者

+ Sebastian Angel
+ Andrew J Blumberg
+ Eleftherios Ioannidis
+ Jess Woods

## 笔记

This paper introduces Otti, a general-purpose compiler for (zk)SNARKs that provides support for numerical optimization problems. Otti produces efficient arithmetizations of programs that contain optimization problems including linear programming (LP), semi-definite programming (SDP), and a broad class of stochastic gradient descent (SGD) instances. Numerical optimization is a fundamental algorithmic building block: applications include scheduling and resource allocation tasks, approximations to NP-hard problems, and training of neural networks. Otti takes as input arbitrary programs written in a subset of C that contain optimization problems specified via an easy-to-use API. Otti then automatically produces rank-1 constraint satisfiability (R1CS) instances that express a succinct transformation of those programs. Correct execution of the transformed program implies the optimality of the solution to the original optimization problem. Our evaluation on real benchmarks shows that Otti, instantiated with the Spartan proof system, can prove the optimality of solutions in zero-knowledge in as little as 100 ms—over 4 orders of magnitude faster than existing approaches.

以下是中文翻译：

本文介绍了 Otti，这是一个用于 （zk）SNARK 的通用编译器，可为数值优化问题提供支持。Otti 生成包含优化问题的程序的高效算术化，包括线性规划 （LP）、半定规划 （SDP） 和一大类随机梯度下降 （SGD） 实例。数值优化是一个基本的算法构建块：应用包括调度和资源分配任务、NP-hard 问题的近似值以及神经网络的训练。Otti 将用 C 语言的子集编写的任意程序作为输入，这些程序包含通过易于使用的 API 指定的优化问题。然后，Otti 自动生成 rank-1 约束满足性 （R1CS） 实例，这些实例表示这些程序的简洁转换。正确执行转换后的程序意味着原始优化问题的解决方案的最优性。我们对实际基准的评估表明，使用 Spartan 证明系统实例化的 Otti 可以在短短 100 毫秒内证明零知识解决方案的最优性，比现有方法快 4 个数量级以上。

## 关键词

+ Otti数值优化SNARK编译器
+ 线性规划零知识证明
+ R1CS算术化数值优化
+ 随机梯度下降ZK证明
+ Spartan证明系统应用
+ 优化问题最优性验证
