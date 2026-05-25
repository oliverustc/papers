---
title: "Taking authenticated range queries to arbitrary dimensions"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2014
---

## Taking authenticated range queries to arbitrary dimensions

## 发表信息

+ [原文链接]()

## 作者

+ [Dimitrios Papadopoulos](Dimitrios%20Papadopoulos.md) 
+ Stavros Papadopoulos 
+ [Nikos Triandopoulos](Nikos%20Triandopoulos.md)
## 笔记


We study the problem of authenticated multi-dimensional range queries over outsourced databases, where an owner outsources its database to an untrusted server, which maintains it and answers queries to clients. Previous schemes either scale exponentially in the number of query dimensions, or rely on heuristic data structures without provable bounds. Most importantly, existing work requires an exponential, in the database attributes, number of structures to support queries on every possible combination of dimensions in the database. In this paper, we propose the first schemes that (i) scale linearly with the number of dimensions, and (ii) support queries on any set of dimensions with linear in the number of attributes setup cost and storage. We achieve this through an elaborate fusion of novel and existing set-operation sub-protocols. We prove the security of our solutions relying on the q-Strong Bilinear Diffie-Hellman assumption, and experimentally confirm their feasibility.

## 精准翻译

以下是中文翻译：

我们研究外包数据库上认证多维范围查询 (authenticated multi-dimensional range queries) 的问题，其中数据所有者将其数据库外包给不可信服务器，由服务器维护数据库并向客户端回答查询。以往的方案要么在查询维度数量上呈指数级扩展，要么依赖于没有可证明界限的启发式数据结构。最重要的是，现有工作需要与数据库属性呈指数关系的大量结构来支持数据库中每个可能维度组合上的查询。

在本文中，我们提出了首个具有以下特性的方案：(i) 与维度数量呈线性扩展关系，以及 (ii) 支持任意维度集合上的查询，且设置成本和存储开销与属性数量呈线性关系。我们通过精心融合新颖的和现有的集合操作子协议 (set-operation sub-protocols) 来实现这一目标。我们基于 q-强双线性 Diffie-Hellman 假设 (q-Strong Bilinear Diffie-Hellman assumption) 证明了解决方案的安全性，并通过实验验证了其可行性。

## 关键词

+ 认证多维范围查询
+ 外包数据库
+ 线性扩展性
+ 集合操作
+ q-强双线性DH假设