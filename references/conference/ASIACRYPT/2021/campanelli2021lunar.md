---
title: "Lunar: a toolbox for more efficient universal and updatable zkSNARKs and commit-and-prove extensions"
标题简称:
论文类型: conference
会议简称: ASIACRYPT
发表年份: 2021
modified: 2025-04-13 17:40:03
---

## Lunar: a toolbox for more efficient universal and updatable zkSNARKs and commit-and-prove extensions

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-030-92078-4_1)

## 作者

+ [Matteo Campanelli](Matteo%20Campanelli.md)
+ Antonio Faonio 
+ [Dario Fiore](Dario%20Fiore.md)
+ Anais Querol 
+ Hadrián Rodriguez 

## 笔记

We study how to construct zkSNARKs whose SRS is _universal_ and _updatable_, i.e., valid for all relations within a size-bound and to which a dynamic set of participants can indefinitely add secret randomness. Our focus is: efficient universal updatable zkSNARKs with linear-size SRS and their commit-and-prove variants. We both introduce new formal frameworks and techniques, as well as systematize existing ones.  

以下是中文翻译：

我们研究如何构建具有通用性和可更新性的zkSNARKs系统，其结构化参考字符串（SRS）适用于所有规模限制内的关系，并且允许动态参与者群体持续添加秘密随机性。我们的核心关注点是：实现线性规模SRS的高效通用可更新zkSNARKs及其承诺-证明变体。研究既引入了新的形式化框架与技术，也对现有方法进行了系统化梳理。

We achieve a collection of zkSNARKs with different tradeoffs. One of our schemes achieves the smallest proof size and proving time compared to the state of art for proofs for arithmetic circuits. The language supported by this scheme is a variant of R1CS that we introduce, called R1CS-lite. Another of our constructions directly supports standard R1CS and achieves the fastest proving time for this type of constraints.  
我们实现了一系列具有不同权衡特性的zkSNARK方案。其中一项方案在算术电路证明方面，相较于现有技术，实现了最小的证明尺寸和最快的证明时间。该方案支持的语言是我们引入的一种R1CS变体，称为R1CS-lite。另一项构造则直接支持标准R1CS，并在处理此类约束时达到了最快的证明速度。

These results stem from different contributions: (1) a new algebraically-flavored variant of IOPs that we call _Polynomial Holographic IOPs_ (PHPs); (2) a new compiler that combines our PHPs with _commit-and-prove zkSNARKs_ (CP-SNARKs) for committed polynomials; (3) pairing-based realizations of these CP-SNARKs for polynomials; (4) constructions of PHPs for R1CS and R1CS-lite. Finally, we extend the compiler in item (2) to yield commit-and-prove universal zkSNARKs.  
这些成果源于多方面的贡献：（1）我们提出了一种新的代数风格交互式预言证明（IOP）变体，称为多项式全息IOP（PHPs）；（2）开发了一个新编译器，将我们的PHPs与针对承诺多项式的承诺-证明零知识简洁非交互式论证（CP-SNARKs）相结合；（3）实现了基于配对技术的多项式CP-SNARKs；（4）为R1CS及简化版R1CS设计了PHP构造方案。最后，我们扩展了第二项中的编译器功能，使其能够生成通用的承诺-证明零知识SNARKs。

## 关键词

+ zkSNARK
+ 可更新参数
+ 多项式承诺
+ R1CS
+ 证明可组合性