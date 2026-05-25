---
title: "Non-interactive zero-knowledge proofs for composite statements"

标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 2018
modified: 2025-04-14 09:58:24
---

## Non-interactive zero-knowledge proofs for composite statements

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-319-96878-0_22)

## 作者

+ Shashank Agrawal 
+ [Chaya Ganesh](Chaya%20Ganesh.md)
+ [Payman Mohassel](Payman%20Mohassel.md)
## 笔记

The two most common ways to design non-interactive zero-knowledge (NIZK) proofs are based on Sigma protocols and QAP-based SNARKs. The former is highly efficient for proving algebraic statements while the latter is superior for arithmetic representations.

Motivated by applications such as privacy-preserving credentials and privacy-preserving audits in cryptocurrencies, we study the design of NIZKs for composite statements that compose algebraic and arithmetic statements in arbitrary ways. Specifically, we provide a framework for proving statements that consist of ANDs, ORs and function compositions of a mix of algebraic and arithmetic components. This allows us to explore the full spectrum of trade-offs between proof size, prover cost, and CRS size/generation cost. This leads to proofs for statements of the form: knowledge of x such that $SHA(g^x) = y$  for some public y where the prover’s work is 500 times fewer exponentiations compared to a QAP-based SNARK at the cost of increasing the proof size to 2404 group and field elements. In application to anonymous credentials, our techniques result in 8 times fewer exponentiations for the prover at the cost of increasing the proof size to 298 elements.

以下是中文翻译：

设计非交互式零知识(NIZK)证明最常见的两种方法是基于Sigma协议和基于QAP的SNARK。前者在证明代数语句方面效率很高，而后者在算术表示方面具有优势。

受隐私保护凭证和加密货币中隐私保护审计等应用的启发，我们研究了针对复合语句的NIZK设计，这些复合语句以任意方式组合代数和算术语句。具体来说，我们提供了一个框架，用于证明由代数和算术组件混合而成的AND、OR和函数组合构成的语句。这使我们能够探索证明大小、证明者计算成本以及CRS(Common Reference String，公共参考串)大小/生成成本之间的全部权衡范围。这导致了对如下形式语句的证明：对于某个公开的y，知道x使得$SHA(g^x) = y$成立，其中与基于QAP的SNARK相比，证明者的工作量减少了500倍的指数运算，代价是将证明大小增加到2404个群元素和域元素。在匿名凭证的应用中，我们的技术使证明者的指数运算减少了8倍，代价是将证明大小增加到298个元素。

## 关键词

+ 复合语句NIZK非交互零知识
+ Sigma协议QAP-SNARK混合框架
+ 代数算术语句AND-OR组合证明
+ 隐私凭证加密货币审计应用
+ 证明大小证明开销权衡CRS