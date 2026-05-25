---
title: "JEDI: Many-to-Many End-to-End encryption and key delegation for IoT"
标题简称:
论文类型: conference
会议简称: USENIX Security
发表年份: 2019
created: 2025-04-27 08:56:31
modified: 2025-04-27 09:20:23
---

## JEDI: Many-to-Many End-to-End encryption and key delegation for IoT

## 发表信息

+ [原文链接](https://www.usenix.org/conference/usenixsecurity19/presentation/kumar-sam)

## 作者

+ Sam Kumar 
+ [Yuncong Hu](Yuncong%20Hu.md) 
+ Michael P Andersen 
+ [Raluca Ada Popa](Raluca%20Ada%20Popa.md)
+ David E Culler 

## 笔记

As the Internet of Things (IoT) emerges over the next decade, developing secure communication for IoT devices is of paramount importance. Achieving end-to-end encryption for large-scale IoT systems, like smart buildings or smart cities, is challenging because multiple principals typically interact _indirectly_ via intermediaries, meaning that the recipient of a message is not known in advance. This paper proposes JEDI (**J**oining **E**ncryption and **D**elegation for **I**oT), a many-to-many end-to-end encryption protocol for IoT. JEDI encrypts and signs messages end-to-end, while conforming to the decoupled communication model typical of IoT systems. JEDI's keys support expiry and fine-grained access to data, common in IoT. Furthermore, JEDI allows principals to delegate their keys, restricted in expiry or scope, to other principals, thereby granting access to data and managing access control in a scalable, distributed way. Through careful protocol design and implementation, JEDI can run across the spectrum of IoT devices, including ultra low-power deeply embedded sensors severely constrained in CPU, memory, and energy consumption. We apply JEDI to an existing IoT messaging system and demonstrate that its overhead is modest.

以下是中文翻译：

随着物联网(Internet of Things, IoT)在未来十年的发展，为物联网设备开发安全通信变得尤为重要。为大规模物联网系统（如智能建筑或智能城市）实现端到端加密具有挑战性，因为多个主体通常通过中介间接交互，这意味着消息接收者无法提前确定。本文提出了JEDI（连接加密与授权的物联网协议，Joining Encryption and Delegation for IoT），这是一个面向物联网的多对多端到端加密协议。JEDI对消息进行端到端加密和签名，同时符合物联网系统典型的解耦通信模型。JEDI的密钥支持过期机制和细粒度的数据访问控制，这些特性在物联网中很常见。此外，JEDI允许主体将其密钥（受限于过期时间或使用范围）委托给其他主体，从而以可扩展、分布式的方式实现数据访问授权和访问控制管理。通过精心的协议设计和实现，JEDI可以在各类物联网设备上运行，包括在CPU、内存和能耗方面受到严格限制的超低功耗深度嵌入式传感器。我们将JEDI应用于现有的物联网消息系统，并证明其开销适中。

## 关键词

+ 物联网端到端加密JEDI
+ 多对多加密协议
+ 密钥委托访问控制
+ 解耦通信IoT模型
+ 细粒度数据访问
+ 嵌入式设备安全通信
