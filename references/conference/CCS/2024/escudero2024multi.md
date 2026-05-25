---
title: "Multi-Verifier Zero-Knowledge Proofs for Any Constant Fraction of Corrupted Verifiers"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2024
modified: 2025-04-21 08:47:11
created: 2025-04-09 16:01:44
---

## Multi-Verifier Zero-Knowledge Proofs for Any Constant Fraction of Corrupted Verifiers

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3658644.3670357)

## 作者

+ Daniel Escudero
+ Antigoni Polychroniadou
+ Yifan Song
+ [Chenkai Weng](Chenkai%20Weng.md)

## 笔记

In this work we study the efficiency of Zero-Knowledge (ZK) arguments of knowledge, particularly exploring Multi-Verifier ZK (MVZK) protocols as a midway point between Non-Interactive ZK and Designated-Verifier ZK, offering versatile applications across various domains. We introduce a new MVZK protocol designed for the preprocessing model, allowing any constant fraction of verifiers to be corrupted, potentially colluding with the prover. Our contributions include the first MVZK over rings. Unlike recent prior works on fields in the dishonest majority case, our protocol demonstrates communication complexity independent of the number of verifiers, contrasting the linear complexity of previous approaches. This key advancement ensures improved scalability and efficiency. We provide an end-to-end implementation of our protocol. The benchmark shows that it achieves a throughput of 1.47 million gates per second for 64 verifiers with 50% corruption, and 0.88 million gates per second with 75% corruption.

以下是中文翻译：

在本研究中，我们探讨了零知识（Zero-Knowledge, ZK）知识论证的效率，特别是研究多验证者零知识（Multi-Verifier ZK, MVZK）协议，作为非交互式零知识（Non-Interactive ZK）和指定验证者零知识（Designated-Verifier ZK）之间的一个中间点，提供了在各个领域的多样化应用。我们提出了一种新的MVZK协议，旨在预处理模型中，允许任何常数比例的验证者被攻击，可能与证明者（prover）串通。我们的贡献包括第一个基于环的MVZK协议。与最近在不诚实多数情况下对域的研究不同，我们的协议展示了通信复杂性与验证者数量无关，这与之前方法的线性复杂性形成对比。这一关键进展确保了更好的可扩展性和效率。我们提供了该协议的端到端实现。基准测试显示，在50%腐败率下，64个验证者的吞吐量达到每秒147万门电路，在75%腐败率下，吞吐量为每秒88万门电路。

## 关键词

+ 多验证者零知识证明
+ 预处理模型
+ 通信复杂度
+ 腐败验证者
+ 环上零知识证明
+ 可扩展性