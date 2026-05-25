---
title: "Fairness in an unfair world: Fair multiparty computation from public bulletin boards"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2017
created: 2025-04-29 10:33:21
modified: 2025-04-29 10:34:47
---

## Fairness in an unfair world: Fair multiparty computation from public bulletin boards

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3133956.3134092)

## 作者

+ [Arka Rai Choudhuri](Arka%20Rai%20Choudhuri.md)
+ [Matthew Green](Matthew%20Green.md)
+ [Abhishek Jain](Abhishek%20Jain.md)
+ Gabriel Kaptchuk 
+ [Ian Miers](Ian%20Miers.md)
## 笔记

Secure multiparty computation allows mutually distrusting parties to compute a function on their private inputs such that nothing but the function output is revealed. Achieving fairness --- that all parties learn the output or no one does -- is a long studied problem with known impossibility results in the standard model if a majority of parties are dishonest. We present a new model for achieving fairness in MPC against dishonest majority by using public bulletin boards implemented via existing infrastructure such as blockchains or Google's certificate transparency logs. We present both theoretical and practical constructions using either witness encryption or trusted hardware (such as Intel SGX). Unlike previous works that either penalize an aborting party or achieve weaker notions such as $\Delta$-fairness, we achieve complete fairness using existing infrastructure.

以下是中文翻译：

安全多方计算（Secure multiparty computation）允许互不信任的各方基于各自的私有输入计算某个函数，且除了函数输出结果外不泄露任何其他信息。实现公平性——即所有参与方要么都获得输出结果，要么都得不到结果——是一个长期研究的问题。在标准模型下，如果大多数参与方都不诚实，已知存在不可能性结果。我们提出了一个新模型，通过使用基于现有基础设施（如区块链或谷歌证书透明度日志）实现的公共公告板（public bulletin boards），在不诚实多数情况下实现多方计算中的公平性。我们提出了基于见证加密（witness encryption）或可信硬件（如英特尔SGX）的理论和实践构造方案。与之前的工作不同，我们既不需要惩罚中止的参与方，也不需要实现诸如$\Delta$-公平性等较弱的概念，而是能够利用现有基础设施实现完全公平性。

## 关键词

+ 公平多方计算
+ 见证加密
+ 可信硬件
+ 公告板
+ 区块链