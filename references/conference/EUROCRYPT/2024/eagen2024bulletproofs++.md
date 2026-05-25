---
title: "Bulletproofs++: Next generation confidential transactions via reciprocal set membership arguments"
标题简称: 
论文类型: conference
会议简称: EUROCRYPT
发表年份: 2024
created: 2025-04-15 17:19:43
modified: 2025-04-22 16:18:29
---

## Bulletproofs++: Next generation confidential transactions via reciprocal set membership arguments

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-58740-5_9?fromPaywallRec=false)

## 作者

+ Liam Eagen 
+ Sanket Kanjalkar 
+ Tim Ruffing 
+ Jonas Nick 

## 笔记

Zero-knowledge proofs are a cryptographic cornerstone of privacy-preserving technologies such as “Confidential Transactions” (CT), which aims at hiding monetary amounts in cryptocurrency transactions. Due to its asymptotically logarithmic proof size and transparent setup, most state-of-the-art CT protocols use the Bulletproofs (BP) zero-knowledge proof system for set membership proofs such as range proofs. However, even taking into account recent efficiency improvements, BP comes with a serious overhead in terms of concrete proof size as well as verifier running time and thus puts a large burden on practical deployments of CT and its extensions.

In this work, we introduce Bulletproofs++ (BP++), a drop-in replacement for BP that improves its concrete efficiency and compactness significantly. As for BP, the security of BP++ relies only on the hardness of the discrete logarithm problem in the random oracle model, and BP++ retains all features of Bulletproofs including transparent setup and support for proof aggregation, multi-party proving and batch verification. Asymptotically, BP++ range proofs require only O(n/log⁡n) group scalar multiplications compared to _O_(_n_) for BP and BP+.

At the heart of our construction are novel techniques for permutation and set membership, enabling highly efficient proofs of statements encoded as arithmetic circuits. Concretely, a single BP++ range proof to establish that a committed value is in a 64-bit range (as commonly required by CT) is just 416 bytes over a 256-bit elliptic curve, 38% smaller than an equivalent BP and 27% smaller than BP+. When instantiated on the secp256k1 curve as used in Bitcoin, our benchmarks show that proving is about 5 times faster than BP and verification is about 3 times faster than BP+. When aggregating 32 range proofs, proving and verification are about 9.5 times and 5.5 times faster, respectively.

以下是中文翻译：

零知识证明是隐私保护技术的密码学基石，如"保密交易"（Confidential Transactions, CT），该技术旨在隐藏加密货币交易中的货币金额。由于其渐近对数级的证明大小和透明的设置，大多数最先进的CT协议使用Bulletproofs（BP）零知识证明系统来进行集合成员证明，如范围证明。然而，即使考虑到最近的效率改进，BP在具体证明大小以及验证者运行时间方面仍有严重的开销，因此给CT及其扩展的实际部署带来了巨大负担。

在本研究中，我们介绍了Bulletproofs++（BP++），这是BP的直接替代方案，显著提高了其具体效率和紧凑性。与BP一样，BP++的安全性仅依赖于随机预言机模型中离散对数问题的困难性，并保留了Bulletproofs的所有特性，包括透明设置和对证明聚合、多方证明和批量验证的支持。从渐近角度来看，BP++范围证明仅需要O(n/log⁡n)次群标量乘法运算，相比之下BP和BP+需要O(n)次。

我们构造的核心是新颖的置换和集合成员技术，能够对算术电路编码的语句进行高效证明。具体而言，在256位椭圆曲线上，用于证明承诺值在64位范围内（CT常见要求）的单个BP++范围证明仅需416字节，比等效的BP小38%，比BP+小27%。当在比特币使用的secp256k1曲线上实现时，我们的基准测试显示，证明速度比BP快约5倍，验证速度比BP+快约3倍。当聚合32个范围证明时，证明和验证速度分别快约9.5倍和5.5倍。

## 关键词

+ Bulletproofs++
+ 范围证明
+ 保密交易
+ 集合成员证明
+ 离散对数假设
+ 零知识证明