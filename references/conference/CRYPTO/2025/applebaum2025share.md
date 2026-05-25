---
title: "How to Share an NP Statement or Combiners for Zero-Knowledge Proofs"
标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 2025
created: 2025-06-09 10:37:25
modified: 2025-06-09 10:41:21
---

## How to Share an NP Statement or Combiners for Zero-Knowledge Proofs

## 发表信息

+ [原文链接](https://eprint.iacr.org/2025/334)

## 作者

+ Benny Applebaum
+ Eliran Kachlon

## 笔记

In Crypto'19, Goyal, Jain, and Sahai (GJS) introduced the elegant notion of *secret-sharing of an NP statement* (NPSS). Roughly speaking, a t-out-of-n secret sharing of an NP statement is a reduction that maps an instance-witness pair to n instance-witness pairs such that any subset of (t−1) reveals no information about the original witness, while any subset of t allows full recovery of the original witness. Although the notion was formulated for general t≤n, the only existing construction (due to GJS) applies solely to the case where t=n and provides only computational privacy. In this paper, we further explore NPSS and present the following contributions.

1. **Definition.** We revisit the notion of NPSS by formulating a new definition of information-theoretically secure NPSS. This notion serves as a cryptographic analogue of standard NP-reductions and can be compiled into the GJS definition using any one-way function.
2. **Construction.** We construct information-theoretic t-out-of-n NPSS for any values of $t \leq n$ with complexity polynomial in n. Along the way, we present a new notion of secure multiparty computation that may be of independent interest.
3. **Applications.** Our NPSS framework enables the *non-interactive combination* of n instances of zero-knowledge proofs, where only $t_s$ of them are sound and only $t_z$ are zero-knowledge, provided that $t_s+t_{z} \gt n$. Our combiner preserves various desirable properties, such as the succinctness of the proof. Building on this, we establish the following results under the minimal assumption of one-way functions: (i) *Standard NIZK implies NIZK in the Multi-String Model* (Groth and Ostrovsky, J. Cryptology, 2014), where security holds as long as a majority of the n common reference strings were honestly generated. Previously, such a transformation was only known in the common random string model, where the reference string is uniformly distributed. (ii) A *Designated-Prover NIZK in the Multi-String Model*, achieving a strong form of two-round Multi-Verifier Zero-Knowledge in the honest-majority setting. (iii) A *three-round secure multiparty computation protocol* for general functions in the honest-majority setting. The round complexity of this protocol is optimal, resolving a line of research that previously relied on stronger assumptions (Asharov et al., Eurocrypt'12; Gordon et al., Crypto'15; Ananth et al., Crypto'18; Badrinarayanan et al., Asiacrypt'20; Applebaum et al., TCC'22).

以下是中文翻译：

在Crypto'19会议上，Goyal、Jain与Sahai（GJS）提出了**NP语句的秘密共享**（_secret-sharing of an NP statement_，NPSS）这一精妙概念。简言之，一个t-out-of-n的NP语句秘密共享是一种归约方法，它将一个实例-见证对（instance-witness pair）映射为n个实例-见证对，使得任意（t−1）个子集均不泄露原始见证的任何信息，而任意t个子集则可完全恢复原始见证。尽管该概念针对一般性t≤n提出，但现有唯一构造（来自GJS）仅适用于t=n的情形，且仅提供计算隐私性（computational privacy）。本文进一步探索NPSS，并作出以下贡献：

1. **定义**
    我们通过提出信息论安全（information-theoretically secure）NPSS的新定义，重新审视NPSS概念。该定义可作为标准NP归约（NP-reductions）的密码学类比，并可通过任意单向函数（one-way function）编译为GJS的定义。
    
2. **构造**
    我们为任意t≤n的值构建了信息论t-out-of-n NPSS，其复杂度为n的多项式。在此过程中，我们提出了一种可能具有独立价值的安全多方计算（secure multiparty computation）新概念。
    
3. **应用**
    我们的NPSS框架实现了零知识证明（zero-knowledge proofs）n个实例的**非交互式组合**（non-interactive combination），其中仅需tsts​个实例具备可靠性（sound）、tztz​个实例具备零知识性（zero-knowledge），且满足$t_s+t_{z} \gt n$。该组合器保留了多项理想特性（如证明的简洁性）。基于此，我们在单向函数的最小假设下取得以下成果：
    （i）**标准非交互式零知识（NIZK）蕴含多字符串模型（Multi-String Model）下的NIZK**（Groth与Ostrovsky, J. Cryptology, 2014），其安全性仅需n个公共参考字符串（common reference strings）中多数为诚实生成即可。此前，此类转换仅在公共随机字符串模型（common random string model）中已知。
    （ii）**多字符串模型下的指定证明者NIZK**（Designated-Prover NIZK），在诚实多数场景中实现了两轮多验证者零知识（Multi-Verifier Zero-Knowledge）的强形式。
    （iii）**诚实多数场景下通用函数的三轮安全多方计算协议**，其轮复杂度最优，终结了此前依赖更强假设的研究路线（Asharov等人, Eurocrypt'12; Gordon等人, Crypto'15; Ananth等人, Crypto'18; Badrinarayanan等人, Asiacrypt'20; Applebaum等人, TCC'22）。

## 关键词

+ NP语句的秘密共享
+ 信息论安全
+ 零知识证明非交互式组合
+ 多字符串模型
+ 安全多方计算