---
title: "Optiswap: Fast optimistic fair exchange"
标题简称:
论文类型: conference
会议简称: AsiaCCS
发表年份: 2020
---

## Optiswap: Fast optimistic fair exchange

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3320269.3384749)

## 作者

+ Lisa Eckey 
+ Sebastian Faust 
+ Benjamin Schlosser 


## 笔记

Selling digital commodities securely over the Internet is a challenging task when Seller and Buyer do not trust each other. With the advent of cryptocurrencies, one prominent solution for digital exchange is to rely on a smart contract as a trusted arbiter that fairly resolves disputes when Seller and Buyer disagree. Such protocols have an optimistic mode, where the digital exchange between the parties can be completed with only minimal interaction with the smart contract. In this work we present OptiSwap, a new smart contract based fair exchange protocol that significantly improves the optimistic case of smart contract based fair exchange protocols. In particular, OptiSwap has almost no overhead in communication complexity, and improves on the computational overheads of the parties compared to prior solutions. An additional feature of OptiSwap is a protection mechanism against so-called grieving attacks, where an adversary attempts to violate the financial fairness of the protocol by forcing the honest party to pay fees. We analyze OptiSwap's security in the UC model and provide benchmark results over Ethereum.

以下是中文翻译：

在卖方（Seller）与买方（Buyer）互不信任的情况下，通过互联网安全地销售数字商品（digital commodities）是一项具有挑战性的任务。随着加密货币（cryptocurrencies）的兴起，一种主流的数字交换解决方案是依赖智能合约（smart contract）作为可信仲裁者，在买卖双方发生争议时公平地解决纠纷。此类协议通常具备”乐观模式”（optimistic mode），即在理想情况下，双方仅需与智能合约进行最少的交互即可完成数字商品的交换。

在卖方（Seller）与买方（Buyer）互不信任的情况下，通过互联网安全地销售数字商品（digital commodities）是一项具有挑战性的任务。随着加密货币（cryptocurrencies）的兴起，一种主流的数字交换解决方案是依赖智能合约（smart contract）作为可信仲裁者，在买卖双方发生争议时公平地解决纠纷。此类协议通常具备“乐观模式”（optimistic mode），即在理想情况下，双方仅需与智能合约进行最少的交互即可完成数字商品的交换。

本文提出了 OptiSwap——一种基于智能合约的公平交换协议（fair exchange protocol），显著优化了现有智能合约公平交换协议在乐观情形下的性能。具体而言，OptiSwap 在通信复杂度（communication complexity）方面几乎无额外开销，并且相较于已有方案，进一步降低了参与方的计算开销（computational overheads）。此外，OptiSwap 还引入了一种防护机制，可抵御所谓的”骚扰攻击”（grieving attacks）——在此类攻击中，攻击者试图通过迫使诚实参与方支付交易费用，破坏协议的经济公平性（financial fairness）。我们在通用可组合（UC, Universal Composability）模型下对 OptiSwap 的安全性进行了形式化分析，并在以太坊（Ethereum）平台上提供了基准测试结果。

## 关键词

+ 智能合约
+ 公平交换
+ 乐观模式
+ 区块链
+ 可组合安全性
