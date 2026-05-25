---
title: "Zerocash: Decentralized anonymous payments from bitcoin"
标题简称:
论文类型: conference
会议简称: S&P
发表年份: 2014
created: 2025-04-21 10:23:14
modified: 2025-04-21 10:24:07
---

## Zerocash: Decentralized anonymous payments from bitcoin

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/6956581)

## 作者

+ Eli Ben Sasson 
+ [Alessandro Chiesa](Alessandro%20Chiesa.md)
+ [Christina Garman](Christina%20Garman.md)
+ [Matthew Green](Matthew%20Green.md)
+ [Ian Miers](Ian%20Miers.md)
+ [Eran Tromer](Eran%20Tromer.md) 
+ Madars Virza 

## 笔记

Bitcoin is the first digital currency to see widespread adoption. While payments are conducted between pseudonyms, Bit coin cannot offer strong privacy guarantees: payment transactions are recorded in a public decentralized ledger, from which much information can be deduced. Zero coin (Miers et al., IEEE S&P 2013) tackles some of these privacy issues by unlinking transactions from the payment's origin. Yet, it still reveals payments' destinations and amounts, and is limited in functionality. In this paper, we construct a full-fledged ledger-based digital currency with strong privacy guarantees. Our results leverage recent advances in zero-knowledge Succinct Non-interactive Arguments of Knowledge (zk-SNARKs). First, we formulate and construct decentralized anonymous payment schemes (DAP schemes). A DAP scheme enables users to directly pay each other privately: the corresponding transaction hides the payment's origin, destination, and transferred amount. We provide formal definitions and proofs of the construction's security. Second, we build Zero cash, a practical instantiation of our DAP scheme construction. In Zero cash, transactions are less than 1 kB and take under 6 ms to verify - orders of magnitude more efficient than the less-anonymous Zero coin and competitive with plain Bit coin.

以下是中文翻译：

比特币是第一个广泛采用的数字货币。尽管支付是在伪名之间进行的，但比特币无法提供强有力的隐私保障：支付交易记录在一个公共的去中心化账本中，从中可以推断出许多信息。Zero coin（Miers et al., IEEE S&P 2013）通过将交易与支付来源解耦来解决一些隐私问题。然而，它仍然暴露了支付的目的地和金额，并且功能有限。本文构建了一种具有强隐私保障的全面的基于账本的数字货币。我们的研究结果利用了在零知识简洁非交互式知识论证（zk-SNARKs）方面的最新进展。首先，我们制定并构建了去中心化匿名支付方案（DAP方案）。DAP方案使用户能够直接彼此私密支付：相应的交易隐藏了支付的来源、目的地和转账金额。我们提供了构建安全性的正式定义和证明。其次，我们构建了Zero cash，这是我们DAP方案构建的一个实用实例。在Zero cash中，交易小于1 kB，验证时间少于6毫秒——效率比不那么匿名的Zero coin高出几个数量级，并且与普通比特币相当。

## 关键词

+ Zerocash
+ 去中心化匿名支付
+ zk-SNARK
+ 隐私保护数字货币
+ 匿名交易
+ DAP方案