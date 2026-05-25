---
title: "Hyperplonk: Plonk with linear-time prover and high-degree custom gates"
标题简称: Hyperplonk
论文类型: conference
会议简称: EUROCRYPT
发表年份: 2023
modified: 2025-04-20 21:07:58
created: 2025-04-07 16:51:57
---

## Hyperplonk: Plonk with linear-time prover and high-degree custom gates

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-30617-4_17)

## 作者

+ [Binyi Chen](Binyi%20Chen.md)
+ [Benedikt Bünz](Benedikt%20Bünz.md)
+ [Dan Boneh](Dan%20Boneh.md)
+ [Zhenfei Zhang](Zhenfei%20Zhang.md)

## 笔记

Plonk is a widely used succinct non-interactive proof system that uses univariate polynomial commitments. Plonk is quite flexible: it supports circuits with low-degree “custom” gates as well as circuits with lookup gates (a lookup gate ensures that its input is contained in a predefined table). For large circuits, the bottleneck in generating a Plonk proof is the need for computing a large FFT.

We present HyperPlonk, an adaptation of Plonk to the boolean hypercube, using multilinear polynomial commitments. HyperPlonk retains the flexibility of Plonk but provides several additional benefits. First, it avoids the need for an FFT during proof generation. Second, and more importantly, it supports custom gates of much higher degree than Plonk without harming the running time of the prover. Both of these can dramatically speed up the prover’s running time. Since HyperPlonk relies on multilinear polynomial commitments, we revisit two elegant constructions: one from Orion and one from Virgo. We show how to reduce the Orion opening proof size to less than 10 KB (an almost factor 1000 improvement) and show how to make the Virgo FRI-based opening proof simpler and shorter (This is an extended abstract. The full version is available on EPRINT[22]).

以下是中文翻译：

Plonk 是一种广泛使用的简洁非交互式证明系统，采用单变量多项式承诺。Plonk 具有相当大的灵活性：它支持低度“自定义”门的电路以及带有查找门的电路（查找门确保其输入包含在预定义的表中）。对于大型电路，生成 Plonk 证明的瓶颈在于需要计算大量的快速傅里叶变换（FFT）。

我们提出了 HyperPlonk，这是对 Plonk 在布尔超立方体上的一种改编，使用多线性多项式承诺。HyperPlonk 保留了 Plonk 的灵活性，但提供了几个额外的好处。首先，它在证明生成过程中避免了 FFT 的需求。其次，更重要的是，它支持比 Plonk 更高度的自定义门，而不会影响证明者的运行时间。这两点都可以显著加快证明者的运行时间。由于 HyperPlonk 依赖于多线性多项式承诺，我们重新审视了两种优雅的构造：一种来自 Orion，另一种来自 Virgo。我们展示了如何将 Orion 开放证明的大小减少到不到 10 KB（几乎是 1000 倍的改进），并展示了如何使基于 Virgo 的 FRI 开放证明更简单且更短（这是一个扩展摘要。完整版本可在 EPRINT [22] 上获得）。

## 关键词

+ HyperPlonk
+ 多线性多项式承诺
+ 布尔超立方
+ 无FFT证明
+ 高次自定义门