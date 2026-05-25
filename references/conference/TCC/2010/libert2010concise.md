---
title: "Concise mercurial vector commitments and independent zero-knowledge sets with short proofs"
标题简称:
论文类型: conference
会议简称: TCC
发表年份: 2010
---

## Concise mercurial vector commitments and independent zero-knowledge sets with short proofs

## 发表信息

+ [原文链接]()

## 作者

+ [[Benoît Libert]]
+ Moti Yung  


## 笔记

Introduced by Micali, Rabin and Kilian (MRK), the basic primitive of zero-knowledge sets (ZKS) allows a prover to commit to a secret set _S_ so as to be able to prove statements such as $x \in S$ or $x \notin S$. Chase _et al._ showed that ZKS protocols are underlain by a cryptographic primitive termed _mercurial commitment_. A (trapdoor) mercurial commitment has two commitment procedures. At committing time, the committer can choose not to commit to a specific message and rather generate a dummy value which it will be able to softly open to any message without being able to completely open it. Hard commitments, on the other hand, can be hardly or softly opened to only one specific message. At Eurocrypt 2008, Catalano, Fiore and Messina (CFM) introduced an extension called trapdoor _q_-mercurial commitment (qTMC), which allows committing to a vector of _q_ messages. These qTMC schemes are interesting since their openings w.r.t. specific vector positions can be short (ideally, the opening length should not depend on _q_), which provides zero-knowledge sets with much shorter proofs when such a commitment is combined with a Merkle tree of arity _q_. The CFM construction notably features short proofs of _non-membership_ as it makes use of a qTMC scheme with short soft openings. A problem left open is that hard openings still have size $O(q)$, which prevents proofs of membership from being as compact as those of non-membership. In this paper, we solve this open problem and describe a new qTMC scheme where hard and short position-wise openings, both, have _constant size_. We then show how our scheme is amenable to constructing independent zero-knowledge sets (i.e., ZKS’s that prevent adversaries from correlating their set to the sets of honest provers, as defined by Gennaro and Micali). Our solution retains the short proof property for this important primitive as well.

以下是中文翻译：

由 Micali、Rabin 和 Kilian（MRK）提出的零知识集合（zero-knowledge sets, ZKS）这一基础原语，允许证明者对一个秘密集合 $S$ 进行承诺，并能够证明诸如 $x \in S$ 或 $x \notin S$ 等陈述。Chase 等人指出，ZKS 协议的基础是一种称为水银承诺（mercurial commitment）的密码学原语。一种（陷门型）水银承诺包含两种承诺过程：在承诺阶段，承诺者可以选择不承诺某个具体消息，而是生成一个“虚拟值”（dummy value），该值之后可被“软打开”（softly open）为任意消息，但无法被“完全打开”（completely open）。相比之下，“硬承诺”（hard commitments）只能被硬打开或软打开为唯一特定的消息。

在 Eurocrypt 2008 上，Catalano、Fiore 和 Messina（CFM）提出了一种称为陷门 $q$ -水银承诺（trapdoor $q$ -mercurial commitment, qTMC）的扩展方案，允许对长度为 $q$ 的消息向量进行承诺。这类 qTMC 方案具有重要意义，因为其针对向量中特定位置的打开（opening）可以非常简短（理想情况下，打开长度不应依赖于 $q$）。当此类承诺与 $q$ 元 Merkle 树结合使用时，可显著缩短零知识集合的证明长度。CFM 的构造尤其以非成员性（non-membership）证明简短著称，因为它采用了一种具有短软打开（short soft openings）的 qTMC 方案。然而，一个尚未解决的问题是：硬打开（hard openings）的大小仍为 $O (q)$，这导致成员性（membership）证明无法像非成员性证明那样紧凑。

本文解决了这一开放问题，提出了一种新型 qTMC 方案，其中硬打开与软打开在各个位置上的长度均为常数大小（constant size）。我们进一步展示了该方案适用于构建独立零知识集合（independent zero-knowledge sets）——即能够防止敌手将其集合与诚实证明者的集合相关联的 ZKS（该概念由 Gennaro 和 Micali 定义）。我们的方案在实现这一重要原语的同时，依然保持了证明简短的特性。

## 关键词

+ 陷门q-水银承诺qTMC
+ 零知识集合ZKS
+ 常数大小打开承诺
+ 独立零知识集合
+ 非成员性证明
+ Merkle树向量承诺