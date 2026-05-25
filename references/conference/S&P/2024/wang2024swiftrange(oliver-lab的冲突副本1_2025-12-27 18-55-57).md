---
title: "SwiftRange: a short and efficient zero-knowledge range argument for confidential transactions and more"
标题简称:
论文类型: conference
会议简称: S&P
发表年份: 2024
modified: 2025-04-17 09:41:04
created: 2025-04-11 11:52:16
---

## SwiftRange: a short and efficient zero-knowledge range argument for confidential transactions and more

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/10646857)

## 作者

+ [Nan Wang](Nan%20Wang.md)
+ [Sid Chi-Kin Chau](Sid%20Chi-Kin%20Chau.md)
+ [Dongxi Liu](Dongxi%20Liu.md)
## 笔记

Zero-knowledge range proofs play a critical role in confidential transactions (CT) on blockchain systems. They are used to prove the non-negativity of committed transaction payments without disclosing the exact values. Logarithmicsized range proofs with transparent setups, e.g., Bulletproofs, which aim to prove a committed value lies in the range [0, 2 -1] where is the bit length of the range, have gained growing popularity for communication-critical blockchain systems as they increase scalability by allowing a block to accommodate more transactions. In this paper, we propose SwiftRange, a new type of logarithmic-sized zero-knowledge range argument with a transparent setup in the discrete logarithm setting. Our argument can be a drop-in replacement for range proofs in blockchain-based confidential transactions. Compared with Bulletproofs, our argument has higher computational efficiency and lower round complexity while incurring comparable communication overheads for CT-friendly ranges, where N ∈ {32, 64}. Specifically, a single SwiftRange achieves 1.73× and 1.37× proving efficiency with no more than 1.1× communication costs for both ranges, respectively. More importantly, our argument is doubly efficient in verification efficiency. Furthermore, our argument has a smaller size when N ≤ 16, making it competitive for many other communication-critical applications. Our argument supports the aggregation of multiple single arguments for greater efficiency in communication and verification. Finally, we benchmarked our argument against the state-of-the-art range proofs to demonstrate its practicality.

以下是中文翻译：

零知识范围证明在区块链系统的隐私交易（CT）中发挥着关键作用。它们用于证明已确认交易支付的非负性，而无需披露具体数值。具有透明设置的对数大小范围证明（如Bulletproofs）旨在证明承诺值位于$[0, 2^N-1]$范围内（其中N是范围的比特长度），这类证明在注重通信效率的区块链系统中越来越受欢迎，因为它们通过允许区块容纳更多交易来提高可扩展性。

在本文中，我们提出了SwiftRange，这是一种新型的具有透明设置的对数大小零知识范围论证，基于离散对数设置。我们的论证可以作为区块链隐私交易中范围证明的直接替代品。与Bulletproofs相比，对于CT友好的范围$N \in \{32, 64\}$，我们的论证具有更高的计算效率和更低的轮次复杂度，同时保持可比的通信开销。具体而言，单个SwiftRange在这两个范围内分别实现了1.73倍和1.37倍的证明效率，通信成本增加不超过1.1倍。更重要的是，我们的论证在验证效率方面具有双重优势。此外，当$N≤16$时，我们的论证具有更小的规模，这使其在许多其他注重通信效率的应用中具有竞争力。

我们的论证支持多个单一论证的聚合，以实现更高的通信和验证效率。最后，我们将我们的论证与最先进的范围证明进行了基准测试，以证明其实用性。

## 关键词

+ 零知识范围证明
+ 隐私交易区块链
+ 对数大小范围论证
+ 透明设置离散对数
+ SwiftRange协议
+ Bulletproofs改进