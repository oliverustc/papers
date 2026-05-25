---
title: "Threshold encryption with silent setup"

标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 2024
created: 2025-04-17 10:50:10
modified: 2025-04-29 16:32:17
---

## Threshold encryption with silent setup

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-68394-7_12)
+ [code](https://github.com/tangle-network/silent-threshold-encryption-gadget)

## 作者

+ [Sanjam Garg](Sanjam%20Garg.md) 
+ [Dimitris Kolonelos](Dimitris%20Kolonelos.md)
+ [Guru-Vamsi Policharla](Guru-Vamsi%20Policharla.md)
+ [Mingyuan Wang](Mingyuan%20Wang.md) 

## 笔记

We build a concretely efficient threshold encryption scheme where the joint public key of a set of parties is computed as a _deterministic_ function of their locally computed public keys, enabling a _silent_ setup phase. By eliminating interaction from the setup phase, our scheme immediately enjoys several highly desirable features such as asynchronous setup, multiverse support, and dynamic threshold.

Prior to our work, the only known constructions of threshold encryption with silent setup relied on heavy cryptographic machinery such as indistinguishability Obfuscation or witness encryption for all of NP. Our core technical innovation lies in building a special purpose witness encryption scheme for the statement “at least _t_ parties have signed a given message”. Our construction relies on pairings and is proved secure in the Generic Group Model.

Notably, our construction, restricted to the special case of threshold t=1, gives an alternative construction of the (flexible) distributed broadcast encryption from pairings, which has been the central focus of several recent works.

We implement and evaluate our scheme to demonstrate its concrete efficiency. Both encryption and partial decryption are constant time, taking <7ms and <1ms, respectively. For a committee of 1024 parties, the aggregation of partial decryptions takes <200ms, when all parties provide partial decryptions. The size of each ciphertext is ≈8× larger than an ElGamal ciphertext.

以下是中文翻译：

我们构建了一种具体高效的门限加密方案，其中一组参与者的联合公钥作为其本地计算公钥的一个_确定性_函数进行计算，从而实现了_无声_设置阶段。通过消除设置阶段的交互，我们的方案立即享有多个高度期望的特性，如异步设置、多世界支持和动态门限。

在我们的工作之前，已知的唯一依赖无声设置的门限加密构造依赖于重型密码学机制，如不可区分混淆（indistinguishability Obfuscation）或针对所有NP问题的见证加密（witness encryption）。我们核心的技术创新在于为“至少_t_个参与者已签署给定消息”这一命题构建了一种特殊目的的见证加密方案。我们的构造依赖于配对，并在一般群模型（Generic Group Model）中证明了其安全性。

值得注意的是，我们的构造在门限_t=1_的特例下，提供了一种基于配对的（灵活的）分布式广播加密的替代构造，这也是最近几项工作的核心焦点。

我们实现并评估了我们的方案，以证明其具体效率。加密和部分解密的时间均为常数，分别为<7毫秒和<1毫秒。对于一个由1024个参与者组成的委员会，当所有参与者提供部分解密时，聚合部分解密的时间小于200毫秒。每个密文的大小约为ElGamal密文的8倍。

## 关键词

+ 无声设置门限加密确定性公钥
+ 见证加密门限签名配对构造
+ 异步设置动态门限多世界支持
+ 通用群模型门限加密安全证明
+ 分布式广播加密配对替代构造