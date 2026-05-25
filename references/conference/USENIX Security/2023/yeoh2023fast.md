---
title: "Fast IDentity Online with Anonymous Credentials FIDO-AC"
标题简称:
论文类型: conference
会议简称: USENIX Security
发表年份: 2023
created: 2025-05-09 14:47:51
modified: 2025-05-09 14:48:30
---

## Fast IDentity Online with Anonymous Credentials FIDO-AC

## 发表信息

+ [原文链接](https://www.usenix.org/conference/usenixsecurity23/presentation/yeoh)

## 作者

+ Wei-Zhu Yeoh
+ Michal Kepkowski
+ Gunnar Heide
+ Dali Kaafar
+ [Lucjan Hanzlik](Lucjan%20Hanzlik.md)

## 笔记

Web authentication is a critical component of today's Internet and the digital world we interact with. The FIDO2 protocol enables users to leverage common devices to easily authenticate to online services in both mobile and desktop environments, following the passwordless authentication approach based on cryptography and biometric verification. However, there is little to no connection between the authentication process and users' attributes. More specifically, the FIDO protocol does not specify methods that could be used to combine trusted attributes with the FIDO authentication process generically and allow users to disclose them to the relying party arbitrarily. In essence, applications requiring attributes verification (e.g., age or expiry date of a driver's license, etc.) still rely on ad-hoc approaches that do not satisfy the data minimization principle and do not allow the user to check the disclosed data. A primary recent example is the data breach on Singtel Optus, one of the major telecommunications providers in Australia, where very personal and sensitive data (e.g., passport numbers) were leaked. This paper introduces FIDO-AC, a novel framework that combines the FIDO2 authentication process with the user's digital and non-shareable identity. We show how to instantiate this framework using off-the-shelf FIDO tokens and any electronic identity document, e.g., the ICAO biometric passport (ePassport). We demonstrate the practicality of our approach by evaluating a prototype implementation of the FIDO-AC system.

以下是中文翻译：

Web认证是当今互联网和我们所交互的数字世界的关键组成部分。FIDO2协议(FIDO2 protocol)使用户能够利用常见设备在移动和桌面环境中轻松地向在线服务进行认证，遵循基于密码学和生物特征验证的无密码认证方法。然而，认证过程与用户属性之间几乎没有任何关联。更具体地说，FIDO协议没有规定可以通用地将可信属性与FIDO认证过程相结合，并允许用户任意向依赖方披露这些属性的方法。本质上，需要属性验证的应用程序（例如，驾驶证的年龄或有效期等）仍然依赖于特定方法，这些方法既不满足数据最小化原则，也不允许用户检查所披露的数据。最近的一个主要例子是澳大利亚主要电信供应商之一Singtel Optus发生的数据泄露事件，其中泄露了非常个人和敏感的数据（如护照号码）。

本文介绍了FIDO-AC，这是一个将FIDO2认证过程与用户的数字化且不可共享的身份相结合的新型框架。我们展示了如何使用现成的FIDO令牌和任何电子身份文档（例如，ICAO生物特征护照(ePassport)）来实例化该框架。通过评估FIDO-AC系统的原型实现，我们证明了我们方法的实用性。

## 关键词

+ FIDO-AC匿名凭证认证框架
+ FIDO2无密码认证扩展
+ 电子护照ePassport属性验证
+ 用户属性隐私保护披露
+ 数据最小化原则认证
+ 生物特征认证属性结合
