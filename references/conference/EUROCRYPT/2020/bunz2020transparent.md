---
title: "Transparent SNARKs from DARK Compilers"
标题简称:
论文类型: conference
会议简称: EUROCRYPT
发表年份: 2020
modified: 2025-04-09 15:54:05
---

## Transparent SNARKs from DARK Compilers

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-030-45721-1_24)

## 作者

+ [Benedikt Bünz](Benedikt%20Bünz.md)
+ [Ben Fisch](Ben%20Fisch.md)
+ Alan Szepieniec

## 笔记

We construct a new polynomial commitment scheme for univariate and multivariate polynomials over finite fields, with logarithmic size evaluation proofs and verification time, measured in the number of coefficients of the polynomial. The underlying technique is a Diophantine Argument of Knowledge (DARK), leveraging integer representations of polynomials and groups of unknown order. Security is shown from the strong RSA and the adaptive root assumptions. Moreover, the scheme does not require a trusted setup if instantiated with class groups. We apply this new cryptographic compiler to a restricted class of algebraic linear IOPs, which we call Polynomial IOPs, to obtain doubly-efficient public-coin interactive arguments of knowledge for any NP relation with succinct communication. With linear preprocessing, the online verifier’s work is logarithmic in the circuit complexity of the relation.

There are many existing examples of Polynomial IOPs (PIOPs) dating back to the first PCP (BFLS, STOC’91). We present a generic compilation of any PIOP using our DARK polynomial commitment scheme. In particular, compiling the PIOP from PLONK (GWC, ePrint’19), an improvement on Sonic (MBKM, CCS’19), yields a public-coin interactive argument with quasi-linear preprocessing, quasi-linear (online) prover time, logarithmic communication, and logarithmic (online) verification time in the circuit size. Applying Fiat-Shamir results in a SNARK, which we call $\mathsf{Supersonic}$.

Supersonic is also concretely efficient with 10 KB proofs and under 100 ms verification time for circuits with 1 million gates (estimated for 120-bit security). Most importantly, this SNARK is transparent: it does not require a trusted setup. We obtain zk-SNARKs by applying a hiding variant of our polynomial commitment scheme with zero-knowledge evaluations. Supersonic is the first complete zk-SNARK system that has both a practical prover time as well as asymptotically logarithmic proof size and verification time. The full version of the paper is available online [19].

以下是中文翻译：

我们构建了一种新的多项式承诺方案，适用于有限域上的单变量和多变量多项式，具有对数大小的评估证明和验证时间，以多项式的系数数量为度量。该方案的基础技术是知识的丢番图论证（Diophantine Argument of Knowledge, DARK），利用多项式的整数表示和未知阶群。安全性基于强RSA假设和自适应根假设。此外，如果使用类群实例化，该方案不需要可信的初始化。我们将这一新的密码编译器应用于一种受限的代数线性交互证明（IOP）类别，称为多项式IOP（Polynomial IOP），以获得针对任何NP关系的双重高效公共币交互知识论证，通信效率高。通过线性预处理，在线验证者的工作量在关系的电路复杂度中是对数级的。

已有许多多项式IOP（PIOP）的实例，追溯到第一个概率检查器（PCP，BFLS，STOC’91）。我们展示了如何使用我们的DARK多项式承诺方案对任何PIOP进行通用编译。特别地，从PLONK（GWC，ePrint’19）编译的PIOP，作为对Sonic（MBKM，CCS’19）的改进，产生了一个公共币交互论证，具有准线性预处理、准线性（在线）证明者时间、对数通信和对数（在线）验证时间，均与电路大小相关。应用Fiat-Shamir结果得到一个SNARK，我们称之为$\mathsf{Supersonic}$。

Supersonic在具体效率上也表现优异，对于具有100万个门的电路，其证明大小为10 KB，验证时间少于100毫秒（估计基于120位安全性）。最重要的是，这个SNARK是透明的：它不需要可信的初始化。我们通过应用一种隐藏变体的多项式承诺方案，结合零知识评估，获得了zk-SNARK。Supersonic是第一个具有实用证明时间以及渐近对数证明大小和验证时间的完整zk-SNARK系统。论文的完整版本可在线获取[19]。

## 关键词

+ 透明SNARK
+ 多项式承诺方案
+ 丢番图知识论证
+ 未知阶群
+ Supersonic