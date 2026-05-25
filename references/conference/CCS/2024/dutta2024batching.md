---
title: "Batching-efficient ram using updatable lookup arguments"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2024
modified: 2025-04-22 15:50:48
created: 2025-04-13 17:07:04
---

## Batching-efficient ram using updatable lookup arguments

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3658644.3670356)

## 作者

+ Moumita Dutta 
+ [Chaya Ganesh](Chaya%20Ganesh.md)
+ Sikhar Patranabis 
+ Shubh Prakash 
+ Nitin Singh 

## 笔记

RAM (random access memory) is an important primitive in verifiable computation. In this paper, we focus on realizing RAM with efficient batching property, i.e, proving a batch of _m_ updates on a RAM of size N while incurring a cost that is sublinear in N. Classical approaches based on Merkle-trees or address ordered transcripts to model RAM correctness are either concretely inefficient, or incur linear overhead in the size of the RAM. Recent works explore cryptographic accumulators based on unknown-order groups (RSA, class-groups) to model the RAM state. While recent RSA accumulator based approaches offer significant improvement over classical methods, they incur linear overhead in the size of the accumulated set to compute witnesses, as well as prohibitive constant overheads.

We realize a batching-efficient RAM with superior asymptotic and concrete costs as compared to existing approaches. Towards this: (i) we build on recent constructions of lookup arguments to allow efficient lookups even in presence of table _updates_, and (ii) we realize a variant of sub-vector relation addressed in prior works, which we call _committed index lookup_. We combine the two building blocks to realize batching-efficient RAM with sublinear dependence on size of the RAM. Our construction incurs an amortized proving cost of ~O(m log m + √(mN)) for a batch of m updates on a RAM of size _N_. Our results also benefit the recent arguments for sub-vector relation, by enabling them to be efficient in presence of updates to the table. We believe that this is a contribution of independent interest.

We implement our solution to evaluate its concrete efficiency. Our experiments show that it offers significant improvement over existing works on batching-efficient accumulators/RAMs, with a substantially reduced resource barrier.

以下是中文翻译：

RAM（随机存取存储器）是验证计算中的一个重要基础组件。本文聚焦于实现具备高效批处理特性的RAM，即在大小为N的RAM上证明一批m次更新时，所需成本低于N的线性增长。传统方法依赖Merkle树或地址有序记录来模拟RAM的正确性，但这些方法要么实际效率低下，要么在RAM规模上产生线性开销。近期研究探索了基于未知阶群（如RSA、类群）的加密累加器来模拟RAM状态。尽管基于RSA累加器的最新方法较传统手段有显著改进，但在计算见证时仍面临累加集大小的线性开销及难以承受的常数因子开销问题。

We realize a batching-efficient RAM with superior asymptotic and concrete costs as compared to existing approaches. Towards this: (i) we build on recent constructions of lookup arguments to allow efficient lookups even in presence of table _updates_, and (ii) we realize a variant of sub-vector relation addressed in prior works, which we call _committed index lookup_. We combine the two building blocks to realize batching-efficient RAM with sublinear dependence on size of the RAM. Our construction incurs an amortized proving cost of ~O(m log m + √(mN)) for a batch of m updates on a RAM of size _N_. Our results also benefit the recent arguments for sub-vector relation, by enabling them to be efficient in presence of updates to the table. We believe that this is a contribution of independent interest.  
我们实现了一种批处理高效的随机存取存储器（RAM），其渐近成本和实际成本均优于现有方法。为此：（i）我们基于最新的查找论证构造，即使在表更新的情况下也能实现高效查找；（ii）我们实现了先前工作中提到的子向量关系的一种变体，称之为承诺索引查找。通过结合这两个基础模块，我们实现了对RAM大小具有亚线性依赖的批处理高效RAM。对于大小为N的RAM上的一批m次更新，我们的构造分摊证明成本约为~O(m log m + √(mN))。我们的成果还优化了近期关于子向量关系的论证，使其在表更新的情况下仍保持高效。我们认为这是一项具有独立价值的重要贡献。

We implement our solution to evaluate its concrete efficiency. Our experiments show that it offers significant improvement over existing works on batching-efficient accumulators/RAMs, with a substantially reduced resource barrier.  
我们实施解决方案以评估其实际效率。实验结果表明，相较于现有批量高效累加器/RAM的研究成果，我们的方法在显著降低资源壁垒的同时，实现了性能上的重大提升。

## 关键词

+ 随机存取存储器
+ 批处理高效
+ 查找论证
+ 加密累加器
+ 验证计算
+ 子向量关系