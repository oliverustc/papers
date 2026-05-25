---
title: "A Succinct Range Proof for Polynomial-based Vector Commitment"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2024
modified: 2025-04-27 08:54:41
created: 2025-04-15 16:33:47
---

## A Succinct Range Proof for Polynomial-based Vector Commitment

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3658644.3670324)

## 作者

+ Rui Gao 
+ Zhiguo Wan 
+ [Yuncong Hu](Yuncong%20Hu.md)
+ Huaqun Wang 

## 笔记

A range proof serves as a protocol for the prover to prove to the verifier that a committed number lies in a specified range, such as [0,2n), without disclosing the actual value. Range proofs find extensive application in various domains. However, the efficiency of many existing schemes diminishes significantly when confronted with batch proofs encompassing multiple elements.
To improve the scalability and efficiency, we propose MissileProof, a vector range proof scheme, proving that every element in the committed vector is within [0,2n). We first reduce this argument to a bi-to-univariate SumCheck problem and a bivariate polynomial ZeroTest problem. Then generalizing the idea of univariate SumCheck PIOP, we design a bi-to-univariate SumCheck PIOP. By introducing a random polynomial, we construct the bivariate polynomial ZeroTest using a univariate polynomial ZeroTest and a univariate polynomial SumCheck PIOP. Finally, combining the PIOP for vector range proof, a KZG-based polynomial commitment scheme and the Fiat-Shamir transformation, we get a zero-knowledge succinct non-interactive vector range proof.
Compared with existing schemes, our scheme has the optimal proof size (O(1)), the optimal commitment length (O(1)), and the optimal verification time (O(1)), at the expense of slightly sacrificing proof time (O(log l ⋅ n log n) operations on the prime field for FFT and O(ln) group exponentiations in G). Moreover, we implemented an anti-money-laundering stateless blockchain based on the MissileProof. The gas consumption of the verification smart contract is reduced by 85%.

以下是中文翻译：

范围证明作为一种协议，旨在让证明者向验证者证明一个已承诺的数字位于指定范围内，例如 [0,2^n)，而无需透露实际值。范围证明在多个领域得到了广泛应用。然而，许多现有方案在面对包含多个元素的批量证明时，其效率显著下降。

为了提高可扩展性和效率，我们提出了 MissileProof，一种向量范围证明方案，证明已承诺向量中的每个元素都在 [0,2^n) 范围内。我们首先将这一论证简化为一个双变量到单变量的和检查（SumCheck）问题和一个双变量多项式零测试（ZeroTest）问题。然后，我们在单变量和检查的概念基础上，设计了一个双变量到单变量的和检查 PIOP（公开可验证的交互式证明）。通过引入随机多项式，我们利用单变量多项式零测试和单变量多项式和检查 PIOP 构造了双变量多项式零测试。最后，结合向量范围证明的 PIOP、基于 KZG 的多项式承诺方案以及 Fiat-Shamir 转换，我们得到了一个零知识简洁非交互式向量范围证明。

与现有方案相比，我们的方案在证明大小（O(1)）、承诺长度（O(1)）和验证时间（O(1)）方面均达到了最优，代价是稍微牺牲了证明时间（在素数域上进行 O(log l ⋅ n log n) 次 FFT 操作和 O(ln) 次 G 中的群指数运算）。此外，我们基于 MissileProof 实现了一种反洗钱的无状态区块链，验证智能合约的燃气消耗减少了 85%。

## 关键词

+ 范围证明
+ 向量承诺
+ 零知识证明
+ PIOP
+ KZG多项式承诺
+ 反洗钱区块链