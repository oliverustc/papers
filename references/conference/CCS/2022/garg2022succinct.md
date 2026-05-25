---
title: "Succinct zero knowledge for floating point computations"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2022
created: 2025-04-16 11:22:14
modified: 2025-04-16 11:22:36
---

## Succinct zero knowledge for floating point computations

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3548606.3560653)

## 作者

+ [Sanjam Garg](Sanjam%20Garg.md) 
+ [Abhishek Jain](Abhishek%20Jain.md)
+ Zhengzhong Jin 
+ [Yinuo Zhang](Yinuo%20Zhang.md)
## 笔记

We study the problem of constructing succinct zero knowledge proof systems for floating point computations. The standard approach to handle floating point computations requires conversion to binary circuits, following the IEEE-754 floating point standard. This approach incurs a poly(w) overhead in prover efficiency for computations with w-bit precision, resulting in very high prover runtimes -- already the key bottleneck in the design of succinct arguments. We make the following contributions: -We propose a new model for verifying floating point computations that guarantees approximate correctness w.r.t. a relative error bound. This model is inspired by numerical analysis, and is very meaningful for applications such as machine learning and scientific computing. -Using this model, we present a general method for constructing succinct zero-knowledge proofs for floating point computations starting from existing public-coin "commit-and-prove'' systems. For computations with w-bit precision, our approach incurs only a log(w) overhead in prover running time. Our compiler nearly preserves (up to a factor of 2) the communication complexity of the underlying protocol, and requires sub-linear verification time. The resulting proof can be made non-interactive in the random oracle model. Concretely, our scheme is ~57x faster than the method following IEEE standard exactly [35] for 32-bit floating point computations. Central to our main result, and of independent interest, is a new batch range proof system in standard prime order groups that does not rely on bit decomposition.

以下是中文翻译：

我们研究了为浮点计算构建简洁零知识证明系统的问题。处理浮点计算的标准方法需要按照IEEE-754浮点标准将其转换为二进制电路。对于w位精度的计算，这种方法会导致证明者效率产生poly(w)的开销，从而导致证明者运行时间非常长——这已经成为设计简洁论证系统的主要瓶颈。我们做出了以下贡献：

-我们提出了一个新的浮点计算验证模型，该模型保证了相对误差范围内的近似正确性。这个模型受数值分析启发，对机器学习和科学计算等应用非常有意义。

-基于这个模型，我们提出了一种通用方法，可以从现有的公开投币"承诺并证明"系统出发，构建浮点计算的简洁零知识证明。对于w位精度的计算，我们的方法在证明者运行时间上只产生log(w)的开销。我们的编译器几乎保持了底层协议的通信复杂度（最多增加2倍），并且需要亚线性的验证时间。在随机预言机模型中，所得到的证明可以变成非交互式的。

具体而言，对于32位浮点计算，我们的方案比严格遵循IEEE标准的方法快约57倍。作为我们主要成果的核心，同时也具有独立研究价值的是，我们在标准素数阶群中提出了一个新的批量范围证明系统，该系统不依赖于位分解。

## 关键词

+ 零知识证明
+ 浮点计算
+ 近似正确性
+ 科学计算
+ 证明大小优化