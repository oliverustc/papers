---
title: "Piano: extremely simple, single-server PIR with sublinear server computation"
标题简称:
论文类型: conference
会议简称: S&P
发表年份: 2024
created: 2025-04-27 09:27:28
modified: 2025-04-27 09:33:20
---

## Piano: extremely simple, single-server PIR with sublinear server computation

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/10646686)

## 作者

+ Mingxun Zhou 
+ Andrew Park 
+ [Wenting Zheng](Wenting%20Zheng.md)
+ [Elaine Shi](Elaine%20Shi.md)
## 笔记

We construct a sublinear-time single-server preprocessing Private Information Retrieval (PIR) scheme with an optimal tradeoff between client storage and server computation (up to poly-logarithmic factors). Our scheme achieves amortized $\tilde{O}(\sqrt{n})$ server and client computation and $O(\sqrt{n})$ online communication per query, and requires $\tilde{O}_{\lambda}(\sqrt{n})$ client storage. Unlike prior single-server PIR schemes that rely on heavy cryptographic machinery such as Homomorphic Encryption, our scheme relies only on Pseudo-Random Functions (PRF). To the best of our knowledge, Piano is the first practical single-server sublinear-time PIR scheme, and we outperform the state-of-the-art single-server PIR by 10×-300×. In comparison with the best known two-server PIR scheme, Piano enjoys comparable performance but our construction is considerably simpler. Experimental results show that for a 100GB database and with 60ms round-trip latency, Piano achieves 93ms response time, while the best known prior scheme requires 11s or more.

以下是中文翻译：

我们构建了一个次线性时间的单服务器预处理隐私信息检索(Private Information Retrieval, PIR)方案，该方案在客户端存储和服务器计算之间实现了最优权衡(在多对数因子范围内)。我们的方案在每次查询中实现了摊销的$\tilde{O}(\sqrt{n})$服务器和客户端计算复杂度，$O(\sqrt{n})$在线通信复杂度，并且需要$\tilde{O}_{\lambda}(\sqrt{n})$客户端存储空间。与之前依赖同态加密(Homomorphic Encryption)等重型密码学工具的单服务器PIR方案不同，我们的方案仅依赖伪随机函数(Pseudo-Random Functions, PRF)。据我们所知，Piano是首个实用的单服务器次线性时间PIR方案，其性能比现有最先进的单服务器PIR方案提高了10到300倍。与已知最佳的双服务器PIR方案相比，Piano具有相当的性能，但我们的构造方案明显更简单。实验结果表明，对于100GB的数据库，在60ms往返延迟的情况下，Piano实现了93ms的响应时间，而此前最佳方案需要11秒或更长时间。

## 关键词

+ 单服务器私有信息检索
+ 次线性时间PIR
+ 伪随机函数
+ 预处理PIR
+ 隐私数据库查询
+ 最优存储计算权衡