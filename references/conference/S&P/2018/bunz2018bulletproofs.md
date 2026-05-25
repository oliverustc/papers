---
title: "Bulletproofs: Short proofs for confidential transactions and more"
标题简称:
论文类型: conference
会议简称: S&P
发表年份: 2018
modified: 2025-04-22 16:06:33
created: 2025-04-08 17:03:06
---

## Bulletproofs: Short proofs for confidential transactions and more

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/8418611)

## 作者

+ [Benedikt Bünz](Benedikt%20Bünz.md)
+ [Jonathan Bootle](Jonathan%20Bootle.md)
+ [Dan Boneh](Dan%20Boneh.md)
+ Andrew Poelstra
+ Pieter Wuille
+ Greg Maxwell

## 笔记

We propose Bulletproofs, a new non-interactive zero-knowledge proof protocol with very short proofs and without a trusted setup; the proof size is only logarithmic in the witness size. Bulletproofs are especially well suited for efficient range proofs on committed values: they enable proving that a committed value is in a range using only 2 log_2(n)+9 group and field elements, where n is the bit length of the range. Proof generation and verification times are linear in n. Bulletproofs greatly improve on the linear (in n) sized range proofs in existing proposals for confidential transactions in Bitcoin and other cryptocurrencies. Moreover, Bulletproofs supports aggregation of range proofs, so that a party can prove that m commitments lie in a given range by providing only an additive O(log(m)) group elements over the length of a single proof. To aggregate proofs from multiple parties, we enable the parties to generate a single proof without revealing their inputs to each other via a simple multi-party computation (MPC) protocol for constructing Bulletproofs. This MPC protocol uses either a constant number of rounds and linear communication, or a logarithmic number of rounds and logarithmic communication. We show that verification time, while asymptotically linear, is very efficient in practice. The marginal cost of batch verifying 32 aggregated range proofs is less than the cost of verifying 32 ECDSA signatures. Bulletproofs build on the techniques of Bootle et al. (EUROCRYPT 2016). Beyond range proofs, Bulletproofs provide short zero-knowledge proofs for general arithmetic circuits while only relying on the discrete logarithm assumption and without requiring a trusted setup. We discuss many applications that would benefit from Bulletproofs, primarily in the area of cryptocurrencies. The efficiency of Bulletproofs is particularly well suited for the distributed and trustless nature of blockchains. The full version of this article is available on ePrint.

以下是中文翻译：

我们提出了Bulletproofs，这是一种新型的非交互式零知识证明(non-interactive zero-knowledge proof)协议，具有非常短的证明长度，且无需可信设置；证明大小仅为见证规模的对数级别。

Bulletproofs特别适用于对已承诺值进行高效的范围证明：它们能够使用仅2 log_2(n)+9个群元素和域元素来证明一个已承诺的值位于某个范围内，其中n是范围的比特长度。证明的生成和验证时间与n呈线性关系。Bulletproofs极大地改进了比特币和其他加密货币中现有机密交易方案中呈线性大小(与n相关)的范围证明。

此外，Bulletproofs支持范围证明的聚合，使得一方可以通过仅提供单个证明长度的O(log(m))个附加群元素，来证明m个承诺值都位于给定范围内。为了聚合来自多方的证明，我们通过一个简单的多方计算(MPC)协议使各方能够生成单个证明，而无需相互透露输入。该MPC协议可以使用恒定轮数和线性通信量，或对数轮数和对数通信量。

我们表明，虽然验证时间在渐近意义上是线性的，但在实践中非常高效。批量验证32个聚合范围证明的边际成本低于验证32个ECDSA签名的成本。Bulletproofs建立在Bootle等人(EUROCRYPT 2016)的技术基础之上。除了范围证明，Bulletproofs还为一般算术电路提供简短的零知识证明，仅依赖离散对数假设且无需可信设置。

我们讨论了许多可从Bulletproofs中受益的应用，主要在加密货币领域。Bulletproofs的效率特别适合区块链的分布式和去信任特性。本文的完整版本可在ePrint上获取。

## 关键词

+ Bulletproofs
+ 范围证明
+ 非交互式零知识证明
+ 保密交易
+ 无可信设置
+ 离散对数假设