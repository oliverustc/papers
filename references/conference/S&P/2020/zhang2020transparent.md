---
title: Transparent Polynomial Delegation and Its Applications to Zero Knowledge Proof
标题简称: Virgo
论文类型: conference
会议简称: S&P
发表年份: 2020
modified: 2025-04-21 17:14:34
created: 2025-04-07 16:53:43
---

## Transparent Polynomial Delegation and Its Applications to Zero Knowledge Proof

## 发表信息

+ [原文](https://ieeexplore.ieee.org/abstract/document/9152704)
+ [Archive原文](https://eprint.iacr.org/2019/1482)
+ [video](https://www.youtube.com/watch?v=dRggr686ZzE&t=154s)
+ [code](https://github.com/sunblaze-ucb/Virgo)

## 作者

+ [Jiaheng Zhang](Jiaheng%20Zhang.md)
+ [Tiancheng Xie](Tiancheng%20Xie.md)
+ [Yupeng Zhang](Yupeng%20Zhang.md)
+ [Dawn Song](Dawn%20Song.md)

## 笔记

We present a new succinct zero knowledge argument scheme for layered arithmetic circuits without trusted setup. The prover time is O(C + nlogn) and the proof size is O(D logC +log2 n) for a D-depth circuit with n inputs and C gates. The verification time is also succinct, O(D logC + log2 n), if the circuit is structured. Our scheme only uses lightweight cryptographic primitives such as collision-resistant hash functions and is plausibly post-quantum secure. We implement a zero knowledge argument system, Virgo, based on our new scheme and compare its performance to existing schemes. Experiments show that it only takes 53 seconds to generate a proof for a circuit computing a Merkle tree with 256 leaves, at least an order of magnitude faster than all other succinct zero knowledge argument schemes. The verification time is 50ms, and the proof size is 253KB, both competitive to existing systems.Underlying Virgo is a new transparent zero knowledge verifiable polynomial delegation scheme with logarithmic proof size and verification time. The scheme is in the interactive oracle proof model and may be of independent interest.

以下是中文翻译：

我们提出了一个新的简洁零知识论证方案，适用于分层算术电路(layered arithmetic circuits)，且无需可信设置。对于一个具有n个输入和C个门电路、深度为D的电路，证明者的计算时间为O(C + nlogn)，证明大小为O(D logC +log2 n)。如果电路是结构化的，验证时间也是简洁的，为O(D logC + log2 n)。我们的方案仅使用轻量级密码学原语，如抗碰撞哈希函数(collision-resistant hash functions)，并且可能具有后量子安全性。

我们基于这个新方案实现了一个零知识论证系统Virgo，并将其性能与现有方案进行了比较。实验表明，对于计算具有256个叶子节点的默克尔树(Merkle tree)的电路，仅需53秒即可生成证明，这比所有其他简洁零知识论证方案至少快一个数量级。验证时间为50毫秒，证明大小为253KB，这两项指标都与现有系统具有竞争力。

Virgo的基础是一个新的透明零知识可验证多项式委托方案(transparent zero knowledge verifiable polynomial delegation scheme)，具有对数级别的证明大小和验证时间。该方案采用交互式预言证明模型(interactive oracle proof model)，可能具有独立的研究价值。

## 关键词

+ 透明零知识证明
+ 可验证多项式委托
+ 分层算术电路
+ Virgo证明系统
+ 无可信设置
+ 后量子安全