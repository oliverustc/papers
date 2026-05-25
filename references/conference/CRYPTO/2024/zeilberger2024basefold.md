---
title: "BaseFold: Efficient Field-Agnostic Polynomial Commitment Schemes from Foldable Codes"
标题简称: BaseFold
论文类型: conference
会议简称: CRYPTO
发表年份: 2024
modified: 2025-04-10 16:59:54
---

## BaseFold: Efficient Field-Agnostic Polynomial Commitment Schemes from Foldable Codes

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-68403-6_5)

## 作者

+ [Hadas Zeilberger](Hadas%20Zeilberger.md)
+ [Binyi Chen](Binyi%20Chen.md)

## 笔记

This works introduces $\mathsf{BaseFold}$, a new field-agnostic Polynomial Commitment Scheme (PCS) for multilinear polynomials that has $O(\log^2(n))$ verifier costs and $O(n \log n)$ prover time. An important application of a multilinear PCS is constructing Succinct Non-interactive Arguments (SNARKs) from multilinear polynomial interactive oracle proofs (PIOPs). Furthermore, field-agnosticism is a major boon to SNARK efficiency in applications that require (or benefit from) a certain field choice.

Our inspiration for $\mathsf{BaseFold}$ is the Fast Reed-Solomon Interactive-Oracle Proof of Proximity ( $\mathsf{FRI}$ IOPP), which leverages two properties of Reed-Solomon (RS) codes defined over “FFT-friendly” fields: $O(n \log n)$ encoding time, and a second property that we call foldability. We first introduce a generalization of the $\mathsf{FRI}$ IOPP that works over any foldable linear code in linear time. Second, we construct a new family of linear codes which we call random foldable codes, that are a special type of punctured Reed-Muller codes, and prove tight bounds on their minimum distance. Unlike RS codes, our new codes are foldable and have $O(n \log n)$ encoding time over any sufficiently large field. Finally, we construct a new multilinear PCS by carefully interleaving our IOPP with the classical sumcheck protocol, which also gives a new multilinear PCS from $\mathsf{FRI}$.

$\mathsf{BaseFold}$ is 2–3 times faster than prior multilinear PCS constructions from $\mathsf{FRI}$ when defined over the same finite field. More significantly, using Hyperplonk (Eurocrypt, 2022) as a multilinear PIOP backend for apples-to-apples comparison, we show that $\mathsf{BaseFold}$ results in a SNARK that has better concrete efficiency across a range of field choices than with any prior multilinear PCS in the literature. Hyperplonk with $\mathsf{BaseFold}$ has a proof size that is more than 10 times smaller than Hyperplonk with Brakedown and its verifier is over 30 times faster for circuits with more than $2^{20}$ gates. Compared to , Hyperplonk with $\mathsf{BaseFold}$ retains efficiency over any sufficiently large field. For illustration, with $\mathsf{BaseFold}$ we can prove ECDSA signature verification over the secp256k1 curve more than 20 times faster than Hyperplonk with $\mathsf{FRI}$ and the verifier is also twice as fast. Proofs of signature verification have many useful applications, including offloading blockchain transactions and enabling anonymous credentials over the web.

以下是中文翻译：

这篇论文介绍了 $\mathsf{BaseFold}$，一种新的与域无关的多线性多项式承诺方案（Polynomial Commitment Scheme，PCS），其验证者成本为 $O(\log^2(n))$，证明者时间为 $O(n \log n)$。多线性PCS的重要应用之一是从多线性多项式交互式oracle证明（Polynomial Interactive Oracle Proofs，PIOPs）构建简洁非交互式论证（Succinct Non-interactive Arguments，SNARKs）。此外，与域无关性在需要（或受益于）特定域选择的应用中对SNARK效率有重大促进作用。

我们对 $\mathsf{BaseFold}$ 的灵感来源于快速Reed-Solomon交互式oracle接近证明（Fast Reed-Solomon Interactive-Oracle Proof of Proximity，$\mathsf{FRI}$ IOPP），该证明利用了定义在“FFT友好”域上的Reed-Solomon（RS）码的两个特性：$O(n \log n)$ 的编码时间，以及我们称之为可折叠性（foldability）的第二个特性。我们首先介绍了一个 $\mathsf{FRI}$ IOPP的广义形式，该形式可以在任何可折叠线性码上以线性时间运行。其次，我们构造了一种新的线性码家族，称为随机可折叠码（random foldable codes），这是一种特殊类型的穿孔Reed-Muller码，并证明了它们的最小距离的紧界限。与RS码不同，我们的新码是可折叠的，并且在任何足够大的域上具有 $O(n \log n)$ 的编码时间。最后，我们通过将我们的IOPP与经典的求和检查协议（sumcheck protocol）巧妙交错，构建了一个新的多线性PCS，这也为 $\mathsf{FRI}$ 提供了一个新的多线性PCS。

当在相同有限域上定义时，$\mathsf{BaseFold}$ 比之前基于 $\mathsf{FRI}$ 的多线性PCS构造快2到3倍。更重要的是，使用Hyperplonk（Eurocrypt, 2022）作为多线性PIOP后端进行同类比较，我们展示了 $\mathsf{BaseFold}$ 在一系列域选择中实现的SNARK在具体效率上优于文献中任何先前的多线性PCS。使用 $\mathsf{BaseFold}$ 的Hyperplonk，其证明大小比使用Brakedown的Hyperplonk小10倍以上，且其验证者在超过 $2^{20}$ 个门电路的情况下速度快30倍以上。与之相比，使用 $\mathsf{BaseFold}$ 的Hyperplonk在任何足够大的域上保持效率。举例来说，使用 $\mathsf{BaseFold}$，我们可以在secp256k1曲线上比使用 $\mathsf{FRI}$ 的Hyperplonk快20倍以上地证明ECDSA签名验证，且验证者的速度也快两倍。签名验证的证明具有许多有用的应用，包括卸载区块链交易和在网络上启用匿名凭证。

## 关键词

+ 多项式承诺方案
+ 域无关
+ 可折叠码
+ FRI交互式预言机证明
+ 多线性多项式
+ SNARK