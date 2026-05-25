---
title: "Compressed-protocol theory and practical application to plug  play secure algorithmics"
标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 2020
modified: 2025-04-13 17:05:28
---

## Compressed-protocol theory and practical application to plug  play secure algorithmics

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-030-56877-1_18)

## 作者

+ Thomas Attema 
+ Ronald Cramer 

## 笔记

Σ-protocols provide the basis of a widely used class of efficient proof systems, called sigma-protocols. Recently, Bulletproofs (Bootle et al., EUROCRYPT 2016, and Bünz et al., S&P 2018) were proposed as an alternative approach for zero-knowledge on arithmetic circuits achieving logarithmic communication instead of linear. Their core is an ingenious logarithmic-size knowledge proof for a certain quadratic relation. However, reducing ZK for general relations to this requires a somewhat clumsy "reinvention" of cryptographic protocol theory. We take a quite different view and reconcile Bulletproofs with Σ-protocol theory such that (a) simpler circuit ZK is developed within the established theory, while (b) achieving exactly the same logarithmic communication. The natural key here is linearization. First, we repurpose Bulletproofs as a blackbox compression mechanism for ZK proofs for general linear relations (over commitments to secret vectors in a compact way); this is our core. Second, we reduce the case of general nonlinear relations to blackbox application of our core via a new variant of a technique based on arithmetic secret sharing (Cramer et al., ICITS 2012). We also add versatility by enabling previously not-considered scenarios, e.g., when a secret input is spread across multiple commitments. From the discrete logarithm assumption or the generalized strong RSA assumption, standard implementation platforms give logarithmic communication. Moreover, under the knowledge-of-exponent assumption (KEA), communication drops to constant, as with ZK-SNARKs. Our theory should more broadly be useful for the modular ("plug & play") design of practical cryptographic protocols.

以下是中文翻译：

Σ-协议为安全算法提供了一个被广泛理解的基础。最近，Bulletproofs（Bootle等，EUROCRYPT 2016，以及Bünz等，S&P 2018）被提出作为一种可替换的选择，以应对算术电路的零知识（ZK），实现对数通信而不是线性通信。其核心是针对某些二次关系的巧妙对数大小的知识证明BP。然而，将一般关系的ZK简化到此，需要一种有些笨拙的“重新发明”密码协议理论。我们采取一种相当不同的观点，并将Bulletproofs与Σ-协议理论调和，使得(a) 在建立的理论内发展更简单的电路ZK，同时(b) 实现完全相同的对数通信。这里的自然关键是线性化。首先，我们将BPs作为一种黑箱压缩机制，重新利用于处理一般线性关系的ZK证明（在紧凑提交的秘密向量上）；这是我们的核心。其次，我们通过对Σ-协议（Cramer等，ICITS 2012）中基于算术秘密共享技术的新变体，减少一般非线性关系的情况到我们核心的黑箱应用。另一方面，我们通过启用之前未曾解决的场景来增强多样性，例如，当一个秘密输入分散在多个承诺中时。从离散对数假设或广义强RSA假设出发，标准实现平台导致对数通信。此外，在知识指数假设（KEA）下，通信降至常数，如同ZK-SNARKS。总之，我们的理论应更普遍地对实用密码协议的模块化（”即插即用”）设计有用；我们的另一项工作（2020）关于部分知识证明进一步证明了这一点。

## 关键词

+ 压缩协议Sigma协议Bulletproofs统一框架
+ 对数通信算术电路零知识证明
+ 线性关系黑箱压缩承诺秘密向量
+ 算术秘密共享非线性关系约减
+ 离散对数强RSA知识指数假设