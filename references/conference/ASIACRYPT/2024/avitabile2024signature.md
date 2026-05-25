---
title: Signature-based witness encryption with compact ciphertext
标题简称: 
论文类型: conference
会议简称: ASIACRYPT
发表年份: 2024
modified: 2025-04-29 10:39:02
created: 2025-04-15 14:12:27
---

## Signature-based witness encryption with compact ciphertext

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-981-96-0875-1_1)

## 作者

+ Gennaro Avitabile 
+ [Nico Döttling](Nico%20D%C3%B6ttling.md)
+ Bernardo Magri 
+ Christos Sakkas 
+ Stella Wohnig 

## 笔记

Signature-based witness encryption (SWE) is a recently proposed notion that allows to encrypt a message with respect to a tag T and a set of signature verification keys. The resulting ciphertext can only be decrypted by a party who holds at least k different valid signatures w.r.t. T and k different verification keys out of the n keys specified at encryption time. Natural applications of this primitive involve distributed settings (e.g., blockchains), where multiple parties sign predictable messages, such as polling or randomness beacons. However, known SWE schemes without trusted setup have ciphertexts that scale linearly in the number of verification keys. This quickly becomes a major bottleneck as the system gets more distributed and the number of parties increases.

Towards showing the feasibility of SWE with ciphertext size sub-linear in the number of keys, we give a construction based on indistinguishability obfuscation (iO) for Turing machines and strongly puncturable signatures (SPS).

以下是中文翻译：

基于签名的见证加密(Signature-based witness encryption, SWE)是最近提出的一个概念，它允许使用标签T和一组签名验证密钥对消息进行加密。生成的密文只能被持有至少k个不同的有效签名(相对于T)和n个加密时指定的验证密钥中的k个不同密钥的参与方解密。这种原语的自然应用场景包括分布式环境(如区块链)，其中多个参与方对可预测的消息进行签名，例如投票或随机信标。然而，已知的无需可信设置的SWE方案中，密文大小与验证密钥数量呈线性关系。随着系统分布程度的提高和参与方数量的增加，这很快就会成为一个主要瓶颈。

为了证明密文大小相对于密钥数量呈次线性增长的SWE方案的可行性，我们提出了一个基于图灵机不可区分混淆(indistinguishability obfuscation, iO)和强可打孔签名(strongly puncturable signatures, SPS)的构造方案。

## 关键词

+ 见证加密
+ 不可区分混淆
+ 可打孔签名
+ 分布式签名
+ 密码学