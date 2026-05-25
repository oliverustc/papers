---
title: Randomizable proofs and delegatable anonymous credentials

标题简称: 
论文类型: conference
会议简称: CRYPTO
发表年份: 2009
created: 2025-05-23 01:24:40
modified: 2025-05-26 05:05:25
tags:
  - 需要调研引用文献
---

## Randomizable proofs and delegatable anonymous credentials

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-642-03356-8_7)

## 作者

+ Mira Belenkiy
+ [Jan Camenisch](Jan%20Camenisch.md)
+ [Melissa Chase](Melissa%20Chase.md)
+ [Markulf Kohlweiss](Markulf%20Kohlweiss.md)
+ [Anna Lysyanskaya](Anna%20Lysyanskaya.md)
+ [Hovav Shacham](Hovav%20Shacham.md)
## 笔记

We construct a practical delegatable anonymous credential system. The system relies on a new randomizable proof system built from the Groth-Sahai (GS) proof framework, and in particular from our construction of randomizable commitments and proofs. In a nutshell, a randomizable proof is a proof that can be re-randomized: given a proof $\pi$ of a statement $x$, one can compute a new proof $\pi'$ of the same statement $x$ such that $\pi$ and $\pi'$ are indistinguishable. Using this tool, we construct the first delegatable anonymous credential system where credentials can be anonymously delegated to any depth. A user who has been issued a credential can use it to obtain new credentials from higher authorities, and can further delegate the composite credential. Security is based on the DLIN assumption in bilinear groups and is proved in the standard model without random oracles.

以下是中文翻译：

我们构建了一个实用的可委托匿名凭证系统。该系统依赖于一种新的可随机化证明系统，该系统基于Groth-Sahai（GS）证明框架构建，特别是基于我们对可随机化承诺和证明的构造。简而言之，可随机化证明是一种可以被重新随机化的证明：给定陈述$x$的证明$\pi$，可以计算同一陈述$x$的新证明$\pi'$，使得$\pi$和$\pi'$不可区分。利用这个工具，我们构建了首个可委托匿名凭证系统，其中凭证可以在任意深度匿名委托。已获得凭证的用户可以使用它从上级权威机构获取新凭证，并可进一步委托复合凭证。安全性基于双线性群中的DLIN假设，并在无随机预言机的标准模型中得到证明。

## 关键词

+ 可随机化证明Groth-Sahai框架委托凭证
+ 可委托匿名凭证任意深度委托链
+ 匿名凭证重新随机化隐私保护
+ DLIN假设双线性群标准模型安全
+ 匿名委托链无随机预言机证明系统