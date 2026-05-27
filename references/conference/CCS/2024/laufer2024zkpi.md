---
title: "zkPi: Proving Lean Theorems in Zero-Knowledge"
doi: 10.1145/3658644.3670322
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2024

modified: 2025-04-13 14:30:43
---
## zkPi: Proving Lean Theorems in Zero-Knowledge

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3658644.3670322)

## 作者

+ Evan Laufer,
+ [Alex Ozdemir](Alex%20Ozdemir.md)
+ [Dan Boneh](Dan%20Boneh.md)

## 笔记

Interactive theorem provers (ITPs), such as Lean and Coq, can express formal proofs for a large category of theorems, from abstract math to software correctness. Consider Alice who has a Lean proof for some public statement T. Alice wants to convince the world that she has such a proof, without revealing the actual proof. Perhaps the proof shows that a secret program is correct or safe, but the proof itself might leak information about the program's source code. A natural way for Alice to proceed is to construct a succinct, zero-knowledge, non-interactive argument of knowledge (zkSNARK) to prove that she has a Lean proof for the statement T.
In this work we build zkPi, the first zkSNARK for proofs expressed in Lean, a state of the art interactive theorem prover. With zkPi, a prover can convince a verifier that a Lean theorem is true, while revealing little else. The core problem is building an efficient zkSNARK for dependent typing. We evaluate zkPi on theorems from two core Lean libraries: stdlib and mathlib. zkPi successfully proves 57.9% of the theorems in stdlib, and 14.1% of the theorems in mathlib, within 4.5 minutes per theorem. A zkPi proof is sufficiently short that Fermat could have written one in the margin of his proverbial notebook.
Interactive theorem provers (ITPs) can express virtually all systems of formal reasoning. Thus, an implemented zkSNARK for ITP theorems generalizes practical zero-knowledge's interface beyond the status quo: circuit satisfiability and program execution.

以下是中文翻译：

交互式定理证明器(Interactive theorem provers, ITPs)，如Lean和Coq，能够为大类定理表达形式化证明，涵盖从抽象数学到软件正确性的范围。设想Alice拥有某个公开陈述T的Lean证明。Alice想要向世界证明她确实拥有这样的证明，但不想透露实际的证明内容。也许这个证明表明某个秘密程序是正确或安全的，但证明本身可能会泄露程序源代码的信息。对Alice来说，一个自然的方法是构建一个简洁的、零知识的、非交互式知识论证(zkSNARK)来证明她拥有该陈述T的Lean证明。

在本研究中，我们构建了zkPi，这是首个针对Lean（一个最先进的交互式定理证明器）中表达的证明的zkSNARK。通过zkPi，证明者可以使验证者确信某个Lean定理是正确的，同时几乎不会泄露其他信息。核心问题是为依赖类型构建高效的zkSNARK。我们在Lean的两个核心库：stdlib和mathlib中对zkPi进行了评估。zkPi成功证明了stdlib中57.9%的定理，以及mathlib中14.1%的定理，每个定理平均用时4.5分钟。zkPi的证明非常简短，以至于费马完全可以将其写在他那本著名笔记本的页边空白处。

交互式定理证明器(ITPs)几乎可以表达所有形式推理系统。因此，针对ITP定理实现的zkSNARK将实用零知识的接口扩展到了超越现状的范围：电路可满足性和程序执行。

## 关键词

+ 零知识证明
+ 定理证明
+ Lean
+ zkSNARK
+ 依赖类型
+ 形式化验证