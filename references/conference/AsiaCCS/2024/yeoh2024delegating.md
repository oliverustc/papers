---
title: Delegating FIDO Credentials Using Single-use ECDSA Signatures
doi: 10.1145/3634737.3657004
标题简称: 
论文类型: conference
会议简称: AsiaCCS
发表年份: 2024
created: 2025-05-09 14:37:34
modified: 2025-05-09 15:00:49
---
## Delegating FIDO Credentials Using Single-use ECDSA Signatures

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3634737.3657004)

## 作者

+ Wei-Zhu Yeoh
+ [Lucjan Hanzlik](Lucjan%20Hanzlik.md)
+ Oliver Valta

## 笔记

Single-use delegatable signatures allow a delegatee to give the signing right in a restrictive way to a third party. This cryptographic primitive finds applications in the design of blank checks and can even delegate access rights in web authentication. Unfortunately, known constructions work only with non-standard signature schemes and require non-existing secure hardware, making them impractical.

In this paper, we construct single-use delegatable ECDSA signatures based on commodity smartphones with hardware-backed keystores. We show how to apply our construction to the web authentication use case. In particular, we show how to delegate FIDO credentials to third parties while not introducing new assumptions to the setting besides the delegate's trust in the security of the keystore. As an independent application, we discuss the use of our construction as a way to implement blind checks in ECDSA-based cryptocurrencies.

以下是中文翻译：

一次性可委托签名（single-use delegatable signatures）允许受托人以受限方式将签名权限委托给第三方。这种密码学原语在空白支票的设计中有所应用，甚至可以在网络认证中委托访问权限。然而，已知的构造方案仅适用于非标准签名方案，且需要目前尚不存在的安全硬件，这使得它们在实践中难以应用。

在本文中，我们基于具有硬件支持密钥库的普通智能手机，构建了一次性可委托的ECDSA（Elliptic Curve Digital Signature Algorithm，椭圆曲线数字签名算法）签名方案。我们展示了如何将我们的构造应用于网络认证场景。特别地，我们展示了如何将FIDO（Fast IDentity Online）凭证委托给第三方，同时除了受托方对密钥库安全性的信任外，不引入新的假设条件。作为一个独立的应用，我们讨论了如何将我们的构造用作在基于ECDSA的加密货币中实现空白支票的方法。

## 关键词

+ 可委托签名
+ FIDO凭证
+ ECDSA
+ 网络认证
+ 硬件密钥库