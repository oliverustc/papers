---
title: "Short-lived zero-knowledge proofs and signatures"
标题简称:
论文类型: conference
会议简称: ASIACRYPT
发表年份: 2022
created: 2025-04-28 15:00:19
modified: 2025-04-28 15:01:11
---

## Short-lived zero-knowledge proofs and signatures

## 发表信息

+ [原文链接]([Short-lived Zero-Knowledge Proofs and Signatures | SpringerLink](https://link.springer.com/chapter/10.1007/978-3-031-22969-5_17))

## 作者

+ [Arasu Arun](Arasu%20Arun.md)
+ [[Joseph Bonneau]] 
+ Jeremy Clark 

## 笔记

### 背景与动机

数字签名和零知识证明通常具有永久的可验证性，但在许多实际场景中，例如 DKIM 邮件签名 [53]，签名只需要在几分钟内有效，而永久的认证反而会在数据泄露时成为长期伪造证据。传统解决方案如定期轮换密钥并公布旧密钥 [45]，或使用指定验证者证明 [49]，都要求交互或依赖第三方后续行为。本文旨在设计一种非交互、公开可验证的证明或签名，它在指定时间间隔 \(t\) 内是可靠且匿名的，但经过 \(t\) 时间后，任何人都可以伪造出与真实证明不可区分的副本，从而天然实现可否认性。关键挑战在于如何在不引入交互或可信第三方的前提下，使伪造过程必须消耗恰好 \(t\) 步顺序计算，并确保真实证明与伪造证明在密码学上不可区分。

### 相关工作

[8] Baldimtsi et al. Indistinguishable Proofs of Work or Knowledge. **EUROCRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=Indistinguishable+Proofs+of+Work+or+Knowledge)
> 核心思路：提出“工作或知识”证明，证明者可以证明要么知道证据要么完成了并行化的工作量证明。
> 局限与区别：所需工作量是并行化的，不保证顺序时间延迟；本文使用顺序 VDF，确保不可加速。

[16] Boneh et al. Verifiable Delay Functions. **CRYPTO 2018** [Google Scholar](https://scholar.google.com/scholar?q=Verifiable+Delay+Functions)
> 核心思路：形式化定义 VDF，并给出基于重复平方的构造。
> 局限与区别：VDF 本身不提供零知识或可否认性；本文利用 VDF 的时序性构造短时存活证明。

[32] Cramer et al. Proofs of partial knowledge and simplified design of witness hiding protocols. **CRYPTO 1994** [Google Scholar](https://scholar.google.com/scholar?q=Proofs+of+partial+knowledge+and+simplified+design+of+witness+hiding+protocols)
> 核心思路：给出 Σ-协议的析取（Σ-OR）构造，用于证明多个陈述中至少一个为真。
> 局限与区别：直接使用 Σ-OR 组合 VDF 会导致可区分性问题；本文通过改造挑战或引入零知识 VDF 规避。

[38] Ferradi et al. slow motion zero knowledge identifying with colliding commitments. **ICISC 2015** [Google Scholar](https://scholar.google.com/scholar?q=slow+motion+zero+knowledge+identifying+with+colliding+commitments)
> 核心思路：提出“衰落签名”，使用 RSW 时间锁谜题，验证者需执行 t 步才能验证。
> 局限与区别：验证过程慢（需 t 步），且需要可信第三方预计算；本文验证高效，且不需要第三方。

[49] Jakobsson et al. Designated verifier proofs and their applications. **EUROCRYPT 1996** [Google Scholar](https://scholar.google.com/scholar?q=Designated+verifier+proofs+and+their+applications)
> 核心思路：证明形如“x 为真或我知道验证者的私钥”，使证明仅对指定验证者可信。
> 局限与区别：可否认性局限于指定验证者；本文的短时存活证明对任何人公开可验证且时间后全体可伪造。

[64] Pietrzak K. Simple verifiable delay functions. **ITCS 2018** [Google Scholar](https://scholar.google.com/scholar?q=Simple+verifiable+delay+functions)
> 核心思路：基于重复平方的多轮递归证明，证明大小 \(O(\log t)\)。
> 局限与区别：同样不具有零知识性；本文将其用于重新随机化改进。

[72] Specter et al. KeyForge: non-attributable email from forward-forgeable signatures. **USENIX Security 2021** [Google Scholar](https://scholar.google.com/scholar?q=KeyForge+non-attributable+email+from+forward-forgeable+signatures)
> 核心思路：通过后续发布秘密值或时间戳更新使签名可伪造。
> 局限与区别：需要未来行动（公布密钥或时间戳者签名）才能实现可否认性；本文无需后续行动。

[77] Wesolowski B. Efficient verifiable delay functions. **EUROCRYPT 2019** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+verifiable+delay+functions)
> 核心思路：基于随机素数挑战的紧凑 VDF 证明，证明大小为两个群元素。
> 局限与区别：不隐藏 VDF 输出，直接使用会导致可区分性；本文基于其构造零知识 VDF 和水印 VDF。

### 核心技术与方案

**整体框架**  
本文的所有构造均围绕一个核心思想：将待证明的陈述 \(x\) 与“在时限 \(t\) 内无法完成的 VDF 计算”进行析取。证明者若知道 \(x\) 的证据，可在少于 \(t\) 的时间内生成证明；伪造者则必须计算 VDF 才能完成析取的另一分支。由于 VDF 保证 \(t\) 步顺序计算不可并行加速，若验证者在信标 \(b\) 公布后 \(\Delta < t\) 时间内收到证明，可确信证明不是伪造的。

**通用构造（§5）**  
给定任意 NP 关系 \(R\) 和任意 VDF，构造关系 \(R_{\text{VDF}} = \{(b, (y,\pi)) \mid \text{VDF.Verify}(b,y,\pi)\}\)，然后将 \(R\) 与 \(R_{\text{VDF}}\) 取析取（使用通用 NIZK 系统）。证明者提供真实证据即可；伪造者先计算 VDF.Eval(\(b\)) 得到 \((y,\pi)\) 再使用 VDF 分支。该方案获得可重用伪造性：一次 VDF 计算可用于伪造任意多个不同 \(x\) 的证明。但通用 NIZK 效率低（约 60 s）。

**基于 Σ-协议的构造**  
本文重点针对 Σ-协议设计高效方案。直接采用 Σ-OR 组合 VDF 会导致可区分性，因为 VDF 输出 \(y\) 是唯一确定的，证明者和伪造者将泄露不同 \(y\)。为此提出三种改进：

1. **Σ-Precomp（§6.2）**：证明者在预计算阶段随机选取 \(b^*\) 并计算 VDF(\(b^*\))。在生成证明时，通过调整挑战 \(c_2 = b \oplus b^*\) 将 VDF 输入映射到已计算的 \(b^*\)，而伪造者无法预知挑战，必须计算 VDF(\(b \oplus c_2\))。该方案避免泄露真实 \(y\)，但每次证明需预计算一次 VDF，不具可重用性。

2. **Σ-rrVDF（§6.3）**：引入重新随机化 VDF，即给定一个 VDF 解 \((b,y,\pi)\)，可快速生成另一个随机输入的解。这样证明者只需预计算一次，后续可通过重新随机化产生新的随机解用于多次证明，改善预计算开销。

3. **Σ-zkVDF（§7）**：构造零知识 VDF，使其不泄露输出 \(y\)。文中基于 Wesolowski 证明设计了一个 Σ-协议（Protocol 2），用盲化处理 \(a = y \cdot h^v\) 替代直接输出 \(y\)，并给出相应的证明算法。将 Σ-zkVDF 与待证 Σ-协议进行标准 Σ-OR 组合即得短时存活证明，且获得可重用伪造性：一次 VDF 计算可用于所有关于同一信标 \(b\) 的伪造。

**短时存活签名（§8）**  
签名是证明的特殊情况。文中给出三种构造：
- **Sign-Trapdoor（§8.1）**：直接使用陷门 VDF，签名即为 VDF 输出 \((y,\pi)\)，私钥为 VDF 陷门（如 RSA 因数）。由于 VDF 是确定性的，签名与伪造输出完全相同，实现完美不可区分。但无可重用性。
- **Sign-Watermark（§8.2）**：使用可水印 VDF，将消息 \(m\) 作为水印嵌入 VDF 证明的生成中（修改 Fiat-Shamir 挑战为 \(\ell \gets \text{HashToPrime}(y \parallel \mu)\)）。这样一次 VDF 预计算后，通过快速重算水印可伪造任意消息，实现可重用伪造性（但限于同一签名者）。
- 通用方法（§5）也可将任何签名方案转化为短时存活签名，但效率低。

**安全性直觉**  
所有方案的 \(t\)-可靠性（\(t\)-Soundness）都归结于 VDF 的时序性：任何在少于 \(t\) 步内输出合法证明的敌手，要么提取出证据，要么赢得 VDF 时序性游戏。可区分性依赖随机性（信标 \(b\) 的不可预测性）和零知识性质。可重用伪造性依赖于 VDF 计算与具体语句无关，或通过水印/盲化技术实现。

**渐进复杂度**  
- 通用 zk-SNARK：证明大小恒定（～300 B），验证 <10 ms，但证明耗时～60 s。  
- Σ-zkVDF：额外开销 545 B，证明时间约 120 ms（含两次幂指数操作）。  
- Sign-Trapdoor：额外 272 B，签名时间约 10 ms。  
- Sign-Watermark：额外 272 B，签名时间约 10 ms。  
- 重新随机化 Pietrzak 证明：在建议硬件速度下，重随机化可在数分钟完成（表3）。

### 核心公式与流程

**[VDF 关系定义]**
$$
R_{\text{VDF}} = \{(x = b, w = (y, \pi)) \mid \text{VDF.Verify}(b, y, \pi) = \text{Accept}\}
$$
> 作用：将验证 VDF 解本身表述为 NP 关系，用于析取。

**[Σ-Precomp 协议（Protocol 1）— 伪造算法关键步骤]**
$$
\begin{aligned}
&\text{Forge}(pp, x, b):\\
&1.\quad (\tilde{a}, \tilde{c}_1, \tilde{z}) \gets \Sigma_R.\text{Simulate}(x)\\
&2.\quad c \gets \mathcal{O}(x \parallel b \parallel \tilde{a})\\
&3.\quad c_2 \gets c \oplus \tilde{c}_1\\
&4.\quad (y, \pi_\text{VDF}) \gets \text{VDF.Eval}(b \oplus c_2)
\end{aligned}
$$
> 作用：伪造者通过模拟 Σ-协议的 R 分支，使得 VDF 输入成为随机值，必须执行 VDF 计算。

**[zk-PoKP 协议（Protocol 2）— 零知识证明幂等性]**
$$
\begin{aligned}
&\text{Prove}(g, u, y):\\
&1.\quad v \stackrel{\$}{\gets} [-B, B]\\
&2.\quad a \gets y \cdot h^v\\
&3.\quad \ell \gets \text{HashToPrime}(a)\\
&4.\quad u = q_1\ell + r_1,\; v = q_2\ell + r_2\\
&5.\quad Q \gets g^{q_1} h^{q_2}\\
&6.\quad \pi \gets \langle a, Q, r_2\rangle
\end{aligned}
$$
> 作用：盲化输出 \(y\) 为 \(a\)，使得 VDF 计算不被泄露，用于 Σ-zkVDF 构造。

**[Sign-Trapdoor 协议（Protocol 3）— 签名流程]**
$$
\begin{aligned}
&\text{Sign}(sk, m, b): \quad x \gets \text{Hash}(m \| b),\; \sigma \gets \text{tdVDF.TrapdoorEval}(sk, x)\\
&\text{Forge}(m, b): \quad x \gets \text{Hash}(m \| b),\; \sigma \gets \text{tdVDF.Eval}(x)
\end{aligned}
$$
> 作用：签名使用陷门高效计算 VDF，伪造必须执行顺序计算。由于 VDF 是确定函数，两者输出完全一致。

### 实验结果

实验硬件为 2.3 GHz 8-Core Intel Core i9 笔记本电脑，16 GB 内存。使用 2048 位 RSA 群（安全参数 λ = 128）。对比基线包括 zk-SNARK（Groth16）和三种 Σ-协议构造。表2显示：通用 zk-SNARK 方案证明时间约 60 s，完全不实用；Σ-zkVDF 证明时间仅 120 ms，额外证明大小 545 B；Sign-Trapdoor 和 Sign-Watermark 签名时间约 10 ms，额外大小 272 B。表3展示了 Pietrzak 证明重新随机化的性能：在硬件速度为 \(2^{25}\) 次运算/秒时，延迟参数 \(t\) 对应 1 分钟时，RSA-2048 重随机化需 28 s，RSA-1024 需 8 s；延迟 15 分钟时分别需 110 s 和 35 s。在更快的硬件（\(2^{30}\) ops/s）下，1 分钟延迟对应 145 s（RSA-2048）。这些数值表明，短时存活签名和 Σ-zkVDF 计算开销极低，适合实际部署，但可重用伪造（重随机化）仍需分钟级时间，适合在后台执行。

### 局限性与开放问题

所有构造依赖 VDF 计算，目前需要有人实际执行该计算才能实现伪造；未来可探索附加于现有连续 VDF 计算（如区块链）或去中心化协议。Σ-zkVDF 仅提供 1-可重用伪造性，能否扩展至 k-可重用（通过 RSA 累加器合并历史信标）是开放问题。基于 Wesolowski 证明的零知识 VDF 无法利用 Pietrzak 类型的更高效重新随机化；构造 Pietrzak 风格的零知识 VDF 会显著改善伪造速度。水印 VDF 签名需要每个签名者独立的 VDF 计算，理想方案应允许一次 VDF 计算（如通过累加器）伪造来自不同签名者的证明。最后，可将现有基于 Σ-协议的高效证明系统（如 Bulletproofs、PLONK）的内核替换为本文的短时存活 Σ-协议，获得无需编码 VDF 电路的通用短时存活 SNARK。

### 强关联论文

[8] Baldimtsi, F., Kiayias, A., Zacharias, T., Zhang, B. Indistinguishable Proofs of Work or Knowledge. **EUROCRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=Indistinguishable+Proofs+of+Work+or+Knowledge)

[16] Boneh, D., Bonneau, J., Bünz, B., Fisch, B. Verifiable Delay Functions. **CRYPTO 2018** [Google Scholar](https://scholar.google.com/scholar?q=Verifiable+Delay+Functions)

[32] Cramer, R., Damgård, I., Schoenmakers, B. Proofs of partial knowledge and simplified design of witness hiding protocols. **CRYPTO 1994** [Google Scholar](https://scholar.google.com/scholar?q=Proofs+of+partial+knowledge+and+simplified+design+of+witness+hiding+protocols)

[38] Ferradi, H., Géraud, R., Naccache, D. slow motion zero knowledge identifying with colliding commitments. **ICISC 2015** [Google Scholar](https://scholar.google.com/scholar?q=slow+motion+zero+knowledge+identifying+with+colliding+commitments)

[49] Jakobsson, M., Sako, K., Impagliazzo, R. Designated verifier proofs and their applications. **EUROCRYPT 1996** [Google Scholar](https://scholar.google.com/scholar?q=Designated+verifier+proofs+and+their+applications)

[64] Pietrzak, K. Simple verifiable delay functions. **ITCS 2018** [Google Scholar](https://scholar.google.com/scholar?q=Simple+verifiable+delay+functions)

[72] Specter, M.A., Park, S., Green, M. KeyForge: non-attributable email from forward-forgeable signatures. **USENIX Security 2021** [Google Scholar](https://scholar.google.com/scholar?q=KeyForge+non-attributable+email+from+forward-forgeable+signatures)

[77] Wesolowski, B. Efficient verifiable delay functions. **EUROCRYPT 2019** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+verifiable+delay+functions)


## 关键词

+ 短暂证明
+ 可验证延迟函数
+ 时间约束
+ 零知识签名
+ 顺序计算