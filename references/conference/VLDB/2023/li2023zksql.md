---
title: "ZKSQL: Verifiable and Efficient Query Evaluation with Zero-Knowledge Proofs"
标题简称:
论文类型: conference
会议简称: VLDB
发表年份: 2023

modified: 2025-04-09 14:00:47
---

## ZKSQL: Verifiable and Efficient Query Evaluation with Zero-Knowledge Proofs

## 发表信息

+ [原文链接](https://dl.acm.org/doi/10.14778/3594512.3594513)

## 作者

+ Xiling Li
+ [Chenkai Weng](Chenkai%20Weng.md)
+ Yongxin Xu
+ [Xiao Wang](Xiao%20Wang.md)
+ Jennie Rogers

## 笔记

Individuals and organizations are using databases to store personal information at an unprecedented rate. This creates a quandary for data providers. They are responsible for protecting the privacy of individuals described in their database. On the other hand, data providers are sometimes required to provide statistics about their data instead of sharing it wholesale with strong assurances that these answers are correct and complete such as in regulatory filings for the US SEC and other goverment organizations.
We introduce a system, ZKSQL, that provides authenticated answers to ad-hoc SQL queries with zero-knowledge proofs. Its proofs show that the answers are correct and sound with respect to the database's contents and they do not divulge any information about its input records. This system constructs proofs over the steps in a query's evaluation and it accelerates this process with authenticated set operations. We validate the efficiency of this approach over a suite of TPC-H queries and our results show that ZKSQL achieves two orders of magnitude speedup over the baseline.

以下是中文翻译：

个人和组织正以前所未有的速度使用数据库存储个人信息。这给数据提供者带来了两难境地。一方面，他们有责任保护数据库中个人信息的隐私。另一方面，数据提供者有时需要提供关于其数据的统计信息，而不是完整共享数据，同时还要强有力地保证这些答案的正确性和完整性，比如在向美国证券交易委员会(US SEC)和其他政府组织提交监管文件时。

我们介绍了一个系统ZKSQL，该系统可以使用零知识证明(zero-knowledge proofs)为临时SQL查询提供经过认证的答案。其证明表明答案相对于数据库内容是正确和可靠的，并且不会泄露任何关于输入记录的信息。该系统在查询评估的各个步骤中构建证明，并通过经过认证的集合运算(authenticated set operations)来加速这一过程。我们通过一系列TPC-H查询验证了这种方法的效率，结果表明ZKSQL比基准方法实现了两个数量级的速度提升。

## 关键词

+ ZKSQL零知识SQL查询验证
+ 隐私保护数据库查询
+ 认证集合运算
+ SQL查询完整性证明
+ 监管数据隐私合规
+ 零知识证明数据统计