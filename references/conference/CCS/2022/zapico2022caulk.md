---
title: "Caulk: Lookup arguments in sublinear time"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2022
created: 2025-04-16 09:42:16
modified: 2025-04-16 09:44:28
---

## Caulk: Lookup arguments in sublinear time

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3548606.3560646)

## 作者

+ Arantxa Zapico 
+ Vitalik Buterin 
+ [Dmitry Khovratovich](Dmitry%20Khovratovich.md)
+ [Mary Maller](Mary%20Maller.md)
+ Anca Nitulescu 
+ Mark Simkin 

## 笔记

### 背景与动机
零知识集合成员证明和查找论证是隐私保护应用（如匿名支付、可验证计算）的核心基础。传统方案存在显著效率瓶颈：基于 Merkle 树加 SNARK 的方法虽然渐近复杂度为对数级别，但实际开销巨大，例如 Zcash 早期使用 SHA-2 的 Merkle 树导致证明时间高达 40 秒，即使改用代数哈希（如 Poseidon）也仅能加速一个数量级。另一类方案依赖于 RSA 累加器或配对，但往往需要隐藏阶群或线性大小的公共参数。对于查找表场景，Plookup 协议要求证明者计算量至少与表的大小 N 成线性关系，无论实际查找的元素数量 m 是多少。这些高计算开销严重限制了系统的可扩展性和实际部署。本文提出的 Caulk 方案旨在填补这个空白，实现证明时间与表大小呈亚线性关系（对单个元素证明为 O(log N)，对 m 个元素查找为 O(m² + m log N)），从而突破现有方案的性能瓶颈。

### 相关工作

[5] Benarroch 等. Zero-knowledge proofs for set membership: Efficient, succinct, modular. **FC 2021** [Google Scholar](https://scholar.google.com/scholar?q=Zero-knowledge+proofs+for+set+membership%3A+Efficient%2C+succinct%2C+modular)
> 核心思路：基于 PST 向量承诺方案实现位置隐藏链接性，通过打开公共多项式在隐藏位置的值来证明元素属于集合。
> 局限与区别：证明大小和验证者计算量均为 O(log N)，需要 log N 次配对操作。Caulk 在此基础上实现了常数大小的证明和常数次配对验证。

[10] Camenisch 和 Lysyanskaya. Dynamic accumulators and application to efficient revocation of anonymous credentials. **CRYPTO 2002** [Google Scholar](https://scholar.google.com/scholar?q=Dynamic+accumulators+and+application+to+efficient+revocation+of+anonymous+credentials)
> 核心思路：设计基于 RSA 累加器的知识证明协议，将 Pedersen 承诺与累加器关联，用于证明元素属于某个大集合。
> 局限与区别：需要隐藏阶群，群元素尺寸远大于标准椭圆曲线群（如 2048 位 vs 256 位），导致计算和通信开销大。Caulk 使用标准双线性群，参数更小。

[11] Campanelli 等. Succinct zero-knowledge batch proofs for set accumulators. **IACR ePrint 2021** [Google Scholar](https://scholar.google.com/scholar?q=Succinct+zero-knowledge+batch+proofs+for+set+accumulators)
> 核心思路：为 RSA 累加器设计位置隐藏链接性方案，证明时间不依赖于累加器大小。
> 局限与区别：仍需 RSA 模数或类群，涉及结构化设置。Caulk 只需通用的 power-of-tau 设置，在标准双线性群中实现。

[16] Gabizon 和 Williamson. plookup: A simplified polynomial protocol for lookup tables. **IACR ePrint 2020** [Google Scholar](https://scholar.google.com/scholar?q=plookup%3A+A+simplified+polynomial+protocol+for+lookup+tables)
> 核心思路：构造多项式协议，将表格值编码到多项式根中，通过证明两个多项式乘法关系来实现查找。
> 局限与区别：证明者时间至少为 O(N)，与表大小成正比，即使只查找少量元素。Caulk 的证明者时间与表大小呈亚线性。

[29] ZCash Protocol Specification. **ZCash 2022** [Google Scholar](https://scholar.google.com/scholar?q=ZCash+protocol+specification)
> 核心思路：使用 SHA-2 的 Merkle 树结合 Groth16 SNARK 实现匿名交易，证明树中某个叶子的存在。
> 局限与区别：由于 SHA-2 的电路规模巨大，证明时间约 40 秒。Caulk 使用 KZG 承诺和代数结构，避免了复杂哈希运算。

### 核心技术与方案
Caulk 的整体框架基于 KZG 多项式承诺方案。向量 C 被编码为多项式 C(X) = Σ c_i λ_i(X)，其 中 λ_i 是单位根 H = {1, ω, ..., ω^{N-1}} 的 Lagrange 插值基。打开向量中第 i 个元素等价于证明多项式在点 ω^{i-1} 处的取值。

对于单个元素证明（m=1），核心思路是将标准 KZG 打开过程进行盲化。具体地，证明者不直接透露秘密位置 ω^{i-1} 和值 v，而是构造一个盲化的线性多项式 z(X) = a(X - ω^{i-1})，其中 a 是随机盲化因子。然后计算盲化的商多项式 T(X) 和辅助多项式 S(X)，使得配对方程 e(C - cm, [1]₂) = e([T]₁, [z]₂) + e([h]₁, [S]₂) 成立。cm = [v + hr]₁ 是 Pedersen 承诺，h 是另一个生成元。该方程在代数上等价于 C(X) - v - hr = T(X)z(X) + hS(X)，通过构造 T(X) = Q(X)/a + sh 和 S(X) = -r - sz(X) 可以消去盲化项和随机项，恢复出 KZG 打开关系 C(X) - v = Q(X)(X - ω^{i-1})。为了证明 z(X) 确实形如 a(X - ω^{i-1}) 且 ω^{i-1} 是 N 次单位根，引入了辅助多项式 f(X)（定义在大小为 log(N)+6 的小单位根群 Vₙ 上），通过一系列约束（如 f(σ²)(1-σ) = f(1)-f(σ)，f(σ⁴⁺ⁱ⁺¹) = f(σ⁴⁺ⁱ)²，最后 f(σ⁵⁺ˡᵒᵍ⁽ᴺ⁾σ⁻¹) = 1）来证明 b/a 是 N 次单位根。这个子协议 R_unity 提供了对知识 a、b 的零知识论证。安全性基于 KZG 的可靠性和代数群模型下的 q-SDH 假设和离散对数假设。通信开销为 6 G₁、2 G₂、4 F，验证者进行常数次（4 次）配对。

对于多个元素查找（m>1），方案扩展为两个 KZG 承诺之间的位置隐藏链接性，即证明 cm（包含 m 个元素）中的所有元素都属于 C（包含 N 个元素）。证明者首先确定元素在 C 中出现的索引集合 I，构造子多项式 C_I(X) 和零化多项式 z_I(X)。核心是证明三个关键多项式方程：C(X) - C_I(X) = z_I(X)H₁(X)（证明子集的正确性，可通过预计算所有单个位置的 KZG 证明并聚合得到 H₁ 的承诺，聚合代价 O(|I| log² |I|)）；z_I(u(X)) = z_{Vₘ}(X)H₂(X)（证明 u(X) 编码的单位根集合是 z_I(X) 的根集，其中 u(X) 是另一个多项式，其系数是 I 对应的单位根，该方程通过子协议 R_unity' 实现，R_unity' 使用多层平方关系聚合证明所有系数都是 N 次单位根，这需要 O(m log N) 的时间）；C_I(u(X)) - φ(X) = z_{Vₘ}(X)H₃(X)（证明两个承诺编码相同的值集，仅基不同）。这三个方程通过随机挑战 χ 聚合成一个验证方程。该协议的证明大小为 14 G₁、1 G₂、4 F。验证者只需要进行常数次（4 次）配对操作。证明者时间复杂度为 O(m² + m log N)，其中二次项主要来源于计算 H₂(X) 和 H₃(X)。预计算所有 KZG 单个打开证明需要 O(N log N) 的 G₂ 群运算。安全性依赖于 q-SDH、q-DHE 和 q-SFrac 假设。

### 核心公式与流程

**[单元素证明的验证方程]**
$$e(C - \mathrm{cm}, [1]_2) = e([T]_1, [z]_2) + e([h]_1, [S]_2)$$
> 作用：验证盲化后的 KZG 打开关系成立。C 是向量承诺，cm 是 Pedersen 承诺，T 是盲化商多项式，z 是盲化线性多项式，S 是辅助多项式用于消除盲化项。

**[查找证明的验证方程]**
$$e([C]_1 - [C_I]_1, [1]_2) = e([z_I]_1, [H_1]_2)$$
> 作用：验证子集 I 对应的子承诺 C_I 确实是原始承诺 C 的一部分，即存在多项式 H₁ 使得 C(X) - C_I(X) = z_I(X) H₁(X)。

**[证明系数为单位根的聚合方程]**
$$\begin{aligned}
p(X,Y) = &(u(X)\rho_1(Y) + \bar{U}(X,Y))^2 - h_1(X)z_{\mathbb{V}_n}(Y) \\
&- (\bar{U}(X, Y\sigma) + \mathrm{id}(X)\rho_n(Y)) - z_{\mathbb{V}_m}(X)h_2(X,Y)
\end{aligned}$$
> 作用：聚合证明多项式 u(X) 的所有系数（在 V_m 的 Lagrange 基下）都是 N 次单位根的多层约束。u(X) 编码了被查找元素的索引位置对应的单位根。

**[证明查找值和索引的聚合方程]**
$$z_I(u(\alpha)) + \chi(C_I(u(\alpha)) - \phi(\alpha)) = z_{\mathbb{V}_m}(\alpha) H_2(\alpha)$$
> 作用：通过随机挑战 χ 聚合两个验证：1) u(X) 的系数是 z_I(X) 的根；2) C_I(X) 和 φ(X) 在对应点取值相同。φ(X) 是编码了被查找元素的多项式。

### 实验结果
实验运行于配备 Intel i7-8565U CPU 和 8GB RAM 的笔记本。对于单元素成员证明（表 2），Caulk 的证明时间在 N=2⁶ 到 N=2²² 范围内从 0.0164s 到 0.0299s，几乎不随表大小增长。与 Merkle-Poseidon 树（MT-Pos）相比，当 N=2²² 时，Caulk 快约 300 倍（0.03s vs 8.953s）。与 Merkle-SHA-2 树（MT-SHA）相比，快约 5000 倍。与 RSA 累加器（Harisa）相比，Caulk 的证明时间更小（0.03s vs 0.029s 持平），但证明尺寸更小（0.6KB vs 1.17KB）。验证者时间所有方案接近，Caulk 约 0.01s。对于多元素查找（表 3），当 N=2²⁰ 且 m=50 时，Caulk 的证明时间为 2.767s，而 MT-Pos-20 为 271.4s，加速约 98 倍。Harisa 随 m 线性增长（m=50 时 6.011s），Caulk 的二次项在 m 较大时使性能下降，但在 m 较小时（如 m=10）仍优于 Harisa（0.565s vs 1.228s）。预计算时间（表 4）为 O(N log N)，N=2²⁰ 时需要约 9.1 小时。

### 局限性与开放问题
Caulk 的核心局限之一是证明者需要 O(N) 的存储空间来保存所有预计算的 KZG 打开证明，对于 N 极大的表格（如 2³⁰）这会造成严重的存储压力。其次，查找证明的证明时间具有 O(m²) 项，当被查找元素数量 m 较大时（如数百或数千），二次复杂度会迅速占主导，使效率低于线性方案。此外，协议的设置依赖于通用的 power-of-tau 仪式，虽然可更新，但仍需一次初始的信任设置。未来工作可探索有损压缩预计算数据的方法，或通过批处理和更高效的聚合技术降低二次复杂度，以及设计完全无设置的方案。

### 强关联论文

[5] Benarroch 等. Zero-knowledge proofs for set membership: Efficient, succinct, modular. **FC 2021** [Google Scholar](https://scholar.google.com/scholar?q=Zero-knowledge+proofs+for+set+membership%3A+Efficient%2C+succinct%2C+modular)

[10] Camenisch 和 Lysyanskaya. Dynamic accumulators and application to efficient revocation of anonymous credentials. **CRYPTO 2002** [Google Scholar](https://scholar.google.com/scholar?q=Dynamic+accumulators+and+application+to+efficient+revocation+of+anonymous+credentials)

[11] Campanelli 等. Succinct zero-knowledge batch proofs for set accumulators. **IACR ePrint 2021** [Google Scholar](https://scholar.google.com/scholar?q=Succinct+zero-knowledge+batch+proofs+for+set+accumulators)

[16] Gabizon 和 Williamson. plookup: A simplified polynomial protocol for lookup tables. **IACR ePrint 2020** [Google Scholar](https://scholar.google.com/scholar?q=plookup%3A+A+simplified+polynomial+protocol+for+lookup+tables)

[21] Kate 等. Constant-size commitments to polynomials and their applications. **ASIACRYPT 2010** [Google Scholar](https://scholar.google.com/scholar?q=Constant-size+commitments+to+polynomials+and+their+applications)

[27] Tomescu 等. Aggregatable subvector commitments for stateless cryptocurrencies. **SCN 2020** [Google Scholar](https://scholar.google.com/scholar?q=Aggregatable+subvector+commitments+for+stateless+cryptocurrencies)

[29] ZCash Protocol Specification. **ZCash 2022** [Google Scholar](https://scholar.google.com/scholar?q=ZCash+protocol+specification)


## 关键词

+ 向量承诺
+ 查找论证
+ 零知识证明
+ 成员资格
+ 可验证计算