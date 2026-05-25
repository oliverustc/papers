---
title: "Fast RS-IOP Multivariate Polynomial Commitments and Verifiable Secret Sharing"
标题简称:
论文类型: conference
会议简称: USENIX Security
发表年份: 2024
created: 2025-04-17 10:26:29
modified: 2025-04-17 10:27:03
---

## Fast RS-IOP Multivariate Polynomial Commitments and Verifiable Secret Sharing

## 发表信息

+ [原文链接](https://www.usenix.org/conference/usenixsecurity24/presentation/zhang-zongyang)

## 作者

+ Zongyang Zhang 
+ Weihan Li 
+ [Yanpei Guo](Yanpei%20Guo.md) 
+ Kexin Shi 
+ [Sherman SM Chow](Sherman%20SM%20Chow.md)
+ Ximeng Liu 
+ Jin Dong 

## 笔记

Supporting proofs of evaluations, polynomial commitment schemes (PCS) are crucial in secure distributed systems. Schemes based on fast Reed–Solomon interactive oracle proofs (RS-IOP) of proximity have recently emerged, offering transparent setup, plausible post-quantum security, efficient operations, and, notably, sublinear proof size and verification. Manifesting a new paradigm, PCS with one-to-many proof can enhance the performance of (asynchronous) verifiable secret sharing ((A)VSS), a cornerstone in distributed computing, for proving multiple evaluations to multiple verifiers. Current RS-IOP-based multivariate PCS, including HyperPlonk (Eurocrypt '23) and Virgo (S&P '20), however, only offer quasi-linear prover complexity in the polynomial size.

We propose PolyFRIM, a fast RS-IOP-based multivariate PCS with optimal linear prover complexity, 5-25× faster than prior arts while ensuring competent proof size and verification. Heeding the challenging absence of FFT circuits for multivariate evaluation, PolyFRIM surpasses Zhang et al.'s (Usenix Sec. '22) one-to-many univariate PCS, accelerating proving by 4-7× and verification by 2-4× with 25% shorter proof. Leveraging PolyFRIM, we propose an AVSS scheme FRISS with a better efficiency tradeoff than prior arts from multivariate PCS, including Bingo (Crypto '23) and Haven (FC '21).

以下是中文翻译：

支持评估证明的多项式承诺方案（Polynomial Commitment Schemes, PCS）在安全分布式系统中至关重要。基于快速的Reed–Solomon交互式Oracle证明（RS-IOP）接近性的方案最近出现，提供了透明的设置、合理的后量子安全性、高效的操作，以及显著的亚线性证明大小和验证。作为一种新范式，具有一对多证明的PCS可以增强（异步）可验证秘密共享（(A)VSS）的性能，后者是分布式计算的基石，能够为多个验证者证明多个评估。然而，当前基于RS-IOP的多变量PCS，包括HyperPlonk（Eurocrypt '23）和Virgo（S&P '20），仅在多项式大小中提供准线性的证明者复杂度。

我们提出了PolyFRIM，这是一种基于快速RS-IOP的多变量PCS，具有最佳的线性证明者复杂度，比之前的方案快5-25倍，同时确保了合理的证明大小和验证效率。鉴于多变量评估缺乏快速傅里叶变换（FFT）电路的挑战，PolyFRIM超越了Zhang等人（Usenix Sec. '22）的单变量一对多PCS，证明速度提高了4-7倍，验证速度提高了2-4倍，且证明长度缩短了25%。借助PolyFRIM，我们提出了一种效率权衡优于之前方案的AVSS方案FRISS，基于多变量PCS，包括Bingo（Crypto '23）和Haven（FC '21）。

## 关键词

+ RS-IOP多变量多项式承诺方案
+ 线性证明者复杂度优化
+ 可验证秘密共享AVSS
+ 透明后量子设置
+ 亚线性证明大小验证
+ 一对多证明分布式计算