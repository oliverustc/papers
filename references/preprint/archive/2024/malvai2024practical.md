---
title: "Practical Proofs of Parsing for Context-free Grammars"
标题简称:
论文类型: preprint
预印本简称: archive
发表年份: 2024
created: 2025-04-16 10:35:39
modified: 2025-04-16 10:38:09
---

## Practical Proofs of Parsing for Context-free Grammars

## 发表信息

+ [原文链接](https://eprint.iacr.org/2024/562)

## 作者

+ Harjasleen Malvai 
+ Siam Hussain 
+ Gregory Neven 
+ [Andrew Miller](Andrew%20Miller.md) 

## 笔记

We present a scheme to prove, in zero-knowledge (ZK), the correct parsing of a string in context-free grammar (CFG). This is a crucial step towards applications such as proving statements about web API responses in ZK. To the best of our knowledge, this is the first ZK scheme to prove the correctness of CFG parsing with complexity linear in the length of the string. Further, our algorithm flexibly accommodates different ZK proof systems. We demonstrate this flexibility with multiple implementations using both non-interactive and interactive proof paradigms. Given general-purpose ZK programming frameworks, our implementations are not only compact (e.g., around 200 lines of code for the non-interactive version) but also deliver competitive performance. In the non-interactive setting, proving the correct parsing of a ≈1KB string takes 24 seconds, even for grammars with $2^{10}$ production rules. In the interactive setting the same proof takes just 1.6 seconds.  

以下是中文翻译：

我们提出了一个方案，用于在零知识（ZK）环境下证明上下文无关文法（CFG）中字符串的正确解析。这是朝着在零知识证明中验证网络API响应等应用迈出的关键一步。据我们所知，这是首个在字符串长度上呈线性复杂度的CFG解析正确性零知识证明方案。此外，我们的算法能够灵活适配不同的零知识证明系统。我们通过使用非交互式和交互式证明范式的多个实现来展示这种灵活性。基于通用零知识编程框架，我们的实现不仅简洁（例如，非交互式版本仅需约200行代码），而且具有竞争力的性能。在非交互式环境中，即使对于具有$2^{10}$个产生式规则的文法，证明约1KB字符串的正确解析仅需24秒。在交互式环境中，相同的证明仅需1.6秒。

## 关键词

+ 上下文无关文法解析零知识证明
+ CFG字符串解析线性复杂度ZK
+ 网络API响应零知识验证
+ 非交互式交互式证明范式
+ ZK解析通用编程框架实现