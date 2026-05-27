---
title: "Direct Range Proofs for Paillier Cryptosystem and Their Applications"
doi: 10.1145/3658644.3690261
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2024
created: 2025-04-16 13:47:29
modified: 2025-04-16 13:49:48
---
## Direct Range Proofs for Paillier Cryptosystem and Their Applications

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3658644.3690261)

## 作者

+ Zhikang Xie 
+ Mengling Liu 
+ [Haiyang Xue](Haiyang%20Xue.md)
+ [Man Ho Au](Man%20Ho%20Au.md)
+ Robert H Deng 
+ Siu-Ming Yiu 

## 笔记

The Paillier cryptosystem is renowned for its applications in electronic voting, threshold ECDSA, multi-party computation, and more, largely due to its additive homomorphism. In these applications, range proofs for the Paillier cryptosystem are crucial for maintaining security, because of the mismatch between the message space in the Paillier system and the operation space in application scenarios.

In this paper, we present novel range proofs for the Paillier cryptosystem, specifically aimed at optimizing those for both Paillier plaintext and affine operation. We interpret encryptions and affine operations as commitments over integers, as opposed to solely over $\mathbb{Z}_N$ . Consequently, we propose direct range proof for the updated cryptosystem, thereby eliminating the need for auxiliary integer commitments as required by the current state-of-the-art. Our work yields significant improvements: in the range proof for Paillier plaintext, our approach reduces communication overheads by approximately 60%, and computational overheads by 30% and 10% for the prover and verifier, respectively. In the range proof for Paillier affine operation, our method reduces the bandwidth by 70%, and computational overheads by 50% and 30% for the prover and verifier, respectively. Furthermore, we demonstrate that our techniques can be utilized to improve the performance of threshold ECDSA and the DCR-based instantiation of the Naor-Yung CCA2 paradigm.

以下是中文翻译：

Paillier密码系统因其加法同态特性，在电子投票、门限ECDSA、多方计算等领域得到广泛应用。在这些应用中，由于Paillier系统的消息空间与应用场景中的操作空间存在不匹配，Paillier密码系统的范围证明对于维护安全性至关重要。

在本文中，我们提出了针对Paillier密码系统的新型范围证明方法，特别针对Paillier明文和仿射运算进行了优化。我们将加密和仿射运算解释为整数上的承诺，而不仅仅局限于$\mathbb{Z}_N$上的承诺。因此，我们为更新后的密码系统提出了直接范围证明，从而消除了当前最先进方法所需的辅助整数承诺。我们的工作带来了显著改进：在Paillier明文的范围证明中，我们的方法将通信开销减少了约60%，证明者和验证者的计算开销分别减少了30%和10%。在Paillier仿射运算的范围证明中，我们的方法将带宽减少了70%，证明者和验证者的计算开销分别减少了50%和30%。此外，我们证明了我们的技术可以用于提高门限ECDSA和基于DCR的Naor-Yung CCA2范式实现的性能。

## 关键词

+ Paillier密码系统
+ 范围证明
+ 零知识证明
+ 门限ECDSA
+ 仿射运算
+ 整数承诺