---
title: "Eos: Efficient private delegation of zkSNARK provers"
标题简称:
论文类型: conference
会议简称: USENIX Security
发表年份: 2023
created: 2025-04-21 08:41:52
modified: 2025-04-21 08:42:37
---

## Eos: Efficient private delegation of zkSNARK provers

## 发表信息

+ [原文链接](https://www.usenix.org/conference/usenixsecurity23/presentation/chiesa)

## 作者

+ [Alessandro Chiesa](Alessandro%20Chiesa.md)
+ Ryan Lehmkuhl 
+ [Pratyush Mishra](Pratyush%20Mishra.md)
+ [Yinuo Zhang](Yinuo%20Zhang.md)
## 笔记

### 背景与动机
零知识简洁非交互式知识论证（zkSNARKs）允许证明者向验证者证明一个陈述为真，同时不泄露任何额外信息。然而，生成 zkSNARK 证明的计算开销非常大，这限制了其应用范围，例如在去中心化私人货币和计算系统中。一种直观的思路是利用云服务器来生成证明，但现有方法如 DIZK [46] 需要向云机器泄露私有信息，这在隐私敏感的应用中是不可接受的。因此，如何在保护隐私的前提下，将证明生成委托给不受信任的机器，成为了一个亟待解决的问题。本文旨在设计并实现隐私保护的委托协议，使得证明者可以将 zkSNARK 证明生成外包给一组工人，只要至少有一个工人不与其他工人共谋，就不会向任何工人泄露私有信息。

### 相关工作

[7] Block 和 Garman. Honest Majority Multi-Prover Interactive Arguments. **IACR ePrint 2022/557** [Google Scholar](https://scholar.google.com/scholar?q=Honest+Majority+Multi-Prover+Interactive+Arguments)
> 核心思路：在诚实多数（至少 n/2+1 个工人诚实）的假设下，设计分布式证明协议，实现渐近 n 倍加速。
> 局限与区别：该协议牺牲了隐私，即使诚实工人也能看到（部分）证据；且未实现或评估性能。本文在恶意安全模型下实现隐私保护，且提供具体实现。

[36] Ozdemir 和 Boneh. Experimenting with Collaborative zk-SNARKs: Zero-Knowledge Proofs for Distributed Secrets. **USENIX Security 2022** [Google Scholar](https://scholar.google.com/scholar?q=Experimenting+with+Collaborative+zk-SNARKs)
> 核心思路：设计“协作证明”协议，让持有证据秘密共享的多方共同生成 zkSNARK 证明，支持多个 zkSNARK [26,24,14]。
> 局限与区别：协议设计上未利用诚实委托方进行预处理，因而需更重的密码学开销；恶意安全采用信息论 MAC 导致 2× 的工人计算和通信开销，以及 (2n-1)× 的委托方通信开销。本文利用诚实委托方减少预处理成本，并使用 PIOP 一致性检查器实现轻量恶意安全，性能提升 6-8 倍。

[19] Dayama 等. How to prove any NP statement jointly? Efficient Distributed-prover Zero-Knowledge Protocols. **PETS 2022** [Google Scholar](https://scholar.google.com/scholar?q=How+to+prove+any+NP+statement+jointly)
> 核心思路：为 IOP 类 SNARK [3] 构建协作证明者，协议与本文的 PIOP 委托类似。
> 局限与区别：与 [36] 类似，应用场景是分布式计算而非委托，且依赖重量级密码学实现恶意安全；未实现或评估。本文的委托设置允许委托方参与预处理以降低开销。

[41] Schoenmakers 等. Trinocchio: Privacy-Preserving Outsourcing by Distributed Verifiable Computation. **ACNS 2016** [Google Scholar](https://scholar.google.com/scholar?q=Trinocchio)
> 核心思路：研究隐私保护的委托可验证计算，由 MPC 执行计算，再使用 zkSNARK 子协议证明正确性。
> 局限与区别：目标 zkSNARK 是电路特定设置的 [37]，而本文针对通用设置；使用 Shamir 秘密共享（抗 n/2 腐败），本文用加法秘密共享（抗 n-1 腐败）；需要委托方重构 Shamir 份额，本文无需；只达到半诚实安全，本文达到恶意安全。

[28] Kanjalkar 等. Publicly Auditable MPC-as-a-Service with succinct verification and universal setup. **EuroS&P 2021 Workshops** [Google Scholar](https://scholar.google.com/scholar?q=Publicly+Auditable+MPC-as-a-Service+with+succinct+verification+and+universal+setup)
> 核心思路：设计可审计 MPC，在证据秘密共享时生成 MARLIN [14] 类型 zkSNARK 证明给第三方审计。
> 局限与区别：与 Trinocchio 类似，使用 Shamir 秘密共享（抗 n/2 腐败）。本文使用加法秘密共享（抗 n-1 腐败）；本文协议更通用，支持不同 PIOP 和 PC 方案。

[46] Wu 等. DIZK: A Distributed Zero Knowledge Proof System. **USENIX Security 2018** [Google Scholar](https://scholar.google.com/scholar?q=DIZK)
> 核心思路：将 [26] 的证明计算分布在集群中，旨在优化空间复杂度，不隐藏证据。
> 局限与区别：与本文互补；可将 DIZK 技术用于每个工人的计算，以进一步提高可扩展性，同时由于工人仅处理秘密份额而保持隐私。

### 核心技术与方案

本文构建的委托协议针对基于 PIOP（多项式交互式预言机证明）和 PC（多项式承诺方案）构造的通用设置 zkSNARK [14]。协议分为预处理阶段和在线阶段，支持两种模式：隔离模式（每个诚实工人只与委托方 D 通信）和协作模式（工人之间直接通信）。安全模型保证只要至少一个工人诚实且不共谋，证据 w 完全隐藏，且工人可恶意偏离协议。

**协议设计思路。** 直接使用现成的 MPC 协议（如 SPDZ [18]）存在两个问题：一是恶意安全需要昂贵的公钥密码和认证三元组；二是将 zkSNARK 证明者算法（包含椭圆曲线运算、多项式算术）表达为电路时开销极大。本文通过三个步骤克服这些问题。

**第一步：针对委托设置设计专用协议。** 利用委托方 D 是诚实的这一事实，在预处理阶段让 D 生成乘法三元组（协作模式），或在隔离模式下直接由 D 执行乘法功能，从而消除公钥密码开销。具体地，在隔离模式下，当遇到私密乘法门时，工人向 D 发送份额，D 重建后重新分享乘积。在协作模式下，工人使用 D 预先生成的三元组进行安全乘法。

**第二步：实现恶意安全。** 核心思想是利用 zkSNARK 的底层组件（PIOP 和 PC 方案）的简洁验证性质，而非整体的知识可靠性。本文引入 PIOP 一致性检查器（Consistency Checker, Ch），使得 D 可以高效地检查工人计算的多项式预言机是否与诚实证明者应生成的一致。以 MARLIN PIOP [14] 为例，一致性检查器仅需对证据的低次扩展在随机点进行求值并核对，开销仅为 O(|w|) 次域乘法。若工人作弊，则最终证明将无效，从而阻止恶意行为。该检查器避免了 SPDZ 中认证三元的开销。

**第三步：设计高效的 PIOP 和 PC 方案电路。** 关键优化如下：
- 多项式的多点求值和插值（FFT/IFFT）在每个系数上是线性运算，因此对应电路不含乘法门。
- 多项式除法当除数为公开多项式时也是线性运算，电路深度为 0。
- 多项式乘法通过 FFT 后逐点相乘再 IFFT 实现，仅需约 2d 个乘法门，深度为 1。
- 椭圆曲线上的多标量乘（MSM）可利用加法同态性质，电路深度为 0（当标量或基点之一公开时）。
- 具体 PC 方案 KZG [29] 的承诺和打开电路深度均为 0。

**协议流程概述。** 图中给出了完整协议 Π_SNARK（Fig. 4）。预处理阶段若为协作模式，D 生成乘法三元组并分发给工人。在线阶段，D 将索引证明密钥 ipk、实例 x 发送给工人，并将证据 w 和随机数 r 秘密共享。之后循环执行 zkSNARK 证明者的各轮：执行电路 C_SNARK.Round，D 接收承诺 C_j；D 调用一致性检查器的查询算法 ChQ 获得查询点及期望答案；工人通过 ExecCircuit 打开多项式求值证明；D 验证证明；最后执行 Finalize 得到最终证明 π。

**安全性证明概要（附录 A）。** 证明通过模拟器 S 获得理想世界执行与真实世界不可区分。S 使用模拟的证据（全零）和随机数运行协议，并利用随机预言机编程以匹配诚实输出。对于 Reveal 门，S 从真实证明中读取正确的线值，并调整份额使得重建结果一致。一致性检查器引入的拒绝概率可通过 PC 方案的抽取性和绑定性以及 PIOP 的完备性与可靠性归约为可忽略概率。

**渐进复杂度。** 委托方 D 的计算复杂度为 O(|w|)（仅执行一致性检查器中的求值），通信量在隔离模式下为 O(|C|)（证明显式传输），在协作模式下包括预处理和在线阶段，总通信量与电路大小线性。工人计算量主要来自 FFT 和 MSM，与本地证明者相当，但可通过并行化进一步优化。

### 核心公式与流程

**[多项式加法 PolyAdd]**
$$
p_3,i = \mathsf{Add}_{\mathbb{F}}(p_{1,i}, p_{2,i}) \quad \forall i \in \{0,\ldots,d\}
$$
> 作用：两多项式逐系数相加，电路深度为 0。

**[快速傅里叶变换 FFT]**
$$
\{p(\omega^i)\}_{i=0}^{|H|-1} \leftarrow \mathsf{FFT}(p, H)
$$
> 作用：将多项式系数表示转换为在光滑子群 H 上的求值表示，仅含加法和与公开数乘法，深度 0。

**[多项式乘法 PolyMul]**
$$
\begin{aligned}
e_1 &:= \mathsf{FFT}(p_1, H), \quad e_2 := \mathsf{FFT}(p_2, H) \\
e_3 &:= \text{element-wise product of } e_1 \text{ and } e_2 \\
p_3 &:= \mathsf{IFFT}(e_3, H)
\end{aligned}
$$
> 作用：利用 FFT 实现多项式乘法，仅需约 2d 个乘法门，深度 1。

**[多项式除法 PolyDiv（除数为公开）]**
$$
p = q \cdot d + r, \quad \deg(r) < \deg(d)
$$
> 作用：对公开除数 d 的多项式除法是线性运算，电路深度 0。

**[CKZG.Commit]**
$$
C := \mathsf{MSM}(p, \{\alpha^i \mathcal{G}\}_{i=0}^{d}) + \mathsf{MSM}(\bar{p}, \{\alpha^i \gamma \mathcal{G}\}_{i=0}^{d})
$$
> 作用：KZG 多项式承诺，通过两次多标量乘实现，深度 0。

**[CKZG.Open]**
$$
\begin{aligned}
\bar{\nu} &:= \mathsf{PolyEval}(\bar{p}, z) \\
(w, \bar{w}) &:= \mathsf{PolyDiv}(p, X-z), \ \mathsf{PolyDiv}(\bar{p}, X-z) \\
W &:= \mathsf{CKZG.Commit}(ck, w; \bar{w}) \\
\pi &:= (W, \bar{\nu})
\end{aligned}
$$
> 作用：KZG 打开证明，深度 0。

**[一致性检查器 Ch（MARLIN PIOP 示例）]**
$$
\begin{aligned}
&\text{采样 } z \overset{\$}{\leftarrow} \mathbb{F} \\
&\text{查询预言机 } \hat{w} \text{ 得到 } \nu := \hat{w}(z) \\
&\text{本地用重心插值计算 } \hat{w}(z), \text{ 检查是否等于 } \nu
\end{aligned}
$$
> 作用：以 O(|w|) 代价检查工人提供的第一轮多项式预言机是否与正确证据一致。

**[委托协议相乘处理（隔离模式）]**
$$
\text{工人发送 }[[w_a]]_i, [[w_b]]_i \text{ 给 } \mathcal{D}, \text{ 重建后 } \mathcal{D} \text{ 重新分享 } w_c = w_a w_b
$$
> 作用：隔离模式下直接由诚实委托方完成秘密乘法，避免预处理。

**[委托协议相乘处理（协作模式预处理）]**
$$
\begin{aligned}
&\mathcal{D} \text{ 生成三元组 } (\alpha_k, \beta_k, \gamma_k = \alpha_k \cdot \beta_k) \text{ 并秘密共享} \\
&\text{工人利用三元组执行安全乘法}
\end{aligned}
$$
> 作用：协作模式下预先生成三元组，在线阶段高效完成安全乘法。

### 实验结果

实验设置了三种委托方环境：高带宽笔记本电脑（LAPTOPHB，AWS r4.xlarge，3Gbps）、低带宽笔记本电脑（LAPTOPLB，350Mbps下行/13Mbps上行）、以及智能手机（MOBILE，Google Pixel 4a，6GB RAM，WiFi 350/13Mbps）。工人在 AWS c5.24xlarge（96核）上运行，分别位于 us-west-1 和 us-east-1。评估针对 MARLIN zkSNARK [14]。

**Q1：能否证明更大实例？** 在固定时间预算（100秒）下，LAPTOPHB 上本地可证明最大规模为 2^18 约束，而协作模式可达 2^21（8倍提升）；在 MOBILE 上本地仅能 2^16，协作模式可达 2^21（32倍提升）。在固定内存预算（3GB）下，所有设置下孤立模式和协作模式均可证明 2^25 约束，而本地仅能 2^17，提升 256 倍。

**Q2：委托的开销如何？** 端到端延迟：在 LAPTOPHB 上，孤立模式相比本地证明快 5.5-8.5 倍，协作模式快 5.5-9 倍，且相对于非隐私的工人本地证明只有 1.1-1.9 倍开销。在 MOBILE 上，协作模式快 22-26 倍。委托方在线时间：在 LAPTOPHB 上，孤立模式减少至少 19 倍，协作模式减少至少 592 倍。在 MOBILE 上，协作模式减少至少 96 倍。

**与 OB22 [36] 对比：** 在 LAPTOPHB 上，EOS 延迟比 OB22 快 6-8 倍，工人间通信减少 5 倍，委托方-工人通信减少 3 倍。

### 局限性与开放问题

本文协议仅适用于通用设置（universal setup）的 zkSNARK，对于电路特定设置的方案需另行设计。协议的安全性依赖于 PIOP 的一致性检查器和 PC 方案的抽取性，若底层 PIOP 不满足相关性质则无法适用。另外，在极低带宽环境下（如移动端，仅仅 13Mbps 上行），隔离模式仍面临较大通信瓶颈，未来可探索压缩通信或更高效的秘密共享方案。此外，本文仅实现了 MARLIN 一个实例，推广到更多 PIOP 和 PC 方案（如 PLONK [24]、Spartan [42]）需要进一步工作。

### 强关联论文

[14] Chiesa 等. Marlin: Preprocessing zkSNARKs with Universal and Updatable SRS. **EUROCRYPT 2020** [Google Scholar](https://scholar.google.com/scholar?q=Marlin)

[36] Ozdemir 和 Boneh. Experimenting with Collaborative zk-SNARKs: Zero-Knowledge Proofs for Distributed Secrets. **USENIX Security 2022** [Google Scholar](https://scholar.google.com/scholar?q=Experimenting+with+Collaborative+zk-SNARKs)

[19] Dayama 等. How to prove any NP statement jointly? Efficient Distributed-prover Zero-Knowledge Protocols. **PETS 2022** [Google Scholar](https://scholar.google.com/scholar?q=How+to+prove+any+NP+statement+jointly)

[41] Schoenmakers 等. Trinocchio: Privacy-Preserving Outsourcing by Distributed Verifiable Computation. **ACNS 2016** [Google Scholar](https://scholar.google.com/scholar?q=Trinocchio)

[28] Kanjalkar 等. Publicly Auditable MPC-as-a-Service with succinct verification and universal setup. **EuroS&P 2021 Workshops** [Google Scholar](https://scholar.google.com/scholar?q=Publicly+Auditable+MPC-as-a-Service+with+succinct+verification+and+universal+setup)

[46] Wu 等. DIZK: A Distributed Zero Knowledge Proof System. **USENIX Security 2018** [Google Scholar](https://scholar.google.com/scholar?q=DIZK)

[18] Damgård 等. Multiparty Computation from Somewhat Homomorphic Encryption. **CRYPTO 2012** [Google Scholar](https://scholar.google.com/scholar?q=Multiparty+Computation+from+Somewhat+Homomorphic+Encryption)

[29] Kate 等. Constant-Size Commitments to Polynomials and Their Applications. **ASIACRYPT 2010** [Google Scholar](https://scholar.google.com/scholar?q=Constant-Size+Commitments+to+Polynomials+and+Their+Applications)

[24] Gabizon 等. PLONK: Permutations over Lagrange-bases for Oecumenical Noninteractive arguments of Knowledge. **IACR ePrint 2019/953** [Google Scholar](https://scholar.google.com/scholar?q=PLONK)

[7] Block 和 Garman. Honest Majority Multi-Prover Interactive Arguments. **IACR ePrint 2022/557** [Google Scholar](https://scholar.google.com/scholar?q=Honest+Majority+Multi-Prover+Interactive+Arguments)


## 关键词

+ Eos隐私保护zkSNARK委托
+ 证明生成外包云计算
+ 多工作者联合证明生成
+ 抗合谋隐私保护协议
+ 通用设置zkSNARK优化
+ 移动设备证明委托
