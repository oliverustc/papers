---
title: "Efficient multiplicative-to-additive function from Joye-Libert cryptosystem and its application to threshold ECDSA"
doi: 10.1145/3576915.3616595
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2023
created: 2025-04-16 14:07:12
modified: 2025-04-16 15:38:49
---
## Efficient multiplicative-to-additive function from Joye-Libert cryptosystem and its application to threshold ECDSA

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3576915.3616595)

## 作者

+ [Haiyang Xue](Haiyang%20Xue.md)
+ [Man Ho Au](Man%20Ho%20Au.md)
+ Mengling Liu 
+ Kwan Yin Chan 
+ Handong Cui 
+ [Xiang Xie](Xiang%20Xie.md) 
+ [Tsz Hon Yuen](Tsz%20Hon%20Yuen.md)
+ [Chengru Zhang](Chengru%20Zhang.md)
## 笔记

Threshold ECDSA receives interest lately due to its widespread adoption in blockchain applications. A common building block of all leading constructions involves a secure conversion of multiplicative shares into additive ones, which is called the multiplicative-to-additive (MtA) function. MtA dominates the overall complexity of all existing threshold ECDSA constructions. Specifically, O(n2) invocations of MtA are required in the case of n active signers. Hence, improvement of MtA leads directly to significant improvements for all state-of-the-art threshold ECDSA schemes.
In this paper, we design a novel MtA by revisiting the Joye-Libert (JL) cryptosystem. Specifically, we revisit JL encryption and propose a JL-based commitment, then give efficient zero-knowledge proofs for JL cryptosystem which are the first to have standard soundness. Our new MtA offers the best time-space complexity trade-off among all existing MtA constructions. It outperforms state-of-the-art constructions from Paillier by a factor of 1.85 to 2 in bandwidth and 1.2 to 1.7 in computation. It is 7X faster than those based on Castagnos-Laguillaumie encryption only at the cost of 2X more bandwidth. While our MtA is slower than OT-based constructions, it saves 18.7X in bandwidth requirement. In addition, we also design a batch version of MtA to further reduce the amortised time and space cost by another 25%.

以下是中文翻译：

由于在区块链应用中的广泛采用，门限ECDSA近来受到了广泛关注。所有主流构造方案的一个共同基础模块涉及将乘法份额安全转换为加法份额，这被称为乘法转加法（MtA）函数。MtA在所有现有门限ECDSA构造中占据主导地位。具体来说，在n个活跃签名者的情况下，需要O(n²)次MtA调用。因此，改进MtA直接导致所有最先进的门限ECDSA方案的显著改进。

在本文中，我们通过重新审视Joye-Libert（JL）密码系统设计了一种新颖的MtA。具体来说，我们重新审视了JL加密并提出了基于JL的承诺方案，然后为JL密码系统提供了高效的零知识证明，这是首个具有标准可靠性的方案。我们的新MtA在所有现有MtA构造中提供了最佳的时空复杂度权衡。与基于Paillier的最新构造相比，在带宽方面提升了1.85到2倍，在计算方面提升了1.2到1.7倍。它比基于Castagnos-Laguillaumie加密的方案快7倍，仅仅以2倍带宽为代价。虽然我们的MtA比基于OT的构造更慢，但它在带宽需求方面节省了18.7倍。此外，我们还设计了MtA的批处理版本，进一步将摊销时间和空间成本降低了25%。

## 关键词

+ 门限ECDSA
+ 乘法转加法
+ Joye-Libert密码系统
+ 零知识证明
+ 密码学
+ 区块链