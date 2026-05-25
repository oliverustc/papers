---
title: "Scalable multi-party computation for zk-SNARK parameters in the random beacon model"
标题简称:
论文类型: preprint
预印本简称: archive
发表年份: 2017
created: 2025-06-10 02:36:19
modified: 2025-06-10 02:39:41
---

## Scalable multi-party computation for zk-SNARK parameters in the random beacon model

## 发表信息

+ [原文链接](https://eprint.iacr.org/2017/1050)

## 作者

+ [Sean Bowe](Sean%20Bowe.md)
+ [Ariel Gabizon](Ariel%20Gabizon.md)
+ [Ian Miers](Ian%20Miers.md)
## 笔记

Zero-knowledge succinct non-interactive arguments of knowledge (zk-SNARKs) have emerged as a valuable tool for verifiable computation and privacy preserving protocols. Currently practical schemes require a common reference string (CRS) to be constructed in a one-time setup for each statement. Ben-Sasson, Chiesa, Green, Tromer and Virza devised a multi-party protocol to securely compute such a CRS, and an adaptation of this protocol was used to construct the CRS for the Zcash cryptocurrency. The scalability of these protocols is obstructed by the need for a "precommitment round" which forces participants to be defined in advance and requires them to secure their secret randomness throughout the duration of the protocol. Our primary contribution is a more scalable multi-party computation (MPC) protocol, secure in the random beacon model, which omits the precommitment round. We show that security holds even if an adversary has limited influence on the beacon. Next, we apply our main result to obtain a two-round protocol for computing an extended version of the CRS of Groth's SNARK. We show that knowledge soundness is maintained in the generic group model when using this CRS. We also contribute a more secure pairing-friendly elliptic curve construction and implementation, tuned for use in zk-SNARKs, in light of recent optimizations to the Number Field Sieve algorithm which reduced the security estimates of existing pairing-friendly curves used in zk-SNARK applications.

以下是中文翻译：

零知识简洁非交互式知识论证（zk-SNARKs）已成为可验证计算和隐私保护协议的重要工具。当前实用方案要求为每个声明（statement）在一次性设置中构建公共参考字符串（Common Reference String, CRS）。Ben-Sasson、Chiesa、Green、Tromer和Virza设计了一种多方协议来安全计算此类CRS，该协议的改进版本被用于构建Zcash加密货币的CRS。这些协议的可扩展性因"预提交轮次（precommitment round）"而受限——该机制要求参与者必须预先确定，并需在整个协议执行期间确保其秘密随机性的安全性。

我们的核心贡献是提出了一种更具可扩展性的多方计算（Multi-Party Computation, MPC）协议，该协议在随机信标（random beacon）模型中安全运行，且无需预提交轮次。我们证明，即使对手对信标的影响有限，安全性仍可保障。随后，我们应用这一主要成果，设计了一种两轮协议以计算Groth的SNARK方案中CRS的扩展版本。通过理论分析表明，在通用群模型（generic group model）中使用该CRS时，知识可靠性（knowledge soundness）依然成立。

针对近期数域筛法（Number Field Sieve）算法的优化降低了现有zk-SNARK应用中配对友好曲线（pairing-friendly curves）的安全估值，我们还提出了一种更安全的配对友好椭圆曲线构造与实现方案，专门为zk-SNARK应用优化。

## 关键词

+ zk-SNARK参数可扩展多方计算
+ 随机信标模型安全协议
+ 公共参考字符串CRS生成
+ Groth SNARK扩展两轮协议
+ 配对友好椭圆曲线安全优化
+ 预提交轮次消除设计