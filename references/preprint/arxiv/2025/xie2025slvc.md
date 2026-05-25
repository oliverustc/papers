---
title: "SLVC-DIDA: Signature-less Verifiable Credential-based Issuer-hiding and Multi-party Authentication for Decentralized Identity"
标题简称:
论文类型: preprint
预印本简称: arxiv
发表年份: 2025
created: 2025-04-16 10:42:06
modified: 2025-05-13 11:21:45
---

## SLVC-DIDA: Signature-less Verifiable Credential-based Issuer-hiding and Multi-party Authentication for Decentralized Identity

## 发表信息

+ [原文链接](https://arxiv.org/abs/2501.11052)

## 作者

+ Tianxiu Xie
+ Keke Gai
+ Jing Yu
+ [Liehuang Zhu](Liehuang%20Zhu.md)
+ [Bin Xiao](Bin%20Xiao.md)
## 笔记

As an emerging paradigm in digital identity, Decentralized Identity (DID) appears advantages over traditional identity management methods in a variety of aspects, e.g., enhancing user-centric online services and ensuring complete user autonomy and control. Verifiable Credential (VC) techniques are used to facilitate decentralized DID-based access control across multiple entities. However, existing DID schemes generally rely on a distributed public key infrastructure that also causes challenges, such as context information deduction, key exposure, and issuer data leakage. To address the issues above, this paper proposes a Permanent Issuer-Hiding (PIH)-based DID multi-party authentication framework with a signature-less VC model, named SLVC-DIDA, for the first time. Our proposed scheme avoids the dependence on signing keys by employing hashing and issuer membership proofs, which supports universal zero-knowledge multi-party DID authentications, eliminating additional technical integrations. We adopt a zero-knowledge RSA accumulator to maintain the anonymity of the issuer set, thereby enabling public verification while safeguarding the privacy of identity attributes via a Merkle tree-based VC list. By eliminating reliance on a Public Key Infrastructure (PKI), SLVC-DIDA enables fully decentralized issuance and verification of DIDs. Furthermore, our scheme ensures PIH through the implementation of the zero-knowledge Issuer set and VC list, so that the risks of key leakage and contextual inference attacks are effectively mitigated. Our experiments further evaluate the effectiveness and practicality of SLVC-DIDA.

以下是中文翻译：

摘要：作为数字身份的新兴范式，去中心化身份（DID）在增强以用户为中心的在线服务及确保用户完全自主控制等多方面展现出优于传统身份管理方法的优势。可验证凭证（VC）技术被用于促进基于DID的多实体间去中心化访问控制。然而，现有DID方案普遍依赖分布式公钥基础设施，这也带来了上下文信息推断、密钥暴露及颁发者数据泄露等挑战。针对上述问题，本文首次提出了一种无签名VC模型的永久颁发者隐藏（PIH）DID多方认证框架——SLVC-DIDA。该方案通过哈希与颁发者成员证明替代签名密钥依赖，支持通用零知识多方DID认证，无需额外技术集成。我们采用零知识RSA累加器维护颁发者集合的匿名性，从而在实现公开验证的同时，借助基于Merkle树的VC列表保护身份属性隐私。通过摆脱对公钥基础设施（PKI）的依赖，SLVC-DIDA实现了完全去中心化的DID颁发与验证。此外，方案通过零知识颁发者集合与VC列表的实施确保PIH特性，有效降低了密钥泄露与上下文推理攻击的风险。实验进一步验证了SLVC-DIDA的有效性与实用性。

## 关键词

+ SLVC-DIDA无签名可验证凭证DID认证
+ 永久颁发者隐藏PIH多方认证框架
+ 零知识RSA累加器颁发者匿名性
+ Merkle树VC列表身份属性隐私
+ 去中心化身份无PKI依赖验证
