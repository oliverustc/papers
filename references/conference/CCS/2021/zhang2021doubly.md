---
title: "Doubly Efficient Interactive Proofs for General Arithmetic Circuits with Linear Prover Time"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2021

modified: 2025-04-21 17:07:40
created: 2025-04-07 16:26:55
---

## Doubly Efficient Interactive Proofs for General Arithmetic Circuits with Linear Prover Time

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3460120.3484767)
+ [code](https://github.com/TAMUCrypto/virgo-plus)

## 作者

+ [Jiaheng Zhang](Jiaheng%20Zhang.md)
+ [Tianyi Liu](Tianyi%20Liu.md)
+ [Dawn Song](Dawn%20Song.md)
+ [Xiang Xie](Xiang%20Xie.md)
+ [Yupeng Zhang](Yupeng%20Zhang.md)

## 笔记

We propose a new doubly efficient interactive proof protocol for general arithmetic circuits. The protocol generalizes the interactive proof for layered circuits proposed by Goldwasser, Kalai and Rothblum to arbitrary circuits, while preserving the optimal prover complexity that is strictly linear to the size of the circuits. The proof size remains succinct for low depth circuits and the verifier time is sublinear for structured circuits. We then construct a new zero knowledge argument scheme for general arithmetic circuits using our new interactive proof protocol together with polynomial commitments. Our key technique is a new sumcheck equation that reduces a claim about the output of one layer to claims about its input only, instead of claims about all the layers above which inevitably incurs an overhead proportional to the depth of the circuit. We developed efficient algorithms for the prover to run this sumcheck protocol and to combine multiple claims back into one in linear time in the size of the circuit. Not only does our new protocol achieve optimal prover complexity asymptotically, but it is also efficient in practice. Our experiments show that it only takes 0.3 seconds to generate the proof for a circuit with more than 600,000 gates, which is 13 times faster than the original interactive proof protocol on the corresponding layered circuit. The proof size is 208 kilobytes and the verifier time is 66 milliseconds. Our implementation can take general arithmetic circuits directly, without transforming them to layered circuits with a high overhead on the size of the circuit.

以下是中文翻译：

我们提出了一个针对通用算术电路的新型双重高效交互式证明协议。该协议将Goldwasser、Kalai和Rothblum提出的针对分层电路(layered circuits)的交互式证明扩展到任意电路，同时保持了严格线性于电路规模的最优证明者复杂度。对于低深度电路，证明大小保持简洁，且对于结构化电路，验证者时间为次线性的。随后，我们利用这个新的交互式证明协议结合多项式承诺(polynomial commitments)，构建了一个针对通用算术电路的新型零知识论证方案。

我们的关键技术是一个新的求和检查(sumcheck)方程，它将关于一层输出的声明仅归约为关于其输入的声明，而不是关于其上所有层的声明（后者不可避免地会产生与电路深度成比例的开销）。我们开发了高效算法，使证明者能够以线性于电路规模的时间运行这个求和检查协议，并将多个声明重新合并为一个。

我们的新协议不仅在渐近意义上实现了最优的证明者复杂度，在实践中也非常高效。我们的实验表明，对于一个包含超过600,000个门的电路，仅需0.3秒即可生成证明，这比在相应分层电路上运行原始交互式证明协议快13倍。证明大小为208千字节，验证者时间为66毫秒。我们的实现可以直接处理通用算术电路，无需将其转换为分层电路（这种转换会导致电路规模的巨大开销）。

## 关键词

+ 交互式证明
+ 算术电路
+ 零知识论证
+ 求和检查协议
+ 证明效率