---
title: "Dubhe: Succinct Zero-Knowledge Proofs for Standard AES and related Applications"
标题简称: Dubhe
论文类型: conference
会议简称: USENIX Security
发表年份: 2023
modified: 2025-04-08 21:49:55
---

## Dubhe: Succinct Zero-Knowledge Proofs for Standard AES and related Applications

## 发表信息

+ [原文链接](https://www.usenix.org/conference/usenixsecurity23/presentation/ding-changchang)

## 作者

+ Changchang Ding
+ [Yan Huang](Yan%20Huang.md)

## 笔记

We explore a new approach to construct zero-knowledge proofs by combining ideas from the succinct proof system GKR, the Fully Linear PCP (FLPCP), and MPC-in-the-Head ZKPoK. Our discovery contributes to the state-of-the-art of ZKP in two aspects:

(1) Methodology: We demonstrate a way to build transparent ZK proofs from simplified variant of FLPCP and KKW. The resulting proofs are practically efficient (O(|C|)-time prover, O(log(|C|)-time verifier, O(log(|C|))-bandwidth where |C| is the number of poly- nomial gates), and work readily for circuits defined with polynomial gates over any finite field.

(2) Applications: We present efficient (interactive) identification schemes, ring identification schemes, (non-interactive) digital signatures and ring signatures, all based on the standard AES ciphersuite. We also show the first practically efficient verifiable symmetric-key encryption scheme, based on counter-mode AES.

以下是中文翻译：

我们探索了一种构建零知识证明的新方法，该方法结合了来自简洁证明系统GKR、完全线性PCP (Fully Linear PCP, FLPCP)和基于多方计算的零知识证明协议(MPC-in-the-Head ZKPoK)的思想。我们的发现在以下两个方面推进了零知识证明(ZKP)的研究现状：

(1) 方法论：我们展示了一种通过简化的FLPCP变体和KKW来构建透明零知识证明的方法。所得到的证明在实践中具有高效性（证明者时间复杂度为 $O(|C|)$，验证者时间复杂度为 $O(\log(|C|))$，带宽为 $O(\log(|C|))$，其中 $|C|$ 是多项式门的数量），并且可以直接应用于任何有限域上由多项式门定义的电路。

(2) 应用：我们提出了基于标准AES密码套件的高效（交互式）身份识别方案、环身份识别方案、（非交互式）数字签名和环签名方案。我们还展示了第一个实用高效的可验证对称密钥加密方案，该方案基于计数器模式的AES。

## 关键词

+ Dubhe简洁AES零知识证明
+ GKR证明系统透明ZK
+ MPC-in-the-Head优化
+ AES电路环签名方案
+ 可验证对称密钥加密
+ 完全线性PCP构造
