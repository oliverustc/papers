---
title: "Fairswap: How to fairly exchange digital goods"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2018
---

## Fairswap: How to fairly exchange digital goods

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3243734.3243857)

## 作者

+ Stefan Dziembowski 
+ Lisa Eckey 
+ Sebastian Faust 


## 笔记

We introduce FairSwap -- an efficient protocol for fair exchange of digital goods using smart contracts. A fair exchange protocol allows a sender S to sell a digital commodity x for a fixed price p to a receiver R. The protocol is said to be secure if R only pays if he receives the correct x. Our solution guarantees fairness by relying on smart contracts executed over decentralized cryptocurrencies, where the contract takes the role of an external judge that completes the exchange in case of disagreement. While in the past there have been several proposals for building fair exchange protocols over cryptocurrencies, our solution has two distinctive features that makes it particular attractive when users deal with large commodities. These advantages are: (1) minimizing the cost for running the smart contract on the blockchain, and (2) avoiding expensive cryptographic tools such as zero-knowledge proofs. In addition to our new protocols, we provide formal security definitions for smart contract based fair exchange, and prove security of our construction. Finally, we illustrate several applications of our basic protocol and evaluate practicality of our approach via a prototype implementation for fairly selling large files over the cryptocurrency Ethereum.

以下是中文翻译：

我们提出 FairSwap——一种利用智能合约（smart contracts）实现数字商品公平交换的高效协议。公平交换协议允许发送方 S 以固定价格 p 向接收方 R 出售数字商品 x。该协议被称为安全的，当且仅当 R 仅在接收到正确的 x 时才支付款项。我们的方案通过依赖在去中心化加密货币（decentralized cryptocurrencies）上执行的智能合约来保障公平性，其中智能合约充当外部仲裁者（external judge），在双方发生争议时完成交换。

尽管过去已有多种基于加密货币构建公平交换协议的提案，但我们的方案具备两个显著特性，使其在用户处理大规模数字商品时尤为适用：（1）最小化在区块链上运行智能合约的成本；（2）避免使用零知识证明（zero-knowledge proofs）等昂贵的密码学工具。

除提出新协议外，我们还为基于智能合约的公平交换提供了形式化的安全性定义，并证明了所构建方案的安全性。最后，我们展示了该基础协议的若干应用场景，并通过在以太坊（Ethereum）加密货币平台上实现原型系统，对大规模文件公平销售的实用性进行了评估。

## 关键词

+ 公平交换
+ 智能合约
+ 区块链
+ 数字商品
+ 成本优化