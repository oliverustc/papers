---
title: "Continuous Space-Bounded Non-malleable Codes from Stronger Proofs-of-Space"
标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 2019

modified: 2025-04-10 16:46:55
---

## Continuous Space-Bounded Non-malleable Codes from Stronger Proofs-of-Space

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-030-26948-7_17)

## 作者

+ [Binyi Chen](Binyi%20Chen.md)
+ [Yilei Chen](Yilei%20Chen.md)
+ [Kristina Hostáková](Kristina%20Hostáková.md)
+ [Pratyay Mukherjee](Pratyay%20Mukherjee.md)

## 笔记

Non-malleable codes are encoding schemes that provide protections against various classes of tampering attacks. Recently Faust et al. (CRYPTO 2017) initiated the study of space-bounded non-malleable codes that provide such protections against tampering within small-space devices. They put forward a construction based on any non-interactive proof-of-space (NIPoS). However, the scheme only protects against an a priori bounded number of tampering attacks.

We construct non-malleable codes that are resilient to an unbounded polynomial number of space-bounded tamperings. Towards that we introduce a stronger variant of $\text{NIPoS}$ called proof-extractable $\text{NIPoS}$ ($\text{PExt-NIPoS}$), and propose two approaches of constructing such a primitive. Using a new proof strategy we show that the generic encoding scheme of Faust et al. achieves unbounded tamper-resilience when instantiated with a $\text{PExt-NIPoS}$. We show two methods to construct $\text{PExt-NIPoS}$

1. The first method uses a special family of “memory-hard” graphs, called challenge-hard graphs (CHG), a notion we introduce here. We instantiate such family of graphs based on an extension of stack of localized expanders (first used by Ren and Devadas in the context of proof-of-space). In addition, we show that the graph construction used as a building block for the proof-of-space by Dziembowski et al. (CRYPTO 2015) satisfies challenge-hardness as well. These two CHG-instantiations lead to continuous space-bounded NMC with different features in the random oracle model.

2. Our second instantiation relies on a new measurable property, called uniqueness of $\text{NIPoS}$. We show that standard extractability can be upgraded to proof-extractability if the $\text{NIPoS}$ also has uniqueness. We propose a simple heuristic construction of $\text{NIPoS}$, that achieves (partial) uniqueness, based on a candidate memory-hard function in the standard model and a publicly verifiable computation with small-space verification. Instantiating the encoding scheme of Faust et al. with this $\text{NIPoS}$, we obtain a continuous space-bounded NMC that supports the “most practical” parameters, complementing the provably secure but “relatively impractical” CHG-based constructions. Additionally, we revisit the construction of Faust et al. and observe that due to the lack of uniqueness of their $\text{NIPoS}$, the resulting encoding schemes yield “highly impractical” parameters in the continuous setting.

We conclude the paper with a comparative study of all our non-malleable code constructions with an estimation of concrete parameters.

以下是中文翻译：

不可篡改码(non-malleable codes)是一种能够防御各类篡改攻击的编码方案。最近，Faust等人(CRYPTO 2017)开创性地研究了空间受限的不可篡改码，这种编码可以防御在小空间设备中的篡改。他们提出了一个基于非交互式空间证明(non-interactive proof-of-space, NIPoS)的构造方案。然而，该方案仅能防御事先限定数量的篡改攻击。

我们构造了一种能够抵抗无限多项式次数的空间受限篡改的不可篡改码。为此，我们引入了NIPoS的一个更强变体，称为可证明提取的NIPoS(proof-extractable NIPoS, PExt-NIPoS)，并提出了两种构造这种原语的方法。通过一种新的证明策略，我们证明了当使用PExt-NIPoS实例化时，Faust等人的通用编码方案可以实现无限次数的篡改抵抗。我们展示了构造PExt-NIPoS的两种方法：

1. 第一种方法使用一类特殊的"内存困难"图(memory-hard graphs)，称为挑战困难图(challenge-hard graphs, CHG)，这是我们在此首次提出的概念。我们基于本地化扩展器栈(stack of localized expanders)的扩展来实例化这类图（该结构最初由Ren和Devadas在空间证明的背景下使用）。此外，我们证明了Dziembowski等人(CRYPTO 2015)在其空间证明中使用的图构造也满足挑战困难性。这两种CHG实例化在随机预言机模型中产生了具有不同特性的连续空间受限不可篡改码。

2. 我们的第二种实例化依赖于一个新的可度量属性，称为NIPoS的唯一性(uniqueness)。我们证明，如果NIPoS具有唯一性，则标准可提取性可以升级为可证明提取性。我们提出了一个基于标准模型中候选内存困难函数和小空间验证的公开可验证计算的简单启发式NIPoS构造，该构造实现了（部分）唯一性。使用这种NIPoS实例化Faust等人的编码方案，我们获得了一个支持"最实用"参数的连续空间受限不可篡改码，这补充了可证明安全但"相对不实用"的基于CHG的构造。此外，我们重新审视了Faust等人的构造，发现由于其NIPoS缺乏唯一性，在连续设置中产生的编码方案具有"高度不实用"的参数。

我们通过对所有不可篡改码构造的具体参数估计进行比较研究来结束本文。

## 关键词

+ 密码学
+ 零知识
+ 协议