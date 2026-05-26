---
title: "Checking computations in polylogarithmic time"
标题简称:
论文类型: conference
会议简称: STOC
发表年份: 1991
modified: 2025-04-08 11:55:33
---

## Checking computations in polylogarithmic time

## 发表信息

+ [原文链接](https://dl.acm.org/doi/10.1145/103418.103428)


## 作者

+ László Babai
+ Lance Fortnow
+ Leonid A. Levin
+ Mario Szegedy

## 笔记

### 背景与动机

如何确保大规模计算或超长数学证明的正确性是一个基础性问题。传统的确定性验证需要重复整个计算过程，当计算规模巨大或涉及不可靠的软硬件时，代价过高。Manuel Blum 提出的实例检查概念试图通过高效的概率性检查来缓解这一困境，但已有的交互式证明协议 [LFKN, Sh] 以及 MIP = NEXP 协议 [BFL] 虽然证明了多项式时间可验证性，但检查时间仍为多项式级别，无法达到 polylog 级。本文的核心动机是：能否将任何非确定性计算任务（包括数学证明）转化为一种“透明证明”，使得验证者仅需 polylog 时间（即对数级别）即可高概率地判断其正确性，同时保持原证明的完备性和可计算性。这一目标在软件和硬件可靠性成本高昂的场景下尤为关键：一个极小的、可硬连线的检查器可以监督一群使用不可靠软件和未经测试硬件的超级计算机。

### 相关工作

[LFKN] Lund, Fortnow, Karloff, Nisan. *Algebraic Methods for Interactive Proof Systems*. **FOCS 1990** [Google Scholar](https://scholar.google.com/scholar?q=Algebraic+Methods+for+Interactive+Proof+Systems)
> 核心思路：利用多项式算术化将求和验证转化为单变量多项式插值，并设计了 LFKN 协议，证明了 #P 可在交互式证明中验证。
> 局限与区别：该协议需要多项式时间（或交互轮数随问题规模增长）且假设证明方提供低次多项式，但尚未解决 polylog 时间验证问题，且未处理错误容忍。

[Sh] Shamir. *IP = PSPACE*. **FOCS 1990** [Google Scholar](https://scholar.google.com/scholar?q=IP=PSPACE)
> 核心思路：将 PSPACE 问题算术化并通过交互式证明系统验证，展示了代数方法的强大能力。
> 局限与区别：验证时间仍为多项式，且未涉及对证明本身的错误容错或极快检查。

[BFL] Babai, Fortnow, Lund. *Non-Deterministic Exponential Time Has Two-Prover Interactive Protocols*. **Computational Complexity 1991** [Google Scholar](https://scholar.google.com/scholar?q=Non-Deterministic+Exponential+Time+Has+Two-Prover+Interactive+Protocols)
> 核心思路：利用低次多项式扩展和 LFKN 型协议，证明了 NEXP 具有多证明人交互证明，并提出了多项式编码与低次检验方法。
> 局限与区别：其透明证明的构造需要表大小为 $N^{\Theta(\log\log N)}$（因直接使用多线性扩展），指数时间过长；本文通过引入中等大小的子域 $H$ 并采用 $|H|$ -平滑扩展，将表大小压缩到 $N^{1+\Theta(\varepsilon)}$，从而实现了 polylog 时间验证和多项式时间编辑。

[BK] Blum, Kannan. *Designing Programs that Check Their Work*. **STOC 1989** [Google Scholar](https://scholar.google.com/scholar?q=Designing+Programs+that+Check+Their+Work)
> 核心思路：提出 Blum-Kannan 程序检查器定义，要求程序宣称计算某语言 L 时，检查器能高概率判断程序是否对所有输入正确，或对给定输入是否正确。
> 局限与区别：检查器需要与程序交互且运行时间为多项式；本文的检查器无需交互，运行时间为 polylog，但限制了必须将输入/输出编码为错误校正形式，且检查的是“特定计算”而非语言。

[BeF] Beaver, Feigenbaum. *Hiding Instances in Multioracle Queries*. **STACS 1990** [Google Scholar](https://scholar.google.com/scholar?q=Hiding+Instances+in+Multioracle+Queries)
> 核心思路：提出随机自归约思想，允许从有噪声的函数近似中恢复多项式的值。
> 局限与区别：该技术需要 $|F| \ge d+2$ 以及 $\alpha<1/(2d)$ 的噪声界限；本文结合 [BGW] 的纠错技术将其改进为可容忍 15% 的常数噪声。

[BGW] Ben-Or, Goldwasser, Wigderson. *Completeness Theorems for Non-Cryptographic Fault-Tolerant Distributed Computation*. **STOC 1988** [Google Scholar](https://scholar.google.com/scholar?q=Completeness+Theorems+for+Non-Cryptographic+Fault-Tolerant+Distributed+Computation)
> 核心思路：利用低次多项式的 Reed-Muller 码性质，设计秘密分享中可容忍三分之一错误参与者的协议。
> 局限与区别：本文将其用于函数逼近纠错，并证明了在 $|F|$ 足够大时，从 15% 误差恢复多项式是可能的。

[Swz] Schwartz. *Fast Probabilistic Algorithms for Verification of Polynomial Identities*. **J. ACM 1980** [Google Scholar](https://scholar.google.com/scholar?q=Fast+Probabilistic+Algorithms+for+Verification+of+Polynomial+Identities)
> 核心思路：引理指出次数为 d 的 m 元多项式在域的子集 I^m 上最多有 d/|I| 的比例为零点。
> 局限与区别：该引理为低次多项式编码的距离分析提供了基础，本文用于证明低次扩展的纠错能力（码距至少 75%）。

[KU] Kolmogorov, Uspenskii. *On the Definition of an Algorithm*. **Uspekhi Mat. Nauk 1958** [Google Scholar](https://scholar.google.com/scholar?q=On+the+Definition+of+an+Algorithm)
> 核心思路：提出指针机模型，认为其可以在常数因子内模拟任何现实计算模型。
> 局限与区别：本文采纳该论文，将“快”定义为近线性时间（线性乘 polylog），并基于指针机/RAM 定义 NF 类（非确定性快速），进而构造 NF 完全问题——骨牌问题。

[LG] Levin, Gács. *Causal Nets or What Is a Deterministic Computation?*. **Information and Control 1982** [Google Scholar](https://scholar.google.com/scholar?q=Causal+Nets+or+What+Is+a+Deterministic+Computation)
> 核心思路：提出因果网概念，将计算历史表示成图结构，使得验证可以用固定结构的排序网络在 polylog 并行时间内完成。
> 局限与区别：本文在此基础上设计了骨牌问题的验证结构，实现了 NF 完全性的约化。

### 核心技术与方案

**整体框架** 本文的核心是构造一个“友好的概率扩展”证明系统：给定任意确定性证明系统（即 NP 类问题），可以在多项式时间内将任何证明转换为透明证明，使得验证者只需 polylog 时间即可高概率接受或拒绝。转换分为两个主要层次：首先将计算问题（或数学证明）编码为一个组合问题——骨牌问题（Domino Problem），该问题是 NF 完全（非确定性近线性时间）的；然后利用代数方法将骨牌问题的可满足性条件算术化为多元低次多项式的零点验证，再通过 LFKN 型协议及错误容忍编码实现 polylog 验证。

---

#### 第一层：从计算到组合（骨牌问题）

本文采用 Kolmogorov-Uspenskii 指针机模型（等价于 RAM）作为计算模型，定义 NF 类为在近线性时间内可解决的非确定性问题。为了得到一个 NF 完全问题，将计算的历史（RAM 的寄存器状态序列）压缩为近线性长度的记录（通过排序网络消除冗余）。具体地，将计算历史看作对固定结构的排序网络的着色（每个门在每个时刻的比特值），正确性等价于某些局部一致性条件（相邻节点的颜色对必须属于允许的“骨牌”集）。由此引出骨牌问题：给定一个标准图族 $G_n$（如 Shuffle-Exchange 图），图的大小为 $\Theta(2^n)$，以及一个骨牌集和基色序列（代表输入），要求将图的所有节点染色，使得每条边对应的颜色对属于骨牌集，并且基区域的颜色与给定序列一致。该问题是 NF 完全的，即任何 NF 问题都可以通过 polylog 时间的实例变换和近线性时间的见证变换约化到它。因此，只需针对骨牌问题构造透明证明即可。

---

#### 第二层：骨牌问题的算术化

令 $A: V \to C$ 是一个染色（$C \subset \mathbf{F}$ 为颜色集）。为构造代数条件，选取集合 $H \subset \mathbf{F}$，$|H| = 2^\ell$，其中 $\ell = \Theta(\log n / \varepsilon)$，并令 $m = n/\ell$（视为整数），从而将 $V$ 与 $H^m$ 等同。将 $A$ 唯一扩展到 $|H|$-平滑（即每个变量次数 $\le |H|$）的多项式 $\widetilde{A}: \mathbf{I}^m \to \mathbf{F}$，其中 $\mathbf{I} \subset \mathbf{F}$ 是尺寸为 $\Theta(n^2 |H|)$ 的集合（以保证低次测试和 Schwartz 引理的效果）。骨牌问题的局部条件（每条边两端颜色及边类型必须属于允许集 $D$）可以转化为两类多项式在 $H^m$ 上的零点条件：

1. 对于每个不允许的骨牌 $\delta \in D_0\setminus D$，构造多项式 $\varphi_\delta^A(e) = \psi_\delta( \widetilde{A}(P_1(e)), \widetilde{A}(P_2(e)), P_3(e) )$，要求在 $e \in E$（即 $H^m$）上恒为零。
2. 颜色集条件：$f(t)=\prod_{\gamma \in C} (t-\gamma)$，要求在 $v \in V$ 上 $f(\widetilde{A}(v))=0$。

所有多项式次数均为 $|H|^{O(1)}$ 乘以 $n^{c_1+1/\varepsilon}$。验证这些零点等价于验证求和式 $\sum_{x\in H^m} (\text{各项平方}) = 0$，可以利用 LFKN 型协议实现。

---

#### 第三层：LFKN 型验证与错误容忍

对于形如 $\sum_{u \in H^m} f(u) = a$ 的等式，LFKN 协议（Sec 5.1）通过 $m$ 轮交互验证：每轮将求和变量减少一个，最终退化到单个多项式值。本文需要验证的是所有多项式为零（即求和为零），这可以通过求和平方或利用 Sec 5.2 的随机化技巧（将多项式视为 $p(t)=\sum f(u)t^{\sigma(u)}$，验证随机点 $p(\xi)=0$）转化为一个求和验证。透明证明包含了所有必要的中间多项式表（$\widetilde{A}$ 的值以及各层部分和）。最终，为了抵抗证明中可能出现的少量错误（如硬件错误导致个别比特翻转），将整个透明证明 $P_0$ 用 Theorem 4.6 的错误校正码进一步编码得到 $P'$。该编码具有以下性质：若 $P'$ 与某个有效码字相距 $\le 10\%$，则可在 polylog 时间内恢复每一位；若相距 $\ge 15\%$，则高概率拒绝。因此检查器只需在 polylog 时间内在 $P'$ 上重建所需的每一位 $P_0$ 的数据，然后运行 LFKN 协议即可。由于检查器不需要交互（透明证明是静态的），其运行时间即为 $(\log \|T,P\|)^{O(1/\varepsilon)}$。

---

#### 复杂度总结

- **编辑阶段**（Solver/Editor）：给定原始证明 $W$，可在时间 $\|W\|^{1+\varepsilon}$ 内计算透明证明 $E(W)$（包括低次扩展、部分和表、纠错编码）。
- **检查阶段**（Checker）：在 $(\log \|T,P\|)^{O(1/\varepsilon)}$ 时间内完成验证，随机访问 $O((\log N)^{O(1/\varepsilon)})$ 个比特。
- **错误容忍**：若定理候选 $T$ 或证明 $P$ 存在 $\le 10\%$ 的错误（Hamming 距离），可唯一恢复正确的 $T'$ 和 $P'$；若存在 $\ge 15\%$ 错误则高概率拒绝。
- **编码开销**：透明证明长度 $\le \|W\|^{1+\varepsilon}$，纠错编码后长度增加但仍在 $N^{1+\varepsilon}$ 内。

### 核心公式与流程

**[低次扩展公式]**
$$ g_u(x) = \prod_{i=1}^m \prod_{h \in H_i \setminus \{u_i\}} (x_i - h), \quad \widetilde{f}(x) = \sum_{u \in H^m} f(u) \frac{g_u(x)}{g_u(u)} $$
> 作用：将任意函数 $f: H^m \to \mathbf{F}$ 唯一扩展为每个变量次数 $\le |H|$ 的多项式 $\widetilde{f}$。

**[Schwartz 引理]**
$$ \Pr_{x \in \mathbf{I}^m}[f(x)=0] \le \frac{d}{|\mathbf{I}|} $$
> 作用：低次多项式在有限域子集上零点比例受次数与子集大小之比限制，保证编码距离。

**[LFKN 协议核心递推]**
$$ f_{i-1}(x_1,\dots,x_{i-1}) = \sum_{h \in H} f_i(x_1,\dots,x_{i-1},h) $$
> 作用：将 $m$ 维求和逐轮降维至单变量多项式，每轮通过插值和随机抽样验证一致性。

**[纠错编码构造]**
$$ N = 2^{m\ell} \cdot k, \quad \mathbf{F} = GF(2^k), \quad H \subset \mathbf{F}, |H| = 2^\ell, \quad E_0(x): H^m \to \mathbf{F} \text{ 的 } |H|\text{-平滑扩展} $$
> 作用：利用低次多项式构造具有 75% 最小距离的纠错码，且可在 polylog 时间内恢复任意比特。

**[骨牌问题代数化]**
$$ f(t) = \prod_{\gamma \in C} (t-\gamma), \quad \varphi_\delta^A(e) = \psi_\delta( A(P_1(e)), A(P_2(e)), P_3(e) ) $$
> 作用：将染色合法性转化为若干多项式在 $H^m$ 上的零点条件，从而可用求和协议验证。

### 实验结果

本文为纯理论论文，无传统实验。但提供了关键参数分析和复杂度对比：

- **参数选择**：令 $|H| = 2^\ell$，$\ell = \Theta(\log n / \varepsilon)$，$m = n/\ell$，则透明证明大小 $|\mathbf{I}|^m = N (|I|/|H|)^m = N (\Theta(n^2))^m = N^{1+\Theta(\varepsilon)}$。当 $\varepsilon=0.1$ 时，证明长度约为原长度的 $N^{1.1}$ 倍。
- **检查时间**：$(\log N)^{O(1/\varepsilon)}$，例如 $\varepsilon=0.1$ 时，检查时间为 $(\log N)^{O(10)}$。对于 $N=2^{300}$（宇宙粒子数），$\log N \approx 300$，检查时间约 $300^{O(10)}$ 次操作，实际可行。
- **错误容忍能力**：Theorem 4.6 保证若字符串与有效码字 Hamming 距离 $\le 10\%$，可在 polylog 时间内恢复每一位；若 $\ge 15\%$ 则高概率拒绝。容错率 10% 对应了实用硬件错误率的上限。
- **与 Blum-Kannan 检查器的对比**：本文的检查器无需交互，运行时间 polylog 而非多项式，但要求输入/输出为错误校正编码形式，且仅检查特定计算（而非语言）。相比之下，后者需要交互且时间为多项式，但无需编码假设。

### 局限性与开放问题

本文的构造中检查时间的指数依赖于 $1/\varepsilon$，即 $(\log N)^{O(1/\varepsilon)}$，如何消除该指数依赖（即实现真正的 polylog 而非 $(\log)^{O(1/\varepsilon)}$）是一个有趣的开问题。此外，透明证明的长度为 $N^{1+\varepsilon}$，当 $\varepsilon$ 很小时，虽然检查更快，但证明长度增长到近二次，实际可用性受限。另外，定理候选必须编码为错误校正形式，对于短定理（如数学命题）仍需假设其自包含性极长，这在实践中可能不自然。最后，是否能在保持 polylog 时间的同时减少编码开销至接近线性，是进一步研究方向。

### 强关联论文

[LFKN] Lund, Fortnow, Karloff, Nisan. *Algebraic Methods for Interactive Proof Systems*. **FOCS 1990** [Google Scholar](https://scholar.google.com/scholar?q=Algebraic+Methods+for+Interactive+Proof+Systems)

[Sh] Shamir. *IP = PSPACE*. **FOCS 1990** [Google Scholar](https://scholar.google.com/scholar?q=IP=PSPACE)

[BFL] Babai, Fortnow, Lund. *Non-Deterministic Exponential Time Has Two-Prover Interactive Protocols*. **Computational Complexity 1991** [Google Scholar](https://scholar.google.com/scholar?q=Non-Deterministic+Exponential+Time+Has+Two-Prover+Interactive+Protocols)

[BK] Blum, Kannan. *Designing Programs that Check Their Work*. **STOC 1989** [Google Scholar](https://scholar.google.com/scholar?q=Designing+Programs+that+Check+Their+Work)

[BeF] Beaver, Feigenbaum. *Hiding Instances in Multioracle Queries*. **STACS 1990** [Google Scholar](https://scholar.google.com/scholar?q=Hiding+Instances+in+Multioracle+Queries)

[BGW] Ben-Or, Goldwasser, Wigderson. *Completeness Theorems for Non-Cryptographic Fault-Tolerant Distributed Computation*. **STOC 1988** [Google Scholar](https://scholar.google.com/scholar?q=Completeness+Theorems+for+Non-Cryptographic+Fault-Tolerant+Distributed+Computation)

[Swz] Schwartz. *Fast Probabilistic Algorithms for Verification of Polynomial Identities*. **J. ACM 1980** [Google Scholar](https://scholar.google.com/scholar?q=Fast+Probabilistic+Algorithms+for+Verification+of+Polynomial+Identities)

[KU] Kolmogorov, Uspenskii. *On the Definition of an Algorithm*. **Uspekhi Mat. Nauk 1958** [Google Scholar](https://scholar.google.com/scholar?q=On+the+Definition+of+an+Algorithm)

[Li] Lipton. *New Directions in Testing*. **Manuscript 1989** [Google Scholar](https://scholar.google.com/scholar?q=New+Directions+in+Testing)

[Sz] Szegedy. *Efficient MIP Protocol and a Stronger Condition on Clique Approximation*. **In preparation** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+MIP+Protocol+and+a+Stronger+Condition+on+Clique+Approximation)


## 关键词

+ 概率可检验证明PCP
+ 多项式时间计算验证
+ 低度多项式测试
+ 多证明者交互证明MIP
+ 简洁证明系统
+ 代数编码计算