---
title: "How to leak a secret"
标题简称:
论文类型: conference
会议简称: ASIACRYPT
发表年份: 2001
created: 2025-05-12 08:44:54
modified: 2025-05-12 08:45:46
---

## How to leak a secret

## 发表信息

+ [原文链接]()

## 作者

+ Ronald L Rivest
+ Adi Shamir
+ Yael Tauman

## 笔记

In this paper we formalize the notion of a _ring signature_, which makes it possible to specify a set of possible signers without revealing which member actually produced the signature.Unlike group signatures, ring signatures have no group managers, no setup procedures, no revocation procedures, and no coordination:any user can choose any set of possible signers that includes himself,and sign any message by using his secret key and the others’ public keys,without getting their approval or assistance. Ring signatures provide an elegant way to leak authoritativ secrets in an anonymous way, to sign casual email in a way which can only be verified by its intended recipient, and to solve other problems in multiparty computations. The main contribution of this paper is a new construction of such signatures which is unconditionally signer-ambiguous, provably secure in the random oracle model,and exceptionally efficient:adding each ring member increases the cost of signing or verifying by a single modular multiplication and a single symmetric encryption.

以下是中文翻译：

本文提出并形式化了环签名(ring signature)的概念，它能够指定一组可能的签名者而不暴露实际产生签名的成员身份。与群签名(group signature)不同，环签名没有群管理员、无需设置程序、无需撤销程序，也无需协调：任何用户都可以选择包含自己在内的任意一组可能的签名者，并使用自己的私钥和其他人的公钥对任何消息进行签名，而无需获得他们的批准或协助。环签名为以下场景提供了一种优雅的解决方案：以匿名方式泄露权威性秘密、以只能被预期接收者验证的方式签署日常电子邮件，以及解决其他多方计算问题。本文的主要贡献是提出了这种签名的一种新构造，它具有无条件的签名者模糊性，在随机预言机模型下可证明安全，并且效率极高：添加每个环成员仅增加一次模乘运算和一次对称加密的开销。

## 关键词

+ 环签名
+ 签名者匿名性
+ 随机预言机模型
+ 秘密泄露
+ 无需协调签名