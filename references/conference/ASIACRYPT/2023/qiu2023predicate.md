---
title: "Predicate aggregate signatures and applications"
标题简称:
论文类型: conference
会议简称: ASIACRYPT
发表年份: 2023
created: 2025-04-17 10:54:09
modified: 2025-04-17 10:54:33
---

## Predicate aggregate signatures and applications

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-981-99-8724-5_9)

## 作者

+ Tian Qiu 
+ Qiang Tang 

## 笔记

Motivated by applications in anonymous reputation systems and blockchain governance, we initiate the study of predicate aggregate signatures (PAS), which is a new primitive that enables users to sign multiple messages, and these individual signatures can be aggregated by a combiner, preserving the anonymity of the signers. The resulting PAS discloses only a brief description of signers for each message and provides assurance that both the signers and their description satisfy the specified public predicate.

We formally define PAS and give a construction framework to yield a logarithmic size signature, and further reduce the verification time also to logarithmic. We also give several instantiations for several concrete predicates that may be of independent interest.

To showcase its power, we also demonstrate its applications to multiple settings including multi-signatures, aggregate signatures, threshold signatures, (threshold) ring signatures, attribute-based signatures, etc, and advance the state of the art in all of them.

以下是中文翻译：

受匿名声誉系统和区块链治理应用的启发，我们开始研究谓词聚合签名（Predicate Aggregate Signatures, PAS），这是一种新原语，允许用户对多个消息进行签名，并且这些单独的签名可以由组合器（combiner）进行聚合，同时保持签名者的匿名性。生成的PAS仅为每条消息披露签名者的简要描述，并确保签名者及其描述满足指定的公共谓词（public predicate）。

我们正式定义了PAS，并给出了一个构造框架，以生成对数大小的签名，并进一步将验证时间也减少到对数级别。我们还为多个具体谓词提供了若干实例，这些实例可能具有独立的研究价值。

为了展示其强大功能，我们还演示了其在多个场景中的应用，包括多重签名、聚合签名、门限签名（threshold signatures）、（门限）环签名（ring signatures）、基于属性的签名（attribute-based signatures）等，并在所有这些领域推动了技术的进步。

## 关键词

+ 谓词聚合签名
+ 匿名签名
+ 聚合签名
+ 环签名
+ 隐私保护