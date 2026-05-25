---
title: "Subvector commitments with application to succinct arguments"
标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 2019
modified: 2025-04-11 11:24:32
---

## Subvector commitments with application to succinct arguments

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-030-26948-7_19)

## 作者

+ Russell WF Lai 
+ [Giulio Malavolta](Giulio%20Malavolta.md)
## 笔记

We put forward the notion of subvector commitments (SVC): An SVC allows one to open a committed vector at a set of positions, where the opening size is independent of length of the committed vector and the number of positions to be opened. We propose two constructions under variants of the root assumption and the CDH assumption, respectively. We further generalize SVC to a notion called linear map commitments (LMC), which allows one to open a committed vector to its images under linear maps with a single short message, and propose a construction over pairing groups.

Equipped with these newly developed tools, we revisit the “CS proofs” paradigm [Micali, FOCS 1994] which turns any arguments with public-coin verifiers into non-interactive arguments using the Fiat-Shamir transform in the random oracle model. We propose a compiler that turns any (linear, resp.) PCP into a non-interactive argument, using exclusively SVCs (LMCs, resp.). For an approximate 80 bits of soundness, we highlight the following new implications:

1. There exists a succinct non-interactive argument of knowledge (SNARK) with public-coin setup with proofs of size 5360 bits, under the adaptive root assumption over class groups of imaginary quadratic orders against adversaries with runtime $2^{128}$. At the time of writing, this is the shortest SNARK with public-coin setup.

2. There exists a non-interactive argument with private-coin setup, where proofs consist of 2 group elements and 3 field elements, in the generic bilinear group model.

以下是中文翻译：

我们提出了子向量承诺(subvector commitments, SVC)的概念：SVC允许在一组位置打开已承诺的向量，其中开启大小独立于已承诺向量的长度和需要开启的位置数量。我们分别基于根假设(root assumption)的变体和CDH假设(CDH assumption)提出了两种构造方案。我们进一步将SVC推广到一个称为线性映射承诺(linear map commitments, LMC)的概念，它允许通过单个简短消息将已承诺的向量开启到其在线性映射下的像，并在配对群上提出了一种构造方案。

借助这些新开发的工具，我们重新审视了"CS证明"范式[Micali, FOCS 1994]，该范式在随机预言模型中使用Fiat-Shamir变换将任何具有公共币验证者的论证转化为非交互式论证。我们提出了一个编译器，它专门使用SVC（分别使用LMC）将任何（线性）PCP转化为非交互式论证。对于约80比特的可靠性，我们强调以下新的推论：

1. 在虚二次序类群上的自适应根假设下，针对运行时间为$2^{128}$的对手，存在一个具有公共币设置的简洁非交互式知识论证(SNARK)，其证明大小为5360比特。在撰写本文时，这是具有公共币设置的最短SNARK。

2. 在通用双线性群模型中，存在一个具有私有币设置的非交互式论证，其证明由2个群元素和3个域元素组成。

## 关键词

+ 密码学
+ 零知识
+ 协议