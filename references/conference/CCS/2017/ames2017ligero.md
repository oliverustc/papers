---
title: "Ligero: Lightweight Sublinear Arguments Without a Trusted Setup"
标题简称: Ligero
论文类型: conference
会议简称: CCS
发表年份: 2017
modified: 2025-04-08 17:13:15
---

## Ligero: Lightweight Sublinear Arguments Without a Trusted Setup

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3133956.3134104)

## 作者

+ Scott Ames
+ [Carmit Hazay](Carmit%20Hazay.md)
+ [Yuval Ishai](Yuval%20Ishai.md)
+ [Muthuramakrishnan Venkitasubramaniam](Muthuramakrishnan%20Venkitasubramaniam.md)
## 笔记

We design and implement a simple zero-knowledge argument protocol for NP whose communication complexity is proportional to the square-root of the verification circuit size. The protocol can be based on any collision-resistant hash function. Alternatively, it can be made non-interactive in the random oracle model, yielding concretely efficient zk-SNARKs that do not require a trusted setup or public-key cryptography.
Our protocol is attractive not only for very large verification circuits but also for moderately large circuits that arise in applications. For instance, for verifying a SHA-256 preimage in zero-knowledge with 2-40 soundness error, the communication complexity is roughly 44KB (or less than 34KB under a plausible conjecture), the prover running time is 140 ms, and the verifier running time is 62 ms. This proof is roughly 4 times shorter than a similar proof of ZKB++ (Chase et al., CCS 2017), an optimized variant of ZKBoo (Giacomelli et al., USENIX 2016).
The communication complexity of our protocol is independent of the circuit structure and depends only on the number of gates. For 2-40 soundness error, the communication becomes smaller than the circuit size for circuits containing roughly 3 million gates or more. Our efficiency advantages become even bigger in an amortized setting, where several instances need to be proven simultaneously.
Our zero-knowledge protocol is obtained by applying an optimized version of the general transformation of Ishai et al. (STOC 2007) to a variant of the protocol for secure multiparty computation of Damgard and Ishai (Crypto 2006). It can be viewed as a simple zero-knowledge interactive PCP based on "interleaved" Reed-Solomon codes.

以下是中文翻译：

我们设计并实现了一个简单的零知识论证协议(zero-knowledge argument protocol)用于NP问题,其通信复杂度与验证电路规模的平方根成正比。该协议可以基于任何抗碰撞哈希函数(collision-resistant hash function)构建。另外,在随机预言机模型(random oracle model)中,它可以被转化为非交互式的形式,从而产生具体高效的零知识简洁非交互式知识论证(zk-SNARKs),且不需要可信设置或公钥密码学。

我们的协议不仅适用于非常大的验证电路,也适用于应用中出现的中等规模电路。例如,对于在零知识条件下验证SHA-256原像,当可靠性错误为2-40时,通信复杂度约为44KB(在一个合理的猜想下可低于34KB),证明者运行时间为140毫秒,验证者运行时间为62毫秒。这个证明比ZKB++(Chase等人,CCS 2017)的类似证明约短4倍,而ZKB++是ZKBoo(Giacomelli等人,USENIX 2016)的优化变体。

我们协议的通信复杂度与电路结构无关,仅取决于门的数量。当可靠性错误为2-40时,对于包含约300万个或更多门的电路,通信复杂度会小于电路规模。在需要同时证明多个实例的分摊设置中,我们的效率优势会变得更加显著。

我们的零知识协议是通过将Ishai等人(STOC 2007)的通用转换的优化版本应用于Damgard和Ishai(Crypto 2006)的安全多方计算协议的变体而获得的。它可以被视为基于"交错"里德所罗门码(Reed-Solomon codes)的简单零知识交互式PCP。

## 关键词

+ 零知识论证
+ 亚线性通信
+ 无可信设置
+ 里德所罗门码
+ 零知识PCP