---
title: "Orion: Zero Knowledge Proof with Linear Prover Time"

标题简称: Orion
论文类型: conference
会议简称: CRYPTO
发表年份: 2022
modified: 2025-04-22 11:27:57
created: 2025-04-07 16:43:36
---

## Orion: Zero Knowledge Proof with Linear Prover Time

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-15985-5_11)
+ [archive](https://eprint.iacr.org/2022/1010)
+ [code](https://github.com/sunblaze-ucb/Orion)

## 作者

+ [Tiancheng Xie](Tiancheng%20Xie.md)
+ [Yupeng Zhang](Yupeng%20Zhang.md)
+ [Dawn Song](Dawn%20Song.md)

## 笔记

Zero-knowledge proof is a powerful cryptographic primitive that has found various applications in the real world. However, existing schemes with succinct proof size suffer from a high overhead on the proof generation time that is super-linear in the size of the statement represented as an arithmetic circuit, limiting their efficiency and scalability in practice. In this paper, we present Orion, a new zero-knowledge argument system that achieves $O(N)$ prover time of field operations and hash functions and $O(\log^2⁡N)$ proof size. Orion is concretely efficient and our implementation shows that the prover time is 3.09 s and the proof size is 1.5 MB for a circuit with $2^{20}$ multiplication gates. The prover time is the fastest among all existing succinct proof systems, and the proof size is an order of magnitude smaller than a recent scheme proposed in Golovnev et al. 2021.

In particular, we develop two new techniques leading to the efficiency improvement. (1) We propose a new algorithm to test whether a random bipartite graph is a lossless expander graph or not based on the densest subgraph algorithm. It allows us to sample lossless expanders with an overwhelming probability. The technique improves the efficiency and/or security of all existing zero-knowledge argument schemes with a linear prover time. The testing algorithm based on densest subgraph may be of independent interest for other applications of expander graphs. (2) We develop an efficient proof composition scheme, code switching, to reduce the proof size from square root to polylogarithmic in the size of the computation. The scheme is built on the encoding circuit of a linear code and shows that the witness of a second zero-knowledge argument is the same as the message in the linear code. The proof composition only introduces a small overhead on the prover time.

以下是中文翻译：

零知识证明是一种强大的密码学原语，在现实世界中有着广泛的应用。然而，现有的具有简洁证明大小的方案在证明生成时间上存在较高的开销，该时间与表示为算术电路的语句大小呈超线性关系，这限制了它们在实践中的效率和可扩展性。在本文中，我们提出了Orion，这是一个新的零知识论证系统，实现了O(N)的证明者字段运算和哈希函数时间，以及O(log²N)的证明大小。Orion具有具体的效率，我们的实现表明，对于具有2²⁰个乘法门的电路，证明者时间为3.09秒，证明大小为1.5 MB。证明者时间是所有现有简洁证明系统中最快的，而证明大小比Golovnev等人2021年提出的最新方案小一个数量级。

具体而言，我们开发了两项导致效率提升的新技术。(1)我们提出了一种基于最密子图算法(densest subgraph algorithm)的新算法，用于测试随机二分图是否为无损扩展图(lossless expander graph)。它使我们能够以压倒性的概率采样无损扩展图。该技术提高了所有具有线性证明者时间的现有零知识论证方案的效率和/或安全性。基于最密子图的测试算法可能对扩展图的其他应用具有独立的研究价值。(2)我们开发了一种高效的证明组合方案，即代码切换(code switching)，将证明大小从计算规模的平方根减少到多对数。该方案建立在线性码的编码电路之上，并证明第二个零知识论证的见证与线性码中的消息相同。这种证明组合仅在证明者时间上引入少量开销。

## 关键词

+ Orion线性证明者时间零知识
+ 无损扩展图最密子图测试
+ 代码切换证明组合多对数大小
+ 算术电路线性时间ZK论证
+ 线性码编码电路证明压缩