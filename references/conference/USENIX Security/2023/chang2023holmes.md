---
title: "HOLMES: Efficient Distribution Testing for Secure Collaborative Learning"
标题简称:
论文类型: conference
会议简称: USENIX Security
发表年份: 2023
modified: 2025-04-09 10:53:32
---

## HOLMES: Efficient Distribution Testing for Secure Collaborative Learning

## 发表信息

+ [原文链接](https://www.usenix.org/conference/usenixsecurity23/presentation/chang)

## 作者

+ 

## 笔记

Using secure multiparty computation (MPC), organizations which own sensitive data (e.g., in healthcare, finance or law enforcement) can train machine learning models over their joint dataset without revealing their data to each other. At the same time, secure computation restricts operations on the joint dataset, which impedes computation to assess its quality. Without such an assessment, deploying a jointly trained model is potentially illegal. Regulations, such as the European Union's General Data Protection Regulation (GDPR), require organizations to be legally responsible for the errors, bias, or discrimination caused by their machine learning models. Hence, testing data quality emerges as an indispensable step in secure collaborative learning. However, performing distribution testing is prohibitively expensive using current techniques, as shown in our experiments.

We present HOLMES, a protocol for performing distribution testing efficiently. In our experiments, compared with three non-trivial baselines, HOLMES achieves a speedup of more than 10× for classical distribution tests and up to 104× for multidimensional tests. The core of HOLMES is a hybrid protocol that integrates MPC with zero-knowledge proofs and a new ZK-friendly and naturally oblivious sketching algorithm for multidimensional tests, both with significantly lower computational complexity and concrete execution costs.

以下是中文翻译：

通过安全多方计算(secure multiparty computation, MPC)，拥有敏感数据的组织机构(如在医疗、金融或执法领域)可以在不向彼此透露数据的情况下，对其联合数据集进行机器学习模型训练。然而，安全计算限制了对联合数据集的操作，这妨碍了对其质量进行评估的计算。如果缺乏这种评估，部署联合训练的模型可能是非法的。相关法规，如欧盟的《通用数据保护条例》(General Data Protection Regulation, GDPR)要求组织机构对其机器学习模型造成的错误、偏见或歧视承担法律责任。因此，测试数据质量成为安全协作学习中不可或缺的步骤。然而，如我们的实验所示，使用当前技术进行分布测试的成本过于昂贵。

我们提出了HOLMES，这是一个用于高效执行分布测试的协议。在我们的实验中，与三个非平凡的基准相比，HOLMES在经典分布测试中实现了超过10倍的加速，在多维测试中实现了高达104倍的加速。HOLMES的核心是一个混合协议，它将MPC与零知识证明相结合，并引入了一种新的适合零知识证明且天然具有混淆性的多维测试草图算法，这两者都具有显著更低的计算复杂度和具体执行成本。

## 关键词

+ HOLMES分布测试安全学习
+ 安全多方计算MPC数据质量
+ 零知识证明协作学习
+ ZK友好草图算法
+ 多维分布测试优化
+ 隐私保护机器学习
