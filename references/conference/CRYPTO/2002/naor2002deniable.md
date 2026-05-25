---
title: "Deniable ring authentication"

标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 2002
created: 2025-05-28 02:16:03
modified: 2025-05-28 02:48:53
---

## Deniable ring authentication

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/3-540-45708-9_31)

## 作者

+ Moni Naor

## 笔记

Digital Signatures enable authenticating messages in a way that disallows repudiation. While non-repudiation is essential in some applications, it might be undesirable in others. Two related notions of authentication are: Deniable Authentication (see Dwork, Naor and Sahai [[25](https://link.springer.com/chapter/10.1007/3-540-45708-9_31#ref-CR25 "C. Dwork, M. Naor and A. Sahai, Concurrent Zero-Knowledge, Proc. 30th ACM Symposium on the Theory of Computing, Dallas, 1998, pp. 409–418.")]) and Ring Signatures (see Rivest, Shamir and Tauman [[38](https://link.springer.com/chapter/10.1007/3-540-45708-9_31#ref-CR38 "R. L. Rivest, A. Shamir, and Y. Tauman, How to Leak A Secret, Advances in Cryptology-ASIACRYPT 2001, Lecture Notes in Computer Science, Vol. 2248, Springer, pp. 552–565.")]). In this paper we show how to combine these notions and achieve Deniable Ring Authentication: it is possible to convince a verifier that a member of an ad hoc subset of participants (a ring) is authenticating a message m without revealing which one (source hiding), and the verifier V cannot convince a third party that message _m_ was indeed authenticated - there is no ‘paper trail’ of the conversation, other than what could be produced by V alone, as in zero-knowledge.

We provide an efficient protocol for deniable ring authentication based on any strong encryption scheme. That is once an entity has published a public-key of such an encryption system, it can be drafted to any such ring. There is no need for any other cryptographic primitive. The scheme can be extended to yield threshold authentication (e.g. at least _k_ members of the ring are approving the message) as well.

以下是中文翻译：

数字签名（Digital Signatures）能够以一种禁止否认的方式对消息进行认证。虽然不可否认性（Non-repudiation）在某些应用中至关重要，但在其他场景中可能并不适宜。与认证相关的两个概念是：可否认认证（Deniable Authentication，参见Dwork、Naor和Sahai [25](https://link.springer.com/chapter/10.1007/3-540-45708-9_31#ref-CR25 "C. Dwork, M. Naor and A. Sahai, Concurrent Zero-Knowledge, Proc. 30th ACM Symposium on the Theory of Computing, Dallas, 1998, pp. 409–418."))以及环签名（Ring Signatures，参见Rivest、Shamir和Tauman [38](https://link.springer.com/chapter/10.1007/3-540-45708-9_31#ref-CR38 "R. L. Rivest, A. Shamir, and Y. Tauman, How to Leak A Secret, Advances in Cryptology-ASIACRYPT 2001, Lecture Notes in Computer Science, Vol. 2248, Springer, pp. 552–565."))。在本文中，我们展示了如何结合这两个概念并实现可否认环认证（Deniable Ring Authentication）：即可以让验证者确信某个临时子集（一个环）中的成员对消息$m$进行了认证，但无需透露具体是哪一个成员（源隐藏，Source Hiding）；同时验证者$V$无法向第三方证明消息$m$确实被认证过——整个对话不会留下任何“书面痕迹”，除了验证者$V$自身能够生成的内容，这类似于零知识（Zero-Knowledge）的特性。

我们提出了一种基于任意强加密方案（Strong Encryption Scheme）的高效协议来实现可否认环认证。一旦某个实体发布了该加密系统的公钥，它就可以被纳入任何这样的环中，无需使用其他任何密码学原语（Cryptographic Primitive）。此外，该方案还可以扩展为实现门限认证（Threshold Authentication），例如要求环中的至少$k$个成员批准消息。

## 关键词

+ 可否认环认证协议
+ 环签名源隐藏匿名认证
+ 强加密方案无密码原语环
+ 门限认证无书面痕迹
+ 可否认认证零知识组合