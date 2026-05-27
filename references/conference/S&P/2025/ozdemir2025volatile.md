---
title: "Volatile and Persistent Memory for zkSNARKs via Algebraic Interactive Proofs"
doi: 10.1109/sp61157.2025.00054
标题简称:
论文类型: conference
会议简称: S&P
发表年份: 2025
modified: 2025-04-13 14:30:25
---
## Volatile and Persistent Memory for zkSNARKs via Algebraic Interactive Proofs

## 发表信息

+ [原文链接暂无]
+ [archive](https://eprint.iacr.org/2024/979)

## 作者

+ [Alex Ozdemir](Alex%20Ozdemir.md)
+ Evan Laufer 
+ [Dan Boneh](Dan%20Boneh.md) 

## 笔记

In verifiable outsourcing, an untrusted server runs an expensive computation and produces a succinct proof (called a SNARK) of the results. In many scenarios, the computation accesses a RAM that the server maintains a commitment to (persistent RAM) or that is initially zero (volatile RAM). But, SNARKs for such scenarios are limited by the high overheads associated with existing techniques for RAM checking. We develop new proofs about volatile, persistent, and sparse persistent RAM that reduce SNARK proving times. Our results include both asymptotic and concrete improvements--- including a proving time reduction of up to 51.3× for persistent RAM. Along the way, we apply two tools that may be of independent interest. First, we generalize an existing construction to convert any algebraic interactive proof (AIP) into a SNARK. An AIP is a public-coin, non-succinct, interactive proof with a verifier that is an arithmetic circuit. Second, we apply Bézout's identity for polynomials to construct new AIPs for uniqueness and disjointness. These are useful for showing the independence of accesses to different addresses.

以下是中文翻译：

在可验证外包计算中，一个不受信任的服务器执行一项昂贵的计算，并为结果生成一个简洁的证明（称为SNARK）。在许多场景下，该计算会访问服务器维护承诺的RAM（持久性RAM）或初始为零的RAM（易失性RAM）。然而，这类场景下的SNARK受到与现有RAM检查技术相关的高开销限制。我们开发了关于易失性、持久性及稀疏持久性RAM的新证明方法，显著缩短了SNARK的证明时间。我们的成果包括渐进性和具体性两方面的改进——对于持久性RAM，证明时间最多可减少51.3倍。在此过程中，我们运用了两项可能具有独立价值的技术工具：首先，我们推广了一种现有构造方法，将任何代数交互式证明（AIP）转化为SNARK。AIP是一种公开掷币、非简洁的交互式证明，其验证过程由算术电路完成。其次，我们应用多项式贝祖定理构建了关于唯一性和不相交性的新型AIP，这对于证明对不同地址访问的独立性尤为有用。

## 关键词

+ zkSNARK RAM检查
+ 易失性持久性RAM证明
+ 代数交互式证明AIP
+ 多项式贝祖定理
+ 可验证外包计算
+ SNARK证明时间优化