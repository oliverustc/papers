---
title: "Zero-knowledge elementary databases with more expressive queries"
标题简称:
论文类型: conference
会议简称: PKC
发表年份: 2019
modified: 2025-04-11 14:26:20
---

## Zero-knowledge elementary databases with more expressive queries

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-030-17253-4_9)

## 作者

+ [Benoît Libert](Benoît%20Libert.md) 
+ [Khoa Nguyen](Khoa%20Nguyen.md)
+ Benjamin Hong Meng Tan 
+ [Huaxiong Wang](Huaxiong%20Wang.md)
## 笔记

Zero-knowledge elementary databases (ZK-EDBs) are cryptographic schemes that allow a prover to commit to a set $D$ of key-value pairs so as to be able to prove statements such as “x belongs to the support of $D$ and $D(x) = y$ or “x is not in the support of $D$”. Importantly, proofs should leak no information beyond the proven statement and even the size of $D$ should remain private. Chase et al. (Eurocrypt’05) showed that ZK-EDBs are implied by a special flavor of non-interactive commitment, called mercurial commitment, which enables efficient instantiations based on standard number theoretic assumptions. On the other hand, the resulting ZK-EDBs are only known to support proofs for simple statements like (non-)membership and value assignments. In this paper, we show that mercurial commitments actually enable significantly richer queries. We show that, modulo an additional security property met by all known efficient constructions, they actually enable range queries over keys and values – even for ranges of super-polynomial size – as well as membership/non-membership queries over the space of values. Beyond that, we exploit the range queries to realize richer queries such as k-nearest neighbors and revealing the  smallest or largest records within a given range. In addition, we provide a new realization of trapdoor mercurial commitment from standard lattice assumptions, thus obtaining the most expressive quantum-safe ZK-EDB construction so far.

以下是中文翻译：

零知识基本数据库（Zero-knowledge elementary databases, ZK-EDBs）是一种密码学方案，允许证明者对一组键值对$D$进行承诺，以便能够证明诸如“$x$属于$D$的支持集且$D(x) = y$”或“$x$不在$D$的支持集内”的陈述。重要的是，证明不应泄露超出证明陈述的信息，甚至$D$的大小也应保持私密。Chase等人（Eurocrypt’05）展示了ZK-EDBs由一种特殊类型的非交互式承诺（non-interactive commitment）所隐含，称为水银承诺（mercurial commitment），这种承诺能够基于标准数论假设实现高效的实例化。另一方面，所得到的ZK-EDBs仅被认为支持诸如（非）成员资格和数值分配等简单陈述的证明。在本文中，我们表明水银承诺实际上能够支持更丰富的查询。我们展示，考虑到所有已知高效构造所满足的额外安全属性，它们实际上能够实现对键和值的范围查询——甚至对于超多项式大小的范围——以及对值空间的成员资格/非成员资格查询。除此之外，我们利用范围查询实现更丰富的查询，如k近邻查询和在给定范围内揭示最小或最大记录。此外，我们提供了一种基于标准格假设的新型陷门水银承诺的实现，从而获得迄今为止最具表达力的量子安全ZK-EDB构造。

## 关键词

+ 零知识基本数据库（ZK-EDB）
+ 水银承诺
+ 范围查询
+ 格假设
+ 量子安全构造
+ 隐私保护数据库