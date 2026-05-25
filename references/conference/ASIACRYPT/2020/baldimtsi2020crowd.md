---
title: "Crowd verifiable zero-knowledge and end-to-end verifiable multiparty computation"
标题简称:
论文类型: conference
会议简称: ASIACRYPT
发表年份: 2020
---

## Crowd verifiable zero-knowledge and end-to-end verifiable multiparty computation

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-030-64840-4_24)

## 作者

+ [Foteini Baldimtsi](Foteini%20Baldimtsi.md) 
+ Aggelos Kiayias 
+ Thomas Zacharias 
+ Bingsheng Zhang 


## 笔记

Auditing a secure multiparty computation (MPC) protocol entails the validation of the protocol transcript by a third party that is otherwise untrusted. In this work, we introduce the concept of _end-to-end verifiable_ MPC (VMPC), that requires the validation to provide a correctness guarantee even in the setting that all servers, trusted setup primitives and all the client systems utilized by the input-providing users of the MPC protocol are subverted by an adversary. To instantiate VMPC, we introduce a new concept in the setting of zero-knowlegde protocols that we term _crowd verifiable zero-knowledge_ (CVZK). A CVZK protocol enables a prover to convince a set of verifiers about a certain statement, even though each one individually contributes a small amount of entropy for verification and some of them are adversarially controlled. Given CVZK, we present a VMPC protocol that is based on discrete-logarithm related assumptions. At the high level of adversity that VMPC is meant to withstand, it is infeasible to ensure perfect correctness, thus we investigate the classes of functions and verifiability relations that are feasible in our framework, and present a number of possible applications the underlying functions of which can be implemented via VMPC.


以下是中文翻译：

审计（Auditing）安全多方计算（MPC）协议需要由第三方对协议记录进行验证，而该第三方本身是不可信的。在本研究中，我们提出了端到端可验证多方计算（VMPC）的概念，其要求即使在以下极端情况下仍能提供正确性保证：所有服务器、可信初始化原语以及MPC协议中提供输入的用户所使用的全部客户端系统均被攻击者篡改。

为实现VMPC，我们在零知识协议框架下提出了名为群体可验证零知识（CVZK）的新概念。CVZK协议使证明者能够向一组验证者证实某个陈述的真实性——尽管每个验证者仅贡献少量熵值进行验证，且其中部分验证者可能被恶意控制。基于CVZK协议，我们提出了一种基于离散对数相关假设的VMPC协议。在VMPC设计应对的高度对抗环境下，确保完全正确性是不可行的，因此我们研究了该框架下可行的函数类与可验证关系，并提出了若干可通过VMPC实现其底层功能的潜在应用场景。

## 关键词

+ 端到端可验证多方计算
+ 群体可验证零知识
+ 离散对数假设
+ 协议审计
+ 可验证关系