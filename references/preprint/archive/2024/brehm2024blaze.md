---
title: "Blaze: Fast SNARKs from Interleaved RAA Codes"
标题简称:
论文类型: preprint
预印本简称: archive
发表年份: 2024

modified: 2025-04-10 16:59:33
---

## Blaze: Fast SNARKs from Interleaved RAA Codes

## 发表信息

+ [archive](https://eprint.iacr.org/2024/1609)

## 作者

+ Martijn Brehm
+ [Binyi Chen](Binyi%20Chen.md)
+ [Ben Fisch](Ben%20Fisch.md)
+ Nicolas Resch
+ Ron D. Rothblum
+ [Hadas Zeilberger](Hadas%20Zeilberger.md)

## 笔记

In this work we construct a new and highly efficient multilinear polynomial commitment scheme (MLPCS) over binary  fields, which we call \emph{Blaze}.    Polynomial commitment schemes allow a server to commit to a large polynomial and later decommit to its evaluations. Such schemes have emerged as a key component in recent efficient SNARK constructions.
    
Blaze has an extremely efficient prover, both asymptotically and concretely. The commitment is dominated by $8n$ field additions (i.e., XORs) and one Merkle tree computation. The evaluation proof generation is dominated by $6n$ additions and $5n$ multiplications over the field. The verifier runs in time $O_{\lambda}(\log^2(n))$. Concretely, for sufficiently large message sizes, the prover is faster than all prior schemes except for Brakedown (Golovnev et al., Crypto 2023), but offers significantly smaller proofs than the latter.

The scheme is obtained by combining two ingredients:

1. Building on the code-switching technique (Ron-Zewi and Rothblum, JACM 2024), we show how to compose any error-correcting code together with an interactive oracle proof of proximity (IOPP) underlying existing MLPCS constructions, into a new MLPCS. The new MLPCS inherits its proving time from the code's encoding time, and its verification complexity from the underlying MLPCS. The composition is distinctive in that it is done purely on the information-theoretic side.

2. We apply the above methodology using an extremely efficient error-correcting code known as the Repeat-Accumulate-Accumulate (RAA) code. We give new asymptotic and concrete bounds, which demonstrate that (for sufficiently large message sizes) this code has a better encoding time vs. distance tradeoff than previous linear-time encodable codes that were considered in the literature.


以下是中文翻译：

在本研究中，我们构建了一个新的、高效的二进制域上的多线性多项式承诺方案(multilinear polynomial commitment scheme, MLPCS)，我们称之为Blaze。多项式承诺方案允许服务器对一个大型多项式进行承诺，并在之后对其求值进行解承诺。这类方案已成为近期高效简洁非交互式知识论证(SNARK)构造中的关键组件。

Blaze具有极其高效的证明者，无论是渐近性能还是具体实现都很出色。承诺过程主要包含$8n$次域加法运算（即异或运算）和一次默克尔树计算。评估证明的生成主要包含$6n$次加法和$5n$次域乘法运算。验证者的运行时间为$O_{\lambda}(\log^2(n))$。具体而言，对于足够大的消息规模，除了Brakedown（Golovnev等人，Crypto 2023）之外，证明者比所有先前的方案都更快，但比后者提供更小的证明。

该方案通过结合以下两个要素获得：

1. 基于代码切换技术(code-switching technique)（Ron-Zewi和Rothblum，JACM 2024），我们展示了如何将任意纠错码与现有MLPCS构造中的交互式邻近性预言证明(Interactive Oracle Proof of Proximity, IOPP)组合，构建成新的MLPCS。新的MLPCS从代码的编码时间继承其证明时间，从底层MLPCS继承其验证复杂度。这种组合的特点在于它完全在信息论层面上完成。

2. 我们使用一种极其高效的纠错码——重复-累积-累积码(Repeat-Accumulate-Accumulate code, RAA code)应用上述方法。我们给出了新的渐近和具体界限，证明了（对于足够大的消息规模）该代码在编码时间与距离之间的权衡上优于文献中此前考虑的线性时间可编码码。

## 关键词

+ Blaze多线性多项式承诺方案
+ RAA码高效编码SNARK
+ 快速证明者二进制域
+ 代码切换技术IOPP组合
+ 线性时间可编码纠错码