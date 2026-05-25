---
title: "BulletCT: Towards More Scalable Ring Confidential Transactions With Transparent Setup"
标题简称:
论文类型: preprint
预印本简称: archive
发表年份: 2025
modified: 2025-04-17 13:35:37
created: 2025-04-11 11:59:16
---

## BulletCT: Towards More Scalable Ring Confidential Transactions With Transparent Setup

## 发表信息

+ [archive](https://eprint.iacr.org/2025/188)

## 作者

+ [Nan Wang](Nan%20Wang.md) 
+ Qianhui Wang 
+ [Dongxi Liu](Dongxi%20Liu.md)
+ Muhammed F Esgin 
+ Alsharif Abuadbba 

## 笔记

RingCT signatures are essential components of Ring Confidential Transaction (RingCT) schemes on blockchain platforms, enabling anonymous transaction spending and significantly impacting the scalability of these schemes. This paper makes two primary contributions:

We provide the first thorough analysis of a recently developed Any-out-of-N proof in the discrete logarithm (DLOG) setting and the associated RingCT scheme, introduced by ZGSX23 (S&P '23). The proof conceals the number of the secrets to offer greater anonymity than K-out-of-N proofs and uses an efficient "K-Weight" technique for its construction. However, we identify for the first time several limitations of using Any-out-of-N proofs, such as increased transaction sizes, heightened cryptographic complexities and potential security risks. These limitations prevent them from effectively mitigating the longstanding scalability bottleneck.

We then continue to explore the potential of using K-out-of-N proofs to enhance scalability of RingCT schemes. Our primary innovation is a new DLOG-based RingCT signature that integrates a refined "K-Weight"-based K-out-of-N proof and an entirely new tag proof. The latter is the first to efficiently enable the linkability of RingCT signatures derived from the former, effectively resisting double-spending attacks.

Finally, we identify and patch a linkability flaw in ZGSX23's signature. We benchmark our scheme against this patched one to show that our scheme achieves a boost in scalability, marking a promising step forward.

Note: Compared to the camera-ready version of USENIX Security '25, the following improvements have been made: 1 - The typo in Equation (2) on page 9 has been corrected to $\prod^{|R|}_{i=1} (P_i \cdot T^d_i)^{y^ib_i} = (\tau \cdot \eta^d)^{\sum_{k=1}^{|S|}y^{\phi(k)}s_{\phi(k)}}$ to ensure consistency with our implementation. 2 - The security proofs of the pseudo-randomness of tags on page 19 have been improved for greater clarity.

以下是中文翻译：

环形机密交易(Ring Confidential Transaction, RingCT)签名是区块链平台上RingCT方案的核心组件，它能够实现匿名交易支出，并显著影响这些方案的可扩展性。本文做出了两个主要贡献：

我们首次对最近在离散对数(discrete logarithm, DLOG)环境下开发的任意数量证明(Any-out-of-N proof)及其相关RingCT方案进行了深入分析，该方案由ZGSX23（S&P '23）提出。该证明通过隐藏密钥数量来提供比K-out-of-N证明更强的匿名性，并使用高效的"K-Weight"技术进行构建。然而，我们首次识别出使用任意数量证明的几个局限性，如交易规模增加、密码学复杂性提高以及潜在的安全风险。这些局限性使其无法有效解决长期存在的可扩展性瓶颈。

随后，我们继续探索使用K-out-of-N证明来提高RingCT方案可扩展性的潜力。我们的主要创新是一个新的基于DLOG的RingCT签名，它整合了改进的基于"K-Weight"的K-out-of-N证明和一个全新的标签证明(tag proof)。后者是首个能够有效实现源自前者的RingCT签名可链接性的方案，有效防止双重支付攻击。

最后，我们发现并修复了ZGSX23签名中的一个可链接性缺陷。我们将我们的方案与这个修复后的方案进行基准测试，结果表明我们的方案在可扩展性方面实现了提升，标志着一个重要的进步。

注：与USENIX Security '25会议版本相比，做出了以下改进：1 - 修正了第9页等式(2)中的笔误，将其更正为$\prod^{|R|}_{i=1} (P_i \cdot T^d_i)^{y^ib_i} = (\tau \cdot \eta^d)^{\sum_{k=1}^{|S|}y^{\phi(k)}s_{\phi(k)}}$，以确保与我们的实现保持一致。2 - 改进了第19页标签伪随机性的安全性证明，使其更加清晰。

## 关键词

+ BulletCT环形机密交易可扩展性
+ RingCT签名K-out-of-N离散对数
+ K-Weight技术任意数量证明分析
+ 双重支付抵抗标签证明可链接性
+ 透明设置区块链匿名交易优化