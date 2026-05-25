---
title: "Dual polynomial commitment schemes and applications to commit-and-prove SNARKs"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2024
created: 2025-04-23 14:59:43
modified: 2025-04-23 15:16:43
---

## Dual polynomial commitment schemes and applications to commit-and-prove SNARKs

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3658644.3690219)
+ [code](http://github.com/arithmic/Dual_PCS)

## 作者

+ [Chaya Ganesh](Chaya%20Ganesh.md)
+ Vineet Nair 
+ Ashish Sharma 

## 笔记

In this work, we introduce a primitive called a dual polynomial commitment scheme that allows linking together a witness committed to using a univariate polynomial commitment scheme with a witness inside a multilinear polynomial commitment scheme. This yields commit-and-prove (CP) SNARKs with the flexibility of going back and forth between univariate and multilinear encodings of witnesses. This is in contrast to existing CP frameworks that assume compatible polynomial commitment schemes between different components of the proof systems. In addition to application to CP, we also show that our notion yields a version of Spartan with better proof size and verification complexity, at the cost of a more expensive prover.

We achieve this via a combination of the following technical contributions: (i) we construct a new univariate commitment scheme in the updatable SRS setting that has better prover complexity than KZG (ii) we construct a new multilinear commitment scheme in the updatable setting that is compatible for linking with our univariate scheme (iii) we construct an argument of knowledge to prove a given linear relationship between two witnesses committed using a two-tiered commitment scheme (Pedersen+AFG) using Dory as a black-box. These constructions are of independent interest.

We implement our commitment schemes and report on performance. We also implement the version of Spartan with our dual polynomial commitment scheme and demonstrate that it outperforms Spartan in proof size and verification complexity.

以下是中文翻译：

在本研究中，我们提出了一种称为对偶多项式承诺方案(dual polynomial commitment scheme)的原语，它允许将使用单变量多项式承诺方案(univariate polynomial commitment scheme)承诺的证据与多线性多项式承诺方案(multilinear polynomial commitment scheme)中的证据链接在一起。这产生了具有灵活性的承诺-证明(commit-and-prove, CP) SNARK，可以在证据的单变量和多线性编码之间来回转换。这与现有的CP框架形成对比，后者假设证明系统的不同组件之间具有兼容的多项式承诺方案。除了CP的应用外，我们还证明我们的概念产生了一个改进版的Spartan，具有更好的证明大小和验证复杂度，但代价是更高的证明者开销。

我们通过以下技术贡献的组合实现了这一目标：(i)我们在可更新SRS设置中构建了一个新的单变量承诺方案，其证明者复杂度优于KZG；(ii)我们在可更新设置中构建了一个新的多线性承诺方案，该方案可与我们的单变量方案兼容链接；(iii)我们构建了一个知识论证，使用Dory作为黑盒来证明使用两层承诺方案(Pedersen+AFG)承诺的两个证据之间的给定线性关系。这些构造本身具有独立的研究价值。

我们实现了我们的承诺方案并报告了其性能。我们还实现了使用我们的对偶多项式承诺方案的Spartan版本，并证明它在证明大小和验证复杂度方面优于原始Spartan。

## 关键词

+ 多项式承诺
+ 承诺-证明SNARK
+ 单变量承诺
+ 多线性承诺
+ Spartan
+ 可更新SRS