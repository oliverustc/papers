---
title: "Jager: Automated Telephone Call Traceback"
doi: 10.1145/3658644.3690290
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2024
---
## Jager: Automated Telephone Call Traceback

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3658644.3690290)

## 作者

+ David Adei 
+ Varun Madathil 
+ Sathvik Prasad 
+ Bradley Reaves 
+ Alessandra Scafuro 


## 笔记

Unsolicited telephone calls that facilitate fraud or unlawful telemarketing continue to overwhelm network users and the regulators who prosecute them. The first step in prosecuting phone abuse is traceback --- identifying the call originator. This fundamental investigative task currently requires hours of manual effort per call. In this paper, we introduce Jäger, a distributed secure call traceback system. Jäger can trace a call in a few seconds, even with partial deployment, while cryptographically preserving the privacy of call parties, carrier trade secrets like peers and call volume, and limiting the threat of bulk analysis. We establish definitions and requirements of secure traceback, then develop a suite of protocols that meet these requirements using witness encryption, oblivious pseudorandom functions, and group signatures. We prove these protocols secure in the universal composibility framework. We then demonstrate that Jäger has low compute and bandwidth costs per call, and these costs scale linearly with call volume. Jäger provides an efficient, secure, privacy-preserving system to revolutionize telephone abuse investigation with minimal costs to operators

以下是中文翻译：

非法电话骚扰（包括诈骗电话和违规电话营销）持续困扰着网络用户及负责追诉的监管机构。追诉电话滥用行为的第一步是溯源——即确定通话发起方。这项基本调查工作目前每通电话需要数小时的人工操作。在本文中，我们介绍了 Jäger，一个分布式安全通话溯源系统。Jäger 能够在数秒内完成通话追踪，即使在部分部署的情况下也能正常工作，同时通过密码学手段保护通话各方的隐私、运营商的商业机密（如对等节点信息和通话量），并限制批量分析的威胁。我们建立了安全溯源的定义与需求，并基于见证加密（witness encryption）、遗忘伪随机函数（oblivious pseudorandom functions）和群签名（group signatures）开发了一套满足上述需求的协议。我们在通用可组合性（UC）框架下证明了这些协议的安全性。进一步地，我们证明 Jäger 每通电话的计算和带宽开销极低，且这些开销随通话量线性增长。Jäger 为运营商以极低成本提供了一个高效、安全、保护隐私的系统，有望彻底变革电话滥用调查方式。

## 关键词

+ 电话呼叫追溯
+ 自动化追踪
+ 网络欺诈检测
+ 语音网络安全
+ 身份认证