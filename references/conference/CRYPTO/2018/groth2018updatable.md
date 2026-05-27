---
title: "Updatable and Universal Common Reference Strings with Applications to zk-SNARKs"
doi: 10.1007/978-3-319-96878-0_24
标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 2018
modified: 2025-05-12 08:57:26
created: 2025-04-08 17:29:08
---
## Updatable and Universal Common Reference Strings with Applications to zk-SNARKs

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-319-96878-0_24)

## 作者

+ [Jens Groth](Jens%20Groth.md)
+ [Markulf Kohlweiss](Markulf%20Kohlweiss.md)
+ [Mary Maller](Mary%20Maller.md)
+ [Sarah Meiklejohn](Sarah%20Meiklejohn.md)
+ [Ian Miers](Ian%20Miers.md)
## 笔记

By design, existing (pre-processing) zk-SNARKs embed a secret trapdoor in a relation-dependent common reference strings (CRS). The trapdoor is exploited by a (hypothetical) simulator to prove the scheme is zero knowledge, and the secret-dependent structure facilitates a linear-size CRS and linear-time prover computation. If known by a real party, however, the trapdoor can be used to subvert the security of the system. The structured CRS that makes zk-SNARKs practical also makes deploying zk-SNARKS problematic, as it is difficult to argue why the trapdoor would not be available to the entity responsible for generating the CRS. Moreover, for pre-processing zk-SNARKs a new trusted CRS needs to be computed every time the relation is changed.

In this paper, we address both issues by proposing a model where a number of users can update a universal CRS. The updatable CRS model guarantees security if at least one of the users updating the CRS is honest. We provide both a negative result, by showing that zk-SNARKs with private secret-dependent polynomials in the CRS cannot be updatable, and a positive result by constructing a zk-SNARK based on a CRS consisting only of secret-dependent monomials. The CRS is of quadratic size, is updatable, and is universal in the sense that it can be specialized into one or more relation-dependent CRS of linear size with linear-time prover computation.

以下是中文翻译：

根据设计，现有的(预处理)零知识简洁非交互式证明系统(zk-SNARKs)在关系依赖的公共参考串(CRS)中嵌入了一个秘密陷门。这个陷门被(假设的)模拟器用来证明该方案具有零知识性，而这种依赖秘密的结构有助于实现线性大小的CRS和线性时间的证明者计算。然而，如果某个实际参与方知道这个陷门，就可以利用它来破坏系统的安全性。使得zk-SNARKs具有实用性的结构化CRS同时也使其部署变得有问题，因为很难论证为什么负责生成CRS的实体无法获得这个陷门。此外，对于预处理型zk-SNARKs来说，每次关系发生变化时都需要重新计算一个可信的CRS。

在本文中，我们通过提出一个允许多个用户更新通用CRS的模型来解决这两个问题。可更新CRS模型保证，只要参与更新CRS的用户中至少有一个是诚实的，就能确保安全性。我们提供了一个否定性结果，即证明了在CRS中包含私密的依赖秘密多项式的zk-SNARKs无法实现可更新性；同时也提供了一个肯定性结果，即构造了一个基于仅包含依赖秘密单项式的CRS的zk-SNARK。该CRS具有二次规模，可更新，并且具有通用性，能够被特化为一个或多个具有线性规模的关系依赖CRS，同时保持线性时间的证明者计算。

## 关键词

+ 密码学
+ 零知识
+ 协议