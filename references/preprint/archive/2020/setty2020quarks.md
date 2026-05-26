---
title: "Quarks: Quadruple-efficient transparent zkSNARKs"
标题简称:
论文类型: journal
期刊简称: ePrint
发表年份: 2020
modified: 2025-04-17 13:37:09
created: 2025-04-11 11:31:12
---

## Quarks: Quadruple-efficient transparent zkSNARKs

## 发表信息

+ [archive](https://eprint.iacr.org/2020/1275)

## 作者

+ [Srinath Setty](Srinath%20Setty.md)
+ [Jonathan Lee](Jonathan%20Lee.md)
## 笔记

### 背景与动机

零知识简洁非交互式知识论证（zkSNARKs）是现代密码学中用于实现计算隐私和可扩展性的核心构件。一个理想的zkSNARK应同时具备四个特性：证明者高效（线性时间）、证明简短（对数大小）、验证快速（对数时间）以及预处理开销低廉（线性时间且常数小）。然而，现有的透明zkSNARKs（无需可信设置）在这四个目标间存在严重权衡。Spartan [61] 拥有最快的证明者，但其证明大小为 $O(\sqrt{n})$ 且验证时间为 $O(\sqrt{n})$；SuperSonic [29] 实现了对数级的证明大小和验证时间，但证明者因在类群中执行 $O(n \log n)$ 次幂运算而极其缓慢，其单个操作比常规群慢约800倍；Fractal [35] 提供了后量子安全性，但证明大小达 $O(\log^2 n)$ 且证明者开销巨大。此外，所有现有方案在预处理阶段都需要 $\Omega(n)$ 次密码学操作来生成计算承诺，这带来了高昂的启动成本。本文旨在填补这一空白，首次同时实现上述四个效率属性，从而构建名为Quarks的“四重高效”透明zkSNARKs。

### 相关工作

[61] Setty 等. Spartan: Efficient and general-purpose zkSNARKs without trusted setup. **CRYPTO 2020** [Google Scholar](https://scholar.google.com/scholar?q=Spartan%20Efficient%20and%20general-purpose%20zkSNARKs%20without%20trusted%20setup)
> 核心思路：利用求和检查协议与多项式承诺为R1CS构建透明zkSNARK，证明者开销最优。
> 局限与区别：证明大小为 $O(\sqrt{n})$ 且验证时间为 $O(\sqrt{n})$，未实现对数级证明和验证。本文通过Kopis-PC和Sparkle编译器在保持证明者效率的同时将证明大小降至 $O(\log n)$。

[29] Bünz 等. Transparent SNARKs from DARK compilers. **EUROCRYPT 2020** [Google Scholar](https://scholar.google.com/scholar?q=Transparent%20SNARKs%20from%20DARK%20compilers)
> 核心思路：基于强RSA和自适应根假设，在未知阶群中构建多项式承诺，实现对数级证明和验证。
> 局限与区别：证明者因类群运算极慢而效率低下。本文通过使用标准SXDH假设下的双线性群替代未知阶群，实现了更快的证明者。

[35] Chiesa 等. Fractal: Post-quantum and transparent recursive proofs from holography. **CRYPTO 2020** [Google Scholar](https://scholar.google.com/scholar?q=Fractal%20Post-quantum%20and%20transparent%20recursive%20proofs%20from%20holography)
> 核心思路：基于抗碰撞哈希实现后量子安全的透明zkSNARK，支持递归证明。
> 局限与区别：证明大小为 $O(\log^2 n)$，证明者需要 $O(n \log n)$ 次域乘法且内存开销大。本文方案在数字安全假设下提供更短的证明和更快的证明者。

[31] Bünz 等. Bulletproofs: Short proofs for confidential transactions and more. **S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Bulletproofs%20Short%20proofs%20for%20confidential%20transactions%20and%20more)
> 核心思路：基于内积论证的对数级证明，适用于范围证明等场景。
> 局限与区别：验证时间为 $O(n)$，无法实现亚线性验证。本文的副产品Lakonia在保持对数级证明的同时实现了更快的证明和验证。

[69] Wahby 等. Doubly-efficient zkSNARKs without trusted setup. **S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Doubly-efficient%20zkSNARKs%20without%20trusted%20setup)
> 核心思路：为多线性多项式构建承诺方案，承诺大小为 $O(\sqrt{n})$ 群元素。
> 局限与区别：承诺大小导致Spartan的证明很大。本文的Kopis-PC将承诺大小降至常数值 $O(1)$，从而大幅缩短证明。

[52] Lee. Dory: Efficient, transparent arguments for generalised inner products and polynomial commitments. **ePrint 2020** [Google Scholar](https://scholar.google.com/scholar?q=Dory%20Efficient%20transparent%20arguments%20for%20generalised%20inner%20products%20and%20polynomial%20commitments)
> 核心思路：利用向量张量结构实现 $O(\log n)$ 验证的多项式承诺。
> 局限与区别：Eval证明大小常数比Kopis-PC大约3倍。本文选择Kopis-PC作为主要构建块，因其更小的证明常数。

[11] Ames 等. Ligero: Lightweight sublinear arguments without a trusted setup. **CCS 2017** [Google Scholar](https://scholar.google.com/scholar?q=Ligero%20Lightweight%20sublinear%20arguments%20without%20a%20trusted%20setup)
> 核心思路：基于IOP和线性PCP的 $O(\sqrt{n})$ 证明，无需可信设置。
> 局限与区别：证明大小在MB级别且验证者为秒级。本文的Lakonia提供更短证明和更快验证。

[20] Ben-Sasson 等. Aurora: Transparent succinct arguments for R1CS. **EUROCRYPT 2019** [Google Scholar](https://scholar.google.com/scholar?q=Aurora%20Transparent%20succinct%20arguments%20for%20R1CS)
> 核心思路：基于代数IOP的 $O(\log^2 n)$ 证明。
> 局限与区别：证明大小约1.6 MB且验证者需108秒。本文方案在安全性和效率间取得更好平衡。

[16] Ben-Sasson 等. Scalable, transparent, and post-quantum secure computational integrity. **ePrint 2018** [Google Scholar](https://scholar.google.com/scholar?q=Scalable%20transparent%20and%20post-quantum%20secure%20computational%20integrity)
> 核心思路：STARK，基于FRI协议的后量子安全证明系统。
> 局限与区别：证明大小达39 MB，验证者需数分钟。本文方案针对数字安全假设优化，在此类场景中效率更高。

### 核心技术与方案

本文的整体框架以Spartan [61] 的模块化设计为基础，将R1CS的NP陈述转化为多线性多项式求值和求和检查协议实例。核心创新在于三个技术模块：Kopis-PC多项式承诺、Sparkle稀疏多项式承诺编译器、以及未受信任助理加速编码器。Kopis是Xiphos的一个变体，支持更短的证明但验证为 $O(\sqrt{n})$ 级别；Xiphos同时实现证明和验证均为 $O(\log n)$；Lakonia是Kopis的简化版本，无需预处理，提供 $O(\log n)$ 证明但线性验证。

**模块一：Kopis-PC多项式承诺方案。** 现有Hyrax-PC [69] 的承诺大小为 $O(\sqrt{n})$ 群元素，是Spartan证明的主要组成部分。Kopis-PC将承诺降低到单个 $\mathbb{G}_T$ 元素，利用双线性群和双重同态承诺。对于 $\ell$ 变量多线性多项式 $\widetilde{Z}$，设 $s = 2^{\ell/2}$，将 $\widetilde{Z}$ 视为 $s \times s$ 矩阵。承诺过程首先用IPP对每行进行承诺，生成 $s$ 个 $\mathbb{G}_1$ 承诺 $\mathcal{C}_0,\dots,\mathcal{C}_{s-1}$，然后使用BIPP将向量 $(\mathcal{C}_0,\dots,\mathcal{C}_{s-1})$ 承诺为一个 $\mathbb{G}_T$ 元素。在执行Eval协议时，验证者首先发送点 $\boldsymbol{r} = (\boldsymbol{r}_x, \boldsymbol{r}_y)$，双方计算向量 $\boldsymbol{L} = \widetilde{\mathrm{eq}}(i,\boldsymbol{r}_x)$ 和 $\boldsymbol{R} = \widetilde{\mathrm{eq}}(j,\boldsymbol{r}_y)$。证明者计算中间值 $y_{\text{out}} = \langle (\mathcal{C}_0,\dots,\mathcal{C}_{s-1}), \boldsymbol{L} \rangle$ 并提交，然后通过BIPP证明该内积的正确性，最后通过IPP证明 $\langle \boldsymbol{L} \cdot Z, \boldsymbol{R} \rangle = \widetilde{Z}(\boldsymbol{r})$。该方案将Eval证明大小从 $O(\ell)$ 群元素提升到 $O(\ell)$ 目标群元素（常数因子约6），但在Spartan上下文中，主要改进是从 $O(\sqrt{n})$ 降至 $O(\log n)$。安全性依赖于SXDH问题，Eval协议具备知识可靠性。

**模块二：Sparkle编译器改进稀疏多项式承诺。** Spartan的SPARK编译器将稠密多项式承诺转换为稀疏多项式承诺，但依赖于对数深度的分层求和检查，产生 $O(\log^2 n)$ 证明。Sparkle利用第5节的新透明SNARK证明累加关系 $\mathcal{R}_{\mathrm{GP}} = \{(P, \boldsymbol{V}) : P = \prod_i V_i\}$，该SNARK将累加检查归约为求和检查实例：存在多线性多项式 $f$ 满足 $f(0,\boldsymbol{x}) = \nu(\boldsymbol{x})$、$f(1,\dots,1,0) = P$，且 $\forall \boldsymbol{x}: f(1,\boldsymbol{x}) = f(\boldsymbol{x},0) \cdot f(\boldsymbol{x},1)$。这等价于单个求和检查 $0 = \sum_{\boldsymbol{x}} \widetilde{\mathrm{eq}}(\boldsymbol{x},\tau) \cdot (f(1,\boldsymbol{x}) - f(\boldsymbol{x},0) \cdot f(\boldsymbol{x},1))$。结合Kopis-PC，证明大小从 $O(\log^2 n)$ 降至 $O(\log n)$。为保持证明效率，Sparkle采用混合策略：对常数层使用分层求和检查，对剩余部分使用该专用SNARK，证明者开销仅增加约20%。

**模块三：未受信任助理加速编码器。** 编码器需创建R1CS结构的计算承诺，传统方法需 $O(n)$ 次群幂运算。本文允许未受信任助理生成承诺，编码器通过随机挑战验证其正确性。协议中，助理提交承诺 $\mathcal{C}$ 和值 $\nu$，编码器发送随机点 $\boldsymbol{r}$，双方运行PC.Eval证明 $\mathcal{C}(\boldsymbol{r}) = \nu$，编码器本地计算 $\mathcal{G}(\boldsymbol{r})$ 并验证OpenF。由Schwartz-Zippel引理， $\mathcal{G} = \mathcal{G}'$ 的错误概率为 $O(\log m / |\mathbb{F}|)$，可忽略。该协议将编码器成本从 $O_\lambda(n)$ 降低到 $O(n)$ 域乘法加 $O(\log n)$ 密码操作。

**模块四：改进零知识变换。** 传统Hyrax方法要求证明者发送 $\ell$ 个向量承诺，产生 $O(k\ell + d)$ 群元素。新方法利用低权重多项式 $g(\boldsymbol{X}) = b_0 \prod (1-X_i) + \sum b_i (2X_i-1) \prod_{j\neq i}(1-X_j)$，其支撑集大小为 $\ell+1$。证明者选择 $d$ 个独立低权重多项式 $g^j$，构造 $G = \sum g^j$，提交承诺并发送 $z = y + \sum_x G(x)$。运行非隐藏求和检查于 $F+G$ 上，然后通过Eval和sigma协议验证一致性。此方法将通信开销降至 $O(kd + \ell)$。

渐进复杂度总结：对于 $n$ 大小R1CS实例，Xiphos证明者需 $n \mathbb{G}_1$ 次操作，证明大小 $\log n \mathbb{G}_T$，验证时间 $\log n \mathbb{G}_T$；Kopis保持相同证明者代价和证明大小，但验证时间为 $\sqrt{n} \mathbb{G}_2$。

### 核心公式与流程

**[Kopis-PC Eval协议核心方程]**
$$
\widetilde{Z}(\boldsymbol{r}_x,\boldsymbol{r}_y) = \sum_{i \in \{0,1\}^s} \widetilde{\mathrm{eq}}(i,\boldsymbol{r}_x) \cdot \sum_{j \in \{0,1\}^s} Z(i,j) \cdot \widetilde{\mathrm{eq}}(j,\boldsymbol{r}_y) = (\boldsymbol{L} \cdot Z) \cdot \boldsymbol{R}
$$
> 作用：将多线性多项式求值重写为矩阵与向量的双线性形式，使验证者能通过BIPP和IPP协议外包计算。

**[累加关系SNARK的求和检查实例]**
$$
0 = \sum_{\boldsymbol{x} \in \{0,1\}^{\log m}} \widetilde{\mathrm{eq}}(\boldsymbol{x},\tau) \cdot (f(1,\boldsymbol{x}) - f(\boldsymbol{x},0) \cdot f(\boldsymbol{x},1))
$$
> 作用：将 $\prod_i V_i = P$ 的证明归约为多线性多项式 $f$ 的单方程约束，支持通过单次求和检查协议高效证明。

**[低权重多项式定义及其支撑性质]**
$$
g(\boldsymbol{X}) = b_0 \prod_{i=1}^\ell (1-X_i) + \sum_{i=1}^\ell b_i (2X_i-1) \prod_{j=1, j\neq i}^\ell (1-X_j)
$$
> 作用：构造只有 $\ell+1$ 个非零点的多项式族，用于零知识求和检查中掩蔽原始多项式，同时保持证明的简洁性。

**[未受信任助理验证协议结构]**
$$
\begin{aligned}
1.&\ \mathcal{A} \to \mathcal{V}: (\mathcal{C}_\nu; \mathcal{S}_\nu) \gets \text{Commit}_\mathbb{F}(pp_\mathbb{F}; \nu)\\
2.&\ \mathcal{V} \to \mathcal{A}: \boldsymbol{r} \xleftarrow{\$} \mathbb{F}^\ell\\
3.&\ \mathcal{A},\mathcal{V}: b_{\text{poly}} = \text{PC.Eval}(pp, pp_\mathbb{F}, \mathcal{C}, \boldsymbol{r}, \mathcal{C}_\nu; \mathcal{G}, \mathcal{S}, \mathcal{S}_\nu)\\
4.&\ \mathcal{V}: \nu \stackrel{?}{=} \mathcal{G}(\boldsymbol{r})\\
5.&\ \mathcal{A},\mathcal{V}: b_{\text{eval}} = \text{Open}_\mathbb{F}(pp_\mathbb{F}, \mathcal{C}_\nu, \nu, \mathcal{S}_\nu)\\
6.&\ \mathcal{V}: \text{Output } b = b_{\text{poly}} \land b_{\text{eval}}
\end{aligned}
$$
> 作用：通过随机挑战将助理生成承诺的正确性归约为多项式求值一致性和承诺可打开性，避免编码器本地执行密码学操作。

### 实验结果

实验在Azure Standard F16s_v2虚拟机上（16 vCPU, 32 GB RAM, Ubuntu 20.10）单线程运行。基准对比包括：Spartan [61] 的优化实现libSpartan [7]（曲线ard25519），Fractal [35] 使用libiop [55]，SuperSonic [29] 因无公开实现故基于作者成本模型和ANTIC库 [1] 的类群幂运算微基准（每操作≈38 ms）估算。对于 $2^{20}$ 约束的R1CS实例：Xiphos证明者169秒，是Spartan（47秒）的3.8倍，但比SuperSonic（63,700秒）快376倍；Xiphos证明大小61 KB，与SuperSonic（49 KB）竞争，且远小于Fractal（2.3 MB）和Spartan（142 KB）；Xiphos验证时间65 ms，是Spartan（135 ms）的2.1倍，且比SuperSonic（2,570 ms）快39倍。Kopis将证明缩短至39 KB（比SuperSonic短），验证时间390 ms。使用未受信任助理的编码器，Xiphos和Kopis的编码时间为1.8-2.2秒，是Spartan编码器（20秒）的9-11倍，比SuperSonic（17,900秒）快4个数量级。Lakonia（无预处理）在 $2^{20}$ 约束下：证明者19秒，证明11 KB，验证者517 ms，相比Bulletproofs（估计证明者804秒、验证者30,957秒）快42倍和60倍。

### 局限性与开放问题

本文方案依赖于SXDH问题，属于标准假设但并非后量子安全。Fractal [35] 在此方面具有优势，但牺牲了效率。Kopis的验证时间为 $O(\sqrt{n})$，未能满足Quarks的“快速验证”标准，未来工作可探索将Kopis验证降为 $O(\log n)$ 的方案。零知识特性通过低权重多项式构造实现，但仅提供计算零知识，证明结构因包含群元素而失去后量子安全性。最后，大规模R1CS实例（如 $2^{30}$ 以上）中，Xiphos的对数级验证优势更加显著，但证明者内存和计算开销仍需进一步优化以适应超大规模电路。

### 强关联论文

[61] Setty 等. Spartan: Efficient and general-purpose zkSNARKs without trusted setup. **CRYPTO 2020** [Google Scholar](https://scholar.google.com/scholar?q=Spartan%20Efficient%20and%20general-purpose%20zkSNARKs%20without%20trusted%20setup)

[29] Bünz 等. Transparent SNARKs from DARK compilers. **EUROCRYPT 2020** [Google Scholar](https://scholar.google.com/scholar?q=Transparent%20SNARKs%20from%20DARK%20compilers)

[35] Chiesa 等. Fractal: Post-quantum and transparent recursive proofs from holography. **CRYPTO 2020** [Google Scholar](https://scholar.google.com/scholar?q=Fractal%20Post-quantum%20and%20transparent%20recursive%20proofs%20from%20holography)

[69] Wahby 等. Doubly-efficient zkSNARKs without trusted setup. **S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Doubly-efficient%20zkSNARKs%20without%20trusted%20setup)

[31] Bünz 等. Bulletproofs: Short proofs for confidential transactions and more. **S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Bulletproofs%20Short%20proofs%20for%20confidential%20transactions%20and%20more)

[52] Lee. Dory: Efficient, transparent arguments for generalised inner products and polynomial commitments. **ePrint 2020** [Google Scholar](https://scholar.google.com/scholar?q=Dory%20Efficient%20transparent%20arguments%20for%20generalised%20inner%20products%20and%20polynomial%20commitments)

[20] Ben-Sasson 等. Aurora: Transparent succinct arguments for R1CS. **EUROCRYPT 2019** [Google Scholar](https://scholar.google.com/scholar?q=Aurora%20Transparent%20succinct%20arguments%20for%20R1CS)

[11] Ames 等. Ligero: Lightweight sublinear arguments without a trusted setup. **CCS 2017** [Google Scholar](https://scholar.google.com/scholar?q=Ligero%20Lightweight%20sublinear%20arguments%20without%20a%20trusted%20setup)

[16] Ben-Sasson 等. Scalable, transparent, and post-quantum secure computational integrity. **ePrint 2018** [Google Scholar](https://scholar.google.com/scholar?q=Scalable%20transparent%20and%20post-quantum%20secure%20computational%20integrity)

[30] Bünz 等. Proofs for inner pairing products and applications. **ePrint 2019** [Google Scholar](https://scholar.google.com/scholar?q=Proofs%20for%20inner%20pairing%20products%20and%20applications)


## 关键词

+ Quarks四重高效透明zkSNARK
+ R1CS无可信设置SXDH安全
+ 快速证明短证明快速验证
+ Xiphos Kopis对数验证时间
+ 透明SNARK低预处理成本