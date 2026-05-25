---
title: "Revocable TACO: Revocable Threshold based Anonymous Credentials over Blockchains"
标题简称: 
论文类型: conference
会议简称: AsiaCCS
发表年份: 2024
created: 2025-05-20 02:21:25
modified: 2025-05-21 10:48:47
---

## Revocable TACO: Revocable Threshold based Anonymous Credentials over Blockchains

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3634737.3637656)

## 作者

+ Kanchan Bisht
+ Neel Yogendra Kansagra
+ Reisha Ali
+ Mohammed Sayeed Shaik
+ Maria Francis
+ Kotaro Kataoka

## 笔记

The anonymity, multi-show unlinkability, and selective disclosure property of anonymous credentials enables users to access third-party services without revealing unnecessary details or being profiled. Threshold-based anonymous credentials provide a distributed framework to issue these credentials. While all of this enhances privacy, anonymity can also be misused and some schemes, therefore, have an opening mechanism, which enables the authorities to trace a user's identity. Nevertheless, relying solely on this measure is inadequate as the users can continue to use their previously issued anonymous credentials to authenticate themselves successfully with the service providers. To address this issue, we propose a revocation mechanism for such schemes using dynamic threshold accumulators (DTA) (Helminger _et al._ 2021). We first formally define a generic threshold-based anonymous credentials with an opening scheme (TACO) and subsequently propose an extension of TACO, _"Revocable TACO (RTACO)" - revocable threshold-based credentials over blockchains_ - that integrates a revocation mechanism based on DTAs to the TACO system. In RTACO, we integrate a revocation handle into the credential as an extra attribute, allowing the disclosure of this attribute during the opening phase, which is then used to blocklist the credential, preventing its further use. We formally prove the security of this scheme in the universal composability (UC) framework. We also give a proof-of-concept implementation of RTACO over the Ethereum blockchain.

以下是中文翻译：

匿名凭证（anonymous credentials）的匿名性、多次展示不可链接性和选择性披露特性，使用户能够在不透露不必要细节或被画像的情况下访问第三方服务。基于阈值的匿名凭证提供了一个分布式框架来颁发这些凭证。尽管这些特性增强了隐私保护，但匿名性也可能被滥用，因此一些方案设置了开启机制（opening mechanism），使得授权机构能够追踪用户身份。然而，仅仅依赖这一措施是不够的，因为用户可以继续使用之前颁发的匿名凭证成功向服务提供商进行身份认证。为了解决这一问题，我们提出了使用动态阈值累加器（Dynamic Threshold Accumulators, DTA）的吊销机制。

我们首先正式定义了带开启方案的基于阈值的匿名凭证（Threshold-based Anonymous Credentials with Opening Scheme, TACO），随后提出了TACO的扩展版本"可吊销TACO（Revocable TACO, RTACO）"——基于区块链的可吊销阈值凭证，它整合了基于动态阈值累加器的吊销机制。在RTACO中，我们将吊销句柄（revocation handle）作为额外属性集成到凭证中，允许在开启阶段披露此属性，进而用于将凭证列入黑名单，阻止其进一步使用。我们在通用可组合性（Universal Composability, UC）框架下正式证明了该方案的安全性。我们还在以太坊区块链上给出了RTACO的概念验证实现。

## 关键词

+ 可吊销凭证
+ 匿名凭证
+ 阈值密码学
+ 区块链
+ 隐私保护