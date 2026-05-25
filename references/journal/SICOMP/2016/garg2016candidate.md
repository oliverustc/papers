---
title: "Candidate indistinguishability obfuscation and functional encryption for all circuits"
标题简称:
论文类型: journal
期刊简称: SICOMP
发表年份: 2016
created: 2025-04-29 10:25:32
modified: 2025-04-29 10:26:41
---

## Candidate indistinguishability obfuscation and functional encryption for all circuits

## 发表信息

+ [原文链接](https://epubs.siam.org/doi/abs/10.1137/14095772X)

## 作者

+ [Sanjam Garg](Sanjam%20Garg.md) 
+ [Craig Gentry](Craig%20Gentry.md)
+ [Shai Halevi](Shai%20Halevi.md)
+ [Mariana Raykova](Mariana%20Raykova.md)
+ [Amit Sahai](Amit%20Sahai.md)
+ [Brent Waters](Brent%20Waters.md)
## 笔记

In this work, we study _indistinguishability obfuscation_ and _functional encryption_ for general circuits: Indistinguishability obfuscation requires that given any two equivalent circuits C0 and C1 of similar size, the obfuscations of C0 and C1 should be computationally indistinguishable. In functional encryption, ciphertexts encrypt inputs x and keys are issued for circuits C. Using the key SKC to decrypt a ciphertext CTx=Enc(x) yields the value C(x) but does not reveal anything else about x. Furthermore, no collusion of secret key holders should be able to learn anything more than the union of what they can each learn individually. We give constructions for indistinguishability obfuscation and functional encryption that supports all polynomial-size circuits. We accomplish this goal in three steps: (1) We describe a candidate construction for indistinguishability obfuscation for NC1 circuits. The security of this construction is based on a new algebraic hardness assumption. The candidate and assumption use a simplified variant of multilinear maps, which we call _multilinear jigsaw puzzles_. (2) We show how to use indistinguishability obfuscation for NC1 together with fully homomorphic encryption (with decryption in NC1) to achieve indistinguishability obfuscation for all circuits. (3) Finally, we show how to use indistinguishability obfuscation for circuits, public-key encryption, and noninteractive zero knowledge to achieve functional encryption for all circuits. The functional encryption scheme we construct also enjoys succinct ciphertexts, which enables several other applications.

以下是中文翻译：

在本研究中，我们研究了用于一般电路的不可区分混淆(indistinguishability obfuscation)和函数加密(functional encryption)：不可区分混淆要求对于任意两个大小相近的等价电路C0和C1，C0和C1的混淆结果在计算上应该是不可区分的。在函数加密中，密文加密输入x，密钥则针对电路C发放。使用密钥SKC解密密文CTx=Enc(x)可得到值C(x)，但不会泄露关于x的任何其他信息。此外，密钥持有者之间的任何共谋都不应能获得比他们各自单独获得的信息之和更多的信息。

我们提供了支持所有多项式大小电路的不可区分混淆和函数加密的构造方案。我们通过以下三个步骤实现这一目标：

(1) 我们描述了一个针对NC1电路的不可区分混淆的候选构造。该构造的安全性基于一个新的代数难度假设。该候选方案和假设使用了多线性映射(multilinear maps)的一个简化变体，我们称之为多线性拼图(multilinear jigsaw puzzles)。

(2) 我们展示了如何将NC1的不可区分混淆与全同态加密(解密在NC1中进行)结合使用，以实现所有电路的不可区分混淆。

(3) 最后，我们展示了如何使用电路的不可区分混淆、公钥加密和非交互式零知识证明来实现所有电路的函数加密。我们构造的函数加密方案还具有简洁的密文特性，这使得它能够支持其他几个应用场景。

## 关键词

+ 不可区分性混淆候选构造
+ 通用电路函数加密
+ 多线性拼图硬度假设
+ NC1混淆全同态加密组合
+ 简洁密文函数加密
+ 非交互式零知识混淆应用