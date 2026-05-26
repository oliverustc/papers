---
title: "Succinct zero-knowledge batch proofs for set accumulators"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2022
modified: 2025-04-22 09:51:09
created: 2025-04-13 16:51:17
---

## Succinct zero-knowledge batch proofs for set accumulators

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3548606.3560677)

## 作者

+ [Matteo Campanelli](Matteo%20Campanelli.md)
+ [Dario Fiore](Dario%20Fiore.md)
+ Semin Han 
+ Jihye Kim 
+ [Dimitris Kolonelos](Dimitris%20Kolonelos.md)
+ [Hyunok Oh](Hyunok%20Oh.md)
## 笔记

### 背景与动机
区块链系统的全局状态（如 UTXO 集、账户余额集）规模庞大，验证一笔交易通常需要检查状态中元素的存在性（即集合成员关系）以及状态更新的正确性。认证数据结构（如 Merkle 树或 RSA 累加器）通过允许用户仅存储状态的简洁摘要（digest）来实现可扩展验证，但现有方案面临两个核心挑战：隐私性（交易数据不应公开）和吞吐量（批处理交易的能力）。将 zkSNARK 与 Merkle 树结合是实现隐私性和批处理的常见方法，然而，在 SNARK 约束系统中编码约 $O(\log n)$ 层哈希运算会导致证明时间随集合规模 $n$ 和批次大小 $m$ 急剧增长，即便使用 SNARK 友好的哈希函数（如 Poseidon）[37]，性能瓶颈依然严重。RSA 累加器具有常数大小的批量成员证明和更新证明 [12]，但将其验证方程（涉及大整数指数运算）直接编码到 SNARK 约束系统中会产生数百万个约束，在计算上不切实际。近期工作 [10] 仅支持单元素成员关系证明，而 [46] 虽支持批量更新，但证明代价很高，含约 500 万约束的固定开销，性能仅在集合规模达 $2^{20}$、批量大小超 1300 时优于 Merkle 树。本文旨在填补这一空白：设计能高效利用 zkSNARK 与 RSA 累加器的协议，实现可扩展的、零知识的批量成员证明和批量更新证明。

### 相关工作

[10] Benarroch 等. Zero-Knowledge Proofs for Set Membership: Efficient, Succinct, Modular. **FC 2021** [Google Scholar](https://scholar.google.com/scholar?q=Zero-Knowledge+Proofs+for+Set+Membership+Efficient+Succinct+Modular)
> 核心思路：提出一个 Σ-协议，证明素数阶群中的承诺与隐藏序群中的承诺打开到同一整数（累积集元素）。
> 局限与区别：证明大小与整数大小呈线性关系，无法扩展至批量场景。

[46] Ozdemir 等. Scaling Verifiable Computation Using Efficient Set Accumulators. **USENIX Security 2020** [Google Scholar](https://scholar.google.com/scholar?q=Scaling+Verifiable+Computation+Using+Efficient+Set+Accumulators)
> 核心思路：使用 RSA 累加器和 Wesolowski 证明（PoE）进行批量更新（MultiSwap）验证，结合 SNARK 证明哈希-除尽函数求值。
> 局限与区别：存在约 500 万约束的固定开销；其技术不兼容零知识，不能直接用于隐藏元素的批量成员证明。

[12] Boneh 等. Batching Techniques for Accumulators with Applications to IOPs and Stateless Blockchains. **CRYPTO 2019** [Google Scholar](https://scholar.google.com/scholar?q=Batching+Techniques+for+Accumulators+with+Applications+to+IOPs+and+Stateless+Blockchains)
> 核心思路：提出针对隐藏序群的批量证明、简洁知识指数证明（PoKE）和子向量承诺。
> 局限与区别：构建的批量证明要求验证者已知待验证的元素，不适用于隐藏元素的零知识场景。

[21] Campanelli 等. LegoSNARK: Modular Design and Composition of Succinct Zero-Knowledge Proofs. **CCS 2019** [Google Scholar](https://scholar.google.com/scholar?q=LegoSNARK+Modular+Design+and+Composition+of+Succinct+Zero-Knowledge+Proofs)
> 核心思路：提出 Commit-and-Prove SNARK（CP-SNARK）的模块化组合框架。
> 区别：本文使用该框架组合整数算术 CP-SNARK 与自定义的 Σ-协议及 PoKE。

[5] Bari 等. Collision-Free Accumulators and Fail-Stop Signature Schemes Without Trees. **EUROCRYPT 1997** [Google Scholar](https://scholar.google.com/scholar?q=Collision-Free+Accumulators+and+Fail-Stop+Signature+Schemes+Without+Trees)
> 核心思路：提出基于 RSA 群（隐藏序群）的密码学累加器，用单一群元素表示全集。
> 区别：本文在此基础上构建了适用于零知识的批处理协议。

### 核心技术与方案
本文的整体框架基于 Commit-and-Prove SNARK 的模块化组合思想 [21]，针对两类核心关系（批量成员关系和批量插入关系）分别设计了高效的协议——harisa 和 b-ins-arisa。两个协议的共同点是避免将 RSA 群运算直接编码到 SNARK 约束系统中，而是通过组合 Σ-协议或 PoKE 协议与 CP-SNARK 来“外包”指数运算。

**1. 批量成员证明协议 harisa**  
该协议解决的是零知识批量成员证明问题：给定 RSA 累加器 acc（对应集合 $S$）和承诺 $c_{\vec{u}}$（打开为 $\{u_1, \ldots, u_m\}$），证明所有 $u_i \in S$，且 $u_i$ 对验证者保密。核心技术分为三步：

*   **隐藏见证技术**：RSA 累积的批量见证 $W$ 会泄露元素信息。本文引入一种随机化方式：向原始集合 $S$ 中添加前 $2\lambda$ 个素数 $\mathbb{P}_{2\lambda}$（得到新的累加器 $\widehat{\text{acc}}$），然后从 $\mathbb{P}_{2\lambda}$ 中随机挑选子集 $P$，将原见证 $W$ 提升至 $\bar{s}$ 次幂，得到 $\hat{W} = W^{\bar{s}}$，其中 $\bar{s} = \prod_{p_i \in \mathbb{P}_{2\lambda}} p_i^{1-b_i}$，$b_i \leftarrow \{0,1\}$。在 DDH-II 假设下，$\hat{W}$ 在计算上不可与随机群元素区分，从而隐藏了 $u_i$。

*   **组合 Σ-协议与 PoKE**：为了简洁地证明 $\hat{W}^{e} = \widehat{\text{acc}}$（其中 $e = s \cdot \prod_i u_i$，$s = \prod_i p_i^{b_i}$），协议使用 Fiat-Shamir 变换后的 Σ-协议：证明者计算 $R = \hat{W}^r$，挑战 $h = H(\ldots)$，响应 $k = r + e h$。为克服 $k$ 非简洁的问题，引入 PoKE 协议 [12]，仅证明存在 $k$ 使得 $\hat{W}^k = \widehat{\text{acc}}^h R$，验证者只获得 $k \bmod \ell$（$\ell$ 为 $2\lambda$ 比特的素数挑战）和简洁证明 $Q$。

*   **CP-SNARK 链接**：最后，需要将 PoKE 公开的 $\hat{k} = k \bmod \ell$ 与原始承诺 $c_{\vec{u}}$ 绑定。协议使用 CP-SNARK cpΠ^modarithm（基于 [21] 的 LegoGroth16）证明 $\hat{k} = (s \cdot \prod_i u_i)h + r \bmod \ell$，同时使用 cpΠ^bound 证明所有 $u_i > p_{2\lambda}$（确保 $u_i$ 不是人工添加的素数）。这一结合也解决了 Σ-协议在隐藏序群中仅具有 1/2 完备性的经典问题 [4, 54]——因 SNARK 提取器可打开承诺得到 $k = r + s u h$，从而两次执行的差给出 $\text{acc}^{h-h'} = W^{su(h-h')}$，可提取 $su$。

安全性依赖 Adaptive Root 假设、DDH-II 假设以及 CP-SNARK 的安全性，在随机预言机模型下证明了知识可靠性、零知识和简洁性。证明大小、验证时间均与集合大小 $n$ 和批次大小 $m$ 无关。

**2. 批量插入证明协议 b-ins-arisa**  
该协议解决的是批量插入关系的非零知识证明：给定 acc、acc' 和承诺 $c_{\vec{u}}$，证明 $\text{acc}' = \text{acc}^{\prod_i u_i}$（即 acc' 是向 acc 对应集合中插入 $\{u_i\}$ 的结果）。技术思路更简洁：

*   首先，证明者计算 $\pi_1 = \text{PoKE}(\text{acc}, \text{acc}', u^*)$，其中 $u^* = \prod_i u_i$，验证者获得 $\hat{k} = u^* \bmod \ell$ 和简洁证明 $Q$。
*   其次，使用 CP-SNARK cpΠ^modarithm 证明 $\hat{k} \equiv \prod_i u_i \pmod{\ell}$（与 $c_{\vec{u}}$ 绑定）。
*   最后，使用 CP-SNARK cpΠ^{H_{DI}} 证明每个 $u_i$ 是除尽哈希函数 $H_{DI}(x) = \Delta + H(x)$ 的正确输出，从而将任意整数 $x_i$ 映射为可纳入 RSA 累加器的元素。该哈希由 Ozdemir 等人 [46] 提出，在随机预言机模型下是除尽困难的。整个协议的安全性不再需要零知识假设。

**3. 扩展至 MultiSwap**  
利用 [46] 的归约技术，MultiSwap（一组元素交换操作）可以表示为两个批量插入关系的组合：存在中间累加器 $\text{acc}_{\text{mid}}$，使得 $\text{acc} \to \text{acc}_{\text{mid}}$（插入 $Y$）和 $\text{acc}' \to \text{acc}_{\text{mid}}$（插入 $X$）。因此，通过两次调用 b-ins-arisa 即可实现 MultiSwap 证明。

**复杂度分析**：
*   harisa：证明大小常数（约 1.17 KB），验证时间约 63 ms，均与 $n, m$ 无关。证明时间约 $O(m \cdot \text{(RSA运算+SNARK运算)})$，但实践中 RSA 运算占比较小（约 1%）。
*   b-ins-arisa：证明大小约 1.4 KB，验证时间约 120 ms。证明时间主要包括 PoKE 运算（约 $O(1)$ 次指数运算）和 SNARK 证明时间（与 $m$ 线性相关）。

### 核心公式与流程

**[RSA 累加器批量成员验证等式]**
$$
W^{\prod_{i=1}^m u_i} = \text{acc}
$$
> 作用：RSA 累加器的标准批量成员关系，给定见证 $W$ 和元素乘积，可快速验证。本文的隐蔽协议围绕该等式展开。

**[隐藏见证的构成]**
$$
\hat{W} = W^{\bar{s}}, \quad \bar{s} = \prod_{p_i \in \mathbb{P}_{2\lambda}} p_i^{1-b_i}
$$
> 作用：将原始见证随机化为 $\hat{W}$，在 DDH 假设下实现零知识。验证方程变为 $\hat{W}^{s \cdot \prod u_i} = \widehat{\text{acc}}$，其中 $s = \prod p_i^{b_i}$。

**[harisa 核心协议流程 (图2 压缩版)]**
1. 计算 $\widehat{\text{acc}} = \text{acc}^{\prod p_i}$，采样 $b_i$ 得 $s, \bar{s}$，计算 $\hat{W} = W^{\bar{s}}$。
2. 采样随机数 $r$，计算 $R = \hat{W}^r$，获得挑战 $h = H(\ldots)$，计算 $k = r + (u^* s)h$。
3. 生成 PoKE 证明 $\pi_1$（证明 $\hat{W}^k = \widehat{\text{acc}}^h R$），输出 $\pi_1 = (Q, \hat{k})$，其中 $\hat{k} = k \bmod \ell$。
4. 计算 $\pi_2 = \text{cp}\Pi^{\text{modarithm}}.\text{Prv}(\hat{k} = s h u^* + r \pmod{\ell})$。
5. 计算 $\pi_3 = \text{cp}\Pi^{\text{bound}}.\text{Prv}(u_i > p_{2\lambda})$。
6. 输出 $\pi = (\hat{W}, R, c_{s,r}, \pi_1, \pi_2, \pi_3)$。
> 作用：完整定义了 harisa 证明过程的六个步骤，揭示了零知识性、简洁性和可验证性的来源。

**[b-ins-arisa 核心协议流程 (图3 压缩版)]**
1. 计算 $u^* = \prod u_i$，生成 $\pi_1 = \text{PoKE}(\text{acc}, \text{acc}', u^*)$，得 $(Q, \hat{k})$。
2. 计算 $\pi_2 = \text{cp}\Pi^{\text{modarithm}}.\text{Prv}(\hat{k} = u^* \pmod{\ell})$。
3. 计算 $\pi_3 = \text{cp}\Pi^{H_{DI}}.\text{Prv}(u_i = \Delta + H(x_i))$。
4. 输出 $\pi = (\pi_1, \pi_2, \pi_3)$。
> 作用：高效证明批量插入关系的简洁流程，无需零知识。

### 实验结果
**实验设置**：在 Amazon EC2 r5.8xlarge（248GB RAM）上单线程运行。基线方案是基于 Merkle 树的 CP-SNARK（LegoGroth16 [21]），哈希函数采用 Poseidon [37] 或 SHA-256。RSA 累加器使用 2048 位群。CP-SNARK 采用 BLS12-381 曲线。

**批量成员证明 (harisa)**：
*   **证明时间**：对于批量大小 16、集合大小 $2^{16}$，harisa 耗时 2.86 秒，而 MT-Pos-16 需 81.93 秒（快 28.6×），MT-SHA-16 需约 1891 秒（快 661×）。对于批量大小 64，harisa 耗 9.06 秒，MT-Pos-32 需 567.93 秒（快 62.7×）。
*   **验证时间和证明大小**：harisa 验证时间约 63 ms，证明大小 1.17 KB；Merkle 树方案验证时间约 31 ms，证明大小 0.29 KB。harisa 的验证稍慢、证明稍大，但仍在同一量级。
*   **CRS 大小**：harisa 公共参数大小低于 8.5 MB（批量 64），而 MT-Pos-32 的 CRS 超过 650 MB。

**DID 应用**：在模拟车险保费计算的 DID 场景中，对于批量 16，harisa-DID_{pos} 耗时 8.1 秒，MT-DID_{pos} 需 99.55 秒（快 12.3×）；对于批量 64，速度提升至 12.6×。

**MultiSwap (b-ins-arisa)**：
*   与 Merkle-Swap 相比，b-ins-arisa 在交换数量约 140 时达到性能交叉点；而 OWWB [46] 的交叉点在约 1400。
*   验证时间约 120 ms，证明大小 1.4 KB，与基线 Merkle-Swap（0.29 KB，31 ms）相比略有增加。

### 局限性与开放问题
协议的零知识批量成员证明依赖于 DDH-II 假设，该假设在未知阶群中尚未被充分验证。实现中对元素的编码强制要求元素为大于 $p_{2\lambda}$ 的素数，虽可通过哈希到素数扩展，但这增加了约束和计算开销。b-ins-arisa 不支持零知识，其安全性仅适用于“受信任累加器模型”。两个协议的验证时间虽与集合规模无关，但仍比纯 Merkle 树方案验证慢约 2 倍，且证明大小约 4 倍于 Merkle 树方案，在带宽极度受限的场景下可能成为短板。

### 强关联论文

[10] Daniel Benarroch, Matteo Campanelli, Dario Fiore, Kobi Gurkan, and Dimitris Kolonelos. Zero-Knowledge Proofs for Set Membership: Efficient, Succinct, Modular. **FC 2021** [Google Scholar](https://scholar.google.com/scholar?q=Zero-Knowledge+Proofs+for+Set+Membership+Efficient+Succinct+Modular)

[46] Alex Ozdemir, Riad S. Wahby, Barry Whitehat, and Dan Boneh. Scaling Verifiable Computation Using Efficient Set Accumulators. **USENIX Security 2020** [Google Scholar](https://scholar.google.com/scholar?q=Scaling+Verifiable+Computation+Using+Efficient+Set+Accumulators)

[12] Dan Boneh, Benedikt Bünz, and Ben Fisch. Batching Techniques for Accumulators with Applications to IOPs and Stateless Blockchains. **CRYPTO 2019** [Google Scholar](https://scholar.google.com/scholar?q=Batching+Techniques+for+Accumulators+with+Applications+to+IOPs+and+Stateless+Blockchains)

[21] Matteo Campanelli, Dario Fiore, and Anaïs Querol. LegoSNARK: Modular Design and Composition of Succinct Zero-Knowledge Proofs. **CCS 2019** [Google Scholar](https://scholar.google.com/scholar?q=LegoSNARK+Modular+Design+and+Composition+of+Succinct+Zero-Knowledge+Proofs)

[5] Niko Bari and Birgit Pfitzmann. Collision-Free Accumulators and Fail-Stop Signature Schemes Without Trees. **EUROCRYPT 1997** [Google Scholar](https://scholar.google.com/scholar?q=Collision-Free+Accumulators+and+Fail-Stop+Signature+Schemes+Without+Trees)

[4] Endre Bangerter, Jan Camenisch, and Stephan Krenn. Efficiency Limitations for S-Protocols for Group Homomorphisms. **TCC 2010** [Google Scholar](https://scholar.google.com/scholar?q=Efficiency+Limitations+for+S-Protocols+for+Group+Homomorphisms)

[54] Björn Terelius and Douglas Wikström. Efficiency Limitations of S-Protocols for Group Homomorphisms Revisited. **SCN 2012** [Google Scholar](https://scholar.google.com/scholar?q=Efficiency+Limitations+of+S-Protocols+for+Group+Homomorphisms+Revisited)

[17] Jan Camenisch and Anna Lysyanskaya. Dynamic Accumulators and Application to Efficient Revocation of Anonymous Credentials. **CRYPTO 2002** [Google Scholar](https://scholar.google.com/scholar?q=Dynamic+Accumulators+and+Application+to+Efficient+Revocation+of+Anonymous+Credentials)

[38] Jens Groth. On the Size of Pairing-Based Non-interactive Arguments. **EUROCRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=On+the+Size+of+Pairing-Based+Non-interactive+Arguments)

[41] Jiangtao Li, Ninghui Li, and Rui Xue. Universal Accumulators with Efficient Nonmembership Proofs. **ACNS 2007** [Google Scholar](https://scholar.google.com/scholar?q=Universal+Accumulators+with+Efficient+Nonmembership+Proofs)


## 关键词

+ 累加器
+ 零知识证明
+ 批量成员资格
+ RSA累加器
+ 区块链隐私