---
title: "Threshold signatures from inner product argument: Succinct, weighted, and multi-threshold"
doi: 10.1145/3576915.3623096
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2023
created: 2025-04-17 10:48:33
modified: 2025-04-17 10:49:51
---
## Threshold signatures from inner product argument: Succinct, weighted, and multi-threshold

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3576915.3623096)

## 作者

+ [Sourav Das](Sourav%20Das.md)
+ Philippe Camacho 
+ [Zhuolun Xiang](Zhuolun%20Xiang.md)
+ Javier Nieto 
+ [Benedikt Bünz](Benedikt%20Bünz.md) 
+ [Ling Ren](Ling%20Ren.md)
## 笔记

Threshold signatures protect the signing key by sharing it among a group of signers so that an adversary must corrupt a threshold number of signers to be able to forge signatures. Existing threshold signatures with succinct signatures and constant verification times do not work if signers have different weights. Such weighted settings are seeing increasing importance in decentralized systems, especially in the Proof-of-Stake blockchains. This paper presents a new paradigm for threshold signatures for pairing and discrete logarithm-based cryptosystems. Our scheme has a compact verification key consisting of only 7 group elements, and a signature consisting of 8 group elements. Verifying the signature requires 8 exponentiations and 8 bilinear pairings. Our scheme supports arbitrary weight distributions among signers and arbitrary thresholds. It requires non-interactive preprocessing after a universal powers-of-tau setup. We prove the security of our scheme in the Algebraic Group Model and implement it using Golang. Our evaluation shows that our scheme achieves a comparable signature size and verification time to a standard (unweighted) threshold signature. Compared to existing multisignature schemes, our scheme has a much smaller public verification key.

以下是中文翻译：

阈值签名通过将签名密钥共享给一组签名者来保护该密钥，使得对手必须破坏达到阈值的签名者数量才能伪造签名。现有的具有简洁签名和恒定验证时间的阈值签名在签名者具有不同权重的情况下无法工作。这种加权设置在去中心化系统中越来越重要，尤其是在权益证明（Proof-of-Stake）区块链中。本文提出了一种基于配对和离散对数密码系统的阈值签名新范式。我们的方案具有一个仅由7个群元素组成的紧凑验证密钥，以及一个由8个群元素组成的签名。验证签名需要8次指数运算和8次双线性配对。我们的方案支持签名者之间任意的权重分布和任意的阈值。它在通用的tau幂次设定后需要非交互式预处理。我们在代数群模型（Algebraic Group Model）中证明了我们方案的安全性，并使用Golang进行了实现。我们的评估表明，我们的方案在签名大小和验证时间上与标准（无权重）阈值签名相当。与现有的多重签名方案相比，我们的方案具有更小的公共验证密钥。

## 关键词

+ 阈值签名
+ 加权签名
+ 零知识证明
+ 离散对数
+ 区块链


