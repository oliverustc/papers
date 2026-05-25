---
title: "Succinct Hash-Based Arbitrary-Range Proofs"
标题简称:
论文类型: journal
期刊简称: TIFS
发表年份: 2024
modified: 2025-04-17 13:42:27
created: 2025-04-11 12:07:45
---

## Succinct Hash-Based Arbitrary-Range Proofs

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/10752637)

## 作者

+ Weihan Li 
+ Zongyang Zhang 
+ [Yanpei Guo](Yanpei%20Guo.md) 
+ [Sherman SM Chow](Sherman%20SM%20Chow.md)
+ Zhiguo Wan 

## 笔记

Zero-knowledge range proof (ZKRP) asserts that a committed integer V lies in a given range like $[0,2^n-1]$ without other leakages of V. It is vital in various privacy-preserving systems. Moving forward, the quest for post-quantum security is still in its infancy; the proof size of state-of-the-art lattice-based ZKRP (Lyubashevsky et al., CCS 20 and Couteau et al., Eurocrypt 21) remains linear in n, directly impacting the long-term sustainability in applications such as immutable ledgers. Confronting this unresolved impasse, we propose SHARP-PQ, i.e., succinct hash-based arbitrary-range proof with post-quantum security. SHARP-PQ offers proof size poly-logarithmic to n, optimized batch proofs, and versatile (new) capabilities. Its success stems from the improved inner product argument and exploitation of homomorphism. Empirically, SHARP-PQ features at least 10× smaller proof size for multiple ranges over lattice-based ZKRPs while maintaining competitive prover and verifier times. SHARP-PQ also outperforms ZKRPs directly constructed from hash-based generic zero-knowledge proofs at most 10×

以下是中文翻译：

零知识范围证明（ZKRP）声称一个已承诺的整数 $V$ 位于给定范围内，如 $[0,2^n-1]$，而不会泄露 $V$ 的其他信息。这在各种隐私保护系统中至关重要。展望未来，后量子安全的探索仍处于起步阶段；现有最先进的基于格的 ZKRP（Lyubashevsky 等人，CCS 20 和 Couteau 等人，Eurocrypt 21）的证明大小在 $n$ 上保持线性，这直接影响到在不可变账本等应用中的长期可持续性。面对这一未解决的困境，我们提出了 SHARP-PQ，即具有后量子安全性的简洁哈希基础任意范围证明。SHARP-PQ 提供的证明大小与 $n$ 的多对数关系，优化了批量证明，并具有多样化（新的）功能。其成功源于改进的内积论证和同态性质的利用。从经验上看，SHARP-PQ 在多个范围上的证明大小比基于格的 ZKRPs 小至少 10 倍，同时保持竞争力的证明者和验证者时间。SHARP-PQ 还在大多数情况下优于直接从基于哈希的通用零知识证明构造的 ZKRPs，性能提升可达 10 倍。

## 关键词

+ SHARP-PQ后量子安全范围证明
+ 简洁哈希基础任意范围证明
+ 多对数证明大小零知识范围证明
+ 内积论证同态性优化
+ 后量子格基ZKRP改进
+ 批量范围证明可验证系统