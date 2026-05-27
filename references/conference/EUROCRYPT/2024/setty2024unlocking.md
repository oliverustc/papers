---
title: Unlocking the Lookup Singularity with Lasso
doi: 10.1007/978-3-031-58751-1_7
标题简称: Lasso
论文类型: conference
会议简称: EUROCRYPT
发表年份: 2024
modified: 2025-04-11 14:43:24
---
## Unlocking the Lookup Singularity with Lasso

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-58751-1_7)

## 作者

+ [Srinath Setty](Srinath%20Setty.md)
+ [Justin Thaler](Justin%20Thaler.md)
+ [Riad Wahby](Riad%20Wahby.md)
## 笔记

This paper introduces Lasso, a new family of lookup arguments, which allow an untrusted prover to commit to a vector $a \in \mathbb{F}^m$ and prove that all entries of a reside in some predetermined table $t \in \mathbb{F}^n$. Lasso’s performance characteristics unlock the so-called “lookup singularity”. Lasso works with any multilinear polynomial commitment scheme, and provides the following efficiency properties.

For m lookups into a table of size n, Lasso’s prover commits to just $m+n$ field elements. Moreover, the committed field elements are small, meaning that, no matter how big the field $\mathbb{F}$ is, they are all in the set $\{0,...,m\}$. When using a multiexponentiation-based commitment scheme, this results in the prover’s costs dominated by only $O(m+n)$ group operations (e.g., elliptic curve point additions), plus the cost to prove an evaluation of a multilinear polynomial whose evaluations over the Boolean hypercube are the table entries. This represents a significant improvement in prover costs over prior lookup arguments (e.g., plookup, Halo2’s lookups, logUp).

Unlike all prior lookup arguments, if the table t is structured (in a precise sense that we define), then no party needs to commit to t, enabling the use of much larger tables than prior works (e.g., of size $2^{128}$ or larger). Moreover, Lasso’s prover only “pays” in runtime for table entries that are accessed by the lookup operations. This applies to tables commonly used to implement range checks, bitwise operations, big-number arithmetic, and even transitions of a full-fledged CPU such as RISC-V. Specifically, for any integer parameter $c \gt 1$, Lasso’s prover’s dominant cost is committing to $3 \cdot c \cdot m + c \cdot n ^{\frac{1}{c}}$  field elements. Furthermore, all these field elements are “small”, meaning they are in the set $\{0,...,max\{m,n^{1/c}, q\}-1\}$, where q is the maximum value in any of the sub-tables that collectively capture t (in a precise manner that we define).

以下是中文翻译：

本文介绍了一种新的查找参数族——Lasso，它允许一个不可信的证明者对一个向量 $a \in \mathbb{F}^m$ 进行承诺，并证明该向量的所有条目均存在于某个预先确定的表 $t \in \mathbb{F}^n$ 中。Lasso 的性能特征开启了所谓的“查找奇点”。Lasso 可以与任何多线性多项式承诺方案结合使用，并提供以下效率特性。

对于大小为 $n$ 的表进行 $m$ 次查找，Lasso 的证明者只需承诺 $m+n$ 个域元素。此外，承诺的域元素数量较小，这意味着无论域 $\mathbb{F}$ 的大小如何，它们都在集合 $\{0,...,m\}$ 中。当使用基于多重指数运算的承诺方案时，这使得证明者的成本仅由 $O(m+n)$ 次群操作（例如椭圆曲线点加法）主导，加上证明多线性多项式评估的成本，该多项式在布尔超立方体上的评估正是表条目。这与先前的查找参数（如 plookup、Halo2 的查找、logUp）相比，代表了证明者成本的显著改善。

与所有先前的查找参数不同，如果表 $t$ 是结构化的（在我们定义的精确意义上），那么没有任何一方需要对 $t$ 进行承诺，从而使得可以使用比之前工作更大的表（例如，大小为 $2^{128}$ 或更大）。此外，Lasso 的证明者仅在运行时为通过查找操作访问的表条目“付费”。这适用于通常用于实现范围检查、按位操作、大数算术，甚至完整 CPU（如 RISC-V）转换的表。具体而言，对于任何整数参数 $c > 1$，Lasso 的证明者的主导成本是承诺 $3 \cdot c \cdot m + c \cdot n^{\frac{1}{c}}$ 个域元素。此外，所有这些域元素都是“较小的”，这意味着它们在集合 $\{0,...,\max\{m,n^{1/c}, q\}-1\}$ 中，其中 $q$ 是任何子表中最大值的集合，这些子表共同捕获 $t$（以我们定义的精确方式）。

## 关键词

+ Lasso查找参数
+ 查找奇点
+ 多线性多项式承诺
+ 结构化查找表
+ zkVM前端
+ SNARK性能优化