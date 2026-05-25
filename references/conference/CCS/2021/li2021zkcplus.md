---
title: "ZKCPlus: Optimized Fair-exchange Protocol Supporting Practical and Flexible Data Exchange"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2021

modified: 2025-04-08 09:59:54
---

## ZKCPlus: Optimized Fair-exchange Protocol Supporting Practical and Flexible Data Exchange

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3460120.3484558)

## 作者

+ Yun Li
+ Cun Ye
+ Yuguang Hu
+ Ivring Morpheus
+ [Yu Guo](Yu%20Guo.md)
+ Chao Zhang
+ [Yupeng Zhang](Yupeng%20Zhang.md)
+ Zhipeng Sun
+ Yiwen Lu
+ Haodi Wang

## 笔记

Devising a fair-exchange protocol for digital goods has been an appealing line of research in the past decades. The Zero-Knowledge Contingent Payment (ZKCP) protocol first achieves fair exchange in a trustless manner with the aid of the Bitcoin network and zero-knowledge proofs. However, it incurs setup issues and substantial proving overhead, and has difficulties handling complicated validation of large-scale data. In this paper, we propose an improved solution ZKCPlus for practical and flexible fair exchange. ZKCPlus incorporates a new commit-and-prove non-interactive zero-knowledge (CP-NIZK) argument of knowledge under standard discrete logarithmic assumption, which is prover-efficient for data-parallel computations. With this argument we avoid the setup issues of ZKCP and reduce seller's proving overhead, more importantly enable the protocol to handle complicated data validations. We have implemented a prototype of ZKCPlus and built several applications atop it. We rework a ZKCP's classic application of trading sudoku solutions, and ZKCPlus achieves 21-67 times improvement in seller efficiency than ZKCP, with only milliseconds of setup time and 1 MB public parameters. In particular, our CP-NIZK argument shows an order of magnitude higher proving efficiency than the zkSNARK adopted by ZKCP. We also built a realistic application of trading trained CNN models. For a 3-layer CNN containing 8,620 parameters, it takes less than 1 second to prove and verify an inference computation, and also about 1 second to deliver the parameters, which is very promising for practical use.

以下是中文翻译：

在过去几十年中，设计数字商品的公平交换协议一直是一个极具吸引力的研究方向。零知识或有支付协议(Zero-Knowledge Contingent Payment, ZKCP)首次通过比特币网络和零知识证明的辅助，以无信任方式实现了公平交换。然而，该协议存在设置问题和大量的证明开销，并且在处理大规模数据的复杂验证方面存在困难。在本文中，我们提出了一个改进的解决方案ZKCPlus，用于实现实用且灵活的公平交换。

ZKCPlus采用了一种新的承诺-证明型非交互式零知识(CP-NIZK)知识论证，该论证基于标准离散对数假设，对于数据并行计算具有较高的证明者效率。通过这种论证，我们避免了ZKCP的设置问题并减少了卖方的证明开销，更重要的是使协议能够处理复杂的数据验证。

我们已经实现了ZKCPlus的原型并在其基础上构建了几个应用。我们重新实现了ZKCP的经典应用——数独解的交易，与ZKCP相比，ZKCPlus在卖方效率方面实现了21-67倍的提升，仅需毫秒级的设置时间和1 MB的公共参数。特别是，我们的CP-NIZK论证显示出比ZKCP采用的zkSNARK高出一个数量级的证明效率。

我们还构建了一个现实的应用——训练好的CNN模型的交易。对于一个包含8,620个参数的3层CNN，证明和验证一次推理计算所需时间不到1秒，传递参数也只需约1秒，这对于实际应用来说非常有前景。

## 关键词

+ 公平交换
+ 零知识证明
+ 数字商品交易
+ 非交互式知识论证
+ 区块链应用