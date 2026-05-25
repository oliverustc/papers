---
title: "MiMC: Efficient encryption and cryptographic hashing with minimal multiplicative complexity"
标题简称:
论文类型: conference
会议简称: ASIACRYPT
发表年份: 2016
created: 2025-04-21 17:23:37
modified: 2025-04-21 17:29:58
---

## MiMC: Efficient encryption and cryptographic hashing with minimal multiplicative complexity

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-662-53887-6_7)

## 作者

+ Martin Albrecht 
+ [Lorenzo Grassi](Lorenzo%20Grassi.md)
+ [Christian Rechberger](Christian%20Rechberger.md)
+ [Arnab Roy](Arnab%20Roy.md)
+ Tyge Tiessen 

## 笔记

We explore cryptographic primitives with low multiplicative complexity. This is motivated by recent progress in practical applications of secure multi-party computation (MPC), fully homomorphic encryption (FHE), and zero-knowledge proofs (ZK) where primitives from symmetric cryptography are needed and where linear computations are, compared to non-linear operations, essentially “free”. Starting with the cipher design strategy “LowMC” from Eurocrypt 2015, a number of bit-oriented proposals have been put forward, focusing on applications where the multiplicative depth of the circuit describing the cipher is the most important optimization goal.

Surprisingly, albeit many MPC/FHE/ZK-protocols natively support operations in  for large p, very few primitives, even considering all of symmetric cryptography, natively work in such fields. To that end, our proposal for both block ciphers and cryptographic hash functions is to reconsider and simplify the round function of the Knudsen-Nyberg cipher from 1995. The mapping  is used as the main component there and is also the main component of our family of proposals called “MiMC”. We study various attack vectors for this construction and give a new attack vector that outperforms others in relevant settings.

Due to its very low number of multiplications, the design lends itself well to a large class of applications, especially when the depth does not matter but the total number of multiplications in the circuit dominates all aspects of the implementation. With a number of rounds which we deem secure based on our security analysis, we report on significant performance improvements in a representative use-case involving SNARKs.

以下是中文翻译：

我们探索了具有低乘法复杂度的密码学原语。这项研究的动机来自于安全多方计算(secure multi-party computation, MPC)、全同态加密(fully homomorphic encryption, FHE)和零知识证明(zero-knowledge proofs, ZK)等实际应用的最新进展，这些应用需要对称密码学的原语，且其中线性计算相比非线性运算基本上是"免费的"。从2015年欧洲密码学会议提出的"LowMC"密码设计策略开始，已经提出了许多面向比特的方案，主要关注于那些以描述密码的电路的乘法深度作为最重要优化目标的应用。

令人惊讶的是，尽管许多MPC/FHE/ZK协议天然支持大素数p的有限域(GF(p))上的运算，但即使考虑整个对称密码学领域，也很少有原语天然地在这样的域中工作。为此，我们针对分组密码和密码散列函数的建议是重新考虑并简化1995年Knudsen-Nyberg密码的轮函数。映射x→x³被用作其主要组件，同时也是我们称为"MiMC"的方案族的主要组件。我们研究了这种结构的各种攻击向量，并提出了一种在相关场景下优于其他方法的新攻击向量。

由于其极低的乘法次数，该设计非常适合大类应用，特别是在深度不重要但电路中的总乘法次数主导实现所有方面的情况下。基于我们的安全性分析，我们认为采用适当的轮数是安全的，并在涉及简洁非交互式知识论证(SNARKs)的代表性用例中报告了显著的性能改进。

## 关键词

+ MiMC
+ 低乘法复杂度
+ 算术友好哈希函数
+ 零知识证明电路
+ SNARK优化