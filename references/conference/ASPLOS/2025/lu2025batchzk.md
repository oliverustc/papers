---
title: "BatchZK: A Fully Pipelined GPU-Accelerated System for Batch Generation of Zero-Knowledge Proofs"
doi: 10.1145/3669940.3707270
标题简称:
论文类型: conference
会议简称: ASPLOS
发表年份: 2025
created: 2025-04-16 17:33:03
modified: 2025-04-16 17:33:13
---
## BatchZK: A Fully Pipelined GPU-Accelerated System for Batch Generation of Zero-Knowledge Proofs

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3669940.3707270)

## 作者

+ Tao Lu 
+ Yuxun Chen 
+ Zonghui Wang 
+ Xiaohang Wang 
+ Wenzhi Chen 
+ [Jiaheng Zhang](Jiaheng%20Zhang.md) 

## 笔记

Zero-knowledge proof (ZKP) is a cryptographic primitive that enables one party to prove the validity of a statement to other parties without disclosing any secret information. With its widespread adoption in applications such as blockchain and verifiable machine learning, the demand for generating zero-knowledge proofs has increased dramatically. In recent years, considerable efforts have been directed toward developing GPU-accelerated systems for proof generation. However, these previous systems only explored efficiently generating a single proof by reducing latency rather than batch generation to provide high throughput.
We propose a fully pipelined GPU-accelerated system for batch generation of zero-knowledge proofs. Our system has three features to improve throughput. First, we design a pipelined approach that enables each GPU thread to continuously execute its designated proof generation task without being idle. Second, our system supports recent efficient ZKP protocols with their computational modules: sum-check protocol, Merkle tree, and linear-time encoder. We customize these modules to fit our pipelined execution. Third, we adopt a dynamic loading method for the data required for proof generation, reducing the required device memory. Moreover, multi-stream technology enables the overlap of data transfers and GPU computations, reducing overhead caused by data exchanges between host and device memory.
We implement our system and evaluate it on various GPU cards. The results show that our system achieves more than 259.5× higher throughput compared to state-of-the-art GPU-accelerated systems. Moreover, we deploy our system in the verifiable machine learning application, where our system generates 9.52 proofs per second, successfully achieving sub-second proof generation for the first time in this field.

以下是中文翻译：

零知识证明(Zero-knowledge proof, ZKP)是一种密码学原语，它使一方能够向其他方证明某个陈述的有效性，而无需披露任何秘密信息。随着其在区块链和可验证机器学习等应用中的广泛采用，生成零知识证明的需求已显著增加。近年来，大量研究致力于开发GPU加速的证明生成系统。然而，这些现有系统仅探索了通过减少延迟来高效生成单个证明，而非通过批量生成来提供高吞吐量。

我们提出了一个用于批量生成零知识证明的全流水线GPU加速系统。我们的系统具有三个提高吞吐量的特性。首先，我们设计了一种流水线方法，使每个GPU线程能够持续执行其指定的证明生成任务而不会空闲。其次，我们的系统支持近期高效的ZKP协议及其计算模块：和检查协议(sum-check protocol)、默克尔树(Merkle tree)和线性时间编码器(linear-time encoder)。我们定制了这些模块以适应我们的流水线执行。第三，我们采用了证明生成所需数据的动态加载方法，减少了所需的设备内存。此外，多流技术(multi-stream technology)实现了数据传输和GPU计算的重叠，减少了主机内存和设备内存之间数据交换造成的开销。

我们实现了该系统并在各种GPU卡上进行了评估。结果表明，与最先进的GPU加速系统相比，我们的系统实现了超过259.5倍的更高吞吐量。此外，我们将系统部署在可验证机器学习应用中，我们的系统每秒生成9.52个证明，首次在该领域实现了亚秒级的证明生成。

## 关键词

+ 零知识证明
+ GPU加速
+ 批量生成
+ 流水线处理
+ 可验证计算