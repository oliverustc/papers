---
title: "Quadratic span programs and succinct NIZKs without PCPs"
标题简称:
论文类型: conference
会议简称: EUROCRYPT
发表年份: 2013
modified: 2025-04-08 16:40:45
---

## Quadratic span programs and succinct NIZKs without PCPs

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-642-38348-9_37)

## 作者

+ Rosario Gennaro
+ [Craig Gentry](Craig%20Gentry.md)
+ Bryan Parno
+ [Mariana Raykova](Mariana%20Raykova.md)
## 笔记

>**Abstract**
>
>We introduce a new characterization of the NP complexity class, called _Quadratic Span Programs_ (QSPs), which is a natural extension of _span programs_ defined by Karchmer and Wigderson. Our main motivation is the quick construction of succinct, easily verified arguments for NP statements.
>
>To achieve this goal, QSPs use a new approach to the well-known technique of _arithmetization_ of Boolean circuits. Our new approach yields dramatic performance improvements. Using QSPs, we construct a NIZK argument - in the CRS model - for Circuit-SAT consisting of just 7 _group elements_. The CRS size and prover computation are _quasi-linear_, making our scheme seemingly quite practical, a result supported by our implementation. Indeed, our NIZK argument attains the shortest proof, most efficient prover, and most efficient verifier of any known technique. We also present a variant of QSPs, called _Quadratic Arithmetic Programs_ (QAPs), that “naturally” compute _arithmetic_ circuits over large fields, along with succinct NIZK constructions that use QAPs.
>
>Finally, we show how QSPs and QAPs can be used to efficiently and publicly verify outsourced computations, where a client asks a server to compute _F_(_x_) for a given function F and must verify the result provided by the server in considerably less time than it would take to compute F from scratch. The resulting schemes are the most efficient, general purpose publicly verifiable computation schemes.
>
>以下是中文翻译：
>
>我们引入了一种新的NP复杂性类的表征，称为二次跨度程序（Quadratic Span Programs，QSPs），这是Karchmer和Wigderson定义的跨度程序的自然扩展。我们的主要动机是快速构建简洁且易于验证的NP声明的论证。
>
>为了实现这一目标，QSP采用了一种新的方法来处理布尔电路的算术化这一著名技术。我们的新方法带来了显著的性能提升。使用QSP，我们在公共随机字符串（CRS）模型下为电路可满足性问题（Circuit-SAT）构建了一个仅由7个群元素组成的非交互式零知识（NIZK）论证。CRS的大小和证明者的计算量都是准线性的，使我们的方案看起来相当实用，这一结果得到了我们的实现的支持。实际上，我们的NIZK论证达到了已知技术中最短的证明、最有效的证明者和最有效的验证者。我们还提出了一种QSP的变体，称为二次算术程序（Quadratic Arithmetic Programs，QAPs），它“自然”地计算大域上的算术电路，并提供了使用QAP的简洁NIZK构造。
>
>最后，我们展示了如何使用QSP和QAP高效且公开地验证外包计算，其中客户端请求服务器计算给定函数F的F(x)，并且必须在比从头计算F所需的时间显著更短的时间内验证服务器提供的结果。由此产生的方案是最有效的通用公开可验证计算方案。

## 关键词

+ 二次跨度程序
+ 二次算术程序
+ 算术电路
+ 简洁非交互式零知识证明
+ 公开可验证计算