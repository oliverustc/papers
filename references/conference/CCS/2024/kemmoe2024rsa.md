---
title: "RSA-Based Dynamic Accumulator without Hashing into Primes"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2024
---

## RSA-Based Dynamic Accumulator without Hashing into Primes

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3658644.3690199)

## 作者

+ Victor Youdom Kemmoe 
+ [Anna Lysyanskaya](Anna%20Lysyanskaya.md) 


## 笔记

A cryptographic accumulator is a compact data structure for representing a set of elements coming from some domain. It allows for a compact proof of membership and, in the case of a universal accumulator, non-membership of an element x in the data structure. A dynamic accumulator, furthermore, allows elements to be added to and deleted from the accumulator.

Previously known RSA-based dynamic accumulators were too slow in practice because they required that an element in the domain be represented as a prime number. Accumulators based on settings other than RSA had other drawbacks such as requiring a prohibitively large common reference string or a trapdoor, or not permitting deletions.

In this paper, we construct an RSA-based dynamic accumulator that does not require that the accumulated elements be represented as primes and show how it can be extended into a universal accumulator. We also show how to aggregate membership and non-membership witnesses and batch additions and deletions. We demonstrate that, for 112-bit, 128-bit, and 192-bit security, the efficiency gains compared to previously known RSA-based accumulators are substantial, and, for the first time, make cryptographic accumulators a viable candidate for a certificate revocation mechanism as part of a WebPKI-type system. To achieve an efficient verification time for aggregated witnesses, we introduce a variant of Wesolowski's proof of exponentiation (Journal of Cryptology 2020) that does not require hashing into primes.

以下是中文翻译：

密码学累加器（cryptographic accumulator）是一种紧凑的数据结构，用于表示来自某一特定域（domain）的元素集合。它能够为某元素 x 是否属于该数据结构提供紧凑的成员性证明（proof of membership）；在通用累加器（universal accumulator）的情形下，还可提供非成员性证明（proof of non-membership）。动态累加器（dynamic accumulator）进一步支持向累加器中添加或删除元素。

以往已知的基于 RSA 的动态累加器在实践中效率过低，因其要求域中的每个元素必须表示为素数（prime number）。而基于非 RSA 设定的累加器则存在其他缺陷，例如需要长度不可接受的公共参考串（common reference string）、依赖陷门（trapdoor），或不支持元素删除操作。

本文构建了一种基于 RSA 的动态累加器，其无需将被累加的元素表示为素数，并展示了如何将其扩展为通用累加器。我们还提出了成员性与非成员性见证（witnesses）的聚合方法，以及批量添加与删除操作的实现机制。实验表明，在 112 位、128 位和 192 位安全级别下，相较于以往已知的基于 RSA 的累加器，本方案在效率上具有显著提升，并首次使密码学累加器成为 WebPKI 类系统中证书撤销机制（certificate revocation mechanism）的可行候选方案。为实现聚合见证的高效验证，我们引入了 Wesolowski 指数运算证明（proof of exponentiation，《Journal of Cryptology》2020）的一种变体，该变体无需将哈希值映射为素数。

## 关键词

+ RSA动态累加器
+ 通用累加器
+ 见证聚合
+ 证书撤销机制
+ 无素数映射的指数证明