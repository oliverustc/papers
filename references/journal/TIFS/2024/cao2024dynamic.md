---
title: "Dynamic Group Time-Based One-Time Passwords"
doi: 10.1109/tifs.2024.3386350
标题简称:
论文类型: journal
期刊简称: TIFS
发表年份: 2024
created: 2025-05-13 05:36:42
modified: 2025-05-13 05:37:30
---
## Dynamic Group Time-Based One-Time Passwords

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/10494770)

## 作者

+ Xuelian Cao
+ Zheng Yang
+ Jianting Ning
+ Chenglu Jin
+ Rongxing Lu
+ Zhiming Liu
+ Jianying Zhou

## 笔记

Group time-based one-time passwords (GTOTP) is a novel lightweight cryptographic primitive for achieving anonymous client authentication, which enables the efficient generation of time-based one-time passwords on behalf of a group without revealing any information about the actual client’s identity beyond their group membership. The security properties of GTOTP regarding anonymity and traceability have been formulated in a static group management setting (where all group members should be determined during the group initialization phase), yet, a formal treatment for real-world dynamic groups (i.e., group members may join and leave at any time) is still an open question. It is non-trivial to construct an efficient GTOTP scheme that can provide a lightweight password generation procedure run by group members and support dynamic group management, allowing group members to join and leave without affecting other members’ states (non-disruptively). To address the above challenge, we first define the notion and the security model of dynamic group time-based one-time passwords (DGTOTP) in this work. We then present an efficient DGTOTP construction that can generically transform an asymmetric time-based one-time passwords scheme into a DGTOTP scheme utilizing a chameleon hash function family and a Merkle tree scheme. Within our construction, we particularly tailor an outsourcing solution realizing an issue-first-and-join-later (IFJL) strategy, enabling smooth joining and revocation without disrupting other group members. Moreover, our scheme minimizes symmetric cryptographic operations and maintains constant storage for group members, compared to the linear storage cost that grows rapidly with respect to the lifetime of the GTOTP instance in the previous static GTOTP scheme. Our DGTOTP scheme satisfies stronger security guarantees in a dynamic group management setting without random oracles. Our experimental results confirm the efficiency of our DGTOTP scheme.

以下是中文翻译：

群组时间基一次性密码(Group time-based one-time passwords, GTOTP)是一种新型的轻量级密码原语，用于实现匿名客户端认证，它能够高效地代表群组生成基于时间的一次性密码，除了群组成员身份外不会泄露任何关于实际客户端身份的信息。GTOTP关于匿名性和可追踪性的安全属性已在静态群组管理设置（即所有群组成员需要在群组初始化阶段确定）中得到阐述，然而，对于现实世界中的动态群组（即群组成员可以随时加入和离开）的形式化处理仍是一个开放性问题。构建一个能够为群组成员提供轻量级密码生成程序并支持动态群组管理的高效GTOTP方案并非易事，该方案需要允许群组成员在不影响其他成员状态的情况下加入和离开（非中断性）。

为了应对上述挑战，我们首先在本工作中定义了动态群组时间基一次性密码(Dynamic Group Time-based One-Time Passwords, DGTOTP)的概念和安全模型。然后，我们提出了一个高效的DGTOTP构造方案，该方案可以利用变色龙哈希函数族(chameleon hash function family)和默克尔树方案(Merkle tree scheme)将非对称时间基一次性密码方案泛化转换为DGTOTP方案。在我们的构造中，我们特别设计了一个外包解决方案，实现了先发行后加入(issue-first-and-join-later, IFJL)策略，使得成员加入和撤销能够顺畅进行，而不会干扰其他群组成员。此外，与之前静态GTOTP方案中随GTOTP实例生命周期快速增长的线性存储开销相比，我们的方案最小化了对称密码操作并为群组成员维持恒定存储。

我们的DGTOTP方案在动态群组管理设置中满足更强的安全保证，且不依赖随机预言机。我们的实验结果证实了DGTOTP方案的效率。

## 关键词

+ 动态群组时间基一次性密码DGTOTP
+ 匿名客户端认证轻量级原语
+ 变色龙哈希默克尔树动态管理
+ 先发行后加入IFJL策略
+ 非中断成员加入撤销
+ 标准模型动态群组安全