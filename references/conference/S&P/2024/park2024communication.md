---
title: "Communication-efficient, Fault Tolerant PIR over Erasure Coded Storage"
doi: 10.1109/sp54263.2024.00168
标题简称:
论文类型: conference
会议简称: S&P
发表年份: 2024
created: 2025-04-27 09:33:20
modified: 2025-04-28 09:55:25
---
## Communication-efficient, Fault Tolerant PIR over Erasure Coded Storage

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/10646602)

## 作者

+ Andrew Park 
+ Trevor Leong 
+ Francisco Maturana 
+ [Wenting Zheng](Wenting%20Zheng.md)
+ KV Rashmi 

## 笔记

Private information retrieval (PIR) is a technique for a client to retrieve an item from a public database without revealing to an adversarial server the item that was queried. While multi-server PIR has been well-studied in order to obtain better communication and computation relative to single-server schemes, there are far fewer fault-tolerant PIR schemes which can remain functional even in the presence of malicious adversaries. In this paper, we present a solution that combines techniques from both the cryptography and information theory communities to design robust PIR protocols that obtain better computation, communication, and storage compared to prior state-of-the-art schemes. Our results show that our PIR protocols achieve up to 9.1× lower latency, at least 39.2× less total communication, and up to 7.3× less computation than the state-of-art robust PIR protocols for a database 4GB in size and can withstand two malicious servers, and continually outperform the robust PIR baselines for a variety of parameter configurations and failure scenarios.

以下是中文翻译：

私有信息检索(Private Information Retrieval, PIR)是一种使客户端能够从公共数据库中检索项目，同时不向对抗性服务器透露所查询项目的技术。虽然多服务器PIR已经得到充分研究，以获得相比单服务器方案更好的通信和计算效率，但能在恶意对手存在的情况下仍保持功能的容错PIR方案相对较少。在本文中，我们提出了一个结合密码学和信息论领域技术的解决方案，设计出与现有最先进方案相比在计算、通信和存储方面都更优的鲁棒PIR协议。我们的结果表明，对于4GB大小的数据库且能承受两个恶意服务器的情况下，我们的PIR协议相比现有最先进的鲁棒PIR协议实现了高达9.1倍的延迟降低，至少39.2倍的总通信量减少，以及高达7.3倍的计算量减少，并且在各种参数配置和故障场景下持续优于鲁棒PIR基准方案。

## 关键词

+ 私有信息检索PIR
+ 容错鲁棒PIR
+ 纠删码存储
+ 多服务器PIR协议
+ 通信效率优化
+ 信息论密码学结合