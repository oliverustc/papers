---
title: "HyperPianist: Pianist with Linear-Time Prover and Logarithmic Communication Cost"
标题简称: HyperPianist
论文类型: conference
会议简称: S&P
发表年份: 2025
modified: 2025-04-20 23:33:42
created: 2025-04-07 16:55:23
---

## HyperPianist: Pianist with Linear-Time Prover and Logarithmic Communication Cost

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/11023268/)
+ [archive](https://eprint.iacr.org/2024/1273)

## 作者

+ Chongrong Li
+ Pengfei Zhu
+ Yun Li
+ Cheng Hong
+ Wenjie Qu
+ [Jiaheng Zhang](Jiaheng%20Zhang.md)

## 笔记

前置工作：
[Pianist: Scalable zkRollups via Fully Distributed Zero-Knowledge Proofs (**S&P 2024**)](liu2024pianist)

[Hyperplonk: Plonk with linear-time prover and high-degree custom gates (**EUROCRYPT 2023**)](chen2023hyperplonk)

Recent years have seen great improvements in zero-knowledge proofs (ZKPs). Among them, zero-knowledge SNARKs are notable for their compact and efficiently-verifiable proofs, but suffer from high prover costs. Wu et al. (Usenix Security 2018) proposed to distribute the proving task across multiple machines, and achieved significant improvements in proving time. However, existing distributed ZKP systems still have quasi-linear prover cost, and may incur a communication cost that is linear in circuit size. 
In this paper, we introduce $\mathsf{HyperPinanist}$. Inspired by the state-of-the-art distributed ZKP system Pianist (Liu et al., S&P 2024) and the multivariate proof system HyperPlonk (Chen et al., EUROCRYPT 2023), we design a distributed multivariate polynomial interactive oracle proof (PIOP) system with a linear-time prover cost and logarithmic communication cost. Unlike Pianist, $\mathsf{HyperPinanist}$ incurs no extra overhead in prover time or communication when applied to general (non-data-parallel) circuits. To instantiate the PIOP system, we adapt two additively-homomorphic multivariate polynomial commitment schemes, multivariate KZG (Papamanthou et al., TCC 2013) and Dory (Lee et al., TCC 2021), into the distributed setting, and get $\mathsf{HyperPinanist}^K$ and $\mathsf{HyperPinanist}^D$ respectively. Both systems have linear prover complexity and logarithmic communication cost; furthermore, $\mathsf{HyperPinanist}^D$ requires no trusted setup. We also propose $\mathsf{HyperPinanist}+$ , incorporating an optimized lookup argument based on Lasso (Setty et al., EUROCRYPT 2024) with lower prover cost. 
Experiments demonstrate $\mathsf{HyperPinanist}^K$ and $\mathsf{HyperPinanist}^D$ achieve speedups of $63.1 \times$ and $40.2 \times$  over HyperPlonk with 32 distributed machines. Compared to Pianist, $\mathsf{HyperPinanist}^K$ can be $2.9 \times$ and $4.6 \times$ as fast and $\mathsf{HyperPinanist}^D$ can be  $2.4 \times$ and $3.8 \times$ as fast, on vanilla gates and custom gates respectively. With layered circuits, $\mathsf{HyperPinanist}^K$ is up to $5.9 \times$ as fast on custom gates, and $\mathsf{HyperPinanist}^D$ achieves a $4.7 \times$ speedup.

以下是中文翻译：

近年来，零知识证明（Zero-Knowledge Proofs, ZKPs）取得了显著进展。其中，零知识 SNARKs 因其紧凑且高效可验证的证明而受到关注，但其证明者成本较高。Wu 等人（Usenix Security 2018）提出将证明任务分配到多个机器上，从而显著提高了证明时间。然而，现有的分布式 ZKP 系统仍然存在准线性证明者成本，并且可能会导致与电路大小成线性关系的通信成本。

在本文中，我们介绍了 $\mathsf{HyperPinanist}$。该系统受到最先进的分布式 ZKP 系统 Pianist（Liu 等人，S&P 2024）和多变量证明系统 HyperPlonk（Chen 等人，EUROCRYPT 2023）的启发，我们设计了一个具有线性时间证明者成本和对数通信成本的分布式多变量多项式交互式预言机证明（Polynomial Interactive Oracle Proof, PIOP）系统。与 Pianist 不同，$\mathsf{HyperPinanist}$ 在应用于一般（非数据并行）电路时不会产生额外的证明时间或通信开销。为了实例化 PIOP 系统，我们将两种加法同态多变量多项式承诺方案——多变量 KZG（Papamanthou 等人，TCC 2013）和 Dory（Lee 等人，TCC 2021）——适配到分布式环境中，分别得到了 $\mathsf{HyperPinanist}^K$ 和 $\mathsf{HyperPinanist}^D$。这两种系统都具有线性的证明者复杂度和对数的通信成本；此外，$\mathsf{HyperPinanist}^D$ 不需要可信的设置。我们还提出了 $\mathsf{HyperPinanist}^+$，结合了基于 Lasso（Setty 等人，EUROCRYPT 2024）的优化查找论证，以降低证明者成本。

实验表明，$\mathsf{HyperPinanist}^K$ 和 $\mathsf{HyperPinanist}^D$ 在使用 32 台分布式机器时，分别实现了相对于 HyperPlonk 的速度提升为 $63.1 \times$ 和 $40.2 \times$。与 Pianist 相比，$\mathsf{HyperPinanist}^K$ 在普通门和自定义门上的速度分别可以达到 $2.9 \times$ 和 $4.6 \times$，而 $\mathsf{HyperPinanist}^D$ 在普通门和自定义门上的速度分别可以达到 $2.4 \times$ 和 $3.8 \times$。在分层电路中，$\mathsf{HyperPinanist}^K$ 在自定义门上的速度提升高达 $5.9 \times$，而 $\mathsf{HyperPinanist}^D$ 实现了 $4.7 \times$ 的速度提升。

## 关键词

+ 分布式多变量零知识证明
+ 线性时间证明者
+ 对数通信成本
+ HyperPlonk多变量PIOP
+ 多变量KZG多项式承诺
+ 无信任设置zkSNARK