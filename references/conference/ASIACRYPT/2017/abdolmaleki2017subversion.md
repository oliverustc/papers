---
title: "A subversion-resistant SNARK"
标题简称:
论文类型: conference
会议简称: ASIACRYPT
发表年份: 2017
modified: 2025-04-08 17:21:36
---

## A subversion-resistant SNARK

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-319-70700-6_1)

## 作者

+ Behzad Abdolmaleki
+ Karim Baghery
+ Helger Lipmaa
+ Michał Zając

## 笔记

While zk-SNARKs are widely studied, the question of what happens when the CRS has been subverted has received little attention. In ASIACRYPT 2016, Bellare, Fuchsbauer and Scafuro showed the first negative and positive results in this direction, proving also that it is impossible to achieve subversion soundness and (even non-subversion) zero knowledge at the same time. On the positive side, they constructed an involved sound and Sub-ZK argument system for NP. We make Groth’s zk-SNARK for Circuit-SAT from EUROCRYPT 2016 computationally knowledge-sound and perfectly composable Sub-ZK with minimal changes. We just require the CRS trapdoor to be extractable and the CRS to be publicly verifiable. To achieve the latter, we add some new elements to the CRS and construct an efficient CRS verification algorithm. We also provide a definitional framework for sound and Sub-ZK SNARKs and describe implementation results of the new Sub-ZK SNARK.

以下是中文翻译：

虽然零知识简洁非交互式知识论证(zk-SNARKs)已被广泛研究，但当公共参考串(CRS)被破坏时会发生什么的问题却很少受到关注。在2016年亚洲密码学会议(ASIACRYPT)上，Bellare、Fuchsbauer和Scafuro在这个方向上展示了首个正面和负面的研究结果，同时也证明了不可能同时实现破坏可靠性和（即使是非破坏的）零知识性。从积极的方面来看，他们为NP问题构建了一个复杂的可靠且具有破坏零知识性(Sub-ZK)的论证系统。我们对Groth在2016年欧洲密码学会议(EUROCRYPT)上提出的针对电路可满足性(Circuit-SAT)问题的zk-SNARK进行了最小程度的修改，使其具备计算知识可靠性和完美可组合的破坏零知识性。我们只需要CRS陷门可提取，且CRS可公开验证。为实现后者，我们在CRS中添加了一些新元素，并构建了一个高效的CRS验证算法。我们还为可靠且具有破坏零知识性的SNARKs提供了定义框架，并描述了这个新的具有破坏零知识性的SNARK的实现结果。

## 关键词

+ zk-SNARK
+ 破坏抵抗性
+ 零知识性
+ CRS验证
+ 公共参考串