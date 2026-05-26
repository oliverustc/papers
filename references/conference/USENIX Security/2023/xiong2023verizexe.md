---
title: "VeriZexe: Decentralized Private Computation with Universal Setup"
标题简称:
论文类型: conference
会议简称: USENIX Security
发表年份: 2023

modified: 2025-04-21 11:54:04
created: 2025-04-07 17:01:06
---

## VeriZexe: Decentralized Private Computation with Universal Setup

## 发表信息

+ [原文链接](https://www.usenix.org/conference/usenixsecurity23/presentation/xiong)

## 作者

+ [Alex Luoyuan Xiong](Alex%20Luoyuan%20Xiong.md)
+ [Binyi Chen](Binyi%20Chen.md)
+ [Zhenfei Zhang](Zhenfei%20Zhang.md)
+ [Benedikt Bünz](Benedikt%20Bünz.md)
+ [Ben Fisch](Ben%20Fisch.md)
+ Fernando Krell
+ Philippe Camacho

## 笔记

### 背景与动机
分布式账本技术，如比特币和以太坊，通过状态机复制实现了容错性，但计算和状态对全网节点透明，导致严重的隐私问题。为应对这一挑战，Bowe 等人提出了去中心化私有计算（DPC）原语，并给出了 ZEXE 的具体构造，允许用户离线执行任意计算，仅向网络提交一个简洁的零知识证明来验证计算正确性，从而同时实现数据隐私和函数隐私。然而，ZEXE 的每一个应用程序都需要一次独立且昂贵的可信设置，这在大规模部署中几乎不可行。虽然使用通用 SNARK（如 Marlin）可以免除每个应用的单独设置，但基于通用 SNARK 的替代方案性能显著下降，其交易生成速度比原始 ZEXE 慢一个数量级。因此，核心问题是如何在支持通用设置的前提下，不牺牲交易生成的效率。VeriZexe 正是为了解决这一难题而提出，旨在通过一系列高效的电路优化技术，将基于通用 SNARK 的 DPC 方案性能提升到与原始 ZEXE 相当的水平。

### 相关工作

[6] Ben-Sasson 等. Zerocash: Decentralized anonymous payments from bitcoin. **IEEE S&P 2014** [Google Scholar](https://scholar.google.com/scholar?q=Zerocash+Decentralized+anonymous+payments+from+bitcoin)
> 核心思路：提出了一个基于零知识证明的隐私支付系统，实现用户匿名和金额保密。
> 局限与区别：功能固定，仅限于支付场景，不具备函数隐私，无法隐藏执行的智能合约逻辑。

[12] Bowe 等. ZEXE: Enabling decentralized private computation. **IEEE S&P 2020** [Google Scholar](https://scholar.google.com/scholar?q=ZEXE+Enabling+decentralized+private+computation)
> 核心思路：提出了DPC原始定义，通过将计算离线执行并提交证明来实现数据与函数隐私。
> 局限与区别：依赖非通用SNARK（如GM17），每个谓词需要单独的可信设置，实用性受限。

[20] Chiesa 等. Marlin: Preprocessing zkSNARKs with universal and updatable SRS. **EUROCRYPT 2020** [Google Scholar](https://scholar.google.com/scholar?q=Marlin+Preprocessing+zkSNARKs+with+universal+and+updatable+SRS)
> 核心思路：提出了一个具有通用且可更新SRS的预处理zkSNARK。
> 局限与区别：ZEXE的替代方案使用Marlin，但因验证逻辑复杂导致性能远低于原始方案，VeriZexe在此基础上进一步优化。

[27] Gabizon 等. PLONK: Permutations over Lagrange-bases for Oecumenical Noninteractive Arguments of Knowledge. **ePrint 2019** [Google Scholar](https://scholar.google.com/scholar?q=PLONK+Permutations+over+Lagrange-bases+for+Oecumenical+Noninteractive+Arguments+of+Knowledge)
> 核心思路：提出了一种高效的通用SNARK，支持可定制的门电路。
> 局限与区别：VeriZexe基于PLONK的变体进行构建，并设计了TURBOPLONK和ULTRAPLONK约束系统来优化特定操作。

[13] Bowe 等. Recursive proof composition without a trusted setup. **ePrint 2019** [Google Scholar](https://scholar.google.com/scholar?q=Recursive+proof+composition+without+a+trusted+setup)
> 核心思路：提出了利用积累方案实现递归证明组合（Halo），避免了可信设置。
> 局限与区别：VeriZexe借鉴了其积累方案的思想，但将其应用于特定场景，将昂贵的配对检查从电路移至链上验证者。

[26] Gabizon 等. plookup: A simplified polynomial protocol for lookup tables. **ePrint 2020** [Google Scholar](https://scholar.google.com/scholar?q=plookup+A+simplified+polynomial+protocol+for+lookup+tables)
> 核心思路：提出了高效的多项式IOP协议用于证明查询值存在于查找表中。
> 局限与区别：原文主要关注预处理表，VeriZexe将其推广至在线查找表，用于变基MSM优化。

[33] Kate 等. Constant-size commitments to polynomials and their applications. **ASIACRYPT 2010** [Google Scholar](https://scholar.google.com/scholar?q=Constant-size+commitments+to+polynomials+and+their+applications)
> 核心思路：提出了KZG多项式承诺方案，具有常数大小的承诺和证明。
> 局限与区别：KZG方案需要配对操作，VeriZexe通过积累方案将其从电路内移除，减少电路复杂度。

[16] Bünz 等. Proof-carrying data from accumulation schemes. **ePrint 2020** [Google Scholar](https://scholar.google.com/scholar?q=Proof-carrying+data+from+accumulation+schemes)
> 核心思路：形式化并泛化了积累方案（AC）的概念，用于构建证明携带数据系统。
> 局限与区别：VeriZexe应用了其理论，并在此基础上为ZEXE的特定上下文优化了外电路。

### 核心技术与方案
VeriZexe 的整体框架基于 ZEXE 的 DPC 模型，其核心创新在于一系列优化技术，旨在构建一个轻量级的外电路，使其能够高效地验证由通用 SNARK 生成的内层谓词证明。

**1. 轻量级验证电路与积累方案**：ZEXE 的原始构造中，外电路需要内嵌一个完整的 SNARK 验证器来验证内层谓词证明。这导致外电路极其庞大，因为它必须执行昂贵的配对操作。VeriZexe 受 Halo [13] 启发，采用积累方案（Accumulation Scheme，AS）将外电路中的这些昂贵操作剥离。具体而言，对于基于 KZG [33] 等配对型多项式承诺方案的 SNARK，其验证的最终步骤是产生两个 G1 点用于配对检查。VeriZexe 的电路不执行此配对，而是将这两个 G1 点作为公开输入输出。为了确保函数隐私，这两个点会被随机掩码，但掩码方式保证最终的配对检查结果不变。真实的配对检查被延迟到链上验证者那里执行。这样，外电路仅需实现一个轻量级的积累验证器逻辑，而非完整的 SNARK 验证器，从而大幅降低了电路的约束数量。

**2. 实例合并**：对于一个 m 输入、m 输出的事务，原始方案需要对外电路验证 $2m$ 个谓词证明（m 个死亡谓词，m 个出生谓词）。VeriZexe 利用 PLONK 等 SNARK 的代数预处理特性和多项式承诺的加法同态性，将一对死亡和出生谓词合并成一个证明。具体做法是，在预处理阶段，将死亡和出生谓词电路分别填充到大小为 2n（n 为原始谓词大小），其中死亡谓词左填充（前 n 个门为哑元），出生谓词右填充（后 n 个门为哑元）。合并时，两个填充电路的证明密钥和验证密钥可以直接通过多项式加法得到（多项式承诺的加法同态性保证了这一点）。通过合并 $2m$ 个证明为 m 个证明，外电路复杂度从 $2m \cdot C_n$ 降低至 $m \cdot C_{2n}$。由于 $C_{2n} \approx C_n + \delta$，且 $\delta$ 远小于 $C_n$，因此净收益巨大。

**3. 证明批处理**：VeriZexe 提出了一个通用的编译器，将公共硬币的 PIOP 和多项式承诺方案相结合，以支持批量证明。核心思想是在多轮交互中，验证者为所有 $\ell$ 个实例生成相同的随机挑战，而非每个实例单独生成。在最终查询阶段，验证者生成一个统一的查询集，证明者使用 PCS 的批量打开功能来证明所有多项式响应的一致性。这比独立运行 $\ell$ 个证明实例要高效得多，因为它减少了通信复杂度，并摊薄了验证计算成本，从而进一步降低了外电路的复杂度。

**4. 变基多标量乘法（MSM）与在线查找表**：外电路验证需要大量的变基 MSM 操作。VeriZexe 设计了一种基于 Pippenger 算法的优化电路。Pippenger 算法将一个 b 位的 MSM 分解为 $b/c$ 个 c 位的 MSM。对于每个 c 位 MSM，通过构建一个在线查找表来避免昂贵的椭圆曲线群运算。这个表存储了当前基点与所有 $2^c - 1$ 种可能的标量值相乘的结果点。由于基点是动态的（来自验证密钥中的承诺），该表必须在证明阶段“在线”构建。关键的观察是，PLOOKUP [26] 的协议对于在线构建的查找表同样有效，因为证明者会先提交查询表和查找表的值，然后才对它们进行一致性检查。优化后的 MSM 电路在 256 位、128 个基点的场景下，仅需约 34,516 个门，而朴素实现需要约 230,000 个门，效率提升 6.5 倍以上。

**5. 非原生域多项式求值**：内层证明运行在 BLS12-377 的标量域 $\mathbb{F}_r$ 上，而外层电路运行在 BW6-761 的标量域 $\mathbb{F}_p$ 上。因此，外层电路必须模拟 $\mathbb{F}_r$ 上的运算。VeriZexe 设计了高效的模乘和模加 gadget。模乘运算通过将 $\mathbb{F}_p$ 元素拆分为双肢（limb）表示，并引入进位变量来确保中间结果不溢出 $\mathbb{F}_q$，从而用一系列约束等价地表示模 $p$ 的乘法关系。模加运算也类似，通过引入一个商数变量 $w$ 来约束整数等式。这些 gadget 利用了 ULTRAPLONK 约束系统中高效的查找论证进行范围检查。在 BLS12-377 和 BW6-761 的配置下，模乘 gadget 仅需约 23 个约束，模加 gadget 仅需 $\lceil N/4 \rceil + 6$ 个约束（N 为加数数量）。

**6. SNARK 友好对称原语**：为降低约束非代数操作（如 SHA256）的电路成本，VeriZexe 大量采用 Rescue [2] 哈希函数。Rescue 主要依靠域上的代数操作（如幂运算）工作，非常适合在 SNARK 电路中进行约束。VeriZexe 基于 Rescue 构建了伪随机函数（PRF）、哈希函数（CRH）和承诺方案，并设计了 TURBOPLONK 约束系统，通过自定义的高次门（如五次方门）来高效地约束 Rescue 操作。对于 Fiat-Shamir 变换中的挑战派生，使用基于 Rescue 的 Sponge 结构，使得挑战生成在电路内非常廉价。

### 核心公式与流程

**[变基 MSM 优化电路（图 4）]**
> 作用：描述了利用在线查找表实现变基多标量乘法的具体步骤，将昂贵的群运算替换为表查找。

1. For $i \in \{ 1 \ldots n \} \colon$  
   (a) Compute $(2 \cdot P_i, \ldots, (2^c - 1) \cdot P_i)$ using repeated point addition from $P_i$.  
   (b) Create online lookup table: $\mathcal{T}_i = [(0, 0_\mathbb{G}), (1, P_i), (2, 2 \cdot P_i), ..., (2^c - 1, (2^c - 1) \cdot P_i)]$.  
   (c) Decompose $s_i$ into m chunks of c-bit value $[s_{i,0}, \ldots, s_{i,m-1}]$, such that $s_i = \sum_{j=0}^{m-1} s_{i,j} \cdot 2^{cj}$.  

2. For $j = \{ 0 \ldots m - 1 \} \colon$  
   (a) For $i = \{ 0 \ldots n \} \colon$  
      i. Create a point variable $Q_{i,j}$ for the value $s_{i,j} \cdot P_i$.  
      ii. Add an entry to query table $ (s_{i,j}, Q_{i,j}) $ (lookup argument will check if $(s_{i,j}, Q_{i,j}) \in \mathcal{T}_i$).  
   (b) Compute window sum: $\text{wsum}_j = \sum_{i \in [n]} Q_{i,j}$.  

3. Compute $Q = \sum_{j=0}^{m-1} \text{wsum}_j \cdot 2^{cj}$.

**[模乘 gadget（图 6）]**
> 作用：定义了在域 $\mathbb{F}_q$ 的电路中模拟域 $\mathbb{F}_p$ 上乘法 $x \cdot y = z \pmod{p}$ 的约束条件。

Input: $(x_0, x_1), (y_0, y_1) \in [0, 2^m)^2$ such that $x = x_0 + 2^m \cdot x_1 \in \mathbb{F}_p, y = y_0 + 2^m \cdot y_1 \in \mathbb{F}_p$  
Witness: $(w_0, w_1), (z_0, z_1)$  
Relation: $(x_0 + 2^m \cdot x_1) \cdot (y_0 + 2^m \cdot y_1) = z_0 + 2^m \cdot z_1 + (w_0 + 2^m \cdot w_1) \cdot (p_0 + 2^m \cdot p_1)$ over integers  
Circuit:  
1. Range check $w_0, w_1, z_0, z_1 \in [0, 2^m)$.  
2. Compute carrier $c_0'$ and $c_0 = c_0' + 2^m$, range check $c_0 \in [0, 2^{m+k})$ and constrain $z_0 + w_0 \cdot p_0 = x_0 \cdot y_0 + 2^m \cdot (c_0 - 2^m)$.  
3. Compute carrier $c_1'$ and $c_1 = c_1' + 2^{m+1}$, range check $c_1 \in [0, 2^{m+k})$ and constrain $z_1 + w_0 \cdot p_1 + w_1 \cdot p_0 + (c_0 - 2^m) = x_0 \cdot y_1 + x_1 \cdot y_0 + 2^m \cdot (c_1 - 2^{m+1})$.  
4. Constrain $w_1 \cdot p_1 + (c_1 - 2^{m+1}) = x_1 \cdot y_1$.

### 实验结果
实验在 AWS EC2 实例上进行，配备 64 核 AMD EPYC 7R13 处理器 (2.65 GHz) 和 128 GB RAM。主要对比基线是 SnarkVM testnet-2（Aleo 团队维护的 DPC 实现）以及原始 ZEXE。实验结果表明，对于 2×2 的交易，VeriZexe 的交易生成时间为 16.9 秒，相比 SnarkVM 的 151.4 秒提升了约 9 倍；内存使用从 22.81 GB 降至 6.61 GB，提升了约 3.4 倍。在系统设置（Setup）阶段，VeriZexe 仅需 11.8 秒，远快于 SnarkVM 的 176.8 秒，且 SRS 大小仅为 33.1 MB，而 SnarkVM 需要 5.25 GB。验证时间方面，VeriZexe 为 18 毫秒，与 SnarkVM 的 15 毫秒相当。证明大小方面，VeriZexe 为 4.14 KB，高于 SnarkVM 的 0.482 KB，但验证时间恒定，不随交易规模增长。微基准测试显示，其 PLONK 验证器 gadget 仅需约 21k 个 ULTRAPLONK 约束，而变基 MSM 电路在 128 个基点时仅需约 36k 约束，远低于朴素实现的 239k 约束。在不同硬件环境（手机、笔记本、服务器）的测试中，2×2 交易的外层证明生成时间分别约为 270 秒、32.2 秒和 12.7 秒，显示出方案在不同资源设备上的可适应性。

### 局限性与开放问题
VeriZexe 方案的安全性依赖于 Rescue 置换作为一个安全的伪随机置换以及 Rescue 哈希作为随机预言机的假设，这些基于相对较新的低算术复杂度密码学原语，其安全性尚未经过充分的时间检验。此外，ULTRAPLONK 约束系统的知识可靠性误差与门的最大度数 (6) 及门数量成正比，虽然经分析实际影响可忽略，但这引入了额外的理论复杂性。方案在性能与安全性之间的权衡依赖于所选的椭圆曲线对（BLS12-377和BW6-761），未来工作在更通用曲线上的适配性也值得探索。

### 强关联论文

[12] Bowe 等. ZEXE: Enabling decentralized private computation. **IEEE S&P 2020** [Google Scholar](https://scholar.google.com/scholar?q=ZEXE+Enabling+decentralized+private+computation)

[13] Bowe 等. Recursive proof composition without a trusted setup. **ePrint 2019** [Google Scholar](https://scholar.google.com/scholar?q=Recursive+proof+composition+without+a+trusted+setup)

[20] Chiesa 等. Marlin: Preprocessing zkSNARKs with universal and updatable SRS. **EUROCRYPT 2020** [Google Scholar](https://scholar.google.com/scholar?q=Marlin+Preprocessing+zkSNARKs+with+universal+and+updatable+SRS)

[26] Gabizon 等. plookup: A simplified polynomial protocol for lookup tables. **ePrint 2020** [Google Scholar](https://scholar.google.com/scholar?q=plookup+A+simplified+polynomial+protocol+for+lookup+tables)

[27] Gabizon 等. PLONK: Permutations over Lagrange-bases for Oecumenical Noninteractive Arguments of Knowledge. **ePrint 2019** [Google Scholar](https://scholar.google.com/scholar?q=PLONK+Permutations+over+Lagrange-bases+for+Oecumenical+Noninteractive+Arguments+of+Knowledge)

[16] Bünz 等. Proof-carrying data from accumulation schemes. **ePrint 2020** [Google Scholar](https://scholar.google.com/scholar?q=Proof-carrying+data+from+accumulation+schemes)

[33] Kate 等. Constant-size commitments to polynomials and their applications. **ASIACRYPT 2010** [Google Scholar](https://scholar.google.com/scholar?q=Constant-size+commitments+to+polynomials+and+their+applications)

[6] Ben-Sasson 等. Zerocash: Decentralized anonymous payments from bitcoin. **IEEE S&P 2014** [Google Scholar](https://scholar.google.com/scholar?q=Zerocash+Decentralized+anonymous+payments+from+bitcoin)

[35] Kosba 等. Hawk: The blockchain model of cryptography and privacy-preserving smart contracts. **IEEE S&P 2016** [Google Scholar](https://scholar.google.com/scholar?q=Hawk+The+blockchain+model+of+cryptography+and+privacy-preserving+smart+contracts)

[14] Bünz 等. Zether: Towards privacy in a smart contract world. **FC 2020** [Google Scholar](https://scholar.google.com/scholar?q=Zether+Towards+privacy+in+a+smart+contract+world)


## 关键词

+ VeriZexe去中心化私有计算
+ Zexe通用设置DPC
+ Plonk约束系统电路优化
+ 链下私有计算区块链
+ 多标量乘法模运算组件
+ 通用受信设置替代方案
