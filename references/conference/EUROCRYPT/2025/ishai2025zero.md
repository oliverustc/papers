---
title: "Zero-knowledge RAM: doubly efficient and black-box"
标题简称:
论文类型: conference
会议简称: EUROCRYPT
发表年份: 2025
---

## Zero-knowledge RAM: doubly efficient and black-box

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-91134-7_13)

## 作者

+ [Yuval Ishai](Yuval%20Ishai.md)
+ Rafail Ostrovsky 
+ Akash Shah 


## 笔记
We consider the problem of verifying the computations of a RAM program on a committed database $x \in \{0,1\}^n$. A recent work by Ishai, Ostrovsky, and Shah (Crypto 2023) obtained a doubly efficient solution, in which the communication and verifier’s work are polylogarithmic in n and the prover’s work is comparable to the (possibly sublinear) running time of the RAM program. This only makes a black-box use of a collision-resistant hash function, or alternatively can be implemented unconditionally and non-interactively in the random oracle model.

In the current work, we extend this prior work by providing an additional zero-knowledge guarantee and by supporting database updates. This gives the first doubly efficient zero-knowledge implementation of RAM programs that makes a black-box use of symmetric cryptography.

While the extra zero knowledge and updatable database features of our solution are orthogonal in scope, our means for achieving them are technically related: to verify with zero knowledge many computations on the same database, we rely on a database refreshing procedure that we also use to accommodate updates.


以下是中文翻译：

我们研究在已承诺的数据库 $x \in \{0,1\}^n$ 上验证随机存取机（Random Access Machine, RAM）程序计算结果的问题。Ishai、Ostrovsky 与 Shah 在近期工作（CRYPTO 2023）中提出了一种双重高效（doubly efficient）的解决方案：其中通信复杂度与验证者（verifier）的计算开销均为 $n$ 的多对数级别（polylogarithmic），而证明者（prover）的计算开销则与 RAM 程序本身的（可能为次线性的）运行时间相当。该方案仅以黑盒方式（black-box）调用抗碰撞性哈希函数（collision-resistant hash function），或者在随机预言机模型（random oracle model）下可无条件地、非交互式地实现。

在本文工作中，我们在前述研究基础上进一步引入了额外的零知识（zero-knowledge）保证，并支持数据库更新（database updates）。这构成了首个以黑盒方式仅依赖对称密码学（symmetric cryptography）的双重高效零知识 RAM 程序实现方案。

尽管我们方案中新增的零知识性与可更新数据库功能在目标上彼此正交（orthogonal），但实现二者的技术手段却密切相关：为在零知识条件下验证对同一数据库的多次计算，我们依赖一种数据库刷新（database refreshing）过程，而该过程同样被用于处理数据库更新。

## 关键词

+ 零知识证明
+ 双重高效验证
+ 随机存取机（RAM）程序
+ 可更新承诺数据库
+ 黑盒对称密码学
+ 数据库刷新机制