---
title: "Aggregatable distributed key generation"
标题简称:
论文类型: conference
会议简称: EUROCRYPT
发表年份: 2021
created: 2025-05-12 09:16:31
modified: 2025-05-12 09:18:12
---

## Aggregatable distributed key generation

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-030-77870-5_6)

## 作者

+ Kobi Gurkan
+ [Philipp Jovanovic](Philipp%20Jovanovic.md)
+ [Mary Maller](Mary%20Maller.md)
+ [Sarah Meiklejohn](Sarah%20Meiklejohn.md)
+ Gilad Stern
+ [[Alin Tomescu]]

## 笔记

In this paper, we introduce a distributed key generation (DKG) protocol with aggregatable and publicly-verifiable transcripts. Compared with prior _publicly-verifiable_ approaches, our DKG reduces the size of the final transcript and the time to verify it from $O(n^2)$ to $O(n\log⁡n)$, where _n_ denotes the number of parties. As compared with prior non-publicly-verifiable approaches, our DKG leverages "gossip" rather than _all-to-all communication_ to reduce verification and communication complexity. We also revisit existing DKG security definitions, which are quite strong, and propose new and natural relaxations. As a result, we can prove the security of our aggregatable DKG as well as that of several existing DKGs, including the popular Pedersen variant. We show that, under these new definitions, these existing DKGs can be used to yield secure threshold variants of popular cryptosystems such as El-Gamal encryption and BLS signatures. We also prove that our DKG can be securely combined with a new efficient verifiable unpredictable function (VUF), whose security we prove in the random oracle model. Finally, we experimentally evaluate our DKG and show that the per-party overheads scale linearly and are practical. For 64 parties, it takes 71 ms to share and 359 ms to verify the overall transcript, while for 8192 parties, it takes 8 s and 42.2 s respectively.

以下是中文翻译：

在本文中，我们提出了一个具有可聚合和公开可验证记录的分布式密钥生成（Distributed Key Generation，DKG）协议。与之前的公开可验证（publicly-verifiable）方法相比，我们的DKG将最终记录的大小和验证时间从 $O(n^2)$ 减少到 $O(n\log⁡n)$，其中n表示参与方的数量。与之前的非公开可验证方法相比，我们的DKG利用八卦传播（gossip）而不是全对全通信（all-to-all communication）来降低验证和通信复杂度。我们还重新审视了现有的DKG安全定义（这些定义相当严格），并提出了新的、自然的放宽条件。因此，我们能够证明我们的可聚合DKG的安全性，以及几个现有DKG的安全性，包括广受欢迎的Pedersen变体。我们表明，在这些新定义下，这些现有的DKG可以用于产生流行密码系统的安全门限变体，如El-Gamal加密和BLS签名。我们还证明了我们的DKG可以与一个新的高效可验证不可预测函数（Verifiable Unpredictable Function，VUF）安全地结合使用，我们在随机预言机模型中证明了该函数的安全性。最后，我们对我们的DKG进行了实验评估，并表明每个参与方的开销呈线性增长且具有实用性。对于64个参与方，共享需要71毫秒，验证整体记录需要359毫秒，而对于8192个参与方，这两个过程分别需要8秒和42.2秒。

## 关键词

+ 分布式密钥生成
+ 可聚合公开可验证转录
+ BLS签名门限化
+ 可验证不可预测函数
+ Pedersen DKG