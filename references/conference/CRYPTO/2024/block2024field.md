---
title: "Field-Agnostic SNARKs from Expand-Accumulate Codes"

标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 2024

modified: 2025-04-08 21:03:53
---

## Field-Agnostic SNARKs from Expand-Accumulate Codes

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-68403-6_9)

## 作者

+ [Alexander R. Block](Alexander%20R.%20Block.md)
+ [Zhiyong Fang](Zhiyong%20Fang.md)
+ [Jonathan Katz](Jonathan%20Katz.md)
+ [Justin Thaler](Justin%20Thaler.md)
+ Hendrik Waldner
+ [Yupeng Zhang](Yupeng%20Zhang.md)

## 笔记

### 背景与动机
构建高效的非交互式简洁知识论证（SNARK）是密码学领域的核心问题之一，其在区块链等场景具有广泛的应用前景。在众多SNARK构造中，基于纠错码的方案因其良好的具体效率、透明的设置过程以及潜在的后量子安全性而备受关注。然而，现有基于代码的SNARK存在两个主要瓶颈：一是多数方案依赖于特定的有限域，例如，基于Reed-Solomon码的Ligero、Stark和Aurora等方案依赖快速傅里叶变换（FFT）来获得拟线性证明者时间，这要求域具有大阶的2的幂次乘法子群，导致在处理非FFT友好域上的计算（如secp256k1曲线上的ECDSA验证）时效率极低；二是基于通用线性码的方案（如Brakedown）虽然与域无关，但其证明尺寸较大，这源于其底层代码（如Spielman码）的相对距离不够好。本文旨在填补这一空白，构建一种既能与域无关，又具有较小具体证明尺寸的基于代码的SNARK。

### 相关工作

[1] Ames, S.等. Ligero: Lightweight Sublinear Arguments Without a Trusted Setup. **ACM CCS 2017** [Google Scholar](https://scholar.google.com/scholar?q=Ligero+Lightweight+Sublinear+Arguments+Without+a+Trusted+Setup)
> 核心思路：利用Reed-Solomon码构建IOP，实现亚线性证明尺寸。
> 局限与区别：依赖FFT，非域无关；证明尺寸较大。

[8] Ben-Sasson, E.等. Aurora: Transparent Succinct Arguments for R1CS. **EUROCRYPT 2019** [Google Scholar](https://scholar.google.com/scholar?q=Aurora+Transparent+Succinct+Arguments+for+R1CS)
> 核心思路：在Ligero基础上优化，通过线性化技术将证明尺寸降至对数级。
> 局限与区别：同样依赖Reed-Solomon码和FFT，非域无关；证明者时间较长。

[5] Ben-Sasson, E.等. Scalable Zero Knowledge with No Trusted Setup. **CRYPTO 2019** [Google Scholar](https://scholar.google.com/scholar?q=Scalable+Zero+Knowledge+with+No+Trusted+Setup)
> 核心思路：提出STARK方案，利用FRI协议实现量子安全和对数级验证时间。
> 局限与区别：同样基于FFT友好的域，非域无关。

[28] Golovnev, A.等. Brakedown: Linear-Time and Field-Agnostic SNARKs for R1CS. **CRYPTO 2023** [Google Scholar](https://scholar.google.com/scholar?q=Brakedown+Linear-Time+and+Field-Agnostic+SNARKs+for+R1CS)
> 核心思路：利用Spielman等线性时间可编码的线性码构建域无关SNARK，证明尺寸为平方根级。
> 局限与区别：证明了层和距离的具体数值较差，导致其证明尺寸在具体实现中较大。本文直接改进其底层码，获得更小的证明尺寸。

[19] Boyle, E.等. Correlated Pseudorandomness from Expand-Accumulate Codes. **CRYPTO 2022** [Google Scholar](https://scholar.google.com/scholar?q=Correlated+Pseudorandomness+from+Expand-Accumulate+Codes)
> 核心思路：提出了扩展-累加（EA）码，并分析了其在二进制域上的渐近性。
> 局限与区别：其距离分析仅针对二进制域，且相对距离的证明界限不优；对更大有限域的渐近性能分析被留作开放问题。本文解决了这个开放问题，并将分析推广到任意有限域。

### 核心技术与方案

本文的核心技术路线是遵循Brakedown [28] 框架，将构建SNARK的任务转化为构建多项式承诺方案（PCS），而PCS的安全性又依赖于底层线性纠错码的相对距离。因此，提升SNARK性能的关键是找到一个具有高相对距离（以减小证明尺寸）和高效编码算法（以维持快速的证明者时间）的、且与域无关的线性码。

本文的核心技术贡献在于改进了扩展-累加（EA）码 [19] 的距离分析，并将其推广到任意有限域，从而用它替代Brakedown中使用的Spielman码。具体构造如下：

1.  **改进的并置EA码**：论文分析的是“并置EA码”，记为 $C[\mathbf{E}_1, \mathbf{E}_2]$。该码的编码函数为 $C[\mathbf{E}_1, \mathbf{E}_2](\mathbf{x}) \mapsto (\mathbf{x}\mathbf{E}_1\mathbf{A}) \| (\mathbf{x}\mathbf{E}_2\mathbf{A})$，其中 $\mathbf{A}$ 是上三角累加矩阵，$\mathbf{E}_1$ 是每行恰好有 $t$ 个非零元的扩展矩阵，$\mathbf{E}_2$ 是服从伯努利分布的随机稀疏矩阵。之所以采用并置结构，是因为分析能证明 $\mathbf{E}_1\mathbf{A}$ 对于低重量输入（$\text{wt}(\mathbf{x}) = O(n/t)$）具有良好距离，而对于高重量输入则依赖 $\mathbf{E}_2\mathbf{A}$ 来保证距离。
2.  **距离分析方法（IOWE技术）**：为了证明该码具有恒定的相对距离，论文采用了输入-输出重量枚举器（IOWE）技术。核心思路是计算一个重量为 $w$ 的均匀随机向量经过累加矩阵 $\mathbf{A}$ 后，映射到重量为 $h$ 的码字的概率。通过分析此概率，进而使用联合界（union bound）来估算存在一个非零消息 $\mathbf{x}$ 使得其编码重量小于某个阈值 $\delta N$ 的概率。对于通用有限域 $\mathbb{F}_q$，论文推导了更复杂的IOWE公式（定理4），该公式考虑了累加过程中非零值的各种组合情况。
3.  **基于PCS的SNARK**：论文直接复用Brakedown [28] 提出的PCS协议（协议1）。在该协议中，证明者将多项式系数排列成 $k \times k$ 矩阵 $\mathbf{C}$，并对每一行进行线性编码（使用EA码），得到 $k \times n$ 矩阵 $\mathbf{C}_1$。承诺是向量 $\text{Root}_i$ 的Merkle树根，其中 $\text{Root}_i$ 是 $\mathbf{C}_1$ 第 $i$ 列的Merkle树根。打开时，验证者通过查询打开若干编码后的列来检查线性关系。证明的可靠性依赖于底层线性码的距离。根据定理5，更大的距离 $\delta$ 意味着可以用更少的列打开次数 $t$ 来达到相同的声音误差。因此，EA码更好的距离直接带来了更小的证明尺寸。
4.  **复杂度与性能**：最终得到的SNARK具有 $O(M \log M)$ 的证明者时间和 $O(\sqrt{M})$ 的证明尺寸，其中 $M$ 是R1CS约束的大小。虽然证明者时间从线性变为拟线性，但由于EA码编码算法极其简单，其具体运行时间与Brakedown的线性时间相近（仅慢1.2倍），而证明尺寸却因其更好的相对距离（0.1 vs. 0.04）而大幅减小（缩小1.9–2.8倍）。

### 核心公式与流程

**[二进制累加码的IOWE（定理2）]**
$$
A_{w,h}^{N,2} = \binom{h - 1}{\left\lceil \frac{w}{2} \right\rceil - 1} \cdot \binom{N - h}{\left\lfloor \frac{w}{2} \right\rfloor}
$$
> 作用：给出了在二进制域下，重量为 $w$ 的向量经过累加矩阵 $\mathbf{A}$ 后，得到重量为 $h$ 的向量的数量。这一公式是分析二进制EA码距离的第一步。

**[通用有限域累加码的IOWE（定理4）]**
$$
A_{w,h}^{N,q} = \sum_{i=0}^{w-1} \binom{h-1}{\left\lceil \frac{w-i}{2} \right\rceil - 1} \binom{N-h}{\left\lfloor \frac{w-i}{2} \right\rfloor} \binom{h-\left\lceil \frac{w-i}{2} \right\rceil}{i} (q-1)^{\left\lceil \frac{w-i}{2} \right\rceil} (q-2)^{i}
$$
> 作用：将上述IOWE分析推广到任意有限域 $\mathbb{F}_q$，其中 $i$ 表示处在“运行”中间（既不开始也不结束运行）的非零元素个数。该公式是本文分析通用域上EA码距离的核心。

**[Brakedown多项式承诺方案（协议1）]**
> 协议1是构建SNARK的基础。其核心流程是：
> 1.  证明者将多项式系数排列成 $k \times k$ 矩阵 $\mathbf{C}$。
> 2.  证明者使用线性码 $E_C$（本文中为EA码）编码矩阵的每一行，得到 $k \times n$ 矩阵 $\mathbf{C}_1$。
> 3.  证明者对 $\mathbf{C}_1$ 的每一列构建Merkle树，最终承诺（Commitment）是这些Merkle树根的Merkle树根。
> 4.  打开时，证明者发送承诺多项式在点 $\mathbf{x}$ 处的值 $y$ 和两个线性组合 $y_r, y_1$。
> 5.  验证者随机选择 $t$ 个列索引，要求证明者打开这些列，并检查这些打开的列与 $y_r$ 和 $y_1$ 的线性关系是否一致（通过编码后的值）。
> 6.  最终，验证者检查 $y$ 是否等于 $\langle \mathbf{x}_1, y_1 \rangle$。

### 实验结果

实验在AWS c5a.16xlarge（64核，124G内存）实例上进行。论文将基于EA码的SNARK与Ligero、Aurora、Brakedown以及Groth16进行了对比。对于ECDSA签名验证（在secp256k1曲线上），由于域无关性，基于EA码的方案可直接在原生域上运行，其R1CS规模为 $2^{16}$ 约束，而Ligero和Aurora等非域无关方案需在$2^{21}$约束的非原生域上运行。实验结果表明，在ECDSA验证任务中，本文证明者时间仅需0.23秒，比Ligero（103秒）、Aurora（534秒）和Groth16（149秒）快2-3个数量级。与同类型的域无关方案Brakedown相比，本文证明者时间（0.23秒）比Brakedown（0.17秒）慢约1.2倍，但证明尺寸显著减小：在可证明距离（$\delta=0.1$）下为1.1MB（对应Brakedown-Improved的1.1MB），在猜想距离（$\delta=0.25$）下仅为778KB，而原始Brakedown的证明尺寸为2.2MB。这表明在获得域无关性的同时，本文方案在以证明尺寸为代价换取灵活性方面取得了很好的权衡，其具体性能在实用规模（如$2^{20}$条约束）下非常具有竞争力。

### 局限性与开放问题
本文的局限在于其距离分析依赖并置两个不同分布的扩展矩阵（$\mathbf{E}_1$ 和 $\mathbf{E}_2$）来覆盖所有输入。论文猜想，单独使用第一种EA码（$\mathbf{E}_1$）就足以构成渐近好码，但这仍是一个未解决的开放问题。此外，论文虽给出了关于EA码伪距离的猜想，但未提供严格的证明，这可能意味着存在针对该码的非平凡攻击，尚需进一步研究。

### 强关联论文

[19] Boyle, E.等. Correlated Pseudorandomness from Expand-Accumulate Codes. **CRYPTO 2022** [Google Scholar](https://scholar.google.com/scholar?q=Correlated+Pseudorandomness+from+Expand-Accumulate+Codes)

[1] Ames, S.等. Ligero: Lightweight Sublinear Arguments Without a Trusted Setup. **ACM CCS 2017** [Google Scholar](https://scholar.google.com/scholar?q=Ligero+Lightweight+Sublinear+Arguments+Without+a+Trusted+Setup)

[5] Ben-Sasson, E.等. Scalable Zero Knowledge with No Trusted Setup. **CRYPTO 2019** [Google Scholar](https://scholar.google.com/scholar?q=Scalable+Zero+Knowledge+with+No+Trusted+Setup)

[8] Ben-Sasson, E.等. Aurora: Transparent Succinct Arguments for R1CS. **EUROCRYPT 2019** [Google Scholar](https://scholar.google.com/scholar?q=Aurora+Transparent+Succinct+Arguments+for+R1CS)

[28] Golovnev, A.等. Brakedown: Linear-Time and Field-Agnostic SNARKs for R1CS. **CRYPTO 2023** [Google Scholar](https://scholar.google.com/scholar?q=Brakedown+Linear-Time+and+Field-Agnostic+SNARKs+for+R1CS)

[14] Bootle, J.等. Linear-Time Zero-Knowledge Proofs for Arithmetic Circuit Satisfiability. **ASIACRYPT 2017** [Google Scholar](https://scholar.google.com/scholar?q=Linear-Time+Zero-Knowledge+Proofs+for+Arithmetic+Circuit+Satisfiability)

[44] Xie, T.等. Orion: Zero Knowledge Proof with Linear Prover Time. **CRYPTO 2022** [Google Scholar](https://scholar.google.com/scholar?q=Orion+Zero+Knowledge+Proof+with+Linear+Prover+Time)

[46] Zhang, J.等. Transparent Polynomial Delegation and Its Applications to Zero Knowledge Proof. **IEEE S&P 2020** [Google Scholar](https://scholar.google.com/scholar?q=Transparent+Polynomial+Delegation+and+Its+Applications+to+Zero+Knowledge+Proof)

[45] Zeilberger, H.等. BaseFold: Efficient Field-Agnostic Polynomial Commitment Schemes from Foldable Codes. **ePrint 2023** [Google Scholar](https://scholar.google.com/scholar?q=BaseFold+Efficient+Field-Agnostic+Polynomial+Commitment+Schemes+from+Foldable+Codes)

[37] Setty, S. Spartan: Efficient and General-Purpose zkSNARKs without Trusted Setup. **CRYPTO 2020** [Google Scholar](https://scholar.google.com/scholar?q=Spartan+Efficient+and+General-Purpose+zkSNARKs+without+Trusted+Setup)


## 关键词

+ 域无关SNARK扩展累积码
+ 透明设置后量子SNARK纠错码
+ ECDSA验证域无关证明系统
+ Brakedown框架多项式承诺推广
+ 常数比率常数距离任意有限域