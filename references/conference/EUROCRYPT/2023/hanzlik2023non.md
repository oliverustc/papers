---
title: "Non-interactive Blind Signatures for Random Messages"
标题简称:
论文类型: conference
会议简称: EUROCRYPT
发表年份: 2023
modified: 2025-04-16 10:20:33
created: 2025-04-09 11:35:00
---

## Non-interactive Blind Signatures for Random Messages

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-30589-4_25)

## 作者

+ [Lucjan Hanzlik](Lucjan%20Hanzlik.md)

## 笔记

Blind signatures allow a signer to issue signatures on messages chosen by the signature recipient. The main property is that the recipient’s message is hidden from the signer. There are many applications, including Chaum’s e-cash system and Privacy Pass, where no special distribution of the signed message is required, and the message can be random. Interestingly, existing notions do not consider this practical use case separately. In this paper, we show that constraining the recipient’s choice over the message distribution spawns a surprising new primitive that improves the well-established state-of-the-art. We formalize this concept by introducing the notion of non-interactive blind signatures (NIBS). Informally, the signer can create a presignature with a specific recipient in mind, identifiable via a public key. The recipient can use her secret key to finalize it and receive a blind signature on a random message determined by the finalization process. The key idea is that online interaction between the signer and recipient is unnecessary. We show an efficient instantiation of NIBS in the random oracle model from signatures on equivalence classes. The exciting part is that, in this case, for the recipient’s public key, we can use preexisting keys for Schnorr, ECDSA signatures, El-Gamal encryption scheme or even the Diffie-Hellman key exchange. Reusing preexisting public keys allows us to distribute anonymous tokens similarly to cryptocurrency airdropping. Additional contributions include tagged non-interactive blind signatures (TNIBS) and their efficient instantiation. A generic construction in the random oracle or common reference string model based on verifiable random functions, standard signatures, and non-interactive proof systems.

以下是中文翻译：

盲签名允许签名者对由签名接收者选择的消息进行签名。其主要特性是接收者的消息对签名者是隐藏的。盲签名有许多应用，包括Chaum的电子现金系统和Privacy Pass，在这些应用中，不需要对签名消息进行特殊分发，消息可以是随机的。有趣的是，现有的概念并未单独考虑这一实际用例。在本文中，我们展示了限制接收者对消息分布选择的情况会产生一个令人惊讶的新原语，从而改善现有的成熟技术。我们通过引入非交互式盲签名（non-interactive blind signatures）的概念来形式化这一思想。非正式地说，签名者可以针对特定的接收者创建一个预签名，该接收者可以通过公钥识别。接收者可以使用她的私钥来完成签名并获得一个随机消息上的盲签名，该随机消息由最终化过程决定。关键在于签名者和接收者之间的在线交互是多余的。我们展示了在随机预言模型中基于等价类签名的盲签名的高效实例化。令人兴奋的是，在这种情况下，对于接收者的公钥，我们可以使用现有的Schnorr、ECDSA签名、El-Gamal加密方案甚至Diffie-Hellman密钥交换的公钥。重用现有的公钥使我们能够以类似于加密货币空投的方式分发匿名代币。其他贡献包括标记的非交互式盲签名及其高效实例化。在随机预言或公共参考字符串模型中基于可验证随机函数、标准签名和非交互式证明系统的通用构造。

## 关键词

+ 非交互式盲签名
+ 随机消息盲签名
+ 等价类签名
+ 匿名代币空投
+ 预签名机制