---
title: "Signature schemes and anonymous credentials from bilinear maps"

标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 2004
created: 2025-05-15 09:58:15
modified: 2025-05-26 05:05:07
---

## Signature schemes and anonymous credentials from bilinear maps

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-540-28628-8_4)

## 作者

+ [Jan Camenisch](Jan%20Camenisch.md)
+ [Anna Lysyanskaya](Anna Lysyanskaya.md)

## 笔记

We propose a new and efficient signature scheme that is provably secure in the plain model. The security of our scheme is based on a discrete-logarithm-based assumption put forth by Lysyanskaya, Rivest, Sahai, and Wolf (LRSW) who also showed that it holds for generic groups and is independent of the decisional Diffie-Hellman assumption. We prove security of our scheme under the LRSW assumption for groups with bilinear maps. We then show how our scheme can be used to construct efficient anonymous credential systems as well as group signature and identity escrow schemes. To this end, we provide efficient protocols that allow one to prove in zero-knowledge the knowledge of a signature on a committed (or encrypted) message and to obtain a signature on a committed message.

以下是中文翻译：

我们提出了一个新的高效签名方案，该方案在标准模型(plain model)下可证明是安全的。我们方案的安全性基于由Lysyanskaya、Rivest、Sahai和Wolf提出的基于离散对数的假设(LRSW假设)，他们同时证明了该假设对通用群(generic groups)成立，且独立于判定性Diffie-Hellman假设。我们在具有双线性映射(bilinear maps)的群中，基于LRSW假设证明了我们方案的安全性。随后，我们展示了如何利用我们的方案构建高效的匿名凭证系统(anonymous credential systems)以及群签名(group signature)和身份托管(identity escrow)方案。为此，我们提供了高效的协议，这些协议允许在零知识(zero-knowledge)条件下证明对承诺（或加密）消息的签名知识，并获取对承诺消息的签名。

## 关键词

+ LRSW假设双线性映射签名
+ 标准模型可证明安全签名
+ 匿名凭证系统群签名身份托管
+ 零知识承诺签名知识证明
+ 通用双线性群签名方案