---
title: "zkPyTorch: A Hierarchical Optimized Compiler for Zero-Knowledge Machine Learning"
标题简称:
论文类型: preprint
预印本简称: archive
发表年份: 2025
created: 2025-06-09 02:22:05
modified: 2025-06-09 02:22:54
---

## zkPyTorch: A Hierarchical Optimized Compiler for Zero-Knowledge Machine Learning

## 发表信息

+ [原文链接](https://eprint.iacr.org/2025/535)

## 作者

+ [Tiancheng Xie](Tiancheng%20Xie.md)
+ Tao Lu
+ [Zhiyong Fang](Zhiyong%20Fang.md)
+ Siqi Wang
+ [Zhenfei Zhang](Zhenfei%20Zhang.md)
+ Yongzheng Jia
+ [Dawn Song](Dawn%20Song.md)
+ [Jiaheng Zhang](Jiaheng%20Zhang.md)

## 笔记

As artificial intelligence (AI) becomes increasingly embedded in high-stakes applications such as healthcare, finance, and autonomous systems, ensuring the verifiability of AI computations without compromising sensitive data or proprietary models is crucial. Zero-knowledge machine learning (ZKML) leverages zero-knowledge proofs (ZKPs) to enable the verification of AI model outputs while preserving confidentiality. However, existing ZKML approaches require specialized cryptographic expertise, making them inaccessible to traditional AI developers. In this paper, we introduce ZKPyTorch, a compiler that seamlessly integrates ML frameworks like PyTorch with ZKP engines like Expander, simplifying the development of ZKML. ZKPyTorch automates the translation of ML operations into optimized ZKP circuits through three key components. First, a ZKP preprocessor converts models into structured computational graphs and injects necessary auxiliary information to facilitate proof generation. Second, a ZKP-friendly quantization module introduces an optimized quantization strategy that reduces computation bit-widths, enabling efficient ZKP execution within smaller finite fields such as M61. Third, a hierarchical ZKP circuit optimizer employs a multi-level optimization framework at model, operation, and circuit levels to improve proof generation efficiency. We demonstrate ZKPyTorch effectiveness through end-to-end case studies, successfully converting VGG-16 and Llama-3 models from PyTorch, a leading ML framework, into ZKP-compatible circuits recognizable by Expander, a state-of-the-art ZKP engine. Using Expander, we generate zero-knowledge proofs for these models, achieving proof generation for the VGG-16 model in 2.2 seconds per CIFAR-10 image for VGG-16 and 150 seconds per token for Llama-3 inference, improving the practical adoption of ZKML.

以下是中文翻译：

随着人工智能（Artificial Intelligence, AI）日益深入医疗、金融和自动驾驶等高风险应用领域，在确保敏感数据和专有模型安全的前提下实现AI计算的可验证性变得至关重要。零知识机器学习（Zero-Knowledge Machine Learning, ZKML）利用零知识证明（Zero-Knowledge Proofs, ZKPs）技术，可在保护机密性的同时验证AI模型输出。然而，现有ZKML方法需要专门的密码学专业知识，导致传统AI开发者难以使用。

本文提出ZKPyTorch——一个将PyTorch等机器学习框架与Expander等ZKP引擎无缝集成的编译器，旨在简化ZKML开发流程。ZKPyTorch通过三大核心组件自动将ML运算转化为优化的ZKP电路：首先，ZKP预处理模块将模型转换为结构化计算图，并注入必要的辅助信息以支持证明生成；其次，ZKP友好型量化模块采用优化量化策略降低计算位宽，使其能在M61等更小的有限域内高效执行ZKP；最后，分层式ZKP电路优化器在模型、操作和电路三个层级实施多级优化框架，显著提升证明生成效率。

我们通过端到端案例研究验证了ZKPyTorch的有效性：成功将主流ML框架PyTorch中的VGG-16和Llama-3模型转换为先进ZKP引擎Expander可识别的ZKP兼容电路。基于Expander生成的零知识证明，VGG-16模型在CIFAR-10数据集上单张图片的证明耗时2.2秒，Llama-3推理每个token的证明耗时150秒，推动了ZKML的实际应用落地。


## 关键词

+ zkPyTorch零知识机器学习编译器
+ PyTorch ZKP电路自动化转换
+ 分层ZKP电路优化框架
+ ZKP友好量化有限域计算
+ VGG Llama模型零知识证明生成