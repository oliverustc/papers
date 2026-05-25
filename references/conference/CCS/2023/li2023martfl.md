---
title: "martfl: Enabling utility-driven data marketplace with a robust and verifiable federated learning architecture"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2023
created: 2025-04-19 11:08:28
modified: 2025-04-19 11:09:10
---

## martfl: Enabling utility-driven data marketplace with a robust and verifiable federated learning architecture

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3576915.3623134)

## 作者

+ [Qi Li](Qi%20Li.md)
+ Zhuotao Liu 
+ [Qi Li](Qi%20Li.md)
+ Ke Xu 

## 笔记

The development of machine learning models requires a large amount of training data. Data marketplace is a critical platform to trade high-quality and private-domain data that is not publicly available on the Internet. However, as data privacy becomes increasingly important, directly exchanging raw data becomes inappropriate. Federated Learning (FL) is a distributed machine learning paradigm that exchanges data utilities (in form of local models or gradients) among multiple parties without directly sharing the original data. However, we recognize several key challenges in applying existing FL architectures to construct a data marketplace. (i) In existing FL architectures, the Data Acquirer (DA) cannot privately assess the quality of local models submitted by different Data Providers (DPs) prior to trading; (ii)The model aggregation protocols in existing FL designs cannot effectively exclude malicious DPs without "overfitting'' to the DA's (possibly biased) root dataset; (iii) Prior FL designs lack a proper billing mechanism to enforce the DA to fairly allocate the reward according to contributions made by different DPs. To address above challenges, we propose martFL, the first federated learning architecture that is specifically designed to enable a secure utility-driven data marketplace. At a high level, martFL is empowered by two innovative designs: (i) a quality-aware model aggregation protocol that allows the DA to properly exclude local-quality or even poisonous local models from the aggregation, even if the DA's root dataset is biased; (ii) a verifiable data transaction protocol that enables the DA to prove, both succinctly and in zero-knowledge, that it has faithfully aggregated these local models according to the weights that the DA has committed to. This enables the DPs to unambiguously claim the rewards proportional to their weights/contributions. We implement a prototype of martFL and evaluate it extensively over various tasks. The results show that martFL can improve the model accuracy by up to 25% while saving up to 64% data acquisition cost.

以下是中文翻译：

机器学习模型的开发需要大量的训练数据。数据市场是一个重要的平台，用于交易高质量和私有领域的数据，这些数据在互联网上并不公开。然而，随着数据隐私变得越来越重要，直接交换原始数据变得不合适。联邦学习（Federated Learning, FL）是一种分布式机器学习范式，它在多个参与方之间交换数据效用（以本地模型或梯度的形式），而不直接共享原始数据。然而，我们认识到在构建数据市场时，现有FL架构面临几个关键挑战：（i）在现有的FL架构中，数据获取者（Data Acquirer, DA）无法在交易之前私下评估不同数据提供者（Data Providers, DPs）提交的本地模型的质量；（ii）现有FL设计中的模型聚合协议无法有效排除恶意DP，而不会对DA的（可能存在偏差的）根数据集“过拟合”；（iii）之前的FL设计缺乏适当的计费机制，无法强制DA根据不同DP的贡献公平分配奖励。为了解决上述挑战，我们提出了martFL，这是第一个专门设计用于实现安全的效用驱动数据市场的联邦学习架构。从高层次来看，martFL通过两个创新设计得以实现：（i）一个质量感知的模型聚合协议，允许DA适当地排除本地质量较差甚至有毒的本地模型，即使DA的根数据集存在偏差；（ii）一个可验证的数据交易协议，使DA能够简洁且以零知识的方式证明其根据DA承诺的权重忠实地聚合了这些本地模型。这使得DP能够明确地根据其权重/贡献主张相应的奖励。我们实现了martFL的原型，并在各种任务上进行了广泛评估。结果表明，martFL可以将模型准确率提高最多25%，同时节省高达64%的数据获取成本。

## 关键词

+ 联邦学习
+ 数据市场
+ 零知识证明
+ 可验证性
+ 模型聚合
+ 隐私保护
+ 恶意防护