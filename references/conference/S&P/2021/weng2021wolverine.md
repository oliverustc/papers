---
title: "Wolverine: Fast, Scalable, and Communication-Efficient Zero-Knowledge Proofs for Boolean and Arithmetic Circuits"
标题简称:
论文类型: conference
会议简称: S&P
发表年份: 2021
modified: 2025-04-09 16:06:03
---

## Wolverine: Fast, Scalable, and Communication-Efficient Zero-Knowledge Proofs for Boolean and Arithmetic Circuits

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/9519498)

## 作者

+ [Chenkai Weng](Chenkai%20Weng.md)
+ [Kang Yang](Kang%20Yang.md)
+ [Jonathan Katz](Jonathan%20Katz.md)
+ [Xiao Wang](Xiao%20Wang.md)

## 笔记

Efficient zero-knowledge (ZK) proofs for arbitrary boolean or arithmetic circuits have recently attracted much attention. Existing solutions suffer from either significant prover overhead (i.e., high memory usage) or relatively high communication complexity (at least κ bits per gate, for computational security parameter κ). In this paper, we propose a new protocol for constant-round interactive ZK proofs that simultaneously allows for an efficient prover with asymptotically optimal memory usage and significantly lower communication compared to protocols with similar memory efficiency. Specifically:•The prover in our ZK protocol has linear running time and, perhaps more importantly, memory usage linear in the memory needed to evaluate the circuit non-cryptographically. This allows our proof system to scale easily to very large circuits.•for statistical security parameter ρ = 40, our ZK protocol communicates roughly 9 bits/gate for boolean circuits and 2–4 field elements/gate for arithmetic circuits over large fields.Using 5 threads, 400 MB of memory, and a 200 Mbps network to evaluate a circuit with hundreds of billions of gates, our implementation (ρ = 40, κ = 128) runs at a rate of 0.45 μs/gate in the boolean case, and 1.6 μs/gate for an arithmetic circuit over a 61-bit field.We also present an improved subfield Vector Oblivious Linear Evaluation (sVOLE) protocol with malicious security that is of independent interest.

以下是中文翻译：

高效的零知识（ZK）证明对于任意布尔或算术电路最近引起了广泛关注。现有的解决方案要么面临显著的证明者开销（即高内存使用），要么具有相对较高的通信复杂度（对于计算安全参数κ，每个门至少需要κ位）。在本文中，我们提出了一种新的协议，用于常数轮交互式零知识证明，该协议同时支持高效的证明者，具有渐近最优的内存使用，并且相比于具有类似内存效率的协议，通信显著降低。具体而言：

• 我们的零知识协议中的证明者具有线性运行时间，并且更重要的是，内存使用量与评估电路所需的非密码学内存呈线性关系。这使得我们的证明系统能够轻松扩展到非常大的电路。

• 对于统计安全参数ρ = 40，我们的零知识协议对于布尔电路的通信大约为每个门9位，对于大域上的算术电路则为每个门2-4个域元素。

使用5个线程、400 MB内存和200 Mbps网络来评估一个包含数百亿个门的电路时，我们的实现（ρ = 40，κ = 128）在布尔情况下的运行速率为0.45 μs/门，而在61位域上的算术电路中为1.6 μs/门。我们还提出了一种改进的子域向量不可知线性评估（sVOLE）协议，具有恶意安全性，具有独立的研究价值。

## 关键词

+ 零知识交互式证明
+ 线性内存零知识
+ sVOLE协议
+ 布尔电路证明
+ 算术电路证明
+ 大规模电路可扩展性