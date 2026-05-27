---
title: "A verifiable and privacy-preserving federated learning training framework"
doi: 10.1109/tdsc.2024.3369658
标题简称:
论文类型: journal
期刊简称: TDSC
发表年份: 2024
modified: 2025-04-27 08:55:20
created: 2025-04-15 16:36:08
---
## A verifiable and privacy-preserving federated learning training framework

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/10444899)

## 作者

+ Haohua Duan 
+ Zedong Peng 
+ Liyao Xiang 
+ [Yuncong Hu](Yuncong%20Hu.md)
+ Bo Li 

## 笔记

Federated learning allows multiple clients to collaboratively train a global model without revealing their private data. Despite its success in many applications, it remains a challenge to prevent malicious clients to corrupt the global model through uploading incorrect model updates. Hence, one critical issue arises in how to validate the training is truly conducted on legitimate neural networks. To address the issue, we propose VPNNT, a zero-knowledge proof scheme for neural network backpropagation. VPNNT enables each client to prove to others that the model updates (gradients) are indeed calculated on the global model of the previous round, without leaking any information about the client's private training data. Our proof scheme is generally applicable to any type of neural network. Different from conventional verification schemes constructing neural network operations by gate-level circuits, we improve verification efficiency by formulating the training process using custom gates — matrix operations, and apply an optimized linear time zero knowledge protocol for verification. Thanks to the recursive structure of neural network backward propagation, common custom gates are combined in verification thereby reducing prover and verifier costs over conventional zero knowledge proofs. Experimental results show that VPNNT is a lightweighted verification scheme for neural network backpropagation with an improved prove time, verification time and proof size.

以下是中文翻译：

联邦学习允许多个客户端在不泄露其私人数据的情况下协作训练一个全球模型。尽管在许多应用中取得了成功，但防止恶意客户端通过上传错误的模型更新来破坏全球模型仍然是一个挑战。因此，如何验证训练确实是在合法神经网络上进行的成为一个关键问题。为了解决这一问题，我们提出了VPNNT，一种用于神经网络反向传播的零知识证明方案（zero-knowledge proof）。VPNNT使每个客户端能够向其他客户端证明模型更新（梯度）确实是在上一轮的全球模型上计算的，而不会泄露任何关于客户端私人训练数据的信息。我们的证明方案适用于任何类型的神经网络。与传统的通过门级电路构建神经网络操作的验证方案不同，我们通过使用自定义门（custom gates）—— 矩阵运算来改进验证效率，并应用优化的线性时间零知识协议进行验证。得益于神经网络反向传播的递归结构，常见的自定义门在验证中被组合，从而降低了证明者和验证者相较于传统零知识证明的成本。实验结果表明，VPNNT是一种轻量级的神经网络反向传播验证方案，具有更短的证明时间、验证时间和证明大小。

## 关键词

+ 联邦学习隐私保护验证
+ 神经网络反向传播零知识证明
+ 自定义门矩阵运算验证
+ 线性时间零知识协议
+ 梯度计算完整性证明
+ 恶意客户端防御机制