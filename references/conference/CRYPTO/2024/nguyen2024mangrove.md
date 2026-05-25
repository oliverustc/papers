---
title: "Mangrove: A Scalable Framework for Folding-Based SNARKs"
标题简称: Mangrove
论文类型: conference
会议简称: CRYPTO
发表年份: 2024
modified: 2025-04-21 10:45:31
created: 2025-04-07 16:49:32
---

## Mangrove: A Scalable Framework for Folding-Based SNARKs

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-68403-6_10)

## 作者

+ Wilson Nguyen
+ Trisha Datta
+ [Binyi Chen](Binyi%20Chen.md)
+ [[Nirvan Tyagi]]
+ [Dan Boneh](Dan%20Boneh.md)

## 笔记

We present a framework for building efficient folding-based SNARKs. First we develop a new “uniformizing” compiler for NP statements that converts any poly-time computation to a sequence of identical simple steps. The resulting uniform computation is especially well-suited to be processed by a folding-based IVC scheme. Second, we develop two optimizations to folding-based IVC. The first reduces the recursive overhead of the IVC by restructuring the relation to which folding is applied. The second employs a “commit-and-fold” strategy to further simplify the relation. Together, these optimizations result in a folding-based SNARK that has a number of attractive features. First, the scheme uses a constant-size transparent common reference string (CRS). Second, the prover has (i) low memory footprint, (ii) makes only two passes over the data, (iii) is highly parallelizable, and (iv) is concretely efficient. Microbenchmarks indicate that proving time is competitive with leading monolithic SNARKs, and significantly faster than other streaming SNARKs. For $2^{24}$  ($2^{32}$) gates, the Mangrove prover is estimated to take 2 minutes (8 hours) with peak memory usage approximately 390 MB (800 MB) on a laptop  The full version of this work is available online at [43].).

以下是中文翻译：

我们提出了一个构建高效折叠基础 SNARK（简洁非交互式知识论证）框架。首先，我们开发了一种新的“统一化”编译器，用于 NP（非确定性多项式）语句，它将任何多项式时间计算转换为一系列相同的简单步骤。生成的统一计算特别适合通过折叠基础的 IVC（交互式验证计算）方案进行处理。其次，我们对折叠基础的 IVC 进行了两项优化。第一项优化通过重组折叠应用的关系，减少了 IVC 的递归开销。第二项优化采用了“承诺与折叠”（commit-and-fold）策略，进一步简化了关系。综合来看，这些优化使得折叠基础的 SNARK 具有若干吸引人的特性。首先，该方案使用固定大小的透明公共参考字符串（CRS）。其次，证明者具有（i）低内存占用，（ii）仅对数据进行两次遍历，（iii）高度可并行化，以及（iv）具体效率高的优点。微基准测试表明，证明时间与领先的单体 SNARK 具有竞争力，并且显著快于其他流式 SNARK。对于 $2^{24}$（$2^{32}$）个门，Mangrove 证明者在一台笔记本电脑上的估计时间为 2 分钟（8 小时），峰值内存使用约为 390 MB（800 MB）。

## 关键词

+ 折叠基础SNARK
+ 增量验证计算
+ 透明公共参考字符串
+ 流式证明
+ 统一化编译器