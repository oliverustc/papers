---
title: "Linear-Time Accumulation Schemes"
标题简称:
论文类型: preprint
预印本简称: archive
发表年份: 2025
created: 2025-05-07 20:12:20
modified: 2025-05-07 20:13:30
---

## Linear-Time Accumulation Schemes

## 发表信息

+ [原文链接](https://eprint.iacr.org/2025/753)

## 作者

+ [Benedikt Bünz](Benedikt%20Bünz.md)
+ [Alessandro Chiesa](Alessandro%20Chiesa.md)
+ Giacomo Fenzi
+ William Wang

## 笔记

好的，作为您的密码学领域研究助手，以下是对论文《Linear-Time Accumulation Schemes》的详细结构化笔记。

### 背景与动机
证明携带数据（PCD）是一个强大的密码学原语，允许互不信任的各方在分布式环境中以可高效验证的方式执行计算。PCD 的传统实现依赖于递归证明组合，成本高昂。近期研究表明，从更轻量级的原语——累加方案（及其密切相关的折叠方案）——可以构建出高效的 PCD。一个高效的累加方案允许将一个成员验证的合取（conjunction）可靠地传播，而无需保留所有已验证的实例-见证对。现有最先进的累加方案，如基于群同态或格的方案，其累加证明者（accumulation prover）的时间复杂度均为超线性，这成为了 PCD 整体效率的瓶颈。本文旨在填补这一空白，提出在随机预言机模型下首个具有线性时间证明者和对数时间验证者的累加方案，命名为 WARP，从而首次实现累加证明者的线性时间复杂度。

### 相关工作

[BMNW25b] Bünz 等. ARC: accumulation for Reed–Solomon codes. **CRYPTO 2025** [Google Scholar](https://scholar.google.com/scholar?q=ARC+accumulation+for+Reed%E2%80%93Solomon+codes)
> 核心思路：提出了基于哈希的累加方案，其核心是面向Reed-Solomon码构建的交互式预言机归约（IOR）。
> 局限与区别：该方案使用了商式（quotients）技术，导致证明者运行时间为拟线性（quasilinear），而WARP利用多元线性扩展和任意线性码，实现了线性时间证明者。

[BMNW25a] Bünz 等. Accumulation without homomorphism. **ITCS 2025** [Google Scholar](https://scholar.google.com/scholar?q=Accumulation+without+homomorphism)
> 核心思路：同样基于哈希，为通用线性码构建了IOR，用于批处理邻近性声明。
> 局限与区别：该工作的IOR不是保距的（distance-preserving），导致只能实现有限深度的累加方案。此外，其安全证明仅覆盖唯一解码（unique-decoding）区域，证明者发送了两个预言机消息。WARP的IOR是保距的，在列表解码（list-decoding）区域也安全，且证明者只发送一个预言机消息。

[BCMS20] Bünz 等. Recursive proof composition from accumulation schemes. **TCC 2020** [Google Scholar](https://scholar.google.com/scholar?q=Recursive+proof+composition+from+accumulation+schemes)
> 核心思路：首次提出了累加方案这一概念，并利用其构建递归证明，其构造依赖基于群的同态承诺。
> 局限与区别：这些群基构造中，证明者需要对承诺进行多标量乘法（MSM），该操作即使使用Pippenger算法也是超线性的，不满足线性时间要求。

[BMMS25] Baweja 等. FICS and FACS: fast IOPPs and accumulation via code-switching. **ePrint 2025** [Google Scholar](https://scholar.google.com/scholar?q=FICS+and+FACS+fast+IOPPs+and+accumulation+via+code-switching)
> 核心思路：提出了一种并行的线性时间累加方案，同样在随机预言机模型下工作。
> 局限与区别：WARP与[BMMS25]是并发工作。主要区别在于：WARP的累加关系更具表达性；WARP的IOR证明者只发送一个预言机，而[BMMS25]发送多个；WARP支持列表解码区域，从而减少验证者的查询量；此外，WARP在不依赖高效容错解码器的情况下实现了直线提取（straightline extraction）。

### 核心技术与方案

WARP方案的整体框架遵循[BMNW25b]的配方：通过编译合适的交互式预言机归约（IOR）来得到一个累加方案。整个过程包括两个核心IOR模块。

第一个IOR模块将PESAT（多项式方程满足）关系 $\mathcal{R}_{\odot}(\mathbb{F})$ 归约到关于约束码（constrained code）的关系 $\mathcal{R}_{c}$。约束码是原始线性码 $\mathcal{C}$ 的变种，其在满足原始编码性质之外，还强制其多元线性扩展（multilinear extension）在某些点上的值等于特定值。构造的核心思路是：证明者发送一个函数 $f$，声称它是有效见证 $\mathbf{w}$ 的编码。验证者采样一个随机点 $\mathbf{\bar{\tau}}$，然后输出一个新的声明，声称 $f$ 接近一个满足“PESAT约束”和空约束的约束码字。此归约的安全性基于：若不存在有效见证，则 $f$ 与目标约束码的距离大的概率极高。

第二个IOR模块实现了从多个 $\mathcal{R}_{c}$ 实例到单一 $\mathcal{R}_{c}$ 实例的归约，即批处理。这是实现无界累加深度的关键。该模块的核心子过程称为“码字批处理（codeword batching）”和“双子约束伪批处理（twin constraint pseudo-batching）”。

码字批处理的目标是，在给定多个函数 $f_i$ 和关于其线性组合的一个声明时，将关于它们的多个邻近性声明合并成一个关于单个函数 $g$ 的声明。其关键创新在于利用“出域采样（out-of-domain sampling）”技术，该技术通过要求证明者提供随机点处 $g$ 的多元线性扩展值，来迫使证明者“选择”一个唯一的接近 $g$ 的码字。这使得后续的验证只需通过“入域采样（in-domain sampling）”进行抽查，从而保证了距离的保持。该协议中，对 $t$ 个入域声明的批处理采用了[CBBZ23]中的技术，使得证明者时间与 $t$ 的乘积项从 $O(t\cdot n)$ 降低到 $O(t\cdot \log n)$。

双子约束伪批处理则处理更复杂的情况：每个函数 $f_i$ 不仅满足一个约束点声明，还满足一个关于打包（bundled）PESAT多项式的声明。该协议借鉴了[BMNW25b]中受[EG23]启发的思路，利用多元线性求和校验（multilinear sumcheck）的变体，通过线性插值多项式 $\hat{\mathbf{A}}(X), \hat{\mathbf{B}}(X), \hat{\mathbf{F}}(X), \hat{\mathbf{U}}(X)$ 将两个不同点上的约束合并到随机点 $X=\tau$ 上。该协议的安全性依赖于线性码的“互相干一致性（mutual correlated agreement）”性质，该性质保证了随机线性组合后的接近码字必然来自于原始函数的接近码字的线性组合。

在安全性证明方面，本文提出了一个关键的工具：放宽的“逐轮”（round-by-round）提取安全定义。与传统的逐轮知识可靠性相比，新定义允许提取器在协议的过程中，利用“输出实例的见证”与“知识状态函数”来逐步推导“输入实例的见证”。这避免了传统定义中要求提取器必须在某个关键轮次后立刻输出见证的强约束，从而使得即使底层码没有高效容错解码器，也可以利用高效的擦除纠正（erasure correction）算法进行直线提取。具体而言，提取器利用见证（$u$）与输出函数（$f$）的接近关系，确定一个大的、无错的位置集合 $S$，然后将 $S$ 上的函数值限制到输入函数 $f_i$ 上，最后通过对 $f_i$ 在 $S$ 上的限制进行擦除纠正，得到接近 $f_i$ 的码字。本文证明了该新定义仍能蕴含（直线）状态恢复知识可靠性，从而为整个累加方案的Fiat-Shamir安全性提供了保障。

该方案的渐进复杂度为：对于单个累加操作，证明者 $\mathbf{P}_{ACC}$ 的域操作数和随机预言查询数与被累加关系的规模 $|\hat{\mathbf{p}}|$ 呈线性关系；验证者 $\mathbf{V}_{ACC}$ 的域操作数为对数级别；判定者 $\mathbf{D}_{ACC}$ 的计算量与被累加关系的规模 $|\hat{\mathbf{p}}|$ 呈线性关系。

### 核心公式与流程

**约束码定义**
$$ \mathcal{C}[(\tau_1, \sigma_1), \dots, (\tau_t, \sigma_t)] = \{ u \in \mathcal{C} : \hat{u}(\tau_i) = \sigma_i \text{ for all } i \in [t] \} $$
其中 $\hat{u}$ 是码字 $u$ 的多元线性扩展。
> 作用：定义了编码必须满足的额外点值约束，是构造IOR的基础。

**出域采样引理（非正式）**
$$ \Pr_{\boldsymbol{\tau} \leftarrow \mathbb{F}^{\log n}} \left[ \exists \text{ distinct } u, v \in \Lambda(\mathcal{C}, f, \delta), \hat{u}(\boldsymbol{\tau}) = \hat{v}(\boldsymbol{\tau}) \right] \leq \frac{|\Lambda(\mathcal{C}, \delta)|^2 \cdot \log n}{|\mathbb{F}|} $$
> 作用：证明了多元线性扩展在域外随机点处能够唯一标识列表中的码字，这是迫使证明者“选择”特定码字的核心。

**码字批处理协议（非正式构造）**
1. 证明者发送 $g := \gamma_1 \cdot f_1 + \gamma_2 \cdot f_2$。
2. 验证者采样 $\tau \leftarrow \mathbb{F}^{\log n}$ 并发给证明者。
3. 证明者发送 $\sigma := \hat{g}(\tau)$。
4. 验证者采样 $x_1, \ldots, x_t \leftarrow [n]$，令 $\tau_i := \text{binary}(x_i)$，并查询 $f_1, f_2$ 在该点值，计算 $\sigma_i := \gamma_1 \cdot f_1(x_i) + \gamma_2 \cdot f_2(x_i)$。
5. 验证者输出声明（约束点）列表。
> 作用：将多个函数的邻近性声明合并到单一函数 $g$ 上，同时保持了距离（distance）。

**双子约束伪批处理协议（非正式构造）**
1. 验证者采样并发送 $\tau \leftarrow \mathbb{F}$。
2. 令插值多项式 $\hat{\mathbf{A}}(X) := (1-X) \cdot \alpha_0 + X \cdot \alpha_1$，$\hat{\mathbf{B}}(X) := (1-X) \cdot \beta_0 + X \cdot \beta_1$ 等。
3. 证明者发送多项式 $\hat{h}_{\mathcal{C}}(X)$ 和 $\hat{h}_{\widehat{P}}(X)$，其值分别与约束点的内插和PESAT约束的内插相关。
4. 验证者检查 $\hat{h}_{\mathcal{C}}(0) + \hat{h}_{\mathcal{C}}(1) = (1-\tau) \cdot \mu_0 + \tau \cdot \mu_1$，对 $\hat{h}_{\widehat{P}}$ 同理。
5. 验证者采样 $\gamma \leftarrow \mathbb{F}$，并设置新的组合约束点。
> 作用：将两个独立的双子约束（点值+PESAT）批处理成一个新的双子约束。

### 实验结果

WARP是一个理论构造，论文中未提供具体的实验或基准测试结果。文中没有设置实验环境。因此无法给出具体的性能数值或与baseline的对比。论文关注的是渐进复杂度的分析，并给出了其与现有哈希基累加方案[BMNW25a, BMNW25b, BMMS25]在渐进复杂度上的理论对比表（表1）。该表显示，与所有现有方案相比，WARP的证明者在算术操作和Merkle承诺数量上均具有最低或并列最低的复杂度；其验证者在算术操作和Merkle开包数量上也具有同样的优势。WARP的有效性由严格的数学证明保证，没有提及适用规模的限制。

### 局限性与开放问题

第一，虽然WARP支持对任意域 $\mathbb{B}$ 上的关系进行累加，但这需要通过域扩张实现，此时证明者的计算复杂度会随扩张域的大小超线性增长，对于小域（如 $\mathbb{B} = GF(2)$），无法实现真正的线性时间。第二，方案的安全性要求域足够大 ($|\mathbb{F}| \ge 2^\lambda$)，这对于某些实际应用场景可能构成限制。第三，方案的参数配置（如线性码的选择、邻近性边界 $\delta$ 的选择）存在复杂的权衡，需要针对具体实例进行精细调整以优化性能，这为实际部署带来了挑战。最后，本文的工作没有提供实际实现的效率和性能数据。

### 强关联论文

[BMNW25b] Bünz, B., Mishra, P., Nguyen, W., Wang, W. ARC: accumulation for Reed–Solomon codes. **CRYPTO 2025** [Google Scholar](https://scholar.google.com/scholar?q=ARC+accumulation+for+Reed%E2%80%93Solomon+codes)

[BMNW25a] Bünz, B., Mishra, P., Nguyen, W., Wang, W. Accumulation without homomorphism. **ITCS 2025** [Google Scholar](https://scholar.google.com/scholar?q=Accumulation+without+homomorphism)

[BCMS20] Bünz, B., Chiesa, A., Mishra, P., Spooner, N. Recursive proof composition from accumulation schemes. **TCC 2020** [Google Scholar](https://scholar.google.com/scholar?q=Recursive+proof+composition+from+accumulation+schemes)

[BMMS25] Baweja, A., Mishra, P., Mopuri, T., Shtepel, M. FICS and FACS: fast IOPPs and accumulation via code-switching. **ePrint 2025** [Google Scholar](https://scholar.google.com/scholar?q=FICS+and+FACS+fast+IOPPs+and+accumulation+via+code-switching)

[BCI+20] Ben-Sasson, E., Carmon, D., Ishai, Y., Kopparty, S., Saraf, S. Proximity gaps for Reed–Solomon codes. **FOCS 2020** [Google Scholar](https://scholar.google.com/scholar?q=Proximity+gaps+for+Reed%E2%80%93Solomon+codes)

[BGKS20] Ben-Sasson, E., Goldberg, L., Kopparty, S., Saraf, S. DEEP-FRI: sampling outside the box improves soundness. **ITCS 2020** [Google Scholar](https://scholar.google.com/scholar?q=DEEP-FRI+sampling+outside+the+box+improves+soundness)

[ACFY24] Arnon, G., Chiesa, A., Fenzi, G., Yogev, E. STIR: Reed–Solomon proximity testing with fewer queries. **CRYPTO 2024** [Google Scholar](https://scholar.google.com/scholar?q=STIR+Reed%E2%80%93Solomon+proximity+testing+with+fewer+queries)

[EG23] Eagen, L., Gabizon, A. ProtoGalaxy: efficient ProtoStar-style folding of multiple instances. **ePrint 2023** [Google Scholar](https://scholar.google.com/scholar?q=ProtoGalaxy+efficient+ProtoStar-style+folding+of+multiple+instances)

[GLS+23] Golovnev, A., Lee, J., Setty, S., Thaler, J., Wahby, R.S. Brakedown: linear-time and field-agnostic SNARKs for R1CS. **CRYPTO 2023** [Google Scholar](https://scholar.google.com/scholar?q=Brakedown+linear-time+and+field-agnostic+SNARKs+for+R1CS)

[BCF+25] Brehm, M., Chen, B., Fisch, B., Resch, N., Rothblum, R.D., Zeilberger, H. Blaze: fast SNARKs from interleaved RAA codes. **EUROCRYPT 2025** [Google Scholar](https://scholar.google.com/scholar?q=Blaze+fast+SNARKs+from+interleaved+RAA+codes)


## 关键词

+ WARP线性时间累积方案
+ 证据携带数据分布式计算完整性
+ 折叠方案后量子安全哈希
+ 交互式邻近预言机归约
+ 擦除纠正直线提取器