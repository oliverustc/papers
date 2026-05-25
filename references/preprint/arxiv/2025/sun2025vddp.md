---
title: "VDDP: Verifiable Distributed Differential Privacy under the Client-Server-Verifier Setup"
标题简称:
论文类型: preprint
预印本简称: arxiv
发表年份: 2025
---

## VDDP: Verifiable Distributed Differential Privacy under the Client-Server-Verifier Setup

## 发表信息

+ [原文链接](https://arxiv.org/abs/2504.21752)

## 作者

+ [Haochen Sun](Haochen%20Sun.md) 
+ Xi He 


## 笔记

Although differential privacy (DP) is widely regarded as the de facto standard for data privacy, its implementation remains vulnerable to unfaithful execution by servers, particularly in distributed settings. In such cases, servers may sample noise from incorrect distributions or generate correlated noise while appearing to follow established protocols. This work addresses these malicious behaviours in a distributed client-server-verifier setup, under Verifiable Distributed Differential Privacy (VDDP), a novel framework for the verifiable execution of distributed DP mechanisms. We systematically capture end-to-end security and privacy guarantees against potentially colluding adversarial behaviours of clients, servers, and verifiers by characterizing the connections and distinctions between VDDP and zero-knowledge proofs (ZKPs).  
We develop three novel and efficient instantiations of VDDP: (1) the Verifiable Distributed Discrete Laplace Mechanism (VDDLM), which achieves up to a 400,000 x improvement in proof generation efficiency with only 0.1--0.2 x error compared with the previous state-of-the-art verifiable differentially private mechanism and includes a tight privacy analysis that accounts for all additional privacy losses due to numerical imprecisions, applicable to other secure computation protocols for DP mechanisms based on cryptography; (2) the Verifiable Distributed Discrete Gaussian Mechanism (VDDGM), an extension of VDDLM that incurs limited overhead in real-world applications; and (3) an improved solution to Verifiable Randomized Response (VRR) under local DP, as a special case of VDDP, achieving up to a 5,000 x reduction in communication costs and verifier overhead.


以下是中文翻译：

尽管差分隐私（Differential Privacy, DP）被广泛视为数据隐私的事实标准，但其在实际部署中仍易受服务器不忠实执行（unfaithful execution）的威胁，尤其在分布式环境中。在此类场景下，服务器可能从错误的分布中采样噪声，或生成相关噪声，同时表面上仍遵循既定协议。

本文针对分布式客户端-服务器-验证者架构中的此类恶意行为，提出可验证分布式差分隐私（Verifiable Distributed Differential Privacy, VDDP）——一种用于可验证执行分布式 DP 机制的新框架。我们通过刻画 VDDP 与零知识证明（Zero-Knowledge Proofs, ZKPs）之间的联系与区别，系统性地刻画了端到端的安全性与隐私保障，以抵御客户端、服务器与验证者之间潜在的共谋攻击。

我们提出了三种新颖且高效的 VDDP 具体实现：（1）可验证分布式离散拉普拉斯机制（Verifiable Distributed Discrete Laplace Mechanism, VDDLM），相较于当前最先进的可验证差分隐私机制，在证明生成效率上最高提升达 400,000 倍，同时误差仅为其 0.1–0.2 倍；该机制还包含一项严格的隐私分析，全面计入因数值不精确性所引入的额外隐私损失，该分析亦适用于其他基于密码学的安全计算协议中的 DP 机制；（2）可验证分布式离散高斯机制（Verifiable Distributed Discrete Gaussian Mechanism, VDDGM），作为 VDDLM 在现实应用中的扩展，仅引入有限的开销；（3）作为 VDDP 的一个特例，我们在本地差分隐私（Local DP）下对可验证随机响应（Verifiable Randomized Response, VRR）提出了改进方案，最高可将通信开销与验证者负担降低 5,000 倍。


## 关键词

+ VDDP可验证分布式差分隐私框架
+ 客户端服务器验证者安全架构
+ VDDLM离散拉普拉斯机制高效证明
+ 本地差分隐私可验证随机响应
+ 零知识证明差分隐私联合保障