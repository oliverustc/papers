---
title: "On the Security of KZG Commitment for VSS"
doi: 10.1145/3576915.3623127
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2023
---
## On the Security of KZG Commitment for VSS

## 发表信息

+ [原文链接]()

## 作者

+ Atsuki Momose 
+ [Sourav Das](Sourav%20Das.md)
+ [Ling Ren](Ling%20Ren.md)
## 笔记

### 背景与动机
Verifiable secret-sharing (VSS) 允许多个节点安全地恢复秘密，是多派计算、分布式密钥生成等协议的核心基础 [6,31]。当需要同时分享大量秘密时，高效的多秘密 VSS 依赖于常数大小的多项式承诺方案，尤其是 Kate、Zaverucha 和 Goldberg 提出的 KZG 承诺 [27]。然而，KZG 承诺在 VSS 环境下缺少两个关键性质。第一，它在标准 adversary 模型下未被证明是 degree binding 的，即无法保证承诺的多项式具有声明的度数，而该度数正是 VSS 的恢复阈值。缺少此性质会导致 VSS 的诚实节点根据不同的份额集合插值出不同的秘密。第二，KZG 承诺不支持用一个公共参考串同时处理不同度数的多项式，一旦阈值变化就需要重新执行昂贵的 powers-of-tau 设置。本文旨在弥补这两个缺陷，提出一种增强的 KZG 承诺，使其在标准模型（基于 SDH 假设）下达到 degree binding，并支持可重配置的阈值。

### 相关工作
[2] Abraham 等人. Bingo: Adaptively Secure Packed Asynchronous Verifiable Secret Sharing and Asynchronous Distributed Key Generation. **CCS 2022** [Google Scholar](https://scholar.google.com/scholar?q=Bingo%3A+Adaptively+Secure+Packed+Asynchronous+Verifiable+Secret+Sharing+and+Asynchronous+Distributed+Key+Generation)
> 核心思路：使用原始 KZG 承诺和双变量多项式实现多秘密 VSS，通信量 O(κ L n + κ n²)。
> 局限与区别：其 degree binding 证明依赖代数群模型 (AGM)，而本文在标准模型下用聚合 Feldman 承诺实现了 degree binding，无需 AGM。

[27] Kate 等人. Constant-size commitments to polynomials and their applications. **ASIACRYPT 2010** [Google Scholar](https://scholar.google.com/scholar?q=Constant-size+commitments+to+polynomials+and+their+applications)
> 核心思路：提出 KZG 多项式承诺，具有常数大小的承诺和评估证明。
> 局限与区别：原始 KZG 承诺的 strong correctness 性质是在 PDH 假设下证明的，但该性质对 VSS 所需的 degree binding 不充分；本文指出该问题并给出增强方案。

[41] Yurek 等人. hbACSS: How to Robustly Share Many Secrets. **NDSS 2022** [Google Scholar](https://scholar.google.com/scholar?q=hbACSS%3A+How+to+Robustly+Share+Many+Secrets)
> 核心思路：利用 IDA 和黑箱错误编码实现多秘密 VSS，通信量 O(κ L n + κ n³)。
> 局限与区别：其 dealer 指控步骤需要发送 O(n) 大小的消息，导致最坏情况通信 O(κ n³)；本文使用系统 RS 码实现常数大小的指控消息，将通信量降至 O(κ n²)。

[21] Feldman. A practical scheme for non-interactive verifiable secret sharing. **FOCS 1987** [Google Scholar](https://scholar.google.com/scholar?q=A+practical+scheme+for+non-interactive+verifiable+secret+sharing)
> 核心思路：提出线性大小的 Feldman 承诺，通过公开系数承诺实现度数的可验证性。
> 局限与区别：Feldman 承诺本身是线性大小，不适合单多项式场景；本文将其作为 degree proof 的聚合工具，与 KZG 承诺结合，实现了可检测的 degree binding。

[3] Alhaddad 等人. High-threshold avss with optimal communication complexity. **FC 2021** [Google Scholar](https://scholar.google.com/scholar?q=High-threshold+avss+with+optimal+communication+complexity)
> 核心思路：提出改进的异步 VSS，通信复杂度 O(κ n²)。
> 局限与区别：仅支持单秘密，不适用于多秘密批量共享。

[8] Bhat 等人. Randpiper–reconfiguration-friendly random beacons with quadratic communication. **CCS 2021** [Google Scholar](https://scholar.google.com/scholar?q=Randpiper–reconfiguration-friendly+random+beacons+with+quadratic+communication)
> 核心思路：设计可重配置的随机信标，利用 VSS 实现秘密分享。
> 局限与区别：其 VSS 基于原始 KZG，当阈值变化时需重置 powers-of-tau，本文的增强 KZG 避免了这一开销。

[11] Bünz 等人. Bulletproofs: Short proofs for confidential transactions and more. **S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Bulletproofs%3A+Short+proofs+for+confidential+transactions+and+more)
> 核心思路：提出基于内积论证的多项式承诺，无需可信设置。
> 局限与区别：Bulletproofs 的证明是 O(log n) 大小，但非交互且不具同态性；本文的增强 KZG 保持同态性且度数证明仅 O(d) 大小，适合 VSS 中的批量聚合。

[12] Cachin 等人. Asynchronous verifiable information dispersal. **SRDS 2005** [Google Scholar](https://scholar.google.com/scholar?q=Asynchronous+verifiable+information+dispersal)
> 核心思路：提出 IDA 协议，用于在异步网络中分发信息。
> 局限与区别：黑箱 IDA 无法通过单个符号检测消息有效性，本文利用系统 RS 码的特定结构实现了常数大小的指控。

[17] Damgård 等人. Scalable and unconditionally secure multiparty computation. **CRYPTO 2007** [Google Scholar](https://scholar.google.com/scholar?q=Scalable+and+unconditionally+secure+multiparty+computation)
> 核心思路：使用随机掩码多项式实现度数验证，用于 MPC 预处理阶段。
> 局限与区别：该方案需要 O(n) 轮交互，且不适用于异步网络；本文的 degree proof 在常数轮内完成，适合同步 VSS。

[19] Das 等人. Practical asynchronous distributed key generation. **S&P 2022** [Google Scholar](https://scholar.google.com/scholar?q=Practical+asynchronous+distributed+key+generation)
> 核心思路：利用 VSS 实现异步 DKG，通信量 O(κ n³)。
> 局限与区别：其底层 VSS 是单秘密的，本文的多秘密 VSS 可将共享多个秘密的成本线性摊销。

### 核心技术与方案
本文的核心贡献是增强 KZG 承诺，使其具备 degree binding 性质，并构造相应的多秘密 VSS 协议。整体方案分为两部分：增强的 KZG 承诺和基于该承诺的多秘密 VSS。

**增强的 KZG 承诺**。在原始 KZG 承诺（Commit, CreateWitness, VerifyEval）之外，添加两个函数 ProveDeg 和 VerifyDeg。ProveDeg 输入多个多项式 $\phi_1(\cdot),\dots,\phi_L(\cdot)$ 及其承诺 $v_k = g^{\phi_k(\tau)}$，输出 degree proof $\pi$。具体地，首先生成随机系数 $\rho_k = \mathsf{H}(\mathbf{v} \| k)$（通过随机预言机），然后计算聚合多项式 $\Phi(\cdot) = \sum_{k=1}^L \rho_k \phi_k(\cdot)$ 的系数 $\alpha_0,\dots,\alpha_d$，输出 $\pi = [g^{\alpha_1},\dots,g^{\alpha_d}]$。VerifyDeg 输入度数 $d$、承诺向量 $\mathbf{v}$、proof $\pi$、索引 $i$ 和评估值 $\phi(i)$，验证两个等式：$$ \prod_{k=1}^L g^{\rho_k \phi_k(i)} = \prod_{j=0}^d \pi_j^{i^j}, \qquad \prod_{k=1}^L e(v_k, g)^{\rho_k} = \prod_{j=0}^d e(\pi_j, g^{\tau^j}). $$ 第一个等式保证 $\Phi(i)$ 等于聚合评估值；第二个等式通过配对保证 $\Phi(\tau)$ 等于聚合承诺。由于 $\Phi(\cdot)$ 是度数 $d$ 的随机线性组合，若某个 $\phi_k(\cdot)$ 次数高于 $d$，则 $\Phi(\cdot)$ 将偏离实际程度，从而被检测。安全性证明基于 SDH 假设：若对手能产生 degree binding 的反例，则可构造 SDH 攻击。该增强方案使用统一的 powers-of-tau CRS $[g, g^\tau, \dots, g^{\tau^m}]$，支持所有 $0 < d \leq m$，无需因阈值变化而重新设置。

**多秘密 VSS 协议**。协议基于 IDA 和系统 RS 码，通信复杂度 $O(\kappa L n + \kappa n^2)$，容忍 $f < n/3$ 的静态破坏。主要步骤：
1. **Commit**：Dealer 生成 $L = f+1$ 个度数 $f$ 的随机多项式 $\phi_1(\cdot),\dots,\phi_L(\cdot)$ 分别分享秘密 $z_k$，并计算 KZG 承诺 $\mathbf{v}$ 和 degree proof $\pi_v$。然后，对每个节点 $i$，构造两个度数 $f$ 的编码多项式 $\psi_i(\cdot)$ 和 $\psi_i'(\cdot)$，满足 $\psi_i(k) = \phi_k(i) \oplus \rho_{i,k}$，$\psi_i'(k) = w_{i,k} \oplus \rho_{i,k}'$（其中 $w_{i,k}$ 是 KZG 见证，$\rho$ 是基于 PRF 的一次一密）。计算这些编码多项式的 KZG 承诺 $\mathbf{u}, \mathbf{u}'$ 及 degree proof $\pi_u, \pi_u'$。Dealer 通过 gradecast 广播承诺和 degree proof，并向每个节点 $j$ 发送编码符号 $\text{code}_{i,j} = (\psi_i(j), \psi_i'(j), \mu_{j,i}, \mu_{j,i}')$，其中 $\mu$ 是评估见证。
2. **Forward 与 Reconstruct**：节点 $i$ 收到所有 $\text{code}_{j,i}$ 后，验证每个编码多项式评估和 degree proof，若通过则转发给节点 $j$。节点 $j$ 收集 $f+1$ 个来自不同节点的正确编码符号，插值得到 $\psi_j(\cdot)$ 和 $\psi_j'(\cdot)$，解密得到份额 $s_{j,k} = \psi_j(k) \oplus \rho_{j,k}$ 和见证 $w_{j,k} = \psi_j'(k) \oplus \rho_{j,k}'$。
3. **Accuse**：若节点 $j$ 发现任何 $(s_{j,k}, w_{j,k}, v_k)$ 不是有效份额（即不通过 VerifyEval），则发送一个常数大小的指控消息，包含一个无效的编码符号对及相关见证，并揭示 PRF 密钥。
4. **Ready/Complete/Output**：节点发送 “ready” 如果它已转发所有编码、拥有有效份额且未收到有效指控。收到 $2f+1$ 个 “ready” 后发送 “complete”。最终，若收到超过 $f$ 个 “complete” 则输出 $b=1$ 及份额。

协议的 correctness 证明依赖于 degree binding 性质：至少 $f+1$ 个诚实节点的份额定义了一个唯一的度数 $f$ 多项式，其余节点的份额必须与之一致。Secrecy 通过模拟证明实现：模拟器可对诚实节点使用虚假秘密，因为 PRF 保证了编码多项式与真实秘密不可区分。

### 核心公式与流程

**[增强的 KZG 承诺 — ProveDeg]**
$$ \rho_k = \mathsf{H}(\mathbf{v} \| k), \quad \alpha_j = \sum_{k=1}^L \rho_k a_{k,j}, \quad \pi = [g^{\alpha_1}, \dots, g^{\alpha_d}] $$
> 作用：生成 degree proof，证明所有多项式的度数不超过 $d$。$\alpha_j$ 是聚合多项式 $\Phi(\cdot) = \sum \rho_k \phi_k(\cdot)$ 的系数。

**[增强的 KZG 承诺 — VerifyDeg]**
$$ \prod_{k=1}^L g^{\rho_k \phi_k(i)} = \prod_{j=0}^d \pi_j^{i^j}, \qquad \prod_{k=1}^L e(v_k, g)^{\rho_k} = \prod_{j=0}^d e(\pi_j, g^{\tau^j}) $$
> 作用：验证给定索引 $i$ 上的评估值与聚合多项式一致，且承诺值与多项式在 $\tau$ 处聚合一致。通过配对检查确保 $\Phi(\tau) = \sum \rho_k \phi_k(\tau)$。

**[多秘密 VSS — IDA 编码多项式]**
$$ \psi_i(k) = \phi_k(i) \oplus \rho_{i,k}, \quad \psi_i'(k) = w_{i,k} \oplus \rho_{i,k}', \quad \text{for } k \in [L] $$
> 作用：将节点 $i$ 的 $L$ 个份额和见证通过系统 RS 码编码为两个度数 $f$ 的多项式，然后用 KZG 承诺保护。$\rho$ 是一次一密 PRF。

**[新份额计算（DPSS）]**
$$ s_{j,i} = \sum_{k \in T_i} \lambda_k \cdot \hat{s}_{j,k,l}, \quad v_i = \prod_{k \in T_i} \hat{v}_{k,l}^{\lambda_k}, \quad w_{j,i} = \prod_{k \in T_i} \hat{w}_{j,k,l}^{\lambda_k} $$
> 作用：在动态委员会秘密共享中，新节点 $j$ 根据选定的 $T_i$ 和索引 $l$ 计算新份额、承诺和见证。$\lambda_k$ 是 Lagrange 系数。

### 实验结果
本文未提供实验评估。所有结果均为理论分析。协议 VSS 的通信复杂度为 $O(\kappa L n + \kappa n^2)$，其中 $L$ 为秘密数量，$n$ 为节点数，$\kappa$ 为安全参数。该复杂度在 $L = \Theta(n)$ 时为 $O(\kappa n^2)$，是线性通信（每个节点常量开销）的最优结果。DPSS 协议的通信为 $O(\kappa n^3)$，在常数轮内完成。计算开销方面，Dealer 的 KZG 承诺和见证生成需 $O(d L n)$ 次群指数运算，degree proof 生成需 $O(d L)$ 次；每个节点验证需 $O(L)$ 次配对和 $O(d)$ 次群指数运算。通过使用随机掩码多项式替代 Feldman 承诺作为 degree proof，可将配对操作降为 $O(1)$，但安全性不变。

### 局限性与开放问题
本文的多秘密 VSS 仅达到静态安全性，而 Bingo [2] 实现了适应性安全，将本方案的 degree binding 技术扩展到适应安全是未来工作。另一个局限是故障容忍度限于 $f < n/3$，若希望在同步模型下达到 $f < n/2$ 的最优阈值，IDA 方法的投票机制需要 $n - f$ 个诚实转发者，因此 $n - 2f$ 必须为 $\Omega(n)$ 才能保持线性通信，这本质上限制了阈值。此外，KZG 承诺的计算开销仍较高（$O(n)$ 次群指数），尽管已远低于一些替代方案，但实际部署中仍需权衡。

### 强关联论文

[2] Abraham et al. Bingo: Adaptively Secure Packed Asynchronous Verifiable Secret Sharing and Asynchronous Distributed Key Generation. **CCS 2022** [Google Scholar](https://scholar.google.com/scholar?q=Bingo%3A+Adaptively+Secure+Packed+Asynchronous+Verifiable+Secret+Sharing+and+Asynchronous+Distributed+Key+Generation)

[27] Kate et al. Constant-size commitments to polynomials and their applications. **ASIACRYPT 2010** [Google Scholar](https://scholar.google.com/scholar?q=Constant-size+commitments+to+polynomials+and+their+applications)

[41] Yurek et al. hbACSS: How to Robustly Share Many Secrets. **NDSS 2022** [Google Scholar](https://scholar.google.com/scholar?q=hbACSS%3A+How+to+Robustly+Share+Many+Secrets)

[21] Feldman. A practical scheme for non-interactive verifiable secret sharing. **FOCS 1987** [Google Scholar](https://scholar.google.com/scholar?q=A+practical+scheme+for+non-interactive+verifiable+secret+sharing)

[3] Alhaddad et al. High-threshold avss with optimal communication complexity. **FC 2021** [Google Scholar](https://scholar.google.com/scholar?q=High-threshold+avss+with+optimal+communication+complexity)

[8] Bhat et al. Randpiper–reconfiguration-friendly random beacons with quadratic communication. **CCS 2021** [Google Scholar](https://scholar.google.com/scholar?q=Randpiper–reconfiguration-friendly+random+beacons+with+quadratic+communication)

[11] Bünz et al. Bulletproofs: Short proofs for confidential transactions and more. **S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Bulletproofs%3A+Short+proofs+for+confidential+transactions+and+more)

[12] Cachin et al. Asynchronous verifiable information dispersal. **SRDS 2005** [Google Scholar](https://scholar.google.com/scholar?q=Asynchronous+verifiable+information+dispersal)

[17] Damgård et al. Scalable and unconditionally secure multiparty computation. **CRYPTO 2007** [Google Scholar](https://scholar.google.com/scholar?q=Scalable+and+unconditionally+secure+multiparty+computation)

[19] Das et al. Practical asynchronous distributed key generation. **S&P 2022** [Google Scholar](https://scholar.google.com/scholar?q=Practical+asynchronous+distributed+key+generation)


## 关键词

+ 多项式承诺
+ 度绑定性
+ 可验证秘密共享
+ KZG 承诺
+ 强 Diffie-Hellman 假设