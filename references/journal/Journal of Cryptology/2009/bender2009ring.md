---
title: "Ring signatures: Stronger definitions, and constructions without random oracles"
doi: 10.1007/s00145-007-9011-9
标题简称:
论文类型: journal
期刊简称: Journal of Cryptology
发表年份: 2009
created: 2025-05-28 01:48:17
modified: 2025-05-28 01:48:23
---
## Ring signatures: Stronger definitions, and constructions without random oracles

## 发表信息

+ [原文链接](https://link.springer.com/article/10.1007/s00145-007-9011-9)

## 作者

+ Adam Bender
+ [Jonathan Katz](Jonathan%20Katz.md)
+ Ruggero Morselli

## 笔记

### 背景与动机
环签名允许一个用户代表一个可能的签名者集合（环）对消息进行签名，而不泄露究竟是环中的哪一位成员生成了该签名。该概念由 Rivest, Shamir 和 Tauman 首次形式化提出 [20]，其灵活性优于群签名：它无需中央权威或用户间的协调，环可以临时按需组建，用户能精确控制签名关联的匿名级别。这一特性使其天然适用于匿名泄露秘密、资源访问控制以及指定验证者签名等场景。然而，现有工作所提供的安全定义要么相当非形式化，要么在处理现实攻击时显得异常薄弱。具体而言，这些定义通常假设诚实用户总是针对一个由完全诚实生成的公钥构成的环来签名，而未考虑环中包含对手恶意生成的公钥的情况。显然，无法抵御此类攻击的方案实用性受限，因为环签名的“ad-hoc”性质使得公钥难以被中心化机构验证。本文旨在填补这一空白，通过提出更强的安全定义来刻画这些现实的攻击，并构建首批在标准模型下（不依赖随机预言机或理想密码模型）安全的环签名方案。

### 相关工作

[20] Rivest et al. How to leak a secret. **Asiacrypt 2001** [Google Scholar](https://scholar.google.com/scholar?q=How+to+leak+a+secret)
> 核心思路：首次形式化了环签名概念，并基于陷门排列和对称加密给出了一个构造。
> 局限与区别：其安全性分析在随机预言机模型中进行，且匿名性和不可伪造性定义未考虑环中包含恶意密钥的情况。

[1] Abe et al. 1-out-of-n signatures from a variety of keys. **Asiacrypt 2002** [Google Scholar](https://scholar.google.com/scholar?q=1-out-of-n+signatures+from+a+variety+of+keys)
> 核心思路：提出了允许环内公钥来自不同类型系统的签名方案，并给出了更强的“选择子环攻击下的不可伪造性”定义。
> 局限与区别：该定义仍未涵盖敌手生成部分公钥的攻击（即不保护 w.r.t. 内部腐败）。

[3] Bellare et al. Foundations of group signatures. **Eurocrypt 2003** [Google Scholar](https://scholar.google.com/scholar?q=Foundations+of+group+signatures)
> 核心思路：为群签名提供了形式化基础，并给出了一个基于通用假设的构造。
> 局限与区别：群签名有中心群管理员，与环签名的去中心化本质不同；该构造不直接适用于环签名场景，且未处理敌手控制的公钥。

[12] Dwork and Naor. Zaps and their applications. **FOCS 2000** [Google Scholar](https://scholar.google.com/scholar?q=Zaps+and+their+applications)
> 核心思路：引入了ZAP——一种两轮、公共硬币、可抵抗适应性攻击的见证不可区分证明系统。
> 局限与区别：本文利用ZAP的见证不可区分性来证明环签名中签名者的匿名性，这是构造中实现强匿名的关键工具。

[21] Waters. Efficient identity-based encryption without random oracles. **Eurocrypt 2005** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+identity-based+encryption+without+random+oracles)
> 核心思路：提出了一种在标准模型下可证安全的基于身份加密方案，并附带了一个签名方案。
> 局限与区别：本文直接基于该签名方案构造了一个高效的2用户环签名方案，通过巧妙的代数变换实现双线性群上的匿名性。

[10] Damgård and Nielsen. Improved non-committing encryption schemes. **Crypto 2000** [Google Scholar](https://scholar.google.com/scholar?q=Improved+non-committing+encryption+schemes+based+on+a+general+complexity+assumption)
> 核心思路：引入了“不经意密钥生成器”的概念，允许在不持有密钥的情况下生成公钥。
> 局限与区别：本文利用该技术增强通用构造的匿名性，使其能够抵御“完全密钥泄露”攻击，即即使生成密钥的随机数全部公开，匿名性依然成立。

### 核心技术与方案

本文的核心贡献分为两部分：重新定义安全性和构造方案。

**1. 更强的安全定义**
本文指出，先前工作（如 [20, 1]）的匿名性和不可伪造性定义存在严重缺陷。例如，它们假设签名时使用的环全部由诚实生成的密钥组成。这无法防御敌手生成恶意公钥并诱骗用户将其加入环中的现实攻击。为此，本文提出了一系列更强的定义，并证明了它们之间的层次关系。
- **匿名性**：从“基本匿名性”出发，逐步加强为“针对恶意选择的密钥的匿名性”、“抵抗归因攻击的匿名性”，最终到“抗完全密钥泄露的匿名性”（Definition 4）。后者允许敌手获取除挑战签名者外所有诚实用户的全部随机数，但仍无法区分签名者。
- **不可伪造性**：从“固定环攻击下的不可伪造性”（Definition 5）加强到“选择子环攻击下的不可伪造性”（Definition 6），最终到“针对内部腐败的不可伪造性”（Definition 7）。后者允许敌手通过腐败预言机获取任何用户的私钥，且允许环中包含任意数量的敌手生成公钥，只要最终伪造的签名相对于一个完全由未腐败诚实用户组成的环有效。

**2. 基于通用假设的构造（Section 5）**
该方案满足最强安全性（匿名性抗归因攻击，不可伪造性抗内部腐败），是标准模型下的首个通用构造。其核心思想是“加密一个标准签名，并用一个ZAP证明该加密正确”。
- **构造思路**：每个用户拥有两对密钥：一对标准签名密钥 (sk_S, pk_S) 和一对加密密钥 (sk_E, pk_E)（sk_E 被丢弃）。一个关键的随机字符串 r 也作为公钥的一部分。签名时，签名者 i* 首先用自己的签名密钥对消息和整个环的哈希（即 M* = M || PK1 || ... || PKn）生成标准签名 σ'。然后，它使用一种特殊的概率加密算法 Enc*，该算法将输入的消息（这里是 σ'）秘密分割并分别用环中所有用户的加密公钥加密，这样只有掌握至少一个解密密钥才能恢复。具体来说，对于环中的 n 个用户，它随机选择 s_1,...,s_{n-1}，并输出一个向量，其中第 i 个分量是：
$$
C_i^* = 
\begin{cases} 
\mathsf{Enc}_{pk_{E,i}}(s_i), & \text{for } i \neq i^* \\
\mathsf{Enc}_{pk_{E,i^*}}(\sigma' \oplus (\bigoplus_{j=1}^{n-1} s_j)), & \text{for } i = i^*
\end{cases}
$$
但实际算法中，非签名者位置的加密内容是 0 的字符串，而签名者位置是真实签名 σ'。最后，它生成一个ZAP证明，证明这 n 个密文 {C_i*} 中至少有一个是对应公钥 pk_{S,i} 的一个有效签名的加密。
- **安全性直觉**：
    - **匿名性**：由于ZAP的见证不可区分性和加密的语义安全性，敌手无法区分签名者使用的是谁的签名密钥生成的σ'。即使敌手控制了某些公钥，也因无法解密而无法区分。
    - **不可伪造性**：要伪造一个环签名，敌手必须能产生一个有效的ZAP证明。由于ZAP的可靠性，这几乎必然意味着敌手伪造了一个对某个诚实用户公钥有效的标准签名，从而攻破了标准签名方案的安全性。

**3. 高效的2用户环签名方案（Section 6）**
该方案基于Waters签名方案 [21] 在双线性群上构造，仅支持两个用户，但效率远超通用构造，并满足强匿名性（抗完全密钥泄露）和选择子环攻击下的不可伪造性。
- **构造思路**：核心洞察是 Waters 签名中的元素 h 可以来自另一个用户的公钥。用户 A 的公钥为 $(g_1 = g^\alpha, u', u_1, ..., u_n)$，私钥为 α。用户 B 的公钥为 $(\bar{g}_1, \bar{u}', \bar{u}_1, ..., \bar{u}_n)$。A 代表环 {A, B} 签名的关键计算是 $\bar{g}_1^\alpha$。因为 B 也能用自己的私钥 $\bar{\alpha}$ 计算 $g_1^{\bar{\alpha}} = \bar{g}_1^{\alpha} = g^{\alpha \bar{\alpha}}$，这个值是对称的，因此无法区分签名者。
- **关键步骤**：
    - **签名** (Sign): 对消息 M，签名者（假设为 A）计算 $s = \bar{g}_1^\alpha$，$w = u'\prod_{i:M_i=1}u_i$，$\bar{w} = \bar{u}'\prod_{i:M_i=1}\bar{u}_i$，选择随机数 r，输出签名 $\sigma = (A, B) = (s \cdot (w \cdot \bar{w})^r, g^r)$。
    - **验证** (Vrfy): 验证者检查双线性配对等式：$\hat{e}(g_1, \bar{g}_1) \cdot \hat{e}(B, w \cdot \bar{w}) \stackrel{?}{=} \hat{e}(A, g)$。该等式成立是因为 $\hat{e}(s \cdot (w\bar{w})^r, g) = \hat{e}(g^{\alpha\bar{\alpha}}, g) \cdot \hat{e}((w\bar{w})^r, g) = \hat{e}(g_1, \bar{g}_1) \cdot \hat{e}(g^r, w\bar{w})$。
- **安全性直觉**：
    - **匿名性**：由于 $s = g^{\alpha \bar{\alpha}}$ 对两个用户对称，在信息论意义上签名是完全匿名的。
    - **不可伪造性**：通过高效的归约证明，任何能够伪造该环签名的敌手都可以被转化为一个能够伪造Waters标准签名的敌手。归约的关键在于，模拟器可以将Waters挑战公钥巧妙地拆分给环中的两个用户，从而在模拟签名时可以利用挑战签名预言机的响应。

### 核心公式与流程

**[通用构造的环签名算法 (Sign)]**
$$
\begin{aligned}
&\text{输入: } SK_{i^*}, M, R = (PK_1, ..., PK_n) \\
&\text{1. 解析 } PK_i = (pk_{S,i}, pk_{E,i}, r_i), \ SK_{i^*} = sk_{S,i^*} \\
&\text{2. } M^* := M || PK_1 || ... || PK_n \\
&\text{3. } \sigma'_{i^*} \gets \mathsf{Sign}'_{sk_{S,i^*}}(M^*) \\
&\text{4. 对 } i \in [n]:\\
&\quad \text{若 } i = i^*: C^*_i = \mathsf{Enc}^*_{R_E}(\sigma'_{i^*}; \omega_i)\\
&\quad \text{否则: } C^*_i = \mathsf{Enc}^*_{R_E}(0^{|\sigma'|}; \omega_i) \\
&\text{5. } \pi = \mathcal{P}_{r_1}( \bigvee_{i=1}^n (pk_{S,i}, M^*, R_E, C^*_i) \in L, (\sigma'_{i^*}, \omega_{i^*}))\\
&\text{6. 输出 } \sigma = (C^*_1, ..., C^*_n, \pi)
\end{aligned}
$$
> 作用：描述了通用构造中签名者是如何将标准签名隐藏在众多密文中，并用ZAP证明其正确性的。

**[2用户方案的签名验证方程]**
$$
\hat{e}(g_1, \bar{g}_1) \cdot \hat{e}(B, w \cdot \bar{w}) = \hat{e}(A, g)
$$
> 作用：双线性配对验证，保证了签名 $(A, B)$ 的有效性。其关键性质是，等式左侧的 $g_1$ 和 $\bar{g}_1$ 在双线性映射下是对称的，从而保证了匿名性。

**[通用构造的密钥生成 (Gen)]**
$$
\begin{aligned}
&\text{1. } (pk_S, sk_S) \gets \mathsf{Gen}'(1^k)\\
&\text{2. } (pk_E, sk_E) \gets \mathsf{EGen}(1^k); \text{ 并丢弃 } sk_E\\
&\text{3. } r \gets \{0, 1\}^{\ell(k)}\\
&\text{4. 输出 } PK = (pk_S, pk_E, r), \ SK = sk_S
\end{aligned}
$$
> 作用：该密钥生成算法展示了通用构造中，一个用户的公钥由签名公钥、加密公钥和一个随机字符串组成，而私钥仅是签名私钥。

### 实验结果
本文是纯粹的理论工作，并未提供任何针对实现方案的实验性能数据，也没有在特定硬件或数据集上进行测试。论文的核心贡献在于形式化定义和标准模型下可证安全的构造。其“效率”分析主要体现在理论层面的计算复杂度和通信开销对比上。通用构造的计算复杂度与环的大小 n 线性相关，主要开销来源于生成 n 个密文（每个密文包含一个 n 次加密）以及生成一个 ZAP 证明。ZAP 证明的计算成本非常高，因为它需要为 OR 关系提供一个非交互证明，通常只能在理论上证明存在。相比之下，2用户方案的计算复杂度极低，仅需进行常数次群元素运算和几个双线性对（验证时需计算 $\hat{e}(g_1, \bar{g}_1)$ 和 $\hat{e}(B, w \cdot \bar{w})$）。因此，从实用角度看，2用户方案是高效的，而通用构造主要用于证明可行性与理论上的安全性。论文证明了前者的不可伪造性归约到Waters签名 [21] 的安全性，是紧的，这意味着在实际应用中可以选择相对安全参数，性能损失在可接受的范围内。

### 局限性与开放问题
通用构造虽然理论上可行，但依赖于ZAP这一复杂且有争议的密码学原语，导致其效率极低，实用性有限。2用户方案虽高效，但只能处理恰好两个用户组成的环，应用场景受限。未来的一个重要开放问题是设计一个在标准模型下既高效又可扩展（支持任意规模环）的环签名方案，这类方案至今仍然非常少见。此外，如何构造在标准模型下同时满足抗输出性（unforgeability w.r.t. insider corruption）和强匿名性（anonymity against full key exposure）的高效方案依然是一个挑战。

### 强关联论文

[21] B. Waters. Efficient identity-based encryption without random oracles. **Eurocrypt 2005** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+identity-based+encryption+without+random+oracles)

[10] I. Damgård and J.B. Nielsen. Improved non-committing encryption schemes based on a general complexity assumption. **Crypto 2000** [Google Scholar](https://scholar.google.com/scholar?q=Improved+non-committing+encryption+schemes+based+on+a+general+complexity+assumption)

[12] C. Dwork and M. Naor. Zaps and their applications. **FOCS 2000** [Google Scholar](https://scholar.google.com/scholar?q=Zaps+and+their+applications)

[3] M. Bellare, D. Micciancio, and B. Warinschi. Foundations of group signatures: Formal definitions, simplified requirements, and a construction based on general assumptions. **Eurocrypt 2003** [Google Scholar](https://scholar.google.com/scholar?q=Foundations+of+group+signatures)

[1] M. Abe, M. Ohkubo, and K. Suzuki. 1-out-of-n signatures from a variety of keys. **Asiacrypt 2002** [Google Scholar](https://scholar.google.com/scholar?q=1-out-of-n+signatures+from+a+variety+of+keys)

[20] R.L. Rivest, A. Shamir, and Y. Tauman. How to leak a secret. **Asiacrypt 2001** [Google Scholar](https://scholar.google.com/scholar?q=How+to+leak+a+secret)


## 关键词

+ 环签名强安全性定义
+ 匿名性不可伪造性形式化
+ 标准模型环签名构造
+ 无随机预言模型安全证明
+ 临时性签名群组密码
+ 环签名安全性分离结果