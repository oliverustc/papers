---
title: "HyperNova: Recursive arguments for customizable constraint systems"
标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 2024
created: 2025-04-21 10:35:51
modified: 2025-04-21 10:36:33
---

## HyperNova: Recursive arguments for customizable constraint systems

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-68403-6_11)

## 作者

+ Abhiram Kothapalli 
+ [Srinath Setty](Srinath%20Setty.md) 

## 笔记

We introduce _HyperNova_, a new recursive argument for proving incremental computations whose steps are expressed with CCS (Setty et al. ePrint 2023/552), a customizable constraint system that simultaneously generalizes Plonkish, R1CS, and AIR without overheads. HyperNova makes four contributions, each resolving a major problem in the area of recursive arguments.

First, it provides a folding scheme for CCS where the prover’s cryptographic cost is a _single_ multi-scalar multiplication (MSM) of size equal to the number of variables in the constraint system, which is optimal when using an MSM-based commitment scheme. The folding scheme can fold multiple instances at once, making it easier to build generalizations of IVC such as PCD. Second, when proving program executions on stateful machines (e.g., EVM, RISC-V), the cost of proving a step of a program is proportional only to the size of the circuit representing the instruction invoked by the program step (“a la carte” cost profile). Third, we show how to achieve zero-knowledge for “free” and _without_ the need to employ _zero-knowledge_ SNARKs: we use a folding scheme to “randomize” IVC proofs. This highlights a new application of folding schemes. Fourth, we show how to efficiently instantiate HyperNova over a cycle of elliptic curves. For this, we provide a general technique, which we refer to as CycleFold, that applies to all modern folding-scheme-based recursive arguments.

以下是中文翻译：

我们介绍了HyperNova，这是一种新的递归论证方法，用于证明增量计算，其步骤通过CCS（Setty等，ePrint 2023/552）表示，这是一种可定制的约束系统，能够同时推广Plonkish、R1CS和AIR而没有额外开销。HyperNova做出了四项贡献，每一项都解决了递归论证领域中的一个重大问题。

首先，它为CCS提供了一种折叠方案，其中证明者的加密成本仅为一次多标量乘法（MSM），其大小等于约束系统中变量的数量，这在使用基于MSM的承诺方案时是最优的。该折叠方案可以一次折叠多个实例，使得构建IVC（增量验证计算）等的推广变得更加容易，例如PCD（可组合证明）。其次，在对有状态机器（例如EVM、RISC-V）上的程序执行进行证明时，证明程序一步的成本仅与表示程序步骤所调用指令的电路大小成正比（”单点点餐”成本特征）。第三，我们展示了如何以”免费”的方式实现零知识，而无需使用零知识SNARKs：我们使用折叠方案来”随机化”IVC证明。这突出了折叠方案的新应用。第四，我们展示了如何高效地在椭圆曲线的循环上实例化HyperNova。为此，我们提供了一种通用技术，称为CycleFold，该技术适用于所有基于现代折叠方案的递归论证。

## 关键词

+ 递归论证
+ 可定制约束系统
+ 折叠方案
+ 增量验证计算
+ CycleFold
+ 零知识证明