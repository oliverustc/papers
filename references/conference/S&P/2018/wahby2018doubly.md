---
title: "Doubly-efficient zkSNARKs without trusted setup"
doi: 10.1109/sp.2018.00060
标题简称:
论文类型: conference
会议简称: S&P
发表年份: 2018
modified: 2025-04-08 20:59:27
---
## Doubly-efficient zkSNARKs without trusted setup

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/8418646)

## 作者

+ Riad S. Wahby
+ Ioanna Tzialla
+ Abhi Shelat
+ [Justin Thaler](Justin%20Thaler.md)
+ [Michael Walfish](Michael%20Walfish.md)
## 笔记

We present a zero-knowledge argument for NP with low communication complexity, low concrete cost for both the prover and the verifier, and no trusted setup, based on standard cryptographic assumptions. Communication is proportional to d log G (for d the depth and G the width of the verifying circuit) plus the square root of the witness size. When applied to batched or data-parallel statements, the prover's runtime is linear and the verifier's is sub-linear in the verifying circuit size, both with good constants. In addition, witness-related communication can be reduced, at the cost of increased verifier runtime, by leveraging a new commitment scheme for multilinear polynomials, which may be of independent interest. These properties represent a new point in the tradeoffs among setup, complexity assumptions, proof size, and computational cost. We apply the Fiat-Shamir heuristic to this argument to produce a zero-knowledge succinct non-interactive argument of knowledge (zkSNARK) in the random oracle model, based on the discrete log assumption, which we call Hyrax. We implement Hyrax and evaluate it against five state-of-the-art baseline systems. Our evaluation shows that, even for modest problem sizes, Hyrax gives smaller proofs than all but the most computationally costly baseline, and that its prover and verifier are each faster than three of the five baselines.

以下是中文翻译：

我们提出了一种零知识论证（zero-knowledge argument），适用于NP问题，具有低通信复杂度、对证明者（prover）和验证者（verifier）均低具体成本，并且不需要可信设置（trusted setup），基于标准的密码学假设。通信量与$d \log G$成正比（其中$d$为验证电路的深度，$G$为宽度），加上见证大小的平方根。当应用于批处理或数据并行语句时，证明者的运行时间是线性的，而验证者的运行时间在验证电路大小上是亚线性的，且这两者都有良好的常数。此外，通过利用一种针对多线性多项式的新承诺方案（commitment scheme），可以减少与见证相关的通信，代价是增加验证者的运行时间，这一承诺方案可能具有独立的研究价值。这些特性代表了在设置、复杂性假设、证明大小和计算成本之间权衡的新视角。我们将Fiat-Shamir启发式应用于此论证，以在随机预言机模型中生成基于离散对数假设的零知识简洁非交互式知识论证（zkSNARK），我们称之为Hyrax。我们实现了Hyrax，并将其与五个最先进的基线系统进行了评估。我们的评估显示，即使对于适度的问题规模，Hyrax所生成的证明比除了最计算成本高的基线之外的所有证明都要小，并且其证明者和验证者的速度均快于五个基线中的三个。

## 关键词

+ 双重高效zkSNARK
+ Hyrax证明系统
+ 无可信设置
+ 多线性多项式承诺
+ 离散对数假设
+ 批处理零知识证明