---
title: "Batch Range Proof: How to Make Threshold ECDSA More Efficient"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2024
modified: 2025-04-15 16:38:26
created: 2025-04-13 17:55:03
---

## Batch Range Proof: How to Make Threshold ECDSA More Efficient

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3658644.3670287)

## 作者

+ Guofeng Tang 
+ Shuai Han 
+ Li Lin 
+ Changzheng Wei 
+ Ying Yan 

## 笔记

With the demand of cryptocurrencies, threshold ECDSA recently regained popularity. So far, several methods have been proposed to construct threshold ECDSA, including the usage of OT and homomorphic encryptions (HE). Due to the mismatch between the plaintext space and the signature space, HE-based threshold ECDSA always requires zero-knowledge range proofs, such as Paillier and Joye-Libert (JL) encryptions. However, the overhead of range proofs constitutes a major portion of the total cost.

In this paper, we propose efficient batch range proofs to improve the efficiency of threshold ECDSA. At the heart of our efficiency improvement is a new technical tool called_Multi-Dimension Forking Lemma,_ as a generalization of the well-known general forking lemma [Bellare and Neven, CCS 2006]. Based on our new tool, we construct efficient batch range proofs for Paillier and JL encryptions, and use them to give batch multiplication-to-addition (MtA) protocols, which are crucial to most threshold ECDSA. Our constructions improve the prior Paillier-based MtA by a factor of 2 and the prior JL-based MtA by a factor of 3, in both computation and bandwidth in an amortized way. Our batch MtA can be used to improve the efficiency of most Paillier and JL based threshold ECDSA. As three typical examples, our benchmarking results show: 1. We improve the Paillier-based CGGMP20 [Canetti et al., CCS 2020] in bandwidth by a factor of 2.1 to 2.4, in computation by a factor of 1.5 to 1.7. 2. By implementing threshold ECDSA with the batch JL MtA of XAL+23 [Xue et al., CCS 2023] and our batch JL MtA respectively, our batch construction improves theirs in bandwidth by a factor of 2.0 to 2.29, in computation by a factor of 1.88 to 2.09. 3. When replacing OT-based MtA in DKLs24 [Doerner et al., S&P 2024] with our Paillier-based batch MtA, we improve the bandwidth efficiency by 7.8× at the cost of 5.7× slower computation.

以下是中文翻译：

随着加密货币需求的增长，门限ECDSA（椭圆曲线数字签名算法）近期再度受到关注。目前，已提出多种构建门限ECDSA的方法，其中包括利用不经意传输（OT）和同态加密（HE）技术。由于明文空间与签名空间的不匹配，基于同态加密的门限ECDSA方案往往需要引入零知识范围证明机制，如采用Paillier加密或Joye-Libert（JL）加密方案。然而，范围证明的开销在整个方案成本中占据了相当大的比重。

本文提出高效的批量范围证明以提升门限ECDSA的效率。我们效率提升的核心在于一种名为"多维分叉引理"的新技术工具，这是对著名通用分叉引理[Bellare和Neven，CCS 2006]的推广。基于这一新工具，我们为Paillier和JL加密构建了高效的批量范围证明，并利用它们设计了批量乘法转加法（MtA）协议，这对多数门限ECDSA方案至关重要。我们的构造在计算和带宽上均以摊销方式，将现有基于Paillier的MtA效率提升2倍，基于JL的MtA提升3倍。批量MtA可显著优化多数基于Paillier和JL的门限ECDSA方案效率。通过三个典型实例的基准测试表明：1. 在基于Paillier的CGGMP20方案[Canetti等，CCS 2020]中，带宽效率提升2.1至2.4倍，计算效率提升1.5至1.7倍；2. 分别采用XAL+23[Xue等，CCS 2023]的批量JL MtA与我们的方案实现门限ECDSA时，我们的构造在带宽上优化2.0至2.29倍，计算上优化1.88至2.09倍；3. 将DKLs24[Doerner等，S&P 2024]中基于OT的MtA替换为我们的Paillier批量MtA后，带宽效率提升7.8倍，但计算速度降低5.7倍。

## 关键词

+ 门限ECDSA
+ 批量范围证明
+ 乘法转加法
+ 同态加密
+ 零知识证明
+ 多维分叉引理
