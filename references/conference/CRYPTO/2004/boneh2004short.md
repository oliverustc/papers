---
title: "Short group signatures"

标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 2004
created: 2025-05-20 03:12:28
modified: 2025-05-20 03:14:48
---

## Short group signatures

## 发表信息

+ [原文链接]()

## 作者

+ [Dan Boneh](Dan%20Boneh.md)
+ Xavier Boyen
+ [Hovav Shacham](Hovav%20Shacham.md)
## 笔记

We construct a short group signature scheme. Signatures in our scheme are approximately the size of a standard RSA signature with the same security. Security of our group signature is based on the Strong Diffie-Hellman assumption and a new assumption in bilinear groups called the Decision Linear assumption. We prove security of our system, in the random oracle model, using a variant of the security definition for group signatures recently given by Bellare, Micciancio, and Warinschi.

以下是中文翻译：

我们构建了一个简短的群签名方案。我们方案中的签名大小大约与具有相同安全性的标准RSA签名相当。我们的群签名安全性基于强Diffie-Hellman假设（Strong Diffie-Hellman assumption）和双线性群中的一个新假设，称为线性判定假设（Decision Linear assumption）。我们在随机预言模型中，使用Bellare、Micciancio和Warinschi最近提出的群签名安全性定义的变体，证明了我们系统的安全性。

## 关键词

+ 短群签名方案双线性群
+ 强Diffie-Hellman判定线性假设
+ 随机预言机群签名安全证明
+ 可撤销匿名性实用群签名
+ 标准RSA大小签名群签名