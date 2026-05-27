---
title: "Groundhog: A Restart-based Systems Framework for Increasing Availability in Threshold Cryptosystems"
doi: 10.1109/sp61157.2025.00056
标题简称:
论文类型: conference
会议简称: S&P
发表年份: 2025
modified: 2025-04-13 14:40:16
---
## Groundhog: A Restart-based Systems Framework for Increasing Availability in Threshold Cryptosystems

## 发表信息

+ [原文链接暂无]
+ [pdf](https://sibin.github.io/papers/2025_IEEE_S&P_GroundHog_Ashish.pdf)

## 作者

+ Ashish Kashinath 
+ Disha Agarwala 
+ Gabriel Kulp 
+ [Sourav Das](Sourav%20Das.md)
+ Sibin Mohan 
+ Radha Venkatagiri 

## 笔记

Threshold cryptosystems (TCs), developed to eliminate single points of failure in applications such as key management-as-a-service, signature schemes, encrypted data storage and even blockchain applications, rely on the assumption that an adversary does not corrupt more than a fixed number of nodes in a network. This assumption, once broken, can lead to the entire system being compromised. In this paper, we present a systems-level solution, viz., a reboot-based framework, Groundhog, that adds a layer of resiliency on top of threshold cryptosystems (as well as others); our framework ensures the system can be protected against malicious (mobile) adversaries that can corrupt up all but one device in the network. Groundhog ensures that a sufficient number of honest devices is always available to ensure the availability of the entire system. Our framework is general- izable to multiple threshold cryptosystems — we demonstrate this by integrating it with two well-known TC protocols — the Distributed Symmetric key Encryption system (DiSE) and the Boneh, Lynn and Shacham Distributed Signatures (BLS) system. In fact, Groundhog may have applicability in sys- tems beyond those based on threshold cryptography — we demonstrate this on a simpler cryptographic protocol that we developed named PassAround. We developed a (generalizable) container-based framework that can be used to combine Groundhog (and its guarantees) with cryptographic protocols and evaluated our system using, (a) case studies of real world attacks as well as (b) extensive measurements by implementing the aforementioned DiSE, BLS and PassAround protocols on Groundhog. We show that Groundhog is able to guarantee high availability with minimal overheads (less than 7%) . In some instances, Groundhog actually improves the performance of the TC schemes!

以下是中文翻译：

阈值密码系统（TCs）旨在消除密钥管理即服务、签名方案、加密数据存储乃至区块链应用中的单点故障，其安全性基于一个假设：攻击者无法攻陷网络中超过预设数量的节点。一旦这一假设被打破，整个系统便可能沦陷。本文提出了一种系统级解决方案——基于重启的框架Groundhog，为阈值密码系统（及其他类似系统）额外增添了一层韧性保障。该框架确保系统能够抵御恶意（移动）攻击者，即使网络中仅剩一台设备未被攻陷，系统仍可得到保护。Groundhog通过持续维持足够数量的可信设备，保障整个系统的可用性。 本框架具有广泛适用性，我们通过将其与两个经典TC协议——分布式对称密钥加密系统（DiSE）和Boneh-Lynn-Shacham分布式签名系统（BLS）集成验证了这一点。实际上，Groundhog的适用范围可能超越阈值密码系统——我们通过自研的简易加密协议PassAround也验证了其通用性。我们开发了可通用的容器化框架，能将Groundhog（及其保障机制）与各类密码协议结合，并通过以下方式评估系统性能：(a) 真实攻击案例研究；(b) 在Groundhog上实现DiSE、BLS和PassAround协议进行大规模实测。结果表明，Groundhog能以极低开销（低于7%）确保高可用性，某些情况下甚至能提升TC方案的性能表现。

## 关键词

+ 阈值密码系统可用性
+ 基于重启的框架
+ 移动对手防护
+ 分布式对称密钥加密DiSE
+ BLS分布式签名
+ 容器化密码框架