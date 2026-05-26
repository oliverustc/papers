---
title: "PLONK: Permutations over Lagrange-bases for oecumenical noninteractive arguments of knowledge"
标题简称:
论文类型: preprint
预印本简称: archive
发表年份: 2019
modified: 2025-04-10 16:41:58
---

## PLONK: Permutations over Lagrange-bases for oecumenical noninteractive arguments of knowledge

## 发表信息

最早在2017年放在archive上，但2025年3月又有了更新

+ [原文链接](https://eprint.iacr.org/2019/953)

## 作者

+ [Ariel Gabizon](Ariel%20Gabizon.md)
+ Zachary J. Williamson
+ Oana Ciobotaru

## 笔记

### 背景与动机
零知识简洁非交互式知识论证（zk-SNARK）在实际部署中的一大障碍是结构化参考字符串（SRS）的生成方式。理想情况下，SRS应具备“通用且可更新”的特性，即同一个SRS可用于所有不超过特定规模上限的电路，且任何时刻都可由新参与方更新，仅需保证所有更新者中至少有一方诚实即可保证安全性。Maller 等人于提出的 Sonic 协议 [MBKM19] 是第一个满足完全简洁性的通用zk-SNARK，但其证明构造的开销仍然较高，尤其是在需要完全简洁验证的模式下。Sonic 的算术化方案受 [BCC+16] 启发，其中隐含的“求值”过程相对间接，并且其置换论证基于双变量多项式系数上的邻接单形式关系，这导致了较高的证明者计算复杂度。本文旨在填补这一空白，通过一种更直接的电路算术化方式，并结合基于乘法子群上单变量多项式求值的置换论证，显著降低证明者的运行时间，同时保持完全简洁的验证和通用的SRS。

### 相关工作
[BG12] Bayer, S. and Groth, J. Efficient zero-knowledge argument for correctness of a shuffle. *EUROCRYPT 2012* [Google Scholar](https://scholar.google.com/scholar?q=Efficient+zero-knowledge+argument+for+correctness+of+a+shuffle)
> 核心思路：提出了一种用于证明置换正确性的论证协议，其核心在于构造一个“Grand Product”来验证两个序列的乘积相等。
> 局限与区别：该协议的实现依赖于检验多项式在“邻接单形式”系数之间的关系。PlonK 将其思想迁移到乘法子群上，通过检验多项式在邻接群元素上的值关系来简化协议。

[MBKM19] Maller, M., Bowe, S., Kohlweiss, M., and Meiklejohn, S. Sonic: Zero-knowledge SNARKs from linear-size universal and updateable structured reference strings. *ePrint 2019* [Google Scholar](https://scholar.google.com/scholar?q=Sonic:+Zero-knowledge+SNARKs+from+linear-size+universal+and+updateable+structured+reference+strings)
> 核心思路：首个同时实现通用SRS和完全简洁验证的SNARK。其算术化借鉴了 [BCC+16]，并通过巧妙的批处理策略摊销双变量多项式求值的开销，从而得到一个证明者效率更高但非完全简洁的版本。
> 局限与区别：其完全简洁版本需要计算273n次群指数运算，效率较低。PlonK 通过使用基于单变量多项式求值和乘法子群的算术化，绕开了双变量多项式求值这一瓶颈，显著降低了证明者的计算量。

[Gro16] Groth, J. On the size of pairing-based non-interactive arguments. *EUROCRYPT 2016* [Google Scholar](https://scholar.google.com/scholar?q=On+the+size+of+pairing-based+non-interactive+arguments)
> 核心思路：提出了当时最有效的非通用SNARK，其证明仅包含2个G1元素和1个G2元素，验证复杂度低。
> 局限与区别：其SRS是电路相关的，不可通用，且不可更新。PlonK 在证明者计算量上约为 Groth16 方案的1.1至3倍（取决于加法门数量），但换取了通用性和可更新性。

[KZG10] Kate, A., Zaverucha, G. M., and Goldberg, I. Constant-size commitments to polynomials and their applications. *ASIACRYPT 2010* [Google Scholar](https://scholar.google.com/scholar?q=Constant-size+commitments+to+polynomials+and+their+applications)
> 核心思路：提出多项式承诺方案，允许对一个多项式进行承诺，并在给定一个点后，提供一个常数大小的证明来验证该点的求值是正确的。
> 局限与区别：PlonK 采用并批处理了该方案的变体，使其能够同时高效地验证多个多项式在多个点上的求值，这是整个协议编译的关键工具。

[CHM+19] Chiesa, A., Hu, Y., Maller, M., Mishra, P., Vesely, N., and Ward, N. P. Marlin: Preprocessing zkSNARKs with universal and updatable SRS. *ePrint 2019* [Google Scholar](https://scholar.google.com/scholar?q=Marlin:+Preprocessing+zkSNARKs+with+universal+and+updatable+SRS)
> 核心思路：与 PlonK 同时期的并行工作，同样旨在构造通用SNARK。其核心贡献在于提出了一种在拉格朗日基下验证稀疏双变量多项式求值的技术。
> 局限与区别：Marlin 基于 R1CS 约束系统，PlonK 基于特定类型的定制约束系统。对于具有“频繁大加法扇入”的约束系统，Marlin 可能表现更好。但对于包含较多乘法门的电路，PlonK 在证明者群运算量和证明大小上均有所优势（约2倍）。

[COS19] Chiesa, A., Ojha, D., and Spooner, N. Fractal: Post-quantum and transparent recursive proofs from holography. *ePrint 2019* [Google Scholar](https://scholar.google.com/scholar?q=Fractal:+Post-quantum+and+transparent+recursive+proofs+from+holography)
> 核心思路：与 Marlin 类似，也关注通用SNARK，并在后量子安全和递归证明方面有独特贡献。同样提出了在拉格朗日基下验证稀疏双变量多项式求值的技术。
> 局限与区别：Fractal 是透明的（无需可信设置），而 PlonK 需要一个通用且可更新的 SRS。在完全简洁模式下，PlonK 的证明者效率更高。

### 核心技术与方案
PlonK 的整体框架是将电路满足性问题转化为一组多项式恒等式的验证问题。它包含三个核心层次：算术化、置换检查和多项式承诺编译。

**算术化与约束系统**
论文定义了一种特定的约束系统，参数为 $n$（门数）和 $m$（线数）。它通过五个选择子向量 $\mathbf{q_L}, \mathbf{q_R}, \mathbf{q_O}, \mathbf{q_M}, \mathbf{q_C}$ 和一个线连接关系 $\mathcal{V}=(\mathbf{a}, \mathbf{b}, \mathbf{c})$ 来描述电路。一个赋值 $\mathbf{x} \in \mathbb{F}^m$ 满足电路当且仅当对于每个门 $i \in [n]$，以下等式成立：
$$
(\mathbf{q_L})_i \cdot \mathbf{x}_{\mathbf{a}_i} + (\mathbf{q_R})_i \cdot \mathbf{x}_{\mathbf{b}_i} + (\mathbf{q_O})_i \cdot \mathbf{x}_{\mathbf{c}_i} + (\mathbf{q_M})_i \cdot (\mathbf{x}_{\mathbf{a}_i} \mathbf{x}_{\mathbf{b}_i}) + (\mathbf{q_C})_i = 0.
$$
这可以表示任意扇入为2的算术电路。证明者需要为左、右、输出三条线构造三个多项式 $f_L, f_R, f_O$，使其在乘法子群 $H$ 上的取值分别对应电路注释中的线值。

**置换检查与线连接**
电路中的线连接（“拷贝约束”）要求某些线值必须相等。这些约束可以统一为一个作用在 $3n$ 个元素上的置换 $\sigma$。PlonK 利用并改进了基于 [BG12] 的置换论证。其核心思想是，构造一个辅助多项式 $Z(X)$，使得若值序列 $(f_L(g^i), f_R(g^i), f_O(g^i))$ 拷贝满足置换 $\sigma$，则 $Z$ 在乘法子群 $H$ 的连续点上满足递推关系：
$$Z(g) = 1, \quad Z(g^{i+1}) = Z(g^i) \cdot \frac{f_L'(g^i) \cdot f_R'(g^i) \cdot f_O'(g^i)}{g_L'(g^i) \cdot g_R'(g^i) \cdot g_O'(g^i)}$$
其中 $f'$ 和 $g'$ 是原始多项式加上随机数 $\beta, \gamma$ 和位置标识多项式后的版本。验证者只需在 $H$ 上检查两点恒等式：$L_1(a)(Z(a)-1) = 0$ 和 $Z(a) f'(a) = g'(a) Z(a \cdot g)$。这种基于乘法子群的构造，利用拉格朗日基的稀疏表示，极大地简化了协议的复杂度。

**多项式承诺编译与最终协议**
最后，整个“理想化”的多项式协议（其中证明者发送多项式，理想验证者检查多项式恒等式）通过一个批处理的 [KZG10] 多项式承诺方案 [KZG10, MBKM19] 进行编译。该编译过程将理想协议转换为一个在代数群模型下具有知识可靠性的具体协议。最终协议中，证明者需要：
1. 提交线多项式 $f_L, f_R, f_O$ 和置换多项式 $Z$。
2. 与验证者交互，执行置换检查。
3. 计算并提交一个商多项式 $t(X)$，其被设计用来同时打包门约束和置换约束的检查，使其在 $H$ 上为零。即 $t(X) = (GateConstraint + \alpha \cdot PermutationConstraint) / Z_H(X)$，其中 $Z_H(X)$ 是 $H$ 的零化多项式。
4. 打开承诺，证明随机挑战点上的求值正确。

最终，验证者仅需进行两次配对操作和少量群指数运算即可验证证明。对于“快速”证明者版本，证明者工作量约为 $9(n+a) \mathbb{G}_1$ 指数运算，其中 $a$ 是加法门数，通信开销为 $9 \mathbb{G}_1$ 元素和 $6 \mathbb{F}$ 元素。

### 核心公式与流程

**[批处理多项式承诺打开]**
给定两个求值点 $z$ 和 $z'$，以及两组多项式 $\{f_i\}$ 和 $\{f'_i\}$，证明者计算：
$$h(X) := \sum_{i=1}^{t_1} \gamma^{i-1} \cdot \frac{f_i(X) - f_i(z)}{X - z}$$
$$h'(X) := \sum_{i=1}^{t_2} \gamma'^{i-1} \cdot \frac{f'_i(X) - f'_i(z')}{X - z'}$$
验证者通过一个随机数 $r'$ 将两个检查合并为一个配对等式：
$$e(F + z \cdot W + r' z' \cdot W', [1]_2) \cdot e(-W - r' \cdot W', [x]_2) = 1$$
> 作用：这是 PlonK 编译工具的核心，允许零知识地同时证明多个多项式在多个点的求值正确性，显著降低证明大小和验证复杂度。

**[核心检查恒等式]**
验证者最终需要验证以下理想恒等式在子群 $H$ 上成立：
$$\mathbf{q_L} \cdot f_L + \mathbf{q_R} \cdot f_R + \mathbf{q_O} \cdot f_O + \mathbf{q_M} \cdot f_L \cdot f_R + (\mathbf{q_C} + \mathsf{PI}) = 0$$
$$L_1(a)(Z(a)-1) = 0$$
$$Z(a) f'(a) = g'(a) Z(a \cdot g)$$
> 作用：第一个恒等式强制执行电路的门约束，后两个强制执行线拷贝约束（置换检查）。这些恒等式在理想协议中被完美地检查，然后在具体协议中通过商多项式 $t(X)$ 和随机挑战合并。

**[最终验证配对等式]**
在编译后的非交互协议中，验证者执行唯一的配对检查：
$$e([W_z]_1 + u \cdot [W_{z\omega}]_1, [x]_2) \stackrel{?}{=} e(z \cdot [W_z]_1 + u z \omega \cdot [W_{z\omega}]_1 + [F]_1 - [E]_1, [1]_2)$$
> 作用：此等式同时验证了所有多项式在点 $z$ 和 $z\omega$ 上的求值正确性，以及对线性化多项式 $r(X)$ 的检查。它是 PlonK 证明大小恒定为 $9 \mathbb{G}_1 + 6 \mathbb{F}$ 的关键，验证者仅需执行 2 次配对运算。

### 实验结果
实验在 Surface Pro 6 (i7-8650U, 16GB RAM) 上使用 BN254 曲线和 Barretenberg 库进行。测试结果表明，即使对于包含超过一百万个门的电路，PlonK 证明的构造也可以在消费级硬件上完成，时间约为 23 秒，这标志着通用 SNARK 在效率上的重大进步。具体地，对于 $2^{20}$ 个门，证明构造时间约为 32 秒。电路预处理（一次性的）时间约为 12 秒。验证时间则稳定在约 1.3 毫秒，与电路规模几乎无关。在证明构造中，快速傅里叶变换的时间与椭圆曲线标量乘的时间相当。与同类工作相比，PlonK 的 SRS 大小仅与门数线性相关（而非更大），这是一个显著的优势。与完全简洁的 Sonic 相比，PlonK 的证明者工作量减少了约 7.5 到 20 倍的群指数运算。与通用 SNARK Marlin [CHM+19] 相比，对于同样规模的门数 $n$，PlonK 在证明者群运算和证明大小上约有 2 倍的优势。

### 局限性与开放问题
PlonK 的主要局限在于其算术化针对常数扇入电路进行了优化，对于具有“频繁大加法扇入”的约束系统（如 R1CS 中的全稠密约束），其性能可能不如 Marlin [CHM+19] 等基于 R1CS 的方案。将 PlonK 的设计与 Marlin/Fractal 中用于处理稀疏双变量求值的思路相结合，可能会带来进一步的性能提升，尤其是在可以将部分证明者工作委托给外部辅助者（helper）的场景下。此外，虽然本文分析了代数群模型下的知识可靠性，但将安全性完全建立在标准假设上，并探索后量子安全变体，仍是有价值的开放方向。

### 强关联论文

[MBKM19] Maller, M., Bowe, S., Kohlweiss, M., and Meiklejohn, S. **Sonic: Zero-knowledge SNARKs from linear-size universal and updateable structured reference strings.** *IACR Cryptology ePrint Archive*, 2019:99, 2019. [Google Scholar](https://scholar.google.com/scholar?q=Sonic:+Zero-knowledge+SNARKs+from+linear-size+universal+and+updateable+structured+reference+strings)

[BG12] Bayer, S. and Groth, J. **Efficient zero-knowledge argument for correctness of a shuffle.** In *Advances in Cryptology - EUROCRYPT 2012*, pages 263–280, 2012. [Google Scholar](https://scholar.google.com/scholar?q=Efficient+zero-knowledge+argument+for+correctness+of+a+shuffle)

[Gro16] Groth, J. **On the size of pairing-based non-interactive arguments.** In *Advances in Cryptology - EUROCRYPT 2016*, pages 305–326, 2016. [Google Scholar](https://scholar.google.com/scholar?q=On+the+size+of+pairing-based+non-interactive+arguments)

[KZG10] Kate, A., Zaverucha, G. M., and Goldberg, I. **Constant-size commitments to polynomials and their applications.** In *Advances in Cryptology - ASIACRYPT 2010*, pages 177–194, 2010. [Google Scholar](https://scholar.google.com/scholar?q=Constant-size+commitments+to+polynomials+and+their+applications)

[CHM+19] Chiesa, A., Hu, Y., Maller, M., Mishra, P., Vesely, N., and Ward, N. P. **Marlin: Preprocessing zkSNARKs with universal and updatable SRS.** *IACR Cryptology ePrint Archive*, 2019:1047, 2019. [Google Scholar](https://scholar.google.com/scholar?q=Marlin:+Preprocessing+zkSNARKs+with+universal+and+updatable+SRS)

[COS19] Chiesa, A., Ojha, D., and Spooner, N. **Fractal: Post-quantum and transparent recursive proofs from holography.** *IACR Cryptology ePrint Archive*, 2019:1076, 2019. [Google Scholar](https://scholar.google.com/scholar?q=Fractal:+Post-quantum+and+transparent+recursive+proofs+from+holography)

[Gab19] Gabizon, A. **Auroralight: improved prover efficiency and SRS size in a soniclike system.** *IACR Cryptology ePrint Archive*, 2019:601, 2019. [Google Scholar](https://scholar.google.com/scholar?q=Auroralight:+improved+prover+efficiency+and+SRS+size+in+a+soniclike+system)

[BCC+16] Bootle, J., Cerulli, A., Chaidos, P., Groth, J., and Petit, C. **Efficient zero-knowledge arguments for arithmetic circuits in the discrete log setting.** In *Advances in Cryptology - EUROCRYPT 2016*, pages 327–357, 2016. [Google Scholar](https://scholar.google.com/scholar?q=Efficient+zero-knowledge+arguments+for+arithmetic+circuits+in+the+discrete+log+setting)

[FKL18] Fuchsbauer, G., Kiltz, E., and Loss, J. **The algebraic group model and its applications.** In *Advances in Cryptology - CRYPTO 2018*, pages 33–62, 2018. [Google Scholar](https://scholar.google.com/scholar?q=The+algebraic+group+model+and+its+applications)

[BGM17] Bowe, S., Gabizon, A., and Miers, I. **Scalable multi-party computation for zk-snark parameters in the random beacon model.** *Cryptology ePrint Archive, Report 2017/1050*, 2017. [Google Scholar](https://scholar.google.com/scholar?q=Scalable+multi-party+computation+for+zk-snark+parameters+in+the+random+beacon+model)


## 关键词

+ PLONK通用SNARK构造
+ 可更新通用结构化参考字符串
+ 多项式承诺置换论证
+ 简洁验证算术电路
+ Lagrange基非交互式知识论证