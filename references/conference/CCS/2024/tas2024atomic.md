---
title: "Atomic and fair data exchange via blockchain"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2024
---

## Atomic and fair data exchange via blockchain

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3658644.3690248)

## 作者

+ Ertem Nusret Tas 
+ István András Seres 
+ [Yinuo Zhang](Yinuo%20Zhang.md)
+ Márk Melczer 
+ Mahimna Kelkar 
+ [Joseph Bonneau](Joseph%20Bonneau.md) 
+ Valeria Nikolaenko 


## 笔记

We introduce a blockchain Fair Data Exchange (FDE) protocol, enabling a storage server to transfer a data file to a client atomically: the client receives the file if and only if the server receives an agreed-upon payment. We put forth a new definition for a cryptographic scheme that we name verifiable encryption under committed key (VECK), and we propose two instantiations for this scheme. Our protocol relies on a blockchain to enforce the atomicity of the exchange and uses VECK to ensure that the client receives the correct data (matching an agreed-upon commitment) before releasing the payment for the decrypting key. Our protocol is trust-minimized and requires only constant-sized on-chain communication, concretely 3 signatures, 1 verification key, and 1 secret key, with most of the data stored and communicated off-chain. It also supports exchanging only a subset of the data, can amortize the server's work across multiple clients, and offers a general framework to design alternative FDE protocols using different commitment schemes. A prominent application of our protocol is the Danksharding data availability scheme on Ethereum, which commits to data via KZG polynomial commitments. We also provide an open-source implementation for our protocol with both instantiations for VECK, demonstrating our protocol's efficiency and practicality on Ethereum.

以下是中文翻译：

我们提出一种基于区块链的公平数据交换（Fair Data Exchange, FDE）协议，使存储服务器能够以原子性方式将数据文件传输给客户端：当且仅当服务器收到双方约定的付款时，客户端才会获得该文件。我们提出了一种新型密码学方案的定义，称之为“承诺密钥下的可验证加密”（Verifiable Encryption under Committed Key, VECK），并给出了该方案的两种具体实现。

本协议利用区块链强制执行交换的原子性，并采用 VECK 机制，确保客户端在释放用于解密密钥的付款之前，已收到与事先约定承诺（commitment）相匹配的正确数据。该协议具有最小化信任（trust-minimized）特性，且仅需常数大小的链上通信量——具体而言，仅需 3 个签名、1 个验证密钥和 1 个秘密密钥，其余大部分数据均在链下存储与传输。此外，本协议支持仅交换数据子集、可在多个客户端之间分摊服务器的计算开销，并提供了一个通用框架，允许使用不同的承诺方案（commitment schemes）设计替代性的 FDE 协议。

本协议的一个突出应用场景是以太坊（Ethereum）中的 Danksharding 数据可用性方案，该方案通过 KZG 多项式承诺（KZG polynomial commitments）对数据进行承诺。我们还提供了本协议的开源实现，包含 VECK 的两种实例化方案，并在以太坊上验证了协议的高效性与实用性。

## 关键词

+ 公平数据交换
+ 可验证加密
+ 区块链原子交换
+ 数据可用性
+ KZG多项式承诺

