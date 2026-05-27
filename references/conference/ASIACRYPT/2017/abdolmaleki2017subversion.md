---
title: "A subversion-resistant SNARK"
doi: 10.1007/978-3-319-70700-6_1
标题简称:
论文类型: conference
会议简称: ASIACRYPT
发表年份: 2017
modified: 2025-04-08 17:21:36
---
## A subversion-resistant SNARK

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-319-70700-6_1)

## 作者

+ Behzad Abdolmaleki
+ Karim Baghery
+ Helger Lipmaa
+ Michał Zając

## 笔记

### 背景与动机
传统的zk-SNARK完全依赖于公共参考字符串（CRS）的正确生成，但Snowden事件之后，密码学社群高度关注CRS生成者可能被颠覆（subversion）的威胁。Bellare等人在ASIACRYPT 2016 [2]中首次系统研究了该问题，证明了同时实现颠覆可靠性（subversion soundness）和（即使是标准）零知识在非交互设置下是不可能的；但他们也构造了一个满足（标准）可靠性和计算性颠覆零知识（Sub-ZK）的NP论证系统。然而，该方案通信量是线性的，且构造复杂，难以直接用于构造高效的非交互零知识论证（SNARK）。当前最高效的SNARK是Groth于EUROCRYPT 2016 [27]基于二次算术程序（QAP）的zk-SNARK，其论证仅包含3个双线性群元素，验证者仅需计算3对配对和与陈述规模线性相关的指数运算。本文填补的空白是：如何以最小的改动使Groth的顶级SNARK同时具备完美可组合的颠覆零知识（即使在恶意生成的CRS下论证也保持零知识）和在颠覆通用双线性群模型（Sub-GBGM）中的适应性知识可靠性。

### 相关工作

[2] Bellare等. NIZKs with an Untrusted CRS: Security in the Face of Parameter Subversion. **ASIACRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=NIZKs+with+an+Untrusted+CRS%3A+Security+in+the+Face+of+Parameter+Subversion)
> 核心思路：首次在非交互零知识中定义了颠覆零知识（Sub-ZK），证明颠覆可靠性与零知识不可兼得，并构造了满足标准可靠性和计算性Sub-ZK的NP论证系统。
> 局限与区别：该构造复杂且通信量线性，不满足SNARK的简洁性；本文则聚焦于将最简洁的SNARK改造为Sub-ZK，且实现的是统计/完美Sub-ZK，而非计算性。

[27] Groth. On the Size of Pairing-Based Non-Interactive Arguments. **EUROCRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=On+the+Size+of+Pairing-Based+Non-Interactive+Arguments)
> 核心思路：提出了当时最高效的zk-SNARK，论证仅3个群元素，验证者仅需3对配对和与输入长度线性相关的预计算指数运算。
> 局限与区别：未考虑颠覆攻击；其CRS不可公开验证，且未提供CRS陷阱门可提取性，因此直接使用无法满足Sub-ZK。

[22] Gennaro等. Quadratic Span Programs and Succinct NIZKs without PCPs. **EUROCRYPT 2013** [Google Scholar](https://scholar.google.com/scholar?q=Quadratic+Span+Programs+and+Succinct+NIZKs+without+PCPs)
> 核心思路：引入二次算术程序（QAP）作为描述电路可满足性的多项式语言，使得验证者可以通过少量配对运算检查多项式等式。
> 局限与区别：构造的SNARK效率低于Groth [27]且同样未考虑颠覆性；本文基于Groth SNARK，继承了其高效性。

[17] Danezis等. Square Span Programs with Applications to Succinct NIZK Arguments. **ASIACRYPT 2014** [Google Scholar](https://scholar.google.com/scholar?q=Square+Span+Programs+with+Applications+to+Succinct+NIZK+Arguments)
> 核心思路：提出平方跨度程序（SSP）和相关的知识假设（如PKE）用于构造SNARK。
> 局限与区别：本文采用了相同类型的非可验证假设（BDH-KE），但将其适配到Sub-ZK的陷阱门提取场景；PKE假设的简化版本（BDH-KE）正是本文Sub-ZK证明的核心工具。

[6] Ben-Sasson等. Secure Sampling of Public Parameters for Succinct Zero Knowledge Proofs. **IEEE SP 2015** [Google Scholar](https://scholar.google.com/scholar?q=Secure+Sampling+of+Public+Parameters+for+Succinct+Zero+Knowledge+Proofs)
> 核心思路：提出基于多方计算（MPC）的CRS生成协议，只要至少一个参与者诚实，CRS便是安全的。
> 局限与区别：该方案计算开销极大，且信任模型为“至少一个相信”，而非“零信任”；本文的方案完全不需要信任任何CRS生成者，且在效率上远高于MPC方法。

[19] Fuchsbauer. Subversion-Zero-Knowledge SNARKs. **IACR eprint 2017/587** [Google Scholar](https://scholar.google.com/scholar?q=Subversion-Zero-Knowledge+SNARKs)
> 核心思路：独立地构造了抗颠覆的SNARK。
> 局限与区别：虽然目标相同，但技术路线不同；本文基于Groth [27]并专注于最小改动、公开验证和批处理优化的高效率实现。

### 核心技术与方案
本文方案基于Groth的QAP-based SNARK [27]，其整体框架是将零知识论证问题转化为检查多项式等式 $a(X)b(X) - c(X) \equiv h(X)\ell(X) \pmod{\ell(X)}$。方案的构造思路如下：

**1. CRS生成的分段化与公开验证性**。为了在CRS被颠覆时仍能提取出必要的陷阱门，本文将CRS生成算法分为三个子算法：`K_tc`（生成随机种子如 $\chi,\alpha,\beta,\gamma,\delta$）、`K_crs`（从种子确定性计算CRS）以及 `K_ts`（从种子生成模拟陷阱门）。在Groth原版CRS的基础上，方案增加了 $2n+3$ 个新的群元素（包括 $[ \gamma ]_1$、$[ \chi^i ]_1$、$[ \ell_i(\chi) ]_1$ 等），并设计了一个高效的CRS验证算法 `CV`。`CV` 通过一系列双线性配对等式检查（如 $[ iota ]_1 \bullet [1]_2 = [1]_1 \bullet [iota]_2$ 保证坐标一致性，利用拉格朗日基多项式验证 $\ell_i(\chi)$ 的正确性），确保任何被 `CV` 接受的CRS必然是从某个有效的种子通过 `K_crs` 诚实计算而来的。这一步是获得CRS陷阱门可提取性的基础。

**2. 完美子完备性**。定理2证明了该SNARK具有完美子完备性：一方面，`CV` 会以概率1接受诚实生成的CRS（这通过验证方程和 $\ell(X)=X^n-1$ 的性质直接验证）；另一方面，给定一个被 `CV` 接受的CRS，诚实证明者按照Groth的协议生成的论证 $\pi = (\mathfrak{a}, \mathfrak{b}, \mathfrak{c})$ 必然被验证者接受。论证的构造与Groth原版一致：$\mathfrak{a} = [\sum A_j u_j(\chi) + \alpha + r_a \delta]_1$，$\mathfrak{b} = [\sum A_j v_j(\chi) + \beta + r_b \delta]_2$，$\mathfrak{c}$ 通过精心组合 $r_b\mathfrak{a}$、$r_a(\mathfrak{b}-r_b\delta)$ 以及公开的CRS元素计算，使得最终验证等式 $\mathfrak{a} \bullet \mathfrak{b} = \mathfrak{c} \bullet [\delta]_2 + \text{public sum} + [\alpha\beta]_T$ 只当 $a(X)b(X)-c(X)=h(X)\ell(X)$ 时成立。

**3. 适应性知识可靠性**。定理3在Sub-GBGM中证明适应性知识可靠性。与Groth [27]在标准GBGM中的证明相比，证明的难点在于处理新增加的CRS元素（如 $[ \ell_i(\chi) ]_1$）和允许通用敌手创建的新的随机变量 $Y_i$（通过哈希到椭圆曲线生成）。证明的核心是：通过分析验证多项式 $V(X,Y) = A B - C X_\delta - \text{public part} - X_\alpha X_\beta$ 的系数，可以导出所有与 $Y_i$ 相关的系数 $A_{y_j}$、$B_{y_j}$、$C_{y_j}$ 必须为零（例如，从 $X_\alpha Y_j$ 项系数 $A_\alpha B_{y_j} + A_{y_j} B_\alpha = 0$ 且 $B_\alpha=0$（由 $A_\alpha B_\beta=1$ 和对称性可归一化为 $B_\alpha=0$）可得 $B_{y_j}=0$，进而推出 $A_{y_j}=C_{y_j}=0$）。消除这些新项后，证明约化为Groth原版的可靠性证明。最后，通过Schwartz-Zippel引理给出下界 $\Omega(\sqrt{p/n})$，其中 $p$ 是群阶，$n$ 是门数量。

**4. 完美可组合Sub-ZK**。定理5在BDH-KE假设下证明完美可组合Sub-ZK。首先，引理2证明 `CV` 接受的CRS必然在信息论意义下唯一确定了种子 $\text{tc} = (\chi,\alpha,\beta,\gamma,\delta)$，从而在BDH-KE假设下，存在一个高效的提取器 `X_Σ` 能从颠覆者输出的被 `CV` 接受的CRS中提取出该种子（定理4）。然后，模拟器 `S`（算法5）使用提取出的陷阱门 `ts = (\chi,\alpha,\beta,\delta)$` 并选取随机 $\sigma, \tau \in \mathbb{Z}_p$，计算模拟论证：$\mathfrak{a} = [\sigma]_1$，$\mathfrak{b} = [\tau]_2$，$\mathfrak{c} = [(\sigma\tau - \alpha\beta - \sum_{j=m_0+1}^m (u_j(\chi)\beta + v_j(\chi)\alpha + w_j(\chi)))/\delta]_1$。由于在真实证明中，$r_a$ 和 $r_b$ 使 $\mathfrak{a}$ 和 $\mathfrak{b}$ 均匀随机，并且 $\mathfrak{c}$ 由验证等式唯一确定（引理3），所以真实分布 $(\mathfrak{a}, \mathfrak{b}, \mathfrak{c})$ 与模拟分布完全相同，从而实现了完美零知识。借助定理1，可组合Sub-ZK自动蕴含无界Sub-ZK。

**5. 效率分析**。CRS总大小为 $4m + 3n + 13$ 个群元素。证明者的计算由 $\Theta(n \log n)$ 的域运算和 $\Theta(n)$ 的密码学运算（指数运算）主导。验证者的在线计算仅为3对配对。CRS验证 `CV` 通过批处理技术（使用随机系数 $t_i$ 将多个配对检查合并为单个配对方程）可显著加速：在安全级别 $2^{-80}$ 下，`CV` 的批处理版本比证明者算法更快。论证大小仅为2个 $\mathbb{G}_1$ 元素和1个 $\mathbb{G}_2$ 元素。

### 核心公式与流程

**[QAP多项式等式]**
$$
\left( \sum_{j=0}^{m} A_j u_j(X) \right) \left( \sum_{j=0}^{m} A_j v_j(X) \right) - \sum_{j=0}^{m} A_j w_j(X) = h(X) \ell(X)
$$
> 作用：定义了QAP关系；证明者需知道秘密的 $\mathbf{w}$ 和多项式 $h(X)$ 使得该等式成立；这是所有后续构造的基础。

**[CRS验证(`CV`)中的一个配对检查]**
$$
[ \ell_i(\chi) ]_1 \bullet ( [\chi]_2 - [\omega']_2 ) = [\zeta]_T \quad (\text{其中 } \omega' = \omega^{i-1}, \zeta = (\chi^n-1) \omega^{i-1} / n)
$$
> 作用：通过一个双线性配对验证拉格朗日基多项式在点 $\chi$ 上的值 $\ell_i(\chi)$ 是否正确计算，这是确保整个CRS中所有多项式值正确性的关键。

**[验证者验证等式]**
$$
\mathfrak{a} \bullet \mathfrak{b} = \mathfrak{c} \bullet [\delta]_2 + \left( \sum_{j=0}^{m_0} A_j \left[ \frac{u_j(\chi)\beta + v_j(\chi)\alpha + w_j(\chi)}{\gamma} \right]_1 \right) \bullet [\gamma]_2 + [\alpha\beta]_T
$$
> 作用：验证者检查这个配对等式是否成立；它是整个SNARK唯一的核心验证方程，其成立当且仅当证明者知道满足QAP关系的秘密。

**[模拟器计算]**
$$
\mathfrak{c} = [(\sigma\tau - \alpha\beta - \sum_{j=m_0+1}^{m} (u_j(\chi)\beta + v_j(\chi)\alpha + w_j(\chi)))/\delta]_1
$$
> 作用：模拟器使用提取的陷阱门和随机 $\sigma, \tau$ 计算论证的 $\mathfrak{c}$ 组件，使得其与真实证明的分布完全相同，从而实现完美零知识。

### 实验结果
实验使用libsnark [8]库实现，运行在标准桌面环境（具体硬件配置在全文版 [1] 中）。实验评估了CRS验证 `CV` 的批处理加速效果。结果显示，使用批处理技术后，`CV` 算法在信息理论安全等级 $2^{-40}$ 下的执行速度快于证明者算法；在 $2^{-80}$ 安全等级下，`CV` 仍比原始未经批处理的 `CV` 快约一个数量级。这表明抗颠覆性引入的额外计算开销（CRS验证）通过简单的批处理优化即可变得非常小，甚至不妨碍系统整体效率。此外，证明者和验证者的计算时间与Groth [27]的原始zksnark相近，因为核心协议未改变。

### 局限性与开放问题
本文的CRS长度仍然是 $\Omega(n)$（与门数量线性相关），并未实现完全简洁（fully succinct），即CRS本身不简洁。构造一个同时具有简洁CRS和简洁论证的、且高效实用的抗颠覆SNARK是重要的开放问题。此外，Sub-ZK的安全证明在不可验证的BDH-KE假设和Sub-GBGM下完成，寻找更强的标准假设下的安全性证明是未来的方向。

### 强关联论文

[2] Bellare等. NIZKs with an Untrusted CRS: Security in the Face of Parameter Subversion. **ASIACRYPT 2016**

[6] Ben-Sasson等. Secure Sampling of Public Parameters for Succinct Zero Knowledge Proofs. **IEEE SP 2015**

[8] Ben-Sasson等. Succinct Non-Interactive Zero Knowledge for a Von Neumann Architecture. **USENIX 2014**

[17] Danezis等. Square Span Programs with Applications to Succinct NIZK Arguments. **ASIACRYPT 2014**

[19] Fuchsbauer. Subversion-Zero-Knowledge SNARKs. **IACR eprint 2017/587**

[22] Gennaro等. Quadratic Span Programs and Succinct NIZKs without PCPs. **EUROCRYPT 2013**

[25] Groth. Simulation-Sound NIZK Proofs for a Practical Language and Constant Size Group Signatures. **ASIACRYPT 2006**

[27] Groth. On the Size of Pairing-Based Non-Interactive Arguments. **EUROCRYPT 2016**

[30] Lipmaa. Progression-Free Sets and Sublinear Pairing-Based Non-Interactive Zero-Knowledge Arguments. **TCC 2012**

[35] Parno等. Pinocchio: Nearly Practical Verifiable Computation. **IEEE SP 2013**


## 关键词

+ zk-SNARK
+ 破坏抵抗性
+ 零知识性
+ CRS验证
+ 公共参考串