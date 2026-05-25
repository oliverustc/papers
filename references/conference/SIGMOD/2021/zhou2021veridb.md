---
title: "Veridb: An sgx-based verifiable database"
标题简称:
论文类型: conference
会议简称: SIGMOD
发表年份: 2021
modified: 2025-04-11 11:29:50
---

## Veridb: An sgx-based verifiable database

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3448016.3457308)

## 作者

+ Wenchao Zhou 
+ Yifan Cai 
+ Yanqing Peng 
+ Sheng Wang 
+ Ke Ma 
+ Feifei Li 

## 笔记

The emergence of trusted hardwares (such as Intel SGX) provides a new avenue towards verifiable database. Such trust hardwares act as an additional trust anchor, allowing great simplification and, in turn, performance improvement in the design of verifiable databases. In this paper, we introduce the design and implementation of VeriDB, an SGX-based verifiable database that supports relational tables, multiple access methods and general SQL queries. Built on top of write-read consistent memory, VeriDB provides verifiable page-structured storage, where results of storage operations can be efficiently verified with low, constant overhead. VeriDB further provides verifiable query execution that supports general SQL queries. Through a series of evaluation using practical workload, we demonstrate that VeriDB incurs low overhead for achieving verifiability: an overhead of 1-2 microseconds for read/write operations, and a 9% - 39% overhead for representative analytical workloads.

以下是中文翻译：

可信硬件（例如 Intel SGX）的出现为可验证数据库提供了新的途径。这些可信硬件作为额外的信任锚，使得可验证数据库的设计大大简化，从而提高了性能。本文介绍了 VeriDB 的设计与实现，这是一个基于 SGX 的可验证数据库，支持关系表、多种访问方法和通用 SQL 查询。VeriDB 构建在写读一致的内存之上，提供可验证的页面结构存储，其中存储操作的结果可以以低且恒定的开销高效验证。VeriDB 进一步提供可验证的查询执行，支持通用 SQL 查询。通过一系列使用实际工作负载的评估，我们证明 VeriDB 在实现可验证性方面的开销很低：读/写操作的开销为 1-2 微秒，而代表性的分析工作负载的开销为 9% - 39%。

## 关键词

+ Intel SGX可信执行环境
+ 可验证数据库VeriDB
+ 页面结构存储验证
+ SQL查询可验证执行
+ 关系数据库完整性
+ 硬件信任锚