---
title: "Bulletproofs: Short proofs for confidential transactions and more"
标题简称:
论文类型: conference
会议简称: S&P
发表年份: 2018
modified: 2025-04-22 16:06:33
created: 2025-04-08 17:03:06
---

## Bulletproofs: Short proofs for confidential transactions and more

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/8418611)

## 作者

+ [Benedikt Bünz](Benedikt%20Bünz.md)
+ [Jonathan Bootle](Jonathan%20Bootle.md)
+ [Dan Boneh](Dan%20Boneh.md)
+ Andrew Poelstra
+ Pieter Wuille
+ Greg Maxwell

## 笔记

### 背景与动机
区块链上的机密交易要求隐藏转账金额，但节点仍需验证交易有效，例如确保输出金额非负且输入不小于输出。现有方法要么依赖可信设置（如 SNARKs），要么证明尺寸过大——以比特币机密交易为例，一个 32 位范围证明往往占用 5 KB 以上，远超交易体本身。在 Mimblewimble 等精简区块链方案中，后续 UTXO 所附带的范围证明尺寸成为存储瓶颈。本文提出的 Bulletproofs 无需可信设置、仅依赖于离散对数假设，且证明尺寸仅为输入比特长度的对数级，同时支持多证明聚合，大幅降低存储和传输开销。

### 相关工作

[7] Bootle 等. Efficient zero-knowledge arguments for arithmetic circuits in the discrete log setting. **EUROCRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+zero-knowledge+arguments+for+arithmetic+circuits+in+the+discrete+log+setting)
> 核心思路：首次提出基于内积论证的对数级算术电路证明，通信量为 6·log₂(n) 个群元素。
> 局限与区别：内积论证的通信乘数为 6，且未处理聚合和承诺作为电路输入的情况。Bulletproofs 将该乘数降至 2，并拓展为支持多证明聚合和直接以 Pedersen 承诺作为电路输入。

[2] Maxwell. Confidential transactions. 2016
> 核心思路：用 Pedersen 承诺隐藏交易金额，但需要线性尺寸的范围证明。
> 局限与区别：其 Borromean 签名或 Polestra 等人的优化方案 [3] 仍为线性尺寸。Bulletproofs 将对数尺寸引入即用场景。

[3] Poelstra 等. Confidential assets.
> 核心思路：优化了范围证明的通信，每个比特仅需 0.63 个群元素。
> 局限与区别：证明尺寸仍为 O(n)，且不支持聚合。

[4] Ben-Sasson 等. SNARKs for C. **CRYPTO 2013** [Google Scholar](https://scholar.google.com/scholar?q=SNARKs+for+C)
> 核心思路：通过 PCP 和椭圆曲线配对实现常数大小证明，但依赖可信设置。
> 局限与区别：需要每次应用执行复杂的可信安装仪式，不适合去中心化场景。Bulletproofs 完全避免可信设置。

[6] Ben-Sasson 等. Scalable, transparent, and post-quantum secure computational integrity. **2018** [Google Scholar](https://scholar.google.com/scholar?q=Scalable+transparent+and+post+quantum+secure+computational+integrity)
> 核心思路：基于哈希函数实现透明、后量子安全的证明（STARK）。
> 局限与区别：证明尺寸在实用中仍达数百 KB（如 200 KB 以上），且证明生成需大 FFT、内存开销高。Bulletproofs 在相同安全级别下证明仅约 1 KB。

[8] Poelstra. Mimblewimble.
> 核心思路：利用 Pedersen 承诺的加性同态，将交易签名密钥设为承诺之差，从而省去脚本公钥、实现交易修剪。
> 局限与区别：仍依赖线性范围证明。Bulletproofs 的对数尺寸与其交易聚合思想结合，可使全网存储大幅缩减。

[13] Noether 等. Ring confidential transactions. **Ledger 2016** [Google Scholar](https://scholar.google.com/scholar?q=Ring+confidential+transactions)
> 核心思路：在 Monero 中使用环签名和线性范围证明实现机密交易。
> 局限与区别：范围证明的线性尺寸导致交易体积较大。Bulletproofs 可直接替代其范围证明部分。

[17] Dagher 等. Provisions: Privacy-preserving proofs of solvency for Bitcoin exchanges. **2015** [Google Scholar](https://scholar.google.com/scholar?q=Provisions+Privacy+preserving+proofs+of+solvency+for+Bitcoin+exchanges)
> 核心思路：交易所向用户证明偿付能力，每个账户需一个线性范围证明。
> 局限与区别：对有 200 万客户的交易所，范围证明约占 13 GB。Bulleproofs 可将这部分压缩至 2 KB 以内。

### 核心技术与方案

#### 1. 改进的内积论证
原始内积论证 [7] 需传送 6·log₂(n) 个群元素。Bulletproofs 通过修改待证明的关系——将内积值 c 绑定到一个固定的群元素 u 上，从而将每轮通信量从 2 个群元素减为 2 个群元素，且递归深度不变。

**关系**：证明者声称知晓向量 a, b ∈ ℤₚⁿ，满足 P = g^a h^b 且 c = ⟨a, b⟩。

**Protocol 2 的递归步**：设 n 为 2 的幂。证明者计算 c_L = ⟨a_{[:n/2]}, b_{[n/2:]}⟩, c_R = ⟨a_{[n/2:]}, b_{[:n/2]}⟩，并发送 L = g_{[n/2:]}^{a_{[n/2:]}} h_{[n/2:]}^{b_{[n/2:]}} u^{c_L} 和 R = g_{[:n/2]}^{a_{[n/2:]}} h_{[n/2:]}^{b_{[:n/2]}} u^{c_R}。收到挑战 x 后，双方计算：
- g' = g_{[:n/2]}^{x^{-1}} ∘ g_{[n/2:]}^{x}
- h' = h_{[:n/2]}^{x} ∘ h_{[n/2:]}^{x^{-1}}
- P' = L^{x²} P R^{x⁻²}
证明者计算 a' = a_{[:n/2]}·x + a_{[n/2:]}·x⁻¹，b' = b_{[:n/2]}·x⁻¹ + b_{[n/2:]}·x，然后对 (g', h', u, P'; a', b') 递归执行。
递归基础 n=1 时直接发送 a, b 并验证 P = g^a h^b u^{a·b}。

**安全性直觉**：若证明者能对三个不同挑战 x 都给出可接受的分支，则提取器可通过解线性方程组提取出 a, b, c。若提取失败则意味着找到群中非平凡离散对数关系。该协议满足统计的 witness-extended emulation。

**复杂度**：通信 2·⌈log₂(n)⌉ 个群元素 + 2 个 ℤₚ 元素。证明者计算 O(n) 次群指数，验证者计算 O(n) 次群指数。

#### 2. 对数级范围证明
利用内积论证构造对承诺值 v ∈ [0, 2ⁿ - 1] 的范围证明，核心思想是将范围条件编码为某个多项式恒等式的零次项。

**构造**：
- 证明者将 v 分解为比特向量 a_L ∈ {0,1}ⁿ，并令 a_R = a_L - 1ⁿ。
- 构造两个带随机掩码的多项式：
  l(X) = a_L - z·1ⁿ + s_L·X
  r(X) = yⁿ ∘ (a_R + z·1ⁿ + s_R·X) + z²·2ⁿ
- 计算 t(X) = ⟨l(X), r(X)⟩ = t₀ + t₁·X + t₂·X²。当 a_L, a_R 满足约束时，t₀ 仅依赖于 y, z, v。
- 证明者提交对 t₁, t₂ 的 Pedersen 承诺 T₁, T₂。挑战 x 下发后，证明者打开 t = ⟨l(x), r(x)⟩ 并发送 τ_x, μ, l, r。
- 验证者检查两层关系：t 的承诺一致性，以及 l, r 对 P = A·Sˣ·g⁻ᶻ·h'^{z·yⁿ + z²·2ⁿ} 的打开。

**对数压缩**：将 (58) 步中明文传输 l, r 替换为运行 Protocol 2，通信降至 2⌈log₂n⌉ + 4 群元素 + 5 ℤₚ 元素（共 688 字节对 64 位范围）。

#### 3. 多证明聚合
当同一证明者需为 m 个不同的 vⱼ 同时做范围证明时，Bulletproofs 可聚合：只需将每个 vⱼ 的比特向量 a_{L,j} 拼接为长度为 n·m 的长向量，并相应修改多项式 r(X) 中的偏移项。最终证明尺寸仅随 log₂(m) 增长（增加至 2⌈log₂(n·m)⌉ + 4 群元素），而非线性增长。此性质对 CoinJoin 和 Provisions 场景至关重要。

#### 4. 多方 MPC 协议
允许 m 个互不信任的参与方各自持有秘密值 v_k 和承诺 V_k，通过简单加法同态组合 A⁽ᵏ⁾, S⁽ᵏ⁾, T⁽ᵏ⁾ 等元素，共同生成单个聚合范围证明。消息传递只需一轮线性通信或对数轮对数通信。

#### 5. 通用算术电路证明
将任意算术电路化为 Hadamard 积加线性约束的表示，再通过类似范围证明的多项式检查转换为内积论证。支持将 Pedersen 承诺作为电路输入，无需在电路中实现群指数。通信量为 2⌈log₂n⌉ + 9 群元素 + 6 ℤₚ 元素。

#### 6. 验证优化
- **单次多指数**：重新组织验证方程，归约为一个大小为 2n + 2log₂n + 7 的多指数运算。
- **批验证**：对 m 个独立证明，合并为一个大小为 2n + 2 + m·(2log₂n + 5) 的多指数，边际验证成本近乎线性降低。

### 核心公式与流程

**[改进内积论证递归步]**
$$ \begin{aligned} c_L &= \langle \mathbf{a}_{[:n/2]}, \mathbf{b}_{[n/2:]} \rangle, \quad c_R = \langle \mathbf{a}_{[n/2:]}, \mathbf{b}_{[:n/2]} \rangle \\ L &= \mathbf{g}_{[n/2:]}^{\mathbf{a}_{[n/2:]}} \mathbf{h}_{[n/2:]}^{\mathbf{b}_{[n/2:]}} u^{c_L} \\ R &= \mathbf{g}_{[:n/2]}^{\mathbf{a}_{[n/2:]}} \mathbf{h}_{[n/2:]}^{\mathbf{b}_{[:n/2]}} u^{c_R} \\ \mathbf{g}' &= \mathbf{g}_{[:n/2]}^{x^{-1}} \circ \mathbf{g}_{[n/2:]}^{x} \\ \mathbf{h}' &= \mathbf{h}_{[:n/2]}^{x} \circ \mathbf{h}_{[n/2:]}^{x^{-1}} \\ P' &= L^{x^2} P R^{x^{-2}} \\ \mathbf{a}' &= \mathbf{a}_{[:n/2]} \cdot x + \mathbf{a}_{[n/2:]} \cdot x^{-1} \\ \mathbf{b}' &= \mathbf{b}_{[:n/2]} \cdot x^{-1} + \mathbf{b}_{[n/2:]} \cdot x \end{aligned} $$
> 作用：将对 n 维向量的内积论证降低为对 n/2 维向量的论证，递归下去直至常数大小。

**[范围证明核心检查]**
$$ \begin{aligned} g^t h^{\tau_x} &\stackrel{?}{=} g^{k(y,z) + z \langle \mathbf{1}^n, \mathbf{y}^n \rangle} V^{z^2} T_1^x T_2^{x^2} \\ P &\stackrel{?}{=} h^\mu \mathbf{g}^\mathbf{l} \mathbf{h}'^\mathbf{r} \end{aligned} $$
> 作用：第一式验证承诺值 t 与承诺 V 及辅助承诺 T₁, T₂ 的一致性；第二式验证向量 l, r 与承诺 A, S 及 Pedersen 向量承诺 P 的匹配，两者结合确保 v ∈ [0, 2ⁿ－1]。

**[聚合范围证明验证]**
$$ g^t h^{\tau_x} \stackrel{?}{=} g^{k(y,z) + z\langle\mathbf{1}^{n\cdot m}, \mathbf{y}^{n\cdot m}\rangle} \cdot \mathbf{V}^{\mathbf{z}^2 \cdot \mathbf{z}^m} \cdot T_1^x \cdot T_2^{x^2} $$
> 作用：将多个承诺 Vⱼ 联合纳入验证方程，使一个检查同时确认所有 vⱼ 都在范围内。

### 实验结果

实验环境：Intel i7-6820HQ 2.00 GHz，单线程，内存 < 100 MB。对比基线为 Poelstra 等人的优化方案 [3]（3.8 KB 对 64 位范围）。单 64 位范围证明尺寸 688 字节（[3] 为 3.8 KB），验证时间 3.9 ms。32 个范围聚合后证明尺寸仅 1.0 KB（对比 32× [3] = 121 KB），聚合验证时间 62 ms（均摊 1.9 ms/证明）。边际批验证成本 2.58 ms，低于单个 ECDSA 签名验证（86 μs）。SHA256 原像证明（25400 乘法门）尺寸 1376 字节，验证 833 ms，批验证边际 58 ms。Prover 时间随电路规模线性增长，证明尺寸随乘法门数对数增长。

### 局限性与开放问题
Bulletproofs 的证明和验证时间与电路尺寸线性相关，对极大电路（如数十亿门）可能不够实用；其安全性基于离散对数假设，不抵御量子计算机攻击。如何将批验证技术推广到不同电路的混合场景，以及如何设计更高效的多方证明生成协议（尤其是对任意电路的 MPC 协作），仍是开放问题。

### 强关联论文

[2] G. Maxwell. Confidential transactions. **2016** [Google Scholar](https://scholar.google.com/scholar?q=confidential+transactions)

[3] A. Poelstra, A. Back, M. Friedenbach, G. Maxwell, P. Wuille. Confidential assets. **[Google Scholar](https://scholar.google.com/scholar?q=Confidential+assets)**

[4] E. Ben-Sasson, A. Chiesa, D. Genkin, E. Tromer, M. Virza. SNARKs for C: Verifying program executions succinctly and in zero knowledge. **CRYPTO 2013** [Google Scholar](https://scholar.google.com/scholar?q=SNARKs+for+C)

[6] E. Ben-Sasson, I. Ben-Tov, Y. Horesh, M. Riabzev. Scalable, transparent, and post-quantum secure computational integrity. **2018** [Google Scholar](https://scholar.google.com/scholar?q=Scalable+transparent+and+post+quantum+secure+computational+integrity)

[7] J. Bootle, A. Cerulli, P. Chaidos, J. Groth, C. Petit. Efficient zero-knowledge arguments for arithmetic circuits in the discrete log setting. **EUROCRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+zero+knowledge+arguments+for+arithmetic+circuits+in+the+discrete+log+setting)

[8] A. Poelstra. Mimblewimble. **[Google Scholar](https://scholar.google.com/scholar?q=Mimblewimble)**

[13] S. Noether, A. Mackenzie et al. Ring confidential transactions. **Ledger 2016** [Google Scholar](https://scholar.google.com/scholar?q=Ring+confidential+transactions)

[17] G. Dagher, B. Bünz, J. Bonneau, J. Clark, D. Boneh. Provisions: Privacy-preserving proofs of solvency for Bitcoin exchanges. **2015** [Google Scholar](https://scholar.google.com/scholar?q=Provisions+Privacy+preserving+proofs+of+solvency+for+Bitcoin+exchanges)


## 关键词

+ Bulletproofs
+ 范围证明
+ 非交互式零知识证明
+ 保密交易
+ 无可信设置
+ 离散对数假设