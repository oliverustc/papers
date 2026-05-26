---
title: "Fully dynamic attribute-based signatures for circuits from codes"
标题简称:
论文类型: conference
会议简称: PKC
发表年份: 2024
created: 2025-05-13 05:38:15
modified: 2025-05-13 05:38:53
---

## Fully dynamic attribute-based signatures for circuits from codes

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-57718-5_2)

## 作者

+ San Ling
+ [Khoa Nguyen](Khoa%20Nguyen.md)
+ Duong Hieu Phan
+ Khai Hanh Tang
+ [Huaxiong Wang](Huaxiong%20Wang.md)
+ [Yanhong Xu](Yanhong%20Xu.md)
## 笔记

### 背景与动机
属性签名（ABS）由 Maji 等人于 CT-RSA 2011 提出 [69]，允许用户利用经权威认证的属性匿名签署满足策略的消息，兼具细粒度认证和隐私保护。现有 ABS 研究主要沿三个方向展开：扩展签名策略的表达能力（如支持任意电路 [37,80]）、增加新功能（如可撤销性 [13,46,55,84,85]）、以及丰富计算假设的多样性（目前仅有配对和格基构造，缺乏基于码的方案）。在撤销功能方面，现有方案要么撤销用户身份（这在 ABS 语境下不自然），要么未给出清晰的撤销模型。在防范量子攻击方面，需要后量子假设下的 ABS 方案，但迄今只有基于格的构造 [7,37,46]，而基于码、多变量、同源等其他后量子基础的 ABS 尚未出现。本文旨在同时推进这三个方向：提出首个基于码的 ABS 方案，支持任意布尔电路，并实现属性的全动态性（同时支持动态注册、密钥更新与撤销），且签名尺寸相比格基方案 [37] 减少了一个 $\widetilde{\mathcal O}(\lambda)$ 因子。

---

### 相关工作

[69] Maji 等. Attribute-based signatures. **CT-RSA 2011** [Google Scholar](https://scholar.google.com/scholar?q=Attribute-based+signatures)
> 核心思路：首次形式化定义 ABS，利用双线性配对实现单调访问结构。
> 局限与区别：仅支持单调策略，且无撤销功能；本文基于码假设且支持非单调电路。

[37] El Kaafarani 等. Attribute-based signatures for unbounded circuits in the ROM and efficient instantiations from lattices. **PKC 2018** [Google Scholar](https://scholar.google.com/scholar?q=Attribute-based+signatures+for+unbounded+circuits+in+the+ROM+and+efficient+instantiations+from+lattices)
> 核心思路：首个基于格的后量子 ABS 方案，支持任意电路，签名尺寸 $\widetilde{\mathcal O}(C \cdot \lambda^2 + \lambda^3)$。
> 局限与区别：仅满足 ROM 安全性，不支持动态撤销；本文的方案在 QROM 下安全且签名尺寸更优（$\widetilde{\mathcal O}(C \cdot \lambda + \lambda^2)$），并实现了全动态性。

[75] Nguyen 等. New code-based privacy-preserving cryptographic constructions. **ASIACRYPT 2019** [Google Scholar](https://scholar.google.com/scholar?q=New+code-based+privacy-preserving+cryptographic+constructions)
> 核心思路：提出基于码的可更新 Merkle 树累加器和承诺方案。
> 局限与区别：未给出 ABS 构造；本文直接引入该累加器和承诺方案作为构建模块，并结合新的零知识技术实现 ABS。

[82] Stern. A new identification scheme based on syndrome decoding. **CRYPTO 1993** [Google Scholar](https://scholar.google.com/scholar?q=A+new+identification+scheme+based+on+syndrome+decoding)
> 核心思路：引入基于码的 Σ-协议，使用均匀随机排列和均匀随机掩码向量证明线性方程及权重条件。
> 局限与区别：本文质疑其基本原理，指出均匀随机掩码和排列并非必要，并提出更一般的抽象框架，允许非均匀掩码和非排列函数，从而提升效率。

[56] Libert 等. Signature schemes with efficient protocols and dynamic group signatures from lattice assumptions. **ASIACRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=Signature+schemes+with+efficient+protocols+and+dynamic+group+signatures+from+lattice+assumptions)
> 核心思路：对 Stern 协议进行抽象，将有效证人集合推广为任意子集，允许细粒度的排列族。
> 局限与区别：仍遵循均匀随机排列和均匀随机掩码；本文进一步放松这两点，允许非均匀掩码和非排列函数。

[57] Libert 等. Zero-knowledge arguments for matrix-vector relations and lattice-based group encryption. **Theoretical Computer Science 2019** [Google Scholar](https://scholar.google.com/scholar?q=Zero-knowledge+arguments+for+matrix-vector+relations+and+lattice-based+group+encryption)
> 核心思路：提出处理位乘法（如 $x_3 = x_1 \cdot x_2$）的 Stern 技术，使用扩展向量和排列函数。
> 局限与区别：本文的 NAND 门协议基于该工作但节省了 1/2 的通信开销。

[74] Nguyen 等. Group encryption: full dynamicity, message filtering and code-based instantiation. **PKC 2021** [Google Scholar](https://scholar.google.com/scholar?q=Group+encryption%3A+full+dynamicity%2C+message+filtering+and+code-based+instantiation)
> 核心思路：提出基于码的全动态群加密方案，利用 Merkle 树累加器。
> 局限与区别：方案针对群加密而非 ABS；本文借鉴其 “commit-then-accumulate-then-prove” 框架，并创新使用奇偶重量条件实现高效的活动属性证明。

[86] Tsabary. An equivalence between attribute-based signatures and homomorphic signatures, and new constructions for both. **TCC 2017** [Google Scholar](https://scholar.google.com/scholar?q=An+equivalence+between+attribute-based+signatures+and+homomorphic+signatures%2C+and+new+constructions+for+both)
> 核心思路：证明 ABS 与同态签名的等价性，基于格给出有界深度电路 ABS 方案。
> 局限与区别：电路深度有界，且不支持动态撤销；本文支持任意电路且全动态。

[44] Feng 等. Secure stern signatures in quantum random oracle model. **ISC 2019** [Google Scholar](https://scholar.google.com/scholar?q=Secure+stern+signatures+in+quantum+random+oracle+model)
> 核心思路：利用 Unruh 变换将 Stern 协议转化为 QROM 安全的非交互零知识论证。
> 局限与区别：本文沿用该方法将交互式协议转化为非交互签名，并首次在 ABS 上下文中提供 QROM 安全证明。

---

### 核心技术与方案

**整体框架**：采用 “commit-then-accumulate-then-prove” 方法。权威机构维护一棵 Merkle 树，叶子节点存储对属性 $\mathbf x$ 的承诺 $\mathbf d = \mathbf C_0 \cdot \mathsf{RE}(\mathbf x) \oplus \mathbf C_1 \cdot \mathsf{RE}(\mathbf r)$，其中 $\mathbf r$ 是随机掩码，$\mathsf{RE}$ 是正则编码函数。仅当 $\mathbf d$ 的汉明重量为奇数时才被接受为有效，这为后续的活跃性证明带来便利。签名时，用户证明：（i）$\mathbf d$ 被正确累积到当前根 $\mathbf u_\tau$；（ii）$\mathbf d$ 是对 $\mathbf x$ 的有效承诺且具有奇数重量；（iii）$\mathbf x$ 满足策略 $P$（表示为 NAND 电路）。该论证通过多次运行改进的 Stern 协议并应用 Unruh 变换成为非交互零知识证明（NIZK）。

**各层处理**：

- **累加器层**：利用 Nguyễn 等 [75] 的 Merkle 树累加器，证明等式 $\mathbf M_{\mathsf{acc}} \cdot \mathbf w_{\mathsf{acc}} = \mathbf v_{\mathsf{acc}}$，其中 $\mathbf w_{\mathsf{acc}}$ 包含叶节点承诺和路径节点。通过本文的抽象框架，掩码向量大小从 $2\ell m + 2(\ell-1)n$ 降至 $2\ell m + (\ell-1)n$。
- **承诺层**：证明 $\mathbf d = \mathbf C_0 \cdot \mathsf{RE}(\mathbf x) \oplus \mathbf C_1 \cdot \mathsf{RE}(\mathbf r)$ 且 $\mathbf 1^{\top} \mathbf d = 1$（奇数重量）。利用 $\mathsf{Encode}$ 将 $\mathbf d$ 扩展为 $2n$ 向量，并将奇数重量条件转化为线性方程。掩码向量从 $2n + m_0 + m_1$ 压缩为 $n + (2^c-1)n/c + (2^c-1)k/c$。
- **策略层**：将任意布尔电路转化为 NAND 门网络。对每个 NAND 门 $(x_1,x_2,x_3)$ 满足 $x_1 \cdot x_2 \oplus x_3 = 1$，本文设计编码 $\mathsf{ENC}(x_1,x_2,x_3) \in \{0,1\}^4$ 及函数 $F_{\mathsf{nand}}, F'_{\mathsf{nand}}, F''_{\mathsf{nand}}$。关键创新：$\mathsf{valid}_{\mathsf{nand}} = \mathcal B_{\mathsf{odd}}^4$（奇数重量向量），因此掩码集合 $\mathcal R_{\mathsf{nand}} = \mathcal B_{\mathsf{odd}}^4$，大小为 3 比特（原方案需 4 比特）。利用 $F_{\mathsf{nand}}$ 的“同态”性质，可同时证明 NAND 关系和与电路中其他部分共享的输入比特。

**安全证明**：方案在 QROM 下满足统计隐私和计算不可伪造性，基于 $2\text{-}\mathsf{RNSD}_{n,2n,c}$ 和 $2\text{-}\mathsf{RNSD}_{n,L+k,c}$ 问题的困难性。隐私通过模拟器程序化随机预言机 $\mathcal H_{\mathsf{FS}}$ 生成与真实签名统计不可区分的模拟签名得到。不可伪造性通过将 $\mathcal H_G$ 模拟为高次多项式从而提取有效证人 $\xi$ 来证明。

**复杂度**：签名大小为 $\widetilde{\mathcal O}(C \cdot \lambda + \lambda^2)$，其中 $C$ 为电路规模，$\lambda$ 安全参数。对比格基方案 [37] 的 $\widetilde{\mathcal O}(C \cdot \lambda^2 + \lambda^3)$ 减少了 $\widetilde{\mathcal O}(\lambda)$ 因子。

---

### 核心公式与流程

**[抽象 Stern 协议的核心关系]**
$$
\mathrm{R}_{\text{abstract}} = \left\{((\mathbf M, \mathbf v), \mathbf w) \in \left(\mathbb Z_2^{D_0\times D} \times \mathbb Z_2^{D_0}\right) \times \text{VALID}: \mathbf M \cdot \mathbf w = \mathbf v\right\}
$$
> 作用：将各类零知识证明统一为证明满足线性方程的向量属于有效集合。协议基于集合 VALID、掩码空间 $\mathcal R$、挑战函数 $F,F',F''$ 满足四个条件：同态性、闭合性、均匀性、掩码分布相同性。

**[NAND 门的编码与函数]**
$$
\mathsf{ENC}(x_1,x_2,x_3) = \left[\bar x_1\bar x_2\oplus x_3 \;\mid\; \bar x_1 x_2\oplus x_3 \;\mid\; x_1\bar x_2\oplus x_3 \;\mid\; x_1 x_2\oplus x_3\right]^\top
$$
$$
F_{\mathsf{nand}}((e_1,e_2,e_3), X) = \left[x_{e_1,e_2}\oplus e_3 \;\mid\; x_{e_1,\bar e_2}\oplus e_3 \;\mid\; x_{\bar e_1,e_2}\oplus e_3 \;\mid\; x_{\bar e_1,\bar e_2}\oplus e_3\right]^\top
$$
> 作用：将 NAND 门条件 $x_1\cdot x_2\oplus x_3=1$ 转化为对奇重量向量的线性测试 $[0\,0\,0\,1]\cdot X = 1$。函数 $F_{\mathsf{nand}}$ 是“置换加常数”的混合，用于在证明中隐蔽证人，并通过同态性兼容掩码。

**[掩码空间的优化：以二进制向量证明为例]**
$$
\mathcal R_{\mathsf{bin}} = (\mathcal B_{\mathsf{odd}}^2 \| \dots \| \mathcal B_{\mathsf{odd}}^2) \subset \{0,1\}^{2n}, \quad |\mathcal R_{\mathsf{bin}}| = 2^n
$$
> 作用：相比传统方案用 $\{0,1\}^{2n}$ 作为掩码空间，本文利用每个 $2$-bit 块仅能取奇数重量这一事实，将掩码表示压缩为 $n$ 比特（而非 $2n$ 比特）。类似优化应用于正则字和 NAND 编码。

**[FDABS 方案的提取器]**
$$
\mathcal E_{\mathsf{fdabs}}: \text{输入签名 } \Sigma \text{ 和 } \mathcal H_G = p_G \text{（高次多项式），输出证人 } \xi' = (\mathbf d', \mathbf x', \mathbf r', \mathsf{bin}(j'), \mathbf w'_\ell, \dots, \mathbf w'_1)
$$
> 作用：通过将随机预言机 $\mathcal H_G$ 实例化为可逆多项式，提取出所有三个响应（对应挑战 1,2,3），进而恢复出有效证人，用于不可伪造性证明。

---

### 实验结果

本文未提供具体实验，但通过理论分析和表 1 与已有方案进行对比。下表总结了已知 ABS 方案的特征（基于表 1 原文）：

- 在配对基方案中，Okamoto-Takashima 2011 [76] 支持非单调访问结构，签名尺寸 $\mathcal O(S \cdot \lambda)$；Sakai 等 2016 [80] 支持任意电路，尺寸 $\mathcal O(C \cdot \lambda)$；Sakai 等 2018 [81] 支持图灵机或自动机。
- 格基方案中，Tsabary 2017 [86] 仅支持有界深度电路（$\widetilde{\mathcal O}(D \cdot \lambda)$），El Kaafarani-Katsumata 2018 [37] 支持任意电路但签名尺寸 $\widetilde{\mathcal O}(C \cdot \lambda^2 + \lambda^3)$，且仅在 ROM 下安全。
- 本文方案首次基于码假设，支持任意电路，签名尺寸 $\widetilde{\mathcal O}(C \cdot \lambda + \lambda^2)$，在 QROM 下安全，并实现了全动态性（同时支持注册和撤销）。

由于码基参数通常比格基大得多（例如 $n = \mathcal O(\lambda)$ 而格基中 $n \log q$ 等），实际签名大小估计为数十 MB，仍远非实用。但作为理论贡献，本文在渐进性能上优于格基方案 [37]。

---

### 局限性与开放问题

本文方案在理论效率上取得改进，但实际签名尺寸仍然很大（数十 MB），距离实用尚有距离。主要瓶颈源于码基协议中需要大量的承诺和重复运行以实现可靠零知识（$\kappa = \mathcal O(\lambda)$ 次重复）。此外，本文假设属性空间和策略基于布尔电路，未考虑更高效的访问结构表示（如算术电路或结构化策略）。开放问题包括：设计实用化的后量子 ABS 方案（例如使用更短的证明技术或格/码混合方案）；探索不完全依赖 Unruh 变换的 QROM 安全构造；将全动态性扩展到去中心化或层次化设置中。

---

### 强关联论文

[37] El Kaafarani, A., Katsumata, S. Attribute-based signatures for unbounded circuits in the ROM and efficient instantiations from lattices. **PKC 2018** [Google Scholar](https://scholar.google.com/scholar?q=Attribute-based+signatures+for+unbounded+circuits+in+the+ROM+and+efficient+instantiations+from+lattices)

[69] Maji, H.K., Prabhakaran, M., Rosulek, M. Attribute-based signatures. **CT-RSA 2011** [Google Scholar](https://scholar.google.com/scholar?q=Attribute-based+signatures)

[75] Nguyen, K., Tang, H., Wang, H., Zeng, N. New code-based privacy-preserving cryptographic constructions. **ASIACRYPT 2019** [Google Scholar](https://scholar.google.com/scholar?q=New+code-based+privacy-preserving+cryptographic+constructions)

[82] Stern, J. A new identification scheme based on syndrome decoding. **CRYPTO 1993** [Google Scholar](https://scholar.google.com/scholar?q=A+new+identification+scheme+based+on+syndrome+decoding)

[56] Libert, B., Ling, S., Mouhartem, F., Nguyen, K., Wang, H. Signature schemes with efficient protocols and dynamic group signatures from lattice assumptions. **ASIACRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=Signature+schemes+with+efficient+protocols+and+dynamic+group+signatures+from+lattice+assumptions)

[57] Libert, B., Ling, S., Mouhartem, F., Nguyen, K., Wang, H. Zero-knowledge arguments for matrix-vector relations and lattice-based group encryption. **Theoretical Computer Science 2019** [Google Scholar](https://scholar.google.com/scholar?q=Zero-knowledge+arguments+for+matrix-vector+relations+and+lattice-based+group+encryption)

[74] Nguyen, K., Safavi-Naini, R., Susilo, W., Wang, H., Xu, Y., Zeng, N. Group encryption: full dynamicity, message filtering and code-based instantiation. **PKC 2021** [Google Scholar](https://scholar.google.com/scholar?q=Group+encryption%3A+full+dynamicity%2C+message+filtering+and+code-based+instantiation)

[44] Feng, H., Liu, J., Wu, Q. Secure stern signatures in quantum random oracle model. **ISC 2019** [Google Scholar](https://scholar.google.com/scholar?q=Secure+stern+signatures+in+quantum+random+oracle+model)

[86] Tsabary, R. An equivalence between attribute-based signatures and homomorphic signatures, and new constructions for both. **TCC 2017** [Google Scholar](https://scholar.google.com/scholar?q=An+equivalence+between+attribute-based+signatures+and+homomorphic+signatures%2C+and+new+constructions+for+both)

[80] Sakai, Y., Attrapadung, N., Hanaoka, G. Attribute-based signatures for circuits from bilinear map. **PKC 2016** [Google Scholar](https://scholar.google.com/scholar?q=Attribute-based+signatures+for+circuits+from+bilinear+map)


## 关键词

+ 属性基签名（ABS）
+ 完全动态属性管理
+ 编码假设
+ Stern式零知识协议
+ 后量子签名
+ 隐私保护访问控制