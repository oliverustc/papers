---
title: "Threshold BBS signatures for distributed anonymous credential issuance"
标题简称:
论文类型: conference
会议简称: S&P
发表年份: 2023
created: 2025-05-23 01:27:38
modified: 2025-05-23 01:27:44
---

## Threshold BBS signatures for distributed anonymous credential issuance

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/10179470)

## 作者

+ Jack Doerner
+ Yashvanth Kondi
+ Eysa Lee
+ Abhi Shelat
+ LaKyah Tyner

## 笔记

We propose a secure multiparty signing protocol for the BBS+ signature scheme; in other words, an anonymous credential scheme with threshold issuance. We prove that due to the structure of the BBS+ signature, simply verifying the signature produced by an otherwise semi-honest protocol is sufficient to achieve composable security against a malicious adversary. Consequently, our protocol is extremely simple and efficient: it involves a single request from the client (who requires a signature) to the signing parties, two exchanges of messages among the signing parties, and finally a response to the client; in some deployment scenarios the concrete cost bottleneck may be the client's local verification of the signature that it receives. Furthermore, our protocol can be extended to support the strongest form of blind signing and to serve as a distributed evaluation protocol for the Dodis-Yampolskiy Oblivious VRF. We validate our efficiency claims by implementing and benchmarking our protocol.

以下是中文翻译：

我们为BBS+签名方案提出了一种安全的多方签名协议，换言之，这是一种支持阈值签发的匿名凭证方案。我们证明，由于BBS+签名的结构特性，仅需验证由半诚实协议生成的签名，就足以实现针对恶意对手的可组合安全性。因此，我们的协议极其简单且高效：它包括客户端（需要签名者）向签名方发起单次请求、签名方之间两轮消息交换，以及最终向客户端的响应；在某些部署场景中，具体的成本瓶颈可能是客户端对所接收签名的本地验证。此外，我们的协议可以扩展以支持最强形式的盲签名，并可作为Dodis-Yampolskiy隐式VRF的分布式评估协议。我们通过实现和基准测试验证了效率声明。

## 关键词

+ BBS+签名方案
+ 阈值匿名凭证
+ 多方签名协议
+ 盲签名
+ 可组合安全性
+ 分布式VRF