---
title: "Siniel: Distributed Privacy-Preserving zkSNARK"
标题简称: 
论文类型: conference
会议简称: NDSS
发表年份: 2025
modified: 2025-04-13 16:39:23
---

## Siniel: Distributed Privacy-Preserving zkSNARK

## 发表信息

+ [原文链接](https://eprint.iacr.org/2024/1803)

## 作者

+ Yunbo Yang 
+ Yuejia Cheng 
+ Kailun Wang 
+ Xiaoguo Li 
+ Jianfei Sun 
+ Jiachen Shen 
+ Xiaolei Dong 
+ Zhenfu Cao 
+ Guomin Yang 
+ Robert H Deng 

## 笔记

Zero-knowledge Succinct Non-interactive Argument of Knowledge (zkSNARK) is a powerful cryptographic primitive, in which a prover convinces a verifier that a given statement is true without leaking any additional information. However, existing zkSNARKs suffer from high computation overhead in the proof generation. This limits the applications of zkSNARKs, such as private payments, private smart contracts, and anonymous credentials. Private delegation has become a prominent way to accelerate proof generation.  

以下是中文翻译：

零知识简洁非交互式知识论证（zkSNARK）作为一种强大的密码学原语，允许证明者在不泄露任何额外信息的情况下，使验证者确信某一陈述的真实性。然而，现有zkSNARK技术在证明生成阶段面临高计算开销的问题，这限制了其在隐私支付、私有智能合约及匿名凭证等领域的应用。为此，私有委托已成为加速证明生成的重要途径。

In this work, we propose Siniel, an efficient private delegation framework for zkSNARKs constructed from polynomial interactive oracle proof (PIOP) and polynomial commitment scheme (PCS). Our protocol allows a computationally limited prover (a.k.a. delegator) to delegate its expensive prover computation to several workers without leaking any information about the private witness. Most importantly, compared with the recent work EOS (USENIX'23), the state-of-the-art zkSNARK prover delegation framework, a prover in Siniel needs not to engage in the MPC protocol after sending its shares of private witness. This means that a Siniel prover can outsource the entire computation to the workers.  
在这项工作中，我们提出了Siniel，一个高效的zkSNARKs私有委托框架，该框架基于多项式交互式预言证明（PIOP）和多项式承诺方案（PCS）构建。我们的协议允许计算能力有限的证明者（即委托者）将其昂贵的证明计算任务委托给多个工作者，而不会泄露任何关于私有见证的信息。最重要的是，与最新研究成果EOS（USENIX'23）——当前最先进的zkSNARK证明者委托框架相比，Siniel中的证明者在发送其私有见证份额后无需再参与多方计算（MPC）协议。这意味着Siniel的证明者可以将整个计算过程完全外包给工作者。

We compare Siniel with EOS and show significant performance advantages of the former. The experimental results show that, under low bandwidth conditions (10MBps), Siniel saves about 16% time for delegators than that of EOS, whereas under high bandwidth conditions (1000MBps), Siniel saves about 80% than EOS.  
我们将Siniel与EOS进行对比，结果显示前者具有显著的性能优势。实验数据表明，在低带宽环境（10MBps）下，Siniel为委托者节省的时间比EOS约多16%；而在高带宽条件（1000MBps）下，Siniel的节省幅度更是达到了约80%。

## 关键词

+ 分布式zkSNARK
+ 证明委托
+ 多项式交互式预言证明（PIOP）
+ 多项式承诺方案
+ 隐私保护证明生成
+ 多方计算