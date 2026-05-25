---
title: "HydraProofs: Optimally Computing All Proofs in a Vector Commitment with applications to efficient zkSNARKs over data from multiple users"
标题简称:
论文类型: conference
会议简称: S&P
发表年份: 2025
created: 2025-05-13 03:12:21
modified: 2025-05-13 03:19:08
---

## HydraProofs: Optimally Computing All Proofs in a Vector Commitment with applications to efficient zkSNARKs over data from multiple users

## 发表信息

+ [原文链接](https://www.computer.org/csdl/proceedings-article/sp/2025/223600d180/26hiVmh7o9q)
+ [archive](https://eprint.iacr.org/2025/813)

## 作者

+ [Christodoulos Pappas](Christodoulos%20Pappas.md)
+ [Dimitrios Papadopoulos](20-杂/blog-archive/survey/researchers/Dimitrios%20Papadopoulos.md)
+ [Charalampos Papamanthou](20-杂/blog-archive/survey/researchers/Charalampos%20Papamanthou.md)

## 笔记

In this work, we introduce HydraProofs, the first vector commitment (VC) scheme that achieves the following two properties. (i) The prover can produce all the opening proofs for different elements (or consecutive sub-arrays) for a vector of size N in optimal time O(N). (ii) It is directly compatible with a family of zkSNARKs that encode their input as a multi-linear polynomial, i.e., our VC can be directly used when running the zkSNARK on its pre-image, without the need to open'' the entire vector pre-image inside the zkSNARK. To the best of our knowledge, all prior VC schemes either achieve (i) but are not efficiently pluggable'' into zkSNARKs (e.g., a Merkle tree commitment that requires re-computing the entire hash tree inside the circuit), or achieve (ii) but take (NlogN) time. We then combine HydraProofs with the seminal GKR protocol and apply the resulting zkSNARK in a setting where multiple users participate in a computation executed by an untrusted server and each user wants to ensure the correctness of the result and that her data was included. Our experimental evaluation shows our approach outperforms prior ones by 4-16x for prover times on general circuits. Finally, we consider two concrete application use cases, verifiable secret sharing and verifiable robust aggregation. For the former, our construction achieves the first scheme for Shamir's secret sharing with linear time prover (lower than the time needed for the dealer computation). For the second we propose a scheme that works against misbehaving aggregators and our experiments show it can be reasonably deployed in existing schemes with minimal slow-downs.

以下是中文翻译：

在本研究中，我们提出了HydraProofs，这是第一个同时实现以下两个特性的向量承诺(vector commitment, VC)方案：(i) 证明者可以在最优时间复杂度$O(N)$内为大小为N的向量中的不同元素(或连续子数组)生成所有开启证明。(ii) 它可以直接与将输入编码为多线性多项式的zkSNARK(零知识简洁非交互式知识论证)系列兼容，即我们的VC可以在zkSNARK对其原像进行运算时直接使用，无需在zkSNARK内部"开启"整个向量原像。据我们所知，所有先前的VC方案要么实现了(i)但无法高效地"插入"到zkSNARK中（例如，需要在电路内重新计算整个哈希树的默克尔树承诺），要么实现了(ii)但需要$(N\log N)$的时间。

我们随后将HydraProofs与开创性的GKR协议相结合，并将由此产生的zkSNARK应用于多用户参与由不可信服务器执行计算的场景中，其中每个用户都希望确保结果的正确性以及其数据被包含在内。我们的实验评估表明，在通用电路上，我们的方法在证明者时间方面比之前的方法提高了4-16倍。

最后，我们考虑了两个具体的应用案例：可验证秘密共享(verifiable secret sharing)和可验证鲁棒聚合(verifiable robust aggregation)。对于前者，我们的构造实现了Shamir秘密共享的首个线性时间证明者方案（低于经销商计算所需的时间）。对于后者，我们提出了一个可以应对恶意聚合者的方案，我们的实验表明，该方案可以以最小的性能损失合理地部署在现有方案中。

## 关键词

+ 向量承诺最优证明生成
+ 多线性多项式兼容zkSNARK
+ GKR协议结合
+ 可验证秘密共享线性时间
+ 可验证鲁棒聚合
+ 多用户隐私计算验证