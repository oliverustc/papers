---
title: "Phecda: Post-Quantum Transparent zkSNARKs from Improved Polynomial Commitment and VOLE-in-the-Head with Application in Publicly Verifiable AES"
标题简称:
论文类型: conference
会议简称: S&P
发表年份: 2025
modified: 2025-04-13 14:37:31
---

## Phecda: Post-Quantum Transparent zkSNARKs from Improved Polynomial Commitment and VOLE-in-the-Head with Application in Publicly Verifiable AES

## 发表信息

+ [原文链接](https://www.computer.org/csdl/proceedings-article/sp/2025/223600a055/21B7R1Oem1q)

## 作者

+ Changchang Ding
+ [Yan Huang](Yan%20Huang.md)

## 笔记

### 背景与动机
零知识证明是现代密码学的核心原语，支撑着远程认证、电子投票、加密货币和去中心化金融等关键基础设施。为了满足实际部署需求，非交互式且透明（无需可信设置）的零知识证明系统尤为重要。许多最优的证明系统 [1–5] 均构建在 GKR 协议 [6] 之上，该协议将分层电路计算的正确性转化为指数级减少的多项式约束。这些协议的关键区别在于证明最终多项式约束的方式：Hyrax [2] 使用基于椭圆曲线的同态承诺；Libra [1] 使用随机掩码多项式和椭圆曲线上的可验证多项式委托。但这些方法受限于椭圆曲线，计算开销大且难以支持离散对数假设不成立的域。Virgo [3] 使用 FRI [7] 基于的可验证多项式委托，实现了更快的证明者和透明性。然而，随着 GKR 变换本身已被不断改进 [1, 4, 10, 11]，完成剩余证明的成本在这些协议中日益占据主导地位。以 AES 计算为例，MPCitH 的验证者时间和证明大小分别占 Dubhe [5] 总成本的 95% 和 62%，后者将 GKR 与 MPCitH 结合。因此，解决这些新的性能瓶颈至关重要。Phecda 旨在填补这一空白：通过开发一种专门用于简洁证明 GKR 输入层多线性约束的透明多项式承诺方案，以及一种基于 VOLE-in-the-Head 的高效协议来证明所有线性关系，从而突破现有方案在验证时间、证明大小和可扩展性上的瓶颈，实现优于现有方案的透明 zkSNARK。

### 相关工作

[1] Xie 等. Libra: Succinct Zero-Knowledge Proofs with Optimal Prover Computation. **CRYPTO 2019** [Google Scholar](https://scholar.google.com/scholar?q=Libra%3A+Succinct+Zero-Knowledge+Proofs+with+Optimal+Prover+Computation)
> 核心思路：使用随机掩码多项式和椭圆曲线上的可验证多项式委托来证明 GKR 产生的多项式约束。
> 局限与区别：依赖椭圆曲线，不支持离散对数假设不成立的域，且不是透明的。

[2] Wahby 等. Doubly-Efficient zkSNARKs without Trusted Setup. **IEEE S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Doubly-Efficient+zkSNARKs+without+Trusted+Setup)
> 核心思路：使用基于椭圆曲线的同态承诺来承诺证据并证明多项式约束。
> 局限与区别：与 Libra 类似，受限于椭圆曲线，计算成本高，且不是透明的。

[3] Zhang 等. Transparent Polynomial Delegation and its Applications to Zero Knowledge Proof. **IEEE S&P 2020** [Google Scholar](https://scholar.google.com/scholar?q=Transparent+Polynomial+Delegation+and+its+Applications+to+Zero+Knowledge+Proof)
> 核心思路：利用 FRI（Fast Reed-Solomon Interactive Oracle Proof of Proximity）实现透明的可验证多项式委托（zkVPD），从而处理 GKR 的输入层。
> 局限与区别：Phecda 采用了一种新的 PC 直接处理输入层检查，比 Virgo 的 zkVPD 更具体高效，且 Virgo 不支持二元扩域。

[5] Ding 和 Huang. Dubhe: Succinct Zero-Knowledge Proofs for Standard AES and Related Applications. **USENIX Security 2023** [Google Scholar](https://scholar.google.com/scholar?q=Dubhe%3A+Succinct+Zero-Knowledge+Proofs+for+Standard+AES+and+Related+Applications)
> 核心思路：将 FLPCP 与简化的 MPC-in-the-Head（MPCitH）协议结合，处理所有剩余的多项式约束。
> 局限与区别：Phecda 使用 PC 替换 Dubhe 中的 MPCitH 来验证秘密多项式在公开点的评估，使证明大小与证据长度无关（简洁）；同时使用 VOLEitH 替换 MPCitH，获得了额外的渐进和具体性能优势。

[12] Bootle 等. Gemini: Elastic SNARKs for Diverse Environments. **CRYPTO 2022** [Google Scholar](https://scholar.google.com/scholar?q=Gemini%3A+Elastic+SNARKs+for+Diverse+Environments)
> 核心思路：通过对应的单变量多项式来承诺和证明多线性多项式。
> 局限与区别：Gemini 的场景需要可信设置，使用特定椭圆曲线上的双线性映射。Phecda 基于新的批处理低度测试（LDT），是透明、抗量子的，并支持更广泛的域。

[14] Chen 等. HyperPlonk: Plonk with Linear-Time Prover and High-Degree Custom Gates. **EUROCRYPT 2023** [Google Scholar](https://scholar.google.com/scholar?q=HyperPlonk%3A+Plonk+with+Linear-Time+Prover+and+High-Degree+Custom+Gates)
> 核心思路：与 Gemini 类似，通过单变量多项式承诺多线性多项式。
> 局限与区别：同样依赖于双线性映射和可信设置，而 Phecda 的方法是透明和抗量子的。

[13] Roy. SoftSpokenOT: Quieter OT Extension from Small-Field Silent VOLE in the Minicrypt Model. **CRYPTO 2022** [Google Scholar](https://scholar.google.com/scholar?q=SoftSpokenOT%3A+Quieter+OT+Extension+from+Small-Field+Silent+VOLE+in+the+Minicrypt+Model)
> 核心思路：提出基于GGM树的透明VOLE生成方法。
> 局限与区别：该工作提供了VOLE生成的底层工具。Phecda的VOLEitH ZKP借鉴并扩展了其GGM树技术来构造高效的线性关系证明协议。

[15] Baum 等. Publicly Verifiable Zero-Knowledge and Post-Quantum Signatures from VOLE-in-the-Head. **CRYPTO 2023** [Google Scholar](https://scholar.google.com/scholar?q=Publicly+Verifiable+Zero-Knowledge+and+Post-Quantum+Signatures+from+VOLE-in-the-Head)
> 核心思路：将SoftSpokenOT的VOLE生成与Quicksilver的多项式验证结合，构造后量子签名方案（FAEST）。
> 局限与区别：FAEST侧重于使用复制码证明小域上的小型二次电路（如AES）。Phecda的VOLEitH协议侧重于使用线性MDS码高效证明大域上的线性关系，且协议轮次和检查更少。

[16] Yang 等. Quicksilver: Efficient and Affordable Zero-Knowledge Proofs for Circuits and Polynomials over Any Field. **ACM CCS 2021** [Google Scholar](https://scholar.google.com/scholar?q=Quicksilver%3A+Efficient+and+Affordable+Zero-Knowledge+Proofs+for+Circuits+and+Polynomials+over+Any+Field)
> 核心思路：提出一种利用VOLE承诺来证明任意多项式关系的方法。
> 局限与区别：Phecda的VOLEitH协议在构造上仅专注于线性关系，并在设计上受到了Quicksilver思想的启发，但协议细节和安全性证明是全新的。

### 核心技术与方案

Phecda 的整体框架如图 1 所示，由四个主要模块组成：GKR、FLPCP、多项式承诺（PC）和 VOLE-in-the-Head（VOLEitH）。工作流程是：首先，GKR 协议接收一个验证目标计算的分层电路，并将其正确性转化为一系列等价的约束。这些约束包括：SumCheck 轮次中的线性等式、层间乘法等式、以及在输入层对一个秘密多线性多项式在公开点上的求值。其次，FLPCP 将每个乘法等式进一步转化为一组秘密输入和线性关系。最后，PC 模块和 VOLEitH 模块分别处理最终的多线性多项式求值和线性关系，共同提供零知识性质。

**多项式承诺方案** 的核心思想是利用一个 i-变元多线性多项式 $f_i$ 与其对应的 $2^i$ 次单变量多项式 $\check{f}_i$ 之间的一一对应关系。为了承诺 $f_i$，证明者承诺 $\check{f}_i$，例如使用 Merkle 树。给定一个公开点 $z = (z_0, ..., z_{n-1})$ 和声称的求值 $y$，证明者证明 $f(z) = y$。这通过一系列部分求值得到的多线性多项式 $f_i$ 来实现，其中 $f_i$ 是 $f$ 在前 $n-i$ 个分量上固定后的结果。协议的关键在于，验证者通过检查多个“FFT 类”等式来确保这些 $\check{f}_i$ 的诚实计算。具体而言，协议利用一个特殊的批处理低度测试（mLDT）协议，一次性验证所有 $n$ 个 $\check{f}_i$ 的度数都正确（即不超过 $2^i$），成本与单个 LDT 相当。mLDT 的核心是构造一系列辅助多项式 $g_i$，并通过随机线性组合将它们联系起来，最后在足够多的随机点上验证 $g_i, f_i, g_{i-1}, f_{i-1}$ 之间的 FFT 关系。该方案的安全性依赖于对 $\kappa$ 个随机点上上述等式的检查，声音误差为 $(\frac{1}{\rho} + 3\delta)^\kappa \cdot \epsilon_{\text{mLDT}}(\delta)$，其中 $\rho$ 是 Reed-Solomon 码的速率，$\delta$ 是承诺多项式与码字的最大相对距离。协议的零知识性通过预先在多项式系数中包含 $2\kappa(n+1)$ 个哑元秘密值来保证，这些值在揭示点时会泄露线性信息，但由于哑元的存在，这些信息不会泄露真实证据。

**VOLE-in-the-Head 协议** 允许证明者承诺一个秘密 $X \in \mathbb{F}_p^{\ell \times m}$，并向验证者证明 $\mathbf{A} \circ \mathbf{X} + a = 0$ 成立，其中 $\mathbf{A}$ 和 $a$ 是公开常数，$\circ$ 表示对应元素乘积之和。其核心思想是构造一个分布正确的随机向量不经意线性评估（VOLE）。证明者首先生成 $n$ 棵 GGM 树，每棵有 $N$ 片叶子，种子为 $seed_{j,k}$。从这些种子通过 PRG 派生出值 $t_{i,j,k}$，并计算 $u_{i,j} := \sum_{k=0}^{N-1} t_{i,j,k}$ 和 $v_{i,j} := -\sum_{k=0}^{N-1} s_k t_{i,j,k}$，其中 $\{s_k\}$ 是公开的不同域元素。通过公开的 MDS 编码矩阵 $\mathbf{G}$ 和矩阵 $\mathbf{C}$（用于调整），证明者发送 $\mathbf{C}$ 作为对 $(U,V)$ 的承诺。在在线阶段，证明者首先发送 $X' := X - U_1$，然后证明者通过一系列交互步骤（包括发送哈希值、回应均匀随机挑战 $\alpha$ 和 $\mathbf{d}$，以及打开 GGM 树）来证明线性关系。验证者计算相应的 $\mathbf{Q}$ 矩阵，并最终检查两个关键等式：$\operatorname{Hash}(\alpha\mathbf{Q}_1 + \mathbf{Q}_2 - \mathbf{S}\mathbf{G}\mathbf{D})$ 和 $\operatorname{Hash}(\alpha a + \mathbf{A} \circ (\mathbf{S} + \alpha \mathbf{X}'))$ 是否与证明者先前发送的哈希值匹配。该协议的声音误差为 $1 - (1 - 1/p)(1 - 1/N^\delta)$，其中 $\delta = n - m + 1$ 是 MDS 码的最小距离。协议的知识证明性质通过特殊的声音性（$(\binom{n}{n-\delta+1}+1, N^{n-\delta}+1)$-special sound）保证，即从足够多的接受对话中可提取出证据。

**系统集成** 将 GKR 和 FLPCP 作为编译器，将电路验证转化为线性约束（由 VOLEitH 处理）和一个多线性多项式求值问题（由 PC 处理）。Phecda 的安全性（完备性、知识健壮性、诚实验证者零知识）通过其子协议的安全性的组合得到证明，其知识健壮性误差被限定为 $\epsilon \leq \epsilon_{\text{PC}} + \mathcal{E}_{\text{Compiler}} + \epsilon_{\text{VOLEitH}}$。

**渐进复杂度**：对于门数为 $C$、深度为 $d$、证据长度为 $w$ 的电路，Phecda 的证明者时间为 $O(C + w \log w)$，验证者时间为 $O(d \log C + \log^2 w)$，证明大小为 $O(d \log C + \log^2 w)$。相比 Dubhe 的 $O(d\log C + w)$ 验证者和证明大小，有了显著的渐进改进。在 VOLEitH 模块内部，对于 $I$ 个秘密证据和 $M$ 个线性约束，证明者和验证者时间均为 $O(NI + MI + mN)$，证明大小为 $O(I\log p + m\log N)$，其中 $n=2m$ 为编码参数，$N$ 为安全参数。

### 核心公式与流程

**[GKR 层间关系式 (2)]**
$$
V_{i-1}(t_{i-1}) = \widetilde{\operatorname{add}}_i(r_i, s_i, t_{i-1})\left(\widetilde{V}_i(r_i) + \widetilde{V}_i(s_i)\right) + \widetilde{\operatorname{mul}}_i(r_i, s_i, t_{i-1})\widetilde{V}_i(r_i)\widetilde{V}_i(s_i)
$$
> 作用：将第 $i-1$ 层的输出值 $V_{i-1}(t_{i-1})$ 的正确性，约简为对第 $i$ 层多线性多项式在两个随机点 $r_i, s_i$ 上的求值 $\widetilde{V}_i(r_i), \widetilde{V}_i(s_i)$ 的检查。

**[PC 协议核心验证等式 (4) 和 (5)]**
$$
\check{f}_{i-1}(v) = \frac{\hat{u}\check{f}_i(u) - u\check{f}_i(\hat{u})}{\hat{u} - u} + z_{n-i}\frac{\check{f}_i(u) - \check{f}_i(\hat{u})}{u - \hat{u}}, \quad \forall i \in \{2,...,n\}, j \in [\kappa]
$$
$$
y = \frac{u_j^{(1)}\check{f}_1(\hat{u}_j^{(1)}) - \hat{u}_j^{(1)}\check{f}_1(u_j^{(1)})}{u_j^{(1)} - \hat{u}_j^{(1)}} + z_{n-1}\frac{\check{f}_1(u_j^{(1)}) - \check{f}_1(\hat{u}_j^{(1)})}{u_j^{(1)} - \hat{u}_j^{(1)}}, \quad \forall j \in [\kappa]
$$
> 作用：这两个等式是 PC 协议中 Verifier 检查的核心。它们确保了从第 $i$ 层 ($\check{f}_i$) 推导出第 $i-1$ 层 ($\check{f}_{i-1}$) 的多变量多项式关系在单变量形式下是正确的，本质上是对多线性多项式 $f$ 在点 $z$ 上的求值 $y$ 的递归验证。其中 $u, \hat{u}$ 是共轭点，$v = \text{lift}^{(i)}(u)$。

**[VOLEitH 验证等式 (6) 和 (7)]**
$$
h_{\alpha\mathbf{V}_1 + \mathbf{V}_2} = \operatorname{Hash}(\alpha\mathbf{Q}_1 + \mathbf{Q}_2 - \mathbf{S}\mathbf{G}\mathbf{D})
$$
$$
h_{\mathbf{A} \circ \mathbf{U}_2} = \operatorname{Hash}(\alpha a + \mathbf{A} \circ (\mathbf{S} + \alpha \mathbf{X}'))
$$
> 作用：等式 (6) 验证了证明者构建的两个 VOLE 关系的一致性。等式 (7) 验证了线性约束 $\mathbf{A}\circ\mathbf{X} + a = 0$ 成立。Verifier 通过检查这些哈希值来确信证明者的声明的正确性，而无需直接操作大型矩阵。

**[AES 仿真引理]**
$$
a \star b = c \iff (a \times b \oplus c) \times m^{-1} \in [2^{k+1}]
$$
> 作用：该引理是构建新 AES 验证电路的基础。它将 AES 中定义在 GF$(2^8)$ 小环上的乘法（$\star$，模数 $m$，如 0x011B）和环上乘法（$*$，模数 0x0101），转换为大字段 GF$(2^N)$（$N>14$）上的操作（$\times$），并附加一个范围检查。这允许 GKR 和 PC 在一个统一的、对大字段友好的环境中高效处理 AES 的所有操作。

### 实验结果

实验在配备 Intel i9-11900H CPU 和 64GB DDR4 内存的 Linux PC 上运行，使用 Rust 实现。**对于可验证 AES**（图 7），与 Dubhe 的方案相比，Phecda 展示了显著优势。例如，验证 1024 个 AES 块时，Phecda 的证明者时间比 Dubhe 的额外证据方案快 2.33 倍，验证者时间快 1270 倍，证明大小小 102 倍；即便对标 Dubhe 无额外证据的方案，Phecda 仍有 540 倍更快的证明者、1070 倍更快的验证者和 3.8 倍更小的证明。Phecda 验证 1024 个 AES 块仅需约 10ms，证明大小为 576KB。**对于新的多项式承诺方案**（表 5、6、7），其批处理 LDT（mLDT）使得证明者、验证者和通信开销相比独立 LDT 分别快 1.14-1.21 倍、1.65-1.71 倍和小 1.66-1.77 倍。在与 Virgo 的比较中（表 6），在 GF$((2^{127}-1)^2)$ 域上，Phecda 的 PC 在证明者时间上快 25-35%，验证者时间快 8.3-9.7%，证明大小小 7-8%。在与 Orion 的比较中（表 7），Phecda 的 PC 在验证者时间上快 25-44 倍，证明大小小 11.6-18.5 倍，但证明者时间慢 6.5-15.7 倍。**对于 VOLE-in-the-Head 协议**（表 8），在验证 AES 的线性约束时，相较于 MPCitH，VOLEitH 的证明者、验证者和证明大小分别提升约 5.5 倍、3.3 倍和 3.6 倍。

### 局限性与开放问题

Phecda 的 PC 方案虽然验证者时间和通信量极优，但其证明者时间相比 Orion 这类具有线性时间证明者的方案仍有差距，这在大规模输入时可能成为瓶颈。此外，整个系统的构造相对复杂，涉及 GKR、FLPCP、PC 和 VOLEitH 多个模块的组合，其实际部署和调试难度较高。Phecda 的 VOLEitH 协议的安全分析依赖于特定的 MDS 编码假设和随机预言机模型，未来工作可以探索更弱的假设或标准化其协议设计，并考虑将其泛化到证明更通用的多项式关系，而不仅限于线性约束。

### 强关联论文

[3] J. Zhang, T. Xie, Y. Zhang, and D. Song. Transparent polynomial delegation and its applications to zero knowledge proof. **IEEE Symposium on Security and Privacy 2020** [Google Scholar](https://scholar.google.com/scholar?q=Transparent+polynomial+delegation+and+its+applications+to+zero+knowledge+proof)

[5] C. Ding and Y. Huang. Dubhe: Succinct zero-knowledge proofs for standard aes and related applications. **USENIX Security 2023** [Google Scholar](https://scholar.google.com/scholar?q=Dubhe%3A+Succinct+zero-knowledge+proofs+for+standard+aes+and+related+applications)

[12] J. Bootle, A. Chiesa, Y. Hu, and M. Orru. Gemini: Elastic snarks for diverse environments. **CRYPTO 2022** [Google Scholar](https://scholar.google.com/scholar?q=Gemini%3A+Elastic+snarks+for+diverse+environments)

[13] L. Roy. SoftSpokenOT: Quieter OT extension from small-field silent vole in the minicrypt model. **CRYPTO 2022** [Google Scholar](https://scholar.google.com/scholar?q=SoftSpokenOT%3A+Quieter+OT+extension+from+small-field+silent+vole+in+the+minicrypt+model)

[14] B. Chen, B. Bunz, D. Boneh, and Z. Zhang. Hyperplonk: Plonk with linear-time prover and high-degree custom gates. **EUROCRYPT 2023** [Google Scholar](https://scholar.google.com/scholar?q=Hyperplonk%3A+Plonk+with+linear-time+prover+and+high-degree+custom+gates)

[15] C. Baum, L. Braun, C. D. de Saint Guilhem, M. Klooß, E. Orsini, L. Roy, and P. Scholl. Publicly verifiable zero-knowledge and post-quantum signatures from vole-in-the-head. **CRYPTO 2023** [Google Scholar](https://scholar.google.com/scholar?q=Publicly+verifiable+zero-knowledge+and+post-quantum+signatures+from+vole-in-the-head)

[16] K. Yang, P. Sarkar, C. Weng, and X. Wang. Quicksilver: Efficient and affordable zero-knowledge proofs for circuits and polynomials over any field. **ACM CCS 2021** [Google Scholar](https://scholar.google.com/scholar?q=Quicksilver%3A+Efficient+and+affordable+zero-knowledge+proofs+for+circuits+and+polynomials+over+any+field)

[27] T. Xie, Y. Zhang, and D. Song. Orion: Zero knowledge proof with linear prover time. **CRYPTO 2022** [Google Scholar](https://scholar.google.com/scholar?q=Orion%3A+Zero+knowledge+proof+with+linear+prover+time)


## 关键词

+ 后量子透明zkSNARK
+ VOLE-in-the-Head零知识论证
+ 多线性多项式承诺
+ AES验证电路
+ 随机预言机模型
+ 抗量子密码学