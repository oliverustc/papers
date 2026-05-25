---
title: "Sonic: Zero-Knowledge SNARKs from Linear-Size Universal and Updatable Structured Reference Strings"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2019
modified: 2025-04-15 16:37:28
created: 2025-04-08 17:28:08
---

## Sonic: Zero-Knowledge SNARKs from Linear-Size Universal and Updatable Structured Reference Strings

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3319535.3339817)

## 作者

+ [Mary Maller](Mary%20Maller.md)
+ [Sean Bowe](Sean%20Bowe.md)
+ [Markulf Kohlweiss](Markulf%20Kohlweiss.md)
+ [Sarah Meiklejohn](Sarah%20Meiklejohn.md)
## 笔记

Ever since their introduction, zero-knowledge proofs have become an important tool for addressing privacy and scalability concerns in a variety of applications. In many systems each client downloads and verifies every new proof, and so proofs must be small and cheap to verify. The most practical schemes require either a trusted setup, as in (pre-processing) zk-SNARKs, or verification complexity that scales linearly with the complexity of the relation, as in Bulletproofs. The structured reference strings required by most zk-SNARK schemes can be constructed with multi-party computation protocols, but the resulting parameters are specific to an individual relation. Groth et al. discovered a zk-SNARK protocol with a universal structured reference string that is also updatable, but the string scales quadratically in the size of the supported relations.
Here we describe a zero-knowledge SNARK, Sonic, which supports a universal and continually updatable structured reference string that scales linearly in size. We also describe a generally useful technique in which untrusted "helpers" can compute advice that allows batches of proofs to be verified more efficiently. Sonic proofs are constant size, and in the "helped" batch verification context the marginal cost of verification is comparable with the most efficient SNARKs in the literature.

以下是中文翻译：

自从零知识证明(zero-knowledge proofs)被引入以来，它已成为解决各种应用中隐私和可扩展性问题的重要工具。在许多系统中，每个客户端都需要下载并验证每个新的证明，因此证明必须体积小且易于验证。目前最实用的方案要么需要可信设置，如(预处理)零知识简洁非交互式知识论证(zk-SNARKs)，要么验证复杂度与关系复杂度呈线性增长，如防弹证明(Bulletproofs)。大多数zk-SNARK方案所需的结构化参考字符串可以通过多方计算协议构建，但产生的参数仅适用于特定关系。Groth等人发现了一个具有通用结构化参考字符串且可更新的zk-SNARK协议，但该字符串的大小与所支持关系的大小呈二次方增长。

在本文中，我们描述了一个零知识SNARK系统Sonic，它支持大小呈线性增长的通用且可持续更新的结构化参考字符串。我们还描述了一种普遍实用的技术，其中不可信的"帮助者"(helpers)可以计算建议(advice)，使批量证明的验证更加高效。Sonic证明具有恒定大小，在"帮助"批量验证的情况下，验证的边际成本可与文献中最高效的SNARK相媲美。

## 关键词

+ 零知识证明
+ SNARK
+ 通用参考字符串
+ 可更新参数
+ 批量验证