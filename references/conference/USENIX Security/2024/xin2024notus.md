---
title: "Notus: Dynamic Proofs of Liabilities from Zero-knowledge RSA Accumulators"
标题简称: Notus
论文类型: conference
会议简称: USENIX Security
发表年份: 2024
modified: 2025-04-23 09:18:01
created: 2025-04-08 21:18:18
---

## Notus: Dynamic Proofs of Liabilities from Zero-knowledge RSA Accumulators

## 发表信息

+ [原文链接](https://www.usenix.org/conference/usenixsecurity24/presentation/xin)

## 作者

+ [Jiajun Xin](Jiajun%20Xin.md)
+ Arman Haghighi
+ Xiangan Tian
+ [Dimitrios Papadopoulos](Dimitrios%20Papadopoulos.md)

## 笔记

Proofs of Liabilities (PoL) allow an untrusted prover to commit to its liabilities towards a set of users and then prove independent users' amounts or the total sum of liabilities, upon queries by users or third-party auditors. This application setting is highly dynamic. User liabilities may increase/decrease arbitrarily and the prover needs to update proofs in epoch increments (e.g., once a day for a crypto-asset exchange platform). However, prior works mostly focus on the static case and trivial extensions to the dynamic setting open the system to windows of opportunity for the prover to under-report its liabilities and rectify its books in time for the next check, unless all users check their liabilities at all epochs. In this work, we develop Notus, the first dynamic PoL system for general liability updates that avoids this issue. Moreover, it achieves O(1) query proof size, verification time, and auditor overhead-per-epoch. The core building blocks underlying Notus are a novel zero-knowledge (and SNARK-friendly) RSA accumulator and a corresponding zero-knowledge MultiSwap protocol, which may be of independent interest. We then propose optimizations to reduce the prover's update overhead and make Notus scale to large numbers of users (10^6 in our experiments). Our results are very encouraging, e.g., it takes less than 2ms to verify a user's liability and the proof size is 256 Bytes. On the prover side, deploying Notus on a cloud-based testbed with 256 cores and exploiting parallelism, it takes about 3 minutes to perform the complete epoch update, after which all proofs have already been computed.

以下是中文翻译：

负债证明(Proofs of Liabilities, PoL)允许不受信任的证明者对其面向一组用户的负债进行承诺，然后根据用户或第三方审计员的查询，证明单个用户的金额或负债总额。这种应用场景具有高度动态性。用户负债可能会任意增加/减少，且证明者需要按时间周期(epoch)更新证明(例如，加密资产交易平台每天一次)。然而，先前的研究主要集中在静态场景，而对动态场景的简单扩展会给系统留下漏洞，使证明者有机会少报其负债并在下次检查前及时修正账目，除非所有用户都在每个周期检查他们的负债。

在本研究中，我们开发了Notus，这是第一个针对一般负债更新的动态PoL系统，可以避免上述问题。此外，它实现了O(1)的查询证明大小、验证时间和每周期审计员开销。Notus的核心构建模块是一个新颖的零知识(且SNARK友好)的RSA累加器和相应的零知识MultiSwap协议，这些可能具有独立的研究价值。

随后，我们提出了优化方案以减少证明者的更新开销，使Notus能够扩展到大量用户(在我们的实验中达到10^6)。我们的结果非常令人鼓舞，例如，验证用户负债只需不到2毫秒，且证明大小仅为256字节。在证明者方面，在具有256个核心的云测试平台上部署Notus并利用并行计算，完成整个周期更新大约需要3分钟，之后所有证明就已经计算完成。

## 关键词

+ Notus动态负债证明PoL
+ RSA累加器零知识
+ MultiSwap零知识协议
+ 加密资产交易所审计
+ O(1)查询复杂度证明
+ 动态更新用户负债
