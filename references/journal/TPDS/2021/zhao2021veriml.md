---
title: "VeriML: Enabling Integrity Assurances and Fair Payments for Machine Learning as a Service"
doi: 10.1109/tpds.2021.3068195
标题简称:
论文类型: journal
期刊简称: TPDS
发表年份: 2021
modified: 2025-04-09 09:38:25
---
## VeriML: Enabling Integrity Assurances and Fair Payments for Machine Learning as a Service

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/9384314)

## 作者

+ Lingchen Zhao; 
+ Qian Wang; 
+ Cong Wang; 
+ Qi Li; 
+ Chao Shen; 
+ Bo Feng

## 笔记

Machine Learning as a Service (MLaaS) allows clients with limited resources to outsource their expensive ML tasks to powerful servers. Despite the huge benefits, current MLaaS solutions still lack strong assurances on: 1) service correctness (i.e., whether the MLaaS works as expected); 2) trustworthy accounting (i.e., whether the bill for the MLaaS resource consumption is correctly accounted); 3) fair payment (i.e., whether a client gets the entire MLaaS result before making the payment). Without these assurances, unfaithful service providers can return improperly-executed ML task results or partially-trained ML models while asking for over-claimed rewards. Moreover, it is hard to argue for wide adoption of MLaaS to both the client and the service provider, especially in the open market without a trusted third party. In this article, we present VeriML, a novel and efficient framework to bring integrity assurances and fair payments to MLaaS. With VeriML, clients can be assured that ML tasks are correctly executed on an untrusted server, and the resource consumption claimed by the service provider equals to the actual workload. We strategically use succinct non-interactive arguments of knowledge (SNARK) on randomly-selected iterations during the ML training phase for efficiency with tunable probabilistic assurance. We also develop multiple ML-specific optimizations to the arithmetic circuit required by SNARK. Our system implements six common algorithms: linear regression, logistic regression, neural network, support vector machine, K-means and decision tree. The experimental results have validated the practical performance of VeriML.

以下是中文翻译：

机器学习即服务(Machine Learning as a Service, MLaaS)使资源有限的客户能够将其昂贵的机器学习任务外包给强大的服务器。尽管带来巨大益处，当前的MLaaS解决方案仍缺乏以下几个方面的有力保障：1) 服务正确性（即MLaaS是否按预期工作）；2) 可信计费（即MLaaS资源消耗的账单是否正确计算）；3) 公平支付（即客户在付款前是否获得完整的MLaaS结果）。没有这些保障，不诚信的服务提供商可能会返回执行不当的机器学习任务结果或部分训练的机器学习模型，同时要求过高的报酬。此外，在没有可信第三方的开放市场中，很难说服客户和服务提供商广泛采用MLaaS。

在本文中，我们提出了VeriML，这是一个新颖且高效的框架，为MLaaS带来完整性保证和公平支付。通过VeriML，客户可以确信机器学习任务在不可信服务器上得到正确执行，且服务提供商声称的资源消耗等于实际工作负载。为了在可调节的概率保证下实现效率，我们战略性地在机器学习训练阶段对随机选择的迭代使用简洁非交互式知识论证(Succinct Non-interactive Arguments of Knowledge, SNARK)。我们还为SNARK所需的算术电路开发了多个机器学习特定的优化方案。我们的系统实现了六种常见算法：线性回归(linear regression)、逻辑回归(logistic regression)、神经网络(neural network)、支持向量机(support vector machine)、K均值(K-means)和决策树(decision tree)。实验结果验证了VeriML的实用性能。

## 关键词

+ VeriML机器学习即服务完整性保证
+ SNARK随机迭代抽样验证
+ 机器学习公平支付协议
+ 可验证计算外包资源消耗
+ 算术电路ML特定优化
+ 概率保证可调节验证方案