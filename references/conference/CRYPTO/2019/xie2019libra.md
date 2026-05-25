---
title: "Libra: Succinct Zero-Knowledge Proofs with Optimal Prover Computation"

标题简称: Libra
论文类型: conference
会议简称: CRYPTO
发表年份: 2019
modified: 2025-04-08 22:03:37
---

## Libra: Succinct Zero-Knowledge Proofs with Optimal Prover Computation

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-030-26954-8_24)

## 作者

+ [Tiancheng Xie](Tiancheng%20Xie.md)
+ [Jiaheng Zhang](Jiaheng%20Zhang.md)
+ [Yupeng Zhang](Yupeng%20Zhang.md)
+ [Charalampos Papamanthou](Charalampos%20Papamanthou.md)
+ [Dawn Song](Dawn%20Song.md)

此篇paper的作者都是高手

## 笔记

We present Libra, the first zero-knowledge proof system that has both optimal prover time and succinct proof size/verification time. In particular, if C is the size of the circuit being proved (i) the prover time is $O(C)$ irrespective of the circuit type; (ii) the proof size and verification time are both $O(d\log C)$ for d-depth log-space uniform circuits (such as RAM programs). In addition Libra features an one-time trusted setup that depends only on the size of the input to the circuit and not on the circuit logic. Underlying Libra is a new linear-time algorithm for the prover of the interactive proof protocol by Goldwasser, Kalai and Rothblum (also known as GKR protocol), as well as an efficient approach to turn the GKR protocol to zero-knowledge using small masking polynomials. Not only does Libra have excellent asymptotics, but it is also efficient in practice. For example, our implementation shows that it takes 200 s to generate a proof for constructing a SHA2-based Merkle tree root on 256 leaves, outperforming all existing zero-knowledge proof systems. Proof size and verification time of Libra are also competitive.

以下是中文翻译：

我们提出了Libra，这是第一个具有最佳证明者时间和简洁证明大小/验证时间的零知识证明系统。特别地，如果$C$是被证明电路的大小，(i) 证明者时间为$O(C)$，与电路类型无关；(ii) 对于深度为$d$的对数空间均匀电路（例如RAM程序），证明大小和验证时间均为$O(d \log C)$。此外，Libra具有一次性可信设置，该设置仅依赖于电路输入的大小，而不依赖于电路逻辑。Libra的基础是一个新的线性时间算法，适用于Goldwasser、Kalai和Rothblum的交互式证明协议（也称为GKR协议），以及一种高效的方法，利用小的掩蔽多项式将GKR协议转化为零知识证明。Libra不仅具有优异的渐进性质，而且在实际应用中也表现高效。例如，我们的实现表明，生成一个256叶子构建SHA2基础的Merkle树根的证明需要200秒，超越了所有现有的零知识证明系统。Libra的证明大小和验证时间也具有竞争力。


## 关键词

+ Libra最优证明者时间简洁零知识证明
+ GKR协议线性时间算法掩蔽多项式
+ 对数验证时间均匀电路SNARK构造
+ 一次性可信设置电路输入依赖
+ SHA2 Merkle树实用零知识证明性能