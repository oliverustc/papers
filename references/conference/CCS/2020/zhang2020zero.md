---
title: "Zero Knowledge Proofs for Decision Tree Predictions and Accuracy"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2020

modified: 2025-05-07 22:34:11
created: 2025-04-07 16:21:14
---

## Zero Knowledge Proofs for Decision Tree Predictions and Accuracy

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3372297.3417278)

## 作者

+ [Jiaheng Zhang](Jiaheng%20Zhang.md)
+ [Zhiyong Fang](Zhiyong%20Fang.md)
+ [Yupeng Zhang](Yupeng%20Zhang.md)
+ [Dawn Song](Dawn%20Song.md)

## 笔记

Machine learning has become increasingly prominent and is widely used in various applications in practice. Despite its great success, the integrity of machine learning predictions and accuracy is a rising concern. The reproducibility of machine learning models that are claimed to achieve high accuracy remains challenging, and the correctness and consistency of machine learning predictions in real products lack any security guarantees. In this paper, we initiate the study of zero knowledge machine learning and propose protocols for zero knowledge decision tree predictions and accuracy tests. The protocols allow the owner of a decision tree model to convince others that the model computes a prediction on a data sample, or achieves a certain accuracy on a public dataset, without leaking any information about the model itself. We develop approaches to efficiently turn decision tree predictions and accuracy into statements of zero knowledge proofs. We implement our protocols and demonstrate their efficiency in practice. For a decision tree model with 23 levels and 1,029 nodes, it only takes 250 seconds to generate a zero knowledge proof proving that the model achieves high accuracy on a dataset of 5,000 samples and 54 attributes, and the proof size is around 287 kilobytes.

以下是中文翻译：

机器学习(machine learning)已变得越来越重要，并在实践中被广泛应用于各种场景。尽管取得了巨大成功，但机器学习预测的完整性和准确性已成为一个日益突出的问题。声称能够达到高准确率的机器学习模型的可复现性仍然具有挑战性，而实际产品中机器学习预测的正确性和一致性也缺乏任何安全保证。

在本文中，我们开创性地研究了零知识机器学习(zero knowledge machine learning)，并提出了零知识决策树预测和准确率测试的协议。这些协议允许决策树模型的所有者在不泄露模型本身任何信息的情况下，向他人证明该模型能够对数据样本进行预测，或在公共数据集上达到特定的准确率。我们开发了一种方法，可以高效地将决策树预测和准确率转化为零知识证明的陈述。

我们实现了这些协议并证明了它们在实践中的效率。对于一个具有23层和1,029个节点的决策树模型，仅需250秒就能生成零知识证明，证明该模型在一个包含5,000个样本和54个属性的数据集上达到了高准确率，且证明的大小约为287千字节。

## 关键词

+ 零知识证明
+ 机器学习
+ 决策树
+ 隐私保护
+ 完整性验证
