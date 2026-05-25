---
title: "Composable and modular anonymous credentials: Definitions and practical constructions"
标题简称:
论文类型: conference
会议简称: ASIACRYPT
发表年份: 2015
created: 2025-05-15 10:38:27
modified: 2025-05-26 05:05:15
---

## Composable and modular anonymous credentials: Definitions and practical constructions

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-662-48800-3_11)

## 作者

+ [Jan Camenisch](Jan%20Camenisch.md)
+ Maria Dubovitskaya
+ Kristiyan Haralambiev
+ [Markulf Kohlweiss](Markulf%20Kohlweiss.md)

## 笔记

It takes time for theoretical advances to get used in practical schemes. Anonymous credential schemes are no exception. For instance, existing schemes suited for real-world use lack formal, composable definitions, partly because they do not support straight-line extraction and rely on random oracles for their security arguments. To address this gap, we propose unlinkable redactable signatures (URS), a new building block for privacy-enhancing protocols, which we use to construct the first efficient UC-secure anonymous credential system that supports multiple issuers, selective disclosure of attributes, and pseudonyms. Our scheme is one of the first such systems for which both the size of a credential and its presentation proof are independent of the number of attributes issued in a credential. Moreover, our new credential scheme does not rely on random oracles. As an important intermediary step, we address the problem of building a functionality for a complex credential system that can cover many different features. Namely, we design a core building block for a single issuer that supports credential issuance and presentation with respect to pseudonyms and then show how to construct a full-fledged credential system with multiple issuers in a modular way. We expect this definitional approach to be of independent interest.

以下是论文摘要的中文翻译：

理论进展在实际方案中得到应用需要一定的时间。匿名凭证（Anonymous credential）方案也不例外。例如，现有适用于现实世界的方案缺乏正式的、可组合的定义，部分原因是它们不支持直线提取（straight-line extraction）且依赖随机预言机（random oracles）来进行安全性论证。为解决这一差距，我们提出了不可链接可编辑签名（unlinkable redactable signatures，URS），这是一个用于隐私增强协议的新型基础构件，我们用它构建了第一个高效的UC安全匿名凭证系统，该系统支持多发行者、属性选择性披露以及匿名身份。我们的方案是少数几个凭证大小和其展示证明都独立于凭证中发行的属性数量的系统之一。此外，我们的新凭证方案不依赖随机预言机。作为一个重要的中间步骤，我们解决了为复杂凭证系统构建功能性的问题，该系统可以涵盖多种不同特征。具体而言，我们设计了一个针对单一发行者的核心构件，支持与匿名身份相关的凭证发行和展示，并展示了如何以模块化方式构建一个功能完整的多发行者凭证系统。我们期望这种定义方法本身就具有独立的研究价值。

## 关键词

+ 匿名凭证
+ UC安全
+ 不可链接可编辑签名
+ 选择性属性披露
+ 可组合密码学
+ 多发行者系统