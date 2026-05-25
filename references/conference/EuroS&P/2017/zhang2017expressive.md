---
title: "An expressive zero-knowledge set accumulator"
标题简称:
论文类型: conference
会议简称: EuroS&P
发表年份: 2017
modified: 2025-04-13 13:51:10
---

## An expressive zero-knowledge set accumulator

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/7961978)

## 作者

+ [Yupeng Zhang](Yupeng%20Zhang.md) 
+ [Jonathan Katz](Jonathan%20Katz.md) 
+ [Charalampos Papamanthou](Charalampos%20Papamanthou.md) 

## 笔记

We present a new construction of an expressive set accumulator. Unlike existing cryptographic accumulators, ours provides succinct proofs for a large collection of operations over accumulated sets, including intersection, union, set difference, SUM, COUNT, MIN, MAX, and RANGE, as well as arbitrary nestings of the above. We also show how to extend our accumulator to be zero-knowledge. The security of our accumulator is based on extractability assumptions and other assumptions that hold in the generic group model. Our construction has asymptotically optimal verification complexity and proof size, constant update complexity, and public verifiability/updatability-namely, any client who knows the public key and the last accumulator value can verify the supported operations and update the accumulator. The expressiveness of our accumulator comes at the cost of quadratic prover time. However, we show that the cryptographic operations involved are cheap compared to those incurred by generic approaches (e.g., SNARKs) that are equally expressive: our prover runs faster for sets of up to 5 million items. Our accumulator serves as a powerful cryptographic tool with many applications. For example, it can be applied to efficiently support verification of a rich collection of SQL queries when used as a drop-in replacement in existing verifiable database systems (e.g., IntegriDB, CCS 2015).

以下是中文翻译：

我们提出了一种新的表达能力强的集合累加器构造。与现有的密码学累加器不同，我们的累加器为一系列操作提供了简洁的证明，这些操作包括交集、并集、集合差、求和（SUM）、计数（COUNT）、最小值（MIN）、最大值（MAX）和范围（RANGE），以及上述操作的任意嵌套。我们还展示了如何将我们的累加器扩展为零知识（zero-knowledge）。我们的累加器安全性基于可提取性假设（extractability assumptions）以及在通用群模型（generic group model）中成立的其他假设。我们的构造具有渐进最优的验证复杂度和证明大小，常数更新复杂度，以及公共可验证性/可更新性——即，任何知道公钥和最后累加器值的客户端都可以验证支持的操作并更新累加器。我们累加器的表达能力是以二次证明者时间为代价的。然而，我们表明，所涉及的密码学操作与通用方法（例如，SNARKs）所产生的操作相比是便宜的，后者同样具备表达能力：我们的证明者在处理高达 500 万项的集合时运行速度更快。我们的累加器作为一种强大的密码学工具，具有广泛的应用。例如，当作为现有可验证数据库系统（如 IntegriDB，CCS 2015）的替代品使用时，它可以有效支持对丰富的 SQL 查询集合的验证。

## 关键词

+ 零知识集合累加器
+ 集合运算证明
+ 可提取性假设
+ 通用群模型
+ 可验证数据库
+ 简洁证明