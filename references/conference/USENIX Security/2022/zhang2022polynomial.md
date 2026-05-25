---
title: "Polynomial Commitment with a One-to-Many Prover and Applications"
标题简称:
论文类型: conference
会议简称: USENIX Security
发表年份: 2022

modified: 2025-04-21 00:28:11
created: 2025-04-07 16:59:47
---

## Polynomial Commitment with a One-to-Many Prover and Applications

## 发表信息

+ [原文链接](https://www.usenix.org/conference/usenixsecurity22/presentation/zhang-jiaheng)

## 作者

+ [Jiaheng Zhang](Jiaheng%20Zhang.md)
+ [Tiancheng Xie](Tiancheng%20Xie.md)
+ Thang Hoang
+ [Elaine Shi](Elaine%20Shi.md)
+ [Yupeng Zhang](Yupeng%20Zhang.md)

## 笔记

Verifiable Secret Sharing (VSS) is a foundational cryptographic primitive that serves as an essential building block in multi-party computation and decentralized blockchain applications. One of the most practical ways to construct VSS is through a polynomial commitment, where the dealer commits to a random polynomial whose 0-th coefficient encodes the secret to be shared, and proves the evaluation of the committed polynomial at a different point to each of N verifiers, i.e., the polynomial commitment is used in a "one-to-many" fashion.

The recent work of Tomescu et al. (IEEE S&P 2020) was the first to consider polynomial commitment with "one-to-many prover batching", such that the prover can prove evaluations at N different points at the cost of Oe(1) proofs. However, their scheme is not optimal and requires a trusted setup.

In this paper, we asymptotically improve polynomial commitment with one-to-many prover batching. We propose two novel schemes. First, we propose a scheme with optimal asymptotics in all dimensions in the trusted setup setting. Second, we are the first to consider one-to-many prover batching for transparent polynomial commitments, and we propose a transparent scheme whose performance approximately matches the best-known scheme in the trusted setup setting.

We implement our schemes and evaluate their performance. Our scheme in the trusted setup setting improves the proof size by 20× and the verifier time by 7.8× for 2 21 parties, with a small overhead on the prover time. Our transparent polynomial commitment removes the trusted setup and further improves the prover time by 2.3×.

以下是中文翻译：

可验证秘密共享（Verifiable Secret Sharing, VSS）是一种基础的密码学原语，是多方计算和去中心化区块链应用中的重要构建块。构造VSS的最实用方法之一是通过多项式承诺（polynomial commitment），在这种方法中，分发者承诺一个随机多项式，其0次系数编码了要共享的秘密，并向每个N个验证者证明在不同点上对承诺多项式的评估，即多项式承诺以“一个对多个”的方式使用。

Tomescu等人（IEEE S&P 2020）的最新研究首次考虑了具有“一个对多个证明者批处理”的多项式承诺，使得证明者可以以$O_e(1)$的成本在N个不同点上证明评估。然而，他们的方案并不最优，并且需要一个可信的设置（trusted setup）。

在本文中，我们在一个对多个证明者批处理的情况下，渐近地改进了多项式承诺。我们提出了两种新颖的方案。首先，我们提出了一种在可信设置下在所有维度上具有最优渐近性的方案。其次，我们首次考虑了透明多项式承诺（transparent polynomial commitments）中的一个对多个证明者批处理，并提出了一种透明方案，其性能大致与可信设置下已知的最佳方案相匹配。

我们实现了我们的方案并评估了其性能。在可信设置下，我们的方案将证明大小提高了20倍，并将2^21个参与者的验证者时间提高了7.8倍，证明者时间的额外开销较小。我们的透明多项式承诺消除了可信设置，并进一步将证明者时间提高了2.3倍。

## 关键词

+ 一对多多项式承诺批量证明
+ 可验证秘密共享VSS
+ 透明多项式承诺
+ 无可信设置多项式方案
+ 证明批量化证明优化
+ 分布式区块链密码学
