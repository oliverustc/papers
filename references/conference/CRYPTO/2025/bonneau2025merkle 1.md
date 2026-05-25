---
title: "Merkle Mountain Ranges are Optimal: On witness update frequency for cryptographic accumulators"
标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 2025
---

## Merkle Mountain Ranges are Optimal: On witness update frequency for cryptographic accumulators

## 发表信息

+ [原文链接]()

## 作者

+ [Joseph Bonneau](Joseph%20Bonneau.md) 
+ [Jessica Chen](Jessica%20Chen.md)
+ [Miranda Christ](Miranda%20Christ.md)
+ [Ioanna Karantaidou](Ioanna%20Karantaidou.md)
## 笔记

We study append-only set commitments with efficient updates and inclusion proofs, or cryptographic _accumulators_. In particular, we examine how often the inclusion proofs (or _witnesses_) for individual items must change as new items are added to the accumulated set. Using a compression argument, we show unconditionally that to accumulate a set of _n_ items, any construction with a succinct accumulator value ($O(\lambda \  \mathsf{polylog} \  n)$  storage) must induce at least $\omega(n)$  total witness updates as _n_ items are sequentially added. In a certain regime, we strengthen this bound to $\Omega(n\log n/\log\log n)$  total witness updates. These lower bounds hold not just in the worst case, but with overwhelming probability over a random choice of the accumulated set. Our results show that a close variant of the Merkle Mountain range, an elegant construction that has become popular in practice, is essentially optimal.

以下是中文翻译：

我们研究具有高效更新和包含证明（inclusion proofs）的仅追加集合承诺（append-only set commitments），亦即密码学**累加器**（cryptographic accumulators）。特别地，我们考察在向被累加集合中逐个添加新元素时，针对各个元素的包含证明（或称**见证**（witnesses））必须更新的频率。

利用压缩论证（compression argument），我们无条件地证明：对于累积包含 _n_ 个元素的集合，任何具有简洁累加器值（即存储开销为 $O(\lambda \, \mathsf{polylog} \, n)$）的构造，在依次添加 _n_ 个元素的过程中，其见证总更新次数至少为 $\omega(n)$。在特定参数范围内，我们将该下界进一步加强至 $\Omega(n\log n/\log\log n)$ 次总见证更新。这些下界不仅适用于最坏情况，而且对于被累加集合的随机选取，以压倒性概率（overwhelming probability）成立。

我们的结果表明，Merkle Mountain Range（MMR）的一个紧密变体——一种在实践中广受欢迎的优雅构造——在上述意义下本质上是最优的。

## 关键词

+ 密码学累加器
+ 见证更新下界
+ Merkle Mountain Range
+ 压缩论证
+ 仅追加集合承诺