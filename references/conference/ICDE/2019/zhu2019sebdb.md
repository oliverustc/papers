---
title: "SEBDB: Semantics empowered blockchain database"
标题简称:
论文类型: conference
会议简称: ICDE
发表年份: 2019
created: 2025-04-19 11:29:21
modified: 2025-04-19 11:29:56
---

## SEBDB: Semantics empowered blockchain database

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/8731416)

## 作者

+ Yanchao Zhu 
+ Zhao Zhang 
+ Cheqing Jin 
+ Aoying Zhou 
+ Ying Yan 

## 笔记

Blockchain has been adopted in many applications to construct trust among multiple participants, such as supply chain management, digital assets transfer, philanthropy, etc. Blockchain platforms are often used as decentralized databases. However, existing blockchain platforms are far less convenient to use than traditional databases. They are lack of the capability of modelling complex tasks conveniently and efficiently, especially when both on-chain and off-chain data are involved at the same time. In this paper, we propose and implement a novel blockchain database, called SEBDB, which leverages the existing databases' functionality which are optimized for decades. Comparing to existing works, SEBDB is the first platform which considers both useability and scalability. Specifically, first, weaddrelationaldata semantics into blockchain platform, where each transaction is a tuple with multiple attributes in a pre-defined table. Second, we use SQL-like language as the general interface, instead of code-level APIs, to support convenient application development, in which intrinsic operations are re-defined and re-implemented to suit for blockchain platform. Third, as RDBMS has achieved great success in the past decades, our system, though not relying on RDBMS, treats it as an important component. Finally, we define a mini-benchmark to evaluate the performance of the blockchain database. Extensive experiments demonstrate the effectiveness and efficiency of our proposed system.

以下是中文翻译：

区块链已经被广泛应用于许多领域，以在多个参与者之间建立信任，例如供应链管理、数字资产转移、慈善等。区块链平台通常被用作去中心化数据库。然而，现有的区块链平台在使用便利性上远不及传统数据库。它们缺乏方便有效建模复杂任务的能力，尤其是在同时涉及链上和链下数据时。在本文中，我们提出并实现了一种新颖的区块链数据库，称为SEBDB，该数据库利用了经过数十年优化的现有数据库功能。与现有工作相比，SEBDB是第一个同时考虑可用性和可扩展性的平台。具体而言，首先，我们将关系数据语义引入区块链平台，其中每个交易都是一个具有多个属性的元组，存储在预定义的表中。其次，我们使用类似SQL的语言作为通用接口，而不是代码级API，以支持方便的应用开发，在此过程中，内部操作被重新定义和实现，以适应区块链平台。第三，尽管我们的系统不依赖于关系数据库管理系统（RDBMS），但仍将其视为一个重要组成部分，因为RDBMS在过去几十年中取得了巨大的成功。最后，我们定义了一个小型基准测试，以评估区块链数据库的性能。大量实验表明我们提出的系统在有效性和效率上均表现优异。

## 关键词

+ 区块链数据库
+ 关系数据语义
+ SQL查询接口
+ 链上链下数据
+ 可用性与可扩展性
+ 去中心化数据库