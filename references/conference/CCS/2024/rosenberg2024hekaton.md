---
title: "Hekaton: Horizontally-Scalable zkSNARKs Via Proof Aggregation"
标题简称: Hekaton
论文类型: conference
会议简称: CCS
发表年份: 2024
modified: 2025-04-23 15:20:35
created: 2025-04-09 14:04:08
---

## Hekaton: Horizontally-Scalable zkSNARKs Via Proof Aggregation

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3658644.3690282)
+ [code](https://github.com/Pratyush/hekaton-system)

## 作者

+ Michael Rosenberg
+ Tushar Mopuri
+ Hossein Hafezi
+ [Ian Miers](Ian%20Miers.md)
+ [Pratyush Mishra](Pratyush%20Mishra.md)
## 笔记

### 背景与动机

零知识简洁非交互式知识论证（zkSNARK）允许证明者向验证者秘密且可验证地证明大型计算的正确执行，这一特性使其成为区块链、可验证密钥目录等诸多系统增强问责性、可扩展性和隐私性的有力工具。然而现有 zkSNARK 方案在证明大型计算时面临严重的可扩展性瓶颈：证明算法的运行时间和空间复杂度均随电路规模线性增长，且并行化效果不佳，导致即使相对简单的计算（如 700×700 矩阵乘法需 6.85 亿门）也需要数十分钟和 1.7TB 内存 [46]。此外，许多实际应用（如 RAM 程序证明）天然要求将循环展开、分支全走，进一步加剧了电路膨胀，而电路本机缺乏内存访问能力，现有内存检查方法要么开销过大，要么对分布式场景施加额外限制。因此，迫切需要一种能水平扩展、支持任意计算结构且内存友好的 zkSNARK 方案，使分布式证明器能够高效处理现实规模的计算任务。

### 相关工作

[46] Wu 等. DIZK: A distributed zero knowledge proof system. **USENIX Security 2018** [Google Scholar](https://scholar.google.com/scholar?q=DIZK+A+Distributed+Zero+Knowledge+Proof+System)
> 核心思路：将 zkSNARK 证明算法中的 FFT 和多标量乘法等核心操作设计为分布式算法，在多节点上并行执行。
> 局限与区别：需要线性量的节点间通信，导致每门延迟比本地证明高 10 倍以上；而 Hekaton 仅需常数级通信。

[47] Xie 等. zkBridge: Trustless Cross-chain Bridges Made Practical. **CCS 2022** [Google Scholar](https://scholar.google.com/scholar?q=zkBridge+Trustless+Cross%E2%80%90chain+Bridges+Made+Practical)
> 核心思路：仅支持数据并行计算（重复相同子电路），主节点仍需执行与子电路大小成正比的密码学工作。
> 局限与区别：仅支持数据并行，且通信量仍为线性；Hekaton 支持任意电路结构，并保证主节点工作量仅随子电路数量增长。

[37] Liu 等. Pianist: scalable zkrollups via fully distributed zero-knowledge proofs. **S&P 2024** [Google Scholar](https://scholar.google.com/scholar?q=Pianist+Scalable+zkRollups+via+Fully+Distributed+Zero%E2%80%90Knowledge+Proofs)
> 核心思路：利用双变量多项式承诺将 Plonk 的全局置换检查分解为每个工作节点的局部置换检查，实现常数大小证明和验证时间。
> 局限与区别：其 SRS 大小随电路总规模线性增长，而 Hekaton 的 SRS 仅随独特的子电路数量增长；Hekaton 在实验中表现出更优的延迟和吞吐量。

[40] Nguyen 等. Mangrove: a scalable framework for folding-based snarks. **CRYPTO 2024** [Google Scholar](https://scholar.google.com/scholar?q=Mangrove+A+Scalable+Framework+for+Folding%E2%80%90Based+SNARKs)
> 核心思路：同样使用基于承诺和证明的置换检查技术，但仅报告估算性能，未提供完整实现。
> 局限与区别：若应用于分布式环境，会产生线性节点间通信；Hekaton 则保持常数通信。

[18] Bünz 等. Proofs for inner pairing products and applications. **ASIACRYPT 2021** [Google Scholar](https://scholar.google.com/scholar?q=Proofs+for+Inner+Pairing+Products+and+Applications)
> 核心思路：提出内配对积论证系统（MIPP/TIPP），用于构造 Groth16 等方案的聚合方案。
> 局限与区别：原有方案仅能聚合相同电路的证明；Hekaton 将其推广为支持多电路（非同质）聚合。

[32] Kosba 等. MIRAGE: succinct arguments for randomized algorithms with applications to universal zk-snarks. **USENIX Security 2020** [Google Scholar](https://scholar.google.com/scholar?q=MIRAGE+Succinct+Arguments+for+Randomized+Algorithms+with+Applications+to+Universal+zkSNARKs)
> 核心思路：构造了 Groth16 的 commit-carrying 变体，证明由三个群元素组成，验证方程包含承诺项。
> 局限与区别：Hekaton 在其基础上设计了新的 commit-carrying 聚合方案，支持多电路聚合。

[19] Campanelli 等. Legosnark: modular design and composition of succinct zero-knowledge proofs. **CCS 2019** [Google Scholar](https://scholar.google.com/scholar?q=Legosnark+Modular+Design+and+Composition+of+Succinct+Zero%E2%80%90Knowledge+Proofs)
> 核心思路：提出 commit-carrying zkSNARK 概念，承诺与 SNARK 协同设计，使承诺内容可直接在电路中作为证据使用。
> 局限与区别：原概念未涉及聚合；Hekaton 将其扩展为 commit-carrying 聚合方案。

[45] Tyagi 等. Versa: verifiable registries with efficient client audits from RSA authenticated dictionaries. **CCS 2022** [Google Scholar](https://scholar.google.com/scholar?q=Versa+Verifiable+Registries+with+Efficient+Client+Audits+from+RSA+Authenticated+Dictionaries)
> 核心思路：使用 RSA 累加器替代 Merkle 树，结合 SNARK 构造不变性证明，实现常数大小证明。
> 局限与区别：不兼容已有基于 Merkle 树的注册表；Hekaton 直接证明 SHA-256 Merkle 树的批处理更新，兼容现有系统。

[49] Zhang 等. vRAM: faster verifiable RAM with program-independent preprocessing. **S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=vRAM+Faster+Verifiable+RAM+with+Program%E2%80%90Independent+Preprocessing)
> 核心思路：利用置换检查技术实现内存的读/写一致性证明。
> 局限与区别：依赖挑战来自哈希承诺，需 commit-carrying SNARK；Hekaton 将其扩展到分布式分区场景，并设计分区友好的内存检查器。

### 核心技术与方案

Hekaton 的整体框架称为“分治聚合”（Divide-and-Aggregate, DNA）。其核心思路是将大型电路 $C$ 划分为 $n$ 个较小的子电路 $C_1,\ldots,C_n$，将子电路之间的共享线替换为对全局内存的访问，构造增广子电路 $C_1',\ldots,C_n'$，每个增广子电路由各工作节点使用一个“内部” zkSNARK（称为 ARG）独立证明，最后使用证明聚合方案 Agg 将这些子证明聚合成一个简洁的可验证证明。

该框架面临两个核心挑战：如何支持不同子电路的证明聚合（多电路聚合），以及如何高效处理子电路间共享的线。Hekaton 通过以下技术加以解决。

**分区友好的内存检查器。** 为检查共享线的一致性，Hekaton 设计了一种基于置换检查的新型内存检查器，而非传统的在线检查（Merkle 树）或完整内存迹检查。该检查器利用多项式求值的递增性质：给定挑战 $r$，内存迹 $T$ 和地址排序迹 $A$ 的多项式求值可通过累乘方式逐步计算。具体地，将迹按子电路划分为子迹 $T_i$ 和 $A_i$（对应子电路 $C_i$ 中的内存访问），每个内存检查子电路 $M_i$ 接收上一子电路传来的部分累积乘积 $\tau_i$ 和 $\alpha_i$，处理本子迹后输出新的累积乘积 $\tau_{i+1}$ 和 $\alpha_{i+1}$。$M_i$ 仅需 $O(s_i)$ 个门（$s_i$ 为 $C_i$ 中的共享线数），且与相邻子电路仅共享常数个线。构造细节：$M_i$ 验证本子迹中所有入口的子电路号均为 $i$，验证地址排序迹中相邻相同地址的值一致性，并计算更新后的累积乘积。该方法的每条共享线仅消耗 13 个约束，远低于 Merkle 树方案的 $300\log s$ 约束。

**承诺携带型聚合方案（commit-carrying aggregation）。** 为在分布式场景中安全地生成挑战 $r$，需要将各子电路的迹承诺聚合成一个简洁承诺，然后通过随机预言机导出 $r$。Hekaton 定义了新的承诺携带型聚合方案，使之不仅能聚合证明，还能聚合子电路的承诺。该方案以 Mirage（一种 Groth16 的承诺携带变体）为内部 SNARK，并基于内配对积论证系统（MIPP/TIPP）[18] 构造聚合。具体地，聚合证明需验证以下随机化配对等式对随机挑战 $t$ 成立：
$$
\prod_i e(t^i\cdot A_i, B_i) = e(\alpha,\beta)^{\sum t^i} \prod_i e(t^i\cdot C_i, \delta_i) \prod_i e(t^i\cdot D_i, \eta_i)
$$
其中 $(A_i, B_i, C_i)$ 是子证明，$D_i$ 是子承诺，$(\alpha,\beta,\delta_i,\eta_i)$ 来自各子电路的验证密钥。由于子电路不同，$\delta_i$ 和 $\eta_i$ 各异，为保持简洁性，Hekaton 利用子电路结构在设置阶段已知这一事实，将 $\delta_i$ 和 $\eta_i$ 的承诺预先计算并包含在聚合验证密钥中。此外，通过将多个 TIPP 实例合并为一个，降低了聚合证明者的计算开销。

**优化。** Hekaton 包含若干实际优化：将内存设为只读（证明者初始化内存为所有共享线的值），避免复杂的读写检查；通过将子电路编号和访问地址作为公共输入并在设置阶段预处理，避免为每个子电路生成唯一的 SRS，使得 SRS 大小仅随独特子电路类型数增长；使用 Merkle 树将各子电路的不同公共输入同质化，简化聚合方案对异构公共输入的处理；进行批设置优化，进一步减少 TIPP 数量。

在安全性方面，Hekaton 依赖于随机预言机模型和内部 SNARK 的知识合理性，聚合方案本身作为承诺携带型 SNARK 保证了完整性和知识可靠性。系统的证明由最终聚合证明、聚合承诺、Merkle 路径证明和少量域元素组成，大小随子电路数量呈对数增长。分布式证明中，每个工作节点仅需执行单个子电路的承诺和证明运算（与子电路大小成正比），通信量为常数（一个证明加一个承诺的大小），聚合节点的工作量随子电路数线性增长（但聚合本身也可分布式化，文中未实现但指出为未来工作）。验证者只需验证一个聚合证明和一条 Merkle 路径，验证时间与子电路数对数相关。

### 核心公式与流程

**[Mirage 验证方程]**
$$e(A, B) = e(\alpha, \beta) e(C, \delta) e(D, \eta)$$
> 作用：Mirage 作为内部 SNARK，检查证明 $(A,B,C)$ 相对于承诺 $D$ 的有效性。该方程是聚合方案的基础。

**[聚合随机化检查]**
$$\prod_i e(t^i\cdot A_i, B_i) = e(\alpha,\beta)^{\sum t^i} \prod_i e(t^i\cdot C_i, \delta_i) \prod_i e(t^i\cdot D_i, \eta_i)$$
> 作用：聚合证明者需对该等式在随机挑战 $t$ 下成立给出证明。左侧使用 TIPP，右侧使用 MIPP，Hekaton 通过批处理进一步减少 TIPP 实例。

**[内存检查子电路 $M_i$ 的公共接口]**
- 公共输入：挑战 $r$，上一子电路的最后迹入口 $(t, a)$，累积乘积 $(\tau_i, \alpha_i)$
- 公共输出：本子电路的最后迹入口 $(t', a')$，更新后乘积 $(\tau_{i+1}, \alpha_{i+1})$
- 见证：本子迹 $T_i$ 和 $A_i$
> 作用：$M_i$ 验证本子迹的合法性并更新累积乘积，相邻子电路仅共享常数个线（上述公共输入/输出），使分区证明成为可能。

**[分布式工作流程]**
1. 设置：协调者生成并划分内存迹，分发给各工作节点。
2. 承诺：各工作节点并行调用 ARG.C 提交子迹，将承诺发回协调者。
3. 挑战：协调者通过 Agg.C 聚合承诺，使用随机预言机导出挑战 $r$，分发给各工作节点。
4. 证明：各工作节点并行调用 ARG.P 生成子证明，发回协调者。
5. 聚合：协调者调用 Agg.P 聚合所有子证明，输出最终证明。
> 作用：实现水平可扩展性，每个子电路独立证明，仅需两轮通信（承诺+证明）。

### 实验结果

实验在大型多租户 HPC 集群上进行，节点配备 AMD EPYC 7763（128 核，512GB 内存）。每个子电路分配一个核心，限制 3.5GB 内存，对应约 130 万约束的子电路。Hekaton 展示了强水平可扩展性：在 4096 核配置下，证明 $2^{35}$ 门的电路可在 1 小时内完成。通信开销每子电路不到 1MB。证明大小随子电路数对数增长，在 $2^{18}$ 子电路时约 32kB，验证时间 83ms。与基线单线程 Mirage 相比，Hekaton 的归一化吞吐量（约束/核心-秒）达到单线程的 90%（4 核），当扩展到 32 倍时仍有 87% 的基线吞吐量，而 Groth16 单机 32 线程降至 5%。与 Pianist 对比（在相同硬件上验证），Hekaton 在 $2^{27}$ 约束时延迟为 11.6 秒（2048 核），而 Pianist 在 $2^{25}$ 约束时需要 <10 秒（2048 核），考虑到电路表示差异（Plonk 约束 ≈ 7 倍 R1CS 约束）和曲线效率（Pianist 用 BN254，Hekaton 用 BLS12-381），Hekaton 大约有 3× 低延迟优势。在可验证密钥目录（VKD）应用中，使用 SHA-256 Merkle 树（深度 128），Hekaton 可高效证明批处理更新，吞吐量随批大小增加。在 RAM 计算应用中，基于置换的内存检查器达到约 50kHz 吞吐量，远优于 Merkle 树基的 0.2kHz，并能证明约 3300 万周期的计算。聚合时间线性增长，在 $2^{16}$ 子电路时约 100 秒，但文中指出聚合本身可分布式化。

### 局限性与开放问题

Hekaton 的聚合步骤目前仍由单个节点执行，成为扩展至极大子电路数时的瓶颈，未来工作可设计分布式聚合方案。文中指出其“分治聚合”框架不包含那些在内部 SNARK 证明过程中进行细粒度聚合的方案（如 aPlonk），如何统一这些方案留待后续研究。虽然共享线成本低（13 约束/线），但最优的电路分区问题仍是开放挑战，尽管 Hekaton 兼容已有的自动分区方案[24,42]。最后，Hekaton 使用 BLS12-381 曲线，若迁移至更快的曲线（如 BN254）可能进一步提升性能，但需全面评估安全性和兼容性。

### 强关联论文

[46] Howard Wu, Wenting Zheng, Alessandro Chiesa, Raluca Ada Popa, and Ion Stoica. DIZK: A distributed zero knowledge proof system. **USENIX Security 2018** [Google Scholar](https://scholar.google.com/scholar?q=DIZK+A+Distributed+Zero+Knowledge+Proof+System)

[47] Tiancheng Xie, Jiaheng Zhang, Zerui Cheng, Fan Zhang, Yupeng Zhang, Yongzheng Jia, Dan Boneh, and Dawn Song. zkBridge: Trustless Cross-chain Bridges Made Practical. **CCS 2022** [Google Scholar](https://scholar.google.com/scholar?q=zkBridge+Trustless+Cross%E2%80%90chain+Bridges+Made+Practical)

[37] Tianyi Liu, Tiancheng Xie, Jiaheng Zhang, Dawn Song, and Yupeng Zhang. Pianist: scalable zkrollups via fully distributed zero-knowledge proofs. **S&P 2024** [Google Scholar](https://scholar.google.com/scholar?q=Pianist+Scalable+zkRollups+via+Fully+Distributed+Zero%E2%80%90Knowledge+Proofs)

[40] Wilson Nguyen, Trisha Datta, Binyi Chen, Nirvan Tyagi, and Dan Boneh. Mangrove: a scalable framework for folding-based snarks. **CRYPTO 2024** [Google Scholar](https://scholar.google.com/scholar?q=Mangrove+A+Scalable+Framework+for+Folding%E2%80%90Based+SNARKs)

[18] Benedikt Bünz, Mary Maller, Pratyush Mishra, Nirvan Tyagi, and Psi Vesely. Proofs for inner pairing products and applications. **ASIACRYPT 2021** [Google Scholar](https://scholar.google.com/scholar?q=Proofs+for+Inner+Pairing+Products+and+Applications)

[32] Ahmed E. Kosba, Dimitrios Papadopoulos, Charalampos Papamanthou, and Dawn Song. MIRAGE: succinct arguments for randomized algorithms with applications to universal zk-snarks. **USENIX Security 2020** [Google Scholar](https://scholar.google.com/scholar?q=MIRAGE+Succinct+Arguments+for+Randomized+Algorithms+with+Applications+to+Universal+zkSNARKs)

[19] Matteo Campanelli, Dario Fiore, and Anaïs Querol. Legosnark: modular design and composition of succinct zero-knowledge proofs. **CCS 2019** [Google Scholar](https://scholar.google.com/scholar?q=Legosnark+Modular+Design+and+Composition+of+Succinct+Zero%E2%80%90Knowledge+Proofs)

[45] Nirvan Tyagi, Ben Fisch, Andrew Zitek, Joseph Bonneau, and Stefano Tessaro. Versa: verifiable registries with efficient client audits from RSA authenticated dictionaries. **CCS 2022** [Google Scholar](https://scholar.google.com/scholar?q=Versa+Verifiable+Registries+with+Efficient+Client+Audits+from+RSA+Authenticated+Dictionaries)

[49] Yupeng Zhang, Daniel Genkin, Jonathan Katz, Dimitrios Papadopoulos, and Charalampos Papamanthou. vRAM: faster verifiable RAM with program-independent preprocessing. **S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=vRAM+Faster+Verifiable+RAM+with+Program%E2%80%90Independent+Preprocessing)


## 关键词

+ 零知识SNARK
+ 水平可扩展性
+ 证明聚合
+ 分布式系统
+ 并行证明
+ 可验证性