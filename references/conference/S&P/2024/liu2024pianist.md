---
title: "Pianist: Scalable zkRollups via Fully Distributed Zero-Knowledge Proofs"
标题简称:
论文类型: conference
会议简称: S&P
发表年份: 2024

modified: 2025-05-09 09:27:59
created: 2025-04-07 16:54:34
---

## Pianist: Scalable zkRollups via Fully Distributed Zero-Knowledge Proofs

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/10646741)
+ [archive](https://eprint.iacr.org/2023/1271)
+ [code](https://github.com/dreamATD/pianist-gnark)

## 作者

+ [Tianyi Liu](Tianyi%20Liu.md)
+ [Tiancheng Xie](Tiancheng%20Xie.md)
+ [Jiaheng Zhang](Jiaheng%20Zhang.md)
+ [Dawn Song](Dawn%20Song.md)
+ [Yupeng Zhang](Yupeng%20Zhang.md)

## 笔记

### 背景与动机

区块链技术的可扩展性是制约其大规模应用的关键瓶颈之一。为了提升交易吞吐量，zkRollup和zkEVM等技术被提出，它们依赖于零知识证明（ZKP）来验证链下交易批处理的正确性，从而将验证成本从重新执行所有交易降低为仅检查一个小型证明。然而，在这些方案中，证明生成是性能瓶颈，例如广泛使用的Plonk系统[31]在单台机器上仅能支持约2^25个门的电路，需要数TB内存的集群才能处理更大规模的任务。现有的分布式ZKP方案，如DIZK[46]和deVirgo[48，虽然在计算上实现了线性扩展，但它们存在高额的通信开销：DIZK的通信量随电路总规模线性增长，deVirgo的通信量和证明大小也随机器数量增加。这限制了它们在实际部署中的应用，尤其是在类似矿池的异步环境中。本文旨在填补这一空白，提出一种全新的完全分布式ZKP方案，能够在实现证明时间线性加速的同时，将每台机器的通信量优化为常数，且保持证明大小和验证时间恒定，从而大幅提升zkRollup和zkEVM的可扩展性。

### 相关工作

[31] Gabizon, A., Williamson, Z.J., Ciobotaru, O.: Plonk: Permutations over lagrange-bases for oecumenical noninteractive arguments of knowledge. **IACR Cryptol. ePrint Arch. 2019** [Google Scholar](https://scholar.google.com/scholar?q=Plonk%3A+Permutations+over+lagrange-bases+for+oecumenical+noninteractive+arguments+of+knowledge)
> 核心思路：提出了一种高效的通用zk-SNARK方案，使用单变量多项式表示算术约束和复制约束，具有通用且可更新的可信设置。
> 局限与区别：在一个大的电路中，证明生成计算和内存开销巨大，成为瓶颈，且不支持分布式生成。

[46] Wu, H., Zheng, W., Chiesa, A., Popa, R.A., Stoica, I.: Dizk: A distributed zero knowledge proof system. **USENIX Security 2018** [Google Scholar](https://scholar.google.com/scholar?q=Dizk%3A+A+distributed+zero+knowledge+proof+system)
> 核心思路：首个分布式ZKP系统，将Groth16[33]的证明生成任务划分为多个Map-Reduce任务。
> 局限与区别：机器间通信量线性于电路总规模（O(N)），需要复杂的网络同步，不适合大规模异步部署。

[48] Xie, T., Zhang, J., Cheng, Z., Zhang, F., Zhang, Y., Jia, Y., Boneh, D., Song, D.X.: zkbridge: Trustless cross-chain bridges made practical. **CCS 2022** [Google Scholar](https://scholar.google.com/scholar?q=zkbridge%3A+Trustless+cross-chain+bridges+made+practical)
> 核心思路：提出了deVirgo，一个基于Virgo[51]的分布式ZKP协议，实现了线性计算加速。
> 局限与区别：由于使用了FRI协议和Merkle树，通信量和证明大小仍随机器数量增长（O(N) 通信，O(log^2 N) 证明大小），且缺乏鲁棒性。

[12] Ambrona, M., Beunardeau, M., Schmitt, A.L., Toledo, R.R.: aplonk: Aggregated plonk from multi-polynomial commitment schemes. **IACR Cryptol. ePrint Arch. 2022** [Google Scholar](https://scholar.google.com/scholar?q=aplonk%3A+Aggregated+plonk+from+multi-polynomial+commitment+schemes)
> 核心思路：提出aPlonk，一种基于Plonk[31]的分布式解决方案，利用多多项式承诺和广义IPA聚合证明。
> 局限与区别：需要各个佐证节点共享Fiat-Shamir随机性，导致多次同步；验证成本对数于参与方数量；仅支持数据并行电路且涉及递归证明。

[49] Zapico, A., Buterin, V., Khovratovich, D., Maller, M., Nitulescu, A., Simkin, M., Fabra, U.P.: Caulk: Lookup arguments in sublinear time. **CCS 2022** [Google Scholar](https://scholar.google.com/scholar?q=Caulk%3A+Lookup+arguments+in+sublinear+time)
> 核心思路：提出了使用预计算的多项式来处理查找参数的亚线性方案，其中包含利用拉格朗日多项式聚合的思想。
> 区别：本文借鉴了使用拉格朗日多项式进行聚合的技术来规避双变量多项式乘法中的交叉项问题，但将其应用于构建分布式SNARK的约束系统。

### 核心技术与方案

本文提出的Pianist方案旨在通过完全分布式的计算实现zkSNARK生成，核心思路是将单变量多项式约束系统扩展为双变量形式，并设计相应的双变量多项式承诺方案。

**双变量多项式约束系统**：该方案基于Plonk的算术约束系统。对于M台机器，每台机器i负责大小为T的子电路，并定义其局部多项式 $a_i(X), b_i(X), o_i(X)$。为了避免使用幂级数聚合时产生的交叉项，Pianist使用Y变量上的拉格朗日多项式 $R_i(Y)$ 将所有局部多项式聚合为双变量多项式，例如 $A(Y,X) = \sum_{i=0}^{M-1} R_i(Y) a_i(X)$。这样，当Y被赋值为 $\omega_Y^i$ 时，$A(Y,X)$ 恰好等于第i台机器的局部多项式。基于此，整个电路的约束可以表示为 $G(Y,X) + \lambda P_0(Y,X) + \lambda^2 P_1(Y,X) = V_X(X) H_X(Y,X) + V_Y(Y) H_Y(Y,X)$，其中 $V_X(X)=X^T-1$, $V_Y(Y)=Y^M-1$。这种设计使得分层IOP协议得以实现：主节点 $P_0$ 只需在收到随机挑战α后，从各机器收集其局部多项式在 α 处的评估值和部分证明，就能计算得到 $H_Y(Y,\alpha)$，从而完成整个协议。该协议的知识可靠性通过Schwartz-Zippel引理保证，证明挑战值使虚假多项式被接受的概率极低。

**分布式双变量KZG承诺**：为了将上述IOP编译为SNARK，Pianist提出了一个可被分布式计算的双变量KZG承诺方案（DKZG）。该方案的关键在于公共参数包含 $g^{R_i(\tau_Y) L_j(\tau_X)}$ 的所有幂次。这样，每台机器i可以独立地使用本地子集 $U_{i,j}$ 提交其局部多项式 $f_i(X)$，生成局部承诺 $com_{f_i}$。主节点 $P_0$ 只需将这些局部承诺相乘即可得到全局承诺 $com_f = \prod com_{f_i}$。在打开阶段，机器i发送局部评估值 $f_i(\alpha)$ 和局部证明 $\pi_0^{(i)}$，$P_0$ 聚合这些值得到 $f(Y,\alpha)$ 和聚合证明 $\pi_0$，并进一步计算 $f(\beta, \alpha)$ 和 $\pi_1$。最终，验证者通过配对检查 $e(com_f\ /\ g^z, g) = e(\pi_0, g^{\tau_X - \alpha}) e(\pi_1, g^{\tau_Y - \beta})$ 来验证。该方案保证了通信量为常数（每台机器仅发送常数大小消息），且证明大小和验证时间均为常数。

**鲁棒协作证明系统**：为了应对恶意节点，Pianist还引入了一个鲁棒协作证明系统。在测试合并阶段，主节点 $P_0$ 通过验证每个子证明来检测恶意机器。它通过检查每个机器i的局部多项式评估和证明是否正确，并为其设定一个二进制指示符 $b_i$。只有通过了检查的证明（$b_i=1$）才会被合并到最终证明中，从而实现了部分可靠性。

**协议流程与复杂度**: 整体协议包括预处理阶段和证明阶段。预处理阶段生成DKZG公共参数和所有公开多项式的承诺。证明阶段中，每台机器计算并提交其局部多项式承诺，主节点 $P_0$ 接收随机挑战并广播给各机器，各机器返回局部评估值和证明，由 $P_0$ 聚合后发送给验证者。系统总计算复杂度为 O(N log T + M log M) 域运算（每台机器O(T log T)，主节点额外O(M log M)）和 O(N) 群运算。通信复杂度为 O(1) 每台机器，证明大小和验证复杂度均为 O(1)。

**对普通电路的扩展**: 该方案进一步扩展到支持任意连接的普通电路。为此，需要为跨子电路的导线连接定义新的目标位置多项式 $\sigma_{Y, s,i}(X)$ 和 $\sigma_{X, s,i}(X)$。由于乘积穿越不同子电路后，最后一个乘积值 $z_i^*$ 不再归1，方案引入了一个新的多项式 $W(Y)$ 来跟踪跨子电路的乘积，并添加相应的约束 $P_2(Y)$ 和 $P_3(Y,X)$。这使得分布式IOP协议能处理任意拓扑的电路，而不仅仅是数据并行的电路。

### 核心公式与流程

**[双变量约束系统]**
$$
G(Y, X) + \lambda P_0(Y, X) + \lambda^2 P_1(Y, X) = V_X(X) H_X(Y, X) + V_Y(Y) H_Y(Y, X)
$$
> 作用：这是整个约束系统的核心方程，它将所有子电路的约束（用$P_0, P_1$表示）和门约束（$G$）与X方向和Y方向的项（$V_X H_X$和$V_Y H_Y$）联系起来。验证者通过挑战点$(\alpha, \beta)$上的评估来检查所有子电路约束是否正确满足。

**[分布式KZG验证]**
$$
e(com_f / g^{z}, g) = e(\pi_0, g^{\tau_X - \alpha}) e(\pi_1, g^{\tau_Y - \beta})
$$
> 作用：这是分布式KZG方案的核心验证方程。验证者检查聚合承诺 $com_f$ 和评估值 $z = f(\beta, \alpha)$ 是否匹配，其中 $\pi_0$ 是X维度上的聚合证明，$\pi_1$ 是Y维度上的证明。$g, \tau_X, \tau_Y$ 是公共参数，$\alpha, \beta$ 是挑战点。

**[普通电路的乘积链约束]**
$$
p_{i,3}(X) := L_{T-1}(X) \left(w_i z_i(X) f_i(X) - w_{(i+1)\% M} f_i'(X)\right)
$$
> 作用：对于普通电路，由于乘积跨越了不同子电路，此公式用于约束相邻子电路之间乘积值的连续性。它确保第i个子电路的最后一个乘积 $z_i^*$ 正确链接到第i+1个子电路的起始乘积。

### 实验结果

实验在AWS m6i.16xlarge实例（64 vCPU, 256 GB内存）上进行，使用BN254曲线，并通过Gnark库实现。对于zkRollup应用（基于Polygon Hermez电路），使用64台机器时，Pianist能在313秒内为8192笔交易生成证明，而优化的Plonk单机版仅能处理32笔交易（95秒），实现了64倍的规模提升。令人印象深刻的是，每台机器与主节点间的通信量仅为2.1 KB，证明大小为2.2 KB，验证时间恒定为3.5毫秒。对于随机生成的通用电路（$2^{25}$个门），使用32台机器时，Pianist在5秒内生成证明，相比Plonk单机版的121秒，加速24.2倍，且通信量（2080-2336字节）、证明大小（2816字节）和验证时间（3-5毫秒）均保持恒定小。主节点 $P_0$ 的额外合并时间也仅为几毫秒，说明其不是瓶颈。内存方面，对于$2^{24}$门电路，Pianist将每台机器的峰值内存从Plonk的70.7 GB降至1.92 GB（32台机器），展示了极好的可伸缩性。

### 局限性与开放问题

尽管Pianist在分布式ZKP生成上取得了显著进步，但仍有一些局限性。虽然方案支持具有任意连接的普通电路，但对子电路间复杂连接的支持是通过引入$W(Y)$多项式实现的，可能增加了实现的复杂性。此外，该方案的效率高度依赖于双变量KZG承诺，它需要一个可信设置，且该设置的大小与电路总规模线性相关，虽然该设置是通用且可更新的。与基于递归证明的PCD/IVC方案（如Nova）相比，Pianist在支持增量可验证计算方面存在局限性，它更适用于静态的、可以预先划分的批量计算任务。未来工作可以考虑如何将本方案与查找参数、自定义门等先进技术更紧密地结合，以进一步减少验证成本和电路规模。

### 强关联论文

[31] Gabizon, A., Williamson, Z.J., Ciobotaru, O.: Plonk: Permutations over lagrange-bases for oecumenical noninteractive arguments of knowledge. **IACR Cryptol. ePrint Arch. 2019** [Google Scholar](https://scholar.google.com/scholar?q=Plonk%3A+Permutations+over+lagrange-bases+for+oecumenical+noninteractive+arguments+of+knowledge)

[46] Wu, H., Zheng, W., Chiesa, A., Popa, R.A., Stoica, I.: Dizk: A distributed zero knowledge proof system. **USENIX Security 2018** [Google Scholar](https://scholar.google.com/scholar?q=Dizk%3A+A+distributed+zero+knowledge+proof+system)

[48] Xie, T., Zhang, J., Cheng, Z., Zhang, F., Zhang, Y., Jia, Y., Boneh, D., Song, D.X.: zkbridge: Trustless cross-chain bridges made practical. **CCS 2022** [Google Scholar](https://scholar.google.com/scholar?q=zkbridge%3A+Trustless+cross-chain+bridges+made+practical)

[12] Ambrona, M., Beunardeau, M., Schmitt, A.L., Toledo, R.R.: aplonk: Aggregated plonk from multi-polynomial commitment schemes. **IACR Cryptol. ePrint Arch. 2022** [Google Scholar](https://scholar.google.com/scholar?q=aplonk%3A+Aggregated+plonk+from+multi-polynomial+commitment+schemes)

[49] Zapico, A., Buterin, V., Khovratovich, D., Maller, M., Nitulescu, A., Simkin, M., Fabra, U.P.: Caulk: Lookup arguments in sublinear time. **CCS 2022** [Google Scholar](https://scholar.google.com/scholar?q=Caulk%3A+Lookup+arguments+in+sublinear+time)

[35] Kate, A., Zaverucha, G.M., Goldberg, I.: Constant-size commitments to polynomials and their applications. **ASIACRYPT 2010** [Google Scholar](https://scholar.google.com/scholar?q=Constant-size+commitments+to+polynomials+and+their+applications)

[41] Papamanthou, C., Shi, E., Tamassia, R.: Signatures of correct computation. **TCC 2013** [Google Scholar](https://scholar.google.com/scholar?q=Signatures+of+correct+computation)


## 关键词

+ 全分布式零知识证明
+ zkRollup可扩展性
+ Plonk协议
+ 数据并行电路
+ 分布式证明生成
+ zkEVM区块链扩展

