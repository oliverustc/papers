---
title: "Halo Infinite: Proof-Carrying Data from Additive Polynomial Commitments"

标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 2021
modified: 2025-04-10 16:55:41
---

## Halo Infinite: Proof-Carrying Data from Additive Polynomial Commitments

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-030-84242-0_23)
+ [Major revision on archive](https://eprint.iacr.org/2020/1536)

## 作者

+ [Dan Boneh](Dan%20Boneh.md)
+ Justin Drake
+ [Ben Fisch](Ben%20Fisch.md)
+ [Ariel Gabizon](Ariel%20Gabizon.md)

## 笔记

Polynomial commitment schemes (PCS) have recently been in the spotlight for their key role in building SNARKs. A PCS provides the ability to commit to a polynomial over a finite field and prove its evaluation at points. A succinct PCS has commitment and evaluation proof size sublinear in the degree of the polynomial. An efficient PCS has sublinear proof verification. Any efficient and succinct PCS can be used to construct a SNARK with similar security and efficiency characteristics (in the random oracle model).

Proof-carrying data (PCD) enables a set of parties to carry out an indefinitely long distributed computation where every step along the way is accompanied by a proof of correctness. It generalizes incrementally verifiable computation and can even be used to construct SNARKs. Until recently, however, the only known method for constructing PCD required expensive SNARK recursion. A system called Halo first demonstrated a new methodology for building PCD without SNARKs, exploiting an aggregation property of the Bulletproofs inner-product argument. The construction was heuristic because it makes non-black-box use of a concrete instantiation of the Fiat-Shamir transform. We expand upon this methodology to show that PCD can be (heuristically) built from any homomorphic polynomial commitment scheme (PCS), even if the PCS evaluation proofs are neither succinct nor efficient. In fact, the Halo methodology extends to any PCS that has an even more general property, namely the ability to aggregate linear combinations of commitments into a new succinct commitment that can later be opened to this linear combination. Our results thus imply new constructions of SNARKs and PCD that were not previously described in the literature and serve as a blueprint for future constructions as well.

以下是中文翻译：

多项式承诺方案（Polynomial Commitment Schemes, PCS）最近因其在构建SNARK（Succinct Non-interactive Argument of Knowledge）中的关键作用而受到关注。PCS提供了在有限域上对多项式进行承诺的能力，并证明其在特定点的评估。简洁的PCS在承诺和评估证明的大小上均小于多项式的度数的线性。高效的PCS则具有亚线性的证明验证时间。任何高效且简洁的PCS都可以用于构建具有类似安全性和效率特征的SNARK（在随机预言机模型中）。

证明携带数据（Proof-Carrying Data, PCD）使得一组参与方能够进行无限长的分布式计算，其中每一步都伴随着正确性的证明。它是增量可验证计算的推广，甚至可以用于构建SNARK。然而，直到最近，构建PCD的唯一已知方法需要昂贵的SNARK递归。一个名为Halo的系统首次展示了一种新的构建PCD的方法，无需SNARK，利用了Bulletproofs内积论证的聚合特性。该构造是启发式的，因为它对Fiat-Shamir变换的具体实例进行了非黑箱式的使用。我们在此基础上扩展了该方法论，表明PCD可以（启发式地）基于任何同态多项式承诺方案（PCS）构建，即使该PCS的评估证明既不简洁也不高效。实际上，Halo的方法论可以扩展到任何具有更一般特性的PCS，即能够将承诺的线性组合聚合成一个新的简洁承诺，并且该承诺可以在后续阶段打开为该线性组合。因此，我们的结果暗示了新的SNARK和PCD构造，这些构造在文献中尚未被描述，并且为未来的构造提供了蓝图。

## 关键词

+ Halo Infinite加法多项式承诺PCD
+ 证明携带数据SNARK递归避免
+ 同态PCS聚合线性组合承诺
+ 增量可验证计算Bulletproofs扩展
+ 无可信设置SNARK PCD新构造