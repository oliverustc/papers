---
title: "Marlin: Preprocessing zkSNARKs with universal and updatable SRS"
标题简称: Marlin
论文类型: conference
会议简称: EUROCRYPT
发表年份: 2020
modified: 2025-04-27 09:07:03
created: 2025-04-08 17:30:40
---

## Marlin: Preprocessing zkSNARKs with universal and updatable SRS

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-030-45721-1_26)

## 作者

+ [Alessandro Chiesa](Alessandro%20Chiesa.md)
+ [Yuncong Hu](Yuncong%20Hu.md)
+ [Mary Maller](Mary%20Maller.md)
+ [Pratyush Mishra](Pratyush%20Mishra.md)
+ Noah Vesely
+ Nicholas Ward

## 笔记

We present a methodology to construct preprocessing zkSNARKs where the structured reference string (SRS) is universal and updatable. This exploits a novel use of _holography_ [Babai et al., STOC 1991], where fast verification is achieved provided the statement being checked is given in encoded form.

We use our methodology to obtain a preprocessing zkSNARK where the SRS has linear size and arguments have constant size. Our construction improves on Sonic [Maller et al., CCS 2019], the prior state of the art in this setting, in all efficiency parameters: proving is an order of magnitude faster and verification is thrice as fast, even with smaller SRS size and argument size. Our construction is most efficient when instantiated in the algebraic group model (also used by Sonic), but we also demonstrate how to realize it under concrete knowledge assumptions. We implement and evaluate our construction.

The core of our preprocessing zkSNARK is an efficient _algebraic holographic proof_ (AHP) for rank-1 constraint satisfiability (R1CS) that achieves linear proof length and constant query complexity.

以下是中文翻译：

我们提出了一种构建预处理零知识简洁非交互式知识论证(preprocessing zkSNARK)的方法,其中结构化参考字符串(SRS)具有通用性和可更新性。这种方法新颖地运用了全息技术[Babai et al., STOC 1991],只要待验证的陈述以编码形式给出,就能实现快速验证。

我们利用这种方法获得了一个预处理zkSNARK,其SRS具有线性大小,而论证具有常量大小。我们的构造在所有效率参数上都优于该领域此前最先进的[Sonic Maller et al., CCS 2019](maller2019sonic):证明速度提高了一个数量级,验证速度提高了三倍,同时SRS大小和论证大小都更小。我们的构造在代数群模型(algebraic group model)中实现时效率最高(Sonic也使用了该模型),但我们也展示了如何在具体的知识假设下实现它。我们实现并评估了这个构造。

我们的预处理zkSNARK的核心是一个高效的代数全息证明(AHP),用于秩1约束可满足性(R1CS)问题,该证明实现了线性的证明长度和常量的查询复杂度。

## 关键词

+ 预处理zkSNARK
+ 通用更新结构化参考字符串
+ 代数全息证明
+ R1CS约束系统
+ Marlin