---
title: "The random oracle methodology, revisited"
doi: 10.1145/1008731.1008734
标题简称:
论文类型: journal
期刊简称: JACM
发表年份: 2004
modified: 2025-04-08 18:38:28
---
## The random oracle methodology, revisited

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/1008731.1008734)

## 作者

+ [Ran Canetti](Ran%20Canetti.md)
+ [Oded Goldreich](Oded%20Goldreich.md)
+ [Shai Halevi](Shai%20Halevi.md)
## 笔记

>**Abstract**
>We take a critical look at the relationship between the security of cryptographic schemes in the Random Oracle Model, and the security of the schemes that result from implementing the random oracle by so called "cryptographic hash functions".The main result of this article is a negative one: There exist signature and encryption schemes that are secure in the Random Oracle Model, but for which _any implementation_ of the random oracle results in insecure schemes. In the process of devising the above schemes, we consider possible definitions for the notion of a "good implementation" of a random oracle, pointing out limitations and challenges.  

以下是中文翻译：

我们深入审视了密码方案在随机预言模型中的安全性与通过所谓”密码学哈希函数”实现随机预言后所得方案安全性之间的关系。本文的核心结论是消极的：存在一些签名和加密方案，在随机预言模型下是安全的，但任何对随机预言的具体实现都会导致这些方案变得不安全。在构建上述方案的过程中，我们探讨了”良好实现”随机预言这一概念的可能定义，指出了其中的局限性和挑战。

## 关键词

+ 随机预言模型安全性分析
+ 密码哈希函数实现局限性
+ 随机预言不可实现性结果
+ 签名加密方案安全分离
+ 密码学标准模型证明
+ 随机预言方法论批判