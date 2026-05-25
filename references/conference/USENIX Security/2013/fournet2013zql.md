---
title: "ZQL: A Compiler for Privacy-Preserving Data Processing"
标题简称:
论文类型: conference
会议简称: USENIX Security
发表年份: 2013
---

## ZQL: A Compiler for Privacy-Preserving Data Processing

## 发表信息

+ [原文链接](https://www.usenix.org/conference/usenixsecurity13/technical-sessions/presentation/fournet)

## 作者

+ Cédric Fournet 
+ [Markulf Kohlweiss](Markulf%20Kohlweiss.md) 
+ George Danezis 
+ Zhengqin Luo 


## 笔记

ZQL is a query language for expressing simple computations on private data. Its compiler produces code to certify data, perform client-side computations, and verify the correctness of their results. Under the hood, it synthesizes zero-knowledge protocols that guarantee both integrity of the query results and privacy for all other data.

We present the ZQL language, its compilation scheme down to concrete cryptography, and the security guarantees it provides. We report on a prototype compiler that produces F# and C++. We evaluate its performance on queries for smart-meter billing, for pay-as-you-drive insurance policies, and for location-based services.

以下是中文翻译：

ZQL是一种用于表达私有数据上简单计算的查询语言。其编译器生成用于认证数据、执行客户端计算并验证其结果正确性的代码。在底层，它综合了零知识协议，既保证查询结果的完整性，又保护所有其他数据的隐私。

我们介绍了ZQL语言、其编译方案以及所提供的安全保障，并报告了一个生成F#和C++代码的原型编译器。我们在智能电表计费、按用量计费的车险保单以及基于位置的服务等查询场景下对其性能进行了评估。

## 关键词

+ ZQL隐私保护查询语言
+ 零知识协议编译器
+ 私有数据计算认证
+ 查询结果完整性保护
+ 客户端安全计算
+ 隐私保护数据处理

