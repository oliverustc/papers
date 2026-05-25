---
title: "Bifurcated signatures: folding the accountability vs anonymity dilemma into a single private signing scheme"
标题简称:
论文类型: conference
会议简称: EUROCRYPT
发表年份: 2021
created: 2025-05-23 01:41:37
modified: 2025-05-23 01:42:47
---

## Bifurcated signatures: folding the accountability vs anonymity dilemma into a single private signing scheme

## 发表信息

+ [原文链接]()

## 作者

+ [Benoît Libert](Benoît%20Libert.md)
+ [Khoa Nguyen](Khoa%20Nguyen.md)
+ Thomas Peters
+ Moti Yung

## 笔记

Over the development of modern cryptography, often, alternative cryptographic schemes are developed to achieve goals that in some important respect are orthogonal. Thus, we have to choose either a scheme which achieves the first goal and not the second, or vice versa. This results in two types of schemes that compete with each other. In the basic area of user privacy, specifically in anonymous (multi-use credentials) signing, such an orthogonality exists between anonymity and accountability.

The conceptual contribution of this work is to reverse the above orthogonality by design, which essentially typifies the last 25 years or so, and to suggest an alternative methodology where the opposed properties are carefully folded into a single scheme. The schemes will support both opposing properties simultaneously in a bifurcated fashion, where:

- First, based on rich semantics expressed over the message’s context and content, the user, etc., the relevant property is applied point-wise per message operation depending on a predicate; and
    
- Secondly, at the same time, the schemes provide what we call “branch-hiding;” namely, the resulting calculated value hides from outsiders which property has actually been locally applied.

Specifically, we precisely define and give the first construction and security proof of a “Bifurcated Anonymous Signature” (BiAS): A scheme which supports either absolute anonymity or anonymity with accountability, based on a specific contextual predicate, while being branch-hiding. This novel signing scheme has numerous applications not easily implementable or not considered before, especially because: (i) the conditional traceability does _not_ rely on a trusted authority as it is (non-interactively) encapsulated into signatures; and (ii) signers _know_ the predicate value and can make a conscious choice at each signing time.

Technically, we realize BiAS from homomorphic commitments for a general family of predicates that can be represented by bounded-depth circuits. Our construction is generic and can be instantiated in the standard model from lattices and, more efficiently, from bilinear maps. In particular, the signature length is independent of the circuit size when we use commitments with suitable efficiency properties.

以下是中文翻译：

在现代密码学的发展过程中，常常会开发出实现不同且在某些重要方面相互正交的目标的替代性密码方案。因此，我们必须选择要么实现第一个目标而不实现第二个目标的方案，要么反之。这导致了两种相互竞争的方案类型。在用户隐私的基本领域，特别是在匿名（多次使用凭证）签名中，匿名性和问责性之间存在这样的正交性。

本工作的概念性贡献是通过设计来扭转上述正交性（这基本上是过去25年左右的典型特征），并提出一种替代方法，在这种方法中，对立的属性被精心整合到单一方案中。这些方案将以分叉方式同时支持两种对立的属性，其中：

首先，基于对消息上下文和内容、用户等表达的丰富语义，相关属性根据谓词按每条消息操作逐点应用；

其次，同时，这些方案提供我们称为"分支隐藏"（branch-hiding）的功能；即，生成的计算值对外部人员隐藏了实际上在本地应用了哪种属性。

具体而言，我们精确定义并给出了"分叉匿名签名"（Bifurcated Anonymous Signature，BiAS）的首个构造和安全性证明：该方案基于特定的上下文谓词，支持绝对匿名性或带问责性的匿名性，同时具有分支隐藏特性。这种新颖的签名方案有许多以前不容易实现或未考虑过的应用，特别是因为：(i) 条件可追踪性不依赖于可信机构，因为它（非交互式地）被封装在签名中；以及 (ii) 签名者知道谓词值，并且可以在每次签名时做出有意识的选择。

从技术上讲，我们通过同态承诺（homomorphic commitments）为可由有界深度电路表示的谓词通用族实现了BiAS。我们的构造是通用的，可以在标准模型中从格（lattices）实现，或者更高效地从双线性映射（bilinear maps）实现。特别是，当我们使用具有适当效率属性的承诺时，签名长度与电路大小无关。

## 关键词

+ 分叉匿名签名
+ 匿名性与问责性
+ 分支隐藏
+ 同态承诺
+ 格与双线性映射