---
title: "Proof-carrying data without succinct arguments"
标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 2021
created: 2025-04-22 15:09:39
modified: 2025-04-22 15:10:29
---

## Proof-carrying data without succinct arguments

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-030-84242-0_24)

## 作者

+ [Benedikt Bünz](Benedikt%20Bünz.md) 
+ [Alessandro Chiesa](Alessandro%20Chiesa.md)
+ William Lin 
+ [Pratyush Mishra](Pratyush%20Mishra.md)
+ Nicholas Spooner 

## 笔记

### 背景与动机
证明携带数据（PCD）是一种强大的密码学原语，它允许互不信任的各方执行可以无限运行的分布式计算，同时确保每个中间状态都能被高效验证 [CT10]。PCD 的应用范围广泛，包括语言语义执行、可验证 MapReduce 计算、图像认证和区块提升系统。构建 PCD 的经典方法依赖于非交互式参数（SNARKs）的递归组合，但这一方法要求 SNARK 具备亚线性验证时间，这极大地限制了可选方案，并带来了实际效率上的代价，例如需要昂贵的配对友好曲线循环或大量哈希函数计算 [BCCT13; BCTV14; COS20]。近期，[BCMS20] 提出了一种替代构造，利用具有累积方案的 SNARK（而非亚线性验证）来实现递归，从而放宽了条件。然而，所有已知的 PCD 构建仍依赖于 SNARK 的某种形式的简洁性。本文旨在进一步探究 PCD 能否从更弱的原语出发构建，具体而言，是否可以利用一个无需任何简洁性的非交互式论证系统（NARK）来构建 PCD，并探索这种放宽对具体效率的提升潜力。

### 相关工作

[BCMS20] Bunz, Chiesa, Mishra, Spooner. Proof-Carrying Data from Accumulation Schemes. **TCC 2020** [Google Scholar](https://scholar.google.com/scholar?q=Proof-Carrying+Data+from+Accumulation+Schemes)
> 核心思路：提出了原子累积方案（atomic accumulation scheme）的概念，并证明了任何具有该方案的 SNARK 都可以用来构建 PCD。
> 局限与区别：该方案仍然要求底层的 NARK 是 SNARK（即具有简洁的论证），而本文则进一步放宽到任何 NARK 都可以，只要其具有本文新提出的分裂累积方案（split accumulation scheme）。本文的分裂累积方案将累积器的证据与实例分离，允许累积器的实例部分保持简短，从而支持非简洁的 NARK。

[BCCT13] Bitansky, Canetti, Chiesa, Tromer. Recursive Composition and Bootstrapping for SNARKs and Proof-Carrying Data. **STOC 2013** [Google Scholar](https://scholar.google.com/scholar?q=Recursive+Composition+and+Bootstrapping+for+SNARKs+and+Proof-Carrying+Data)
> 核心思路：提出了通过递归组合 SNARK 来构建 PCD 的经典方法，并证明了 PCD 可以“引导”出用于机器计算的 SNARK。
> 局限与区别：该方法要求底层的 SNARK 具有亚线性验证时间，这制约了其具体效率和可用的密码学假设。本文的工作表明，在存在分裂累积方案的情况下，递归组合甚至可以由非简洁的 NARK 实现，这提供了全新的可行性。

[BCTV14] Ben-Sasson, Chiesa, Tromer, Virza. Scalable Zero Knowledge via Cycles of Elliptic Curves. **CRYPTO 2014** [Google Scholar](https://scholar.google.com/scholar?q=Scalable+Zero+Knowledge+via+Cycles+of+Elliptic+Curves)
> 核心思路：引入椭圆曲线循环技术（cycles of elliptic curves），实现了高效的递归组合，并在此基础上构建了可扩展的 zkSNARK。
> 局限与区别：该技术依赖于配对友好的椭圆曲线，这带来了较慢的群运算和较大的参数规模。相比之下，本文基于分裂累积的方案可以使用标准椭圆曲线循环（如 Pasta 曲线），从而在递归步骤中获得更好的具体效率。

[COS20] Chiesa, Ojha, Spooner. Fractal: Post-Quantum and Transparent Recursive Proofs from Holography. **EUROCRYPT 2020** [Google Scholar](https://scholar.google.com/scholar?q=Fractal%3A+Post-Quantum+and+Transparent+Recursive+Proofs+from+Holography)
> 核心思路：提出了一个后量子安全的、透明的 PCD 构造，基于全息论证（holographic arguments）和哈希函数。
> 局限与区别：虽然该方案避免了配对，但其递归开销（prover 和 verifier 的计算成本）相对较高。本文的分裂累积方案在离散对数设定下实现了更低的递归阈值（recursion threshold），尽管论证大小是线性的。

[Val08] Valiant. Incrementally Verifiable Computation or Proofs of Knowledge Imply Time/Space Efficiency. **TCC 2008** [Google Scholar](https://scholar.google.com/scholar?q=Incrementally+Verifiable+Computation+or+Proofs+of+Knowledge+Imply+Time%2FSpace+Efficiency)
> 核心思路：提出了增量可验证计算（IVC）的概念，这是 PCD 的一个特例，其中计算是单链式的。
> 局限与区别：该工作奠定了理论框架，而本文关注的是如何从更弱的原语（具有分裂累积的 NARK）出发，实现 IVC 或更一般的 PCD。

[Halo20] Bowe, Grigg, Hopwood. Halo: Recursive Proof Composition without a Trusted Setup. ePrint 2019/1021 [Google Scholar](https://scholar.google.com/scholar?q=Halo%3A+Recursive+Proof+Composition+without+a+Trusted+Setup)
> 核心思路：提出了无需可信设置的递归组合方案，基于内积论证（inner product argument）和循环的椭圆曲线。
> 局限与区别：Halo 依赖于 SNARK 具有对数级验证，并通过一个对数级成本的原子累积方案实现递归。本文的分裂累积方案将其验证者成本降低到常数级，从而获得了更低的递归阈值。

[BGH19] Bowe, Grigg, Hopwood. Halo: Recursive Proof Composition without a Trusted Setup. ePrint 2019/1021 [Google Scholar](https://scholar.google.com/scholar?q=Halo%3A+Recursive+Proof+Composition+without+a+Trusted+Setup)
> 核心思路：与 Halo20 相同，该技术报告是 Halo 方案的早期版本，提出了内积论证和循环曲线的结合。
> 局限与区别：本文直接构建于 Halo 的离散对数设定之上，但避免了其累积方案中对数级的验证成本。

[BDFG20] Boneh, Drake, Fisch, Gabizon. Halo Infinite: Recursive zk-SNARKs from any Additive Polynomial Commitment Scheme. ePrint 2020/1536 [Google Scholar](https://scholar.google.com/scholar?q=Halo+Infinite%3A+Recursive+zk-SNARKs+from+any+Additive+Polynomial+Commitment+Scheme)
> 核心思路：同时期工作，研究减少递归论证成本的问题，提出了加法多项式承诺方案的私有聚合，其对应于本文的分裂累积。
> 局限与区别：BDFG20 专注于 PC 方案层面的通用协议，而本文提出了对于一般关系谓词的分裂累积定义，并证明了其足以构建 PCD 方案。此外，本文还包含了全面的实现和评估。

### 核心技术与方案
本文的核心是在一个统一的框架下，利用“分裂累积方案”这一新概念来构建 PCD，该方案是 [BCMS20] 中“原子累积方案”的放宽版本。

**1. 分裂累积方案**
在原子累积方案 [BCMS20] 中，一个累积器 acc 是一个单一的短字符串，其验证者 V 必须完整读取它。而对于分裂累积方案，一个累积器被分成一个短的实例部分 acc.x 和一个长的证据部分 acc.w。验证V只接收实例部分 acc.x 和一个短的证明 pf，而不需要查看长的证据。这种分离允许我们构造这样的方案：即使底层 NARK 的证据（例如，一个大的多项式或赋值向量）很长，其累积器实例 (acc.x) 和验证者 (V) 的复杂度依然很低（例如常数级）。这与传统的 SNARK 不同，SNARK 要求论证本身是简洁的。

**2. 从分裂累积构建 PCD**
作者证明了任何具有分裂累积方案的 NARK（无需任何简洁性）都可以用来构建 PCD（定理 1）。其核心是图 2 中的递归电路 R。在每一步，NARK 证明一个声明：新的输出 $z_{i+1}$ 是通过正确应用函数 F 从旧状态 $z_i$ 得到的，并且存在一个累积证明 $pf$ 使得累积验证者 V 接受对旧证明 $\pi_i$ 和旧累积器 $acc_i$ 的累积结果。关键点是，R 的输入（即被证明的声明）只包含 $\pi_i$ 和 $acc_i$ 的短实例部分（$\pi_i.x$ 和 $acc_i.x$），而不包含其长的证据部分（$\pi_i.w, acc_i.w$）。这确保了电路 R 的大小仅由累积验证者 V 的复杂度决定，而与底层 NARK 的论证大小无关。

**3. 基于离散对数的 NARK 及其分裂累积**
为了实例化该框架，作者构造了一个基于离散对数（DL）假设和随机预言机的透明（transparent）zkNARK for R1CS（定理 2）。这个 zkNARK 是通过对基于 Pedersen 承诺的 R1CS sigma 协议应用 Fiat-Shamir 变换得到的（图 3）。其论证大小是线性的（O(M) 个域元素，M 是约束数），验证时间也是线性的。
然而，作者为其构造了一个极其高效的分裂累积方案，其累积验证者 V 的复杂度是常数（O(1) 个群标量乘法和域操作）。这个方案的效率由以下设计保证：
- **谓词与累积器**：被累积的谓词 $\Phi_V$ 对应于 NARK 的验证者。一个谓词输入 $(qx, qw)$ 将一个短的实例（R1CS 输入 x 和 sigma 协议的第一步承诺）与一个长的证据（sigma 协议的第二步响应，包含一个长的盲化赋值 $s$）分离开。累积器也以相同方式分裂。
- **累积过程**：累积过程本质上是对多个实例-证据对进行随机线性组合（通过幂次 $\beta$）。由于累积器的实例部分和证据部分都是线性组合的，累积器的新实例 $acc.x$ 可以通过只读取短的输入实例来计算。然而，一个关键的非线性成分来自于 R1CS 的 Hadamard 乘积约束：$A_z \circ B_z = C_z$。简单地组合线性项会引入交叉项 $z_A \circ z_B' + z_A' \circ z_B$。
- **处理 Hadamard 乘积**：这些交叉项被捕获并包含在累积证明 pf 中。具体而言，累积证明包含了一个对交叉项 $z_A \circ z_B' + z_A' \circ z_B$ 的承诺（见步骤 3 的 pf 计算）。然后，累积器中的新 Hadamard 乘积承诺 $C_\circ$ 被更新为 $C_\circ + \beta \cdot pf + \beta^2 \cdot qx.C_C$，其中 $qx.C_C$ 是新输入中已有的承诺 $C_C$，它表示 $z_A \circ z_B$。这个二次方的更新方程保证了如果所有输入的 R1CS 方程都成立，那么新累积器的方程也成立。

**4. 安全性证明**
安全性证明利用了一个新提出的“期望时间分叉引理”（Lemma 6.1），该引理允许从随机预言机模型中的期望多项式时间对手那里提取多个接受的重放。对于方案的知识可靠性证明，作者构造了一个提取器，它：
1. 使用分叉引理从对手那里获得多个接受的重放，这些重放对应于不同的挑战 $\beta$，从而能够求解线性系统，从累积器的线性组合中恢复原始输入的属性和证据。
2. 利用一个“寻找零点游戏”引理（零查找游戏引理），证明如果关于多项式（比如由累积器隐含的电池多项式）的方程在由随机预言机选择的点上成立，那么它必须以压倒性概率是一个恒等式。这保证了从线性组合中恢复的向量正确地满足原始的 R1CS 方程。

### 核心公式与流程

**[递归电路 R（原子累积 vs. 分裂累积）]**
$$
\begin{array}{l|l}
\text{原子累积 [BCMS20]} & R((avk, z_{i+1}, acc_{i+1}), (z_i, \pi_i, acc_i, pf_{i+1})) : \\
  & \quad \text{check } z_{i+1} = F(z_i) \\
  & \quad \text{set } q_i := ((avk, z_i, acc_i), \pi_i) \\
  & \quad \text{check } ACC.V(avk, q_i, acc_i, acc_{i+1}, pf_{i+1}) = 1 \\
\hline
\text{分裂累积（本文）} & R((avk, z_{i+1}, acc_{i+1}.x), (z_i, \pi_i.x, acc_i.x, pf_{i+1})) : \\
  & \quad \text{check } z_{i+1} = F(z_i) \\
  & \quad \text{set } qx_i := ((avk, z_i, acc_i.x), \pi_i.x) \\
  & \quad \text{check } ACC.V(avk, [qx_i], [acc_i.x], acc_{i+1}.x, pf_{i+1}) = 1
\end{array}
$$
> 作用：对比了两种递归方式的关键区别。在分裂累积方案中，递归电路 R 的输入只包含 $\pi_i$ 和 $acc_i$ 的短实例部分（$\pi_i.x$, $acc_i.x$），而忽略了其长的证据部分（$\pi_i.w$, $acc_i.w$）。这使得 R 的大小仅由累积验证者的复杂度决定，从而避免了论证大小对递归的影响。

**[累积证明更新公式]**
$$
C_{\circ}^{(new)} = C_{\circ}^{(old)} + \beta \cdot pf + \beta^2 \cdot qx.C_C
$$
其中 $pf = Commit(ck, z_A \circ z_B' + z_A' \circ z_B)$ 是累积证明（承诺到交叉项）。
> 作用：该公式是累积方案处理 Hadamard 乘积（非线性约束）的核心。它通过一个二次多项式将新输入（$qx.C_C$）和旧累积器（$C_{\circ}^{(old)}$）组合起来，其中交叉项由累积证明 pf 捕获。这个结构确保了如果所有输入都满足 R1CS 方程，线性组合后的新累积器也满足它。

**[NARK 的 sigma 协议验证方程]**
$$
C_A + \gamma C_A' = CM.Commit(ck, A \cdot [x; s]; \sigma_A)
$$
$$
C_B + \gamma C_B' = CM.Commit(ck, B \cdot [x; s]; \sigma_B)
$$
$$
C_C + \gamma C_C' = CM.Commit(ck, C \cdot [x; s]; \sigma_C)
$$
$$
C_C + \gamma C_1 + \gamma^2 C_2 = CM.Commit(ck, s_A \circ s_B; \sigma_{\circ})
$$
> 作用：这些是 zkNARK for R1CS 的基本验证方程。前三个方程验证了承诺 $C_A, C_B, C_C$ 对应于输入 x 和响应 s 的线性变换（A, B, C）。最后一个方程验证了 Hadamard 乘积约束 $A[x;s] \circ B[x;s] = C[x;s]$。这些验证检查是累积方案累积的谓词。

**[分裂累积的 Hadamard 乘积谓词 $\Phi_{HP}$]**
$$
\Phi_{HP}(\mathsf{pp}_{\Phi}, \ell, \mathsf{qx}, \mathsf{qw}) \text{ checks that:}
$$
$$
C_1 = CM.Commit(ck, a; \omega_1) \land C_2 = CM.Commit(ck, b; \omega_2) \land C_3 = CM.Commit(ck, a \circ b; \omega_3)
$$
> 作用：定义了本文分裂累积方案的核心谓词。它检查一个承诺 $C_3$ 是不是对两个向量 a 和 b 的 Hadamard 乘积的承诺。这个谓词用于累积 zkNARK 验证者的非线性检查。

### 实验结果
作者使用 Rust 实现了所有方案，并在名为“Pasta”的 255 位标准椭圆曲线循环（Pallas 曲线）上进行实验，该曲线被 Zcash 等实际项目使用。实验主要比较了三类累积方案的验证者约束成本：基于内积论证的原子累积（AS_IPA）、基于 Pedersen 承诺的分裂累积（AS_PC）、以及本文针对 R1CS 的分裂累积（AS_R1CS w/o ZK 和 w/ ZK）。关键实验数据来自于图 7 和表 3 等。结果表明，当对 $2^{20}$ 个约束进行计算时，AS_R1CS 的无零知识版本的验证者约束成本约为 $52 \times 10^{3}$，包含零知识时约为 $99 \times 10^{3}$。相比之下，AS_PC 的累积验证者成本仅为 $30 \times 10^{3}$ 个约束，而 AS_IPA 则需要 $435 \times 10^{3}$ 个约束，高出 8 到 20 倍。对于递归阈值的测试表明，本文基于分裂累积的 IVC 其递归阈值为 $52 \times 10^{3}$ 或 $99 \times 10^{3}$ 约束，比基于 AS_IPA 的 IVC（数百千约束）至少便宜 8.5 倍，甚至低于基于高效配对的 SNARK（如 Groth16）的递归阈值。实验还测量了证明者（P）的时间，对于 $2^{17}$ 约束的系统，AS_R1CS w/o ZK 的证明者时间为 2.0 秒，积累一个旧累积器和一个新证明。验证者的时间非常快（约 2 毫秒），表明其理论上的常数级复杂度在实际中也得到了体现。

### 局限性与开放问题
本文的 PCD 方案虽然具有常数级累积验证者，但论证大小是线性的（O(M) 个域元素），这限制了其在需要非常短证明的应用中的适用性。此外，虽然累积证明 pf 是短的，但累积器中包含的证据部分（acc.w）仍然是线性的，导致了较大的“完整”累积器大小（例如 8.4 MB）。未来的一个开放问题是，能否将分裂累积的思想扩展到其他密码学设定中，例如基于格的后量子密码学，以构建具有类似效率优势的后量子 PCD 方案。

### 强关联论文

[BCMS20] Bunz, Chiesa, Mishra, Spooner. Proof-Carrying Data from Accumulation Schemes. **TCC 2020** [Google Scholar](https://scholar.google.com/scholar?q=Proof-Carrying+Data+from+Accumulation+Schemes)

[BCCT13] Bitansky, Canetti, Chiesa, Tromer. Recursive Composition and Bootstrapping for SNARKs and Proof-Carrying Data. **STOC 2013** [Google Scholar](https://scholar.google.com/scholar?q=Recursive+Composition+and+Bootstrapping+for+SNARKs+and+Proof-Carrying+Data)

[BCTV14] Ben-Sasson, Chiesa, Tromer, Virza. Scalable Zero Knowledge via Cycles of Elliptic Curves. **CRYPTO 2014** [Google Scholar](https://scholar.google.com/scholar?q=Scalable+Zero+Knowledge+via+Cycles+of+Elliptic+Curves)

[COS20] Chiesa, Ojha, Spooner. Fractal: Post-Quantum and Transparent Recursive Proofs from Holography. **EUROCRYPT 2020** [Google Scholar](https://scholar.google.com/scholar?q=Fractal%3A+Post-Quantum+and+Transparent+Recursive+Proofs+from+Holography)

[Val08] Valiant. Incrementally Verifiable Computation or Proofs of Knowledge Imply Time/Space Efficiency. **TCC 2008** [Google Scholar](https://scholar.google.com/scholar?q=Incrementally+Verifiable+Computation+or+Proofs+of+Knowledge+Imply+Time%2FSpace+Efficiency)

[Halo20] Bowe, Grigg, Hopwood. Halo: Recursive Proof Composition without a Trusted Setup. ePrint 2019/1021 [Google Scholar](https://scholar.google.com/scholar?q=Halo%3A+Recursive+Proof+Composition+without+a+Trusted+Setup)

[BGH19] Bowe, Grigg, Hopwood. Halo: Recursive Proof Composition without a Trusted Setup. ePrint 2019/1021 [Google Scholar](https://scholar.google.com/scholar?q=Halo%3A+Recursive+Proof+Composition+without+a+Trusted+Setup)

[BDFG20] Boneh, Drake, Fisch, Gabizon. Halo Infinite: Recursive zk-SNARKs from any Additive Polynomial Commitment Scheme. **ePrint 2020/1536** [Google Scholar](https://scholar.google.com/scholar?q=Halo+Infinite%3A+Recursive+zk-SNARKs+from+any+Additive+Polynomial+Commitment+Scheme)


## 关键词

+ 密码学
+ 零知识
+ 协议