---
title: "Spartan and bulletproofs are simulation-extractable for free"
标题简称:
论文类型: conference
会议简称: EUROCRYPT
发表年份: 2023
modified: 2025-04-13 17:49:05
---

## Spartan and bulletproofs are simulation-extractable (for free !)

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-30617-4_18)

## 作者

+ Quang Dao 
+ [Paul Grubbs](Paul%20Grubbs.md)
## 笔记

Increasing deployment of advanced zero-knowledge proof systems, especially zkSNARKs, has raised critical questions about their security against real-world attacks. Two classes of attacks of concern in practice are adaptive soundness attacks, where an attacker can prove false statements by choosing its public input after generating a proof, and malleability attacks, where an attacker can use a valid proof to create another valid proof it could not have created itself. Prior work has shown that simulation-extractability (SIM-EXT), a strong notion of security for proof systems, rules out these attacks. In this paper, we prove that two transparent, discrete-log-based zkSNARKs, Spartan and Bulletproofs, are simulation-extractable (SIM-EXT) in the random oracle model if the discrete logarithm assumption holds in the underlying group. Since these assumptions are required to prove standard security properties for Spartan and Bulletproofs, our results show that SIM-EXT is, surprisingly, "for free" with these schemes. Our result is the first SIM-EXT proof for Spartan and encompasses both linear- and sublinear-verifier variants. Our result for Bulletproofs encompasses both the aggregate range proof and arithmetic circuit variants, and is the first to not rely on the algebraic group model (AGM), resolving an open question posed by Ganesh et al. (EUROCRYPT '22). As part of our analysis, we develop a generalization of the tree-builder extraction theorem of Attema et al. (TCC '22), which may be of independent interest.  

以下是中文翻译：

随着高级零知识证明系统（尤其是zkSNARKs）的广泛应用，其在实际攻击中的安全性引发了关键质疑。实践中尤为关注两类攻击：一是适应性可靠性攻击，即攻击者能在生成证明后通过选择公共输入来伪造虚假陈述；二是可塑性攻击，指攻击者利用有效证明生成其本无法独立创建的其他有效证明。已有研究表明，证明系统的强安全概念——模拟可提取性（SIM-EXT）能有效抵御这些攻击。 本文证明，在随机预言模型下，若底层群满足离散对数假设，则两种基于离散对数的透明zkSNARK方案（Spartan和Bulletproofs）具有模拟可提取性。由于这些假设本就是证明Spartan和Bulletproofs标准安全性所需的前提，我们的研究意外揭示：对这些方案而言，SIM-EXT特性竟是"零成本"获得的。这是Spartan方案的首个SIM-EXT证明，同时涵盖线性和亚线性验证器版本；对Bulletproofs的分析则首次不依赖代数群模型（AGM），解决了Ganesh等人（EUROCRYPT '22）提出的开放性问题，并覆盖聚合范围证明和算术电路两种变体。作为研究副产品，我们拓展了Attema等人（TCC '22）的树构建提取定理，该成果可能具有独立学术价值。

## 关键词

+ 模拟可提取性
+ Spartan
+ Bulletproofs
+ 离散对数假设
+ 零知识证明安全性