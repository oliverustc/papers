---
title: "Zero-knowledge accumulators and set algebra"
标题简称:
论文类型: conference
会议简称: ASIACRYPT
发表年份: 2016
modified: 2025-04-13 13:49:35
---

## Zero-knowledge accumulators and set algebra

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-662-53890-6_3)

## 作者

+ Esha Ghosh 
+ Olga Ohrimenko 
+ [Dimitrios Papadopoulos](Dimitrios%20Papadopoulos.md) 
+ Roberto Tamassia 
+ [Nikos Triandopoulos](Nikos%20Triandopoulos.md)
## 笔记

Cryptographic accumulators allow to succinctly represent a set by an accumulation value with respect to which short (non-)membership proofs about the set can be efficiently constructed and verified. Traditionally, their security captures soundness but offers no privacy: Convincing proofs reliably encode set membership, but they may well leak information about the accumulated set.

In this paper we put forward a strong privacy-preserving enhancement by introducing and devising zero-knowledge accumulators that additionally provide hiding guarantees: Accumulation values and proofs leak nothing about a dynamic set that evolves via element insertions/deletions. We formalize the new property using the standard real-ideal paradigm, namely demanding that an adaptive adversary with access to query/update oracles, cannot tell whether he interacts with honest protocol executions or a simulator fully ignorant of the set (even of the type of updates on it). We rigorously compare the new primitive to existing ones for privacy-preserving verification of set membership (or other relations) and derive interesting implications among related security definitions, showing that zero-knowledge accumulators offer stronger privacy than recent related works by Naor et al. [TCC 2015] and Derler et al. [CT-RSA 2015]. We construct the first dynamic universal zero-knowledge accumulator that we show to be perfect zero-knowledge and secure under the q-Strong Bilinear Diffie-Hellman assumption.

Finally, we extend our new privacy notion and our new construction to provide privacy-preserving proofs also for an authenticated dynamic set collection—a primitive for efficiently verifying more elaborate set operations, beyond set-membership. We introduce a primitive that supports a zero-knowledge verifiable set algebra: Succinct proofs for union, intersection and set difference queries over a dynamically evolving collection of sets can be efficiently constructed and optimally verified, while—for the first time—they leak nothing about the collection beyond the query result.

以下是中文翻译：

密码学累加器(Cryptographic accumulators)允许通过累加值简洁地表示一个集合,并且可以针对该集合高效地构造和验证简短的(非)成员资格证明。传统上,其安全性体现在可靠性方面,但不提供隐私保护:虽然令人信服的证明可靠地编码了集合成员资格,但它们可能会泄露关于累加集合的信息。

本文提出了一个强大的隐私保护增强方案,通过引入和设计零知识累加器(zero-knowledge accumulators)来提供额外的隐藏保证:累加值和证明不会泄露任何关于通过元素插入/删除而动态演化的集合的信息。我们使用标准的真实-理想范式(real-ideal paradigm)来形式化这个新特性,即要求具有查询/更新预言机访问权限的自适应对手无法判断他是在与诚实的协议执行交互,还是在与完全不知道集合信息(甚至不知道其更新类型)的模拟器交互。我们严格比较了这个新原语与现有的用于集合成员资格(或其他关系)隐私保护验证的原语,并推导出相关安全定义之间的有趣含义,表明零知识累加器提供了比Naor等人[TCC 2015]和Derler等人[CT-RSA 2015]最近相关工作更强的隐私保护。我们构造了第一个动态通用零知识累加器,证明它具有完美零知识性,并在q-强双线性Diffie-Hellman假设(q-Strong Bilinear Diffie-Hellman assumption)下是安全的。

最后,我们将新的隐私概念和构造扩展到经过认证的动态集合集(authenticated dynamic set collection)——这是一个用于高效验证更复杂集合运算的原语,超越了集合成员资格验证。我们引入了一个支持零知识可验证集合代数(zero-knowledge verifiable set algebra)的原语:可以高效构造并最优验证动态演化的集合集合上的并集、交集和差集查询的简洁证明,同时——这是首次——除了查询结果外不会泄露关于该集合集合的任何信息。

## 关键词

+ 零知识证明
+ 密码学累加器
+ 集合代数
+ 隐私保护
+ 动态验证