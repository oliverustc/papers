---
title: "Scalable multi-party computation for zk-SNARK parameters in the random beacon model"
标题简称:
论文类型: preprint
预印本简称: archive
发表年份: 2017
created: 2025-06-10 02:36:19
modified: 2025-06-10 02:39:41
---

## Scalable multi-party computation for zk-SNARK parameters in the random beacon model

## 发表信息

+ [原文链接](https://eprint.iacr.org/2017/1050)

## 作者

+ [Sean Bowe](Sean%20Bowe.md)
+ [Ariel Gabizon](Ariel%20Gabizon.md)
+ [Ian Miers](Ian%20Miers.md)
## 笔记

### 背景与动机
zk-SNARK 实现简洁的公开可验证零知识证明，但其安全性依赖于一个可信的公共参考字符串 (CRS)。一旦 CRS 生成过程被攻破，证明就能被伪造，在 Zcash 等加密货币中可能导致数十亿美元的盗窃。此前由 Ben-Sasson 等人 [9] 设计的 MPC 协议虽能安全生成 CRS，但需要一个“预承诺阶段”，要求参与者预先选定、提前承诺秘密值并在整个协议期间保护这些秘密，严格限制了可扩展性。该协议仅能支持个位数参与者，参与者需保持在线数日 [37]，这不但增加了攻击面，也带来了严重的后勤挑战。对于区块链这类高价值应用，假设一百或一千个参与者中有一个诚实远比假设六或十个参与者中有一个诚实更具说服力。为此，本文引入随机信标模型，旨在构建一个无需预承诺、支持成百上千动态参与者的可扩展 MPC 协议。

### 相关工作

[9] Ben-Sasson等. Secure Sampling of Public Parameters for Succinct Zero Knowledge Proofs. **SP 2015** [Google Scholar](https://scholar.google.com/scholar?q=Secure+Sampling+of+Public+Parameters+for+Succinct+Zero+Knowledge+Proofs)
> 核心思路：设计多轮交互的MPC协议，参与者通过预承诺阶段绑定其秘密值，并利用零知识证明来防止恶意适配。
> 局限与区别：该协议强制要求参与者预承诺、必须在线且数量受限。本文通过引入随机信标去除了预承诺阶段，实现了参与者可交换的开放协议。

[16] Bowe等. A Multi-party Protocol for Constructing the Public Parameters of the Pinocchio zk-SNARK. **ePrint 2017** [Google Scholar](https://scholar.google.com/scholar?q=A+Multi-party+Protocol+for+Constructing+the+Public+Parameters+of+the+Pinocchio+zk-SNARK)
> 核心思路：对[9]进行实现和适配，用于 Zcash 的 CRS 生成，并给出了具体的协议和验证方法。
> 局限与区别：该协议同样存在预承诺要求，且参与者需保护秘密数日。本文方案则允许参与者随时加入或退出，无需长时间持有秘密。

[27] Groth. On the Size of Pairing-Based Non-Interactive Arguments. **EUROCRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=On+the+Size+of+Pairing-Based+Non-Interactive+Arguments)
> 核心思路：提出当前最高效的 zk-SNARK，证明仅含 3 个群元素，验证只需 3 个配对。
> 局限与区别：Groth 的 CRS 在信任设置上同样面临挑战。本文通过扩展该 CRS，设计了两阶段 MPC 协议来安全地生成它。

[23] Gennaro等. Quadratic Span Programs and Succinct NIZKs without PCPs. **EUROCRYPT 2013** [Google Scholar](https://scholar.google.com/scholar?q=Quadratic+Span+Programs+and+Succinct+NIZKs+without+PCPs)
> 核心思路：提出二次算术程序 (QAP) 的概念，为 zk-SNARK 提供了高效的代数基础。
> 局限与区别：该工作给出了 QAP 的理论模型，但未涉及 CRS 的安全分布式生成。本文基于此模型调用 Groth 的 NILP，并为其构造 MPC 协议。

[7] Barreto等. Constructing Elliptic Curves with Prescribed Embedding Degrees. **ePrint 2002** [Google Scholar](https://scholar.google.com/scholar?q=Constructing+Elliptic+Curves+with+Prescribed+Embedding+Degrees)
> 核心思路：提出 BLS 曲线族，能够构造特定嵌入次数的配对友好椭圆曲线。
> 局限与区别：本文采用了 BLS12-381 曲线，该曲线属于 BLS 曲线族的一个子家族，相比之前广泛使用的 BN 曲线，在实现 128 比特安全时具有更优的性能。

### 核心技术与方案

本文提出了一种称为“参与者可交换多方计算 (px-MPC)”的新型协议，通过随机信标移除预承诺阶段来提升 CRS 生成的可扩展性。核心思路是，在每一轮协议尾声，利用一个公开的随机信标值去最终随机化所有参与者的累积乘积。即使最后一个恶意参与者自适应地选择其秘密值，也无法控制最终结果，因为信标将引入一个独立的随机因子。

协议流程如下：一个深度为 $d$ 的电路由交替的乘/除层 $C_1,...,C_d$ 和线性组合层 $L_1,...,L_d$ 组成。每轮处理一层 $C_\ell$，包含 $N$ 个玩家（不同轮之间玩家身份可不同）。玩家 $j$ 对其在层 $\ell$ 的输入向量 $\mathbf{x}_j^\ell$ 执行以下步骤：首先广播每个输入 $x \in \mathbf{x}_j^\ell$ 的承诺 $[x]_1$ 及其知识证明 $y_{x,j} = \mathsf{POK}(x_j, \mathsf{transcript}_{\ell, j-1})$；然后针对层内每个门 $\mathsf{g}$，播放其累积输出 $[\mathsf{g}]^j = M_\mathsf{g}(\mathbf{x}_j^\ell) \cdot [\mathsf{g}]^{j-1}$。在 $N$ 个玩家之后，协议协调者从随机信标 $\mathsf{RB}$ 获取一个随机向量 $\mathbf{x}^{\prime\ell}$，并计算最终输出 $[\mathsf{g}] = M_\mathsf{g}(\mathbf{x}^{\prime\ell}) \cdot [\mathsf{g}]^N$。由于最终结果中的秘密 $s^\ell$ 为 $\mathbf{x}_1^\ell \cdots \mathbf{x}_N^\ell \cdot \mathbf{x}^{\prime\ell}$，其中 $\mathbf{x}^{\prime\ell}$ 在玩家 $N$ 提交后才能获知且独立于它，因此能防止自适应攻击。

安全性证明基于知识指数假设 (KEA) 和随机信标模型。定理 5.1 指出，对于任意高效预言机电路 $\mathcal{A}$，若随机信标对 $\mathcal{A}$ 是 $u$-co-resistant，则存在一个高效的 $\mathcal{B}$，使得对任意谓词 $P$，有 $ \Pr(P(\mathbf{C}_S, \mathcal{B}(\mathbf{C}_S)) = \mathsf{acc}) \geq 2^{-ud} \cdot \mathrm{adv}_{\mathcal{A}, P} - \mathrm{negl}(\lambda)$。证明通过构造模拟器 $\mathcal{B}$ 实现：$\mathcal{B}$ 拿到诚实生成的CRS $\mathbf{C}_S$ 后，在协议内部以盲打方式选择合适的玩家输入，使得协议最终输出恰好为 $\mathbf{C}_S$。若攻击者 $\mathcal{A}$ 能利用协议输出伪造证明，则 $\mathcal{B}$ 就得到对 $\mathbf{C}_S$ 的伪造，从而将 $\mathcal{A}$ 的成功概率因子 $2^{-ud}$ 下归约到标准模型的安全。

本文具体化了 Groth 的 zk-SNARK [27] 的 CRS 生成，将其深度降低为 2。第一阶段（C1）以 $\{x, \alpha, \beta\}$ 为输入，输出幂序列 $\{x^i\}, \{\alpha x^i\}, \{\beta x^i\}$，本质上是乘/除层。第一阶段后的线性组合层（L1）计算 $x^i \cdot t(x)$ 和 $u_i(x), v_i(x), w_i(x)$ 的线性组合。第二阶段（C2）以 $\{\delta\}$ 为输入，通过除法计算 $\{x^i t(x)/\delta\}$ 和 $\{\frac{\beta u_i + \alpha v_i + w_i}{\delta}\}$。协议验证者使用配对检查保证每步正确性，同时检查知识证明提取出的秘密值与广播值一致。

### 核心公式与流程

**SameRatio 协议 (Algorithm 1)**
$$\mathsf{SameRatio}((A,B), (C,D)) = \mathsf{acc} \iff e(A,D) = e(B,C)$$
> 功能：利用双线性配对检查是否存在 $s \in \mathbb{F}_p^*$ 使得 $B = s \cdot A$ 且 $D = s \cdot C$，确保两对元素拥有相同的离散对数比例。

**Knowledge of Exponent Assumption (KEA, Definition 3.3)**
$$ \Pr[x \neq [\alpha]_1 \land \mathsf{SameRatio}((g_1, x), (r, y)) : x, y \leftarrow \mathcal{A}(z, r)] = \mathrm{negl}(\lambda) $$
> 功能：从 $\mathbb{G}_1$ 中的一个元素 $x$ 和 $\mathbb{G}_2$ 中的一个元素 $y$（与给定 $r$ 保持相同比例）恢复出标量 $\alpha$，防止攻击者生成无法提取的承诺。

**CheckPOK 协议 (Algorithm 4)**
$$ \mathsf{CheckPOK}(a, v, b) = \mathsf{SameRatio}((g_1, a), (\mathcal{R}(a, v), b)) $$
> 功能：验证知识证明，通过检查 $a$ 与 $b$ 是否满足与随机预言机回答 $\mathcal{R}(a, v)$ 相同的比例关系，从而防止重放攻击并提取秘密值。

**第一阶段 (Round 1) 乘法操作**
$$ [x^i]^{j} := x_j^i \cdot [x^i]^{j-1}, \quad [\alpha x^i]^{j} := \alpha_j x_j^i \cdot [\alpha x^i]^{j-1}, \quad [\beta x^i]^{j} := \beta_j x_j^i \cdot [\beta x^i]^{j-1} $$
> 功能：玩家 $j$ 将自己的秘密值累乘到前期累积的幂次和 MAC 元素上，逐步构建出以 $x = \prod x_k$ 为底数的各幂次幂。

**第二阶段 (Round 2) 除法操作**
$$ [\delta]^j := [\delta]^{j-1} / \delta_j, \quad [K_i]^j := [K_i]^{j-1} / \delta_j, \quad [H_i]^j := [H_i]^{j-1} / \delta_j $$
> 功能：玩家 $j$ 用自己的秘密值 $\delta_j$ 逐步从目标元素中“除掉”，最终达到除以 $\delta = \prod \delta_k$ 的效果，避免不良选取。

### 实验结果
实验在 Intel Core i7-3770S CPU @ 3.10GHz，32GB RAM 的台式机上运行，使用 Rust 语言实现。由于协议性能与参与者数量无关，仅需测量单用户单次计算的耗时与带宽。对于 $2^{21}$ 个乘法门的电路（对应约 60 次 SHA256 计算，也是Zcash现有规模），第一阶段用户输入下载为 1.13GB、上传为 0.56GB，计算耗时约 15 分钟；第二阶段下载为 0.37GB、上传为 0.19GB，计算更少。核间计算（即线性组合层，由协调者完成）需要额外策略，但无需用户参与。相比先前现实世界对 [16] 的执行，本文每用户计算时间有了显著改善（$\mathbf{X}$ 倍），且避免了预承诺导致的空闲时间。该曲线 BLS12-381 比先前 BN256曲线计算更复杂，但协议和实现优化抵消了这一开销。

### 局限性与开放问题
当前协议假设一个同步网络，且使用随机信标作为关键安全假设，虽然信标允许对手有限影响，但仍需可信或足够强的随机源。协议的验证阶段需要协调者重新计算所有操作，对大规模电路的验证计算负担可能较重（数十分钟）。此外，协议目前仅针对 Groth 的 zk-SNARK 实现，是否可以适配其他证明系统尚需研究。针对随机信标在去中心化世界中的具体实现（如可验证延迟函数 [18]）的进一步形式化建模也是开放方向。

### 强关联论文

[9] Ben-Sasson等. Secure Sampling of Public Parameters for Succinct Zero Knowledge Proofs. **SP 2015** [Google Scholar](https://scholar.google.com/scholar?q=Secure+Sampling+of+Public+Parameters+for+Succinct+Zero+Knowledge+Proofs)

[16] Bowe等. A Multi-party Protocol for Constructing the Public Parameters of the Pinocchio zk-SNARK. **ePrint 2017** [Google Scholar](https://scholar.google.com/scholar?q=A+Multi-party+Protocol+for+Constructing+the+Public+Parameters+of+the+Pinocchio+zk-SNARK)

[27] Groth. On the Size of Pairing-Based Non-Interactive Arguments. **EUROCRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=On+the+Size+of+Pairing-Based+Non-Interactive+Arguments)

[23] Gennaro等. Quadratic Span Programs and Succinct NIZKs without PCPs. **EUROCRYPT 2013** [Google Scholar](https://scholar.google.com/scholar?q=Quadratic+Span+Programs+and+Succinct+NIZKs+without+PCPs)

[11] Ben-Sasson等. Zerocash: Decentralized Anonymous Payments from Bitcoin. **SP 2014** [Google Scholar](https://scholar.google.com/scholar?q=Zerocash:+Decentralized+Anonymous+Payments+from+Bitcoin)

[8] Barreto等. Pairing-Friendly Elliptic Curves of Prime Order. **ePrint 2005** [Google Scholar](https://scholar.google.com/scholar?q=Pairing-Friendly+Elliptic+Curves+of+Prime+Order)

[7] Barreto等. Constructing Elliptic Curves with Prescribed Embedding Degrees. **ePrint 2002** [Google Scholar](https://scholar.google.com/scholar?q=Constructing+Elliptic+Curves+with+Prescribed+Embedding+Degrees)

[13] Ben-Sasson等. SNARKs for C: Verifying Program Executions Succinctly and in Zero Knowledge. **CRYPTO 2013** [Google Scholar](https://scholar.google.com/scholar?q=SNARKs+for+C:+Verifying+Program+Executions+Succinctly+and+in+Zero+Knowledge)

[36] Parno等. Pinocchio: Nearly Practical Verifiable Computation. **SP 2013** [Google Scholar](https://scholar.google.com/scholar?q=Pinocchio:+Nearly+Practical+Verifiable+Computation)

[30] Kim等. Extended Tower Number Field Sieve: A New Complexity for the Medium Prime Case. **ePrint 2015** [Google Scholar](https://scholar.google.com/scholar?q=Extended+Tower+Number+Field+Sieve:+A+New+Complexity+for+the+Medium+Prime+Case)


## 关键词

+ zk-SNARK参数可扩展多方计算
+ 随机信标模型安全协议
+ 公共参考字符串CRS生成
+ Groth SNARK扩展两轮协议
+ 配对友好椭圆曲线安全优化
+ 预提交轮次消除设计