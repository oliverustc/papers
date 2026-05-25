---
title: "Geppetto: Versatile verifiable computation"
标题简称:
论文类型: conference
会议简称: S&P
发表年份: 2015
created: 2025-05-09 14:24:04
modified: 2025-05-09 14:24:30
---

## Geppetto: Versatile verifiable computation

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/7163030)
+ [archive](https://eprint.iacr.org/2014/976)

## 作者

+ Craig Costello
+ Cédric Fournet
+ Jon Howell
+ [Markulf Kohlweiss](Markulf%20Kohlweiss.md)
+ Benjamin Kreuter
+ Michael Naehrig
+ Bryan Parno
+ Samee Zahur

## 笔记

Cloud computing sparked interest in Verifiable Computation protocols, which allow a weak client to securely outsource computations to remote parties. Recent work has dramatically reduced the client's cost to verify the correctness of results, but the overhead to produce proofs largely remains impractical. Geppetto introduces complementary techniques for reducing prover overhead and increasing prover flexibility. With Multi-QAPs, Geppetto reduces the cost of sharing state between computations (e.g., for MapReduce) or within a single computation by up to two orders of magnitude. Via a careful instantiation of cryptographic primitives, Geppetto also brings down the cost of verifying outsourced cryptographic computations (e.g., verifiably computing on signed data); together with Geppetto's notion of bounded proof bootstrapping, Geppetto improves on prior bootstrapped systems by five orders of magnitude, albeit at some cost in universality. Geppetto also supports qualitatively new properties like verifying the correct execution of proprietary (i.e., secret) algorithms. Finally, Geppetto's use of energy-saving circuits brings the prover's costs more in line with the program's actual (rather than worst-case) execution time. Geppetto is implemented in a full-fledged, scalable compiler that consumes LLVM code generated from a variety of apps, as well as a large cryptographic library.

以下是中文翻译：

云计算激发了对可验证计算（Verifiable Computation）协议的研究兴趣，该协议允许弱客户端将计算安全地外包给远程方。近期研究已大幅降低客户端验证结果正确性的成本，但生成证明的开销在很大程度上仍不实用。Geppetto引入了一系列互补技术，用于降低证明者开销并提高证明者的灵活性。通过Multi-QAP技术，Geppetto将计算间（如MapReduce）或单个计算内共享状态的成本降低了高达两个数量级。通过对密码学原语的精心实例化，Geppetto还降低了验证外包密码学计算的成本（例如，对签名数据进行可验证计算）；结合Geppetto的有界证明自举（bounded proof bootstrapping）概念，Geppetto相比先前的自举系统提升了五个数量级，尽管在通用性方面有所损失。Geppetto还支持全新的定性特性，例如验证专有（即保密）算法的正确执行。最后，Geppetto对节能电路的运用使证明者的成本更贴近程序的实际（而非最坏情况）执行时间。Geppetto已被实现为一个完整的、可扩展的编译器，能够处理由各类应用程序生成的LLVM代码，以及一个大型密码学库。

## 关键词

+ 可验证计算
+ Multi-QAP
+ 证明者开销优化
+ 有界证明自举
+ 外包密码学计算
+ LLVM编译器