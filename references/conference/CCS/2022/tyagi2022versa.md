---
title: "VeRSA: Verifiable registries with efficient client audits from RSA authenticated dictionaries"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2022
created: 2025-04-21 11:14:58
modified: 2025-04-21 11:15:27
---

## VeRSA: Verifiable registries with efficient client audits from RSA authenticated dictionaries

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3548606.3560605)
+ [code](https://github.com/nirvantyagi/versa)

## 作者

+ [[Nirvan Tyagi]] 
+ [Ben Fisch](Ben%20Fisch.md)
+ Andrew Zitek 
+ [[Joseph Bonneau]] 
+ Stefano Tessaro 

## 笔记

Verifiable registries allow clients to securely access a key-value mapping maintained by an untrusted server. Registries must be audited to ensure global invariants are preserved, which, in turn, allows for efficient monitoring of individual registry entries by their owners. To this end, existing proposals either assume trusted third-party auditors or rely on incrementally verifiable computation (IVC) via expensive recursive SNARKs to make registries client-auditable.  

In this work, we give new client-auditable verifiable registries with throughputs up to 100 x greater than baseline IVC solutions. Our approach relies on an authenticated dictionary based on RSA accumulators for which we develop a new constant-size invariant proof. We use this as a replacement for Merkle trees to optimize the baseline IVC approach, but also provide a novel construction which dispenses with SNARKs entirely. This latter solution adopts a new checkpointing method to ensure client view consistency.

可验证注册表允许客户端安全地访问由不可信服务器维护的键值映射。注册表必须经过审计，以确保全局不变性得以保持，这反过来又允许注册表的所有者对各个注册条目进行高效监控。为此，现有方案要么假设存在可信的第三方审计员，要么依赖于通过昂贵的递归 SNARK（可缩放非交互式零知识证明）进行增量可验证计算（IVC）来使注册表可供客户端审计。

以下是中文翻译：

在本工作中，我们提出了新的客户端可审计可验证注册表，其吞吐量比基线 IVC 解决方案高出多达 100 倍。我们的方法依赖于基于 RSA 累加器的认证字典，并为其开发了一种新的常量大小的不变性证明。我们将其用作 Merkle 树的替代方案，以优化基线 IVC 方法，并提供了一种全新的构造，完全不依赖于 SNARK。这后一种解决方案采用了一种新的检查点方法，以确保客户端视图的一致性。

## 关键词

+ 可验证注册表
+ RSA累加器
+ 可审计
+ 认证字典
+ 区块链