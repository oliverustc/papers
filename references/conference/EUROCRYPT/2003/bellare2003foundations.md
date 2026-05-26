---
title: "Foundations of group signatures: Formal definitions, simplified requirements, and a construction based on general assumptions"
标题简称:
论文类型: conference
会议简称: EUROCRYPT
发表年份: 2003
created: 2025-05-26 03:37:59
modified: 2025-05-26 03:38:10
---

## Foundations of group signatures: Formal definitions, simplified requirements, and a construction based on general assumptions

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/3-540-39200-9_38)

## 作者

+ [Mihir Bellare](Mihir%20Bellare.md)
+ Daniele Micciancio
+ Bogdan Warinschi

## 笔记

### 背景与动机
群签名由 Chaum 和 van Heyst 于 EUROCRYPT 1991 提出 [14]，允许群成员代表群匿名签名，群管理者可追溯签名者身份。然而，此后涌现了大量非形式化的安全需求（如不可链接性、不可伪造性、抗合谋攻击 [5]、可责备性 [5]、抗陷害攻击 [15]），这些需求含义模糊、相互重叠，且缺乏统一的定义框架。现有方案 [2,5] 虽声称在随机预言机模型中可证明安全，但并未给出群签名安全的形式定义——例如，匿名性仅被描述为“给定有效签名，除管理者外任何人难以识别签名者”，这类似于仅用“密文不应泄露消息”来定义加密安全，而实际需要精确的攻击模型和优势刻画。此外，所有方案均依赖随机预言机，尚无标准模型下可证明安全的构造。本文旨在为群签名提供严格的形式化安全定义（全匿名性与全可追踪性），证明这两条强性质蕴含所有已有非形式化需求，并基于一般假设（陷门置换的存在性）在标准模型中给出一个满足定义的具体构造，从而填补群签名理论基础的空缺。

### 相关工作

[14] Chaum 等. Group signatures. **EUROCRYPT 1991** [Google Scholar](https://scholar.google.com/scholar?q=Group+signatures)
> 核心思路：首次引入群签名概念，提出基本匿名性与可追踪性需求。
> 局限与区别：未给出形式化安全定义，也未考虑合谋攻击。

[5] Ateniese 等. Some open issues and directions in group signature. **Financial Crypto 1999** [Google Scholar](https://scholar.google.com/scholar?q=Some+open+issues+and+directions+in+group+signature)
> 核心思路：指出群签名面临的重要开放问题，包括抗合谋攻击和可责备性。
> 局限与区别：仍缺乏统一的形式化定义，其提出的需求相互独立。

[2] Ateniese 等. A practical and provably secure coalition-resistant group signature scheme. **CRYPTO 2000** [Google Scholar](https://scholar.google.com/scholar?q=A+practical+and+provably+secure+coalition-resistant+group+signature+scheme)
> 核心思路：给出一个抗合谋攻击的群签名方案，并在随机预言机模型中证明安全。
> 局限与区别：未给出群签名的整体安全定义，仅分析子协议性质；依赖随机预言机假设。

[16] Dolev 等. Nonmalleable cryptography. **SIAM J. Comput. 2000** [Google Scholar](https://scholar.google.com/scholar?q=Nonmalleable+cryptography)
> 核心思路：提出公钥加密的不可延展性及 IND-CCA 安全概念，并给出基于陷门置换的构造。
> 区别：本文用 IND-CCA 安全加密作为构件，而非仅用 CPA 安全。

[17] Feige 等. Multiple non-interactive zero-knowledge proofs under general assumptions. **SIAM J. Comput. 1999** [Google Scholar](https://scholar.google.com/scholar?q=Multiple+non-interactive+zero-knowledge+proofs+under+general+assumptions)
> 核心思路：给出基于一般假设（陷门置换）的非交互零知识证明系统。
> 区别：本文需模拟声音的 NIZK，并利用 [27] 的变换获得该性质。

[27] Sahai. Non-malleable non-interactive zero knowledge and adaptive chosen-ciphertext security. **FOCS 1999** [Google Scholar](https://scholar.google.com/scholar?q=Non-malleable+non-interactive+zero+knowledge+and+adaptive+chosen-ciphertext+security)
> 核心思路：构造模拟声音的 NIZK 系统，并用于实现 CCA 安全加密。
> 区别：本文要求 NIZK 同时满足模拟声音性和适应性零知识，该文献提供了理论基础。

[6] Bellare 等. How to sign given any trapdoor permutation. **J. ACM 1992** [Google Scholar](https://scholar.google.com/scholar?q=How+to+sign+given+any+trapdoor+permutation)
> 核心思路：基于陷门置换构造安全的数字签名方案。
> 区别：本文用该方案作为群成员签名方案的基础构件。

[20] Goldwasser 等. A digital signature scheme secure against adaptive chosen-message attacks. **SIAM J. Comput. 1988** [Google Scholar](https://scholar.google.com/scholar?q=A+digital+signature+scheme+secure+against+adaptive+chosen-message+attacks)
> 核心思路：提出适应性选择消息攻击下的不可伪造性定义。
> 区别：本文要求成员签名满足该标准的安全性。

### 核心技术与方案

#### 形式化安全定义

本文首先定义了群签名方案的四元组算法（GKg，GSig，GVf，Open），要求正确性：真签名总能通过验证且打开算法正确恢复签名者身份。然后提出两个强安全性质：

**全匿名性** 采用不可区分性实验（图1左）。攻击者拥有所有群成员的秘密密钥及访问打开预言机（除挑战签名外）的能力。在挑战阶段，攻击者选择消息 $m$ 和两个身份 $i_0, i_1$；挑战者随机选 $b \leftarrow \{0,1\}$，返回用 $\mathbf{gsk}[i_b]$ 对 $m$ 的签名 $\sigma$；攻击者需猜测 $b$。优势定义为 $\mathbf{Adv}_{\mathcal{GS},A}^{\mathrm{anon}}(k,n) = \Pr[\mathrm{Exp}^{\mathrm{anon-1}}=1] - \Pr[\mathrm{Exp}^{\mathrm{anon-0}}=1]$。若对所有多项式时间攻击者该优势可忽略，则方案满足全匿名性。

**全可追踪性** 采用实验（图1右）。攻击者已知群管理者秘密密钥 $\mathrm{gmsk}$，可自适应地腐化若干群成员（获得其秘密密钥 $\mathbf{gsk}[j]$），并最终输出一个消息-签名对 $(m,\sigma)$ 使得：$\sigma$ 是有效签名，但打开算法输出 $\bot$ 或输出某个未被腐化的成员身份（且该成员未对该消息签过名）。若对任何多项式时间攻击者，该事件概率可忽略，则方案满足全可追踪性。

#### 蕴含关系

本文证明全匿名性和全可追踪性蕴含了所有已有的非形式化安全需求，包括：
- 不可伪造性：将全可追踪性实验中攻击者限制为无腐化且无 $\mathrm{gmsk}$ 即得。
- 可责备性：若攻击者（群管理者或用户）能陷害他人，则可直接转化为全可追踪性攻击。
- 抗合谋攻击：全可追踪性实验已允许任意数量成员合谋。
- 抗陷害攻击：全可追踪性直接阻止签名被打开为未参与者。
- 不可链接性：从全匿名性可推导（论文指出该事实将在完整版中证明）。

#### 基于一般假设的构造

本文使用三个基本构件：IND-CCA 安全公钥加密方案 $\mathcal{AE}$（由 [16] 基于陷门置换存在性得到）、适应性选择消息攻击下不可伪造的数字签名方案 $\mathcal{DS}$（由 [6] 基于陷门置换得到）、以及针对特定 NP 关系 $\rho$ 的模拟声音非交互零知识证明系统 $(P,V)$（由 [17,27] 基于陷门置换得到）。关系 $\rho$ 定义如下：

$$((pk_e, pk_s, M, C), (i, pk', \mathrm{cert}, s, r)) \in \rho \iff \mathsf{Vf}(pk_s, \langle i, pk' \rangle, \mathrm{cert})=1 \;\wedge\; \mathsf{Vf}(pk', M, s)=1 \;\wedge\; \mathsf{Enc}(pk_e, \langle i, pk', \mathrm{cert}, s \rangle; r)=C.$$

构造如图2所示：
- **群密钥生成 GKg**：生成 $\mathcal{AE}$ 密钥对 $(pk_e, sk_e)$、$\mathcal{DS}$ 密钥对 $(pk_s, sk_s)$、以及公共参考串 $R$。对每个成员 $i=1\dots n$，生成签名密钥对 $(pk_i, sk_i)$，由管理者用 $sk_s$ 对 $\langle i, pk_i \rangle$ 签名得到证书 $\mathrm{cert}_i$。成员密钥 $\mathbf{gsk}[i] = (k, R, i, pk_i, sk_i, \mathrm{cert}_i, pk_e, pk_s)$。群公钥 $gpk = (R, pk_e, pk_s)$，群管理者密钥 $gmsk = (n, pk_e, sk_e, pk_s)$。
- **群签名 GSig**：成员用 $sk_i$ 对消息 $m$ 签名得 $s$，随机选择 $r$，以 $pk_e$ 加密 $\langle i, pk_i, \mathrm{cert}_i, s \rangle$ 得密文 $C$，然后生成 NIZK 证明 $\pi$ 证明存在 $(i, pk_i, \mathrm{cert}_i, s, r)$ 使得该关系成立。签名 $\sigma = (C, \pi)$。
- **验证 GVf**：验证 $\pi$ 相对于定理 $(pk_e, pk_s, m, C)$ 的有效性。
- **打开 Open**：验证 $\pi$，若无效返回 $\bot$；否则用 $sk_e$ 解密 $C$ 得到 $\langle i, pk, \mathrm{cert}, s \rangle$，检查 $i \le n$、$\mathrm{cert}$ 是 $\langle i, pk \rangle$ 的有效证书、$s$ 是 $m$ 在 $pk$ 下的有效签名，若通过则返回 $i$，否则返回 $\bot$。

#### 安全性证明概要

**引理1（全匿名性）**：若 $\mathcal{AE}$ 是 IND-CCA 安全的，且 $(P,V)$ 是模拟声音的计算零知识证明系统，则构造的方案是全匿名的。证明策略：构造一系列游戏，逐步将挑战签名中的加密替换为对无关消息的加密，利用零知识性质模拟证明，最终将匿名性归约到 IND-CCA 安全。

**引理2（全可追踪性）**：若 $\mathcal{DS}$ 是适应性选择消息攻击下不可伪造的，且 $(P,V)$ 是可靠的，则构造的方案是全可追踪的。证明策略：利用可靠性，敌手提供的有效签名中必有一个有效的解密结果，其包含的成员签名或证书之一必然构成对底层签名方案的伪造。

**定理1**：若陷门置换族存在，则存在紧致的、满足全匿名性和全可追踪性的群签名方案。紧致性体现在密钥和签名长度均为 $\mathrm{poly}(k, \log n)$。

### 核心公式与流程

**关系ρ定义**
$$((pk_e, pk_s, M, C), (i, pk', \mathrm{cert}, s, r)) \in \rho \iff \mathsf{Vf}(pk_s, \langle i, pk' \rangle, \mathrm{cert})=1 \;\wedge\; \mathsf{Vf}(pk', M, s)=1 \;\wedge\; \mathsf{Enc}(pk_e, \langle i, pk', \mathrm{cert}, s \rangle; r)=C.$$
> 定义了签名者需要证明的NP关系：密文C是对某成员身份、公钥、证书和签名的加密，且这些结构满足正确的验证关系。

**全匿名性实验**
$$\begin{aligned}
&\mathbf{Exp}_{\mathcal{GS},A}^{\mathrm{anon-b}}(k,n): \\
&(gpk,gmsk,\mathbf{gsk}) \xleftarrow{\$} \mathsf{GKg}(1^k,1^n) \\
&(St,i_0,i_1,m) \xleftarrow{\$} A^{\mathrm{Open}(gmsk,\cdot,\cdot)}(\text{choose},gpk,\mathbf{gsk}) \\
&\sigma \xleftarrow{\$} \mathsf{GSig}(\mathbf{gsk}[i_b],m) \\
&d \xleftarrow{\$} A^{\mathrm{Open}(gmsk,\cdot,\cdot)}(\text{guess},St,\sigma) \\
&\text{If } A \text{ did not query } (m,\sigma) \text{ then return } d \text{ else return } 0.
\end{aligned}$$
> 定义全匿名性：攻击者知道所有成员密钥和公开密钥，可访问打开预言机，选择两个身份和消息，获得其中一人的签名后猜测是哪一个。

**全可追踪性实验**
$$\begin{aligned}
&\mathbf{Exp}_{\mathcal{GS},A}^{\mathrm{trace}}(k,n): \\
&(gpk,gmsk,\mathbf{gsk}) \xleftarrow{\$} \mathsf{GKg}(1^k,1^n) \\
&St \leftarrow (gmsk,gpk); \; \mathcal{C} \leftarrow \emptyset; \; K \leftarrow \varepsilon; \; \text{Cont} \leftarrow \text{true} \\
&\text{While (Cont = true)}: \\
&\quad (\text{Cont},St,j) \xleftarrow{\$} A^{\mathrm{GSig}(gsk[\cdot],\cdot)}(\text{choose},St,K) \\
&\quad \text{If Cont = true: } \mathcal{C} \leftarrow \mathcal{C} \cup \{j\}; \; K \leftarrow \mathbf{gsk}[j] \\
&(m,\sigma) \xleftarrow{\$} A^{\mathrm{GSig}(gsk[\cdot],\cdot)}(\text{guess},St) \\
&\text{If GVf}(gpk,m,\sigma)=0 \text{ return } 0 \\
&\text{If Open}(gmsk,m,\sigma)=\bot \text{ return } 1 \\
&\text{If } \exists i\text{ such that Open}(gmsk,m,\sigma)=i \notin \mathcal{C} \text{ and } i,m\text{ not queried then return } 1 \\
&\text{else return } 0.
\end{aligned}$$
> 定义全可追踪性：攻击者已知gmsk，可自适应腐化成员并获得其密钥，最终输出有效签名，若打开失败或打开为未腐化成员且该成员未签过该消息，则攻击成功。

**构造方案（算法伪代码）**
$$\begin{aligned}
&\mathsf{GKg}(k,n): \\
&\; R \xleftarrow{\$} \{0,1\}^{p(k)};\; (pk_e,sk_e) \xleftarrow{\$} \mathsf{K}_e(k);\; (pk_s,sk_s) \xleftarrow{\$} \mathsf{K}_s(k) \\
&\; \text{For } i=1\text{ to } n: \\
&\quad (pk_i,sk_i) \xleftarrow{\$} \mathsf{K}_s(k);\; \mathrm{cert}_i \leftarrow \mathsf{Sig}(sk_s,\langle i,pk_i\rangle) \\
&\quad \mathbf{gsk}[i] \leftarrow (k,R,i,pk_i,sk_i,\mathrm{cert}_i,pk_e,pk_s) \\
&\; gpk \leftarrow (R,pk_e,pk_s);\; gmsk \leftarrow (n,pk_e,sk_e,pk_s) \\
&\; \text{return } (gpk,gmsk,\mathbf{gsk}) \\
&\mathsf{GSig}(\mathbf{gsk}[i],m): \\
&\; \text{parse } \mathbf{gsk}[i] = (k,R,i,pk_i,sk_i,\mathrm{cert}_i,pk_e,pk_s) \\
&\; s \leftarrow \mathsf{Sig}(sk_i,m);\; r \xleftarrow{\$} \{0,1\}^k;\; C \leftarrow \mathsf{Enc}(pk_e,\langle i,pk_i,\mathrm{cert}_i,s\rangle;r) \\
&\; \pi \xleftarrow{\$} P(k,(pk_e,pk_s,m,C),(i,pk_i,\mathrm{cert}_i,s,r),R) \\
&\; \sigma \leftarrow (C,\pi);\; \text{return } \sigma \\
&\mathsf{GVf}(gpk,(m,\sigma)): \\
&\; \text{parse } gpk = (R,pk_e,pk_s);\; \text{parse } \sigma = (C,\pi) \\
&\; \text{return } V(k,(pk_e,pk_s,m,C),\pi,R) \\
&\mathsf{Open}(gmsk,gpk,m,\sigma): \\
&\; \text{parse } gmsk = (n,pk_e,sk_e,pk_s);\; \text{parse } \sigma = (C,\pi) \\
&\; \text{if } V(k,(m,C),\pi,R)=0 \text{ return } \bot \\
&\; \text{parse } \mathsf{Dec}(sk_e,C) = \langle i,pk,\mathrm{cert},s\rangle \\
&\; \text{if } (n<i \text{ or } \mathsf{Vf}(pk,m,s)=0 \text{ or } \mathsf{Vf}(pk_s,\langle i,pk\rangle,\mathrm{cert})=0) \text{ return } \bot \\
&\; \text{else return } i
\end{aligned}$$
> 描述了构造的具体步骤：群公钥包含NIZK参考串和加密/签名公钥；成员签名由加密的证书-签名对和NIZK证明组成；验证只验证NIZK；打开需解密并验证内部签名的正确性。

### 实验结果
该论文为纯理论工作，未提供实验验证。论文提出的构造基于一般假设（陷门置换），核心目的在于证明存在性而非实用性。作者明确指出所得方案是多项式时间但不可实用，应将其视为一个可行性结果。因此，没有性能数值、数据集或与 baseline 的对比。所有分析均通过形式化安全归约完成。

### 局限性与开放问题
本文方案仅适用于静态群（成员固定），动态群问题在第五节讨论但仅给出方向性扩展，未提供完整定义与构造。全匿名性和全可追踪性未涵盖群管理者不诚实的情形（如虚假打开），即使第五节提到了通过非承诺加密和可验证打开来解决，但未给出完整证明。此外，方案依赖陷门置换，实际应用中效率较低；是否存在基于更弱假设（如单向函数）或更高效（如基于双线性对）的构造仍是开放问题。

### 强关联论文

[14] D. Chaum, E. van Heyst. Group signatures. **EUROCRYPT 1991** [Google Scholar](https://scholar.google.com/scholar?q=Group+signatures)

[5] G. Ateniese, G. Tsudik. Some open issues and directions in group signature. **Financial Crypto 1999** [Google Scholar](https://scholar.google.com/scholar?q=Some+open+issues+and+directions+in+group+signature)

[2] G. Ateniese, J. Camenisch, M. Joye, G. Tsudik. A practical and provably secure coalition-resistant group signature scheme. **CRYPTO 2000** [Google Scholar](https://scholar.google.com/scholar?q=A+practical+and+provably+secure+coalition-resistant+group+signature+scheme)

[16] D. Dolev, C. Dwork, M. Naor. Nonmalleable cryptography. **SIAM J. Comput. 2000** [Google Scholar](https://scholar.google.com/scholar?q=Nonmalleable+cryptography)

[17] U. Feige, D. Lapidot, A. Shamir. Multiple non-interactive zero-knowledge proofs under general assumptions. **SIAM J. Comput. 1999** [Google Scholar](https://scholar.google.com/scholar?q=Multiple+non-interactive+zero-knowledge+proofs+under+general+assumptions)

[27] A. Sahai. Non-malleable non-interactive zero knowledge and adaptive chosen-ciphertext security. **FOCS 1999** [Google Scholar](https://scholar.google.com/scholar?q=Non-malleable+non-interactive+zero+knowledge+and+adaptive+chosen-ciphertext+security)

[6] M. Bellare, S. Micali. How to sign given any trapdoor permutation. **J. ACM 1992** [Google Scholar](https://scholar.google.com/scholar?q=How+to+sign+given+any+trapdoor+permutation)

[20] S. Goldwasser, S. Micali, R. Rivest. A digital signature scheme secure against adaptive chosen-message attacks. **SIAM J. Comput. 1988** [Google Scholar](https://scholar.google.com/scholar?q=A+digital+signature+scheme+secure+against+adaptive+chosen-message+attacks)


## 关键词

+ 群签名形式化定义
+ 匿名性
+ 可追踪性
+ 陷门置换
+ 密码学基础