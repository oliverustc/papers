---
title: "Zexe: Enabling decentralized private computation"
标题简称:
论文类型: conference
会议简称: S&P
发表年份: 2020
---

## Zexe: Enabling decentralized private computation

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/9152634)

## 作者

+ [Sean Bowe](Sean%20Bowe.md)
+ [Alessandro Chiesa](Alessandro%20Chiesa.md)
+ [Matthew Green](Matthew%20Green.md)
+ [Ian Miers](Ian%20Miers.md)
+ [Pratyush Mishra](Pratyush%20Mishra.md)
+ Howard Wu 


## 笔记

Ledger-based systems that support rich applications often suffer from two limitations. First, validating a transaction requires re-executing the state transition that it attests to. Second, transactions not only reveal which application had a state transition but also reveal the application's internal state. We design, implement, and evaluate ZEXE, a ledger-based system where users can execute offline computations and subsequently produce transactions, attesting to the correctness of these computations, that satisfy two main properties. First, transactions hide all information about the offline computations. Second, transactions can be validated in constant time by anyone, regardless of the offline computation. The core of ZEXE is a construction for a new cryptographic primitive that we introduce, decentralized private computation (DPC) schemes. In order to achieve an efficient implementation of our construction, we leverage tools in the area of cryptographic proofs, including succinct zero knowledge proofs and recursive proof composition. Overall, transactions in ZEXE are 968 bytes regardless of the offline computation, and generating them takes less than 1 min plus a time that grows with the offline computation. We demonstrate how to use ZEXE to realize privacy-preserving analogues of popular applications: private user-defined assets and private decentralized exchanges for these assets.


以下是中文翻译：

支持丰富应用的账本型系统（ledger-based systems）通常面临两个局限性。首先，验证一笔交易需要重新执行其所证明的状态转换（state transition）。其次，交易不仅会暴露发生状态转换的应用程序，还会泄露该应用程序的内部状态。

我们设计、实现并评估了 ZEXE——一种基于账本的系统，用户可在离线状态下执行计算，并随后生成交易以证明这些计算的正确性，且该交易满足两个核心特性：第一，交易完全隐藏离线计算的所有信息；第二，任何人均可在常数时间内验证交易，无论其对应的离线计算复杂度如何。

ZEXE 的核心是一种我们新提出的密码学原语构造：去中心化私有计算（Decentralized Private Computation, DPC）方案。为实现该构造的高效实例化，我们利用了密码学证明领域的多种工具，包括简洁零知识证明（succinct zero-knowledge proofs）和递归证明组合（recursive proof composition）。总体而言，ZEXE 中的交易大小恒为 968 字节，与离线计算的复杂度无关；生成交易所需时间少于 1 分钟，外加一个随离线计算规模线性增长的部分。

我们展示了如何利用 ZEXE 实现流行应用的隐私保护版本：私有用户自定义资产（private user-defined assets）以及针对这些资产的私有去中心化交易所（private decentralized exchanges）。

## 关键词

+ 去中心化私有计算（DPC）
+ 简洁零知识证明
+ 隐私保护智能合约
+ 递归证明组合
+ 恒定大小交易
+ 账本型系统