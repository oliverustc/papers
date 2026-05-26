---
title: "Ceno: Non-uniform, Segment and Parallel Zero-Knowledge Virtual Machine"
标题简称: Ceno
论文类型: journal
期刊简称: Journal of Cryptology
发表年份: 2025
modified: 2025-04-29 16:29:09
created: 2025-04-07 17:09:14
---

## Ceno: Non-uniform, Segment and Parallel Zero-Knowledge Virtual Machine

## 发表信息

+ [原文链接](https://link.springer.com/article/10.1007/s00145-024-09533-2)
+ [code](https://github.com/scroll-tech/ceno)

## 作者

+ [Tianyi Liu](Tianyi%20Liu.md)
+ [Zhenfei Zhang](Zhenfei%20Zhang.md)
+ Yuncong Zhang
+ Wenqing Hu
+ [Ye Zhang](Ye%20Zhang.md)
## 笔记

### 背景与动机
传统的零知识虚拟机 (zkVM) 采用统一的电路来模拟完整的虚拟机执行逻辑，这导致证明器在证明动态程序时必须为所有控制流和存储操作（如栈、内存、跳转）生成大量约束，其工作量与程序最大长度而非实际执行路径成正比。以 Scroll 的 zkEVM [55] 为例，每个操作码可能产生超过一百个控制器见证，显著增加了证明复杂度。现有的 vRAM 方案 [68] 虽然也使用 GKR 协议，但其通过索引高位选择操作码的方式要求所有操作码电路大小统一，并需对程序长度设置上限并进行填充，同时需要按时间顺序重排 RAM 操作并验证相邻条目的时间戳和地址关系，这导致额外的承诺和范围检查开销。本文旨在填补一个空白：如何设计一个 zkVM，其证明成本仅与程序实际执行的操作码数量成正比，并能利用程序内部的重复结构（如同类型操作码的批量执行）来进一步提升效率，同时避免传统方法中为处理动态控制流而引入的固定冗余。

### 相关工作

[25] Goldwasser et al. Delegating computation: interactive proofs for muggles. **STOC 2008** [Google Scholar](https://scholar.google.com/scholar?q=Delegating+computation%3A+interactive+proofs+for+muggles)
> 核心思路：提出了 GKR 协议，一种用于通用算术电路的交互式证明，证明器运行时间与电路大小成线性关系。
> 局限与区别：原始 GKR 协议及其早期改进（如 [19]）对于非数据并行电路，其证明器复杂度不是最优的线性时间。

[56] Thaler. Time-Optimal Interactive Proofs for Circuit Evaluation. **CRYPTO 2013** [Google Scholar](https://scholar.google.com/scholar?q=Time-Optimal+Interactive+Proofs+for+Circuit+Evaluation)
> 核心思路：改进了 GKR 协议，实现了对通用电路的拟线性时间证明器。
> 局限与区别：该工作并未专门针对 zkVM 场景，未利用程序执行中存在的天然并行结构（如重复的操作码）。

[62] Xie et al. Libra: Succinct zero-knowledge proofs with optimal prover computation. **CRYPTO 2019** [Google Scholar](https://scholar.google.com/scholar?q=Libra%3A+Succinct+zero-knowledge+proofs+with+optimal+prover+computation)
> 核心思路：提出了 Libra，一个具有最优证明器复杂度的 GKR 实例化，其证明器时间与电路大小成线性关系。
> 局限与区别：主要针对静态电路，未涉及如何将动态程序执行高效地映射到其架构中。

[68] Zhang et al. vRAM: Faster verifiable RAM with program-independent preprocessing. **IEEE S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=vRAM%3A+Faster+verifiable+RAM+with+program-independent+preprocessing)
> 核心思路：提出了 vRAM 方法，使用 GKR 协议证明 RAM 执行，通过预处理来加速。
> 局限与区别：必须将操作码电路大小标准化，对程序长度进行填充，并需要重排 RAM 操作和验证时间戳顺序。本文通过非均匀证明器和移除对连续范围检查的需求，克服了这些限制。

[22] Gabizon et al. PLONK: Permutations over Lagrange-bases for Oecumenical Noninteractive arguments of Knowledge. **ePrint 2019** [Google Scholar](https://scholar.google.com/scholar?q=PLONK%3A+Permutations+over+Lagrange-bases+for+Oecumenical+Noninteractive+arguments+of+Knowledge)
> 核心思路：提出了 PLONK 协议，是一种广泛应用的 zk-SNARK 方案。
> 局限与区别：PLONK 证明器需要对所有中间见证进行多项式承诺，并依赖 FFT 进行多项式乘法，其复杂度为 O(N log N)，而 GKR 协议在这些方面具有优势，因为它只需要承诺输入和输出，且核心的 sumcheck 协议是线性时间的。

[29] Kothapalli et al. Nova: Recursive zero-knowledge arguments from folding schemes. **CRYPTO 2022** [Google Scholar](https://scholar.google.com/scholar?q=Nova%3A+Recursive+zero-knowledge+arguments+from+folding+schemess)
> 核心思路：提出了 Nova，一种基于折叠方案的递归证明系统，适合将长执行序列分段证明。
> 局限与区别：Nova 等方案主要关注递归证明的效率，而本文则专注于优化第一阶段的非递归证明，通过利用程序结构来减少约束。

[66] Zhang et al. Doubly efficient interactive proofs for general arithmetic circuits with linear prover time. **CCS 2021** [Google Scholar](https://scholar.google.com/scholar?q=Doubly+efficient+interactive+proofs+for+general+arithmetic+circuits+with+linear+prover+time)
> 核心思路：改进了 GKR，支持非连续层电路，提高了通用电路的验证效率。
> 局限与区别：其拓扑排序的方法难以支持自定义层结构，且不支持高扇入门；本文通过引入“粘贴自”和“复制到”等操作，提出了一种更灵活的层结构。

### 核心技术与方案

本文的核心思想是将 zkVM 的证明过程分为两个阶段，并引入非均匀证明器以降低第一阶段的开销。

第一阶段，程序执行被分解为多个段（segments）。根据分段粒度的不同，本文提出了两种互补的设计：**Ceno Basic** 和 **Ceno Pro**。

**Ceno Basic** 的操作码级并行化。该方案将程序执行中出现的同类型操作码（opcode）聚类。证明器为每种操作码类型创建一个数据并行电路，该电路的输入是代表该操作码所有执行实例的见证，输出是各种芯片记录（如栈、内存的读写记录）。证明器使用 GKR 布局的数据并行电路为每个操作码类型生成证明。此阶段的核心在于，每个操作码电路的副本数量由程序的实际执行流动态决定，因此证明器是非均匀的。第一阶段的输出是每个操作码类型电路的读写记录乘积 $`\delta_R^{(\text{op})}`$ 和 $`\delta_W^{(\text{op})}`$。

**Ceno Pro** 的基本块级并行化。该方案进一步利用程序在编译器层面的结构——基本块（Basic Block, BB）。基本块是一段顺序执行的、内部无分支的指令序列。Ceno Pro 将每个基本块建模为一个 GKR 图电路，其中块内的每个非栈操作码都是一个子电路，而栈操作则被建模为连接这些子电路的导线。子电路不再管理复杂的栈操作和字节码查找，这些操作被推迟到第二阶段。第一阶段的证明器为每个基本块电路生成证明，其输出是块内所有子电路的芯片记录乘积。

第二阶段，验证器验证第一阶段的所有证明，并检查所有芯片记录的一致性。关键的等式是确保所有操作产生的“写记录乘积”等于所有操作产生的“读记录乘积”，即：
$$`
\delta_R^{(\text{mem,finl})} \cdot \delta_R^{(\text{st,finl})} \cdot \left(\prod_{\text{op in opcodes}} \delta_R^{(\text{op})}\right) \cdot \left(\prod_{\text{chip in Lookup}} \delta_R^{(\text{chip})}\right) = \delta_W^{(\text{mem,init})} \cdot \left(\prod_{\text{op in opcodes}} \delta_W^{(\text{op})}\right) \cdot \left(\prod_{\text{chip in Lookup}} \delta_W^{(\text{chip})}\right)
$$`
对于 Ceno Pro，验证器在验证过程中扮演了一个重要角色：它维护一个本地栈，通过反向扫描程序的操作码序列，来“模拟”基本块内部的栈操作。具体来说，验证器在验证一个基本块的证明时，从 BB final 电路开始，将其输出评估推入本地栈。然后，对于每个操作码，根据它是弹出还是推入操作，从栈中弹出或推入相应的 GKR 评估值。最后，验证 BB start 电路时，校验本地栈的状态。这种方法将栈操作的成本从证明器（需为每次执行生成约束）转移到了验证器（只需为每条操作码指令执行一次逻辑操作），极大地减少了约束数量。

算法的安全性基于离线内存检查论证，所有存储操作都被规约到集合相等性论证。该论证通过一个随机线性组合（RLC）将记录映射为域元素，并验证所有元素的乘积是否相等，如以下公式所示：
$$`
\prod_{i} (RLC(w_i) + \tau) = \prod_{i} (RLC(r_i) + \tau)
`$$
其中 $w_i$ 和 $r_i$ 分别是写入和读取的记录，$\tau$ 是验证器提供的随机挑战。GKR 协议为这些证明提供了完备性和知识可靠性，其安全性依赖于 sumcheck 协议的正确性。证明器时间复杂度为 O(N)，其中 N 是总执行步数。验证器的时间复杂度为 O(log^2 N)。递归证明可以进一步减小证明大小和验证时间。

### 核心公式与流程

**[离线内存检查的集合相等性论证]**
$$`
\prod_{i=0}^{N_w-1} (\text{RLC}(w_i) + \tau) = \prod_{i=0}^{N_r-1} (\text{RLC}(r_i) + \tau)
`$$
> 作用：这是整个系统安全性的基石。它将内存、栈等芯片操作的一致性检验规约为一个乘积相等检验。证明器需要证明写入和读取的记录集合（经过随机化后）是相等的，从而确保没有无意或恶意的内存访问。

**[Ceno Basic 验证器核心检查等式]**
$$`
\delta_R^{(\text{mem,finl})} \cdot \delta_R^{(\text{st,finl})} \cdot \left(\prod_{\text{op} \in Q} \delta_R^{(\text{op})}\right) \cdot \left(\prod_{\text{chip} \in \text{Lookup}} \delta_R^{(\text{chip})}\right) = \delta_W^{(\text{mem,init})} \cdot \left(\prod_{\text{op} \in Q} \delta_W^{(\text{op})}\right) \cdot \left(\prod_{\text{chip} \in \text{Lookup}} \delta_W^{(\text{chip})}\right)
`$$
> 作用：这是 Ceno Basic 协议第二阶段的核心验证等式。$\delta$ 项代表各电路输出的读写记录集合的乘积。该等式确保了所有读写操作在整个程序执行过程中是全局一致的。

**[Ceno Pro 的 GKR 层间关系（数据并行 Gate 实例化）]**
$$`
\widetilde{V}_i(\mathbf{Y}||\mathbf{T}) = \sum_{\mathbf{b}_s^{(0)}, \ldots, \mathbf{b}_s^{(d-1)}, \mathbf{b}_x^{(0)} \ldots \mathbf{b}_x^{(d-1)}} \tilde{eq}(\mathbf{T},\mathbf{b}_s^{(0)},\ldots,\mathbf{b}_s^{(d-1)})G_A(\mathbf{Y},\mathbf{b}_x^{(0)},\ldots,\mathbf{b}_x^{(d-1)}) \cdot \widetilde{V}_{i+1}(\mathbf{b}_x^{(0)}||\mathbf{b}_s^{(0)}) \ldots \widetilde{V}_{i+1}(\mathbf{b}_x^{(d-1)}||\mathbf{b}_s^{(d-1)})
`$$
> 作用：这是 GKR 协议中，对于包含高扇出乘积门 (Gate A) 的电路，第 i 层输出 $`\widetilde{V}_i`$ 与下一层输入 $`\widetilde{V}_{i+1}`$ 之间的数学关系。它通过一个 sumcheck 过程来证明输出是由多个输入的乘积正确计算得到的，是 GKR 证明过程的核心步骤。

**[Ceno Pro 基本块中栈操作的阶段分离]**
> 作用：该流程不是公式，而是一个关键的概念流程。在 Ceno Pro 中，第一阶段（证明器）的电路仅包含非栈操作码，栈操作被省略。第二阶段（验证器）在进行验证时，通过模拟栈操作来重建电路内的连线关系。这个过程被表述为：验证器扫描基本块的操作码，并针对每一个栈操作对其本地栈执行反向操作，从而正确地将各个 GKR 子电路的输入输出评估值连接起来。

### 实验结果

论文仅提供了 Ceno Basic 和 Ceno Pro 中部分 EVM 操作码的承诺见证大小（如表1所示），未提供完整的实验设置、运行环境和性能基准。对于 Ceno Basic，其每个操作码的见证大小在 0 到 140 之间（取决于操作类型，如 MSTORE 消耗 $`64 + 32 \times 32`$）。对于 Ceno Pro，许多栈操作操作码（如 POP, SWAP2, DUP1, PUSH1）的见证大小被标记为“-”，表示它们在第一阶段电路中不被需要，从而证明了 Ceno Pro 在减少栈相关约束方面的有效性。非栈操作如 ADD 的见证大小从 Ceno Basic 的 128 降低到 Ceno Pro 的 32，JUMPI 从 64 降低到 16。这些数字表明 Ceno Pro 方案能够显著减少电路内的约束数量。

### 局限性与开放问题
Ceno Pro 方案虽然对重复执行的基本块非常有效，但对于执行次数很少或完全不重复的基本块，其阶段性部署的复杂度可能使其效率不如更直接的 Ceno Basic 方案。如何自动地、最优地将程序分割成不同的段，并决定每个段应采用 Ceno Basic 还是 Ceno Pro 方案，仍是一个复杂的优化问题，需要进一步的研究。此外，虽然 GKR 协议的证明器是线性的，但其验证器和递归证明的复杂度仍需要在实际部署中进行更精细的权衡和优化。

### 强关联论文

[68] Zhang et al. vRAM: Faster verifiable RAM with program-independent preprocessing. **IEEE S&P 2018**

[25] Goldwasser et al. Delegating computation: interactive proofs for muggles. **STOC 2008**

[22] Gabizon et al. PLONK: Permutations over Lagrange-bases for Oecumenical Noninteractive arguments of Knowledge. **ePrint 2019**

[62] Xie et al. Libra: Succinct zero-knowledge proofs with optimal prover computation. **CRYPTO 2019**

[66] Zhang et al. Doubly efficient interactive proofs for general arithmetic circuits with linear prover time. **CCS 2021**

[56] Thaler. Time-Optimal Interactive Proofs for Circuit Evaluation. **CRYPTO 2013**

[29] Kothapalli et al. Nova: Recursive zero-knowledge arguments from folding schemes. **CRYPTO 2022**

[15] Chen et al. Hyperplonk: Plonk with linear-time prover and high-degree custom gates. **EUROCRYPT 2023**

[50] Setty. Spartan: Efficient and general-purpose zksnarks without trusted setup. **CRYPTO 2020**

[19] Cormode et al. Practical Verified Computation with Streaming Interactive Proofs. **ITCS 2012**


## 关键词

+ Ceno零知识虚拟机zkVM
+ 非均匀分段并行零知识证明
+ 数据并行电路程序执行证明
+ GKR方案非均匀证明者
+ 操作码基本块层级分段
+ 可验证计算任意代码