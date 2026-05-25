---
title: "IntegriDB: Verifiable SQL for outsourced databases"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2015
---

## IntegriDB: Verifiable SQL for outsourced databases

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/2810103.2813711)

## 作者

+ [Yupeng Zhang](Yupeng%20Zhang.md) 
+ [Jonathan Katz](Jonathan%20Katz.md) 
+ [Charalampos Papamanthou](Charalampos%20Papamanthou.md) 


## 笔记

This paper presents IntegriDB, a system allowing a data owner to outsource storage of a database to an untrusted server, and then enable anyone to perform verifiable SQL queries over that database. Our system handles a rich subset of SQL queries, including multidimensional range queries, JOIN, SUM, MAX/MIN, COUNT, and AVG, as well as (limited) nestings of such queries. Even for tables with 105 entries, IntegriDB has small proofs (a few KB) that depend only logarithmically on the size of the database, low verification time (tens of milliseconds), and feasible server computation (under a minute). Efficient updates are also supported. We prove security of IntegriDB based on known cryptographic assumptions, and demonstrate its practicality and expressiveness via performance measurements and verifiable processing of SQL queries from the TPC-H and TPC-C benchmarks.


## 精准翻译

以下是中文翻译：

本文提出了 IntegriDB 系统，该系统允许数据所有者将数据库存储外包给不可信服务器，然后使任何人都能够对该数据库执行可验证的 SQL 查询。我们的系统处理丰富的 SQL 查询子集，包括多维范围查询、JOIN 连接、SUM 求和、MAX/MIN 最大最小值、COUNT 计数和 AVG 平均值，以及此类查询的（有限）嵌套。即使对于包含 10^5 条记录的表，IntegriDB 也具有小型证明（几 KB），这些证明仅与数据库大小呈对数关系，验证时间短（数十毫秒），服务器计算可行（不到一分钟）。系统还支持高效更新。我们基于已知的密码学假设证明了 IntegriDB 的安全性，并通过性能测量和对 TPC-H 和 TPC-C 基准测试中 SQL 查询的可验证处理来展示其实用性和表达能力。

## 关键词

+ 可验证数据库
+ SQL查询验证
+ 外包数据库
+ 密码学证明
+ 对数级证明