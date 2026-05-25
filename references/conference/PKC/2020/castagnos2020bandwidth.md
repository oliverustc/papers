---
title: "Bandwidth-efficient threshold EC-DSA"
标题简称:
论文类型: conference
会议简称: PKC
发表年份: 2020
created: 2025-04-28 17:08:15
modified: 2025-04-28 17:09:09
---

## Bandwidth-efficient threshold EC-DSA

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-030-45388-6_10)

## 作者

+ Guilhem Castagnos 
+ Dario Catalano 
+ Fabien Laguillaumie 
+ Federico Savasta 
+ Ida Tucker 

## 笔记

Threshold Signatures allow _n_ parties to share the power of issuing digital signatures so that any coalition of size at least t+1 can sign, whereas groups of _t_ or less players cannot. Over the last few years many schemes addressed the question of realizing efficient threshold variants for the specific case of EC-DSA signatures. In this paper we present new solutions to the problem that aim at reducing the overall bandwidth consumption. Our main contribution is a new variant of the Gennaro and Goldfeder protocol from ACM CCS 2018 that avoids all the required range proofs, while retaining provable security against malicious adversaries in the dishonest majority setting. Our experiments show that – for all levels of security – our signing protocol reduces the bandwidth consumption of best previously known secure protocols for factors varying between 4.4 and 9, while key generation is consistently two times less expensive. Furthermore compared to these same protocols, our signature generation is faster for 192-bits of security and beyond.

以下是中文翻译：

门限签名(Threshold Signatures)允许n个参与方共享发布数字签名的权力，使得任何规模至少为t+1的联盟都可以进行签名，而t个或更少的参与者则无法签名。在过去几年中，许多方案致力于实现EC-DSA签名(EC-DSA signatures)特定情况下的高效门限变体。在本文中，我们提出了该问题的新解决方案，旨在降低整体带宽消耗。我们的主要贡献是提出了Gennaro和Goldfeder在2018年ACM CCS会议上提出的协议的一个新变体，该变体避免了所有必需的范围证明(range proofs)，同时在不诚实多数设置下保持了对恶意对手的可证明安全性。我们的实验表明 - 在所有安全级别下 - 我们的签名协议将此前已知最佳安全协议的带宽消耗降低了4.4到9倍不等，而密钥生成的开销则始终降低了一半。此外，与这些相同的协议相比，我们的签名生成在192比特及更高的安全性水平下速度更快。

## 关键词

+ 门限EC-DSA
+ 带宽优化
+ 多方签名协议
+ 范围证明消除
+ 不诚实多数安全
+ 密钥生成协议