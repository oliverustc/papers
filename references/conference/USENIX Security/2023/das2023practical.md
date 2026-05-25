---
title: "Practical asynchronous high-threshold distributed key generation and distributed polynomial sampling"
标题简称:
论文类型: conference
会议简称: USENIX Security
发表年份: 2023
modified: 2025-04-13 16:44:05
---

## Practical asynchronous high-threshold distributed key generation and distributed polynomial sampling

## 发表信息

+ [原文链接](https://www.usenix.org/conference/usenixsecurity23/presentation/das)

## 作者

+ [Sourav Das](Sourav%20Das.md)
+ [Zhuolun Xiang](Zhuolun%20Xiang.md)
+ Lefteris Kokoris-Kogias 
+ [Ling Ren](Ling%20Ren.md)
## 笔记

Distributed Key Generation (DKG) is a technique to bootstrap threshold cryptosystems without a trusted party. DKG is an essential building block to many decentralized protocols such as randomness beacons, threshold signatures, Byzantine consensus, and multiparty computation. While significant progress has been made recently, existing asynchronous DKG constructions are inefficient when the reconstruction threshold is larger than one-third of the total nodes. In this paper, we present a simple and concretely efficient \emph{asynchronous} DKG (ADKG) protocol among _n_ = 3_t_ + 1 nodes that can tolerate up to _t_ malicious nodes and support any reconstruction threshold _ℓ_ ≥ _t_. Our protocol has an expected _O_(κn3) communication cost, where κ is the security parameter, and only assumes the hardness of the Discrete Logarithm. The core ingredient of our ADKG protocol is an asynchronous protocol to secret share a random polynomial of degree _ℓ_ ≥ _t_, which has other applications, such as asynchronous proactive secret sharing and asynchronous multiparty computation. We implement our high-threshold ADKG protocol and evaluate it using a network of up to 128 geographically distributed nodes. Our evaluation shows that our high-threshold ADKG protocol reduces the running time by 90% and bandwidth usage by 80% over the state-of-the-art.

以下是中文翻译：

分布式密钥生成（DKG）是一种无需依赖可信第三方即可启动门限密码系统的技术。作为众多去中心化协议的核心组件，DKG广泛应用于随机信标、门限签名、拜占庭共识及多方计算等领域。尽管近期研究取得显著进展，但当重构门限超过总节点数的三分之一时，现有异步DKG方案仍存在效率瓶颈。本文提出一种简洁高效的异步DKG（ADKG）协议，在n=3t+1个节点中可容忍最多t个恶意节点，并支持任意重构门限ℓ≥t。该协议预期通信成本为O(κn³)（κ为安全参数），仅基于离散对数难题假设。 本ADKG协议的核心创新在于实现了对ℓ≥t阶随机多项式的异步秘密共享，该技术还可应用于异步主动秘密共享和异步多方计算等场景。我们实现了高门限ADKG协议，并在128个地理分布式节点构成的网络中进行了测试。实验数据显示，相较于现有最优方案，我们的高门限ADKG协议将运行时间缩短90%，带宽消耗降低80%。

## 关键词

+ 异步分布式密钥生成ADKG
+ 高门限密码系统
+ 秘密多项式采样
+ 拜占庭容错密钥生成
+ 随机信标门限签名
+ 异步多方计算
