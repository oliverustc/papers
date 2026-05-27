---
title: "Dual polynomial commitment schemes and applications to commit-and-prove SNARKs"
doi: 10.1145/3658644.3690219
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2024
created: 2025-04-23 14:59:43
modified: 2025-04-23 15:16:43
---
## Dual polynomial commitment schemes and applications to commit-and-prove SNARKs

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3658644.3690219)
+ [code](http://github.com/arithmic/Dual_PCS)

## 作者

+ [Chaya Ganesh](Chaya%20Ganesh.md)
+ Vineet Nair 
+ Ashish Sharma 

## 笔记

### 背景与动机
当前零知识简洁非交互论证系统中，多项式承诺方案是连接信息论证明系统与密码学编译器的核心工具。不同证明系统对多项式的表示方式存在根本差异：基于代数哈希证明或多项式交互式预言证明的SNARK通常使用单变量多项式，并采用系数向量表示，而基于和项检查的SNARK则倾向于使用多线性多项式并以评估向量表示。Commit-and-prove SNARK框架允许将不同证明系统模块化组合，但现有框架假设不同组件使用的多项式承诺方案是“兼容”的，即它们对多项式的表示方式一致。这一假设严重限制了CP-SNARK的通用性——例如，Grothend16（基于KZG单变量承诺）无法直接与Lasso（基于多线性承诺的查找论证）组合。此外，查找论证在表达位分解、范围检查等“SNARK不友好”操作时比电路表示高效得多，且Lasso和Jolt共同推动了“查找奇点”理念，即SNARK前端仅由查找组成。因此，构建一个能够无缝链接单变量和多线性多项式承诺的通用框架，对于实现真正的CP-SNARK模块化至关重要。本文提出的双多项式承诺方案正是为了解决这一技术瓶颈，使得在不同表示方式的证明系统之间自由切换成为可能。

### 相关工作

[2] Diego F. Aranha et al. ECLIPSE: Enhanced Compiling Method for Pedersen-Committed zkSNARK Engines. **CRYPTO 2022** [Google Scholar](https://scholar.google.com/scholar?q=ECLIPSE+Enhanced+Compiling+Method+for+Pedersen-Committed+zkSNARK+Engines)
> 核心思路：提供一个从信息论对象到CP-SNARK的通用编译器，假设Pedersen向量承诺。
> 局限与区别：该编译器仅适用于与Pedersen承诺兼容的证明系统，无法处理使用KZG等不同承诺方案的证明系统。

[5] Jonathan Bootle et al. Gemini: Elastic SNARKs for Diverse Environments. **CRYPTO 2022** [Google Scholar](https://scholar.google.com/scholar?q=Gemini+Elastic+SNARKs+for+Diverse+Environments)
> 核心思路：利用线性同构将多线性多项式的单项式基映射到单变量多项式的单项式基。
> 局限与区别：本文采用的线性同构是将多线性多项式的傅里叶基映射到单变量多项式的FFT基，这使得链接证明更高效。

[6] Matteo Campanelli et al. Lunar: A Toolbox for More Efficient Universal and Updatable zkSNARKs and Commit-and-Prove Extensions. **PKC 2021** [Google Scholar](https://scholar.google.com/scholar?q=Lunar+A+Toolbox+for+More+Efficient+Universal+and+Updatable+zkSNARKs+and+Commit-and-Prove+Extensions)
> 核心思路：提供通用编译器，假设KZG承诺用于CP-SNARK的链接组件。
> 局限与区别：其链接组件仅适用于KZG承诺方案，无法处理多线性承诺方案。

[7] Matteo Campanelli et al. Natively Compatible Super-Efficient Lookup Arguments and How to Apply Them. **ePrint 2024** [Google Scholar](https://scholar.google.com/scholar?q=Natively+Compatible+Super-Efficient+Lookup+Arguments+and+How+to+Apply+Them)
> 核心思路：提出一个编译器，将单变量查找论证转换为与多线性SNARK兼容的版本。
> 局限与区别：该方案需要额外的链接证明（和项检查），增加了验证者复杂度（多个配对操作），而本文的KZG-FFT-FOURIER方案不需要链接证明。

[12] Ariel Gabizon and Zachary J. Williamson. plookup: A simplified polynomial protocol for lookup tables. **ePrint 2020** [Google Scholar](https://scholar.google.com/scholar?q=plookup+A+simplified+polynomial+protocol+for+lookup+tables)
> 核心思路：提出一种基于单变量多项式的查找论证。
> 局限与区别：仅适用于Plonk等使用相同多项式表示（单变量）的SNARK系统。

[19] Aniket Kate et al. Constant-Size Commitments to Polynomials and Their Applications. **ASIACRYPT 2010** [Google Scholar](https://scholar.google.com/scholar?q=Constant-Size+Commitments+to+Polynomials+and+Their+Applications)
> 核心思路：提出基于双线性群的常数大小多项式承诺方案，承诺为单个群元素。
> 局限与区别：KZG基于系数表示，需要证明者执行FFT获得多项式系数，本文的KZG-FFT方案通过修改SRS避免了这一开销。

[22] Jonathan Lee. Dory: Efficient, Transparent Arguments for Generalised Inner Products and Polynomial Commitments. **CRYPTO 2021** [Google Scholar](https://scholar.google.com/scholar?q=Dory+Efficient+Transparent+Arguments+for+Generalised+Inner+Products+and+Polynomial+Commitments)
> 核心思路：提出透明的内积论证和多项式承诺方案。
> 局限与区别：本文的透明双承诺方案dory-link使用Dory作为黑盒进行链接证明，需要处理额外线性关系。

[24] Charalampos Papamanthou et al. Signatures of Correct Computation. **TCC 2013** [Google Scholar](https://scholar.google.com/scholar?q=Signatures+of+Correct+Computation)
> 核心思路：提出基于多线性多项式的签名方案，其中包括多项式分解技术。
> 局限与区别：本文的KZG-FOURIER评估协议使用了类似的多项式分解，但通过线性同构映射到单变量多项式进行检查。

[25] Srinath Setty. Spartan: Efficient and General-Purpose zkSNARKs Without Trusted Setup. **CRYPTO 2020** [Google Scholar](https://scholar.google.com/scholar?q=Spartan+Efficient+and+General-Purpose+zkSNARKs+Without+Trusted+Setup)
> 核心思路：提出免信任设置的通用SNARK，使用稀疏多线性多项式承诺。
> 局限与区别：Spartan的大乘积检查依赖GKR或和项检查，导致证明大小和验证时间与约束数成对数关系，本文通过GPR-AIR将其优化为常数。

[27] Srinath T. V. Setty et al. Unlocking the Lookup Singularity with Lasso. **CRYPTO 2024** [Google Scholar](https://scholar.google.com/scholar?q=Unlocking+the+Lookup+Singularity+with+Lasso)
> 核心思路：提出基于和项检查的查找论证，自然与多线性SNARK（如Spartan）兼容。
> 局限与区别：Lasso仅适用于多线性多项式承诺方案，无法直接与单变量SNARK（如Grothend16）组合。

### 核心技术与方案

本文的核心创新是双多项式承诺方案，其允许对同一见证向量同时获得单变量和多线性两种多项式承诺，并提供链接证明保证两者一致性。方案由两个主要实例构成：基于可更新SRS的KZG-FFT-FOURIER和基于透明设置的dory-link。

**双承诺方案KZG-FFT-FOURIER**的基石是两个新的多项式承诺方案——单变量方案KZG-FFT和多线性方案KZG-FOURIER。KZG-FFT的作用是使证明者可以直接使用见证向量（视为多项式在FFT域上的评估向量）进行承诺，而无需先通过FFT转化为系数向量。其SRS生成方式如下：采样秘密随机数 $r \in_R \mathbb{F}$，并计算 $\alpha_i = N^{-1} \cdot \prod_{j \in [0, n-1]} (1 + (\omega_N^{-i} \cdot r)^{2^j})$，其中 $N=2^n$ 是域的大小，$\omega_N$ 是本原单位根。承诺群元素为 $g_1^{\alpha_i}$，使得见证向量 $\mathbf{a}$ 的承诺可由 $C_f = \prod_i (h_{1,i}^{(d)})^{a_i}$ 直接计算，其中 $h_{1,i}^{(d)}$ 是通过递归折叠从SRS导出的。该承诺等价于 $g_1^{f(r^{2^{n-d}})}$，$f$ 是以 $\mathbf{a}$ 为评估值的单变量多项式。评估协议与KZG相同：证明者计算商多项式 $q(Y) = (f(Y) - v)/(Y-u)$ 并在FFT域上评估后承诺为 $C_q$；验证者检查 $e(C_f \cdot g_1^{-v}, g_2) = e(C_q, h_{2,n-d} \cdot g_2^{-u})$。由于证明者直接处理评估向量，避免了FFT插值，且商多项式的评估计算可高度并行化。安全性依赖N-DLOG假设下的代数群模型。

KZG-FOURIER利用了线性同构 $\mathcal{U}_n$，它将多线性多项式的傅里叶基 $\{L_i^{(n)}\}$ 一对一映射到单变量多项式的FFT基 $\{U_i^{(n)}\}$，其中 $U_i^{(n)} = \frac{1}{N} \prod_{j=0}^{n-1} (1 + (\omega_N^{-i} \cdot Y)^{2^j})$。由于 $\mathcal{U}_n$ 将多线性多项式 $f$ 的傅里叶系数向量 $\mathbf{f}$ 映射到单变量多项式 $w_f$ 的评估向量，因此对 $f$ 的承诺可通过对 $w_f$ 使用KZG-FFT完成，即 $C_f = C_{w_f}$。评估协议基于多项式分解：对于评估点 $\mathbf{z} \in \mathbb{F}^d$，存在多项式 $q_k$ 使得 $f(\mathbf{X}^{(d)}) - y = \sum_{k=0}^{d-1} (X_k - z_k) q_k(\mathbf{X}^{(k)})$。验证者检查此关系在 $\mathcal{U}_d$ 下的像，即检查 $\mathcal{U}_d(f)(z) - y = \sum_{k=0}^{d-1} \mathcal{U}_d(X_k q_k)(z) - z_k \mathcal{U}_d(q_k)(z)$，其中 $z$ 是验证者随机选择的点。证明者通过提供各 $q_k$ 对应的分解多项式 $\psi_{q_k,e}$ 和 $\psi_{q_k,o}$ 的承诺及其在 $z$ 幂点上的评估来证明正确性，最终通过一个批处理的KZG-FFT评估检查完成。该协议在多线性一侧提供 $O(\log D)$ 的验证时间和 $O(D \log^2 D)$ 的证明者时间。

由于 $\mathcal{U}_n$ 是线性同构，对同一见证向量 $\mathbf{a}$，KZG-FFT和KZG-FOURIER的承诺完全相同（均为KZG-FFT.commit(srs$_P$, $D$, $\mathbf{a})$），因此KZG-FFT-FOURIER的链接证明是平凡的——验证者只需检查两个承诺是否相等。这一性质使得该双承诺方案在运行链接证明时没有额外开销。

透明双承诺方案dory-link基于Dory透明证明系统。承诺采用AFG类型的结构：对见证向量 $\mathbf{a}$ 的承诺为 $C_{\mathbf{a}} = \prod_i e(\tau_i^{(1,d)}, g_2^{a_i})$，对单变量多项式系数向量 $\mathbf{f} = (f_0, \ldots, f_{D-1})$ 的承诺为 $C_f = \prod_i e(\tau_i^{(1,d)}, g_2^{f_i})$。链接证明需要证明 $\mathbf{a} = M_{\omega_D} \cdot \mathbf{f}$，即 $\mathbf{a}$ 是 $\mathbf{f}$ 的FFT变换结果。这一线性关系通过新论证系统Linear-Rel证明，该系统将Dory作为黑盒运行两个实例：第一个证明存在向量 $\mathbf{a}$ 满足 $C_{\mathbf{a}}$，第二个证明存在向量 $\mathbf{f}$ 满足 $C_f$ 和 $M_{\omega_D} \cdot \mathbf{f} = \mathbf{a}$。评估协议则直接使用Dory的评估协议。该方案提供透明设置，但代价是证明和验证复杂度较KZG-FFT-FOURIER更高。

**应用：Spartan AIR**。本文利用KZG-FFT-FOURIER构建了Spartan的一个变体Spartan-AIR。Spartan的稀疏多线性多项式承诺中，一个大乘积检查用于离线内存检查。原有的大乘积检查（如使用GKR [15, 28]或和项检查 [26]）需要将见证作为多线性多项式承诺，导致证明大小和对数级验证时间。本文提出的GPR-AIR使用KZG-FFT将见证作为单变量多项式承诺，实现了常数大小的证明和常数时间验证。GPR-AIR的协议是一个基于单变量多项式交互式预言证明的论证，通过商多项式技术检查乘积关系 $\prod_i a_i = q$。由于两种协议共享的见证在KZG-FFT-FOURIER中具有相同的承诺，Spartan-AIR可直接集成，将大乘积检查的开销从对数级降为常数。

**安全性**：KZG-FFT-FOURIER在AGM下基于N-DLOG假设满足知识可靠性；dory-link基于SXDH假设满足知识可靠性。

**渐进复杂度**：KZG-FFT-FOURIER的证明者复杂度为 $O(D)$（单变量评估）和 $O(D \log^2 D)$（多线性评估），验证者复杂度为 $O(\log D)$，承诺为固定大小（常数个群元素）。dory-link的证明者和验证者复杂度均为 $O(\log D)$，但常数更大。Spartan-AIR相比原始Spartan，验证时间从 $O(\log C)$ 降为 $O(1)$，证明大小从 $O(\log C)$ 降为 $O(1)$，但证明者时间显著增加，达到 $O(C^2)$ 量级，由于GPR-AIR中商多项式评估的计算量。

### 核心公式与流程

**[KZG-FFT 设置中的SRS生成]**

$$\alpha_i = N^{-1} \cdot \prod_{j=0}^{n-1} (1 + (\omega_N^{-i} \cdot r)^{2^j}),\quad i \in [0, N-1]$$

$$\text{srs}_{\mathcal{P}} = \{h_{1,i}^{(n)} = g_1^{\alpha_i}\},\quad \text{srs}_{\mathcal{V}} = \{h_{2,j} = g_2^{r^{2^j}}\},\quad \pi = (g_1^r, g_2^r)$$

> 作用：将秘密随机数 $r$ 经过FFT矩阵变换得到 $\alpha_i$，使得承诺可直接由见证向量计算。$r$ 的幂次用于验证。

**[KZG-FFT 承诺]**

$$h_{1,i}^{(k)} = h_{1,i}^{(k+1)} \cdot h_{1,i+2^k}^{(k+1)},\quad \forall i \in [0, 2^k-1]$$

$$C_f = \prod_{i \in [0, D-1]} (h_{1,i}^{(d)})^{a_i} = g_1^{f(r^{2^{n-d}})}$$

> 作用：通过递归折叠SRS得到适应度数 $D=2^d$ 的承诺基，承诺值是多项式 $f$ 在秘密点 $r^{2^{n-d}}$ 上的评估的编码。

**[KZG-FFT 评估验证]**

$$e(C_f \cdot g_1^{-v}, g_2) = e(C_q, h_{2,n-d} \cdot g_2^{-u})$$

> 作用：验证商多项式关系 $f(Y) - v = (Y-u)q(Y)$ 在秘密点成立。等价于检查 $f(u)=v$。

**[线性同构 $\mathcal{U}_n$]**

$$\mathcal{U}_n(L_i^{(n)}) = U_i^{(n)} = \frac{1}{N} \prod_{j=0}^{n-1} (1 + (\omega_N^{-i} \cdot Y)^{2^j}),\quad i \in [0, N-1]$$

> 作用：将多线性多项式的傅里叶基映射到单变量多项式的FFT基，使得两个函数空间同构。

**[KZG-FOURIER 评估协议中的多项式分解]**

$$f(\mathbf{X}^{(d)}) - y = \sum_{k=0}^{d-1} (X_k - z_k) \cdot q_k(\mathbf{X}^{(k)})$$

> 作用：多线性多项式在某点的评估值可以通过一系列逐维度的线性分解表示，验证者只需检查此关系。

**[KZG-FOURIER 评估最终检查]**

$$\mathcal{U}_d(f)(z) - y = \sum_{k=0}^{d-1} \left( \mathcal{U}_d(X_k q_k)(z) - z_k \cdot \mathcal{U}_d(q_k)(z) \right)$$

> 作用：将多线性关系映射到单变量域后，通过随机点 $z$ 的评估检查验证多项式身份，依赖Schwartz-Zippel引理。

**[Dory-link 承诺]**

$$C_{\mathbf{a}} = \prod_{i=0}^{D-1} e(\tau_i^{(1,d)}, g_2^{a_i}),\quad C_f = \prod_{i=0}^{D-1} e(\tau_i^{(1,d)}, g_2^{f_i})$$

> 作用：使用透明的Dory公共参数对见证向量 $\mathbf{a}$ 和对应多项式系数向量 $\mathbf{f}$ 分别承诺，链接证明需证 $\mathbf{a} = M_{\omega_D} \cdot \mathbf{f}$。

### 实验结果

实验基于BLS12-381曲线，在46核256GB RAM的QCT机架服务器上运行，证明者使用多核，验证者使用单核。KZG-FFT-FOURIER的承诺时间随见证大小线性增长，从 $2^{15}$ 时的0.26秒到 $2^{20}$ 时的3.74秒。单变量评估证明者时间从0.29秒（$2^{15}$）增长到5.04秒（$2^{20}$），但验证者时间几乎恒定在19.86毫秒左右。多线性评估验证者时间从60.21毫秒（$2^15$）增长到387.71毫秒（$2^{20}$）。多线性评估证明者时间增长较快，从7.21秒（$2^{15}$）到4616.05秒（$2^{20}$）。证明大小固定：单变量0.12KB，多线性从5.56KB（$2^{15}$）增长到7.43KB（$2^{20}$）。与标准KZG和PST对比（见论文完整版），KZG-FFT在承诺阶段明显更快，因为避免了FFT插值。

dory-link的承诺时间约0.1-0.3秒，评估证明者时间从3.76秒（$2^9$）到147.22秒（$2^{15}$），验证者时间从0.74秒到1.19秒，但常数较大，适用于较小规模（$2^{15}$以内）。证明大小从35.75KB（$2^9$）到59.37KB（$2^{15}$）。

Spartan vs Spartan-AIR的性能对比显示，在约束数为 $2^{17}$ 时，Spartan-AIR的评估证明者时间为497.75秒（vs Spartan的27.76秒），但验证者时间降至0.64秒（vs 1.10秒），证明大小降至37.85KB（vs 78.78KB），分别实现了1.7倍验证时间加速和2倍证明大小缩减。更小规模时，加速比略低。当稀疏度比例从1提升到2时，Spartan-AIR的证明大小和验证时间进一步优化。这些结果验证了Spartan-AIR在需要极小证明和快速验证的场景（如区块链递归证明中的最终Layer-1验证）中的优势。

### 局限性与开放问题

当前KZG-FFT-FOURIER的多线性评估证明者复杂度高达 $O(D \log^2 D)$，在大规模问题上非常缓慢，如何优化多线性评估证明者的性能是一个开放问题。dory-link方案虽然透明，但常数较大且仅适用于较小规模，设计更高效的透明链接机制值得探索。协议的零知识性质未在本工作中实现，但作者认为可通过标准技术轻松添加。如何将双承诺方案扩展到更多表示方式（如代数中间表示的约束系统）并保持链接效率，是另一个有前景的方向。

### 强关联论文

[2] Diego F. Aranha et al. ECLIPSE: Enhanced Compiling Method for Pedersen-Committed zkSNARK Engines. **CRYPTO 2022**

[5] Jonathan Bootle et al. Gemini: Elastic SNARKs for Diverse Environments. **CRYPTO 2022**

[6] Matteo Campanelli et al. Lunar: A Toolbox for More Efficient Universal and Updatable zkSNARKs and Commit-and-Prove Extensions. **PKC 2021**

[7] Matteo Campanelli et al. Natively Compatible Super-Efficient Lookup Arguments and How to Apply Them. **ePrint 2024**

[12] Ariel Gabizon and Zachary J. Williamson. plookup: A simplified polynomial protocol for lookup tables. **ePrint 2020**

[15] Shafi Goldwasser et al. Delegating computation: interactive proofs for muggles. **STOC 2008**

[19] Aniket Kate et al. Constant-Size Commitments to Polynomials and Their Applications. **ASIACRYPT 2010**

[22] Jonathan Lee. Dory: Efficient, Transparent Arguments for Generalised Inner Products and Polynomial Commitments. **CRYPTO 2021**

[25] Srinath Setty. Spartan: Efficient and General-Purpose zkSNARKs Without Trusted Setup. **CRYPTO 2020**

[27] Srinath T. V. Setty et al. Unlocking the Lookup Singularity with Lasso. **CRYPTO 2024**


## 关键词

+ 多项式承诺
+ 承诺-证明SNARK
+ 单变量承诺
+ 多线性承诺
+ Spartan
+ 可更新SRS