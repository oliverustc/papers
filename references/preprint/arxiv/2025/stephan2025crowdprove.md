---
title: "CrowdProve: Community Proving for ZK Rollups"
标题简称:
论文类型: preprint
预印本简称: arxiv
发表年份: 2025
modified: 2025-04-09 14:06:01
---

## CrowdProve: Community Proving for ZK Rollups

## 发表信息

+ [原文链接](https://arxiv.org/abs/2501.03126)

## 作者

+ John Stephan
+ Matej Pavlovic
+ Antonio Locascio
+ Benjamin Livshits

## 笔记

Zero-Knowledge (ZK) rollups have become a popular solution for scaling blockchain systems, offering improved transaction throughput and reduced costs by aggregating Layer 2 transactions and submitting them as a single batch to a Layer 1 blockchain. However, the computational burden of generating validity proofs, a key feature of ZK rollups, presents significant challenges in terms of performance and decentralization. Current solutions rely on centralized infrastructure to handle the computational tasks, limiting the scalability and decentralization of rollup systems.
This paper proposes CrowdProve, a prover orchestration layer for outsourcing computation to unreliable commodity hardware run by a broad community of small provers. We apply CrowdProve to proving transaction batches for a popular ZK rollup.
Through our experimental evaluation, we demonstrate that community proving can achieve performance comparable to, and in some cases better than, existing centralized deployments. Our results show that even systems utilizing modest hardware configurations can match the performance of centralized solutions, making community-based proof generation a viable and cost-effective alternative. CrowdProve allows both the rollup operator and community participants to benefit: the operator reduces infrastructure costs by leveraging idle community hardware, while community provers are compensated for their contributions.

以下是中文翻译：

零知识证明（Zero-Knowledge, ZK）卷叠已成为区块链系统扩容的流行解决方案。通过聚合二层（Layer 2）交易并将其作为单个批次提交到一层（Layer 1）区块链，它可以提高交易吞吐量并降低成本。然而，生成有效性证明（这是ZK卷叠的一个关键特性）所带来的计算负担在性能和去中心化方面带来了重大挑战。目前的解决方案依赖于中心化基础设施来处理计算任务，这限制了卷叠系统的可扩展性和去中心化程度。

本文提出了CrowdProve，这是一个证明者编排层（prover orchestration layer），用于将计算任务外包给由广大小型证明者社区运行的不可靠商用硬件。我们将CrowdProve应用于为一个流行的ZK卷叠生成交易批次证明。

通过我们的实验评估，我们证明社区证明可以达到与现有中心化部署相当，在某些情况下甚至更好的性能。我们的结果表明，即使使用普通硬件配置的系统也能够匹配中心化解决方案的性能，使基于社区的证明生成成为一个可行且具有成本效益的替代方案。CrowdProve使卷叠运营商和社区参与者都能受益：运营商通过利用社区闲置硬件降低基础设施成本，而社区证明者则因其贡献获得补偿。

## 关键词

+ CrowdProve社区证明ZK卷叠
+ 证明者编排外包计算去中心化
+ 商用硬件区块链扩容方案
+ ZK卷叠有效性证明生成
+ 去中心化证明者激励机制