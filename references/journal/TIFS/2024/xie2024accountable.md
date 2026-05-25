---
title: "Accountable and secure threshold EdDSA signature and its applications"
标题简称:
论文类型: journal
期刊简称: TIFS
发表年份: 2024
created: 2025-04-17 10:52:00
modified: 2025-04-17 10:52:36
---

## Accountable and secure threshold EdDSA signature and its applications

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/10605124)

## 作者

+ Yumeng Xie 
+ Qing Fan 
+ Chuan Zhang 
+ Tong Wu 
+ Yuao Zhou 
+ Debiao He 
+ [Liehuang Zhu](Liehuang%20Zhu.md)
## 笔记

Threshold signatures as a method to realize multi-party cooperation and trust distribution in blockchain have been widely studied in recent years. However, among these researches, few threshold signature schemes achieve all the properties of accountability, privacy, and key protection for the EdDSA-based blockchain systems. To fill this gap, we propose an EdDSA-based accountable threshold signature protocol with privacy and proactive refresh, named TAPS-PR. Meanwhile, we define new security models and give a detailed analysis to prove protocol security. In TAPS-PR, the threshold is variable and hidden with the signing quorum from the public view. However, the signing quorum can be traced when threshold signatures related to fraudulent events are generated. We also enhance the key security of each signer by proactive refresh, which realizes updating the private key while the public key remains unchanged. Apart from that, we present ATS-PR with increased efficiency and reduced communication cost at the cost of weaker security. The theoretical analysis and experimental results indicate that our protocols perform efficiently in terms of communication and computation overhead. Furthermore, we use Tezos, a blockchain project employing EdDSA, as a case study to demonstrate the compatibility of our protocol with real-world blockchain applications.

以下是中文翻译：

阈值签名作为实现区块链中多方合作和信任分配的一种方法，近年来得到了广泛研究。然而，在这些研究中，很少有基于EdDSA（Edwards-curve Digital Signature Algorithm）的阈值签名方案能够实现问责性、隐私性和密钥保护的所有属性。为填补这一空白，我们提出了一种基于EdDSA的可问责阈值签名协议，具有隐私保护和主动刷新功能，命名为TAPS-PR。同时，我们定义了新的安全模型，并进行了详细分析以证明协议的安全性。在TAPS-PR中，阈值是可变的，并且与签名法定人数一起对公众视野隐藏。然而，当与欺诈事件相关的阈值签名被生成时，签名法定人数可以被追踪。我们还通过主动刷新增强了每个签名者的密钥安全性，实现了在公钥保持不变的情况下更新私钥。除此之外，我们还提出了ATS-PR，提升了效率并降低了通信成本，但以牺牲部分安全性为代价。理论分析和实验结果表明，我们的协议在通信和计算开销方面表现出高效性。此外，我们以Tezos（一个采用EdDSA的区块链项目）作为案例研究，以展示我们的协议与现实世界区块链应用的兼容性。

## 关键词

+ TAPS-PR可问责EdDSA阈值签名
+ 隐私保护与主动密钥刷新
+ 可变隐藏阈值签名法定人数
+ 欺诈事件签名者追踪
+ 区块链阈值签名协议
+ 多方信任分配Tezos应用