---
title: "With a little help from my friends: Constructing practical anonymous credentials"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2021
created: 2025-05-09 14:25:31
modified: 2025-05-09 14:26:13
---

## With a little help from my friends: Constructing practical anonymous credentials

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3460120.3484582)
+ [archive](https://eprint.iacr.org/2021/1419)

## 作者

+ [Lucjan Hanzlik](Lucjan%20Hanzlik.md)
+ Daniel Slamanig

## 笔记

Anonymous credentials (ACs) are a powerful cryptographic tool for the secure use of digital services, when simultaneously aiming for strong privacy guarantees of users combined with strong authentication guarantees for providers of services. They allow users to selectively prove possession of attributes encoded in a credential without revealing any other meaningful information about themselves. While there is a significant body of research on AC systems, modern use-cases of ACs such as mobile applications come with various requirements not sufficiently considered so far. These include preventing the sharing of credentials and coping with resource constraints of the platforms (e.g., smart cards such as SIM cards in smartphones). Such aspects are typically out of scope of AC constructions, and, thus AC systems that can be considered entirely practical have been elusive so far.

In this paper we address this problem by introducing and formalizing the notion of core/helper anonymous credentials (CHAC). The model considers a constrained core device (e.g., a SIM card) and a powerful helper device (e.g., a smartphone). The key idea is that the core device performs operations that do not depend on the size of the credential or the number of attributes, but at the same time the helper device is unable to use the credential without its help. We present a provably secure generic construction of CHACs using a combination of signatures with flexible public keys (SFPK) and the novel notion of aggregatable attribute-based equivalence class signatures (AAEQ) along with a concrete instantiation. The key characteristics of our scheme are that the size of showing tokens is independent of the number of attributes in the credential(s) and that the core device only needs to compute a single elliptic curve scalar multiplication, regardless of the number of attributes. We confirm the practical efficiency of our CHACs with an implementation of our scheme on a Multos smart card as the core and an Android smartphone as the helper device. A credential showing requires less than 500 ms on the smart card and around 200 ms on the smartphone (even for a credential with 1000 attributes).

以下是中文翻译：

在本文中，我们通过引入并形式化核心/辅助匿名凭证(core/helper anonymous credentials, CHAC)的概念来解决这个问题。该模型考虑了一个受约束的核心设备(例如SIM卡)和一个功能强大的辅助设备(例如智能手机)。其核心思想是核心设备执行的操作不取决于凭证的大小或属性的数量，而同时辅助设备无法在没有其帮助的情况下使用凭证。我们使用灵活公钥签名(SFPK)和新颖的可聚合属性基等价类签名(AAEQ)的组合，以及一个具体实例化，提出了CHAC的可证明安全的通用构造。

我们方案的关键特征是显示令牌的大小与凭证中的属性数量无关，核心设备只需要计算一个椭圆曲线标量乘法，无论属性数量如何。我们通过将我们的方案实现在Multos智能卡(作为核心)和Android智能手机(作为辅助设备)上，确认了我们CHAC的实际效率。凭证显示在智能卡上需要不到500毫秒，在智能手机上需要大约200毫秒(即使凭证有1000个属性)。

## 关键词

+ 匿名凭证
+ 多设备架构
+ 属性基签名
+ 灵活公钥
+ 隐私保护
