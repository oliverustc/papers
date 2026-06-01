---
title: "Reinforced concrete: A fast hash function for verifiable computation"
doi: 10.1145/3548606.3560686
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2022
created: 2025-04-22 15:12:43
modified: 2025-04-22 15:18:39
---
## Reinforced concrete: A fast hash function for verifiable computation

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3548606.3560686)

## 作者

+ [Lorenzo Grassi](Lorenzo%20Grassi.md)
+ [Dmitry Khovratovich](Dmitry%20Khovratovich.md)
+ Reinhard Lüftenegger 
+ [Christian Rechberger](Christian%20Rechberger.md)
+ Markus Schofnegger 
+ Roman Walch 

## 笔记

### 背景与动机
零知识证明（SNARKs）使可验证计算成为可能，但其性能瓶颈主要源于常规程序（面向比特串）与 SNARK 算术电路（面向大素数域）之间的语义鸿沟。例如，加密货币 Zcash 中需要计算 70 次 SHA-256 哈希，在原生环境下仅需 10 微秒，而生成对应的 SNARK 证明却需 40 秒以上 [3]。为缓解这一瓶颈，学界设计了大量面向素数域的密码原语，如 Poseidon [30]、Rescue [7] 等。然而，当这些哈希函数被用于递归证明（如 Fractal [19]）时，尽管其零知识门数很少，原生 x86 计算速度却极慢（Poseidon 比 SHA-256 慢约 60 倍），导致证明生成总时间反增。本文旨在填补空白：设计一种在零知识证明和原生计算中均快速的哈希函数，尤其适用于集合成员证明（Merkle 树）和递归可验证计算。

### 相关工作

[30] Grassi 等. Poseidon: A New Hash Function for Zero-Knowledge Proof Systems. **Usenix Security 2021** [Google Scholar](https://scholar.google.com/scholar?q=Poseidon+Zero-Knowledge+Proof+Systems)
> 核心思路：采用 Hades 设计策略，全轮 S 盒层与部分 S 盒层交替，最小化乘法复杂度。
> 局限与区别：原生计算性能差（19 μs 处理 512 比特），在递归场景中成为瓶颈。本文通过引入基于查找表的 Bars 层极大提升原生速度。

[7] Aly 等. Design of Symmetric-Key Primitives for Advanced Cryptographic Protocols. **IACR Trans. Symmetric Cryptol. 2020** [Google Scholar](https://scholar.google.com/scholar?q=Design+of+Symmetric-Key+Primitives+for+Advanced+Cryptographic+Protocols)
> 核心思路：基于代换-置换网络，使用低次幂函数作为 S 盒。
> 局限与区别：原生计算极慢（480 μs），且抵抗代数攻击的轮数要求高。本文通过高度非线性的 Bars 层提供更强代数安全性，同时保持高速。

[5] Albrecht 等. Feistel Structures for MPC, and More. **ESORICS 2019** [Google Scholar](https://scholar.google.com/scholar?q=Feistel+Structures+for+MPC)
> 核心思路：推广 MiMC 的 Feistel 结构，使用立方函数作为轮函数。
> 局限与区别：门数较多（1326 R1CS），原生性能一般（38 μs）。本文在门数和原生速度之间取得更好平衡。

[28] Grassi 等. A New Feistel Approach Meets Fluid-SPN: Griffin for Zero-Knowledge Applications. **ePrint 2022/403** [Google Scholar](https://scholar.google.com/scholar?q=Griffin+Zero-Knowledge+Applications)
> 核心思路：融合 Feistel 和 SPN，使用 Quadratic 轮函数与线性层。
> 局限与区别：原生计算较慢（115 μs）。本文利用查找表将原生速度提升至与 Blake2 接近。

[32] Grassi 等. Invertible F_p^n. **ePrint 2021/1695** [Google Scholar](https://scholar.google.com/scholar?q=Invertible+F_p%5En)
> 核心思路：设计置换 Neptune，优化零知识门数。
> 局限与区别：原生性能 20 μs，仍比本文慢 5–18 倍。

[16] Bowe 等. Zcash Orchard: Sinsemilla Gadget. **2021** [Google Scholar](https://scholar.google.com/scholar?q=Sinsemilla+Gadget+Zcash+Orchard)
> 核心思路：基于 Pedersen 哈希的变体，利用 EC 加法中的查找表优化门数。
> 局限与区别：只提供抗碰撞性，缺乏抗原像性；原生计算慢（137 μs）。本文提供抗原像性且原生速度更快。

[3] ZCash protocol specification. **2022** [Google Scholar](https://scholar.google.com/scholar?q=ZCash+protocol+specification)
> 核心思路：定义了 Pedersen 哈希和 Sinsemilla 等原语。
> 局限与区别：Pedersen 哈希依赖离散对数假设且原生速度慢。本文无需强假设。

[36] Hopwood. Zcon0 conference notes. **2019** [Google Scholar](https://scholar.google.com/scholar?q=Zcon0+conference+notes+Hopwood)
> 核心思路：提供了 SHA-256 和 Blake2s 的 R1CS 门数估算。
> 局限与区别：SHA-256 和 Blake2s 在零知识中门数极大（>20000）。本文在门数上减少 50 倍以上。

[12] Bertoni 等. On the Indifferentiability of the Sponge Construction. **EUROCRYPT 2008** [Google Scholar](https://scholar.google.com/scholar?q=On+the+Indifferentiability+of+the+Sponge+Construction)
> 核心思路：提出海绵结构，将固定长度置换转换为可调输出长度的哈希函数。
> 本文基于该结构构建 RC，利用其安全归约性质。

[25] Gabizon 等. plookup: A simplified polynomial protocol for lookup tables. **ePrint 2020/315** [Google Scholar](https://scholar.google.com/scholar?q=plookup+simplified+polynomial+protocol+lookup+tables)
> 核心思路：在 Plonk 中高效支持查找门。
> 本文利用查找门实现 Bars 层，仅需 378 个门。

### 核心技术与方案
整体上，Reinforced Concrete（RC）是一个基于海绵结构 [12] 的哈希函数，其底层置换作用于 $\mathbb{F}_p^3$，提供 128 比特安全性。RC 置换由三组件构成：Bricks（低次非线性置换）、Concrete（仿射扩散层）和 Bars（高次非线性层）。Bricks 与 Concrete 交替排列 6 组，中间嵌入一次 Bars 层，形成“Concrete-Bricks-…-Concrete-Bars-Concrete-…-Concrete-Bricks-Concrete”结构。外围部分（6 个 Bricks+Concrete 对）抵抗统计攻击（如反弹攻击 [41]），中间部分（Bricks-Concrete-Bars-Concrete-Bricks）抵抗代数攻击（如 Gröbner 基 [22]、插值攻击 [37]）。

**Bricks 层** 定义为 $\mathbb{F}_p^3 \to \mathbb{F}_p^3$ 的非线性置换，采用度为 5 的幂次（要求 $\gcd(p-1,5)=1$）与二次多项式组合：
$$
\operatorname{Bricks}(x_1,x_2,x_3) = (x_1^{d},\; x_2(x_1^2+\alpha_1 x_1+\beta_1),\; x_3(x_2^2+\alpha_2 x_2+\beta_2)),
$$
其中 $\alpha_i^2-4\beta_i$ 不是二次剩余，保证可逆性 [28]。

**Concrete 层** 是 $3\times3$ MDS 矩阵乘法加常数：
$$
\text{Concrete}^{(j)}(x) = \begin{pmatrix}2&1&1\\1&2&1\\1&1&2\end{pmatrix}x + c^{(j)}.
$$
矩阵 $M = \operatorname{circ}(2,1,1)$ 对所有 $p\ge 3$ 可逆且 MDS，$c^{(j)}$ 是用 Shake-128 选取的随机常数。

**Bars 层** 是关键创新。它对每个状态字独立应用函数 $\text{Bar}:\mathbb{F}_p\to\mathbb{F}_p$，定义为“分解 - S盒 - 组合”。分解 $\text{Decomp}$ 将 $x\in\mathbb{F}_p$ 表示为 $n$ 个“桶”$x_i\in\mathbb{Z}_{s_i}$，满足 $\prod s_i > p$；组合 $\text{Comp}$ 将 $y_i$ 加权求和模 $p$。S 盒 $S$ 在 $x_i < p'$ 时作用非线性函数 $f$，否则为恒等映射，$p'$ 选为不大于 $\min_i v_i$ 的最大素数，$(v_1,\ldots,v_n)=\text{Decomp}(p-1)$。$f$ 是 $\mathbb{Z}_{p'}$ 上的 MiMC 型置换，保证 Bar 是 $\mathbb{F}_p$ 上的置换（Lemma 3）。

**零知识电路实现** 围绕 Bars 层构建约束系统：(1) 约束 $x = \sum x_i b_i \bmod p$ 和 $y = \sum y_i b_i \bmod p$；(2) 用变量 $z_i$ 标记 $x_i$ 是否小于 $p'$，并用表 $T_2$ 约束 $z_i$ 为二进制；(3) 用变量 $c_i$ 标记“溢出”状态，由有限状态自动机 $\mathcal{A}$ 描述，并用表 $T_3$ 约束 $c_i$ 序列合法；(4) 用表 $T_1$ 约束 $(x_i,\; i\cdot z_i,\; y_i,\; c_i)$ 对应正确 S 盒输出和溢出标志。总查找门数约为 $1.59n$，对 BLS12-381/BN254 实例 $n=27$，门数约 378。系统满足完备性（Lemma 1）和可靠性（Lemma 2），即 $y=\text{Bar}(x)$ 当且仅当存在中间变量满足所有约束。

**安全性论证** 分为统计和代数两方面：统计攻击（差分、线性、反弹）受限于 Bricks+Concrete 层提供的扩散，作者证明 5 轮以上无法反弹攻击，且当前设计有至少 2 轮安全裕度；代数攻击（Gröbner 基、插值攻击）因 Bars 层的高次性和基于查找表的非多项式表示而失效，对 10 比特弱化版本已有实验验证。整体碰撞/原像安全目标为 $2^{128}$ 次域操作。

### 核心公式与流程

**Bricks 层**
$$
\operatorname{Bricks}(x_1,x_2,x_3) = (x_1^{d},\; x_2(x_1^2+\alpha_1 x_1+\beta_1),\; x_3(x_2^2+\alpha_2 x_2+\beta_2))
$$
> 作用：提供低次非线性扩散，抵抗统计攻击。要求 $d=5$ 且 $\alpha_i^2-4\beta_i$ 非二次剩余以保证可逆。

**Concrete 层**
$$
\text{Concrete}^{(j)}(x) = \begin{pmatrix}2&1&1\\1&2&1\\1&1&2\end{pmatrix}x + c^{(j)}
$$
> 作用：用 MDS 矩阵实现全扩散，常数 $c^{(j)}$ 打破对称性。

**Bar 函数**
$$
\text{Bar} = \text{Comp} \circ \text{SBox} \circ \text{Decomp}
$$
其中 Decomp 将 $x$ 写为 $x = \sum x_i \prod_{j>i} s_j$，S 盒独立作用每个 $x_i$（若 $x_i<p'$ 则用 $f$，否则恒等），Comp 加权求和模 $p$。
> 作用：通过查找表实现高次非线性，抵抗代数攻击。在零知识电路中用约 $1.59n$ 个查找门实现。

**RC 置换（完整）**
$$
\begin{aligned}
RC := &\text{Concrete}^{(8)} \circ \text{Bricks} \circ \text{Concrete}^{(7)} \\
&\circ \text{Bricks} \circ \text{Concrete}^{(6)} \circ \text{Bricks} \\
&\circ \text{Concrete}^{(5)} \circ \text{Bars} \circ \text{Concrete}^{(4)} \\
&\circ \text{Bricks} \circ \text{Concrete}^{(3)} \circ \text{Bricks} \\
&\circ \text{Concrete}^{(2)} \circ \text{Bricks} \circ \text{Concrete}^{(1)}
\end{aligned}
$$
> 作用：海绵的底层层叠，外层 6 组 Bricks+Concrete 抗统计攻击，中间 Bars 层抗代数攻击。

### 实验结果
本文用 Rust 实现了 RC 及其对比方案，测试平台为 Intel i7-4790（3.6 GHz），所有哈希函数输入 512 比特（对应 RC 一次置换，处理两个 $\mathbb{F}_p$ 元素）。主要结果见表 2：在 BN254 域上，RC 耗时 3419 ns，Poseidon 耗时 19944 ns（RC 快 5.8 倍），Rescue 耗时 470030 ns（RC 快 137 倍），Feistel-MiMC 耗时 37980 ns（RC 快 11 倍），Griffin 耗时 113670 ns（RC 快 33 倍），Neptune 耗时 20265 ns（RC 快 5.9 倍）。在特制域 $p_{ST}$ 上，RC 仅需 1087 ns，比 Poseidon 快 16.7 倍，比 Blake2s（213 ns）慢约 5 倍，但 Blake2s 的 Plookup 门数是 RC 的 7 倍。Merkle 树累积实验（表 3）进一步印证：构建 $2^{20}$ 个叶子的树，RC 在 BN254 上需 3.91 s，而 Poseidon 需 22.6 s，SHA-256 需 0.624 s，RC 的额外开销仅约 6 倍，远超其他零知识友好哈希。零知识门数方面，RC 需要 378 个 Plookup 门，Poseidon 需要 633 个常规门，Rescue 需要 480 个门；面积-度积 RC 为 5670，Poseidon 为 9495，Rescue 为 7200。整体表明 RC 在原生性能和零知识效率之间取得了前所未有的平衡。

### 局限性与开放问题
当前 RC 依赖证明系统支持查找门（如 Plookup [25]、Halo2 [3]），若不支持则电路规模可达约 5000 约束，失去优势。Bars 层的分解参数需针对每个域单独设计（如 BLS12-381 和 BN254 的桶大小不同），缺乏通用性；未来可研究自动生成或统一参数的方法。另外，当前设计仅提供海绵结构实例，非海绵形式的 RC（如可逆加密模式）尚未探索，不同场景下是否可进一步优化需后续工作。

### 强关联论文

[30] Grassi 等. Poseidon: A New Hash Function for Zero-Knowledge Proof Systems. **Usenix Security 2021** [Google Scholar](https://scholar.google.com/scholar?q=Poseidon+Zero-Knowledge+Proof+Systems)

[7] Aly 等. Design of Symmetric-Key Primitives for Advanced Cryptographic Protocols. **IACR Trans. Symmetric Cryptol. 2020** [Google Scholar](https://scholar.google.com/scholar?q=Design+of+Symmetric-Key+Primitives+for+Advanced+Cryptographic+Protocols)

[5] Albrecht 等. Feistel Structures for MPC, and More. **ESORICS 2019** [Google Scholar](https://scholar.google.com/scholar?q=Feistel+Structures+for+MPC)

[28] Grassi 等. A New Feistel Approach Meets Fluid-SPN: Griffin for Zero-Knowledge Applications. **ePrint 2022/403** [Google Scholar](https://scholar.google.com/scholar?q=Griffin+Zero-Knowledge+Applications)

[32] Grassi 等. Invertible F_p^n. **ePrint 2021/1695** [Google Scholar](https://scholar.google.com/scholar?q=Invertible+F_p%5En)

[16] Bowe 等. Zcash Orchard: Sinsemilla Gadget. **2021** [Google Scholar](https://scholar.google.com/scholar?q=Sinsemilla+Gadget+Zcash+Orchard)

[3] ZCash protocol specification. **2022** [Google Scholar](https://scholar.google.com/scholar?q=ZCash+protocol+specification)

[36] Hopwood. Zcon0 conference notes. **2019** [Google Scholar](https://scholar.google.com/scholar?q=Zcon0+conference+notes+Hopwood)

[12] Bertoni 等. On the Indifferentiability of the Sponge Construction. **EUROCRYPT 2008** [Google Scholar](https://scholar.google.com/scholar?q=On+the+Indifferentiability+of+the+Sponge+Construction)

[25] Gabizon 等. plookup: A simplified polynomial protocol for lookup tables. **ePrint 2020/315** [Google Scholar](https://scholar.google.com/scholar?q=plookup+simplified+polynomial+protocol+lookup+tables)


## 关键词

+ 哈希函数
+ 零知识证明
+ 可验证计算
+ 密码学原语
+ 素数域