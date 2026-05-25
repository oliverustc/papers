---
title: "Ghostor: Toward a Secure Data-Sharing System from Decentralized Trust"
标题简称:
论文类型: conference
会议简称: NSDI
发表年份: 2020
created: 2025-04-27 09:14:53
modified: 2025-04-27 09:20:04
---

## Ghostor: Toward a Secure Data-Sharing System from Decentralized Trust

## 发表信息

+ [原文链接](https://www.usenix.org/conference/nsdi20/presentation/hu-yuncong)

## 作者

+ [Yuncong Hu](Yuncong%20Hu.md) 
+ Sam Kumar 
+ [Raluca Ada Popa](Raluca%20Ada%20Popa.md)

## 笔记

Data-sharing systems are often used to store sensitive data. Both academia and industry have proposed numerous solutions to protect the user privacy and data integrity from a compromised server. Practical state-of-the-art solutions, however, use weak threat models based on centralized trust—they assume that part of the server will remain uncompromised, or that the adversary will not perform active attacks. We propose Ghostor, a data-sharing system that, using only decentralized trust, (1) hides user identities from the server, and (2) allows users to detect server-side integrity violations. To achieve (1), Ghostor avoids keeping any per-user state at the server, requiring us to redesign the system to avoid common paradigms like per-user authentication and user-specific mailboxes. To achieve (2), Ghostor develops a technique called verifiable anonymous history. Ghostor leverages a blockchain rarely, publishing only a single hash to the blockchain for the entire system once every epoch. We measured that Ghostor incurs a 4–5x throughput overhead compared to an insecure baseline. Although significant, Ghostor's overhead may be worth it for security- and privacy-sensitive applications.

以下是中文翻译：

数据共享系统通常用于存储敏感数据。学术界和工业界已经提出了许多解决方案来保护用户隐私和数据完整性，以防服务器被攻破。然而，当前实用的最先进解决方案都使用基于中心化信任的弱威胁模型——它们假设部分服务器将保持未被攻破，或者攻击者不会进行主动攻击。我们提出了Ghostor，这是一个仅使用去中心化信任的数据共享系统，它能够(1)对服务器隐藏用户身份，以及(2)允许用户检测服务器端的完整性违规。为了实现目标(1)，Ghostor避免在服务器端保存任何针对单个用户的状态，这要求我们重新设计系统以避免使用常见的范式，如针对单个用户的身份认证和用户特定的邮箱。为了实现目标(2)，Ghostor开发了一种称为"可验证匿名历史"(verifiable anonymous history)的技术。Ghostor很少使用区块链，每个周期(epoch)仅向区块链发布整个系统的单个哈希值。我们的测量表明，与不安全的基准系统相比，Ghostor的吞吐量开销为4-5倍。尽管这种开销很大，但对于注重安全性和隐私性的应用来说，Ghostor的开销可能是值得的。

## 关键词

+ 去中心化信任
+ 数据共享系统
+ 用户身份隐藏
+ 可验证匿名历史
+ 完整性验证
+ 区块链轻量应用