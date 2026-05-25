---
title: "Non-interactive Anonymous Tokens with Private Metadata Bit"
标题简称:
论文类型: preprint
预印本简称: archive
发表年份: 2025
created: 2025-05-09 14:27:36
modified: 2025-05-09 14:29:15
---

## Non-interactive Anonymous Tokens with Private Metadata Bit

## 发表信息

+ [原文链接](https://eprint.iacr.org/2025/430)

## 作者

+ [Foteini Baldimtsi](Foteini%20Baldimtsi.md)
+ [Lucjan Hanzlik](Lucjan%20Hanzlik.md)
+ Quan Nguyen
+ Aayush Yadav

## 笔记

Anonymous tokens with private metadata bit (ATPM) have received increased interest as a method for anonymous client authentication while also embedding trust signals that are only readable by the authority who holds the issuance secret key and nobody else. A drawback of all existing ATPM constructions is that they require client-issuer interaction during the issuance process. In this work, we build the first non-interactive anonymous tokens (NIAT) with private metadata bit, inspired by the recent work of Hanzlik (Eurocrypt '23) on non-interactive blind signatures.

[Non-interactive Blind Signatures for Random Messages (**EUROCRYPT 2023**)](hanzlik2023non)

We discuss how the non-interaction property during the issuance process allows for more efficient issuance protocols that avoid the need for online signing. We construct an efficient NIAT scheme based on Structure-preserving Signatures on Equivalence Classes (SPS-EQ) and experimentally evaluate its performance. We also present an extension to our NIAT construction that allows the identification of clients who attempt to double-spend (i.e., present the same token twice).

以下是中文翻译：

具有私有元数据位的匿名令牌(Anonymous tokens with private metadata bit, ATPM)作为一种匿名客户端认证方法受到越来越多的关注，该方法能够嵌入信任信号，这些信号只能被持有发行密钥的权威机构读取，其他任何人都无法读取。现有所有ATPM构造的一个缺点是在发行过程中需要客户端与发行方进行交互。在本研究中，我们受到Hanzlik（Eurocrypt '23）关于非交互式盲签名最新研究的启发，构建了首个具有私有元数据位的非交互式匿名令牌(Non-interactive anonymous tokens, NIAT)。我们讨论了发行过程中的非交互特性如何实现更高效的发行协议，从而避免了在线签名的需求。我们基于等价类结构保持签名(Structure-preserving Signatures on Equivalence Classes, SPS-EQ)构建了一个高效的NIAT方案，并对其性能进行了实验评估。我们还提出了NIAT构造的一个扩展，该扩展允许识别试图重复使用（即两次出示相同令牌）的客户端。

## 关键词

+ 非交互式匿名令牌私有元数据位
+ NIAT非交互盲签名认证
+ SPS-EQ等价类结构保持签名
+ 匿名客户端认证信任信号
+ 双重使用检测匿名令牌扩展