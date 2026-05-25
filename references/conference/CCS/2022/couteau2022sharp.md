---
title: "Sharp: Short relaxed range proofs"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2022
modified: 2025-04-15 16:44:32
created: 2025-04-11 11:49:07
---

## Sharp: Short relaxed range proofs

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3548606.3560628)

## 作者

+ [Geoffroy Couteau](Geoffroy%20Couteau.md)
+ Dahmun Goudarzi 
+ Michael Klooß
+ [Michael Reichle](Michael%20Reichle.md)
## 笔记

We provide optimized range proofs, called Sharp, in discrete logarithm and hidden order groups, based on square decomposition. In the former setting, we build on the paradigm of Couteau et al. (Eurocrypt '21) and optimize their range proof (from now on, CKLR) in several ways: (1) We introduce batching via vector commitments and an adapted ∑;-protocol. (2) We introduce a new group switching strategy to reduce communication. (3) As repetitions are necessary to instantiate CKLR in standard groups, we provide a novel batch shortness test that allows for cheaper repetitions. The analysis of our test is nontrivial and forms a core technical contribution of our work. For example, for λ = 128 bit security and B = 64 bit ranges for N = 1 (resp. N = 8) proof(s), we reduce the proof size by 34% (resp. 75%) in arbitrary groups, and by 66% (resp. 88%) in groups of order 256-bit, compared to CKLR.

As Sharp and CKLR proofs satisfy a "relaxed" notion of security, we show how to enhance their security with one additional hidden order group element. In RSA groups, this reduces the size of state of the art range proofs (Couteau et al., Eurocrypt '17) by 77% (λ = 128, B = 64, N = 1).

Finally, we implement our most optimized range proof. Compared to the state of the art Bulletproofs (Bünz et al., S&P 2018), our benchmarks show a very significant runtime improvement. Eventually, we sketch some applications of our new range proofs.

以下是中文翻译：

我们提供了一种基于平方分解的优化范围证明，称为Sharp，适用于离散对数和隐藏阶群。在前一种设置中，我们基于Couteau等人（Eurocrypt '21）的范式，并在多个方面优化了他们的范围证明（以下简称CKLR）：(1) 我们通过向量承诺和适应的∑-协议引入了批处理。 (2) 我们引入了一种新的群切换策略，以减少通信量。 (3) 由于在标准群中实例化CKLR时需要重复，我们提供了一种新颖的批量简短性测试，允许更便宜的重复。我们测试的分析并非简单，构成了我们工作的核心技术贡献。例如，对于λ = 128位安全性和B = 64位范围的N = 1（或N = 8）证明，我们在任意群中将证明大小减少了34%（或75%），在256位阶的群中减少了66%（或88%），相比于CKLR。

由于Sharp和CKLR证明满足”放宽”的安全性概念，我们展示了如何通过增加一个额外的隐藏阶群元素来增强它们的安全性。在RSA群中，这将最先进的范围证明（Couteau等人，Eurocrypt '17）的大小减少了77%（λ = 128，B = 64，N = 1）。

最后，我们实现了我们最优化的范围证明。与最先进的Bulletproofs（Bünz等人，S&P 2018）相比，我们的基准测试显示出显著的运行时改进。最终，我们简要概述了我们新范围证明的一些应用。

## 关键词

+ 范围证明
+ 零知识证明
+ 离散对数
+ 群论
+ 密码学