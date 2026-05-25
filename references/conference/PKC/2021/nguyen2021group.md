---
title: "Group encryption: full dynamicity, message filtering and code-based instantiation"
标题简称:
论文类型: conference
会议简称: PKC
发表年份: 2021
created: 2025-05-13 05:40:32
modified: 2025-05-13 05:41:51
---

## Group encryption: full dynamicity, message filtering and code-based instantiation

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-030-75248-4_24)

## 作者

+ [Khoa Nguyen](Khoa%20Nguyen.md)
+ Reihaneh Safavi-Naini
+ [Willy Susilo](Willy%20Susilo.md)
+ [Huaxiong Wang](Huaxiong%20Wang.md)
+ [Yanhong Xu](Yanhong%20Xu.md)
+ Neng Zeng

## 笔记

Group encryption (GE), introduced by Kiayias, Tsiounis and Yung (Asiacrypt’07), is the encryption analogue of group signatures. It allows to send verifiably encrypted messages satisfying certain requirements to certified members of a group, while keeping the anonymity of the receivers. Similar to the tracing mechanism in group signatures, the receiver of any ciphertext can be identified by an opening authority - should the needs arise. The primitive of GE is motivated by a number of interesting privacy-preserving applications, including the filtering of encrypted emails sent to certified members of an organization.

This paper aims to improve the state-of-affairs of GE systems. Our first contribution is the formalization of fully dynamic group encryption (FDGE) - a GE system simultaneously supporting dynamic user enrolments and user revocations. The latter functionality for GE has not been considered so far. As a second contribution, we realize the message filtering feature for GE based on a list of _t_-bit keywords and 2 commonly used policies: “permissive” - accept the message if it contains at least one of the keywords as a substring; “prohibitive” - accept the message if all of its _t_-bit substrings are at Hamming distance at least _d_ from all keywords, for $d \ge 1$. This feature so far has not been substantially addressed in existing instantiations of GE based on DCR, DDH, pairing-based and lattice-based assumptions. Our third contribution is the first instantiation of GE under code-based assumptions. The scheme is more efficient than the lattice-based construction of Libert et al. (Asiacrypt’16) - which, prior to our work, is the only known instantiation of GE under post-quantum assumptions. Our scheme supports the 2 suggested policies for message filtering, and in the random oracle model, it satisfies the stringent security notions for FDGE that we put forward.

以下是中文翻译：

群加密(Group encryption, GE)由Kiayias、Tsiounis和Yung(Asiacrypt'07)首次提出，是群签名的加密对应物。它允许向群组的认证成员发送可验证的加密消息，同时保持接收者的匿名性。与群签名中的追踪机制类似，在必要时，开启权限机构可以识别任何密文的接收者。GE原语的提出源于许多有趣的隐私保护应用，包括对发送给组织认证成员的加密邮件进行过滤。

本文旨在改进GE系统的现状。我们的第一个贡献是形式化完全动态群加密(Fully Dynamic Group Encryption, FDGE)——一个同时支持动态用户注册和用户撤销的GE系统。GE的后一种功能迄今尚未被考虑。作为第二个贡献，我们基于_t_位关键词列表和两个常用策略实现了GE的消息过滤功能："允许性"——如果消息包含至少一个关键词作为子串则接受该消息；"禁止性"——如果消息的所有_t_位子串与所有关键词的汉明距离至少为_d_(其中$d \ge 1$)则接受该消息。这一功能在现有基于DCR、DDH、配对和格基假设的GE实例中尚未得到实质性解决。我们的第三个贡献是首次基于编码假设(code-based assumptions)实现GE。该方案比Libert等人(Asiacrypt'16)的格基构造更加高效——在我们的工作之前，后者是唯一已知的基于后量子假设的GE实例。我们的方案支持上述两种消息过滤策略，并且在随机预言机模型中，满足我们提出的FDGE严格安全性定义。

## 关键词

+ 群加密
+ 完全动态群加密（FDGE）
+ 消息过滤
+ 编码假设
+ 后量子密码学
+ 用户撤销机制