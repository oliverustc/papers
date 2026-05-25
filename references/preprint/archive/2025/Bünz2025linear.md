---
title: "Linear-Time Accumulation Schemes"
标题简称:
论文类型: preprint
预印本简称: archive
发表年份: 2025
created: 2025-05-07 20:12:20
modified: 2025-05-07 20:13:30
---

## Linear-Time Accumulation Schemes

## 发表信息

+ [原文链接](https://eprint.iacr.org/2025/753)

## 作者

+ [Benedikt Bünz](Benedikt%20Bünz.md)
+ [Alessandro Chiesa](Alessandro%20Chiesa.md)
+ Giacomo Fenzi
+ William Wang

## 笔记

Proof-carrying data (PCD) is a powerful cryptographic primitive for computational integrity in a distributed setting. State-of-the-art constructions of PCD are based on accumulation schemes (and, closely related, folding schemes). We present WARP, the first accumulation scheme with linear prover time and logarithmic verifier time. Our scheme is hash-based (secure in the random oracle model), plausibly post-quantum secure, and supports unbounded accumulation depth. We achieve our result by constructing an interactive oracle reduction of proximity that works with any linear code over a sufficiently large field. We take a novel approach by constructing a straightline extractor that relies on erasure correction, rather than error-tolerant decoding like prior extractors. Along the way, we introduce a variant of straightline round-by-round knowledge soundness that is compatible with our extraction strategy.

以下是中文翻译：

证据携带数据（proof-carrying data, PCD）是一种强大的密码学原语，用于分布式环境中的计算完整性验证。目前最先进的PCD构造方案都基于累积方案（以及与之密切相关的折叠方案）。

我们提出WARP，这是第一个具有线性证明者时间和对数验证者时间的累积方案。我们的方案基于哈希函数（在随机预言机模型中安全），可能具有后量子安全性，并支持无限制的累积深度。

我们通过构造一个可与任何足够大域上的线性码一起工作的交互式邻近预言机归约（interactive oracle reduction of proximity）来实现我们的结果。我们采用了一种新颖的方法，构造了一个依赖于擦除纠正（erasure correction）而非像先前提取器那样依赖容错解码的直线提取器（straightline extractor）。在此过程中，我们引入了一种直线逐轮知识可靠性（straightline round-by-round knowledge soundness）的变体，该变体与我们的提取策略相兼容。

## 关键词

+ WARP线性时间累积方案
+ 证据携带数据分布式计算完整性
+ 折叠方案后量子安全哈希
+ 交互式邻近预言机归约
+ 擦除纠正直线提取器