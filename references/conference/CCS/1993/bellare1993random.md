---
title: "Random oracles are practical: a paradigm for designing efficient protocols"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 1993
modified: 2025-04-08 11:41:08
---

## Random oracles are practical: a paradigm for designing efficient protocols

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/168588.168596)
+ [2021年重制版](https://cseweb.ucsd.edu/~Mihir/papers/ro.pdf)

## 作者

+ [Mihir Bellare](Mihir%20Bellare.md)
+ Phillip Rogaway

## 笔记

> **Abstract**
> We argue that the random oracle model—where all parties have access to a public random oracle—provides a bridge between cryptographic theory and cryptographic practice. In the paradigm we suggest, a practical protocol P is produced by first devising and proving correct a protocol PR for the random oracle model, and then replacing oracle accesses by the computation of an “appropriately chosen” function h. This paradigm yields protocols much more efficient than standard ones while retaining many of the advantages of provable security. We illustrate these gains for problems including encryption, signatures, and zero-knowledge proofs.

以下是中文翻译：

我们认为，随机预言模型——所有参与方都能访问一个公共的随机预言——为密码学理论与密码学实践之间架起了一座桥梁。在我们提出的范式中，首先设计并证明随机预言模型下的协议P的正确性，随后用”恰当选择”的函数h的计算替代对预言的访问，从而产生一个实用的协议P。这一范式不仅保留了可证明安全性的诸多优势，还使得协议比传统方法高效得多。我们通过加密、签名及零知识证明等问题展示了这些优势。

## 关键词

+ 随机预言模型
+ 可证明安全性
+ 数字签名
+ 零知识证明
+ 加密协议