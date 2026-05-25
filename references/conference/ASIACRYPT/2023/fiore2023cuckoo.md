---
title: "Cuckoo commitments: registration-based encryption and key-value map commitments for large spaces"
标题简称:
论文类型: conference
会议简称: ASIACRYPT
发表年份: 2023
modified: 2025-04-13 17:40:15
---

## Cuckoo commitments: registration-based encryption and key-value map commitments for large spaces

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-981-99-8733-7_6)

## 作者

+ [Dario Fiore](Dario%20Fiore.md)
+ [Dimitris Kolonelos](Dimitris%20Kolonelos.md)
+ Paola de Perthuis 

## 笔记

Registration-Based Encryption (RBE) [Garg et al. TCC’18] is a public-key encryption mechanism in which users generate their own public and secret keys, and register their public keys with a central authority called the key curator. Similarly to Identity-Based Encryption (IBE), in RBE users can encrypt by only knowing the public parameters and the public identity of the recipient. Unlike IBE, though, RBE does not suffer the key escrow problem—one of the main obstacles of IBE’s adoption in practice—since the key curator holds no secret.  

以下是中文翻译：

基于注册的加密（RBE）[Garg等人，TCC’18]是一种公钥加密机制，用户在其中自行生成公钥和私钥，并将公钥注册到一个称为密钥管理中心的中央机构。与基于身份的加密（IBE）类似，在RBE中，用户仅需知道公共参数和接收者的公开身份即可进行加密。然而，与IBE不同的是，RBE不存在密钥托管问题——这是IBE在实际应用中面临的主要障碍之一——因为密钥管理中心并不持有任何秘密信息。

In this work, we put forward a new methodology to construct RBE schemes that support large users identities (i.e., arbitrary strings). Our main result is the first efficient pairing-based RBE for large identities. Prior to our work, the most efficient RBE is that of [Glaeser et al. ePrint’22] which only supports small identities. The only known RBE schemes with large identities are realized either through expensive non-black-box techniques (ciphertexts of 3.6 TB for 1000 users), via a specialized lattice-based construction [Döttling et al. Eurocrypt’23] (ciphertexts of 2.4 GB), or through the more complex notion of Registered Attribute-Based Encryption [Hohenberger et al. Eurocrypt’23]. By unlocking the use of pairings for RBE with large identity space, we enable a further improvement of three orders of magnitude, as our ciphertexts for a system with 1000 users are 1.7 MB.  
在本研究中，我们提出了一种新方法来构建支持大规模用户身份（即任意字符串）的RBE方案。我们的主要成果是首个基于配对且适用于大规模身份的高效RBE方案。在此之前，最高效的RBE方案来自[Glaeser等人，ePrint’22]，但它仅支持小规模身份。已知的支持大规模身份的RBE方案要么通过昂贵的非黑盒技术实现（1000用户时密文达3.6TB），要么依赖专门的基于格的构造[Döttling等人，Eurocrypt’23]（密文为2.4GB），或是通过更复杂的注册属性基加密概念[Hohenberger等人，Eurocrypt’23]。通过解锁配对技术在大规模身份空间RBE中的应用，我们实现了三个数量级的显著提升——在1000用户系统中，我们的密文大小仅为1.7MB。

The core technique of our approach is a novel use of cuckoo hashing in cryptography that can be of independent interest. We give two main applications. The first one is the aforementioned RBE methodology, where we use cuckoo hashing to compile an RBE with small identities into one for large identities. The second one is a way to convert any vector commitment scheme into a key-value map commitment. For instance, this leads to the first algebraic pairing-based key-value map commitments.  

## 关键词

+ 注册基础加密
+ 布谷鸟哈希
+ 向量承诺
+ 密钥值映射承诺
+ 配对加密
我们方法的核心技术是对布谷鸟哈希在密码学中的创新应用，这一技术本身具有独立的研究价值。我们展示了两个主要应用方向：首先是前述的基于注册的加密（RBE）方法，通过布谷鸟哈希将适用于小标识符的RBE方案扩展至大标识符场景；其次，提出了一种将任意向量承诺方案转化为键值映射承诺的通用方法。例如，这一转换催生了首个基于代数配对的键值映射承诺方案。