---
title: "A practical and provably secure coalition-resistant group signature scheme"

标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 2000
created: 2025-05-26 10:49:41
modified: 2025-05-26 05:05:35
---

## A practical and provably secure coalition-resistant group signature scheme

## 发表信息

+ [原文链接]()

## 作者

+ Giuseppe Ateniese
+ [Jan Camenisch](Jan%20Camenisch.md)
+ Marc Joye
+ Gene Tsudik

## 笔记

A group signature scheme allows a group member to sign messages anonymously on behalf of the group. However, in the case of a dispute, the identity of a signature’s originator can be revealed (only) by a designated entity. The interactive counterparts of group signatures are identity escrow schemes or group identification scheme with revocable anonymity. This work introduces a new provably secure group signature and a companion identity escrow scheme that are significantly more efficient than the state of the art. In its interactive, identity escrow form, our scheme is proven secure and coalition-resistant under the strong RSA and the decisional Diffie-Hellman assumptions. The security of the non-interactive variant, i.e., the group signature scheme, relies additionally on the Fiat-Shamir heuristic (also known as the random oracle model).

以下是中文翻译：

一群签名方案允许群成员代表该群匿名签署消息。然而，在争议情况下，签名发起者的身份只能由指定实体揭示。群签名的交互式对应物是身份托管方案或具有可撤销匿名性的群识别方案。本研究引入了一种新的可证明安全的群签名及其伴随的身份托管方案，这些方案在效率上显著优于现有技术。在其交互式身份托管形式中，我们的方案在强RSA和可判定Diffie-Hellman假设下被证明是安全且抵抗合谋的。非交互式变体，即群签名方案的安全性还额外依赖于Fiat-Shamir启发式（也称为随机 oracle 模型）。

[Foundations of group signatures: Formal definitions, simplified requirements, and a construction based on general assumptions (**EUROCRYPT 2003**)](bellare2003foundations)提出了本文在安全性的不足之处如下：

### 安全性证明的不足之处

尽管本文中的方案声称在随机预言模型中已被证明安全，但该工作存在明显不足：

#### 匿名性要求表述过于模糊

该论文将匿名性简单地描述为"给定某消息的有效签名，除群管理者外，识别实际签名者对所有人来说在计算上都是困难的"。这类似于将加密方案的隐私要求简化为"密文不应向密钥拥有者以外的人透露消息信息"，而实际上，真正捕捉隐私性需要更精确和非平凡的定义。

#### 攻击模型不明确

该论文留下了多个关键问题未解答：

- 攻击者是否可以查看或请求之前的签名？
- 攻击者是否能要求群管理者"打开"之前的一些签名？
- 攻击者是否可以预先获取部分信息来排除某些签名者？

## 结论

由于这些问题未得到解答，声称该方案已经实现了"已证明安全"为时过早。要真正达到密码学意义上的安全证明，需要更严格和明确的安全定义及攻击模型。

## 关键词

+ 可证明安全抗合谋群签名
+ 身份托管可撤销匿名性
+ 强RSA判定Diffie-Hellman安全假设
+ Fiat-Shamir启发式非交互签名
+ 实用群签名效率改进