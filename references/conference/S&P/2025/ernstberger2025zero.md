---
title: "Zero-Knowledge Location Privacy via Accurate Floating-Point SNARKs"
doi: 10.1109/sp61157.2025.00057
标题简称:
论文类型: conference
会议简称: S&P
发表年份: 2025
modified: 2025-04-16 11:19:05
created: 2025-04-13 14:41:04
---
## Zero-Knowledge Location Privacy via Accurate Floating-Point SNARKs

## 发表信息

+ [原文链接暂无]
+ [arxiv](https://arxiv.org/abs/2404.14983)

## 作者

+ [Jens Ernstberger](Jens%20Ernstberger.md)
+ [Chengru Zhang](Chengru%20Zhang.md)
+ Luca Ciprian 
+ [Philipp Jovanovic](Philipp%20Jovanovic.md)
+ Sebastian Steinhorst 

## 笔记

We introduce Zero-Knowledge Location Privacy (ZKLP), enabling users to prove to third parties that they are within a specified geographical region while not disclosing their exact location. ZKLP supports varying levels of granularity, allowing for customization depending on the use case. To realize ZKLP, we introduce the first set of Zero-Knowledge Proof (ZKP) circuits that are fully compliant to the IEEE 754 standard for floating-point arithmetic. Our results demonstrate that our floating point circuits amortize efficiently, requiring only 64 constraints per operation for 2^15 single-precision floating-point multiplications. We utilize our floating point implementation to realize the ZKLP paradigm. In comparison to a baseline, we find that our optimized implementation has 15.9x less constraints utilizing single precision floating-point values, and 12.2x less constraints when utilizing double precision floating-point values. We demonstrate the practicability of ZKLP by building a protocol for privacy preserving peer-to-peer proximity testing — Alice can test if she is close to Bob by receiving a single message, without either party revealing any other information about their location. In such a setting, Bob can create a proof of (non-)proximity in 0.26 s, whereas Alice can verify her distance to about 470 peers per second.

以下是中文翻译：

我们推出了零知识位置隐私（ZKLP）技术，使用户能够向第三方证明自己位于特定地理区域内，而无需透露具体位置。ZKLP支持不同级别的精度划分，可根据实际应用场景灵活调整。为实现这一技术，我们首创了完全符合IEEE 754浮点运算标准的零知识证明（ZKP）电路组。实验数据显示，我们的浮点电路能高效分摊计算量，在2^15次单精度浮点乘法运算中，每次操作仅需64个约束条件。 通过采用浮点运算实现方案，我们成功构建了ZKLP范式。与基准方案相比，优化后的单精度浮点值实现方案约束条件减少15.9倍，双精度浮点值方案减少12.2倍。为验证ZKLP的实用性，我们开发了隐私保护的点对点邻近性检测协议——Alice仅需接收一条消息即可检测是否接近Bob，且双方均无需泄露任何其他位置信息。在该协议中，Bob可在0.26秒内生成（非）邻近性证明，而Alice每秒可验证与约470个对等节点的距离。

## 关键词

+ 零知识位置隐私ZKLP
+ 浮点运算零知识证明
+ IEEE 754标准兼容电路
+ 隐私保护邻近性检测
+ 地理区域证明
+ 点对点位置验证