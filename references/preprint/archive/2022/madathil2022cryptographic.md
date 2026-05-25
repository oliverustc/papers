---
title: "Cryptographic oracle-based conditional payments"
标题简称:
论文类型: preprint
预印本简称: archive
发表年份: 2022
created: 2025-04-29 10:49:13
modified: 2025-04-29 10:50:01
---

## Cryptographic oracle-based conditional payments

## 发表信息

+ [原文链接](https://www.ndss-symposium.org/ndss-paper/cryptographic-oracle-based-conditional-payments/)

## 作者

+ Varun Madathil 
+ Sri AravindaKrishnan Thyagarajan 
+ Dimitrios Vasilopoulos 
+ Lloyd Fournier 
+ [Giulio Malavolta](Giulio%20Malavolta.md)
+ Pedro Moreno-Sanchez 

## 笔记

We consider a scenario where two mutually distrustful parties, Alice and Bob, want to perform a payment conditioned on the outcome of some real-world event. A semi-trusted oracle (or a threshold number of oracles, in a distributed trust setting) is entrusted to attest that such an outcome indeed occurred, and only then the payment is successfully made. Such oracle-based conditional (ObC) payments are ubiquitous in many real-world applications, like financial adjudication, pre-scheduled payments or trading, and are a necessary building block to introduce information about real-world events into blockchains. In this work we show how to realize ObC payments with provable security guarantees and efficient instantiations. To do this, we propose a new cryptographic primitive that we call verifiable witness encryption based on threshold signatures (VweTS): Users can encrypt signatures on payments that can be decrypted if a threshold number of signers (e.g., oracles) sign another message (e.g., the description of an event outcome). We require two security notions: (1) one-wayness that guarantees that without the threshold number of signatures, the ciphertext hides the encrypted signature, and (2) verifiability, that guarantees that a ciphertext that correctly verifies can be successfully decrypted to reveal the underlying signature. We present provably secure and efficient instantiations of VweTS where the encrypted signature can be some of the widely used schemes like Schnorr, ECDSA or BLS signatures. Our main technical innovation is a new batching technique for cut-and- choose, inspired by the work of Lindell-Riva on garbled circuits. Our VweTS instantiations can be readily used to realize ObC payments on virtually all cryptocurrencies of today in a fungible, cost-efficient, and scalable manner. The resulting ObC payments are the first to support distributed trust (i.e., multiple oracles) without requiring any form of synchrony or coordination among the users and the oracles. To demonstrate the practicality of our scheme, we present a prototype implementation and our benchmarks in commodity hardware show that the computation overhead is less than 25 seconds even for a threshold of 4-of-7 and a payment conditioned on 1024 different real-world event outcomes, while the communication overhead is below 2.3 MB.

以下是中文翻译：

我们考虑这样一个场景：两个互不信任的参与方，Alice和Bob，希望基于某个现实世界事件的结果进行支付。一个半可信的预言机（或在分布式信任设置中的多个预言机中的阈值数量）被委托来证实该结果确实发生，只有在这种情况下支付才能成功完成。这种基于预言机的条件支付（Oracle-based Conditional payment，ObC）在许多现实应用中普遍存在，如金融裁决、预定支付或交易，并且是将现实世界事件信息引入区块链的必要构建模块。

在本研究中，我们展示了如何实现具有可证明安全保障和高效实例化的ObC支付。为此，我们提出了一个新的密码学原语，称为基于阈值签名的可验证见证加密（Verifiable Witness Encryption based on Threshold Signatures，VweTS）：用户可以加密支付签名，只有当阈值数量的签名者（如预言机）签署另一条消息（如事件结果描述）时才能解密。我们需要两个安全性概念：(1)单向性，保证在没有达到阈值数量签名的情况下，密文能隐藏加密的签名；(2)可验证性，保证正确验证的密文可以成功解密以显示底层签名。

我们提出了VweTS的可证明安全且高效的实例化方案，其中加密的签名可以是当前广泛使用的方案，如Schnorr、ECDSA或BLS签名。我们的主要技术创新是一种新的批处理剪切选择技术，这受到Lindell-Riva关于混淆电路工作的启发。我们的VweTS实例化可以直接用于在当今几乎所有加密货币上实现ObC支付，具有可替代性、成本效益和可扩展性。由此产生的ObC支付是首个支持分布式信任（即多个预言机）而无需用户和预言机之间进行任何形式同步或协调的方案。

为了证明我们方案的实用性，我们提供了原型实现，在普通硬件上的基准测试表明，即使在4-of-7的阈值设置下，对1024个不同现实世界事件结果的条件支付，计算开销也少于25秒，而通信开销低于2.3 MB。

## 关键词

+ 基于预言机条件支付区块链
+ VweTS阈值签名可验证见证加密
+ 分布式信任ObC支付协议
+ 剪切选择批处理技术
+ Schnorr ECDSA BLS签名条件支付