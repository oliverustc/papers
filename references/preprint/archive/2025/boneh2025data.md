---
title: "Data availability sampling with repair"
标题简称:
论文类型: preprint
预印本简称: archive
发表年份: 2025
---

## Data availability sampling with repair

## 发表信息

+ [原文链接](https://eprint.iacr.org/2025/1414)

## 作者

+ [Dan Boneh](Dan%20Boneh.md) 
+ Joachim Neu 
+ Valeria Nikolaenko 
+ Aditi Partap 


## 笔记

### 背景与动机
区块链共识协议的水平可扩展性要求将交易载荷的传播与排序分离，从而让共识节点只对载荷的加密哈希引用达成一致，而载荷本身通过一种称为可验证分布式存储的系统来分发和验证。在这一范式中，数据可用性采样是关键原语，它允许验证者通过交互式采样来确认载荷是否可检索，即使网络中存在多数敌手。然而，现有DAS方案在理论上均未正式处理不完整分片的修复问题，而这正是以太坊“Danksharding”愿景的核心动机：当某些存储节点在分发过程中未能接收到其编码分片时，必须能够高效地修复这些缺失份额，否则系统性能会因单点故障而严重退化。尽管已有工作如Ethereum的PeerDAS依赖高性能的“超节点”进行全局解码和重新编码来完成修复，但这一过程带宽与计算开销极大。为此，本文旨在填补DAS缺乏本地修复形式化定义与高效构造的空白，提出一种能显著降低存储与修复开销的新方案。

### 相关工作

[33] Hall-Andersen, Simkin, Wagner. Foundations of Data Availability Sampling. **IACR Communications in Cryptology 2025** [Google Scholar](https://scholar.google.com/scholar?q=Foundations+of+Data+Availability+Sampling)
> 核心思路：首次给出了DAS的提取器式安全性定义，并提出了基于擦除码承诺的通用构造框架。
> 局限与区别：其定义的修复是全局性的（通过多次采样重建整个编码），本文则聚焦于本地修复，允许节点仅用少数份额就能修复单个缺失份额；此外，其模型未覆盖Retrieve协议。

[24] Ethereum Foundation. **Ethereum Fulu fork specifications** [Google Scholar](https://scholar.google.com/scholar?q=Ethereum+Fulu+fork+specifications)
> 核心思路：实现了二维Reed-Solomon码和KZG承诺的PeerDAS协议，于2025年12月部署。
> 局限与区别：PeerDAS的一维Reed-Solomon码不支持本地修复，修复时必须对整个载荷进行解码和重新编码，导致带宽和计算开销很大（需128 kB带宽）。本文方案通过多重码实现了约2.1倍的修复带宽降低。

[32] Hall-Andersen, Simkin, Wagner. FRIDA: Data Availability Sampling from FRI. **CRYPTO 2024** [Google Scholar](https://scholar.google.com/scholar?q=FRIDA+Data+Availability+Sampling+from+FRI)
> 核心思路：使用FRI协议作为承诺方案，支持透明设置。
> 局限与区别：其方案不支持本地修复；在修复子网数量上需要8192个（本文仅需32个），且在存储和带宽方面均不如本文方案。

[55] Ethereum Roadmap. **Danksharding** [Google Scholar](https://scholar.google.com/scholar?q=Danksharding)
> 核心思路：提出了基于2D Reed-Solomon码和KZG承诺的以太坊扩展蓝图，强调需要本地修复。
> 局限与区别：该路线图本身未给出具体的本地修复构造或形式化定义；本文提供了基于多重码的完整实现和安全性分析。

[10] Cachin, Tessaro. Asynchronous Verifiable Information Dispersal. **Distributed Computing 2005** [Google Scholar](https://scholar.google.com/scholar?q=Asynchronous+Verifiable+Information+Dispersal)
> 核心思路：提出了第一个异步可验证信息分发协议（AVID），通过门限签名保证可检索性。
> 局限与区别：AVID属于VDA流派，其安全依赖于诚实多数假设，且不支持交互式采样；本文的DAS方案则能容忍敌手多数，并引入了本地修复。

[12] Cohen, Goren, Kokoris-Kogias, Sonnino, Spiegelman. Proof of Availability and Retrieval in a Modular Blockchain Architecture. **FC 2023** [Google Scholar](https://scholar.google.com/scholar?q=Proof+of+Availability+and+Retrieval+in+a+Modular+Blockchain+Architecture)
> 核心思路：提出了模块化区块链中可验证分发的完整系统模型，包括了可用性证明和检索证明。
> 局限与区别：该工作属于VDA，未涵盖交互式采样或本地修复。本文从该工作中借用了乐观情形下的检索安全定义，并将其移植到DAS语境。

[53] Papamanthou, Shi, Tamassia. Signatures of Correct Computation. **TCC 2013** [Google Scholar](https://scholar.google.com/scholar?q=Signatures+of+Correct+Computation)
> 核心思路：提出了PST多项式承诺方案，支持对多项式及其导数的求值证明。
> 局限与区别：原方案不支持批量打开和证明的本地修复。本文在其基础上进行了推广，实现了对多重码的承诺、批量打开和本地修复。

[20] Feist, Khovratovich. Fast Amortized KZG Proofs. **ePrint Archive 2023** [Google Scholar](https://scholar.google.com/scholar?q=Fast+Amortized+KZG+Proofs)
> 核心思路：提出了KZG承诺的批量打开算法，通过FFT将计算复杂度从O(N²)降到O(N log N)。
> 局限与区别：该算法仅适用于单变量多项式。本文将其技术推广到多元多项式，用于多重码承诺的批量打开和本地修复。

### 核心技术与方案

本文的框架始于两类底层原语：(i) 一个 $(k,M,\Delta,r)$-局部可纠错码，其编码 $C:\Sigma^k\to\Gamma^M$ 支持本地纠错算法LocalCorrect，只需访问 $r$ 个符号即可修复任一符号，r远小于解码所需的最少符号数； (ii) 一个对应的局部可纠错擦除码承诺方案，在承诺“代码绑定”性质的基础上，额外提供CLocalCorrect算法，允许利用仅 $r$ 个已知位置的开销来修复任一位置的开销证明。

在此基础上，一个通用的编译器将代码和承诺组合成完整的DAS方案。设 $n$ 为存储节点数量，编码长度 $M$ 整除 $n$。分撒者运行编码和批次打开，为每个节点分配一个编码符号及其证明。在验证中，每个验证者采样 $Q$ 个随机位置，每个查询返回编码符号和证明，验证通过则计为一次成功。若超过 $\delta \ell$ 个验证者成功，则称数据可用。**提取**算法Ext收集所有成功查询的符号，若满足无冲突则运行 $C$ 的解码算法。**检索**协议Retrieve分两步：若代码是系统性的，优先尝试直接获取数据符号；否则逐位置扫描直到收集到超过 $(1-\Delta)M$ 个符号。**本地修复**协议LocalRepair则调用编码的LocalCorrect从 $r$ 个其他位置恢复缺失符号，再调用承诺的CLocalCorrect恢复对应的开销证明。

安全性证明在两个方面进行。**乐观情形可靠性**假定敌手最多控制 $f$ 比例的存储节点。若超过 $\delta\ell$ 个验证者成功，那么成功查询至少覆盖了 $(1-\Delta+f)M$ 个不同位置。即使敌手随后背叛所有 $fM$ 个位置，剩余 $(1-\Delta)M$ 个被诚实节点维护的位置足以支持解码。理论上界从而为 $\binom{\ell}{\delta\ell} \cdot \binom{M}{(1-\Delta+f)M} \cdot (1-\Delta+f)^{\delta\ell Q}$。**最坏情形可靠性**中验证者查询可能全部落入一个 $(1-\Delta)M$ 大小的子集，因此是通过 $\binom{\ell}{\delta\ell} \cdot \binom{M}{(1-\Delta)M} \cdot (1-\Delta)^{\delta\ell Q}$ 来界定。

为了实现高效的本地修复，本文的基础编码选用多重码：将数据解释为一个二元多项式 $h(X_1,X_2)$，编码不仅包括其在所有 $\{( \omega^{i},\omega^{j})\}_{i,j\in[q]}$ 上的求值，还包含这两个一阶偏导数 $h_1' = \frac{\partial}{\partial X_1}h$ 和 $h_2' = \frac{\partial}{\partial X_2}h$ 的求值。记总次数为 $d$，参数取 $d=90, q=128$，数据长度为4096个域元素。这一编码极小距离达到0.53（高于Reed-Solomon码的0.5），且任一符号可以通过任意 $d+1=91$ 个其他符号得到修复。代码的**系统性**通过一个新颖的快速算法实现：首先从系统性数据（满足 $i+j\le d$ 的求值点）反推出多项式的系数，然后利用一系列FFT计算所有 $q^2$ 个位置的完整求值。

承诺方案PSTMult基于PST的多元承诺，关键洞察是：在点 $(\omega^{i_1},\omega^{i_2})$ 处，式
$$h(X_1,X_2) = (X_1-\omega^{i_1})q_1(X_1,X_2)+(X_2-\omega^{i_2})q_2(X_2)+h(\omega^{i_1},\omega^{i_2})$$
中的商多项式满足 $q_1(\omega^{i_1},\omega^{i_2}) = h_1'(\omega^{i_1},\omega^{i_2})$ 和 $q_2(\omega^{i_2}) = h_2'(\omega^{i_1},\omega^{i_2})$。通过进一步展开 $q_1,q_2$，可得
$$h = (X_1-\omega^{i_1})^2q_{11}+(X_1-\omega^{i_1})(X_2-\omega^{i_2})q_{12}+(X_2-\omega^{i_2})^2q_{22}+(X_1-\omega^{i_1})h_1'+(X_2-\omega^{i_2})h_2'+h$$
证明大小因此压缩为三个群元素 $([q_{11}(\boldsymbol\tau)]_1,[q_{12}(\boldsymbol\tau)]_1,[q_{22}(\boldsymbol\tau)]_1)$，验证仅需四对配对操作。

批处理打开算法将计算复杂度从 $O(q^2d^2)$ 降低到 $O(q^2\log q)$。仍以二元多项式为例：记 $h(X_1,X_2)=\sum_{u=0}^d h_u(X_2)X_1^u$，要计算所有 $\pi_{11}^{(i)}$ 即 $[q_{11}^{(i)}(\boldsymbol\tau)]_1$。观察发现 $q_{11}^{(i)}$ 可表达为
$$q_{11}^{(i)} = \sum_{u\in[d-1]} u\cdot G_u(\boldsymbol X)\cdot(\omega^{i})^{u-1},$$
其中 $G_u = \sum_{v>u} h_v(X_2)X_1^{v-u-1}$。于是先通过Toeplitz矩阵-向量积（可用FFT在 $O(d\log d)$ 内完成）计算出所有 $[G_u(\boldsymbol\tau)]_1$，再经过一次群上的离散傅里叶变换即得全部 $\pi_{11}^{(i)}$。$\pi_{12}$ 和 $\pi_{22}$ 的批量计算同理，均复用类似结构。

证明的本地修复同样得益于上述结构：$\pi_{11}^{(i)}$ 视作一元多项式在 $\omega^i$ 处的求值，故任意 $d-1$ 个不同 $\pi_{11}^{(j)}$ 可通过拉格朗日插值修复第 $i$ 个。对于二元证明 $\pi_{12}^{(i,j)},\pi_{22}^{(i,j)}$，文中证明它们可以整体拟合成总次数 $\le d-2$ 的二元多项式，从而只需 $d-1$ 个位于一条直线上的点即可用拉格朗日插值恢复。安全性（位置绑定）归约到非对称 $d$-SBDH假设，使用到代数群模型下的可提取性。

实际部署时，为了降低子网数量，可将数据划分成 $Y$ 行，每行独立编码后逐行拼接形成每个节点储存的块。取 $Y=8$，子网数从9216降至1225，本地修复子网数降至32。

### 核心公式与流程

**[编码算法系统性]**
$$
\begin{aligned}
&h(X_1,X_2)=\sum_{i+j\le d}h_{i,j}X_1^iX_2^j\\
&\Pi_x = (h(\omega^{i},\omega^{j}),\; h_1'(\omega^{i},\omega^{j}),\; h_2'(\omega^{i},\omega^{j}))\quad \text{for } x=i\cdot q+j,\; i,j\in[q].
\end{aligned}
$$
> 作用：将数据恢复为二元多项式系数，然后计算所有求值点和偏导数，构成编码符号。

**[承诺验证方程（以点 $(\omega^{i_1},\omega^{i_2})$ 为例，$[y]_1=h(\boldsymbol\tau),[\pi_{11}]_1=q_{11}(\boldsymbol\tau)$ 等）]**
$$
\begin{aligned}
e\big(\text{com}-[z]_1-[z_1(\tau_1-\omega^{i_1})]_1-[z_2(\tau_2-\omega^{i_2})]_1,\;[1]_2\big)=\\
e(\pi_{11},[(\tau_1-\omega^{i_1})^2]_2)+
e(\pi_{12},[(\tau_1-\omega^{i_1})(\tau_2-\omega^{i_2})]_2)+
e(\pi_{22},[(\tau_2-\omega^{i_2})^2]_2).
\end{aligned}
$$
> 作用：验证节点提供的求值 $z=h(\cdot)$ 及其偏导数 $z_1,z_2$ 是否正确。

**[本地修复概率上界（最坏情形可靠性）]**
$$
\binom{\ell}{\delta\ell}\cdot\binom{M}{(1-\Delta)M}\cdot(1-\Delta)^{\delta\ell Q}\le 2^{-\kappa}.
$$
> 作用：给定安全参数 $\kappa$ 和验证者数 $\ell$，据此选择采样次数 $Q$ 以保证提取成功。

### 实验结果

实验在 Apple M1 Pro 单核上执行，使用 C 语言实现，底层依赖 BLS12-381 曲线（blst库）。编码128 kB数据（4096个域元素）用时46.1 ms，约为Ethereum的PeerDAS（2.6 ms）的18倍。承诺计算（MSM大小4186）用时44 ms，与PeerDAS（41 ms）接近。单次验证用时2.9 ms，PeerDAS为1.15 ms，开销增加主要源于四对配对。批处理打开算法（串行）用时20.3 s，但该算法高度可并行：91次Toeplitz矩阵-向量积以及后续的2次DFT均可独立执行。基于任务数和单核最慢任务（约5.1 ms）估计，在96核机器上并行可将耗时压缩至约0.38 s。节点存储方面，基线版本每个节点仅需0.23 kB（3个群元素），而PeerDAS需8.18 kB（256个域元素+4个群元素），提升约35倍。加入批处理（Y=8）后存储变为1.88 kB（24+24个元素），仍为4.3倍改进。本地修复总带宽基线为21.3 kB（PeerDAS为128 kB），批处理后为60 kB（2.1倍改进）。修复所需子网数基线为91（比PeerDAS多42%），批处理后降至32（PeerDAS为64）。采样带宽基线为9.14 kB（PeerDAS为16.37 kB），批处理后为24.4 kB（升高约1.5倍），但本文方案（不包含批处理）可同时提供40比特的乐观情形可靠性，而PeerDAS目前提供0比特。

### 局限性与开放问题

本文的批处理方案虽然大幅降低了子网数，但仍需1225个子网用于分撒，在极端网络条件下可能仍是负担。能否通过随机线性组合各行承诺来进一步压缩子网数和证明大小，是一个开放方向。此外，将支持“两条直线交叉修复”的更高效本地纠错算法（至少两条直线上各取 $\lceil d/2\rceil$ 点即可修复）集成到承诺方案中，可以进一步降低修复带宽。对于高维（多于2元）多项式，将本承诺方案自然推广并保持效率也是后续可以关注的问题。

### 强关联论文

[24] Ethereum Foundation. **Ethereum Fulu fork specifications** [Google Scholar](https://scholar.google.com/scholar?q=Ethereum+Fulu+fork+specifications)
[33] Hall-Andersen, Simkin, Wagner. Foundations of Data Availability Sampling. **IACR Communications in Cryptology 2025** [Google Scholar](https://scholar.google.com/scholar?q=Foundations+of+Data+Availability+Sampling)
[32] Hall-Andersen, Simkin, Wagner. FRIDA: Data Availability Sampling from FRI. **CRYPTO 2024** [Google Scholar](https://scholar.google.com/scholar?q=FRIDA+Data+Availability+Sampling+from+FRI)
[55] Ethereum Roadmap. **Danksharding** [Google Scholar](https://scholar.google.com/scholar?q=Danksharding)
[10] Cachin, Tessaro. Asynchronous Verifiable Information Dispersal. **Distributed Computing 2005** [Google Scholar](https://scholar.google.com/scholar?q=Asynchronous+Verifiable+Information+Dispersal)
[53] Papamanthou, Shi, Tamassia. Signatures of Correct Computation. **TCC 2013** [Google Scholar](https://scholar.google.com/scholar?q=Signatures+of+Correct+Computation)
[20] Feist, Khovratovich. Fast Amortized KZG Proofs. **ePrint Archive 2023** [Google Scholar](https://scholar.google.com/scholar?q=Fast+Amortized+KZG+Proofs)
[40] Kopparty, Saraf, Yekhanin. High-rate codes with sublinear-time decoding. **J. ACM 2014** [Google Scholar](https://scholar.google.com/scholar?q=High-rate+codes+with+sublinear-time+decoding)
[51] Nazirkhanova, Neu, Tse. Information Dispersal with Provable Retrievability for Rollups. **AFT 2022** [Google Scholar](https://scholar.google.com/scholar?q=Information+Dispersal+with+Provable+Retrievability+for+Rollups)


## 关键词

+ DAS数据可用性采样局部修复
+ 局部可纠错重数码高效修复
+ 多元多项式承诺偏导数开放
+ 以太坊Danksharding PeerDAS扩展
+ 可验证信息分散部分重构