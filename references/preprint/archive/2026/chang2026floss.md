---
title: "FLOSS: Fast Linear Online Secret-Shared Shuffling"
标题简称:
论文类型: preprint
预印本简称: archive
发表年份: 2026
---

## FLOSS: Fast Linear Online Secret-Shared Shuffling

## 发表信息

+ [原文链接](https://eprint.iacr.org/2026/672)

## 作者

+ Ian Chang
+ Sela Navot
+ [Alex Ozdemir](Alex Ozdemir.md)
+ [Nirvan Tyagi](Nirvan Tyagi.md)

## 笔记

Randomly permuting secret data vectors is a core building block in many privacy-preserving protocols, including those for analytics, advertising, and communication. Existing approaches either rely on computation-heavy public key cryptography and zero-knowledge proofs or scale poorly for large vectors due to use of a quasilinear-sized permutation network. This work presents a preprocessing approach to enable fast linear-time online shuffles in the malicious-secure two-party computation (2PC) setting. We propose FLOSS, a 2PC protocol for securely computing any interactive arithmetic permutation circuit, a notion we introduce to capture how higher level protocols are built on secret-shared field arithmetic and permutations. We show how secret-shared sorting (a subprotocol in data analytics) can be described as an arithmetic permutation circuit, and can thus be compiled to an efficient online 2PC protocol using FLOSS. Our implementation and evaluation confirm FLOSS performs online shuffles fast: shuffling $2^{20}$ elements in under 500ms, greater than $800\times$ faster than state-of-the-art alternatives.

以下是中文翻译：

对秘密数据向量进行随机置换是许多隐私保护协议的核心构建模块，包括用于分析、广告和通信的协议。现有方法要么依赖计算开销较大的公钥密码学和零知识证明，要么因使用准线性规模的置换网络而难以扩展到大型向量。本研究提出了一种预处理方法，在恶意安全的双方计算（2PC）环境中实现快速线性时间在线洗牌。我们提出FLOSS，一种用于安全计算任意交互式算术置换电路的2PC协议——这一概念由我们引入，用于捕捉高层协议如何基于秘密共享域运算和置换构建。我们展示了秘密共享排序（数据分析中的子协议）如何被描述为算术置换电路，从而可以使用FLOSS编译为高效的在线2PC协议。我们的实现和评估证实了FLOSS的在线洗牌速度：在不到500毫秒内洗牌$2^{20}$个元素，比现有最先进方案快800倍以上。

## 关键词

+ FLOSS线性时间在线秘密共享洗牌
+ 恶意安全双方计算2PC洗牌协议
+ 算术置换电路秘密共享置换
+ 预处理方法快速在线洗牌
+ 隐私保护分析广告通信协议
