---
title: "How to use plain witness encryption: registered ABE, flexible broadcast, and more"
标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 2023
created: 2025-04-29 10:34:47
modified: 2025-04-29 17:13:03
---

## How to use plain witness encryption: registered ABE, flexible broadcast, and more

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-38551-3_16)

## 作者

+ Cody Freitag 
+ [Brent Waters](Brent%20Waters.md)
+ David J Wu 

## 笔记

Witness encryption is a generalization of public-key encryption where the public key can be any NP statement _x_ and the associated decryption key is any witness _w_ for _x_. While early constructions of witness encryption relied on multilinear maps and indistinguishability obfuscation (iO), recent works have provided direct constructions of witness encryption that are more efficient than iO (and also seem unlikely to yield iO). Motivated by this progress, we revisit the possibility of using witness encryption to realize advanced cryptographic primitives previously known only in “obfustopia.”

In this work, we give new constructions of _trustless_ encryption systems from _plain_ witness encryption (in conjunction with the learning-with-errors assumption): (1) flexible broadcast encryption (a broadcast encryption scheme where users choose their _own_ secret keys and users can encrypt to an _arbitrary_ set of public keys); and (2) registered attribute-based encryption (a system where users choose their own keys and then register their public key together with a set of attributes with a deterministic and transparent key curator). Both primitives were previously only known from iO. We also show how to use our techniques to obtain an _optimal_ broadcast encryption scheme in the random oracle model.

Underlying our constructions is a novel technique for using witness encryption based on a new primitive which we call _function-binding hash functions_. Whereas a somewhere statistically binding hash function statistically binds a digest to a few bits of the input, a function-binding hash function statistically binds a digest to the _output_ of a function of the inputs. As we demonstrate in this work, function-binding hash functions provide us new ways to leverage the power of plain witness encryption and use it as the foundation of advanced cryptographic primitives. Finally, we show how to build function-binding hash functions for the class of disjunctions of block functions from leveled homomorphic encryption; this in combination with witness encryption yields our main results.

以下是中文翻译：

见证加密(Witness encryption)是公钥加密的一种泛化形式，其中公钥可以是任何NP陈述_x_，而相关的解密密钥是_x_的任何见证_w_。虽然早期的见证加密构造依赖于多线性映射和不可区分混淆(indistinguishability obfuscation, iO)，但最近的研究提供了比iO更高效的见证加密直接构造方法（这些方法似乎也不太可能产生iO）。受这一进展的启发，我们重新探讨了使用见证加密来实现先前仅在"混淆世界"(obfustopia)中已知的高级密码学原语的可能性。

在本研究中，我们基于普通见证加密（结合学习与错误假设(learning-with-errors assumption)）给出了无信任(trustless)加密系统的新构造：(1) 灵活广播加密（一种用户可以选择自己的私钥并且可以对任意公钥集合进行加密的广播加密方案）；以及 (2) 注册型基于属性的加密（一个用户选择自己的密钥，然后向确定性且透明的密钥管理者注册其公钥及一组属性的系统）。这两种原语此前仅能通过iO实现。我们还展示了如何使用我们的技术在随机预言机模型中获得最优的广播加密方案。

我们构造的基础是一种基于新原语的见证加密使用技术，我们称之为函数绑定哈希函数(function-binding hash functions)。与某处统计绑定哈希函数将摘要统计绑定到输入的几个比特不同，函数绑定哈希函数将摘要统计绑定到输入函数的输出。正如我们在本研究中所展示的，函数绑定哈希函数为我们提供了新的方法来利用普通见证加密的能力，并将其用作高级密码学原语的基础。最后，我们展示了如何从分层同态加密构建块函数析取的函数绑定哈希函数；这与见证加密相结合产生了我们的主要研究成果。

## 关键词

+ 密码学
+ 零知识
+ 协议