---
title: "ZKML: An Optimizing System for ML Inference in Zero-Knowledge Proofs"
标题简称:
论文类型: conference
会议简称: EuroSys
发表年份: 2024

modified: 2025-04-09 09:26:18
---

## ZKML: An Optimizing System for ML Inference in Zero-Knowledge Proofs

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3627703.3650088)

## 作者

+ Bing-Jyue Chen
+ Suppakit Waiwitlikhit
+ Ion Stoica
+ Daniel Kang

## 笔记

Machine learning (ML) is increasingly used behind closed systems and APIs to make important decisions. For example, social media uses ML-based recommendation algorithms to decide what to show users, and millions of people pay to use ChatGPT for information every day. Because ML is deployed behind these closed systems, there are increasing calls for transparency, such as releasing model weights. However, these service providers have legitimate reasons not to release this information, including for privacy and trade secrets. To bridge this gap, recent work has proposed using zero-knowledge proofs (specifically a form called ZK-SNARKs) for certifying computation with private models but has only been applied to unrealistically small models.
In this work, we present the first framework, ZKML, to produce ZK-SNARKs for realistic ML models, including state-of-the-art vision models, a distilled GPT-2, and the ML model powering Twitter's recommendations. We accomplish this by designing an optimizing compiler from TensorFlow to circuits in the halo2 ZK-SNARK proving system. There are many equivalent ways to implement the same operations within ZK-SNARK circuits, and these design choices can affect performance by 24×. To efficiently compile ML models, ZKML contains two parts: gadgets (efficient constraints for low-level operations) and an optimizer to decide how to lay out the gadgets within a circuit. Combined, these optimizations enable proving on a wider range of models, faster proving, faster verification, and smaller proofs compared to prior work.

以下是中文翻译：

机器学习（ML）越来越多地用于封闭系统和API中，以做出重要决策。例如，社交媒体使用基于ML的推荐算法来决定向用户展示什么内容，数以百万计的人每天支付使用ChatGPT获取信息。由于ML部署在这些封闭系统中，因此对透明度的呼声日益高涨，例如要求发布模型权重。然而，这些服务提供商有正当理由不公开这些信息，包括隐私和商业机密。为了弥补这一差距，最近的工作提出使用零知识证明（zero-knowledge proofs，特别是一种称为ZK-SNARKs的形式）来认证具有私有模型的计算，但仅应用于不切实际的小模型。

在本工作中，我们提出了第一个框架ZKML，用于为现实的ML模型生成ZK-SNARKs，包括最先进的视觉模型、一个提炼的GPT-2以及支撑Twitter推荐的ML模型。我们通过设计一个优化编译器，将TensorFlow中的操作编译为halo2 ZK-SNARK证明系统中的电路来实现这一目标。在ZK-SNARK电路中，有许多等效的方法可以实现相同的操作，这些设计选择可能会影响性能高达24倍。为了高效编译ML模型，ZKML包含两个部分：小工具（gadgets，低级操作的高效约束）和一个优化器，用于决定如何在电路中布局小工具。综合这些优化，使得在更广泛的模型上进行证明、加快证明速度、加快验证速度以及生成更小的证明，相较于以前的工作都有了显著提升。

## 关键词

+ 机器学习推理证明
+ ZK-SNARK
+ zkML编译器
+ halo2证明系统
+ 私有模型认证
+ 优化编译器