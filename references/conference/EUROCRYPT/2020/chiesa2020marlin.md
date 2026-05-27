---
title: "Marlin: Preprocessing zkSNARKs with universal and updatable SRS"
doi: 10.1007/978-3-030-45721-1_26
标题简称: Marlin
论文类型: conference
会议简称: EUROCRYPT
发表年份: 2020
modified: 2025-04-27 09:07:03
created: 2025-04-08 17:30:40
---
## Marlin: Preprocessing zkSNARKs with universal and updatable SRS

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-030-45721-1_26)

## 作者

+ [Alessandro Chiesa](Alessandro%20Chiesa.md)
+ [Yuncong Hu](Yuncong%20Hu.md)
+ [Mary Maller](Mary%20Maller.md)
+ [Pratyush Mishra](Pratyush%20Mishra.md)
+ Noah Vesely
+ Nicholas Ward

## 笔记

### 背景与动机
在零知识简洁非交互知识论证（zkSNARK）的众多应用中，预处理设置允许将电路描述在离线阶段压缩为一个短摘要，从而在后续在线阶段实现与电路规模无关的验证时间。然而，已有高效预处理构造（如Groth16 [Gro16]）所使用的结构化参考串（SRS）是电路相关的：每次电路修改都需要重新执行昂贵的多方安全计算仪式。为了解决这一可持续性问题，学术界提出了通用SRS的概念，即单个SRS可以支持任意电路，但已知实现普遍引入显著开销。最近Sonic [Mal+19]首次实现了高效通用且可更新的预处理zkSNARK，但其证明者开销比电路专用方案高出一个数量级，论证规模和验证时间也较逊色。本文的目标是在保持通用SRS优势的同时，大幅缩小与电路专用方案之间的效率差距。为此，本文提出了一套基于“代数全息证明”（AHP）与可提取多项式承诺的组合新方法，从而得到性能全面优于Sonic的预处理zkSNARK Marlin。

### 相关工作

[Mal+19] M. Maller et al. Sonic: Zero-Knowledge SNARKs from Linear-Size Universal and Updateable Structured Reference Strings. **CCS 2019** [Google Scholar](https://scholar.google.com/scholar?q=Sonic+Zero-Knowledge+SNARKs+from+Linear-Size+Universal+and+Updateable+Structured+Reference+Strings)
> 核心思路：通过多项式承诺和代数协议构造首个高效通用SRS的预处理zkSNARK。
> 局限与区别：证明者时间较电路专用方案慢10倍以上，论证大小和验证时间均不理想。本文通过引入AHP和优化多项式承诺，在所有效率参数上实现了改进。

[Gro16] J. Groth. On the Size of Pairing-Based Non-interactive Arguments. **EUROCRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=On+the+Size+of+Pairing-Based+Non-interactive+Arguments)
> 核心思路：提出目前最紧凑的电路专用zkSNARK，论证仅含3个群元素。
> 局限与区别：SRS电路专用，不支持通用性和可更新性。本文在保持通用SRS的同时，论证大小仍远小于Sonic，且验证时间接近Groth16。

[KZG10] A. Kate et al. Constant-Size Commitments to Polynomials and Their Applications. **ASIACRYPT 2010** [Google Scholar](https://scholar.google.com/scholar?q=Constant-Size+Commitments+to+Polynomials+and+Their+Applications)
> 核心思路：提出多项式承诺方案，支持常数大小的承诺和求值证明。
> 局限与区别：原始方案不满足可提取性，且仅支持单一度界和单点求值。本文对其进行了扩展，实现多轮、多多项式的可提取承诺，并支持每个多项式独立度界。

[FKL18] G. Fuchsbauer et al. The Algebraic Group Model and its Applications. **CRYPTO 2018** [Google Scholar](https://scholar.google.com/scholar?q=The+Algebraic+Group+Model+and+its+Applications)
> 核心思路：提出代数群模型（AGM），在安全证明中利用代数算法必须输出表示的性质。
> 局限与区别：本文利用AGM构造了更高效的多项式承诺方案（每个承诺只需一个群元素），并结合知识假设提供另一变体。

[Ben+19c] E. Ben-Sasson et al. Aurora: Transparent Succinct Arguments for R1CS. **EUROCRYPT 2019** [Google Scholar](https://scholar.google.com/scholar?q=Aurora:+Transparent+Succinct+Arguments+for+R1CS)
> 核心思路：提出非全息代数协议，用于R1CS，具有线性证明长度和常数查询复杂度。
> 局限与区别：非全息，验证者需读取完整的电路描述，因此无法直接实现预处理。本文将其全息化，使得验证者仅需查询编码后的索引多项式，验证时间降至对数复杂度。

[GWC19] A. Gabizon et al. PLONK: Permutations over Lagrange-bases for Oecumenical Noninteractive arguments of Knowledge. **Cryptology ePrint Archive 2019** [Google Scholar](https://scholar.google.com/scholar?q=PLONK:+Permutations+over+Lagrange-bases+for+Oecumenical+Noninteractive+arguments+of+Knowledge)
> 核心思路：独立提出类似通用SRS方案，使用置换论证。
> 局限与区别：本文构造直接支持R1CS，且编译器更一般化，支持任何AHP；PLONK则专注于特定约束系统。

### 核心技术与方案
本文的核心技术路线分为三个层次：底层是信息论原语——代数全息证明（AHP）；上层是密码学原语——可提取多项式承诺；通过一个编译器将二者结合，得到通用且可更新SRS的预处理参数。

**编译器（Theorem 8.1）：** 编译器接收一个公开随机的AHP和一个可提取多项式承诺方案，输出一个预处理参数。核心思想是将AHP中索引器输出的多项式用承诺方案提交，并将证明者每轮输出的多项式也用承诺提交；随后验证者声明查询集，证明者提供求值及证明。编译器保留了AHP的知识证明属性和零知识属性（如果承诺是隐藏的）。编译器要求底层多项式承诺方案满足可提取性，否则无法从论证证明者还原出AHP证明者所需的完整多项式。

**AHP for R1CS（Theorem 5.2）：** 本文的AHP将R1CS问题转化为三个层次的全息“求和检查”（sumcheck），依次检查：1) 逐项乘积 $Az \circ Bz = Cz$，通过随机点查询和多项式等式 $z_A(X)z_B(X)-z_C(X)=h_0(X)v_H(X)$ 执行；2) 线性关系，例如 $z_A$ 与 $z$ 通过矩阵 $A$ 相关联，通过随机点 $\alpha$ 将问题归约到单一求和检查：$q_1(X)=s(X)+r(\alpha,X)(\sum \eta_M \hat{z}_M(X))-(\sum \eta_M r_M(\alpha,X))\hat{z}(X)$ 在 $H$ 上求和为零（其中 $r=u_H$，$r_M$ 是矩阵低度扩展的特定混合）；3) 核心困难在于评估 $r_M(\alpha,\beta_1)$，本文通过另外两层求和检查将其进一步归约到只查询索引多项式（low-degree extensions of row/col/val），从而验证者仅需 $O(\log m)$ 次操作。整个AHP具有线性证明长度 $O(m)$ 和常数查询复杂度，7轮交互，证明者时间 $O((m+b)\log(m+b))$，验证者时间 $O(|x|+\log m)$。

**可提取多项式承诺（Section 6.2）：** 基基于KZG10构造，但增加了可提取性。有两种方法：1) 使用知识承诺（对每个承诺需两个群元素），基于PKE假设；2) 在代数群模型（AGM）中，每个承诺仅需一个群元素，依赖更强的模型但效率更高。方案支持同时承诺多个多项式、每个多项式独立度界（通过移位多项式技巧），以及在多个点求值（只需按点分组，分别生成证明）。方案满足彻底性、可提取性（在相应假设下）、完美隐藏（可选，通过额外随机多项式实现），且SRS是可更新的（仅包含单项式幂次）。效率上，AGM变体中承诺大小 $2n\ \mathbb{G}_1$（非隐藏）或 $2n\ \mathbb{G}_1$（隐藏），证明大小 $1\ \mathbb{G}_1+1\ \mathbb{F}_q$，验证时间约为 $2$ 个配对加 $O(n)$ 量级的多标量乘法。

**系统最终效率（Fig.1）：** Marlin的论证大小在BN-256曲线上为704字节（Sonic为1152），在BLS12-381上为880字节（Sonic为1472）。证明者时间比Sonic快10倍以上（例如，$2^{20}$约束下Marlin需796秒，Sonic需1024秒，但文中指出Sonic未实现无帮助变体，故对比基于估算），验证者时间减少到2个配对（Sonic为7个，但使用批处理后为2个）。SRS大小为 $4m\ \mathbb{G}_1$，小于Sonic的 $8m\ \mathbb{G}_1$。

### 核心公式与流程

**[R1CS索引关系定义]**
$$
(\mathrm{i}, \mathrm{x}, \mathrm{w}) = ((\mathbb{F}, H, K, A, B, C), x, w)
$$
其中 $A,B,C$ 是 $H\times H$ 矩阵，$z=(x,w)$，满足 $Az \circ Bz = Cz$。
> 作用：定义本文所处理的计算问题，是后续协议的基础。

**[多项式编码全息检验的核心公式]**
$$
\hat{M}(X,Y) := \sum_{\kappa\in K} u_H(X,\text{row}_M(\kappa))\,u_H(Y,\text{col}_M(\kappa))\,\text{val}_M(\kappa)
$$
> 作用：将稀疏矩阵 $M$ 编码为三个度小于 $|K|$ 的多项式（row, col, val）的线性组合，用于全息验证。利用 $u_H$ 在对角线上不为零、其余位置为零的性质。

**[求和检查（sumcheck）原型方程]**
$$
f(X) = h(X)v_H(X) + Xg(X) + \sigma/|H|
$$
其中 $f$ 在 $H$ 上的和为 $\sigma$，当且仅当存在多项式 $h,g$ 满足该等式。
> 作用：将子集求和问题转化为多项式等式检验，是协议的核心子程序。

**[AHP最终验证的配对方程]**
$$
e(C - vG - \gamma\bar{v}G, H) = e(\mathsf{w}, \beta H - zH)
$$
> 作用：多项式承诺的求值检验，$C$ 是承诺的线性组合，$v$ 是求值线性组合，$\mathsf{w}$ 是见证多项式承诺。

### 实验结果
本文在BLS12-381曲线上实现了Marlin，并与Groth16进行了对比（Fig. 2）。实验环境未明确给出，但测试了约束数量从 $2^{10}$ 到 $2^{20}$ 的场景。证明者时间：在 $2^{20}$ 约束下，Marlin需796秒，Groth16需512秒，Marlin约为Groth16的1.55倍。验证者时间：Marlin在所有规模下均为7.5毫秒，Groth16为2.0毫秒，Marlin约为Groth16的3.75倍。由于Sonic的无帮助变体当时无工作实现，文中未包含Sonic的实测数据。总体而言，Marlin在通用SRS下取得了接近电路专用方案Groth16的性能，且论证大小远小于Sonic。

### 局限性与开放问题
本文的AHP协议需要域 $\mathbb{F}$ 包含大小光滑的乘法子群，这限制了对任意有限域的适用性，虽然可通过使用加法子群绕过。可提取多项式承诺在AGM下的安全性依赖于代数群模型，该模型比标准模型强，虽然目前未见具体攻击，但学术界对其现实安全性仍有讨论。此外，编译器要求每个多项式承诺的查询点必须从一个超多项式大小的子集中均匀抽样（“可容许”查询采样器），这在某些场景中可能需要额外随机性来保证。未来工作可尝试将本方法论扩展到多元多项式全息证明，或构造更高效的零知识AHP以减少需要对隐藏承诺的数量。

### 强关联论文

[Mal+19] M. Maller et al. Sonic: Zero-Knowledge SNARKs from Linear-Size Universal and Updateable Structured Reference Strings. **CCS 2019** [Google Scholar](https://scholar.google.com/scholar?q=Sonic+Zero-Knowledge+SNARKs+from+Linear-Size+Universal+and+Updateable+Structured+Reference+Strings)

[Gro16] J. Groth. On the Size of Pairing-Based Non-interactive Arguments. **EUROCRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=On+the+Size+of+Pairing-Based+Non-interactive+Arguments)

[KZG10] A. Kate et al. Constant-Size Commitments to Polynomials and Their Applications. **ASIACRYPT 2010** [Google Scholar](https://scholar.google.com/scholar?q=Constant-Size+Commitments+to+Polynomials+and+Their+Applications)

[FKL18] G. Fuchsbauer et al. The Algebraic Group Model and its Applications. **CRYPTO 2018** [Google Scholar](https://scholar.google.com/scholar?q=The+Algebraic+Group+Model+and+its+Applications)

[Ben+19c] E. Ben-Sasson et al. Aurora: Transparent Succinct Arguments for R1CS. **EUROCRYPT 2019** [Google Scholar](https://scholar.google.com/scholar?q=Aurora:+Transparent+Succinct+Arguments+for+R1CS)

[GWC19] A. Gabizon et al. PLONK: Permutations over Lagrange-bases for Oecumenical Noninteractive arguments of Knowledge. **Cryptology ePrint Archive 2019** [Google Scholar](https://scholar.google.com/scholar?q=PLONK:+Permutations+over+Lagrange-bases+for+Oecumenical+Noninteractive+arguments+of+Knowledge)

[Gro+18] J. Groth et al. Updatable and Universal Common Reference Strings with Applications to zk-SNARKs. **CRYPTO 2018** [Google Scholar](https://scholar.google.com/scholar?q=Updatable+and+Universal+Common+Reference+Strings+with+Applications+to+zk-SNARKs)

[COS20] A. Chiesa et al. Fractal: Post-Quantum and Transparent Recursive Proofs from Holography. **EUROCRYPT 2020** [Google Scholar](https://scholar.google.com/scholar?q=Fractal:+Post-Quantum+and+Transparent+Recursive+Proofs+from+Holography)


## 关键词

+ 预处理zkSNARK
+ 通用更新结构化参考字符串
+ 代数全息证明
+ R1CS约束系统
+ Marlin