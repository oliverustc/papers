---
title: "Efficient verifiable delay functions"
标题简称:
论文类型: conference
会议简称: EUROCRYPT
发表年份: 2019
created: 2025-04-28 16:45:56
modified: 2025-04-28 16:46:28
---

## Efficient verifiable delay functions

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-030-17659-4_13)

## 作者

+ Benjamin Wesolowski 

## 笔记

We construct a verifiable delay function (VDF). A VDF is a function whose evaluation requires running a given number of sequential steps, yet the result can be efficiently verified. They have applications in decentralised systems, such as the generation of trustworthy public randomness in a trustless environment, or resource-efficient blockchains. To construct our VDF, we actually build a _trapdoor_ VDF. A trapdoor VDF is essentially a VDF which can be evaluated efficiently by parties who know a secret (the trapdoor). By setting up this scheme in a way that the trapdoor is unknown (not even by the party running the setup, so that there is no need for a trusted setup environment), we obtain a simple VDF. Our construction is based on groups of unknown order such as an RSA group, or the class group of an imaginary quadratic field. The output of our construction is very short (the result and the proof of correctness are each a single element of the group), and the verification of correctness is very efficient.

以下是中文翻译：

我们构建了一个可验证延迟函数(verifiable delay function, VDF)。VDF是一种需要运行指定数量顺序步骤才能求值，但其结果可以被高效验证的函数。它们在去中心化系统中有着广泛应用，例如在无信任环境中生成可信的公共随机性，或构建资源高效的区块链。

为了构建我们的VDF，我们实际上构建了一个陷门VDF(trapdoor VDF)。陷门VDF本质上是一种对于知道密钥（即陷门）的参与方来说可以高效求值的VDF。通过以一种陷门未知的方式设置这个方案（即使是运行设置的参与方也不知道陷门，因此不需要可信的设置环境），我们获得了一个简单的VDF。

我们的构造基于未知阶群(groups of unknown order)，如RSA群或虚二次域(imaginary quadratic field)的类群(class group)。我们构造的输出非常简短（结果和正确性证明各自都只是群中的一个元素），并且正确性验证非常高效。

## 关键词

+ 可验证延迟函数
+ 陷门VDF
+ 未知阶群
+ RSA群
+ 去中心化随机性