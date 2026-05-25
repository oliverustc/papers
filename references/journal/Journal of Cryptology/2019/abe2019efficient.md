---
title: "Efficient Fully Structure-Preserving Signatures and Shrinking Commitments"
标题简称:
论文类型: journal
期刊简称: Journal of Cryptology
发表年份: 2019
created: 2025-05-12 09:13:24
modified: 2025-05-12 09:15:41
---

## Efficient Fully Structure-Preserving Signatures and Shrinking Commitments

## 发表信息

+ [原文链接]()

## 作者

+ Masayuki Abe
+ [Jens Groth](Jens%20Groth.md)
+ [Markulf Kohlweiss](Markulf%20Kohlweiss.md)
+ Miyako Ohkubo
+ Mehdi Tibouchi

## 笔记

In structure-preserving signatures, public keys, messages, and signatures are all collections of source group elements of some bilinear groups. In this paper, we introduce fully structure-preserving signature schemes, with the additional requirement that even secret keys are group elements. This strong property allows efficient non-interactive proofs of knowledge of the secret key, which is useful in designing cryptographic protocols under simulation-based security where online extraction of the secret key is needed. We present efficient constructions under simple standard assumptions and pursue even more efficient constructions with the extra property of randomizability based on the generic bilinear group model. An essential building block for our efficient standard model construction is a shrinking structure-preserving trapdoor commitment scheme, which is by itself an important primitive and of independent interest as it appears to contradict a known impossibility result that structure-preserving commitments cannot be shrinking. We argue that a relaxed binding property lets us circumvent the impossibility while still retaining the usefulness of the primitive in important applications as mentioned above.

以下是中文翻译：

在结构保持签名(structure-preserving signatures)中，公钥、消息和签名都是某些双线性群的源群元素的集合。在本文中，我们引入了完全结构保持签名方案，其附加要求是连私钥也是群元素。这个强大的特性允许对私钥进行高效的非交互式知识证明，这在设计基于模拟的安全性的密码学协议时非常有用，特别是在需要在线提取私钥的场景中。我们基于简单的标准假设提出了高效的构造方案，并在通用双线性群模型(generic bilinear group model)的基础上，追求具有可随机化(randomizability)这一额外特性的更高效构造。

我们在标准模型下进行高效构造的一个重要构建模块是收缩结构保持陷门承诺方案(shrinking structure-preserving trapdoor commitment scheme)，这本身就是一个重要的原语，具有独立的研究价值，因为它似乎与已知的"结构保持承诺不能是收缩的"这一不可能性结果相矛盾。我们论证了一个放宽的绑定属性(binding property)让我们能够绕过这个不可能性，同时仍然保持了该原语在上述重要应用中的实用性。

## 关键词

+ 完全结构保持签名
+ 双线性群密码构造
+ 收缩结构保持陷门承诺
+ 非交互式知识证明
+ 通用双线性群模型
+ 可随机化签名方案