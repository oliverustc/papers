---
title: "UC non-interactive, proactive, threshold ECDSA with identifiable aborts"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2020
created: 2025-04-17 09:51:35
modified: 2025-04-17 10:14:54
---

## UC non-interactive, proactive, threshold ECDSA with identifiable aborts

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3372297.3423367)

## 作者

+ [Ran Canetti](Ran%20Canetti.md)
+ Rosario Gennaro 
+ Steven Goldfeder 
+ Nikolaos Makriyannis 
+ Udi Peled 

## 笔记

Building on the Gennaro & Goldfeder and Lindell & Nof protocols (CCS '18), we present two threshold ECDSA protocols, for any number of signatories and any threshold, that improve as follows over the state of the art: -- For both protocols, only the last round requires knowledge of the message, and the other rounds can take place in a preprocessing stage, lending to a non-interactive threshold ECDSA protocol. -- Both protocols withstand adaptive corruption of signatories. Furthermore, they include a periodic refresh mechanism and offer full proactive security. -- Both protocols realize an ideal threshold signature functionality within the UC framework, in the global random oracle model, assuming Strong RSA, DDH, semantic security of the Paillier encryption, and a somewhat enhanced variant of existential unforgeability of ECDSA. -- Both protocols achieve accountability by identifying corrupted parties in case of failure to generate a valid signature. The two protocols are distinguished by the round-complexity and the identification process for detecting cheating parties. Namely: -- For the first protocol, signature generation takes only 4 rounds (down from the current state of the art of 8 rounds), but the identification process requires computation and communication that is quadratic in the number of parties. -- For the second protocol, the identification process requires computation and communication that is only linear in the number of parties, but signature generation takes 7 rounds. These properties (low latency, compatibility with cold-wallet architectures, proactive security, identifiable abort and composable security) make the two protocols ideal for threshold wallets for ECDSA-based cryptocurrencies.

以下是中文翻译：

基于Gennaro & Goldfeder和Lindell & Nof协议（CCS '18），我们提出了两种阈值ECDSA协议，适用于任意数量的签署者和任意阈值，并在以下方面改进了现有技术： 

-- 对于这两种协议，只有最后一轮需要知道消息，其余轮次可以在预处理阶段进行，从而形成一种非交互式的阈值ECDSA协议。 

-- 两种协议均能抵御自适应腐败签署者的攻击。此外，它们包含周期性刷新机制，并提供完全的主动安全性。 

-- 两种协议在UC框架内实现了理想的阈值签名功能，假设在全局随机预言机模型下，强RSA、离散对数假设（DDH）、Paillier加密的语义安全性以及ECDSA的存在性不可伪造性有一定增强变体。 

-- 两种协议通过在生成有效签名失败时识别被腐败方来实现问责制。两种协议的主要区别在于轮次复杂度和检测作弊方的识别过程。具体而言： 

-- 对于第一个协议，签名生成仅需4轮（较当前技术的8轮减少），但识别过程需要的计算和通信与参与方的数量呈平方关系。 

-- 对于第二个协议，识别过程所需的计算和通信仅与参与方的数量呈线性关系，但签名生成需要7轮。 

这些特性（低延迟、与冷钱包架构的兼容性、主动安全性、可识别的中止和可组合安全性）使得这两种协议非常适合基于ECDSA的加密货币的阈值钱包。

## 关键词

+ 阈值ECDSA
+ 主动安全
+ UC框架
+ 密钥共享
+ 多方计算