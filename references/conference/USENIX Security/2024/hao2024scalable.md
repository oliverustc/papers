---
title: "Scalable Zero-knowledge Proofs for Non-linear Functions in Machine Learning"
标题简称:
论文类型: conference
会议简称: USENIX Security
发表年份: 2024

modified: 2025-05-07 22:36:19
created: 2025-04-07 17:02:00
---

## Scalable Zero-knowledge Proofs for Non-linear Functions in Machine Learning

## 发表信息

+ [原文链接](https://www.usenix.org/conference/usenixsecurity24/presentation/hao-meng-scalable)

## 作者

+ [Meng Hao](Meng%20Hao.md)
+ Hanxiao Chen
+ [Hongwei Li](Hongwei%20Li.md)
+ [Chenkai Weng](Chenkai%20Weng.md)
+ Yuan Zhang
+ Haomiao Yang
+ Tianwei Zhang

## 笔记

Zero-knowledge (ZK) proofs have been recently explored for the integrity of machine learning (ML) inference. However, these protocols suffer from high computational overhead, with the primary bottleneck stemming from the evaluation of non-linear functions. In this paper, we propose the first systematic ZK proof framework for non-linear mathematical functions in ML using the perspective of table lookup. The key challenge is that table lookup cannot be directly applied to non-linear functions in ML since it would suffer from inefficiencies due to the intolerably large table. Therefore, we carefully design several important building blocks, including digital decomposition, comparison, and truncation, such that they can effectively utilize table lookup with a quite small table size while ensuring the soundness of proofs. Based on these building blocks, we implement complex mathematical operations and further construct ZK proofs for current mainstream non-linear functions in ML such as ReLU, sigmoid, and normalization. The extensive experimental evaluation shows that our framework achieves 50∼179× runtime improvement compared to the state-of-the-art work, while maintaining a similar level of communication efficiency.

以下是中文翻译：

零知识证明(Zero-knowledge proofs, ZK proofs)近期被探索用于机器学习(Machine Learning, ML)推理的完整性验证。然而，这些协议存在较高的计算开销，主要瓶颈来自非线性函数的计算。在本文中，我们从查表的角度提出了第一个针对机器学习中非线性数学函数的系统性零知识证明框架。主要挑战在于查表方法不能直接应用于机器学习中的非线性函数，因为这会由于过大的表格规模导致效率低下。因此，我们精心设计了几个重要的基础模块，包括数字分解、比较和截断，使它们能够在确保证明可靠性的同时，通过相当小的表格大小有效地利用查表方法。基于这些基础模块，我们实现了复杂的数学运算，并进一步构建了针对当前主流机器学习非线性函数（如ReLU、sigmoid和归一化）的零知识证明。大量实验评估表明，与最先进的工作相比，我们的框架在保持类似通信效率水平的同时，实现了50~179倍的运行时间改进。

## 关键词

+ 机器学习非线性函数ZK证明
+ 查表方法零知识优化
+ ReLU sigmoid归一化ZK证明
+ 数字分解比较截断构建块
+ 机器学习推理完整性验证
+ 零知识证明计算开销优化
