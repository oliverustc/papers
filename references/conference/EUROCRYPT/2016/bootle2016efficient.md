---
title: "Efficient zero-knowledge arguments for arithmetic circuits in the discrete log setting"
doi: 10.1007/978-3-662-49896-5_12
标题简称:
论文类型: conference
会议简称: EUROCRYPT
发表年份: 2016
modified: 2025-05-12 08:49:07
created: 2025-04-08 17:01:54
---
## Efficient zero-knowledge arguments for arithmetic circuits in the discrete log setting

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-662-49896-5_12)

## 作者

+ [Jonathan Bootle](Jonathan%20Bootle.md)
+ Andrea Cerulli
+ Pyrros Chaidos
+ [Jens Groth](Jens%20Groth.md)
+ Christophe Petit

## 笔记

### 背景与动机
零知识论证是密码学核心工具，允许证明者向验证者证明一个陈述为真而不泄露任何额外信息。对于算术电路满足性这一NP完全问题，构建高效的零知识论证具有广泛应用，如认证协议、可验证计算等。现有基于离散对数假设的最高效方案是Groth以线性代数为基础的论证[21]及其变体[36]，它们的通信复杂度均为电路规模的平方根。这种平方根复杂度似乎成为离散对数设定下的一个根本性障碍。本文的目标是突破这一障碍，实现对数通信复杂度的零知识论证，同时保持完全基于离散对数假设的强安全性和良好的计算效率。

### 相关工作

[10] Cramer等. Zero-knowledge proofs for finite field arithmetic. **CRYPTO 1998** [Google Scholar](https://scholar.google.com/scholar?q=Zero-knowledge+proofs+for+finite+field+arithmetic)
> 核心思路：给出了算术电路满足性的线性通信复杂度零知识论证。
> 局限与区别：通信复杂度为O(N)，远高于本文的对数复杂度。

[21] Groth. Linear algebra with sub-linear zero-knowledge arguments. **CRYPTO 2009** [Google Scholar](https://scholar.google.com/scholar?q=Linear+algebra+with+sub-linear+zero-knowledge+arguments)
> 核心思路：基于线性代数构造了7轮、平方根通信复杂度的算术电路论证，是离散对数设定下此前最有效的方案。
> 局限与区别：本文通过避免其黑盒归约到线性代数陈述，将其改进为5轮且计算开销更低，并进一步突破其平方根通信障碍实现对数量级。

[36] Seo. Round-efficient sub-linear zero-knowledge arguments for linear algebra. **PKC 2011** [Google Scholar](https://scholar.google.com/scholar?q=Round-efficient+sub-linear+zero-knowledge+arguments+for+linear+algebra)
> 核心思路：改进了Groth[21]的轮数，将7轮减少至5轮，但计算复杂度显著增加。
> 局限与区别：本文的5轮方案在减少轮数的同时大幅降低了计算成本，且对数版本进一步将通信降至O(log N)。

[2] Bayer等. Efficient zero-knowledge argument for correctness of a shuffle. **EUROCRYPT 2012** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+zero-knowledge+argument+for+correctness+of+a+shuffle)
> 核心思路：给出了洗牌正确性的对数通信复杂度论证。
> 局限与区别：该技术仅适用于特定低深度陈述，不适用于一般NP语言。本文的技术则适用于任意算术电路。

[13] Gennaro等. Quadratic span programs and succinct NIZKs without PCPs. **EUROCRYPT 2013** [Google Scholar](https://scholar.google.com/scholar?q=Quadratic+span+programs+and+succinct+NIZKs+without+PCPs)
> 核心思路：引入二次算术程序（QAP）实现非交互简洁论证，也消除了加法门。
> 局限与区别：其安全性依赖配对假设和不可伪造知识提取假设，而本文仅依赖离散对数假设。

[34] Parno等. Pinocchio: nearly practical verifiable computation. **IEEE S&P 2013** [Google Scholar](https://scholar.google.com/scholar?q=Pinocchio+nearly+practical+verifiable+computation)
> 核心思路：基于QAP构建了实际的可验证计算系统，验证速度可快于本地计算。
> 局限与区别：依赖强假设（知识指数假设），本文虽验证较慢但在证明者计算和假设强度上更有优势。

### 核心技术与方案

本文的核心思想是将算术电路满足性问题约化成一个内积关系，然后利用一个递归构造的内积论证以对数通信复杂度证明该关系。整个方案可分为三个层次：电路约化、多项式承诺协议和内积论证。

**第一层：电路约化。** 将任意算术电路（假设已预处理使输入/输出线只关联乘法门）表示为一组矩阵方程。设乘法门总数为 $N = mn$，将其输入输出排列成三个 $m \times n$ 矩阵 $A, B, C$，满足 $A \circ B = C$（Hadamard乘积）。电路的线性约束（包括加法门、常数乘法门和线连接）可写成 $Q$ 个线性方程，形式为 $\sum_i \boldsymbol{a}_i \cdot \boldsymbol{w}_{q,a,i} + \sum_i \boldsymbol{b}_i \cdot \boldsymbol{w}_{q,b,i} + \sum_i \boldsymbol{c}_i \cdot \boldsymbol{w}_{q,c,i} = K_q$。利用两个形式变量 $Y$ 和 $X$，可将所有 $N+Q$ 个方程压缩为一个Laurent多项式 $t(X)$，其常数项为零当且仅当电路可满足。关键构造是定义向量多项式 $\boldsymbol{r}(X) = \sum_i \boldsymbol{a}_i y^i X^i + \sum_i \boldsymbol{b}_i X^{-i} + X^m \sum_i \boldsymbol{c}_i X^i + \boldsymbol{d} X^{2m+1}$ 和 $\boldsymbol{s}(X)$（可由公开电路信息计算），然后令 $\boldsymbol{r}'(X) = \boldsymbol{r}(X) \circ \boldsymbol{y}' + 2\boldsymbol{s}(X)$，最终 $t(X) = \boldsymbol{r}(X) \cdot \boldsymbol{r}'(X) - 2K$。该多项式的常数项恰好是电路满足性判断表达式，因此电路满足当且仅当常数项为0。

**第二层：多项式承诺协议。** 用于证明 $t(X)$ 在随机点 $x$ 的取值 $v$ 与承诺一致，且隐藏多项式系数。协议包括PolyCommit、PolyEval和PolyVerify。核心技巧是将多项式系数排列为 $m \times n$ 矩阵，用 $m$ 个Pedersen多承诺承诺各行，并添加盲化行向量隐藏列加权和。验证时，验证者利用同态性计算 $\prod_i T_i^{x^{in}}$ 得到承诺的行加权和，打开这 $n$ 个元素即可计算 $t(x)$。该协议通信为 $O(m+n)$ 个群/域元素，设置 $m \approx n$ 可得 $\tilde{O}(\sqrt{\deg t})$ 通信。协议具有 $(m_1+m_2)n+1$-特殊可靠性，可在(多项式维度+1)个接受揭示中提取出多项式。

**第三层：递归内积论证。** 这是突破平方根障碍的关键。考虑内积关系 $A = \boldsymbol{g}^{\boldsymbol{a}}, B = \boldsymbol{h}^{\boldsymbol{b}}, \boldsymbol{a}\cdot\boldsymbol{b} = z$，其中 $\boldsymbol{g}, \boldsymbol{h} \in \mathbb{G}^n$，$\boldsymbol{a}, \boldsymbol{b} \in \mathbb{Z}_p^n$。递归减少的思路是将向量分为 $m$ 块，证明者先发送“对角线”承诺 $A_k = \prod_i \boldsymbol{g}_i^{\boldsymbol{a}_{i+k}}$ 和 $B_k$ 以及内积值 $z_k$，接收挑战 $x$ 后，双方计算压缩的承诺 $A' = \prod_k A_k^{x^k} = (\prod_i \boldsymbol{g}_i^{x^{-i}})^{\boldsymbol{a}'}$，其中 $\boldsymbol{a}' = \sum_i \boldsymbol{a}_i x^i$，压缩长度至 $n/m$。递归应用此步骤 $\mu$ 次后，向量长度缩至常数，证明者直接揭示。该协议通信为 $O(\sum (m_i-1))$ 群元素和 $O(m_1)$ 域元素。选择 $m_i=2$ 时，通信为 $O(\log n)$。安全证明基于分叉引理：从 $(2m_\mu-1)\cdots(2m_2-1)$ 个接受对话中可提取合法 $\boldsymbol{a}, \boldsymbol{b}$，该数是 $O(n^2)$ 多项式量级。

**系统集成与复杂度。** 将上述三层结合：证明者先发送线向量承诺 $A_i, B_i, C_i, D$，接收挑战 $y$；计算 $t(X)$ 并用PolyCommit承诺，接收挑战 $x$；计算 $\boldsymbol{r} = \boldsymbol{r}(x)$ 和 $\rho$；若 $\mu=0$ 则直接发送 $(\text{pe}, \boldsymbol{r}, \rho)$，验证者检查 $\text{Com}_{ck}(\boldsymbol{r};\rho)$ 等于相关承诺的幂积，并验证 $v = \boldsymbol{r}\cdot\boldsymbol{r}' - 2K$。若 $\mu>0$，则验证者利用同态性计算 $\boldsymbol{g}^{\boldsymbol{r}}$ 和 $\boldsymbol{h}^{\boldsymbol{r}'}$，然后双方运行内积论证。最终系统在 $\mu=0$ 时得平方根通信（约 $2\sqrt{N}$ 群元素和 $2\sqrt{N}$ 域元素），在$\mu = \log N - 1$ 且 $m_i=2$ 时得对数通信（$4\log N+7$ 群元素和 $2\log N+6$ 域元素）。证明者计算为 $12N$ 次群指数，验证者为 $4N$ 次群指数，均为线性。

### 核心公式与流程

**[电路满足性判据]**
$$
\begin{aligned}
&\sum_{i=1}^m \boldsymbol{a}_i \cdot (\boldsymbol{b}_i \circ \boldsymbol{Y}') Y^i + \sum_{i=1}^m \boldsymbol{a}_i \cdot \boldsymbol{w}_{a,i}(Y) \\
&+ \sum_{i=1}^m \boldsymbol{b}_i \cdot \boldsymbol{w}_{b,i}(Y) + \sum_{i=1}^m \boldsymbol{c}_i \cdot \boldsymbol{w}_{c,i}(Y) - K(Y) = 0
\end{aligned}
$$
> 作用：将电路乘法门和线性约束统一为一个关于变量 $Y$ 的多项式方程，评估于随机 $y$ 可验证。

**[多项式承诺的验证方程]**
$$
\operatorname{Com}_{ck}(\bar{\boldsymbol{t}}; \bar{\tau}) = \left(\prod_{i=0}^{m_1-1} (T_i')^{x^{(i-m_1)n}}\right) \left(\prod_{i=0}^{m_2-1} (T_i'')^{x^{in+1}}\right) U^{x^2}
$$
> 作用：验证者检查打开值 $\bar{\boldsymbol{t}}$ 与承诺 $T_i', T_i'', U$ 在点 $x$ 的一致性。

**[内积递归的核心等式]**
$$
\boldsymbol{g}' = \prod_{i=1}^m \boldsymbol{g}_i^{x^{-i}}, \quad A' = \prod_{k=1-m}^{m-1} A_k^{x^k}, \quad \boldsymbol{a}' = \sum_{i=1}^m \boldsymbol{a}_i x^i
$$
> 作用：给定挑战 $x$，证明者和验证者共同计算压缩后的承诺和压缩后的向量，将长度 $n$ 的内积约化到长度 $n/m$。

### 实验结果

实验在Intel i5-4690K平台上进行，Python实现，使用NumPy、Petlib（OpenSSL椭圆曲线操作封装）和NTL（多项式乘法）。电路描述采用Pinocchio[34]格式，预处理后转换为乘法门和线性约束表。对比基线的Pinocchio使用配对设定和知识指数假设。对于包含347K乘法门的矩阵乘法电路，本文平方根版本的证明时间为14.7秒（Pinocchio为167.4秒），快约11倍；对数版本证明时间为49.9秒，仍快约3.4倍。对于包含1400K乘法门的最短路径电路，平方根版证明时间35.1秒（Pinocchio 523.3秒），快约15倍。在证明者计算方面，本文在所有测试电路上均大幅优于Pinocchio，尤其在含大量乘法门的电路上优势明显。然而验证时间远逊于Pinocchio（Pinocchio可快过本地执行），本文验证时间为线性，且平方根版通信为数十KB，对数版为数KB，均大于Pinocchio的288字节。密钥生成方面，本文密钥大小与电路规模相关的平方根或对数关系，且不特定于电路，可跨电路复用，而Pinocchio密钥大小8N且电路特定。

### 局限性与开放问题

本文验证者计算仍为线性（O(N)次群指数），与Pinocchio等可子线性验证的方案有本质差距。通信虽达到对数级但仍非恒定，平方根版本在超大规模电路下仍显臃肿。安全性仅针对公开随机串模型（SHVZK），实际应用中需额外转换以抵御恶意验证者。开放问题包括：能否在离散对数假设下实现常数或亚线性通信与验证的平衡，以及如何将递归内积技术推广到更一般的代数关系。

### 强关联论文

[21] Groth. Linear algebra with sub-linear zero-knowledge arguments. **CRYPTO 2009** [Google Scholar](https://scholar.google.com/scholar?q=Linear+algebra+with+sub-linear+zero-knowledge+arguments)

[36] Seo. Round-efficient sub-linear zero-knowledge arguments for linear algebra. **PKC 2011** [Google Scholar](https://scholar.google.com/scholar?q=Round-efficient+sub-linear+zero-knowledge+arguments+for+linear+algebra)

[10] Cramer et al. Zero-knowledge proofs for finite field arithmetic. **CRYPTO 1998** [Google Scholar](https://scholar.google.com/scholar?q=Zero-knowledge+proofs+for+finite+field+arithmetic)

[13] Gennaro et al. Quadratic span programs and succinct NIZKs without PCPs. **EUROCRYPT 2013** [Google Scholar](https://scholar.google.com/scholar?q=Quadratic+span+programs+and+succinct+NIZKs+without+PCPs)

[34] Parno et al. Pinocchio: nearly practical verifiable computation. **IEEE S&P 2013** [Google Scholar](https://scholar.google.com/scholar?q=Pinocchio+nearly+practical+verifiable+computation)

[2] Bayer et al. Efficient zero-knowledge argument for correctness of a shuffle. **EUROCRYPT 2012** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+zero-knowledge+argument+for+correctness+of+a+shuffle)


## 关键词

+ 零知识论证
+ 算术电路可满足性
+ 离散对数假设
+ 内积论证
+ 对数通信复杂度