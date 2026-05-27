---
title: "Brakedown: Linear-Time and Field-Agnostic SNARKs for R1CS"
doi: 10.1007/978-3-031-38545-2_7
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2023
modified: 2025-04-21 10:52:20
created: 2025-04-08 20:57:45
---
## Brakedown: Linear-Time and Field-Agnostic SNARKs for R1CS

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-38545-2_7)

## 作者

+ Alexander Golovnev
+ [Jonathan Lee](Jonathan%20Lee.md)
+ [Srinath Setty](Srinath%20Setty.md)
+ [Justin Thaler](Justin%20Thaler.md)
+ Riad S. Wahby

## 笔记

### 背景与动机
可验证计算是密码学核心问题之一，SNARK 作为其关键原语，能够以亚线性的证明大小和验证开销证明 NP 语句的成立。然而，现有 SNARK 的实际应用受限于证明者的高昂开销（包括渐近复杂度和具体性能），这阻碍了其在大规模 NP 语句（如拥有数百万约束的 R1CS 实例）上的应用。这些开销主要来源于执行大规模快速傅里叶变换、构建庞大的 Merkle 哈希树或进行大规模的多指数运算，前两者通常被视为超线性时间，后者虽然复杂度可观，但基于群操作（相比于域操作）的昂贵性亦非理想。同时，许多实际应用（如基于特定椭圆曲线的密码协议）工作在非 FFT 友好或非离散对数友好的域上，而现有 SNARK 大多要求域具备特定代数结构（如拥有光滑阶的单位根或离散对数难解群），这给工程实现带来了限制。此外，许多高效 SNARK 需要一个复杂的可信设置过程来生成公共参考串，这在实践中是一个重大部署障碍。因此，本文旨在填补一个空白：设计并实现一个无需可信设置、与域无关（field-agnostic）、且拥有真正的线性时间证明者的 SNARK，该 SNARK 能够适用于任意足够大的有限域，其证明大小和验证时间仍保持亚线性。

### 相关工作

[20] Bootle 等. Linear-time zero-knowledge proofs for arithmetic circuit satisfiability. **ASIACRYPT 2017** [Google Scholar](https://scholar.google.com/scholar?q=Linear-time+zero-knowledge+proofs+for+arithmetic+circuit+satisfiability)
> 核心思路：提出首个具有线性时间证明者的交互式论证系统。
> 局限与区别：其安全性建立在特定的格假设上，且未实现具体系统；本文的方案在随机预言机模型中实现，且提供了具体的实现和性能评估。

[21] Bootle, Chiesa, Groth. Linear-time arguments with sublinear verification from tensor codes. **TCC 2020** [Google Scholar](https://scholar.google.com/scholar?q=Linear-time+arguments+with+sublinear+verification+from+tensor+codes)
> 核心思路：构建了一个具有线性时间证明者和亚线性验证者的交互式预言机证明（IOP），并提出了一种通用的多项式承诺方案框架。
> 局限与区别：该工作是理论性的，并未实现具体系统；本文从中提取并具体化了一个线性时间的多项式承诺方案，并针对其所需的线性时间可编码编码进行了优化和实现，最终构建了可运行的SNARK。

[63] Setty. Spartan: efficient and general-purpose zkSNARKs without trusted setup. **CRYPTO 2020** [Google Scholar](https://scholar.google.com/scholar?q=Spartan%3A+efficient+and+general-purpose+zkSNARKs+without+trusted+setup)
> 核心思路：提出了一个无需可信设置的SNARK，其证明者开销主要是一个O(N)大小的多指数运算。
> 局限与区别：Spartan 的证明者依然需要 O(N) 次群操作（多指数运算），而本文的 Brakedown 通过新的线性时间承诺方案，将证明者开销降低到 O(N) 次域操作，避免了昂贵的群运算。

[4] Ames 等. Ligero: lightweight sublinear arguments without a trusted setup. **CCS 2017** [Google Scholar](https://scholar.google.com/scholar?q=Ligero%3A+lightweight+sublinear+arguments+without+a+trusted+setup)
> 核心思路：提出了一个无需可信设置的亚线性论证方案，具有 O(√N) 大小的证明。
> 局限与区别：Ligero 的证明者使用了 Reed-Solomon 码，需要 FFT 操作，因此不是线性时间的，且需要 FFT 友好的域；Brakedown 通过使用线性时间可编码编码避免了 FFT 操作。

[14] Ben-Sasson 等. Aurora: transparent succinct arguments for R1CS. **EUROCRYPT 2019** [Google Scholar](https://scholar.google.com/scholar?q=Aurora%3A+transparent+succinct+arguments+for+R1CS)
> 核心思路：一个透明的（无需可信设置）SNARK，具有 polylog 大小的证明。
> 局限与区别：Aurora 的证明者也需要 FFT 操作，因此不是线性时间的，且其证明大小虽具渐近优势，但本文 Brakedown 的证明者在具体性能上快得多。

### 核心技术与方案

本文提出 Brakedown，一个无需可信设置、与域无关的线性时间 SNARK，它通过将设定于 BCG [21] 的线性时间多项式承诺方案与 Spartan [63] 的线性时间多项式 IOP 相结合而构建。核心技术贡献在于：1) 从 BCG 理论中蒸馏并明确化了一个实用的线性时间多项式承诺方案；2) 设计并实现了一个用于该方案的高效线性时间可编码编码（LTE code）。整个系统分为以下几个层次：

**多项式 IOP：** 源于 Spartan [63]。对于一个给定的 R1CS 实例 (A, B, C, io)，检查其满足性可规约为验证一个等式：0 = sum_{x in {0,1}^s} eq(τ, x) * [A(x)Z(x) * B(x)Z(x) - C(x)Z(x)]。其中 s=log M, A, B, C 是矩阵的多元线性扩展（MLE），Z 是包含证据和公开输入的向量的 MLE。Spartan 使用 sum-check 协议递归地验证此等式，最终将其规约为验证 Z 在随机点 r_y 上的评估值，以及 A, B, C 在随机点 (r_x, r_y) 上的评估值。

**线性时间多项式承诺方案：** 这是应用于本论文中的核心思想，从 BCG [21] 中蒸馏并明确化，以承诺协议中出现的 Z 的 MLE（即证据的 MLE）。该方案针对 t=2 的情况进行了具体描述。其核心流程如下：

-   **承诺阶段：** 证明者将多项式的系数矩阵（即其 Lagrange 基上的评估）看作一个 m×m 矩阵 u。然后对 u 的每一行 u_i 使用线性时间可编码编码函数 Enc 进行编码，得到编码后的矩阵 û= (Enc(u_1), ..., Enc(u_m))。在 IOP 中，承诺即是这个编码矩阵 û；在随机预言机模型中，承诺是 û 的 Merkle 哈希。
-   **测试阶段：** 验证者发送随机挑战向量 r ∈ F^m，证明者返回声称是 u 的各行的随机线性组合 u' = Σ_i r_i * u_i。为了验证 u' 与编码矩阵 û 的一致性，验证者随机选择 ℓ=Θ(λ) 个列索引 j，并确认：Enc(u')_j == Σ_i r_i * û_{i, j}。这保证了每行 û_i 都接近于一个有效的码字，证明了证明者被绑定到了一个特定的多项式 g*。
-   **评估阶段：** 当验证者期望得到多项式的值 g(r) 时，使用 q_1, q_2（使得 g(r) = <q_1⊗q_2, u>）替换测试阶段的向量 r，进行一次相同的交互（使用新的随机列集合 Q'）。若测试均通过，则最终输出 <u'', q_2> 作为 g(r) 的评估值，其中 u'' 是评估阶段证明者返回的线性组合。
-   **可提取性：** 论文通过两种方式证明方案的提取性。第一，如果编码支持高效解码，可以通过对每行进行解码来获得多项式系数。第二，即使编码不支持解码，也可以通过重放测试阶段（Lemma 2 & 3）提取出足够多线性无关的挑战以及对应的正确响应向量，然后通过解线性方程组来恢复出多项式的整个系数矩阵。

**线性时间可编码编码：** 为了实例化承诺方案中的 Enc，本文设计了一种新的线性时间可编码编码。其构造是递归的：对一个消息 x ∈ F^n，其编码 Enc(x) = (x, z, v)。首先，x 是消息本身的系统部分。然后，用一个随机稀疏矩阵 A (n × n/5) 将 x 压缩为 y，再递归地对 y 编码得到 z，最后用一个随机稀疏矩阵 B (n/3 × n/3) 与 z 相乘得到 v。距离分析的核心是表明任何非零消息的编码都具有足够大的 Hamming 权（至少 δn/ρ = n/12），这是通过分析消息的 Hamming 权的大小分三种情况，并利用随机矩阵的高概率性质完成的。论文坚持这种构造是随机的，但随机性在公共参数生成时固定，使得失败概率可以忽略（低于 2^{-100}）。

整个系统的复杂度如下：
-   **证明者计算：** O(N) 次域操作。
-   **验证者计算：** O_λ(N^{1/t}) 次域操作。对于 t=2，即为 O_λ(√N)。
-   **证明大小：** O_λ(N^{1/t})。对于 t=2，即为 O_λ(√N)。
-   **预处理（验证者公共参数）：** O(N) 次域操作。

### 核心公式与流程

**[R1CS 实例定义]**
$$ R_{R1CS} = \{ ((\mathbb F, A, B, C, io, M, N), w) : A z \circ B z = C z, z=(w, 1, io) \} $$
> 作用：定义了 R1CS 关系，即一个 NP 完全问题。

**[Spartan 式多项式 IOP 的核心校验]**
$$ 0 \stackrel{?}{=} \sum_{x \in \{0,1\}^s} \tilde{eq}(\tau, x) \cdot \left[ \left( \sum_{y} \tilde{A}(x,y) \cdot \tilde{Z}(y) \right) \cdot \left( \sum_{y} \tilde{B}(x,y) \cdot \tilde{Z}(y) \right) - \sum_{y} \tilde{C}(x,y) \cdot \tilde{Z}(y) \right] $$
> 作用：将 R1CS 实例的满足性检查规约为一个随机点上的求和检查。

**[线性时间多项式承诺方案 - 一致性测试]**
$$ (Enc(u'))_j \stackrel{?}{=} \sum_{i=1}^m r_i \cdot \hat{u}_{i,j}, \quad \forall j \in Q $$
> 作用：验证证明者返回的随机线性组合 u' 与承诺的编码矩阵 û 是一致的，从而将证明者绑定到一个多项式。

**[知识提取 (无解码)]**
$$ r_1, ..., r_m \in \mathbb{F}^m, \quad u'_1, ..., u'_m \in \mathbb{F}^m $$
$$ u'_i = r_i^T \cdot C \Rightarrow C = (r_1, ..., r_m)^{-1} \cdot (u'_1, ..., u'_m)^T $$
> 作用：通过重放交互，提取 m 个线性无关的挑战和对应的响应，通过高斯消元解出多项式系数矩阵 C。

**[Brakedown 线性时间编码]**
$$ Enc: \mathbb{F}^n \rightarrow \mathbb{F}^{n/\rho}, \quad Enc(x) = (x, z, v) $$
$$ y = x \cdot A, \quad z = Enc(y), \quad v = z \cdot B $$
> 作用：Brakedown 使用的递归编码结构，其中 A 和 B 是随机稀疏矩阵。

### 实验结果

实验在 Azure Standard F16s v2 (16 vCPUs, 32 GB) 和 Azure Standard F64s v2 (64 vCPUs, 128 GB) 虚拟机上运行，使用 BLAKE3 哈希函数。主要基线包括 Ligero [4]、Aurora [14]、Spartan [63]、Fractal [32] 等 SNARK。核心发现如下：

-   在多项式承诺（PC）微基准测试中，Brakedown-PC 的证明者计算（提交和打开）对于大规模多项式（如度 >= 2^25）明显快于 FRI-PC 和 Ligero-PC-1/4，与 Ligero-PC-1/2 相当。其提交时间比 FRI-PC 快 2-9 倍。
-   对于 SNARK 的 1/2-SNARK 形态（证明大小亚线性于陈述），Brakedown 的证明者在所有测试的实例大小（至 2^26 约束）中都是最快的。例如，对于 2^20 约束，Brakedown 的证明时间比 Aurora 快超过一个数量级，比 Ligero 也快很多。
-   在完整 SNARK 形态（验证端也亚线性）下，Brakedown 的证明者仍是最快的。对于 2^20 约束，其证明时间约为 Spartan 和 Xiphos 的 1/2 到 1/3，比 Fractal 快超过一个数量级。
-   Brakedown 的主要不足在于其证明大小较大。在 1/2-SNARK 形, 对于 2^20 约束，Brakedown 证明大小约为 1000 MB，而 Shockwave（使用 Reed-Solomon 码的 Brakedown 变体）和 Ligero-1/2 的证明大小小得多（低 5-15 倍）。但其证明仍然远小于 NP 证据大小（对于 N >= 2^18 约束）。
-   Brakedown 和 Shockwave 的验证者时间与 Spartan 竞争，但比 Fractal 等后量子 SNARK 快一个数量级以上。
-   Brakedown 和 Shockwave 支持在 128 位域上运行，并能达到至少 100 位安全性，且在小域上因域算术更快而获得了更好的具体性能。
-   线性时间编码的公共参数生成时间较快，对于处理 2^20 长度的输入，生成时间约为 700ms。

### 局限性与开放问题

Brakedown 的主要局限性在于其证明大小相对较大（O_λ(√N)），虽然远小于 NP 证据，但显著大于 Fractal (polylog) 等方案。这直接导致了其验证者计算（也是 O_λ(√N)）比许多现有 SNARK 要慢。Shockwave 变体虽然通过使用 Reed-Solomon 码改善了此问题并实现了更快的验证和更小的证明，但它放弃了线性时间证明者和域无关性。本文的方案目前不具备零知识性，这是未来应用的重要障碍。此外，本文采用的线性时间编码是在“可忽略概率失败”的随机化参数下构造的，虽然概率极小，但理论上不是完全确定的。未来的工作应着重于通过递归组合来实现更小的证明（如 Orion 所做），以及更高效地实现零知识性质。

### 强关联论文

[21] Bootle, J., Chiesa, A., Groth, J. Linear-time arguments with sublinear verification from tensor codes. **TCC 2020** [Google Scholar](https://scholar.google.com/scholar?q=Linear-time+arguments+with+sublinear+verification+from+tensor+codes)

[63] Setty, S. Spartan: efficient and general-purpose zkSNARKs without trusted setup. **CRYPTO 2020** [Google Scholar](https://scholar.google.com/scholar?q=Spartan%3A+efficient+and+general-purpose+zkSNARKs+without+trusted+setup)

[4] Ames, S., Hazay, C., Ishai, Y., Venkitasubramaniam, M. Ligero: lightweight sublinear arguments without a trusted setup. **CCS 2017** [Google Scholar](https://scholar.google.com/scholar?q=Ligero%3A+lightweight+sublinear+arguments+without+a+trusted+setup)

[14] Ben-Sasson, E., Chiesa, A., Riabzev, M., Spooner, N., Virza, M., Ward, N.P. Aurora: transparent succinct arguments for R1CS. **EUROCRYPT 2019** [Google Scholar](https://scholar.google.com/scholar?q=Aurora%3A+transparent+succinct+arguments+for+R1CS)

[32] Chiesa, A., Ojha, D., Spooner, N. Fractal: post-quantum and transparent recursive proofs from holography. **EUROCRYPT 2020** [Google Scholar](https://scholar.google.com/scholar?q=Fractal%3A+post-quantum+and+transparent+recursive+proofs+from+holography)

[28] Bünz, B., Fisch, B., Szepieniec, A. Transparent SNARKs from DARK compilers. **EUROCRYPT 2020** [Google Scholar](https://scholar.google.com/scholar?q=Transparent+SNARKs+from+DARK+compilers)

[8] Ben-Sasson, E., Bentov, I., Horesh, Y., Riabzev, M. Fast reed-solomon interactive oracle proofs of proximity. **ICALP 2018** [Google Scholar](https://scholar.google.com/scholar?q=Fast+reed-solomon+interactive+oracle+proofs+of+proximity)

[78] Zhang, J., Xie, T., Zhang, Y., Song, D. Transparent polynomial delegation and its applications to zero knowledge proof. **S&P 2020** [Google Scholar](https://scholar.google.com/scholar?q=Transparent+polynomial+delegation+and+its+applications+to+zero+knowledge+proof)

[20] Bootle, J., Cerulli, A., Ghadafi, E., Groth, J., Hajiabadi, M., Jakobsen, S.K. Linear-time zero-knowledge proofs for arithmetic circuit satisfiability. **ASIACRYPT 2017** [Google Scholar](https://scholar.google.com/scholar?q=Linear-time+zero-knowledge+proofs+for+arithmetic+circuit+satisfiability)

[23] Bootle, J., Chiesa, A., Liu, S. Zero-knowledge succinct arguments with a linear-time prover. **ePrint 2020** [Google Scholar](https://scholar.google.com/scholar?q=Zero-knowledge+succinct+arguments+with+a+linear-time+prover)


## 关键词

+ 零知识论证
+ SNARK
+ 线性时间证明
+ 后量子密码学
+ 多项式承诺