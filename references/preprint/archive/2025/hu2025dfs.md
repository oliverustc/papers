---
title: "DFS: Delegation-friendly zkSNARK and Private Delegation of Provers"
标题简称:
论文类型: preprint
预印本简称: archive
发表年份: 2025
created: 2025-04-27 09:07:03
modified: 2025-04-27 09:08:16
---

## DFS: Delegation-friendly zkSNARK and Private Delegation of Provers

## 发表信息

+ [原文链接](https://eprint.iacr.org/2025/296)
据说已经中USENIX Security 2025

## 作者

+ [Yuncong Hu](Yuncong%20Hu.md) 
+ [Pratyush Mishra](Pratyush%20Mishra.md)
+ [Xiao Wang](Xiao%20Wang.md) 
+ Jie Xie 
+ [Kang Yang](Kang%20Yang.md)
+ Yu Yu 
+ Yuwen Zhang 

## 笔记

Zero-Knowledge Succinct Non-interactive Arguments of Knowledge (zkSNARKs) lead to proofs that can be succinctly verified but require huge computational resources to generate. Prior systems outsource proof generation either through public delegation, which reveals the witness to the third party, or, more preferably, private delegation that keeps the witness hidden using multiparty computation (MPC). However, current private delegation schemes struggle with scalability and efficiency due to MPC inefficiencies, poor resource utilization, and suboptimal design of zkSNARK protocols. In this paper, we introduce DFS, a new zkSNARK that is delegation-friendly for both public and private scenarios. Prior work focused on optimizing the MPC protocols for existing zkSNARKs, while DFS uses co-design between MPC and zkSNARK so that the protocol is efficient for both distributed computing and MPC. In particular, DFS achieves linear prover time and logarithmic verification cost in the non-delegated setting. For private delegation, DFS introduces a scheme with zero communication overhead in MPC and achieves malicious security for free, which results in logarithmic overall communication; while prior work required linear communication. Our evaluation shows that DFS is as efficient as state-of-the-art zkSNARKs in public delegation; when used for private delegation, it scales better than previous work. In particular, for $2^{24}$ constraints, the total communication of DFS is less than 500KB, while prior work incurs 300GB, which is linear to the circuit size. Additionally, we identify and address a security flaw in prior work, EOS (USENIX'23).

以下是中文翻译：

零知识简洁非交互式知识论证(Zero-Knowledge Succinct Non-interactive Arguments of Knowledge, zkSNARKs)可以生成能够简洁验证的证明，但生成这些证明需要巨大的计算资源。现有系统通过两种方式将证明生成外包：一种是公开委托，但这会向第三方泄露见证(witness)；另一种更可取的方式是私有委托，通过多方计算(multiparty computation, MPC)保持见证的隐私性。然而，由于MPC效率低下、资源利用率差以及zkSNARK协议设计不够优化，当前的私有委托方案在可扩展性和效率方面存在问题。

本文介绍了DFS，这是一个新的zkSNARK方案，适用于公开和私有委托场景。先前的研究主要关注于为现有zkSNARK优化MPC协议，而DFS采用MPC和zkSNARK的协同设计，使得协议在分布式计算和MPC方面都能高效运行。具体而言，在非委托设置下，DFS实现了线性证明者时间和对数级验证成本。

对于私有委托，DFS提出了一个在MPC中零通信开销的方案，并自动实现恶意安全性，从而实现对数级的总体通信量；而先前的工作需要线性通信量。我们的评估表明，DFS在公开委托方面与最先进的zkSNARK方案效率相当；在私有委托方面，其可扩展性优于先前的工作。特别是，对于2^24个约束条件，DFS的总通信量少于500KB，而先前的工作需要300GB，与电路规模呈线性关系。此外，我们还发现并解决了先前工作EOS（USENIX'23）中的一个安全漏洞。

## 关键词

+ DFS委托友好zkSNARK
+ 私有委托多方计算MPC
+ 零通信开销恶意安全委托
+ 线性证明者对数验证成本
+ zkSNARK协同设计分布式计算