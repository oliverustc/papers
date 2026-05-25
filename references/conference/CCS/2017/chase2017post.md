---
title: "Post-Quantum Zero-Knowledge and Signatures from Symmetric-Key Primitives"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2017
modified: 2025-04-08 17:11:20
---

## Post-Quantum Zero-Knowledge and Signatures from Symmetric-Key Primitives

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3133956.3133997)

## 作者

+ [Melissa Chase](Melissa%20Chase.md)
+ David Derler
+ Steven Goldfeder
+ [Claudio Orlandi](Claudio%20Orlandi.md)
+ Sebastian Ramacher
+ Christian Rechberger,
+ Daniel Slamanig
+ Greg Zaverucha

## 笔记

We propose a new class of post-quantum digital signature schemes that: (a) derive their security entirely from the security of symmetric-key primitives, believed to be quantum-secure, and (b) have extremely small keypairs, and, (c) are highly parameterizable.
In our signature constructions, the public key is an image y=f(x) of a one-way function f and secret key x. A signature is a non-interactive zero-knowledge proof of x, that incorporates a message to be signed. For this proof, we leverage recent progress of Giacomelli et al. (USENIX'16) in constructing an efficient Σ-protocol for statements over general circuits. We improve this Σ-protocol to reduce proof sizes by a factor of two, at no additional computational cost. While this is of independent interest as it yields more compact proofs for any circuit, it also decreases our signature sizes.
We consider two possibilities to make the proof non-interactive: the Fiat-Shamir transform and Unruh's transform (EUROCRYPT'12, '15,'16). The former has smaller signatures, while the latter has a security analysis in the quantum-accessible random oracle model. By customizing Unruh's transform to our application, the overhead is reduced to 1.6x when compared to the Fiat-Shamir transform, which does not have a rigorous post-quantum security analysis.
We implement and benchmark both approaches and explore the possible choice of f, taking advantage of the recent trend to strive for practical symmetric ciphers with a particularly low number of multiplications and end up using Low MC (EUROCRYPT'15).

以下是中文翻译：

我们提出了一类新的后量子数字签名方案，该方案：(a) 其安全性完全源自被认为具有量子安全性的对称密钥原语，(b) 具有极小的密钥对，以及 (c) 具有高度可参数化的特点。

在我们的签名构造中，公钥是单向函数f的像y=f(x)，其中x为私钥。签名是关于x的非交互式零知识证明，其中包含了待签名的消息。对于这个证明，我们利用了Giacomelli等人(USENIX'16)最近在构建通用电路语句的高效Σ协议(Σ-protocol)方面的进展。我们改进了这个Σ协议，在不增加计算成本的情况下将证明大小减少了一半。这不仅对于任何电路都能产生更紧凑的证明而具有独立价值，同时也减小了我们的签名大小。

我们考虑了两种使证明成为非交互式的方法：Fiat-Shamir变换和Unruh变换(EUROCRYPT'12, '15,'16)。前者具有更小的签名大小，而后者在量子可访问随机预言模型(quantum-accessible random oracle model)中具有安全性分析。通过将Unruh变换定制化应用于我们的方案，与没有严格后量子安全性分析的Fiat-Shamir变换相比，开销降低到了1.6倍。

我们实现并对这两种方法进行了基准测试，并探索了函数f的可能选择。利用近期追求具有特别少的乘法运算的实用对称密码的趋势，我们最终选择使用Low MC(EUROCRYPT'15)。

## 关键词

+ 后量子密码学
+ 数字签名
+ 对称密钥原语
+ Sigma协议
+ 量子安全性