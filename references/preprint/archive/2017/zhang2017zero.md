---
title: "A Zero-Knowledge Version of vSQL"
标题简称:
论文类型: preprint
预印本简称: archive
发表年份: 2017
modified: 2025-04-11 10:54:53
---

## A Zero-Knowledge Version of vSQL

## 发表信息

+ [archive](https://eprint.iacr.org/2017/1146)

## 作者

+ [Yupeng Zhang](Yupeng%20Zhang.md)
+ Daniel Genkin
+ [Jonathan Katz](Jonathan%20Katz.md)
+ [Dimitrios Papadopoulos](Dimitrios%20Papadopoulos.md)
+ [Charalampos Papamanthou](Charalampos%20Papamanthou.md)

## 笔记

### 背景与动机
可验证计算协议允许弱验证者将程序执行外包给强大但不可信的证明者，同时确保结果正确。Kilian的开创性工作 [23] 之后，学界构建了众多支持任意计算的协议，其中最突出的依赖基于二次算术程序的简洁论证知识 [17]，并产生了多个优化系统 [29]。这些方案大多需要预处理阶段，要么针对特定电路 [26, 13]，要么针对通用电路 [2, 4, 3]，前者无法在不重新运行昂贵预处理的情况下自适应更改计算，后者则因通用电路规模过大而引入巨大具体开销。Zhang等人于IEEE S&P 2017提出的vSQL系统 [30] 是打破上述模式的例外，其预处理仅依赖输入上界而非具体电路，并将加密操作数从与电路乘法门数线性相关降低至与输入规模线性相关，在验证SQL查询时实现了5–121倍的证明者时间减少。然而，vSQL缺乏零知识属性，即不向验证者隐藏见证信息，而这一属性在加密货币等应用中至关重要。本文旨在为vSQL所依赖的底层论证系统赋予零知识性质，填补其无法保护隐私的空白。

### 相关工作

[5] Bitansky 等. From extractable collision resistance to succinct non-interactive arguments of knowledge, and back again. **ITCS 2012** [Google Scholar](https://scholar.google.com/scholar?q=From+extractable+collision+resistance+to+succinct+non-interactive+arguments+of+knowledge%2C+and+back+again)
> 核心思路：定义并构建基于提取碰撞抵抗的简洁非交互知识论证。
> 局限与区别：该工作提供了SNARK的理论基础，但其构造的实用性远不如后续基于二次算术程序的具体系统，且不具备vSQL那种与电路无关的预处理优势。

[23] Kilian. A note on efficient zero-knowledge proofs and arguments. **STOC 1992** [Google Scholar](https://scholar.google.com/scholar?q=A+note+on+efficient+zero-knowledge+proofs+and+arguments)
> 核心思路：开创性地利用Merkle树将交互式证明转化为简洁论证。
> 局限与区别：Kilian的协议是密码学论证领域的奠基之作，但具体效率不高，不支持本文所追求的计算独立预处理。

[12] Cormode 等. Practical verified computation with streaming interactive proofs. **ITCS 2012** [Google Scholar](https://scholar.google.com/scholar?q=Practical+verified+computation+with+streaming+interactive+proofs)
> 核心思路：提出CMT协议，一种用于验证算术电路评估的高效交互式证明系统。
> 局限与区别：CMT协议本身不是零知识的，其协议消息会泄露电路中间值。本文通过在同态承诺上运行CMT协议来解决此问题。

[17] Gennaro 等. Quadratic span programs and succinct NIZKs without PCPs. **EUROCRYPT 2013** [Google Scholar](https://scholar.google.com/scholar?q=Quadratic+span+programs+and+succinct+NIZKs+without+PCPs)
> 核心思路：提出二次算术程序范式，构建了无需PCP的高效非交互零知识论证。
> 局限与区别：基于QAP的方案虽然可高效实现零知识，但预处理与电路强相关，无法实现vSQL所拥有的与电路无关的预处理特性。

[30] Zhang 等. vSQL: Verifying arbitrary SQL queries over dynamic outsourced databases. **IEEE S&P 2017** [Google Scholar](https://scholar.google.com/scholar?q=vSQL%3A+Verifying+arbitrary+SQL+queries+over+dynamic+outsourced+databases)
> 核心思路：结合CMT协议和可验证多项式委托，提出验证外包数据库查询的系统，且预处理仅依赖输入上界。
> 局限与区别：vSQL不是零知识的。本文的核心贡献正是在vSQL框架基础上，通过zk-VPD和在同态承诺上运行CMT来赋予其零知识属性。

[26] Parno 等. Pinocchio: Nearly practical verifiable computation. **IEEE S&P 2013** [Google Scholar](https://scholar.google.com/scholar?q=Pinocchio%3A+Nearly+practical+verifiable+computation)
> 核心思路：基于二次算术程序构建了首个真正实用的通用可验证计算系统。
> 局限与区别：Pinocchio需要针对每个电路进行昂贵的预处理，无法像vSQL那样自适应地改变被验证的计算。

[18] Goldwasser 等. Delegating computation: interactive proofs for muggles. **STOC 2008** [Google Scholar](https://scholar.google.com/scholar?q=Delegating+computation%3A+interactive+proofs+for+muggles)
> 核心思路：提出首个对数空间验证者的交互式证明系统用于委托任意多项式时间计算。
> 局限与区别：该工作为CMT协议提供了理论基础，但其原始构造效率较低，且不满足零知识。

[11] Chiesa 等. A zero knowledge sumcheck and its applications. **ePrint 2017** [Google Scholar](https://scholar.google.com/scholar?q=A+zero+knowledge+sumcheck+and+its+applications)
> 核心思路：展示如何利用信息论技术使包括sum-check和CMT在内的一大类代数协议具备零知识。
> 局限与区别：目前尚不明确如何将这种信息论方法兼容地整合进依赖多项式（如vSQL中的zk-VPD）的协议中。

[28] Wahby 等. Doubly-efficient zkSNARKs without trusted setup. **ePrint 2017** [Google Scholar](https://scholar.google.com/scholar?q=Doubly-efficient+zkSNARKs+without+trusted+setup)
> 核心思路：独立且并行的工作，为充分并行的电路提出高效零知识论证，同样使用在承诺上运行CMT的方法。
> 局限与区别：该构造无需预处理且安全性基于DDH，但通信与验证时间与见证大小平方根成正比；而本文构造有可信预处理但实现了对数级别的通信与验证，更适合见证量大的场景。

### 核心技术与方案

本文的整体框架沿袭vSQL [30]，结合了CMT协议 [12] 与可验证多项式委托协议（VPD）。为了达成零知识，作者对这两个核心模块分别进行了改造：将VPD替换为本文提出的零知识可验证多项式委托协议（zk-VPD），并将CMT协议移植到同态承诺上运行。

**1. 零知识可验证多项式委托协议。** 在标准的VPD中，证明者输出多项式在某个点上的求值结果本身，这泄露了信息。本文的zk-VPD修改了这一过程：证明者输出的是一个对求值结果的计算承诺，同时提供一个证明，证明该承诺确实是针对承诺的多项式在指定点上的正确求值。方案基于双线性群上的q-SDH假设和扩展的q-PKE假设。具体地，在KeyGen阶段生成一组参数，允许对变量度为d的多项式进行承诺。CommitPoly算法输出一个二元组构成的多项式承诺。CommitValue算法利用多项式恒等式引理，将多项式求值验证转化为一系列等式，并生成对中间多项式的承诺作为证明。Ver算法通过双线性映射验证这些承诺与初始多项式承诺及求值承诺之间的关系，确认求值承诺的正确性。这保证了绑定性和求值可提取性，即如果一个恶意证明者能提供有效的证明，就一定“知道”多项式及其求值。零知识性则通过模拟器实现：模拟器可以为任意多项式伪造出与真实协议不可区分的承诺和证明，因为承诺本身是统计隐藏的，且模拟器可以生成与真实交互分布一致的随机承诺。

**2. 同态承诺上的Sum-check协议。** 标准sum-check协议会泄漏被加和多项式各轮的系数。为了隐藏这些信息，本文让证明者发送这些系数的同态承诺而非系数本身。验证者利用承诺的线性同态性，可以在本地计算出一个承诺，该承诺等于本轮输出值 $g_i(0) + g_i(1)$。然后，双方执行一个零知识论证 $\mathcal{ZK}_{eq}$，证明这个本地计算的承诺与上一轮结束时得到的承诺是同一个值的承诺，从而验证了sum-check第i轮的正确性。接着，双方利用同态性计算出一个承诺，用于下一轮。该过程的零知识性来源于承诺的统计隐藏性质和 $\mathcal{ZK}_{eq}$ 的零知识性。其可靠性论证基于承诺的可提取性（由q-PKE假设确保）和基础sum-check协议的可靠性。最终，若存在恶意证明者通过了验证，则要么打破了 $\mathcal{ZK}_{eq}$ 的可靠性，要么打破了基础sum-check协议的可靠性。

**3. 同态承诺上的CMT协议。** 与sum-check同理，为了隐藏电路中间层的值，CMT协议中的所有中间消息均以同态承诺的形式传递。协议在每一层通过sum-check验证该层的计算，并将值承诺传递给下一层，以此从输出层逐层传递到输入层。在每层，除了sum-check外，证明者还需要提供承诺，用于证明两个子求值点的乘积关系（通过 $\mathcal{ZK}_{prod}$ 协议确认），以及通过承诺证明层间依赖关系的正确性。协议的零知识性由底层的承诺、sum-check以及两个专用零知识子协议共同保证。其可靠性同样依赖于承诺的可提取性、 $\mathcal{ZK}_{eq}$ 和 $\mathcal{ZK}_{prod}$ 的可靠性，以及基础CMT协议的可靠性。最终，验证者持有的承诺是指向输入层某个随机点上的求值。

**4. 系统整体集成。** 最终构造结合了zk-VPD和同态承诺上的CMT。预处理阶段仅基于输入大小n生成参数（因为zk-VPD的参数独立于电路）。在协议执行中，证明者首先对其输入（包括公知输入x和见证w）的多线性扩展多项式进行zk-VPD承诺。然后，双方执行同态承诺上的CMT协议，从输出层（固定为1）开始，逐层验证，最终得到一个对输入层随机点求值的承诺。接着，证明者使用zk-VPD生成一个针对同一随机点求值的承诺和证明。验证者通过 $\mathcal{ZK}_{eq}$ 确认这两个承诺值一致，从而将电路的执行正确性归结为zk-VPD的正确性。之后，验证者再随机挑战一个输入空间中的点，证明者再次使用zk-VPD提供对该点求值的承诺，验证者通过本地计算输入的多线性扩展值并与承诺对比，确认承诺的多项式确实对应输入。该构造的知识可靠性证明依赖zk-VPD的求值可提取性和CMT协议的可靠性。零知识性证明通过组合zk-VPD模拟器和CMT模拟器完成。系统的渐进复杂度为：证明者时间 $O(|C| \cdot \log(width(C)))$，验证者时间 $O(|x| + d \cdot \text{polylog}(|C|))$，交互轮数 $O(d \log(width(C)))$，通信量与电路深度和宽度对数相关。

### 核心公式与流程

**[zk-VPD的验证方程]**
$$
e(\mathsf{com}_{f,1} / \mathsf{com}_{y,1}, g) = e(g^{s_{\ell+1}}, \mathsf{com}_{\ell+1,1}) \prod_{i=1}^{\ell} e(g^{s_i - t_i}, \mathsf{com}_i)
$$
> 作用：双线性验证方程，用于验证承诺 $\mathsf{com}_y$ 确实是多项式 $f$ 在点 $t$ 上的正确求值承诺。其中 $\mathsf{com}_f$ 是多项式承诺， $\mathsf{com}_i$ 是证明中用于表示多项式恒等式的各分量承诺。

**[CMT协议中多线性扩展表示的层间计算关系]**
$$
\tilde{V}_i(z) = \sum_{\substack{g \in \{0,1\}^{s_i} \\ u,v \in \{0,1\}^{s_{i+1}}}} \tilde{\beta}_i(z, g) \cdot \left(\tilde{\mathsf{add}}_{i+1}(g,u,v) \cdot (\tilde{V}_{i+1}(u) + \tilde{V}_{i+1}(v)) + \tilde{\mathsf{mult}}_{i+1}(g,u,v) \cdot (\tilde{V}_{i+1}(u) \cdot \tilde{V}_{i+1}(v))\right)
$$
> 作用：定义了电路第 $i$ 层值的多线性扩展 $\tilde{V}_i$ 与第 $i+1$ 层值 $\tilde{V}_{i+1}$ 之间的核心代数关系。CMT协议通过sum-check循环利用此公式，将关于第 $i$ 层值的计算正确性归约为关于第 $i+1$ 层值的计算正确性。

**[zk-VPD中CommitValue算法的核心等式]**
$$
f(x_1,\dots,x_\ell) + r_f x_{\ell+1} - (y + r_y x_{\ell+1}) = \sum_{i=1}^\ell (x_i - t_i) \cdot (q_i(x_i,\dots,x_\ell) + r_i x_{\ell+1}) + x_{\ell+1} \left(r_f - r_y - \sum_{i=1}^\ell r_i (x_i - t_i)\right)
$$
> 作用：基于多项式恒等引理，将证明承诺值 $y$ 等于多项式 $f$ 在 $t$ 点的求值这一陈述，转化为存在低度多项式 $q_i$ 和随机掩码 $r_i$，使得上述等式成立。这是zk-VPD生成证明 $\pi$ 的代数基础。

### 实验结果
本文是理论密码学贡献，没有报告实验。
> 然而，论文指出其渐近复杂度与原始vSQL [30] 相同，仅在具体常数上因额外加密操作而略有增加。鉴于vSQL相比QAP方案在验证SQL查询时已实现5–121倍的性能提升，本文的零知识版本在保持这种相对优势的同时，提供了关键性的隐私保护。

### 局限性与开放问题
本文的构造依赖于知识假设（扩展的q-PKE），这比标准假设（如DDH或q-SDH）更强，可能引发对安全性的疑虑。与同时期Wahby等人的工作 [28] 相比，本文需要可信的预处理阶段，而后者在无预处理且仅依赖DDH的条件下实现了类似功能，但在通信和验证复杂度上存在以见证大小为根号的折衷。一个开放问题是是否存在一种同时拥有本文的对数复杂度、Wahby等人的弱假设性和无预处理特征的理想构造。此外，将本方案扩展到支持动态数据或实现非交互性，也是值得探索的方向。

### 强关联论文

[30] Zhang 等. vSQL: Verifying arbitrary SQL queries over dynamic outsourced databases. **IEEE S&P 2017**

[12] Cormode 等. Practical verified computation with streaming interactive proofs. **ITCS 2012**

[18] Goldwasser 等. Delegating computation: interactive proofs for muggles. **STOC 2008**

[17] Gennaro 等. Quadratic span programs and succinct NIZKs without PCPs. **EUROCRYPT 2013**

[28] Wahby 等. Doubly-efficient zkSNARKs without trusted setup. **ePrint 2017**

[11] Chiesa 等. A zero knowledge sumcheck and its applications. **ePrint 2017**

[5] Bitansky 等. From extractable collision resistance to succinct non-interactive arguments of knowledge, and back again. **ITCS 2012**

[23] Kilian. A note on efficient zero-knowledge proofs and arguments. **STOC 1992**

[26] Parno 等. Pinocchio: Nearly practical verifiable computation. **IEEE S&P 2013**


## 关键词

+ vSQL零知识版本扩展
+ 零知识可验证多项式委托
+ 同态承诺隐藏见证
+ 数据库查询零知识验证
+ 简洁通信验证零知识论证
+ 加密货币隐私保护应用