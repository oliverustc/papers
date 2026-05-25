---
title: "zkSaaS: Zero-KnowledgeSNARKs as a Service"
标题简称:
论文类型: conference
会议简称: USENIX Security
发表年份: 2023
modified: 2025-04-11 11:17:00
---

## zkSaaS: Zero-KnowledgeSNARKs as a Service

## 发表信息

+ [原文链接](https://www.usenix.org/conference/usenixsecurity23/presentation/garg)

## 作者

+ [Sanjam Garg](Sanjam%20Garg.md) 
+ [Aarushi Goel](Aarushi%20Goel.md)
+ [Abhishek Jain](Abhishek%20Jain.md)
+ [Guru-Vamsi Policharla](Guru-Vamsi%20Policharla.md)
+ Sruthi Sekar 

## 笔记

A decade of active research has led to practical constructions of zero-knowledge succinct non-interactive arguments of knowledge (zk-SNARKs) that are now being used in a wide variety of applications. Despite this astonishing progress, overheads in proof generation time remain significant.

In this work, we envision a world where consumers with low computational resources can outsource the task of proof generation to a group of untrusted servers in a privacy-preserving manner. The main requirement is that these servers should be able to collectively generate proofs at a faster speed (than the consumer). Towards this goal, we introduce a framework called zk-SNARKs-as-a-service (zkSaaS) for faster computation of zk-SNARKs. Our framework allows for distributing proof computation across multiple servers such that each server is expected to run for a shorter duration than a single prover. Moreover, the privacy of the prover's witness is ensured against any minority of colluding servers.

We design custom protocols in this framework that can be used to obtain faster runtimes for widely used zk-SNARKs, such as Groth16 [EUROCRYPT 2016], Marlin [EUROCRYPT 2020] and Plonk [EPRINT 2019]. We implement proof of concept zkSaaS for the Groth16 and Plonk provers. In comparison to generating these proofs on commodity hardware, we can not only generate proofs for a larger number of constraints (without memory exhaustion), but can also get ≈22× speed-up when run with 128 parties for 225 constraints with Groth16 and 221 gates with Plonk.

以下是中文翻译：

经过十年的积极研究，零知识简洁非交互式知识论证(zk-SNARKs)已经有了实用的构建方案，并在各种应用中得到广泛使用。尽管取得了惊人的进展，但在证明生成时间方面的开销仍然很大。

在本研究中，我们设想这样一个场景：计算资源有限的用户可以以隐私保护的方式将证明生成任务外包给一组不受信任的服务器。主要要求是这些服务器应该能够集体以更快的速度(比用户更快)生成证明。为此，我们提出了一个称为zk-SNARKs即服务(zkSaaS)的框架，用于更快地计算zk-SNARKs。我们的框架允许在多个服务器之间分配证明计算，使得每个服务器的运行时间预期都比单个证明者更短。此外，对于任何少数串通的服务器，都能确保证明者见证(witness)的隐私性。

我们在这个框架中设计了定制协议，可用于为广泛使用的zk-SNARKs获得更快的运行时间，如Groth16 [EUROCRYPT 2016]、Marlin [EUROCRYPT 2020]和Plonk [EPRINT 2019]。我们为Groth16和Plonk证明者实现了概念验证性的zkSaaS。与在普通硬件上生成这些证明相比，我们不仅可以为更多的约束条件生成证明(不会耗尽内存)，而且在使用128个参与方的情况下，对于Groth16的$2^{25}$个约束和Plonk的$2^{21}$个门电路，可以获得约22倍的速度提升。

## 关键词

+ zkSaaS分布式zkSNARK服务
+ 证明生成外包多服务器
+ Groth16 Plonk分布式加速
+ 隐私保护证明外包
+ 抗合谋见证隐私保护
+ zk-SNARK云计算框架
