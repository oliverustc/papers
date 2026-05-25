---
title: "Multivariate Multi-Polynomial Commitment and its Applications"
标题简称:
论文类型: preprint
预印本简称: archive
发表年份: 2024
modified: 2025-04-17 13:36:28
created: 2025-04-11 13:56:48
---

## Multivariate Multi-Polynomial Commitment and its Applications

## 发表信息

+ [archive](https://eprint.iacr.org/2024/827)

## 作者

+ [Xiao Yang](Xiao%20Yang.md)
+ [Chengru Zhang](Chengru%20Zhang.md)
+ [Mark Ryan](Mark%20Ryan.md)
+ Gao Meng 

## 笔记

We introduce and formally define Multivariate Multi-Polynomial (MMP) commitment, a commitment scheme on multiple multivariate polynomials, and illustrate the concept with an efficient construction, which enjoys constant commitment size and logarithmic proof size. We further enhance our MMP scheme to achieve the zero-knowledge property. 

Additionally, combined with a novel zero-knowledge range proof for Pedersen subvector commitment, we present a Zero-Knowledge Range Proof (ZKRP) for MMP commitment. 

We present two sample applications. Firstly, our MMP commitment can be used for efficient aggregation of SNARK based on multivariate polynomial commitments. As a showcase,  we apply MMP commitment to HyperPlonk and refer to this variant of HyperPlonk as aHyperPlonk.  For $k$ instances, each with circuit size $n$, the communication and verification complexity is reduced from $O(k \cdot \log n)$ to $O(\log k + \log n)$ , while the prover complexity remains the same. Secondly,  we propose a novel zero-knowledge proof for vehicle GPS traces based on  ZKRP for MMP, which allows vehicle owners to prove if a vehicle has/hasn't passed through some location during a specific time interval.

以下是中文翻译：

我们介绍并正式定义了多变量多项式承诺（Multivariate Multi-Polynomial，MMP），这是一种针对多个多变量多项式的承诺方案，并通过一个高效的构造来说明这一概念。该方案具有常数大小的承诺和对数大小的证明等特点。我们进一步增强了MMP方案以实现零知识特性。

此外，结合一个针对Pedersen子向量承诺的新型零知识范围证明，我们提出了MMP承诺的零知识范围证明（Zero-Knowledge Range Proof，ZKRP）。

我们提出了两个应用示例。首先，我们的MMP承诺可用于基于多变量多项式承诺的SNARK的高效聚合。作为展示，我们将MMP承诺应用于HyperPlonk，并将这个HyperPlonk的变体称为aHyperPlonk。对于$k$个实例，每个实例的电路规模为$n$，通信和验证复杂度从 $O(k \cdot \log n)$ 降低到 $O(\log k + \log n)$，而证明者复杂度保持不变。其次，我们基于MMP的ZKRP提出了一个针对车辆GPS轨迹的新型零知识证明，它允许车主证明车辆在特定时间区间内是否经过某个位置。

## 关键词

+ MMP多变量多项式承诺方案
+ 零知识范围证明Pedersen承诺
+ SNARK聚合HyperPlonk效率优化
+ 车辆GPS轨迹零知识位置证明
+ 常数承诺对数证明多项式方案