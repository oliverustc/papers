---
title: "Non-interactive zero-knowledge and its applications"
doi: 10.1145/62212.62222
标题简称:
论文类型: conference
会议简称: STOC
发表年份: 1988
modified: 2025-04-08 18:40:24
---
## Non-interactive zero-knowledge and its applications

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/62212.62222)
+ [2019年重制版](https://dl.acm.org/doi/pdf/10.1145/3335741.3335757)

## 作者

+ Manuel Blum
+ Paul Feldman
+ [Silvio Micali](Silvio%20Micali.md)
## 笔记

### 背景与动机
零知识证明系统自 Goldwasser、Micali 和 Rackoff [GMR] 提出以来，被广泛应用于复杂性理论和密码学。已知的零知识证明系统普遍依赖三个核心要素：证明者与验证者之间的交互、验证者隐藏的随机性、以及底层计算问题的困难性。Ben-Or 等人的工作 [BGGHMR] 已证明所有 IP 中的语言都拥有零知识证明，Blum [B2] 也指出任何定理都存在除泄露自身长度外不泄露任何知识的证明。然而，这些系统都需要多轮交互，这在许多实际场景中造成了瓶颈，例如证明者可能处于无法接收消息的环境中。Blum、Feldman 和 Micali 的这篇开创性工作旨在回答一个根本性问题：交互和隐藏随机性在零知识证明中是否是本质必需的？他们证明了计算困难性本身可能是以使交互变得非必需，并且随机性的保密性也可以被消除。具体而言，他们提出了非交互式零知识证明模型，其中证明者和验证者共享一个公共随机串，证明者可以非交互地、以零知识方式向验证者证明任何 NP 断言的有效性。这项工作填补了零知识证明理论中的一个重要空白，并首次构建了可抵抗选择密文攻击的公钥加密方案，解决了自 1978 年以来困扰密码学界的一个基础性问题。

### 相关工作

[GMR] Goldwasser, Micali, Rackoff. The Knowledge Complexity of Interactive Proof-Systems. **SIAM J. on Computing** [Google Scholar](https://scholar.google.com/scholar?q=The+Knowledge+Complexity+of+Interactive+Proof-Systems)
> 核心思路：首次定义了交互式零知识证明系统，其中证明者和验证者通过多轮交互，证明者能在不泄露任何额外知识的情况下使验证者相信断言的正确性。
> 局限与区别：该系统本质上是交互式的，依赖于验证者的隐藏随机性。本文旨在证明交互和隐藏随机性不是零知识证明的必要条件，并提出了非交互式模型。

[GMW] Goldreich, Micali, Wigderson. Proofs that Yield Nothing but their Validity and a Methodology of Cryptographic Design. **FOCS 1986** [Google Scholar](https://scholar.google.com/scholar?q=Proofs+that+Yield+Nothing+but+their+Validity+and+a+Methodology+of+Cryptographic+Design)
> 核心思路：在安全加密方案存在的假设下，证明了任何 NP 语言都拥有交互式零知识证明系统。
> 局限与区别：该结果依然基于交互模型。本文进一步弱化了模型假设，证明只需一个公共随机串即可对 NP 断言进行零知识证明，无需交互。

[GM] Goldwasser, Micali. Probabilistic Encryption. **JCSS 1984** [Google Scholar](https://scholar.google.com/scholar?q=Probabilistic+Encryption)
> 核心思路：提出了概率加密的概念，并基于二次剩余假设（QRA）构建了语义安全的加密方案。
> 局限与区别：该工作奠定了密码学安全性的基础，但其安全性不抵抗自适应选择密文攻击。本文利用 NIZK 构造了可抵抗该攻击的加密方案。

[FFS] Feige, Fiat, Shamir. Zero-knowledge proofs of identity. **STOC 1987** [Google Scholar](https://scholar.google.com/scholar?q=Zero-knowledge+proofs+of+identity)
> 核心思路：受零知识证明启发，提出了高效的交互式身份识别方案。
> 局限与区别：该方案是交互式的。本文的非交互式模型为更广泛的应用场景（如邮件或不可达证明者）提供了可能。

[GMW2] Goldreich, Micali, Wigderson. How to Play Any Mental Game. **STOC 1987** [Google Scholar](https://scholar.google.com/scholar?q=How+to+Play+Any+Mental+Game)
> 核心思路：利用零知识证明，证明了在诚实多数协议下的完备性定理。
> 局限与区别：该结果依赖于交互式证明。本文的非交互式证明可视为构造其他密码学原语（如 CCA 安全加密）的核心模块。

[BBS] Blum, Blum, Shub. A simple and secure pseudo-random number generator. **SIAM J. on Computing 1986** [Google Scholar](https://scholar.google.com/scholar?q=A+simple+and+secure+pseudo-random+number+generator)
> 核心思路：基于二次剩余或分解假设，提出了一个密码学安全的伪随机数生成器。
> 局限与区别：本文在多定理 NIZK 中使用了密码学强伪随机生成器，以压缩公共随机串的消耗，其安全性可以基于与 QRA 相同的假设。

[RM] / [Y] Yao. Theory and Application of Trapdoor Functions. **FOCS 1982** [Google Scholar](https://scholar.google.com/scholar?q=Theory+and+Application+of+Trapdoor+Functions)
> 核心思路：提出了伪随机生成器的存在性等价于单向函数存在的思想。
> 局限与区别：本文在构造中使用了伪随机生成器，将其作为工具来扩展公共随机串的使用效率，而非探索其存在性基础。

### 核心技术与方案
本文的核心在于提出非交互式零知识证明模型并给出具体构造，最后将其应用于构造抗选择密文攻击的公钥加密方案。

**一、模型与假设**
该模型要求证明者 P 与验证者 V 共享一个由外部生成的公共随机串 σ。证明者根据定理和 σ 生成一个单向的证明消息 y 发送给验证者。验证者基于 x、y 和 σ 运行确定性算法来判定是否接受。该模型比交互模型更弱，因为共享随机串能力可以通过交互实现，反之则不成立。文中假设区分两个大素数乘积数与三个大素数乘积数的计算难题是困难的（2OR3A），该假设蕴含了二次剩余假设（QRA）。

**二、单定理非交互式零知识证明**
该方案专门用于证明图的三染色问题（3COL），这是 NP 完全的。
1.  **构造思路**：方案的直观思想是将三染色方案编码为关于二次剩余与二次非剩余的数学信息。
    *   **证明者**：随机选择三个 $k$ 比特的 Blum 整数 $n_1, n_2, n_3 \in Z_2(k)$（两个大素数乘积），以及相应的二次非剩余 $q_1, q_2, q_3$（满足 $(q_i | n_i) = 1$）。然后，将三种颜色分别编码为 $Z_{n_1}^{+1} \times Z_{n_2}^{+1} \times Z_{n_3}^{+1}$ 空间中的一个等价类。对于图中每个节点，根据其颜色选择空间中对应的一个元素作为标签。接着，对于每条边，公共随机串被划分成三元组。证明者需要为边的每个三元组计算“签名”，这些签名本质上是平方根。签名的类型（共 8 种）由三元组和相邻节点标签的二次特征决定。只有正确染色才能给出符合所有约束的签名集合。
    *   **验证者**：验证每个节点的标签都属于正确集合，并检查为公共随机串的每个三元组是否都提供了一个有效的签名。如果所有检查通过，则接受。
2.  **安全性直觉**：
    *   **完备性**：如果图是 3-可染色的，证明者可以根据其染色方案为每个边生成正确的签名，验证者会以压倒性概率接受。
    *   **可靠性**：如果图不是 3-可染色的，那么无论如何选择标签，总存在一条边，其两个端点属于同一个颜色等价类。对于随机选择的 σ 三元组，其所属的等价类是均匀随机的。由于可用的签名类型（抽屉）严格少于 8 个，证明者必定会失败（无法提供正确的签名），可靠性得以保证。
    *   **零知识**：存在一个模拟器 M，它不知道真实的 3-染色方案。M 选择 $n_i \in Z_2(k)$ 并知道其分解。它选择二次剩余的 $q_i$ 和所有节点的标签。它构建一个 σ，其中所有三元组都是二次剩余。由于 M 知道分解，它可以轻松地为每个三元组提供任意类型的签名。根据 QRA，模拟的 σ 与真实随机串无法区分，因此模拟的证明与真实证明在计算上不可区分。

**三、多定理非交互式零知识证明**
单定理方案限制了证明者只能用同一个 σ 证明一个定理。实际场景中，证明者需要证明多个定理。本文通过“一次初始化，多次证明”的框架解决了此问题。
1.  **构造思路**：首先，证明者利用 σ 的一部分非交互地证明一个随机定理（例如，随机选取的 $n \in Z_3(k)$ 的成员资格），将此作为“种子证明” $y_0$。随后，证明所有后续的重要定理 $T_i$ 时，证明 $y_i$ 的生成不仅依赖 σ，还依赖于之前的 $y_0$。重要定理的证明**彼此独立**。
2.  **方案细节**：证明者随机选取 $n \in Z_3(k)$（三个素数乘积）。证明 $n \in Z_3(k)$ 等价于证明一个辅助图是 3-可染色的，因此可复用单定理方案。之后，对于每个需要证明的 4-可染色图 G，证明者将 $Z_n^{+1}$ 的 4 个等价类对应 4 种颜色。它用每个等价类中的一个元素标记每个节点。对于每条边 (u, v)，它选择一个随机 $y_{uv}$ 使得 $e_u \cdot e_v \cdot y_{uv}$ 是二次剩余，并输出其平方根 $x_{uv}$。证明者还使用密码学强伪随机发生器计算一个长的伪随机序列，并对序列中的块进行处理，要求验证者检查足够多的块是否具有正确的二次特征。
3.  **安全性直觉**：
    *   **可靠性**：利用 $n \in Z_3(k)$ 的性质，$Z_n^{+1}$ 恰好有 4 个等价类。如果图不是 4-可染色的，那么必有一条边的两端标签属于同一类。验证者通过检查 $y_{uv}$ 的二次特征和伪随机序列块的统计特征，可以以高概率检测出不正确染色。
    *   **零知识**：模拟器 M 选择 $n \in Z_2(k)$（知道分解），并构造一个证明 $n \in Z_2(k)$ 是 $Z_3(k)$ 的假证明（这可以通过巧妙地选择 σ 实现）。然后 M 将图中所有节点标签设为二次剩余。对于每条边，它将 $y_{uv}$ 也设为二次剩余。利用 $n$ 的分解，M 可以对伪随机序列中的所有块提供所需的平方根。由于 QRA 和 2OR3A，该模拟分布与真实分布不可区分。

**四、复杂度分析**
*   **单定理方案**：通信复杂度为 $O(k^5)$ 比特量级，其中 $k$ 是安全参数。计算量：证明者需生成 $n_1, n_2, n_3$、计算平方根，总计算量为 $O(k^5)$ 次模运算；验证者为 $O(k^5)$ 次模运算。
*   **多定理方案**：初始随机串长度固定。证明每个定理的通信量和计算量均为输入图规模的拟多项式函数，主要代价来自生成和处理伪随机序列。

**五、应用：抗选择密文攻击的公钥加密**
本文将 NIZK 应用于公钥密码学，解决了长期以来关于抗选择密文（CCA）安全的加密方案的存在性问题。核心思想是：加密者不仅发送密文 $y$，还需要附加一个非交互式零知识证明 $\pi$，证明其“知道” $y$ 的明文 $m$（即拥有解密 $y$ 所需的随机性）。接收者在解密时，先验证 $\pi$ 的有效性，如果为真才输出解密结果，否则输出 $\bot$。这样做使得任何攻击者即使拥有对解密设备的访问权限（选择密文攻击），也无法获得有用信息，因为该设备只有在攻击者已经“知道”密文对应的明文时才会输出，从而防御了 CCA 攻击。

### 核心公式与流程
**[二次剩余预测定义]**
$$Q_x(y) = \begin{cases} 0, & \text{if } y \text{ is a quadratic residue modulo } x; \\ 1, & \text{otherwise} \end{cases}$$
> 作用：定义了模 $x$ 下的二次剩余预测，是协议中编码颜色和计算签名的核心数学工具。

**[2OR3A 假设]**
$$| P_{Z_2(k)} - P_{Z_3(k)} | < k^{-c}$$
其中 $P_{Z_s(k)} = Pr(x \leftarrow Z_s(k): C_k(x) = 1)$
> 作用：假设区分两个素数乘积（$Z_2(k)$）和三个素数乘积（$Z_3(k)$）是困难的。该假设是 NIZK 方案安全性证明的核心，并蕴含二次剩余假设（QRA）。

**[单定理协议中的签名类型]**
对于边 $(a, b)$ 的每个 8k 个三元组 $(z_1, z_2, z_3)$：计算以下之一：
$$
\begin{aligned}
&\text{type }0: (\sqrt{z_1}, \sqrt{z_2}, \sqrt{z_3}) \\
&\text{type }1: (\sqrt{q_1 z_1}, \sqrt{z_2}, \sqrt{z_3}) \\
&\text{type }2: (\sqrt{z_1}, \sqrt{q_2 z_2}, \sqrt{z_3}) \\
&\text{type }3: (\sqrt{z_1}, \sqrt{z_2}, \sqrt{q_3 z_3}) \\
&\text{type }4: (\sqrt{a_1 z_1}, \sqrt{a_2 z_2}, \sqrt{a_3 z_3}) \\
&\text{type }5: (\sqrt{b_1 z_1}, \sqrt{b_2 z_2}, \sqrt{b_3 z_3}) \\
&\text{type }6: (\sqrt{a_1 b_1 z_1}, \sqrt{a_2 b_2 z_2}, \sqrt{a_3 b_3 z_3}) \\
&\text{type }7: (\sqrt{q_1 z_1}, \sqrt{q_2 z_2}, \sqrt{q_3 z_3}) \\
\end{aligned}
$$
> 作用：这些签名将三元组映射到不同的“抽屉”，是证明染色方案正确的关键。只有染色正确时，这些签名才可能全部被正确计算。

**[多定理方案中的边证据生成]**
对于每条边 $(u, v)$：
随机选择 $y_{uv} \in Z_n^{+1}$ 使得 $e_u \cdot e_v \cdot y_{uv} \mod n$ 是一个二次剩余，然后计算其随机平方根 $x_{uv}$。同时，利用伪随机发生器 Gen 为每个 $y_{uv}$ 生成序列，并发送相关平方根。
> 作用：该步骤将边的合理性与颜色关系绑定。如果 $e_u$ 和 $e_v$ 属于不同颜色类，则 $y_{uv}$ 必须是二次非剩余，否则 $y_{uv}$ 会是二次剩余。验证者通过统计检查 $y_{uv}$ 的性质来确认染色正确性。

### 实验结果
本文为理论性论文，未包含传统意义上的实验评估，其“实验结果”体现在理论证明和应用构建上。论文的贡献在于：
1.  **理论模型确认**：严格定义了非交互式零知识证明，并证明了在标准密码学假设（2OR3A 和 QRA）下，对于任意 NP 语言，都存在单定理和多定理的非交互式零知识证明系统。
2.  **安全性证明**：通过构造性的证明，给出了完备性、可靠性和零知识性的形式化论证，是密码学理论论文的标准范式。
3.  **应用构建**：该理论成果最直接的应用是构建了首个可证明安全的、抵抗选择密文攻击的公钥加密方案。该方案解决了自 1978 年以来的一个开放问题，标志着密码学的一个里程碑。
4.  **参数与规模**：方案中，证明者需要处理 $O(k^5)$ 量级的随机串和计算（$k$ 为安全参数）。实际运行此系统需要较大的计算和通信开销，但这是为达到 CCA 安全所付出的理论证明上的代价。
5.  **无实验数据**：作为 1988 年的 STOC 论文，当时并没有进行实际系统实现或性能基准测试。其“性能”体现在渐进复杂度和理论可证安全性上，而非实际吞吐量或延迟。

### 局限性与开放问题
本文的局限性在于其构造依赖于特定的数论假设（区分 2 素数与 3 素数的困难性），并且构造相对复杂，尤其是多定理方案，其运行时间和通信量都很大。开放问题是能否将非交互式零知识证明建立在更弱的、更通用的假设上，例如仅仅依赖于单向函数的存在。此外，本文提出的 CCA 安全加密方案是存在性证明，其效率极低，远非实用，因此寻找实用的 CCA 安全方案也是一个重要的开放问题（正是后续 Cramer-Shoup 等方案追求的目标）。

### 强关联论文
[GMR] Goldwasser, Micali, Rackoff. The Knowledge Complexity of Interactive Proof-Systems. **SIAM J. on Computing** [Google Scholar](https://scholar.google.com/scholar?q=The+Knowledge+Complexity+of+Interactive+Proof-Systems)

[GMW] Goldreich, Micali, Wigderson. Proofs that Yield Nothing but their Validity and a Methodology of Cryptographic Design. **FOCS 1986** [Google Scholar](https://scholar.google.com/scholar?q=Proofs+that+Yield+Nothing+but+their+Validity+and+a+Methodology+of+Cryptographic+Design)

[GM] Goldwasser, Micali. Probabilistic Encryption. **JCSS 1984** [Google Scholar](https://scholar.google.com/scholar?q=Probabilistic+Encryption)

[BBS] Blum, Blum, Shub. A simple and secure pseudo-random number generator. **SIAM J. on Computing 1986** [Google Scholar](https://scholar.google.com/scholar?q=A+simple+and+secure+pseudo-random+number+generator)

[FFS] Feige, Fiat, Shamir. Zero-knowledge proofs of identity. **STOC 1987** [Google Scholar](https://scholar.google.com/scholar?q=Zero-knowledge+proofs+of+identity)

[GMW2] Goldreich, Micali, Wigderson. How to Play Any Mental Game. **STOC 1987** [Google Scholar](https://scholar.google.com/scholar?q=How+to+Play+Any+Mental+Game)

[BM] Blum, Micali. How To Generate Sequences Of Cryptographically Strong Pseudo-Random Bits. **SIAM J. on Computing 1984** [Google Scholar](https://scholar.google.com/scholar?q=How+To+Generate+Sequences+Of+Cryptographically+Strong+Pseudo-Random+Bits)


## 关键词

+ 非交互式零知识证明NIZK
+ 公共参考串模型CRS
+ 选择密文安全公钥加密
+ 零知识去交互化
+ 随机字符串替代交互
+ 密码学基础原语