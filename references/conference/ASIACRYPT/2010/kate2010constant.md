---
title: "Constant-size commitments to polynomials and their applications"
标题简称:
论文类型: conference
会议简称: ASIACRYPT
发表年份: 2010
modified: 2025-04-13 17:44:41
---

## Constant-size commitments to polynomials and their applications

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-642-17373-8_11)

## 作者

+ [Aniket Kate](Aniket%20Kate.md)
+ Gregory M Zaverucha 
+ Ian Goldberg 

## 笔记

We introduce and formally define polynomial commitment schemes, and provide two efficient constructions. A polynomial commitment scheme allows a committer to commit to a polynomial with a short string that can be used by a verifier to confirm claimed evaluations of the committed polynomial. Although the homomorphic commitment schemes in the literature can be used to achieve this goal, the sizes of their commitments are linear in the degree of the committed polynomial. On the other hand, polynomial commitments in our schemes are of constant size (single elements). The overhead of opening a commitment is also constant; even opening multiple evaluations requires only a constant amount of communication overhead. Therefore, our schemes are useful tools to reduce the communication cost in cryptographic protocols. On that front, we apply our polynomial commitment schemes to four problems in cryptography: verifiable secret sharing, zero-knowledge sets, credentials and content extraction signatures.  
以下是中文翻译：

我们引入并正式定义了多项式承诺方案（polynomial commitment schemes），并提供了两种高效的构造方法。多项式承诺方案允许承诺方使用一个短字符串对多项式进行承诺，验证方可以使用该字符串来确认所承诺多项式的声明求值结果。尽管文献中的同态承诺方案（homomorphic commitment schemes）可以用来实现这一目标，但它们的承诺大小与所承诺多项式的度数呈线性关系。另一方面，我们方案中的多项式承诺具有常数大小（单个元素）。打开承诺的开销也是常数级的；即使打开多个求值也仅需要常数量级的通信开销。因此，我们的方案是降低密码学协议中通信成本的有用工具。在这方面，我们将多项式承诺方案应用于密码学中的四个问题：可验证秘密共享（verifiable secret sharing）、零知识集合（zero-knowledge sets）、凭证（credentials）和内容提取签名（content extraction signatures）。

## 关键词提炼

1. **多项式承诺方案** - 核心技术创新
2. **常数大小承诺** - 主要性能优势
3. **通信开销优化** - 实际应用价值
4. **可验证秘密共享** - 重要应用领域
5. **零知识密码学** - 技术应用范畴

An extended version of this paper is available [24]. This research