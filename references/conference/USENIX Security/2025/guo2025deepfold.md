---
title: "DeepFold: Efficient Multilinear Polynomial Commitment from Reed-Solomon Code and Its Application to Zero-knowledge Proofs"
标题简称:
论文类型: conference
会议简称: USENIX Security
发表年份: 2025

modified: 2025-06-09 10:35:01
created: 2025-05-13 09:23:43
---

## DeepFold: Efficient Multilinear Polynomial Commitment from Reed-Solomon Code and Its Application to Zero-knowledge Proofs

## 发表信息

+ 原文链接暂无
+ [archive](https://eprint.iacr.org/2024/1595)

## 作者

+ [Yanpei Guo](Yanpei%20Guo.md)
+ Xuanming Liu
+ Kexi Huang
+ Wenjie Qu
+ Tianyang Tao
+ [Jiaheng Zhang](Jiaheng%20Zhang.md)

## 笔记

This work presents Deepfold, a novel multilinear polynomial commitment scheme (PCS) based on Reed-Solomon code that offers optimal prover time and a more concise proof size. For the first time, Deepfold adapts the FRI-based multilinear PCS to the list decoding radius setting, requiring significantly fewer query repetitions and thereby achieving a $3 \times$ reduction in proof size compared to Basefold (Crypto'24), while preserving its advantages in prover time. Compared with PolyFRIM (USENIX Security'24), Deepfold achieves a $2 \times$ improvement in prover time, verifier time, and proof size. Another contribution of this work is a batch evaluation scheme, which enables the FRI-based multilinear PCS to handle polynomials whose size is not a power of two more efficiently.

Our scheme has broad applications in zk-SNARKs, since PCS is a key component in modern zk-SNARK constructions. For example, when replacing the PCS component of Virgo (S&P'20) with Deepfold, our scheme achieves a $2.5 \times$ faster prover time when proving the knowledge of a Merkle tree with 256 leaves, while maintaining the similar proof size. When replacing the PCS component of HyperPlonk (Eurocrypt'23) with Deepfold, our scheme has about $3.6 \times$ faster prover time. Additionally, when applying our arbitrary length input commitment to verifiable matrix multiplications for matrices of size $1200 \times 768$ and $768 \times 2304$, which are actual use cases in GPT-2 model, the performance showcases a $2.4 \times$ reduction in prover time compared to previous approaches.

以下是中文翻译：

本文提出了Deepfold，这是一种基于里德-所罗门码(Reed-Solomon code)的新型多重线性多项式承诺方案(multilinear polynomial commitment scheme, PCS)，它实现了最优的证明者时间并具有更简洁的证明规模。Deepfold首次将基于FRI的多重线性PCS应用于列表解码半径(list decoding radius)设置，显著减少了查询重复次数，从而与Basefold (Crypto'24)相比实现了证明规模减少3倍，同时保持了其在证明者时间方面的优势。与PolyFRIM (USENIX Security'24)相比，Deepfold在证明者时间、验证者时间和证明规模方面都实现了2倍的改进。本工作的另一个贡献是批量评估方案，它使基于FRI的多重线性PCS能够更高效地处理大小不是2的幂次方的多项式。

我们的方案在零知识简洁非交互式论证系统(zk-SNARKs)中有广泛的应用，因为PCS是现代zk-SNARK构造中的关键组件。例如，当用Deepfold替换Virgo (S&P'20)中的PCS组件时，在证明具有256个叶子的默克尔树(Merkle tree)的知识时，我们的方案实现了2.5倍更快的证明者时间，同时保持了类似的证明规模。当用Deepfold替换HyperPlonk (Eurocrypt'23)中的PCS组件时，我们的方案实现了约3.6倍更快的证明者时间。此外，当将我们的任意长度输入承诺应用于大小为$1200 \times 768$和$768 \times 2304$的矩阵的可验证矩阵乘法时（这些是GPT-2模型中的实际应用场景），与之前的方法相比，性能展示了2.4倍的证明者时间减少。

## 关键词

+ DeepFold多线性多项式承诺方案
+ 里德-所罗门码密码应用
+ FRI基多线性承诺优化
+ 列表解码半径设置
+ zk-SNARK证明者效率
+ 批量评估任意长度多项式