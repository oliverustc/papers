---
title: "ServeDB: Secure, verifiable, and efficient range queries on outsourced database"
标题简称:
论文类型: conference
会议简称: ICDE
发表年份: 2019
---

## ServeDB: Secure, verifiable, and efficient range queries on outsourced database

## 发表信息

+ [原文链接]()

## 作者

+ Songrui Wu 
+ [Qi Li](Qi%20Li.md)
+ Guoliang Li 
+ Dong Yuan 
+ Xingliang Yuan 
+ Cong Wang 


## 笔记

Data outsourcing to cloud has been a common IT practice nowadays due to its significant benefits. Meanwhile, security and privacy concerns are critical obstacles to hinder the further adoption of cloud. Although data encryption can mitigate the problem, it reduces the functionality of query processing, e.g., disabling SQL queries. Several schemes have been proposed to enable one-dimensional query on encrypted data, but multi-dimensional range query has not been well addressed. In this paper, we propose a secure and scalable scheme that can support multi-dimensional range queries over encrypted data. The proposed scheme has three salient features: (1) Privacy: the server cannot learn the contents of queries and data records during query processing. (2) Efficiency: we utilize hierarchical cubes to encode multi-dimensional data records and construct a secure tree index on top of such encoding to achieve sublinear query time. (3) Verifiability: our scheme allows users to verify the correctness and completeness of the query results to address server's malicious behaviors. We perform formal security analysis and comprehensive experimental evaluations. The results on real datasets demonstrate that our scheme achieves practical performance while guaranteeing data privacy and result integrity.

以下是中文翻译：

数据外包到云端已成为当今常见的 IT 实践，因为其具有显著的优势。与此同时，安全和隐私问题是阻碍云计算进一步采用的关键障碍。尽管数据加密可以缓解这一问题，但它降低了查询处理的功能性，例如，使 SQL 查询无法执行。已有若干方案被提出以支持加密数据上的一维查询，但多维范围查询 (multi-dimensional range query) 尚未得到很好的解决。

在本文中，我们提出了一个安全且可扩展的方案，能够支持加密数据上的多维范围查询。所提出的方案具有三个显著特征：（1）隐私性：服务器在查询处理过程中无法获知查询内容和数据记录的内容。（2）效率性：我们利用分层立方体 (hierarchical cubes) 对多维数据记录进行编码，并在此类编码之上构建安全树索引 (secure tree index) 以实现亚线性查询时间 (sublinear query time)。（3）可验证性：我们的方案允许用户验证查询结果的正确性和完整性，以应对服务器的恶意行为。

我们进行了形式化安全分析和全面的实验评估。在真实数据集上的结果表明，我们的方案在保证数据隐私和结果完整性的同时实现了实用的性能。

## 关键词

+ 多维范围查询
+ 加密数据查询
+ 分层立方体编码
+ 安全树索引
+ 可验证性
+ 隐私保护