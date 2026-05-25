---
title: "Subversion-zero-knowledge SNARKs"
标题简称:
论文类型: conference
会议简称: PKC
发表年份: 2018
modified: 2025-04-08 17:22:54
---

## Subversion-zero-knowledge SNARKs

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-319-76578-5_11)

## 作者

+ [Georg Fuchsbauer](Georg%20Fuchsbauer.md)
## 笔记

Subversion zero knowledge for non-interactive proof systems demands that zero knowledge (ZK) be maintained even when the common reference string (CRS) is chosen maliciously. SNARKs are proof systems with succinct proofs, which are at the core of the cryptocurrency Zcash, whose anonymity relies on ZK-SNARKs; they are also used for ZK contingent payments in Bitcoin.

We show that under a plausible hardness assumption, the most efficient SNARK schemes proposed in the literature, including the one underlying Zcash and contingent payments, satisfy subversion ZK or can be made to at very little cost. In particular, we prove subversion ZK of the original SNARKs by Gennaro et al. and the almost optimal construction by Groth; for the Pinocchio scheme implemented in libsnark we show that it suffices to add 4 group elements to the CRS. We also argue informally that Zcash is anonymous even if its parameters were set up maliciously.

以下是中文翻译：

对非交互式证明系统而言，子版本零知识（subversion zero knowledge）要求即使在公共参考字符串（common reference string, CRS）被恶意选择的情况下，仍然保持零知识（zero knowledge, ZK）。SNARK（简洁非交互式知识论证明）是具有简洁证明的证明系统，构成了加密货币Zcash的核心，其匿名性依赖于ZK-SNARK；它们也被用于比特币中的ZK有条件支付（ZK contingent payments）。

我们展示了在一个合理的难度假设下，文献中提出的最有效的SNARK方案，包括支撑Zcash和有条件支付的方案，满足子版本零知识或可以以极小的成本实现。特别地，我们证明了Gennaro等人提出的原始SNARK和Groth的几乎最优构造的子版本零知识；对于在libsnark中实现的Pinocchio方案，我们表明只需向CRS中添加4个群元素即可。我们还非正式地论证了，即使Zcash的参数是恶意设置的，它仍然是匿名的。

## 关键词

+ 子版本零知识
+ SNARK安全性
+ 公共参考字符串
+ 恶意设置安全性
+ Zcash匿名性
+ 有条件零知识支付