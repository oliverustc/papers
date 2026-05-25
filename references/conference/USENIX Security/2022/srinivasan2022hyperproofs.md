---
title: "Hyperproofs: Aggregating and Maintaining Proofs in Vector Commitments"
标题简称: Hyperproofs
论文类型: conference
会议简称: USENIX Security
发表年份: 2022
modified: 2025-04-17 10:23:24
created: 2025-04-07 16:58:58
---

## Hyperproofs: Aggregating and Maintaining Proofs in Vector Commitments

## 发表信息

+ [原文链接](https://www.usenix.org/conference/usenixsecurity22/presentation/srinivasan)

## 作者

+ Srinivasan, Shravan
+ Chepurnoy, Alexander
+ [Charalampos Papamanthou](Charalampos%20Papamanthou.md)
+ Tomescu, Alin
+ [Yupeng Zhang](Yupeng%20Zhang.md)

## 笔记

We present Hyperproofs, the first vector commitment (VC) scheme that is efficiently maintainable and aggregatable. Similar to Merkle proofs, our proofs form a tree that can be efficiently maintained: updating all n proofs in the tree after a single leaf change only requires O(logn) time. Importantly, unlike Merkle proofs, Hyperproofs are efficiently aggregatable, anywhere from 10× to 41× faster than SNARK-based aggregation of Merkle proofs. At the same time, an individual Hyperproof consists of only logn algebraic hashes (e.g., 32-byte elliptic curve points) and an aggregation of b such proofs is only O(log(blogn))-sized. Hyperproofs are also reasonably fast to update when compared to Merkle trees with SNARK-friendly hash functions.

As another benefit over Merkle trees, Hyperproofs are homomorphic: digests (and proofs) for two vectors can be homomorphically combined into a digest (and proofs) for their sum. Homomorphism is very useful in emerging applications such as stateless cryptocurrencies. First, it enables unstealability, a novel property that incentivizes proof computation. Second, it makes digests and proofs much more convenient to update.

Finally, Hyperproofs have certain limitations: they are not transparent, have linear-sized public parameters, are slower to verify, and have larger aggregated proofs and slower verification than SNARK-based approaches. Nonetheless, end-to-end, aggregation and verification in Hyperproofs is 10× to 41× faster than in SNARK-based Merkle trees.

以下是中文翻译：

我们提出了Hyperproofs，这是一种高效可维护且可聚合的向量承诺（vector commitment, VC）方案。与Merkle证明类似，我们的证明形成了一棵树，可以高效地维护：在单个叶子节点发生变化后，更新树中的所有 $n$ 个证明只需 $O(\log n)$ 时间。重要的是，与Merkle证明不同，Hyperproofs可以高效聚合，其速度比基于SNARK的Merkle证明聚合快10倍到41倍。同时，单个Hyperproof仅由 $O(\log n)$ 个代数哈希（例如，32字节的椭圆曲线点）组成，而 $b$ 个此类证明的聚合大小仅为 $O(\log(b \log n))$。与使用SNARK友好哈希函数的Merkle树相比，Hyperproofs的更新速度也相对较快。

作为对Merkle树的另一个优势，Hyperproofs是同态的：两个向量的摘要（digests）和证明可以同态地组合成它们和的摘要（digests）和证明。同态性在新兴应用中非常有用，例如无状态加密货币。首先，它使得不可盗取性成为可能，这是一种激励证明计算的新颖属性。其次，它使摘要和证明的更新变得更加便利。

最后，Hyperproofs也存在某些局限性：它们不透明，公共参数规模为线性，验证速度较慢，并且聚合证明的大小和验证速度均比基于SNARK的方法更大。然而，整体而言，Hyperproofs中的聚合和验证速度比基于SNARK的Merkle树快10倍到41倍。

## 关键词

+ Hyperproofs向量承诺聚合
+ 可维护向量承诺方案
+ 同态向量承诺
+ 无状态加密货币
+ Merkle证明聚合优化
+ 椭圆曲线代数哈希
