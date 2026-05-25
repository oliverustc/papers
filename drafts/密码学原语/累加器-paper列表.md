---
modified: 2025-05-09 14:54:35
title: 累加器调研-paper列表
created: 2025-04-13 16:50:59
draft: true
---
## 零知识累加器

Esha Ghosh, Olga Ohrimenko, Dimitrios Papadopoulos, Roberto Tamassia, Nikos Triandopoulos **Zero-knowledge accumulators and set algebra** (**ASIACRYPT 2016**) [web](https://link.springer.com/chapter/10.1007/978-3-662-53890-6_3) [scholar](https://scholar.google.com.hk/scholar?hl=zh-CN&as_sdt=0%2C5&q=Zero-knowledge%20accumulators%20and%20set%20algebra&btnG=) [obsidian](ghosh2016zero)

针对集合成员资格证明（set membership proof），提出零知识累加器 (zero-knowledge accumulators) 来提供额外的隐藏保证: 累加值和证明不会泄露任何关于通过元素插入/删除而动态演化的集合的信息。

Alex Ozdemir, Riad Wahby, Barry Whitehat, Dan Boneh **Scaling verifiable computation using efficient set accumulators** (**USENIX Security 2020**) [web](https://www.usenix.org/conference/usenixsecurity20/presentation/ozdemir) [scholar](https://scholar.google.com.hk/scholar?hl=zh-CN&as_sdt=0%2C5&q=Scaling%20verifiable%20computation%20using%20efficient%20set%20accumulators&btnG=) [obsidian](ozdemir2020scaling)

Merkle tree 证明数据完整性的替代方案，通过 rsa 累加器，实现更加高效的更新证明。

Foteini Baldimtsi, Ioanna Karantaidou, Srinivasan Raghuraman **Oblivious accumulators** (**PKC 2024**) [web](https://link.springer.com/chapter/10.1007/978-3-031-57722-2_4) [scholar](https://scholar.google.com.hk/scholar?hl=zh-CN&as_sdt=0%2C5&q=Oblivious%20accumulators&btnG=) [obsidian](baldimtsi2024oblivious)

实现了累加器元素隐藏和添加-删除的不可区分性。

Matteo Campanelli, Mathias Hall-Andersen, Simon Holmgaard Kamp **Curve trees: Practical and transparent Zero-Knowledge accumulators** (**USENIX Security 2023**) [web](https://www.usenix.org/conference/usenixsecurity23/presentation/campanelli) [scholar](https://scholar.google.com.hk/scholar?hl=zh-CN&as_sdt=0%2C5&q=Curve%20trees%3A%20Practical%20and%20transparent%20Zero-Knowledge%20accumulators&btnG=) [obsidian](campanelli2023curve)

无需可信设置的累加器

Shravan Srinivasan, Ioanna Karantaidou, Foteini Baldimtsi, Charalampos Papamanthou **Batching, aggregation, and zero-knowledge proofs in bilinear accumulators** (**CCS 2022**) [web](https://dl.acm.org/doi/abs/10.1145/3548606.3560676) [scholar](https://scholar.google.com.hk/scholar?hl=zh-CN&as_sdt=0%2C5&q=Batching%2C%20aggregation%2C%20and%20zero-knowledge%20proofs%20in%20bilinear%20accumulators&btnG=) [obsidian](srinivasan2022batching)

基于双线性配对的高效、可聚合可批量证明的累加器。

Jiajun Xin, Arman Haghighi, Xiangan Tian, Dimitrios Papadopoulos **Notus: Dynamic Proofs of Liabilities from Zero-knowledge RSA Accumulators** (**USENIX Security 2024**) [web](https://www.usenix.org/conference/usenixsecurity24/presentation/xin) [scholar](https://scholar.google.com.hk/scholar?hl=zh-CN&as_sdt=0%2C5&q=Notus%3A%20Dynamic%20Proofs%20of%20Liabilities%20from%20Zero-knowledge%20RSA%20Accumulators&btnG=) [obsidian](xin2024notus)

Snark friendly 的 rsa 累加器，用于实现区块链的负债证明

[[Nirvan Tyagi]], Ben Fisch, Andrew Zitek, [[Joseph Bonneau]], Stefano Tessaro **VeRSA: Verifiable registries with efficient client audits from RSA authenticated dictionaries** (**CCS 2022**) [web](https://dl.acm.org/doi/abs/10.1145/3548606.3560605) [scholar](https://scholar.google.com.hk/scholar?hl=zh-CN&as_sdt=0%2C5&q=VeRSA%3A%20Verifiable%20registries%20with%20efficient%20client%20audits%20from%20RSA%20authenticated%20dictionaries&btnG=) [obsidian](tyagi2022versa)


[Matteo Campanelli](Matteo%20Campanelli.md), Dario Fiore, Semin Han, Jihye Kim, Dimitris Kolonelos, Hyunok Oh **Succinct zero-knowledge batch proofs for set accumulators** (**CCS 2022**) [web](https://dl.acm.org/doi/abs/10.1145/3548606.3560677) [scholar](https://scholar.google.com.hk/scholar?hl=zh-CN&as_sdt=0%2C5&q=Succinct%20zero-knowledge%20batch%20proofs%20for%20set%20accumulators&btnG=) [obsidian](campanelli2022succinct)


Victor Youdom Kemmoe, [Anna Lysyanskaya](Anna%20Lysyanskaya.md) **RSA-Based Dynamic Accumulator without Hashing into Primes** (**CCS 2024**) [web](https://dl.acm.org/doi/abs/10.1145/3658644.3690199) [scholar](https://scholar.google.com.hk/scholar?hl=zh-CN&as_sdt=0%2C5&q=RSA-Based%20Dynamic%20Accumulator%20without%20Hashing%20into%20Primes&btnG=) [obsidian](kemmoe2024rsa)
