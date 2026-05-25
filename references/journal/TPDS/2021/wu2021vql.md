---
title: "VQL: Efficient and verifiable cloud query services for blockchain systems"
标题简称:
论文类型: journal
期刊简称: TPDS
发表年份: 2021
modified: 2025-04-17 13:38:06
created: 2025-04-11 11:03:36
---

## VQL: Efficient and verifiable cloud query services for blockchain systems

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/9541060)

## 作者

+ Haotian Wu 
+ Zhe Peng 
+ Songtao Guo 
+ Yuanyuan Yang 
+ [Bin Xiao](Bin%20Xiao.md)
## 笔记

Despite increasingly emerging applications, a primary concern for blockchain to be fully practical is the inefficiency of data query. Direct queries on the blockchain take much time by searching every block, while indirect queries on a blockchain database greatly degrade the authenticity of query results. To conquer the authenticity problem, we propose a Verifiable Query Layer (VQL) that can be deployed in the cloud to provide both efficient and verifiable data query services for blockchain systems. The middleware layer extracts data from the underlying blockchain system and efficiently reorganizes them in databases. To prevent falsified data from being stored in the middleware, a cryptographic fingerprint is calculated based on each constructed database. The database fingerprint will be first verified by miners and then written into the blockchain. Moreover, public users can verify the entire databases or several databases that interest them in the middleware layer. We implement VQL together with the verification schemes and conduct extensive experiments based on a practical blockchain system. The evaluation results demonstrate that VQL can efficiently support various data query services and guarantee the authenticity of query results for blockchain systems.

以下是中文翻译：

尽管区块链的应用日益增多，但其全面实用的主要问题仍然是数据查询的低效性。直接在区块链上进行查询需要花费大量时间逐个搜索每个区块，而在区块链数据库上进行间接查询则会严重降低查询结果的真实性。为了解决真实性问题，我们提出了一种可验证查询层（Verifiable Query Layer, VQL），该层可以在云端部署，为区块链系统提供高效且可验证的数据查询服务。中间件层从底层区块链系统中提取数据，并高效地将其在数据库中重新组织。为了防止伪造数据存储在中间件中，我们基于每个构建的数据库计算一个密码学指纹（cryptographic fingerprint）。数据库指纹将首先由矿工进行验证，然后写入区块链。此外，公共用户可以在中间件层验证整个数据库或他们感兴趣的若干个数据库。我们实现了VQL及其验证方案，并基于一个实际的区块链系统进行了广泛的实验。评估结果表明，VQL能够高效支持各种数据查询服务，并确保区块链系统查询结果的真实性。

## 关键词

+ VQL可验证区块链查询层
+ 密码学指纹数据库完整性
+ 云端区块链查询服务
+ 中间件层数据重组验证
+ 区块链查询结果真实性保证
+ 矿工验证数据库指纹上链