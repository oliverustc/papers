---
title: "Scalable zkSNARKs for Matrix Computations: A Generic Framework for Verifiable Deep Learning"
doi: 10.1007/978-981-95-5116-3_12
标题简称:
论文类型: conference
会议简称: ASIACRYPT
发表年份: 2025
---
## Scalable zkSNARKs for Matrix Computations: A Generic Framework for Verifiable Deep Learning

## 发表信息

+ [原文链接]()

## 作者

+ Mingshu Cong 
+ [Sherman SM Chow](Sherman%20SM%20Chow.md)
+ Siu-Ming Yiu 
+ [Tsz Hon Yuen](Tsz%20Hon%20Yuen.md)
## 笔记

Sublinear proof sizes have recently become feasible in verifiable machine learning (VML), yet no approach achieves the trio of strictly linear prover time, logarithmic proof size and verification time, and architecture privacy. Hurdles persist because we lack a succinct commitment to the full neural network and a framework for heterogeneous models, leaving verification dependent on architecture knowledge. Existing limits motivate our new approach: a unified proof-composition framework that casts VML as the design of zero-knowledge succinct non-interactive arguments of knowledge (zkSNARKs) for matrix computations. Representing neural networks with linear and non-linear layers as a directed acyclic graph of atomic matrix operations enables topology-aware composition without revealing the graph. Modeled this way, we split proving into a reduction layer and a compression layer that attests to the reduction with a proof of proof. At the reduction layer, inspired by reduction of knowledge (Crypto ’23), root-node proofs are reduced to leaf-node proofs under an interface standardized for heterogeneous linear and non-linear operations. Next, a recursive zkSNARK compresses the transcript into a single proof while preserving architecture privacy.

Complexity-wise, for a matrix expression with _M_ atomic operations on $n \times n$  matrices, the prover runs in $O(Mn^2)$ time while proof size and verification time are $O(\log (Mn))$ , outperforming known VML systems. Honed for this framework, we formalize relations directly in matrices or vectors—a more intuitive form for VML than traditional polynomials. Our LiteBullet proof, an inner-product proof built on folding and its connection to sumcheck (Crypto ’21), yields a polynomial-free alternative. With these ingredients, we reconcile heterogeneity, zero knowledge, succinctness, and architecture privacy in a single VML system.


## 精准翻译

以下是中文翻译：

亚线性证明大小最近在可验证机器学习（verifiable machine learning, VML）中变得可行，然而没有方法能够同时实现严格线性的证明者时间、对数级证明大小和验证时间，以及架构隐私这三个目标。持续存在的障碍是因为我们缺乏对完整神经网络的简洁承诺以及异构模型的框架，使得验证依赖于架构知识。现有的限制促使我们提出新方法：一个统一的证明组合框架，将 VML 转化为矩阵计算的零知识简洁非交互知识论证（zero-knowledge succinct non-interactive arguments of knowledge, zkSNARKs）的设计。

将具有线性和非线性层的神经网络表示为原子矩阵操作的有向无环图，使得拓扑感知组合成为可能而无需揭示图结构。通过这种建模方式，我们将证明过程分为归约层和压缩层，压缩层通过证明的证明来证实归约过程。在归约层，受知识归约（Crypto '23）启发，根节点证明在为异构线性和非线性操作标准化的接口下被归约为叶节点证明。接下来，递归 zkSNARK 将转录压缩为单一证明，同时保持架构隐私。

在复杂性方面，对于在 $n \times n$ 矩阵上具有 $M$ 个原子操作的矩阵表达式，证明者运行时间为 $O(Mn^2)$，而证明大小和验证时间为 $O(\log (Mn))$，优于已知的 VML 系统。为该框架量身定制，我们直接以矩阵或向量形式化关系——这对 VML 而言比传统多项式更直观。我们的 LiteBullet 证明是一种基于折叠及其与 sumcheck 连接（Crypto '21）构建的内积证明，提供了无多项式的替代方案。通过这些要素，我们在单一 VML 系统中协调了异构性、零知识、简洁性和架构隐私。

## 关键词

+ 可验证机器学习
+ zkSNARK
+ 架构隐私
+ 矩阵计算
+ 零知识证明