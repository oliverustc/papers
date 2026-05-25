---
title: Scalable collaborative zk-snark and its application to efficient proof outsourcing
标题简称: 
论文类型: Conference
undefined: USENIX Security
发表年份: 2025
created: 2025-06-09 10:30:36
modified: 2025-06-09 10:36:52
---

## Scalable Collaborative zk-SNARK and Its Application to Fully Distributed Proof Delegation

## 发表信息

+ [原文链接](https://eprint.iacr.org/2024/940)

## 作者

+ Xuanming Liu
+ Zhelei Zhou
+ Yinghao Wang
+ Jinye He
+ Bingsheng Zhang
+ Xiaohu Yang
+ [Jiaheng Zhang](Jiaheng%20Zhang.md)

## 笔记

Collaborative zk-SNARK (USENIX'22) allows multiple parties to compute a proof over distributed witness. It offers a promising application called proof delegation (USENIX'23), where a client delegates the tedious proof generation to many servers while ensuring no one can learn the witness. Unfortunately, existing works suffer from significant efficiency issues and face challenges when scaling to complex applications. In this work, we introduce the first scalable collaborative zk-SNARK for general circuits, built upon HyperPlonk (Eurocrypt'23). Our result overcomes existing barriers, offering fully distributed workload and small communication. For data-parallel circuits, the communication overhead is even sublinear. We propose several efficient collaborative and distributed protocols for multivariate primitives, which form the main building blocks of our results and may be of independent interest. In addition, we design a new permutation check protocol for Plonk arithmetization, which is MPC-friendly and suitable for collaborative zk-SNARKs. With 128 servers jointly generating a proof for a circuit of size $2^{21}$ gates, the experiment demonstrates over 30× speedup and reduced RAM requirements compared to a local prover, while the witness is still private. Previous works were unable to achieve such savings in both time and memory efficiency. Moreover, our protocol performs well under various network conditions, making it practical for real-world applications.

以下是中文翻译：

协作式zk-SNARK（Collaborative zk-SNARK，USENIX'22）允许多方在分布式见证（witness）数据上联合生成证明。该技术为一种称为证明委托（proof delegation，USENIX'23）的应用提供了可能：客户端将繁重的证明生成任务委托给多个服务器，同时确保任何服务器都无法获取见证数据。然而，现有方案存在显著的效率问题，且难以扩展到复杂应用场景。

本研究提出了首个适用于通用电路的、可扩展的协作式zk-SNARK方案，其基于HyperPlonk（Eurocrypt'23）构建。我们的成果突破了现有技术瓶颈，实现了完全分布式的工作负载和极低的通信开销。对于数据并行电路，通信开销甚至达到亚线性（sublinear）。我们提出了若干高效的多方协作分布式协议，用于处理多元多项式基元（multivariate primitives），这些协议既是本研究的核心组件，也可能具有独立的应用价值。此外，我们为Plonk算术化（Plonk arithmetization）设计了一种新型置换检查协议，该协议兼容多方计算（MPC）框架，特别适合协作式zk-SNARK场景。

实验表明，当128台服务器联合为一个包含$2^{21}$个逻辑门的电路生成证明时，相较于本地证明者，我们的方案实现了30倍以上的加速，同时显著降低了内存需求，且全程保护见证数据的隐私性。现有方案无法同时实现时间与内存效率的此类优化。此外，我们的协议在不同网络条件下均表现优异，具备实际部署的可行性。

## 关键词

+ 协作式zk-SNARK系统
+ 分布式证明生成与委托
+ HyperPlonk算术化优化
+ 多方计算零知识证明
+ 亚线性通信开销
+ 置换检查协议MPC友好设计