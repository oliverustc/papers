---
title: "Tight zk cpu: Batched zk branching with cost proportional to evaluated instruction"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2024
created: 2025-04-20 20:05:58
modified: 2025-04-20 20:07:04
---

## Tight zk cpu: Batched zk branching with cost proportional to evaluated instruction

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3658644.3690289)

## 作者

+ Yibin Yang 
+ David Heath 
+ [Carmit Hazay](Carmit%20Hazay.md)
+ Vladimir Kolesnikov 
+ [Muthuramakrishnan Venkitasubramaniam](Muthuramakrishnan%20Venkitasubramaniam.md)
## 笔记

We explore Zero-Knowledge Proofs (ZKPs) of statements expressed as programs written in high-level languages, e.g., C or assembly. At the core of executing such programs in ZK is the repeated evaluation of a CPU step, achieved by branching over the CPU's instruction set. This approach is general and covers traversal-execution of a program's control flow graph (CFG): here CPU instructions are straight-line program fragments (of various sizes) associated with the CFG nodes. This highlights the usefulness of ZK CPUs with a _large_ number of instructions of _varying sizes._

We formalize and design an efficient _tight_ ZK CPU, where the cost (both computation and communication, for each party) of each step depends only on the instruction taken. This qualitatively improves over state of the art, where cost scales with the size of the _largest_ CPU instruction (largest CFG node).

Our technique is formalized in the standard commit-and-prove paradigm, so our results are compatible with a variety of (interactive and non-interactive) general-purpose ZK.

We implemented an interactive tight arithmetic (over F261-1) ZK CPU based on _Vector Oblivious Linear Evaluation_ (VOLE) and compared it to the state-of-the-art non-tight VOLE-based ZK CPU Batchman (Yang et al. CCS'23). In our experiments, under the same hardware configuration, we achieve comparable performance when instructions are of the same size and a 5-18× improvement when instructions are of varied size. Our VOLE-based tight ZK CPU (over F261-1) can execute 100K (resp. 450K) multiplication gates per second in a WAN-like (resp. LAN-like) setting. It requires ≤ 102 Bytes per multiplication gate. Our basic building block, ZK _Unbalanced Read-Only Memory,_ may be of independent interest.

以下是中文翻译：

我们探讨了以高级语言（例如 C 或汇编语言）编写的程序表示的语句的零知识证明 （ZKP）。在 ZK 中执行此类程序的核心是对 CPU 步骤的重复评估，通过分支 CPU 的指令集来实现。这种方法是通用的，涵盖了程序控制流图 （CFG） 的遍历执行：这里的 CPU 指令是与 CFG 节点关联的直线程序片段（各种大小）。这突出了具有大量不同大小指令的 ZK CPU 的有用性。

我们形式化并设计了一个高效的紧密 ZK CPU，其中每一步的成本（计算和通信，对于每一方）仅取决于所采取的指令。这在定性上改进了最先进的技术，其中成本随着最大 CPU 指令（最大 CFG 节点）的大小而扩展。

我们的技术以标准提交和证明范例进行正式化，因此我们的结果与各种（交互式和非交互式）通用 ZK 兼容。

我们实现了一个基于矢量遗忘线性评估 （VOLE） 的交互式紧密算术 （over F2-1） ZK CPU，并将其与最先进的基于 VOLE 的非紧密 ZK CPU Batchman （Yang et al. CCS'23） 进行了比较。在我们的实验中，在相同的硬件配置下，当指令大小相同时，我们实现了相当的性能，当指令大小不同时，我们实现了 5-18× 的改进。我们基于 VOLE 的紧密 ZK CPU（超过 F2-1）可以在类似 WAN（或类似 LAN）的设置中每秒执行 100K（或 450K）乘法门。每个乘法门≤ 102 字节。我们的基本构建块 ZKUnbalanced Read-Only Memory 可能具有独立的兴趣。

## 关键词

+ 零知识证明
+ ZK CPU
+ 指令执行
+ VOLE
+ 控制流图