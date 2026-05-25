---
title: "ElectionGuard: a Cryptographic Toolkit to Enable Verifiable Elections"
标题简称: 
论文类型: conference
undefined: USENIX Security
发表年份: 2025
created: 2025-05-07 21:51:58
modified: 2025-05-07 21:53:57
---

## ElectionGuard: a Cryptographic Toolkit to Enable Verifiable Elections

## 发表信息

+ [原文链接](https://www.usenix.org/conference/usenixsecurity24/presentation/benaloh)

## 作者

+ Josh Benaloh 
+ Michael Naehrig 
+ Olivier Pereira 
+ Dan S Wallach 

## 笔记

ElectionGuard is a flexible set of open-source tools that—when used with traditional election systems—can produce end-to-end verifiable elections whose integrity can be verified by observers, candidates, media, and even voters themselves. ElectionGuard has been integrated into a variety of systems and used in actual public U.S. elections in Wisconsin, California, Idaho, Utah, and Maryland as well as in caucus elections in the U.S. Congress. It has also been used for civic voting in the Paris suburb of Neuilly-sur-Seine and for an online election by a Switzerland/Denmark-based organization.

The principal innovation of ElectionGuard is the separation of the cryptographic tools from the core mechanics and user interfaces of voting systems. This separation allows the cryptography to be designed and built by security experts without having to re-invent and replace the existing infrastructure. Indeed, in its preferred deployment, ElectionGuard does not replace the existing vote counting infrastructure but instead runs alongside and produces its own independently-verifiable tallies. Although much of the cryptography in ElectionGuard is, by design, not novel, some significant innovations are introduced which greatly simplify the process of verification.

This paper describes the design of ElectionGuard, its innovations, and many of the learnings from its implementation and growing number of real-world deployments.

以下是中文翻译：

ElectionGuard是一套灵活的开源工具，当与传统选举系统结合使用时，可以实现端到端可验证的选举，其完整性可以被观察员、候选人、媒体，甚至选民自己验证。ElectionGuard已被整合到多个系统中，并在美国威斯康星州、加利福尼亚州、爱达荷州、犹他州和马里兰州的实际公共选举中使用，同时也在美国国会的党团选举中得到应用。此外，它还被用于法国巴黎郊区纳伊苏塞纳（Neuilly-sur-Seine）的公民投票，以及一个总部位于瑞士/丹麦的组织的在线选举。

ElectionGuard的主要创新在于将密码学工具与投票系统的核心机制和用户界面分离。这种分离使得密码学可以由安全专家设计和构建，而无需重新发明和替换现有基础设施。事实上，在其首选部署方式中，ElectionGuard并不替代现有的计票基础设施，而是与之并行运行，并产生其自身独立可验证的计票结果。虽然ElectionGuard中的大部分密码学技术在设计上并非创新，但它引入了一些重要的创新，这些创新大大简化了验证过程。

本文描述了ElectionGuard的设计、其创新点，以及从其实施和日益增多的实际部署中获得的诸多经验教训。

## 关键词

+ ElectionGuard可验证选举工具包
+ 端到端选举可验证性
+ 密码学投票系统设计
+ 选举完整性与隐私保护
+ 开源选举基础设施
+ 实际选举部署经验