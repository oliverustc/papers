---
title: "How to Prove Statements Obliviously?"

标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 2024

modified: 2025-04-10 17:07:28
---

## How to Prove Statements Obliviously?

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-68403-6_14)

## 作者

+ [Sanjam Garg](Sanjam%20Garg.md)
+ [Aarushi Goel](Aarushi%20Goel.md)
+ [Mingyuan Wang](Mingyuan%20Wang.md)

## 笔记

Cryptographic applications often require proving statements about hidden secrets satisfying certain circuit relations. Moreover, these proofs must often be generated obliviously, i.e., without knowledge of the secret. This work presents a new technique called—FRI on hidden values—for efficiently proving such statements. This technique enables a polynomial commitment scheme for values hidden inside linearly homomorphic primitives, such as linearly homomorphic encryption, linearly homomorphic commitment, group exponentiation, fully homomorphic encryption, etc. Building on this technique, we obtain the following results.

1. An efficient SNARK for proving the honest evaluation of FHE ciphertexts. This allows for an efficiently verifiable private delegation of computation, where the client only needs to perform logarithmic many FHE computations to verify the correctness of the computation.

2. An efficient approach for privately delegating the computation of zkSNARKs to a single untrusted server, without requiring the server to make any non-black-box use of cryptography. All prior works require multiple servers and the assumption that some subset of the servers are honest.

3. A weighted threshold signature scheme that does not require any setup. In particular, parties may sample their own keys independently, and no distributed key generation (DKG) protocol is needed. Furthermore, the efficiency of our scheme is completely independent of the weights.

Prior to this work, there were no known black-box feasibility results for any of these applications. We also investigate the use of this approach in the context of public proof aggregation. These are only a few representative applications that we explore in this paper. We expect our techniques to be widely applicable in many other scenarios.

以下是中文翻译：

加密应用通常需要证明关于隐藏秘密满足特定电路关系的陈述。此外，这些证明往往必须以隐蔽的方式生成，即在不知道秘密的情况下进行。本文提出了一种称为“隐藏值上的FRI”（FRI on hidden values）的新技术，用于高效地证明此类陈述。这项技术使得能够为隐藏在线性同态原语（如线性同态加密、线性同态承诺、群体指数运算、全同态加密等）内部的值提供多项式承诺方案。基于这一技术，我们获得了以下结果。

1. 一种高效的SNARK（简洁非交互式零知识证明）用于证明全同态加密（FHE）密文的诚实计算。这允许高效可验证的私有计算委托，其中客户端只需执行对数次FHE计算即可验证计算的正确性。

2. 一种高效的方法，用于将zkSNARK（零知识简洁非交互式证明）计算私有委托给单个不可信服务器，而无需服务器对密码学进行任何非黑箱使用。所有先前的工作都需要多个服务器，并假设某些服务器的子集是诚实的。

3. 一种无需任何设置的加权门限签名方案。特别是，各方可以独立地生成自己的密钥，无需任何分布式密钥生成（DKG）协议。此外，我们方案的效率完全独立于权重。

在本研究之前，对于这些应用没有已知的黑箱可行性结果。我们还探讨了在公共证明聚合背景下使用该方法的可能性。这些只是我们在本文中探讨的一些代表性应用。我们期望我们的技术在许多其他场景中也具有广泛的适用性。

## 关键词

+ 隐蔽值FRI多项式承诺技术
+ FHE私有计算委托可验证SNARK
+ zkSNARK单服务器私有委托
+ 无设置加权门限签名方案
+ 线性同态原语隐蔽证明方法