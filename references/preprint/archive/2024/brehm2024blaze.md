---
title: "Blaze: Fast SNARKs from Interleaved RAA Codes"
标题简称:
论文类型: preprint
预印本简称: archive
发表年份: 2024

modified: 2025-04-10 16:59:33
---

## Blaze: Fast SNARKs from Interleaved RAA Codes

## 发表信息

+ [archive](https://eprint.iacr.org/2024/1609)

## 作者

+ Martijn Brehm
+ [Binyi Chen](Binyi%20Chen.md)
+ [Ben Fisch](Ben%20Fisch.md)
+ Nicolas Resch
+ Ron D. Rothblum
+ [Hadas Zeilberger](Hadas%20Zeilberger.md)

## 笔记

### 背景与动机
现代密码学证明系统的发展使得证明者能够向高效验证者证明复杂计算的正确性。多项式承诺方案（PCS）是实现这类系统的核心组件，其中多线性多项式承诺方案（MLPCS）近年来受到广泛关注，被用于GKR、Spartan、Hyperplonk、Lasso/Jolt等高效证明系统 [44, 67, 31, 5, 69]。二进制扩域上的方案尤其吸引人，因为此类域与计算机硬件高度兼容，例如加法对应XOR操作，Intel处理器原生支持某些二进制域的乘法，避免了素数域中常见的嵌入开销 [39, 40]。然而，现有MLPCS方案面临证明者时间与证明大小之间的权衡：Brakedown [45] 拥有极快的证明者但证明体积较大；BaseFold [75] 和 FRI-Binius [40] 证明体积小但证明者因使用FFT而较慢。Blaze 旨在填补这一空白，构建一个在二进制扩域上兼具极快证明者（线性时间）和 polylog 级证明大小与验证时间的 MLPCS。

### 相关工作

[2] Ames 等. Ligero: lightweight sublinear arguments without a trusted setup. **Des. Codes Cryptogr. 2023** [Google Scholar](https://scholar.google.com/scholar?q=Ligero+lightweight+sublinear+arguments+without+a+trusted+setup)
> 核心思路：基于 Reed-Solomon 码和 IOPP 的 PCS 构造，验证者时间 $O(\sqrt{n})$。
> 局限与区别：证明大小和验证时间为 $O(\sqrt{n})$，Blaze 通过交错和代码切换将其降低到 polylog。

[45] Golovnev 等. Brakedown: linear-time and field-agnostic SNARKs for R1CS. **Crypto 2023** [Google Scholar](https://scholar.google.com/scholar?q=Brakedown+linear-time+and+field-agnostic+SNARKs+for+R1CS)
> 核心思路：使用 Spielman 码作为基础码，证明者时间线性，但证明大小为 $O(\sqrt{n})$。
> 局限与区别：Blaze 使用 RAA 码和进一步的交错压缩，证明体积更小，且对大规模实例更快。

[75] Zeilberger 等. BaseFold: efficient field-agnostic polynomial commitment schemes from foldable codes. **Crypto 2024** [Google Scholar](https://scholar.google.com/scholar?q=BaseFold+efficient+field-agnostic+polynomial+commitment+schemes+from+foldable+codes)
> 核心思路：利用折叠码（如 Reed-Solomon）和 sumcheck 实现 polylog 证明大小，但编码需 $O(n\log n)$ 时间。
> 局限与区别：Blaze 通过交错将 BaseFold 应用于更小的实例，消除了 FFT 开销，证明者更快。

[40] Diamond & Posen. Polylogarithmic proofs for multilinears over binary towers. **ePrint 2024/504** [Google Scholar](https://scholar.google.com/scholar?q=Polylogarithmic+proofs+for+multilinears+over+binary+towers)
> 核心思路：将 BaseFold 适配到二进制塔域，同样 $O(n\log n)$ 编码时间。
> 局限与区别：Blaze 的 RAA 码编码仅需线性时间（仅 XOR 和置换），远快于 FFT。

[17] Block 等. Field-agnostic SNARKs from expand-accumulate codes. **Crypto 2024** [Google Scholar](https://scholar.google.com/scholar?q=Field-agnostic+SNARKs+from+expand-accumulate+codes)
> 核心思路：使用 Expand-Accumulate 码，编码 $O(n\log n)$，证明大小 $O(\sqrt{n})$。
> 局限与区别：RAA 码比 EA 码有更好的率-距离权衡，编码更快（只有 2 次累加和 2 次置换）。

[74] Xie 等. Orion: Zero Knowledge Proof with Linear Prover Time. **Crypto 2022** [Google Scholar](https://scholar.google.com/scholar?q=Orion+Zero+Knowledge+Proof+with+Linear+Prover+Time)
> 核心思路：在 Brakedown 基础上组合另一个证明系统以降低证明大小，但组合发生在密码学层面，需证明复杂密码操作。
> 局限与区别：Blaze 的组合发生在信息论层面（IOPP），更简洁且避免了密码操作的正确性证明。

[63] Ron-Zewi & Rothblum. Local proofs approaching the witness length. **JACM 2024** [Google Scholar](https://scholar.google.com/scholar?q=Local+proofs+approaching+the+witness+length)
> 核心思路：代码切换技术，通过将任意纠错码与 IOPP 结合构造高效的证明系统。
> 区别：Blaze 将代码切换与交错结合，并专门设计与 RAA 码的 MLIOP。

[7] Bazzi 等. The minimum distance of turbo-like codes. **IEEE Trans. Inf. Theory 2008** [Google Scholar](https://scholar.google.com/scholar?q=The+minimum+distance+of+turbo-like+codes)
> 核心思路：分析 RAA 码的最小距离期望，但未给出显式率-距离权衡。
> 局限：Blaze 提供了更紧的渐进和具体边界，并支持通过测试降低失败概率。

[53] Kliewer 等. New results on the minimum distance of repeat multiple accumulate codes. **Allerton Conf. 2007** [Google Scholar](https://scholar.google.com/scholar?q=New+results+on+the+minimum+distance+of+repeat+multiple+accumulate+codes)
> 核心思路：证明 RAA 码可达到接近 GV 界，但失败概率界不具体。
> 区别：Blaze 结合两种分析思路，给出显式可计算的失败概率界。

### 核心技术与方案

Blaze 的整体框架由两个技术层次构成：第一层是“代码切换”与“交错”的组合，使得任何线性码 C 的 IOPP 可以被“提升”为交错码 $C^t$ 的高效 IOPP（其中 $t$ 是交错参数），编码时间与 C 的编码时间成比例，而证明和验证复杂度则继承自底层小实例的 IOPP。第二层是选择合适的基码——Repeat-Accumulate-Accumulate (RAA) 码，它具有极快的线性时间编码（仅需 XOR 和置换），并拥有接近 GV 界的良好距离。Blaze 进一步将 RAA 码通过比特切片（bit slicing）扩展到二进制扩域 $\mathrm{GF}(2^f)$，从而支持大域密码学应用。

**代码切换与交错提升**：设 $C:\mathbb{F}^k\to\mathbb{F}^n$ 是一个线性码，其距离为 $\lambda$，并假设存在一个适用于 $R_{\mathrm{MLE}}[C]$ 的 IOPP（即验证输入 y 是否为某个消息 m 的编码且 $\widehat{m}(z)=v$）。那么对于任意 $t\in\mathbb{N}$，可以构造交错码 $C^t:\mathbb{F}^{t\times k}\to\mathbb{F}^{t\times n}$，对应关系 $R_{\mathrm{MLE}}[C^t]$ 的 IOPP 具有以下结构：证明者首先将评估点分解为 $z=(z_1,z_2)\in\mathbb{F}^{\log t}\times\mathbb{F}^{\log k}$，并发送函数 $u(i)=\widehat{m_i}(z_2)$，其中 $m_i$ 是消息矩阵的第 i 行。验证者检查 $\widehat{u}(z_1)=v$。然后验证者随机选取 $r\in\mathbb{F}^t$，令 $y_{\mathrm{combo}}=r^T y$（即各行的线性组合）。由于 $C$ 是线性的，$y_{\mathrm{combo}}$ 是 $C$ 的一个码字，其对应的消息为 $m_{\mathrm{combo}}=r^T m$。若证明者伪造了 $\tilde{u}\neq u$，则大概率 $\langle u,r\rangle \neq \langle\tilde{u},r\rangle$，因此验证者可以通过在 $y_{\mathrm{combo}}$ 上运行底层 $C$ 的 IOPP（针对评估点 $z_2$ 和正确值 $\langle\tilde{u},r\rangle$）来捕获作弊。若输入 y 整体远离 $C^t$，则利用线性码的邻近间隙定理（Theorem 3），随机线性组合 $r^T y$ 以高概率远离 $C$，从而底层 IOPP 的可靠性保证拒绝。

**交错提升的复杂度**：底层 IOPP 的参数（如查询复杂度 $q_{\text{inp}}, q_{\text{idx}}, q_{\text{proof}}$，证明通信量 $cc_{\text{oracle}}, cc$，轮数 $\ell$，证明者时间 $T_P$，验证者时间 $T_V$）被保持，额外开销仅为：非 oracle 通信增加 $2t$（发送 u 和 r），证明者时间增加 $O(tn)$（计算 $r^T y$），验证者时间增加 $O(t\cdot q_{\text{inp}})$。通过选取 $t=\Theta(\log n)$，证明者时间主要受限于编码 $C^t$ 的 $O(tn)$，而验证时间和证明大小均为 polylog（底层 IOPP 的 polylog 复杂度）。

**RAA 码及其距离分析**：RAA 码编码一个长度为 $k=n/r$ 的消息，通过以下步骤得到长度为 $n$ 的码字：1) 每个比特重复 $r$ 次；2) 用排列 $\pi_1$ 重排；3) 累积（模 2 前缀和）；4) 用排列 $\pi_2$ 重排；5) 再次累积。编码仅需 $2(kr-1)$ 个 XOR 门。Blaze 给出了新的距离分析（Theorem 4），将期望分析拆分为中间权重小和大两种情况，分别组合推理和来自 Kliewer 等 [53] 的渐进方法，得到显式的失败概率表达式（式 (2)）。对于 $k=2^{22}, r=4$，可达到距离 $\delta=0.19$，失败概率约 $2^{-27.4}$。进一步通过测试（检查所有小重量消息的编码重量）可将失败概率降至 $2^{-41.5}$（$O(k^2)$ 时间）。

**针对 RAA 码的 MLIOP 与 IOPP 编译**：Blaze 首先为包装后的 RAA 码（即 Packed RAA，将 $f$ 个二进制码字打包为 $\mathrm{GF}(2^f)$ 上的码字）设计一个 MLIOP，利用 sumcheck 验证累积步骤，利用 grand product 参数 [68] 验证置换步骤，并利用 BaseFold-FRI IOPP [40,75] “假装”可以访问中间计算阶段的多线性扩展。然后将该 MLIOP 通过 Lemma 1 编译为 IOPP，最终通过 Merkle 哈希和 Fiat-Shamir 转换为非交互式 MLPCS。

**最终方案的复杂度**（Theorem 7）：对于交错包装 RAA 码（交错层数 $t$），IOPP 在近邻参数 $\delta$ 下：证明者时间 $O(tn + n\log n)$，验证者时间 $O((t+\log n)\lambda/\delta)$，证明大小 $O(n)$（oracle）加 $2t+O(\log n)$（非 oracle）。当 $t=\Theta(\log n)$ 时，证明者时间 $O(tn)$，验证者时间 $O(\log n \cdot \lambda/\delta)$。具体地，用 $r=4$ 的 RAA 码，承诺阶段由 $8n$ 次域加法（XOR）和一次 Merkle 树计算主导，评估证明由 $6n$ 次乘法和 $5n$ 次加法主导（这些操作涵盖了多项式求值本身）。

### 核心公式与流程

**[多线性扩展公式]**
$$
\widehat{f}(x) = \sum_{b\in\{0,1\}^m} eq(x,b)\cdot f(b),\quad eq(x,b)=\prod_{i=1}^m (x_i b_i + (1-x_i)(1-b_i))
$$
> 作用：定义多线性多项式，用于将向量编码为多项式并实现后续 sumcheck 和评估。

**[交错提升的关键分解恒等式]**
$$
\widehat{u}(z_1) = \sum_{b_1} eq(b_1,z_1)\cdot \widehat{m_{b_1}}(z_2) = \widehat{m}(z)
$$
> 作用：验证分解 $u(i)=\widehat{m_i}(z_2)$ 的正确性，若证明者篡改 $u$，则随机线性组合会以高概率暴露。

**[邻近间隙定理 (Theorem 3)]**
$$
\Pr_{u\in U}[\Delta(u,V) < \delta - \varepsilon] \leq \frac{1}{\varepsilon |\mathbb{F}|}
$$
> 作用：保证若输入矩阵 $M$ 远离交错码 $C^t$，则随机线性组合 $r^T M$ 以高概率远离 $C$，从而底层 IOPP 的可靠性可以继承。

**[RAA 编码生成矩阵]**
$$
\mathrm{RAA}_{\pi_1,\pi_2}(x) = A\cdot M_{\pi_2}\cdot A \cdot M_{\pi_1}\cdot F_r \cdot x
$$
其中 $A$ 为累积矩阵（下三角全1），$M_\pi$ 为置换矩阵，$F_r$ 为重复矩阵。
> 作用：明确 RAA 编码的线性代数表示，为距离分析和 IOPP 构造提供基础。

**[交错提升 IOPP (Lemma 2) 的参数变换]**
- 非 oracle 通信：$cc + 2t$
- 证明者时间：$O(tn) + T_P(\delta',k)$
- 验证者时间：$O(t\cdot q_{\text{inp}}(\delta',k)) + T_V(\delta',k)$
- 可靠性误差：$\epsilon + \frac{1}{(\delta - \delta')|\mathbb{F}|}$
> 作用：量化交错提升带来的额外开销，其中 $t$ 是交错参数，$k$ 和 $n$ 是底层码的消息长度和块长度。

### 实验结果

Blaze 与 Brakedown [45]、BaseFold [75]、ZeromorphFRI [55] 在二进制扩域上进行了比较。实验硬件未在论文中详细说明（仅提到在“标准笔记本电脑”上运行）。对于消息大小 $k=2^{25}$ 及更大的多线性多项式，Blaze 的证明者时间快于 BaseFold 和 ZeromorphFRI，与 Brakedown 相当，但证明体积比 Brakedown 小约 10 倍（具体数据：对于 $k=2^{22}, r=4$，Blaze 证明大小约 1.5 MB，而 Brakedown 约 15 MB；BaseFold 约 500 KB）。验证者时间与 BaseFold 和 ZeromorphFRI 接近（毫秒级），而 Brakedown 验证需要 $O(\sqrt{n})$ 时间（约百毫秒级）。Blaze 特别适合大规模实例（$k\ge 2^{25}$），因为此时 RAA 码的编码优势（线性时间，仅 XOR 和置换）超过 BaseFold 等所需的 FFT 开销；但对于小规模实例（$k<2^{20}$），由于 RAA 码的失败概率较高且交错增益不明显，Brakedown 或 BaseFold 可能更优。

### 局限性与开放问题

RAA 码的参数生成过程是一次性随机化过程，存在一定的失败概率（即使通过测试也无法完全消除）。尽管概率极低（如 $2^{-27.4}$），但在需要严格安全保障的场景中，缺乏高效的确定性“认证”算法来保证距离确实足够大，这是一个开放问题。此外，Blaze 目前仅适用于二进制扩域，对于素数域的扩展尚未解决；论文提到可能遵循 Block 等 [17] 的方法，但未实现。对于小消息规模（$< 2^{20}$），Blaze 的证明体积相对较大，不如 BaseFold 紧凑，因此该方案更适合大型多项式场景。

### 强关联论文

[45] Golovnev, A., Lee, J., Setty, S., Thaler, J., Wahby, R.S. Brakedown: linear-time and field-agnostic SNARKs for R1CS. **Crypto 2023** [Google Scholar](https://scholar.google.com/scholar?q=Brakedown+linear-time+and+field-agnostic+SNARKs+for+R1CS)

[75] Zeilberger, H., Chen, B., Fisch, B. BaseFold: efficient field-agnostic polynomial commitment schemes from foldable codes. **Crypto 2024** [Google Scholar](https://scholar.google.com/scholar?q=BaseFold+efficient+field-agnostic+polynomial+commitment+schemes+from+foldable+codes)

[40] Diamond, B.E., Posen, J. Polylogarithmic proofs for multilinears over binary towers. **ePrint 2024/504** [Google Scholar](https://scholar.google.com/scholar?q=Polylogarithmic+proofs+for+multilinears+over+binary+towers)

[17] Block, A.R., Fang, Z., Katz, J., Thaler, J., Waldner, H., Zhang, Y. Field-agnostic SNARKs from expand-accumulate codes. **Crypto 2024** [Google Scholar](https://scholar.google.com/scholar?q=Field-agnostic+SNARKs+from+expand-accumulate+codes)

[74] Xie, T., Zhang, Y., Song, D. Orion: Zero Knowledge Proof with Linear Prover Time. **Crypto 2022** [Google Scholar](https://scholar.google.com/scholar?q=Orion+Zero+Knowledge+Proof+with+Linear+Prover+Time)

[63] Ron-Zewi, N., Rothblum, R. Local proofs approaching the witness length. **JACM 2024** [Google Scholar](https://scholar.google.com/scholar?q=Local+proofs+approaching+the+witness+length)

[7] Bazzi, L., Mahdian, M., Spielman, D.A. The minimum distance of turbo-like codes. **IEEE Trans. Inf. Theory 2008** [Google Scholar](https://scholar.google.com/scholar?q=The+minimum+distance+of+turbo-like+codes)

[53] Kliewer, J., Zigangirov, K.S., Costello Jr., D.J. New results on the minimum distance of repeat multiple accumulate codes. **Allerton Conf. 2007** [Google Scholar](https://scholar.google.com/scholar?q=New+results+on+the+minimum+distance+of+repeat+multiple+accumulate+codes)

[2] Ames, S., Hazay, C., Ishai, Y., Venkitasubramaniam, M. Ligero: lightweight sublinear arguments without a trusted setup. **Des. Codes Cryptogr. 2023** [Google Scholar](https://scholar.google.com/scholar?q=Ligero+lightweight+sublinear+arguments+without+a+trusted+setup)

[55] Kohrita, T., Towa, P. Zeromorph: zero-knowledge multilinear-evaluation proofs from homomorphic univariate commitments. **ePrint 2023/917** [Google Scholar](https://scholar.google.com/scholar?q=Zeromorph+zero-knowledge+multilinear-evaluation+proofs+from+homomorphic+univariate+commitments)


## 关键词

+ Blaze多线性多项式承诺方案
+ RAA码高效编码SNARK
+ 快速证明者二进制域
+ 代码切换技术IOPP组合
+ 线性时间可编码纠错码