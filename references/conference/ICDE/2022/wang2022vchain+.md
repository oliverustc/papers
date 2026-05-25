---
title: "vChain+: Optimizing verifiable blockchain boolean range queries"
标题简称:
论文类型: conference
会议简称: ICDE
发表年份: 2022
modified: 2025-04-11 11:13:43
---

## vChain+ : Optimizing verifiable blockchain boolean range queries

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/9835165/)

## 作者

+ Haixin Wang 
+ [Cheng Xu](Cheng%20Xu.md)
+ Ce Zhang 
+ [Jianliang Xu](Jianliang%20Xu.md)
+ Zhe Peng 
+ Jian Pei 

## 笔记

Blockchain has recently gained massive attention thanks to the success of cryptocurrencies and decentralized applications. With immutability and tamper-resistance features, it can be seen as a promising secure database solution. To address the need of searches over blockchain databases, prior work vChain proposed a novel verifiable processing framework that ensures query integrity without maintaining a full copy of the blockchain database. It however suffers from several limitations, including linear-scan search performance in the worst case and impractical public key management. In this paper, we propose a new searchable blockchain system, vChain+, that supports efficient verifiable boolean range queries with additional features. Specifically, we propose a sliding window accumulator index to achieve efficient query processing even for the worst case. We also design an object registration index to enable practical public key management without compromising the security guarantee. To support richer queries, we employ optimal tree-based indexes to index both keywords and numerical attributes of the data objects. Several optimizations are also proposed to further improve the query performance. Security analysis and empirical study validate the robustness and performance improvement of the proposed system. Compared with vChain, vChain+ improves the query performance by up to 913x.

以下是中文翻译：

得益于加密货币和去中心化应用的成功，区块链(Blockchain)近期获得了广泛关注。凭借其不可变性和防篡改特性，区块链可被视为一种有前景的安全数据库解决方案。为了解决在区块链数据库上进行搜索的需求，先前的研究工作vChain提出了一种新颖的可验证处理框架，该框架无需维护区块链数据库的完整副本即可确保查询完整性。然而，它存在若干局限性，包括最坏情况下的线性扫描搜索性能以及不切实际的公钥管理。在本文中，我们提出了一个新的可搜索区块链系统vChain+，该系统支持高效的可验证布尔范围查询(verifiable boolean range queries)并具有额外特性。具体而言，我们提出了一种滑动窗口累加器索引(sliding window accumulator index)，以实现即便在最坏情况下也能高效的查询处理。我们还设计了一个对象注册索引(object registration index)，在不影响安全保证的前提下实现实用的公钥管理。为支持更丰富的查询，我们采用最优树形索引来索引数据对象的关键词和数值属性。我们还提出了几项优化措施来进一步提升查询性能。安全性分析和实证研究验证了所提出系统的稳健性和性能改进。与vChain相比，vChain+将查询性能提高了最多913倍。

## 关键词

+ 可验证区块链查询
+ 布尔范围查询
+ 滑动窗口累加器索引
+ 公钥管理
+ 查询完整性
+ 区块链数据库