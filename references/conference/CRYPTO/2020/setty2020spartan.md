---
title: "Spartan: Efficient and general-purpose zkSNARKs without trusted setup"

标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 2020
modified: 2025-04-11 14:43:37
---

## Spartan: Efficient and general-purpose zkSNARKs without trusted setup

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-030-56877-1_25)

## 作者

+ [Srinath Setty](Srinath%20Setty.md)

## 笔记

This paper introduces Spartan, a new family of zeroknowledge succinct non-interactive arguments of knowledge (zkSNARKs) for the rank-1 constraint satisfiability (R1CS), an NP-complete language that generalizes arithmetic circuit satisfiability. A distinctive feature of Spartan is that it offers the first zkSNARKs without trusted setup (i.e., transparent zkSNARKs) for NP where verifying a proof incurs sub-linear costs—without requiring uniformity in the NP statement’s structure. Furthermore, Spartan offers zkSNARKs with a time-optimal prover, a property that has remained elusive for nearly all zkSNARKs in the literature. To achieve these results, we introduce new techniques that we compose with the sum-check protocol, a seminal interactive proof protocol: (1) computation commitments, a primitive to create a succinct commitment to a description of a computation; this technique is crucial for a verifier to achieve sub-linear costs after investing a one-time, public computation to preprocess a given NP statement; (2) spark, a cryptographic compiler to transform any existing extractable polynomial commitment scheme for multilinear polynomials to one that efficiently handles sparse multilinear polynomials; this technique is critical for achieving a time-optimal prover; and (3) a compact encoding of an R1CS instance as a low-degree polynomial. The end result is a public-coin succinct interactive argument of knowledge for NP (which can be viewed as a succinct variant of the sum-check protocol ); we transform it into a zkSNARK using prior techniques. By applying spark to different commitment schemes, we obtain several zkSNARKs where the verifier’s costs and the proof size range from O(log2 n) to O( √n) depending on the underlying commitment scheme (n denotes the size of the NP statement). These schemes do not require a trusted setup except for one that requires a universal trusted setup. We implement Spartan as a library in about 8,000 lines of Rust. We use the library to build a transparent zkSNARK in the random oracle model where security holds under the discrete logarithm assumption. We experimentally evaluate it and compare with recent zkSNARKs for R1CS instance sizes up to 220 constraints. Among schemes without trusted setup, Spartan offers the fastest prover with speedups of 36–152× depending on the baseline, produces proofs that are shorter by 1.2–416×, and incurs the lowest verification times with speedups of 3.6–1326×. When compared to the state-of-the-art zkSNARK with trusted setup, Spartan’s prover is 2× faster for arbitrary R1CS instances and 16× faster for data-parallel workloads

以下是中文翻译：

本文介绍了Spartan，这是一种新的零知识简洁非交互式知识论证（zkSNARKs）系列，针对的是秩-1约束可满足性（R1CS），这是一种NP完全语言，概括了算术电路的可满足性。Spartan的一个显著特点是，它提供了首个无需可信设置的zkSNARK（即透明zkSNARK），在NP中验证证明的成本为次线性成本——而不需要NP陈述结构的统一性。此外，Spartan还提供了具有时间最优证明者的zkSNARK，这一特性在文献中的几乎所有zkSNARK中都难以实现。

为了实现这些结果，我们引入了新的技术，并与和谐检查协议（sum-check protocol）这一开创性的交互式证明协议相结合：（1）计算承诺，这是一种创建对计算描述的简洁承诺的原语；这一技术对验证者在对给定的NP陈述进行一次性公共计算以进行预处理后，实现次线性成本至关重要；（2）spark，这是一种密码编译器，用于将任何现有的可提取多项式承诺方案转换为能够高效处理稀疏多线性多项式的方案；这一技术对于实现时间最优证明者至关重要；（3）将R1CS实例紧凑编码为低度多项式。最终结果是一个针对NP的公共币简洁交互知识论证（可以视为和谐检查协议的简洁变体）；我们利用之前的技术将其转换为zkSNARK。通过将spark应用于不同的承诺方案，我们获得了几个zkSNARK，其中验证者的成本和证明大小根据基础承诺方案的不同而变化，从\(O(\log^2 n)\)到\(O(\sqrt{n})\)（\(n\)表示NP陈述的大小）。这些方案不需要可信设置，除了一个需要通用可信设置的方案。

我们将Spartan实现为一个包含约8000行Rust代码的库。我们利用该库构建了一个在随机预言机模型下的透明zkSNARK，安全性基于离散对数假设。我们对其进行了实验评估，并与最近的R1CS实例大小达到220个约束的zkSNARK进行了比较。在没有可信设置的方案中，Spartan提供了最快的证明者，速度提升在36到152倍之间，生成的证明比其他方案短1.2到416倍，并且验证时间最低，速度提升在3.6到1326倍之间。与最先进的具有可信设置的zkSNARK相比，Spartan的证明者对于任意R1CS实例快2倍，对于数据并行工作负载快16倍。

## 关键词

+ Spartan透明zkSNARK无可信设置
+ R1CS次线性验证计算承诺
+ spark稀疏多线性多项式编译器
+ 和谐检查协议SNARK构造
+ 离散对数假设最优证明者