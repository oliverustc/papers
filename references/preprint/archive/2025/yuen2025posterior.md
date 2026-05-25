---
title: "Posterior Security: Anonymity and Message Hiding of Standard Signatures"
标题简称:
论文类型: preprint
预印本简称: archive
发表年份: 2025
created: 2025-05-23 02:00:07
modified: 2025-05-23 02:03:02
---

## Posterior Security: Anonymity and Message Hiding of Standard Signatures

## 发表信息

+ [原文链接](https://eprint.iacr.org/2025/855)

已经被CCS 2025接受，后续等到有链接之后再更新此笔记的位置

## 作者

+ [Tsz Hon Yuen](Tsz%20Hon%20Yuen.md)
+ Ying-Teng Chen
+ Shimin Pan
+ Jiangshan Yu
+ Joseph K Liu

## 笔记

We introduce posterior security of digital signatures, the additional security features after the original signature is generated. It is motivated by the scenario that some people store their secret keys in secure hardware and can only obtain a standard signature through a standardized interface. In this paper, we consider two different posterior security features: anonymity and message hiding. We first introduce incognito signature, a new mechanism to anonymize a standard signature. Different from other ring or group signatures, the signer generates a standard (non-anonymous) signature first. The signature is then anonymized by a converter before sending to the verifier, by hiding the signer public key with a set of decoy public keys. We then introduce concealed signature which hides the message in a commitment. The standard signature is converted such that it can be verified with the commitment. The models of posterior anonymity and posterior message hiding capture the separation of the signer and the converter. Anonymity or message hiding is provided by the converter after the creation of a standard signature by the signer. We give generic constructions of incognito signature and concealed signature. It can be applied to standard signatures like Schnorr. It gives the first practical anonymized ECDSA signature, and the signature size is logarithmic to the number of decoy public keys n. The existing ring signature scheme with ECDSA keys is at least 152 times longer than our scheme for n≤4096. The incognito signature and concealed signature can be composed to provide posterior anonymity and message hiding. It is useful in applications like two-tier central bank digital currency, where users want to hide their addresses (public keys) and transaction amounts (messages) when the payment is settled in the interbank layer.

以下是中文翻译：

我们介绍了数字签名的后验安全性(posterior security)，即原始签名生成后的额外安全特性。这一概念源于某些人将其密钥存储在安全硬件中，只能通过标准化接口获取标准签名的场景。在本文中，我们考虑两种不同的后验安全特性：匿名性和消息隐藏。首先，我们引入了隐匿签名(incognito signature)，这是一种匿名化标准签名的新机制。与其他环签名或群签名不同，签名者首先生成标准(非匿名)签名。然后，该签名在发送给验证者之前由转换器进行匿名化处理，通过使用一组诱饵公钥来隐藏签名者的公钥。其次，我们引入了隐藏签名(concealed signature)，它将消息隐藏在承诺(commitment)中。标准签名被转换，使其可以通过承诺进行验证。后验匿名性和后验消息隐藏的模型体现了签名者和转换器的分离。匿名性或消息隐藏是在签名者创建标准签名后由转换器提供的。

我们提供了隐匿签名和隐藏签名的通用构造方法。这些方法可应用于Schnorr等标准签名。它提供了首个实用的匿名化ECDSA签名，且签名大小与诱饵公钥数量n呈对数关系。对于n≤4096，现有使用ECDSA密钥的环签名方案至少比我们的方案长152倍。隐匿签名和隐藏签名可以组合使用，以提供后验匿名性和消息隐藏功能。这在双层中央银行数字货币等应用中非常有用，用户希望在银行间层面结算支付时隐藏其地址(公钥)和交易金额(消息)。

## 关键词

+ 后验安全性数字签名匿名性
+ 隐匿签名转换器标准签名匿名化
+ 隐藏签名消息承诺零知识
+ 匿名ECDSA对数环签名大小
+ 中央银行数字货币隐私支付