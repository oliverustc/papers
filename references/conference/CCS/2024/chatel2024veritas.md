---
title: "Veritas: Plaintext encoders for practical verifiable homomorphic encryption"
doi: 10.1145/3658644.3670282
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2024
---
## Veritas: Plaintext encoders for practical verifiable homomorphic encryption

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3658644.3670282)

## 作者

+ Sylvain Chatel 
+ Christian Knabenhans 
+ Apostolos Pyrgelis 
+ Carmela Troncoso 
+ [Jean-Pierre Hubaux](Jean-Pierre%20Hubaux.md)
## 笔记

Homomorphic encryption has become a practical solution for protecting the privacy of computations on sensitive data. However, existing homomorphic encryption pipelines do not guarantee the correctness of the computation result in the presence of a malicious adversary. We propose two plaintext encodings compatible with state-of-the-art fully homomorphic encryption schemes that enable practical client-verification of homomorphic computations while supporting all the operations required for modern privacy-preserving analytics. Based on these encodings, we introduce VERITAS, a ready-to-use library for the verification of computations executed over encrypted data. VERITAS is the first library that supports the verification of any homomorphic operation. We demonstrate its practicality for various applications and, in particular, we show that it enables verifiability of homomorphic analytics with less than 3 x computation overhead compared to the homomorphic encryption baseline.

以下是中文翻译：

同态加密（Homomorphic encryption）已成为保护敏感数据计算隐私的实用解决方案。然而，现有的同态加密流程无法在存在恶意对手的情况下保证计算结果的正确性。我们提出了两种与最先进全同态加密方案兼容的明文编码方法，能够在支持现代隐私保护分析所需全部操作的同时，实现实用的客户端可验证同态计算。基于这些编码方法，我们推出了 VERITAS——一个可直接用于验证密文计算结果的即用型函数库。VERITAS 是首个支持验证任意同态操作的函数库。我们通过多个应用场景验证了其实际可行性，特别证明了相较于同态加密基准方案，该库可实现计算开销低于 3 倍的可验证同态分析。

## 关键词

+ 可验证同态计算
+ 明文编码
+ 同态加密
+ 计算正确性
+ 隐私保护分析
