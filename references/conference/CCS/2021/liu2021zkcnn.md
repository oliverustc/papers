---
title: "zkCNN: Zero Knowledge Proofs for Convolutional Neural Network Predictions and Accuracy"
标题简称: zkCNN
论文类型: conference
会议简称: CCS
发表年份: 2021
modified: 2025-04-08 09:59:55
---

## zkCNN: Zero Knowledge Proofs for Convolutional Neural Network Predictions and Accuracy

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3460120.3485379)
+ [code](https://github.com/TAMUCrypto/zkCNN)
+ 

## 作者

+ [Tianyi Liu](Tianyi%20Liu.md)
+ [Xiang Xie](Xiang%20Xie.md)
+ [Yupeng Zhang](Yupeng%20Zhang.md)

## 笔记

Deep learning techniques with neural networks are developing prominently in recent years and have been deployed in numerous applications. Despite their great success, in many scenarios it is important for the users to validate that the inferences are truly computed by legitimate neural networks with high accuracy, which is referred to as the integrity of machine learning predictions. To address this issue, in this paper, we propose zkCNN, a zero knowledge proof scheme for convolutional neural networks (CNN). The scheme allows the owner of the CNN model to prove to others that the prediction of a data sample is indeed calculated by the model, without leaking any information about the model itself. Our scheme can also be generalized to prove the accuracy of a secret CNN model on a public dataset.
Underlying zkCNN is a new sumcheck protocol for proving fast Fourier transforms and convolutions with a linear prover time, which is even faster than computing the result asymptotically. We also introduce several improvements and generalizations on the interactive proofs for CNN predictions, including verifying the convolutional layer, the activation function of ReLU and the max pooling. Our scheme is highly efficient in practice. It can support the large CNN of VGG16 with 15 million parameters and 16 layers. It only takes 88.3 seconds to generate the proof, which is 1264× faster than existing schemes. The proof size is 341 kilobytes, and the verifier time is only 59.3 milliseconds. Our scheme can further scale to prove the accuracy of the same CNN on 20 images.

以下是中文翻译：

近年来，基于神经网络的深度学习技术发展迅速，并已在众多应用中得到部署。尽管取得了巨大成功，但在许多场景中，用户需要验证推理结果确实是由具有高准确率的合法神经网络计算得出的，这被称为机器学习预测的完整性。为解决这个问题，本文提出了zkCNN，一种用于卷积神经网络(Convolutional Neural Networks, CNN)的零知识证明方案。该方案允许CNN模型的所有者向他人证明数据样本的预测确实是由该模型计算得出的，同时不泄露关于模型本身的任何信息。我们的方案还可以推广到证明秘密CNN模型在公开数据集上的准确率。

zkCNN的基础是一个新的求和检查协议(sumcheck protocol)，用于证明快速傅里叶变换和卷积运算，具有线性证明者时间复杂度，在渐近意义上甚至比计算结果更快。我们还对CNN预测的交互式证明引入了几项改进和推广，包括验证卷积层、ReLU激活函数和最大池化操作。我们的方案在实践中具有很高的效率。它可以支持具有1500万个参数和16层的大型CNN网络VGG16。生成证明仅需88.3秒，比现有方案快1264倍。证明大小为341千字节，验证者时间仅为59.3毫秒。我们的方案还可以进一步扩展到证明同一CNN在20张图像上的准确率。

## 关键词

+ 零知识证明
+ 卷积神经网络
+ 机器学习
+ 求和检查协议
+ 隐私保护