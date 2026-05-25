---
title: "Poseidon: A new hash function for Zero-Knowledge proof systems"
标题简称:
论文类型: conference
会议简称: USENIX Security
发表年份: 2021
created: 2025-04-22 15:19:26
modified: 2025-04-22 15:19:53
---

## Poseidon: A new hash function for Zero-Knowledge proof systems

## 发表信息

+ [原文链接](https://www.usenix.org/conference/usenixsecurity21/presentation/grassi)

## 作者

+ [Lorenzo Grassi](Lorenzo%20Grassi.md)
+ [Dmitry Khovratovich](Dmitry%20Khovratovich.md)
+ [Christian Rechberger](Christian%20Rechberger.md)
+ [Arnab Roy](Arnab%20Roy.md)
+ Markus Schofnegger 

## 笔记

The area of practical computational integrity proof systems, like SNARKs, STARKs, Bulletproofs, is seeing a very dynamic development with several constructions having appeared recently with improved properties and relaxed setup requirements. Many use cases of such systems involve, often as their most expensive part, proving the knowledge of a preimage under a certain cryptographic hash function, which is expressed as a circuit over a large prime field. A notable example is a zero-knowledge proof of coin ownership in the Zcash cryptocurrency, where the inadequacy of the SHA-256 hash function for such a circuit caused a huge computational penalty.

In this paper, we present a modular framework and concrete instances of cryptographic hash functions which work natively with GF(p) objects. Our hash function Poseidon uses up to 8x fewer constraints per message bit than Pedersen Hash.

Our construction is not only expressed compactly as a circuit, but can also be tailored for various proof systems using specially crafted polynomials, thus bringing another boost in performance. We demonstrate this by implementing a 1-out-of-a-billion membership proof with Merkle trees in less than a second by using Bulletproofs.

以下是中文翻译：

实用计算完整性证明系统(computational integrity proof systems)领域，如SNARKs、STARKs、Bulletproofs等，正经历着非常活跃的发展，最近出现了几种具有改进性能和放宽设置要求的构造方案。这类系统的许多用例都涉及（通常作为其最耗费资源的部分）证明某个密码学哈希函数下的原像知识，这被表示为大素数域上的电路。一个典型的例子是Zcash加密货币中的零知识币权证明，其中SHA-256哈希函数在此类电路中的不适用性导致了巨大的计算损耗。

在本文中，我们提出了一个模块化框架，以及可以原生处理GF(p)对象的密码学哈希函数的具体实例。我们的哈希函数Poseidon在每个消息比特上使用的约束条件比Pedersen哈希少至8倍。

我们的构造不仅可以作为电路被紧凑地表达，还可以通过使用特别设计的多项式来适应各种证明系统，从而带来另一个性能提升。我们通过使用Bulletproofs在不到一秒的时间内实现了使用默克尔树的十亿分之一成员资格证明，来证明这一点。

## 关键词

+ Poseidon哈希函数ZKP
+ GF(p)域哈希函数
+ 算术电路约束优化
+ Merkle树成员性证明
+ SNARKs哈希原语
+ Bulletproofs高效证明
