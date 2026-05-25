---
title: "Efficient range proofs with transparent setup from bounded integer commitments"
标题简称:
论文类型: conference
会议简称: EUROCRYPT
发表年份: 2021
modified: 2025-04-16 10:54:35
created: 2025-04-11 11:50:13
---

## Efficient range proofs with transparent setup from bounded integer commitments

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-030-77883-5_9)

## 作者

+ [Geoffroy Couteau](Geoffroy%20Couteau.md)
+ Michael Klooß 
+ Huang Lin 
+ [Michael Reichle](Michael%20Reichle.md)
## 笔记

We introduce a new approach for constructing range proofs. Our approach is modular, and leads to highly competitive range proofs under standard assumption, using less communication and (much) less computation than the state of the art methods, and without relying on a trusted setup. Our range proofs can be used as a drop-in replacement in a variety of protocols such as distributed ledgers, anonymous transaction systems, and many more, leading to significant reductions in communication and computation for these applications.

At the heart of our result is a new method to transform any commitment over a finite field into a commitment scheme which allows to commit to and efficiently prove relations about _bounded integers_. Combining these new commitments with a classical approach for range proofs based on square decomposition, we obtain several new instantiations of a paradigm which was previously limited to RSA-based range proofs (with high communication and computation, and trusted setup). More specifically, we get:

- Under the discrete logarithm assumption, we obtain the most compact and efficient range proof among all existing candidates (with or without trusted setup). Our proofs are 12% to 20% shorter than the state of the art Bulletproof (Bootle et al., CRYPTO’18) for standard choices of range size and security parameter, and are more efficient (both for the prover and the verifier) by more than an order of magnitude.
    
- Under the LWE assumption, we obtain range proofs that improve over the state of the art in a batch setting when at least a few dozen range proofs are required. The amortized communication of our range proofs improves by up to two orders of magnitudes over the state of the art when the number of required range proofs grows.
    
- Eventually, under standard class group assumptions, we obtain the first concretely efficient standard integer commitment scheme (without bounds on the size of the committed integer) which does not assume trusted setup.

以下是中文翻译：

我们提出了一种构建范围证明的新方法。我们的方法是模块化的，在标准假设下能产生极具竞争力的范围证明，与现有最先进的方法相比，需要更少的通信量和（更少的）计算量，并且不依赖可信设置。我们的范围证明可以在各种协议中作为即插即用的替代方案，如分布式账本、匿名交易系统等多种应用中，能显著降低这些应用的通信和计算开销。

我们成果的核心是一种新方法，可以将有限域上的任何承诺转换为一种承诺方案，该方案允许对有界整数进行承诺并高效地证明其关系。将这些新的承诺方案与基于平方分解的经典范围证明方法相结合，我们获得了几种新的实现方式，突破了之前仅限于基于RSA的范围证明（具有高通信量、高计算量和可信设置要求）的范式。具体来说，我们得到：

- 在离散对数假设下，我们获得了在所有现有方案中（无论是否需要可信设置）最紧凑和最高效的范围证明。对于标准范围大小和安全参数的选择，我们的证明比现有最先进的Bulletproof（Bootle等人，CRYPTO'18）短12%到20%，且效率（对证明者和验证者而言）提高了一个数量级以上。
    
- 在LWE假设下，当需要至少几十个范围证明时，我们在批处理环境中获得了优于现有技术的范围证明。随着所需范围证明数量的增加，我们的范围证明的平均通信量比现有技术提升了最多两个数量级。
    
- 最终，在标准类群假设下，我们获得了第一个具体可行的标准整数承诺方案（对所承诺整数的大小没有限制），且不需要可信设置。

## 关键词

+ 范围证明
+ 有界整数承诺
+ 透明设置
+ 离散对数
+ LWE假设