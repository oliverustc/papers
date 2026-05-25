---
title: "Protostar: Generic efficient accumulationfolding for special-sound protocols"
标题简称:
论文类型: conference
会议简称: ASIACRYPT
发表年份: 2023
created: 2025-04-21 10:37:45
modified: 2025-04-21 10:39:26
---

## Protostar: Generic efficient accumulationfolding for special-sound protocols

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-981-99-8724-5_3)

## 作者

+ [Benedikt Bünz](Benedikt%20Bünz.md) 
+ [Binyi Chen](Binyi%20Chen.md) 

## 笔记

Accumulation is a simple yet powerful primitive that enables incrementally verifiable computation (IVC) without the need for recursive SNARKs. We provide a generic, efficient accumulation (or folding) scheme for any $(2k−1)$-move special-sound protocol with a verifier that checks $\mathscr{l}$ degree-_d_ equations. The accumulation verifier only performs k+2 elliptic curve multiplications and k+d+O(1) field/hash operations. Using the compiler from BCLMS21 (Crypto 21), this enables building efficient IVC schemes where the recursive circuit only depends on the number of rounds and the verifier degree of the underlying special-sound protocol but not the proof size or the verifier time. We use our generic accumulation compiler to build Protostar. Protostar is a non-uniform IVC scheme for Plonk that supports high-degree gates and (vector) lookups. The recursive circuit is dominated by 3 group scalar multiplications and a hash of $d^*$ field elements, where $d^*$ is the degree of the highest gate. The scheme does not require a trusted setup or pairings, and the prover does not need to compute any FFTs. The prover in each accumulation/IVC step is also only logarithmic in the number of supported circuits and independent of the table size in the lookup.

以下是中文翻译：

累积（Accumulation）是一种简单而强大的原语，使增量可验证计算（Incrementally Verifiable Computation, IVC）成为可能，而无需递归SNARKs。我们提供了一种通用、高效的累积（或折叠）方案，适用于任何$(2k−1)$步特殊声学协议（special-sound protocol），其验证者检查$\mathscr{l}$度_d_方程。累积验证者仅需执行$k+2$次椭圆曲线乘法和$k+d+O(1)$次域/哈希操作。利用BCLMS21（Crypto 21）中的编译器，这使得构建高效的IVC方案成为可能，其中递归电路仅依赖于基础特殊声学协议的轮数和验证者的度，而与证明大小或验证者时间无关。我们使用通用累积编译器构建了Protostar。Protostar是一个针对Plonk的非均匀IVC方案，支持高阶门和（向量）查找。递归电路主要由3次群标量乘法和对$d^*$个域元素的哈希组成，其中$d^*$是最高门的度。该方案不需要可信的设置或配对，且证明者无需计算任何FFT。在每个累积/IVC步骤中，证明者的计算复杂度仅与支持的电路数量呈对数关系，并且与查找中的表大小无关。

## 关键词

+ 累积
+ 折叠
+ 增量可验证计算
+ Plonk
+ 特殊声学协议