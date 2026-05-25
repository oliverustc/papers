---
title: "Efficient Batch Threshold Encryption Using Partial Fraction Techniques"
标题简称:
论文类型: preprint
预印本简称: archive
发表年份: 2026
---

## Efficient Batch Threshold Encryption Using Partial Fraction Techniques

## 发表信息

+ [原文链接](https://eprint.iacr.org/2026/674)

## 作者

+ [Dan Boneh](Dan Boneh.md)
+ Rohit Nema
+ [Arnab Roy](Arnab%20Roy.md)
+ Ertem Nusret Tas

## 笔记

Batch encryption enables a holder of the secret key to publish a succinct pre-decryption key for a set of ciphertexts, such that exactly that set can be decrypted while other ciphertexts remain secret. Existing constructions either rely on epochs or, when epochless, suffer from large public parameters (quadratic in the batch size) and are vulnerable to censorship. In this work, we present an epochless, censorship-resistant batch encryption scheme with linear-sized public parameters, constant-sized pre-decryption keys and ciphertexts, and efficient batch decryption. Our construction extends the partial fraction techniques of Jutla, Nema, and Roy's threshold encryption scheme: we exploit partial fraction decomposition such that publishing a single group element as the pre-decryption key lets the decryptor decrypt all ciphertexts in the batch. We prove CCA security of our scheme, and show how to thresholdize it. Our results directly benefit applications such as encrypted mempools for MEV mitigation and time-lock encrypted storage.

以下是中文翻译：

批量加密使密钥持有者能够为一组密文发布简洁的预解密密钥，使得该组密文可被精确解密，而其他密文保持保密。现有构造要么依赖于纪元（epoch），要么在无纪元设计中面临公共参数过大（与批次大小呈二次方关系）以及易受审查攻击等问题。在本研究中，我们提出了一种无纪元、抗审查的批量加密方案，具有线性大小的公共参数、常数大小的预解密密钥和密文，以及高效的批量解密。我们的构造扩展了Jutla、Nema和Roy阈值加密方案中的部分分式技术：通过利用部分分式分解，发布单个群元素作为预解密密钥，使解密者能够解密批次中的所有密文。我们证明了方案的CCA安全性，并展示了如何将其门限化。我们的结果直接应用于加密内存池（用于MEV缓解）和时间锁加密存储等场景。

## 关键词

+ 批量加密无纪元抗审查方案
+ 部分分式分解预解密密钥批量解密
+ CCA安全门限批量加密
+ 加密内存池MEV缓解应用
+ 线性公共参数常数密文大小
