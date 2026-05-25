---
title: "Succinct zero-knowledge batch proofs for set accumulators"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2022
modified: 2025-04-22 09:51:09
created: 2025-04-13 16:51:17
---

## Succinct zero-knowledge batch proofs for set accumulators

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3548606.3560677)

## 作者

+ [Matteo Campanelli](Matteo%20Campanelli.md)
+ [Dario Fiore](Dario%20Fiore.md)
+ Semin Han 
+ Jihye Kim 
+ [Dimitris Kolonelos](Dimitris%20Kolonelos.md)
+ [Hyunok Oh](Hyunok%20Oh.md)
## 笔记

Cryptographic accumulators are a common solution to proving information about a large set S. They allow one to compute a short digest of S and short certificates of some of its basic properties, notably membership of an element. Accumulators also allow one to track set updates: a new accumulator is obtained by inserting/deleting a given element. In this work we consider the problem of generating membership and update proofs for  batches of elements so that we can succinctly prove additional properties of the elements (i.e., proofs are of constant size regardless of the batch size), and we can preserve privacy. Solving this problem would allow obtaining blockchain systems with improved privacy and scalability. The state-of-the-art approach to achieve this goal is to combine accumulators (typically Merkle trees) with zkSNARKs. This solution is however expensive for provers and does not scale for large batches of elements. In particular, there is no scalable solution for proving batch membership proofs when we require zero-knowledge (a standard definition of privacy-preserving protocols). In this work we propose new techniques to efficiently use zkSNARKs with RSA accumulators. We design and implement two main schemes: 1) \harisa, which proves batch membership in zero-knowledge; 2) \insarisa, which proves batch updates. For batch membership, the prover in \harisa is orders of magnitude faster than existing approaches based on Merkle trees (depending on the hash function). For batch updates we get similar cost savings compared to approaches based on Merkle trees; we also improve over the recent solution of Ozdemir et al. [USENIX'20].

以下是中文翻译：

密码累加器是证明大型集合S相关信息的一种常见解决方案。它们能够计算出S的简短摘要及其某些基本属性（尤其是元素成员资格）的简短证明。累加器还能追踪集合的更新：通过插入或删除给定元素获得新的累加器。在本研究中，我们探讨了为批量元素生成成员资格及更新证明的问题，旨在简洁地证明元素的额外属性（即无论批量大小如何，证明保持恒定尺寸），并保护隐私。解决此问题将有助于开发出隐私性和可扩展性更优的区块链系统。

实现这一目标的最先进方法是将累加器（通常是默克尔树）与zkSNARKs相结合。然而，这种方案对证明者来说成本高昂，且在处理大批量元素时难以扩展。特别是，当我们需要零知识（隐私保护协议的标准定义）时，目前尚无可扩展的解决方案来证明批量成员资格。

在这项工作中，我们提出了新技术以高效地将zkSNARKs与RSA累加器结合使用。我们设计并实现了两大方案：1）HARISA，用于零知识证明批量成员资格；2）INSARISA，用于证明批量更新。在批量成员资格方面，HARISA中的证明者比基于Merkle树的现有方法快数个数量级（具体取决于哈希函数）。对于批量更新，与基于Merkle树的方法相比，我们实现了类似的成本节约；同时，我们还改进了Ozdemir等人[USENIX'20]的最新解决方案。

## 关键词

+ 累加器
+ 零知识证明
+ 批量成员资格
+ RSA累加器
+ 区块链隐私