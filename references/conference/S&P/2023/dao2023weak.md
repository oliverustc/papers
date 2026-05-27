---
title: "Weak fiat-shamir attacks on modern proof systems"
doi: 10.1109/sp46215.2023.10179408
标题简称:
论文类型: conference
会议简称: S&P
发表年份: 2023
created: 2025-04-21 10:49:19
modified: 2025-04-21 10:49:54
---
## Weak fiat-shamir attacks on modern proof systems

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/10179408)

## 作者

+ Quang Dao 
+ Jim Miller 
+ Opal Wright 
+ [Paul Grubbs](Paul%20Grubbs.md)
## 笔记

A flurry of excitement amongst researchers and practitioners has produced modern proof systems built using novel technical ideas and seeing rapid deployment, especially in cryptocurrencies. Most of these modern proof systems use the Fiat-Shamir (F-S) transformation, a seminal method of removing interaction from a protocol with a public-coin verifier. Some prior work has shown that incorrectly applying F-S (i.e., using the so-called "weak" F-S transformation) can lead to breaks of classic protocols like Schnorr’s discrete log proof; however, little is known about the risks of applying F-S incorrectly for modern proof systems seeing deployment today.In this paper, we fill this knowledge gap via a broad theoretical and practical study of F-S in implementations of modern proof systems. We perform a survey of open-source implementations and find 30 weak F-S implementations affecting 12 different proof systems. For four of these—Bulletproofs, Plonk, Spartan, and Wesolowski’s VDF—we develop novel knowledge soundness attacks accompanied by rigorous proofs of their efficacy. We perform case studies of applications that use vulnerable implementations, and demonstrate that a weak F-S vulnerability could have led to the creation of unlimited currency in a private smart contract platform. Finally, we discuss possible mitigations and takeaways for academics and practitioners.

以下是中文翻译：

研究人员和从业者之间的热烈讨论催生了基于新颖技术思想构建的现代证明系统，并在加密货币领域得到了快速部署。这些现代证明系统大多数采用了Fiat-Shamir（F-S）变换，这是一种通过公共硬币验证者消除协议中交互的开创性方法。一些早期的研究表明，不正确地应用F-S（即使用所谓的“弱”F-S变换）可能导致经典协议（如Schnorr的离散对数证明）的破坏；然而，对于现代证明系统在实际部署中不当应用F-S的风险知之甚少。本文通过对现代证明系统中F-S实施的广泛理论和实践研究，填补了这一知识空白。我们对开源实现进行了调查，发现有30个弱F-S实现影响了12种不同的证明系统。对于其中的四个系统——Bulletproofs、Plonk、Spartan和Wesolowski的VDF——我们开发了新颖的知识安全性攻击，并提供了其有效性的严格证明。我们对使用这些脆弱实现的应用进行了案例研究，并展示了弱F-S漏洞可能导致在一个私有智能合约平台上创建无限货币。最后，我们讨论了可能的缓解措施和对学术界与从业者的启示。

## 关键词

+ 弱Fiat-Shamir变换
+ 知识安全性攻击
+ 现代证明系统
+ Bulletproofs安全漏洞
+ Plonk安全分析
+ 零知识证明实现安全