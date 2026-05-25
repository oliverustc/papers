---
title: "Zero-Knowledge Middleboxes"
标题简称:
论文类型: conference
会议简称: USENIX Security
发表年份: 2022
modified: 2025-04-13 17:50:45
---

## Zero-Knowledge Middleboxes

## 发表信息

+ [原文链接](https://www.usenix.org/conference/usenixsecurity22/presentation/grubbs)

## 作者

+ [Paul Grubbs](Paul%20Grubbs.md)
+ [Arasu Arun](Arasu%20Arun.md)
+ [Ye Zhang](Ye%20Zhang.md)
+ [[Joseph Bonneau]] 
+ [Michael Walfish](Michael%20Walfish.md)
## 笔记

This paper initiates research on zero-knowledge middleboxes (ZKMBs). A ZKMB is a network middlebox that enforces network usage policies on encrypted traffic. Clients send the middlebox zero-knowledge proofs that their traffic is policy-compliant; these proofs reveal nothing about the client's communication except that it complies with the policy. We show how to make ZKMBs work with unmodified encrypted-communication protocols (specifically TLS 1.3), making ZKMBs invisible to servers. As a contribution of independent interest, we design optimized zero-knowledge proofs for TLS 1.3 session keys.  

We apply the ZKMB paradigm to several case studies. Experimental results suggest that in certain settings, performance is in striking distance of practicality; an example is a middlebox that filters domain queries (each query requiring a separate proof) when the client has a long-lived TLS connection with a DNS resolver. In such configurations, the middlebox's overhead is 2–5 ms of running time per proof, and client latency to create a proof is several seconds. On the other hand, clients may have to store hundreds of MBs depending on the underlying zero-knowledge proof machinery, and for some applications, latency is tens of seconds.  

以下是中文翻译：

本文开创性地研究了零知识中间盒（ZKMBs）技术。ZKMB是一种网络中间设备，能够在加密流量上执行网络使用策略。客户端向中间盒发送零知识证明，证实其流量符合策略要求；这些证明仅揭示通信符合策略，而不会泄露任何关于客户通信内容的信息。我们展示了如何使ZKMB与未经修改的加密通信协议（特别是TLS 1.3）协同工作，从而让服务器感知不到ZKMB的存在。作为一项具有独立价值的贡献，我们为TLS 1.3会话密钥设计了优化的零知识证明方案。

我们将ZKMB范式应用于多个案例研究。实验结果表明，在特定配置下，其性能已接近实用水平；例如，当客户端与DNS解析器保持长期TLS连接时，用于过滤域名查询（每个查询需独立生成证明）的中间件，其处理每个证明的运行时间开销仅为2-5毫秒，而客户端生成证明的延迟为数秒。然而，根据所采用的零知识证明机制不同，客户端可能需要存储数百MB数据，且部分应用场景下延迟可达数十秒。

## 关键词

+ 零知识中间盒ZKMB
+ TLS 1.3加密流量策略
+ 网络访问控制ZK证明
+ 零知识DNS过滤
+ 加密通信合规验证
+ 网络安全隐私保护
