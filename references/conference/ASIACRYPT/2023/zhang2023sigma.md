---
title: "Sigma protocols from verifiable secret sharing and their applications"
标题简称:
论文类型: conference
会议简称: ASIACRYPT
发表年份: 2023
modified: 2025-04-14 09:53:38
---

## Sigma protocols from verifiable secret sharing and their applications

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-981-99-8724-5_7)

## 作者

+ Min Zhang 
+ Yu Chen
+ Chuanzhou Yao 
+ Zhichao Wang 

## 笔记

Sigma protocols are one of the most common and efficient zero-knowledge proofs (ZKPs). Over the decades, a large number of Sigma protocols are proposed, yet few works pay attention to the common design principal. In this work, we propose a generic framework of Sigma protocols for algebraic statements from verifiable secret sharing (VSS) schemes. Our framework provides a general and unified approach to understanding Sigma protocols. It not only neatly explains the classic protocols such as Schnorr, Guillou-Quisquater and Okamoto protocols, but also leads to new Sigma protocols that were not previously known. Furthermore, we show an application of our framework in designing ZKPs for composite statements, which contain both algebraic and non-algebraic statements. We give a generic construction of non-interactive ZKPs for composite statements by combining Sigma protocols from VSS and ZKPs following MPC-in-the-head paradigm in a seamless way via a technique of witness sharing reusing. Our construction has advantages of requiring no “glue” proofs for combining algebraic and non-algebraic statements. By instantiating our construction using Ligero++ (Bhadauria et al., CCS 2020) and designing an associated Sigma protocol from VSS, we obtain a concrete ZKP for composite statements which achieves a tradeoff between running time and proof size, thus resolving the open problem left by Backes et al. (PKC 2019).

以下是中文翻译：

## 关键词

+ Sigma协议
+ 可验证秘密共享
+ 零知识证明
+ 复合语句
+ 代数语句

Sigma协议是最常见和最高效的零知识证明(zero-knowledge proofs, ZKPs)之一。几十年来，已经提出了大量的Sigma协议，但很少有研究关注其共同的设计原则。在本研究中，我们提出了一个基于可验证秘密共享(verifiable secret sharing, VSS)方案的代数语句Sigma协议通用框架。我们的框架为理解Sigma协议提供了一个一般性的统一方法。它不仅能够简洁地解释诸如Schnorr、Guillou-Quisquater和Okamoto等经典协议，还能推导出此前未知的新型Sigma协议。

此外，我们展示了该框架在设计复合语句零知识证明方面的应用，这些复合语句同时包含代数语句和非代数语句。我们通过见证共享复用(witness sharing reusing)技术，将基于VSS的Sigma协议和遵循MPC-in-the-head范式的零知识证明无缝结合，从而为复合语句提供了一个通用的非交互式零知识证明构造方法。我们的构造方法的优势在于不需要用于组合代数语句和非代数语句的"粘合"证明。通过使用Ligero++(Bhadauria等人，CCS 2020)实例化我们的构造，并设计相关的基于VSS的Sigma协议，我们获得了一个具体的复合语句零知识证明，该证明在运行时间和证明大小之间实现了权衡，从而解决了Backes等人(PKC 2019)遗留的开放性问题。