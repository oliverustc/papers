---
title: Updatable Privacy-Preserving Blueprints
标题简称: 
论文类型: conference
会议简称: ASIACRYPT
发表年份: 2024
modified: 2025-04-21 11:07:05
created: 2025-04-15 14:08:59
---

## Updatable Privacy-Preserving Blueprints

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-981-96-0875-1_4)

## 作者

+ Bernardo David 
+ Felix Engelmann 
+ Tore Frederiksen 
+ [Markulf Kohlweiss](Markulf%20Kohlweiss.md) 
+ Elena Pagnin 
+ Mikhail Volkhov 

## 笔记

Privacy-preserving blueprint schemes (Kohlweiss et al., EUROCRYPT’23) offer a mechanism for safeguarding user’s privacy while allowing for specific legitimate controls by a designated auditor agent. These schemes enable users to create escrows encrypting the result of evaluating a function $y = P(t,x)$, with P being publicly known, t a secret used during the auditor’s key generation, and x the user’s private input. Crucially, escrows only disclose the blueprinting result $y = P(t,x)$ to the designated auditor, even in cases where the auditor is fully compromised. The original definition and construction only support the evaluation of functions P on an input x provided by a single user.

We address this limitation by introducing updatable privacy-preserving blueprint schemes (UPPB), which enhance the original notion with the ability for multiple users to non-interactively update the private user input x while blueprinting. Moreover, UPPBs contain a proof that y is the result of a sequence of valid updates, while revealing nothing else about the private inputs $\{x_{i}\}$ of updates. As in the case of privacy-preserving blueprints, we first observe that UPPBs can be realized via a generic construction for arbitrary predicates P based on FHE and NIZKs. Our main result is $\mathsf{uBlu}$, an efficient instantiation for a specific predicate comparing the values x and t, where x is the cumulative sum of users’ private inputs and t is a fixed private value provided by the auditor in the setup phase. This rather specific setting already finds interesting applications such as privacy-preserving anti-money laundering and location tracking, and can be extended to support more generic predicates.

From the technical perspective, we devise a novel technique to keep the escrow size concise, independent of the number of updates, and reasonable for practical applications. We achieve this via a novel characterization of malleability for the algebraic NIZK by Couteau and Hartmann (CRYPTO’20) that allows for an additive update function.

以下是中文翻译：

隐私保护蓝图方案(privacy-preserving blueprint schemes)(Kohlweiss等人，EUROCRYPT'23)提供了一种机制，在允许指定审计代理进行特定合法控制的同时保护用户隐私。这些方案使用户能够创建托管加密，加密评估函数$y = P(t,x)$的结果，其中P是公开已知的，t是审计者密钥生成过程中使用的密钥，x是用户的私有输入。关键的是，即使在审计者完全被攻破的情况下，托管加密也只向指定的审计者披露蓝图结果$y = P(t,x)$。ev。

我们通过引入可更新隐私保护蓝图方案(updatable privacy-preserving blueprint schemes, UPPB)来解决这一限制，该方案通过允许多个用户在蓝图过程中非交互式地更新私有用户输入x来增强原始概念。此外，UPPB包含一个证明，表明y是一系列有效更新的结果，同时不泄露关于更新的私有输入$\{x_{i}\}$的任何其他信息。与隐私保护蓝图一样，我们首先观察到UPPB可以通过基于全同态加密(FHE)和非交互式零知识证明(NIZKs)的通用构造来实现任意谓词P。我们的主要结果是$\mathsf{uBlu}$，这是一个针对特定谓词的高效实例化，该谓词比较值x和t，其中x是用户私有输入的累积和，t是审计者在设置阶段提供的固定私有值。这种相当特定的设置已经找到了有趣的应用，如隐私保护反洗钱和位置追踪，并且可以扩展以支持更通用的谓词。

从技术角度来看，我们设计了一种新颖的技术来保持托管加密的大小简洁，与更新次数无关，并且适合实际应用。我们通过对Couteau和Hartmann(CRYPTO'20)的代数非交互式零知识证明的可延展性的新特征描述来实现这一点，该特征允许加法更新函数。

## 关键词

+ 隐私保护蓝图
+ 可更新方案
+ 全同态加密
+ 零知识证明
+ 反洗钱