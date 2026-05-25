---
title: "Concretely efficient lattice-based polynomial commitment from standard assumptions"

标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 2024
created: 2025-04-21 10:57:11
modified: 2025-04-21 10:57:50
---

## Concretely efficient lattice-based polynomial commitment from standard assumptions

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-68403-6_13)

## 作者

+ Intak Hwang 
+ Jinyeong Seo 
+ Yongsoo Song 

## 笔记

Polynomial commitment is a crucial cryptographic primitive in constructing zkSNARKs. Most practical constructions to date are either vulnerable against quantum adversaries or lack homomorphic properties, which are essential for recursive proof composition and proof batching. Recently, lattice-based constructions have drawn attention for their potential to achieve all the desirable properties, though they often suffer from concrete inefficiency or rely on newly introduced assumptions requiring further cryptanalysis.

In this paper, we propose a novel construction of a polynomial commitment scheme based on standard lattice-based assumptions. Our scheme achieves a square-root proof size and verification complexity, ensuring concrete efficiency in proof size, proof generation, and verification. Additionally, it features a transparent setup and publicly verifiability.

When compared with Brakedown (CRYPTO 2023), a recent code-based construction, our scheme offers comparable performance across all metrics. Furthermore, its proof size is approximately 4.1 times smaller than SLAP (EUROCRYPT 2024), a recent lattice-based construction.

以下是中文翻译：

多项式承诺（Polynomial commitment）是构建zkSNARKs的重要密码学原语。目前大多数实用构造要么对量子对手脆弱，要么缺乏同态性质（homomorphic properties），而同态性质对于递归证明组合和证明批处理至关重要。最近，基于格的构造（lattice-based constructions）因其可能实现所有期望属性而受到关注，尽管它们通常存在具体效率低下或依赖于新引入的假设，这些假设需要进一步的密码分析。

在本文中，我们提出了一种基于标准格假设的新型多项式承诺方案。我们的方案实现了平方根的证明大小和验证复杂性，确保了在证明大小、证明生成和验证方面的具体效率。此外，它具有透明的设置和公开可验证性。

与Brakedown（CRYPTO 2023）这一近期的基于代码的构造相比，我们的方案在所有指标上提供了可比的性能。此外，它的证明大小比SLAP（EUROCRYPT 2024）这一近期的基于格的构造小约4.1倍。

## 关键词

+ 格基多项式承诺平方根证明
+ 标准格假设透明设置zkSNARK
+ 后量子多项式承诺同态性
+ 递归证明批处理格基方案
+ 具体高效格承诺与Brakedown比较