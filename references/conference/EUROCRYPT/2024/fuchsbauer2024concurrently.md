---
title: "Concurrently secure blind schnorr signatures"
标题简称:
论文类型: conference
会议简称: EUROCRYPT
发表年份: 2024
---

## Concurrently secure blind schnorr signatures

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-58723-8_5)

## 作者

+ [Georg Fuchsbauer](Georg%20Fuchsbauer.md)
+ Mathias Wolf 


## 笔记

Many applications of blind signatures, e.g. in blockchains, require compatibility of the resulting signatures with the existing system. This makes blind issuing of Schnorr signatures (now being standardized and supported by major cryptocurrencies) desirable. Concurrent security of the signing protocol is required to thwart denial-of-service attacks.

We present a concurrently secure blind-signing protocol for Schnorr signatures, using the standard primitives NIZK and PKE and assuming that Schnorr signatures themselves are unforgeable. Our protocol is the first to be compatible with standard Schnorr implementations over 256-bit elliptic curves. We cast our scheme as a generalization of blind and partially blind signatures: we introduce the notion of _predicate blind signatures_, in which the signer can define a predicate that the blindly signed message must satisfy.

We provide implementations and benchmarks for various choices of primitives and scenarios, such as blindly signing Bitcoin transactions only when they meet certain conditions specified by the signer.

以下是中文翻译：

盲签名的许多应用（例如在区块链中）要求所生成的签名与现有系统兼容。这使得对Schnorr签名（目前正在被标准化，并已被主要加密货币所支持）进行盲签发成为一项重要需求。为了防御拒绝服务攻击，签名协议的并发安全性是必要的。

我们提出了一个针对Schnorr签名的并发安全盲签名协议，该协议使用标准原语NIZK（非交互式零知识证明）和PKE（公钥加密），并在Schnorr签名本身不可伪造的假设下构建。我们的协议是第一个与256位椭圆曲线上标准Schnorr实现兼容的协议。我们将我们的方案表述为盲签名和部分盲签名的推广：我们引入了谓词盲签名（predicate blind signatures）的概念，其中签名者可以定义盲签名消息必须满足的谓词。

我们为各种原语选择和应用场景提供了实现和基准测试，例如仅在满足签名者指定的特定条件时才对比特币交易进行盲签名。

## 关键词

+ 并发安全盲签名
+ Schnorr盲签名
+ 谓词盲签名
+ 非交互式零知识证明
+ 拒绝服务攻击防御