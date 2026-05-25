---
title: "zk-creds: Flexible anonymous credentials from zksnarks and existing identity infrastructure"
标题简称:
论文类型: conference
会议简称: S&P
发表年份: 2023
modified: 2025-05-15 05:46:12
created: 2025-04-14 09:35:08
---

## zk-creds: Flexible anonymous credentials from zksnarks and existing identity infrastructure

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/10179430)
+ [archive](https://eprint.iacr.org/2022/878)
+ [code](https://github.com/rozbb/zkcreds-rs)

## 作者

+ Michael Rosenberg
+ Jacob White
+ [Christina Garman](Christina%20Garman.md)
+ [Ian Miers](Ian%20Miers.md)
## 笔记

Frequently, users on the web need to show that they are, for example, not a robot, old enough to access an age restricted video, or eligible to download an ebook from their local public library without being tracked. Anonymous credentials were developed to address these concerns. However, existing schemes do not handle the realities of deployment or the complexities of real-world identity. Instead, they implicitly make assumptions such as there being an issuing authority for anonymous credentials that, for real applications, requires the local department of motor vehicles to issue sophisticated cryptographic tokens to show users are over 18. In reality, there are multiple trust sources for a given identity attribute, their credentials have distinctively different formats, and many, if not all, issuers are unwilling to adopt new protocols.We present and build zk-creds, a protocol that uses general-purpose zero-knowledge proofs to 1) remove the need for credential issuers to hold signing keys: credentials can be issued to a bulletin board instantiated as a transparency log, Byzantine system, or even a blockchain; 2) convert existing identity documents into anonymous credentials without modifying documents or coordinating with their issuing authority; 3) allow for flexible, composable, and complex identity statements over multiple credentials. Concretely, identity assertions using zk-creds take less than 150ms in a real-world scenario of using a passport to anonymously access age-restricted videos.

以下是中文翻译：

用户在网络上经常需要证明自己，例如，表明自己不是机器人、足够年龄以访问年龄限制的视频，或有资格在不被追踪的情况下从当地公共图书馆下载电子书。为了解决这些问题，匿名凭证（anonymous credentials）应运而生。然而，现有的方案并未考虑到部署的现实情况或现实世界身份的复杂性。相反，它们隐含地假设存在一个为匿名凭证提供的发放机构，而在实际应用中，这需要当地机动车辆管理局发放复杂的加密令牌，以证明用户年满18岁。实际上，对于给定的身份属性，存在多个信任来源，它们的凭证格式各不相同，且许多（如果不是全部）发放者都不愿意采用新协议。

我们提出并构建了zk-creds，这是一种使用通用零知识证明（zero-knowledge proofs）的协议，旨在实现以下目标：1）消除凭证发放者持有签名密钥的需求：凭证可以发放到一个作为透明日志、拜占庭系统，甚至区块链实例化的公告板上；2）在不修改文件或与发放机构协调的情况下，将现有身份文件转换为匿名凭证；3）允许在多个凭证上进行灵活、可组合和复杂的身份声明。具体而言，在使用护照匿名访问年龄限制视频的实际场景中，使用zk-creds进行身份声明的时间少于150毫秒。

## 关键词

+ 匿名凭证
+ 零知识证明
+ 透明度日志
+ 身份隐私保护
+ 遗留身份文件转换
+ zk-SNARK应用