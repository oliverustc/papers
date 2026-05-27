---
title: "AUC: Accountable Universal Composability"
doi: 10.1109/sp46215.2023.10179384
标题简称:
论文类型: conference
会议简称: S&P
发表年份: 2023
created: 2025-05-23 01:08:01
modified: 2025-05-23 01:08:13
---
## AUC: Accountable Universal Composability

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/10179384)

## 作者

+ Mike Graf
+ [Ralf Küsters](Ralf%20K%C3%BCsters.md)
+ [Daniel Rausch](Daniel%20Rausch.md)
## 笔记

Accountability is a well-established and widely used security concept that allows for obtaining undeniable cryptographic proof of misbehavior, thereby incentivizing honest behavior. There already exist several general purpose account-ability frameworks for formal game-based security analyses. Unfortunately, such game-based frameworks do not support modular security analyses, which is an important tool to handle the complexity of modern protocols.Universal composability (UC) models provide native support for modular analyses, including re-use and composition of security results. So far, accountability has mainly been modeled and analyzed in UC models for the special case of MPC protocols, with a general purpose accountability framework for UC still missing. That is, a framework that among others supports arbitrary protocols, a wide range of accountability properties, handling and mixing of accountable and non-accountable security properties, and modular analysis of accountable protocols.To close this gap, we propose AUC, the first general purpose accountability framework for UC models, which supports all of the above, based on several new concepts. We exemplify AUC in three case studies not covered by existing works. In particular, AUC unifies existing UC accountability approaches within a single framework.

以下是中文翻译：

问责制是一个成熟且广泛使用的安全概念，它允许获得无可否认的不当行为加密证据，从而激励诚实的行为。已经存在几个通用的问责制框架，用于正式的基于游戏的安全分析。遗憾的是，这种基于游戏的框架不支持模块化安全分析，而模块化安全分析是处理现代协议复杂性的重要工具。通用可组合性 （UC） 模型为模块化分析提供原生支持，包括安全结果的重用和组合。到目前为止，问责制主要在 UC 模型中针对 MPC 协议的特殊情况进行建模和分析，目前仍缺少 UC 的通用问责框架。也就是说，一个框架，其中包括支持任意协议、广泛的问责制属性、可问责和非可问责安全属性的处理和混合，以及可问责协议的模块化分析。为了缩小这一差距，我们提出了 AUC，这是 UC 模型的第一个通用问责框架，它基于几个新概念支持上述所有内容。我们在现有工作未涵盖的三个案例研究中举例说明了 AUC。特别是，AUC 将现有的 UC 问责方法统一在一个框架中。

## 关键词

+ 通用可组合性框架
+ 问责制安全模型
+ 模块化安全分析
+ 安全多方计算问责
+ 形式化安全分析
+ 可组合协议设计