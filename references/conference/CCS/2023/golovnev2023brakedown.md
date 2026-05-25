---
title: "Brakedown: Linear-Time and Field-Agnostic SNARKs for R1CS"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2023
modified: 2025-04-21 10:52:20
created: 2025-04-08 20:57:45
---

## Brakedown: Linear-Time and Field-Agnostic SNARKs for R1CS

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-38545-2_7)

## 作者

+ Alexander Golovnev
+ [Jonathan Lee](Jonathan%20Lee.md)
+ [Srinath Setty](Srinath%20Setty.md)
+ [Justin Thaler](Justin%20Thaler.md)
+ Riad S. Wahby

## 笔记

This paper introduces a SNARK called _Brakedown_. Brakedown targets R1CS, a popular NP-complete problem that generalizes circuit-satisfiability. It is the first built system that provides a _linear-time_ prover, meaning the prover incurs _O_(_N_) finite field operations to prove the satisfiability of an _N_-sized R1CS instance. Brakedown ’s prover is faster, both concretely and asymptotically, than prior SNARK implementations. It does not require a trusted setup and may be post-quantum secure. Furthermore, it is compatible with _arbitrary_ finite fields of sufficient size; this property is new among built proof systems with sublinear proof sizes. To design Brakedown, we observe that recent work of Bootle, Chiesa, and Groth (BCG, TCC 2020) provides a polynomial commitment scheme that, when combined with the linear-time interactive proof system of Spartan (CRYPTO 2020), yields linear-time IOPs and SNARKs for R1CS (a similar theoretical result was previously established by BCG, but our approach is conceptually simpler, and crucial for achieving high-speed SNARKs). A core ingredient in the polynomial commitment scheme that we distill from BCG is a linear-time encodable code. Existing constructions of such codes are believed to be impractical. Nonetheless, we design and engineer a new one that is practical in our context.

We also implement a variant of Brakedown that uses Reed-Solomon codes instead of our linear-time encodable codes; we refer to this variant as _Shockwave_. Shockwave is _not_ a linear-time SNARK, but it provides shorter proofs and lower verification times than Brakedown, and also provides a faster prover than prior plausibly post-quantum SNARKs.

以下是中文翻译：

本文介绍了一种称为 Brakedown 的 SNARK。Brakedown 针对 R1CS（约束满足问题），这是一个流行的 NP 完全问题，广义上涉及电路可满足性。它是第一个提供线性时间证明者的系统，这意味着证明者在证明大小为 N 的 R1CS 实例的可满足性时需进行 O(N) 次有限域运算。Brakedown 的证明者在具体和渐近意义上都比先前的 SNARK 实现更快。它不需要可信设置，并且可能具有后量子安全性。此外，它与足够大任意有限域兼容；这一特性在具有亚线性证明大小的构建证明系统中是新的。为设计 Brakedown，我们观察到 Bootle、Chiesa 和 Groth（BCG，TCC 2020）最近的工作提供了一种多项式承诺方案，当与 Spartan（CRYPTO 2020）的线性时间交互证明系统结合时，可以为 R1CS 产生线性时间的 IOPs 和 SNARKs（BCG 之前确立了类似的理论结果，但我们的方法在概念上更简单，并且对于实现高速 SNARK 至关重要）。我们从 BCG 中提炼出的多项式承诺方案的一个核心成分是线性时间可编码码。现有的此类码的构造被认为不够实用。尽管如此，我们设计并工程出一种在我们上下文中实用的新编码。

我们还实现了一种 Brakedown 的变体，该变体使用 Reed-Solomon 码而不是我们的线性时间可编码码；我们将这一变体称为 Shockwave。Shockwave 并不是一种线性时间的 SNARK，但它提供了比 Brakedown 更短的证明和更低的验证时间，同时也提供了比先前的可合理认为具有后量子安全性的 SNARK 更快的证明者。

## 关键词

+ 零知识论证
+ SNARK
+ 线性时间证明
+ 后量子密码学
+ 多项式承诺