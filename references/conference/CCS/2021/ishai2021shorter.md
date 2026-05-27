---
title: "Shorter and faster post-quantum designated-verifier zkSNARKs from lattices"
doi: 10.1145/3460120.3484572
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2021
modified: 2025-04-11 11:41:42
---
## Shorter and faster post-quantum designated-verifier zkSNARKs from lattices

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3460120.3484572)

## 作者

+ [Yuval Ishai](Yuval%20Ishai.md)
+ Hang Su 
+ David J Wu 

## 笔记

### 背景与动机
零知识简洁非交互式知识论证 (zkSNARK) 是密码学中实现隐私保护与可验证计算的关键工具。尽管基于配对和代数群假设的预量子构造已在实践中达到了极高的简洁性，例如 Groth (Eurocrypt 2016) 的证明仅 128 字节 [75]，但它们无法抵御量子计算机的攻击。近年来涌现的众多后量子候选方案，例如基于交互式预言机证明 (IOP) 的 Aurora [21] 和 Fractal [47]，以及基于格的构造 [65]，在实现抗量子安全性的同时，产生了显著更大的证明体积。现有的后量子 zkSNARKs 在证明大小上普遍比最简洁的预量子方案大 1000 倍以上，这是其在实际应用中面临的主要瓶颈。本文旨在填补这一鸿沟，通过开发基于格的新构造，在指定验证者预处理模型中实现更短和更快的后量子 zkSNARKs，显著缩小了与预量子方案在性能上的巨大差距。

### 相关工作

[30] Bitansky 等. Succinct Non-interactive Arguments via Linear Interactive Proofs. **TCC 2013** [Google Scholar](https://scholar.google.com/scholar?q=Succinct+Non-interactive+Arguments+via+Linear+Interactive+Proofs)
> 核心思路：提出从线性PCP和线性唯一加密方案编译zkSNARKs的通用框架。
> 局限与区别：该框架的早期实现，如[64, 65]，在格实例化下


## 关键词

+ 后量子密码学
+ 零知识证明
+ 格基密码学
+ 证明大小优化
+ 验证者指定