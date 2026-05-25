---
title: "VeriZexe: Decentralized Private Computation with Universal Setup"
标题简称:
论文类型: conference
会议简称: USENIX Security
发表年份: 2023

modified: 2025-04-21 11:54:04
created: 2025-04-07 17:01:06
---

## VeriZexe: Decentralized Private Computation with Universal Setup

## 发表信息

+ [原文链接](https://www.usenix.org/conference/usenixsecurity23/presentation/xiong)

## 作者

+ [Alex Luoyuan Xiong](Alex%20Luoyuan%20Xiong.md)
+ [Binyi Chen](Binyi%20Chen.md)
+ [Zhenfei Zhang](Zhenfei%20Zhang.md)
+ [Benedikt Bünz](Benedikt%20Bünz.md)
+ [Ben Fisch](Ben%20Fisch.md)
+ Fernando Krell
+ Philippe Camacho

## 笔记

Traditional blockchain systems execute program state transitions on-chain, requiring each network node participating in state-machine replication to re-compute every step of the program when validating transactions. This limits both scalability and privacy. Recently, Bowe et al. introduced a primitive called decentralized private computation (DPC) and provided an instantiation called Zexe, which allows users to execute arbitrary computations off-chain without revealing the program logic to the network. Moreover, transaction validation takes only constant time, independent of the off-chain computation. However, Zexe required a separate trusted setup for each application, which is highly impractical. Prior attempts to remove this per-application setup incurred significant performance loss.  

We propose a new DPC instantiation VeriZexe that is highly efficient and requires only a single universal setup to support an arbitrary number of applications. Our benchmark improves the state-of-the-art by 9x in transaction generation time and by 3.4x in memory usage. Along the way, we also design efficient gadgets for variable-base multi-scalar multiplication and modular arithmetic within the Plonk constraint system, leading to a Plonk verifier gadget using only ∼ 21_k_ Plonk constraints.  

以下是中文翻译：

传统的区块链系统在链上执行程序状态转换，要求参与状态机复制的每个网络节点在验证交易时重新计算程序的每一步骤，这既限制了可扩展性，也影响了隐私性。近期，Bowe等人提出了一种名为去中心化私有计算（DPC）的基础构件，并给出了一个名为Zexe的实现方案，该方案允许用户在链下执行任意计算，而无需向网络公开程序逻辑。此外，交易验证仅需恒定时间，与链下计算量无关。然而，Zexe要求每个应用单独进行可信设置，这在实践中极不现实。此前尝试消除这种按应用设置的努力，均导致了显著的性能损失。

我们提出了一种新型DPC实现方案VeriZexe，其效率极高，仅需一次通用设置即可支持无限应用。经测试，该方案在交易生成时间上比现有最优技术快9倍，内存占用减少3.4倍。在此过程中，我们还为Plonk约束系统设计了高效的变基多标量乘法与模运算组件，最终实现的Plonk验证器组件仅需约21,000个Plonk约束。

## 关键词

+ VeriZexe去中心化私有计算
+ Zexe通用设置DPC
+ Plonk约束系统电路优化
+ 链下私有计算区块链
+ 多标量乘法模运算组件
+ 通用受信设置替代方案
