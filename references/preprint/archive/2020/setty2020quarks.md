---
title: "Quarks: Quadruple-efficient transparent zkSNARKs"
标题简称:
论文类型: journal
期刊简称: ePrint
发表年份: 2020
modified: 2025-04-17 13:37:09
created: 2025-04-11 11:31:12
---

## Quarks: Quadruple-efficient transparent zkSNARKs

## 发表信息

+ [archive](https://eprint.iacr.org/2020/1275)

## 作者

+ [Srinath Setty](Srinath%20Setty.md)
+ [Jonathan Lee](Jonathan%20Lee.md)
## 笔记

We introduce Xiphos and Kopis, new transparent zero-knowledge succinct non-interactive arguments of knowledge (zkSNARKs) for R1CS. They do not require a trusted setup, and their security relies on the standard SXDH problem. They achieve non-interactivity in the random oracle model using the Fiat-Shamir transform. Unlike prior transparent zkSNARKs, which support either a fast prover, short proofs, or quick verification, our work is the first to simultaneously achieve all three properties (both asymptotically and concretely) and in addition an inexpensive setup phase, thereby providing the first quadruple-efficient transparent zkSNARKs (Quarks).

Under both schemes, for an R1CS instance of size n and security parameter $\lambda$, the prover incurs $O_{\lambda}(n)$ costs to produce a proof of size $O_{\lambda}(\log n)$. In Xiphos, verification time is $O_{\lambda}(\log n)$, and in Kopis it is $O_{\lambda}(\sqrt{n})$ . In terms of concrete efficiency, compared to prior state-of-the-art transparent zkSNARKs, Xiphos offers the fastest verification; its proof sizes are competitive with those of SuperSonic [EUROCRYPT 2020], a prior transparent SNARK with the shortest proofs in the literature. Xiphos’s prover is fast: its prover is $\approx 3.8 \times$ of Spartan [CRYPTO 2020], a prior transparent zkSNARK with the fastest prover in the literature, and is $376 \times$ faster than SuperSonic. Kopis, at the cost of increased verification time (which is still concretely faster than SuperSonic), shortens Xiphos’s proof sizes further, thereby producing proofs shorter than SuperSonic. Xiphos and Kopis incur $10--10,000 \times$ lower preprocessing costs for the verifier in the setup phase depending on the baseline. Finally, a byproduct of Kopis is Lakonia, a NIZK for R1CS with $O_{\lambda}(\log n)$-sized proofs, which provides an alternative to Bulletproofs [S&P 2018] with over an order of magnitude faster proving and verification times.

以下是中文翻译：

我们提出了Xiphos和Kopis，这是两种新的透明零知识简洁非交互式知识论证（zkSNARKs）系统，用于R1CS。它们不需要可信设置，其安全性依赖于标准SXDH问题。它们通过Fiat-Shamir变换在随机预言机模型中实现非交互性。与之前的透明zkSNARKs（要么支持快速证明者，要么支持短证明，要么支持快速验证）不同，我们的工作是首次同时实现这三个特性（无论是渐近性能还是具体性能），并且具有低成本的设置阶段，从而提供了首个四重高效的透明zkSNARKs（Quarks）。

在这两个方案中，对于大小为n且安全参数为 $\lambda$ 的R1CS实例，证明者需要 $O_{\lambda}(n)$ 的成本来生成大小为 $O_{\lambda}(\log n)$ 的证明。在Xiphos中，验证时间为 $O_{\lambda}(\log n)$ ，而在Kopis中为 $O_{\lambda}(\sqrt{n})$ 。就具体效率而言，与之前最先进的透明zkSNARKs相比，Xiphos提供了最快的验证速度；其证明大小与SuperSonic [EUROCRYPT 2020]（文献中具有最短证明的先前透明SNARK）相当。Xiphos的证明者速度很快：其证明者速度约为Spartan [CRYPTO 2020]（文献中具有最快证明者的先前透明zkSNARK）的3.8倍，比SuperSonic快376倍。Kopis以增加验证时间为代价（但具体验证速度仍快于SuperSonic），进一步缩短了Xiphos的证明大小，从而产生比SuperSonic更短的证明。根据基准的不同，Xiphos和Kopis在设置阶段为验证者带来的预处理成本降低了10-10,000倍。最后，Kopis的一个副产品是Lakonia，这是一个用于R1CS的NIZK，具有 $O_{\lambda}(\log n)$ 大小的证明，它为Bulletproofs [S&P 2018]提供了一个替代方案，证明和验证时间快了一个数量级以上。

## 关键词

+ Quarks四重高效透明zkSNARK
+ R1CS无可信设置SXDH安全
+ 快速证明短证明快速验证
+ Xiphos Kopis对数验证时间
+ 透明SNARK低预处理成本