---
title: "Gemini: Elastic SNARKs for diverse environments"
标题简称:
论文类型: conference
会议简称: EUROCRYPT
发表年份: 2022
modified: 2025-04-27 09:03:01
created: 2025-04-11 11:19:48
---

## Gemini: Elastic SNARKs for diverse environments

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-07085-3_15)

## 作者

+ [Jonathan Bootle](Jonathan%20Bootle.md)
+ [Alessandro Chiesa](Alessandro%20Chiesa.md)
+ [Yuncong Hu](Yuncong%20Hu.md)
+ Michele Orru 

## 笔记

We introduce a new class of succinct arguments, that we call elastic. Elastic SNARKs allow the prover to allocate different resources (such as memory and time) depending on the execution environment and the statement to prove. The resulting output is independent of the prover’s configuration. To study elastic SNARKs, we extend the streaming paradigm of [Block et al., TCC’20]. We provide a definitional framework for elastic polynomial interactive oracle proofs for R1CS instances and design a compiler which transforms an elastic PIOP into a preprocessing argument system that supports streaming or random access to its inputs. Depending on the configuration, the prover will choose different trade-offs for time (either linear, or quasilinear) and memory (either linear, or logarithmic). We prove the existence of elastic SNARKS by presenting Gemini, a novel FFT-free preprocessing argument. We prove its security and develop a proof-of-concept implementation in Rust based on the arkworks framework. We provide benchmarks for large R1CS instances of tens of billions of gates on a single machine.

以下是中文翻译：

我们介绍了一类新的简洁论证，称为弹性论证(elastic)。弹性零知识简洁非交互式论证系统(elastic SNARKs)允许证明者根据执行环境和待证明的语句来分配不同的资源(如内存和时间)。最终输出结果与证明者的配置无关。为了研究弹性SNARKs，我们扩展了[Block等人，TCC'20]提出的流式范式。

我们为R1CS实例提供了弹性多项式交互式预言证明(elastic polynomial interactive oracle proofs)的定义框架，并设计了一个编译器，可以将弹性PIOP转换为支持流式处理或随机访问输入的预处理论证系统。根据不同的配置，证明者可以在时间(线性或准线性)和内存(线性或对数)之间选择不同的权衡。

我们通过提出Gemini(一种新型的无FFT预处理论证)证明了弹性SNARKs的存在性。我们证明了其安全性，并基于arkworks框架在Rust中开发了概念验证实现。我们在单台机器上对包含数百亿门电路的大型R1CS实例进行了基准测试。

## 关键词

+ 弹性SNARK
+ 流式证明
+ 无FFT预处理论证
+ R1CS
+ 内存时间权衡