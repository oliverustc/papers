---
title: "Proof-carrying data without succinct arguments"
标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 2021
created: 2025-04-22 15:09:39
modified: 2025-04-22 15:10:29
---

## Proof-carrying data without succinct arguments

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-030-84242-0_24)

## 作者

+ [Benedikt Bünz](Benedikt%20Bünz.md) 
+ [Alessandro Chiesa](Alessandro%20Chiesa.md)
+ William Lin 
+ [Pratyush Mishra](Pratyush%20Mishra.md)
+ Nicholas Spooner 

## 笔记

Proof-carrying data (PCD) is a powerful cryptographic primitive that enables mutually distrustful parties to perform distributed computations that run indefinitely. Known approaches to construct PCD are based on succinct non-interactive arguments of knowledge (SNARKs) that have a succinct verifier or a succinct accumulation scheme.

In this paper we show how to obtain PCD without relying on SNARKs. We construct a PCD scheme given any non-interactive argument of knowledge (e.g., with linear-size arguments) that has a _split accumulation scheme_, which is a weak form of accumulation that we introduce.

Moreover, we construct a transparent non-interactive argument of knowledge for R1CS whose split accumulation is verifiable via a (small) _constant number of group and field operations_. Our construction is proved secure in the random oracle model based on the hardness of discrete logarithms, and it leads, via the random oracle heuristic and our result above, to concrete efficiency improvements for PCD.

Along the way, we construct a split accumulation scheme for Hadamard products under Pedersen commitments and for a simple polynomial commitment scheme based on Pedersen commitments.

Our results are supported by a modular and efficient implementation.

以下是中文翻译：

携证数据（proof-carrying data, PCD）是一种强大的密码学原语，它使互不信任的各方能够执行可无限运行的分布式计算。已知的构建PCD的方法都基于简洁非交互式知识论证（succinct non-interactive arguments of knowledge, SNARKs），这种论证具有简洁的验证器或简洁的累积方案。

在本文中，我们展示了如何在不依赖SNARKs的情况下获得PCD。我们构建了一个PCD方案，该方案基于任何具有分离累积方案（split accumulation scheme，这是我们提出的一种弱形式的累积）的非交互式知识论证（例如，具有线性大小论证的方案）。

此外，我们为R1CS构建了一个透明的非交互式知识论证，其分离累积可通过（少量）固定数量的群运算和域运算进行验证。我们的构建在随机预言模型中基于离散对数的困难性得到了安全性证明，并且通过随机预言启发式方法和我们上述的结果，为PCD带来了具体的效率改进。

在研究过程中，我们构建了Pedersen承诺下Hadamard积的分离累积方案，以及基于Pedersen承诺的简单多项式承诺方案的分离累积方案。

我们的研究结果得到了模块化且高效的实现支持。

## 关键词

+ 密码学
+ 零知识
+ 协议