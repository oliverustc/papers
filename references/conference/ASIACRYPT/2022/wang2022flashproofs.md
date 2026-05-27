---
title: "Flashproofs: Efficient zero-knowledge arguments of range and polynomial evaluation with transparent setup"
doi: 10.1007/978-3-031-22966-4_8
标题简称:
论文类型: conference
会议简称: ASIACRYPT
发表年份: 2022
modified: 2025-04-16 17:36:37
created: 2025-04-11 11:58:26
---
## Flashproofs: Efficient zero-knowledge arguments of range and polynomial evaluation with transparent setup

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-22966-4_8)

## 作者

+ [Nan Wang](Nan%20Wang.md) 
+ [Sid Chi-Kin Chau](Sid%20Chi-Kin%20Chau.md)
## 笔记

### 背景与动机
零知识证明是现代密码学应用（如机密交易、签名方案）的核心组件，允许证明者在不泄露秘密信息的情况下说服验证者一个论断的真实性。然而，通用构造在特定语言（如区间证明和多项式求值证明）上往往难以达到最佳效率，因此需要针对性的专用构造。在离散对数设定下，现有的区间证明方案存在三个主要瓶颈：需要可信设置的方案（如 zkSNARK [28]）会留下后门，有损去中心化安全；实现透明设置的方案（如 Bulletproofs [13]）则面临开销不平衡的问题，要么计算昂贵（线性次群指数运算），要么通信开销大（zkSTARK [5] 的证明大小约 45KB）；基于有界整数承诺的方案（如 CKLR21 [20]）需要在范围大小和可靠性误差之间进行权衡，难以在确保可忽略错误的同时适用于大范围。对于多项式求值证明，Bayer & Groth (BG13) [3] 的方案在 DL 设定下实现了对数的通信效率，但对于高阶多项式，其计算和通信开销仍然较高。本文旨在填补这些空白，提出一种在 DL 设定下具有透明设置、且在计算和通信之间实现更优平衡的区间论证和多项式评估论证方案。

### 相关工作

[13] Bünz B. et al. Bulletproofs: Short Proofs for Confidential Transactions and More. **IEEE S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Bulletproofs+Short+Proofs+for+Confidential+Transactions+and+More)
> 核心思路：基于内积论证实现对数级通信的通用范围证明，透明设置。
> 局限与区别：证明方和验证方均需要线性次群指数运算，计算开销大。本文通过矩阵折叠和二次项抵消技术，将验证计算量降至 O(N^{2/3})，显著提升了计算效率。

[3] Bayer S. & Groth J. Zero-Knowledge Argument for Polynomial Evaluation with Application to Blacklists. **EUROCRYPT 2013** [Google Scholar](https://scholar.google.com/scholar?q=Zero-Knowledge+Argument+for+Polynomial+Evaluation+with+Application+to+Blacklists)
> 核心思路：提出基于 DL 的对数通信多项式求值论证，用于成员/非成员证明。
> 局限与区别：证明过程中的群指数运算和通信开销与 log D 线性相关。本文通过新的方程和重压缩技术，将通信和验证计算量分别降至 O(√log D) 和 O(log D + √log D)，实现了非平凡的效率提升。

[20] Couteau G. et al. Efficient Range Proofs with Transparent Setup from Bounded Integer Commitments. **EUROCRYPT 2021** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+Range+Proofs+with+Transparent+Setup+from+Bounded+Integer+Commitments)
> 核心思路：基于 Legendre 三平方定理和有界整数承诺实现常数效率的区间证明。
> 局限与区别：在给定群下，范围大小与可靠性误差之间存在内在权衡。对于大范围或需要可忽略误差的场景，必须增加迭代次数或使用大的类群，这会增加开销。本文的方案在同等可靠性水平下，计算和通信效率更高，且无此权衡。

[28] Groth J. On the Size of Pairing-Based Non-Interactive Arguments. **EUROCRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=On+the+Size+of+Pairing-Based+Non-Interactive+Arguments)
> 核心思路：提出常数验证大小的 zkSNARK，含可信设置。
> 局限与区别：需要可信设置，这与去中心化应用的原则相悖。本文的方案是透明设置的，无需任何信任假设。

[5] Ben-Sasson E. et al. Scalable, Transparent, and Post-Quantum Secure Computational Integrity. **IACR Cryptol. ePrint Arch. 2018** [Google Scholar](https://scholar.google.com/scholar?q=Scalable+Transparent+and+Post-Quantum+Secure+Computational+Integrity)
> 核心思路：基于哈希的透明设置 zkSTARK，具有多对数验证效率。
> 局限与区别：证明大小较大（~45KB），通信成本高。本文的区间证明在典型场景下（如32位、64位）的证明大小更低（738B、994B）。

[14] Bünz B. et al. Transparent SNARKs from DARK Compilers. **EUROCRYPT 2020** [Google Scholar](https://scholar.google.com/scholar?q=Transparent+SNARKs+from+DARK+Compilers)
> 核心思路：基于类群假设实现透明的对数效率 SNARK。
> 局限与区别：依赖类群假00设，其群大小远大于椭圆曲线群，安全强度和效率在实用中不如 DL 设定下的方案。本文基于标准的 256 位椭圆曲线，更易部署。

[7] Ben-Sasson E. et al. Succinct Non-Interactive Zero Knowledge for a von Neumann Architecture. **USENIX Security 2014** [Google Scholar](https://scholar.google.com/scholar?q=Succinct+Non-Interactive+Zero+Knowledge+for+a+von+Neumann+Architecture)
> 核心思路：提出通用 zkSNARK，含可信设置。
> 局限与区别：需要可信设置，验证 Gas 成本较高（约 773K）。本文的区间证明 Gas 成本更低，且无需可信设置。

### 核心技术与方案
本文提出了 Flashproofs，包含区间论证和多项式评估论证两个核心模块，均为在 DL 设定下具有透明设置的三轮交互式协议，支持通过 Fiat-Shamir 启发式转换为非交互式。安全性基于离散对数假设，满足完美完备性、计算可靠性（通过见证扩展仿真证明）和完美特殊诚实验证者零知识。

**区间论证** 采用位分解的变体。给定一个承诺值 $y$ 在范围 $[0, 2^N-1]$ 内，证明方将 $y$ 的二进制表示展开为 $L \times K$ 矩阵，其中元素 $w_{lK+k} = 2^{lK+k}b_{lK+k}$，$b$ 为比特。核心创新在于一种二次项抵消技术：证明方为每行 $l$ 计算 $v_l = \sum_{k=0}^{K-1} w_{lK+k} e_k + r_l$（$e_k$ 为验证方提供的挑战，$r_l$ 为随机盲化因子）。验证方通过计算 $f_l = \sum_{k=0}^{K-1} 2^{lK+k} e_k - v_l$ 并检验 $f_l \cdot v_l$ 的特定结构，使得形如 $w_{lK+k}(2^{lK+k} - w_{lK+k})e_k^2$ 的二次项消失，从而以一定概率迫使 $w_{lK+k} \in \{0, 2^{lK+k}\}$（即 $b$ 为比特）。该技术消除了证明方中不必要的约束，将计算量从线性降至 $O(L + K^2)$。通过优化挑战生成方式（例如令 $e_0 = e^{-1}, e_1 = e, e_2 = e^4$ 等），可将多项式的项数从 $O(K^2)$ 进一步合并为 $O(F(K))$（$F(K)$ 见论文），提升 25.9% 的证明效率（K=4 时）。该协议的总通信复杂度为 $O(N^{2/3})$，验证方计算量为 $O(N^{2/3})$ 个群指数运算，证明方计算量略低于线性（$O(N^{4/3})$ 未经优化，优化后为线性的常倍数）。此外，该协议支持聚合：对于 $M$ 个参数，通信和验证开销为 $O((MN)^{2/3})$ 每个参数。

**多项式评估论证** 基于 BG13 [3] 框架，旨在证明两个承诺值 $x, y$ 满足 $y = P(x; D)$。正文提供两个协议：
1.  **低度协议（LD，适用于 $D \in [3, 2^9]$）**：引入新方程 $z_j^2 - z_{j+1}e = (2x^{2^j}m_j - m_{j+1})e + m_j^2$，其中 $z_j = x^{2^j}e + m_j$（$m_j$ 为随机盲化元素）。该方程同时验证了 $x^{2^j}$ 与 $z_j$ 的线性关系以及 $x^{2^j}$ 与 $x^{2^{j+1}}$ 的二次关系，将 BG13 中需要的两个群元素和一个域元素合并为仅一个群元素和一个域元素，显著减少通信和计算。证明方计算量为 $4\log D + 2$ 个群指数，验证方为 $2\log D + 7$ 个，通信为 $\log D + 3$ 个群元素和 $\log D + 3$ 个域元素。
2.  **高度协议（HD，适用于 $D > 2^9$）**：在低度协议基础上，进一步优化系数 $\sum_{j=0}^{J} w_j e^j$ 的承诺方式。通过将其分解为 $L \times K$ 矩阵（$J+1 = L \cdot K$），使用向量承诺承诺每个列，并引入盲化因子 $\theta_l$ 后计算 $f_l$。验证方利用 $\prod_{l=0}^{L-1} g_l^{f_l} \cdot h^s \stackrel{?}{=} \prod_{k=0}^{K-1} c_{w_k}^{e^k}$ 检查其正确性，从而将 log $D$ 个群元素替换为 $3\sqrt{\log D}$ 个，将计算量从 $O(\log D)$ 降至 $O(\log D + \sqrt{\log D})$。证明方计算量为 $3\log D + 3\sqrt{\log D} + 2$ 个群指数，验证方为 $\log D + 3\sqrt{\log D} + 6$ 个，通信为 $2\sqrt{\log D} + 3$ 个群元素和 $\log D + \sqrt{\log D} + 4$ 个域元素。两个协议均支持聚合，当聚合 $M$ 个参数时，每个参数的开销可渐近地降至 $O(\sqrt{\log D})$。

**安全性论证** 基于 DL 假设，通过构造仿真器证明完美 SHVZK（模拟器能在给定挑战下随机选择承诺和域元素，完美匹配真实分布）。可靠性通过构造见证提取仿真器证明：仿真器重放证明方获取 $T$ 个诚实转录（$T$ 取决于协议参数，如区间论证为 $K^2+K+2$ 个），然后利用线性代数（Vandermonde 矩阵求逆）从挑战向量和响应中提取所有承诺的秘密值（如 $w_{lK+k}, y, x$），从而确保即使恶证明方能生成接受转录，系统也能提取出有效的见证。

### 核心公式与流程

**[区间论证的核心验证方程]**
$$f_l \cdot v_l \stackrel{?}{=} \sum_{k=0}^{K-1} \underbrace{w_{lK+k}(2^{lK+k} - w_{lK+k})}_{=0 \text{ if } w \in \{0, 2^{lK+k}\}} e_k^2 + \text{交叉项} + \text{线性项} + \text{常数项}$$
> 作用：通过检查 $f_l \cdot v_l$ 中不存在 $e_k^2$ 项来强制每个元素属于 $\{0, 2^{lK+k}\}$。前提是证明方在挑战前承诺了所有交叉项和线性项的系数。

**[多项式评估低度协议的核心方程]**
$$z_j^2 - z_{j+1} e \stackrel{?}{=} (2x^{2^j}m_j - m_{j+1})e + m_j^2, \quad j \in \{0, \ldots, J-1\}$$
$$z_0 \stackrel{?}{=} x e + m_0$$
> 作用：第一个方程通过平方项 $z_j^2$ 消除二次项 $e^2$，从而同时验证 $x^{2^j}$ 与 $z_j$ 的线性关系以及 $x^{2^j}$ 与 $x^{2^{j+1}}$ 的二次关系。第二个方程验证输入 $x$ 与 $z_0$ 的线性关系。

**[多项式评估高度协议的验证方程]**
$$\prod_{l=0}^{L-1} g_l^{f_l} \cdot h^{s} \stackrel{?}{=} \prod_{k=0}^{K-1} c_{w_k}^{e^k}$$
$$g^{\zeta} \cdot h^{q} \stackrel{?}{=} c_y^{e^{J+1}} \cdot \prod_{l=0}^{L-1} c_{\theta_l}^{e^{lK}}, \quad \zeta = Q(e; J+1) - \sum_{l=0}^{L-1} f_l e^{lK}$$
> 作用：第一个方程使用向量承诺验证了 $f_l$ 与系数矩阵的正确关系。第二个方程结合前一个，确保 $Q(e; J+1)$ 的系数 $w_j$ 被正确承诺，从而验证 $y$ 是 $e^{J+1}$ 的系数，即 $y = P(x; D)$。

### 实验结果
实验在 Intel Core i7-8700 CPU @3.2GHz 上进行，使用 Java 实现（基于 Bouncy Castle），对区间论证和多项式评估论证的 Gas 成本、运行时间和通信开销进行了评估。对于区间论证，优化后的版本在 64 位范围下，证明时间 111.5 毫秒，验证时间 35.5 毫秒，远优于 Bulletproofs（证明 950.4 毫秒，验证 355.9 毫秒）和 CKLR21（验证 50.8 毫秒，但需多次迭代）。在 Gas 成本方面，我们的 32 位和 64 位区间论证的验证成本分别为 236,584 和 317,474 Gas，与需要可信设置的 zkSNARK (Groth16) 的 220,100 Gas 非常接近，远低于 Bulletproofs（64 位：3,703,549 Gas）。通信开销方面，64 位区间论证的证明大小为 994 字节，显著优于 Bulletproofs 的 674 字节但略高于 CKLR21（827 字节，经三次迭代后）。集合 16 个区间论证时，每论证的平均 Gas 成本可降低 20% 至约 188K（32 位）和 254K（64 位），平均通信开销降至 656 字节。对于多项式评估，与 BG13 相比，我们的低度协议在 $D=511$ 时证明速度提升约 1.8 倍（50 毫秒对 90 毫秒），验证速度提升约 2.6 倍（45 毫秒对 100 毫秒）。高度协议进一步提升了验证速度（35 毫秒对 100 毫秒），且在 $D > 2^9$ 时更具优势。

### 局限性与开放问题
尽管 Flashproofs 在通信和计算之间取得了更优的平衡，但其多项式评估论证继承了 BG13 [3] 的固有局限性：对于只有少量零项的最坏情况多项式，验证所需域乘法的数量与度数呈线性关系，这在高阶多项式时可能成为计算瓶颈。此外，本文的方案聚焦于单变量多项式，对于多变量多项式（如内积）的扩展效率与变量数量线性相关。未来工作可以考虑将目前针对特定语言的高效构造与通用语言的递归证明技术相结合，以实现轻量级、可实际部署的区块链应用（如能源共享 [34, 42]）。

### 强关联论文

[13] Bunz B., Bootle J., Boneh D., Poelstra A., Wuille P., Maxwell G. Bulletproofs: Short Proofs for Confidential Transactions and More. **IEEE S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Bulletproofs+Short+Proofs+for+Confidential+Transactions+and+More)

[3] Bayer S., Groth J. Zero-Knowledge Argument for Polynomial Evaluation with Application to Blacklists. **EUROCRYPT 2013** [Google Scholar](https://scholar.google.com/scholar?q=Zero-Knowledge+Argument+for+Polynomial+Evaluation+with+Application+to+Blacklists)

[20] Couteau G., Klooß M., Lin H., Reichle M. Efficient Range Proofs with Transparent Setup from Bounded Integer Commitments. **EUROCRYPT 2021** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+Range+Proofs+with+Transparent+Setup+from+Bounded+Integer+Commitments)

[28] Groth J. On the Size of Pairing-Based Non-Interactive Arguments. **EUROCRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=On+the+Size+of+Pairing-Based+Non-Interactive+Arguments)

[5] Ben-Sasson E., Bentov I., Horesh Y., Riabzev M. Scalable, Transparent, and Post-Quantum Secure Computational Integrity. **IACR Cryptol. ePrint Arch. 2018** [Google Scholar](https://scholar.google.com/scholar?q=Scalable+Transparent+and+Post-Quantum+Secure+Computational+Integrity)

[10] Bootle J., Cerulli A., Chaidos P., Groth J., Petit C. Efficient Zero-Knowledge Arguments for Arithmetic Circuits in the Discrete Log Setting. **EUROCRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+Zero-Knowledge+Arguments+for+Arithmetic+Circuits+in+the+Discrete+Log+Setting)

[7] Ben-Sasson E., Chiesa A., Tromer E., Virza M. Succinct Non-Interactive Zero Knowledge for a von Neumann Architecture. **USENIX Security 2014** [Google Scholar](https://scholar.google.com/scholar?q=Succinct+Non-Interactive+Zero+Knowledge+for+a+von+Neumann+Architecture)

[14] Bünz B., Fisch B., Szepieniec A. Transparent SNARKs from DARK Compilers. **EUROCRYPT 2020** [Google Scholar](https://scholar.google.com/scholar?q=Transparent+SNARKs+from+DARK+Compilers)


## 关键词

+ 零知识证明
+ 范围证明
+ 多项式求值
+ 透明设置
+ 离散对数
