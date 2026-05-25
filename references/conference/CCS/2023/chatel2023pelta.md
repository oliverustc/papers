---
title: "Pelta-shielding multiparty-fhe against malicious adversaries"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2023
created: 2025-04-16 10:56:52
modified: 2025-04-16 10:57:18
---

## Pelta-shielding multiparty-fhe against malicious adversaries

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3576915.3623139)

## 作者

+ Sylvain Chatel 
+ Christian Mouchet 
+ Ali Utkan Sahin 
+ Apostolos Pyrgelis 
+ Carmela Troncoso 
+ [Jean-Pierre Hubaux](Jean-Pierre%20Hubaux.md)
## 笔记

Multiparty fully homomorphic encryption (MFHE) schemes enable multiple parties to efficiently compute functions on their sensitive data while retaining confidentiality. However, existing MFHE schemes guarantee data confidentiality and the correctness of the computation result only against honest-but-curious adversaries. In this work, we provide the first practical construction that enables the verification of MFHE operations in zero-knowledge, protecting MFHE from malicious adversaries. Our solution relies on a combination of lattice-based commitment schemes and proof systems which we adapt to support both modern FHE schemes and their implementation optimizations. We implement our construction in PELTA. Our experimental evaluation shows that PELTA is one to two orders of magnitude faster than existing techniques in the literature.  
以下是中文翻译：

多方全同态加密（MFHE）方案允许多方在保持数据机密性的同时，高效地对敏感数据进行函数计算。然而，现有的MFHE方案仅能确保数据保密性及计算结果正确性，以对抗诚实但好奇的敌手。本研究首次提出了一种实用构造方法，支持以零知识方式验证MFHE操作，从而保护MFHE免受恶意敌手攻击。我们的解决方案结合了基于格的承诺方案与证明系统，并对其进行了调整，以兼容现代FHE方案及其实现优化。我们在PELTA中实现了这一构造。实验评估表明，PELTA比文献中现有技术的速度快一到两个数量级。

## 关键词

+ 全同态加密
+ 零知识证明
+ 多方计算
+ 恶意安全
+ 隐私保护