---
title: "Pianist: Scalable zkRollups via Fully Distributed Zero-Knowledge Proofs"
标题简称:
论文类型: conference
会议简称: S&P
发表年份: 2024

modified: 2025-05-09 09:27:59
created: 2025-04-07 16:54:34
---

## Pianist: Scalable zkRollups via Fully Distributed Zero-Knowledge Proofs

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/10646741)
+ [archive](https://eprint.iacr.org/2023/1271)
+ [code](https://github.com/dreamATD/pianist-gnark)

## 作者

+ [Tianyi Liu](Tianyi%20Liu.md)
+ [Tiancheng Xie](Tiancheng%20Xie.md)
+ [Jiaheng Zhang](Jiaheng%20Zhang.md)
+ [Dawn Song](Dawn%20Song.md)
+ [Yupeng Zhang](Yupeng%20Zhang.md)

## 笔记

In the past decade, blockchains have seen various financial and technological innovations, with cryptocurrencies reaching a market cap of over 1 trillion dollars. However, scalability is one of the key issues hindering the deployment of blockchains in many applications. To improve the throughput of the transactions, zkRollups and zkEVM techniques using the cryptographic primitive of zero-knowledge proofs (ZKPs) have been proposed and many companies are adopting these technologies in the layer-2 solutions. However, in these technologies, the proof generation of the ZKP is the bottleneck and the companies have to deploy powerful machines with TBs of memory to batch a large number of transactions in a ZKP.In this work, we improve the scalability of these techniques by proposing new schemes of fully distributed ZKPs. Our schemes can improve the efficiency and the scalability of ZKPs using multiple machines, while the communication among the machines is minimal. With our schemes, the ZKP generation can be distributed to multiple participants in a model similar to the mining pools. Our protocols are based on Plonk, an efficient zero-knowledge proof system with a universal trusted setup. The first protocol is for data-parallel circuits. For a computation of M sub-circuits of size T each, using M machines, the prover time is $O(T \log T + M \log M)$, while the prover time of the original Plonk on a single machine is $O(MT \log(MT))$. Our protocol incurs only $O(1)$ communication per machine, and the proof size and verifier time are both $O(1)$, the same as the original Plonk. Moreover, we show that with minor modifications, our second protocol can support general circuits with arbitrary connections while preserving the same proving, verifying, and communication complexity. The technique is general and may be of independent interest for other applications of ZKP.We implement Pianist (Plonk vIA uNlimited dISTribution), a fully distributed ZKP system using our protocols. Pianist can generate the proof for 8192 transactions in 313 seconds on 64 machines. This improves the scalability of the Plonk scheme by 64×. The communication per machine is only 2.1 KB, regardless of the number of machines and the size of the circuit. The proof size is 2.2 KB and the verifier time is 3.5 ms. We further show that Pianist has similar improvements for general circuits. On a randomly generated circuit with 225 gates, it only takes 5 s to generate the proof using 32 machines,24.2× faster than Plonk on a single machine.

以下是中文翻译：

在过去十年中，区块链经历了各种金融和技术创新，加密货币的市值超过1万亿美元。然而，扩展性是阻碍区块链在许多应用中部署的关键问题之一。为了提高交易的吞吐量，提出了使用零知识证明（Zero-Knowledge Proofs, ZKPs）这一密码学原语的zkRollups和zkEVM技术，许多公司正在采用这些技术作为二层解决方案。然而，在这些技术中，ZKP的证明生成是瓶颈，公司必须部署具有TB级内存的强大机器，以在ZKP中批处理大量交易。在本研究中，我们通过提出全分布式ZKP的新方案来改善这些技术的扩展性。我们的方案可以利用多台机器提高ZKP的效率和扩展性，同时机器之间的通信最小化。通过我们的方案，ZKP生成可以分配给多个参与者，模型类似于矿池。我们的协议基于Plonk，一种具有通用可信设置的高效零知识证明系统。第一个协议适用于数据并行电路。对于每个大小为T的M个子电路的计算，使用M台机器，证明者的时间为 \(O(T \log T + M \log M)\)，而原始Plonk在单台机器上的证明者时间为 \(O(MT \log(MT))\)。我们的协议每台机器仅需 \(O(1)\) 的通信，证明大小和验证时间均为 \(O(1)\)，与原始Plonk相同。此外，我们还展示了通过少量修改，我们的第二个协议可以支持具有任意连接的通用电路，同时保持相同的证明、验证和通信复杂度。这项技术是通用的，可能对ZKP的其他应用具有独立的兴趣。我们实现了Pianist（Plonk vIA uNlimited dISTribution），一个使用我们协议的全分布式ZKP系统。Pianist可以在64台机器上为8192笔交易生成证明，耗时313秒。这使得Plonk方案的扩展性提高了64倍。每台机器的通信仅为2.1 KB，无论机器数量和电路大小如何。证明大小为2.2 KB，验证时间为3.5毫秒。我们进一步展示，Pianist在通用电路上也有类似的改进。在一个随机生成的具有225个门的电路上，使用32台机器生成证明仅需5秒，比单台机器上的Plonk快24.2倍。

后续工作：
[HyperPianist: Pianist with Linear-Time Prover and Logarithmic Communication Cost (**S&P 2025**)](li2024hyperpianist)

## 关键词

+ 全分布式零知识证明
+ zkRollup可扩展性
+ Plonk协议
+ 数据并行电路
+ 分布式证明生成
+ zkEVM区块链扩展

