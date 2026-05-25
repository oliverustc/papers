---
title: "MIRAGE: Succinct arguments for randomized algorithms with applications to universal zk-SNARKs"
标题简称:
论文类型: conference
会议简称: USENIX Security
发表年份: 2020
modified: 2025-04-11 11:45:38
---

## MIRAGE: Succinct arguments for randomized algorithms with applications to universal zk-SNARKs

## 发表信息

+ [原文链接](https://www.usenix.org/conference/usenixsecurity20/presentation/kosba)

## 作者

+ [Ahmed Kosba](Ahmed%20Kosba.md)
+ [Dimitrios Papadopoulos](Dimitrios%20Papadopoulos.md) 
+ [Charalampos Papamanthou](Charalampos%20Papamanthou.md) 
+ [Dawn Song](Dawn%20Song.md) 

## 笔记

The last few years have witnessed increasing interest in the deployment of zero-knowledge proof systems, in particular ones with succinct proofs and efficient verification (zk-SNARKs). One of the main challenges facing the wide deployment of zk-SNARKs is the requirement of a trusted key generation phase per different computation to achieve practical proving performance. Existing zero-knowledge proof systems that do not require trusted setup or have a single trusted preprocessing phase suffer from increased proof size and/or additional verification overhead. On the other other hand, although universal circuit generators for zk-SNARKs (that can eliminate the need for per-computation preprocessing) have been introduced in the literature, the performance of the prover remains far from practical for real-world applications.

In this paper, we first present a new zk-SNARK system that is well-suited for randomized algorithms—in particular it does not encode randomness generation within the arithmetic circuit allowing for more practical prover times. Then, we design a universal circuit that takes as input any arithmetic circuit of a bounded number of operations as well as a possible value assignment, and performs randomized checks to verify consistency. Our universal circuit is linear in the number of operations instead of quasi-linear like other universal circuits. By applying our new zk-SNARK system to our universal circuit, we build MIRAGE, a universal zk-SNARK with very succinct proofs—the proof contains just one additional element compared to the per-circuit preprocessing state-of-the-art zk-SNARK by Groth (Eurocrypt 2016). Finally, we implement MIRAGE and experimentally evaluate its performance for different circuits and in the context of privacy-preserving smart contracts.

以下是中文翻译：

过去几年，零知识证明系统的部署引起了越来越多的关注，尤其是具有简洁证明和高效验证的系统（zk-SNARKs）。zk-SNARKs大规模部署面临的主要挑战之一是每次不同计算都需要可信密钥生成阶段才能实现实用的证明性能。不需要可信设置或仅需单次可信预处理阶段的现有零知识证明系统，都面临证明尺寸增大和/或额外验证开销的问题。另一方面，尽管文献中已经引入了zk-SNARKs的通用电路生成器（可消除每次计算预处理的需要），但证明者的性能仍远未达到实际应用的要求。

在本文中，我们首先提出了一种新的zk-SNARK系统，该系统非常适合随机化算法——特别是它不在算术电路中编码随机数生成，从而允许更实用的证明者时间。然后，我们设计了一种通用电路，该电路以任意有界操作数的算术电路及可能的值分配为输入，并执行随机化检查以验证一致性。我们的通用电路在操作数方面是线性的，而不像其他通用电路那样是准线性的。通过将我们的新zk-SNARK系统应用于通用电路，我们构建了MIRAGE，一个具有非常简洁证明的通用zk-SNARK——与Groth（Eurocrypt 2016）的每电路预处理最先进zk-SNARK相比，证明中仅多一个额外元素。最后，我们实现了MIRAGE，并针对不同电路以及隐私保护智能合约的背景，对其性能进行了实验评估。

## 关键词

+ MIRAGE通用zk-SNARK
+ 随机化算法零知识证明
+ 通用电路生成器
+ 无可信设置SNARKs
+ 隐私保护智能合约
+ 线性通用电路构造