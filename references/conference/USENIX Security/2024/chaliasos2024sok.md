---
title: "SoK: What Dont We Know Understanding Security Vulnerabilities in SNARKs"
标题简称:
论文类型: conference
会议简称: USENIX Security
发表年份: 2024
modified: 2025-04-17 13:44:34
created: 2025-04-13 14:50:49
---

## SoK: What Dont We Know Understanding Security Vulnerabilities in SNARKs

## 发表信息

+ [原文链接](https://www.usenix.org/conference/usenixsecurity24/presentation/chaliasos)

## 作者

+ Stefanos Chaliasos 
+ [Jens Ernstberger](Jens%20Ernstberger.md) 
+ David Theodore 
+ David Wong 
+ Mohammad Jahanara 
+ Benjamin Livshits 

## 笔记

Zero-knowledge proofs (ZKPs) have evolved from being a theoretical concept providing privacy and verifiability to having practical, real-world implementations, with SNARKs (Succinct Non-Interactive Argument of Knowledge) emerging as one of the most significant innovations. Prior work has mainly focused on designing more efficient SNARK systems and providing security proofs for them. Many think of SNARKs as "just math," implying that what is proven to be correct and secure is correct in practice. In contrast, this paper focuses on assessing end-to-end security properties of real-life SNARK implementations. We start by building foundations with a system model and by establishing threat models and defining adversarial roles for systems that use SNARKs. Our study encompasses an extensive analysis of 141 actual vulnerabilities in SNARK implementations, providing a detailed taxonomy to aid developers and security researchers in understanding the security threats in systems employing SNARKs. Finally, we evaluate existing defense mechanisms and offer recommendations for enhancing the security of SNARK-based systems, paving the way for more robust and reliable implementations in the future.

以下是中文翻译：

零知识证明（ZKPs）已从提供隐私与可验证性的理论概念，发展为具有实际应用价值的技术，其中简洁非交互式知识论证（SNARKs）成为最具突破性的创新之一。既往研究主要集中于设计更高效的SNARK系统并为其提供安全性证明。许多人将SNARKs视为"纯粹的数学"，认为理论上被证明正确且安全的方案在实践中必然无误。与此不同，本文着重评估现实场景中SNARK实现方案的端到端安全特性。我们首先构建系统模型基础，针对采用SNARKs的系统建立威胁模型并定义攻击者角色。通过对SNARK实现中141个真实漏洞的全面分析，本研究提出了细致的分类体系，帮助开发者和安全研究人员理解SNARK系统的安全威胁。最后，我们评估现有防御机制，并就增强基于SNARK的系统安全性提出建议，为未来实现更健壮可靠的系统铺平道路。

## 关键词

+ SNARKs安全漏洞分类
+ 零知识证明实现安全
+ SNARK实现端到端安全
+ 141漏洞分析分类体系
+ ZKP系统威胁模型
+ SNARK防御机制评估
