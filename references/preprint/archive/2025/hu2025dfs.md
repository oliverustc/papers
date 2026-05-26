---
title: "DFS: Delegation-friendly zkSNARK and Private Delegation of Provers"
标题简称:
论文类型: preprint
预印本简称: archive
发表年份: 2025
created: 2025-04-27 09:07:03
modified: 2025-04-27 09:08:16
---

## DFS: Delegation-friendly zkSNARK and Private Delegation of Provers

## 发表信息

+ [原文链接](https://eprint.iacr.org/2025/296)
据说已经中USENIX Security 2025

## 作者

+ [Yuncong Hu](Yuncong%20Hu.md) 
+ [Pratyush Mishra](Pratyush%20Mishra.md)
+ [Xiao Wang](Xiao%20Wang.md) 
+ Jie Xie 
+ [Kang Yang](Kang%20Yang.md)
+ Yu Yu 
+ Yuwen Zhang 

## 笔记

### 背景与动机
零知识简洁非交互式知识论证（zkSNARKs）允许证明者向验证者证明其知道满足任意 NP 关系的证据，但证明生成过程通常需要巨大的计算和内存资源，这使得资源受限的设备（如手机）难以高效生成证明。为解决此问题，现有工作提出了证明委托方案，允许证明者将生成过程外包给拥有更强计算能力的第三方。委托方案分为公开委托和私有委托两类：公开委托将证据暴露给第三方，而私有委托则通过安全多方计算（MPC）隐藏证据。私有委托对于涉及敏感用户数据的应用（如私人金融交易或身份验证）至关重要。然而，现有的私有委托方案如 zkSAAS [36] 和 EOS [23] 面临诸多瓶颈：MPC 协议存在固有的低效通信问题；资源利用效率低，无法通过并行计算有效扩展；并且所选的 zkSNARK 本身（如 Plonk [35]）包含如乘积检查等对 MPC 通信开销极大的操作。因此，设计一种能结合分布式计算和 MPC 优势、实现水平可扩展的私有委托方案是当前的核心挑战。

### 相关工作

[23] Chiesa 等. Eos: Efficient Private Delegation of zkSNARK Provers. **USENIX Security 2023** [Google Scholar](https://scholar.google.com/scholar?q=Eos%3A+Efficient+Private+Delegation+of+zkSNARK+Provers)
> 核心思路：基于加法秘密共享的私有委托方案，通过优化 Marlin 的 MPC 实现来提升性能。
> 局限与区别：未能达到声称的恶意安全性，存在选择性失败攻击漏洞；其通信开销与电路规模呈线性关系，不支持分布式并行计算。

[36] Garg 等. zk-SaaS: Zero-Knowledge SNARKs as a Service. **USENIX Security 2023** [Google Scholar](https://scholar.google.com/scholar?q=zk-SaaS%3A+Zero-Knowledge+SNARKs+as+a+Service)
> 核心思路：采用诚实多数威胁模型和打包秘密共享来加速 Plonk 的证明生成。
> 局限与区别：Plonk 的乘积检查在 MPC 中不友好，导致线性通信开销；仅达到半诚实安全，且受星型网络拓扑结构中中心节点资源的限制。

[58] Ozdemir 和 Boneh. Experimenting with Collaborative zk-SNARKs: Zero-Knowledge Proofs for Distributed Secrets. **USENIX Security 2022** [Google Scholar](https://scholar.google.com/scholar?q=Experimenting+with+Collaborative+zk-SNARKs%3A+Zero-Knowledge+Proofs+for+Distributed+Secrets)
> 核心思路：最早提出“MPC友好性”作为评估 zkSNARK 的标准，测试了 Groth16、Marlin 和 Plonk 的 MPC 性能。
> 局限与区别：通信与电路规模线性相关，且未考虑分布式计算，无法横向扩展。

[53] Liu 等. Scalable Collaborative zk-SNARK: Fully Distributed Proof Generation and Malicious Security. **IACR ePrint 2024** [Google Scholar](https://scholar.google.com/scholar?q=Scalable+Collaborative+zk-SNARK%3A+Fully+Distributed+Proof+Generation+and+Malicious+Security)
> 核心思路：基于 GKR 协议的 zkSNARK Libra，扩展了数据并行电路。
> 局限与区别：局限于分层算术电路结构，证明大小和验证时间与重复电路规模线性相关，通信仍为线性开销，对非并行电路的扩展性不佳。

### 核心技术与方案
DFS 的核心思路是针对 Rank-1 Constraint Systems (R1CS) 设计一个对委托友好的新 zkSNARK，通过协同设计 MPC 协议与 zkSNARK 协议来同时提升分布式计算和安全性。其整体框架基于 PIOP + PC 方案方法学。

**对分布式计算友好的 PIOP 设计**。
DFS 避免了使用快速傅里叶变换（FFT）和离线内存检查等需要随机内存访问、难以在分布式环境中高效实现的操作。DFS 的 PIOP 逻辑上分为两部分：第一，通过多线性求和检查证明行检查关系 $Az \circ Bz = Cz$，这涉及一个单层的多项式内积操作。第二，通过另一个求和检查验证列检查（即 $z_M = Mz$）。关键的创新在于，DFS 使用基于求和检查的查找协议 LogUp [45] 来代替 Spartan [67] 中不可扩展的离线内存检查，从而高效地证明矩阵的求值。由于矩阵数据是公开的，这部分（全息性）可以在没有 MPC 开销的情况下进行。
DFS 实例化了 PST13 多项式承诺方案 [59]，该方案基于双线性配对，其核心操作（椭圆曲线多点标量乘法，MSM）是线性且可高效并行化的。

**安全性与复杂度**。
在单机环境下，DFS 实现了线性证明时间 $O(m+n)$（$m$ 为输入规模，$n$ 为非零条目数）和对数验证时间 $O(\log m + \log n)$。其安全性来自于：行检查和列检查的证明遵循 Spartan 的安全性论证 [67]，而全息部分通过 LogUp 保证矩阵求值正确性，从而保证了整体完备性、知识可靠性和零知识。

**私有委托中的核心构造**。
DFS 的一个关键性质是其独一无二的“单层乘法门”结构。在私有委托中，这允许使用“安全抵御加法攻击”的 MPC 协议。由于 zkSNARK 的公开可验证性保证了完整性，任何在乘法输出上的加法攻击都会被最终的验证步骤检测到，因此可以省去昂贵的 MPC 乘法正确性检查，实现“免费”的恶意安全性。
在具体实现上，对于三方诚实多数设置，DFS 可以使用复制秘密共享（RSS）。由于其单层内积特性，在 RSS 下，内积计算可以完全在本地完成，无需任何 MPC 通信。对于双方恶意敌手设置，DFS 可以使用加法秘密共享（AddSS）。通过让委托方提供部分认证的 Beaver 三元组，避免了在乘法输出上引入认证，从而在保持高效的同时防止了选择性失败攻击。此外，DFS 的全息性允许在私有委托的后期进行“模式切换”，从私有委托切换到公开委托，从而利用所有节点的计算资源来加速主要计算。

**渐进复杂度**。
在三方 RSS 设置下，每个节点的计算复杂度为 $O(N_w + (m+n)/N_w)$，通信复杂度为 $O(\log m + \log n)$。在双方 AddSS 设置下，计算复杂度相同，但通信复杂度为 $O((m+n)/N_w)$（由于乘法需要线性通信）。委托方的计算和通信复杂度始终为 $O(\log m + \log n)$。

### 核心公式与流程

**[R1CS 定义]**
$$ \mathcal{R}_{\text{R1CS}} = \{( (\mathbb{F}, n, m, A, B, C), x, w ) \mid A z \circ B z = C z \} $$
> 作用：定义了 DFS 要证明的 NP 关系，其中 $z = (x \parallel 1 \parallel w)$ 是包含公共输入和私有证据的向量。

**[矩阵-向量乘积的表示]**
$$ \hat{M}(\mathbf{x}) := \sum_{\mathbf{y} \in \{0,1\}^s} \mathbf{M}(\mathbf{x}, \mathbf{y}) \mathbf{z}(\mathbf{y}) $$
> 作用：将矩阵向量乘积 $M_z$ 表示为向量 $\mathbf{z}$ 与矩阵多重线性多项式 $\mathbf{M}$ 的求和，其中 $\mathbf{x}$ 是输出索引，$\mathbf{y}$ 是输入索引。DFS 利用该式将关系证明转化为关于 $\hat{A}, \hat{B}, \hat{C}$ 的零检验。

**[行检查的批量求和检查]**
$$ r_A v_A + r_B v_B + r_C v_C \stackrel{?}{=} \sum_{\vec{y} \in \{0,1\}^m} M_{\rho_x}(\vec{y}) \mathbf{z}(\vec{y}) $$
> 作用：将验证 $\hat{A}(\rho_x), \hat{B}(\rho_x), \hat{C}(\rho_x)$ 的正确性转化为一个单一的求和检查问题，其中 $M_{\rho_x}(\vec{y})$ 是 $A, B, C$ 的带权重组合。这是私有委托中唯一涉及内积的步骤。

**[矩阵求值转换为查找]**
$$ \mathbf{M}(\mathbf{i}, \mathbf{j}) = \sum_{\mathbf{x}} \nu_M(\mathbf{x}) \, \text{eq}(\hat{r}_M(\mathbf{x}), \mathbf{i}) \, \text{eq}(\hat{c}_M(\mathbf{x}), \mathbf{j}) $$
> 作用：将矩阵逐项表达为基于其非零条目的索引函数和值函数的求和。DFS 将此求值证明归约为一个查找关系证明，即证明 $\text{eq}_{row}(\mathbf{x})$ 和 $\text{eq}_{col}(\mathbf{x})$ 是通过从已知静态表中根据索引 $\hat{r}_M(\mathbf{x})$ 和 $\hat{c}_M(\mathbf{x})$ 正确查找得到的。

**[DFS 协议简要流程]**
1.  **提交**：证明者提交多项式 $\mathbf{z}$ 的承诺。
2.  **行检查**：通过求和检查证明 $Az \circ Bz = Cz$，得到评估点 $\rho_x$。
3.  **列检查**：证明者发送 $\hat{A}(\rho_x), \hat{B}(\rho_x), \hat{C}(\rho_x)$ 的值，验证者通过求和检查验证它们的正确性，得到评估点 $\rho_y$ 和 $\rho_z$。
4.  **矩阵求值**：使用 LogUp 查找协议证明 $M(\rho_x, \rho_y)$ 的计算正确性。
5.  **承诺打开**：验证所有多项式求值的承诺。
> 作用：描述了 DFS 协议的主要交互步骤，将 R1CS 证明分解为几个可高效并行处理和进行 MPC 的子步骤。

### 实验结果
实验在配备 Intel Xeon Cascade Lake 6248 CPU 和 192GB 内存的集群上进行，带宽 100Gbps。对于私有委托，DFS 在 $2^{24}$ 约束条件下，RSS 和 AddSS 方案的总通信量分别低于 500KB 和 20GB，而 zkSAAS [36] 需要 300GB 通信。在时间上，DFS 使用 192-128 vCPU 耗时约 50 秒，zkSAAS 使用 280 vCPU 耗时约 4000 秒。相比于 EOS [23]（使用 192 vCPU 约 500 秒/$2^{24}$ 约束），DFS 在相同设置下性能更优，主要得益于 DFS 协议的线性证明时间和对数验证器开销。在公开委托中，对于 $2^{25}$ 约束，DFS 与 Pianist [52] 耗时相近（约 20 秒，512 vCPU），但 DFS 证明大小约为 17 KB，Pianist 为 2.8 KB，DFS 的验证时间在对数范围内（40-50ms），而 Pianist 为常数（3.5ms）。DFS 的优势在于其线性证明时间和更强的私有委托支持。

### 局限性与开放问题
虽然 DFS 在私有委托中取得了对数通信的突破，但其协议安全性依赖于“单层乘法门”这一特定结构，该结构源于专门设计的 PIOP。LogUp 虽然避免了随机内存访问，但其在私有委托场景下的优化依赖于在多项式计算中避免非线性的分层结构，这仅适用于 DFS 的见证无关部分。今后工作可探索如何将此框架扩展到更一般的算术电路结构，或评估其后量子安全方案（如基于编码的承诺方案）在分布式和 MPC 环境下的可行性。此外，DFS 的常数级证明大小虽短，但并非最短，是否存在能在保持线性证明时间同时实现最简常数的方案仍有探索空间。

### 强关联论文

[23] Chiesa等. Eos: Efficient Private Delegation of zkSNARK Provers. **USENIX Security 2023**

[36] Garg等. zk-SaaS: Zero-Knowledge SNARKs as a Service. **USENIX Security 2023**

[58] Ozdemir和Boneh. Experimenting with Collaborative zk-SNARKs: Zero-Knowledge Proofs for Distributed Secrets. **USENIX Security 2022**

[53] Liu等. Scalable Collaborative zk-SNARK: Fully Distributed Proof Generation and Malicious Security. **IACR ePrint 2024**

[52] Liu等. Pianist: Scalable zkRollups via Fully Distributed Zero-Knowledge Proofs. **S&P 2024**

[67] Setty. Spartan: Efficient and General-Purpose zkSNARKs Without Trusted Setup. **CRYPTO 2020**

[22] Chiesa等. Marlin: Preprocessing zkSNARKs with Universal and Updatable SRS. **EUROCRYPT 2020**

[35] Gabizon等. PLONK: Permutations over Lagrange-bases for Oecumenical Noninteractive arguments of Knowledge. **IACR ePrint 2019**

[45] Haböck. Multivariate lookups based on logarithmic derivatives. **IACR ePrint 2022**

[59] Papamanthou等. Signatures of Correct Computation. **TCC 2013**


## 关键词

+ DFS委托友好zkSNARK
+ 私有委托多方计算MPC
+ 零通信开销恶意安全委托
+ 线性证明者对数验证成本
+ zkSNARK协同设计分布式计算