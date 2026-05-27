---
title: "Threshold signatures in the multiverse"
doi: 10.1109/sp46215.2023.10179436
标题简称:
论文类型: conference
会议简称: S&P
发表年份: 2023
created: 2025-04-17 10:41:54
modified: 2025-04-17 10:42:38
---
## Threshold signatures in the multiverse

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/10179436)

## 作者

+ Leemon Baird 
+ [Sanjam Garg](Sanjam%20Garg.md) 
+ [Abhishek Jain](Abhishek%20Jain.md)
+ [Pratyay Mukherjee](Pratyay%20Mukherjee.md) 
+ Rohit Sinha 
+ [Mingyuan Wang](Mingyuan%20Wang.md) 
+ [Yinuo Zhang](Yinuo%20Zhang.md)
## 笔记

好的，以下是根据您提供的论文全文生成的详尽结构化笔记。

### 背景与动机

区块链应用（如去中心化预言机网络）中，不同智能合约对不同数据源、节点声誉和安全性阈值有定制化需求，这导致一个系统中存在多个由不同节点子集和阈值定义的“宇宙”。传统的门限签名方案 [25, 26] 设计用于一个静态的、所有验证者共享相同信任模型的“单宇宙”场景。若在该场景下为每个宇宙独立运行一个门限签名实例，会导致严重可扩展性问题：节点密钥、签名计算和网络带宽均随宇宙数量线性增长，例如在模拟 Chainlink 的2000节点、100宇宙配置下，节点带宽可达近1GB [19, 27]。另一种可行方案是使用 SNARK [11, 12] 证明签名集合的有效性，但会引入极高的聚合计算开销（数分钟）和潜在的不安全哈希函数 [7]，且其安全证明不在随机预言机模型中。多签名方案 [14, 37] 虽能实现密钥无关，但聚合签名和验证计算量均与宇宙大小成线性关系，导致高昂的链上验证成本。本文旨在填补这一空白，提出一种多宇宙阈值签名（MTS）方案，其中任何节点可以使用恒定的密钥和签名，实现非交互式宇宙创建、紧凑的聚合签名和高效的链上验证。

### 相关工作

[25] Desmedt等. Society and group oriented cryptography: A new concept. **CRYPTO 1987** [Google Scholar](https://scholar.google.com/scholar?q=Society+and+group+oriented+cryptography)
> 核心思路：提出了门限密码学的概念，允许将秘密拆分给多个参与者。
> 局限与区别：仅适用于单一固定门限和参与者集合，不适用于多宇宙动态设置。

[26] Desmedt等. Threshold cryptosystems. **CRYPTO 1989** [Google Scholar](https://scholar.google.com/scholar?q=Threshold+cryptosystems)
> 核心思路：将门限概念扩展到公钥密码系统，提出了门限签名方案的基础框架。
> 局限与区别：同样局限于固定门限，无法处理不同验证者有不同的信任模型。

[33] Gennaro等. Secure distributed key generation for discrete-log based cryptosystems. **Journal of Cryptology 2007** [Google Scholar](https://scholar.google.com/scholar?q=Secure+distributed+key+generation+for+discrete-log+based+cryptosystems)
> 核心思路：设计了交互式分布式密钥生成协议，使得多方可合作产生一个共享公钥。
> 局限与区别：其交互式特性在多宇宙场景下会频繁执行，导致高昂的通信和计算开销。

[16] Boneh等. Short signatures from the Weil pairing. **ASIACRYPT 2001** [Google Scholar](https://scholar.google.com/scholar?q=Short+signatures+from+the+Weil+pairing)
> 核心思路：提出了基于双线性对的短签名，具有签名聚合和门限特性。
> 局限与区别：本文在其基础上扩展，通过改变设置方式处理多宇宙问题，但原始的 BLS 方案（如结合 [33]）会产生宇宙相关的密钥。

[14] Boneh等. Compact multi-signatures for smaller blockchains. **ASIACRYPT 2018** [Google Scholar](https://scholar.google.com/scholar?q=Compact+multi-signatures+for+smaller+blockchains)
> 核心思路：提出了紧凑的多签名方案，聚合签名大小恒定。
> 局限与区别：在多宇宙场景下，聚合签名需包含签名者身份列表，导致验证开销和签名大小与宇宙规模线性相关。

[38] Micali等. Compact certificates of collective knowledge. **IEEE S&P 2021** [Google Scholar](https://scholar.google.com/scholar?q=Compact+certificates+of+collective+knowledge)
> 核心思路：使用对数大小的证明来证明一个阈值数量的签名，优化了加权或大规模场景。
> 局限与区别：其证书大小在实践中（例如几百个节点）反而可能超过简单的签名列表，且链上验证成本高昂。

### 核心技术与方案

本文的核心技术主要体现在其从单宇宙 BLS 门限签名到多宇宙 MTS 的构造思路。该方案的核心思想是解耦单个节点的密钥与特定宇宙的验证密钥。

1.  **密钥生成是非交互式的**：系统中的每个节点独立运行 `KGen`，使用一个 PRG 种子作为私钥 $\mathsf{sk}=s$，并生成一个 $B$ 维的向量公钥 $\mathsf{pk}=g_1^{F(s)}$。这使得节点的密钥独立于它所属的任何宇宙。

2.  **针对一个特定宇宙的非交互式设置**：创建一个由节点集合 $U$、权重 $\{W_i\}$ 和阈值 $T$ 定义的宇宙 $(U, \Lambda)$。首先，系统将所有节点公钥拼接成一个总权重为 $W = \sum W_i$ 的向量 $\overline{\mathsf{pk}}$，并隐式定义一个 $W-1$ 次多项式 $f$，使得 $g_1^{f(x)}$ 对应 $\overline{\mathsf{pk}}[x]$。为了将门限从 $W$ 降低到 $T$，方案引入了公共点 $\{g_1^{f(x)}\}$，其中 $x \in \{- (W-T), \dots, -1, 0\}$。关键的安全机制在于，每个参与设置的节点 $P_i$ 分享一个随机数 $k_i$，使得最终的公共参数 `pp` 包含所有公共点的随机指数幂，即 $g_1^{k \cdot f(x)}$，其中 $k$ 是所有 $k_i$ 的带系数线性组合。这防止了攻击者根据公共点破解私钥。

3.  **签名与聚合是宇宙无关的**：节点在签名消息 $m$ 时，只需计算其私钥对应的 BLS 签名 $\sigma = H(m)^{F(\mathsf{sk})}$。这个过程完全独立于宇宙。对于任意宇宙，聚合者收集超过阈值 $T$ 的签名后，执行 `Aggregate` 算法。该算法使用宇宙的 `pp` 和 Lagrange 系数 $\lambda_i$，计算三个元素：$\sigma' = \langle \vec{\sigma}, \vec{\lambda}^{\mathsf{par}} \rangle$，$\sigma_0' = \langle B, \vec{\lambda}^{\mathsf{pub}} \rangle$ 和 $\sigma_1' = \langle A, \vec{\lambda}^{\mathsf{pub}} \rangle$，其中 $B$ 和 $A$ 分别代表 `pp` 中的 $g_1^{f(x)}$ 和 $g_1^{k \cdot f(x)}$ 部分。

4.  **验证的安全性和高效性**：验证使用两个双线性对等式：
   $$e(\mathsf{VK}_0 / \sigma_0', H(m)) = e(g_1, \sigma')$$
   $$e(\sigma_1', g_2) = e(\sigma_0', \mathsf{VK}_1)$$
   第一个等式确保聚合签名 $\sigma'$ 是消息 $m$ 被最多 $T$ 个签名者签名的结果；第二个等式强制 $\sigma_0'$ 必须是公共点 $g_1^{f(x)}$ 的线性组合（而非攻击者随意伪造），这不仅保证了第一个等式计算的有效性，也是安全性证明的关键。

5.  **加权设置的扩展**：通过“虚拟化”实现，即权重为 $W_i$ 的节点被视作 $W_i$ 个虚拟节点，每个生成一个部分签名，但所有虚拟节点共享同一个 PRG 种子密钥。

安全性基于 co-CDH 假设 [16] 和一个知识假设 [23]，证明策略是：若存在敌手能伪造 MTS 签名，则可构造另一敌手来求解 co-CDH 问题。该构造在模拟中将 co-CDH 挑战嵌入到有限个（随机选择的）诚实节点的公钥和随机预言机的响应中，并通过知识提取证明敌手签名中 $\sigma_0'$ 的合法性，进而提取出关于挑战的线性关系来求解。方案的通信复杂度方面，每个节点发送的签名大小为 $B$ 个群元素；聚合者最终生成的聚合签名为 3 个群元素；验证者计算量为 4 次双线性对运算和 1 次群乘法。

### 核心公式与流程

**[KGen：密钥生成]**
$$(\mathsf{pk} = g_1^{F(s)}, \mathsf{sk} = s) \in G_1^B \times \{0,1\}^\kappa$$
> 作用：每个节点独立生成一个 PRG 种子作为私钥，并扩展出一个 $B$ 维的公钥向量，与宇宙无关。

**[Sign：签名]**
$$\sigma = H(m)^{F(\mathsf{sk})} \in G_2^B$$
> 作用：节点使用私钥对消息 $m$ 进行签名，输出一个 $B$ 维的群元素向量。

**[Verify：验证（关键等式）]**
$$\left\{ \begin{array}{c} e(\mathsf{VK}_0 / \sigma_0', H(m)) = e(g_1, \sigma') \\ e(\sigma_1', g_2) = e(\sigma_0', \mathsf{VK}_1) \end{array} \right.$$
> 作用：第一个等式利用双线性对检查聚合签名 $\sigma'$ 是 $H(m)$ 的线性组合结果，其指数等于公钥的线性组合（即 $\mathsf{VK}_0$ 减去$\sigma_0'$的指数）。第二个等式强制 $\sigma_0'$ 必须是公共点的正确线性组合，防止伪造。

**[Aggregate：聚合（关键步骤）]**
$${\lambda_i} \leftarrow \text{Lagrange}(X \cup \{-(W-T), \dots, -1\})$$
$$\sigma_0' = \langle \vec{B}, \vec{\lambda}^{\text{pub}} \rangle, \quad \sigma_1' = \langle \vec{A}, \vec{\lambda}^{\text{pub}} \rangle, \quad \sigma' = \langle \vec{\sigma}, \vec{\lambda}^{\text{par}} \rangle$$
> 作用：聚合者根据参与签名的集合 $X$ 计算 Lagrange 系数 $\lambda_i$。利用这些系数，对多个签名 $\sigma$ 和公共参数（$\vec{B}$ 为公共点，$\vec{A}$ 为其随机指数版本）进行指数上的线性组合，生成最终的聚合签名。

### 实验结果

作者使用 BLS12-381 曲线在 Rust 中实现了 MTS 方案，并在 Macbook Pro M1 Pro 芯片上进行单线程基准测试。实验对比了 zk-SNARK（Groth16 / PLONK）、紧凑证书 [38]、标准门限 BLS 和 BLS 多签名 [14] 等方案。在 2000 节点、100 宇宙的模拟配置（权值 $B=1$）下：**
1) 带宽**：MTS 的聚合带宽仅为 0.188 MB，而标准门限 BLS 需要 9.16 MB，在加权场景（$B=50$）下差距更大（MTS 为 9.16 MB，门限 BLS 为 457 MB）。**
2) 聚合时间**：MTS 聚合时间为 0.61 秒，远超 zk-SNARK 的 302 秒，也比门限 BLS 的 0.282 秒稍慢，但作者指出这是可接受的。**
3) 签名与验证性能**：MTS 的签名大小为 192 字节（2个$G_1$，1个$G_2$），与 zk-SNARK 方案相同，但大于门限 BLS 的 48 字节。MTS 的验证时间为 6.43 毫秒（4 次配对运算，1 次群乘法），略慢于门限 BLS 的 3.51 毫秒，但显著优于紧凑证书的 190 毫秒和多签名的 5.12 毫秒。** 
4) EVM Gas 成本**：MTS 的验证 Gas 成本为 198,500，设置成本为 90,000，优于多签名方案（验证 415,000，设置高达 60,000,000）。实验表明，MTS 在带宽、聚合效率方面优于或与对比方案持平，但在验证和签名大小上并非最优，却提供了独特的“多宇宙”特性，在实用参数下整体性能良好。

### 局限性与开放问题

本文的 MTS 方案在安全性上并未达到强不可伪造性（strong unforgeability），即同一个消息可以存在多个不同的有效聚合签名，因为聚合者可以从超过阈值的签名中选择子集进行聚合。这限制了其在某些需要签名唯一性的应用场景。此外，作者承认其安全性证明中的安全损失（security loss）并非最优，这可能会影响实际部署时参数的选择。最后，一个开放问题是能否在不显著牺牲效率的前提下，设计出满足强不可伪造性的 MTS 方案。

### 强关联论文

[14] Boneh等. Compact multi-signatures for smaller blockchains. **ASIACRYPT 2018** [Google Scholar](https://scholar.google.com/scholar?q=Compact+multi-signatures+for+smaller+blockchains)

[16] Boneh等. Short signatures from the Weil pairing. **ASIACRYPT 2001** [Google Scholar](https://scholar.google.com/scholar?q=Short+signatures+from+the+Weil+pairing)

[23] Damgård等. Towards practical public key systems secure against chosen ciphertext attacks. **CRYPTO 1991** [Google Scholar](https://scholar.google.com/scholar?q=Towards+practical+public+key+systems+secure+against+chosen+ciphertext+attacks)

[25] Desmedt等. Society and group oriented cryptography: A new concept. **CRYPTO 1987** [Google Scholar](https://scholar.google.com/scholar?q=Society+and+group+oriented+cryptography)

[26] Desmedt等. Threshold cryptosystems. **CRYPTO 1989** [Google Scholar](https://scholar.google.com/scholar?q=Threshold+cryptosystems)

[33] Gennaro等. Secure distributed key generation for discrete-log based cryptosystems. **Journal of Cryptology 2007** [Google Scholar](https://scholar.google.com/scholar?q=Secure+distributed+key+generation+for+discrete-log+based+cryptosystems)

[37] Micali等. Accountable-subgroup multisignatures: Extended abstract. **ACM CCS 2001** [Google Scholar](https://scholar.google.com/scholar?q=Accountable-subgroup+multisignatures)

[38] Micali等. Compact certificates of collective knowledge. **IEEE S&P 2021** [Google Scholar](https://scholar.google.com/scholar?q=Compact+certificates+of+collective+knowledge)

[11] Bitansky等. The hunting of the SNARK. **Journal of Cryptology 2017** [Google Scholar](https://scholar.google.com/scholar?q=The+hunting+of+the+SNARK)

[41] Pointcheval等. Security arguments for digital signatures and blind signatures. **Journal of Cryptology 2000** [Google Scholar](https://scholar.google.com/scholar?q=Security+arguments+for+digital+signatures+and+blind+signatures)


## 关键词

+ 多元阈值签名
+ BLS签名
+ 去中心化预言机网络
+ 聚合签名
+ 非交互式异步设置
+ 加权阈值