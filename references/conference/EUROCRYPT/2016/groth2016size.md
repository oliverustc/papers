---
title: "On the size of pairing-based non-interactive arguments"
标题简称:
论文类型: conference
会议简称: EUROCRYPT
发表年份: 2016
created: 2025-05-12 08:54:37
modified: 2025-05-12 08:56:54
---

## On the size of pairing-based non-interactive arguments

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-662-49896-5_11)

## 作者

+ [Jens Groth](Jens%20Groth.md)

## 笔记

### 背景与动机
非交互式论证（NIZK）是实现可验证计算、匿名数字货币（如 Zerocash）等高级密码学协议的核心构建块，其效率——特别是证明大小与验证复杂度——直接决定系统实用性。尽管基于配对的简洁非交互式论证（SNARG/SNARK）在理论上取得了巨大进展，如 Gennaro 等人 [GGPR13] 提出的二次算术程序（QAP）和 Parno 等人 [PHGR13] 的 Pinocchio 系统，但这些方案的证明长度仍不为最小，且其安全性往往依赖特定假设。本文的核心动机是探索在非对称双线性群上，基于通用群模型，一个 SNARK 在理论上能够达到的证明大小的下界。具体而言，作者通过构造一个仅含 3 个群元件的实用 SNARK，并证明单群元件 SNARG 不可能存在，填补了理论下限与高效构造之间的空白。此外，该工作还回答了 Bitansky 等人 [BCI+13] 提出的关于线性交互证明（LIP）是否具有线性判决过程的开放问题。

### 相关工作

[GGPR13] Gennaro 等. Quadratic Span Programs and Succinct NIZKs without PCPs. **EUROCRYPT 2013** [Google Scholar](https://scholar.google.com/scholar?q=Quadratic+Span+Programs+and+Succinct+NIZKs+without+PCPs)
> 核心思路：引入二次算术程序（QAP）将电路可满足性问题转化为多项式整除性检查，奠定了后续高效 SNARK 的理论基础。
> 局限与区别：其原始构造的证明由 4 个群元件组成，验证需执行多个配对乘积方程；本文将其精简为 3 个群元件和单个配对方程。

[PHGR13] Parno 等. Pinocchio: Nearly Practical Verifiable Computation. **IEEE S&P 2013** [Google Scholar](https://scholar.google.com/scholar?q=Pinocchio:Nearly+Practical+Verifiable+Computation)
> 核心思路：将 QAP 编译为具体的零知识 SNARK 系统，展示了 SNARK 在可验证计算中的实用性。
> 局限与区别：其证明需 7 个群元件（对称群）或 8 个元件（非对称群），本文将非对称群中的证明大小减至 3 个元件。

[BCI+13] Bitansky 等. Succinct Non-interactive Arguments via Linear Interactive Proofs. **TCC 2013** [Google Scholar](https://scholar.google.com/scholar?q=Succinct+Non-interactive+Arguments+via+Linear+Interactive+Proofs)
> 核心思路：提出线性交互证明（LIP）作为 SNARK 的信息论抽象层，证明 LIP 可编译为配对基 SNARK。
> 局限与区别：本文回应了其开放问题——证明了具有线性判决过程的 LIP 不存在，从而导出单群元件 SNARG 的下界。

[DFGK14] Danezis 等. Square Span Programs with Applications to Succinct NIZK Arguments. **ASIACRYPT 2014** [Google Scholar](https://scholar.google.com/scholar?q=Square+Span+Programs+with+Applications+to+Succinct+NIZK+Arguments)
> 核心思路：引入平方跨度程序（SSP），对布尔电路可满足性问题构造了仅含 2 个群元件的 LIP（布尔情况）。
> 局限与区别：该方法通过将乘法转化为平方（可能增加电路规模）实现大小的缩减，本文则直接对算术电路实现了 2 元件 LIP（通过平方化），但更强调通用情况下的 3 元件构造。

[GW11] Gentry 和 Wichs. Separating Succinct Non-interactive Arguments from All Falsifiable Assumptions. **STOC 2011** [Google Scholar](https://scholar.google.com/scholar?q=Separating+Succinct+Non-interactive+Arguments+from+All+Falsifiable+Assumptions)
> 核心思路：证明 SNARG 无法基于标准可证伪假设构造，必须依赖非可证伪假设（如知识假设或通用群模型）。
> 局限与区别：该负面结果论证了本文采用通用群模型进行安全性分析的合理性。

### 核心技术与方案
本文工作分为两个核心部分：首先，构造了一个仅含 3 个域元素的线性交互证明（LIP）用于二次算术程序（QAP）；然后，将该 LIP 编译为非对称双线性群上的零知识 SNARK。

**第一阶段：3 域元素的 LIP 构造**
该 LIP 包含四元算法。设置阶段选取随机秘密 $\alpha, \beta, \gamma, \delta, x \in \mathbb{F}^*$，生成公开参考串 $\pmb{\sigma}$（包含多个与秘密相关的多项式求值结果）和陷门 $\tau$。证明阶段，给定语句 $a_1,\dots,a_\ell$ 和完整赋值 $a_0=1,a_1,\dots,a_m$（满足 QAP 等式），证明者随机选取 r 和 s，利用 $\pmb{\sigma}$ 中的信息线性组合出三个域元素 $A, B, C$：
$$A = \alpha + \sum_{i=0}^m a_i u_i(x) + r\delta$$
$$B = \beta + \sum_{i=0}^m a_i v_i(x) + s\delta$$
$$C = \frac{\sum_{i=\ell+1}^m a_i (\beta u_i(x) + \alpha v_i(x) + w_i(x)) + h(x)t(x)}{\delta} + As + rB - rs\delta$$
验证阶段，验证者仅需检查一个二次方程：
$$A \cdot B = \alpha \cdot \beta + \frac{\sum_{i=0}^\ell a_i (\beta u_i(x) + \alpha v_i(x) + w_i(x))}{\gamma} \cdot \gamma + C \cdot \delta$$
安全性的核心在于系统变量间的代数结构：$\alpha$ 和 $\beta$ 约束了 $A, B, C$ 所使用的线性组合的一致性；$\gamma$ 和 $\delta$ 隔离了公开语句部分与私有见证及商多项式部分的计算，防止跨项混合攻击；随机数 r, s 提供了零知识。通过 Schwartz-Zippel 引理，证明任何成功的仿射对手策略必然导致一个有效的见证提取，从而证明知识可靠性。

**第二阶段：编译为配对基 SNARK**
将该 LIP 以指数形式嵌入非对称双线性群：$A, C$ 放于 $\mathbb{G}_1$，$B$ 放于 $\mathbb{G}_2$（以利用 $\mathbb{G}_1$ 更短的表示）。参考串 $\sigma$ 包含群元素形式的上述域元素。证明者通过多指数运算计算 $\pi = (A, B, C)$。验证方程变为单一配对乘积等式：
$$e(A, B) = e(G^\alpha, H^\beta) \cdot e\left(G^{\frac{\sum_{i=0}^\ell a_i (\beta u_i(x) + \alpha v_i(x) + w_i(x))}{\gamma}}, H^\gamma\right) \cdot e(C, H^\delta)$$
系统具有完美完备性和完美零知识性。安全性在通用双线性群模型中归约到 LIP 的知识可靠性：由于只有 3 个配对运算，验证复杂度极低。证明大小为 2 个 $\mathbb{G}_1$ 元素和 1 个 $\mathbb{G}_2$ 元素。证明者需 $O(n \log n)$ 域运算（通过 FFT 求商多项式）和约 $(m+3n+3)$ 次 $\mathbb{G}_1$ 指数运算。

**下界结果**
针对 Bitansky 等人 [BCI+13] 的开放问题，作者证明不存在具有线性判决过程的 LIP（对于拥有难判决问题的关系生成器）。核心论证是：线性判决过程意味着所有验证方程线性，此时一个可判断 Yes/No 实例的对手可以通过先构建 Yes 实例上验证矩阵的生成空间，然后检查目标实例的验证矩阵是否落于该空间内，来攻破语言困难性。由此导出，在 Type III 配对基 SNARG 中，证明必须同时包含 $\mathbb{G}_1$ 和 $\mathbb{G}_2$ 元素，排除了单群元素 SNARG 的存在可能。这为 3 元素构造提供了近乎最优的理论下界支持，但 2 元素（各来源组一个）的情况仍未决。

### 核心公式与流程

**[设置算法 Setup]**
$$(\alpha, \beta, \gamma, \delta, x) \xleftarrow{\$} \mathbb{F}_p^{*5}; \quad \tau = (\alpha,\beta,\gamma,\delta,x)$$
$$\sigma = \left(G^\alpha, G^\beta, H^\beta, H^\gamma, G^\delta, H^\delta, \{G^{x^i}\}_{i=0}^{n-1}, \{H^{x^i}\}_{i=0}^{n-1}, \left\{ G^{\frac{\beta u_i(x) + \alpha v_i(x) + w_i(x)}{\gamma}} \right\}_{i=0}^\ell, \left\{ G^{\frac{\beta u_i(x) + \alpha v_i(x) + w_i(x)}{\delta}} \right\}_{i=\ell+1}^m, \left\{ G^{\frac{x^i t(x)}{\delta}} \right\}_{i=0}^{n-2} \right)$$
> 作用：生成具有特定秘密结构的公共参考串，该结构编码了 QAP 的信息。

**[证明算法 Prove]**
$$r, s \xleftarrow{\$} \mathbb{Z}_p; \quad \pi = (A, B, C)$$
$$A = G^{\alpha + \sum_{i=0}^m a_i u_i(x) + r\delta}$$
$$B = H^{\beta + \sum_{i=0}^m a_i v_i(x) + s\delta}$$
$$C = G^{\frac{\sum_{i=\ell+1}^m a_i(\beta u_i(x)+\alpha v_i(x)+w_i(x)) + h(x)t(x)}{\delta} + s(\alpha+\sum_{i=0}^m a_i u_i(x)) + r(\beta+\sum_{i=0}^m a_i v_i(x)) + rs\delta}$$
> 作用：证明者使用见证和随机性计算三个群元素作为证明。

**[验证算法 Verify]**
$$e(A, B) \stackrel{?}{=} e(G^\alpha, H^\beta) \cdot e\left( G^{\frac{\sum_{i=0}^\ell a_i(\beta u_i(x)+\alpha v_i(x)+w_i(x))}{\gamma}}, H^\gamma \right) \cdot e(C, H^\delta)$$
> 作用：验证者通过单一配对乘积等式检查证明的有效性，该等式对应 LIP 的二次方程。

**[模拟算法 Sim]**
$$r,s \xleftarrow{\$} \mathbb{Z}_p; \quad A = G^r; \quad B = H^s; \quad C = G^{\frac{rs - \alpha\beta - \sum_{i=0}^\ell a_i(\beta u_i(x)+\alpha v_i(x)+w_i(x))}{\delta}}$$
> 作用：利用陷门 $\tau = (\alpha,\beta,\delta,x)$ 生成与真实证明不可区分的模拟证明。

### 实验结果
论文并未实现真实系统，而是采用理论比较（表 1 和表 2）展示其方案的性能优势。对于布尔电路可满足性（表 1）：本文方案的 CRS 大小为 $3m+n$ 个 $\mathbb{G}_1$ 和 $m$ 个 $\mathbb{G}_2$，证明大小为 $2\mathbb{G}_1+1\mathbb{G}_2$，证明者计算量仅为 $n$ 次 $\mathbb{G}_1$ 指数运算，验证者计算量为 $\ell$ 次 $\mathbb{G}_1$ 乘法加 3 次配对。与 [DFGK14] 相比，证明从 $3\mathbb{G}_1+1\mathbb{G}_2$ 降至 $2\mathbb{G}_1+1\mathbb{G}_2$，配对从 6 个减至 3 个。对于算术电路（表 2）：在非对称配对设定下，本文方案 CRS 为 $m+2n$ 个 $\mathbb{G}_1$ 和 $n$ 个 $\mathbb{G}_2$，证明为 $2\mathbb{G}_1+1\mathbb{G}_2$，证明者需 $(m+3n-\ell)$ 次 $\mathbb{G}_1$ 指数和 $n$ 次 $\mathbb{G}_2$ 指数，验证者仅需 $\ell$ 次 $\mathbb{G}_1$ 指数和 3 次配对。对比 [SVdV15]（7+1 个群元件，12 次配对），以及 [PHGR13]（8 个对称群元件，11 次配对），本文在所有维度均实现最优。尤其在递归 SNARK 构造 [BCTV14a] 中，由于证明更小、验证更快，递归语句规模变小，预期可减少近一个数量级的证明者计算。

### 局限性与开放问题
本文的方案被证明在通用群模型中安全，但其安全性不依赖于可证伪假设，这是该类 SNARK 的共同特征。主要的开放问题是能否彻底消除证明大小与下界之间的差距：本文排除了单群元素 SNARG，但 2 元素（一个 $\mathbb{G}_1$ 和一个 $\mathbb{G}_2$）SNARG 的存在性既未被构造也未被否定。此外，方案的效率优势在某种程度上依赖将 QAP 的底层多项式求值点预设为 FFT 友好点，对于非结构化电路，证明者的 $O(n\log n)$ 域运算可能带来额外开销。最后，文中对“良性关系生成器”的假设——即辅助输入分布允许知识提取——虽然理论上必要，但在实践中需谨慎对待。

### 强关联论文

[GGPR13] Gennaro 等. Quadratic Span Programs and Succinct NIZKs without PCPs. **EUROCRYPT 2013**

[PHGR13] Parno 等. Pinocchio: Nearly Practical Verifiable Computation. **IEEE S&P 2013**

[BCI+13] Bitansky 等. Succinct Non-interactive Arguments via Linear Interactive Proofs. **TCC 2013**

[DFGK14] Danezis 等. Square Span Programs with Applications to Succinct NIZK Arguments. **ASIACRYPT 2014**

[GW11] Gentry 和 Wichs. Separating Succinct Non-interactive Arguments from All Falsifiable Assumptions. **STOC 2011**

[BCTV14a] Ben-Sasson 等. Scalable Zero Knowledge via Cycles of Elliptic Curves. **CRYPTO 2014**

[BCCT13] Bitansky 等. Recursive Composition and Bootstrapping for SNARKS and Proof-Carrying Data. **STOC 2013**

[SVdV15] Schoenmakers 等. Trinocchio: Privacy-Friendly Outsourcing by Distributed Verifiable Computation. **ePrint 2015**


## 关键词

+ 简洁非交互式知识论证
+ 配对密码学
+ 算术电路可满足性
+ 零知识证明
+ 配对下界证明