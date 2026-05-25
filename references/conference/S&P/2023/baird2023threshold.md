---
title: "Threshold signatures in the multiverse"
标题简称:
论文类型: conference
会议简称: S&P
发表年份: 2023
created: 2025-04-17 10:41:54
modified: 2025-04-17 10:42:38
---

## Threshold signatures in the multiverse

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/10179436)

## 作者

+ Leemon Baird 
+ [Sanjam Garg](Sanjam%20Garg.md) 
+ [Abhishek Jain](Abhishek%20Jain.md)
+ [Pratyay Mukherjee](Pratyay%20Mukherjee.md) 
+ Rohit Sinha 
+ [Mingyuan Wang](Mingyuan%20Wang.md) 
+ [Yinuo Zhang](Yinuo%20Zhang.md)
## 笔记

We introduce a new notion of multiverse threshold signatures (MTS). In an MTS scheme, multiple universes – each defined by a set of (possibly overlapping) signers, their weights, and a specific security threshold – can co-exist. A universe can be (adaptively) created via a non-interactive asynchronous setup. Crucially, each party in the multiverse holds constant-sized keys and releases compact signatures with size and computation time both independent of the number of universes. Given sufficient partial signatures over a message from the members of a specific universe, an aggregator can produce a short aggregate signature relative to that universe.We construct an MTS scheme building on BLS signatures. Our scheme is practical, and can be used to reduce bandwidth complexity and computational costs in decentralized oracle networks. As an example data point, consider a multiverse containing 2000 nodes and 100 universes (parameters inspired by Chainlink’s use in the wild), each of which contains arbitrarily large subsets of nodes and arbitrary thresholds. Each node computes and outputs 1 group element as its partial signature; the aggregator performs under 0.7 seconds of work for each aggregate signature, and the final signature of size 192 bytes takes 6.4 ms (or 198K EVM gas units) to verify. For this setting, prior approaches, when used to construct MTS, yield schemes that have one of the following drawbacks: (i) partial signatures that are 48× larger, (ii) have aggregation times 311× worse, or (iii) have signature size 39× and verification gas costs 3.38× larger. We also provide an open-source implementation and a detailed evaluation.

以下是中文翻译：

我们引入了一种新的多元阈值签名（Multiverse Threshold Signatures, MTS）概念。在MTS方案中，多个宇宙——每个宇宙由一组（可能重叠的）签名者、他们的权重以及特定的安全阈值定义——可以共存。一个宇宙可以通过非交互式异步设置（non-interactive asynchronous setup）进行（自适应）创建。关键是， multiverse中的每个参与方都持有固定大小的密钥，并释放其大小和计算时间均与宇宙数量无关的紧凑签名。给定来自特定宇宙成员的足够部分签名，聚合器可以生成相对于该宇宙的短聚合签名。

我们构建了一个基于BLS签名的MTS方案。我们的方案是实用的，可以用于降低去中心化预言机网络中的带宽复杂性和计算成本。作为一个示例数据点，考虑一个包含2000个节点和100个宇宙的多元宇宙（这些参数受到Chainlink在实际应用中的启发），每个宇宙包含任意大的节点子集和任意的阈值。每个节点计算并输出1个组元素作为其部分签名；聚合器在每个聚合签名上工作不超过0.7秒，最终签名的大小为192字节，验证时间为6.4毫秒（或198K EVM气体单位）。在这种设置下，之前的方法在用于构建MTS时，会产生以下缺陷之一：（i）部分签名大48倍，（ii）聚合时间差311倍，或（iii）签名大小大39倍且验证气体成本大3.38倍。我们还提供了一个开源实现和详细评估。

## 关键词

+ 多元阈值签名
+ BLS签名
+ 去中心化预言机网络
+ 聚合签名
+ 非交互式异步设置
+ 加权阈值