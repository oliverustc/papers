---
title: "Lova: lattice-based folding scheme from unstructured lattices"
标题简称: 
论文类型: conference
会议简称: ASIACRYPT
发表年份: 2024
created: 2025-04-21 11:06:02
modified: 2025-04-21 11:07:59
---

## Lova: lattice-based folding scheme from unstructured lattices

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-981-96-0894-2_10)

## 作者

+ Giacomo Fenzi 
+ Christian Knabenhans 
+ Ngoc Khanh Nguyen 
+ Duc Tu Pham 

## 笔记

Folding schemes (Kothapalli et al., CRYPTO 2022) are a conceptually simple, yet powerful cryptographic primitive that can be used as a building block to realise incrementally verifiable computation (IVC) with low recursive overhead without general-purpose non-interactive succinct arguments of knowledge (SNARK). Most folding schemes known rely on the hardness of the discrete logarithm problem, and thus are both not quantum-resistant and operate over large prime fields. Existing post-quantum folding schemes (Boneh, Chen, ePrint 2024/257) based on lattice assumptions instead are secure under structured lattice assumptions, such as the Module Short Integer Solution Assumption (MSIS), which also binds them to relatively complex arithmetic. In contrast, we construct Lova, the first folding scheme whose security relies on the (unstructured) SIS assumption. We provide a Rust implementation of Lova, which makes only use of arithmetic in hardware-friendly power-of-two moduli. Crucially, this avoids the need of implementing and performing any finite field arithmetic. At the core of our results lies a new _exact_ Euclidean norm proof which might be of independent interest.

以下是中文翻译：

折叠方案（Folding schemes）（Kothapalli et al., CRYPTO 2022）是一种概念上简单但功能强大的密码学原语，可以作为实现增量可验证计算（incrementally verifiable computation, IVC）的构建块，且具有低递归开销，而无需通用非交互式简洁知识证明（non-interactive succinct arguments of knowledge, SNARK）。已知的大多数折叠方案依赖于离散对数问题的困难性，因此既不具备抗量子能力，又只能在大素数域上操作。现有的基于格假设的后量子折叠方案（Boneh, Chen, ePrint 2024/257）在结构化格假设下是安全的，例如模块短整数解假设（Module Short Integer Solution Assumption, MSIS），这也使得它们的算术操作相对复杂。相比之下，我们构造了Lova，这是第一个安全性依赖于（非结构化）SIS假设的折叠方案。我们提供了Lova的Rust实现，该实现仅使用硬件友好的二次幂模数中的算术运算。关键是，这避免了实现和执行任何有限域算术的需要。我们结果的核心是一个新的精确欧几里得范数证明，这可能具有独立的研究价值。

## 关键词

+ 折叠方案
+ 格密码学
+ 后量子安全
+ 增量可验证计算
+ SIS假设

+ 折叠方案
+ 格密码学
+ 后量子安全
+ 增量可验证计算
+ SIS假设