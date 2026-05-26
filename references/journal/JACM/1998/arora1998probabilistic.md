---
title: "Probabilistic checking of proofs: a new characterization of NP"
标题简称:
论文类型: journal
期刊简称: JACM
发表年份: 1998
modified: 2025-04-08 12:00:05
---

## Probabilistic checking of proofs: a new characterization of NP

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/273865.273901)

## 作者

+ Sanjeev Arora
+ Shmuel Safra

## 笔记

### 背景与动机
精确求解 NP 完全问题在多项式时间内被认为是不可行的，但近似解的计算难度长期以来难以刻画。例如团问题的近似算法，最佳结果仅能达到 $O(n / \log^2 n)$ 的近似比，而证明其存在常数近似比为 NP 难久未解决。Feige 等人于 1991 年取得突破，指出若团常数可常数近似，则 NP 问题可在 $n^{O(\log \log n)}$ 时间内确定性地求解，即 “几乎” 为 NP 难，但并未完成标准 NP 难的证明 [Feige et al. 1991]。本文的直接动机是填补这一空白，证明团问题的任何常数因子近似均为 NP 难。更深层的驱动力来自交互式证明与概率可检验证明的理论进展：Babai 等人证明了 MIP = NEXPTIME [Babai et al. 1991b]，而 Feige 等人将其“缩放”后用于逼近问题 [Feige et al. 1991]。然而，这些缩放版本产生的验证者在随机位与查询位之间仍存在权衡，尚未达到最优。本文试图给出 NP 类的一个新的精确刻画，即 NP 中的语言拥有仅使用对数随机位和对数查询位的概率可检验证明系统，从而为多种近似问题的 NP 难性证明提供统一框架。

### 相关工作

[Feige et al. 1991] Feige, U. et al. Approximating Clique is Almost NP-Complete. **FOCS 1991** [Google Scholar](https://scholar.google.com/scholar?q=Approximating+Clique+is+Almost+NP-Complete)
> 核心思路：利用交互式证明中的缩放结果，将团近似问题归约到一种特殊的验证器，表明若可常数近似，则 NP 可在 $n^{O(\log \log n)}$ 时间内求解。
> 局限与区别：该结果只是“几乎”NP 难，未能证明标准 NP 难；本文在此基础上改进了验证器的效率，将查询数降低到对数级别，从而证明了常数近似团问题为 NP 难。

[Babai et al. 1991b] Babai, L. et al. Non-deterministic Exponential Time has Two-prover Interactive Protocols. **Comput. Complex. 1991** [Google Scholar](https://scholar.google.com/scholar?q=Non-deterministic+Exponential+Time+has+Two-prover+Interactive+Protocols)
> 核心思路：证明 MIP = NEXPTIME，即非确定性指数时间类中的语言可由多证明者交互式验证。
> 局限与区别：该结果是本工作的理论基础，但本文将其“缩放”至 NP 并聚焦于验证者的随机性和查询复杂度，而 MIP 结果中验证者可能需要多项式随机位与查询。

[Fortnow et al. 1988] Fortnow, L. et al. On the Power of Multi-prover Interactive Protocols. **Structure in Complexity Theory 1988** [Google Scholar](https://scholar.google.com/scholar?q=On+the+Power+of+Multi-prover+Interactive+Protocols)
> 核心思路：提出了 MIP 的等价形式（随机图灵机与预言机交互），即概率可检验证明的雏形。
> 局限与区别：该工作主要关注复杂性类的定性包含关系，而非验证者资源的具体限制（如对数随机位和查询位）。

[Goldwasser et al. 1989] Goldwasser, S. et al. The Knowledge Complexity of Interactive Proofs. **SIAM J. Comput. 1989** [Google Scholar](https://scholar.google.com/scholar?q=The+Knowledge+Complexity+of+Interactive+Proofs)
> 核心思路：引入交互式证明模型，定义知识复杂性。
> 局限与区别：本文使用的是 MIP 模型（多证明者）而非 IP，两者的区别在于证明者之间能否通信；此外本文更侧重于验证资源的最小化。

[Lund et al. 1992] Lund, C. et al. Algebraic Methods for Interactive Proof Systems. **J. ACM 1992** [Google Scholar](https://scholar.google.com/scholar?q=Algebraic+Methods+for+Interactive+Proof+Systems)
> 核心思路：利用代数方法证明 IP = PSPACE，其中使用 Sum-Check 协议。
> 局限与区别：Sum-Check 协议是本文核心组件之一，但 Lund 等人将其用于验证 PSPACE 中的问题，本文则将其适配并用于 NP 的 PCP 验证器中。

[Shamir 1992] Shamir, A. IP = PSPACE. **J. ACM 1992** [Google Scholar](https://scholar.google.com/scholar?q=IP+%3D+PSPACE)
> 核心思路：独立证明 IP = PSPACE。
> 局限与区别：同 Lund 等人，Shamir 的工作基于 IP 模型，本文需要多证明者/唯一证明者模型来实现更紧的资源界限。

[Babai et al. 1991a] Babai, L. et al. Checking Computations in Polylogarithmic Time. **STOC 1991** [Google Scholar](https://scholar.google.com/scholar?q=Checking+Computations+in+Polylogarithmic+Time)
> 核心思路：提出在编码输入下，用 polylog 时间验证 NP 证明的模型。
> 局限与区别：该工作改变了计算模型（编码输入），本文则在不改变标准模型下，仅限制随机位和查询位，且实现了对数随机位和亚对数查询位。

[Alon et al. 1992] Alon, N. et al. Simple Constructions of Almost k-wise Independent Random Variables. **Rand. Struct. Algor. 1992** [Google Scholar](https://scholar.google.com/scholar?q=Simple+Constructions+of+Almost+k-wise+Independent+Random+Variables)
> 核心思路：构造近似 k-wise 独立的随机变量。
> 局限与区别：该项技术曾被视为低度测试取样的替代思路，但本文直接使用基于多项式性质的确定性分析，且改进后的分析仅需 $O(m)$ 次查询，而非 $O(mh)$。

[Papadimitriou and Yannakakis 1991] Papadimitriou, C. and Yannakakis, M. Optimization, Approximation and Complexity Classes. **J. Comput. Syst. Sci. 1991** [Google Scholar](https://scholar.google.com/scholar?q=Optimization%2C+Approximation+and+Complexity+Classes)
> 核心思路：定义 MAX-SNP 类，并建立近似难度与完全性理论。
> 局限与区别：本文的结果（特别是后来的 PCP 定理）直接冲击了 MAX-SNP 的近似难度，但本文本身主要关注团问题，未涉及 MAX-SNP。

### 核心技术与方案

本文的核心是证明 **NP = PCP(log n, log n)**。证明的关键在于构造一种“正规形式”的验证者，并利用“验证者合成”技术逐步提升效率。

首先，作者定义了 PCP 类：一个语言 $L$ 属于 $\text{PCP}(r(n), q(n))$，若存在一个概率多项式时间验证者 $M$，对大小为 $n$ 的输入 $x$，它使用 $O(r(n))$ 随机位，查询 $O(q(n))$ 个证明位，并且：若 $x \in L$，则存在一个证明 $\Pi$ 使得 $M$ 以概率 1 接受；若 $x \notin L$，则对所有证明 $\Pi$，$M$ 接受的概率 $<1/2$。验证者的查询是非自适应的：它先根据输入和随机位决定查询的位置，然后一次性读出所有查询位的值。

为了刻画更精细的复杂性，本文引入了 RPCP（受限 PCP）类，它额外参数化了验证者使用的字母表大小 $2^{s(n)}$和决策时间 $t(n)$。一个 RPCP 验证者使用大小为 $2^{O(s(n))}$的字母表，进行 $O(q(n))$ 次查询，每次读取一个字母符号，且其第三阶段（基于读取的符号决定接受/拒绝）的运行时间为 $O(t(n))$。

**正规形式验证者**是合成技术的核心。一个 $(r(n), s(n), q(n), t(n))$-约束的正规形式验证者 $V$ 具有以下能力：给定一个 3CNF 公式 $\varphi$ 和整数 $p$，它可以检查一个 $p$ 部分拆分编码的赋值是否满足 $\varphi$。具体地，证明被期望为 $\sigma(z_1) \# \dots \# \sigma(z_p) \# \pi$，其中 $\sigma$ 是一个编码方案（基于多项式扩展），$z_i$ 是部分赋值。若每个 $z_i$ 都是有效的码字，且它们的拼接是满足性赋值，则存在 $\pi$ 使 $V$ 以概率 1 接受。若任何 $z_i$ 不接近任何码字，或拼接不满足公式，则所有 $\pi$ 下接受概率 $<1/2$。该验证者只需要 $O(r(n))$ 随机位、使用大小为 $2^{O(s(n))}$的字母表、进行 $O(p + q(n))$ 次查询，决策时间为 $O(p \cdot t(n))$。

**验证者合成引理** (Lemma 3.4) 是效率提升的关键。假设存在一个 $(r(n), s(n), q(n), t(n))$-约束的正规形式验证者 $V_2$，则对于任何 RPCP 验证者 $V_1$，可以“合成”一个新的验证者 $V_{\text{new}}$。$V_{\text{new}}$ 不直接读取 $V_1$ 要查询的原始符号，而是期望证明中给出这些符号的编码（使用 $V_2$的编码方案）。然后，$V_{\text{new}}$ 调用 $V_2$ 来检查 $V_1$ 的决策电路（大小为 $O(T^2)$，$T$ 是 $V_1$ 的决策时间）对应的 3CNF 公式是否被这些编码的赋值所满足。合成后，新验证者的随机位为 $O(R + r(\tau))$，字母表大小为 $2^{s(\tau)}$，查询数为 $O(Q + q(\tau))$，决策时间为 $O(Q \cdot t(\tau))$，其中 $\tau = O(T^2)$。由于 $\tau$ 远小于 $n$，这一过程能显著降低查询位数。

**定理 3.5** 的核心是构造一个具体的正规形式验证者。其核心思想是使用多项式编码和代数表示：将赋值（$n = (h+1)^m$ 位）编码为一个 $m$ 元 $h$ 次多项式 $f$。然后，验证者利用 3SAT 的代数表示：存在一族多项式 $\{P_i^f\}$，使得若 $f$ 对应一个满足性赋值，则每个 $P_i^f$ 在 $[0,h]^{4m}$ 上的和为 0；否则，对大部分 $i$ 这个和不为 0。验证者首先使用**低度测试** (Procedure 2) 检查 $f$ 是否接近一个 $h$ 次多项式。若通过，它随机选择一个 $P_i^f$，并使用**Sum-Check 协议** (Procedure 1) 验证它是否在 $[0,h]^{4m}$ 上求和为 0。Sum-Check 需要读取 $P_i^f$ 在一个随机点的值，这又需要 $f$ 在 3 个随机点的值，由于 $f$ 接近低度多项式，直接用 $f$ 的值代替是安全的。该验证者是 $(\log n, h \log h, m, \text{poly}(h))$-约束的。其中，低度测试的改进分析（Lemma 4.6.4, Lemma 5.2.1）是关键，它允许将所需查询数从 $O(mh)$ 降至 $O(m)$。

最终，通过递归应用合成引理，从初始的 $(\log n, 2^{O(\sqrt{\log n})}, \sqrt{\log n}, 2^{O(\sqrt{\log n})})$ 验证者出发，经过若干轮合成，逐步降低验证者使用的字母表大小和决策时间，最终将查询位数降至 $\log^{0.5+\epsilon} n$，从而证明了 NP $\subseteq$ PCP(log n, $\log^{0.5+\epsilon} n$)。结合已知的 NP = PCP(0, poly(n)) 和逆包含关系，即有 NP = PCP(log n, $\log^{0.5+\epsilon} n$)。

### 核心公式与流程

**[NP的PCP刻画]**
$$\text{NP} = \text{PCP}(\log n, \log n)$$
> 作用：核心定理，表明NP类中的语言拥有一个使用对数随机位和对数查询位的概率可检验证明系统。

**[验证者合成引理]**
若存在一个$(r(n), s(n), q(n), t(n))$-约束的正规形式验证者 $V_2$，则
$$\text{RPCP}(R(n), S(n), Q(n), T(n)) \subseteq \text{RPCP}(R(n) + r(\tau), s(\tau), Q(n) + q(\tau), Q(n) \cdot t(\tau))$$
其中 $\tau = O(T(n)^2)$。
> 作用：合成引理是效率提升的核心技术，允许将繁重的检查工作委托给一个更高效的子验证者，从而降低总查询位数。

**[低度测试性质]**
设 $f: \mathbb{F}^l \to \mathbb{F}$，若 $f$ 是 $\text{F}_d[y_1, \dots, y_l]$ 中的多项式，则存在表格 $T$ 使测试以概率 1 接受；若 $f$ 不是 $\delta$-接近该多项式族（$\delta < 0.01$），则测试拒绝概率 $\geq 3/4$。测试需 $O(1/\delta)$ 个点值和 $O(l/\delta)$ 个表项查询。
> 作用：低度测试保证证明中提供的函数确实接近一个低次多项式，这是后续代数检查的前提。改进后的分析将查询数从 $O(lh)$ 降到 $O(l)$。

**[Sum-Check 协议正确性]**
$$\Pr[\text{Sum-Check rejects}] \geq 1 - \frac{d l}{q}$$
若 $B \in \text{F}_d[x_1, \dots, x_l]$ 在 $H^l$ 上的和不为 $c$，则协议拒绝概率至少为 $1 - dl/q$。
> 作用：Sum-Check 提供了一种高效的方法（使用 $O(l)$ 次查询和 $O(l \log q)$ 随机位）来验证一个多项式的和是否等于给定值，是验证代数条件的核心。

### 实验结果
本文是纯粹的理论计算机科学论文，不涉及传统意义上的实验。其为近似算法与计算复杂性理论提供了深刻的结构性结果。核心“实验”成果体现在：
第一，证明了团问题的常数因子近似是 NP 难的，这直接解决了悬而未决的难题。进一步地，结果显示即使近似因子达到 $2^{\log^{0.5-\epsilon} n}$（$n$ 为图顶点数，$\epsilon$ 为任意正常数）仍是 NP 难的。
第二，给出了一个关于 NP 类的新的“概率可检验证明”刻画，即 NP = PCP(log n, log n)，这一刻画是紧的（若 P $\neq$ NP），因为若随机位或查询位为 $o(\log n)$ 则可推得 NP = P。
第三，该工作为后续一系列近似难度结果（例如 MAX-3SAT 的不可近似性）奠定了基础，这些后续结果在 Arora 等人的后续论文 [Arora et al. 1992] 中得到了实验验证（即在理论意义上证明了近似问题是 NP 难）。
本文的结果也直接影响了后续对 PCP 常数查询位（PCP(log n, 1)）的证明进程，后者进一步优化了近似难度的界限。

### 局限性与开放问题
本文的核心定理 NP = PCP(log n, log n) 已经接近最优，但其证明中使用的字段大小远大于 $\log n$，这导致证明长度较大。一个开放问题是如何进一步降低证明长度，例如达到 $n^{1+\epsilon}$，这在后续的 Polishchuk 和 Spielman 的工作中得到了部分解决。另一个开放问题是能否将查询数进一步降低到常数，即是否 NP = PCP(log n, 1)，这一猜想在本文发表后的紧凑结果 [Arora et al. 1992a] 中被证实。本文提出的合成技术虽然强大，但递归应用时对常数因子有累积效应，当时尚未得到最优的常数查询位数。

### 强关联论文

[Feige et al. 1991] Feige, U. et al. Approximating Clique is Almost NP-Complete. **FOCS 1991** [Google Scholar](https://scholar.google.com/scholar?q=Approximating+Clique+is+Almost+NP-Complete)

[Babai et al. 1991a] Babai, L. et al. Checking Computations in Polylogarithmic Time. **STOC 1991** [Google Scholar](https://scholar.google.com/scholar?q=Checking+Computations+in+Polylogarithmic+Time)

[Babai et al. 1991b] Babai, L. et al. Non-deterministic Exponential Time has Two-prover Interactive Protocols. **Comput. Complex. 1991** [Google Scholar](https://scholar.google.com/scholar?q=Non-deterministic+Exponential+Time+has+Two-prover+Interactive+Protocols)

[Goldwasser et al. 1989] Goldwasser, S. et al. The Knowledge Complexity of Interactive Proofs. **SIAM J. Comput. 1989** [Google Scholar](https://scholar.google.com/scholar?q=The+Knowledge+Complexity+of+Interactive+Proofs)

[Lund et al. 1992] Lund, C. et al. Algebraic Methods for Interactive Proof Systems. **J. ACM 1992** [Google Scholar](https://scholar.google.com/scholar?q=Algebraic+Methods+for+Interactive+Proof+Systems)

[Shamir 1992] Shamir, A. IP = PSPACE. **J. ACM 1992** [Google Scholar](https://scholar.google.com/scholar?q=IP+%3D+PSPACE)

[Fortnow et al. 1988] Fortnow, L. et al. On the Power of Multi-prover Interactive Protocols. **Structure in Complexity Theory 1988** [Google Scholar](https://scholar.google.com/scholar?q=On+the+Power+of+Multi-prover+Interactive+Protocols)

[Papadimitriou and Yannakakis 1991] Papadimitriou, C. and Yannakakis, M. Optimization, Approximation and Complexity Classes. **J. Comput. Syst. Sci. 1991** [Google Scholar](https://scholar.google.com/scholar?q=Optimization%2C+Approximation+and+Complexity+Classes)

[Arora et al. 1992a] Arora, S. et al. Proof Verification and Intractability of Approximation Problems. **FOCS 1992** [Google Scholar](https://scholar.google.com/scholar?q=Proof+Verification+and+Intractability+of+Approximation+Problems)

[Alon et al. 1992] Alon, N. et al. Simple Constructions of Almost k-wise Independent Random Variables. **Rand. Struct. Algor. 1992** [Google Scholar](https://scholar.google.com/scholar?q=Simple+Constructions+of+Almost+k-wise+Independent+Random+Variables)


## 关键词

+ NP新特征概率可检验证明
+ 对数随机位多项式验证
+ 近似最大团NP难度
+ PCP定理基础
+ 概率证明验证系统
+ 计算复杂度NP完全性