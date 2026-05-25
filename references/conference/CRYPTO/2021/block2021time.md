---
title: "Time-and space-efficient arguments from groups of unknown order"

标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 2021
created: 2025-04-28 17:02:33
modified: 2025-04-28 17:05:44
---

## Time-and space-efficient arguments from groups of unknown order

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-030-84259-8_5)

## 作者

+ Alexander R Block 
+ Justin Holmgren 
+ Alon Rosen 
+ Ron D Rothblum 
+ Pratik Soni 

## 笔记

We construct public-coin time- and space-efficient zero-knowledge arguments for NP. For every time T and space S non-deterministic RAM computation, the prover runs in time T⋅polylog(T) and space S⋅polylog(T), and the verifier runs in time n⋅polylog(T), where n is the input length. Our protocol relies on hidden order groups, which can be instantiated with a trusted setup from the hardness of factoring (products of safe primes), or without a trusted setup using class groups. The argument-system can heuristically be made non-interactive using the Fiat-Shamir transform. Our proof builds on DARK (Bünz et al., Eurocrypt 2020), a recent succinct and efficiently verifiable polynomial commitment scheme. We show how to implement a variant of DARK in a time- and space-efficient way. Along the way we: 1. Identify a significant gap in the proof of security of DARK. 2. Give a non-trivial modification of the DARK scheme that overcomes the aforementioned gap. The modified version also relies on significantly weaker cryptographic assumptions than those in the original DARK scheme. Our proof utilizes ideas from the theory of integer lattices in a novel way. 3. Generalize Pietrzak's (ITCS 2019) proof of exponentiation (PoE) protocol to work with general groups of unknown order (without relying on any cryptographic assumption). In proving these results, we develop general-purpose techniques for working with (hidden order) groups, which may be of independent interest.

以下是中文翻译：

我们构建了针对NP问题的公共随机(public-coin)时空高效零知识论证系统。对于每个时间复杂度为T、空间复杂度为S的非确定性RAM计算，证明者的运行时间为T⋅polylog(T)，空间复杂度为S⋅polylog(T)，验证者的运行时间为n⋅polylog(T)，其中n为输入长度。我们的协议依赖于隐藏阶群(hidden order groups)，该群可以通过基于分解难度假设(安全素数的乘积)的可信设置来实例化，或使用类群(class groups)在无需可信设置的情况下实例化。该论证系统可以通过菲亚特-沙米尔变换(Fiat-Shamir transform)启发式地转换为非交互式系统。

我们的证明基于DARK(Bünz等人，Eurocrypt 2020)，这是一个最新的简洁且可高效验证的多项式承诺方案。我们展示了如何以时空高效的方式实现DARK的一个变体。在此过程中，我们：

1. 发现了DARK安全性证明中的一个重要缺陷。

2. 对DARK方案进行了非平凡的修改以克服上述缺陷。修改后的版本还比原始DARK方案依赖于更弱的密码学假设。我们的证明以新颖的方式运用了整数格理论的思想。

3. 将Pietrzak(ITCS 2019)的指数证明(proof of exponentiation, PoE)协议推广到一般的未知阶群(无需依赖任何密码学假设)。

在证明这些结果的过程中，我们开发了用于处理(隐藏阶)群的通用技术，这些技术可能具有独立的研究价值。

## 关键词

+ 时空高效零知识论证NP
+ 隐藏阶群DARK多项式承诺
+ 类群指数证明PoE推广
+ 可信设置因子分解安全假设
+ 整数格理论零知识论证应用