---
title: "How to Share an NP Statement or Combiners for Zero-Knowledge Proofs"
标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 2025
created: 2025-06-09 10:37:25
modified: 2025-06-09 10:41:21
---

## How to Share an NP Statement or Combiners for Zero-Knowledge Proofs

## 发表信息

+ [原文链接](https://eprint.iacr.org/2025/334)

## 作者

+ Benny Applebaum
+ Eliran Kachlon

## 笔记

### 背景与动机
秘密共享允许将一份秘密拆分成 $n$ 份，只有当至少 $t$ 份合在一起时才能重构秘密，而少于 $t$ 份则无法获取任何信息。Goyal, Jain 和 Sahai 于 Crypto 2019 将这一经典概念拓展至 NP 语句，提出了 NP 语句的秘密共享（NPSS）[37]，它将一个实例-证据对映射到 $n$ 个实例-证据对，使得任意 $t-1$ 份不泄露原始证据信息，而任意 $t$ 份可完整恢复原始证据。然而，NPSS 的现有构造仅适用于 $t=n$ 的情形，并且仅提供了计算安全性。对于更一般的门限 $t \le n$，特别是信息论安全的 NPSS 是否存在，此前完全未知。本文旨在填补这一空白，建立信息论安全 NPSS 的精确定义，并给出任意门限下的高效构造。该构造不仅本身具有理论价值，还能作为强大的组合工具，非交互地将多个零知识证明实例的安全性组合起来，从而简洁地解决多字符串模型 NIZK、两轮分布式零知识证明以及三轮安全多方计算等文献中遗留的公开问题，且这些应用仅基于最弱假设——单向函数的存在性。

### 相关工作

[37] Goyal 等. Simultaneous Amplification: The Case of Non-Interactive Zero-Knowledge. **Crypto 2019** [Google Scholar](https://scholar.google.com/scholar?q=Simultaneous%20Amplification%3A%20The%20Case%20of%20Non-Interactive%20Zero-Knowledge)
> 核心思路：首次提出 NPSS 概念，并基于非交互承诺构造了 $(n,n)$-NPSS 和一个隐私阈值 $t_p < n/3$、恢复阈值 $t_c > 2n/3$ 的“间隙构造”。
> 局限与区别：仅实现计算安全性，无法支持任意门限 $t$。本文首次实现信息论安全的任意门限 NPSS。

[38] Groth 和 Ostrovsky. Cryptography in the Multi-String Model. **J. Cryptology 2014** [Google Scholar](https://scholar.google.com/scholar?q=Cryptography%20in%20the%20Multi-String%20Model)
> 核心思路：提出多字符串模型，允许多个 CRS 共同存在，只要多数 CRS 诚实生成便保证安全。
> 局限与区别：其构造依赖双线性群或公共随机串模型，无法从结构化 CRS 的 NIZK 直接转化。本文通过 NPSS 实现了从任意 NIZK 到多字符串 NIZK 的通用转化。

[16] Blum 等. Non-Interactive Zero-Knowledge and Its Applications. **STOC 1988** [Google Scholar](https://scholar.google.com/scholar?q=Non-Interactive%20Zero-Knowledge%20and%20Its%20Applications)
> 核心思路：引入非交互零知识证明概念及其在密码学中的应用。
> 局限与区别：依赖于公共参考串模型，而本文的目标是增强其对 CRS 生成过程的容错性。

[44] Ishai 等. Zero-Knowledge Proofs from Secure Multiparty Computation. **SIAM J. Comput. 2009** [Google Scholar](https://scholar.google.com/scholar?q=Zero-Knowledge%20Proofs%20from%20Secure%20Multiparty%20Computation)
> 核心思路：提出 MPC-in-the-head 范式，利用安全多方计算构造零知识证明。
> 局限与区别：本文将其作为构造 AND-NPSS 的核心技术，但通过引入部分赋值和 OT 消息的特殊处理，实现了信息论安全的NPSS。

[33] Goldreich 等. How to Play Any Mental Game or A Completeness Theorem for Protocols with Honest Majority. **STOC 1987** [Google Scholar](https://scholar.google.com/scholar?q=How%20to%20Play%20Any%20Mental%20Game%20or%20A%20Completeness%20Theorem%20for%20Protocols%20with%20Honest%20Majority)
> 核心思路：提出 GMW 协议，可在混淆传输（OT）混合模型中安全计算任意函数。
> 局限与区别：本文利用其 1-隐私性和完美正确性来构建 AND-NPSS，但通过部分赋值机制处理了 OT 消息泄露导致的隐私问题。

[6] Applebaum 等. Verifiable Relation Sharing and Multi-Verifier Zero-Knowledge in Two Rounds: Trading NIZKs with Honest Majority. **Crypto 2020** [Google Scholar](https://scholar.google.com/scholar?q=Verifiable%20Relation%20Sharing%20and%20Multi-Verifier%20Zero-Knowledge%20in%20Two%20Rounds%3A%20Trading%20NIZKs%20with%20Honest%20Majority)
> 核心思路：构造了两轮诚实多数多验证者零知识协议，但需要亚指数安全的单射单向函数，且复杂度随参与者指数增长。
> 局限与区别：本文通过 NPSS 将两轮多验证者零知识证明简化为基于单向函数的多字符串 dp-NIZK，完全消除了上述两个限制。

[50] Naor. Bit Commitment Using Pseudo-Randomness. **Crypto 1989** [Google Scholar](https://scholar.google.com/scholar?q=Bit%20Commitment%20Using%20Pseudo-Randomness)
> 核心思路：利用伪随机生成器构造统计绑定的比特承诺方案。
> 局限与区别：本文在多字符串模型下采用 Naor 承诺来实现从 NIZK 到多字符串 NIZK 的转换，使转换可基于单向函数。

[24] Cohen 等. Efficient Multiparty Protocols via Log-Depth Threshold Formulae. **Crypto 2013** [Google Scholar](https://scholar.google.com/scholar?q=Efficient%20Multiparty%20Protocols%20via%20Log-Depth%20Threshold%20Formulae)
> 核心思路：提出了基于对数深度阈值公式构造高效 MPC 协议的通用框架。
> 局限与区别：本文采用了类似的递归框架，但定义了一种适用于 NPSS 的“$\chi$-双重安全”MPC 新概念，并通过服务器替换生成器（$G_\vee$ 和 $G_\wedge$）来实现。

### 核心技术与方案

**整体框架**：本文的核心贡献包含两个层次。首先，定义并构造了一种信息论安全的 NP 语句秘密共享方案（NPSS）。其次，利用该 NPSS 作为构建模块，设计了一系列密码协议的应用，包括多字符串模型 NIZK、NIZK 组合器、两轮多验证者零知识证明和三轮安全多方计算。

**NPSS 的构造**：这项工作的核心技术是将 NPSS 的构造转化为一个特定的安全多方计算（MPC）协议的构造问题。具体而言，构造分为两步：
1. **从 MPC 到 NPSS**：对于一个目标访问结构 $\chi$（如 $t$-out-of-$n$），首先构造一个满足“$\chi$-双重安全”的 MPC 协议 $\pi'$，用于计算一个与原始电路-SAT 实例 $f$ 相关的特殊函数 $\mathcal{F}_f$。该函数将 $n$ 个客户端输入异或后得到 $x$，并输出 $f(x)$。然后，将 $\pi'$ 中每个客户端 $c_i$ 的“扩展视图”（包括其自己的变量、收到的消息和 OT 的选择输出）作为第 $i$ 份 NPSS 的部分赋值 $y_i$，并将其验证逻辑编码成一个新的电路-SAT 实例 $f_i$。整体变量空间 $y$ 是 $\pi'$ 中所有变量的取值。恢复时，授权集合 $S$ 的部分赋值通过提取器 $\text{Ext}'$ 恢复出所有客户端的输入 $x_1, \ldots, x_n$，进而得到原始证据 $x = x_1 \oplus \cdots \oplus x_n$。隐私性由 $\pi'$ 的 $\chi$-被动安全性保证。
2. **从布尔公式到 MPC**：为了构造满足 $\chi$-双重安全的 MPC 协议，本文引入了“服务器替换生成器”的概念，包括 AND 生成器 $G_\wedge$ 和 OR 生成器 $G_\vee$。给定一个安全协议和一个要被替换的服务器 $\tau$：
   * $G_\vee$ (OR 生成器)：将 $\tau$ 替换为两个新服务器 $A$ 和 $B$，两者都持有 $\tau$ 的完整视图副本。只要 $A$ 或 $B$ 中有一个是诚实的，就能保证正确性，而隐私性要求 $A$ 和 $B$ 都未被泄露（即它们构成一个“强”的系统，类似于 OR 门）。
   * $G_\wedge$ (AND 生成器)：将 $\tau$ 替换为两个新服务器 $A$ 和 $B$，两者的视图通过 2-out-of-2 秘密共享方式拆分。只要 $A$ 和 $B$ 都诚实，就能保证正确性，而隐私性要求至少有一个未被泄露（即它们构成一个“弱”的系统，类似于 AND 门）。
   通过结合 GMW 协议（作为 AND 基本块）和“复制协议”（作为 OR 基本块），按照 $\chi$ 对应的对数深度单调公式进行递归构造，最终得到一个仅由客户端组成、满足 $\chi$-双重安全的 MPC 协议。利用对数深度的排序网络，该方案可实现任意 $t$-out-of-$n$ 门限。

**关键点——部分赋值**：在 AND-NPSS 的构造中，对于 OT 接收方 $P_2$，其视图中的 $z_{1-s}$ 项被保留为未赋值（$*$）。电路 $f_2$ 利用扩展逻辑（例如 $(s \land z_1) \lor (\neg s \land z_0)$）在 $z_{1-s}=*$ 时正确计算出 $z_s$ 的值，从而既保证了正确性，又通过不包含 $z_{1-s}$ 的赋值维护了隐私性。这是实现信息论安全的关键技术细节。

**应用**：
* **MS-NIZK**：给定多字符串 CRS $(crs_1, \ldots, crs_n)$ 和实例 $f$，证明者使用 $t=\lceil (n+1)/2\rceil$-out-of-$n$ NPSS 生成 $f_i$ 和 $y_i$，将 $y_i$ 的全局赋值 $y$ 用统计绑定承诺承诺，并为每个 $(f_i, Y)$ 生成一个 NIZK 证明 $\pi_i$。安全性依赖于多数 CRS 的诚实性和承诺的绑定/隐藏性质。
* **NIZK 组合器**：将每个 $n$ 个 NIZK 方案的 CRS 集合视为多字符串，应用 MS-NIZK 构造。安全性要求大多数候选方案同时满足可靠性和零知识。
* **两轮多验证者零知识证明**：首先基于单向函数构造一个单定理的指定证明者 NIZK（dp-NIZK），然后使用 NPSS 将其提升到多字符串模型，其中每个 CRS 由一个验证者生成并附带私钥。这实现了简单通信模式：第一轮每个验证者广播 CRS 并向证明者发送私钥，第二轮证明者发布证明。
* **三轮安全多方计算**：利用上述两轮多验证者零知识证明协议和文献中的技术，构造一个全安全的 3 轮 MPC 协议，实现了在有主动腐败少数参与者情况下的保证输出递送。

**复杂度分析**：NPSS 构造生成的每个电路 $f_i$ 的大小为 $|f| \cdot \text{poly}(2^d \cdot n)$，其中 $d$ 是访问结构 $\chi$ 的单调公式深度。对于 $t$-out-of-$n$ 门限，深度为 $O(\log n)$，因此复杂度为 $|f| \cdot \text{poly}(n)$。NPSS 算法（R, W, Sim, Dec）的运行时间均为 $\text{poly}(|f| \cdot 2^d \cdot n) = \text{poly}(n \cdot |f|)$。对于应用，MS-NIZK 的证明规模是原 NIZK 证明规模的 $n$ 倍再乘以 $\text{poly}(n, \kappa)$ 因子，其中 $\kappa$ 是安全参数。3 轮 MPC 的通信复杂度为 $\text{poly}(\kappa, |\text{电路}|, n)$，其中 $n$ 是参与方数量。

### 核心公式与流程

**[NPSS 的定义]**

**完整性**：对任意满足 $f$ 的 $x$，$W(f,x)$ 输出 $(y, y_1, \ldots, y_n)$，使得每个 $y_i$ 在布尔值上与 $y$ 一致，且 $f_i(y_i) = 1$。

**隐私性**：对任意未经授权的集合 $Z \notin \mathcal{A}$ 和满足 $f$ 的 $x$，分布 $\{W(f,x)\}_Z$ 与 $\text{Sim}(f, Z)$ 相同。

**恢复性**：对任意经授权的集合 $S \in \mathcal{A}$ 和两两布尔值一致的 $(y_i)_{i \in S}$，若每个 $y_i$ 满足 $f_i$，则 $\text{Dec}(f, S, (y_i)_{i \in S})$ 输出一个满足 $f$ 的 $x$。

**[AND/OR 生成器的安全条件]**

设 $\pi$ 在 $\mathcal{P}$ 上计算 $\mathcal{F}$ 且满足 $\chi$-双重安全，$\tau \in \mathcal{S}$ 是服务器。

**$G_\vee$ (OR 生成器)**：新协议 $\pi'$ 满足 $\chi_\vee$-双重安全，其中：
$$
\chi_\vee(S) = \begin{cases} \chi(S), & \text{if } A,B \notin S \\ \chi((S \setminus \{A,B\}) \cup \{\tau\}), & \text{otherwise} \end{cases}
$$

**$G_\wedge$ (AND 生成器)**：新协议 $\pi'$ 满足 $\chi_\wedge$-双重安全，其中：
$$
\chi_\wedge(S) = \begin{cases} \chi((S \setminus \{A,B\}) \cup \{\tau\}), & \text{if } A,B \in S \\ \chi(S \setminus \{A,B\}), & \text{otherwise} \end{cases}
$$

**[从 MPC 到 NPSS 的构造]**

**实例映射器 $R$**: $R(f)$ 输出 $(f_1, \ldots, f_n)$，其中 $f_i$ 验证 $\pi'$ 中客户端 $c_i$ 的扩展视图。

**赋值映射器 $W$**: $W(f, x)$ 随机生成 $x_1, \ldots, x_n$ 满足 $x = x_1 \oplus \cdots \oplus x_n$，并诚实执行 $\pi'$ 得到全局赋值 $y$ 和部分赋值 $y_i$（仅对 $c_i$ 的扩展视图赋值）。

**模拟器 $\text{Sim}$**: 对未经授权的 $Z$，利用 $\pi'$ 的模拟器 $\text{Sim}'$ 生成 $Z$ 中客户端的视图，再扩展为 $y_i$。

**解码器 $\text{Dec}$**: 对经授权的 $S$，利用 $\pi'$ 的提取器 $\text{Ext}'$ 从视图恢复所有输入 $(x_1, \ldots, x_n)$，并输出 $x = x_1 \oplus \cdots \oplus x_n$。

**[GMW 协议中的 OLE 乘法]**

MPC 协议中的 AND 乘法运算通过 OT 实现。设 $v_1^A$ 和 $v_2^B$ 分别是 $A$ 和 $B$ 持有的秘密共享份额，要计算共享 $v_1 \cdot v_2$。具体步骤为（以 $G_\wedge$ 中的乘法为例）:
1. $A$ 采样随机 $v_3^A, r \gets \{0,1\}$。
2. 第一次 OLE: $A$ 输入 $(v_1^A, v_1^A \cdot v_2^A \oplus v_3^A \oplus r)$，$B$ 输入 $v_2^B$，$B$ 输出 $y_1$。
3. 第二次 OLE: $A$ 输入 $(v_2^A, r)$，$B$ 输入 $v_1^B$，$B$ 输出 $y_2$。
4. $B$ 计算 $x_3^B = y_1 \oplus y_2 \oplus v_1^B \cdot v_2^B$，$A$ 设 $x_3^A = v_3^A$。

### 实验结果

该论文是理论性的，未报告实验结果。

### 局限性与开放问题
本文的 NPSS 构造依赖于 MPC 协议和对数深度公式，对于实际应用来说，其产生的电路实例 $f_i$ 的规模仍然有 $\text{poly}(n)$ 的因子增长，当 $n$ 很大时可能不高效。将 NPSS 应用于构造三轮 MPC 时，虽然轮数最优，但其总通信复杂度的具体多项式系数尚不明确，需要进一步优化以提升实用性。此外，本文提出的信息论安全 NPSS 是否可接入标准 NP 归约（如 Karp 归约）从而无需修改底层电路结构，仍是一个开放问题。

### 强关联论文

[37] Goyal, V., Jain, A., Sahai, A. Simultaneous Amplification: The Case of Non-Interactive Zero-Knowledge. **Crypto 2019** [Google Scholar](https://scholar.google.com/scholar?q=Simultaneous%20Amplification%3A%20The%20Case%20of%20Non-Interactive%20Zero-Knowledge)

[38] Groth, J., Ostrovsky, R. Cryptography in the Multi-String Model. **J. Cryptology 2014** [Google Scholar](https://scholar.google.com/scholar?q=Cryptography%20in%20the%20Multi-String%20Model)

[16] Blum, M., Feldman, P., Micali, S. Non-Interactive Zero-Knowledge and Its Applications. **STOC 1988** [Google Scholar](https://scholar.google.com/scholar?q=Non-Interactive%20Zero-Knowledge%20and%20Its%20Applications)

[44] Ishai, Y., Kushilevitz, E., Ostrovsky, R., Sahai, A. Zero-Knowledge Proofs from Secure Multiparty Computation. **SIAM J. Comput. 2009** [Google Scholar](https://scholar.google.com/scholar?q=Zero-Knowledge%20Proofs%20from%20Secure%20Multiparty%20Computation)

[33] Goldreich, O., Micali, S., Wigderson, A. How to Play Any Mental Game or A Completeness Theorem for Protocols with Honest Majority. **STOC 1987** [Google Scholar](https://scholar.google.com/scholar?q=How%20to%20Play%20Any%20Mental%20Game%20or%20A%20Completeness%20Theorem%20for%20Protocols%20with%20Honest%20Majority)

[6] Applebaum, B., Kachlon, E., Patra, A. Verifiable Relation Sharing and Multi-Verifier Zero-Knowledge in Two Rounds: Trading NIZKs with Honest Majority. **Crypto 2020** [Google Scholar](https://scholar.google.com/scholar?q=Verifiable%20Relation%20Sharing%20and%20Multi-Verifier%20Zero-Knowledge%20in%20Two%20Rounds%3A%20Trading%20NIZKs%20with%20Honest%20Majority)

[50] Naor, M. Bit Commitment Using Pseudo-Randomness. **Crypto 1989** [Google Scholar](https://scholar.google.com/scholar?q=Bit%20Commitment%20Using%20Pseudo-Randomness)

[24] Cohen, G., et al. Efficient Multiparty Protocols via Log-Depth Threshold Formulae. **Crypto 2013** [Google Scholar](https://scholar.google.com/scholar?q=Efficient%20Multiparty%20Protocols%20via%20Log-Depth%20Threshold%20Formulae)

[5] Applebaum, B., Kachlon, E., Patra, A. Round-Optimal Honest-Majority MPC in Minicrypt and with Everlasting Security. **TCC 2022** [Google Scholar](https://scholar.google.com/scholar?q=Round-Optimal%20Honest-Majority%20MPC%20in%20Minicrypt%20and%20with%20Everlasting%20Security)

[1] Ajtai, M., Komlós, J., Szemerédi, E. An $O(n \log n)$ Sorting Network. **STOC 1983** [Google Scholar](https://scholar.google.com/scholar?q=An%20O(n%20log%20n)%20Sorting%20Network)


## 关键词

+ NP语句的秘密共享
+ 信息论安全
+ 零知识证明非交互式组合
+ 多字符串模型
+ 安全多方计算