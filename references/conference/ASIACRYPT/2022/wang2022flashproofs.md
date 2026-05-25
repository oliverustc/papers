---
title: "Flashproofs: Efficient zero-knowledge arguments of range and polynomial evaluation with transparent setup"
标题简称:
论文类型: conference
会议简称: ASIACRYPT
发表年份: 2022
modified: 2025-04-16 17:36:37
created: 2025-04-11 11:58:26
---

## Flashproofs: Efficient zero-knowledge arguments of range and polynomial evaluation with transparent setup

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-22966-4_8)

## 作者

+ [Nan Wang](Nan%20Wang.md) 
+ [Sid Chi-Kin Chau](Sid%20Chi-Kin%20Chau.md)
## 笔记

We propose Flashproofs, a new type of efficient special honest verifier zero-knowledge arguments with a transparent setup in the discrete logarithm (DL) setting. First, we put forth gas-efficient range arguments that achieve $O(N^{\frac{2}{3}})$ communication cost, and involve group exponentiations for verification and a slightly sub-linear number of group exponentiations for proving with respect to the range , where _N_ is the bit length of the range. For typical confidential transactions on blockchain platforms supporting smart contracts, verifying our range arguments consumes only 237K and 318K gas for 32-bit and 64-bit ranges, which are comparable to 220K gas incurred by verifying the most efficient zkSNARK with a trusted setup (EUROCRYPT ‘ 16) at present. Besides, the aggregation of multiple arguments can yield further efficiency improvement. Second, we present polynomial evaluation arguments based on the techniques of Bayer & Groth (EUROCRYPT ‘ 13). We provide two zero-knowledge arguments, which are optimised for lower-degree () and higher-degree () polynomials, where _D_ is the polynomial degree. Our arguments yield a non-trivial improvement in the overall efficiency. Notably, the number of group exponentiations for proving drops from to . The communication cost and the number of group exponentiations for verification decrease from to . To the best of our knowledge, our arguments instantiate the most communication-efficient arguments of membership and non-membership in the DL setting among those not requiring trusted setups. More importantly, our techniques enable a significantly asymptotic improvement in the efficiency of communication and verification (group exponentiations) from to when multiple arguments satisfying different polynomials with the same degree and inputs are aggregated.

以下是中文翻译：

我们提出了Flashproofs，一种新型的高效特殊诚实验证者零知识论证，具有离散对数设置中的透明设置。首先，我们提出了燃气效率高的范围论证，达到$O(N^{\frac{2}{3}})$通信复杂度，其中验证涉及群指数运算，而证明涉及相对于范围_N_（范围的比特长度）的略低于线性数量的群指数运算。对于区块链平台上支持智能合约的典型保密交易，验证我们的范围论证对于32位和64位范围分别仅消耗237K和318K燃气，这与目前验证最高效的具有可信设置的zkSNARK（EUROCRYPT’16）所需的220K燃气相当。此外，多个论证的聚合可以进一步提高效率。其次，我们基于Bayer和Groth（EUROCRYPT’13）的技术提出了多项式求值论证。我们提供了两种零知识论证，分别针对低次和高次多项式进行优化，其中_D_是多项式的次数。我们的论证在整体效率上取得了显著的改进。特别是，证明中的群指数运算数量降低了。通信复杂度和验证中的群指数运算数量也相应减少。据我们所知，我们的论证在离散对数设置中实现了最通信高效的成员资格和非成员资格论证，且不需要可信设置。更重要的是，当多个满足不同多项式（相同次数和输入）的论证被聚合时，我们的技术实现了通信和验证效率的显著渐近改进。

## 关键词

+ 零知识证明
+ 范围证明
+ 多项式求值
+ 透明设置
+ 离散对数
