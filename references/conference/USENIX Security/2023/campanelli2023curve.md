---
title: "Curve trees: Practical and transparent Zero-Knowledge accumulators"
标题简称:
论文类型: conference
会议简称: USENIX Security
发表年份: 2023
modified: 2025-04-18 09:44:37
created: 2025-04-13 17:08:34
---

## Curve trees: Practical and transparent Zero-Knowledge accumulators

## 发表信息

+ [原文链接](https://www.usenix.org/conference/usenixsecurity23/presentation/campanelli)

## 作者

+ [Matteo Campanelli](Matteo%20Campanelli.md)
+ Mathias Hall-Andersen 
+ Simon Holmgaard Kamp 

## 笔记

### 背景与动机
零知识集合成员证明是匿名支付、凭证和许可名单等隐私应用的核心模块，允许用户在不泄露具体元素的情况下证明其知晓集合中的某个元素。现有高效方案，如 Zcash Sapling，依赖强信任假设——需要一个由可信第三方生成的公共参考串，这构成了部署的障碍。为了解决这一信任问题，研究者探索了透明方案（无需可信设置），但它们在效率上存在瓶颈：有的计算或通信开销仍然较高，例如基于透明多项式承诺或环签名的方法；有的则依赖于群阶未知的累加器（如基于 RSA 或类群），其计算开销比椭圆曲线方案高约 20 倍。本文旨在填补这一空白：设计一个既完全透明（无需可信设置）又具有实际高效性的零知识集合成员证明方案，其安全仅依赖于离散对数和随机谕言模型这样简单且广泛使用的假设。

### 相关工作

[7] Ben-Sasson 等. Zerocash: Decentralized Anonymous Payments from Bitcoin. **IEEE S&P 2014** [Google Scholar](https://scholar.google.com/scholar?q=Zerocash+Decentralized+Anonymous+Payments+from+Bitcoin)
> 核心思路：引入基于零知识证明的匿名加密货币概念。
> 局限与区别：其核心证明系统需要可信设置，而 Curve Trees 完全透明。

[13] Bünz 等. Bulletproofs: Short Proofs for Confidential Transactions and More. **IEEE S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Bulletproofs+Short+Proofs+for+Confidential+Transactions+and+More)
> 核心思路：提供了一种高效的透明的证明系统，用于范围证明和一般关系。
> 局限与区别：Bulletproofs 本身不提供集合压缩功能；Curve Trees 将 Bulletproofs 与一种新的代数数据结构结合，实现了高效的集合成员证明。

[22] Catalano 等. On the Impossibility of Algebraic Vector Commitments in Pairing-Free Groups. **ePrint 2022** [Google Scholar](https://scholar.google.com/scholar?q=On+the+Impossibility+of+Algebraic+Vector+Commitments+in+Pairing-Free+Groups)
> 核心思路：证明了在无配对群中，不可能同时实现简短承诺和线性验证的代数向量承诺。
> 局限与区别：Curve Trees 通过利用 2-cycle 椭圆曲线的结构，优雅地绕过了这一不可能结果，实现了高效的代数操作。

[33] Grassi 等. Poseidon: A New Hash Function for Zero-Knowledge Proof Systems. **USENIX Security 2021** [Google Scholar](https://scholar.google.com/scholar?q=Poseidon+A+New+Hash+Function+for+Zero-Knowledge+Proof+Systems)
> 核心思路：提出一类对零知识证明系统友好的哈希函数。
> 局限与区别：Poseidon 的实例化缺乏长期的安全性分析，而 Curve Trees 基于经典的 DLOG 假设，安全性基础更稳固，且实验性能显著优于基于 Poseidon 的 Merkle 树方案。

[36] Hopwood 等. Zcash Protocol Specification, Version 2021.2.16 [Nu5 Proposal]. **Technical Report 2021** [Google Scholar](https://scholar.google.com/scholar?q=Zcash+Protocol+Specification+Version+2021.2.16+Nu5+Proposal)
> 核心思路：在 Zcash 中使用了基于 Pedersen 哈希的 Merkle 树和 Groth16 证明系统。
> 局限与区别：该方案依赖 Groth16 的可信设置，并且其“Pedersen 哈希”电路需要约 44000 个约束，而 Curve Trees 的电路仅需约 4500 个约束，效率提高一个数量级。

[39] Lai 等. Omniring: Scaling Private Payments without Trusted Setup. **ACM CCS 2019** [Google Scholar](https://scholar.google.com/scholar?q=Omniring+Scaling+Private+Payments+without+Trusted+Setup)
> 核心思路：提出一种拥有亚线性证明大小但线性验证时间的透明匿名支付方案。
> 局限与区别：Omniring 的验证时间与集合大小成线性关系，而 Curve Trees 的验证时间为亚线性。

### 核心技术与方案
本文的核心创新是 Curve Trees，一种用于零知识集合成员证明的完全透明且高效的累加器构造。它巧妙地结合了 Pedersen 承诺、2-cycle 椭圆曲线和 Commit-and-Prove 技术。

**1. Curve Tree 数据结构**
Curve Tree 本质上是一棵经过特殊设计的 Merkle 树。与标准 Merkle 树不同，其内部节点不是传统哈希函数的输出，而是另一个椭圆曲线上的点。关键技巧在于利用 2-cycle 椭圆曲线：存在一对椭圆曲线 $\mathbb{E}_{(\text{evn})}$ 和 $\mathbb{E}_{(\text{odd})}$，使得一条曲线的基域是另一条曲线的标量域，反之亦然。这意味着 $\mathbb{E}_{(\text{evn})}$ 上的一个点 $(X, Y)$ 可以直接被 $\mathbb{E}_{(\text{odd})}$ 的标量域（$\mathbb{F}_p$）中的元素表示。因此，可以定义一个“压缩函数”：将 $\mathbb{E}_{(\text{evn})}$ 上的 $\ell$ 个点，通过计算它们在 $\mathbb{E}_{(\text{odd})}$ 上的 Pedersen 承诺（视为一组标量的线性组合），压缩成一个 $\mathbb{E}_{(\text{odd})}$ 上的点。树的每一层交替使用这条曲线，从而克服了“类型不匹配”的问题，形成一棵完全的“代数”树。树的根节点是整个集合的公开摘要。

**2. 零知识成员证明**
为了在不泄露被证明元素的前提下证明其属于集合，Curve Trees 利用了 Pedersen 承诺的可重随机化特性。证明过程如下：证明者首先沿着从根到目标叶子的路径，对路径上的每个内部节点进行重随机化，生成一系列隐藏版本的节点（$\hat{C}^{(0)}, \hat{C}^{(1)}, ..., \hat{C}^{(D-1)}$）。然后，证明者使用 Commit-and-Prove 系统（实例化为 Bulletproofs）来证明以下两个关系，而不是证明每一层：
*   **偶数层关系 ($\mathcal{R}^{(\text{evn-levels})}$)**：证明所有偶数层的重随机化父节点（在 $\mathbb{E}_{(\text{evn})}$ 上）与它的一个子节点（在 $\mathbb{E}_{(\text{odd})}$ 上）之间的 Pedersen 承诺关系是正确的。
*   **奇数层关系 ($\mathcal{R}^{(\text{odd-levels})}$)**：类似地，证明所有奇数层的对应关系。
这种将 D 层关系压缩为两个证明的技巧，使得证明的大小和验证时间主要取决于树的深度 D，而非集合大小 n。

**3. 安全性证明**
方案的安全性依赖于标准假设：
*   **可计算绑定**：基于椭圆曲线上的 DLOG 假设（广义离散对数假设）。证明的核心是通过归纳法，利用 DLOG 假设保证恶意证明者无法找到一个不在集合中的元素，使其能通过重随机化与树的根节点匹配。具体地，如果恶意证明者成功，则可以通过提取的方程构造一个打破 DLOG 假设的算法。
*   **完美隐藏**：直接来源于 Pedersen 承诺的完美隐藏性质。
*   **零知识**：通过模拟器实现。模拟器可以生成伪造的、但无法区分的重随机化节点和 Bulletproofs 证明。

**4. 复杂度分析**
*   **通信复杂度**（证明大小）：$O(D + \log n)$。其中 D 是树的深度，$\log n$ 项来自 Bulletproofs 的通信轮次。具体而言，证明由 D-1 个重随机化的中间节点和两个 Bulletproofs 组成。
*   **计算复杂度**：
    *   **证明者**：$O(n)$，其中 $n$ 是集合大小，对应于构建树和生成证明的开销。
    *   **验证者**：$O(\sqrt[D]{n})$，仅依赖于深度 D，对于固定深度是常数。

### 核心公式与流程

**[Curve Tree 节点标签计算]**
$$
C = \left\langle \vec{\mathrm{X}}, \vec{G}_{(\_)}^\mathrm{x} \right\rangle + \left\langle \vec{\mathrm{Y}}, \vec{G}_{(\_)}^\mathrm{y} \right\rangle
$$
> 作用：定义了一个内部节点 C 如何由它的 $\ell$ 个子节点（表示为点 $(X_i, Y_i)$）计算得出。这本质上是基于 2-cycle 曲线中另一条曲线的 Pedersen 承诺，实现了代数压缩。

**[单层选择-重随机化关系]**
$$
\mathcal{R}^{(\text{single-level},\mathbb{E}_{(\_)})} := \left\{ 
\begin{array}{c} 
C = \langle \vec{\mathbb{X}}, \vec{G}_{(\_)}^\mathrm{x} \rangle + \langle \vec{\mathbb{Y}}, \vec{G}_{(\_)}^\mathrm{y} \rangle + [r] \cdot H_{(\_)} \\ 
\hat{C} = (\mathbb{X}_i, \mathbb{Y}_i) + [\delta] \cdot H_{\text{other}(\_)} 
\end{array}
\right\}
$$
> 作用：定义了单个树层上的核心证明关系。证明者需证明：(1) 已知一个重随机化的父节点 C 的“打开”（即其子节点列表），(2) 已知一个重随机化的子节点 $\hat{C}$，它是 C 的某个子节点 $(\mathbb{X}_i, \mathbb{Y}_i)$ 的重随机化版本。

**[压缩点版本的优化关系]**
$$
\mathcal{R}^{(\text{single-level}^\star, (\underline{\cdot}))} := \left\{ 
\begin{array}{c} 
C = \langle \vec{\mathbb{X}}, \vec{G}_{(\underline{\cdot})}^\mathrm{x} \rangle + [r] \cdot H_{(\underline{\cdot})} \\ 
\wedge (\mathbb{X}_i, \mathbb{Y}) \in \mathcal{P}_{\text{other}(\underline{\cdot})} \\ 
\wedge \hat{C} = (\mathbb{X}_i, \mathbb{Y}) + [\delta] \cdot H_{\text{other}(\underline{\cdot})} 
\end{array}
\right\}
$$
> 作用：这是通过点压缩优化后的关系。它只使用子节点的 X 坐标来计算父节点，并通过二次剩余等特性定义“允许点”集合 $\mathcal{P}$，从而消除了对 Y 坐标的依赖，减少了电路规模。

### 实验结果
实验在一个具有 8 个 vCPU（4 个物理核心）的 Intel Xeon 8375C 实例上进行。核心性能数据（针对 128 位安全级）如下：
*   **Curve Trees 核心性能**：对于规模为 $2^{40}$ 的集合，使用 Pasta 曲线时，零知识成员证明大小为 2.9 KB，生成时间 1.74 秒，验证时间 40.41 毫秒，批处理（100 个）验证时间 2.73 毫秒。
*   **与 Poseidon Merkle 树对比**：对于 $2^{30}$ 的集合，Curve Trees (Pasta) 的生成时间（1.5 秒）是 Poseidon (8:1) 方案（8.5 秒）的 1/5.6，验证时间（31 毫秒）是 Poseidon (825 毫秒) 的 1/27。
*   **与匿名支付系统对比**：在 VCash 应用中，对于 $2^{32}$ 匿名集，Curve Trees 方案（Pasta）的交易大小为 4 KB，生成时间 3.43 秒，验证时间 78.40 毫秒，批处理验证时间 4.98 毫秒。这优于非透明的 Zcash Sapling（2.8 KB，2.38 秒，7 毫秒），并且在批处理场景下，性能优于所有对比的透明方案。
*   **参数规模**：实验在集合大小从 $2^{20}$ 到 $2^{40}$ 的范围内均取得了良好性能，证明了方案的可扩展性。

### 局限性与开放问题
一个潜在局限性是当集合大小极小（如 $2^{10}$）时，Curve Trees 因引入恒定开销（如树结构）可能不如某些针对小集合优化的方案（如 Omniring）。其次，方案依赖于 2-cycle 椭圆曲线的存在，限制了可选的曲线种类，例如 Halo2 需要带平滑子群的曲线，因而不能使用 secp256k1/secq256k1 循环，而 Curve Trees 支持后者。尽管安全性基于经典假设，但实际使用的 Pedersen 哈希和 Bulletproofs 的安全性证明在 ROM 中，这引入了一个可公开访问的随机谕言机。未来的工作可以探索如何在不依赖 2-cycle 曲线的情况下实现类似的代数结构，或者将本方案与更新、更高效的证明系统（如 Halo2）相结合，以进一步提升性能。

### 强关联论文

[7] Eli Ben-Sasson, Alessandro Chiesa, Christina Garman, Matthew Green, Ian Miers, Eran Tromer, Madars Virza. Zerocash: Decentralized anonymous payments from bitcoin. **IEEE S&P 2014**

[13] Benedikt Bünz, Jonathan Bootle, Dan Boneh, Andrew Poelstra, Pieter Wuille, Greg Maxwell. Bulletproofs: Short proofs for confidential transactions and more. **IEEE S&P 2018**

[22] Dario Catalano, Dario Fiore, Rosario Gennaro, Emanuele Giunta. On the impossibility of algebraic vector commitments in pairing-free groups. **ePrint 2022**

[33] Lorenzo Grassi, Dmitry Khovratovich, Christian Rechberger, Arnab Roy, Markus Schofnegger. Poseidon: A new hash function for zero-knowledge proof systems. **USENIX Security 2021**

[36] Daira Hopwood, Sean Bowe, Taylor Hornby, Nathan Wilcox. Zcash protocol specification, version 2021.2.16 [nu5 proposal]. **Technical Report 2021**

[39] Russell W. F. Lai, Viktoria Ronge, Tim Ruffing, Dominique Schröder, Sri Aravinda Krishnan Thyagarajan, Jiafan Wang. Omniring: Scaling private payments without trusted setup. **ACM CCS 2019**


## 关键词

+ 曲线树零知识集合累加器
+ 透明零知识集合成员证明
+ 无信任设置累加器
+ 匿名加密货币Vcash
+ 椭圆曲线2-周期承诺
+ 离散对数随机预言机安全
