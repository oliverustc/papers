---
title: "EVOKE: Efficient Revocation of Verifiable Credentials in IoT Networks"
标题简称:
论文类型: conference
会议简称: USENIX Security
发表年份: 2024
---

## EVOKE: Efficient Revocation of Verifiable Credentials in IoT Networks

## 发表信息

+ [原文链接](https://www.usenix.org/conference/usenixsecurity24/presentation/mazzocca)

## 作者

+ Carlo Mazzocca 
+ Abbas Acar 
+ Selcuk Uluagac 
+ Rebecca Montanari 


## 笔记

The lack of trust is one of the major factors that hinder collaboration among Internet of Things (IoT) devices and harness the usage of the vast amount of data generated. Traditional methods rely on Public Key Infrastructure (PKI), managed by centralized certification authorities (CAs), which suffer from scalability issues, single points of failure, and limited interoperability. To address these concerns, Decentralized Identifiers (DIDs) and Verifiable Credentials (VCs) have been proposed by the World Wide Web Consortium (W3C) and the European Union as viable solutions for promoting decentralization and "electronic IDentification, Authentication, and trust Services" (eIDAS). Nevertheless, at the state-of-the-art, there are no efficient revocation mechanisms for VCs specifically tailored for IoT devices, which are characterized by limited connectivity, storage, and computational power.

This paper presents EVOKE, an efficient revocation mechanism of VCs in IoT networks. EVOKE leverages an ECC-based accumulator to manage VCs with minimal computing and storage overhead while offering additional features like mass and offline revocation. We designed, implemented, and evaluated a prototype of EVOKE across various deployment scenarios. Our experiments on commodity IoT devices demonstrate that each device only requires minimal storage (i.e., approximately 1.5 KB) to maintain verification information, and most notably half the storage required by the most efficient PKI certificates. Moreover, our experiments on hybrid networks, representing typical IoT protocols (e.g., Zigbee), also show minimal latency in the order of milliseconds. Finally, our large-scale analysis demonstrates that even when 50% of devices missed updates, approximately 96% of devices in the entire network were updated within the first hour, proving the scalability of EVOKE in offline updates.

以下是中文翻译：

缺乏信任是阻碍物联网（IoT）设备协作和充分利用大量生成数据的主要因素之一。传统方法依赖于由集中式认证机构（CAs）管理的公钥基础设施（PKI），这导致了可扩展性问题、单点故障和有限的互操作性。为了解决这些问题，万维网联盟（W3C）和欧盟提出了去中心化标识符（DIDs）和可验证凭证（VCs），作为促进去中心化和“电子身份识别、认证和信任服务”（eIDAS）的可行解决方案。然而，目前尚无专门为物联网设备量身定制的高效VC撤销机制，而物联网设备的特点是连接性、存储和计算能力有限。

本文介绍了EVOKE，一种在物联网网络中高效的VC撤销机制。EVOKE利用基于椭圆曲线密码学（ECC）的累加器，以最小的计算和存储开销管理VC，同时提供批量撤销和离线撤销等附加功能。我们设计、实现并评估了EVOKE的原型，涵盖了多种部署场景。我们在普通物联网设备上的实验表明，每个设备仅需约1.5 KB的最小存储空间来维护验证信息，显著低于最有效的PKI证书所需的存储空间。此外，我们在混合网络（代表典型的物联网协议，如Zigbee）上的实验也显示了毫秒级的最小延迟。最后，我们的大规模分析表明，即使有50%的设备错过了更新，整个网络中约96%的设备在第一个小时内仍得到了更新，证明了EVOKE在离线更新中的可扩展性。

## 关键词

+ EVOKE物联网可验证凭证撤销
+ ECC累加器轻量级VC管理
+ 去中心化身份DID可验证凭证
+ 离线批量撤销机制
+ IoT设备低存储认证
+ eIDAS数字身份信任服务
