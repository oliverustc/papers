---
title: "Kronos: A secure and generic sharding blockchain consensus with optimized overhead"
标题简称: 
论文类型: conference
会议简称: NDSS
发表年份: 2025
modified: 2025-04-13 16:40:42
---

## Kronos: A secure and generic sharding blockchain consensus with optimized overhead

## 发表信息

+ [原文链接](https://www.ndss-symposium.org/ndss-paper/kronos-a-secure-and-generic-sharding-blockchain-consensus-with-optimized-overhead/)
+ [archive](https://eprint.iacr.org/2024/206)

## 作者

+ Yizhong Liu 
+ Andi Liu 
+ Yuan Lu 
+ Zhuocheng Pan 
+ Yinuo Li 
+ Jianwei Liu 
+ Song Bian 
+ Mauro Conti 

## 笔记

Sharding enhances blockchain scalability by dividing the network into shards, each managing specific unspent transaction outputs or accounts. As an introduced new transaction type, cross-shard transactions pose a critical challenge to the security and efficiency of sharding blockchains.
Currently, there is a lack of a generic sharding blockchain consensus pattern that achieves both security and low overhead.

In this paper, we present Kronos, a secure sharding blockchain consensus achieving optimized overhead.
In particular, we propose a new textit{secure sharding blockchain consensus pattern}, based on a textit{buffer} managed jointly by shard members. Valid transactions are transferred to the payee via the buffer, while invalid ones are rejected through happy or unhappy paths.
Kronos is proved to achieve textit{security} textit{with atomicity} under malicious clients while maintaining textit{optimal intra-shard overhead}. Efficient rejection even requires no Byzantine fault tolerance (BFT) protocol execution in happy paths, and the cost in unhappy paths is still not higher than a two-phase commit.
Besides, we propose secure cross-shard certification methods. Handling $b$ transactions, Kronos is proved to achieve cross-shard communication with low textit{cross-shard overhead} $mathcal{O}(n b lambda)$ ($n$ for the shard size and $lambda$ for the security parameter).
Notably, Kronos imposes no restrictions on BFT and does not rely on timing assumptions, offering optional constructions in various modules. Kronos could serve as a universal framework for enhancing the performance and scalability of existing BFT protocols. Kronos supports generic models, including asynchronous networks, and can increase the throughput by several orders of magnitude.

We implement Kronos using two prominent BFT protocols: asynchronous Speeding Dumbo (NDSS'22) and partially synchronous Hotstuff (PODC'19). Extensive experiments (over up to 1000 AWS EC2 nodes across 4 AWS regions) demonstrate Kronos scales the consensus nodes to thousands, achieving a substantial throughput of 320 ktx/sec with 2.0 sec latency. Compared with the past solutions, Kronos outperforms, achieving up to a 12$times$ improvement in throughput and a 50% reduction in latency when cross-shard transactions dominate the workload.

以下是中文翻译：

分片技术通过将区块链网络划分为多个分片，每个分片管理特定的未花费交易输出或账户，从而增强了区块链的可扩展性。作为一种新引入的交易类型，跨分片交易对分片区块链的安全性和效率构成了重大挑战。目前，尚缺乏一种通用的分片区块链共识模式，能够同时实现安全性和低开销。

在本文中，我们提出了Kronos，一种实现优化开销的安全分片区块链共识。具体而言，我们提出了一种新的 $\textit{安全分片区块链共识模式}$，该模式基于由分片成员共同管理的 $\textit{缓冲区}$。有效的交易通过缓冲区转移给收款方，而无效的交易则通过快乐路径或不快乐路径被拒绝。Kronos被证明在恶意客户端下能够实现 $\textit{具有原子性的安全性}$，同时保持 $\textit{最佳的分片内开销}$。有效的拒绝甚至在快乐路径中无需执行拜占庭容错（BFT）协议，而在不快乐路径中的成本也不高于两阶段提交。

此外，我们还提出了安全的跨分片认证方法。在处理$b$笔交易时，Kronos被证明能够以低 $\textit{跨分片开销}$ $O(n b \lambda)$（其中$n$为分片大小，$\lambda$为安全参数）实现跨分片通信。值得注意的是，Kronos对BFT没有任何限制，也不依赖于时间假设，提供了各种模块中的可选构造。Kronos可以作为一个通用框架，增强现有BFT协议的性能和可扩展性。Kronos支持通用模型，包括异步网络，并可以将吞吐量提高几个数量级。

我们使用两种著名的BFT协议实现了Kronos：异步Speeding Dumbo（NDSS'22）和部分同步Hotstuff（PODC'19）。大量实验（在4个AWS区域的1000个AWS EC2节点上进行）表明，Kronos能够将共识节点扩展到数千个，达到320 ktx/sec的显著吞吐量，延迟为2.0秒。与过去的解决方案相比，Kronos在吞吐量上实现了高达12$times$的提升，并在跨分片交易占主导地位时减少了50%的延迟。

## 关键词

+ 分片区块链共识
+ 跨分片交易
+ 拜占庭容错
+ 区块链可扩展性
+ 原子性安全
+ 异步网络