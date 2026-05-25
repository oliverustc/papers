---
title: "Trustboost: Boosting trust among interoperable blockchains"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2023
created: 2025-04-19 11:03:07
modified: 2025-04-19 11:06:47
---

## Trustboost: Boosting trust among interoperable blockchains

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3576915.3623080)

## 作者

+ Peiyao Sheng 
+ Xuechao Wang 
+ Sreeram Kannan 
+ Kartik Nayak 
+ Pramod Viswanath 

## 笔记

Currently there exist many blockchains with weak trust guarantees, limiting applications and participation. Existing solutions to boost the trust using a stronger blockchain, e.g., via checkpointing, requires the weaker blockchain to give up sovereignty. In this paper, we propose a family of protocols in which multiple blockchains interact to create a combined ledger with boosted trust. We show that even if several of the interacting blockchains cease to provide security guarantees, the combined ledger continues to be secure - our Trustboost protocols achieve the optimal threshold of tolerating the insecure blockchains. This optimality, along with the necessity of blockchain interactions, is formally shown within the classic shared memory model, tackling the long standing open challenge of solving consensus in the presence of both Byzantine objects and processes. Furthermore, our proposed construction of Trustboost simply operates via smart contracts and require no change to the underlying consensus protocols of the participating blockchains, a form of "consensus on top of consensus''. The protocols are lightweight and can be used on specific (e.g., high value) transactions; we demonstrate the practicality by implementing and deploying Trustboost as cross-chain smart contracts in the Cosmos ecosystem using approximately 3,000 lines of Rust code, made available as open source [52]. Our evaluation shows that using 10 Cosmos chains in a local testnet, Trustboost has a gas cost of roughly $2 with a latency of 2 minutes per request, which is in line with the cost on a high security chain such as Bitcoin or Ethereum.

以下是中文翻译：

目前，许多区块链存在信任保障不足的问题，这限制了应用和参与。现有的通过更强大的区块链（例如，通过检查点机制）来增强信任的解决方案，要求较弱的区块链放弃主权。在本文中，我们提出了一系列协议，使多个区块链相互作用，创建一个增强信任的联合账本。我们证明，即使几个交互的区块链停止提供安全保障，联合账本仍然是安全的——我们的Trustboost协议达到了容忍不安全区块链的最优阈值。这一最优性以及区块链交互的必要性在经典共享内存模型中得到了正式证明，解决了在存在拜占庭对象和进程的情况下达成共识这一长期未解的挑战。此外，我们提出的Trustboost构造通过智能合约简单操作，无需更改参与区块链的底层共识协议，形成一种“共识之上的共识”。这些协议轻量级，可用于特定（例如，高价值）交易；我们通过在Cosmos生态系统中实现和部署Trustboost作为跨链智能合约，使用大约3000行Rust代码，展示了其实用性，并以开源形式提供[52]。我们的评估显示，在本地测试网中使用10条Cosmos链时，Trustboost的燃气费用大约为2美元，每个请求的延迟为2分钟，这与比特币或以太坊等高安全性链上的费用相符。

## 关键词

+ 区块链互操作性
+ 跨链协议
+ 共识机制
+ 信任增强
+ 智能合约
+ 拜占庭容错