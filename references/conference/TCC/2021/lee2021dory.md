---
title: "Dory: Efficient, transparent arguments for generalised inner products and polynomial commitments"
标题简称:
论文类型: conference
会议简称: TCC
发表年份: 2021
created: 2025-04-28 16:53:19
modified: 2025-04-28 16:55:15
---

## Dory: Efficient, transparent arguments for generalised inner products and polynomial commitments

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-030-90453-1_1)

## 作者

+ [Jonathan Lee](Jonathan%20Lee.md)
## 笔记

This paper presents Dory, a transparent setup, public-coin interactive argument for inner-pairing products between committed vectors of elements of two source groups. For a product of vectors of length _n_, proofs are 6logn target group elements and _O_(1) additional elements. Verifier work is dominated by an O(logn) multi-exponentiation in the target group and _O_(1) pairings. Security is reduced to the standard SXDH assumption in the standard model.

We apply Dory to build a multivariate polynomial commitment scheme via the Fiat-Shamir transform. For a dense polynomial with _n_ coefficients, Prover work to compute a commitment is dominated by a multi-exponentiation in one source group of size _n_. Prover work to show that a commitment to an evaluation is correct is O(nlog8/log25) in general (O(n1/2) for univariate or multilinear polynomials); communication complexity and Verifier work are both O(logn). These asymptotics previously required trusted setup or concretely inefficient groups of unknown order. Critically for applications, these arguments can be batched, saving large factors on the Prover and improving Verifier asymptotics: to validate ℓ polynomial evaluations for polynomials of size at most _n_ requires O(ℓ+logn) exponentiations and O(ℓlogn) field operations.

Dory is also concretely efficient: Using one core and setting n=220, commitments are 192 bytes. Evaluation proofs are ∼18 kB, requiring ∼3 s to generate and ∼25 ms to verify. For batches at n=220, the marginal cost per evaluation is <1 kB communication, ∼300 ms for the Prover and ∼1 ms for the Verifier.

以下是中文翻译：

本文提出了Dory，这是一个透明设置、公共随机币的交互式论证系统，用于证明两个源群中已承诺向量之间的内部配对积。对于长度为_n_的向量积，证明包含6logn个目标群元素和_O_(1)个额外元素。验证者的工作主要由目标群中的O(logn)次多重指数运算和_O_(1)次配对运算组成。在标准模型中，其安全性可归约为标准SXDH(Symmetric External Diffie-Hellman)假设。

我们将Dory应用于构建一个通过Fiat-Shamir变换的多变量多项式承诺方案。对于具有_n_个系数的密集多项式，生成承诺时证明者的工作主要由一个大小为_n_的源群中的多重指数运算决定。证明者在证明承诺的评估正确性时，一般情况下的工作量为O(nlog8/log25)（对于单变量或多线性多项式为O(n1/2)）；通信复杂度和验证者的工作量均为O(logn)。这些渐近性能之前需要可信设置或具体效率低下的未知阶群。对于应用来说至关重要的是，这些论证可以批处理，大大降低了证明者的开销并改善了验证者的渐近性能：验证最大规模为_n_的ℓ个多项式评估需要O(ℓ+logn)次指数运算和O(ℓlogn)次域运算。

Dory在实际应用中也具有很高的效率：使用单核且n=220时，承诺大小为192字节。评估证明约为18 kB，生成时间约为3秒，验证时间约为25毫秒。对于n=220的批处理，每次评估的边际成本不到1 kB的通信量，证明者约需300毫秒，验证者约需1毫秒。

## 关键词

+ 透明设置多项式承诺
+ 内积论证系统Dory
+ SXDH假设安全归约
+ 配对群多重指数运算
+ 批处理多项式评估验证
+ 简洁论证系统效率
