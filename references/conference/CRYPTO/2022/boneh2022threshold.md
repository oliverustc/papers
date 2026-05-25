---
title: "Threshold signatures with private accountability"

标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 2022
created: 2025-05-13 05:09:39
modified: 2025-05-28 02:57:14
---

## Threshold signatures with private accountability

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-15985-5_19)

## 作者

+ [Dan Boneh](Dan%20Boneh.md)
+ Chelsea Komlo

## 笔记

Existing threshold signature schemes come in two flavors: (i) _fully private_, where the signature reveals nothing about the set of signers that generated the signature, and (ii) _accountable_, where the signature completely identifies the set of signers. In this paper we propose a new type of threshold signature, called TAPS, that is a hybrid of privacy and accountability. A TAPS signature is fully private from the public’s point of view. However, an entity that has a secret tracing key can trace a signature to the threshold of signers that generated it. A TAPS makes it possible for an organization to keep its inner workings private, while ensuring that signers are accountable for their actions. We construct a number of TAPS schemes. First, we present a generic construction that builds a TAPS from any accountable threshold signature. This generic construction is not efficient, and we next focus on efficient schemes based on standard assumptions. We build two efficient TAPS schemes (in the random oracle model) based on the Schnorr signature scheme. We conclude with a number of open problems relating to efficient TAPS.

以下是中文翻译：

现有的门限签名方案分为两类：(i) 完全私密型，其中签名不会泄露任何关于生成签名的签名者集合的信息，以及 (ii) 可追责型，其中签名完全标识出签名者集合。在本文中，我们提出了一种新型的门限签名方案，称为TAPS（Traceable Anonymous Threshold Signature，可追踪匿名门限签名），它是隐私性和可追责性的混合体。从公众的角度来看，TAPS签名是完全私密的。然而，拥有秘密追踪密钥的实体可以追踪签名到生成它的门限签名者集合。TAPS使组织能够保持其内部运作的私密性，同时确保签名者对其行为负责。我们构造了多个TAPS方案。首先，我们提出了一个通用构造，它可以从任何可追责的门限签名构建TAPS。这个通用构造不够高效，因此我们接下来关注基于标准假设的高效方案。我们基于Schnorr签名方案构建了两个高效的TAPS方案（在随机预言机模型中）。最后，我们提出了一些与高效TAPS相关的开放性问题。

---

先基于原文的重点内容，做出下文笔记：

本文将门限签名主要分为两类：

### 隐私门限签名-privacy threshold signature-PTS

> 私有阈值签名（PTS）方案在需要隐藏组织内部运作时使用。例如，一个运行网络服务器的组织可能会选择将服务器的秘密TLS密钥分割到n台机器中，以便至少需要t台机器来生成签名并完成TLS握手。通过使用PTS，组织可以将阈值t对外隐藏，以避免泄露攻击者需要攻陷的机器数量，从而伪造签名。同样，签名不应透露参与生成签名的t台机器的集合，以确保不会暴露当前在线的机器信息。

对消息 $m$ 的签名 $\sigma$ 不会泄露关于门限 $t$ 的任何信息，也不会泄露生成该签名的 $t$ 个参与方的法定人数的信息。即使对手看到一系列其选择的消息上的签名，这一点仍然成立。

+ [Practical threshold signatures (**EUROCRYPT 2000**)](shoup2000practical)
+ [Fully distributed threshold RSA under standard assumptions (**ASIACRYPT 2001**)](fouque2001fully)
+ [Threshold signatures, multisignatures and blind signatures based on the gap-Diffie-Hellman-group signature scheme (**PKC 2002**)](boldyreva2002threshold)
+ 

### 可追责门限签名 accountable threshold signature ATS

> 可追溯阈值签名（ATS）方案通常用于需要问责的金融应用中。例如，如果五位银行高管中需要三位来授权银行转账，那么在批准欺诈性转账的情况下，必须确保完全的问责。当使用ATS方案时，针对欺诈交易的签名将能够识别出授权该交易的三位银行高管。

+ [Short signatures from the Weil pairing (**ASIACRYPT 2001**)](boneh2001short)
+ [Multi-signatures in the plain public-key model and a general forking lemma (**CCS 2006**)](bellare2006multi)
+ [Multisignatures secure under the discrete logarithm assumption and a generalized forking lemma (**CCS 2008**)](bagherzandi2008multisignatures)
+ [Accountable-subgroup multisignatures (**CCS 2001**)](micali2001accountable)
+ [MuSig: Simple two-round Schnorr multi-signatures (**CRYPTO 2021**)](nick2021musig2)

本文提出了一种同时保证可追责和隐私的门限签名算法（Threshold， Accountable， and Private Signature）：

其主要的工作流程如下：

1. 密钥生成：生成公钥$pk$，n个私钥$sk_1,...,sk_n$，一个追踪密钥$sk_t$
2. 签名生成：$n$个用户中的$t$个对消息$m$生成签名$\sigma$
3. 签名验证：$pk$，$m$，$\sigma$输出$accept$/$reject$,且验证过程中对$t$的数值和具体签名者的身份一无所知
4. 任何持有$sk_t$的用户都能追踪出签名$\sigma$是由哪些用户签名的

## 相关工作

### 环签名

+ [How to leak a secret (**ASIACRYPT 2001**)](rivest2001leak)
+ [Deniable ring authentication (**CRYPTO 2002**)](naor2002deniable)
+ [Ring signatures: Stronger definitions, and constructions without random oracles (**Journal of Cryptology 2009**)](bender2009ring)

#### accountable/traceable ring signature 可追溯环签名

+ [Short Accountable Ring Signatures Based on DDH **ESORICS 2015**](https://link.springer.com/chapter/10.1007/978-3-319-24174-6_13)
+ [Sub-linear size traceable ring signatures without random oracles.](https://globals.ieice.org/en_transactions/fundamentals/10.1587/transfun.E95.A.151/_p)
+ [Traceable ring signature. **PKC 2007**](https://link.springer.com/chapter/10.1007/978-3-540-71677-8_13)
+ [Accountable ring signatures: a smart card approach.](https://link.springer.com/chapter/10.1007/1-4020-8147-2_18)
+ [Anonymous Identification in Ad Hoc Groups **(EUROCRYPT 2004)**](https://link.springer.com/chapter/10.1007/978-3-540-24676-3_36)
#### threshold ring signature 门限环签名

+ [Threshold Ring Signatures and Applications to Ad-hoc Groups **(CRYPTO 2002)**](https://link.springer.com/chapter/10.1007/3-540-45708-9_30)
+ [Threshold Ring Signatures: New Definitions and Post-quantum Security **(PKC 2020)**](https://link.springer.com/chapter/10.1007/978-3-030-45388-6_15)
+ [A Separable Threshold Ring Signature Scheme](https://link.springer.com/chapter/10.1007/978-3-540-24691-6_2)
+ [Stronger Notions and a More Efficient Construction of Threshold Ring Signatures](https://link.springer.com/chapter/10.1007/978-3-030-88238-9_18)
+ [Separable Linkable Threshold Ring Signatures](https://link.springer.com/chapter/10.1007/978-3-540-30556-9_30)
这些方案都无法实现可追溯，即使是几个linkable threshold ring signatures也只是能支持将产生两个环签名的用户链接(link)起来,无法追溯

### 群签名

[Short group signatures (**CRYPTO 2004**)](boneh2004short)
[Foundations of fully dynamic group signatures (**Journal of Cryptology 2020**)](bootle2020foundations)



## 引用此工作的后续工作

https://scholar.google.com.hk/scholar?start=0&hl=zh-CN&as_sdt=2005&sciodt=0,5&cites=3241213673582167487&scipsc=




## 关键词

+ TAPS可追踪匿名门限签名
+ 隐私可追责混合门限签名
+ 追踪密钥签名者集合识别
+ Schnorr随机预言机TAPS构造
+ 门限签名隐私与问责平衡