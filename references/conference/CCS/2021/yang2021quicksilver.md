---
title: "QuickSilver: Efficient and Affordable Zero-Knowledge Proofs for Circuits and Polynomials over Any Field"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2021
modified: 2025-04-09 15:56:12
---

## QuickSilver: Efficient and Affordable Zero-Knowledge Proofs for Circuits and Polynomials over Any Field

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3460120.3484556)

## 作者

+ [Kang Yang](Kang%20Yang.md)
+ Pratik Sarkar
+ [Chenkai Weng](Chenkai%20Weng.md)
+ [Xiao Wang](Xiao%20Wang.md)

## 笔记

Zero-knowledge (ZK) proofs with an optimal memory footprint have attracted a lot of attention, because such protocols can easily prove very large computation with a small memory requirement. Such ZK protocol only needs O(M) memory for both parties, where M is the memory required to verify the statement in the clear. In this paper, we propose several new constant-round ZK protocols in this setting, which improve the concrete efficiency and, at the same time, enable sublinear amortized communication for circuits with some notion of relaxed uniformity. In the circuit-based model, where the computation is represented as a circuit over a field, our ZK protocol achieves a communication complexity of 1 field element per non-linear gate for any field size while keeping the computation very cheap. We implemented our protocol, which shows extremely high efficiency and affordability. Compared to the previous best-known implementation, we achieve 6x--7x improvement in computation and 3x--7x improvement in communication. When running on intro-level AWS instances, our protocol only needs one US dollar to prove one trillion AND gates (or 2.5 US dollars for one trillion multiplication gates over a 61-bit field). In the setting where part of the computation can be represented as a set of polynomials with a "degree-separated" format, we can achieve communication sublinear to the polynomial size: the communication only depends on the total number of distinct variables in all the polynomials and the highest degree of all polynomials, independent of the number of multiplications to compute all polynomials. Using the improved ZK protocol, we can prove matrix multiplication with communication proportional to the input size, rather than the number of multiplications. Proving the multiplication of two 1024 x 1024 matrices, our implementation, with one thread and 1 GB of memory, only needs 10 seconds and communicates 25 MB.

以下是中文翻译：

具有最优内存占用的零知识（Zero-knowledge，ZK）证明引起了广泛关注，因为此类协议可以在较小的内存需求下轻松证明大规模计算。这种ZK协议仅需要双方使用O(M)的内存，其中M是明文验证声明所需的内存。在本文中，我们提出了几种新的常数轮ZK协议，这些协议不仅提高了具体效率，同时还为具有某种松弛一致性概念的电路实现了子线性的分摊通信复杂度。

在基于电路的模型中，即计算以域上的电路形式表示时，我们的ZK协议在保持计算成本很低的同时，对任何域大小都实现了每个非线性门仅需1个域元素的通信复杂度。我们实现的协议展现出极高的效率和经济性。与之前最好的实现相比，我们在计算效率上实现了6-7倍的提升，在通信效率上实现了3-7倍的提升。在入门级AWS实例上运行时，我们的协议仅需1美元就能证明一万亿个AND门（或2.5美元证明一万亿个61位域上的乘法门）。

在部分计算可以表示为具有"度分离"（degree-separated）格式的多项式集合的情况下，我们可以实现相对于多项式规模的子线性通信：通信量仅取决于所有多项式中不同变量的总数和所有多项式的最高次数，而与计算所有多项式所需的乘法次数无关。使用改进的ZK协议，我们可以用与输入规模成比例的通信量来证明矩阵乘法，而不是与乘法次数成比例。对于1024 x 1024矩阵的乘法证明，我们的实现仅使用单线程和1GB内存，只需10秒时间和25MB通信量。

## 关键词

+ 零知识证明
+ 电路验证
+ 通信优化
+ 内存高效
+ 隐私保护