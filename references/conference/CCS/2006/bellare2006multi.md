---
title: "Multi-signatures in the plain public-key model and a general forking lemma"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2006
---

## Multi-signatures in the plain public-key model and a general forking lemma

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/1180405.1180453)

## 作者

+ [Mihir Bellare](Mihir%20Bellare.md) 
+ Gregory Neven 


## 笔记

A multi-signature scheme enables a group of signers to produce a compact, joint signature on a common document, and has many potential uses. However, existing schemes impose key setup or PKI requirements that make them impractical, such as requiring a dedicated, distributed key generation protocol amongst potential signers, or assuming strong, concurrent zero-knowledge proofs of knowledge of secret keys done to the CA at key registration. These requirements limit the use of the schemes. We provide a new scheme that is proven secure in the plain public-key model, meaning requires nothing more than that each signer has a (certified) public key. Furthermore, the important simplification in key management achieved is not at the cost of efficiency or assurance: our scheme matches or surpasses known ones in terms of signing time, verification time and signature size, and is proven secure in the random-oracle model under a standard (not bilinear map related) assumption. The proof is based on a simplified and general Forking Lemma that may be of independent interest.

以下是中文翻译：

多重签名方案使得一组签名者能够在一个共同文档上生成一个紧凑的联合签名，并具有许多潜在的应用。然而，现有方案通常需要密钥设置或公钥基础设施（PKI）要求，这使得它们在实际应用中不够可行，例如需要潜在签名者之间进行专门的分布式密钥生成协议，或者假设在密钥注册时向证书授权机构（CA）进行强并发的零知识证明以证明对秘密密钥的知识。这些要求限制了这些方案的使用。我们提供了一种新方案，该方案在普通公钥模型中被证明是安全的，这意味着只需每个签名者拥有一个（经过认证的）公钥。此外，实现的密钥管理重要简化并没有以效率或保证为代价：我们的方案在签名时间、验证时间和签名大小方面与已知方案相匹配或超越，并且在随机预言模型下，在一个标准（非双线性映射相关）假设下被证明是安全的。该证明基于一个简化的通用分叉引理，可能具有独立的研究价值。

## 关键词

+ 多重签名
+ 普通公钥模型
+ 分叉引理
+ 数字签名
+ 密钥管理