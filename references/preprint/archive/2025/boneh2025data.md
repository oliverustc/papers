---
title: "Data availability sampling with repair"
标题简称:
论文类型: preprint
预印本简称: archive
发表年份: 2025
---

## Data availability sampling with repair

## 发表信息

+ [原文链接](https://eprint.iacr.org/2025/1414)

## 作者

+ [Dan Boneh](Dan%20Boneh.md) 
+ Joachim Neu 
+ Valeria Nikolaenko 
+ Aditi Partap 


## 笔记

Data availability sampling (DAS) is an important technique to horizontally scale consensus protocols without compromising on the number of adversarial nodes that can be tolerated. DAS is on the technical roadmap of major blockchains such as Ethereum. A major challenge for DAS schemes, that has not been formally studied in the literature, is how incomplete shares can be repaired. The need for repairing data shares motivates key aspects of Ethereum's DAS-based sharding vision called "Danksharding". In this work, we make two contributions. First, we provide a new definitional framework that formalizes the notion of local repair, along with the security guarantees that a DAS scheme must provide. Second, we propose a new DAS scheme designed with efficient local repair in mind, based on locally-correctable multiplicity codes. To facilitate using these codes, we introduce a new multivariate polynomial commitment scheme that (i) supports efficient openings of partial derivatives of a committed polynomial, (ii) supports fast batch opening proof generation at many points, and (iii) has an algorithm to recompute (repair) opening proofs at a point from only a few other proofs. The proposed scheme improves upon the state-of-the-art Ethereum PeerDAS scheme, deployed in December 2025, in storage overhead, local repair bandwidth and coordination, while only slightly increasing dispersal cost and sampling bandwidth. As an additional benefit, our construction also supports efficient partial reconstruction, i.e., retrieving parts of the stored data. All of our techniques readily carry over to data availability schemes based on verifiable information dispersal (VID) as well.



以下是中文翻译：

数据可用性采样（Data Availability Sampling, DAS）是一项重要技术，能够在不影响可容忍对抗节点数量的前提下，实现共识协议的水平扩展。DAS技术已被纳入以太坊等主要区块链的技术路线图。DAS方案面临的一个重大挑战是如何修复不完整的数据分片，这一问题在文献中尚未得到正式研究。修复数据分片的需求推动了以太坊基于DAS的分片愿景的关键方面，即"Danksharding"。

在本研究中，我们做出了两项贡献。首先，我们提供了一个新的定义框架，正式化了局部修复（local repair）的概念，以及DAS方案必须提供的安全保证。其次，我们提出了一个新的DAS方案，该方案基于局部可纠错重数码（locally-correctable multiplicity codes），专门针对高效局部修复而设计。为了便于使用这些码，我们引入了一个新的多元多项式承诺方案（multivariate polynomial commitment scheme），该方案具有以下特性：(i) 支持对承诺多项式的偏导数进行高效开放；(ii) 支持在多个点进行快速批量开放证明生成；(iii) 具有仅从少数其他证明重新计算（修复）某点开放证明的算法。所提出的方案在存储开销、局部修复带宽和协调方面改进了最先进的以太坊PeerDAS方案（该方案于2025年12月部署），同时仅略微增加了分散成本和采样带宽。作为额外的好处，我们的构造还支持高效的部分重构（partial reconstruction），即检索存储数据的部分内容。我们的所有技术也可直接应用于基于可验证信息分散（Verifiable Information Dispersal, VID）的数据可用性方案。


## 关键词

+ DAS数据可用性采样局部修复
+ 局部可纠错重数码高效修复
+ 多元多项式承诺偏导数开放
+ 以太坊Danksharding PeerDAS扩展
+ 可验证信息分散部分重构