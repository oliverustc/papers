---
title: "Ceno: Non-uniform, Segment and Parallel Zero-Knowledge Virtual Machine"
标题简称: Ceno
论文类型: journal
期刊简称: Journal of Cryptology
发表年份: 2025
modified: 2025-04-29 16:29:09
created: 2025-04-07 17:09:14
---

## Ceno: Non-uniform, Segment and Parallel Zero-Knowledge Virtual Machine

## 发表信息

+ [原文链接](https://link.springer.com/article/10.1007/s00145-024-09533-2)
+ [code](https://github.com/scroll-tech/ceno)

## 作者

+ [Tianyi Liu](Tianyi%20Liu.md)
+ [Zhenfei Zhang](Zhenfei%20Zhang.md)
+ Yuncong Zhang
+ Wenqing Hu
+ [Ye Zhang](Ye%20Zhang.md)
## 笔记

In this paper, we explore a novel Zero-knowledge Virtual Machine (zkVM) framework leveraging succinct, non-interactive zero-knowledge proofs for verifiable computation over any code. Our approach divides the proof of program execution into two stages. In the first stage, the process breaks down program execution into segments, identifying and grouping identical sections. These segments are then proved through data-parallel circuits that allow for varying amounts of duplication. In the subsequent stage, the verifier examines these segment proofs, reconstructing the program’s control and data flow based on the segments’ duplication number and the original program. The second stage can be further attested by a uniform recursive proof. We propose two specific designs of this concept, where segmentation and parallelization occur at two levels: opcode and basic block. Both designs try to minimize the control flow that affects the circuit size and support dynamic copy numbers, ensuring that computational costs directly correlate with the actual code executed (i.e., you only pay as much as you use). In our second design, in particular, by proposing an innovative data-flow reconstruction technique in the second stage, we can drastically cut down on the stack operations even compared to the original program execution. Note that the two designs are complementary rather than mutually exclusive. Integrating both approaches in the same zkVM could unlock more significant potential to accommodate various program patterns. We present an asymmetric GKR scheme to implement our designs, pairing a non-uniform prover and a uniform verifier to generate proofs for dynamic-length data-parallel circuits. The use of a GKR prover also significantly reduces the size of the commitment. GKR allows us to commit only the circuit’s input and output, whereas in Plonkish-based solutions, the prover needs to commit to all the witnesses.

以下是中文翻译：

在本文中，我们探讨了一种新颖的零知识虚拟机（Zero-knowledge Virtual Machine，zkVM）框架，该框架利用简洁的非交互式零知识证明（non-interactive zero-knowledge proofs）实现对任意代码的可验证计算。我们的方法将程序执行的证明分为两个阶段。在第一阶段，过程将程序执行分解为多个片段，识别并分组相同的部分。这些片段通过数据并行电路（data-parallel circuits）进行证明，允许不同数量的重复。在随后的阶段中，验证者检查这些片段证明，根据片段的重复数量和原始程序重建程序的控制流和数据流。第二阶段可以通过统一的递归证明（uniform recursive proof）进一步验证。我们提出了该概念的两种具体设计，其中分段和并行化在两个层面上进行：操作码（opcode）和基本块（basic block）。这两种设计都旨在最小化影响电路大小的控制流，并支持动态复制数量，确保计算成本与实际执行的代码直接相关（即，您只需为使用的部分付费）。特别是在我们的第二种设计中，通过在第二阶段提出一种创新的数据流重建技术，我们能够显著减少堆栈操作，甚至相较于原始程序执行。需要注意的是，这两种设计是互补的，而非相互排斥的。在同一zkVM中整合这两种方法可能会释放出更大的潜力，以适应各种程序模式。我们提出了一种不对称的GKR方案来实现我们的设计，将非均匀的证明者（non-uniform prover）与均匀的验证者（uniform verifier）配对，以生成动态长度数据并行电路的证明。使用GKR证明者还显著减少了承诺的大小。GKR允许我们仅对电路的输入和输出进行承诺，而在基于Plonkish的解决方案中，证明者需要对所有见证（witnesses）进行承诺。

## 关键词

+ Ceno零知识虚拟机zkVM
+ 非均匀分段并行零知识证明
+ 数据并行电路程序执行证明
+ GKR方案非均匀证明者
+ 操作码基本块层级分段
+ 可验证计算任意代码