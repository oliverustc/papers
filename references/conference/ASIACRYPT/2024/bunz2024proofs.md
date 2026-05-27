---
title: "Proofs for deep thought: Accumulation for large memories and deterministic computations"
doi: 10.1007/978-981-96-0935-2_9
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

### 背景与动机

证明机器计算的正确性时，证明内存读写操作的正确性（即内存证明）是一个核心挑战。传统方法需要证明 Merkle 树打开或多集哈希，导致证明电路较大。具体而言，Spice [SAGL18] 采用离线内存检查，每个读写操作约需 1500 个约束，若用于增量可验证计算（IVC），每个步骤需提交上千个元素。ProtoStar [BC23] 针对静态只读内存提出了基于 LogUp 的查找协议，但无法支持动态内存写入。本文旨在构造一个支持动态内存读写的、证明者开销与内存大小无关的内存证明 IVC 方案，并进一步利用 GKR 协议优化，使得每个读写操作仅需提交 6 个小内存表元素（若为 32 位值，则少于一个域元素）。

### 相关工作

[BC23] Benedikt Bünz et al. ProtoStar: Generic Efficient Accumulation/Folding for Special Sound Protocols. **ePrint 2023** [Google Scholar](https://scholar.google.com/scholar?q=ProtoStar+Generic+Efficient+Accumulation%2FFolding+for+Special+Sound+Protocols)
> 核心思路：提出将任意特殊声音交互协议编译为累积方案和 IVC 的通用方法，利用 LogUp 实现静态表查找，每个读操作仅需两个群标量乘法。
> 局限与区别：不支持动态内存写操作，且表必须静态预处理。本文在其基础上扩展 LogUp 以支持动态读写和内存更新。

[SAGL18] Srinath Setty et al. Proving the correct execution of concurrent services in zero-knowledge. **ePrint 2018** [Google Scholar](https://scholar.google.com/scholar?q=Proving+the+correct+execution+of+concurrent+services+in+zero+knowledge)
> 核心思路：采用离线内存检查和多集哈希，约 1500 个约束每读写。
> 局限与区别：约束数量大，导致 IVC 证明者开销大。本文通过 LogUp 和 GKR 将约束降至 6 个小元素提交。

[BEGKN91] Manuel Blum et al. Checking the Correctness of Memories. **FOCS 1991** [Google Scholar](https://scholar.google.com/scholar?q=Checking+the+Correctness+of+Memories)
> 核心思路：经典离线内存检查，通过构建读写列表并证明它们构成置换。
> 局限与区别：原始方法需要线性扫描内存；本文采用 LogUp 风格的置换检查，证明者复杂度与内存大小 T 无关。

[Hab22] Ulrich Haböck. Multivariate lookups based on logarithmic derivatives. **ePrint 2022** [Google Scholar](https://scholar.google.com/scholar?q=Multivariate+lookups+based+on+logarithmic+derivatives)
> 核心思路：提出 LogUp 查找参数，利用对数导数等式证明元素属于表。
> 局限与区别：仅支持静态表；本文将其扩展到动态内存的索引查找和内存更新。

[PH23] Shahar Papini et al. Improving logarithmic derivative lookups using GKR. **ePrint 2023** [Google Scholar](https://scholar.google.com/scholar?q=Improving+logarithmic+derivative+lookups+using+GKR)
> 核心思路：使用 GKR 协议避免提交大逆元，降低证明者开销。
> 局限与区别：未与 IVC 累积方案结合。本文将其与 ProtoStar 兼容，构造累积友好的 GKR，并应用至内存证明。

[STW23] Srinath Setty et al. Unlocking the lookup singularity with Lasso. **ePrint 2023** [Google Scholar](https://scholar.google.com/scholar?q=Unlocking+the+lookup+singularity+with+Lasso)
> 核心思路：Lasso 查找，线性时间证明者，表结构化时独立于表大小。
> 局限与区别：仅支持静态表读操作。本文针对动态内存，且支持写操作。

[BCLMS21] Benedikt Bünz et al. Proof-Carrying Data Without Succinct Arguments. **CRYPTO 2021** [Google Scholar](https://scholar.google.com/scholar?q=Proof-Carrying+Data+Without+Succinct+Arguments)
> 核心思路：证明从累积方案到 IVC 的通用编译方法。
> 局限与区别：本文应用其编译器，但底层交互协议需满足特殊设计要求。

[KST22] Abhiram Kothapalli et al. Nova: Recursive Zero-Knowledge Arguments from Folding Schemes. **CRYPTO 2022** [Google Scholar](https://scholar.google.com/scholar?q=Nova+Recursive+Zero-Knowledge+Arguments+from+Folding+Schemes)
> 核心思路：Folding 方案构造 IVC，验证者仅需少量群操作。
> 局限与区别：主要面向算术电路，而非内存证明。本文使用 ProtoStar 编译器而非 Nova。

[Val08] Paul Valiant. Incrementally Verifiable Computation or Proofs of Knowledge Imply Time/Space Efficiency. **TCC 2008** [Google Scholar](https://scholar.google.com/scholar?q=Incrementally+Verifiable+Computation+or+Proofs+of+Knowledge+Imply+Time%2FSpace+Efficiency)
> 核心思路：IVC 概念引入，通过递归 SNARK 实现。
> 局限与区别：早期工作依赖 SNARK 进行递归，开销大。本文采用累积方案，效率更高。

### 核心技术与方案

本文的整体框架如下：首先构造三个 LogUp 风格的特殊声音子协议，分别对应内存正确的三个性质——读写列表置换、初始读值与旧内存一致、内存更新正确（称为 mem-update）。然后将这三个子协议并行组合成完整的证明协议 $\Pi_{\mathsf{MP}}$，该协议具有 2 轮通信、验证者度为 3，且证明者消息中非零元素个数为 $O(\ell)$（$\ell$ 是读写操作数），与内存大小 $T$ 无关。最后利用 ProtoStar 编译器 [BC23] 将其编译为累积方案，进而得到 IVC 方案。

**子协议 1：置换检查 $\Pi_{\mathsf{perm}}$**  
给定两个等长序列 $\mathbf{w}, \mathbf{t}$，证明它们是置换，即 $\sum_{i=1}^\ell \frac{1}{X + \mathbf{w}_i} = \sum_{i=1}^T \frac{1}{X + \mathbf{t}_i}$。证明者发送每个分式的值 $\mathbf{h}_j = 1/(x_1 + \mathbf{w}_j)$ 和 $\mathbf{g}_i = 1/(x_1 + \mathbf{t}_i)$，验证者检查求和相等以及每个分式分母与分子的乘积为 1。该协议是 $2(\ell + T)$-特殊声音。

**子协议 2：索引向量查找 $\Pi_{\mathsf{ivlk}}$**  
证明每个查询向量 $\mathbf{w}_j$ 等于表 $\mathbf{t}$ 中地址 $\mathbf{b}_j$ 处的值。使用等式：$\sum_{j=1}^\ell \frac{1}{X + Y \cdot \mathbf{b}_j + \mathbf{w}_j} = \sum_{i=1}^T \frac{\mathbf{m}_i}{X + Y \cdot i + \mathbf{t}_i}$，其中 $\mathbf{m}_i$ 是计数器。验证者检查两个求和相等以及每个分式与其分母的乘积关系。

**子协议 3：内存更新 $\Pi_{\mathsf{mu}}$**  
证明更新向量 $\mathbf{w}$（即 $W.v - R.v$）与稀疏的 $\Delta$（内存差值向量）一致。使用等式：$\sum_{j=1}^\ell \frac{\mathbf{w}_j}{X + Y \cdot \mathbf{b}_j + \mathbf{w}_j} = \sum_{i=1}^T \frac{\Delta_i}{X + Y \cdot i + \Delta_i}$。该协议验证者度为 3，证明者消息非零元素为 $4\ell$。

**完整内存证明协议 $\Pi_{\mathsf{MP}}$**  
证明者发送 $R, W, m, NM$（新内存），验证者检查 $R.a = W.a$。然后挑战 $x_1, x_2, x_3$ 用于三个子协议中的线性组合。证明者发送所有分式向量，验证者执行 8 个检查（包括三个求和等式和六个分式乘法等式）。该协议是 $((\ell+T), 2(\ell+T))$-特殊声音。所有计算可在 $O(\ell)$ 时间内完成，独立于 $T$。

**累积友好 GKR 协议**  
为了减少提交大逆元的开销，本文引入了修改后的 GKR 协议，使用双变量求和检查（bivariate sumcheck）代替多线性求和检查，将轮数从 $O(\log^2 n)$ 降至 $O(\log n)$。关键子协议是 $\Pi_{\mathsf{eval}}$，让验证者高效评估高次多项式：通过发送幂次矩阵 $A$ 和 Lagrange 多项式系数，将验证者度降至 $2k$。双变量求和检查仅需 3 轮，通信复杂度 $O(\sqrt{n})$。进一步可通过 $c$-变量求和检查将通信降至 $O(c \cdot n^{1/c})$，轮数 $(c+1)\log n$。将 GKR 集成到内存证明中后，证明者不再需要提交大逆元，每个读写仅需提交 6 个与表元素等大小的值（若为 32 位，则少于一个 256 位域元素）。累积方案中，$P_{\mathsf{acc}}$ 时间主要为 $(6\ell, \mathbb{T})$-MSM（表大小元素的多标量乘法），$V_{\mathsf{acc}}$ 时间为 $(c+1)\log T$ 个群标量乘法。

### 核心公式与流程

**置换检查等式**
$$
\sum_{j=1}^{\ell} \frac{1}{X + \mathbf{w}_j} = \sum_{i=1}^{T} \frac{1}{X + \mathbf{t}_i}
$$
> 作用：判断两序列是否为置换（当 $\ell = T$ 时）。

**索引向量查找等式**
$$
\sum_{j=1}^{\ell} \frac{1}{X + Y \cdot \mathbf{b}_j + \mathbf{w}_j} = \sum_{i=1}^{T} \frac{\mathbf{m}_i}{X + Y \cdot i + \mathbf{t}_i}
$$
> 作用：证明 $\mathbf{w}_j = \mathbf{t}_{\mathbf{b}_j}$，即按地址在表中查找值。

**内存更新等式**
$$
\sum_{j=1}^{\ell} \frac{\mathbf{w}_j}{X + Y \cdot \mathbf{b}_j + \mathbf{w}_j} = \sum_{i=1}^{T} \frac{\Delta_i}{X + Y \cdot i + \Delta_i}
$$
> 作用：证明 $\mathbf{w}_j = \Delta_{\mathbf{b}_j}$ 且 $\Delta_i$ 在未修改地址处为 0。

**双变量求和检查（简化版）**
验证者对挑战 $a, b$ 检查：
$$
\sum_{x \in \mathbb{G}_1} f_1(x) \stackrel{?}{=} T,\quad \sum_{y \in \mathbb{G}_2} f_2(y) \stackrel{?}{=} f_1(a),\quad T^* \stackrel{?}{=} f_2(b),\quad T^* \stackrel{?}{=} f(a,b)
$$
> 作用：3 轮协议证明 $\sum_{x \in \mathbb{G}_1, y \in \mathbb{G}_2} f(x,y) = T$，通信 $O(\sqrt{n})$。

**多项式评估子协议 $\Pi_{\mathsf{eval}}$**
验证者计算 $A(0) = a$，$A(i) = A(i-1)^2$，然后检查：
$$
\prod_{j=1}^k L_{\mathbf{x}_j}^{\mathbb{H}}(a_j) \stackrel{?}{=} \prod_{j=1}^k \frac{c_{\mathbf{x}_j} (A(\log m, j) - 1)}{a_j - \omega_{\mathbf{x}_j}}
$$
> 作用：验证者仅需低次运算即可确认多项式在 $a$ 处的值正确。

### 实验结果

本文为理论工作，未提供传统实验数据。但给出了详细的渐近效率表（表 4）。核心性能数值如下：在 plain 版本中，$P_{\mathsf{acc}}$ 时间包含 $(6\ell, \mathbb{T})$-MSM 和 $(9\ell, \mathbb{F})$-MSM，$V_{\mathsf{acc}}$ 时间为 4 个群操作。使用 GKR 优化后，$P_{\mathsf{acc}}$ 时间降为仅 $(6\ell, \mathbb{T})$-MSM（$\mathbb{T}$ 为表元素集，例如 32 位值），$V_{\mathsf{acc}}$ 时间约为 $(c+1)\log T$ 个群操作。与 Spice 相比，每个读写操作从 1500 个约束降至 6 个表大小元素，实现了超过 100 倍的改进。ProtoStar 实现仅需 2 个群操作每静态读，本文支持动态写且仅需 6 个小元素。实验规模参数：内存大小 $T$ 任意，$\ell$ 为每步读写数，域大小 256 位，表元素例如 32 位。

### 局限性与开放问题

本文主要局限在于 GKR 的 $V_{\mathsf{acc}}$ 时间含 $\log T$ 项，当内存极小时优势不明显。对于超大内存，$O(\log T)$ 群操作仍可能成为瓶颈，尽管本文通过 $c$-变量求和可调低。另一个开放问题是将方案扩展到支持并发读写或非确定性的存储模型，本文仅针对确定性机器计算。此外，完整协议中仍需提交少量 $O(T^{1/c})$ 大小的消息，在 $c$ 较小时可能较大，如何进一步压缩待探索。

### 强关联论文

[BC23] Benedikt Bünz et al. ProtoStar: Generic Efficient Accumulation/Folding for Special Sound Protocols. **ePrint 2023** [Google Scholar](https://scholar.google.com/scholar?q=ProtoStar+Generic+Efficient+Accumulation%2FFolding+for+Special+Sound+Protocols)

[SAGL18] Srinath Setty et al. Proving the correct execution of concurrent services in zero-knowledge. **ePrint 2018** [Google Scholar](https://scholar.google.com/scholar?q=Proving+the+correct+execution+of+concurrent+services+in+zero+knowledge)

[Hab22] Ulrich Haböck. Multivariate lookups based on logarithmic derivatives. **ePrint 2022** [Google Scholar](https://scholar.google.com/scholar?q=Multivariate+lookups+based+on+logarithmic+derivatives)

[PH23] Shahar Papini et al. Improving logarithmic derivative lookups using GKR. **ePrint 2023** [Google Scholar](https://scholar.google.com/scholar?q=Improving+logarithmic+derivative+lookups+using+GKR)

[BEGKN91] Manuel Blum et al. Checking the Correctness of Memories. **FOCS 1991** [Google Scholar](https://scholar.google.com/scholar?q=Checking+the+Correctness+of+Memories)

[BCLMS21] Benedikt Bünz et al. Proof-Carrying Data Without Succinct Arguments. **CRYPTO 2021** [Google Scholar](https://scholar.google.com/scholar?q=Proof-Carrying+Data+Without+Succinct+Arguments)

[KST22] Abhiram Kothapalli et al. Nova: Recursive Zero-Knowledge Arguments from Folding Schemes. **CRYPTO 2022** [Google Scholar](https://scholar.google.com/scholar?q=Nova+Recursive+Zero-Knowledge+Arguments+from+Folding+Schemes)

[STW23] Srinath Setty et al. Unlocking the lookup singularity with Lasso. **ePrint 2023** [Google Scholar](https://scholar.google.com/scholar?q=Unlocking+the+lookup+singularity+with+Lasso)

[Val08] Paul Valiant. Incrementally Verifiable Computation or Proofs of Knowledge Imply Time/Space Efficiency. **TCC 2008** [Google Scholar](https://scholar.google.com/scholar?q=Incrementally+Verifiable+Computation+or+Proofs+of+Knowledge+Imply+Time%2FSpace+Efficiency)


## 关键词

+ 增量可验证计算
+ 内存证明
+ GKR协议
+ 累积方案
+ 证明系统