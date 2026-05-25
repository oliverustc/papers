---
title: "Homomorphic time-lock puzzles and applications"
标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 2019
created: 2025-04-28 16:55:15
modified: 2025-04-28 16:58:48
---

## Homomorphic time-lock puzzles and applications

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-030-26948-7_22)
+ [archive](https://eprint.iacr.org/2019/635)

## 作者

+ [Giulio Malavolta](Giulio%20Malavolta.md)
+ Sri Aravinda Krishnan Thyagarajan 

## 笔记

Time-lock puzzles allow one to encrypt messages for the future, by efficiently generating a puzzle with a solution s that remains hidden until time T has elapsed. The solution is required to be concealed from the eyes of any algorithm running in (parallel) time less than T. We put forth the concept of \emph{homomorphic time-lock puzzles}, where one can evaluate functions over puzzles without solving them, i.e., one can manipulate a set of puzzles with solutions (s1,…,sn) to obtain a puzzle that solves to f(s1,…,sn), for any function f. We propose candidate constructions under concrete cryptographic assumptions for different classes of functions. Then we show how homomorphic time-lock puzzles overcome the limitations of classical time-lock puzzles by proposing new protocols for applications of interest, such as e-voting, multi-party coin flipping, and fair contract signing.

以下是中文翻译：

时间锁谜题(time-lock puzzles)允许人们通过高效生成一个谜题来对未来的消息进行加密，其解决方案s在时间T经过之前都保持隐藏状态。该解决方案需要对任何运行时间少于T的（并行）算法保持隐蔽。我们提出了同态时间锁谜题(homomorphic time-lock puzzles)的概念，在这种谜题中，人们可以在不解决谜题的情况下对谜题进行函数运算，即可以操作一组解决方案为(s1,…,sn)的谜题，以获得一个解决方案为f(s1,…,sn)的谜题，其中f可以是任意函数。我们基于具体的密码学假设，针对不同类别的函数提出了候选构造方案。然后，我们展示了同态时间锁谜题如何克服经典时间锁谜题的局限性，通过提出新的协议来应用于一些感兴趣的领域，如电子投票(e-voting)、多方抛硬币(multi-party coin flipping)和公平合同签署(fair contract signing)。

## 关键词

+ 密码学
+ 零知识
+ 协议