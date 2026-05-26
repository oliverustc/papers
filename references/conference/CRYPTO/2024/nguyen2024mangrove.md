---
title: "Mangrove: A Scalable Framework for Folding-Based SNARKs"
标题简称: Mangrove
论文类型: conference
会议简称: CRYPTO
发表年份: 2024
modified: 2025-04-21 10:45:31
created: 2025-04-07 16:49:32
---

## Mangrove: A Scalable Framework for Folding-Based SNARKs

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-68403-6_10)

## 作者

+ Wilson Nguyen
+ Trisha Datta
+ [Binyi Chen](Binyi%20Chen.md)
+ [[Nirvan Tyagi]]
+ [Dan Boneh](Dan%20Boneh.md)

## 笔记

### 背景与动机
随着 SNARK 应用场景的扩展，证明算法的运行时间和内存消耗成为核心瓶颈，特别是当需要证明大型算术电路时。现有大多数 SNARK 属于单体式，要求证明者保存完整的计算轨迹并执行全局计算，例如对多项式进行承诺和打开，这通常涉及快速傅里叶变换或多标量乘法等全局运算，导致内存占用与语句规模线性相关。虽然通过分块全局计算或设计流式协议可以降低证明者空间复杂度，但这些方法通常会引入时间开销。一种替代策略是通过增量可验证计算 (IVC) 或证明聚合等分块式方法，将大型语句分解为小块分别证明再合并。对于 IVC，过去通常将通用电路或虚拟机作为目标计算，但这导致了三个层面的效率损失：将 NP 语句编码为程序的低效、每一步运行通用电路的开销、以及验证程序状态的成本。折叠方案的出现彻底改变了这一状况，它允许证明者将两个关系实例合并为一个，且折叠验证成本极低。然而，现有折叠方案在将其应用于通用 NP 语句时，仍面临递归开销大、承诺打开成本高等问题。本文旨在填补这一空白，通过一种新的均匀编译器和对折叠 IVC 的两项关键优化，构建一个在证明者时间、内存、输入遍历次数和参考字符串大小方面均达到最优或接近最优的 SNARK 系统。

### 相关工作

[5] Ben-Sasson 等. Scalable, transparent, and post-quantum secure computational integrity. **ePrint 2018** [Google Scholar](https://scholar.google.com/scholar?q=Scalable+transparent+and+post-quantum+secure+computational+integrity)
> 核心思路：构建了基于 STARK 的透明、可扩展证明系统，支持后量子安全。
> 局限与区别：作为单体式 SNARK，其证明者需要保存完整轨迹，内存与语句规模线性正比，而本文实现了常数内存。

[11] Bitansky 等. Recursive composition and bootstrapping for SNARKs and proof-carrying data. **STOC 2013** [Google Scholar](https://scholar.google.com/scholar?q=Recursive+composition+and+bootstrapping+for+SNARKs+and+proof-carrying+data)
> 核心思路：提出了通过递归证明组合实现 IVC 的通用框架，并引入了 Proof-Carrying Data (PCD) 概念。
> 局限与区别：递归证明验证开销大，而本文采用折叠方案，折叠验证比证明验证轻量得多。

[13] Block 等. Time- and space-efficient arguments from groups of unknown order. **CRYPTO 2021** [Google Scholar](https://scholar.google.com/scholar?q=Time+and+space+efficient+arguments+from+groups+of+unknown+order)
> 核心思路：利用未知阶群构建了流式 SNARK，实现内存与输入规模的对数关系。
> 局限与区别：该方案需要 O(log n) 次输入遍历，且内存开销为 O(polylog n)，而本文仅需常数内存和两次遍历。

[16] Bootle 等. Gemini: elastic SNARKs for diverse environments. **EUROCRYPT 2022** [Google Scholar](https://scholar.google.com/scholar?q=Gemini+elastic+SNARKs+for+diverse+environments)
> 核心思路：设计了 Gemini 证明系统，通过弹性方式支持在不同环境下运行，具有流式特性。
> 局限与区别：Gemini 的证明者需要 O(log n) 次数据遍历，内存为 O(log n)，本文在常数次遍历和常数内存上优于它。

[21] Bünz 等. Proof-carrying data without succinct arguments. **CRYPTO 2021** [Google Scholar](https://scholar.google.com/scholar?q=Proof+carrying+data+without+succinct+arguments)
> 核心思路：首次提出利用折叠方案（或积累方案）构建 PCD，无需简洁论证即可实现高效的递归组合。
> 局限与区别：该工作未针对 NP 语句的均匀编译进行优化，且其 PCD 关系中包含了核心计算与承诺打开的混合，本文通过解耦和 commit-and-fold 优化大幅降低了递归开销。

[33] Gabizon 等. PLONK: Permutations over Lagrange-bases for oecumenical noninteractive arguments of knowledge. **ePrint 2019** [Google Scholar](https://scholar.google.com/scholar?q=PLONK+Permutations+over+Lagrange+bases+for+oecumenical+noninteractive+arguments+of+knowledge)
> 核心思路：提出了 Plonk 算术化，通过全局副本约束和门电路多项式对计算轨迹进行编码。
> 局限与区别：Plonk 直接应用会需要保存整个轨迹，本文将其作为编译目标，通过均匀编译器将全局副本约束转化为可传播的局部累积量。

[39] Kothapalli 等. Nova: recursive zero-knowledge arguments from folding schemes. **CRYPTO 2022** [Google Scholar](https://scholar.google.com/scholar?q=Nova+recursive+zero+knowledge+arguments+from+folding+schemes)
> 核心思路：提出了 Nova 折叠方案，将 R1CS 实例的折叠变为松弛实例，实现高效的 IVC。
> 局限与区别：Nova 直接应用于 NP 语句时需要通用电路，导致常数因子过大且仅支持常数长度计算，本文通过 uniform compiler 和 commit-and-fold 避免了通用电路，支持多项式长度计算。

[48] Setty. Spartan: efficient and general-purpose zkSNARKs without trusted setup. **CRYPTO 2020** [Google Scholar](https://scholar.google.com/scholar?q=Spartan+efficient+and+general+purpose+zkSNARKs+without+trusted+setup)
> 核心思路：Spartan 是一种单体式 SNPARK，无需可信设置，拥有线性证明者时间。
> 局限与区别：Spartan 的证明者内存需求与语句规模线性相关，而本文在保持线性证明时间的同时实现常数内存，且在具体效率上与 Spartan 相当。

[20] Bünz 等. ProtoStar: generic efficient accumulation/folding for special sound protocols. **ePrint 2023** [Google Scholar](https://scholar.google.com/scholar?q=ProtoStar+generic+efficient+accumulation+folding+for+special+sound+protocols)
> 核心思路：ProtoStar 提出了一种通用的高效的积累/折叠方案，适用于特殊可靠协议，支持任意度数的多项式映射。
> 局限与区别：本文的折叠方案可看作是 ProtoStar 思想的推广，但引入了针对 k 个实例的直接折叠树构造和对线性映射的通用支持，避免了常数 k 的安全限制，同时通过 commit-and-fold 支持对承诺值的直接操作。

### 核心技术与方案

本文的整体框架分为两个层次：首先通过一个随机化均匀编译器将任意 NP 语句转化为一系列相同的简单步骤（chunk），然后利用经过两方面优化的折叠 PCD 来证明这些均匀步骤的正确性。

**均匀编译器**。本文以 Plonk 算术化为目标。Plonk 算术化包含局部门约束和全局副本约束。局部约束可自然地按门分块，但全局副本约束涉及跨块的连线。编译器的关键在于将全局副本约束转化为一个可局部计算并全局合并的累积量：$$ \prod_{i=1}^{3n} \frac{H(v^{(i)}, i)}{H(v^{(i)}, \sigma^{(i)})} = 1 $$。其中 H 是一个随机化的哈希函数（使用验证者挑战 α, β）。每个 chunk（块）计算该乘积的一部分，即归属于该 chunk 索引范围内的比值乘积。由于 H 是线性的，该乘积可独立计算，最终在 PCD 树的根节点处合并为乘积 1，从而完成全局副本约束。由于 H 使用 α, β 挑战，证明者需要先对证据向量 v 进行承诺，然后接收挑战，再逐块计算，因此需要两次数据遍历。

**基于 PCD 的 SNARK 构造**。经过编译后，每个 chunk j 中包含了门向量 s_j、副本向量 σ_j、和证据值向量 v_j。PCD 树的叶子节点负责证明单个 chunk 的计算正确性，包括门约束和局部乘积 p_j 的计算。内部节点负责合并子树的承诺和累积量：它通过哈希函数合并子树的 Plonk 参数承诺 hplk 和证据承诺 hz，并将子节点的局部累积量相乘得到父节点的累积量 p。根节点需要满足 `(p, hplk, hz) = (1, hplk_root, hz_root)`。整个 PCD 树的递归关系 R_pcd 校验了 PCD 谓词 φ，并递归验证了折叠证明。

**优化 I：解耦 PCD 计算树与控制树**。在标准的 PCD 构造中，每个叶子节点都需要执行完整的 R_pcd 关系，该关系包含了核心的 chunk 计算和递归逻辑。导致即使叶子节点只有简单的 chunk 计算，也要承担递归逻辑的开销（例如承诺打开）。本文提出将叶子节点专用的关系 R_leaf 与递归控制关系 R_pcd 分离。具体地，新的 PCD 谓词 φ_decouple 不直接执行 chunk 计算，而是验证叶子关系 R_leaf 的折叠证明。叶子节点只运行 R_leaf 的折叠，第一层内部节点作为验证者检查这些折叠证明。这样，递归逻辑的开销只出现在内部节点中，而叶子节点完全专注于 chunk 计算。由于叶子节点在总节点数中占绝大多数（对于高扇出树），这一优化显著降低了总证明开销。

**优化 II：Commit-and-Fold 技术**。为了进一步减小叶子关系的规模，本文提出了一个广义的折叠关系，支持对承诺值直接进行多项式关系测试。现有折叠方案要求关系实例包含对证据的承诺，并在关系内打开承诺进行检查，这带来了昂贵的承诺打开约束（例如椭圆曲线标量乘法）。本文的方法放松了关系定义：关系 R 由线性映射 L_x 将证据 x 映射到承诺值 $\bar{x}$，但关系本身只检查一个多项式映射 f(x,w)=0，而不检查承诺是否正确——绑定性质被外部层次（PCD 元组检查）保证。为了实现可折叠性，构造一种宽松的关系 R_poly，引入松弛变量 μ 和 e，使得检查 $$ \hat{f}(x,w,\mu) = e $$，其中 $\hat{f}$ 是 f 的齐次化映射。折叠算法通过随机线性组合将 k 个实例折叠为 1 个。在本文的 SNARK 构造中，叶子关系 R_leaf 被实例化为多项式映射 f，其输入包括值向量 v_j、门向量 s_j、副本 σ_j 和累积量 p_j，输出零当且仅当门约束成立且 p_j 按 perm 公式计算正确。承诺 L_x 仅对证据向量做 Pedersen 承诺，而映射 f 中不包含承诺打开。这一技术移除了 R_leaf 中 100-200 倍的承诺打开约束，大幅降低了证明成本。

**性能与安全性**。本文的 SNARK 安全性依赖于 Pedersen 承诺的绑定性质、哈希函数的抗碰撞性、折叠方案（构造基于 Fiat-Shamir 变换的对数轮特殊可靠协议）的可靠性以及基础 PCD 方案的可靠性。系统实现了以下渐进复杂度：证明者时间复杂度 O(n)；证明者内存 O(k(m+k)log_k(n/m))，通过设定参数 m=O(1), k=O(λ) 可达到常数内存 O(1)；两次数据遍历；透明且常数大小的公共参考字符串。

### 核心公式与流程

**均匀编译的乘积表达**
$$ \prod_{i=1}^{3n} \frac{H(v^{(i)}, i)}{H(v^{(i)}, \sigma^{(i)})} = 1 $$
> 作用：将 Plonk 算术化的全局副本约束转化为一个可局部 chunk 计算并全局合并的乘积形式，其中 H 是由验证者挑战决定的随机哈希函数。

**Plonk 局部门约束**
$$ G(s^{(i)}, v_\ell^{(i)}, v_r^{(i)}, v_o^{(i)}) = s^{(i)} \cdot (v_\ell^{(i)} + v_r^{(i)}) + (1 - s^{(i)}) \cdot v_\ell^{(i)} \cdot v_r^{(i)} - v_o^{(i)} = 0 $$
> 作用：定义了每个门 i 的左、右、输出连线值需要满足的二次多项式约束，s 为选择子指示加法或乘法门。

**SNARK PCD 谓词 φ_{snark}（简化版）**
$$
\begin{array}{l}
\text{If leaf:} \\
\quad \bigwedge_i G(s_j^{(i)}, v_{\ell,j}^{(i)}, v_{r,j}^{(i)}, v_{o,j}^{(i)}) = 0 \\
\quad p_j = \prod_{i=1}^{3m} \frac{H_{\alpha,\beta}(v_j^{(i)}, 3m(j-1)+i)}{H_{\alpha,\beta}(v_j^{(i)}, \sigma_j^{(i)})} \\
\quad hplk_j = MT.H(Commit(j,s_j,\sigma_j)),\quad hv_j = MT.H(Commit(v_j)) \\
\text{Else (internal node):} \\
\quad p = p_0 \cdot p_1 \\
\quad hplk = MT.H(hplk_0, hplk_1),\quad hv = MT.H(hv_0, hv_1)
\end{array}
$$
> 作用：描述了 PCD 树中叶子节点和内部节点需要满足的约束，叶子节点保证 chunk 计算的正确性和承诺的正确性，内部节点保证子树证明的合并逻辑。

**多项式打开关系 R_open**
$$
\mathcal{R}_{\text{open}}(\mathcal{L}_x, \mathcal{L}_e, f) := \{((\bar{x} \in \mathbb{X}, \bar{e} \in \mathbb{E}); x \in \mathbb{F}^m) \mid (\bar{x}, \bar{e}) = (\mathcal{L}_x(x), \mathcal{L}_e(f(x))) \}
$$
> 作用：定义了本文折叠方案的基础关系，该关系要求承诺值 $\bar{x}$ 是证据 x 通过线性映射 $\mathcal{L}_x$ 得到，并且 $\bar{e}$ 是多项式 f 在 x 处的输出通过 $\mathcal{L}_e$ 压缩的结果。

**折叠证明的基本结构（二合一轮）**
$$
\begin{array}{l}
\mathcal{P}: \forall j, \text{ compute } v_{1,j}, \ldots, v_{d-1,j} \text{ s.t. } f(Y\cdot x_j + x_{j+\ell/2}) = Y^d f(x_j) + \sum_{i=1}^{d-1} Y^i v_{i,j} + f(x_{j+\ell/2}) \\
\mathcal{V}: \text{ sample } r \gets \mathbb{F} \\
\mathcal{P}: x_j' \gets r \cdot x_j + x_{j+\ell/2} \\
\mathcal{V}: \bar{x}_j' \gets r \cdot \bar{x}_j + \bar{x}_{j+\ell/2},\quad \bar{e}_j' \gets r^d \cdot \bar{e}_j + \sum r^i \bar{v}_{i,j} + \bar{e}_{j+\ell/2}
\end{array}
$$
> 作用：给出了二合一轮折叠的核心步骤，通过随机线性组合将两个实例压缩为一个，同时通过计算交叉项保证折叠后的关系仍然成立。更高效的多实例折叠方案通过拉格朗日插值实现。

### 实验结果
本文基于 Nova 的现有实现 [44] 进行性能基准测试，硬件为搭载 Apple M2 Pro 芯片和 16GB 内存的 MacBook Pro。对于包含 2^24 个门路的 Plonk 实例，选择内存参数 m 和树扇出 k 使得证明者时间约为 2 分钟，峰值内存约 390 MB。相比之下，Spartan SNARK [48] 证明相同规模实例约需 10 分钟，Gemini [16] 需要约 19 分钟（且需对数次输入遍历）。对于更大规模（2^32 门）的实例，单体式 SNARK 如 Spartan 会因内存过大而难以运行，而 Mangrove 能在约 8 小时内完成证明，内存约 800 MB。Gemini 在该规模下估计需要超过 80 小时。增加内存参数 m 可以大幅缩短证明时间，因为这会减少叶子证明和 PCD 节点的数量。增加树扇出 k 同样能减少节点数量，但节省的成本相对较小，因为主要计算量集中在叶子层。在典型参数下，Mangrove 生成的证明大小约为 34 MB，若进一步通过 Spartan 在此证明上进行压缩（耗时不到一分钟），可将证明大小降至 12 KB。

### 局限性与开放问题
本文介绍的 commit-and-fold 技术虽然显著降低了约束数量，但仍依赖于特定代数困难假设（如离散对数问题保证 Pedersen 承诺的绑定性），因此在后量子安全方面存在隐患。将 Mangrove 的整体方案迁移到格或哈希基础的折叠方案可能是一个有价值的开放方向。此外，虽然本文声称树形 PCD 结构天然支持高度并行性，但针对具体分布式环境下的调度和通信开销尚未进行实验验证，实际部署可能存在瓶颈。最后，本文未显式提供零知识性质，虽然作者指出可以通过已有技术添加，但这会增加系统的复杂度并可能影响具体效率，需要进一步验证。

### 强关联论文

[39] Kothapalli, A., Setty, S., Tzialla, I. Nova: recursive zero-knowledge arguments from folding schemes. **CRYPTO 2022** [Google Scholar](https://scholar.google.com/scholar?q=Nova+recursive+zero+knowledge+arguments+from+folding+schemes)

[21] Bünz, B., Chiesa, A., Lin, W., Mishra, P., Spooner, N. Proof-carrying data without succinct arguments. **CRYPTO 2021** [Google Scholar](https://scholar.google.com/scholar?q=Proof+carrying+data+without+succinct+arguments)

[33] Gabizon, A., Williamson, Z.J., Ciobotaru, O. PLONK: Permutations over Lagrange-bases for oecumenical noninteractive arguments of knowledge. **ePrint 2019** [Google Scholar](https://scholar.google.com/scholar?q=PLONK+Permutations+over+Lagrange+bases+for+oecumenical+noninteractive+arguments+of+knowledge)

[48] Setty, S. Spartan: efficient and general-purpose zkSNARKs without trusted setup. **CRYPTO 2020** [Google Scholar](https://scholar.google.com/scholar?q=Spartan+efficient+and+general+purpose+zkSNARKs+without+trusted+setup)

[16] Bootle, J., Chiesa, A., Hu, Y., Orr&ugrave;, M. Gemini: elastic SNARKs for diverse environments. **EUROCRYPT 2022** [Google Scholar](https://scholar.google.com/scholar?q=Gemini+elastic+SNARKs+for+diverse+environments)

[20] Bünz, B., Chen, B. ProtoStar: generic efficient accumulation/folding for special sound protocols. **ePrint 2023** [Google Scholar](https://scholar.google.com/scholar?q=ProtoStar+generic+efficient+accumulation+folding+for+special+sound+protocols)

[13] Block, A.R., Holmgren, J., Rosen, A., Rothblum, R.D., Soni, P. Time- and space-efficient arguments from groups of unknown order. **CRYPTO 2021** [Google Scholar](https://scholar.google.com/scholar?q=Time+and+space+efficient+arguments+from+groups+of+unknown+order)

[11] Bitansky, N., Canetti, R., Chiesa, A., Tromer, E. Recursive composition and bootstrapping for SNARKs and proof-carrying data. **STOC 2013** [Google Scholar](https://scholar.google.com/scholar?q=Recursive+composition+and+bootstrapping+for+SNARKs+and+proof+carrying+data)

[5] Ben-Sasson, E., Bentov, I., Horesh, Y., Riabzev, M. Scalable, transparent, and post-quantum secure computational integrity. **ePrint 2018** [Google Scholar](https://scholar.google.com/scholar?q=Scalable+transparent+and+post-quantum+secure+computational+integrity)

[37] Kothapalli, A., Setty, S. SuperNova: proving universal machine executions without universal circuits. **ePrint 2022** [Google Scholar](https://scholar.google.com/scholar?q=SuperNova+proving+universal+machine+executions+without+universal+circuits)


## 关键词

+ 折叠基础SNARK
+ 增量验证计算
+ 透明公共参考字符串
+ 流式证明
+ 统一化编译器