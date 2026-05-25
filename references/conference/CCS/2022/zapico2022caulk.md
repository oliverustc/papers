---
title: "Caulk: Lookup arguments in sublinear time"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2022
created: 2025-04-16 09:42:16
modified: 2025-04-16 09:44:28
---

## Caulk: Lookup arguments in sublinear time

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3548606.3560646)

## 作者

+ Arantxa Zapico 
+ Vitalik Buterin 
+ [Dmitry Khovratovich](Dmitry%20Khovratovich.md)
+ [Mary Maller](Mary%20Maller.md)
+ Anca Nitulescu 
+ Mark Simkin 

## 笔记

We present position-hiding linkability for vector commitment schemes: one can prove in zero knowledge that one or m values that comprise commitment $cm$ all belong to the vector of size $N$ committed to in $C$. Our construction $\textsf{Caulk}$ can be used for membership proofs and lookup arguments and outperforms all existing alternatives in prover time by orders of magnitude.
For both single- and multi-membership proofs the $\textsf{Caulk}$ protocol beats SNARKed Merkle proofs by the factor of 100 even if the latter is instantiated with Poseidon hash. Asymptotically our prover needs $O(m^2 + m\log N)$ time to prove a batch of m openings, whereas proof size is $O(1)$ and verifier time is $O(\log(\log N))$. As a lookup argument, $\textsf{Caulk}$ is the first scheme with prover time sublinear in the table size, assuming $O(N\log N)$ preprocessing time and $O(N)$ storage. It can be used as a subprimitive in verifiable computation schemes in order to drastically decrease the lookup overhead.
Our scheme comes with a reference implementation and benchmarks.

以下是中文翻译：

我们提出了向量承诺方案的位置隐藏可链接性：可以在零知识条件下证明构成承诺 cm 的一个或 m 个值都属于在承诺 C 中大小为 N 的向量。我们的构造方案 Caulk 可用于成员证明和查找论证，在证明者计算时间方面比所有现有方案都优越数个数量级。

对于单成员和多成员证明，Caulk 协议比经过 SNARK 处理的 Merkle 证明快 100 倍，即使后者使用 Poseidon 哈希函数实现。从渐近角度看，我们的证明者需要 O(m² + m log N) 时间来证明 m 个开启的批处理，而证明大小为 O(1)，验证者时间为 O(log(log N))。作为查找论证，Caulk 是首个证明者时间小于表大小的方案，前提是需要 O(N log N) 预处理时间和 O(N) 存储空间。它可以作为可验证计算方案中的子原语使用，从而大幅降低查找开销。

我们的方案附有参考实现和基准测试。

## 关键词

+ 向量承诺
+ 查找论证
+ 零知识证明
+ 成员资格
+ 可验证计算