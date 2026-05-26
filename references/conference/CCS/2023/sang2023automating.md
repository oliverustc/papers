---
title: "Ou: Automating the Parallelization of Zero-Knowledge Protocols"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2023
modified: 2025-04-11 10:23:07
---

## Ou: Automating the Parallelization of Zero-Knowledge Protocols

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3576915.3616621)

## 作者

+ Yuyang Sang
+ [Ning Luo](Ning%20Luo.md)
+ Samuel Judson
+ Ben Chaimberg
+ [Timos Antonopoulos](Timos%20Antonopoulos.md)
+ [Xiao Wang](Xiao%20Wang.md)
+ [Ruzica Piskac](Ruzica%20Piskac.md)
+ Zhong Shao

## 笔记

### 背景与动机

零知识证明（ZKP）是现代隐私保护与去中心化应用的核心密码学原语，其通用构造近年在效率上取得了巨大进步 [1]。然而，将 ZK 部署到现实规模的计算任务仍面临两个结构性瓶颈：一是编程抽象落后，主流语言（如 Snarky、Cairo）仅支持基于电路模型的数据无关计算，无法利用非确定性提示（nondeterminism）或随机验证（如 Freivalds 算法）等高效构造；二是硬件资源瓶颈，大多数 zkSNARK 协议 [11, 14, 26, 35, 38] 需要与证明时间线性相关的临时存储，而 VOLE 类协议 [4, 20, 40] 虽降低内存开销却大幅增加带宽需求。虽然前期工作（如 DIZK [41]、zkBridge [42]、EZEE [43]、Giraffe [37] ）已开始将 ZKP 任务“横向扩展”到机器集群，但它们都要求开发者手动修改协议并手工划分计算块，这一过程容易出错且对复杂语句常导致次优解。本文旨在填补这一空白：提供一个编程语言 Ou 和编译器框架 Lian，让开发者用熟悉的类 C 语法编写语句，而编译器自动完成语句的并行分块，无需开发者理解分布式密码学。

### 相关工作

[41] Wu 等. DIZK: A Distributed Zero Knowledge Proof System. **USENIX Security 2018** [Google Scholar](https://scholar.google.com/scholar?q=DIZK%3A+A+Distributed+Zero+Knowledge+Proof+System)
> 核心思路：手动将 Groth 协议 [27] 的 R1CS 约束划分为等大小块，在集群中并行证明。  
> 局限与区别：要求开发者手动划分且协议特定；本文通过编译器自动分析并支持任意 commit-and-prove 后端。

[42] Xie 等. zkBridge: Trustless Cross-chain Bridges Made Practical. **CCS 2022** [Google Scholar](https://scholar.google.com/scholar?q=zkBridge%3A+Trustless+Cross-chain+Bridges+Made+Practical)
> 核心思路：将 Virgo [44] 的证明者计算分布到多服务器，但要求语句本身具有高度并行性。  
> 局限与区别：不能自动处理任意语句；本文利用 precomputation 打破数据依赖性，可并行化原本顺序的语句。

[43] Yang 等. EZEE: Epoch Parallel Zero Knowledge for ANSI C. **ePrint 2022** [Google Scholar](https://scholar.google.com/scholar?q=EZEE%3A+Epoch+Parallel+Zero+Knowledge+for+ANSI+C)
> 核心思路：将 garbled-circuit 类 ZK 协议分布式化，支持多个 prover-verifier 并行运行的 epoch。  
> 局限与区别：针对特定协议并需要手工调整；本文提供通用语言前端和自动划分。

[37] Wahby 等. Full accounting for verifiable outsourcing. **CCS 2017** [Google Scholar](https://scholar.google.com/scholar?q=Full+accounting+for+verifiable+outsourcing)
> 核心思路：在可验证外包环境中自动分解超大计算，使其可直送出城。  
> 局限与区别：不针对 ZK，且依赖手动分析；本文使用 PBO/ILP 自动求解最优划分。

[2] Agrawal 等. Non-Interactive Zero-Knowledge Proofs for Composite Statements. **CRYPTO 2018** [Google Scholar](https://scholar.google.com/scholar?q=Non-Interactive+Zero-Knowledge+Proofs+for+Composite+Statements)
> 核心思路：提出 commit-and-prove 的 NIZK 构造，支持对同一证据证明多个子语句。  
> 局限与区别：未自动化划分；本文将其作为后端使用。

[27] Groth. On the Size of Pairing-Based Non-interactive Arguments. **EUROCRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=On+the+Size+of+Pairing-Based+Non-interactive+Arguments)
> 核心思路：经典 zkSNARK 构造，证明几乎为常数大小。  
> 局限与区别：需要 O(T) 的临时存储；DIZK [41] 手动划分该协议。

[44] Zhang 等. Transparent Polynomial Delegation and Its Applications to Zero Knowledge Proof. **S&P 2020** [Google Scholar](https://scholar.google.com/scholar?q=Transparent+Polynomial+Delegation+and+Its+Applications+to+Zero+Knowledge+Proof)
> 核心思路：基于多项式承诺的透明 SNARK。  
> 局限与区别：被 zkBridge [42] 用于并行化，但只能利用语句已有的并行性。

[4] Baum 等. Mac’n’Cheese: Zero-Knowledge Proofs for Boolean and Arithmetic Circuits with Nested Disjunctions. **CRYPTO 2021** [Google Scholar](https://scholar.google.com/scholar?q=Mac%27n%27Cheese%3A+Zero-Knowledge+Proofs+for+Boolean+and+Arithmetic+Circuits+with+Nested+Disjunctions)
> 核心思路：VOLE 类 ZK 协议，低内存但高带宽。  
> 局限与区别：未自动化划分；本文在评估中将其作为后端。

### 核心技术与方案

本文整体架构分为前端语言 Ou 和后端编译器 Lian。Ou 提供类 C 语法，每个变量用安全格（图 3）中的标签标注，格的两维是公开/私有（pub/pvt/plc）和知识层级（K0/K1/K2）。K0 表示编译时已知，K1 表示分布时已知，K2 仅在运行时已知。类型系统强制执行非干涉性，确保 K0 和 K1 的值可以流入 K2（反之不行），从而保证浅模拟时控制流完全由 K0 值决定。

编译流程分为三个阶段：浅模拟（shallow simulation）、划分（partitioning）和深模拟（deep simulation）。浅模拟首先展开循环、内联普通函数，用 K0 知识简化计算，生成一个由顺序指令块构成的扁平化程序。若函数标注为 `atomic`，则其内部指令会被合并为一个块（仅暴露累积代价和读写集），从而控制后续划分问题的图规模。浅模拟的正确性由定理 1 保证：浅模拟执行得到的扁平程序与原程序在任意完全已知的堆栈上行为等价。

划分阶段对扁平程序进行活跃变量分析，构建有向无环依赖图 G=(V,E)，每个节点 i 有计算代价 PC_i，每条边 (i,j) 有通信代价 C_ij（或 ∞ 表示不可切割，当存在 K2 依赖时强制共处一块）。然后求解以下 PBO 问题：寻找分区函数 chunk(i) ∈ [κ]，使得目标函数 sum_{edges cut} C_ij + max_{t in [κ]} sum_{i in chunk_t} PC_i 最小化。该问题编码为整数线性规划（ILP）或等价于伪布尔优化（PBO），约束条件包括：每个指令恰在一个分区；只有可切割边才被切割；若 i 和 j 在不同分区，则边 (i,j) 必须标记为切割；COP 变量编码各分区计算代价的最大值。求解器输出 chunk 函数后，编译器生成 κ 个分布式程序，每块包含 sync 步骤（用于从其他块接收依赖数据）、对应的指令序列和最终的 consistency check。

深模拟阶段使用 K1 知识（即具体的秘密输入和公有 K0 常数）执行原程序，计算所有可能被跨分区依赖的 K1 值（定理 4 保证 K2 值不会跨分区依赖）。这些值随后随分布式程序一同分发给各个 prover 核心。完整分布式的正确性（定理 6）通过逐步相似论证证明：每个分区中 sync 之后得到的局部堆栈，与未划分执行的相应步骤的堆栈，在必要的依赖变量集上相似。

系统不假设特定 ZK 后端，只需后端支持 commit-and-prove 范式且能安全工作在并行组合下（例如通过 Fiat-Shamir 变换获得的 NIZK）。评估中使用 VOLE 类后端（EMP [39]）以处理大规模语句。编译的渐进复杂度主要由 PBO 求解决定，其输入图为 O(指令数) 个节点，但 atomic 注释可大幅压缩规模；深模拟的代价小于编译时间的 0.5%。

### 核心公式与流程

**[PBO 优化目标]**
$$\min \sum_{i=1}^{\text{ub}} 2^{i-1} \cdot \text{COP}_i + \sum_{e \in E} C_e \cdot Y_e$$
> 作用：平衡各分块的计算代价和跨分块通信代价，其中 ub = log2(∑PC_i)，COP_i 编码各块最大代价的二进制位，Y_e 指示是否切割边 e。约束条件见 5.2 节式 (1)–(8)。

**[浅模拟指令语义（示例）]**
$$(\tau x = e, \Omega) \leadsto_C (\text{cont}, \Omega[\alpha \mapsto \lfloor e' \rfloor_{R_0}], \tau \alpha = e')$$
> 其中 \(\lfloor \cdot \rfloor_{R_0}\) 将 K0 原子值保留下标、其余替换为 SVsym；生成的扁平程序指令记入历史。作用：将程序展开为仅含纯指令的序列。

**[活跃变量分析递推]**
$$\text{LIVE}(i-1) = \{\mu \mapsto j \in \text{LIVE}(i) \mid \mu \notin \text{DEF}(c_i) \cup \text{REF}(c_i)\} \cup \{\mu \mapsto i \mid \mu \in \text{REF}(c_i)\}$$
> 计算每个指令块的读集 (REF) 和写集 (DEF)，再由后向前扫描建立依赖边 (i,j) 及传递的变量集合 DEP(i,j)。

**[正确性定理（简化）]**
$$\forall j \in \text{chunk}^{-1}(t), \Omega_j^{\text{pre}} \approx_S \Omega_{j-1} \quad \text{where } S = \text{DEP}(-, j)$$
> 定理 6：在分布式执行中，sync 之后当前块的堆栈与未划分版本的堆栈在依赖变量上相似，保证后续指令行为一致。

### 实验结果

实验使用 AWS m5.large 实例（2 vCPU, 8GB RAM），选择两类基准程序：梯度下降（GD，逻辑回归，10 个特征，20 个样本，迭代 20–80 轮）和 Merkle 树（MT，数据块数 8–128）。编译器后端采用 VOLE 类 ZK 协议（EMP [39]）。核心性能指标为有效比（sequential cost / distributed cost）和端到端运行时间。对于大型程序（GD 迭代 80 轮，MT 输入 128 块），有效比接近机器数 κ（如 κ=40 时有效比约 39.8/38.6）。atomic 注释可将 PBO 编译时间降低 1–60 倍（GD 中从 2200s 降至 700s），且在某些情况下（MT 32 块，κ=30）反而提升有效比（20.5 vs 15.5），因为缩小搜索空间后 600 秒求解器能找到更优解。端到端测试显示 GD（200 轮）在 κ=1 到 κ=40 时运行时间从 681.55s 降至 21.90s（加速比 31.12 倍）；MT（256 数据块）从 40.23s 降至 5.25s（7.66 倍）。两基准的加速比均接近有效比，仅当每块运行时间接近常数后台开销（约 4s）时略有偏离。

### 局限性与开放问题

本文不处理程序的功能正确性、数据无关性及证据困难性，假定用户书写的 Ou 程序对其预期 ZK 应用是正确且安全的。atomic 注释的效果依赖用户对程序结构的理解，不当标注可能增加编译时间，但不会破坏安全。系统当前仅支持 VOLE 后端作为评估，虽设计上可扩展至其他 commit-and-prove 协议，但需要额外适配工作。处理包含大量跨分区 K2 依赖的程序时，不可切割约束可能限制并行度，导致有效比上限远小于 κ。

### 强关联论文

[41] Wu et al. DIZK: A Distributed Zero Knowledge Proof System. **USENIX Security 2018** [Google Scholar](https://scholar.google.com/scholar?q=DIZK%3A+A+Distributed+Zero+Knowledge+Proof+System)

[37] Wahby et al. Full accounting for verifiable outsourcing. **CCS 2017** [Google Scholar](https://scholar.google.com/scholar?q=Full+accounting+for+verifiable+outsourcing)

[43] Yang et al. EZEE: Epoch Parallel Zero Knowledge for ANSI C. **ePrint 2022** [Google Scholar](https://scholar.google.com/scholar?q=EZEE%3A+Epoch+Parallel+Zero+Knowledge+for+ANSI+C)

[42] Xie et al. zkBridge: Trustless Cross-chain Bridges Made Practical. **CCS 2022** [Google Scholar](https://scholar.google.com/scholar?q=zkBridge%3A+Trustless+Cross-chain+Bridges+Made+Practical)

[44] Zhang et al. Transparent Polynomial Delegation and Its Applications to Zero Knowledge Proof. **S&P 2020** [Google Scholar](https://scholar.google.com/scholar?q=Transparent+Polynomial+Delegation+and+Its+Applications+to+Zero+Knowledge+Proof)

[27] Groth. On the Size of Pairing-Based Non-interactive Arguments. **EUROCRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=On+the+Size+of+Pairing-Based+Non-interactive+Arguments)

[4] Baum et al. Mac’n’Cheese: Zero-Knowledge Proofs for Boolean and Arithmetic Circuits with Nested Disjunctions. **CRYPTO 2021** [Google Scholar](https://scholar.google.com/scholar?q=Mac%27n%27Cheese%3A+Zero-Knowledge+Proofs+for+Boolean+and+Arithmetic+Circuits+with+Nested+Disjunctions)

[16] Campanelli et al. LegoSNARK: Modular Design and Composition of Succinct Zero-Knowledge Proofs. **CCS 2019** [Google Scholar](https://scholar.google.com/scholar?q=LegoSNARK%3A+Modular+Design+and+Composition+of+Succinct+Zero-Knowledge+Proofs)

[30] Jawurek et al. Zero-knowledge using garbled circuits: how to prove non-algebraic statements efficiently. **CCS 2013** [Google Scholar](https://scholar.google.com/scholar?q=Zero-knowledge+using+garbled+circuits%3A+how+to+prove+non-algebraic+statements+efficiently)

[39] Wang et al. EMP-toolkit: Efficient MultiParty Computation Toolkit. **GitHub 2016** [Google Scholar](https://scholar.google.com/scholar?q=EMP-toolkit%3A+Efficient+MultiParty+Computation+Toolkit)


## 关键词

+ 零知识证明
+ 编程语言设计
+ 并行化
+ 编译器优化
+ 形式化方法
+ 组合优化