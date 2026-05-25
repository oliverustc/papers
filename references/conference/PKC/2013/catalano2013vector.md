---
title: "Vector commitments and their applications"
标题简称:
论文类型: conference
会议简称: PKC
发表年份: 2013
---

## Vector commitments and their applications

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-642-36362-7_5)

## 作者

+ Dario Catalano 
+ [Dario Fiore](Dario%20Fiore.md)
## 笔记

We put forward the study of a new primitive that we call Vector Commitment (VC, for short). Informally, VCs allow to commit to an ordered sequence of q values (m 1, . . . , mq) in such a way that one can later open the commitment at specific positions (e.g., prove that mi is the i-th committed message). For security, Vector Commitments are required to satisfy a notion that we call position binding which states that an adversary should not be able to open a commitment to two different values at the same position. Moreover, what makes our primitive interesting is that we require VCs to be concise, i.e. the size of the commitment string and of its openings has to be independent of the vector length.

We show two realizations of VCs based on standard and well established assumptions, such as RSA, and Computational Diffie-Hellman (in bilinear groups). Next, we turn our attention to applications and we show that Vector Commitments are useful in a variety of contexts, as they allow for compact and efficient solutions which significantly improve previous works either in terms of efficiency of the resulting solutions, or in terms of ”quality” of the underlying assumption, or both. These applications include: Verifiable Databases with Efficient Updates, Updatable Zero-Knowledge Databases, and Universal Dynamic Accumulators.


以下是中文翻译：

我们提出了一种新型密码学原语的研究，称之为向量承诺（Vector Commitment，简称 VC）。非正式地讲，向量承诺允许对一个有序的 q 元序列（m₁, …, m_q）进行承诺，使得承诺者后续能够在特定位置打开该承诺（例如，证明 m_i 是第 i 个被承诺的消息）。在安全性方面，向量承诺需满足一种我们称之为位置绑定（position binding）的性质，即敌手无法在同一位置对两个不同的值同时打开同一个承诺。此外，该原语的突出之处在于我们要求向量承诺具备简洁性（concise）：承诺字符串及其打开证明的大小必须与向量长度无关。

我们基于标准且被广泛接受的计算假设（如 RSA 假设和双线性群中的计算性 Diffie-Hellman（Computational Diffie-Hellman）假设）给出了两种向量承诺的具体实现。随后，我们将注意力转向其应用，并表明向量承诺在多种场景中具有实用价值：它们能够实现紧凑且高效的解决方案，在效率、底层假设的“质量”（即假设的可信度或标准性），或两者兼而有之地显著优于已有工作。这些应用场景包括：支持高效更新的可验证数据库（Verifiable Databases with Efficient Updates）、可更新的零知识数据库（Updatable Zero-Knowledge Databases）以及通用动态累加器（Universal Dynamic Accumulators）。

## 关键词

+ 向量承诺
+ 位置绑定
+ 简洁承诺
+ 可验证数据库
+ 动态累加器
+ 零知识数据库