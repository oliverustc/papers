---
title: "When query authentication meets fine-grained access control: A zero-knowledge approach"
标题简称:
论文类型: conference
会议简称: SIGMOD
发表年份: 2018
modified: 2025-04-11 14:03:02
---

## When query authentication meets fine-grained access control: A zero-knowledge approach

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3183713.3183741)

## 作者

+ [Cheng Xu](Cheng%20Xu.md)
+ [Jianliang Xu](Jianliang%20Xu.md)
+ Haibo Hu 
+ [Man Ho Au](Man%20Ho%20Au.md)
## 笔记

Query authentication has been extensively studied to ensure the integrity of query results for outsourced databases, which are often not fully trusted. However, access control, another important security concern, is largely ignored by existing works. Notably, recent breakthroughs in cryptography have enabled fine-grained access control over outsourced data. In this paper, we take the first step toward studying the problem of authenticating relational queries with fine-grained access control. The key challenge is how to protect information confidentiality during query authentication, which is essential to many critical applications. To address this challenge, we propose a novel access-policy-preserving (APP) signature as the primitive authenticated data structure. A useful property of the APP signature is that it can be used to derive customized signatures for unauthorized users to prove the inaccessibility while achieving the zero-knowledge confidentiality. We also propose a grid-index-based tree structure that can aggregate APP signatures for efficient range and join query authentication. In addition to this, a number of optimization techniques are proposed to further improve the authentication performance. Security analysis and performance evaluation show that the proposed solutions and techniques are robust and efficient under various system settings.

以下是中文翻译：

查询认证已经得到了广泛研究，以确保外包数据库的查询结果的完整性，而这些数据库通常并不完全可信。然而，访问控制（access control）作为另一个重要的安全问题，在现有研究中却被大多忽视。值得注意的是，最近在密码学（cryptography）方面的突破使得对外包数据的细粒度访问控制成为可能。在本文中，我们迈出了研究具有细粒度访问控制的关系查询认证问题的第一步。关键挑战在于如何在查询认证过程中保护信息的机密性，这对许多关键应用至关重要。为了解决这一挑战，我们提出了一种新颖的访问策略保留（access-policy-preserving, APP）签名作为原始认证数据结构。APP签名的一个有用特性是，它可以用于为未授权用户推导定制签名，以证明其不可访问性，同时实现零知识机密性（zero-knowledge confidentiality）。我们还提出了一种基于网格索引的树结构，可以聚合APP签名，以高效地进行范围和连接查询认证。此外，我们还提出了一些优化技术，以进一步提高认证性能。安全分析和性能评估表明，所提出的解决方案和技术在各种系统设置下都是稳健且高效的。

## 关键词

+ 查询认证细粒度访问控制
+ 访问策略保留签名
+ 零知识机密性
+ 外包数据库完整性
+ 网格索引认证数据结构
+ 范围查询连接查询认证