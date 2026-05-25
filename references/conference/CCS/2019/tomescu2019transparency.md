---
title: "Transparency logs via append-only authenticated dictionaries"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2019
---

## Transparency logs via append-only authenticated dictionaries

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3319535.3345652)

## 作者

+ [Alin Tomescu](Alin%20Tomescu.md)
+ Vivek Bhupatiraju 
+ [Dimitrios Papadopoulos](Dimitrios%20Papadopoulos.md) 
+ [Charalampos Papamanthou](Charalampos%20Papamanthou.md) 
+ [Nikos Triandopoulos](Nikos%20Triandopoulos.md)
+ Srinivas Devadas 


## 笔记

Transparency logs allow users to audit a potentially malicious service, paving the way towards a more accountable Internet. For example, Certificate Transparency (CT) enables domain owners to audit Certificate Authorities (CAs) and detect impersonation attacks. Yet, to achieve their full potential, transparency logs must be bandwidth-efficient when queried by users. Specifically, everyone should be able to efficientlylook up log entries by their keyand efficiently verify that the log remainsappend-only. Unfortunately, without additional trust assumptions, current transparency logs cannot provide both small-sizedlookup proofs and small-sizedappend-only proofs. In fact, one of the proofs always requires bandwidth linear in the size of the log, making it expensive for everyone to query the log. In this paper, we address this gap with a new primitive called anappend-only authenticated dictionary (AAD). Our construction is the first to achieve (poly) logarithmic size for both proof types and helps reduce bandwidth consumption in transparency logs. This comes at the cost of increased append times and high memory usage, both of which remain to be improved to make practical deployment possible.

以下是中文翻译：

透明度日志（transparency logs）允许用户审计潜在的恶意服务，为建立更负责任的互联网铺平了道路。例如，证书透明度（Certificate Transparency, CT）使域名所有者能够审计证书颁发机构（Certificate Authorities, CAs）并检测冒充攻击。然而，为了充分发挥其潜力，透明度日志在被用户查询时必须具备带宽效率。具体而言，每个人都应该能够高效地通过密钥查找日志条目，并高效地验证日志保持仅追加性（append-only）。不幸的是，在没有额外信任假设的情况下，当前的透明度日志无法同时提供小尺寸的查找证明（lookup proofs）和小尺寸的仅追加证明（append-only proofs）。事实上，其中一种证明总是需要与日志大小成线性关系的带宽，这使得每个人查询日志的成本都很高昂。在本文中，我们通过一种称为仅追加认证字典（append-only authenticated dictionary, AAD）的新原语来解决这一差距。我们的构造是首个在两种证明类型上都实现（多项式）对数大小的方案，有助于减少透明度日志中的带宽消耗。这是以增加追加时间和高内存使用为代价的，这两个问题仍需改进以使实际部署成为可能。

## 关键词

+ 仅追加认证字典
+ 透明度日志
+ 带宽效率
+ 证明大小优化
+ 证书透明度