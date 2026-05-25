---
title: "Monotone-policy aggregate signatures"
标题简称:
论文类型: conference
会议简称: EUROCRYPT
发表年份: 2024
created: 2025-04-28 11:29:47
modified: 2025-04-28 11:32:27
---

## Monotone-policy aggregate signatures

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-58737-5_7)

## 作者

+ Maya Farber Brodsky 
+ [Arka Rai Choudhuri](Arka%20Rai%20Choudhuri.md)
+ [Abhishek Jain](Abhishek%20Jain.md)
+ Omer Paneth 

## 笔记

The notion of aggregate signatures allows for combining signatures from different parties into a short certificate that attests that _all_ parties signed a message. In this work, we lift this notion to capture different, more expressive signing policies. For example, we can certify that a message was signed by a (weighted) threshold of signers.

We present the first constructions of aggregate signatures for monotone policies based on standard polynomial-time cryptographic assumptions. The aggregate signatures in our schemes are succinct, i.e., their size is _independent_ of the number of signers. Moreover, verification is also succinct if all parties sign the same message (or if the messages have a succinct representation). All prior work requires either interaction between the parties or non-standard assumptions (that imply SNARKs for NP).

Our signature schemes are based on non-interactive batch arguments (BARGs) for monotone policies [Brakerski-Brodsky-Kalai-Lombardi-Paneth, Crypto’23]. In contrast to previous constructions, our BARGs satisfy a new notion of _adaptive_ security which is instrumental to our application. Our new BARGs for monotone policies can be constructed from standard BARGs and other standard assumptions.

以下是中文翻译：

聚合签名(aggregate signatures)的概念允许将来自不同参与方的签名组合成一个简短的证书，以证明所有参与方都签署了某个消息。在本研究中，我们扩展了这一概念以涵盖不同的、更具表达力的签名策略。例如，我们可以证明一个消息是由（加权）阈值数量的签名者签署的。

我们提出了基于标准多项式时间密码学假设的首个单调策略(monotone policies)聚合签名构造方案。我们方案中的聚合签名具有简洁性，即其大小与签名者数量无关。此外，如果所有参与方签署相同的消息（或者消息具有简洁表示），验证过程也是简洁的。所有先前的工作要么需要参与方之间的交互，要么需要非标准假设（这些假设暗含了NP问题的简洁非交互式知识论证(SNARKs)）。

我们的签名方案基于单调策略的非交互式批处理论证(BARGs)[Brakerski-Brodsky-Kalai-Lombardi-Paneth, Crypto'23]。与之前的构造不同，我们的BARGs满足一种新的自适应安全性(adaptive security)概念，这对我们的应用至关重要。我们针对单调策略的新型BARGs可以通过标准BARGs和其他标准假设来构造。

## 关键词

+ 单调策略聚合签名
+ 非交互式批处理论证
+ 自适应安全性
+ 简洁签名
+ 门限签名策略
