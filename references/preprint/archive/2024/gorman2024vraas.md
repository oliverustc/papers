---
title: "VRaaS: Verifiable Randomness as a Service on Blockchains"
标题简称:
论文类型: preprint
预印本简称: archive
发表年份: 2024
created: 2025-05-09 14:29:54
modified: 2025-05-09 14:33:59
---

## VRaaS: Verifiable Randomness as a Service on Blockchains

## 发表信息

+ [原文链接](https://eprint.iacr.org/2024/957)

## 作者

+ Jacob Gorman
+ [Lucjan Hanzlik](Lucjan%20Hanzlik.md)
+ [Aniket Kate](Aniket%20Kate.md)
+ Easwar Vivek Mangipudi
+ [Pratyay Mukherjee](Pratyay%20Mukherjee.md)
+ Pratik Sarkar
+ Sri AravindaKrishnan Thyagarajan

## 笔记

Web3 applications, such as on-chain games, NFT minting, and leader elections necessitate access to unbiased, unpredictable, and publicly verifiable randomness. Despite its broad use cases and huge demand, there is a notable absence of comprehensive treatments of on-chain verifiable randomness services. To bridge this, we offer an extensive formal analysis of on-chain verifiable randomness services. We present the first formalization of on-chain verifiable randomness in the blockchain setting by introducing the notion of Verifiable Randomness as a Service (VRaaS). We formally define VRaaS using an ideal functionality $F_{VRaaS}$ in the Universal Composability model. Our definition not only captures the core features of randomness services, such as unbiasability, unpredictability, and public verifiability, but also accounts for many other crucial nuances pertaining to different entities involved, such as smart contracts. Within our framework we study a generic design of Verifiable Random Function (VRF)-based randomness service - where the randomness requester provides an input on which the randomness is evaluated as VRF output. We show that it does satisfy our formal VRaaS definition. Furthermore, we show that the generic protocol captures many real-world randomness services like Chainlink VRF and Supra dVRF. Moreover, we investigate the minimalism of the framework. Towards that, first we show that, the two transactions in-built in our framework are actually necessary for any randomness service to support the essential qualities. We also discover practical vulnerabilities in other designs such as Algorand beacon, Pyth VRF and Band VRF, captured within our framework.

**Note:** This is the full version containing the detailed security proofs.

以下是中文翻译：

Web3应用，如链上游戏、NFT铸造和领导者选举等，都需要访问无偏、不可预测且可公开验证的随机性。尽管其应用场景广泛且需求巨大，但目前缺乏对链上可验证随机性服务的全面研究。为了弥补这一空白，我们提供了对链上可验证随机性服务的深入形式化分析。我们通过引入可验证随机性即服务(Verifiable Randomness as a Service, VRaaS)的概念，首次在区块链环境下对链上可验证随机性进行了形式化定义。我们在通用可组合性(Universal Composability)模型中使用理想功能$F_{VRaaS}$正式定义了VRaaS。我们的定义不仅捕获了随机性服务的核心特征，如无偏性、不可预测性和公开可验证性，还考虑了与不同参与实体（如智能合约）相关的许多其他关键细节。在我们的框架内，我们研究了基于可验证随机函数(VRF)的随机性服务的通用设计——其中随机性请求者提供一个输入，随机性作为VRF输出在该输入上进行评估。我们证明它确实满足我们的形式化VRaaS定义。此外，我们表明该通用协议涵盖了许多现实世界的随机性服务，如Chainlink VRF和Supra dVRF。另外，我们还研究了该框架的最小化特性。为此，我们首先证明，我们框架中内置的两个交易对于任何随机性服务要支持基本特性来说都是必需的。我们还在我们的框架内发现了其他设计（如Algorand信标、Pyth VRF和Band VRF）中的实际漏洞。

**注：**这是包含详细安全性证明的完整版本。

## 关键词

+ VRaaS链上可验证随机性即服务
+ 通用可组合性VRF随机性形式化
+ 无偏不可预测公开可验证随机性
+ Chainlink dVRF区块链随机服务
+ Web3游戏NFT领导选举随机性
