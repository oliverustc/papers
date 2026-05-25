---
title: "Fully dynamic attribute-based signatures for circuits from codes"
标题简称:
论文类型: conference
会议简称: PKC
发表年份: 2024
created: 2025-05-13 05:38:15
modified: 2025-05-13 05:38:53
---

## Fully dynamic attribute-based signatures for circuits from codes

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-57718-5_2)

## 作者

+ San Ling
+ [Khoa Nguyen](Khoa%20Nguyen.md)
+ Duong Hieu Phan
+ Khai Hanh Tang
+ [Huaxiong Wang](Huaxiong%20Wang.md)
+ [Yanhong Xu](Yanhong%20Xu.md)
## 笔记

Attribute-Based Signature (ABS), introduced by Maji et al. (CT-RSA’11), is an advanced privacy-preserving signature primitive that has gained a lot of attention. Research on ABS can be categorized into three main themes: expanding the expressiveness of signing policies, enabling new functionalities, and providing more diversity in terms of computational assumptions. We contribute to the development of ABS in all three dimensions, by providing a fully dynamic ABS scheme for arbitrary circuits from codes. The scheme is the first ABS from code-based assumptions and also the first ABS system offering the full dynamicity functionality (i.e., attributes can be enrolled and revoked simultaneously). Moreover, the scheme features much shorter signature size than a lattice-based counterpart proposed by El Kaafarani and Katsumata (PKC’18).

In the construction process, we put forward a new theoretical abstraction of Stern-like zero-knowledge (ZK) protocols, which are the major tools for privacy-preserving cryptography from codes. Our main insight here actually lies in the questions we ask about the fundamental principles of Stern-like protocols that have remained unchallenged since their conception by Stern at CRYPTO’93. We demonstrate that these long-established principles are not essential, and then provide a refined framework generalizing existing Stern-like techniques and enabling enhanced constructions.

以下是中文翻译：

属性基签名（Attribute-Based Signature, ABS）由Maji等人（CT-RSA'11）首次提出，是一种备受关注的高级隐私保护签名原语。ABS的研究可以分为三个主要方向：扩展签名策略的表达能力、实现新功能、以及提供更多样化的计算假设。我们在这三个维度上都对ABS的发展做出了贡献，提出了一个基于编码的、支持任意电路的完全动态ABS方案。该方案是首个基于编码假设（code-based assumptions）的ABS，也是首个提供完全动态功能（即属性可以同时注册和撤销）的ABS系统。此外，与El Kaafarani和Katsumata（PKC'18）提出的基于格的对应方案相比，本方案的签名大小要小得多。

在构建过程中，我们提出了一个新的Stern式零知识（zero-knowledge, ZK）协议的理论抽象，这些协议是基于编码的隐私保护密码学的主要工具。我们的主要见解实际上在于我们对Stern式协议的基本原理提出的质疑，这些原理自从Stern在CRYPTO'93首次提出以来一直未受到挑战。我们证明了这些长期确立的原理并非必要，并提供了一个改进的框架，该框架既概括了现有的Stern式技术，又能够实现增强型构造。

## 关键词

+ 属性基签名（ABS）
+ 完全动态属性管理
+ 编码假设
+ Stern式零知识协议
+ 后量子签名
+ 隐私保护访问控制