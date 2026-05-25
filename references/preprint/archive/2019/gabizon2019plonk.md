---
title: "PLONK: Permutations over Lagrange-bases for oecumenical noninteractive arguments of knowledge"
标题简称:
论文类型: preprint
预印本简称: archive
发表年份: 2019
modified: 2025-04-10 16:41:58
---

## PLONK: Permutations over Lagrange-bases for oecumenical noninteractive arguments of knowledge

## 发表信息

最早在2017年放在archive上，但2025年3月又有了更新

+ [原文链接](https://eprint.iacr.org/2019/953)

## 作者

+ [Ariel Gabizon](Ariel%20Gabizon.md)
+ Zachary J. Williamson
+ Oana Ciobotaru

## 笔记

zk-SNARK constructions that utilize an updatable universal structured reference string remove one of the main obstacles in deploying zk-SNARKs [GKMMM, Crypto 2018]. The important work of Maller et al. [MBKM, CCS 2019] presented $\mathsf{Sonic}$ - the first potentially practical zk-SNARK with fully succinct verification for general arithmetic circuits with such an SRS.
However, the version of $\mathsf{Sonic}$ enabling fully succinct verification still requires relatively high proof construction overheads. We present a universal SNARK construction with fully succinct verification, and significantly lower prover running time (roughly 7.5-20 less group exponentiations than [MBKM] in the fully succinct verifier mode depending on circuit structure).

Similarly to [MBKM], we rely on a permutation argument based on Bayer and Groth [Eurocrypt 2012]. However, we focus on "Evaluations on a subgroup rather than coefficients of monomials"; which enables simplifying both the permutation argument and the artihmetization step.


以下是中文翻译：

利用可更新的通用结构化参考字符串(universal structured reference string)的零知识简洁非交互式知识论证(zk-SNARK)构造消除了部署zk-SNARK的主要障碍之一[GKMMM, Crypto 2018]。Maller等人的重要工作[MBKM, CCS 2019]提出了$\mathsf{Sonic}$——这是第一个具有这种SRS且可能具有实用价值的、针对通用算术电路具有完全简洁验证的zk-SNARK。

然而，支持完全简洁验证的$\mathsf{Sonic}$版本仍然需要相对较高的证明构造开销。我们提出了一个具有完全简洁验证的通用SNARK构造，并且显著降低了证明者运行时间（在完全简洁验证器模式下，根据电路结构的不同，群指数运算比[MBKM]大约减少了7.5-20倍）。

与[MBKM]类似，我们依赖于基于Bayer和Groth[Eurocrypt 2012]的置换论证(permutation argument)。然而，我们关注于"在子群上的求值而非单项式的系数"；这使得我们能够同时简化置换论证和算术化(arithmetization)步骤。

## 关键词

+ PLONK通用SNARK构造
+ 可更新通用结构化参考字符串
+ 多项式承诺置换论证
+ 简洁验证算术电路
+ Lagrange基非交互式知识论证