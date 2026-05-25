---
title: "Hawk: The blockchain model of cryptography and privacy-preserving smart contracts"
标题简称:
论文类型: conference
会议简称: S&P
发表年份: 2016
---

## Hawk: The blockchain model of cryptography and privacy-preserving smart contracts

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/7546538)

## 作者

+ [Ahmed Kosba](Ahmed%20Kosba.md)
+ [Andrew Miller](Andrew%20Miller.md) 
+ [Elaine Shi](Elaine%20Shi.md)
+ Zikai Wen 
+ [Charalampos Papamanthou](Charalampos%20Papamanthou.md) 


## 笔记

Emerging smart contract systems over decentralized cryptocurrencies allow mutually distrustful parties to transact safely without trusted third parties. In the event of contractual breaches or aborts, the decentralized blockchain ensures that honest parties obtain commensurate compensation. Existing systems, however, lack transactional privacy. All transactions, including flow of money between pseudonyms and amount transacted, are exposed on the blockchain. We present Hawk, a decentralized smart contract system that does not store financial transactions in the clear on the blockchain, thus retaining transactional privacy from the public's view. A Hawk programmer can write a private smart contract in an intuitive manner without having to implement cryptography, and our compiler automatically generates an efficient cryptographic protocol where contractual parties interact with the blockchain, using cryptographic primitives such as zero-knowledge proofs. To formally define and reason about the security of our protocols, we are the first to formalize the blockchain model of cryptography. The formal modeling is of independent interest. We advocate the community to adopt such a formal model when designing applications atop decentralized blockchains.

以下是中文翻译：

新兴的去中心化加密货币（decentralized cryptocurrencies）上的智能合约（smart contract）系统，使得互不信任的各方能够在无需可信第三方（trusted third parties）的情况下安全地进行交易。一旦发生合约违约或交易中止，去中心化的区块链（blockchain）可确保诚实参与方获得相应的补偿。

然而，现有系统缺乏交易隐私性（transactional privacy）。所有交易信息，包括伪名（pseudonyms）之间的资金流向和交易金额，均以明文形式公开在区块链上。

本文提出 Hawk——一种去中心化的智能合约系统，其不会将金融交易以明文形式存储在区块链上，从而在公众视野中保留交易隐私。Hawk 程序员可以以直观的方式编写隐私保护型智能合约（private smart contract），而无需自行实现密码学机制；我们的编译器会自动生成高效的密码学协议（cryptographic protocol），使合约参与方通过零知识证明（zero-knowledge proofs）等密码学原语（cryptographic primitives）与区块链进行交互。

为形式化定义并推理我们协议的安全性，我们首次对密码学中的区块链模型（blockchain model of cryptography）进行了形式化。该形式化建模本身具有独立的研究价值。我们倡导研究社区在设计基于去中心化区块链的应用时，采纳此类形式化模型。

## 关键词

+ 隐私保护智能合约
+ 零知识证明
+ 区块链形式化模型
+ 去中心化交易隐私
+ 自动密码协议生成