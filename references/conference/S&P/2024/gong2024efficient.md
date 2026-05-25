---
title: "Efficient zero-knowledge arguments for paillier cryptosystem"
标题简称:
论文类型: conference
会议简称: S&P
发表年份: 2024
created: 2025-04-16 13:57:08
modified: 2025-04-16 14:05:48
---

## Efficient zero-knowledge arguments for paillier cryptosystem

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/10646829)

## 作者

+ Borui Gong 
+ Wang Fat Lau 
+ [Man Ho Au](Man%20Ho%20Au.md)
+ Rupeng Yang 
+ [Haiyang Xue](Haiyang%20Xue.md)
+ Lichun Li 

## 笔记

We present an efficient zero-knowledge argument of knowledge system customized for the Paillier cryptosystem. Our system enjoys sublinear proof size, low verification cost, and acceptable proof generation effort, while also supporting batch proof generation/verification. Existing works specialized for Paillier cryptosystem feature linear proof size and verification time. Using existing sublinear argument systems for generic statements (e.g., zk-SNARK) results in unaffordable proof generation cost since it involves translating the relations to be proven into an inhibitive large Boolean or arithmetic circuit over a prime order field. Our system does not suffer from these limitations.The core of our argument systems is a constraint system defined over the ring of residue classes modulo a composite number, together with novel techniques tailored for arguing binary values in this setting. We then adapt the approach from Bootle et al. (EUROCRYPT 2016) to compile the constraint system into a sublinear argument system. Our constraint system is generic and can be used to express typical relations in Paillier cryptosystems including range proof, correctness proof, relationships between bits of plaintext, relationships of plaintexts among multiple ciphertexts, and more. Our argument supports batch proof generation and verification, with the amortized cost outperforming state-of-the-art protocol specialized for Paillier when the number of Paillier ciphertext is in the order of hundreds.We report an end-to-end prototype and conduct comprehensive experiments across multiple scenarios. Scenario 1 is Paillier with packing. When we pack 25.6K bits into 400 ciphertexts, a proof that all these ciphertexts are correctly computed is 17 times smaller and is 3 times faster to verify compared with the naive implementation: using 25.6K OR-proofs without packing. Furthermore, we can prove additional statements almost for free, e.g., one can prove that the sum of a subset of the witness bits is less than a threshold t. Another scenario is range proof. To prove that each plaintext in 200 Paillier ciphertexts is of size 256 bits, our proof size is 10 times smaller than the state-of-the-art. Our analysis suggests that our system is asymptotically more efficient than existing protocols, and is highly suitable for scenarios involving a large number (more than 100) of Paillier ciphertexts, which is often the case for data analytics applications.

以下是中文翻译：

我们提出了一个为Paillier密码系统定制的高效零知识论证知识系统。我们的系统具有亚线性证明大小、低验证成本和可接受的证明生成工作量，同时还支持批量证明生成/验证。现有专门针对Paillier密码系统的工作具有线性证明大小和验证时间。使用现有的针对通用语句的亚线性论证系统（如zk-SNARK）会导致无法承受的证明生成成本，因为它涉及将待证明的关系转换为素数阶域上过于庞大的布尔或算术电路。我们的系统不受这些限制。

我们论证系统的核心是在复合数模的剩余类环上定义的约束系统，以及为在此环境下论证二进制值而量身定制的新技术。然后，我们采用Bootle等人（EUROCRYPT 2016）[Efficient zero-knowledge arguments for arithmetic circuits in the discrete log setting (**EUROCRYPT 2016**)](bootle2016efficient)的方法将约束系统编译成亚线性论证系统。我们的约束系统是通用的，可用于表达Paillier密码系统中的典型关系，包括范围证明、正确性证明、明文位之间的关系、多个密文之间明文的关系等。我们的论证支持批量证明生成和验证，当Paillier密文数量在数百个量级时，其摊销成本优于专门针对Paillier的最新协议。

我们报告了一个端到端原型并在多个场景下进行了全面实验。场景1是带有打包的Paillier。当我们将25.6K位打包到400个密文中时，证明所有这些密文都正确计算的证明大小比朴素实现（使用25.6K个不打包的OR证明）小17倍，验证速度快3倍。此外，我们几乎可以零成本地证明额外的语句，例如，可以证明见证比特的某个子集之和小于阈值t。另一个场景是范围证明。要证明200个Paillier密文中的每个明文都是256位大小，我们的证明大小比现有最先进的方法小10倍。我们的分析表明，我们的系统在渐近效率上优于现有协议，特别适用于涉及大量（超过100个）Paillier密文的场景，这在数据分析应用中经常出现。

## 关键词

+ Paillier密码系统
+ 零知识论证
+ 亚线性证明大小
+ 复合数模约束系统
+ 批量证明生成验证
+ 范围证明