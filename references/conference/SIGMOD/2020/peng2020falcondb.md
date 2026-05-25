---
title: "FalconDB: Blockchain-based collaborative database"
标题简称: FalconDB
论文类型: conference
会议简称: SIGMOD
发表年份: 2020
created: 2025-04-19 11:35:44
modified: 2025-04-19 12:02:03
links: https://dl.acm.org/doi/abs/10.1145/3318464.3380594
---

## FalconDB: Blockchain-based collaborative database

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3318464.3380594)

## 作者

+ Yanqing Peng 
+ Min Du 
+ Feifei Li 
+ Raymond Cheng 
+ [Dawn Song](Dawn%20Song.md) 

## 笔记

Nowadays an emerging class of applications are based oncollaboration over a shared database among different entities. However, the existing solutions on shared database may require trust on others, have high hardware demand that is unaffordable for individual users, or have relatively low performance. In other words, there is a trilemma among security, compatibility and efficiency. In this paper, we present FalconDB, which enables different parties with limited hardware resources to efficiently and securely collaborate on a database. FalconDB adopts database servers with verification interfaces accessible to clients and stores the digests for query/update authentications on a blockchain. Using blockchain as a consensus platform and a distributed ledger, FalconDB is able to work without any trust on each other. Meanwhile, FalconDB requires only minimal storage cost on each client, and provides anywhere-available, real-time and concurrent access to the database. As a result, FalconDB over-comes the disadvantages of previous solutions, and enables individual users to participate in the collaboration with high efficiency, low storage cost and blockchain-level security guarantees.

以下是中文翻译：

如今，越来越多的应用程序基于不同实体之间对共享数据库的协作。然而，现有的共享数据库解决方案可能需要对其他方的信任，硬件需求较高，个人用户难以承受，或者性能相对较低。换句话说，在安全性、兼容性和效率之间存在一个三难困境。在本文中，我们提出了FalconDB，它使得具有有限硬件资源的不同方能够高效且安全地协作使用数据库。FalconDB采用具有验证接口的数据库服务器，客户端可以访问这些接口，并在区块链上存储用于查询/更新认证的摘要。利用区块链作为共识平台和分布式账本，FalconDB能够在各方之间无需任何信任的情况下运作。同时，FalconDB对每个客户端的存储成本要求最低，并提供随时可用、实时和并发访问数据库的能力。因此，FalconDB克服了以往解决方案的缺点，使个人用户能够以高效率、低存储成本和区块链级别的安全保障参与协作。

## 关键词

+ 区块链协作数据库
+ FalconDB可验证查询
+ 分布式账本共识
+ 无信任协作数据库
+ 轻量级客户端存储
+ 外包数据库完整性