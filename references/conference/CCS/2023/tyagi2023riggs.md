---
title: "Riggs: Decentralized sealed-bid auctions"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2023
created: 2025-04-16 10:54:35
modified: 2025-04-16 10:55:19
---

## Riggs: Decentralized sealed-bid auctions

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3576915.3623182)

## 作者

+ [Nirvan Tyagi](Nirvan Tyagi.md) 
+ [Arasu Arun](Arasu%20Arun.md)
+ Cody Freitag 
+ [Riad Wahby](Riad%20Wahby.md)
+ [Joseph Bonneau](Joseph Bonneau.md) 
+ David Mazières 

## 笔记

We introduce the first practical protocols for fully decentralized sealed-bid auctions using timed commitments. Timed commitments ensure that the auction is finalized fairly even if all participants drop out after posting bids or if n bidders collude to try to learn the nth bidder's bid value. Our protocols rely on a novel non-malleable timed commitment scheme which efficiently supports range proofs to establish that bidders have sufficient funds to cover a hidden bid value. This allows us to penalize users who abandon bids for exactly the bid value, while supporting simultaneous bidding in multiple auctions with a shared collateral pool. Our protocols are concretely efficient and we have implemented them in an Ethereum-compatible smart contract which automatically enforces payment and delivery of an auctioned digital asset.

以下是中文翻译：

我们介绍了首个使用定时承诺的实用性全去中心化密封竞价拍卖协议。定时承诺确保即使所有参与者在提交出价后退出，或者n个竞标者串通试图获知第n个竞标者的出价，拍卖也能公平完成。我们的协议依赖于一种新型的不可篡改的定时承诺方案，该方案能够高效支持范围证明，以证实竞标者有足够的资金支付隐藏的竞标金额。这使我们能够对放弃竞标的用户处以与竞标金额相当的惩罚，同时支持用户使用共享保证金池在多个拍卖中同时竞标。我们的协议具有具体的实用性，我们已经将其实现在一个以太坊兼容的智能合约中，该合约可以自动执行支付并交付拍卖的数字资产。

## 关键词

+ 密封竞价拍卖
+ 定时承诺
+ 去中心化
+ 智能合约
+ 范围证明
+ 以太坊