---
title: "Kryvos: Publicly tally-hiding verifiable e-voting"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2022
created: 2025-05-07 21:48:00
modified: 2025-05-07 21:48:32
---

## Kryvos: Publicly tally-hiding verifiable e-voting

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3548606.3560701)

## 作者

+ Nicolas Huber 
+ [Ralf Küsters](Ralf%20K%C3%BCsters.md)
+ Toomas Krips 
+ Julian Liedtke 
+ Johannes Müller 
+ [Daniel Rausch](Daniel%20Rausch.md)
+ Pascal Reisert 
+ Andreas Vogt 

## 笔记

Elections are an important corner stone of democratic processes. In addition to publishing the final result (e.g., the overall winner), elections typically publish the full tally consisting of all (aggregated) individual votes. This causes several issues, including loss of privacy for both voters and election candidates as well as so-called Italian attacks that allow for easily coercing voters.

Several e-voting systems have been proposed to address these issues by hiding (parts of) the tally. This property is called tally-hiding. Existing tally-hiding e-voting systems in the literature aim at hiding (part of) the tally from everyone, including voting authorities, while at the same time offering verifiability, an important and standard feature of modern e-voting systems which allows voters and external observers to check that the published election result indeed corresponds to how voters actually voted. In contrast, real elections often follow a different common practice for hiding the tally: the voting authorities internally compute (and learn) the full tally but publish only the final result (e.g., the winner). This practice, which we coin publicly tally-hiding, indeed solves the aforementioned issues for the public, but currently has to sacrifice verifiability due to a lack of practical systems.

In this paper, we close this gap. We formalize the common notion of publicly tally-hiding and propose the first provably secure verifiable e-voting system, called Kryvos, which directly targets publicly tally-hiding elections. We instantiate our system for a wide range of both simple and complex voting methods and various result functions. We provide an extensive evaluation which shows that Kryvos is practical and able to handle a large number of candidates, complex voting methods and result functions. Altogether, Kryvos shows that the concept of publicly tally-hiding offers a new trade-off between privacy and efficiency that is different from all previous tally-hiding systems and which allows for a radically new protocol design resulting in a practical e-voting system.

以下是中文翻译：

选举是民主过程的重要基础。除了公布最终结果（例如整体胜者）外，选举通常会公布包含所有（汇总的）个人投票的完整计数。这会导致几个问题，包括对投票人和选举候选人隐私的损失，以及所谓的意大利攻击（Italian attacks），这些攻击允许轻易强制选民。

已经提出了几个电子投票系统来通过隐藏（部分）计数来解决这些问题。这一特性被称为隐藏计数（tally-hiding）。文献中现有的隐藏计数电子投票系统旨在向所有人（包括投票机构）隐藏计数（部分），同时提供可验证性，这是现代电子投票系统的重要和标准特征，允许选民和外部观察者检查公布的选举结果是否确实对应于选民实际投票的方式。相反，真实选举通常遵循隐藏计数的不同常见做法：投票机构在内部计算（并学习）完整计数，但只公布最终结果（例如胜者）。我们将这一做法称为"公开隐藏计数"（publicly tally-hiding），它确实为公众解决了上述问题，但目前由于缺乏实用系统，必须牺牲可验证性。

在本文中，我们弥补了这一空白。我们形式化了公开计数隐藏（publicly tally-hiding）的常见概念，并提出了首个可证明安全的可验证电子投票系统Kryvos，该系统直接针对公开计数隐藏选举。我们为广泛的简单和复杂投票方法及各种结果函数实现了我们的系统。我们提供了广泛的评估，表明Kryvos是实用的，能够处理大量候选者、复杂的投票方法和结果函数。总之，Kryvos表明，公开计数隐藏的概念提供了隐私和效率之间的新折衷方案，这与所有先前的计数隐藏系统不同，并允许一种激进的新协议设计，从而形成实用的电子投票系统。

## 关键词

+ 电子投票
+ 隐私保护
+ 零知识证明
+ 可验证性
+ 民主制度