---
title: "Separating succinct non-interactive arguments from all falsifiable assumptions"
标题简称:
论文类型: conference
会议简称: STOC
发表年份: 2011
modified: 2025-04-08 23:42:18
---

## Separating succinct non-interactive arguments from all falsifiable assumptions

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/1993636.1993651)

## 作者

+ [Craig Gentry](Craig%20Gentry.md)
+ Daniel Wichs

## 笔记

An argument system for NP is succinct, if its communication complexity is polylogarithmic the instance and witness sizes. The seminal works of Kilian '92 and Micali '94 show that such arguments can be constructed under standard cryptographic hardness assumptions with four rounds of interaction, and that they be made non-interactive in the random-oracle model. However, we currently do not have any construction of succinct non-interactive arguments (SNARGs) in the standard model with a proof of security under any simple cryptographic assumption.  

In this work, we give a broad black-box separation result, showing that black-box reductions cannot be used to prove the security of any SNARG construction based on any falsifiable cryptographic assumption. This includes essentially all common assumptions used in cryptography (one-way functions, trapdoor permutations, DDH, RSA, LWE etc.). More generally, we say that an assumption is falsifiable if it can be modeled as an interactive game between an adversary and an efficient challenger that can efficiently decide if the adversary won the game. This is similar, in spirit, to the notion of falsifiability of Naor '03, and captures the fact that we can efficiently check if an adversarial strategy breaks the assumption.  

Our separation result also extends to designated verifier SNARGs, where the verifier needs a trapdoor associated with the CRS to verify arguments, and slightly succinct SNARGs, whose size is only required to be sublinear in the statement and witness size.  

以下是中文翻译：

若一个针对NP问题的论证系统，其通信复杂度相对于实例和见证规模呈多对数级别，则称其为简洁的。Kilian '92与Micali '94的开创性工作表明，在标准密码学硬度假设下，通过四轮交互可构建此类论证，并能在随机预言机模型中实现非交互式。然而，目前我们尚未在标准模型下，基于任何简单密码学假设的安全性证明，构造出简洁的非交互式论证（SNARGs）。

在这项研究中，我们提出了一个广泛的黑盒分离结论，揭示了黑盒归约方法无法用于证明基于任何可证伪密码学假设的SNARG（简洁非交互式论证）构造的安全性。这几乎涵盖了密码学中所有常见假设，如单向函数、陷门置换、DDH（决策Diffie-Hellman）、RSA、LWE（带错误学习）等。更广义地说，我们认为一个假设是可证伪的，如果它能被建模为敌手与高效挑战者之间的交互游戏，且挑战者能有效判定敌手是否赢得了游戏。这一概念在精神上与Naor于2003年提出的可证伪性理念相似，并体现了我们能够高效检验敌手策略是否破坏了该假设的核心特征。

我们的分离结果同样适用于指定验证者的SNARGs（其中验证者需要与CRS相关联的陷门来验证论证）以及略微简洁的SNARGs（其规模仅需在陈述和见证规模上呈亚线性）。

## 关键词

+ 简洁非交互式论证SNARG
+ 黑盒分离结果
+ 可证伪密码学假设
+ 随机预言机模型
+ 指定验证者论证系统
+ 简洁论证安全性基础
