---
title: "Election verifiability or ballot privacy: Do we need to choose"
标题简称:
论文类型: conference
会议简称: ESORICS
发表年份: 2013
---

## Election verifiability or ballot privacy: Do we need to choose

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-642-40203-6_27)

## 作者

+ Edouard Cuvelier 
+ Olivier Pereira 
+ Thomas Peters 


## 笔记

We propose a new encryption primitive, _commitment consistent encryption_ (CCE), and instances of this primitive that enable building the first universally verifiable voting schemes with a perfectly private audit trail (PPAT) and practical complexity. That is:

- The audit trail that is published for verifying elections guarantees everlasting privacy, and
    
- The computational load required from the participants is only increased by a small constant factor compared to traditional voting schemes, and is optimal in the sense of Cramer, Gennaro and Schoenmakers [16].
    

These properties make it possible to introduce election verifiability in large scale elections as a pure benefit, that is, without loss of privacy compared to a non-verifiable scheme and at a similar level of efficiency.

We propose different approaches for constructing voting schemes with PPAT from CCE, as well as two efficient CCE constructions: one is tailored for elections with a small number of candidates, while the second is suitable for elections with complex ballots.

以下是中文翻译：

我们提出了一种新的加密原语——承诺一致性加密（Commitment Consistent Encryption, CCE），并给出了该原语的具体实例，从而首次构建出具备完美隐私审计轨迹（Perfectly Private Audit Trail, PPAT）且具有实用复杂度的通用可验证投票方案。具体而言：

所发布的用于验证选举结果的审计轨迹可保证永久隐私（everlasting privacy）；

与传统投票方案相比，参与者所需的计算开销仅增加一个较小的常数因子，且在 Cramer、Gennaro 与 Schoenmakers [16] 所定义的意义下达到最优。

这些特性使得在大规模选举中引入选举可验证性成为一种纯粹的增益——即相较于不可验证方案，不会牺牲隐私性，且效率处于相近水平。

我们提出了多种基于 CCE 构建具备 PPAT 特性的投票方案的方法，并给出了两种高效的 CCE 构造：一种针对候选人数量较少的选举场景进行了优化，另一种则适用于选票结构复杂的选举。

## 关键词

+ 承诺一致性加密
+ 完美隐私审计轨迹
+ 通用可验证投票
+ 永久隐私
+ 高效加密构造