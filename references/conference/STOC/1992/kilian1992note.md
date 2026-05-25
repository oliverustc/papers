---
title: "A note on efficient zero-knowledge proofs and arguments"
标题简称:
论文类型: conference
会议简称: STOC
发表年份: 1992
modified: 2025-04-08 11:48:28
---

## A note on efficient zero-knowledge proofs and arguments

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/129712.129782)

## 作者

+ Joe Kilian

## 笔记

>**Abstract**
>In this note, we present new zero-knowledge interactive proofs and arguments for languages in NP. To show that x ε L, with an error probability of at most 2-k, our zero-knowledge proof system requires O(|x|c1)+O(lgc2|x|)k ideal bit commitments, where c1 and c2 depend only on L. This construction is the first in the ideal bit commitment model that achieves large values of k more efficiently than by running k independent iterations of the base interactive proof system. Under suitable complexity assumptions, we exhibit zero knowledge arguments that require O(lgc|x|kl bits of communication, where c depends only on L, and l is the security parameter for the prover. This is the first construction in which the total amount of communication can be less than that needed to transmit the NP witness. Our protocols are based on efficiently checkable proofs for NP[4].

以下是中文翻译：

在这篇文章中，我们提出了针对NP语言的新零知识交互证明和论证。为了证明 \( x \in L \)，在错误概率最多为 \( 2^{-k} \) 的情况下，我们的零知识证明系统需要 \( O(|x|^{c_1}) + O(\log c_2 |x|) k \) 个理想比特承诺，其中 \( c_1 \) 和 \( c_2 \) 仅依赖于 \( L \)。该构造是在理想比特承诺模型中首次以比运行 \( k \) 次独立的基础交互证明系统更高效的方式实现较大值的 \( k \)。在适当的复杂性假设下，我们展示了零知识论证，要求 \( O(\log c |x| k l) \) 位的通信，其中 \( c \) 仅依赖于 \( L \)，而 \( l \) 是证明者的安全参数。这是首次构造出总通信量可以少于传输NP证人所需量的情况。我们的协议基于对NP的高效可验证证明。

## 关键词

+ 简洁零知识论证
+ 理想比特承诺模型
+ NP语言交互证明
+ 通信复杂度次线性
+ 高效可验证证明
+ 零知识证明系统