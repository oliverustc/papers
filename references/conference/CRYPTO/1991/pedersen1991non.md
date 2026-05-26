---
title: "Non-Interactive and Information-Theoretic Secure Verifiable Secret Sharing"
标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 1991
modified: 2025-04-08 18:35:24
---

## Non-Interactive and Information-Theoretic Secure Verifiable Secret Sharing

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/3-540-46766-1_9)

## 作者

+ Torben Pryds Pedersen

## 笔记

### 背景与动机
秘密共享使得一个秘密可以分散成多份份额，由多个参与者保管。Verifiable Secret Sharing (VSS) 在此基础上增加了对份额的验证功能，确保每个参与者收到的份额与其他份额一致。早期 VSS 方案依赖交互过程，参与者需要相互通信或与分发者多次交换消息才能验证份额，这在分发者与参与者之间缺乏信任的许多实际场景中（例如通过邮件分发秘密）是一个严重瓶颈。Feldman 于 1987 年提出了第一个非交互式的 VSS 方案 [Fel87]，该方案依赖同态加密特性，但秘密的隐私依赖于计算的不可行性假设（如离散对数难题），无法提供信息论安全性，即即使攻击者在未来拥有无限计算资源，秘密也无法被保证安全。本文的设计目标是构造一个既非交互、又在信息论意义上不泄露任何关于秘密的信息的 VSS 方案。作者通过在 Shamir 秘密共享方案上叠加一个具有特殊性质的承诺方案，实现了份额的验证与秘密的无条件隐藏，同时保持了大规模拒绝合谋的安全性（阈值 k 可由系统设定）。这一构造填补了非交互与信息论安全之间长期存在的空白。

### 相关工作

[Sha79] Shamir. How to Share a Secret. **Comm. ACM 1979** [Google Scholar](https://scholar.google.com/scholar?q=How+to+Share+a+Secret)
> 核心思路：利用多项式插值，将秘密编码为多项式常数项，各参与者获得多项式上的点值，任意 k 点可恢复秘密。
> 局限与区别：方案仅提供秘密共享，无验证机制，且依赖参与者之间的信任；本文在其基础上增加了承诺与验证。

[Bla79] Blakley. Safeguarding Cryptographic Keys. **AFIPS 1979** [Google Scholar](https://scholar.google.com/scholar?q=Safeguarding+Cryptographic+Keys)
> 核心思路：利用多维几何，秘密作为空间中一点，每个份额对应一个超平面方程。
> 局限与区别：与 Shamir 方案类似，缺少验证功能，且不兼容后续的承诺构造；本文未采用几何方法。

[BGW88] Ben-Or, Goldwasser, Widgerson. Completeness Theorems for Non-Cryptographic Fault-Tolerant Distributed Computation. **STOC 1988** [Google Scholar](https://scholar.google.com/scholar?q=Completeness+Theorems+for+Non-Cryptographic+Fault-Tolerant+Distributed+Computation)
> 核心思路：构造了信息论安全的 VSS 方案，并用于安全多方计算，允许少于 n/3 的不诚实参与者。
> 局限与区别：方案是交互式的，验证过程需要参与者之间多次通信；本文的目标是非交互式。

[CCD88] Chaum, Crépeau, Damgård. Multiparty Unconditionally Secure Protocols. **STOC 1988** [Google Scholar](https://scholar.google.com/scholar?q=Multiparty+Unconditionally+Secure+Protocols)
> 核心思路：构建了同样信息论安全的 VSS 方案，作为设计无条件安全多方协议的基础模块。
> 局限与区别：与 [BGW88] 类似，属于交互式方案；本文避免了交互，且不限制不诚实参与者的数量上限。

[Fel87] Feldman. A Practical Scheme for Non-Interactive Verifiable Secret Sharing. **FOCS 1987** [Google Scholar](https://scholar.google.com/scholar?q=A+Practical+Scheme+for+Non-Interactive+Verifiable+Secret+Sharing)
> 核心思路：利用同态加密（如指数函数）广播加密后的多项式系数，每个参与者通过同态性质验证份额的正确性。
> 局限与区别：方案的计算安全性破坏了秘密的信息论隐私；本文通过使用新的承诺方案实现了信息论安全。

[BCC88] Brassard, Chaum, Crépeau. Minimum Disclosure Proofs of Knowledge. **J. Comput. Syst. Sci. 1988** [Google Scholar](https://scholar.google.com/scholar?q=Minimum+Disclosure+Proofs+of+Knowledge)
> 核心思路：提出了承诺协议与最小泄露证明系统，用于秘密共享中的零知识验证。
> 局限与区别：该工作的承诺方案不具有本文所需的批量承诺可加性；本文的承诺方案是其变体，专门适配 Shamir 方案的多项式结构。

[RB89] Rabin, Ben-Or. Verifiable Secret Sharing and Multiparty Protocols with Honest Majority. **STOC 1989** [Google Scholar](https://scholar.google.com/scholar?q=Verifiable+Secret+Sharing+and+Multiparty+Protocols+with+Honest+Majority)
> 核心思路：构造了允许少于 n/2 的不诚实参与者的交互式 VSS，弱化了 [BGW88] 和 [CCD88] 的阈值要求。
> 局限与区别：仍然需要交互，且安全性依赖于秘密份额的纠错码传输；本文在非交互框架下严格避免了交互。

[Ped91] Pedersen. Distributed Provers with Applications to Undeniable Signatures. **EUROCRYPT 1991** [Google Scholar](https://scholar.google.com/scholar?q=Distributed+Provers+with+Applications+to+Undeniable+Signatures)
> 核心思路：提出了一种非交互 VSS，但要求公开值 g^s 已知；秘密不一定是已知的。
> 局限与区别：该方案无法应用于 s 未知的场景；本文通过将 g^s 替换为承诺 E(s,t) 消除了这一限制，实现了信息论安全。

### 核心技术与方案
本文的核心构造是将 Shamir 秘密共享方案与一个信息论安全的承诺方案深度耦合，实现非交互的份额验证。

**承诺方案**：设 $p$ 和 $q$ 为大素数，$q \mid p-1$，$G_q$ 为 $\mathbb{Z}_p^*$ 中阶为 $q$ 的唯一子群，$g$ 和 $h$ 为 $G_q$ 中两个公开的生成元，且离散对数 $\log_g h$ 未知。承诺者对秘密 $s \in \mathbb{Z}_q$ 的承诺是 $E(s,t) = g^s h^t$，其中 $t \in \mathbb{Z}_q$ 随机选取。该承诺在信息论上完美隐藏 $s$（因为 $E(s,t)$ 在 $G_q$ 上均匀分布），但在计算上绑定——若承诺者可打开为两个不同的 $(s,t)$ 和 $(s',t')$，则意味着他能计算出 $\log_g h = (s - s')/(t' - t) \bmod q$，这在计算上被假定为不可行。

**可验证秘密共享方案**：分发者 D 有二阶段流程。
阶段一（分发与验证）：
1. D 公开承诺 $E_0 = E(s,t)$，其中 $t$ 随机选取。
2. D 选择多项式 $F(x) = s + F_1 x + \cdots + F_{k-1} x^{k-1} \in \mathbb{Z}_q[x]$，并随机选取辅助多项式 $G(x) = t + G_1 x + \cdots + G_{k-1} x^{k-1} \in \mathbb{Z}_q[x]$。D 公开系数承诺 $E_i = E(F_i, G_i)$，$i=1,\dots,k-1$。
3. D 秘密发送 $(s_i, t_i) = (F(i), G(i))$ 给参与者 $P_i$。
4. 每个 $P_i$ 验证验证等式：$$E(s_i, t_i) = \prod_{j=0}^{k-1} E_j^{i^j}.$$

正确性直观：如果 D 诚实遵循协议，则 $E(s_i, t_i) = g^{F(i)} h^{G(i)} = \prod_{j=0}^{k-1} g^{F_j i^j} h^{G_j i^j} = \prod_{j=0}^{k-1} E_j^{i^j}$。

阶段二（秘密恢复）：任意 k 个满足验证等式的参与者可用 Lagrange 插值恢复 $s = \sum_{i \in S} a_i s_i$，其中 $a_i = \prod_{j \in S, j \neq i} \frac{i}{i-j}$。

**安全性分析**：
- 隐藏性（Theorem 4.4）：对于任意少于 k 个参与者的视图 $view_S$，秘密 $s$ 的后验分布与先验一致，均为均匀分布。证明利用 $E_0 = E(s,t)$ 的完美隐藏性以及多项式插值的唯一性：对于任意候选 $s$，存在唯一的 $t$ 和多项式 $F,G$ 与公布的 $E_i$ 一致。
- 一致性（Theorem 4.3）：如果 D 分发不一致的份额，他可以找到两个不同的 k 元子集恢复出不同的 $(s,t)$ 和 $(s',t')$，使得 $E_0 = E(s,t) = E(s',t')$，这等价于计算 $\log_g h$。因此在计算离散对数困难的假设下，D 无法成功。

**渐进复杂度**：秘密长度为 $|q|$ 比特，份额大小为 $2|q|$ 比特，信息率 $1/2$。分发阶段：D 计算 $k$ 个承诺，约需 $2|q|k$ 次模乘。验证阶段：每个参与者需计算 $k-1$ 次幂运算与一次承诺，约 $(2|q|+1)k$ 次模乘。

### 核心公式与流程

**[承诺方案定义]**
$$E(s,t) = g^s h^t$$
> 作用：对秘密 $s$ 进行完美隐藏、计算绑定的承诺。随机数 $t$ 保证每个承诺在 $G_q$ 上均匀分布。

**[份额验证等式]**
$$E(s_i, t_i) = \prod_{j=0}^{k-1} E_j^{i^j}$$
> 作用：参与者 $P_i$ 利用公开的承诺 $E_0, \dots, E_{k-1}$ 验证收到的份额 $(s_i, t_i)$ 是否与分发者的多项式一致。该等式利用同态性质 $E(a,t)E(b,u) = E(a+b \bmod q, t+u \bmod q)$。

**[秘密恢复公式]**
$$s = \sum_{i \in S} \left( \prod_{j \in S, j \neq i} \frac{i}{i - j} \right) s_i$$
> 作用：任意满足验证等式的 k 个参与者 $S$ 通过 Lagrange 插值计算秘密 $s$。同理可恢复 $t$。

**[作弊者计算离散对数的条件]**
$$\log_g h = \frac{s - s'}{t' - t} \bmod q$$
> 作用：如果分发者能构造两组从不同子集恢复出的不同 $(s,t)$ 和 $(s',t')$ 满足同一 $E_0$，则他可直接解出离散对数，从而证明一致性依赖于计算假设。

### 实验结果
本文是理论构造论文，未提供传统意义上的实验数据或仿真。但作者在 Section 4.3 给出了详细的复杂度估算：
- 信息率定义为秘密比特长度除以份额比特长度，值为 $1/2$，即每个秘密比特对应 2 比特份额。
- 分发阶段：计算每个承诺约需 $2|q|$ 次模乘，总计 $2|q|k$ 次模乘。
- 验证阶段：对于参与者 $P_1$，指数均为 $i^1 \in \{1,2,\dots,n\}$，计算量可优化至约 $3|q| + (k-2)(|q| + \log q)$ 次模乘，最坏情况为 $(2|q|+1)k$ 次模乘。
- 与 Feldman 方案 [Fel87] 的比较：Feldman 方案使用 $g^x$ 加密 $l = O(\log |q|)$ 比特的硬核位，当加密同长度秘密时，计算量类似；区别在于 Feldman 方案在秘密隐私上依赖计算假设，本文方案在份额一致性上依赖计算假设。

### 局限性与开放问题
本文方案的核心权衡是：隐私是无条件的（信息论安全），但份额的一致性依赖于“分发者不能计算离散对数”的计算假设。作者在论文末尾指出，非交互模型下无法同时实现信息论安全的隐私与一致性——任何满足信息论隐私的非交互 VSS 都允许一个拥有无限计算能力的敌手分发不一致份额。这一结论暗示了本质上的不可能性，但并未探索是否存在其他模型（如假设有可信初始化阶段、或允许辅助输入）绕过这一下限。此外，方案的信息率为 $1/2$，低于 Shamir 原始方案的 $1$，存在进一步优化的空间。

### 强关联论文

[Sha79] Shamir. How to Share a Secret. **Comm. ACM 1979** [Google Scholar](https://scholar.google.com/scholar?q=How+to+Share+a+Secret)

[Fel87] Feldman. A Practical Scheme for Non-Interactive Verifiable Secret Sharing. **FOCS 1987** [Google Scholar](https://scholar.google.com/scholar?q=A+Practical+Scheme+for+Non-Interactive+Verifiable+Secret+Sharing)

[BGW88] Ben-Or, Goldwasser, Widgerson. Completeness Theorems for Non-Cryptographic Fault-Tolerant Distributed Computation. **STOC 1988** [Google Scholar](https://scholar.google.com/scholar?q=Completeness+Theorems+for+Non-Cryptographic+Fault-Tolerant+Distributed+Computation)

[CCD88] Chaum, Crépeau, Damgård. Multiparty Unconditionally Secure Protocols. **STOC 1988** [Google Scholar](https://scholar.google.com/scholar?q=Multiparty+Unconditionally+Secure+Protocols)

[RB89] Rabin, Ben-Or. Verifiable Secret Sharing and Multiparty Protocols with Honest Majority. **STOC 1989** [Google Scholar](https://scholar.google.com/scholar?q=Verifiable+Secret+Sharing+and+Multiparty+Protocols+with+Honest+Majority)

[BCC88] Brassard, Chaum, Crépeau. Minimum Disclosure Proofs of Knowledge. **J. Comput. Syst. Sci. 1988** [Google Scholar](https://scholar.google.com/scholar?q=Minimum+Disclosure+Proofs+of+Knowledge)

[Ped91] Pedersen. Distributed Provers with Applications to Undeniable Signatures. **EUROCRYPT 1991** [Google Scholar](https://scholar.google.com/scholar?q=Distributed+Provers+with+Applications+to+Undeniable+Signatures)


## 关键词

+ 可验证秘密分享
+ 非交互式
+ 信息论安全
+ 秘密重建
+ 零知识