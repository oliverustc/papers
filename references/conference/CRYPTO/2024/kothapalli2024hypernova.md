---
title: "HyperNova: Recursive arguments for customizable constraint systems"
标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 2024
created: 2025-04-21 10:35:51
modified: 2025-04-21 10:36:33
---

## HyperNova: Recursive arguments for customizable constraint systems

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-68403-6_11)

## 作者

+ Abhiram Kothapalli 
+ [Srinath Setty](Srinath%20Setty.md) 

## 笔记

### 背景与动机

递归论证（IVC） [52] 允许证明者以递增方式生成对“长时间运行”计算的证明，其证明生成和验证开销与已执行步数无关，在去中心化场景中具有广泛应用。传统 IVC 实现 [4,52] 依赖于将 SNARK 验证者编码为电路，通常需要引入椭圆曲线循环来降低电路规模 [4]。为解决该瓶颈，Nova [34] 提出了折叠方案，将检查两个具有相同结构的 NP 实例简化为检查单个实例，避免了通用 SNARK 的昂贵操作，实现与电路规模成正比的少量多标量乘法（MSM）开销。然而，Nova 使用 R1CS 作为底层计算模型，R1CS 局限于特定形式的二次约束，而实际应用中常采用更紧凑的高次定制约束系统（如 Plonkish），将高次约束编码为 R1CS 会导致约束数量膨胀，丧失其原有优势。此外，Sangria [41] 虽将 Nova 扩展到 Plonkish，但其证明者承担的“交叉项”承诺数量随约束度数线性增长，导致性能与使用低度数的 R1CS 无显著差别。针对证明机器执行（如 EVM）的场景，通用电路方法 [2,5] 要求证明一个程序步的成本与所有指令的电路大小之和成正比，而非仅与被执行的指令相关。同时，实现零知识通常依赖于零知识 SNARK [46]，其验证者需在链上执行昂贵的群操作。此外，将 Nova 实例化于椭圆曲线循环 [1,42] 时，第二个曲线上的验证电路规模约为 10,000 个乘法门，进一步膨胀到超过 700 万个门。本文旨在同时解决上述四个开放问题，构建一个能够高效处理自定义、高次约束系统，实现“按需付费”成本，无需 zkSNARK 即可获得零知识，并且能更高效地在椭圆曲线循环上实例化的递归论证方案。

### 相关工作

[4] Ben-Sasson 等. Scalable Zero Knowledge via Cycles of Elliptic Curves. **CRYPTO 2014** [Google Scholar](https://scholar.google.com/scholar?q=Scalable+Zero+Knowledge+via+Cycles+of+Elliptic+Curves)
> 核心思路：利用椭圆曲线循环将 SNARK 验证者表示为电路，构建可扩展的递归零知识证明。
> 局限与区别：该方法要求将 SNARK 验证者表示为两条曲线上的电路，导致第二个曲线上的电路规模较大。HyperNova 的 CycleFold 技术将第二个曲线的电路规模缩小至仅表示一个标量乘法，显著降低开销。

[34] Kothapalli 等. Nova: Recursive Zero-Knowledge Arguments from Folding Schemes. **CRYPTO 2022** [Google Scholar](https://scholar.google.com/scholar?q=Nova:+Recursive+Zero-Knowledge+Arguments+from+Folding+Schemes)
> 核心思路：引入折叠方案，将检查两个 R1CS 实例简化为一个，实现高效的 IVC。
> 局限与区别：Nova 局限于 R1CS（二次约束），无法高效处理高次约束如 Plonkish。HyperNova 推广到 CCS，并提供了仅需一个 MSM 的折叠方案。

[41] Mohnblatt. Sangria: A Folding Scheme for PLONK. **ePrint 2023** [Google Scholar](https://scholar.google.com/scholar?q=Sangria:+A+Folding+Scheme+for+PLONK)
> 核心思路：将 Nova 的折叠方案扩展到 Plonkish 约束系统。
> 局限与区别：Sangria 的证明者必须向 O(度数) 个交叉项提交承诺，导致运算成本随度数线性增加。HyperNova 通过求和检查协议避免了交叉项承诺，使证明者的加密成本与度数无关。

[49] Setty 等. Customizable Constraint Systems for Succinct Arguments. **ePrint 2023** [Google Scholar](https://scholar.google.com/scholar?q=Customizable+Constraint+Systems+for+Succinct+Arguments)
> 核心思路：提出 CCS，统一了 R1CS、Plonkish 和 AIR 约束系统。
> 局限与区别：CCS 本身未提供折叠方案。HyperNova 为 CCS 设计了首个高效的折叠方案。

[46] Setty. Spartan: Efficient and General-Purpose zkSNARKs without Trusted Setup. **CRYPTO 2020** [Google Scholar](https://scholar.google.com/scholar?q=Spartan:+Efficient+and+General-Purpose+zkSNARKs+without+Trusted+Setup)
> 核心思路：利用求和检查协议实现通用 zkSNARK。
> 局限与区别：在区块链场景下，Spartan 实现零知识需要使验证者执行昂贵的群操作（如 Schnorr 证明）。HyperNova 的零知识方案利用折叠方案随机化 IVC 证明，可搭配非零知识的 Spartan 使用，避免了链上群操作。

[14] Bünz 和 Chen. Protostar: Generic Efficient Accumulation/Folding for Special Sound Protocols. **ePrint 2023** [Google Scholar](https://scholar.google.com/scholar?q=Protostar:+Generic+Efficient+Accumulation/Folding+for+Special+Sound+Protocols)
> 核心思路：为特殊可靠协议设计了另一种折叠方案，效率与 HyperNova 类似但逻辑不同。
> 局限与区别：Protostar 的验证者需要三次群标量乘法，而 HyperNova 仅需一次；但在哈希操作上 Protostar 更优。此外，Protostar 只折叠两个实例，扩展到多个实例时度数指数增长，且未提供零知识层和循环曲线实例化的详细方案。

[1] Nova: Recursive SNARKs without trusted setup. **GitHub** [Google Scholar](https://scholar.google.com/scholar?q=Nova:+Recursive+SNARKs+without+trusted+setup)
> 核心思路：Nova 的实现，采用椭圆曲线循环实例化折叠方案。
> 局限与区别：在第二个曲线上的验证电路约为 10,000 个门。HyperNova 的 CycleFold 技术将此电路规模缩减至约 1,000 个门。

[5] Ben-Sasson 等. Succinct Non-Interactive Zero Knowledge for a von Neumann Architecture. **USENIX Security 2014** [Google Scholar](https://scholar.google.com/scholar?q=Succinct+Non-Interactive+Zero+Knowledge+for+a+von+Neumann+Architecture)
> 核心思路：构建通用电路来证明 von Neumann 架构的机器执行。
> 局限与区别：证明一个程序步的成本与整个通用电路大小成正比。HyperNova 的“按需付费”成本模型只与被执行的指令电路大小成正比，而非所有指令之和。

[15] Bünz 等. Proof-carrying Data without Succinct Arguments. **CRYPTO 2021** [Google Scholar](https://scholar.google.com/scholar?q=Proof-carrying+Data+without+Succinct+Arguments)
> 核心思路：提出了折叠方案的推广，用于构建无需简洁论证的 PCD。
> 局限与区别：该工作未涉及自定义、高次约束系统。HyperNova 的多折叠方案能够自然扩展到 PCD [59]。

### 核心技术与方案

**1. 多折叠方案与求和检查协议**：HyperNova 的核心创新是提出了“多折叠方案”，它不仅折叠两个实例，而是能将任意数量的 CCS 实例和一个线性化 CCS 实例折叠成一个线性化 CCS 实例。其关键洞察在于利用求和检查协议 [37] 来避免直接对多个高次约束实例的“交叉项”进行承诺，而这正是 Sangria [41] 的瓶颈。具体地，证明者将一个 CCS 实例的约束（形如高次多项式在超立方体上求和为零）和一个运行中的线性化 CCS 实例的等式，通过随机挑战 $\gamma$ 和 $\beta$ 结合成一个关于多项式 $g(x)$ 的求和方程（公式 7）。然后通过标准求和检查协议将该求和检查简化为检查 $g(r_x') = c$，这是一个单点评估。此后，证明者必须证明该单点评估中的内部求和正确执行，这最终导出对一个新的线性化 CCS 实例的检查，该实例是原有实例的随机线性组合。该方案避免了任何交叉项承诺，证明者的加密成本仅为 O(1) 个群操作，与约束度数无关。

**2. 非均匀 IVC 与按需付费**：标准 IVC 假定每一步使用同一个函数 $F$。HyperNova 引入非均匀 IVC (NIVC)，以一个选择函数 $\varphi$ 控制每一步执行 $\ell$ 个不同函数 $F_1, \dots, F_\ell$ 中的哪一个，从而实现“按需付费”的成本：每一步的证明代价仅与由 $\varphi$ 选中的函数 $F_j$ 的电路大小成比例，与 $\ell$ 和未选中的函数无关。HyperNova 提供了一个通用编译器，利用 CCS 的多折叠方案来构造 NIVC。协议中，证明者维护一个“运行实例”列表 $\mathbf{U}$，每个元素 $\mathbf{U}[j]$ 对应于函数 $F_j$。在每一步，证明者首先使用多折叠方案将“最新实例” $\mathbf{u}_i$（代表第 $i$ 步）折叠入对应的 $\mathbf{U}[j]$ 中，然后生成一个代表“增广函数”（包括折叠验证器）的新实例 $\mathbf{u}_{i+1}$。该增广函数的规模主要取决于 $F_j$ 的大小，因为多折叠验证器（verifier）的电路仅需处理折叠操作，其内部不包括其他 $F_{k}$ 的电路或约束。因此，总代价与被执行的 $F_j$ 成比例。

**3. 零知识层**：HyperNova 提出利用折叠方案本身来实现零知识，而非使用零知识 SNARK。核心思路是“随机化”一个 NIVC 证明。证明者首先将最新实例 $\mathbf{u}$ 折叠入运行实例 $\mathbf{U}$，从而隐藏最后一次执行的指令。然后，证明者使用一个“随机化折叠方案”（如 Nova 的折叠方案）将随机采样的实例-见证对折叠入 $\mathbf{U}$，输出一个与真实分布不可区分的随机化运行实例 $\mathbf{U}'$。为了证明折叠过程正确执行而不泄露秘密输入（包括随机实例），证明者将折叠验证者的检查逻辑编码到一个盲化电路 $\text{blind}$ 中。对该电路，证明者再次应用随机化折叠方案，生成一个最终的、不泄露信息的证明。该构造在标准模型下是可证明的模拟可靠零知识，且最终证明可使用非零知识 SNARK（如 Spartan）进一步压缩，避免了在链上验证器中部署昂贵群操作的场景。该发现强调了折叠方案本身除了构造 IVC 外的新应用——随机化 NP 实例。

**4. CycleFold：椭圆曲线循环的实例化**：HyperNova 提出了 CycleFold 技术来高效地实例化一个椭圆曲线 2-循环，其核心观察是折叠方案验证者中仅需少量（HyperNova 中仅需一个）标量乘法操作需要“非本地”算术。CycleFold 将这个标量乘法操作单独“委托”到循环中的第二条曲线 $E_2$ 上。具体地，在 $E_2$ 的标量域（即 $E_1$ 的基域）上定义一个小电路 $C_{EC}$（约 1,000 个门）专门计算这个标量乘法和点加操作。主折叠方案验证者电路 $C_V$（定义在 $E_1$ 上）并不直接执行该标量乘法，而是将 $C_{EC}$ 的实例-见证作为非确定性输入，利用 Nova 的折叠方案将其折叠到一个运行实例中。这样，HyperNova 在循环中的第二个曲线上仅需要表示一个极小（约 1,000 门）的电路，这比先前方案中将整个折叠验证者表示在两个曲线上导致的 10,000 门甚至 700 万的电路规模低了 1-2 个数量级。该技术有形式化的安全性证明，可推广到其他基于折叠方案的递归论证。

### 核心公式与流程

**[CCS 约束定义]**
$$
\sum_{i=1}^{q} c_i \cdot \left(\prod_{j \in S_i} \left(\sum_{y \in \{0,1\}^{\log n}} \widetilde{M}_j(x, y) \cdot \widetilde{z}(y)\right)\right) = 0, \quad \forall x \in \{0,1\}^m
$$
> 作用：定义了 CCS 的约束方程，适用于高次度、多矩阵、多单项式的约束。

**[多折叠方案的核心多项式 g(x)]**
$$
g(x) := \left(\sum_{j \in [t], k \in [\mu]} \gamma^{(k-1)\cdot t + j} \cdot L_{j,k}(x)\right) + \left(\sum_{k \in [\nu]} \gamma^{\mu \cdot t + k} \cdot Q_k(x)\right)
$$
> 作用：通过随机挑战 $\gamma$ 和 $\beta$，将一组线性化 CCS 实例约束项 $L_{j,k}$ 与 CCS 实例的高次约束 $Q_k$ 结合为一个单一的多项式，并利用求和检查协议对该多项式进行折叠。

**[折叠后的线性化 CCS 实例]**
$$
\begin{aligned}
C &\leftarrow \sum_{k \in [\mu]} \rho^{k} \cdot \mathcal{L}_k.\phi.C + \sum_{k \in [\nu]} \rho^{\mu + k} \cdot \mathcal{C}_k.\phi.C \\
u &\leftarrow \sum_{k \in [\mu]} \rho^{k} \cdot \mathcal{L}_k.\phi.u + \sum_{k \in [\nu]} \rho^{\mu + k} \cdot 1 \\
\text{x} &\leftarrow \sum_{k \in [\mu]} \rho^{k} \cdot \mathcal{L}_k.\phi.\text{x} + \sum_{k \in [\nu]} \rho^{\mu + k} \cdot \mathcal{C}_k.\phi.\text{x} \\
v_j &\leftarrow \sum_{k \in [\mu]} \rho^{k} \cdot \sigma_{j,k} + \sum_{k \in [\nu]} \rho^{\mu + k} \cdot \theta_{j,k}
\end{aligned}
$$
> 作用：在求和检查协议之后，验证者使用随机挑战 $\rho$ 将所有输入实例（包括原始和承诺的）线性组合成一个新的线性化 CCS 实例，完成折叠。

### 实验结果

根据 Theorem 1，HyperNova 的多折叠方案对于单个 CCS 实例（$m$ 个约束，度数 $d$，$n$ 个变量，$N$ 个非零项）的复杂度为：证明者需要 $O(N + t \cdot m + q \cdot m \cdot d \cdot \log^2 d)$ 有限域运算和 O(1) 个群运算（即一次多标量乘法，MSM）；验证者需要 $O(d \cdot \log m)$ 有限域运算和 O(1) 个群运算；通信复杂度为 $O(d \cdot \log m)$ 个有限域元素。这一性能显著优于先前的 Sangria 方案，Sangria 的证明者需要 $O(n \cdot d)$ 个群运算的交叉项承诺。根据 Theorem 2，整个 HyperNova 系统证明者每一步的加密成本为单次 MSM，其大小与函数 $F_j$ 的见证大小 $n_j$ 和控制函数 $\varphi$ 的大小 $n_{\varphi}$ 之和成比例，证明了“按需付费”的线性成本。验证者电路的复杂度在线性化实例中约为主曲线上的 $1 \cdot \mathsf{G}$（一个标量乘法）和 $\log m$ 数量级的哈希操作，这远小于将完整 SNARK 验证者编码所得的电路。通过 CycleFold 技术（Theorem 4），第二个曲线上的电路规模仅为约 1,000 个乘法门，相比之下，先前做法（Nova + 循环曲线）在第二个曲线上的电路规模约为 10,000 门，因而达到了超过 10 倍的改进，使得在统一的配对友好曲线上证明循环中的第二个曲线成为现实。

### 局限性与开放问题

论文指出，它的多折叠方案假设所有 CCS 实例共享相同的结构（即相同的矩阵），但未涉及多个不同结构之间折叠的通用方法。当需要构建像 KiloNova [58] 那样的非均匀 PCD 时，需要考虑如何高效地折叠稀疏 CCS 矩阵中的承诺，这是一个未完全解决的开放问题。另外，零知识方案目前需要使用 Nova 的折叠方案作为预层，其安全基础仍需在标准模型下进行更深入的分析。最后，实现时仍然依赖 Fiat-Shamir 启发式及特定哈希函数（如 Poseidon），在可证明安全性方面存在模型假设的局限。

### 强关联论文

[4] Ben-Sasson 等. Scalable Zero Knowledge via Cycles of Elliptic Curves. **CRYPTO 2014** [Google Scholar](https://scholar.google.com/scholar?q=Scalable+Zero+Knowledge+via+Cycles+of+Elliptic+Curves)

[34] Kothapalli 等. Nova: Recursive Zero-Knowledge Arguments from Folding Schemes. **CRYPTO 2022** [Google Scholar](https://scholar.google.com/scholar?q=Nova:+Recursive+Zero-Knowledge+Arguments+from+Folding+Schemes)

[46] Setty. Spartan: Efficient and General-Purpose zkSNARKs without Trusted Setup. **CRYPTO 2020** [Google Scholar](https://scholar.google.com/scholar?q=Spartan:+Efficient+and+General-Purpose+zkSNARKs+without+Trusted+Setup)

[49] Setty 等. Customizable Constraint Systems for Succinct Arguments. **ePrint 2023** [Google Scholar](https://scholar.google.com/scholar?q=Customizable+Constraint+Systems+for+Succinct+Arguments)

[41] Mohnblatt. Sangria: A Folding Scheme for PLONK. **ePrint 2023** [Google Scholar](https://scholar.google.com/scholar?q=Sangria:+A+Folding+Scheme+for+PLONK)

[14] Bünz 和 Chen. Protostar: Generic Efficient Accumulation/Folding for Special Sound Protocols. **ePrint 2023** [Google Scholar](https://scholar.google.com/scholar?q=Protostar:+Generic+Efficient+Accumulation/Folding+for+Special+Sound+Protocols)

[1] Nova: Recursive SNARKs without trusted setup. **GitHub** [Google Scholar](https://scholar.google.com/scholar?q=Nova:+Recursive+SNARKs+without+trusted+setup)

[5] Ben-Sasson 等. Succinct Non-Interactive Zero Knowledge for a von Neumann Architecture. **USENIX Security 2014** [Google Scholar](https://scholar.google.com/scholar?q=Succinct+Non-Interactive+Zero+Knowledge+for+a+von+Neumann+Architecture)

[15] Bünz 等. Proof-carrying Data without Succinct Arguments. **CRYPTO 2021** [Google Scholar](https://scholar.google.com/scholar?q=Proof-carrying+Data+without+Succinct+Arguments)

[52] Valiant. Incrementally Verifiable Computation or Proofs of Knowledge Imply Time/Space Efficiency. **TCC 2008** [Google Scholar](https://scholar.google.com/scholar?q=Incrementally+Verifiable+Computation+or+Proofs+of+Knowledge+Imply+Time/Space+Efficiency)


## 关键词

+ 递归论证
+ 可定制约束系统
+ 折叠方案
+ 增量验证计算
+ CycleFold
+ 零知识证明