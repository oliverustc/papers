---
title: "Publicly accountable robust multi-party computation"
标题简称:
论文类型: conference
会议简称: S&P
发表年份: 2022
created: 2025-05-23 01:09:23
modified: 2025-05-23 01:09:40
---

## Publicly accountable robust multi-party computation

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/9833608)

## 作者

+ Marc Rivinius
+ Pascal Reisert
+ [Daniel Rausch](Daniel%20Rausch.md)
+ [Ralf Küsters](Ralf%20K%C3%BCsters.md)
## 笔记

In recent years, lattice-based secure multi-party computation (MPC) has seen a rise in popularity and is used more and more in large scale applications like privacy-preserving cloud computing, electronic voting, or auctions. Many of these applications come with the following high security requirements: a computation result should be publicly verifiable, with everyone being able to identify a malicious party and hold it accountable, and a malicious party should not be able to corrupt the computation, force a protocol restart, or block honest parties or an honest third-party (client) that provided private inputs from receiving a correct result. The protocol should guarantee verifiability and accountability even if all protocol parties are malicious. While some protocols address one or two of these often essential security features, we present the first publicly verifiable and accountable, and (up to a threshold) robust SPDZ-like MPC protocol without restart. We propose protocols for accountable and robust online, offline, and setup computations. We adapt and partly extend the lattice-based commitment scheme by Baum et al. (SCN 2018) as well as other primitives like ZKPs. For the underlying commitment scheme and the underlying BGV encryption scheme we determine ideal parameters. We give a performance evaluation of our protocols and compare them to state-of-the-art protocols both with and without our target security features: public accountability, public verifiability and robustness.

以下是中文翻译：

近年来，基于格的安全多方计算 （MPC） 越来越受欢迎，并越来越多地用于保护隐私的云计算、电子投票或拍卖等大规模应用。其中许多应用程序具有以下高安全要求：计算结果应该是可公开验证的，每个人都能够识别恶意方并追究其责任，恶意方不应能够破坏计算、强制重启协议或阻止提供私人输入的诚实方或诚实的第三方（客户端）接收正确的结果。即使所有协议方都是恶意的，该协议也应保证可验证性和问责制。虽然有些协议解决了这些通常必不可少的安全功能中的一两个，但我们提出了第一个可公开验证和负责的、并且（达到阈值）强大的类似 SPDZ 的 MPC 协议，无需重新启动。我们提出了负责任和稳健的在线、离线和设置计算的协议。我们改编并部分扩展了 Baum 等人 （SCN 2018） 的基于晶格的承诺方案以及 ZKP 等其他原语。对于底层承诺方案和底层 BGV 加密方案，我们确定理想参数。我们对我们的协议进行性能评估，并将其与最先进的协议进行比较，无论是否具有我们的目标安全功能：公共问责制、公共可验证性和稳健性。

## 关键词

+ 安全多方计算（MPC）
+ 公共问责制
+ SPDZ协议
+ 格基承诺方案
+ 鲁棒MPC
+ 可公开验证性