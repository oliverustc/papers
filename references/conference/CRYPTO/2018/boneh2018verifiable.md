---
title: "Verifiable delay functions"

标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 2018
created: 2025-04-28 16:27:18
modified: 2025-04-28 16:28:03
---

## Verifiable delay functions

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-319-96884-1_25)

## 作者

+ [Dan Boneh](Dan%20Boneh.md) 
+ [Joseph Bonneau](Joseph Bonneau.md) 
+ [Benedikt Bünz](Benedikt%20Bünz.md) 
+ [Ben Fisch](Ben%20Fisch.md)
## 笔记

We study the problem of building a _verifiable delay function_ (VDF). A requires a specified number of sequential steps to evaluate, yet produces a unique output that can be efficiently and publicly verified. s have many applications in decentralized systems, including public randomness beacons, leader election in consensus protocols, and proofs of replication. We formalize the requirements for s and present new candidate constructions that are the first to achieve an exponential gap between evaluation and verification time.

以下是中文翻译：

我们研究构建可验证延迟函数(verifiable delay function, VDF)的问题。VDF需要特定数量的顺序步骤来评估，但能产生一个可以被高效且公开验证的唯一输出。VDF在去中心化系统中有许多应用，包括公共随机信标、共识协议中的领导者选举以及复制证明。我们形式化了VDF的需求，并提出了新的候选构造方案，这是首次在评估时间和验证时间之间实现指数级差距的方案。

(注：由于原文摘要仅有一段，所以译文也保持一段的形式。原文中虽然没有出现数学公式，但我已准备好按要求处理任何可能出现的数学公式，并严格保持其格式。)

## 关键词

+ 可验证延迟函数VDF形式化
+ 顺序评估公开验证唯一输出
+ 指数级评估验证时间差距
+ 去中心化随机信标领导选举
+ 复制证明VDF应用构造