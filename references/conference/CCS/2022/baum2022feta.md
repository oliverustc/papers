---
title: "Feta: Efficient threshold designated-verifier zero-knowledge proofs"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2022
---

## Feta: Efficient threshold designated-verifier zero-knowledge proofs

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3548606.3559354)

## 作者

+ Carsten Baum 
+ Robin Jadoul 
+ Emmanuela Orsini 
+ Peter Scholl 
+ Nigel P Smart 


## 笔记

Zero-Knowledge protocols have increasingly become both popular and practical in recent years due to their applicability in many areas such as blockchain systems. Unfortunately, public verifiability and small proof sizes of zero-knowledge protocols currently come at the price of strong assumptions, large prover time, or both, when considering statements with millions of gates. In this regime, the most prover-efficient protocols are in the designated verifier setting, where proofs are only valid to a single party that must keep a secret state.

In this work, we bridge this gap between designated-verifier proofs and public verifiability by distributing the verifier efficiently. Here, a set of verifiers can then verify a proof and, if a given threshold t of the n verifiers is honest and trusted, can act as guarantors for the validity of a statement. We achieve this while keeping the concrete efficiency of current designated-verifier proofs, and present constructions that have small concrete computation and communication cost. We present practical protocols in the setting of threshold verifiers with t<n/4 and t<n/3, for which we give performance figures, showcasing the efficiency of our approach.

以下是中文翻译：

近年来，零知识协议（Zero-Knowledge protocols）因其在区块链系统等众多领域的适用性而日益受到关注并走向实用化。然而，当前在处理包含数百万逻辑门的陈述时，零知识协议的公开可验证性与精简证明规模往往需要以强安全性假设、庞大的证明方计算时间或二者兼有为代价。在此类场景下，最高效的证明方协议均采用指定验证者模式（designated verifier），即证明仅对单个需要维护秘密状态的验证方有效。

本研究通过高效分布式验证机制，弥合了指定验证者证明与公开可验证性之间的鸿沟。在该机制中，一组验证者可共同完成证明验证，若 n 个验证者中有达到设定阈值 t 的成员保持诚实可信，即可共同为陈述有效性提供担保。我们在保持当前指定验证者证明具体效率的同时实现了这一目标，提出的构建方案具有较低的具体计算与通信成本。针对阈值参数 t<n/4 与 t<n/3 的验证者场景，我们给出了实际协议方案并提供性能数据，充分证明了该方法的高效性。

## 关键词

+ 分布式验证
+ 阈值验证者
+ 零知识协议
+ 公开可验证性
+ 证明效率