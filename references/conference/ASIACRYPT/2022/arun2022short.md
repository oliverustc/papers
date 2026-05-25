---
title: "Short-lived zero-knowledge proofs and signatures"
标题简称:
论文类型: conference
会议简称: ASIACRYPT
发表年份: 2022
created: 2025-04-28 15:00:19
modified: 2025-04-28 15:01:11
---

## Short-lived zero-knowledge proofs and signatures

## 发表信息

+ [原文链接]([Short-lived Zero-Knowledge Proofs and Signatures | SpringerLink](https://link.springer.com/chapter/10.1007/978-3-031-22969-5_17))

## 作者

+ [Arasu Arun](Arasu%20Arun.md)
+ [[Joseph Bonneau]] 
+ Jeremy Clark 

## 笔记

We introduce the short-lived proof, a non-interactive proof of knowledge with a novel feature: after a specified period of time, the proof is no longer convincing. This time-delayed loss of soundness happens “naturally” without further involvement from the prover or any third party. We propose definitions for short-lived proofs as well as the special case of short-lived signatures. We show several practical constructions built using verifiable delay functions (VDFs). The key idea in our approach is to allow any party to forge any proof by executing a large sequential computation. Some constructions achieve a stronger property called reusable forgeability in which one sequential computation allows forging an arbitrary number of proofs of different statements. We also introduces two novel types of VDFs, re-randomizable VDFs and zero-knowledge VDFs, which may be of independent interest. Our constructions for short-lived \Sigma -protocols and signatures are practically efficient for provers and verifiers, adding a few hundred bytes of overhead and tens to hundreds of milliseconds of proving/verification time.

以下是中文翻译：

我们介绍了短暂证明(short-lived proof)这一概念，这是一种具有新颖特征的非交互式知识证明：在指定的时间段后，该证明将不再具有说服力。这种时延性的可靠性损失会"自然发生"，无需证明者或任何第三方的进一步参与。我们提出了短暂证明的定义，以及作为特例的短暂签名(short-lived signatures)的定义。我们展示了几种基于可验证延迟函数(verifiable delay functions, VDFs)构建的实用方案。我们方法的核心思想是允许任何一方通过执行大规模的顺序计算来伪造任何证明。某些构造实现了一种称为可重用伪造性(reusable forgeability)的更强特性，即一次顺序计算可以允许伪造任意数量的不同陈述的证明。我们还引入了两种新型VDF：可重随机化VDF(re-randomizable VDFs)和零知识VDF(zero-knowledge VDFs)，这些可能具有独立的研究价值。我们针对短暂$\Sigma$-协议和签名的构造方案对于证明者和验证者来说都具有实际效率，仅增加了几百字节的开销，以及数十到数百毫秒的证明/验证时间。

## 关键词

+ 短暂证明
+ 可验证延迟函数
+ 时间约束
+ 零知识签名
+ 顺序计算