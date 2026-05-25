---
title: "Compute, but verify: Efficient multiparty computation over authenticated inputs"
标题简称:
论文类型: conference
会议简称: ASIACRYPT
发表年份: 2024
---

## Compute, but verify: Efficient multiparty computation over authenticated inputs

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-981-96-0938-3_5)

## 作者

+ Moumita Dutta 
+ [Chaya Ganesh](Chaya%20Ganesh.md)
+ Sikhar Patranabis 
+ Nitin Singh 


## 笔记

Traditional notions of secure multiparty computation (MPC) allow mutually distrusting parties to jointly compute a function over their private inputs, but typically do not specify how these inputs are chosen. Motivated by real-world applications where corrupt inputs could adversely impact privacy and operational legitimacy, we consider a notion of _authenticated_ MPC where the inputs are authenticated (for instance, signed using a digital signature) by some certification authority. We propose a generic and efficient compiler that transforms any linear secret sharing based honest-majority MPC protocol into one with input authentication.

Our compiler achieves an ideal notion of authenticated MPC equipped with stronger and more desirable security guarantees than those considered in prior works, while incurring significantly lower computational costs and competitive communication overheads when compared to existing solutions. In particular, we entirely avoid the (potentially expensive) protocol-specific techniques and pre-processing requirements that are inherent to these solutions. For certain corruption thresholds, our compiler additionally preserves the stronger identifiable abort security of the underlying MPC protocol. No existing solution for authenticated MPC achieves this regardless of the corruption threshold.

Along the way, we make several technical contributions that are of independent interest. This includes the notion of distributed proofs of knowledge and concrete realizations of the same for several relations of interest, such as proving knowledge of many popularly used digital signature schemes, and proving knowledge of opening of a Pedersen commitment.

以下是中文翻译：

传统意义上的安全多方计算（Secure Multiparty Computation, MPC）允许多个互不信任的参与方基于各自的私有输入共同计算某个函数，但通常未明确规定这些输入是如何选择的。受现实应用场景（其中恶意输入可能对隐私和操作合法性产生负面影响）的驱动，我们提出了一种认证多方计算（authenticated MPC）的概念：所有输入均需经过某个认证机构进行身份认证（例如使用数字签名进行签署）。我们提出了一种通用且高效的编译器（compiler），可将任何基于线性秘密共享（linear secret sharing）的诚实多数MPC协议转换为具有输入认证功能的协议。

该编译器实现了具备更强、更理想安全保证的认证MPC理想模型，其安全属性优于既有研究方案，同时在计算成本上显著降低，并保持具有竞争力的通信开销。特别值得注意的是，我们完全避免了现有解决方案中固有的（可能代价高昂的协议特定技术和预处理要求。对于特定的腐败阈值，我们的编译器还能额外保留底层MPC协议更强的可识别中止（identifiable abort）安全性。而现有认证MPC方案在任何腐败阈值下均无法实现这一特性。

在研究过程中，我们取得了多项具有独立价值的技术贡献。这包括分布式知识证明（distributed proofs of knowledge）的概念框架，以及针对多个重要关系的具体实现方案——例如证明对多种常用数字签名方案的知识掌握，以及证明对Pedersen承诺（Pedersen commitment）解密的知情权。

## 关键词

+ 认证多方计算
+ 输入认证
+ 安全多方计算
+ 可识别中止
+ 分布式证明