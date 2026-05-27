---
title: "Gzkp: A gpu accelerated zero-knowledge proof system"
doi: 10.1145/3575693.3575711
标题简称:
论文类型: conference
会议简称: ASPLOS
发表年份: 2023
modified: 2025-04-11 11:25:00
---
## Gzkp: A gpu accelerated zero-knowledge proof system

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3575693.3575711)

## 作者

+ Weiliang Ma 
+ Qian Xiong 
+ Xuanhua Shi 
+ Xiaosong Ma 
+ Hai Jin 
+ Haozhao Kuang 
+ Mingyu Gao 
+ [Ye Zhang](Ye%20Zhang.md)
+ Haichen Shen 
+ Weifang Hu 

## 笔记

Zero-knowledge proof (ZKP) is a cryptographic protocol that allows one party to prove the correctness of a statement to another party without revealing any information beyond the correctness of the statement itself. It guarantees computation integrity and confidentiality, and is therefore increasingly adopted in industry for a variety of privacy-preserving applications, such as verifiable outsource computing and digital currency.

A significant obstacle in using ZKP for online applications is the performance overhead of its proof generation. We develop GZKP, a GPU accelerated zero-knowledge proof system that supports different levels of security requirements and brings significant speedup toward making ZKP truly usable. For polynomial computation over a large finite field, GZKP promotes a cache-friendly memory access pattern while eliminating the costly external shuffle in existing solutions. For multi-scalar multiplication, GZKP adopts a new parallelization strategy, which aggressively combines integer elliptic curve point operations and exploits fine-grained task parallelism with load balancing for sparse integer distribution. GZKP outperforms the state-of-the-art ZKP systems by an order of magnitude, achieving up to 48.1× and 17.6× speedup with standard cryptographic benchmarks and a real-world application workload, respectively.

以下是中文翻译：

零知识证明(Zero-knowledge proof, ZKP)是一种密码学协议，它允许一方向另一方证明某个陈述的正确性，而无需透露除了该陈述正确性之外的任何信息。它保证了计算的完整性和机密性，因此在工业领域被越来越多地应用于各种隐私保护应用中，如可验证的外包计算和数字货币。

在在线应用中使用ZKP的一个主要障碍是其证明生成过程中的性能开销。我们开发了GZKP，这是一个GPU加速的零知识证明系统，它支持不同级别的安全需求，并带来了显著的性能提升，使ZKP真正可用。对于大有限域上的多项式计算，GZKP提出了一种缓存友好的内存访问模式，同时消除了现有解决方案中代价高昂的外部随机重排。对于多标量乘法(multi-scalar multiplication)，GZKP采用了一种新的并行化策略，该策略积极地组合整数椭圆曲线点运算，并针对稀疏整数分布利用细粒度任务并行化实现负载均衡。GZKP的性能超过了现有最先进的ZKP系统一个数量级，在标准密码学基准测试和真实应用工作负载中分别实现了高达48.1倍和17.6倍的性能提升。

## 关键词

+ 零知识证明
+ GPU加速
+ 证明生成
+ 多标量乘法
+ 性能优化