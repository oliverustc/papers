---
title: "Reinforced concrete: A fast hash function for verifiable computation"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2022
created: 2025-04-22 15:12:43
modified: 2025-04-22 15:18:39
---

## Reinforced concrete: A fast hash function for verifiable computation

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3548606.3560686)

## 作者

+ [Lorenzo Grassi](Lorenzo%20Grassi.md)
+ [Dmitry Khovratovich](Dmitry%20Khovratovich.md)
+ Reinhard Lüftenegger 
+ [Christian Rechberger](Christian%20Rechberger.md)
+ Markus Schofnegger 
+ Roman Walch 

## 笔记

We propose a new hash function Reinforced Concrete, which is the first generic purpose hash that is fast both for a zero-knowledge prover and in native x86 computations. It is suitable for a various range of zero-knowledge proofs and protocols, from set membership to generic purpose verifiable computation. Being up to 15x faster than its predecessor Poseidon hash, Reinforced Concrete inherits security from traditional time-tested schemes such as AES, whereas taking the zero-knowledge performance from a novel and efficient decomposition of a prime field into compact buckets.

以下是中文翻译：

我们提出了一种新型哈希函数——强化混凝土（Reinforced Concrete），这是首个在零知识证明和原生x86计算中均表现快速的通用型哈希。该函数适用于从集合成员资格到通用可验证计算的广泛零知识证明与协议场景。相较于前代Poseidon哈希，其速度提升高达15倍，同时通过将素数域高效分解为紧凑桶结构，既继承了如AES等久经考验的传统方案的安全性，又实现了卓越的零知识性能。

The new hash function is suitable for a wide range of applications like privacy-preserving cryptocurrencies, verifiable encryption, protocols with state membership proofs, or verifiable computation. It may serve as a drop-in replacement for various prime-field hashes such as variants of MiMC, Poseidon, Pedersen hash, and others.  
新型哈希函数适用于多种应用场景，如隐私保护型加密货币、可验证加密、带状态成员证明的协议或可验证计算。它可作为多种素数域哈希的直接替代方案，包括MiMC变种、Poseidon、Pedersen哈希等。

## 关键词

+ 哈希函数
+ 零知识证明
+ 可验证计算
+ 密码学原语
+ 素数域