---
title: "Zeromorph: Zero-knowledge multilinear-evaluation proofs from homomorphic univariate commitments"
标题简称:
论文类型: journal
期刊简称: Journal of Cryptology
发表年份: 2024
modified: 2025-04-27 08:25:01
created: 2025-04-11 11:38:44
---

## Zeromorph: Zero-knowledge multilinear-evaluation proofs from homomorphic univariate commitments

## 发表信息

+ [原文链接](https://link.springer.com/article/10.1007/s00145-024-09519-0)

## 作者

+ Tohru Kohrita 
+ Patrick Towa 

## 笔记

A multilinear polynomial is a multivariate polynomial of degree at most one in each variable. This paper introduces a new scheme to commit to multilinear polynomials and to later prove evaluations thereof. The scheme exponentially improves on the added prover costs for evaluation proofs to be zero-knowledge. The construction of the scheme is generic and relies only on the additive homomorphic property of any scheme to commit to univariate polynomials, and on a protocol to prove that committed polynomials satisfy public degree bounds. As the construction requires to check that several committed univariate polynomials do not exceed given, separate bounds, the paper also gives a method to batch executions of any degree-check protocol on homomorphic commitments. For an _n_-linear polynomial, the instantiation of the scheme with a hiding version of KZG commitments (Kate et al. in: Abe (ed) ASIACRYPT 2010. LNCS, vol 6477, pp 177–194, Springer, Heidelberg, 2010. [https://doi.org/10.1007/978-3-642-17373-8_11](https://doi.org/10.1007/978-3-642-17373-8_11)) leads to a scheme with an evaluation prover that performs only $n+5$ extra (i.e., compared to the variant of the same scheme that is not zero-knowledge) first-group operations to achieve the zero-knowledge property. In contrast, previous constructions require an extra  multi-scalar multiplication. The instantiation does so without any concessions on the other performance measures compared to the state of the art.

以下是中文翻译：

多线性多项式是每个变量次数至多为一的多元多项式。本文引入了一种新的承诺多线性多项式并随后证明其求值的方案。该方案对求值证明实现零知识所带来的额外证明者开销有指数级的改进。该方案的构造是通用的，仅依赖于任意单变量多项式承诺方案的加法同态性质，以及一个证明已承诺多项式满足公开次数界的协议。由于构造需要检查多个已承诺单变量多项式的次数不超过各自给定的界，本文还给出了一种对同态承诺上任意次数检查协议进行批量执行的方法。对于n元线性多项式，使用KZG承诺的隐藏版本实例化该方案，得到的求值证明者只需额外执行n+5次第一群操作（即相较于同一方案的非零知识变体）即可实现零知识性质。相比之下，先前的构造需要额外的多标量乘法。该实例化在其他性能指标上与现有最优方案相比没有任何妥协。

## 关键词

+ Zeromorph多线性多项式承诺
+ 零知识求值证明
+ KZG同态承诺
+ 次数界批量检查协议
+ 指数级零知识开销改进
+ 单变量到多线性承诺转换
