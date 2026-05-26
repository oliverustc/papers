---
title: "Succinct non-interactive arguments via linear interactive proofs"
标题简称:
论文类型: journal
期刊简称: Journal of Cryptology
发表年份: 2022
created: 2025-04-29 10:28:03
modified: 2025-04-29 10:30:11
---

## Succinct non-interactive arguments via linear interactive proofs

## 发表信息

+ [原文链接](https://link.springer.com/article/10.1007/s00145-022-09424-4)

## 作者

+ Nir Bitansky 
+ [Alessandro Chiesa](Alessandro%20Chiesa.md)
+ [Yuval Ishai](Yuval%20Ishai.md)
+ Rafail Ostrovsky 
+ Omer Paneth 

## 笔记

### 背景与动机
简洁非交互式参数（SNARGs）使得验证 NP 语句的复杂度低于经典的 NP 验证过程。该领域的研究长期聚焦于最小化证明长度，而近年来的工作（受计算委托问题的驱动）也开始关注如何降低验证时间。一个常见的松弛模型是预处理 SNARG：允许验证者在离线阶段进行昂贵的预处理，该过程独立于后续需要证明的语句。近期的预处理 SNARG 构造已实现了公开可验证性、证明仅包含常数个加密（或编码）域元素，以及验证电路的规模与 NP 语句的输入长度呈线性关系等良好特性。尤其值得注意的是，这些构造似乎已“逃离”了基于概率可检验证明（PCP）的传统构造范式的“霸权”。然而，这些现有工作（如 Groth 2010 [64]；Lipmaa 2012 [78]；Gennaro 等 2013 [56]）大多采用针对特定代数满足问题的特制密码学工具，缺乏一个清晰、通用的方法论来分离“信息论层面的概率证明系统”与“密码学编译器”这两个模块。本文旨在填补这一空白：提出一种通用方法论，从适当类型的概率证明系统出发构造预处理 SNARK，并通过不同实例化获得概念上更简单或具有新效率特性的构建。

### 相关工作

[56] Gennaro, R., Gentry, C., Parno, B., Raykova, M. Quadratic Span Programs and Succinct NIZKs without PCPs. **EUROCRYPT 2013** [Google Scholar](https://scholar.google.com/scholar?q=Quadratic+Span+Programs+and+Succinct+NIZKs+without+PCPs)
> 核心思路：引入二次跨度程序（QSP）作为中间表示，并直接编译为 SNARK，无需显式使用 PCP。
> 局限与区别：虽然效率很高，但其方法论是特定于 QSP 这一代数满足问题的，不提供从一般概率证明系统构建的通用框架。本文的工作通过引入线性交互证明（LIP）提供了统一的方法论，并能将 QSP 构造作为一个特例纳入其中。

[64] Groth, J. Short Pairing-Based Non-Interactive Zero-Knowledge Arguments. **ASIACRYPT 2010** [Google Scholar](https://scholar.google.com/scholar?q=Short+Pairing-Based+Non-Interactive+Zero-Knowledge+Arguments)
> 核心思路：利用双线性群中的知识指数假设，构造了首个实用的预处理 SNARK，证明长度仅为常数个群元素。
> 局限与区别：其构造依赖于针对特定二次方程系统的人工密码学工具，缺乏通用性。本文提供的方法论可以看作是对其构造的一种更清晰的重构和解释。

[78] Lipmaa, H. Progression-Free Sets and Sublinear Pairing-Based Non-Interactive Zero-Knowledge Arguments. **TCC 2012** [Google Scholar](https://scholar.google.com/scholar?q=Progression-Free+Sets+and+Sublinear+Pairing-Based+Non-Interactive+Zero-Knowledge+Arguments)
> 核心思路：继承了 Groth 的框架，通过使用无进展集等组合工具来优化参考字符串的大小。
> 局限与区别：同样缺乏通用方法论，其优化是特定于该框架的。本文的 LIP 方法可以统一看待此类构造。

[72] Ishai, Y., Kushilevitz, E., Ostrovsky, R. Efficient Arguments without Short PCPs. **CCC 2007** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+Arguments+without+Short+PCPs)
> 核心思路：提出了使用“结构化”PCP（强线性 PCP）和同态加密构造论证系统的思路，实现了简洁的证明者。
> 局限与区别：其构造是交互式的，且需要使用强线性 PCP（对所有证明者有效，包括恶意的），因此需要进行线性性测试。本文专注于非交互式设置，并使用弱线性 PCP（仅对诚实证明者保证，安全性依赖线性目标可塑性假设），避免了线性性测试，从而保留了 PCP 的代数性质。

[68] Gentry, C., Wichs, D. Separating Succinct Non-Interactive Arguments from All Falsifiable Assumptions. **STOC 2011** [Google Scholar](https://scholar.google.com/scholar?q=Separating+Succinct+Non-Interactive+Arguments+from+All+Falsifiable+Assumptions)
> 核心思路：证明了对于足够难的 NP 语言，SNARG 无法通过黑盒归约到任何可伪造假设来证明安全性。
> 局限与区别：该否定结果论证了使用非标准假设（如知识假设、线性目标可塑性）在构造 SNARG 时的必要性。这为本文采用基于知识指数假设等的线性加密/编码方案提供了理论依据。

### 核心技术与方案
本文提出了一个分层构造方法论，将预处理 SNARK 的构造分解为两个独立部分：(1) 信息论层面的线性交互证明（LIP）；(2) 密码学编译器，将 LIP 转换为 SNARK。

1.  **信息论层面：线性交互证明（LIP）**。LIP 修改了标准交互证明模型，限制证明者（无论是诚实的还是恶意的）只能对其接收到的验证者消息应用线性（或仿射）函数。本文主要关注两类输入无关的两轮 LIP。第一类 LIP 通过通用转换从线性 PCP（LPCP）构造。LPCP 是比传统 PCP 更具结构的变体，其证明预言机是线性函数。给定一个 \(k\)-query LPCP，转换后的 LIP 证明者消息变为 \(k+1\) 个域元素。这通过在 LPCP 的 \(k\) 个查询外，再发送一个随机线性组合查询来实现，验证者通过检查答案是否满足该线性关系来保证一致性。基于 Hadamard PCP（ALMSS 变体）的 LPCP 产生消息复杂度为 \(O(s^2)\) 的 LIP，而基于 QSP 的 LPCP 产生 \(O(s)\) 的 LIP。第二类 LIP 直接从传统 PCP 构造，巧妙地利用了子集和问题的易解性，将 \(k\) 个 PCP 答案位打包成一个域元素，从而让证明者仅发送一个域元素，但代价是所需域的大小指数级增长（如 \(2^{\lambda \cdot \text{polylog}(s)}\)）。

2.  **密码学层面：从 LIP 到预处理 SNARK**。转换的核心思想是使用“线性唯一”加密/编码方案来强制计算有界证明者行为如同 LIP 模型中的线性函数。对于**指定验证者**SNARK，使用线性唯一加密方案。验证者使用该方案加密其 LIP 查询向量，证明者利用加密的同态性质计算其对加密查询的（线性）答案，并将其返回给验证者。解密后，验证者运行 LIP 决策算法。线性唯一性质保证，任何能够生成有效密文的恶意证明者，必须“知道”一个对应的仿射函数，从而将安全性规约到 LIP 本身。对于**公开验证**SNARK，则需要使用线性唯一单向编码，例如基于双线性群和知识指数假设的编码。此类编码支持公开地进行二次决策多项式的零测试（通过配对），使得验证者无需解密即可验证证明。因此，仅当 LIP 的决策算法度 \(d_D \leq 2\) 时，才能使用此类编码，得到公开验证的 SNARK。

3.  **渐近复杂度与安全性**。以电路规模为 \(s\) 的布尔电路为例，基于 Hadamard LPCP 的 LIP 编译后，证明包含 4 个密文/编码，验证时间与输入长度 \(n\) 成线性关系，参考字符串大小为 \(O(s^2)\)。基于 QSP 的 LIP 则可将参考字符串大小降至 \(O(s)\)。两种方案在指定验证者模式下都只需依赖非标准假设（如 Paillier 或 Elgamal 加密的线性目标可塑性或线性唯一性质），在公开验证模式下则依赖双线性群中的知识指数和功率离散对数假设。单密文 SNARK 则来自从传统 PCP 转换的 LIP，证明仅含 1 个 Paillier 密文（非自适应安全），通信复杂度有显著降低，但通常需要更大的域或假定更强的安全性。

### 核心公式与流程

**[从 LPCP 到 LIP 的构造 (Construction 3.1)]**
设 \(V_{LPCP}\) 生成 k 个查询 \(\boldsymbol{q}_1, \ldots, \boldsymbol{q}_k\)，并随机选取 \(\alpha_1, \ldots, \alpha_k\)。LIP 验证者发送：
$$
\boldsymbol{q}_1, \ldots, \boldsymbol{q}_k, \quad \boldsymbol{q}_{k+1} = \sum_{i=1}^{k} \alpha_i \boldsymbol{q}_i
$$
诚实证明者使用线性函数 \(\pi\) 计算答案 \(a_i = \langle \pi, \boldsymbol{q}_i \rangle\)，返回 \(a_1, \ldots, a_{k+1}\)。LIP 验证者首先检查一致性：
$$
a_{k+1} = \sum_{i=1}^{k} \alpha_i a_i
$$
若通过，则使用 \(a_1, \ldots, a_k\) 运行 LPCP 的决策算法。
> 作用：将多查询 LPCP 转换为两轮 LIP，并通过随机线性组合防止证明者对每个查询使用不同线性函数，保证了安全性。证明者消息长度从 k 增长为 k+1。

**[从 LIP 到指定验证者 SNARK 的构造 (Construction 6.1)]**
系统建立 \(G(1^\lambda, 1^\ell)\)：运行 LIP 查询算法 \(Q_{LIP}\) 生成查询 \(\boldsymbol{q} \in \mathbb{F}^m\) 和状态 \(\boldsymbol{u}\)。生成密钥对 \((\mathsf{sk}, \mathsf{pk})\)，输出 \(\sigma = (\mathsf{pk}, \mathsf{Enc}_{\mathsf{pk}}(q_1), \ldots, \mathsf{Enc}_{\mathsf{pk}}(q_m))\) 和 \(\tau = (\mathsf{sk}, \boldsymbol{u})\)。
证明生成 \(P(\sigma, x, w)\)：运行 \(P_{LIP}\) 得到仿射函数 \(\Pi: \mathbb{F}^m \to \mathbb{F}^k\)，使用加密的同态计算 \(\pi = \mathsf{Add}(\mathsf{pk}, \mathsf{Enc}_{\mathsf{pk}}(q_1), \ldots, \mathsf{Enc}_{\mathsf{pk}}(q_m), \Pi)\)，输出 \(\pi\)。
验证 \(V(\tau, x, \pi)\)：解密 \(\pi\) 得到答案 \(\boldsymbol{a}\)，计算 \(D_{LIP}(\mathbb{F}_\lambda, 1^\ell, x, \boldsymbol{u}, \boldsymbol{a})\)。
> 作用：使用线性唯一加密将 LIP 的线性限制强制到计算有界的恶意证明者身上。安全性规约依赖于加密的线性唯一性质（提取仿射函数）和语义安全性（隐藏查询，保证 LIP 知识的可提取性）。

**[从 LIP 到公开验证 SNARK 的构造 (Construction 6.6)]**
与构造 6.1 的区别在于，使用线性唯一单向编码而非加密。\(\sigma\) 包含查询的编码（线性模式，\(\mathsf{Enc}\)），\(\tau\) 包含状态的编码（标准模式，\(\mathsf{SEnc}\)）。证明生成过程类似。验证时，不进行解密，而是直接使用配对（Test 算法）来检验 LIP 决策多项式（二次的）在编码上的零测试结果：
$$
\mathsf{Test}(\mathsf{pk}, t_x, c'_1, \ldots, c'_k, \tilde{c}_1, \ldots, \tilde{c}_{m'})
$$
> 作用：公开验证成为可能，因为验证者无需私钥即可测试解密后的值是否满足决策方程。这要求 LIP 的决策多项式度 \(d_D \le 2\)，以便能通过双线性配对实现公开测试。

### 实验结果
本文是理论性研究，未提供实验评估。然而，论文通过渐近复杂度分析展示了其构造的优势。例如，表 2 总结了多种预处理 SNARK 构造的渐近性能。基于 QSP 的 LIP 编译后，参考字符串大小为 \(O(s)\)，证明包含 4（非自适应）或 8（自适应）个密文/编码，验证时间为 \(n \cdot \text{poly}(\lambda)\)，其中 \(s\) 是电路规模，\(n\) 是输入长度。相比之下，基于传统 PCP 的 LIP 编译后可实现仅 1 个密文的证明（非自适应），这代表了在通信复杂度上的显著改进。论文中详细比较了这些方案的假设等级（Paillier TM vs. Paillier LOEC vs. Bilinear LOED）和安全性（自适应 vs. 非自适应）。这些理论分析表明，通过选择合适的 LIP 底层构造和密码学编译器，可以实现不同效率指标的权衡，例如在参考字符串大小、证明长度、验证者计算量和安全性假设强度之间进行取舍。

### 局限性与开放问题
虽然本文提出的方法论是统一的，但最终的具体构造仍然依赖于非标准假设，例如线性目标可塑性或知识指数假设。这些假设虽然当前被广泛使用，但其安全性基础不如可伪造假设稳固。公开验证的 SNARK 构造目前受限于双线性群，只能处理二次决策多项式，限制了可用的 LIP 类型。此外，具有强知识性质的 LIP（如代数 LIP）虽然可以构造多定理安全的指定验证者 SNARK，但这需要更强形式的线性唯一加密（交互式提取假设），其可实例化和安全性基础有待进一步研究。最后，寻找抗亚指数攻击的线性唯一加密候选方案（如基于某些椭圆曲线群的 Elgamal 变体）并证明其安全性，是一个重要的开放问题。

### 强关联论文

[4] Arora, S., Lund, C., Motwani, R., Sudan, M., Szegedy, M. Proof Verification and the Hardness of Approximation Problems. **J. ACM 1998** [Google Scholar](https://scholar.google.com/scholar?q=Proof+Verification+and+the+Hardness+of+Approximation+Problems)

[28] Ben-Sasson, E., Chiesa, A., Genkin, D., Tromer, E. On the Concrete Efficiency of Probabilistically-Checkable Proofs. **STOC 2013** [Google Scholar](https://scholar.google.com/scholar?q=On+the+Concrete+Efficiency+of+Probabilistically-Checkable+Proofs)

[56] Gennaro, R., Gentry, C., Parno, B., Raykova, M. Quadratic Span Programs and Succinct NIZKs without PCPs. **EUROCRYPT 2013** [Google Scholar](https://scholar.google.com/scholar?q=Quadratic+Span+Programs+and+Succinct+NIZKs+without+PCPs)

[64] Groth, J. Short Pairing-Based Non-Interactive Zero-Knowledge Arguments. **ASIACRYPT 2010** [Google Scholar](https://scholar.google.com/scholar?q=Short+Pairing-Based+Non-Interactive+Zero-Knowledge+Arguments)

[68] Gentry, C., Wichs, D. Separating Succinct Non-Interactive Arguments from All Falsifiable Assumptions. **STOC 2011** [Google Scholar](https://scholar.google.com/scholar?q=Separating+Succinct+Non-Interactive+Arguments+from+All+Falsifiable+Assumptions)

[69] Håstad, J., Khot, S. Query Efficient PCPs with Perfect Completeness. **Theory of Computing 2005** [Google Scholar](https://scholar.google.com/scholar?q=Query+Efficient+PCPs+with+Perfect+Completeness)

[72] Ishai, Y., Kushilevitz, E., Ostrovsky, R. Efficient Arguments without Short PCPs. **CCC 2007** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+Arguments+without+Short+PCPs)

[78] Lipmaa, H. Progression-Free Sets and Sublinear Pairing-Based Non-Interactive Zero-Knowledge Arguments. **TCC 2012** [Google Scholar](https://scholar.google.com/scholar?q=Progression-Free+Sets+and+Sublinear+Pairing-Based+Non-Interactive+Zero-Knowledge+Arguments)


## 关键词

+ 简洁非交互式论证SNARG
+ 线性交互式证明LIP
+ 预处理SNARG构造方法
+ 线性PCP代数有界证明者
+ 线性目标可延展性安全假设
+ 知识SNARG递归组合