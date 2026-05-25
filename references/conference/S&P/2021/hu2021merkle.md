---
title: "Merkle^2 : A low-latency transparency log system"
标题简称: 
论文类型: conference
会议简称: S&P
发表年份: 2021
created: 2025-04-27 08:58:18
modified: 2025-04-27 09:20:14
---

## Merkle^2 : A low-latency transparency log system

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/9519459)

## 作者

+ [Yuncong Hu](Yuncong%20Hu.md) 
+ Kian Hooshmand 
+ Harika Kalidhindi 
+ Seung Jin Yang 
+ [Raluca Ada Popa](Raluca%20Ada%20Popa.md)

## 笔记

Transparency logs are designed to help users audit untrusted servers. For example, Certificate Transparency (CT) enables users to detect when a compromised Certificate Authority (CA) has issued a fake certificate. Practical state-of-the-art transparency log systems, however, suffer from high monitoring costs when used for low-latency applications. To reduce monitoring costs, such systems often require users to wait an hour or more for their updates to take effect, inhibiting low-latency applications. We propose $Merkle^2$, a transparency log system that supports both efficient monitoring and low-latency updates. To achieve this goal, we construct a new multi-dimensional, authenticated data structure that nests two types of Merkle trees, hence the name of our system, $Merkle^2$. Using this data structure, we then design a transparency log system with efficient monitoring and lookup protocols that enables low-latency updates. In particular, all the operations in $Merkle^2$ are independent of update intervals and are (poly)logarithmic to the number of entries in the log. $Merkle^2$ not only has excellent asymptotics when compared to prior work, but is also efficient in practice. Our evaluation shows that $Merkle^2$ propagates updates in as little as 1 second and can support $100 \times$ more users than state-of-the-art transparency logs.

以下是中文翻译：

透明度日志系统旨在帮助用户对不受信任的服务器进行审计。例如，证书透明度(Certificate Transparency, CT)使用户能够检测出当受损的证书颁发机构(Certificate Authority, CA)发布虚假证书的情况。然而，当前最先进的实用透明度日志系统在用于低延迟应用时会产生高昂的监控成本。为了降低监控成本，这些系统通常要求用户等待一小时或更长时间才能使其更新生效，这限制了低延迟应用的使用。

我们提出了$Merkle^2$，这是一个同时支持高效监控和低延迟更新的透明度日志系统。为实现这一目标，我们构建了一个新的多维认证数据结构，该结构嵌套了两种默克尔树(Merkle trees)，这也是我们的系统名称$Merkle^2$的由来。基于这一数据结构，我们设计了一个具有高效监控和查找协议的透明度日志系统，使其能够实现低延迟更新。特别是，$Merkle^2$中的所有操作都独立于更新间隔，并且相对于日志条目数量而言仅需要（多项式）对数时间。

$Merkle^2$不仅在与现有工作相比时具有出色的渐近性能，而且在实践中也非常高效。我们的评估表明，$Merkle^2$能够在短至1秒内传播更新，并且与最先进的透明度日志相比可以支持多100倍的用户数量。

## 关键词

+ 透明度日志
+ 证书透明度
+ 多维认证数据结构
+ 低延迟更新
+ Merkle树
+ 可审计服务器