---
title: "Delay encryption"
标题简称:
论文类型: conference
会议简称: EUROCRYPT
发表年份: 2021
created: 2025-04-28 17:17:57
modified: 2025-04-28 17:18:21
---

## Delay encryption

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-030-77870-5_11)

## 作者

+ Jeffrey Burdges 
+ Luca De Feo 

## 笔记

We introduce a new primitive named Delay Encryption, and give an efficient instantiation based on isogenies of supersingular curves and pairings. Delay Encryption is related to Time-lock Puzzles and Verifiable Delay Functions, and can be roughly described as “time-lock identity based encryption”. It has several applications in distributed protocols, such as sealed bid Vickrey auctions and electronic voting.

We give an instantiation of Delay Encryption by modifying Boneh and Frankiln’s IBE scheme, where we replace the master secret key by a long chain of isogenies, as in the isogeny VDF of De Feo, Masson, Petit and Sanso. Similarly to the isogeny-based VDF, our Delay Encryption requires a trusted setup before parameters can be safely used; our trusted setup is identical to that of the VDF, thus the same parameters can be generated once and shared for many executions of both protocols, with possibly different delay parameters.

We also discuss several topics around delay protocols based on isogenies that were left untreated by De Feo _et al._, namely: distributed trusted setup, watermarking, and implementation issues.

以下是中文翻译：

我们提出了一种名为延迟加密(Delay Encryption)的新原语，并基于超奇异曲线(supersingular curves)的同源映射(isogenies)和配对(pairings)给出了一个高效的实例化方案。延迟加密与时间锁难题(Time-lock Puzzles)和可验证延迟函数(Verifiable Delay Functions)相关，可以粗略地描述为"时间锁基于身份的加密"。它在分布式协议中有多种应用，例如密封投标维克里拍卖(sealed bid Vickrey auctions)和电子投票。

我们通过修改Boneh和Franklin的IBE方案给出了延迟加密的一个实例化方案，其中我们用一个长的同源映射链替换了主密钥，这类似于De Feo、Masson、Petit和Sanso提出的基于同源映射的VDF。与基于同源映射的VDF类似，我们的延迟加密在参数可以安全使用之前需要可信设置(trusted setup)；我们的可信设置与VDF的相同，因此可以一次性生成相同的参数并在两种协议的多次执行中共享使用，且可以使用不同的延迟参数。

我们还讨论了De Feo等人未涉及的几个基于同源映射的延迟协议相关主题，即：分布式可信设置、水印(watermarking)和实现问题。

## 关键词

+ 延迟加密
+ 超奇异曲线同源映射
+ 可验证延迟函数
+ 基于身份的加密
+ 密封投标拍卖