---
title: "Shorter and faster post-quantum designated-verifier zkSNARKs from lattices"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2021
modified: 2025-04-11 11:41:42
---

## Shorter and faster post-quantum designated-verifier zkSNARKs from lattices

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3460120.3484572)

## 作者

+ [Yuval Ishai](Yuval%20Ishai.md)
+ Hang Su 
+ David J Wu 

## 笔记

Zero-knowledge succinct arguments of knowledge (zkSNARKs) enable efficient privacy-preserving proofs of membership for general NP languages. Our focus in this work is on post-quantum zkSNARKs, with a focus on minimizing proof size. Currently, there is a 1000x gap in the proof size between the best pre-quantum constructions and the best post-quantum ones. Here, we develop and implement new lattice-based zkSNARKs in the designated-verifier preprocessing model. With our construction, after an initial preprocessing step, a proof for an NP relation of size 2^20 is just over 16 KB. Our proofs are 10.3x shorter than previous post-quantum zkSNARKs for general NP languages. Compared to previous lattice-based zkSNARKs (also in the designated-verifier preprocessing model), we obtain a 42x reduction in proof size and a 60x reduction in the prover's running time, all while achieving a much higher level of soundness. Compared to the shortest pre-quantum zkSNARKs by Groth (Eurocrypt 2016), the proof size in our lattice-based construction is 131x longer, but both the prover and the verifier are faster (by 1.2x and 2.8x, respectively). Our construction follows the general blueprint of Bitansky et al. (TCC 2013) and Boneh et al. (Eurocrypt 2017) of combining a linear probabilistically checkable proof (linear PCP) together with a linear-only vector encryption scheme. We develop a concretely-efficient lattice-based instantiation of this compiler by considering quadratic extension fields of moderate characteristic and using linear-only vector encryption over rank-2 module lattices.

以下是中文翻译：

零知识简洁知识论证(zkSNARKs)能够为一般NP语言提供高效的隐私保护成员资格证明。本研究关注后量子zkSNARKs，重点是最小化证明大小。目前，最佳的前量子构造和最佳的后量子构造在证明大小上存在1000倍的差距。

在本研究中，我们在指定验证者预处理模型中开发并实现了新的基于格的zkSNARKs。通过我们的构造，在初始预处理步骤之后，对大小为2^20的NP关系的证明仅略超过16 KB。我们的证明比之前用于一般NP语言的后量子zkSNARKs短10.3倍。与之前的基于格的zkSNARKs(同样在指定验证者预处理模型中)相比，我们在证明大小上实现了42倍的减少，在证明者运行时间上实现了60倍的减少，同时还实现了更高水平的可靠性。与Groth(Eurocrypt 2016)提出的最短前量子zkSNARKs相比，我们基于格的构造中的证明大小长131倍，但证明者和验证者都更快(分别快1.2倍和2.8倍)。

我们的构造遵循Bitansky等人(TCC 2013)和Boneh等人(Eurocrypt 2017)提出的通用蓝图，将线性概率可检查证明(线性PCP)与线性唯一向量加密方案相结合。我们通过考虑中等特征的二次扩张域，并在秩2模格上使用线性唯一向量加密，开发了该编译器的具体高效的基于格的实例。

## 关键词

+ 后量子密码学
+ 零知识证明
+ 格基密码学
+ 证明大小优化
+ 验证者指定