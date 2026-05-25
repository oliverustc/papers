---
title: "Field-Agnostic SNARKs from Expand-Accumulate Codes"

标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 2024

modified: 2025-04-08 21:03:53
---

## Field-Agnostic SNARKs from Expand-Accumulate Codes

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-68403-6_9)

## 作者

+ [Alexander R. Block](Alexander%20R.%20Block.md)
+ [Zhiyong Fang](Zhiyong%20Fang.md)
+ [Jonathan Katz](Jonathan%20Katz.md)
+ [Justin Thaler](Justin%20Thaler.md)
+ Hendrik Waldner
+ [Yupeng Zhang](Yupeng%20Zhang.md)

## 笔记

Efficient realizations of succinct non-interactive arguments of knowledge (SNARK) have gained popularity due to their practical applications in various domains. Among existing schemes, those based on error-correcting codes are of particular interest because of their good concrete efficiency, transparent setup, and plausible post-quantum security. However, many existing code-based SNARKs suffer from the disadvantage that they only work over specific finite fields.

In this work, we construct a code-based SNARK that does not rely on any specific underlying field; i.e., it is field-agnostic. Our construction follows the framework of Brakedown and builds a polynomial commitment scheme (and hence a SNARK) based on recently introduced expand-accumulate codes. Our work generalizes these codes to arbitrary finite fields; our main technical contribution is showing that, with high probability, these codes have constant rate and constant relative distance (crucial properties for building efficient SNARKs), solving an open problem from prior work.

As a result of our work we obtain a SNARK where, for a statement of size M, the prover time is $O(M \log M)$ and the proof size is $O(\sqrt{M})$. We demonstrate the concrete efficiency of our scheme empirically via experiments. Proving ECDSA verification on the secp256k1 curve requires only 0.23 s for proof generation, 2 orders of magnitude faster than SNARKs that are not field-agnostic. Compared to the original Brakedown result (which is also field-agnostic), we obtain proofs that are $1.9–2.8 \times$ smaller due to the good concrete distance of our underlying error-correcting code, while introducing only a small overhead of $1.2 \times$ in the prover time.

以下是中文翻译：

高效的简洁非交互式知识论证（SNARK）实现因其在多个领域的实际应用而受到广泛关注。在现有方案中，基于纠错码的方案特别引人注目，因为它们具有良好的具体效率、透明的设置以及合理的后量子安全性。然而，许多现有的基于代码的 SNARK 存在一个缺点，即它们仅适用于特定的有限域。

在本研究中，我们构造了一种不依赖于任何特定底层域的基于代码的 SNARK；即，它是与域无关的。我们的构造遵循 Brakedown 的框架，并基于最近引入的扩展累积码构建了一个多项式承诺方案（因此也构建了一个 SNARK）。我们的工作将这些代码推广到任意有限域；我们主要的技术贡献是证明这些代码以高概率具有常数比率和常数相对距离（这对于构建高效 SNARK 至关重要），解决了之前工作的一个开放问题。

作为我们工作的结果，我们获得了一个 SNARK，对于大小为 $M$ 的语句，证明者的时间为 $O(M \log M)$，证明大小为 $O(\sqrt{M})$。我们通过实验实证展示了我们方案的具体效率。在 secp256k1 曲线上进行 ECDSA 验证的证明生成仅需 0.23 秒，比非域无关的 SNARK 快两个数量级。与原始的 Brakedown 结果（同样是域无关的）相比，由于我们底层纠错码的良好具体距离，我们获得的证明大小减少了 $1.9–2.8 \times$，同时证明者的时间仅增加了 $1.2 \times$ 的小开销。

## 关键词

+ 域无关SNARK扩展累积码
+ 透明设置后量子SNARK纠错码
+ ECDSA验证域无关证明系统
+ Brakedown框架多项式承诺推广
+ 常数比率常数距离任意有限域