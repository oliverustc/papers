---
title: "Secure multiparty computation from threshold encryption based on class groups"

标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 2023
modified: 2025-04-28 17:09:56
created: 2025-04-11 13:58:19
---

## Secure multiparty computation from threshold encryption based on class groups

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-38557-5_20)

## 作者

+ Lennart Braun 
+ Ivan Damgård 
+ [Claudio Orlandi](Claudio%20Orlandi.md)
## 笔记

We construct the first actively-secure threshold version of the cryptosystem based on class groups from the so-called CL framework (Castagnos and Laguillaumie, 2015).

We show how to use our threshold scheme to achieve general universally composable (UC) secure multiparty computation (MPC) with only transparent set-up, i.e., with no secret trapdoors involved.

On the way to our goal, we design new zero-knowledge (ZK) protocols with constant communication complexity for proving multiplicative relations between encrypted values. This allows us to use the ZK proofs to achieve MPC with active security with only a constant factor overhead.

Finally, we adapt our protocol for the so called “You-Only-Speak-Once” (YOSO) setting, which is a very promising recent approach for performing MPC over a blockchain. This is possible because our key generation protocol is simpler and requires significantly less interaction compared to previous approaches: in particular, our new key generation protocol allows the adversary to bias the public key, but we show that this has no impact on the security of the resulting cryptosystem.

以下是中文翻译：

我们构建了第一个基于类群的加密系统的主动安全阈值版本，该系统基于所谓的CL框架（Castagnos和Laguillaumie，2015）。

我们展示了如何利用我们的阈值方案实现一般的可普遍组合（UC）安全多方计算（MPC），仅需透明设置，即不涉及任何秘密陷阱。

在实现目标的过程中，我们设计了新的零知识（ZK）协议，具有恒定的通信复杂度，用于证明加密值之间的乘法关系。这使我们能够利用ZK证明以恒定的额外开销实现具有主动安全性的MPC。

最后，我们将我们的协议适配到所谓的“你只说一次”（YOSO）设置，这是一种在区块链上执行MPC的非常有前景的新方法。这是可能的，因为我们的密钥生成协议比以前的方法更简单，并且需要的交互显著减少：特别是，我们的新密钥生成协议允许对手对公钥施加偏差，但我们证明这对所得到的加密系统的安全性没有影响。

## 关键词

+ 类群阈值加密主动安全MPC
+ CL框架类群密码系统门限化
+ 乘法关系恒定通信ZK证明
+ UC安全MPC透明设置无陷门
+ YOSO区块链MPC密钥生成