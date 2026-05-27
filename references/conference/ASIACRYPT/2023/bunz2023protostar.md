---
title: "Protostar: Generic efficient accumulationfolding for special-sound protocols"
doi: 10.1007/978-981-99-8724-5_3
标题简称:
论文类型: conference
会议简称: ASIACRYPT
发表年份: 2023
created: 2025-04-21 10:37:45
modified: 2025-04-21 10:39:26
---
## Protostar: Generic efficient accumulationfolding for special-sound protocols

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-981-99-8724-5_3)

## 作者

+ [Benedikt Bünz](Benedikt%20Bünz.md) 
+ [Binyi Chen](Binyi%20Chen.md) 

## 笔记

### 背景与动机
增量可验证计算（IVC）允许对任意长计算进行逐步验证，是构建分布式系统、区块链和ZK-EVM的核心技术。传统IVC依赖递归SNARK，但近年积累（accumulation）或折叠（folding）方案通过累积验证检查而非重复证明，大幅降低了递归电路开销。目前最有效的折叠方案（如Nova [22]）仅需两组椭圆曲线标量乘法，仅依赖离散对数假设与随机预言机，无需可信设置与配对。然而，这些方案仅支持固定R1CS约束系统，难以表达高次门（如Plonk中的自定义门）和查找门（lookup gates），而后者正是ZK-EVM等实际应用中不可或缺的。现有扩展方案（如Sangria [24]）在门次数d增加时，群运算量随d线性增长，抵消了高次门的优势；查找折叠方案（如Origami [35]）仍是临时构造，缺乏通用安全证明。本文试图填补两个空白：一是给出一个从任意特殊声音协议构造积累方案的通用框架，简化安全分析与实现；二是利用该框架构建一个支持多电路、高次门和查找门的非均匀IVC方案Protostar，其递归电路仅需3个群标量乘法与d+常数次哈希，且查找开销与表规模无关。

### 相关工作

[6] Bowe et al. Halo: Recursive Proof Composition without a Trusted Setup. **ePrint 2019** [Google Scholar](https://scholar.google.com/scholar?q=Halo+recursive+proof+composition+without+a+trusted+setup+2019)
> 核心思路：通过积累而非递归SNARK实现IVC，首次引入折叠思想。
> 局限与区别：构造针对特定协议，缺乏通用性；递归电路仍较大。

[22] Kothapalli et al. Nova: Recursive Zero-Knowledge Arguments from Folding Schemes. **CRYPTO 2022** [Google Scholar](https://scholar.google.com/scholar?q=Nova+recursive+zero-knowledge+arguments+from+folding+schemes+2022)
> 核心思路：为R1CS设计折叠方案，递归电路仅需2个群标量乘法。
> 局限与区别：仅支持R1CS（度2门），无法直接处理高次门和查找门。

[21] Kothapalli and Setty. SuperNova: Proving Universal Machine Executions without Universal Circuits. **ePrint 2022** [Google Scholar](https://scholar.google.com/scholar?q=SuperNova+proving+universal+machine+executions+without+universal+circuits+2022)
> 核心思路：支持非均匀R1CS，通过运行时选择电路避免通用电路。
> 局限与区别：递归电路仍需常数次哈希和哈希到群操作，累加器大小与所有电路总规模线性相关。

[20] Kothapalli and Setty. HyperNova: Recursive Arguments for Customizable Constraint Systems. **ePrint 2023** [Google Scholar](https://scholar.google.com/scholar?q=HyperNova+recursive+arguments+for+customizable+constraint+systems+2023)
> 核心思路：为CCS（含高次门）设计多折叠方案，递归电路仅1个群乘法，但哈希次数为d log n。
> 局限与区别：不显式支持非均匀计算和查找；哈希/域运算量随门数n对数增长。

[24] Mohnblatt. Sangria: A Folding Scheme for PLONK. **GitHub 2023** [Google Scholar](https://scholar.google.com/scholar?q=Sangria+a+folding+scheme+for+PLONK+2023)
> 核心思路：为Plonk类（度2门）设计折叠方案。
> 局限与区别：门次数d时群运算量增长因子d，缺乏高次门和查找支持，安全证明不完整。

[35] Zhang and Vark. Origami - a Folding Scheme for Halo2 Lookups. **HackMD 2023** [Google Scholar](https://scholar.google.com/scholar?q=Origami+a+folding+scheme+for+Halo2+lookups+2023)
> 核心思路：利用乘积检查和7次多项式构造查找折叠方案。
> 局限与区别：构造针对特定协议，非通用，需要单独安全证明。

[17] Haböck. Multivariate Lookups Based on Logarithmic Derivatives. **ePrint 2022** [Google Scholar](https://scholar.google.com/scholar?q=Multivariate+lookups+based+on+logarithmic+derivatives+2022)
> 核心思路：利用对数导数提出高效查找协议，证明者仅需O(ℓ)操作（ℓ为查找次数）。
> 局限与区别：验证时间为线性，但度低（2），适合作为本文特殊声音协议的基础。

### 核心技术与方案

本文提出一个四步通用编译器，从任意(2k-1)轮特殊声音协议出发构造IVC方案。该编译器由四个层次组成：

1. **承诺压缩**：将协议中每个证明者消息用同态承诺方案（如Pedersen承诺）替换，形成新协议$\Pi_{\mathrm{cm}}$。该协议在$\mathcal{R}_{\mathrm{cm}}^\mathcal{R}$（原关系与承诺绑定的析取）上保持特殊可靠性。

2. **Fiat-Shamir转换**：对$\Pi_{\mathrm{cm}}$应用Fiat-Shamir启发式，得到非交互知识论证（NARK），记为$\mathsf{FS}[\mathrm{cm}[\Pi_{\mathrm{sps}}]]$。验证器$\mathsf{V}_{\mathrm{NARK}}$检查：挑战由随机预言机生成，承诺与消息一致，且满足“松弛”的代数验证方程（引入错误向量$\mathbf{e}$和松弛变量$\mu$，方程形式为$\sum_{j=0}^d \mu^{d-j} f_j^{\mathsf{V}_{\mathrm{sps}}}(\cdot) = \mathbf{e}$）。松弛的目的是允许累积过程中误差的线性组合。

3. **通用累积方案**：为上述NARK设计累积方案，包括累积证明者$\mathsf{P}_{\mathrm{acc}}$、累积验证者$\mathsf{V}_{\mathrm{acc}}$和判定器$D$。核心思想是将两个累加器（原累加器和新NARK证明）通过随机挑战$\alpha$进行线性组合。具体地，在$\mathsf{P}_{\mathrm{acc}}$中，计算误差项$\mathbf{e}_j (1 \le j \le d-1)$使得关于形式变量$X$的多项式$p(X)$（式(1)）在$X=0$和$X=\infty$时的系数分别对应于旧累加器和新证明的验证。然后对误差项进行承诺，并组合出新的累加器实例和证人。$\mathsf{V}_{\mathrm{acc}}$仅检查新实例是否为旧实例和新证明实例的线性组合（$\alpha \mathbf{v} + \mathbf{v}'$），以及新的错误承诺是否等于旧错误承诺加上误差项承诺的线性组合。判定器$D$检查承诺与消息一致且松弛方程成立。特殊可靠性证明：累积方案的安全性通过分析内部交互协议$\Pi_I$的$(d+1)$-特殊可靠性得到，再经Fiat-Shamir转换为NARK，知识误差为$(Q+1)\frac{d+1}{|\mathbb{F}|}+\mathsf{negl}(\lambda)$。

4. **IVC编译器**：应用[8]的定理（Thm 1），将累积方案转化为IVC方案，递归电路实现$\mathsf{V}_{\mathrm{acc}}$本身。递归电路大小仅依赖于$\mathsf{V}_{\mathrm{acc}}$的复杂度，与原始证明大小无关。

对于高维验证器（d较大），本文进一步引入压缩技术$\mathsf{CV}[\Pi_{\mathrm{sps}}]$：通过随机线性组合将$\ell$个度-d方程合并为单个度-$(d+2)$方程，同时引入$2\sqrt{\ell}$个度-2方程验证$\beta$的幂次正确性。这使累积证明者只需$O(\sqrt{\ell})$群操作（而非$d\ell$），累积验证者只需$k+2$个群标量乘法（而非$k+d-1$）。

**Protostar**是本文面向非均匀Plonkup关系$\mathcal{R}_{\mathrm{mplkup}}$的具体实例化。其特殊声音协议$\Pi_{\mathrm{mplkup}}$组合了四个子协议：置换检查$\Pi_\sigma$（度1）、高次门检查$\Pi_{\mathrm{GATE}}$（度d）、查找检查$\Pi_{\mathrm{LK}}$（度2，基于对数导数引理[17]）、电路选择$\Pi_{\mathrm{select}}$（度2）。其中查找协议利用稀疏性优化：证明者发送的$\mathbf{g}$和$\mathbf{m}$向量仅非零位置与查找次数$\ell_{\mathrm{lk}}$有关，而与表大小$T$无关。累积证明者通过同态承诺更新维护累加器中的$\mathbf{g},\mathbf{m},\mathbf{g}\circ\mathbf{t}$等承诺，使每次累积操作仅需$O(\ell_{\mathrm{lk}})$时间而非$O(T)$。电路选择通过布尔向量$\mathbf{b}$将多个分支电路的方程加权求和，使得非均匀性几乎不增加成本。

最终得到的IVC方案Protostar的递归电路包含3个群标量乘法、$d+4$个域运算、$d+O(1)$次哈希（其中$d$为最高门次数）。本地证明者开销为$O(|\mathbf{w}|+\ell_{\mathrm{lk}})$群操作加上计算度$d+2$多项式系数的时间。验证者开销（判定器）为$O(cn+T+\ell_{\mathrm{lk}})$。

### 核心公式与流程

**[对数导数查找关系 (式(5))]**
$$\sum_{i=1}^{\ell} \frac{1}{X + \mathbf{w}_i} = \sum_{i=1}^{T} \frac{\mathbf{m}_i}{X + \mathbf{t}_i}$$
> 作用：该等式成立当且仅当$\mathbf{w}$中的所有元素均属于表$\mathbf{t}$，且$\mathbf{m}_i$为$\mathbf{w}$中等于$\mathbf{t}_i$的计数。这是构建3轮特殊声音查找协议的理论基础。

**[累积协议多项式 (式(1))]**
$$p(X) = \sum_{j=0}^{d} (X + \mathrm{acc}.\mu)^{d-j} \cdot f_j^{\mathsf{V}_{\mathrm{sps}}}\big(X\cdot \mathsf{pi} + \mathrm{acc}.\mathsf{pi}, [X\cdot\mathbf{m}_i + \mathrm{acc}.\mathbf{m}_i]_{i=1}^{k}, [X\cdot r_i + \mathrm{acc}.r_i]_{i=1}^{k-1}\big) - \mathbf{e} - \sum_{j=1}^{d-1} \mathbf{e}_j X^j$$
> 作用：该多项式在$X=\alpha$（累积挑战）处的值对应于新累加器的松弛验证结果。通过$d+1$个不同的$\alpha$值可以插值出整个多项式，从而提取出旧累加器的验证结果（常数项）和新NARK证明的验证结果（$X^d$项系数），证明累积方案的特殊可靠性。

**[压缩验证中的合并方程]**
$$\mathsf{V}_{\mathrm{sps}}'(\mathsf{pi}, [\mathbf{m}_i]_{i=1}^{k+1}, ([r_i]_{i=1}^{k-1}, \beta)) := \sum_{i=0}^{\sqrt{\ell}-1} \sum_{j=0}^{\sqrt{\ell}-1} \beta_i \cdot \beta_j' \cdot \mathsf{V}_{\mathrm{sps}, i+j\sqrt{\ell}}(\mathsf{pi}, [\mathbf{m}_i]_{i=1}^{k}, [r_i]_{i=1}^{k-1})$$
> 作用：将$\ell$个度-d检查压缩为一个度-$(d+2)$检查，其中$\beta_i = \beta^i$，$\beta_j' = \beta^{j\sqrt{\ell}}$由证明者提供，验证者额外检查$2\sqrt{\ell}$个度-2方程保证幂次正确。

### 实验结果
本文未提供具体实验数据，但给出了详细的渐进复杂度对比（见Table 1）。Protostar在非均匀Plonkup支持下的递归证明者开销为3个群标量乘法、$d+O(1)$次哈希；与之相比，HyperNova [20]为1个群乘法但$d\log n$次哈希，SuperNova [21]为2个群乘法但需要哈希到群操作。在查找支持上，Protostar的递归电路仅增加1次哈希，而HyperNova的查找支持增加$O(\log T)$次哈希和$O(\ell_{\mathrm{lk}}\log T)$域运算。Protostar的本地证明者开销为$O(|\mathbf{w}|+\ell_{\mathrm{lk}})$群操作，与表大小$T$无关，而HyperNova的查找证明者包含$O(T)$域操作。理论分析表明，当门次数$d$较大、表规模$T$远大于查找次数$\ell_{\mathrm{lk}}$时，Protostar具有显著优势。

### 局限性与开放问题
Protostar及其中间协议依赖于随机预言机模型（Fiat-Shamir启发式），目前缺乏标准模型下的安全性证明，实际应用需依靠启发式假设。为达到完美完备性，查找协议需要增加度3的检查方程，略微增加验证复杂度；但在实践中可忽略完备性错误而省略这些检查。向量查找协议的轮数增加至5轮，虽然通过累积方案仍保持高效，但协议复杂度略高。此外，本文编译器要求底层特殊声音协议的验证器是代数的，限制了适用范围；对于非代数验证器（如涉及比较、杂凑的验证），仍需单独处理。

### 强关联论文

[8] Bünz et al. Proof-Carrying Data without Succinct Arguments. **CRYPTO 2021** [Google Scholar](https://scholar.google.com/scholar?q=Proof-carrying+data+without+succinct+arguments+2021)

[22] Kothapalli et al. Nova: Recursive Zero-Knowledge Arguments from Folding Schemes. **CRYPTO 2022** [Google Scholar](https://scholar.google.com/scholar?q=Nova+recursive+zero-knowledge+arguments+from+folding+schemes+2022)

[21] Kothapalli and Setty. SuperNova: Proving Universal Machine Executions without Universal Circuits. **ePrint 2022** [Google Scholar](https://scholar.google.com/scholar?q=SuperNova+proving+universal+machine+executions+without+universal+circuits+2022)

[20] Kothapalli and Setty. HyperNova: Recursive Arguments for Customizable Constraint Systems. **ePrint 2023** [Google Scholar](https://scholar.google.com/scholar?q=HyperNova+recursive+arguments+for+customizable+constraint+systems+2023)

[17] Haböck. Multivariate Lookups Based on Logarithmic Derivatives. **ePrint 2022** [Google Scholar](https://scholar.google.com/scholar?q=Multivariate+lookups+based+on+logarithmic+derivatives+2022)

[24] Mohnblatt. Sangria: A Folding Scheme for PLONK. **GitHub 2023** [Google Scholar](https://scholar.google.com/scholar?q=Sangria+a+folding+scheme+for+PLONK+2023)

[35] Zhang and Vark. Origami - a Folding Scheme for Halo2 Lookups. **HackMD 2023** [Google Scholar](https://scholar.google.com/scholar?q=Origami+a+folding+scheme+for+Halo2+lookups+2023)

[6] Bowe et al. Halo: Recursive Proof Composition without a Trusted Setup. **ePrint 2019** [Google Scholar](https://scholar.google.com/scholar?q=Halo+recursive+proof+composition+without+a+trusted+setup+2019)

[16] Gabizon et al. PLONK: Permutations over Lagrange-bases for Oecumenical Noninteractive Arguments of Knowledge. **ePrint 2019** [Google Scholar](https://scholar.google.com/scholar?q=PLONK+permutations+over+Lagrange-bases+for+oecumenical+noninteractive+arguments+of+knowledge+2019)

[29] Setty et al. Customizable Constraint Systems for Succinct Arguments. **ePrint 2023** [Google Scholar](https://scholar.google.com/scholar?q=Customizable+constraint+systems+for+succinct+arguments+2023)


## 关键词

+ 累积
+ 折叠
+ 增量可验证计算
+ Plonk
+ 特殊声学协议