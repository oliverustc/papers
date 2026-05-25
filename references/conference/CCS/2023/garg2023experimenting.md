---
title: "Experimenting with Zero-Knowledge Proofs of Training"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2023

modified: 2025-05-07 22:29:10
created: 2025-04-07 16:28:24
---

## Experimenting with Zero-Knowledge Proofs of Training

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3576915.3623202)

## 作者

+ [Sanjam Garg](Sanjam%20Garg.md)
+ [Aarushi Goel](Aarushi%20Goel.md)
+ Somesh Jha
+ Saeed Mahloujifar
+ Mohammad Mahmoody
+ [Guru-Vamsi Policharla](Guru-Vamsi%20Policharla.md)
+ [Mingyuan Wang](Mingyuan%20Wang.md)

## 笔记

How can a model owner prove they trained their model according to the correct specification? More importantly, how can they do so while preserving the privacy of the underlying dataset and the final model? We study this problem and formulate the notion of zero-knowledge proof of training (zkPoT), which formalizes rigorous security guarantees that should be achieved by a privacy-preserving proof of training. While it is theoretically possible to design zkPoT for any model using generic zero-knowledge proof systems, this approach results in extremely unpractical proof generation times. Towards designing a practical solution, we propose the idea of combining techniques from MPC-in-the-head and zkSNARKs literature to strike an appropriate trade-off between proof size and proof computation time. We instantiate this idea and propose a concretely efficient, novel zkPoT protocol for logistic regression.
Crucially, our protocol is streaming-friendly and does not require RAM proportional to the size of the training circuit, hence, can be done without special hardware. We expect the techniques developed in this paper to also generally be useful for designing efficient zkPoT protocols for other, more sophisticated, ML models.
We implemented and benchmarked prover/verifier running times and proof sizes for training a logistic regression model using mini-batch gradient descent on a 4~GB dataset of 262,144 records with 1024 features. We divide our protocol into three phases: (1) data-independent offline phase (2) data-dependent phase that is independent of the model (3) online phase that depends both on the data and the model. The total proof size (across all three phases) is less than 10% of the data set size (<350 MB). In the online phase, the prover and verifier times are under 10 minutes and half a minute respectively, whereas in the data-dependent phase, they are close to one hour and a few seconds respectively.

以下是中文翻译：

模型所有者如何证明他们按照正确的规范训练了他们的模型？更重要的是，他们如何在保护底层数据集和最终模型隐私的同时做到这一点？我们研究了这个问题，并提出了训练零知识证明(zero-knowledge proof of training, zkPoT)的概念，该概念形式化了隐私保护训练证明应该实现的严格安全保证。虽然理论上可以使用通用零知识证明系统为任何模型设计zkPoT，但这种方法会导致极其不实用的证明生成时间。为了设计一个实用的解决方案，我们提出了结合MPC-in-the-head和zkSNARKs文献中的技术的想法，以在证明大小和证明计算时间之间取得适当的平衡。我们实现了这个想法，并为逻辑回归提出了一个具体高效的新型zkPoT协议。

至关重要的是，我们的协议支持流式处理，不需要与训练电路大小成比例的RAM，因此可以在没有特殊硬件的情况下完成。我们预期本文开发的技术对于设计其他更复杂的机器学习模型的高效zkPoT协议也具有普遍的实用价值。

我们实现并对使用小批量梯度下降在一个4GB数据集（包含262,144条记录和1024个特征）上训练逻辑回归模型的证明者/验证者运行时间和证明大小进行了基准测试。我们将协议分为三个阶段：(1)与数据无关的离线阶段 (2)与模型无关但依赖于数据的阶段 (3)同时依赖于数据和模型的在线阶段。所有三个阶段的总证明大小小于数据集大小的10%（<350 MB）。在在线阶段，证明者和验证者的时间分别在10分钟和半分钟以内，而在依赖数据的阶段，这些时间分别接近一小时和几秒钟。

## 关键词

+ 零知识证明
+ 机器学习
+ 模型训练
+ 隐私保护
+ 数据隐私