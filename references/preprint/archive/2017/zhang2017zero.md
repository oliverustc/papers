---
title: "A Zero-Knowledge Version of vSQL"
标题简称:
论文类型: preprint
预印本简称: archive
发表年份: 2017
modified: 2025-04-11 10:54:53
---

## A Zero-Knowledge Version of vSQL

## 发表信息

+ [archive](https://eprint.iacr.org/2017/1146)

## 作者

+ [Yupeng Zhang](Yupeng%20Zhang.md)
+ Daniel Genkin
+ [Jonathan Katz](Jonathan%20Katz.md)
+ [Dimitrios Papadopoulos](Dimitrios%20Papadopoulos.md)
+ [Charalampos Papamanthou](Charalampos%20Papamanthou.md)

## 笔记

Zero-knowledge arguments of knowledge are powerful cryptographic primitives that allow a computationally strong prover to convince a weaker verifier for the validity of an NP statement, without revealing anything about the corresponding witness (beyond its existence). Most state-of-the-art implementations of such arguments that achieve succinct communication and verification cost follow the quadratic arithmetic program paradigm. One notable exception to this is the vSQL system of [Zhang et al. IEEE S&P 2017] which takes an entirely different approach resulting is significantly fewer cryptographic operations. However, it has the notable downside that is not zero-knowledge (i.e., it does not hide the witness from the verifier), a property that has proven to be of utmost importance in many application (e.g., in cryptocurrencies). In this work, we present a zero-knowledge version of the argument upon which vSQL is based. Our construction utilizes two separate techniques: (i) a novel zero-knowledge verifiable polynomial delegation protocol, and (ii) running parts of the argument of vSQL over homomorphic commitments, thus hiding the committed values.

以下是中文翻译：

零知识知识论证(Zero-knowledge arguments of knowledge)是一种强大的密码学原语，它允许计算能力较强的证明者向计算能力较弱的验证者证明某个NP陈述的有效性，而无需透露关于相应见证(witness)的任何信息（除了其存在性之外）。当前最先进的此类论证实现大多遵循二次算术程序(quadratic arithmetic program)范式，以实现简洁的通信和验证成本。一个显著的例外是[Zhang等人 IEEE S&P 2017]提出的vSQL系统，该系统采用了完全不同的方法，显著减少了密码学运算。然而，它有一个明显的缺点，即不具备零知识性（也就是说，它不能对验证者隐藏见证），而这一特性在许多应用中（如加密货币）已被证明是极其重要的。在本研究中，我们提出了vSQL所基于的论证的零知识版本。我们的构造运用了两种独立的技术：(i)一种新颖的零知识可验证多项式委托(verifiable polynomial delegation)协议，以及(ii)通过同态承诺(homomorphic commitments)执行vSQL论证的部分内容，从而隐藏所承诺的值。

## 关键词

+ vSQL零知识版本扩展
+ 零知识可验证多项式委托
+ 同态承诺隐藏见证
+ 数据库查询零知识验证
+ 简洁通信验证零知识论证
+ 加密货币隐私保护应用