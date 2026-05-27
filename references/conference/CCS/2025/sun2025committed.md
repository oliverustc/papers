---
title: "Committed Vector Oblivious Linear Evaluation and Its Applications"
doi: 10.1145/3719027.3744887
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2025
created: 2025-06-09 10:27:18
modified: 2025-06-09 10:29:28
---
## Committed Vector Oblivious Linear Evaluation and Its Applications

## 发表信息

+ [原文链接](https://eprint.iacr.org/2025/1037)

## 作者

+ Yunqing Sun
+ Hanlin Liu
+ [Kang Yang](Kang%20Yang.md)
+ Yu Yu
+ [Xiao Wang](Xiao%20Wang.md)
+ [Chenkai Weng](Chenkai%20Weng.md)

## 笔记

We introduce the notion of committed vector oblivious linear evaluation (C-VOLE), which allows a party holding a pre-committed vector to generate VOLE correlations with multiple parties on the committed value. It is a unifying tool that can be found useful in zero-knowledge proofs (ZKPs) of committed values, actively secure multi-party computation, private set intersection (PSI), etc. To achieve the best efficiency, we design a tailored commitment scheme and matching C-VOLE protocols, both based on the learning parity with noise assumption. In particular, exploiting the structures of the carefully designed LPN-based commitment minimizes the cost of ensuring consistency between the committed vector and VOLE correlation. As a result, we achieve a 28× improvement over the protocol proposed in prior work (Usenix 2021) that uses ZKP to prove the correct opening of the commitment. We also apply C-VOLE to design a PSI protocol that allows one server to run PSI repeatedly with multiple clients while ensuring that the same set is used across all executions. Compared with the state-of-the-art PSI (CCS 2024) with similar security requirements, our protocol reduces the communication overhead by a factor of 35×.

以下是中文翻译：

我们提出了承诺向量不经意线性评估（Committed Vector Oblivious Linear Evaluation, C-VOLE）的概念，该技术允许持有预先承诺向量（committed vector）的一方与多方基于承诺值生成VOLE关联。它是一种通用工具，可应用于承诺值的零知识证明（Zero-Knowledge Proofs, ZKP）、主动安全的多方计算、隐私集合求交（Private Set Intersection, PSI）等场景。

为实现最优效率，我们设计了一种定制的承诺方案和与之匹配的C-VOLE协议，二者均基于噪声学习奇偶性假设（Learning Parity with Noise, LPN）。特别地，通过利用精心设计的基于LPN的承诺结构，我们最小化了确保承诺向量与VOLE关联间一致性的成本。实验结果表明，相较于先前工作（Usenix 2021）中使用ZKP证明承诺正确打开的方案，我们的协议实现了28倍的性能提升。

此外，我们将C-VOLE应用于PSI协议设计，使单一服务器能够与多个客户端重复执行PSI，同时确保所有执行中使用同一集合。与具备类似安全需求的现有最优PSI方案（CCS 2024）相比，我们的协议将通信开销降低了35倍。

## 关键词

+ 承诺向量不经意线性评估
+ 噪声学习奇偶性假设
+ 隐私集合求交
+ 零知识证明
+ 多方计算