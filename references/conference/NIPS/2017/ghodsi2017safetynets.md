---
title: "SafetyNets: Verifiable Execution of Deep Neural Networks on an Untrusted Cloud"
标题简称: SafetyNets
论文类型: conference
会议简称: NIPS
发表年份: 2017
modified: 2025-04-09 09:19:49
---

## SafetyNets: Verifiable Execution of Deep Neural Networks on an Untrusted Cloud

## 发表信息

+ [原文链接](https://proceedings.neurips.cc/paper/2017/hash/6048ff4e8cb07aa60b6777b6f7384d52-Abstract.html)

## 作者

+ Zahra Ghodsi
+ Tianyu Gu
+ Siddharth Garg

## 笔记

Inference using deep neural networks is often outsourced to the cloud since it is a computationally demanding task.  However, this raises a fundamental issue of trust. How can a client be sure that the cloud has performed inference correctly? A lazy cloud provider might use a simpler but less accurate model to reduce its own computational load, or worse, maliciously modify the inference results sent to the client. We propose SafetyNets, a framework that enables an untrusted server (the cloud) to provide a client with a short mathematical proof of the correctness of inference tasks that they perform on behalf of the client. Specifically, SafetyNets develops and implements a specialized interactive proof (IP) protocol for verifiable execution of a class of deep neural networks, i.e., those that can be represented as arithmetic circuits. Our empirical results on three- and four-layer deep neural networks demonstrate the run-time costs of SafetyNets for both the client and server are low. SafetyNets detects any incorrect computations of the neural network by the untrusted server with high probability, while achieving state-of-the-art accuracy on the MNIST digit recognition (99.4%) and TIMIT speech recognition tasks (75.22%).

以下是中文翻译：

深度神经网络的推断通常被外包给云端，因为这是一项计算密集型任务。然而，这引发了一个根本性的信任问题。客户如何能够确保云端正确地执行了推断？一个懒惰的云服务提供商可能会使用一个更简单但准确性较低的模型，以减少自身的计算负担，或者更糟糕的是，恶意修改发送给客户的推断结果。我们提出了SafetyNets，一个框架，使不可信的服务器（云端）能够为客户提供推断任务正确性的简短数学证明，这些任务是其代表客户执行的。具体而言，SafetyNets开发并实现了一种专门的交互式证明（IP）协议，用于可验证执行一类深度神经网络，即那些可以表示为算术电路的网络。我们在三层和四层深度神经网络上的实证结果表明，SafetyNets对客户和服务器的运行时间成本均较低。SafetyNets以高概率检测不可信服务器对神经网络的任何错误计算，同时在MNIST数字识别（99.4%）和TIMIT语音识别任务（75.22%）上实现了最先进的准确率。

## 关键词

+ 深度神经网络可验证推断
+ 交互式证明协议
+ 算术电路
+ 不可信云计算
+ ZK-SNARK应用
+ 机器学习安全性