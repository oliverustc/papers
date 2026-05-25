---
title: "Traceable ring signature"
标题简称:
论文类型: conference
会议简称: PKC
发表年份: 2007
created: 2025-05-12 08:37:37
modified: 2025-05-12 08:44:38
---

## Traceable ring signature

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-540-71677-8_13)
+ [archive](https://eprint.iacr.org/2006/389)

## 作者

+ Eiichiro Fujisaki
+ Koutarou Suzuki

## 笔记

The ring signature allows a signer to leak secrets anonymously, without the risk of identity escrow. At the same time, the ring signature provides great flexibility: No group manager, no special setup, and the dynamics of group choice. The ring signature is, however, vulnerable to malicious or irresponsible signers in some applications, because of its anonymity. In this paper, we propose a traceable ring signature scheme. A traceable ring scheme is a ring signature except that it can restrict "excessive" anonymity. The traceable ring signature has a tag that consists of a list of ring members and an issue that refers to, for instance, a social affair or an election. A ring member can make any signed but anonymous opinion regarding the issue, but only once (per tag). If the member submits another signed opinion, possibly pretending to be another person who supports the first opinion, the identity of the member is immediately revealed. If the member submits the same opinion, for instance, voting "yes" regarding the same issue twice, everyone can see that these two are linked. The traceable ring signature can suit to many applications, such as an anonymous voting on a BBS, a dishonest whistle-blower problem, and unclonable group identification. We formalize the security definitions for this primitive and show an efficient and simple construction.

以下是中文翻译：

环签名（ring signature）允许签名者匿名泄露秘密，而不存在身份托管的风险。与此同时，环签名还具有极大的灵活性：无需群管理者，无需特殊设置，且群成员的选择是动态的。然而，由于其匿名性，环签名在某些应用场景中容易受到恶意或不负责任的签名者的攻击。

在本文中，我们提出了一种可追踪环签名（traceable ring signature）方案。可追踪环签名本质上是一种环签名，但它能够限制"过度"的匿名性。可追踪环签名包含一个标签（tag），该标签由环成员列表和一个议题（issue）组成，议题可指代某一社会事件或选举。环成员可以就该议题发表任意已签名但匿名的意见，但每个标签只能发表一次。若该成员再次提交签名意见——例如伪装成另一位支持第一个意见的人——其身份将立即被揭露。若该成员就同一议题提交了相同的意见（如两次投票"赞成"），则所有人均可看出这两条意见存在关联。可追踪环签名适用于多种应用场景，例如BBS上的匿名投票、不诚实举报者问题以及不可克隆的群组身份认证。我们对该原语的安全定义进行了形式化，并给出了一种高效且简洁的构造方案。

## 关键词

+ 可追踪环签名
+ 环签名
+ 匿名性限制
+ 双重签名检测
+ 匿名投票
+ 过度匿名防护