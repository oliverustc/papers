---
title: "Efficient zero-knowledge arguments for arithmetic circuits in the discrete log setting"
标题简称:
论文类型: conference
会议简称: EUROCRYPT
发表年份: 2016
modified: 2025-05-12 08:49:07
created: 2025-04-08 17:01:54
---

## Efficient zero-knowledge arguments for arithmetic circuits in the discrete log setting

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-662-49896-5_12)

## 作者

+ [Jonathan Bootle](Jonathan%20Bootle.md)
+ Andrea Cerulli
+ Pyrros Chaidos
+ [Jens Groth](Jens%20Groth.md)
+ Christophe Petit

## 笔记

We provide a zero-knowledge argument for arithmetic circuit satisfiability with a communication complexity that grows logarithmically in the size of the circuit. The round complexity is also logarithmic and for an arithmetic circuit with fan-in 2 gates the computation of the prover and verifier is linear in the size of the circuit. The soundness of our argument relies solely on the well-established discrete logarithm assumption in prime order groups.

At the heart of our new argument system is an efficient zero-knowledge argument of knowledge of openings of two Pedersen multicommitments satisfying an inner product relation, which is of independent interest. The inner product argument requires logarithmic communication, logarithmic interaction and linear computation for both the prover and the verifier.

We also develop a scheme to commit to a polynomial and later reveal the evaluation at an arbitrary point, in a verifiable manner. This is used to build an optimized version of the constant round square root complexity argument of Groth (CRYPTO 2009), which reduces both communication and round complexity.

以下是中文翻译：

我们提供了一种零知识证明（zero-knowledge argument），用于算术电路可满足性（arithmetic circuit satisfiability），其通信复杂度与电路规模呈对数增长。回合复杂度也呈对数增长，对于具有2个输入的算术电路，证明者（prover）和验证者（verifier）的计算复杂度在电路规模上是线性的。我们论证的健壮性仅依赖于在素数阶群体中广泛认可的离散对数假设（discrete logarithm assumption）。

我们新论证系统的核心是一个高效的零知识知识证明，证明者对满足内积关系的两个佩德森多重承诺（Pedersen multicommitments）开口的知识，这本身也是一个独立的研究兴趣。内积论证需要对数级的通信、对数级的交互以及证明者和验证者的线性计算。

我们还开发了一种方案，用于对多项式进行承诺，并在可验证的方式下随后揭示在任意点的评估。这一方案用于构建Groth（CRYPTO 2009）提出的常数回合平方根复杂度论证的优化版本，从而减少了通信和回合复杂度。

## 关键词

+ 零知识论证
+ 算术电路可满足性
+ 离散对数假设
+ 内积论证
+ 对数通信复杂度