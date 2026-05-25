---
title: "On the size of pairing-based non-interactive arguments"
标题简称:
论文类型: conference
会议简称: EUROCRYPT
发表年份: 2016
created: 2025-05-12 08:54:37
modified: 2025-05-12 08:56:54
---

## On the size of pairing-based non-interactive arguments

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-662-49896-5_11)

## 作者

+ [Jens Groth](Jens%20Groth.md)

## 笔记

Non-interactive arguments enable a prover to convince a verifier that a statement is true. Recently there has been a lot of progress both in theory and practice on constructing highly efficient non-interactive arguments with small size and low verification complexity, so-called succinct non-interactive arguments (SNARGs) and succinct non-interactive arguments of knowledge (SNARKs).

Many constructions of SNARGs rely on pairing-based cryptography. In these constructions a proof consists of a number of group elements and the verification consists of checking a number of pairing product equations. The question we address in this article is how efficient pairing-based SNARGs can be.

Our first contribution is a pairing-based (preprocessing) SNARK for arithmetic circuit satisfiability, which is an NP-complete language. In our SNARK we work with asymmetric pairings for higher efficiency, a proof is only 3 group elements, and verification consists of checking a single pairing product equations using 3 pairings in total. Our SNARK is zero-knowledge and does not reveal anything about the witness the prover uses to make the proof.

As our second contribution we answer an open question of Bitansky, Chiesa, Ishai, Ostrovsky and Paneth (TCC 2013) by showing that linear interactive proofs cannot have a linear decision procedure. It follows from this that SNARGs where the prover and verifier use generic asymmetric bilinear group operations cannot consist of a single group element. This gives the first lower bound for pairing-based SNARGs. It remains an intriguing open problem whether this lower bound can be extended to rule out 2 group element SNARGs, which would prove optimality of our 3 element construction.

以下是中文翻译：

非交互式论证使证明者能够使验证者相信某个陈述是真实的。近年来，在构建高效的非交互式论证方面，无论是理论还是实践都取得了巨大进展，特别是在降低规模和验证复杂度方面，这类论证被称为简洁非交互式论证(SNARGs)和简洁非交互式知识论证(SNARKs)。

许多SNARGs的构造都依赖于基于配对的密码学(pairing-based cryptography)。在这些构造中，证明由若干群元素组成，验证则包括检查若干配对积方程。本文要解决的问题是：基于配对的SNARGs能够达到多高的效率。

我们的第一个贡献是为算术电路可满足性（这是一个NP完全语言）构造了一个基于配对的（预处理）SNARK。在我们的SNARK中，我们使用非对称配对以提高效率，证明仅包含3个群元素，验证只需要检查一个配对积方程，总共使用3个配对运算。我们的SNARK具有零知识性，不会泄露证明者用于生成证明的见证(witness)的任何信息。

作为我们的第二个贡献，我们回答了Bitansky、Chiesa、Ishai、Ostrovsky和Paneth（TCC 2013）提出的一个开放问题，证明了线性交互式证明(linear interactive proofs)不可能具有线性决策程序。由此可以推导出，如果证明者和验证者仅使用通用非对称双线性群运算，则SNARGs不可能仅由一个群元素组成。这是首个针对基于配对的SNARGs的下界。一个引人入胜的开放问题是，这个下界是否可以扩展到排除2个群元素的SNARGs，这将证明我们的3元素构造的最优性。

## 关键词

+ 简洁非交互式知识论证
+ 配对密码学
+ 算术电路可满足性
+ 零知识证明
+ 配对下界证明