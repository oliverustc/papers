---
title: "Membership privacy for fully dynamic group signatures"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2019
created: 2025-05-09 14:51:29
modified: 2025-05-09 14:52:26
---

## Membership privacy for fully dynamic group signatures

## 发表信息

+ [原文链接](https://dl.acm.org/doi/10.1145/3319535.3354257)

## 作者

+ Michael Backes
+ [Lucjan Hanzlik](Lucjan%20Hanzlik.md)
+ Jonas Schneider-Bensch

## 笔记

Group signatures present a compromise between the traditional goals of digital signatures and the need for signer privacy, allowing for the creation of unforgeable signatures in the name of a group which reveal nothing about the actual signer's identity beyond their group membership. An important consideration that is absent in prevalent models is that group membership itself may be sensitive information, especially if group membership is dynamic, i.e. membership status may change over time. We address this issue by introducing formal notions of membership privacy for fully dynamic group signature schemes, which can be easily integrated into the most expressive models of group signature security to date. We then propose a generic construction for a fully dynamic group signature scheme with membership privacy that is based on signatures with flexible public key (SFPK) and signatures on equivalence classes (SPSEQ). Finally, we devise novel techniques for SFPK to construct a highly efficient standard model scheme (i.e. without random oracles) that provides shorter signatures than even the non-private state-of-the-art from standard assumptions. This shows that, although the strictly stronger security notions we introduce have been completely unexplored in the study of fully dynamic group signatures so far, they do not come at an additional cost in practice.

以下是中文翻译：

群签名在传统数字签名目标与签名者隐私需求之间提供了一种折衷方案，允许以群体名义创建不可伪造的签名，同时不透露关于实际签名者身份的信息，除了他们的群体成员身份。一个在现有模型中缺失的重要考虑是，群体成员身份本身可能是敏感信息，特别是当群体成员身份是动态的，即成员状态可能随时间变化时。我们通过引入完全动态群签名方案的成员隐私（membership privacy）正式概念来解决这一问题，这可以轻松集成到迄今为止最具表现力的群签名安全模型中。接着，我们提出了一种基于灵活公钥签名（SFPK）和等价类签名（SPSEQ）的完全动态群签名方案的通用构造，具有成员隐私。最后，我们设计了新的SFPK技术，以构建一个高效的标准模型方案（即不使用随机预言机），该方案提供的签名比现有非隐私的最先进方案更短，且基于标准假设。这表明，尽管我们引入的更强安全概念在完全动态群签名的研究中尚未得到探索，但在实践中并不会带来额外的成本。

## 关键词

+ 群签名
+ 成员隐私
+ 动态群
+ 灵活公钥签名
+ 隐私保护