---
title: "Verifiable Secret Sharing Simplified"
doi: 10.1109/sp61157.2025.00046
标题简称:
论文类型: conference
会议简称: S&P
发表年份: 2025
modified: 2025-04-13 14:22:51
---
## Verifiable Secret Sharing Simplified

## 发表信息

+ 

## 作者

+ [Sourav Das](Sourav%20Das.md)
+ [Zhuolun Xiang](Zhuolun%20Xiang.md)
+ [[Alin Tomescu]]
+ Alexander Spiegelman 
+ Benny Pinkas 
+ [Ling Ren](Ling%20Ren.md)
## 笔记

Verifiable Secret Sharing (VSS) is a fundamental building block in cryptography. Despite its importance and extensive studies, existing VSS protocols are often complex and inefficient. Many of them do not support dual thresholds, are not publicly verifiable, or do not properly terminate in asynchronous networks. This paper presents a new and simple approach for designing VSS protocols in synchronous and asynchronous networks. Our VSS protocols are optimally fault-tolerant, i.e., they tolerate a 1/2 and a 1/3 fraction of malicious nodes in synchronous and asynchronous networks, respectively. They only require a public key infrastructure and the hardness of discrete logarithms. Our protocols support dual thresholds, and their transcripts are publicly verifiable. We implement our VSS protocols and evaluate them in a geo-distributed setting with up to 256 nodes. The evaluation demonstrates that our protocols offer asynchronous termination and public verifiability with performance that is comparable to that of existing schemes that lack these features. Compared to the existing schemes with similar guarantees, our approach lowers the bandwidth usage and latency by up to 90%.

以下是中文翻译：

可验证秘密共享（VSS）是密码学中的一项基础构建技术。尽管其重要性已被广泛研究，但现有的VSS协议往往复杂且效率低下。许多协议不支持双阈值，不具备公开可验证性，或在异步网络中无法正确终止。本文提出了一种新颖而简洁的方法，用于设计同步与异步网络中的VSS协议。我们的VSS协议具有最优容错能力，即在同步和异步网络中分别能容忍1/2和1/3比例的恶意节点。仅需依赖公钥基础设施及离散对数难题的假设，我们的协议即支持双阈值，且其交易记录公开可验证。 我们实现了这些VSS协议，并在最多包含256个节点的地理分布式环境中进行了评估。评估结果表明，我们的协议在保持与缺乏这些特性的现有方案相当性能的同时，提供了异步终止和公开可验证性。与具备相似保证的现有方案相比，我们的方法将带宽使用和延迟降低了高达90%。

## 关键词

+ 可验证秘密共享VSS
+ 双阈值协议
+ 公开可验证性
+ 异步网络容错
+ 离散对数假设
+ 分布式密钥生成