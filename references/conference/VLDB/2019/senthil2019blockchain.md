---
title: "Blockchain meets database: design and implementation of a blockchain relational database J"
标题简称:
论文类型: conference
会议简称: VLDB
发表年份: 2019
created: 2025-04-19 11:31:15
modified: 2025-04-19 11:34:03
---

## Blockchain meets database: design and implementation of a blockchain relational database

## 发表信息

+ [原文链接](https://dl.acm.org/doi/10.14778/3342263.3342632)

## 作者

+ Nathan Senthil 
+ Govindarajan Chander 
+ Saraf Adarsh 
+ M Sethi 
+ P Jayachandran 

## 笔记

In this paper, we design and implement the first-ever decentralized replicated relational database with blockchain properties that we term _blockchain relational database_. We highlight several similarities between features provided by blockchain platforms and a replicated relational database, although they are conceptually different, primarily in their trust model. Motivated by this, we leverage the rich features, decades of research and optimization, and available tooling in relational databases to build a blockchain relational database. We consider a permissioned blockchain model of known, but mutually distrustful organizations each operating their own database instance that are replicas of one another. The replicas execute transactions independently and engage in decentralized consensus to determine the commit order for transactions. We design two approaches, the first where the commit order for transactions is agreed upon prior to executing them, and the second where transactions are executed without prior knowledge of the commit order while the ordering happens in parallel. We leverage serializable snapshot isolation (SSI) to guarantee that the replicas across nodes remain consistent and respect the ordering determined by consensus, and devise a new variant of SSI based on block height for the latter approach. We implement our system on PostgreSQL and present detailed performance experiments analyzing both approaches.

以下是中文翻译：

在本文中，我们设计并实现了第一个具有区块链属性的去中心化复制关系数据库，我们称之为区块链关系数据库（blockchain relational database）。我们强调了区块链平台提供的特性与复制关系数据库之间的若干相似之处，尽管它们在概念上是不同的，主要体现在信任模型上。基于这一动机，我们利用关系数据库丰富的特性、数十年的研究和优化以及现有的工具，构建了一个区块链关系数据库。我们考虑了一种受限区块链模型，由已知但相互不信任的组织组成，每个组织各自运行一个数据库实例，这些实例是彼此的副本。这些副本独立执行事务，并通过去中心化共识来确定事务的提交顺序。我们设计了两种方法：第一种是在执行事务之前就达成提交顺序的协议；第二种是在没有事先知道提交顺序的情况下执行事务，同时在并行中进行排序。我们利用可串行快照隔离（Serializable Snapshot Isolation, SSI）来保证跨节点的副本保持一致，并遵循共识确定的排序，并为后一种方法设计了一种基于区块高度的新变体SSI。我们在PostgreSQL上实现了我们的系统，并提供了详细的性能实验，分析了这两种方法。

## 关键词

+ 区块链关系数据库
+ 去中心化共识事务排序
+ 可串行快照隔离SSI
+ 受限区块链模型
+ 分布式数据库一致性
+ PostgreSQL区块链实现