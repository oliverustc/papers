---
title: "Everlasting Anonymous Rate-Limited Tokens"
标题简称:
论文类型: preprint
预印本简称: archive
发表年份: 2025
created: 2025-06-09 09:20:55
modified: 2025-06-09 10:24:31
---

## Everlasting Anonymous Rate-Limited Tokens

## 发表信息

+ [原文链接](https://eprint.iacr.org/2025/1030)

## 作者

+ Rutchathon Chairattana-Apirom
+ [Nico Döttling](Nico%20D%C3%B6ttling.md)
+ [Anna Lysyanskaya](Anna%20Lysyanskaya.md)
+ Stefano Tessaro

## 笔记

Anonymous rate-limited tokens are a special type of credential that can be used to improve the efficiency of privacy-preserving authentication systems like Privacy Pass. In such a scheme, a user obtains a "token dispenser" by interacting with an issuer, and the dispenser allows the user to create up to a pre-determined number k of unlinkable and publicly verifiable tokens. Unlinkable means that one should not be able to tell that two tokens originate from the same dispenser, but also they cannot be linked to the interaction that generated the dispenser. Furthermore, we can limit the rate at which these tokens are created by linking each token to a context (e.g., the service we are authenticating to), and imposing a limit N≤k such that seeing more than N tokens for the same context will reveal the identity of the user. Constructions of such tokens were first given by Camenisch, Hohenberger and Lysyanskaya (EUROCRYPT '05) and Camenisch, Hohenberger, Kohlweiss, Lysyanskaya, and Meyerovich (CCS '06). In this work, we present the first construction of \emph{everlasting} anonymous rate-limited tokens, for which unlinkability holds against computationally unbounded adversaries, whereas other security properties (e.g., unforgeability) remain computational. Our construction relies on pairings. While several parameters in our construction unavoidably grow with k, the key challenge we resolve is ensuring that the complexity of dispensing a token is independent of the parameter k. We are motivated here by the goal of providing solutions that are robust to potential future quantum attacks against the anonymity of previously stored tokens. A construction based on post-quantum secure assumptions (e.g., based on lattices) would be rather inefficient---instead, we take a pragmatic approach dispensing with post-quantum security for properties not related to privacy.

以下是中文翻译：

匿名限次令牌（anonymous rate-limited tokens）是一种特殊类型的凭证，可用于提升隐私保护认证系统（如Privacy Pass）的效率。在该方案中，用户通过与发行方（issuer）交互获得一个“令牌分发器（token dispenser）”，该分发器允许用户生成最多预定数量（k）的不可关联（unlinkable）且可公开验证的令牌。不可关联性意味着：无法判断两个令牌是否源自同一分发器，同时这些令牌也无法与生成分发器的交互过程关联。此外，通过将每个令牌绑定到特定上下文（context）（例如认证目标服务），并设置上限（N≤k），可以限制令牌的生成速率——若同一上下文出现超过N个令牌，将暴露用户身份。

此类令牌的构造最早由Camenisch、Hohenberger和Lysyanskaya（EUROCRYPT '05）以及Camenisch、Hohenberger、Kohlweiss、Lysyanskaya和Meyerovich（CCS '06）提出。本文中，我们首次提出**永久性（everlasting）匿名限次令牌**的构造方案，其不可关联性针对计算能力无界的攻击者成立，而其他安全属性（如不可伪造性）仍保持计算安全性。我们的方案基于配对运算（pairings）。尽管构造中的部分参数不可避免地随k增长，但我们解决的核心难题是确保生成令牌的复杂度与参数k无关。

本研究的动机是为未来潜在的量子攻击（针对已存储令牌的匿名性）提供鲁棒性解决方案。若基于后量子安全假设（如格密码）构造方案，效率将极低——因此，我们采取务实方法，仅对与隐私无关的属性放弃后量子安全性。


## 关键词

+ 永久性匿名限次令牌不可关联性
+ Privacy Pass匿名认证令牌分发器
+ 配对运算永久性匿名安全
+ 后量子鲁棒隐私保护凭证
+ 无界计算攻击者匿名性安全