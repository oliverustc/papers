---
title: "Threshold cryptosystems"
标题简称:
论文类型: conference
会议简称: EUROCRYPT
发表年份: 1992
created: 2025-05-27 11:15:01
modified: 2025-05-27 11:15:37
---

## Threshold cryptosystems

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/3-540-57220-1_47)

## 作者

+ Yvo Desmedt

## 笔记

Often the power to use a cryptosystem has to be shared. In threshold schemes, _t_-out-of-_l_ have the power to regenerate a secret key (while less than _t_ have not). However threshold schemes cannot be used directly in many applications, such as threshold signatures in which _t_-out-of-_l_ have to co-sign a message. A normal threshold scheme would require the shareholders to send their shares to a trusted person who would sign for them. But the use of such a trusted person violates the main point of threshold signatures!

We first overview the research in the field and then discuss a threshold decryption/signature scheme which is as secure as RSA. We conclude by giving a list of open problems.

以下是中文翻译：

通常，使用加密系统的权限需要共享。在阈值方案中，t-out-of-l的参与者有权重新生成一个秘密密钥（而少于t的参与者则没有此权利）。然而，阈值方案在许多应用中无法直接使用，例如在阈值签名中，t-out-of-l的参与者必须共同签署一条消息。一个普通的阈值方案要求持有者将他们的份额发送给一个可信的人，由该人代为签署。但是，使用这样的可信人违反了阈值签名的主要意义！

我们首先概述该领域的研究，然后讨论一种与RSA同样安全的阈值解密/签名方案。最后，我们列出了一些未解决的问题。

## 关键词

+ 阈值密码系统
+ 阈值签名
+ 秘密共享
+ RSA
+ 分布式密码学