---
title: "Cauchyproofs: Batch-Updatable Vector Commitment with Easy Aggregation and Application to Stateless Blockchains"
标题简称:
论文类型: conference
会议简称: S&P
发表年份: 2025
---

## Cauchyproofs: Batch-Updatable Vector Commitment with Easy Aggregation and Application to Stateless Blockchains

## 发表信息

+ [原文链接]()

## 作者

+ Zhongtang Luo 
+ Yanxue Jia 
+ Alejandra Victoria Ospina Gracia 
+ [Aniket Kate](Aniket%20Kate.md)
## 笔记

Stateless blockchain designs have emerged to address the challenge of growing blockchain size using succinct global states. Previous works have developed vector commitments that support proof updates and aggregation to be used as such states. However, maintaining proofs for multiple users still demands significant computational resources, particularly to update proofs with every transaction. This paper introduces Cauchyproofs, a batch-updatable vector commitment that enables proof-serving nodes to efficiently update proofs in quasilinear time relative to the number of users and transactions, utilizing an optimized KZG scheme to achieve complexity $o((|\vec{\alpha}|+|\vec{\beta}|)log^2(|\vec{\alpha}|+|\vec{\beta} |))$ for $|\alpha|$ users and $|\beta|$ transactions, compared to the previous $O(|\alpha|⋅|\beta |)$ approaches. This advancement reduces the computational burden on proof-serving nodes, allowing efficient proof maintenance across large user groups. We demonstrate that our approach is approximately eight times faster than the naive approach at the Ethereumlevel transaction throughput if we perform batch update every hour. Additionally, we present a novel matrix representation for KZG proofs utilizing Cauchy matrices, enabling faster all-proof computations with reduced elliptic curve operations. Finally, we propose an algorithm for history proof query, supporting retrospective proof generation with high efficiency. Our contributions substantially enhance the scalability and practicality of proof-serving nodes in stateless blockchain frameworks.

以下是中文翻译：

无状态区块链设计已经出现，旨在通过使用简洁的全局状态来解决区块链规模不断增长的挑战。先前的研究工作开发了支持证明更新和聚合的向量承诺（vector commitments），以用作此类状态。然而，为多个用户维护证明仍然需要大量的计算资源，特别是在每笔交易中更新证明。本文介绍了 Cauchyproofs，这是一种批量可更新的向量承诺，使证明服务节点能够以相对于用户数量和交易数量的拟线性时间高效更新证明。

该方案利用优化的 KZG 方案，对于 $|\alpha|$ 个用户和 $|\beta|$ 笔交易，实现了复杂度 $o((|\vec{\alpha}|+|\vec{\beta}|)log^2(|\vec{\alpha}|+|\vec{\beta}|))$，相比之前的 $O(|\alpha|⋅|\beta|)$ 方法有显著改进。这一进展减少了证明服务节点的计算负担，允许在大型用户群体中高效维护证明。我们证明，如果每小时执行一次批量更新，在以太坊级别的交易吞吐量下，我们的方法比朴素方法快约八倍。

此外，我们提出了一种利用柯西矩阵（Cauchy matrices）的 KZG 证明新颖矩阵表示法，通过减少椭圆曲线运算实现更快的全证明计算。最后，我们提出了一种历史证明查询算法，支持高效的回溯证明生成。我们的贡献显著增强了无状态区块链框架中证明服务节点的可扩展性和实用性。

## 关键词

+ Cauchyproofs批量可更新向量承诺
+ 无状态区块链
+ KZG多项式承诺优化
+ 拟线性时间复杂度
+ 柯西矩阵证明表示
+ 历史证明查询