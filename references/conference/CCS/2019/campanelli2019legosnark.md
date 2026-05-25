---
title: "LegoSNARK: Modular design and composition of succinct zero-knowledge proofs"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2019
modified: 2025-04-23 08:51:23
created: 2025-04-11 11:37:24
---

## LegoSNARK: Modular design and composition of succinct zero-knowledge proofs

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3319535.3339820)

## 作者

+ [Matteo Campanelli](Matteo%20Campanelli.md)
+ [Dario Fiore](Dario%20Fiore.md)
+ Anais Querol 

## 笔记

We study the problem of building non-interactive proof systems modularly by linking small specialized "gadget" SNARKs in a lightweight manner. Our motivation is both theoretical and practical. On the theoretical side, modular SNARK designs would be flexible and reusable. In practice, specialized SNARKs have the potential to be more efficient than general-purpose schemes. If a computation naturally presents different "components", a modular approach allows exploiting the nuances of a computation and choosing the best gadget for each component. Our contribution is LegoSNARK, a "toolbox" for commit-and-prove zkSNARKs that includes composition tools, lifting compilers, and succinct proof gadgets. We obtain new succinct proof systems: LegoGro16 (a commit-and-prove version of Groth16), LegoUAC (a pairing-based SNARK with universal CRS), and LegoMM (a CP-SNARK for matrix multiplication with optimal proving complexity).

以下是中文翻译：

我们研究通过以轻量级方式链接小型专门化"小工具"SNARKs来模块化构建非交互式证明系统的问题。在理论方面，模块化SNARK设计将是灵活且可重用的。在实践中，专门化SNARKs相比通用方案具有更高的效率潜力。如果计算自然地呈现不同的"组件"，模块化方法允许利用计算的细微差别并为每个组件选择最佳的小工具。我们的贡献是LegoSNARK，一个承诺-证明零知识简洁非交互式知识论证的"工具箱"，包括组合工具、提升编译器和简洁证明小工具。我们获得了新的简洁证明系统：LegoGro16（Groth16的承诺-证明版本）、LegoUAC（具有通用CRS的基于配对的SNARK）和LegoMM（矩阵乘法的CP-SNARK，具有最优证明复杂度）。

## 关键词

+ LegoSNARK
+ 模块化设计
+ 承诺-证明
+ 简洁论证
+ 零知识证明

