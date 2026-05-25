---
title: "Reef: Fast Succinct Non-InteractiveZero-Knowledge Regex Proofs"
标题简称:
论文类型: conference
会议简称: USENIX Security
发表年份: 2024
created: 2025-04-21 10:58:41
modified: 2025-04-23 15:46:35
---

## Reef: Fast Succinct Non-InteractiveZero-Knowledge Regex Proofs

## 发表信息

+ [原文链接](https://www.usenix.org/conference/usenixsecurity24/presentation/angel)
+ [code](https://github.com/eniac/Reef)

## 作者

+ Sebastian Angel 
+ Eleftherios Ioannidis 
+ Elizabeth Margolin 
+ [Srinath Setty](Srinath%20Setty.md) 
+ Jess Woods 

## 笔记

This paper presents Reef, a system for generating publicly verifiable succinct non-interactive zero-knowledge proofs that a committed document matches or does not match a regular expression. We describe applications such as proving the strength of passwords, the provenance of email despite redactions, the validity of oblivious DNS queries, and the existence of mutations in DNA. Reef supports the Perl Compatible Regular Expression syntax, including wildcards, alternation, ranges, capture groups, Kleene star, negations, and lookarounds. Reef introduces a new type of automata, Skipping Alternating Finite Automata (SAFA), that skips irrelevant parts of a document when producing proofs without undermining soundness, and instantiates SAFA with a lookup argument. Our experimental evaluation confirms that Reef can generate proofs for documents with 32M characters; the proofs are small and cheap to verify (under a second).

以下是中文翻译：

本文介绍了Reef，一个生成公开可验证的简洁非交互式零知识证明（non-interactive zero-knowledge proofs）系统，用于证明一个已提交文档是否与正则表达式（regular expression）匹配。我们描述了一些应用场景，例如证明密码的强度、尽管经过编辑仍能验证电子邮件的来源、无知DNS查询的有效性，以及DNA中突变的存在。Reef支持Perl兼容的正则表达式语法，包括通配符、选择、范围、捕获组、克莱尼星（Kleene star）、否定和前后查找（lookarounds）。Reef引入了一种新型自动机，跳过交替有限自动机（Skipping Alternating Finite Automata，SAFA），在生成证明时跳过文档中无关的部分，而不影响证明的正确性，并通过查找参数实例化SAFA。我们的实验评估确认，Reef可以为包含3200万字符的文档生成证明；这些证明体积小且验证成本低（在一秒钟内）。

## 关键词

+ Reef正则表达式零知识证明
+ SAFA跳过交替有限自动机
+ 文档匹配ZK证明系统
+ 密码强度匿名证明
+ DNS查询隐私保护ZK
+ 非交互式简洁正则证明
