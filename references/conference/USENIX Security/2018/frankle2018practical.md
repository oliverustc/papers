---
title: "Practical accountability of secret processes"
标题简称:
论文类型: conference
会议简称: USENIX Security
发表年份: 2018
created: 2025-05-23 01:05:35
modified: 2025-05-23 01:05:55
---

## Practical accountability of secret processes

## 发表信息

+ [原文链接](https://www.usenix.org/conference/usenixsecurity18/presentation/frankie)

## 作者

+ Jonathan Frankle
+ Sunoo Park
+ Daniel Shaar
+ [Shafi Goldwasser](Shafi%20Goldwasser.md)
+ Daniel Weitzner

## 笔记

The US federal court system is exploring ways to improve the accountability of electronic surveillance, an opaque process often involving cases _sealed_ from public view and tech companies subject to _gag orders_ against informing surveilled users. One judge has proposed publicly releasing some metadata about each case on a paper cover sheet as a way to balance the competing goals of (1) secrecy, so the target of an investigation does not discover and sabotage it, and (2) accountability, to assure the public that surveillance powers are not misused or abused.

Inspired by the courts’ accountability challenge, we illustrate how accountability and secrecy are simultaneously achievable when modern cryptography is brought to bear. Our system improves configurability while preserving secrecy, offering new tradeoffs potentially more palatable to the risk-averse court system. Judges, law enforcement, and companies publish commitments to surveillance actions, argue in zero-knowledge that their behavior is consistent, and compute aggregate surveillance statistics by multi-party computation (MPC).

We demonstrate that these primitives perform efficiently at the scale of the federal judiciary. To do so, we implement a hierarchical form of MPC that mirrors the hierarchy of the court system. We also develop statements in succinct zero-knowledge (SNARKs) whose specificity can be tuned to calibrate the amount of information released. All told, our proposal not only offers the court system a flexible range of options for enhancing accountability in the face of necessary secrecy, but also yields a general framework for accountability in a broader class of _secret information processes._

以下是中文翻译：

美国联邦法院系统正在探索改善电子监控问责制的方法。电子监控是一个不透明的过程，通常涉及对公众封闭的案件，且科技公司会受到禁止令的约束，不得告知被监控用户。一位法官提出在纸质封面上公开发布每个案件的部分元数据(metadata)，以平衡两个相互竞争的目标：(1)保密性，使调查对象不会发现并破坏调查；(2)问责制，向公众保证监控权力不会被滥用或误用。

受法院问责制挑战的启发，我们展示了如何通过运用现代密码学同时实现问责制和保密性。我们的系统在保持保密性的同时提高了可配置性，提供了可能更适合规避风险的法院系统的新权衡方案。法官、执法部门和公司发布对监控行为的承诺，以零知识证明(zero-knowledge)的方式论证其行为的一致性，并通过多方计算(multi-party computation, MPC)计算监控统计数据。

我们证明了这些原语(primitives)在联邦司法系统规模下能够高效运行。为此，我们实现了一种与法院系统层级相对应的分层多方计算形式。我们还开发了简洁零知识证明(SNARKs)声明，其具体程度可以调整以校准所发布信息的数量。总的来说，我们的建议不仅为法院系统在必要保密的情况下加强问责制提供了灵活的选择，而且为更广泛的秘密信息处理类别提供了一个通用的问责框架。

## 关键词

+ 电子监控问责制
+ 零知识证明SNARKs
+ 多方安全计算MPC
+ 秘密信息处理框架
+ 司法保密与问责平衡
+ 分层MPC协议
