---
title: "Proofs for deep thought: Accumulation for large memories and deterministic computations"
标题简称: 
论文类型: conference
会议简称: ASIACRYPT
发表年份: 2024
created: 2025-04-21 10:55:34
modified: 2025-04-21 10:56:30
---

## Proofs for deep thought: Accumulation for large memories and deterministic computations

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-981-96-0935-2_9)

## 作者

+ [Benedikt Bünz](Benedikt%20Bünz.md) 
+ [Jessica Chen](Jessica%20Chen.md)
## 笔记

An important part in proving machine computation is to prove the correctness of the read and write operations performed from the memory, which we term memory-proving. Previous methodologies required proving Merkle Tree openings or multi-set hashes, resulting in relatively large proof circuits. We construct an efficient memory-proving Incrementally Verifiable Computation (IVC) scheme from accumulation, which is particularly useful for machine computations with large memories and deterministic steps. In our scheme, the IVC prover $P_{IVC}$ has cost entirely independent of the memory size T and only needs to commit to approximately 15 field elements per read/write operation, marking a more than 100X improvement over prior work. We further reduce this cost by employing a modified, accumulation-friendly version of the GKR protocol. In the optimized version,  $P_{IVC}$ only needs to commit to 6 small memory-table elements per read/write. If the table stores 32-bit values, then this is equivalent to committing to less than one single field element per read and write. Our modified GKR protocol is also valuable for proving other deterministic computations within the context of IVC. Our memory-proving protocol can be extended to support key-value stores. The full version of this article can be found online [BC24]

以下是中文翻译：

证明机器计算的一个重要部分是验证从内存执行的读写操作的正确性，我们称之为内存证明（memory-proving）。以往的方法论需要证明梅克尔树（Merkle Tree）开启或多集合哈希（multi-set hashes），导致相对较大的证明电路。我们构建了一种高效的内存证明增量可验证计算（Incrementally Verifiable Computation, IVC）方案，该方案基于累积（accumulation），特别适用于具有大内存和确定性步骤的机器计算。在我们的方案中，IVC证明者（prover）\( P_{IVC} \) 的成本完全独立于内存大小 \( T \)，每次读写操作仅需承诺大约15个域元素（field elements），相比之前的工作提高了超过100倍。我们进一步通过采用一种修改过的、适合累积的GKR协议（GKR protocol）来减少这一成本。在优化版本中，\( P_{IVC} \) 每次读写仅需承诺6个小内存表元素。如果表中存储的是32位值，这相当于每次读写承诺不到一个单一的域元素。我们修改后的GKR协议在IVC的背景下也对证明其他确定性计算具有重要价值。我们的内存证明协议可以扩展以支持键值存储（key-value stores）。本文的完整版本可以在网上找到 [BC24]。

## 关键词

+ 增量可验证计算
+ 内存证明
+ GKR协议
+ 累积方案
+ 证明系统