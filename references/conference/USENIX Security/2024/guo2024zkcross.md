---
title: "zkCross: A novel architecture for Cross-ChainPrivacy-Preserving auditing"
标题简称:
论文类型: conference
会议简称: USENIX Security
发表年份: 2024
---

## ZkCross: A novel architecture for Cross-ChainPrivacy-Preserving auditing

## 发表信息

+ [原文链接](https://www.usenix.org/conference/usenixsecurity24/presentation/guo-yihao)

## 作者

+ Yihao Guo 
+ Minghui Xu 
+ Xiuzhen Cheng 
+ Dongxiao Yu 
+ Wangjie Qiu 
+ Gang Qu 
+ Weibing Wang 
+ Mingming Song 


## 笔记

One of the key areas of focus in blockchain research is how to realize privacy-preserving auditing without sacrificing the system's security and trustworthiness. However, simultaneously achieving auditing and privacy protection, two seemingly contradictory objectives, is challenging because an auditing system would require transparency and accountability which might create privacy and security vulnerabilities. This becomes worse in cross-chain scenarios, where the information silos from multiple chains further complicate the problem. In this paper, we identify three important challenges in cross-chain privacy-preserving auditing, namely Cross-chain Linkability Exposure (CLE), Incompatibility of Privacy and Auditing (IPA), and Full Auditing Inefficiency (FAI). To overcome these challenges, we propose zkCross, which is a novel two-layer cross-chain architecture equipped with three cross-chain protocols to achieve privacy-preserving cross-chain auditing. Among these three protocols, two are privacy-preserving cross-chain protocols for transfer and exchange, respectively; the third one is an efficient cross-chain auditing protocol. These protocols are built on solid cross-chain schemes to guarantee privacy protection and audit efficiency. We implement zkCross on both local and cloud servers and perform comprehensive tests to validate that zkCross is well-suited for processing large-scale privacy-preserving auditing tasks. We evaluate the performance of the proposed protocols in terms of run time, latency, throughput, gas consumption, audit time, and proof size to demonstrate their practicality.

以下是中文翻译：

区块链研究的关键方向之一是如何在不损害系统安全性与可信性（trustworthiness）的前提下，实现隐私保护型审计（privacy-preserving auditing）。然而，审计与隐私保护这两个看似矛盾的目标难以同时达成，因为审计系统通常要求透明性与可问责性（accountability），而这可能引发隐私泄露与安全漏洞。在跨链（cross-chain）场景中，这一问题尤为严峻，多个区块链形成的信息孤岛（information silos）进一步加剧了挑战的复杂性。

本文识别出跨链隐私保护审计中的三大关键挑战，即：跨链关联性暴露（Cross-chain Linkability Exposure, CLE）、隐私与审计的不兼容性（Incompatibility of Privacy and Auditing, IPA）以及全量审计低效性（Full Auditing Inefficiency, FAI）。为应对上述挑战，我们提出 zkCross——一种新颖的双层跨链架构，配备三种跨链协议以实现隐私保护的跨链审计。其中，两个协议分别为面向资产转移与资产交换的隐私保护跨链协议，第三个协议则是一种高效的跨链审计协议。这些协议均构建于坚实的跨链机制之上，以确保隐私保护能力与审计效率。

我们在本地服务器与云服务器上实现了 zkCross，并开展了全面测试，验证其在处理大规模隐私保护审计任务方面的适用性。我们从运行时间、延迟、吞吐量、Gas 消耗、审计耗时及证明大小（proof size）等多个维度评估所提协议的性能，充分证明了其实际可行性。

## 关键词

+ zkCross跨链隐私保护审计
+ 双层跨链架构协议
+ 跨链关联性暴露防御
+ 零知识证明跨链隐私
+ 区块链信息孤岛问题
+ 隐私与审计兼容性