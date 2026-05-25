---
title: "Oblivious accumulators"
标题简称:
论文类型: conference
会议简称: PKC
发表年份: 2024
created: 2025-04-16 10:08:43
modified: 2025-04-16 10:11:47
---

## Oblivious accumulators

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-57722-2_4)

## 作者

+ [Foteini Baldimtsi](Foteini%20Baldimtsi.md)
+ [Ioanna Karantaidou](Ioanna%20Karantaidou.md)
+ Srinivasan Raghuraman 

## 笔记

A cryptographic accumulator is a succinct set commitment scheme with efficient (non-)membership proofs that typically supports updates (additions and deletions) on the accumulated set. When elements are added to or deleted from the set, an update message is issued. The collection of all the update messages essentially leaks the underlying accumulated set which in certain applications is not desirable.

In this work, we define _oblivious accumulators_, a set commitment with concise membership proofs that _hides the elements and the set size_ from every entity: an outsider, a verifier or other element holders. We formalize this notion of privacy via two properties: _element hiding_ and _add-delete indistinguishability_. We also define _almost-oblivious accumulators_, that only achieve a weaker notion of privacy called _add-delete unlinkability_. Such accumulators hide the elements but not the set size. We consider the trapdoorless, decentralized setting where different users can add and delete elements from the accumulator and compute membership proofs.

We then give a generic construction of an oblivious accumulator based on key-value commitments (KVC). We also show a generic way to construct KVCs from an accumulator and a vector commitment scheme. Finally, we give lower bounds on the communication (size of update messages) required for oblivious accumulators and almost-oblivious accumulators.

以下是中文翻译：

一种密码学累加器是一种简洁的集合承诺方案，具有高效的（非）成员证明，通常支持对累加集合的更新（添加和删除）。当元素被添加到或从集合中删除时，会发出更新消息。所有更新消息的集合实质上泄露了底层的累加集合，而在某些应用中，这种情况是不可取的。

在本研究中，我们定义了_无知累加器_，这是一种集合承诺，具有简洁的成员证明，能够_隐藏元素和集合大小_，不被任何实体所知：外部人员、验证者或其他元素持有者。我们通过两个属性来形式化这种隐私概念：_元素隐藏_和_添加-删除不可区分性_。我们还定义了_几乎无知累加器_，它仅实现一种较弱的隐私概念，称为_添加-删除不可关联性_。这种累加器隐藏元素，但不隐藏集合大小。我们考虑无陷门的去中心化环境，允许不同用户从累加器中添加和删除元素，并计算成员证明。

接着，我们给出了基于键值承诺（KVC）的无知累加器的通用构造方法。我们还展示了一种从累加器和向量承诺方案构造KVC的通用方法。最后，我们给出了对无知累加器和几乎无知累加器所需通信（更新消息的大小）的下界。

## 关键词

+ 无知累加器
+ 集合承诺
+ 元素隐藏
+ 键值承诺
+ 去中心化累加器
+ 隐私保护集合操作