---
title: "Drynx: Decentralized, Secure, Verifiable System for Statistical Queries and Machine Learning on Distributed Datasets"
标题简称: Drynx
论文类型: journal
期刊简称: TIFS
发表年份: 2020
modified: 2025-04-09 09:20:27
---

## Drynx: Decentralized, Secure, Verifiable System for Statistical Queries and Machine Learning on Distributed Datasets

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/document/9019831)

## 作者

+ David Froelicher; 
+ Juan Ramón Troncoso-Pastoriza; 
+ Joao Sa Sousa; 
+ [Jean-Pierre Hubaux](Jean-Pierre%20Hubaux.md)
## 笔记

Data sharing has become of primary importance in many domains such as big-data analytics, economics and medical research, but remains difficult to achieve when the data are sensitive. In fact, sharing personal information requires individuals’ unconditional consent or is often simply forbidden for privacy and security reasons. In this paper, we propose Drynx, a decentralized system for privacy-conscious statistical analysis on distributed datasets. Drynx relies on a set of computing nodes to enable the computation of statistics such as standard deviation or extrema, and the training and evaluation of machine-learning models on sensitive and distributed data. To ensure data confidentiality and the privacy of the data providers, Drynx combines interactive protocols, homomorphic encryption, zero-knowledge proofs of correctness, and differential privacy. It enables an efficient and decentralized verification of the input data and of all the system’s computations thus provides auditability in a strong adversarial model in which no entity has to be individually trusted. Drynx is highly modular, dynamic and parallelizable. Our evaluation shows that it enables the training of a logistic regression model on a dataset (12 features and 600,000 records) distributed among 12 data providers in less than 2 seconds. The computations are distributed among 6 computing nodes, and Drynx enables the verification of the query execution’s correctness in less than 22 seconds.

以下是中文翻译：

数据共享在大数据分析、经济学和医学研究等许多领域已变得至关重要，但当数据具有敏感性时，实现共享仍然困难。事实上，共享个人信息需要个人的无条件同意，或者出于隐私和安全原因往往被直接禁止。在本文中，我们提出了Drynx，这是一个用于对分布式数据集进行隐私保护统计分析的去中心化系统。Drynx依靠一组计算节点，能够计算标准差或极值等统计量，并在敏感的分布式数据上进行机器学习模型的训练和评估。为了确保数据机密性和数据提供者的隐私，Drynx结合了交互式协议(interactive protocols)、同态加密(homomorphic encryption)、正确性零知识证明(zero-knowledge proofs of correctness)和差分隐私(differential privacy)。它能够高效且去中心化地验证输入数据和系统的所有计算，从而在一个强对抗模型中提供可审计性，在该模型中不需要单独信任任何实体。Drynx具有高度模块化、动态性和可并行化的特点。我们的评估表明，它能够在不到2秒的时间内，在由12个数据提供者分布的数据集（12个特征和600,000条记录）上训练逻辑回归模型。计算分布在6个计算节点上，Drynx能够在不到22秒的时间内验证查询执行的正确性。

## 关键词

+ Drynx去中心化隐私统计分析
+ 同态加密分布式数据计算
+ 零知识正确性证明
+ 差分隐私机器学习训练
+ 去中心化可验证查询
+ 多方安全计算审计性