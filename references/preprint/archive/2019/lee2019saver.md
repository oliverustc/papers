---
title: "SAVER: SNARK-friendly, Additively-homomorphic, and Verifiable Encryption and decryption with Rerandomization"
标题简称:
论文类型: preprint
预印本简称: archive
发表年份: 2019
---

## SAVER: SNARK-friendly, Additively-homomorphic, and Verifiable Encryption and decryption with Rerandomization

## 发表信息

+ [原文链接](https://eprint.iacr.org/2019/1270)

## 作者

+ Jiwon Lee 
+ Jaekyoung Choi 
+ Jihye Kim 
+ [Hyunok Oh](Hyunok%20Oh.md)
## 笔记

In the pairing-based zero-knowledge succinct non-interactive arguments of knowledge (zk-SNARK), there often exists a requirement for the proof system to be combined with encryption. As a typical example, a blockchain-based voting system requires the vote to be confidential (using encryption), while verifying voting validity (using zk-SNARKs). In these combined applications, a typical solution is to extend the zk-SNARK circuit to include the encryption code. However, complex cryptographic operations in the encryption algorithm increase the circuit size, which leads to impractically large proving time and CRS size. In this paper, we propose SNARK-friendly, Additively-homomorphic, and Verifiable Encryption and decryption with Rerandomization or SAVER, which is a novel approach to detach the encryption from the SNARK circuit. The encryption in SAVER holds many useful properties. It is SNARK-friendly: the encryption is conjoined with an existing pairing-based SNARK, in a way that the encryptor can prove pre-defined properties while encrypting the message apart from the SNARK. It is additively-homomorphic: the ciphertext holds a homomorphic property from the ElGamal-based encryption. It is a verifiable encryption: one can verify arbitrary properties of encrypted messages by connecting with the SNARK system. It provides a verifiable decryption: anyone without the secret can still verify that the decrypted message is indeed from the given ciphertext. It provides rerandomization: the proof and the ciphertext can be rerandomized as independent objects so that even the encryptor (or prover) herself cannot identify the origin. For the representative application, we also propose a Vote-SAVER based on SAVER, which is a novel voting system where voter's secret key lies only with the voter himself. The Vote-SAVER satisfies receipt-freeness (which implies ballot privacy), individual verifiability (which implies non-repudiation), vote verifiability, tally uniqueness, and voter anonymity. The experimental results show that our SAVER with respect to the Vote-SAVER relation yields 0.7 s for zk-SNARK proving time and 10 ms for encryption, with the CRS size of 16 MB.


以下是中文翻译：

在基于配对（pairing-based）的零知识简洁非交互式知识证明（zero-knowledge succinct non-interactive arguments of knowledge, zk-SNARK）中，常常需要将证明系统与加密机制相结合。一个典型例子是基于区块链的投票系统：该系统要求选票内容保密（通过加密实现），同时又能验证投票的有效性（通过 zk-SNARK 实现）。在这些组合应用场景中，一种常见解决方案是将加密算法的逻辑直接嵌入 zk-SNARK 电路中。然而，加密算法中复杂的密码学操作会显著增大电路规模，从而导致证明时间过长、公共参考串（Common Reference String, CRS）尺寸过大，难以在实际中部署。

本文提出了一种名为 SAVER（SNARK-friendly, Additively-homomorphic, and Verifiable Encryption and decryption with Rerandomization）的新方法，旨在将加密过程从 SNARK 电路中解耦。SAVER 中的加密方案具备多项实用特性：  
- **SNARK 友好性（SNARK-friendly）**：该加密方案可与现有基于配对的 SNARK 紧密结合，使得加密者在加密消息的同时，能够独立于 SNARK 电路证明预定义的属性；  
- **加法同态性（additively-homomorphic）**：密文继承了基于 ElGamal 加密的加法同态性质；  
- **可验证加密（verifiable encryption）**：通过与 SNARK 系统联动，可对加密消息的任意属性进行验证；  
- **可验证解密（verifiable decryption）**：即使不具备私钥的任何第三方，也能验证解密所得消息确实源自给定的密文；  
- **重随机化（rerandomization）**：证明和密文可作为独立对象进行重随机化，使得即便是加密者（或证明者）本人也无法追溯其原始来源。

作为代表性应用，我们基于 SAVER 构建了一个名为 Vote-SAVER 的新型投票系统，其中选民的私钥仅由其本人持有。Vote-SAVER 满足无收据性（receipt-freeness，蕴含选票隐私性）、个体可验证性（individual verifiability，蕴含不可否认性）、选票可验证性、计票唯一性以及选民匿名性。实验结果表明，在 Vote-SAVER 场景下，我们的 SAVER 方案实现的 zk-SNARK 证明时间为 0.7 秒，加密耗时为 10 毫秒，公共参考串（CRS）大小为 16 MB。


## 关键词

+ SAVER SNARK解耦可验证加密
+ zk-SNARK加法同态加密结合
+ 可验证解密重随机化密文
+ ElGamal同态加密SNARK友好
+ Vote-SAVER无收据选民匿名投票