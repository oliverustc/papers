---
title: "vchain: Enabling verifiable boolean range queries over blockchain databases"
标题简称:
论文类型: conference
会议简称: SIGMOD
发表年份: 2019
modified: 2025-04-17 13:45:35
created: 2025-04-11 11:03:17
---

## vchain: Enabling verifiable boolean range queries over blockchain databases

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3299869.3300083)

## 作者

+ [Cheng Xu](Cheng%20Xu.md)
+ Ce Zhang 
+ [Jianliang Xu](Jianliang%20Xu.md)
## 笔记

Blockchains have recently been under the spotlight due to the boom of cryptocurrencies and decentralized applications. There is an increasing demand for querying the data stored in a blockchain database. To ensure query integrity, the user can maintain the entire blockchain database and query the data locally. However, this approach is not economic, if not infeasible, because of the blockchain's huge data size and considerable maintenance costs. In this paper, we take the first step toward investigating the problem of verifiable query processing over blockchain databases. We propose a novel framework, called vChain, that alleviates the storage and computing costs of the user and employs verifiable queries to guarantee the results' integrity. To support verifiable Boolean range queries, we propose an accumulator-based authenticated data structure that enables dynamic aggregation over arbitrary query attributes. Two new indexes are further developed to aggregate intra-block and inter-block data records for efficient query verification. We also propose an inverted prefix tree structure to accelerate the processing of a large number of subscription queries simultaneously. Security analysis and empirical study validate the robustness and practicality of the proposed techniques.

以下是中文翻译：

区块链由于加密货币和去中心化应用的兴起而备受关注。对存储在区块链数据库中的数据进行查询的需求日益增长。为了确保查询的完整性，用户可以维护整个区块链数据库并在本地查询数据。然而，由于区块链庞大的数据规模和可观的维护成本，这种方法在经济上不可行。本文的首要任务是探讨区块链数据库上可验证查询处理的问题。我们提出了一个新颖的框架，称为vChain，该框架减轻了用户的存储和计算成本，并采用可验证查询来保证结果的完整性。为了支持可验证的布尔范围查询，我们提出了一种基于累加器的认证数据结构，该结构能够在任意查询属性上进行动态聚合。进一步开发了两个新索引，以聚合块内和块间的数据记录，从而实现高效的查询验证。我们还提出了一种倒排前缀树结构，以加速同时处理大量订阅查询的过程。安全分析和实证研究验证了所提技术的稳健性和实用性。

## 关键词

+ 区块链可验证布尔范围查询
+ 累加器认证数据结构
+ 动态聚合查询属性
+ 倒排前缀树订阅查询
+ 区块链数据库完整性
+ vChain框架