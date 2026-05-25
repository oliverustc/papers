---
title: "Oblivious message retrieval"
标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 2022
modified: 2025-04-09 12:10:23
---

## Oblivious message retrieval

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-15802-5_26)

## 作者

+ [Zeyu Liu](Zeyu%20Liu.md)
+ [Eran Tromer](Eran%20Tromer.md)

## 笔记

Anonymous message delivery systems, such as private messaging services and privacy-preserving payment systems, need a mechanism for recipients to retrieve the messages addressed to them without leaking metadata or letting their messages be linked. Recipients could download all posted messages and scan for those addressed to them, but communication and computation costs are excessive at scale.

We show how untrusted servers can detect messages on behalf of recipients, and summarize these into a compact encrypted digest that recipients can easily decrypt. These servers operate obliviously and do not learn anything about which messages are addressed to which recipients. Privacy, soundness, and completeness hold even if everyone but the recipient is adversarial and colluding (unlike in prior schemes).

Our starting point is an asymptotically-efficient approach, using Fully Homomorphic Encryption and homomorphically-encoded Sparse Random Linear Codes. We then address the concrete performance using bespoke tailoring of lattice-based cryptographic components, alongside various algebraic and algorithmic optimizations. This reduces the digest size to a few bits per message scanned. Concretely, the servers’ cost is \({\sim }\$1\) per million messages scanned, and the resulting digests can be decoded by recipients in under \({\sim }\)20 ms. Our schemes can thus practically attain the strongest form of receiver privacy for current applications such as privacy-preserving cryptocurrencies.

以下是中文翻译：

匿名消息传递系统，如私人消息服务和隐私保护支付系统，需要一种机制使接收者能够检索发送给他们的消息，同时不泄露元数据或让消息之间产生关联。接收者可以下载所有已发布的消息并扫描寻找发送给他们的消息，但在大规模应用中，通信和计算成本过高。

我们展示了不受信任的服务器如何代表接收者检测消息，并将这些消息汇总成一个接收者可以轻松解密的紧凑加密摘要。这些服务器以隐匿方式运行，不会获知哪些消息是发送给哪些接收者的。即使除接收者之外的所有人都是对抗性的且相互勾结（这与之前的方案不同），隐私性、可靠性和完整性仍然得以保持。

我们的起点是一种渐近高效的方法，使用全同态加密(Fully Homomorphic Encryption)和同态编码的稀疏随机线性码(Sparse Random Linear Codes)。然后，我们通过定制基于格密码学组件，以及各种代数和算法优化来解决具体性能问题。这将摘要大小减少到每条扫描消息仅需几比特。具体而言，服务器扫描每百万条消息的成本约为1美元，接收者可以在约20毫秒内解码生成的摘要。因此，我们的方案可以为当前的应用（如隐私保护加密货币）实现最强形式的接收者隐私保护。

## 关键词

+ 密码学
+ 零知识
+ 协议