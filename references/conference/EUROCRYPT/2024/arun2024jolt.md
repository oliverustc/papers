---
title: "Jolt: SNARKs for Virtual Machines via Lookups"
doi: 10.1007/978-3-031-58751-1_1
标题简称: Jolt
论文类型: conference
会议简称: EUROCRYPT
发表年份: 2024
modified: 2025-04-23 15:20:15
created: 2025-04-08 18:55:32
---
## Jolt: SNARKs for Virtual Machines via Lookups

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-58751-1_1)'
+ [code](https://github.com/a16z/jolt)

## 作者

+ [Arasu Arun](Arasu%20Arun.md)
+ [Srinath Setty](Srinath%20Setty.md)
+ [Justin Thaler](Justin%20Thaler.md)

## 笔记

### 背景与动机
零知识虚拟机（zkVM）允许证明者向验证者证明某个计算机程序被正确执行，是实现可验证计算和区块链扩容的关键基础设施。然而，现有的 zkVM 系统面临严重的性能瓶颈：证明者为每个 CPU 步骤需要生成大量密码学承诺，导致证明计算极其昂贵。传统的 zkVM 前端将每条指令的逻辑编码为大量算术约束或电路门，特别是对于像 RISC-V 这样功能丰富的指令集，这种方式不仅导致电路规模庞大，而且审计和验证困难。一个流行的观点是，更简单的指令集能产生更小的电路，但代价是：标准操作（如 Keccak 哈希或 ECDSA 验证）在简单 VM 上需要模拟成千上万条指令，反而加剧了效率问题。例如，Cairo-VM 的证明者每步需要向约 50 个域元素提交承诺，而其指令集已被特意设计为“SNARK 友好”。因此，亟需一种新范式，在支持复杂指令集的同时，实现比现有系统显著更快的证明者性能，并提升系统的可审计性和可扩展性。Jolt 试图通过将指令执行转化为对大型、结构化查找表的查询来颠覆这一现状，从而消除大量手写的、易出错的电路约束 [Whi, STW23]。

### 相关工作

[GPR21] Goldberg 等. **Cairo – a Turing-complete STARK-friendly CPU architecture**. *Cryptology ePrint Archive 2021* [Google Scholar](https://scholar.google.com/scholar?q=Cairo+STARK-friendly+CPU+architecture)
> 核心思路：设计了一个极简的虚拟机 Cairo-VM，其指令集专门为 STARK 证明系统优化。
> 局限与区别：尽管指令集简单，证明者每步依然需要提交约 50 个域元素，且复杂操作在 Cairo-VM 上需要大量指令模拟。Jolt 证明者在处理更复杂 RISC-V 指令集时，成本反而更低。

[Sol23] Solberg. **RISC Zero prover protocol & analysis**. *GitHub whitepaper 2023* [Google Scholar](https://scholar.google.com/scholar?q=RISC+Zero+prover+protocol+analysis+Solberg)
> 核心思路：RISC Zero 项目使用 RISC-V 指令集，利用 FRI 作为多项式承诺方案，产生证明。
> 局限与区别：RISC Zero 证明者每步至少提交 275 个 31 位域元素，折合约 34 个 256 位等价元素。Jolt 仅需提交不到 11 个 256 位等价元素，性能显著提升。

[STW23] Setty 等. **Lasso: Unlocking the lookup singularity**. *Cryptology ePrint Archive 2023* [Google Scholar](https://scholar.google.com/scholar?q=Lasso+lookup+argument+Setty+Thaler+Wahby)
> 核心思路：提出 Lasso 查找参数，能够对超大（>2^128）但具备“可分解性”的查找表进行高效证明，而无需承诺整个表。
> 局限与区别：Lasso 是 Jolt 的底层技术；Jolt 的核心贡献在于证明所有 RISC-V 指令的求值表都满足 Lasso 所需的“可分解性”和“MLE 结构化”性质。

[GWC19] Gabizon 等. **Plonk: Permutations over Lagrange-bases for oecumenical noninteractive arguments of knowledge**. *ePrint 2019* [Google Scholar](https://scholar.google.com/scholar?q=Plonk+permutations+over+Lagrange+bases)
> 核心思路：设计了一种流行的算术化后端，证明者每门电路需提交约 11 个域元素。
> 局限与区别：Jolt 证明者每步 RISC-V CPU 的成本相当于在 Plonk 后端中仅有一扇门，证明了其极致高效性。

[SAGL18] Setty 等. **Proving the correct execution of concurrent services in zero-knowledge**. *OSDI 2018* [Google Scholar](https://scholar.google.com/scholar?q=Proving+correct+execution+concurrent+services+zero-knowledge+Spice)
> 核心思路：提出了一个高效的内存检查参数，通常仅需对检查迹做轻量级指纹认证。
> 局限与区别：Jolt 使用并优化了 Spice 的内存检查技术，通过 Lasso 来执行必要的范围检查，进一步降低了成本。

[BSCG+13a] Ben-Sasson 等. **SNARKs for C: verifying program executions succinctly and in zero knowledge**. *CRYPTO 2013* [Google Scholar](https://scholar.google.com/scholar?q=SNARKs+for+C+verifying+program+executions)
> 核心思路：通过 TinyRAM 模型将 C 程序编译为 RAM 执行迹，再转化为电路可满足性问题。
> 局限与区别：每个执行步骤需要巨大的电路，且为特定程序重新生成电路。Jolt 的电路是程序独立的（由 ISA 确定），且证明者成本更低。

[WA17] Waterman 等. **The RISC-V instruction set manual**. *RISC-V Foundation 2017* [Google Scholar](https://scholar.google.com/scholar?q=The+RISC-V+instruction+set+manual+Waterman+Asanovic)
> 核心思路：RISC-V 是一个开放、模块化的指令集架构规范。
> 局限与区别：Jolt 将 RISC-V 作为目标 ISA，证明了其所有指令都满足“可分解性”，从而可以被 Lasso 高效处理，表明此方法适用于现实世界的复杂 ISA。

### 核心技术与方案
Jolt 的核心思想是为每个虚拟机步骤承担的工作从**实现指令逻辑**转变为**进行一次查找**。具体来说，对于 RISC-V 的每个操作码 `opcode`，构造一个巨大的查找表 `T_opcode`，该表包含了该指令在所有可能的输入对上（例如，两个 64 位输入）的函数值 `f(x, y)`。Jolt 将所有指令的表拼接成一个单一的超大型表 `T_risc-v`，表的索引由操作码和操作数拼接而成：`[opcode || x || y]`。Jolt 证明者的工作因此简化为：1) 准备操作数 `x, y`（源于寄存器值、立即数或 PC）；2) 执行一次对该超大型表的查找，**并使用 Lasso 证明查找的正确性**。

**分解与 Lasso 协同工作的关键是“可分解性”**。一个大小为 N 的表是可分解的，如果它能被划分为 c 块，每个块大小为 N^{1/c}，并且存在若干个小且“MLE 结构化”的子表。此外，还必须存在一个简单的**组合多项式** g，使得原始表的查询结果 `T[r]` 可以通过组合子表的查询结果得到。Jolt 的核心贡献是证明了 RISC-V 的所有指令都满足这一性质。例如，对于 64 位的逐位与（AND）运算，可以将其分解为 8 个 8 位的逐位与运算，每个子表大小为 2^16，且其多线性扩展（MLE）可以简单计算：$\widetilde{T}_{\text{AND}}(x, y) = \sum_{i=0}^{7} 2^{8i} \cdot x_i \cdot y_i$。对于更复杂的指令，如小于比较（LTU），其分解则需要同时使用 LTU 和等式（EQ）子表，并通过累加和连乘的组合多项式进行重构。

Lasso 协议在此框架下的工作流程是：证明者向 Lasso 提供所有查找查询（操作码和操作数）的迹，以及声称的查找结果。Lasso 验证证明者提供的操作数分解（即“块”）是正确的（通过对块执行范围检查），并证明每个块在对应子表中的访问模式是一致的。这一致性是通过对访问计数的证明来实现的，这本质上是内存检查过程。由于 Jolt 的所有子表都是“MLE 结构化的”（即其 MLE 可以在对数时间内被求值），**Lasso 不需要任何人密码学地提交这些子表**，从而避免了协议的主要开销。

Jolt 的整体框架还包含**内存检查模块**来处理对程序代码、寄存器堆和随机访问内存的读写。Jolt 采用 Spice [SAGL18] 的离线内存检查技术，证明者提交一个由所有内存访问（地址、值、时间戳）构成的三元组迹。Spice 协议确保读操作返回的是最新写入的值。Jolt 将内存检查与 Lasso 结合起来，内存检查中的范围检查（例如，确保字节值在 0..255 之间）也被实现为对小型子表的 Lasso 查找。整个系统的安全性依赖于：**Lasso 查找证明了所有指令逻辑的正确性**；**Spice 内存检查证明了内存状态的正确性**；**一个极小的 R1CS 约束系统（每步少于 50 个约束）则负责“粘合”所有模块的正确性**，例如验证从程序代码中读取的指令被正确地解析成操作码和操作数。这个 R1CS 系统通过 Spartan [Set20] 后端进行证明。

### 核心公式与流程

**[多线性扩展（MLE）定义]**
给定函数 $f: \{0,1\}^\ell \rightarrow \mathbb{F}$，其多线性扩展 $\widetilde{f}: \mathbb{F}^\ell \rightarrow \mathbb{F}$ 是一个在每个变量上次数至多为 1 的多项式，并且对于所有 $x \in \{0,1\}^\ell$，有 $\widetilde{f}(x) = f(x)$。
> 作用：MLE 是将离散的表格函数 $f$ 视为连续多项式，从而允许验证者在随机点应用 Schwartz-Zippel 引理进行概率检查。Lasso 利用 $\widetilde{T}$ 的 MLE 可以在多项式时间内被求值这一性质。

**[逐位与（AND）操作的分解]**
$$z = \sum_{i=0}^{7} 2^{8\cdot i} \cdot \mathrm{AND}(X_i, Y_i)$$
其中 $X_i, Y_i$ 是 $x$ 和 $y$ 的第 $i$ 个 8 位块。
> 作用：此公式直观展示了分解核心。一次对 $2^{128}$ 大小表的查询被转化为 8 次对 $2^{16}$ 大小子表 $\mathrm{AND}$ 的查询，这些子表是可管理的。组合多项式 $g$ 即是此求和公式。

**[小于比较（LTU）操作的分解]**
$$\mathrm{LTU}_W[x \parallel y] = \sum_{i=0}^{c-1} \left( \mathrm{LTU}_{W/c}[X_i \parallel Y_i] \cdot \prod_{j < i} \mathrm{EQ}_{W/c}[X_j \parallel Y_j] \right)$$
> 作用：此公式展示了更复杂的分解。它需要两个子表：$\mathrm{LTU}_{W/c}（用于比较块）$ 和 $\mathrm{EQ}_{W/c}（用于判断高位块是否相等）$。结果是通过从高到低扫描块来确定的。

**[左移位（SLL）操作的分解]**
$$\mathbf{SLL}_i[X_i \parallel Y_0] = \sum_{k \in \{0,1\}^{\log W}} \widetilde{\mathsf{EQ}}(Y_0, k) \cdot \left( \sum_{j=0}^{m_{i,k}'} 2^{j+\text{int}(k)} \cdot X_{i,j} \right)$$
其中 $m_{i,k}'$ 表示第 i 个块中在移位 k 后不会溢出的最高位下标。
> 作用：此公式表明移位操作的分解更为特殊，移位量 $Y_0$ 是一个单独的块。子表 $\mathbf{SLL}_i$ 利用 MLE 求值的灵活性，通过对移位量 $k$ 的一热编码（通过 $\widetilde{\mathsf{EQ}}$）来模拟条件移位。

**[统一所有指令的单一大表构造]**
$$g(w, x) = \sum_{y \in \{0,1\}^8} \widetilde{\mathsf{EQ}}(w, y) \cdot g_{\text{int}(y)}(x)$$
其中 $w$ 是操作码的 8 位表示，$g_i$ 是指令 $i$ 的组合多项式，$x$ 是子表查找结果向量。
> 作用：此公式将多个 ISA 指令的独立查找表合并为一个统一的复合表。通过将操作码 $w$ 作为额外输入，复合多项式 $g$ 使用 MLE 计算出的权重来选择和应用与当前指令对应的组合多项式 $g_{\text{int}(y)}$。

### 实验结果
论文通过理论成本分析而非实验运行来评估 Jolt。核心性能指标是证明者每 CPU 步需要密码学承诺的**域元素个数**及其**位长度**，因为这是使用 Pippenger 算法时证明者的主要瓶颈。对于 RV64（64 位 RISC-V），Jolt 每步需要提交约 106 个域元素；其中 12 个是 64 位的大元素，其余多为 22 位及以下的“小”元素。论文使用“等值转换为 256 位元素”这一归一化指标来衡量成本：Pippenger 算法中，承诺一个 $n$ 位元素所需组操作近似为 $\lceil n/22 \rceil$。据此，Jolt 每步的承诺成本等同于向不到 **11 个** 256 位随机域元素进行 MSM 承诺。作为对比，Plonk [GWC19] 后端每门电路需提交 11 个域元素（其中 7 个为大元素），暗示 Jolt 每步 RISC-V 的成本仅相当于 Plonk 中**约一扇门**。与 RISC Zero（约 34 个 256 位等价元素）和 Cairo-VM（约 13 个 256 位等价元素）的比较，Jolt 的性能优势显著，尽管其目标 ISA（RISC-V）远比 Cairo-VM 复杂。对于内存操作，其额外成本仅约 0.5 个 256 位等价元素每字节。验证者开销微小：主要工作是进行 $O(\log T)$ 次 hash 运算和域运算（T 为执行步数），外加一次多项式打开证明验证。

### 局限性与开放问题
Jolt 主要优化了指令逻辑的证明，对于存储、字节寻址等操作仍依赖较直接的约束。论文未提供完整的实现和基准测试，其性能分析基于理论抽象。对于非算数逻辑类操作（如除法指令），Jolt 需要通过“伪指令”进行分解，这增加了额外的证明步骤和约束。最后，将 Jolt 扩展到支持多线程、异常处理等更复杂的运行时特性会影响其现有架构的简洁性。

### 强关联论文

[STW23] Setty et al. **Lasso: Unlocking the lookup singularity**. *Cryptology ePrint Archive 2023* <a target="_blank" href="https://scholar.google.com/scholar?q=Lasso%3A+Unlocking+the+lookup+singularity">[Google Scholar](https://scholar.google.com/scholar?q=Lasso%3A+Unlocking+the+lookup+singularity)</a>

[GPR21] Goldberg et al. **Cairo – a Turing-complete STARK-friendly CPU architecture**. *Cryptology ePrint Archive 2021* <a target="_blank" href="https://scholar.google.com/scholar?q=Cairo+%E2%80%93+a+Turing-complete+STARK-friendly+CPU+architecture">[Google Scholar](https://scholar.google.com/scholar?q=Cairo+%E2%80%93+a+Turing-complete+STARK-friendly+CPU+architecture)</a>

[Sol23] Solberg. **RISC Zero prover protocol & analysis**. *GitHub 2023* <a target="_blank" href="https://scholar.google.com/scholar?q=RISC+Zero+prover+protocol+%26+analysis">[Google Scholar](https://scholar.google.com/scholar?q=RISC+Zero+prover+protocol+%26+analysis)</a>

[GWC19] Gabizon et al. **PLONK: Permutations over Lagrange-bases for oecumenical noninteractive arguments of knowledge**. *ePrint 2019* <a target="_blank" href="https://scholar.google.com/scholar?q=PLONK%3A+Permutations+over+Lagrange-bases+for+oecumenical+noninteractive+arguments+of+knowledge">[Google Scholar](https://scholar.google.com/scholar?q=PLONK%3A+Permutations+over+Lagrange-bases+for+oecumenical+noninteractive+arguments+of+knowledge)</a>

[SAGL18] Setty et al. **Proving the correct execution of concurrent services in zero-knowledge**. *OSDI 2018* <a target="_blank" href="https://scholar.google.com/scholar?q=Proving+the+correct+execution+of+concurrent+services+in+zero-knowledge">[Google Scholar](https://scholar.google.com/scholar?q=Proving+the+correct+execution+of+concurrent+services+in+zero-knowledge)</a>

[Set20] Setty. **Spartan: efficient and general-purpose zkSNARKs without trusted setup**. *CRYPTO 2020* <a target="_blank" href="https://scholar.google.com/scholar?q=Spartan%3A+efficient+and+general-purpose+zkSNARKs+without+trusted+setup">[Google Scholar](https://scholar.google.com/scholar?q=Spartan%3A+efficient+and+general-purpose+zkSNARKs+without+trusted+setup)</a>

[WA17] Waterman et al. **The RISC-V instruction set manual**. *RISC-V Foundation 2017* <a target="_blank" href="https://scholar.google.com/scholar?q=The+RISC-V+instruction+set+manual">[Google Scholar](https://scholar.google.com/scholar?q=The+RISC-V+instruction+set+manual)</a>

[Whi] Whitehat. **Lookup singularity**. *zkResear.ch Forum* <a target="_blank" href="https://scholar.google.com/scholar?q=Lookup+singularity">[Google Scholar](https://scholar.google.com/scholar?q=Lookup+singularity)</a>

[BSCG+13a] Ben-Sasson et al. **SNARKs for C: verifying program executions succinctly and in zero knowledge**. *CRYPTO 2013* <a target="_blank" href="https://scholar.google.com/scholar?q=SNARKs+for+C%3A+verifying+program+executions+succinctly+and+in+zero+knowledge">[Google Scholar](https://scholar.google.com/scholar?q=SNARKs+for+C%3A+verifying+program+executions+succinctly+and+in+zero+knowledge)</a>


## 关键词

+ 零知识虚拟机
+ 查找奇点
+ RISC-V指令集
+ Lasso查找论证
+ zkVM前端