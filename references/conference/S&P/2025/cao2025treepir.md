---
title: "TreePIR: Efficient Private Retrieval of Merkle Proofs via Tree Colorings with Fast Indexing and Zero Storage Overhead"
doi: 10.1109/sp61157.2025.00032
标题简称:
论文类型: conference
会议简称: S&P
发表年份: 2025
modified: 2025-04-13 14:19:40
---
## TreePIR: Efficient Private Retrieval of Merkle Proofs via Tree Colorings with Fast Indexing and Zero Storage Overhead

## 发表信息

+ [原文链接暂无]
+ [arxiv链接](https://arxiv.org/abs/2205.05211)

## 作者

+ Quang Cao 
+ Son Hoang Dau 
+ Rinaldo Gagiano 
+ Duy Huynh 
+ Xun Yi 
+ Phuc Lu Le 
+ Quang-Hung Luu 
+ Emanuele Viterbo 
+ Yu-Chih Huang 
+ Jingge Zhu 
+ others 

## 笔记

A Batch Private Information Retrieval (batch-PIR) scheme allows a client to retrieve multiple data items from a database without revealing them to the storage server(s). Most existing approaches for batch-PIR are based on batch codes, in particular, probabilistic batch codes (PBC) (Angel et al. S&P'18), which incur large storage overheads. In this work, we show that \textit{zero} storage overhead is achievable for tree-shaped databases. In particular, we develop TreePIR, a novel approach tailored made for private retrieval of the set of nodes along an arbitrary root-to-leaf path in a Merkle tree with no storage redundancy. This type of trees has been widely implemented in many real-world systems such as Amazon DynamoDB, Google's Certificate Transparency, and blockchains. Tree nodes along a root-to-leaf path forms the well-known Merkle proof. TreePIR, which employs a novel tree coloring, outperforms PBC, a fundamental component in state-of-the-art batch-PIR schemes (Angel et al. S&P'18, Mughees-Ren S&P'23, Liu et al. S&P'24), in all metrics, achieving 3× lower total storage and 1.5-2× lower computation and communication costs. Most notably, TreePIR has 8-160× lower setup time and its polylog-complexity indexing algorithm is 19-160× faster than PBC for trees of $2^{10}-2^{24}$ leaves.

以下是中文翻译：

批量私有信息检索(batch Private Information Retrieval, batch-PIR)方案允许客户端从数据库中检索多个数据项，而无需向存储服务器透露这些数据项的内容。目前大多数batch-PIR方案都基于批量编码，特别是概率批量编码(Probabilistic Batch Codes, PBC) (Angel等人 S&P'18)，但这些方案会产生较大的存储开销。在本研究中，我们证明对于树状数据库而言，可以实现零存储开销。

具体而言，我们开发了TreePIR，这是一种新颖的方法，专门用于在默克尔树(Merkle tree)中私密检索从根节点到叶节点路径上的所有节点，且无需额外存储冗余。这类树结构已在许多实际系统中得到广泛应用，如亚马逊DynamoDB、谷歌的证书透明度系统和区块链等。从根节点到叶节点路径上的树节点构成了众所周知的默克尔证明(Merkle proof)。

TreePIR采用了一种新颖的树着色方法，在所有指标上都优于PBC（PBC是当前最先进的batch-PIR方案中的基础组件，如Angel等人 S&P'18、Mughees-Ren S&P'23、Liu等人 S&P'24）。具体来说，TreePIR实现了总存储开销降低3倍，计算和通信成本降低1.5-2倍。最显著的是，TreePIR的设置时间降低了8-160倍，其多项式对数复杂度的索引算法在处理具有2^10-2^24个叶节点的树时，比PBC快19-160倍。

## 关键词

+ 批量私有信息检索
+ Merkle证明私密检索
+ 树着色算法
+ 零存储开销
+ 概率批量编码
+ 证书透明度隐私