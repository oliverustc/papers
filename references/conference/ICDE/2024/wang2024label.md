---
title: "Label Noise Correction for Federated Learning: A Secure, Efficient and Reliable Realization"
doi: 10.1109/icde60146.2024.00277
标题简称:
论文类型: conference
会议简称: ICDE
发表年份: 2024
created: 2025-04-16 10:18:15
modified: 2025-04-22 11:31:14
---
## Label Noise Correction for Federated Learning: A Secure, Efficient and Reliable Realization

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/10597841)

## 作者

+ Haodi Wang 
+ Tangyu Jiang 
+ [Yu Guo](Yu%20Guo.md)
+ Fangda Guo 
+ Rongfang Bie 
+ Xiaohua Jia 

## 笔记

Federated learning has emerged as a promising paradigm for large-scale collaborative training tasks, harnessing diverse local datasets from different clients to jointly train global models. In real-world implementations, client data could have label noise, causing the quality of the global model to be influenced. Existing label-correction solutions assume all the clients are discreet and fail to consider detecting the malicious clients, thus are not practical or privacy-preserving. In this paper, we present zkCor, an efficient and reliable label noise correction scheme with zero-knowledge confidentiality. Our method is designed upon FedCorr [1], but with more relaxed security assumptions. zkCor is established from the ingenious synergy of the label noise correction protocol and the zero-knowledge proof (ZKP), requiring each client to provide a computation integrity proof to the aggregator in each iteration. Thus, clients are forced to jointly guarantee label-correction reliability. We further devise a batch ZKP that is efficient and more suitable for federated learning settings. We rigorously illustrate the building blocks of zkCor and complete the prototype implementation. The extensive experiments demonstrate that zkCor can gain at least 2 to 30 times better performance than the baseline approach on verification workloads with nearly no extra proof time cost from clients.  

以下是中文翻译：

联邦学习作为一种有前景的大规模协作训练范式，通过整合不同客户端的多样化本地数据集来联合训练全局模型。在实际应用中，客户端数据可能存在标签噪声，从而影响全局模型质量。现有标签校正方案均假设所有客户端行为规范，未考虑恶意客户端的检测问题，既缺乏实用性又难以保障隐私安全。本文提出zkCor——一种基于零知识保密机制的高效可靠标签噪声校正方案。我们的方法基于FedCorr[1]构建，但采用了更宽松的安全假设。zkCor通过标签噪声校正协议与零知识证明（ZKP）的精妙协同，要求每个客户端在每次迭代时向聚合器提交计算完整性证明，从而强制所有客户端共同保障标签校正的可靠性。我们进一步设计了适用于联邦学习场景的高效批量ZKP方案，完整阐述了zkCor的构建模块并实现了原型系统。大量实验表明，在验证工作量方面，zkCor相比基线方法可获得至少2至30倍的性能提升，且客户端几乎无需承担额外的证明时间成本。

## 关键词

+ 联邦学习
+ 标签噪声校正
+ 零知识证明
+ 计算完整性证明
+ 隐私保护机器学习
+ 批量ZKP