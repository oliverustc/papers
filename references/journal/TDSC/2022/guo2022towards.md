---
title: "Towards public verifiable and forward-privacy encrypted search by using blockchain"
doi: 10.1109/tdsc.2022.3173291
标题简称:
论文类型: journal
期刊简称: TDSC
发表年份: 2022
created: 2025-04-19 16:22:13
modified: 2025-04-19 16:23:29
---
## Towards public verifiable and forward-privacy encrypted search by using blockchain

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/9772317)

## 作者

+ [Yu Guo](Yu%20Guo.md)
+ Chen Zhang 
+ Cong Wang 
+ Xiaohua Jia 

## 笔记

Dynamic Searchable Symmetric Encryption (DSSE) is a practical cryptographic primitive that assists servers to provide search and update functionalities in the ciphertext domain. Recent work on DSSE schemes has focused on the direction of forward-privacy, requiring that newly added files cannot be linked to previously query results. However, due to the complexity of forward-privacy updates, existing schemes can only address an honest-but-curious server. It is difficult to verify updated results while preserving forward-privacy. In this paper, we explore how blockchain techniques can help us achieve a verifiable and forward-privacy DSSE scheme. Our scheme resorts to the emerging smart contract as a trusted platform to store digests for public result verification, and carefully crafts dynamic query protocols to enable encrypted search with forward-privacy. In our design, indexes are collocated with encrypted files and stored at storage-servers, which makes the blockchain light-weighted and search operations more efficient. Moreover, we propose a hybrid index design to support efficient files deletion. By using our blockchain-assisted primitive, the property collision between dynamic result verification and forward-privacy can be solved. We formally analyze the security strengths and provide the prototype implementation on Ethereum. Experiment results demonstrate the feasibility and usability of our blockchain-assisted DSSE scheme.

以下是中文翻译：

动态可搜索对称加密（Dynamic Searchable Symmetric Encryption, DSSE）是一种实用的密码学原语，帮助服务器在密文域中提供搜索和更新功能。近期关于DSSE方案的研究主要集中在前向隐私（forward-privacy）方向，要求新添加的文件不能与先前的查询结果关联。然而，由于前向隐私更新的复杂性，现有方案只能应对诚实但好奇的服务器（honest-but-curious server）。在保持前向隐私的同时，验证更新结果变得困难。本文探讨区块链技术如何帮助我们实现可验证的前向隐私DSSE方案。我们的方案利用新兴的智能合约作为可信平台来存储用于公共结果验证的摘要，并精心设计动态查询协议，以实现具有前向隐私的加密搜索。在我们的设计中，索引与加密文件共同存放在存储服务器上，这使得区块链轻量化，并提高了搜索操作的效率。此外，我们提出了一种混合索引设计，以支持高效的文件删除。通过使用我们的区块链辅助原语，动态结果验证与前向隐私之间的属性冲突得以解决。我们对安全性进行了正式分析，并在以太坊（Ethereum）上提供了原型实现。实验结果证明了我们区块链辅助DSSE方案的可行性和可用性。

## 关键词

+ 动态可搜索对称加密DSSE
+ 前向隐私加密搜索
+ 区块链辅助结果验证
+ 智能合约可信平台
+ 公共结果可验证性
+ 混合索引文件删除支持