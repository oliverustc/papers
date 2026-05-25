---
title: "AntMan: Interactive Zero-Knowledge Proofs with Sublinear Communication"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2022
modified: 2025-04-09 16:11:16
---

## AntMan: Interactive Zero-Knowledge Proofs with Sublinear Communication

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3548606.3560667)

## 作者

+ 

## 笔记

Recent works on interactive zero-knowledge (ZK) protocols provide a new paradigm with high efficiency and scalability. However, these protocols suffer from high communication overhead, often linear to the circuit size. In this paper, we proposed two new ZK protocols with communication sublinear to the circuit size, while maintaining a similar level of computational efficiency.
(1) We designed a ZK protocol that can prove B executions of any circuit C in communication O(B + |C|) field elements (with free addition gates), while the best prior work requires a communication of O(B|C|) field elements. Our protocol is enabled by a new tool called as information-theoretic polynomial authentication code, which may be of independent interest.
(2) We developed an optimized implementation of this protocol which shows high practicality. For example, with B=2048, |C|=221, and under 50 Mbps bandwidth and 16 threads, QuickSilver, a state-of-the-art ZK protocol based on vector oblivious linear evaluation (VOLE), can only prove 0.71 million MULT gates per second (mgps) and send one field element per gate; our protocol can prove 15.74 mgps (22x improvement) and send 0.0061 field elements per gate (164x improvement) under the same hardware configuration.
(3) Extending the above idea, we constructed a ZK protocol that can prove a single execution of any circuit C in communication O(|C|3/4). This is the first ZK protocol with sublinear communication for an arbitrary circuit in the VOLE-based ZK family.

以下是中文翻译：

近期关于交互式零知识（ZK）协议的研究提供了一种具有高效率和可扩展性的新范式。然而，这些协议存在较高的通信开销问题，通常与电路规模呈线性关系。在本文中，我们提出了两种新的零知识协议，它们的通信复杂度低于电路规模的线性关系，同时保持了类似的计算效率水平。

(1) 我们设计了一个零知识协议，可以在通信复杂度为O(B + |C|)个域元素（加法门免费）的情况下证明任意电路C的B次执行，而之前最好的工作需要O(B|C|)个域元素的通信量。我们的协议得益于一个新工具，称为信息论多项式认证码（information-theoretic polynomial authentication code），这可能具有独立的研究价值。

(2) 我们开发了该协议的优化实现，显示出高度的实用性。例如，在B=2048，|C|=221的情况下，在50 Mbps带宽和16线程的条件下，基于向量不经意线性求值（VOLE）的最新零知识协议QuickSilver每秒只能证明71万个乘法门（mgps），且每个门需要发送一个域元素；而在相同硬件配置下，我们的协议每秒可以证明15.74百万个乘法门（提升22倍），每个门仅需发送0.0061个域元素（提升164倍）。

(3) 在上述思想的基础上，我们构建了一个可以在通信复杂度为O(|C|3/4)的情况下证明任意电路C的单次执行的零知识协议。这是基于VOLE的零知识协议族中首个针对任意电路实现亚线性通信复杂度的协议。

## 关键词

+ 零知识证明
+ 交互式协议
+ 通信复杂度
+ 电路验证
+ 密码学