---
title: "Merkle Mountain Ranges are Optimal: On witness update frequency for cryptographic accumulators"
标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 2025
created: 2025-06-10 05:30:06
modified: 2025-06-10 05:32:28
---

## Merkle Mountain Ranges are Optimal: On witness update frequency for cryptographic accumulators

## 发表信息

+ [原文链接](https://eprint.iacr.org/2025/234)

## 作者

+ [[Joseph Bonneau]]
+ [Jessica Chen](Jessica%20Chen.md)
+ [Miranda Christ](Miranda%20Christ.md)
+ [Ioanna Karantaidou](Ioanna%20Karantaidou.md)
## 笔记

We study append-only set commitments with efficient updates and inclusion proofs, or cryptographic accumulators. In particular, we examine how often the inclusion proofs (or witnesses) for individual items must change as new items are added to the accumulated set. Using a compression argument, we show unconditionally that to accumulate a set of n items, any construction with a succinct commitment (O(λ polylog n) storage) must induce at least ω(n) total witness updates as n items are sequentially added. In a certain regime, we strengthen this bound to Ω(nlog⁡n/log⁡log⁡n) total witness updates. These lower bounds hold not just in the worst case, but with overwhelming probability over a random choice of the accumulated set. Our results show that a close variant of the Merkle Mountain range, an elegant construction that has become popular in practice, is essentially optimal.

以下是中文翻译：

我们研究具有高效更新和包含证明的仅可追加集合承诺（append-only set commitments），即密码累加器（cryptographic accumulators）。具体而言，我们分析了当新元素被加入累加集合时，单个元素的包含证明（即见证值 witnesses）必须更改的频率。通过压缩论证法（compression argument），我们无条件证明：若要累加含 n 个元素的集合，任何具有简洁承诺（仅需 O(λ polylog n) 存储空间）的构造，在顺序添加 n 个元素的过程中，必然引发至少 ω(n) 次总见证值更新。在特定参数范围内，我们将此下界强化至 Ω(n log n / log log n) 次总见证值更新。这些下界不仅适用于最坏情况，且在随机选择累加集合时以压倒性概率成立。我们的结果表明，Merkle Mountain Range（一种实践中广受欢迎的优雅构造）的近似变体本质上是**最优的**。

## 关键词

+ 密码学累加器
+ 见证更新下界
+ Merkle Mountain Range最优性
+ 压缩论证
+ 仅追加集合承诺