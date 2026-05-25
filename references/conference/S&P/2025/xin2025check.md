---
title: "Check-Before-you-Solve: Verifiable Time-lock Puzzles"
标题简称: 
论文类型: conference
会议简称: S&P
发表年份: 2025
modified: 2025-04-22 17:16:02
created: 2025-04-08 21:15:12
---

## "Check-Before-you-Solve": Verifiable Time-lock Puzzles

## 发表信息

+ 原文链接暂无
+ [archive](https://eprint.iacr.org/2025/225)

## 作者

+ [Jiajun Xin](Jiajun%20Xin.md)
+ [Dimitrios Papadopoulos](Dimitrios%20Papadopoulos.md)

## 笔记

Time-lock puzzles are cryptographic primitives that guarantee to the generator that the puzzle cannot be solved in less than T sequential computation steps. They have recently found numerous applications, e.g., in fair contract signing and seal-bid auctions. However, solvers have no a priori guarantee about the solution they will reveal, e.g., about its usefulness within a certain application scenario. In this work, we propose verifiable time-lock puzzles (VTLPs) that address this by having the generator publish a succinct proof that the solution satisfies certain properties (without revealing anything else about it). Hence solvers are now motivated to commit resources into solving the puzzle. We propose VTLPs that support proving arbitrary NP relations R about the puzzle solution. At a technical level, to overcome the performance hurdles of the naive approach of simply solving the puzzle within a SNARK that also checks R, our scheme combines the classic RSA time-lock puzzle of Rivest, Shamir, and Wagner, with novel building blocks for offloading expensive modular group exponentiations and multiplications from the SNARK circuit. We then propose a second VTLP specifically for checking RSA-based signatures and verifiable random functions (VRFs). Our second scheme does not rely on a SNARK and can have several applications, e.g., in the context of distributed randomness generation. Along the road, we propose new constant-size proofs for modular exponent relations over hidden-order groups that may be of independent interest. Finally, we experimentally evaluate the performance of our schemes and report the findings and comparisons with prior approaches.

以下是中文翻译：

时间锁谜题（Time-lock puzzles）是一种密码学原语，能够向生成者保证谜题在少于T个顺序计算步骤内无法被破解。它们近来在公平合同签名和密封竞价拍卖等方面找到了众多应用。然而，求解者对于最终揭示的解没有任何先验保证，例如无法了解该解在特定应用场景下的可用性。在本研究中，我们提出了可验证时间锁谜题（VTLPs），通过让生成者发布一个简洁证明来解决这一问题——该证明说明解满足特定属性（而不透露其他任何信息），从而激励求解者投入资源破解谜题。我们提出的VTLPs支持对谜题解的任意NP关系R进行证明。在技术层面，为克服在检验R的SNARK内部求解谜题这一朴素方法的性能障碍，我们的方案将Rivest、Shamir和Wagner的经典RSA时间锁谜题与用于从SNARK电路中卸载昂贵模群幂运算和乘法运算的新型构建模块相结合。我们还提出了第二种专门用于检验基于RSA的签名和可验证随机函数（VRF）的VTLP，该方案不依赖SNARK，可用于分布式随机性生成等多种应用。此外，我们提出了在隐阶群上模指数关系的新型常数大小证明，具有独立研究价值。最后，我们对方案进行了实验评估并报告了与现有方法的比较结果。

## 关键词

+ 可验证时间锁谜题VTLP
+ RSA时间锁谜题
+ SNARK电路模群幂运算
+ 常数大小证明
+ 可验证随机函数VRF
+ 分布式随机性生成

**Note:** This is the full version of our publication. We made minor modifications to the security definitions.