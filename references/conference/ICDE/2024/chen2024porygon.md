---
title: "Porygon: Scaling blockchain via 3d parallelism"
标题简称: 
论文类型: conference
会议简称: ICDE
发表年份: 2024
created: 2025-04-19 10:55:44
modified: 2025-04-21 00:53:32
---

## Porygon: Scaling blockchain via 3d parallelism

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/10597933)

## 作者

+ Wuhui Chen 
+ Ding Xia 
+ Zhongteng Cai 
+ Hong-Ning Dai 
+ Jianting Zhang 
+ Zicong Hong 
+ Junyuan Liang 
+ Zibin Zheng 

## 笔记

Recently, stateless blockchains have been proposed to alleviate the storage overhead for nodes. A stateless blockchain achieves storage-consensus parallelism, where storage workloads are offloaded from on-chain consensus, enabling more resource-constraint nodes to participate in the consensus. However, existing stateless blockchains still suffer from limited throughput. In this paper, we present Porygon, a novel stateless blockchain with three-dimensional (3D) parallelism. First, Porygon separates the storage and consensus of transactions as the stateless blockchain, achieving the storage-consensus parallelism. This first-dimensional parallelism divides the processing of transactions into several stages and scales the network by supporting more nodes in the system. Based on such a design, we then propose a pipeline mechanism to achieve second-dimensional inter-block parallelism, where relevant stages of processing transactions are pipelined efficiently, thereby reducing transaction latency. Finally, Porygon presents a sharding mechanism to achieve third-dimensional inner-block parallelism. By sharding the executions of transactions of a block and adopting a lightweight cross-shard coordination mechanism, Porygon can effectively execute both intra-shard and cross-shard transactions, consequently achieving outstanding transaction throughput. We evaluate the performance of Porygon by extensive experiments on an implemented prototype and large-scale simulations. Compared with existing blockchains, Porygon boosts throughput by up to 20x, reduces network usage by more than 50%, and simultaneously requires only 5MB of storage consumption per node.

以下是中文翻译：

最近，提出了无状态区块链（stateless blockchain）以减轻节点的存储开销。无状态区块链实现了存储与共识的并行性（storage-consensus parallelism），将存储工作负载从链上共识中卸载，使得更多资源受限的节点能够参与共识。然而，现有的无状态区块链仍然面临有限的吞吐量问题。本文提出了Porygon，一种新颖的无状态区块链，具有三维并行性（3D parallelism）。首先，Porygon将交易的存储与共识分离，作为无状态区块链，实现了存储与共识的并行性。这一维度的并行性将交易处理分为多个阶段，并通过支持系统中的更多节点来扩展网络。基于这样的设计，我们进一步提出了一种流水线机制，以实现第二维度的区块间并行性（inter-block parallelism），在这一过程中，相关的交易处理阶段被高效地流水线化，从而减少交易延迟。最后，Porygon提出了一种分片机制，以实现第三维度的区块内并行性（inner-block parallelism）。通过对区块内交易的执行进行分片，并采用轻量级的跨分片协调机制，Porygon能够有效地执行区块内和跨分片的交易，从而实现卓越的交易吞吐量。我们通过对实现原型和大规模模拟的广泛实验评估Porygon的性能。与现有区块链相比，Porygon的吞吐量提高了最多20倍，网络使用率减少了50%以上，同时每个节点的存储消耗仅需5MB。

## 关键词

+ 无状态区块链
+ 三维并行性
+ 流水线机制
+ 分片机制
+ 区块链可扩展性
+ 交易吞吐量