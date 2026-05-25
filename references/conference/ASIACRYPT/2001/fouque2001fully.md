---
title: "Fully distributed threshold RSA under standard assumptions"
标题简称:
论文类型: conference
会议简称: ASIACRYPT
发表年份: 2001
created: 2025-05-27 11:56:02
modified: 2025-05-27 11:56:08
---

## Fully distributed threshold RSA under standard assumptions

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/3-540-45682-1_19)

## 作者

+ Pierre-Alain Fouque
+ Jacques Stern

## 笔记

The aim of this article is to propose a _fully distributed_ environment for the RSA scheme. What we have in mind is highly sensitive applications and even if we are ready to pay a price in terms of efficiency, we do not want any compromise of the security assumptions that we make. Recently Shoup proposed a practical RSA threshold signature scheme that allows to share the ability to sign between a set of players. This scheme can be used for decryption as well. However, Shoup’s protocol assumes a trusted dealer to generate and distribute the keys. This comes from the fact that the scheme needs a special assumption on the RSA modulus and this kind of RSA moduli cannot be easily generated in an efficient way with many players. Of course, it is still possible to call theoretical results on multiparty computation, but we cannot hope to design efficient protocols. The only practical result to generate RSA moduli in a distributive manner is Boneh and Franklin’s protocol but it seems difficult to modify it in order to generate the kind of RSA moduli that Shoup’s protocol requires.

The present work takes a diffierent path by proposing a method to enhance the key generation with some additional properties and revisits Shoup’s protocol to work with the resulting RSA moduli. Both of these enhancements decrease the performance of the basic protocols. However, we think that in the applications we target, these enhancements provide practical solutions. Indeed, the key generation protocol is usually run only once and the number of players used to sign or decrypt is not very large. Moreover, these players have time to perform their task so that the communication or time complexity are not overly important.

以下是中文翻译：

本文的目的是提出一个完全分布式的RSA方案环境。我们所考虑的是高度敏感的应用，即使我们愿意在效率方面付出代价，也不希望对我们所做的安全假设进行任何妥协。最近，Shoup提出了一种实用的RSA阈值签名方案，该方案允许在一组参与者之间共享签名能力。该方案也可以用于解密。然而，Shoup的协议假设存在一个可信的经销商来生成和分发密钥。这是因为该方案需要对RSA模数的特殊假设，而这种类型的RSA模数在许多参与者的情况下无法高效生成。当然，仍然可以调用多方计算的理论结果，但我们无法指望设计出高效的协议。以分布方式生成RSA模数的唯一实用结果是Boneh和Franklin的协议，但似乎很难对其进行修改，以生成Shoup协议所需的那种RSA模数。

本研究采取不同的路径，提出了一种增强密钥生成的方法，具有一些附加属性，并重新审视Shoup的协议，以便与生成的RSA模数配合使用。这两项增强措施降低了基本协议的性能。然而，我们认为在我们所针对的应用中，这些增强措施提供了实用的解决方案。实际上，密钥生成协议通常只运行一次，而用于签名或解密的参与者数量并不多。此外，这些参与者有时间执行他们的任务，因此通信或时间复杂度并不是特别重要。

## 关键词

+ 门限RSA
+ 分布式密钥生成
+ 阈值签名
+ 安全多方计算
+ 无可信经销商