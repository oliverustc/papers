---
title: "hints: Threshold signatures with silent setup"
标题简称:
论文类型: conference
会议简称: S&P
发表年份: 2024
created: 2025-04-17 10:28:28
modified: 2025-04-17 10:39:56
---

## hints: Threshold signatures with silent setup

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/10646864)

## 作者

+ [Sanjam Garg](Sanjam%20Garg.md) 
+ [Abhishek Jain](Abhishek%20Jain.md)
+ [Pratyay Mukherjee](Pratyay%20Mukherjee.md) 
+ Rohit Sinha 
+ [Mingyuan Wang](Mingyuan%20Wang.md) 
+ [Yinuo Zhang](Yinuo%20Zhang.md)
## 笔记

We propose hinTS — a new threshold signature scheme built on top of the widely used BLS signatures. Our scheme enjoys the following attractive features:A silent setup process where the joint public key of the parties is computed as a deterministic function of their locally computed public keys.Support for dynamic choice of thresholds and signers, after the silent setup, without further interaction.Support for general access policies; in particular, native support for weighted thresholds with zero additional overhead over standard threshold setting.Strong security guarantees, including proactive security and forward security.We prove the security of hinTS in the algebraic group model, and also provide an open-source implementation. Our scheme outperforms all prior proposals that avoid distributed key generation in terms of aggregation time, signature size, and verification time (as well as other qualitative measures). As an example, the aggregation time in hinTS for 1000 signers is under 0.5 seconds, while both signing and verification are constant time algorithms, taking 1 ms and 17.5 ms, respectively.The key technical contribution of our work involves the design of special-purpose succinct proofs to efficiently prove the well-formedness of aggregated public keys. Our solution uses public "hints" released by the signers as part of their public keys (hence the name hinTS).

以下是中文翻译：

我们提出了一种新的阈值签名方案 hinTS，该方案建立在广泛使用的 BLS 签名之上。我们的方案具有以下吸引人的特点：一个静默的设置过程，其中各方的联合公钥作为其本地计算公钥的确定性函数进行计算。在静默设置后，支持动态选择阈值和签名者，无需进一步的交互。支持一般访问策略；特别是，对加权阈值的原生支持，且与标准阈值设置相比没有额外的开销。强大的安全保证，包括主动安全（proactive security）和前向安全（forward security）。我们在代数群模型中证明了 hinTS 的安全性，并提供了一个开源实现。我们的方案在聚合时间、签名大小和验证时间（以及其他定性指标）方面优于所有避免分布式密钥生成的先前提案。例如，hinTS 在 1000 个签名者的聚合时间少于 0.5 秒，而签名和验证都是常数时间算法，分别耗时 1 毫秒和 17.5 毫秒。我们工作的关键技术贡献在于设计了专用的简洁证明（succinct proofs），以高效证明聚合公钥的良构性（well-formedness）。我们的解决方案使用签名者作为其公钥一部分发布的公共”提示”（hints），因此得名 hinTS。

## 关键词

+ 阈值签名
+ BLS签名静默设置
+ 动态阈值访问策略
+ 加权阈值签名
+ 主动安全前向安全
+ 简洁证明聚合公钥