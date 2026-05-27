---
title: "Hyperplonk: Plonk with linear-time prover and high-degree custom gates"
doi: 10.1007/978-3-031-30617-4_17
标题简称: Hyperplonk
论文类型: conference
会议简称: EUROCRYPT
发表年份: 2023
modified: 2025-04-20 21:07:58
created: 2025-04-07 16:51:57
---
## Hyperplonk: Plonk with linear-time prover and high-degree custom gates

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-30617-4_17)

## 作者

+ [Binyi Chen](Binyi%20Chen.md)
+ [Benedikt Bünz](Benedikt%20Bünz.md)
+ [Dan Boneh](Dan%20Boneh.md)
+ [Zhenfei Zhang](Zhenfei%20Zhang.md)

## 笔记

### 背景与动机
简洁非交互式知识论证（SNARK）是密码学与复杂性理论长期研究的核心问题，近年效率的大幅提升催生了众多现实应用。Plonk 系统因证明极短（约 400 字节）且验证快速而成为工业界最广泛采用的 SNARK 之一，同时支持自定义门和查找门等灵活约束。然而 Plonk 的证明者复杂度为 $O_\lambda(s \log s)$，其中 $s$ 是电路门数，瓶颈源于对 $O(s)$ 次单变量多项式的大规模 FFT 与多指数运算。当电路规模 $s > 2^{20}$ 时，FFT 的准线性时间显著拖累证明速度；若引入高次自定义门，所需 FFT 与多指数运算的规模正比于门次数 $d$，进一步恶化性能。现有一些方案通过放弃 Plonk 框架以消除 FFT [17, 25, 32, 43, 51]，但牺牲了 Plonk 的灵活性与短证明优势。HyperPlonk 旨在保留 Plonk 的灵活性的同时消除 FFT 并高效支持高次自定义门，填补了线性时间证明与高次约束兼容性的空白。

### 相关工作

[27] Gabizon 等. PLONK: Permutations over Lagrange-bases for Oecumenical Noninteractive Arguments of Knowledge. **ePrint 2019**
> 核心思路：基于循环子群上的单变量多项式 IOP，通过置换论证实现接线约束，支持低次自定义门。
> 局限与区别：证明者需进行 $O(s \log s)$ FFT，高次门导致多项式度数为 $O(s d)$，运算量过大。HyperPlonk 改用超立方体上的多线性 IOP，消除 FFT 并降低高次门开销。

[29] Gabizon 等. plookup: a simplified polynomial protocol for lookup tables. **ePrint 2020**
> 核心思路：利用循环群上的线性 next 函数，通过排序与乘积论证实现查找表包含证明。
> 局限与区别：next 函数依赖循环群的线性结构，超立方体上不存在线性遍历函数。HyperPlonk 构建二次生成函数并线性化，适配超立方体。

[43] Setty. Spartan: efficient and general-purpose zkSNARKs without trusted setup. **CRYPTO 2020**
> 核心思路：基于 R1CS 与多线性扩展，利用 SumCheck 实现线性时间证明者，无 FFT。
> 局限与区别：Spartan 采用 R1CS 约束，不支持 Plonk 风格的自定义门与查找门。HyperPlonk 采用 Plonk 风格约束系统，提供更高灵活性。

[51] Xie 等. Orion: zero knowledge proof with linear prover time. **CRYPTO 2022** (also ePrint 2022/1010)
> 核心思路：基于张量编码与线性码的线性时间多线性承诺方案，证明大小 $O(\lambda \mu^2)$。
> 局限与区别：Orion 证明大小达数 MB（$\mu=27$ 约 6 MB）。HyperPlonk 的改进 Orion+ 将证明缩小至约 7 KB（$\mu=25$），几乎提升 1000 倍。

[55] Zhang 等. Transparent polynomial delegation and its applications to zero knowledge proof. **IEEE S&P 2020**
> 核心思路：基于 FRI 的多线性多项式承诺方案，递归实现，证明者时间准线性。
> 局限与区别：复杂度和证明大小较高。HyperPlonk 利用张量积单变量 IOP [17] 将 FRI 直接转化为多线性承诺，更简单高效。

[44] Setty, Lee. Quarks: quadruple-efficient transparent zkSNARKs. **ePrint 2020**
> 核心思路：基于超立方体的乘积检查与 SumCheck，实现透明 SNARK。
> 局限与区别：Quarks 使用 R1CS 约束且证明规模较大。HyperPlonk 借鉴其 ProductCheck 技巧，但用于 Plonk 风格的置换与门约束。

[17] Bootle 等. Gemini: elastic SNARKs for diverse environments. **EUROCRYPT 2022**
> 核心思路：通过张量积将单变量多项式 IOP 转化为多线性 IOP，实现线性时间证明者。
> 局限与区别：Gemini 报告证明 18 KB（$\mu=20$），HyperPlonk 可做到 4.7 KB。HyperPlonk 还利用该转化改进 FRI 多线性承诺。

[48] Wahby 等. Doubly-efficient zkSNARKs without trusted setup. **IEEE S&P 2018**
> 核心思路：使用离散对数上的多线性承诺，证明者时间线性。
> 局限与区别：证明大小 $O(\log n)$ 群元素，但证明者需大量群运算。HyperPlonk 结合更高效的多线性承诺可进一步优化。

[40] Papamanthou 等. Signatures of correct computation. **TCC 2013**
> 核心思路：基于双线性群的 KZG 式多线性多项式承诺，证明 $O(\mu)$ 群元素。
> 局限与区别：需要通用可信设置。HyperPlonk 将其作为可选项，并利用其实现小证明（约 5 KB）。

[32] Golovnev 等. Brakedown: linear-time and post-quantum SNARKs for R1CS. **ePrint 2021**
> 核心思路：基于线性码与张量积的线性时间证明者，后量子安全。
> 局限与区别：证明大小 $O(\sqrt{n})$。HyperPlonk 的 Orion+ 改进进一步压缩至 $O(\mu)$。

### 核心技术与方案

**整体框架**：HyperPlonk 是一个多线性 IOP（PolyIOP），可编译为 SNARK。它将 Plonk 的约束系统从循环子群移植到布尔超立方体 $B_\mu = \{0,1\}^\mu$ 上。约束分为门约束与接线约束，分别通过零检查 IOP 和置换 IOP 验证；查找门通过超立方体 Plookup 实现；多个多项式开点通过新的批处理协议 BatchEval 归约到单个 SumCheck。

**门约束**：给定电路 $\mathcal{C}[G]$，定义三个选择器多项式 $S_1,S_2,S_3 : \mathbb{F}^\mu \to \{0,1\}$ 和一个接线置换 $\sigma : B_{\mu+2} \to B_{\mu+2}$。门约束要求对所有 $\mathbf{x} \in B_\mu$ 满足一个多项式恒等式，它混合了加法、乘法、自定义门 $G$ 以及输入多项式 $I$。通过零检查 IOP（基于 SumCheck）证明该恒等式在超立方体上恒为零。零检查 IOP 中每轮证明者发送一个次数至多 $d$ 的单变量多项式承诺，而非明文多项式，这极大压缩了通讯量。证明者总工作量约为 $O(2^\mu d \log^2 d)$ 域运算，而传统 Plonk 需要 $O(s d)$ 群指数。

**接线约束**：接线约束等价于矩阵 $\hat{M}$ 中特定单元格值相等，表达为置换 $\sigma$ 下 $M(\mathbf{x}) = M(\sigma(\mathbf{x}))$。通过多集合相等检查 IOP（MsetCheck）证明两集合 $\{([\mathbf{x}], M(\mathbf{x}))\}$ 与 $\{([\sigma(\mathbf{x})], M(\mathbf{x}))\}$ 相等。MsetCheck 利用随机挑战 $r$ 将问题归约为乘积检查（ProductCheck），后者再归约为零检查（进而归约为 SumCheck）。整个接线约束不再需要 FFT。

**查找门（HyperPlonk+）**：超立方体上不存在线性遍历函数，因此构建了二次生成函数 $g_\mu : B_\mu \to B_\mu$，通过有限域 $\mathbb{F}_{2^\mu}$ 的本原多项式定义。直接复合 $f(g(\cdot))$ 会提升度数，通过定义线性化多项式 $f_{\Delta_\mu}$，使其在超立方体上等于 $f \circ g_\mu$，从而保持度数不增。查找约束通过构建扩展向量 $\mathbf{h}$（每个表元素重复次数为出现次数加一）并运行 MsetCheck 验证，证明 $f(B_\mu) \subseteq t(B_\mu)$。

**批开点协议**：多个多线性多项式在不同点上的开点可以归约为单个 SumCheck。给定 $k$ 个 $\mu$ 变量多项式 $f_i$ 及开点 $\mathbf{z}_i$，验证者发送随机向量 $\mathbf{t} \in \mathbb{F}^\ell$（$k=2^\ell$），构造 $\tilde{g}$ 和 $\tilde{eq}$ 使得 $\sum_{(i,\mathbf{b})} \tilde{g}(\langle i\rangle,\mathbf{b}) \tilde{eq}(\langle i\rangle,\mathbf{b}) = \sum_i eq(\mathbf{t},\langle i\rangle) y_i$。然后运行一个关于 $g^* = \tilde{g} \cdot \tilde{eq}$ 的 SumCheck。证明者复杂度为 $O(k 2^\mu)$，优于先前 $O(k^2 \mu 2^\mu)$。

**Orion+ 改进**：针对 Orion 承诺方案证明过大的问题，使用多线性承诺（如 KZG）对列哈希进行承诺，利用 CP-SNARK 技术将外层的 Merkle 证明替换为 SNARK 证明，从而将证明大小从 $O(\lambda \mu^2)$ 降至 $O(\mu)$。对于 $\mu=25$，证明大小约 7 KB（Orion 为 5.5 MB），同时保持证明者线性时间。

**安全性**：各基本 IOP（SumCheck、ZeroCheck、ProdCheck、MsetCheck、PermCheck、Lookup、BatchEval）均满足完美完备性和可忽略的可靠性误差（如 $O(d\mu/|\mathbb{F}|)$ 或 $O((2^\mu + d\mu)/|\mathbb{F}|)$）。HyperPlonk 整体可靠性误差为 $O((2^\mu + d\mu)/|\mathbb{F}|)$。编译步骤使用多项式承诺方案的见证扩展仿真，保持知识健壮性。

### 核心公式与流程

**[多线性多项式与超立方体编码]**
$$
M(0,0,\langle i\rangle) = L_i,\quad M(0,1,\langle i\rangle) = R_i,\quad M(1,0,\langle i\rangle) = O_i,\quad i=0,\dots,2^\mu-1.
$$
> 作用：将 Plonk 的 $3 \times 2^\mu$ 个矩阵单元格编码为一个 $\mu+2$ 元多线性多项式 $M$，各比特位分别对应左输入、右输入、输出。

**[门恒等式]**
$$
0 = S_1(\mathbf{x})(L_{\mathbf{x}}+R_{\mathbf{x}}) + S_2(\mathbf{x}) L_{\mathbf{x}} R_{\mathbf{x}} + S_3(\mathbf{x}) G(L_{\mathbf{x}},R_{\mathbf{x}}) - O_{\mathbf{x}} + I(\mathbf{x}),\quad \forall \mathbf{x}\in B_\mu.
$$
> 作用：使用三个选择器多项式区分加法门、乘法门、自定义门 $G$ 及输入约束，将电路正确性归约为一个多线性多项式在超立方体上恒为零。

**[线性化生成函数 $f_{\Delta_\mu}$]**
$$
f_{\Delta_\mu}(\mathbf{X}_1,\dots,\mathbf{X}_\mu) := \mathbf{X}_\mu \cdot f(1,\mathbf{X}_1',\dots,\mathbf{X}_{\mu-1}') + (1-\mathbf{X}_\mu) \cdot f(0,\mathbf{X}_1,\dots,\mathbf{X}_{\mu-1}),
$$
其中 $\mathbf{X}_i' = 1-\mathbf{X}_i$ 若 $i\in S$（本原多项式的指数集），否则 $\mathbf{X}_i'=\mathbf{X}_i$。
> 作用：在超立方体上模拟生成函数 $g_\mu$ 的复合 $f(g_\mu(\mathbf{x}))$，且保持每个变量次数为 $d$，可通过两次 $f$ 求值得到。

**[BatchEval 归约公式]**
$$
\sum_{i\in[k]} eq(\mathbf{t},\langle i\rangle) \cdot \left(\sum_{\mathbf{b}\in B_\mu} f_i(\mathbf{b})\, eq(\mathbf{b},\mathbf{z}_i) - y_i\right) = 0.
$$
> 作用：通过随机向量 $\mathbf{t}$ 将 $k$ 个开点验证线性组合为单个 SumCheck，新多项式 $g^* = \tilde{g} \cdot \tilde{eq}$ 次数仅为 2。

### 实验结果
实验采用 BLS12-381 曲线（配对友好）实现 HyperPlonk 原型，并与 Jellyfish Plonk（一个优化的商业级 Plonk 实现）和 Spartan [43] 对比。对于小电路（144 门，3-to-1 Rescue Hash），HyperPlonk 证明者耗时 88 ms，Jellyfish 为 40 ms，Spartan 为 422 ms。对于中等规模电路（Zexe 递归电路，R1CS 约束 $2^{22}$，Plonk+ 约束 $2^{17}$），HyperPlonk 耗时 5.1 s，Jellyfish 13.1 s，Spartan 6 分钟。对于大电路（Rollup of 50 private tx，R1CS 约束 $2^{25}$，Plonk+ 约束 $2^{20}$），HyperPlonk 仅需 38.2 s，Jellyfish 110 s，Spartan 39 分钟。结果表明 HyperPlonk 在大电路上超越 Jellyfish 约 2-3 倍，超越 Spartan 超过 60 倍。证明大小方面，使用 KZG 多线性承诺 [40] 时，对于 $\mu=20$ 的证明约 4.7 KB，$\mu=25$ 约 5.5 KB。作为对比，Kopis [44] 和 Gemini [17] 报告 $\mu=20$ 时分别为 39 KB 和 18 KB。Orion+ 改进后的承诺方案在 $\mu=25$、128 位安全下证明约 7 KB，而原 Orion 为 5.5 MB，缩小近 1000 倍。

### 局限性与开放问题
HyperPlonk 的证明大小依赖于底层多线性承诺方案，使用 KZG 时需要通用可信设置；使用 FRI 变体可透明但证明更大（约 250 KB）。Orion+ 仍需要通用设置才能实现极小证明。对于超大电路（$\mu > 30$），SumCheck 的轮数与超立方体维度 $\mu$ 成正比，可能带来延迟问题。如何进一步将电路约束系统扩展到支持更丰富的算术化（如带有范围约束的查找）且保持线性时间，是未来工作。此外，零知识性质的实现与优化在论文中未详细展开，实际部署需额外处理。

### 强关联论文

[27] Gabizon, A., Williamson, Z.J., Ciobotaru, O. PLONK: permutations over lagrange-bases for oecumenical noninteractive arguments of knowledge. **ePrint 2019** [Google Scholar](https://scholar.google.com/scholar?q=PLONK+permutations+over+lagrange+bases+for+oecumenical+noninteractive+arguments+of+knowledge)

[29] Gabizon, A., Williamson, Z.J. plookup: a simplified polynomial protocol for lookup tables. **ePrint 2020** [Google Scholar](https://scholar.google.com/scholar?q=plookup+a+simplified+polynomial+protocol+for+lookup+tables)

[43] Setty, S. Spartan: efficient and general-purpose zkSNARKs without trusted setup. **CRYPTO 2020** [Google Scholar](https://scholar.google.com/scholar?q=Spartan+efficient+and+general+purpose+zkSNARKs+without+trusted+setup)

[51] Xie, T., Zhang, Y., Song, D. Orion: zero knowledge proof with linear prover time. **CRYPTO 2022** [Google Scholar](https://scholar.google.com/scholar?q=Orion+zero+knowledge+proof+with+linear+prover+time)

[55] Zhang, J., Xie, T., Zhang, Y., Song, D. Transparent polynomial delegation and its applications to zero knowledge proof. **IEEE S&P 2020** [Google Scholar](https://scholar.google.com/scholar?q=Transparent+polynomial+delegation+and+its+applications+to+zero+knowledge+proof)

[44] Setty, S., Lee, J. Quarks: quadruple-efficient transparent zkSNARKs. **ePrint 2020** [Google Scholar](https://scholar.google.com/scholar?q=Quarks+quadruple+efficient+transparent+zkSNARKs)

[17] Bootle, J., Chiesa, A., Hu, Y., Orrù, M. Gemini: elastic SNARKs for diverse environments. **EUROCRYPT 2022** [Google Scholar](https://scholar.google.com/scholar?q=Gemini+elastic+SNARKs+for+diverse+environments)

[48] Wahby, R.S., Tzialla, I., Shelat, A., Thaler, J., Walfish, M. Doubly-efficient zkSNARKs without trusted setup. **IEEE S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Doubly+efficient+zkSNARKs+without+trusted+setup)

[40] Papamanthou, C., Shi, E., Tamassia, R. Signatures of correct computation. **TCC 2013** [Google Scholar](https://scholar.google.com/scholar?q=Signatures+of+correct+computation)

[32] Golovnev, A., Lee, J., Setty, S., Thaler, J., Wahby, R.S. Brakedown: linear-time and post-quantum SNARKs for R1CS. **ePrint 2021** [Google Scholar](https://scholar.google.com/scholar?q=Brakedown+linear+time+and+post+quantum+SNARKs+for+R1CS)


## 关键词

+ HyperPlonk
+ 多线性多项式承诺
+ 布尔超立方
+ 无FFT证明
+ 高次自定义门