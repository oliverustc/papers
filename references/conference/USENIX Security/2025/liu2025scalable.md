---
title: Scalable collaborative zk-snark and its application to efficient proof outsourcing
标题简称: 
论文类型: Conference
undefined: USENIX Security
发表年份: 2025
created: 2025-06-09 10:30:36
modified: 2025-06-09 10:36:52
---

## Scalable Collaborative zk-SNARK and Its Application to Fully Distributed Proof Delegation

## 发表信息

+ [原文链接](https://eprint.iacr.org/2024/940)

## 作者

+ Xuanming Liu
+ Zhelei Zhou
+ Yinghao Wang
+ Jinye He
+ Bingsheng Zhang
+ Xiaohu Yang
+ [Jiaheng Zhang](Jiaheng%20Zhang.md)

## 笔记

### 背景与动机

零知识简洁非交互式知识论证（zk-SNARK）允许证明者为秘密数据（witness）生成简短证明，在区块链、可验证机器学习等场景中有广泛应用。然而，现有 zk-SNARK 的证明生成耗时且内存消耗巨大——即使使用证明者高效的 HyperPlonk，生成包含 $2^{27}$ 个门的电路的证明仍需要数小时和超过 300 GB 内存。一种自然思路是将证明生成外包给一群服务器，但此前的工作 [42, 24] 假设服务器“无害”，直接暴露客户端的秘密 witness，不适合敏感场景。Garg 等人 [16] 首次将 collaborative zk-SNARK 框架 [28] 扩展到证明外包，并实现了基于 Groth16 和 Plonk 的协议，但他们存在一个关键瓶颈：协议中仍需要一个主导服务器承担 $O(T_P)$ 时间和 $O(S_P)$ 空间（与本地证明者相同），导致可扩展性差。本文旨在消除这种强大的主导服务器，使所有服务器平等分担工作，同时保证 witness 隐私。作者转向基于多元多项式的 zk-SNARK（如 Libra [43] 和 HyperPlonk [7]），这些方案避免使用 FFT 且证明者高效，但面对大型电路仍面临单机瓶颈。本文的核心贡献是开发了一套用于计算多元多项式相关原语（sumcheck、productcheck、multilinear 多项式承诺）的高效 MPC 工具箱，利用 packed secret sharing 实现负载均匀分布，从而首次在证明外包中同时实现隐私和可扩展性。

### 相关工作

[16] Garg et al. zkSaaS: Zero-Knowledge SNARKs as a service. **USENIX Security 2023** [Google Scholar](https://scholar.google.com/scholar?q=zkSaaS%3A+Zero-Knowledge+SNARKs+as+a+service)
> 核心思路：利用 packed Shamir 秘密分享设计针对 FFT 和 MSM 的 MPC 协议，实现 Groth16 和 Plonk 的 collaborative 证明。
> 局限与区别：协议依赖一个主导服务器（leader），该服务器的时间与空间复杂度与本地证明者相同 $O(T_P)$ 和 $O(S_P)$，通信瓶颈显著；本文的目标是消除主导服务器，使所有服务器均匀承担 $O(T_P/N)$ 和 $O(S_P/N)$。

[28] Ozdemir, Boneh. Experimenting with Collaborative zk-SNARKs: Zero-Knowledge Proofs for Distributed Secrets. **USENIX Security 2022** [Google Scholar](https://scholar.google.com/scholar?q=Experimenting+with+Collaborative+zk-SNARKs%3A+Zero-Knowledge+Proofs+for+Distributed+Secrets)
> 核心思路：提出 collaborative zk-SNARK 框架，通过通用 MPC 协议实现分布式证明生成，支持 honest majority 和 dishonest majority 设置。
> 局限与区别：通用 MPC 协议没有带来效率提升；本文在该框架基础上设计专用、可扩展的协议。

[42] Xie et al. zkBridge: Trustless Cross-chain Bridges Made Practical. **ACM CCS 2022** [Google Scholar](https://scholar.google.com/scholar?q=zkBridge%3A+Trustless+Cross-chain+Bridges+Made+Practical)
> 核心思路：提出 deVirgo，分布式 GKR 型 zk-SNARK，工作负载均匀分布，但 witness 直接暴露给服务器。
> 局限与区别：不提供 witness 隐私；本文在保护隐私的同时实现均匀负载。

[24] Liu et al. Pianist: Scalable zkRollups via Fully Distributed Zero-Knowledge Proofs. **IEEE S&P 2024** [Google Scholar](https://scholar.google.com/scholar?q=Pianist%3A+Scalable+zkRollups+via+Fully+Distributed+Zero-Knowledge+Proofs)
> 核心思路：设计分布式 Plonk 证明，负载均匀分布，但 witness 暴露。
> 局限与区别：同 [42]，不保护隐私；本文关注隐私保护场景。

[43] Xie et al. Libra: Succinct Zero-Knowledge Proofs with Optimal Prover Computation. **CRYPTO 2019** [Google Scholar](https://scholar.google.com/scholar?q=Libra%3A+Succinct+Zero-Knowledge+Proofs+with+Optimal+Prover+Computation)
> 核心思路：基于 GKR 协议和 multilinear 多项式承诺的 zk-SNARK，证明者复杂度 $O(n)$，针对数据并行电路优化。
> 局限与区别：单机证明者遇到大电路时时间与内存不足；本文将其扩展为可扩展 collaborative 版本。

[7] Chen et al. HyperPlonk: Plonk with Linear-Time Prover and High-Degree Custom Gates. **EUROCRYPT 2023** [Google Scholar](https://scholar.google.com/scholar?q=HyperPlonk%3A+Plonk+with+Linear-Time+Prover+and+High-Degree+Custom+GateS)
> 核心思路：提出线性时间证明者的 Plonk 变体，支持通用电路，使用 zerocheck、productcheck 等原语。
> 局限与区别：单机部署对大型电路不现实；本文为其构建 collaborative 版本，实现负载均匀。

[14] Franklin, Yung. Communication Complexity of Secure Computation. **STOC 1992** [Google Scholar](https://scholar.google.com/scholar?q=Communication+Complexity+of+Secure+Computation)
> 核心思路：提出 packed secret sharing (PSS) 方案，是 Shamir 秘密分享的推广，可打包多个秘密。
> 局限与区别：是本文 MPC 工具箱的基础，但原始工作不涉及 zk-SNARK 证明生成。

[33] Setty. Spartan: Efficient and General-Purpose zkSNARKs without Trusted Setup. **CRYPTO 2020** [Google Scholar](https://scholar.google.com/scholar?q=Spartan%3A+Efficient+and+General-Purpose+zkSNARKs+without+Trusted+Setup)
> 核心思路：基于 R1CS 的透明 zk-SNARK，使用 sumcheck 和 zerocheck。
> 局限与区别：本文指出其原语也可替换为 collaborative 工具，但未在本文实例化，留作未来工作。

[34] Setty, Lee. Quarks: Quadruple-Efficient Transparent zkSNARKs. **ePrint 2020** [Google Scholar](https://scholar.google.com/scholar?q=Quarks%3A+Quadruple-Efficient+Transparent+zkSNARKs)
> 核心思路：提出 productcheck 协议，用于构造 permutation-check 和 multiset-check。
> 局限与区别：本文的 collaborative productcheck 协议基于 Quark 的思路但引入了分布式计算。

### 核心技术与方案

本文的整体框架是基于 collaborative zk-SNARK 定义 [28]，其核心是设计一个安全 MPC 协议 Π，使得 N 个服务器能共同执行一个现有 zk-SNARK 的证明算法 Prove，且每个服务器只持有 witness 的 packed secret shares (PSS)。为了达到可扩展性，作者要求所有服务器的时间复杂度均为 $O(T_P/N)$，空间复杂度均为 $O(S_P/N)$，且总通信也能均匀分布。

由于 GKR 型 zk-SNARK（如 Libra [43]）和 HyperPlonk [7] 都基于多元多项式上的交互证明，其证明者算法主要由 sumcheck、productcheck、zerocheck 和 multilinear 多项式承诺（mvPC）组成。因此，本文的核心技术是构建一套 collaborative 的多元多项式原语工具包，每个原语都通过 PSS、常数轮通信和局部计算实现负载均匀分布。具体如下：

**1. Collaborative sumcheck (Π_dSumcheck)**  
服务器初始持有 f 在 $\{0,1\}^\ell$ 上评估值的 packed shares。利用 multilinear 多项式 sumcheck 的知名算法 [37]，证明者在第 i 轮只需提供 $f_i(0)$ 和 $f_i(1)$，且可通过线性组合（公式 (2)）从上一轮的书签表计算下一轮的表。本文的关键观察是，该线性组合在 packed shares 下可局部完成：每个服务器用公式 (3) 计算下一轮的 packed shares，其中所有操作都是线性组合，不破坏秘密。当进行的轮数使得每个服务器只剩一个 share 时（即 $\ell - \log k$ 轮后），通过一次 $\mathcal{F}_{\text{PSSToSS}}$ 转换将最后的 packed share 转换为 k 个 Shamir 秘密分享，然后继续本地计算最后一小段。该协议的时间复杂度为 $O(n/N)$，空间复杂度 $O(n/N)$，轮复杂度 O(1)，总通信 $O(N)$ 域元素。

**2. Collaborative productcheck (Π_dProdTree)**  
Quark [34] 的 productcheck 需要证明者构造一个 (ℓ+1)-variate 多项式 v，其评估值 $v(0,\mathbf{x}) = f(\mathbf{x})$，且 $v(1,\mathbf{x})$ 等于 f 在 $\{0,1\}^\ell$ 上评估值的乘积树（深度 ℓ 的完全二叉树）的内部节点值。本文的观察是，该乘积树可以这样分布式计算：将 n 个叶子分成 N 个子树，每个服务器负责计算 $\frac{n}{N}-1$ 个内部节点（局部计算乘积树）；然后选一个服务器（如 S1）整合 N 个子树的根节点，再计算一棵 $N$ 个叶子的乘积树，得到剩余 N-1 个内部节点。由于 $N \ll n$，每个服务器仍承担 $O(n/N)$ 计算。但直接在秘密共享上做逐层乘法会导致对数轮的重度降级—本文通过引入掩码（masks）技术，让服务器先乘以掩码后揭示部分“被掩盖”的叶子，使每个服务器得到其子树的明文叶子（但被掩盖），然后本地计算“被掩盖”的乘积树，最后再用另一组掩码（unmask）通过 PSS 乘法恢复正确的乘积树。该过程需要一次在线通信来分发被掩盖的子树，以及一次 $\mathcal{F}_{\text{PSSMult}}$ 来去掩码。复杂度：时间 $O(n/N)$，空间 $O(n/N)$，轮复杂度 O(1)，通信 $O(n)$ 域元素（可均摊至每服务器 $O(n/N)$）。

**3. Collaborative multilinear polynomial commitment (Π_dMVPC)**  
基于 Papamanthou 等 [29] 的 multilinear 多项式承诺方案。承诺计算本质上是多标量乘法（MSM）：$com_f = g^{f(\mathbf{s})} = \prod_{\mathbf{b} \in \{0,1\}^\ell} g^{\prod_i \beta_{b_i}(s_i) \cdot V(\mathbf{b})}$。服务器持有 V 的 packed shares 和预计算好的 packed 形式的群元素参数。通过调用分布式 MSM 协议 $\Pi_{\text{dMSM}}$（源自 [16]），每个服务器承担 $O(n/N)$ 群指数运算。  
打开证明（Open）需要计算 ℓ 个商多项式 $Q_i$ 和余多项式 $R_i$。作者利用 multilinear 多项式的代数性质，通过公式 (5) 在 packed shares 上直接本地递归计算 $Q_i$ 和 $R_i$ 的 packed shares，而不需 FFT。此过程与 sumcheck 类似，直到 $(\ell - \log k)$ 轮后转为 Shamir 分享完成。然后对这些 $Q_i$ 的 packed shares 再通过 $\Pi_{\text{dMSM}}$ 计算群元素承诺。通过批处理技术，所有 $\ell$ 个 MSM 可一轮完成。总体复杂度：时间 $O(n/N)$，空间 $O(n/N)$，通信 $O(N\log n)$ 群元素（由于 MSM）。

**4. 组合实现 collaborative Libra 与 collaborative HyperPlonk**  
- **Collaborative Libra**：针对数据并行电路（B 个相同拷贝），将各拷贝相同位置的变量打包成包。证明过程包括 d 轮 sumcheck 和一次 multilinear 多项式求值，全部用上述 collaborative sumcheck 和 dMVPC 替换。由定理 4 保证安全性（$\{\mathcal{F}_{\text{PSSMult}},\mathcal{F}_{\text{dMSM}},\mathcal{F}_{\text{PSSToSS}}\}$-hybrid 模型），复杂度：时间 $O(n/N)$，空间 $O(n/N)$，轮数 $O(d)$。  
- **Collaborative HyperPlonk**：针对通用电路，证明过程包括：用 $\Pi_{\text{dProdTree}}$ 支持 permutation-check（转化为 productcheck 和 zerocheck），用 collaborative sumcheck 支持 gate identity 的 zerocheck，以及多次 dMVPC.Open。由定理 5 保证安全性（额外用到 $\mathcal{F}_{\text{ProdTree}}$）。复杂度：时间 $O(n/N)$，空间 $O(n/N)$，轮数 O(1)。

### 核心公式与流程

**[Collaborative sumcheck 中下一轮 packed shares 的局部计算]**
$$
\llbracket \boldsymbol{x}_j^{(i+1)}\rrbracket = (1 - r_i) \cdot \llbracket \boldsymbol{x}_j^{(i)}\rrbracket + r_i \cdot \llbracket \boldsymbol{x}_{j + \frac{n_i}{2k}}^{(i)}\rrbracket , \quad j \in \left[ \frac{n_{i+1}}{k} \right]
$$
> 作用：服务器在第 i 轮收到挑战 $r_i$ 后，用此公式从当前轮的 packed shares 逐个线性组合出下一轮的 packed shares，实现无需通信的本地计算该轮书签表。

**[Collaborative multilinear 多项式承诺打开中商与余的 packed shares 局部计算]**
$$
Q_i(\boldsymbol{b}) = R_{i-1}(1,\boldsymbol{b}) - R_{i-1}(0,\boldsymbol{b}), \quad R_i(\boldsymbol{b}) = (1 - u_i) \cdot R_{i-1}(0,\boldsymbol{b}) + u_i \cdot R_{i-1}(1,\boldsymbol{b})
$$
> 作用：给定评估点 $\mathbf{u}$，服务器可对 packed shares 做减法与线性组合，直接得到商多项式 $Q_i$ 和余多项式 $R_i$ 在超立方体上评估值的 packed shares，避免了 FFT 操作。

**[PSSToSS 转换后完成的最后一小段 sumcheck 中 Shamir 分享局部计算]**
$$
\langle x_j^{(i+1)}\rangle = (1 - r_i) \cdot \langle x_j^{(i)}\rangle + r_i \cdot \langle x_{j + \frac{n_i}{2}}^{(i)}\rangle
$$
> 作用：当 packed shares 只剩最后一个包时，转换为 k 个 Shamir 秘密分享后，继续用类似线性组合公式完成剩下的 $O(k)$ 轮 sumcheck，所有操作仍在本地完成。

### 实验结果

实验设置：每个服务器使用 c7.large 实例（4 GB RAM），与 [16] 相同的 packing factor $k = N/4$，安全性抵御至多 $N/4$ 个腐败服务器。网络默认为 4 Gbps。对比的本地证明者也运行在 c7.large 上。

核心性能数值：对于 $2^{24}$ 个门的电路，128 服务器时 collaborative Libra 耗时 8 秒（本地超过 2 分钟，提速 21×），collaborative HyperPlonk 耗时 4 分钟（本地约 1.5 小时，提速 24×）。空间效率：128 服务器可处理比本地大 32× 的电路。与 zkSaaS [16] 对比：在相同电路尺寸 $2^{20}$ 下，随着服务器从 16 增加到 128，collaborative Plonk 的 leader 服务器内存始终接近本地（保持不变），而每服务器内存线性下降；速度提升方面，在 100 Mbps 网络下 Plonk 几乎无提升，而 HyperPlonk 仍可达 6.3×（32 服务器）到 20.3×（128 服务器）加速。通信费用：128 服务器时每服务器通信量 HyperPlonk 为 397 MB，而 Plonk leader 为 22 GB，导致经济成本 HyperPlonk 约 $0.21，Plonk 约 $2（参考 Google Cloud 定价）。

不同网络条件：从 10 Gbps 本地网到 100 Mbps 广域网，HyperPlonk 的加速比下降较少（例如 128 服务器本地网 22.9× 到广域网 20.3×），而 Libra 下降较多（15.6× 到 4.4×），因为 HyperPlonk 是常数轮，受延迟影响更小。增加服务器可以部分缓解网络瓶颈，因为通信进一步均摊。

### 局限性与开放问题

本文的 collaborative Libra 仅针对数据并行电路，而对通用电路尚无有效的均匀分布方案，原因在于 Libra 原始线性时间优化算法 [43, Section 3.3] 对任意形式电路难以分布式实现。另一个开放问题是 instantiating 适用于 R1CS 关系的 collaborative zk-SNARK（如 Spartan [33] 及其变体），其原语本文的工具包可覆盖，但需要进一步组合优化。此外，本文仅考虑了半诚实对手威胁模型，虽然猜测协议对恶意敌手的线性攻击 [18] 具备一定安全性，但正式实现恶意安全需要额外轻量级验证协议，这留作未来工作。

### 强关联论文

[16] Garg et al. zkSaaS: Zero-Knowledge SNARKs as a service. **USENIX Security 2023** [Google Scholar](https://scholar.google.com/scholar?q=zkSaaS%3A+Zero-Knowledge+SNARKs+as+a+service)

[28] Ozdemir, Boneh. Experimenting with Collaborative zk-SNARKs: Zero-Knowledge Proofs for Distributed Secrets. **USENIX Security 2022** [Google Scholar](https://scholar.google.com/scholar?q=Experimenting+with+Collaborative+zk-SNARKs%3A+Zero-Knowledge+Proofs+for+Distributed+Secrets)

[42] Xie et al. zkBridge: Trustless Cross-chain Bridges Made Practical. **ACM CCS 2022** [Google Scholar](https://scholar.google.com/scholar?q=zkBridge%3A+Trustless+Cross-chain+Bridges+Made+Practical)

[24] Liu et al. Pianist: Scalable zkRollups via Fully Distributed Zero-Knowledge Proofs. **IEEE S&P 2024** [Google Scholar](https://scholar.google.com/scholar?q=Pianist%3A+Scalable+zkRollups+via+Fully+Distributed+Zero-Knowledge+Proofs)

[43] Xie et al. Libra: Succinct Zero-Knowledge Proofs with Optimal Prover Computation. **CRYPTO 2019** [Google Scholar](https://scholar.google.com/scholar?q=Libra%3A+Succinct+Zero-Knowledge+Proofs+with+Optimal+Prover+Computation)

[7] Chen et al. HyperPlonk: Plonk with Linear-Time Prover and High-Degree Custom Gates. **EUROCRYPT 2023** [Google Scholar](https://scholar.google.com/scholar?q=HyperPlonk%3A+Plonk+with+Linear-Time+Prover+and+High-Degree+Custom+GateS)

[14] Franklin, Yung. Communication Complexity of Secure Computation. **STOC 1992** [Google Scholar](https://scholar.google.com/scholar?q=Communication+Complexity+of+Secure+Computation)

[33] Setty. Spartan: Efficient and General-Purpose zkSNARKs without Trusted Setup. **CRYPTO 2020** [Google Scholar](https://scholar.google.com/scholar?q=Spartan%3A+Efficient+and+General-Purpose+zkSNARKs+without+Trusted+Setup)

[34] Setty, Lee. Quarks: Quadruple-Efficient Transparent zkSNARKs. **ePrint 2020** [Google Scholar](https://scholar.google.com/scholar?q=Quarks%3A+Quadruple-Efficient+Transparent+zkSNARKs)

[29] Papamanthou et al. Signatures of Correct Computation. **TCC 2013** [Google Scholar](https://scholar.google.com/scholar?q=Signatures+of+Correct+Computation)


## 关键词

+ 协作式zk-SNARK系统
+ 分布式证明生成与委托
+ HyperPlonk算术化优化
+ 多方计算零知识证明
+ 亚线性通信开销
+ 置换检查协议MPC友好设计