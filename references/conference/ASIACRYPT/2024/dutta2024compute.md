---
title: "Compute, but verify: Efficient multiparty computation over authenticated inputs"
标题简称:
论文类型: conference
会议简称: ASIACRYPT
发表年份: 2024
---

## Compute, but verify: Efficient multiparty computation over authenticated inputs

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-981-96-0938-3_5)

## 作者

+ Moumita Dutta 
+ [Chaya Ganesh](Chaya%20Ganesh.md)
+ Sikhar Patranabis 
+ Nitin Singh 


## 笔记

### 背景与动机
传统安全多方计算允许互不信任的参与方联合计算函数，保证输入隐私与输出正确性，但不对输入本身如何选取提供任何保证。许多现实应用——如计算行业平均薪资时雇员需提交经过雇主签名的工资单，或医院联合分析经监管机构签名的患者数据——要求输入必须是可验证的可信数据，即输入已由认证机构签名。直接的做法是将签名验证编码为待计算的算术电路，但这会引入大量哈希与代数运算，导致电路膨胀至无法接受。另一种思路是让认证机构签名对输入的承诺而非输入本身，再由参与方证明输入与该承诺一致，但这破坏了不可关联性：同一输入在不同协议中复用时会通过已签名的承诺被追踪。已有的认证秘密共享方案 [2,11] 只给共享本身提供了静态保证，并未防止恶意方在实际 MPC 执行中使用与认证不同的输入。本文旨在填补这一空白：提出一个通用编译器，将任何基于线性秘密共享的诚实多数 MPC 协议升级为具有输入认证能力的协议，且不要求将认证关系表示为电路、不引入高昂的开销、同时保持不可关联性。

### 相关工作

[2] Aranha, Dalskov, Escudero, Orlandi. Improved Threshold Signatures, Proactive Secret Sharing, and Input Certification from LSS Isomorphisms. **LATINCRYPT 2021**
> 核心思路：利用线性秘密共享同构实现输入认证，输出经认证的输入份额。
> 局限与区别：方案只提供份额本身的静态认证，未保证这些份额在后续 MPC 中一致使用；需要额外的 MAC 一致性检查，且不满足不可关联性。

[11] Blanton, Jeong. Improved Signature Schemes for Secure Multiparty Computation with Certified Inputs. **ESORICS 2018**
> 核心思路：基于认证秘密共享构造针对特定 MPC 协议 [20,21] 的输入认证方案。
> 局限与区别：协议描述未明确要求认证阶段与 MPC 阶段使用同一组输入份额；仅针对特定协议，不具备通用性。

[6] Baum, Jadoul, Orsini, Scholl, Smart. Feta: Efficient Threshold Designated-Verifier Zero-Knowledge Proofs. **ePrint 2022**
> 核心思路：提出分布式验证者零知识证明，支持门限验证。
> 局限与区别：分布式证明中验证者群体检查单一个体提出的证明，而本文的分布式证明（DPoK）将秘密共享视为证明者集合，无单一证明者掌握全部知识；Feta 通信开销随电路大小线性增长，不支持代数关系的紧凑证明。

[13] Boneh, Boyle, Corrigan-Gibbs, Gilboa, Ishai. Zero-Knowledge Proofs on Secret-Shared Data via Fully Linear PCPs. **CRYPTO 2019**
> 核心思路：利用完全线性 PCP 在秘密共享数据上执行零知识证明，编译被动安全为主动安全。
> 局限与区别：针对的是低度电路（如下一条消息函数），而本文处理的认证关系（签名验证）具有代数结构且电路表示巨大；未考虑鲁棒性，不支持在恶意方存在时完成协议。

[3] Attema, Cramer. Compressed Σ-Protocol Theory and Practical Application to Plug & Play Secure Algorithmics. **CRYPTO 2020**
> 核心思路：提出压缩 Sigma 协议，将证明通信量从线性降低到对数。
> 局限与区别：该技术针对单一证明者；本文将其扩展为分布式设置，并增加了鲁棒完备性。

### 核心技术与方案

**1. 分布式证明（DPoK）定义。** 考虑一个 NP 关系 $\mathcal{R}$，证明者 $\mathcal{P}$ 持有实例-见证对 $(x,w)$，见证 $w$ 被（线性）秘密共享为 $w_1,\ldots,w_n$，分配给 $n$ 个工作节点 $\mathcal{W}_i$。工作节点之间不直接通信，所有交互通过广播信道进行，验证者 $\mathcal{V}$ 是公开硬币的。协议结束时验证者输出接受或拒绝。定义要求：完备性（诚实时总是接受）、知识可靠性（存在提取器能从成功的协议中抽取出有效见证）、诚实验证者零知识。鲁棒完备性进一步要求：即使部分工作节点被敌手控制，只要诚实节点持有的份额一致地确定出有效见证，协议仍以压倒性概率接受。鲁棒完备性对于编译器至关重要——它保证即使内部节点作恶，只要提供真实签名的节点诚实，认证过程不会因为恶意节点的捣乱而被阻断。

**2. 离散对数 DPoK 构造。** 以 Schnorr 协议为基础，但让每个工作节点 $\mathcal{W}_i$ 分别用其份额 $s_i$ 运行协议，广播自己的第一消息 $A_i = g^{s_i}$，收到公共挑战 $c$ 后广播响应 $z_i = \alpha_i + c s_i$。验证者检查 $g^{\sum z_i} = \prod A_i \cdot x^c$。这一简单方案通信随见证大小线性增长。为实现对数通信，采用压缩 Sigma 协议 [3] 替代基础 Schnorr 协议。鲁棒完备性通过纠错技术实现：每个工作节点额外预共享一个随机数 $r_i$，并提交承诺 $B_i = h_1^{r_i} h_2^{\omega_i}$；验证者发布随机向量 $\gamma$，各节点广播 $v_i = \langle \gamma, s_i \rangle + r_i$。由于 $(s_i, r_i)$ 构成 Reed-Solomon 码字，线性组合 $v_i$ 仍然是同一个码字。验证者对收到的向量 $v'$ 进行纠错译码（如 Berlekamp-Welch），将错误位置 $\mathcal{C}$ 标记为恶意工作节点，然后用剩余正确节点的承诺 $A_i$ 与重建系数检查 $z = g^{\sum k_i s_i}$ 是否成立。在 $|\mathcal{C}| < (n-t)/2$ 时纠错成功，从而鲁棒性成立。该 DPoK 具有 $t$ 隐私性和 $d$ 鲁棒性（$d < \frac{n-t}{2}$），广播通信复杂度为 $O(n\log \ell)$。

**3. BBS+ 签名 DPoK。** 将 BBS+ 签名验证关系分解为多个离散对数关系，核心在于将签名随机化（通过盲化因子 $u$ 和 $v$）以保证不可关联性，然后秘密共享随机化过程中的辅助值 $(r, v, \beta, t, \eta)$ 给工作节点。协议步骤：证明者广播 $(A', \bar A, d, C, D)$，其中 $C = d^{-v} h_0^{t-\eta}$，$D = h_0^\eta \prod h_i^{m_i}$，$A' = A^u$，$\bar A = (A')^{-\beta} b^u$。随后工作节点和验证者运行两个独立的离散对数 DPoK：一个关于 $D = h_0^\eta \prod h_i^{m_i}$（消息位于秘密中），另一个关于 $C = d^{-v} h_0^{t-\eta}$ 和 $\bar A/d = (A')^{-\beta} h_0^r$。最后验证者检查 $C \cdot D = g_1^{-1}$ 和 $e(A', w) = e(\bar A, g_2)$。该 DPoK 保持同样鲁棒性，额外开销来自预共享的辅助值（$O(n)$ 点对点通信）和两个离散对数 DPoK。

**4. 认证 MPC 编译器。** 仪式化：给定一个秘密共享基底的诚实多数 MPC 协议 $\Pi_{\mathrm{mpc}} = (\Pi_{\mathrm{sh}}, \Pi_{\mathrm{on}})$，编译后的协议 $\Pi_{\mathrm{ampc}}$ 的输入共享阶段 $\overline{\Pi}_{\mathrm{sh}}$ 与原始 $\Pi_{\mathrm{sh}}$ 完全相同。然后在 $\overline{\Pi}_{\mathrm{on}}$ 中，对每个参与方 $P_j$ 实例化一个 BBS+ DPoK（$P_j$ 为证明者，其他方为工作节点和验证者）。如果所有 DPoK 都接受，则继续执行 $\Pi_{\mathrm{on}}$；否则中止。鲁棒性保证了如果 $P_j$ 的输入确实被签名，则即使其他节点中有至多 $t$ 个恶意节点，该 DPoK 仍会成功接受，从而保证协议继续执行。安全证明表明：编译后的协议安全实现理想功能 $\mathcal{F}_{\mathrm{MPC}}^{\mathrm{auth}}$（该功能统一验证签名完整性并要求一致地使用输入），其作弊阈值与底层 DPoK 一致——使用鲁棒 DPoK 时 $t < n/3$，使用非鲁棒版本时保留 $t < n/2$。

### 核心公式与流程

**[DPoK 定义中的知识可靠性条件]**
$$
\Pr\left[\begin{array}{c}\mathcal{V}_{\mathcal{A},\Pi}(\mathsf{pp},x)=1\ \wedge\ ( (x,(s,t))\notin\mathcal{R}\ \vee\ \operatorname{Consistent}(\{s_i\}_{i\notin\mathbb{C}},s)=0)\end{array}\right]\leq \mathsf{negl}(\lambda)
$$
> 作用：定义敌手即使控制部分工作节点和证明者，也无法使验证者接受不满足关系的声明。

**[离散对数 DPoK 纠错检查]**
$$
\left(\prod_{j\in[q]} A_{i_j}^{h_{jk}}\right)_{k=1,\dots,n-t} = (z, 0^{n-t-1})
$$
> 作用：在剔除被纠错标记为恶意的索引集 $\mathcal{C}$ 后，用剩余诚实节点的承诺矩阵与对应的重建系数矩阵 H 验证求解得到正确的公开值 $z$，从而确认秘密与公开值一致。

**[BBS+ 签名验证的核心双线性检查]**
$$
e(A', w) = e(\bar A, g_2)
$$
> 作用：验证随机化后的签名 $(A',\bar A)$ 确实对应于公钥 $w = g_2^x$（私钥 $x$），即确认 $\bar A = (A')^x$ 成立，等效于验证原始 BBS+ 等式 $e(A, w g_2^\beta) = e(g_1 h_0^s \prod h_i^{m_i}, g_2)$。

**[编译器协议 $\Pi_{\mathrm{ampc}}$ 核心步骤]**
$$
\overline{\Pi}_{\mathrm{sh}}: \text{每个 } P_i \text{ 秘密共享输入 } x_i \text{ 同 } \Pi_{\mathrm{sh}}; \quad \overline{\Pi}_{\mathrm{on}}: \forall j\in[n], \text{运行 } \Pi_{\mathrm{bbs+}} \text{ 以 } P_j \text{ 为证明者}; \quad \text{若所有接受则执行 } \Pi_{\mathrm{on}}.
$$
> 作用：概述编译器将输入认证完全置于 MPC 核心计算之前，且直接使用了 MPC 阶段的输入份额，确保了认证与计算的一致性。

### 实验结果
实验平台为单线程 Intel Core i5-9400 2.9 GHz、16 GB RAM、Ubuntu 20.04。实现了 BBS+ 优化协议 $\Pi_{\mathrm{bbs-auth-opt}}$（非鲁棒批次化版本）并集成到 MP-SPDZ 的 Shamir 秘密共享恶意安全 MPC 中。基准场景为“安全 KPI 应用”，多个物流公司拥有包含 10 列的私有数据集，查询指定分类列的子集，计算对应数值列的均值。每方数据集行数从 100 到 4000 不等，参与方数为 3 或 5。结果显示：对于 3 方、4000 行，vanilla MPC 耗时 260 秒、通信约 65 MB；DPoK 额外耗时 246 秒、通信仅 15.8 KB。5 方、4000 行时 vanilla MPC 耗时 958 秒、通信约 342 MB；DPoK 额外耗时 312 秒、通信仅 33 KB。作为对比，将 BBS+ 验证内部化为 MiMC 哈希电路的方案其开销比 vanilla 大数倍乃至一个数量级，例如 5 方、4000 行时耗时 3645 秒、通信 202 MB。实验表明 DPoK 通信开销极小，计算开销随输入大小线性增长，主因来自于非交互零知识证明的代数运算（可并行化）。

### 局限性与开放问题
编译器使用鲁棒 DPoK 时作弊阈值限制为 $t<n/3$，低于原 MPC 的 $t<n/2$，在某些场景下可能存在可用性问题。计算开销随每方输入行数线性增长，对于极大规模输入（如百万级记录）仍面临实际挑战。文中提及了将计算并行化的潜在方向但未实现。此外，目前仅对 BBS+ 和 PS 签名给出了实例，扩展到其他代数签名或更一般的谓词证明（如范围证明）仍需要额外的构造工作。

### 强关联论文

[2] Aranha, Dalskov, Escudero, Orlandi. Improved Threshold Signatures, Proactive Secret Sharing, and Input Certification from LSS Isomorphisms. **LATINCRYPT 2021** [Google Scholar](https://scholar.google.com/scholar?q=Improved+Threshold+Signatures+Proactive+Secret+Sharing+and+Input+Certification+from+LSS+Isomorphisms)

[3] Attema, Cramer. Compressed Σ-Protocol Theory and Practical Application to Plug & Play Secure Algorithmics. **CRYPTO 2020** [Google Scholar](https://scholar.google.com/scholar?q=Compressed+%CE%A3-protocol+Theory+and+Practical+Application+to+Plug+%26+Play+Secure+Algorithmics)

[6] Baum, Jadoul, Orsini, Scholl, Smart. Feta: Efficient Threshold Designated-Verifier Zero-Knowledge Proofs. **ePrint 2022** [Google Scholar](https://scholar.google.com/scholar?q=Feta+Efficient+Threshold+Designated-Verifier+Zero-Knowledge+Proofs)

[11] Blanton, Jeong. Improved Signature Schemes for Secure Multiparty Computation with Certified Inputs. **ESORICS 2018** [Google Scholar](https://scholar.google.com/scholar?q=Improved+Signature+Schemes+for+Secure+Multiparty+Computation+with+Certified+Inputs)

[13] Boneh, Boyle, Corrigan-Gibbs, Gilboa, Ishai. Zero-Knowledge Proofs on Secret-Shared Data via Fully Linear PCPs. **CRYPTO 2019** [Google Scholar](https://scholar.google.com/scholar?q=Zero-Knowledge+Proofs+on+Secret-Shared+Data+via+Fully+Linear+PCPs)

[15] Camenisch, Drijvers, Lehmann. Anonymous Attestation Using the Strong Diffie Hellman Assumption Revisited. **TRUST 2016** [Google Scholar](https://scholar.google.com/scholar?q=Anonymous+Attestation+Using+the+Strong+Diffie+Hellman+Assumption+Revisited)

[22] Damgård, Pastro, Smart, Zakarias. Multiparty Computation from Somewhat Homomorphic Encryption. **CRYPTO 2012** [Google Scholar](https://scholar.google.com/scholar?q=Multiparty+Computation+from+Somewhat+Homomorphic+Encryption)

[36] Keller. MP-SPDZ: A Versatile Framework for Multi-Party Computation. **ACM CCS 2020** [Google Scholar](https://scholar.google.com/scholar?q=MP-SPDZ+A+Versatile+Framework+for+Multi-Party+Computation)

[44] Pointcheval, Sanders. Short Randomizable Signatures. **CT-RSA 2016** [Google Scholar](https://scholar.google.com/scholar?q=Short+Randomizable+Signatures)

[49] Shamir. How to Share a Secret. **Communications of the ACM 1979** [Google Scholar](https://scholar.google.com/scholar?q=How+to+Share+a+Secret)


## 关键词

+ 认证多方计算
+ 输入认证
+ 安全多方计算
+ 可识别中止
+ 分布式证明