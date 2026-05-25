---
title: "McFly: verifiable encryption to the future made practical"
标题简称:
论文类型: conference
会议简称: FC
发表年份: 2023
created: 2025-04-29 10:45:55
modified: 2025-04-29 10:49:13
---

## McFly: verifiable encryption to the future made practical

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-47754-6_15)

## 作者

+ [Nico Döttling](Nico%20D%C3%B6ttling.md)
+ [Lucjan Hanzlik](Lucjan%20Hanzlik.md) 
+ Bernardo Magri 
+ Stella Wohnig 

## 笔记

Blockchain protocols have revolutionized how individuals and devices interact and transact over the internet. More recently, a trend has emerged to harness blockchain technology as a catalyst to enable advanced security features in distributed applications, in particular fairness. However, the tools employed to achieve these security features are either resource wasteful (e.g., time-lock primitives) or only efficient in theory (e.g., witness encryption). We present McFly, a protocol that allows one to efficiently “encrypt a message to the future” such that the receiver can efficiently decrypt the message at the right time. At the heart of the McFly protocol lies a novel primitive that we call signature-based witness encryption (SWE). In a nutshell, SWE allows to encrypt a plaintext with respect to a tag and a set of signature verification keys. Once a threshold multi-signature of this tag under a sufficient number of these verification keys is released, this signature can be used to efficiently decrypt an SWE ciphertext for this tag. We design and implement a practically efficient SWE scheme in the asymmetric bilinear setting. The McFly protocol, which is obtained by combining our SWE scheme with a BFT blockchain (or a blockchain finality layer) enjoys a number of advantages over alternative approaches: There is a very small computational overhead for all involved parties, the users of McFly do not need to actively maintain the blockchain, are neither required to communicate with the committees, nor are they required to post on the blockchain. To demonstrate the practicality of the McFly protocol, we implemented our SWE scheme and evaluated it on a standard laptop with Intel i7 @2,3 GHz.

以下是中文翻译：

区块链协议彻底改变了个人和设备在互联网上进行交互和交易的方式。最近，一种利用区块链技术作为催化剂来实现分布式应用中高级安全特性（特别是公平性）的趋势已经出现。然而，用于实现这些安全特性的工具要么资源浪费（例如时间锁定原语），要么仅在理论上高效（例如见证加密）。我们提出了McFly协议，该协议允许人们高效地"将消息加密到未来"，使接收者能够在适当的时间高效地解密消息。McFly协议的核心是一种我们称之为基于签名的见证加密（signature-based witness encryption，SWE）的新型原语。简而言之，SWE允许针对标签和一组签名验证密钥对明文进行加密。一旦在足够数量的这些验证密钥下发布了该标签的阈值多重签名，这个签名就可以用来高效地解密该标签的SWE密文。我们在非对称双线性设置中设计并实现了一个实用高效的SWE方案。McFly协议通过将我们的SWE方案与BFT区块链（或区块链最终性层）相结合而得到，相比其他方法具有多个优势：所有参与方的计算开销都很小，McFly的用户不需要主动维护区块链，既不需要与委员会通信，也不需要在区块链上发布信息。为了证明McFly协议的实用性，我们实现了我们的SWE方案，并在配备Intel i7 @2.3 GHz的标准笔记本电脑上进行了评估。

## 关键词

+ 未来加密
+ 基于签名的见证加密
+ 阈值多重签名
+ 区块链公平性
+ BFT区块链
+ 时间锁原语