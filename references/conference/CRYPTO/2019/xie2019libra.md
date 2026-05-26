---
title: "Libra: Succinct Zero-Knowledge Proofs with Optimal Prover Computation"

标题简称: Libra
论文类型: conference
会议简称: CRYPTO
发表年份: 2019
modified: 2025-04-08 22:03:37
---

## Libra: Succinct Zero-Knowledge Proofs with Optimal Prover Computation

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-030-26954-8_24)

## 作者

+ [Tiancheng Xie](Tiancheng%20Xie.md)
+ [Jiaheng Zhang](Jiaheng%20Zhang.md)
+ [Yupeng Zhang](Yupeng%20Zhang.md)
+ [Charalampos Papamanthou](Charalampos%20Papamanthou.md)
+ [Dawn Song](Dawn%20Song.md)

此篇paper的作者都是高手

## 笔记

### 背景与动机
零知识证明（ZKP）协议正从纯理论走向实际部署，在加密货币隐私交易和区块链研究中扮演关键角色，但其证明生成（Prover）时间始终是扩展性瓶颈。现有系统普遍面临超线性计算开销，例如 libSNARK 的 $O(C \log C)$ 或 libSTARK 的 $O(C \log^2 C)$ ，其中 $C$ 是电路规模。尽管 Bulletproofs [16] 实现了线性证明时间，但其验证时间也呈线性增长，未能同时满足简洁性和最优证明效率。目前尚缺乏一个同时具备最优线性证明时间、简洁证明大小和亚线性验证时间的 ZKP 系统。Libra 填补了这一空白，它是首个针对对数空间均匀电路同时达到上述三项指标的零知识证明系统，且仅需一次与输入大小相关的可信设置。

### 相关工作

[30] Goldwasser 等. Delegating computation: interactive proofs for Muggles. **J. ACM 2015** [Google Scholar](https://scholar.google.com/scholar?q=Delegating+computation+interactive+proofs+for+Muggles)
> 核心思路：通过将分层电路每一层的值表示为多项式求和，利用 Sumcheck 协议将输出层的断言逐层归约至输入层，实现对数级验证时间和通信量。
> 局限与区别：其证明者复杂度为 $O(C \log C)$，未达线性；且原始协议不具备零知识性。本文在其基础上实现了线性证明时间和零知识性。

[23] Cormode 等. Practical verified computation with streaming interactive proofs. **ITCS 2012** [Google Scholar](https://scholar.google.com/scholar?q=Practical+verified+computation+with+streaming+interactive+proofs)
> 核心思路：利用 GKR 多项式在布尔超立方上的稀疏性质（非零项个数为 $O(S)$），将证明者时间从 $O(S^2)$ 降至 $O(S \log S)$。
> 局限与区别：该方案仅在稀疏性保持时有效，且最终复杂度仍为 $O(S \log S)$。本文通过将单个二维求和检查拆分为两个一维求和检查，彻底消除对数因子，达到 $O(S)$。

[43] Thaler. Time-optimal interactive proofs for circuit evaluation. **CRYPTO 2013** [Google Scholar](https://scholar.google.com/scholar?q=Time+optimal+interactive+proofs+for+circuit+evaluation)
> 核心思路：为规则电路（布线模式可由常数空间描述）设计了一种 $O(C)$ 的 GKR 证明者算法，利用电路的结构化模式加速。
> 局限与区别：该方法强制依赖电路的结构性，无法推广至任意布线模式。本文的线性时间复杂度适用于任意多层电路，无需任何结构假设。

[48] Wahby 等. Doubly-efficient zkSNARKs without trusted setup. **SP 2018** [Google Scholar](https://scholar.google.com/scholar?q=Doubly+efficient+zkSNARKs+without+trusted+setup)
> 核心思路：将 GKR 协议中的所有消息密封在同态承诺中，并在承诺域上执行零知识检验，从而获得零知识性。
> 局限与区别：同态承诺将每一条域加法操作转换为群乘法、域乘法转换为群幂运算，导致验证时间退化约两个数量级。本文使用小型随机多项式直接屏蔽 Sumcheck 消息，避免了开销高昂的同态加密操作。

[16] Bünz 等. Bulletproofs: Short proofs for confidential transactions and more. **SP 2018** [Google Scholar](https://scholar.google.com/scholar?q=Bulletproofs+Short+proofs+for+confidential+transactions+and+more)
> 核心思路：基于内积论证构造零知识证明，证明时间为 $O(C)$，无需可信设置，证明大小为 $O(\log C)$。
> 局限与区别：其验证时间与电路规模 $C$ 呈线性关系，不满足“简洁”定义。本文验证时间为 $O(d \log C)$。

[13] Ben-Sasson 等. Succinct non-interactive zero knowledge for a von Neumann architecture. **USENIX Security 2014** [Google Scholar](https://scholar.google.com/scholar?q=Succinct+non+interactive+zero+knowledge+for+a+von+Neumann+architecture)
> 核心思路：基于 QAP 构造，证明大小和验证时间均为常数，证明时间为 $O(C \log C)$。
> 局限与区别：每一条陈述都需要独立的可信设置（per-statement trusted setup），且证明者复杂度超线性。本文仅需一次与输入大小相关的设置，且证明时间线性。

### 核心技术与方案

本文的整体框架将 GKR 协议与可验证多项式委托 (zkVPD) 相结合，通过引入小型随机多项式屏蔽来实现高效零知识性。系统分为两大部分：**线性时间 GKR 协议**和**高效零知识 GKR 协议**。

**线性时间 GKR 协议**的核心在于将原始 Sumcheck 中的 $2s$ 变量多项式求和拆分为两个 $s$ 变量的多项式求和。原始函数求和形式为 $\sum_{x,y \in \{0,1\}^\ell} f_1(g,x,y) f_2(x) f_3(y)$，其中 $f_1$ 是稀疏的。通过因式分解，将其化为 $\sum_{x \in \{0,1\}^\ell} f_2(x) h_g(x)$，其中 $h_g(x) = \sum_{y \in \{0,1\}^\ell} f_1(g,x,y) f_3(y)$。证明者通过预处理函数 $h_g$ 在超立方上的值（利用 $f_1$ 的稀疏性，线性时间完成，详见算法 4 和算法 5），从而在阶段一和阶段二均能调用标准的双线性 Sumcheck（算法 3）来处理 $s$ 变量多项式，$O(2^\ell)$ 时间即可完成每阶段。

**高效零知识 GKR 协议**的关键在于屏蔽多项式的“小型化”。对于 Sumcheck 协议，屏蔽多项式设为 $g(x_1,\ldots,x_\ell) = a_0 + \sum_{i=1}^\ell g_i(x_i)$，其中每个 $g_i$ 是仅在 $x_i$ 上变量度为 $d$ 的单变量随机多项式。整个 $g$ 仅包含 $O(d\ell)$ 个随机系数，却足以使所有 $O(d\ell)$ 条 Sumcheck 消息被完美屏蔽。对于 GKR 协议在 Sumcheck 后额外泄露的两个评估点 $\tilde{V}_i(u)$ 和 $\tilde{V}_i(v)$，本文使用特殊低度扩展公式（等式 8, 7）进行屏蔽，其中随机多项式 $R_i$ 仅含两个变量且变量度为 2，是常数大小的。该构造依赖 q-SBDH 假设和扩展 PKE 假设。方案保证完备性、可靠性（因随机线性组合）和零知识性（因以上两项掩蔽足以模拟验证者视角）。整体通信量为 $O(d \log C)$，证明者计算量为 $O(|C|)$ 次域运算加 $O(n)$ 次配对群乘运算，验证者计算量为 $O(|x| + d \log C)$ 次域运算；当电路为对数空间均匀时验证时间对数于电路规模，构成简洁论证。

### 核心公式与流程

**[GKR 核心求和公式]**
$$
\begin{array}{l} \tilde{V}_i(g) = \sum_{x, y \in \{0,1\}^{s_{i+1}}} \big(\tilde{add}_{i+1}(g, x, y) (\tilde{V}_{i+1}(x) + \tilde{V}_{i+1}(y)) \\ + \tilde{mult}_{i+1}(g, x, y) (\tilde{V}_{i+1}(x) \tilde{V}_{i+1}(y))\big) \end{array}
$$
> 作用：将电路第 $i$ 层的输出 $\tilde{V}_i$ 在随机点 $g$ 处的值表示为下层门值 $\tilde{V}_{i+1}$ 的多项式和。这是 GKR 协议的核心等式，也是 Sumcheck 协议的起点。

**[两个和的分解]**
$$
\sum_{x, y \in \{0,1\}^\ell} f_1(g, x, y) f_2(x) f_3(y) = \sum_{x \in \{0,1\}^\ell} f_2(x) h_g(x)
$$
> 作用：将原始的二变量和分解为一变量和，使得证明者能够分别处理 $x$ 和 $y$，从而将 2 维 Sumcheck 降为 2 个 1 维 Sumcheck，实现 $O(2^\ell)$ 而非 $O(2^{2\ell})$ 的复杂度。

**[零知识 Sumcheck 的屏蔽多项式]**
$$
g(x_1, \ldots, x_\ell) = a_0 + \sum_{i=1}^\ell g_i(x_i)
$$
> 作用：作为原始多项式 $f$ 的随机掩码。$g$ 仅含 $O(d\ell)$ 个随机系数，恰好覆盖 Sumcheck 中所有 $O(d\ell)$ 条消息，实现零知识性同时避免 $O(2^\ell)$ 大小的屏蔽多项式。

**[低度扩展屏蔽]**
$$
\dot{V}_i(z) \stackrel{\text{def}}{=} \tilde{V}_i(z) + Z_i(z) \sum_{w \in \{0,1\}} R_i(z_1, w)
$$
> 作用：在 $\tilde{V}_i$ 上加上一个在布尔超立方上为零但在点外随机取值的项，从而屏蔽 Sumcheck 结束时泄露的两个求值点 $\tilde{V}_i(u)$ 和 $\tilde{V}_i(v)$。$R_i$ 为两变量、变量度 2 的随机多项式，大小恒定。

**[Construction 2 第5步关键公式]**
$$
\begin{array}{l} \alpha^{(i)} \dot{V}_i(u^{(i)}) + \beta^{(i)} \dot{V}_i(v^{(i)}) = \\ \sum_{\substack{x,y\in\{0,1\}^{s_{i+1}}\\ w\in\{0,1\}}} \big(I(\mathbf{0},w)\cdot Mult_{i+1}(x,y)(\dot{V}_{i+1}(x)\dot{V}_{i+1}(y)) \\ + Add_{i+1}(x, y) (\dot{V}_{i+1}(x) + \dot{V}_{i+1}(y)) \\ + I ((x, y), \mathbf{0}) (\alpha^{(i)} Z_i(u^{(i)}) R_i(u_1^{(i)}, w) + \beta^{(i)} Z_i(v^{(i)}) R_i(v_1^{(i)}, w))\big) \end{array}
$$
> 作用：层间归约核心公式，将两个 $\dot{V}_i$ 的随机线性组合转化为对下层多项式 $\dot{V}_{i+1}$ 的带掩码的 Sumcheck，实现零知识层间递推。

### 实验结果

实验在 Amazon EC2 c5.9xlarge 实例（70 GB RAM、Intel Xeon Platinum 8124M 3 GHz 单核）上进行，每个实验取 10 次平均值。对比基线包括 libSNARK [13]、Ligero [6]、Bulletproofs [16]、Hyrax [48]、libSTARK [8] 和 Aurora [11]。在 Merkle 树根证明基准（256 叶子，使用 SHA-256）上，Libra 的证明者时间仅需 **201-202 秒**，比 libSNARK (360 s) 快约 1.8 倍，比 Ligero (400 s) 快约 2 倍，比 Aurora (3199 s) 快约 16 倍，比 Bulletproofs (13000 s) 快约 65 倍。验证时间 **0.71 秒**，慢于 libSNARK (0.002 s) 和 libSTARK (0.044 s)，但远快于 Bulletproofs (900 s)、Aurora (15.2 s) 和 Hyrax (9.9 s)。证明大小 **51 KB**，小于 Aurora (174 KB)、Ligero (1500 KB) 和 libSTARK (395 KB)，但大于 libSNARK (0.13 KB) 和 Bulletproofs (5.5 KB)。Libra 仅需一次 210 秒的输入相关设置，而 libSNARK 每个程序需一次 1027 秒的设置。在矩阵乘法和图像缩放基准上，Libra 的证明者同样为最快，且验证时间和证明大小随电路规模增长缓慢，体现了亚线性增长的优势。

### 局限性与开放问题
Libra 的验证时间虽为对数，但在实践中仍比 libSNARK 慢数个数量级，主要源于在配对上的运算开销。尽管被称为“一次”可信设置，其公共参数仍需随输入大小 $n$ 线性生成，对极大输入场景（如 2^30 以上）可能成为瓶颈。对于非对数空间均匀的电路（即电路布线无法用对数空间图灵机描述），验证者必须 $\Omega(C)$ 时间读取电路，从而失去简洁性。未来的工作可探索如何将验证者成本进一步降低至绝对常数（如 QAP 方案），同时保持线性的证明者，或消除配对假设以提升性能。

### 强关联论文

[30] Goldwasser S., Kalai Y.T., Rothblum G.N. Delegating computation: interactive proofs for Muggles. **J. ACM 2015** [Google Scholar](https://scholar.google.com/scholar?q=Delegating+computation+interactive+proofs+for+Muggles)

[23] Cormode G., Mitzenmacher M., Thaler J. Practical verified computation with streaming interactive proofs. **ITCS 2012** [Google Scholar](https://scholar.google.com/scholar?q=Practical+verified+computation+with+streaming+interactive+proofs)

[43] Thaler J. Time-optimal interactive proofs for circuit evaluation. **CRYPTO 2013** [Google Scholar](https://scholar.google.com/scholar?q=Time+optimal+interactive+proofs+for+circuit+evaluation)

[48] Wahby R.S., Tzialla I., Shelat A., Thaler J., Walfish M. Doubly-efficient zkSNARKs without trusted setup. **SP 2018** [Google Scholar](https://scholar.google.com/scholar?q=Doubly+efficient+zkSNARKs+without+trusted+setup)

[16] Bünz B., Bootle J., Boneh D., Poelstra A., Wuille P., Maxwell G. Bulletproofs: Short proofs for confidential transactions and more. **SP 2018** [Google Scholar](https://scholar.google.com/scholar?q=Bulletproofs+Short+proofs+for+confidential+transactions+and+more)

[13] Ben-Sasson E., Chiesa A., Tromer E., Virza M. Succinct non-interactive zero knowledge for a von Neumann architecture. **USENIX Security 2014** [Google Scholar](https://scholar.google.com/scholar?q=Succinct+non+interactive+zero+knowledge+for+a+von+Neumann+architecture)

[22] Chiesa A., Forbes M.A., Spooner N. A zero knowledge sumcheck and its applications. **arXiv 2017** [Google Scholar](https://scholar.google.com/scholar?q=A+zero+knowledge+sumcheck+and+its+applications)

[50] Zhang Y., Genkin D., Katz J., Papadopoulos D., Papamanthou C. vSQL: Verifying arbitrary SQL queries over dynamic outsourced databases. **SP 2017** [Google Scholar](https://scholar.google.com/scholar?q=vSQL+Verifying+arbitrary+SQL+queries+over+dynamic+outsourced+databases)

[51] Zhang Y., Genkin D., Katz J., Papadopoulos D., Papamanthou C. vRAM: Faster verifiable RAM with program-independent preprocessing. **SP 2018** [Google Scholar](https://scholar.google.com/scholar?q=vRAM+Faster+verifiable+RAM+with+program+independent+preprocessing)

[46] Wahby R.S., et al. Full accounting for verifiable outsourcing. **CCS 2017** [Google Scholar](https://scholar.google.com/scholar?q=Full+accounting+for+verifiable+outsourcing)


## 关键词

+ Libra最优证明者时间简洁零知识证明
+ GKR协议线性时间算法掩蔽多项式
+ 对数验证时间均匀电路SNARK构造
+ 一次性可信设置电路输入依赖
+ SHA2 Merkle树实用零知识证明性能