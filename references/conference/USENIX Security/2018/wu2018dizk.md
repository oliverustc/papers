---
title: "DIZK: A distributed zero knowledge proof system"
标题简称:
论文类型: conference
会议简称: USENIX Security
发表年份: 2018
modified: 2025-04-27 09:20:34
created: 2025-04-11 11:17:28
---

## DIZK: A distributed zero knowledge proof system

## 发表信息

+ [原文链接](https://www.usenix.org/conference/usenixsecurity18/presentation/wu)
+ [code](https://github.com/scipr-lab/dizk)

## 作者

+ Howard Wu 
+ [Wenting Zheng](Wenting%20Zheng.md)
+ [Alessandro Chiesa](Alessandro%20Chiesa.md)
+ [Raluca Ada Popa](Raluca%20Ada%20Popa.md)
+ Ion Stoica 

## 笔记

Recently there has been much academic and industrial interest in practical implementations of zero knowledge proofs. These techniques allow a party to prove to another party that a given statement is true without revealing any additional information. In a Bitcoin-like system, this allows a payer to prove validity of a payment without disclosing the payment’s details. Unfortunately, the existing systems for generating such proofs are very expensive, especially in terms of memory overhead. Worse yet, these systems are “monolithic”, so they are limited by the memory resources of a single machine. This severely limits their practical applicability. We describe DIZK, a system that distributes the generation of a zero knowledge proof across machines in a compute cluster. Using a set of new techniques, we show that DIZK scales to computations of up to billions of log- ical gates (100× larger than prior art) at a cost of 10μs per gate (100× faster than prior art). We then use DIZK to study various security applications.

以下是中文翻译：

最近，学术界和工业界对零知识证明（zero knowledge proofs）的实际应用产生了浓厚的兴趣。这些技术使得一方能够向另一方证明某个陈述是真实的，而无需透露任何额外的信息。在类似比特币的系统中，这使得付款方能够证明支付的有效性，而无需披露支付的详细信息。不幸的是，现有的生成此类证明的系统非常昂贵，尤其是在内存开销方面。更糟糕的是，这些系统是“单体式”（monolithic）的，因此受到单台机器内存资源的限制。这严重限制了它们的实际应用性。我们描述了DIZK，这是一种在计算集群中分布生成零知识证明的系统。通过一系列新技术，我们展示了DIZK能够扩展到高达数十亿个逻辑门的计算（比现有技术大100倍），每个逻辑门的成本为10微秒（比现有技术快100倍）。然后，我们使用DIZK研究各种安全应用。

**问题描述**：
在单个机器上运行zk-SNARK证明将会因电路规模的扩大而内存不足，最多支持1000-2000万个门门电路，每个门成本超过1ms
**核心思路**：
将zk-SNARK的证明过程分配到一个计算集群中，实现支持最大数十亿个门电路，每个门的成本为10微秒。

对于zk-SNARK中在素数域和椭圆曲线群上的计算，分别给出了高效的分布式实现，即有限域上的分布式快速傅里叶变换和分布式拉格朗日插值评估，有限群上的固定剂和可变基的分布式多标量乘法。

原本的zk-SNARK协议：一个具有 N 条线和 M 个门的电路被转化为 O(N) 个 O(M) 次多项式的可满足性问题。这些多项式的评估产生了大小为 O(N) × O(M) 的稀疏矩阵，只有 O(N + M) 个非零条目。在串行算法中，矩阵的稀疏性给算法设计带来了便利，但是QAP instance reduction 实例缩减依赖于它们的列稀疏性，而相应的 QAP witness reduction 见证缩减则依赖于它们的行稀疏性，但是也存在密集的部分，而密集的部分就带来了延迟问题。

随后在这些组件的基础上，构建了分布式的zk-SNARK

首先，我们进行轻量级的分布式计算，以识别并标注电路中哪些列/行是密集的。其次，我们运行一种混合分布式计算，使用不同的方法来处理稀疏和密集的列/行。总体而言，我们为这些 QAP 例程实现了高效的分布式实现。特别是，这种方法优于仅仅调用诸如 skewjoin [6] 等通用方法来纠正负载不平衡的效果。最后，我们强调，上述大部分技术工作可以作为分布许多其他类似证明系统的起点进行重用。因此，我们将这些独立的组件打包为一个单独的库，我们认为这具有独立的价值。我们还简要提到，支持十亿门电路要求我们生成并使用适合此任务的配对友好椭圆曲线。详细信息请参见 §9。

## 关键词

+ DIZK分布式零知识证明
+ 分布式快速傅里叶变换
+ 多标量乘法分布式计算
+ QAP电路可满足性
+ zk-SNARK规模化
+ 计算集群证明生成
