---
title: "Vector commitments with proofs of smallness: Short range proofs and more"
标题简称:
论文类型: conference
会议简称: PKC
发表年份: 2024
modified: 2025-04-11 11:47:45
---

## Vector commitments with proofs of smallness: Short range proofs and more

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-57722-2_2)

## 作者

+ Benoit Libert 

## 笔记

Vector commitment schemes are compressing commitments to vectors that make it possible to succinctly open a commitment for individual vector positions without revealing anything about other positions. We describe vector commitments enabling constant-size proofs that the committed vector is small (i.e., binary, ternary, or of small norm). As a special case, we obtain range proofs featuring the shortest proof length in the literature with only 3 group elements per proof. As another application, we obtain short pairing-based NIZK arguments for lattice-related statements. In particular, we obtain short proofs (comprised of 3 group elements) showing the validity of ring LWE ciphertexts and public keys. Our constructions are proven simulation-extractable in the algebraic group model and the random oracle model.

以下是中文翻译：

向量承诺方案是一种压缩向量的承诺方式，使得能够简洁地为单个向量位置打开承诺，而不泄露关于其他位置的任何信息。我们描述了能够实现常数大小证明的向量承诺，这些证明表明所承诺的向量是小的（即，二进制、三进制或小范数）。作为一个特例，我们获得了具有文献中最短证明长度的范围证明，每个证明仅需3个群元素。作为另一个应用，我们获得了基于配对的短非交互式零知识（NIZK）论证，用于与格相关的陈述。特别地，我们获得了短证明（由3个群元素组成），以展示环学习有误差（ring LWE）密文和公钥的有效性。我们的构造在代数群模型和随机预言机模型中被证明是可模拟提取的。

## 关键词

+ 向量承诺
+ 小范数证明
+ 范围证明
+ 基于配对的NIZK
+ 格密文有效性证明
+ 代数群模型