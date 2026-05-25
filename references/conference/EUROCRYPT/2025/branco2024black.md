---
title: "Black-box non-interactive zero knowledge from vector trapdoor hash"
标题简称:
论文类型: conference
会议简称: EUROCRYPT
发表年份: 2024
created: 2025-04-28 11:43:36
modified: 2025-04-28 14:58:27
---

## Black-box non-interactive zero knowledge from vector trapdoor hash

## 发表信息

+ [原文链接](https://eprint.iacr.org/2024/1514)

## 作者

+ Pedro Branco 
+ [Arka Rai Choudhuri](Arka%20Rai%20Choudhuri.md)
+ [Nico Döttling](Nico%20D%C3%B6ttling.md)
+ [Abhishek Jain](Abhishek%20Jain.md)
+ [Giulio Malavolta](Giulio%20Malavolta.md)
+ Akshayaram Srinivasan 

## 笔记

We present a new approach for constructing non-interactive zero-knowledge (NIZK) proof systems from vector trapdoor hashing (VTDH) -- a generalization of trapdoor hashing [Döttling et al., Crypto'19]. Unlike prior applications of trapdoor hash to NIZKs, we use VTDH to realize the hidden bits model [Feige-Lapidot-Shamir, FOCS'90] leading to black-box constructions of NIZKs. This approach gives us the following new results: - A statistically-sound NIZK proof system based on the hardness of decisional Diffie-Hellman (DDH) and learning parity with noise (LPN) over finite fields with inverse polynomial noise rate. This gives the first statistically sound NIZK proof system that is not based on either LWE, or bilinear maps, or factoring. - A dual-mode NIZK satisfying statistical zero-knowledge in the common random string mode and statistical soundness in the common reference string mode assuming the hardness of learning with errors (LWE) with polynomial modulus-to-noise ratio. This gives the first black-box construction of such a dual-mode NIZK under LWE. This improves the recent work of Waters (STOC'24) which relied on LWE with super-polynomial modulus-to-noise ratio and required a setup phase with private coins. The above constructions are black-box and satisfy single-theorem zero-knowledge property. Building on the works of Feige et al.(FOCS'90) and Fishclin and Rohrback (PKC'21), we upgrade these constructions (under the same assumptions) to satisfy multi-theorem zero-knowledge property at the expense of making non-black-box use of cryptography.

以下是中文翻译：

我们提出了一种基于向量陷门哈希(Vector Trapdoor Hashing, VTDH)构建非交互式零知识(Non-Interactive Zero-Knowledge, NIZK)证明系统的新方法——这是对陷门哈希[Döttling等人，Crypto'19]的一种泛化。与之前将陷门哈希应用于NIZK的方法不同，我们使用VTDH来实现隐藏比特模型(Hidden Bits Model)[Feige-Lapidot-Shamir，FOCS'90]，从而得到NIZK的黑盒构造。这种方法为我们带来了以下新的结果：

- 一个基于判定性Diffie-Hellman(DDH)假设和具有逆多项式噪声率的有限域上学习奇偶校验与噪声(Learning Parity with Noise, LPN)假设的统计可靠NIZK证明系统。这是首个既不基于LWE，也不基于双线性映射或因子分解的统计可靠NIZK证明系统。

- 一个双模式NIZK系统，在公共随机字符串模式下满足统计零知识性质，在公共参考字符串模式下满足统计可靠性，该系统基于具有多项式模数-噪声比的学习误差(Learning with Errors, LWE)假设。这是首个基于LWE的此类双模式NIZK的黑盒构造。这改进了Waters(STOC'24)的最新工作，后者依赖于具有超多项式模数-噪声比的LWE，并且需要具有私有随机数的设置阶段。

以上构造都是黑盒的，并满足单定理零知识性质。基于Feige等人(FOCS'90)和Fishclin与Rohrback(PKC'21)的工作，我们在相同假设下将这些构造升级为满足多定理零知识性质，但代价是需要非黑盒地使用密码学。

## 关键词

+ 非交互式零知识证明（NIZK）
+ 向量陷门哈希（VTDH）
+ 隐藏比特模型
+ 黑盒构造
+ DDH假设与LPN假设
+ 双模式NIZK