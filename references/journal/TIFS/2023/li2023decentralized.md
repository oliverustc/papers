---
title: "Decentralized threshold signatures with dynamically private accountability"
标题简称:
论文类型: journal
期刊简称: TIFS
发表年份: 2023
created: 2025-05-27 05:09:47
modified: 2025-05-27 05:10:21
---

## Decentralized threshold signatures with dynamically private accountability

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/10375550)

## 作者

+ Meng Li
+ Hanni Ding
+ Qing Wang
+ Mingwei Zhang
+ Weizhi Meng
+ [Liehuang Zhu](Liehuang%20Zhu.md)
+ Zijian Zhang
+ Xiaodong Lin

## 笔记

Threshold signature is a fundamental cryptographic primitive used in many practical applications. As proposed by Boneh and Komlo (CRYPTO’22), TAPS is a threshold signature that is a hybrid of privacy and accountability. It enables a combiner to combine t signature shares while revealing nothing about the threshold t or signing quorum to the public and asks a tracer to track a signature to the quorum that generates it. However, TAPS has three disadvantages: it 1) structures upon a centralized model, 2) assumes that both combiner and tracer are honest, and 3) leaves the tracing unnotarized and static. In this work, we introduce Decentralized, Threshold, dynamically Accountable and Private Signature (DeTAPS) that provides decentralized combining and tracing, enhanced privacy against untrusted combiners (tracers), and notarized and dynamic tracing. Specifically, we adopt Dynamic Threshold Public-Key Encryption (DTPKE) to dynamically notarize the tracing process, design non-interactive zero knowledge proofs to achieve public verifiability of notaries, and utilize the Key-Aggregate Searchable Encryption to bridge TAPS and DTPKE so as to awaken the notaries securely and efficiently. In addition, we formalize the definitions and security requirements for DeTAPS. Then we present a concrete construction and formally prove its security and privacy. To evaluate the performance, we build a prototype based on SGX2 and Ethereum.

以下是中文翻译：

阈值签名是一种基础的密码学原语，广泛应用于许多实际场景。正如Boneh和Komlo在CRYPTO’22中提出的，TAPS是一种结合隐私和问责制的阈值签名。它使得合并者能够在不向公众透露阈值 \(t\) 或签名法定人数的情况下合并 \(t\) 个签名份额，并要求追踪者将签名追踪到生成它的法定人数。然而，TAPS存在三个缺点：1) 依赖于中心化模型，2) 假设合并者和追踪者都是诚实的，3) 追踪过程未进行公证且是静态的。在本研究中，我们引入了去中心化、阈值、动态问责和隐私签名（DeTAPS），提供去中心化的合并和追踪，增强对不可信合并者（追踪者）的隐私保护，并实现公证和动态追踪。具体而言，我们采用动态阈值公钥加密（DTPKE）来动态公证追踪过程，设计非交互式零知识证明以实现公证人的公共可验证性，并利用密钥聚合可搜索加密技术将TAPS与DTPKE结合，以安全高效地唤醒公证人。此外，我们对DeTAPS的定义和安全要求进行了形式化。然后，我们提出了一个具体的构造并正式证明其安全性和隐私性。为了评估性能，我们基于SGX2和以太坊构建了一个原型。

## 关键词

+ 去中心化阈值签名动态问责
+ DeTAPS隐私保护阈值签名
+ 动态阈值公钥加密DTPKE
+ 非交互式零知识公证验证
+ 密钥聚合可搜索加密
+ 阈值签名去中心化合并追踪