---
title: "Non-Interactive Zero-Knowledge Proofs for Composite Statements"

标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 2018
---

## Non-Interactive Zero-Knowledge Proofs for Composite Statements

## 发表信息

+ [DOI](https://doi.org/10.1007/978-3-319-96878-0_22)
+ [ePrint](https://eprint.iacr.org/2018/557)

## 作者

+ Shashank Agrawal
+ [Chaya Ganesh](Chaya%20Ganesh.md)
+ [Payman Mohassel](Payman%20Mohassel.md)
## 笔记

The two most common ways to design non-interactive zero-knowledge (NIZK) proofs are based on Sigma protocols and QAP-based SNARKs. The former is highly efficient for proving algebraic statements while the latter is superior for arithmetic representations. Motivated by applications such as privacy-preserving credentials and privacy-preserving audits in cryptocurrencies, we study the design of NIZKs for composite statements that compose algebraic and arithmetic statements in arbitrary ways. Specifically, we provide a framework for proving statements that consist of ANDs, ORs and function compositions of a mix of algebraic and arithmetic components. This allows us to explore the full spectrum of trade-offs between proof size, prover cost, and CRS size/generation cost. This leads to proofs for statements of the form: knowledge of $x$ such that $SHA(g^x)=y$ for some public $y$ where the prover's work is 500 times fewer exponentiations compared to a QAP-based SNARK at the cost of increasing the proof size to 2404 group and field elements. In application to anonymous credentials, our techniques result in 8 times fewer exponentiations for the prover at the cost of increasing the proof size to 298 elements.

以下是中文翻译：

设计非交互式零知识证明（NIZK）最常见的两种方法是基于Sigma协议和基于QAP的SNARK。前者在证明代数陈述方面非常高效，而后者则更适用于算术表示。受隐私保护凭证和加密货币中隐私保护审计等应用的启发，我们研究了针对以任意方式组合代数和算术陈述的复合陈述的NIZK设计。具体而言，我们提供了一个用于证明由代数和算术组件混合组成的AND、OR及函数复合陈述的框架。这使我们能够探索证明大小、证明者开销与CRS大小/生成开销之间的全面权衡。这导致了如下形式陈述的证明：对于某个公开的$y$，知道满足$SHA(g^x)=y$的$x$，与基于QAP的SNARK相比，证明者的指数运算减少了500倍，代价是将证明大小增加到2404个群和域元素。在匿名凭证的应用中，我们的技术使证明者的指数运算减少了8倍，代价是将证明大小增加到298个元素。

## 关键词

+ 复合陈述非交互式零知识证明框架
+ Sigma协议QAP-SNARK混合构造
+ 代数算术陈述AND-OR组合证明
+ 隐私保护凭证加密货币审计应用
+ 证明大小证明者开销CRS权衡优化