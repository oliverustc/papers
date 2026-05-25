---
title: "Multi-Signature and Game Based Blockchain Interoperability Oracle"
标题简称:
论文类型: journal
期刊简称: TDSC
发表年份: 2025
created: 2025-04-17 10:56:06
modified: 2025-04-17 10:56:36
---

## Multi-Signature and Game Based Blockchain Interoperability Oracle

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/10887331)

## 作者

+ Zhiwei Wang 
+ Siuming Yiu 
+ Longwen Lan 

## 笔记

To solve the problem of blockchain interoperability, we propose an efficient decentralization oracle solution. We design a subgroup Schnorr multisignature for the offchain aggregation mechanism of our system, which is proven to be secure and robust. Compared with threshold signaturebased schemes, the subgroup multisignature-based scheme does not require the execution of the distributed key generation protocol, which greatly reduces off-chain costs. The on-chain verification of the Schnorr signature is also more efficient than the pairing-based signatures. Then, we design a fair incentive mechanism to encourage the oracle nodes to work hard to validate the external data, which is based on a repeated dynamic game. Compared with the existing incentive mechanisms, our mechanism considers the real actions of each node to determine whether it should be rewarded or penalized. We implement our system over the Ethereum blockchain, and the experiments show its good performance.

以下是中文翻译：

为了解决区块链互操作性的问题，我们提出了一种高效的去中心化预言机解决方案。我们为系统的链下聚合机制设计了一种子群Schnorr多重签名（subgroup Schnorr multisignature），该机制被证明是安全且稳健的。与基于门限签名（threshold signature）方案相比，基于子群多重签名的方案不需要执行分布式密钥生成协议，这大大降低了链下成本。Schnorr签名的链上验证效率也优于基于配对的签名。接着，我们设计了一种公平激励机制，以鼓励预言机节点努力验证外部数据，该机制基于重复动态博弈（repeated dynamic game）。与现有的激励机制相比，我们的机制考虑了每个节点的实际行为，以决定其是否应获得奖励或处罚。我们在以太坊区块链上实现了我们的系统，实验结果显示其性能良好。

## 关键词

+ 区块链互操作性预言机
+ 子群Schnorr多重签名
+ 重复动态博弈激励机制
+ 去中心化链下聚合
+ 预言机节点公平激励
+ 以太坊智能合约验证