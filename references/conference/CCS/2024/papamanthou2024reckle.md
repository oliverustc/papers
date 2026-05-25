---
title: "Reckle Trees: Updatable Merkle Batch Proofs with Applications"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2024
modified: 2025-04-23 15:49:29
created: 2025-04-08 21:59:42
---

## Reckle Trees: Updatable Merkle Batch Proofs with Applications

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3658644.3670354)

## 作者

+ [Charalampos Papamanthou](Charalampos%20Papamanthou.md)
+ Shravan Srinivasan
+ Nicolas Gailly
+ Ismael Hishon-Rezaizadeh
+ Andrus Salumets
+ Stjepan Golemac

## 笔记

We propose Reckle trees, a new vector commitment based on succinct RECursive arguments and MerKLE trees. Reckle trees' distinguishing feature is their support for succinct batch proofs that are updatable - enabling new applications in the blockchain setting where a proof needs to be computed and efficiently maintained over a moving stream of blocks. Our technical approach is based on embedding the computation of the batch hash inside the recursive Merkle verification via a hash-based accumulator called canonical hashing. Due to this embedding, our batch proofs can be updated in logarithmic time, whenever a Merkle leaf (belonging to the batch or not) changes, by maintaining a data structure that stores previously-computed recursive proofs. Assuming enough parallelism, our batch proofs are also computable in O(log n) parallel time - independent of the size of the batch. As a natural extension of Reckle trees, we also introduce Reckle+ trees. Reckle+ trees provide updatable and succinct proofs for certain types of Map/Reduce computations. In this setting, a prover can commit to a memory M and produce a succinct proof for a Map/Reduce computation over a subset _I_ of M. The proof can be efficiently updated whenever _I_ or M changes.

以下是中文翻译：

我们提出Reckle树，这是一种基于简洁递归论证（RECursive arguments）与默克尔树（MerKLE trees）的新型向量承诺方案。其核心特性在于支持可更新的简洁批量证明——这一特性为区块链环境开辟了新应用场景，其中需对不断更新的区块流进行证明计算并高效维护。我们的技术路径通过名为规范哈希（canonical hashing）的基于哈希的累加器，将批量哈希计算嵌入递归式默克尔验证过程中。得益于这种嵌入设计，每当默克尔叶节点（无论是否属于该批次）发生变动时，通过维护存储预计算递归证明的数据结构，我们的批量证明可在对数时间内完成更新。在充分并行条件下，批量证明的计算同样仅需O(log n)并行时间——与批次规模无关。作为Reckle树的自然延伸，我们还引入了Reckle+树，它为特定类型的Map/Reduce计算提供可更新且简洁的证明机制。在此框架下，证明者可对内存M作出承诺，并为M的子集I上的Map/Reduce计算生成简洁证明。当I或M发生变更时，该证明可被高效更新。

我们展示并实验评估了Reckle+树的两个应用，动态摘要翻译和可更新的BLS聚合。在动态摘要翻译中，我们维护一个证明，证明使用不同哈希函数（例如，一个使用SNARK友好的Poseidon，另一个使用SNARK不友好的Keccak）计算的Merkle摘要之间的等价性。在可更新的BLS聚合中，我们维护一个证明，证明从Merkle承诺的个人BLS密钥集合的t子集推导的t聚合BLS密钥的正确聚合。我们使用Plonky2进行的评估表明，Reckle树和Reckle+树具有小的内存占用，在更新（10×到15×）和验证（4.78×到1485×）时间方面显著优于先前的方法，支持以前由于巨大成本而不可能实现的应用（Reckle树快200倍），并与之前的批量证明实现具有相似的聚合性能。

## 关键词

+ 向量承诺
+ 默克尔树
+ 批量证明
+ 递归论证
+ 可更新证明
+ BLS聚合

We present and experimentally evaluate two applications of Reckle+ trees, dynamic digest translation and updatable BLS aggregation. In dynamic digest translation we are maintaining a proof of equivalence between Merkle digests computed with different hash functions, e.g., one with a SNARK-friendly Poseidon and the other with a SNARK-unfriendly Keccak. In updatable BLS aggregation we maintain a proof for the correct aggregation of a _t_-aggregate BLS key, derived from a _t_-subset of a Merkle-committed set of individual BLS keys. Our evaluation using Plonky2 shows that Reckle trees and Reckle+ trees have small memory footprint, significantly outperform previous approaches in terms of updates (10× to 15×) and verification (4.78× to 1485×) time, enable applications that were not possible before due to huge costs involved (Reckle trees are up to 200× faster), and have similar aggregation performance with previous implementations of batch proofs.