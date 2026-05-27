---
title: "Atomic and fair data exchange via blockchain"
doi: 10.1145/3658644.3690248
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2024
---
## Atomic and fair data exchange via blockchain

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3658644.3690248)

## 作者

+ Ertem Nusret Tas 
+ István András Seres 
+ [Yinuo Zhang](Yinuo%20Zhang.md)
+ Márk Melczer 
+ Mahimna Kelkar 
+ [Joseph Bonneau](Joseph%20Bonneau.md) 
+ Valeria Nikolaenko 


## 笔记

### 背景与动机
云数据存储市场价值高达数百亿美元，但当前的数据访问模式存在根本性的信任难题：订阅制要求客户预先付费，完全依赖服务商的信誉来交付数据，而利他性分享模式（如 BitTorrent）则缺乏经济激励，导致搭便车问题。区块链虽能提供不可篡改的数据存储，但其链上容量极度受限——在以太坊上存储 1MB 数据的成本约为 2100 美元，这使得将大量数据直接写入区块链的方案不可行。现有的 Layer-2 解决方案（如 rollups）通过提交数据承诺并利用可检索性证明来激励存储，但它们都缺少一种机制来激励服务器在收到请求时实际传输数据。换言之，服务器只有存储的动机，没有提供数据的动机，导致数据虽被存储却难以被访问。本文旨在填补这一空白，设计一个区块链公平数据交换（FDE）协议，使得客户仅在收到完整数据时才向服务器支付款项，反之服务器也仅在收到付款时才泄露数据，并且协议的主链通信开销为常数，不随数据规模增长。

### 相关工作

[3] Asokan et al. Optimistic Fair Exchange of Digital Signatures. **EUROCRYPT 1998** [Google Scholar](https://scholar.google.com/scholar?q=Optimistic+Fair+Exchange+of+Digital+Signatures)
> 核心思路：引入可信第三方（TTP）用于争议解决，在无争议时无需 TTP 参与，实现乐观公平交换。
> 局限与区别：依赖于一个持有秘密的 TTP，无法直接迁移到公开透明的区块链环境中；我们的方案将区块链作为透明支付环境，且 TTP 不接触任何秘密。

[31] Dziembowski et al. FairSwap: How To Fairly Exchange Digital Goods. **CCS 2018** [Google Scholar](https://scholar.google.com/scholar?q=FairSwap+How+FairSwap +如何+Fair+FairSwap + 如何处理+Fair+FairSwap 的论文研究如何* 处理 +** 本文区别**值的论文* * **/ 以及** …[**'*' s 乃拓展了我们的价格以及** [ 号笔记 +* …: ( 并采用以下 [ 个*


## 关键词

+ 公平数据交换
+ 可验证加密
+ 区块链原子交换
+ 数据可用性
+ KZG多项式承诺

