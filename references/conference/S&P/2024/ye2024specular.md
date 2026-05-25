---
title: "Specular: Towards Secure, Trust-minimized Optimistic Blockchain Execution"
标题简称:
论文类型: conference
会议简称: S&P
发表年份: 2024
modified: 2025-04-08 23:07:02
---

## Specular: Towards Secure, Trust-minimized Optimistic Blockchain Execution

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/10646707)

## 作者

+ Zhe Ye
+ Ujval Misra
+ Jiajun Cheng
+ Wenyang Zhou
+ [Dawn Song](Dawn%20Song.md)

## 笔记

An optimistic rollup (ORU) scales a blockchain’s throughput by delegating computation to an untrusted remote chain (L2), refereeing any state claim disagreements between mutually distrusting L2 operators via an interactive dispute resolution protocol. State-of-the-art ORUs employ a monolithic dispute resolution protocol that tightly couples an L1 referee with a specific L2 client binary—oblivious to the system’s higher-level semantics. We argue that this approach (1) magnifies monoculture failure risk, by precluding trust-minimized and permissionless participation using operator-chosen client software; (2) leads to an unnecessarily large and difficult-to-audit TCB; and, (3) suffers from a frequently-triggered, yet opaque upgrade process—both further increasing auditing overhead, and broadening the governance attack surface.To address these concerns, we outline a methodology for designing a secure and resilient ORU with a minimal TCB, by facilitating opportunistic 1-of-N-version programming. Due to its unique challenges and opportunities, we ground this work concretely in the context of the Ethereum ecosystem—where ORUs have gained significant traction. Specifically, we design a semantically-aware proof system, natively targeting the EVM and its instruction set. We present an implementation in a new ORU, Specular, that opportunistically leverages Ethereum’s existing client diversity with minimal source modification, demonstrating our approach’s feasibility.

以下是中文翻译：

乐观Rollup（Optimistic Rollup，ORU）通过将计算委托给不可信的远程链（L2）来扩展区块链的吞吐量，并通过交互式争议解决协议来裁决互不信任的L2操作员之间的任何状态声明争议。当前先进的ORU采用了单体争议解决协议，该协议将L1裁判与特定的L2客户端二进制文件紧密耦合——而忽略了系统更高层次的语义。我们认为这种方法存在以下问题：(1) 放大了单一文化失败的风险，因为它排除了使用操作员选择的客户端软件进行信任最小化和无许可参与的可能；(2) 导致了不必要的大型且难以审计的可信计算基（Trusted Computing Base，TCB）；(3) 遭遇频繁触发但不透明的升级过程——这进一步增加了审计的开销，并扩大了治理攻击面。为了解决这些问题，我们概述了一种设计安全且具有弹性的ORU的方法论，旨在通过促进机会性1-of-N版本编程来最小化TCB。由于其独特的挑战和机遇，我们将这项工作具体定位于以太坊生态系统——在该生态系统中，ORU已经获得了显著的关注。具体而言，我们设计了一个语义感知的证明系统，原生针对以太坊虚拟机（EVM）及其指令集。我们在一个新的ORU中实现了这一系统，名为Specular，它机会性地利用以太坊现有的客户端多样性，且对源代码的修改最小，展示了我们方法的可行性。

## 关键词

+ 乐观Rollup安全
+ 争议解决协议
+ EVM语义感知证明
+ 可信计算基最小化
+ 以太坊客户端多样性
+ 区块链二层扩展