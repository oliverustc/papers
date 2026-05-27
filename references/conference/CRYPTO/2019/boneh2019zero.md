---
title: "Zero-knowledge proofs on secret-shared data via fully linear PCPs"
doi: 10.1007/978-3-030-26954-8_3

标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 2019
modified: 2025-04-11 11:26:36
---
## Zero-knowledge proofs on secret-shared data via fully linear PCPs

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-030-26954-8_3)

## 作者

+ [Dan Boneh](Dan%20Boneh.md) 
+ Elette Boyle 
+ Henry Corrigan-Gibbs 
+ Niv Gilboa 
+ [Yuval Ishai](Yuval%20Ishai.md)
## 笔记

We introduce and study the notion of fully linear probabilistically checkable proof systems. In such a proof system, the verifier can make a small number of linear queries that apply jointly to the input and a proof vector.

Our new type of proof system is motivated by applications in which the input statement is not fully available to any single verifier, but can still be efficiently accessed via linear queries. This situation arises in scenarios where the input is partitioned or secret-shared between two or more parties, or alternatively is encoded using an additively homomorphic encryption or commitment scheme. This setting appears in the context of secure messaging platforms, verifiable outsourced computation, PIR writing, private computation of aggregate statistics, and secure multiparty computation (MPC). In all these applications, there is a need for fully linear proof systems with short proofs.

While several efficient constructions of fully linear proof systems are implicit in the interactive proofs literature, many questions about their complexity are open. We present several new constructions of fully linear zero-knowledge proof systems with sublinear proof size for “simple” or “structured” languages. For example, in the non-interactive setting of fully linear PCPs, we show how to prove that an input vector $x \in {\mathbb{F}}^n$, for a finite field ${\mathbb {F}}$, satisfies a single degree-2 equation with a proof of size $O(\sqrt{n})$ and $O(\sqrt{n})$ linear queries, which we show to be optimal. More generally, for languages that can be recognized by systems of constant-degree equations, we can reduce the proof size to $O(\log n)$ at the cost of $O(\log n)$ rounds of interaction.

We use our new proof systems to construct new short zero-knowledge proofs on distributed and secret-shared data. These proofs can be used to improve the performance of the example systems mentioned above.

Finally, we observe that zero-knowledge proofs on distributed data provide a general-purpose tool for protecting MPC protocols against malicious parties. Applying our short fully linear PCPs to “natural” MPC protocols in the honest-majority setting, we can achieve unconditional protection against malicious parties with sublinear additive communication cost. We use this to improve the communication complexity of recent honest-majority MPC protocols. For instance, using any pseudorandom generator, we obtain a 3-party protocol for Boolean circuits in which the amortized communication cost is only one bit per AND gate per party (compared to 10 bits in the best previous protocol), matching the best known protocols for semi-honest parties.

以下是中文翻译：

我们介绍并研究了完全线性概率可检验证明系统(fully linear probabilistically checkable proof systems)的概念。在这种证明系统中，验证者可以对输入和证明向量进行少量的联合线性查询。

我们提出的这种新型证明系统源于这样的应用场景：输入陈述并不完全对任何单个验证者可用，但仍可以通过线性查询进行高效访问。这种情况出现在输入被分割或在两方或多方之间进行秘密共享的场景中，或者输入使用加法同态加密(additively homomorphic encryption)或承诺方案进行编码的情况下。这种设置出现在安全消息平台、可验证的外包计算、PIR写入、私有聚合统计计算以及安全多方计算(MPC)等场景中。在所有这些应用中，都需要具有简短证明的完全线性证明系统。

虽然在交互式证明文献中已隐含了几种高效的完全线性证明系统构造，但关于其复杂度的许多问题仍未解决。我们为"简单"或"结构化"语言提出了几种新的具有子线性证明规模的完全线性零知识证明系统构造。例如，在完全线性PCP的非交互式设置中，我们展示了如何证明输入向量$x \in {\mathbb{F}}^n$（其中${\mathbb{F}}$为有限域）满足单个二次方程，证明规模为$O(\sqrt{n})$且需要$O(\sqrt{n})$次线性查询，我们证明这是最优的。更一般地，对于可以被常数次方程系统识别的语言，我们可以通过$O(\log n)$轮交互将证明规模减少到$O(\log n)$。

我们使用这些新的证明系统构造了分布式和秘密共享数据上的新型短零知识证明。这些证明可用于改进上述示例系统的性能。

最后，我们观察到分布式数据上的零知识证明为保护MPC协议免受恶意方攻击提供了一个通用工具。将我们的短完全线性PCP应用于诚实多数设置下的"自然"MPC协议中，我们可以以子线性附加通信成本实现对恶意方的无条件防护。我们用这一成果改进了最近的诚实多数MPC协议的通信复杂度。例如，使用任何伪随机生成器，我们得到了一个用于布尔电路的三方协议，其中每个AND门每方的摊销通信成本仅为一比特（相比之前最佳协议的10比特），达到了已知的半诚实方案的最佳水平。


## 关键词

+ 完全线性PCP零知识证明
+ 秘密共享分布式数据证明
+ 子线性证明大小MPC安全
+ 加法同态加密线性查询验证
+ 诚实多数MPC通信复杂度改进