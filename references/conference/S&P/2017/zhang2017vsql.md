---
title: "vSQL: Verifying arbitrary SQL queries over dynamic outsourced databases"
标题简称:
论文类型: conference
会议简称: S&P
发表年份: 2017
---

## VSQL: Verifying arbitrary SQL queries over dynamic outsourced databases

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/7958614)

## 作者

+ [Yupeng Zhang](Yupeng%20Zhang.md) 
+ Daniel Genkin 
+ [Jonathan Katz](Jonathan%20Katz.md) 
+ [Dimitrios Papadopoulos](Dimitrios%20Papadopoulos.md) 
+ [Charalampos Papamanthou](Charalampos%20Papamanthou.md) 


## 笔记

Cloud database systems such as Amazon RDS or Google Cloud SQLenable the outsourcing of a large database to a server who then responds to SQL queries. A natural problem here is to efficiently verify the correctness of responses returned by the (untrusted) server. In this paper we present vSQL, a novel cryptographic protocol for publicly verifiable SQL queries on dynamic databases. At a high level, our construction relies on two extensions of the CMT interactive-proof protocol [Cormode et al., 2012]: (i) supporting outsourced input via the use of a polynomial-delegation protocol with succinct proofs, and (ii) supporting auxiliary input (i.e., non-deterministic computation) efficiently. Compared to previous verifiable-computation systems based on interactive proofs, our construction has verification cost polylogarithmic in the auxiliary input (which for SQL queries can be as large as the database) rather than linear. In order to evaluate the performance and expressiveness of our scheme, we tested it on SQL queries based on the TPC-H benchmark on a database with 6 million rows and 13 columns. The server overhead in our scheme (which is typically the main bottleneck) is up to 120 times lower than previousapproaches based on succinct arguments of knowledge (SNARKs), and moreover we avoid the need for query-dependent pre-processing which is required by optimized SNARK-based schemes. In our construction, the server/client time and the communication cost are comparable to, and sometimessmaller than, those of existing customized solutions which only support specific queries.


以下是中文翻译：

云数据库系统（如 Amazon RDS 或 Google Cloud SQL）使得将大型数据库外包给服务器成为可能，服务器随后响应 SQL 查询。这里的一个自然问题是如何高效验证（不可信）服务器返回响应的正确性。在本文中，我们提出了 vSQL，这是一种针对动态数据库上可公开验证 SQL 查询的新型密码学协议（cryptographic protocol）。在高层次上，我们的构造依赖于 CMT 交互证明协议（interactive-proof protocol）[Cormode et al., 2012]的两个扩展：(i) 通过使用具有简洁证明的多项式委托协议（polynomial-delegation protocol with succinct proofs）来支持外包输入，以及 (ii) 高效支持辅助输入（auxiliary input）（即非确定性计算）。

与之前基于交互证明的可验证计算系统相比，我们的构造在辅助输入方面具有多项对数级（polylogarithmic）的验证成本（对于 SQL 查询，辅助输入可能与数据库一样大），而不是线性成本。为了评估我们方案的性能和表达能力，我们在一个拥有 600 万行和 13 列的数据库上使用基于 TPC-H 基准测试的 SQL 查询对其进行了测试。

我们方案中的服务器开销（通常是主要瓶颈）比之前基于简洁知识论证（succinct arguments of knowledge, SNARKs）的方法低多达 120 倍，而且我们避免了优化的基于 SNARK 方案所需的查询相关预处理需求。在我们的构造中，服务器/客户端时间和通信成本与现有仅支持特定查询的定制化解决方案相当，有时甚至更小。

## 关键词

+ 可验证SQL查询
+ 交互证明协议
+ 云数据库验证
+ 多项式委托协议
+ 动态数据库
+ CMT协议扩展