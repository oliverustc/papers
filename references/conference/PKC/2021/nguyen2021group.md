---
title: "Group encryption: full dynamicity, message filtering and code-based instantiation"
标题简称:
论文类型: conference
会议简称: PKC
发表年份: 2021
created: 2025-05-13 05:40:32
modified: 2025-05-13 05:41:51
---

## Group encryption: full dynamicity, message filtering and code-based instantiation

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-030-75248-4_24)

## 作者

+ [Khoa Nguyen](Khoa%20Nguyen.md)
+ Reihaneh Safavi-Naini
+ [Willy Susilo](Willy%20Susilo.md)
+ [Huaxiong Wang](Huaxiong%20Wang.md)
+ [Yanhong Xu](Yanhong%20Xu.md)
+ Neng Zeng

## 笔记

### 背景与动机

群组加密（GE）是群组签名的加密对偶，允许发送者将满足特定要求的消息加密给群组的认证成员，同时保持接收者的匿名性，并在必要时由开启权威（OA）识别接收者。然而，自 Kiayias 等人于 Asiacrypt 2007 提出以来，GE 的发展远落后于群组签名，主要存在三方面瓶颈：第一，现有模型仅支持动态加入，而用户撤销问题从未被正式处理，撤销用户仍可能解密新密文；第二，消息过滤功能在所有已知实例中仅基于计算困难问题（如离散对数、配对、SIS）定义，无法用于现实中的垃圾邮件过滤；第三，除格基构造外，其他 GE 方案均易受量子攻击，而基于码的构造尚属空白。本文旨在同时填补这三项空白，提出全动态群组加密（FDGE）的形式化模型、支持两种现实过滤策略（允许性和禁止性）的方法，并给出首个基于码的实例化方案。

### 相关工作

[29] Kiayias 等. Group Encryption. **Asiacrypt 2007** [Google Scholar](https://scholar.google.com/scholar?q=Group+Encryption+Kiayias)
> 核心思路：首次提出群组加密概念，基于 DCR 和 DDH 假设给出实例化，支持动态加入，但无撤销功能，消息过滤仅支持离散对数关系。
> 局限与区别：不提供用户撤销机制，过滤策略不实用，且基于经典困难问题。

[15] Cathalo 等. Group Encryption: Non-Interactive Realization in the Standard Model. **Asiacrypt 2009** [Google Scholar](https://scholar.google.com/scholar?q=Group+Encryption+Non-Interactive+Realization+Cathalo)
> 核心思路：在标准模型下给出基于配对的非交互式 GE 构造。
> 局限与区别：仍不支持撤销，过滤仍基于配对关系。

[1] El Aimani, Joye. Toward Practical Group Encryption. **ACNS 2013** [Google Scholar](https://scholar.google.com/scholar?q=Toward+Practical+Group+Encryption+El+Aimani)
> 核心思路：改进配对基 GE 的效率。
> 局限与区别：未处理撤销和实用过滤。

[32] Libert 等. Zero-Knowledge Arguments for Matrix-Vector Relations and Lattice-Based Group Encryption. **Theor. Comput. Sci. 2019** (会议版 Asiacrypt 2016) [Google Scholar](https://scholar.google.com/scholar?q=Zero-Knowledge+Arguments+for+Matrix-Vector+Relations+and+Lattice-Based+Group+Encryption)
> 核心思路：首个基于格假设的 GE 方案，抗量子。
> 局限与区别：不支持撤销，过滤基于 SIS 关系；通信开销大（含 $\log^2 q$ 因子，$q>2^{30}$）；本文码基方案比其高效约两个数量级。

[36] Libert 等. Traceable Group Encryption. **PKC 2014** [Google Scholar](https://scholar.google.com/scholar?q=Traceable+Group+Encryption+Libert)
> 核心思路：引入可追踪机制，允许发布用户特定陷门进行公开追踪。
> 局限与区别：未提供完整的撤销功能，且匿名性仅为弱概念。

[10] Bootle 等. Foundations of Fully Dynamic Group Signatures. **ACNS 2016** [Google Scholar](https://scholar.google.com/scholar?q=Foundations+of+Fully+Dynamic+Group+Signatures+Bootle)
> 核心思路：提出全动态群组签名的鲁棒安全模型，支持加入和撤销。
> 区别：本文将其模型适配到群组加密场景，定义为 FDGE。

[45] Nguyen 等. New Code-Based Privacy-Preserving Cryptographic Constructions. **Asiacrypt 2019** [Google Scholar](https://scholar.google.com/scholar?q=New+Code-Based+Privacy-Preserving+Cryptographic+Constructions+Nguyen)
> 核心思路：基于码的 Merkle 树累加器、范围证明、对数大小环签名和群组签名。
> 区别：本文利用其累加器方案代替数字签名来认证用户公钥，实现动态撤销。

[46] Nojima 等. Semantic Security for the McEliece Cryptosystem Without Random Oracles. **Des. Codes Cryptogr. 2008** [Google Scholar](https://scholar.google.com/scholar?q=Semantic+Security+for+the+McEliece+Cryptosystem+Without+Random+Oracles)
> 核心思路：给出随机化 McEliece 加密方案，具有伪随机密文性质。
> 区别：本文用其作为基础 PKE 并应用 Naor-Yung 转换实现 CCA2 安全。

[44] Naor, Yung. Public-Key Cryptosystems Provably Secure Against Chosen Ciphertext Attacks. **STOC 1990** [Google Scholar](https://scholar.google.com/scholar?q=Public-Key+Cryptosystems+Provably+Secure+Against+Chosen+Ciphertext+Attacks+Naor)
> 核心思路：通过双重加密和零知识证明实现 CCA2 安全。
> 区别：本文采用该转换，将两个 CPA 安全 McEliece 密文结合零知识证明以抵抗选择密文攻击。

[38] Ling 等. Lattice-Based Group Signatures: Achieving Full Dynamicity (and Deniability) with Ease. **Theor. Comput. Sci. 2019** [Google Scholar](https://scholar.google.com/scholar?q=Lattice-Based+Group+Signatures+Achieving+Full+Dynamicity)
> 核心思路：利用 Merkle 树实现全动态群组签名，加入时将叶节点从 0 改为哈希值，撤销时改回 0。
> 区别：本文将该思想应用于群组加密，并适配码基环境。

### 核心技术与方案

**1. 全动态群组加密（FDGE）模型**  
本文借鉴 Bootle 等人 [10] 的全动态群组签名模型，定义 FDGE 的语法和安全性。模型包含设立、OA 密钥生成、GM 密钥生成、关系生成、加入/发行协议、群组更新 GUpdate、加密 Enc、证明 $\mathcal{P}$、验证 $\mathcal{V}$、解密 Dec 和打开 Open 算法。群组信息 $\mathsf{info}_\tau$ 在每个时间段 $\tau$ 发布，反映当前活跃成员。撤销通过 GUpdate 将对应叶子置零实现，GM 可在 $\mathcal{O}(\log N)$ 时间内更新 Merkle 树。安全性包括消息保密性（真实与随机不可区分）、匿名性（接收者不可区分）和可靠性（无法伪造有效密文指向非活跃用户）。在保密性和匿名性中，敌手可完全腐化 GM 和/或 OA；可靠性中仅允许部分腐化 OA。

**2. 消息过滤的零知识证明**  
针对“允许性”策略（消息至少包含一个关键词子串），将消息 $\mathbf{w}\in\{0,1\}^p$ 的全体长度为 $t$ 的子串构成矩阵 $\mathbf{W}\in\mathbb{Z}_2^{t\times(p-t+1)}$，关键词构成矩阵 $\mathbf{S}\in\{0,1\}^{t\times k}$。则存在权重1向量 $\mathbf{g}\in\{0,1\}^{p-t+1},\mathbf{h}\in\{0,1\}^k$ 使得 $\mathbf{W}\mathbf{g}=\mathbf{S}\mathbf{h}$。证明通过 Stern 协议处理二次关系（实质是 LPN 型关系）和固定权重关系，通信开销 $\mathcal{O}(t\cdot(p-t)+k)$。  
针对“禁止性”策略（所有子串与所有关键词的汉明距离至少为 $d$），考虑每个子串与关键词的异或和 $\mathbf{z}_{i,j}$，将其扩展为 $2t-d$ 位使得扩展后向量权重为 $t$，等价于原向量权重至少为 $d$。然后用 Stern 协议证明固定权重向量，通信开销 $\mathcal{O}(t\cdot(p-t+1)\cdot k)$。

**3. 码基 FDGE 实例化**  
- **基础加密**：使用随机化 McEliece 加密 [46]，通过 Naor-Yung 双重加密 [44] 实现 CCA2 安全。发送者用接收者的公钥 $\mathsf{pk}=(\mathbf{G}_0,\mathbf{G}_1)$ 加密消息 $\mathbf{w}$ 得到双密文 $\mathbf{c}_w=(\mathbf{c}_{w,0},\mathbf{c}_{w,1})$，其中 $\mathbf{c}_{w,b}=\mathbf{G}_{j,b}\cdot\binom{\mathbf{r}_{w,b}}{\mathbf{w}}\oplus\mathbf{e}_{w,b}$；同时用 OA 公钥加密接收者身份 $\mathsf{bin}(j)$ 得到 $\mathbf{c}_{\mathsf{oa}}$。  
- **认证机制**：用 Merkle 树累加器 [45] 代替数字签名。用户加入时将其公钥哈希值 $\mathbf{d}\neq\mathbf{0}$ 放入叶子，GM 维护树根 $\mathbf{u}_\tau$。撤销时将该叶子置零。发送者需零知识证明 $\mathbf{d}$ 被累加到当前树根、密文正确、消息满足过滤策略。  
- **零知识证明**：所有证明均归约为 Stern 协议框架下的抽象关系 $R_{\text{abstract}}$：矩阵乘法 $\mathbf{M}\cdot\mathbf{w}=\mathbf{v}$ 且 $\mathbf{w}\in\mathsf{VALID}$。其中 VALID 定义满足特定结构（如固定权重、扩展形式等），并通过置换群保证零知识性和可靠性。交互重复 $\kappa=\omega(\log\lambda)$ 次，经 Fiat-Shamir 转换为非交互证明。  
- **安全性**：依赖于随机化 McEliece 的伪随机密文性质、哈希函数 $h_{\mathbf{B}}$ 的抗碰撞性、以及零知识论证的模拟零知识性和可靠性。在随机预言机模型下证明满足消息保密性、匿名性和可靠性（定理 1）。  
- **复杂度**：GM 密钥 $\mathcal{O}(\lambda)$ 位；OA 和用户密钥 $\mathcal{O}(\lambda^2)$ 位；发送者需下载 $\mathcal{O}(\lambda\cdot\ell)$ 位数据（$\ell=\log N$，$N$ 最大用户数）；验证者只需 $\mathcal{O}(\lambda)$ 位；密文大小 $\mathcal{O}(\lambda^2)$；证明大小 $\omega(\log\lambda)\cdot\mathcal{O}(\lambda^2+\ell\lambda)$。

### 核心公式与流程

**[LPN 型关系归约]**
$$ \mathbf{c} = \mathbf{A} \cdot \mathbf{r} \oplus \mathbf{e} \;\Longleftrightarrow\; \mathbf{c} = \mathbf{H}_{n,m}' \cdot \text{expand}'(\mathbf{A}, \mathbf{r}) \oplus \mathbf{e}, $$
其中 $\mathbf{z} = \text{expand}'(\mathbf{A}, \mathbf{r})$ 是扩展后的向量，$\mathbf{H}_{n,m}'$ 是块对角矩阵，从而转化为标准线性方程 $\mathbf{c} = \mathbf{M}_{\mathrm{VLPN}} \cdot \mathbf{w}_{\mathrm{VLPN}}$ 且 $\mathbf{w}_{\mathrm{VLPN}} \in \mathsf{VALID}_{\mathrm{VLPN}}$。
> 作用：将含有隐藏矩阵的 LPN 关系归约到 Stern 框架的抽象关系。

**[允许性策略矩阵表示]**
$$ \mathbf{W} = [\mathbf{w}_{[1]} \mid \dots \mid \mathbf{w}_{[p-t+1]}] \in \{0,1\}^{t\times(p-t+1)},\quad \mathbf{S} = [\mathbf{s}_1 \mid \dots \mid \mathbf{s}_k] \in \{0,1\}^{t\times k}, $$
存在权重 1 向量 $\mathbf{g},\mathbf{h}$ 使得 $\mathbf{W}\mathbf{g} = \mathbf{S}\mathbf{h}$。
> 作用：将“存在子串等于某关键词”条件转化为双线性方程。

**[禁止性策略扩展技巧]**
对每个 $\mathbf{z}_{i,j} = \mathbf{w}_{[i]} \oplus \mathbf{s}_j \in \{0,1\}^t$，追加 $(t-d)$ 个零得到 $\mathbf{z}_{i,j}^* \in \{0,1\}^{2t-d}$，若 $\mathbf{z}_{i,j}^* \in \mathsf{B}(2t-d, t)$ 则 $wt(\mathbf{z}_{i,j}) \ge d$。
> 作用：将“汉明距离至少 d”条件转化为证明固定权重向量。

**[McEliece 双重加密]**
$$ \mathbf{c}_{w,b} = \mathbf{G}_{j,b} \cdot \binom{\mathbf{r}_{w,b}}{\mathbf{w}} \oplus \mathbf{e}_{w,b}, \quad b\in\{0,1\}; $$
$$ \mathbf{c}_{\mathsf{oa},b} = \mathbf{G}_{\mathsf{oa},b} \cdot \binom{\mathbf{r}_{\mathsf{oa},b}}{\mathsf{bin}(j)} \oplus \mathbf{e}_{\mathsf{oa},b}, \quad b\in\{0,1\}. $$
> 作用：构成 Naor-Yung 双加密，提供 CCA2 安全性。

### 实验结果

本文未提供具体实验数值，因为方案是概念证明（proof-of-concept），且涉及的重型零知识论证使其不实用。但论文从理论渐进复杂度比较了与格基方案 [32] 的效率：本文通信开销比 [32] 小约两个数量级（128 位安全级别），主要原因是 [32] 使用标准模型格签名导致 $\log^2 q$ 因子（$q>2^{30}$），而本文使用 Merkle 树及码基累加器避免了该开销。具体数值估计：通信开销中密文和证明的大小为 $\omega(\log\lambda)\cdot\mathcal{O}(\lambda^2+\ell\lambda)$，对于 $\lambda=128$、$\ell\approx 20$ 时，约数 MB 量级。方案不支持当前实用化，但为后量子 GE 提供了更优渐进效率的选择。

### 局限性与开放问题

本文方案仅作为概念验证，由于零知识论证涉及大量重复（$\kappa$ 次，每次通信开销 $\mathcal{O}(\lambda^2)$），实际运行时通信和计算开销仍很高，无法直接部署。此外，用户加入时 GM 需通过解密挑战验证用户持有解密密钥，此交互过程效率较低。未来工作包括寻找更具实用性的后量子 GE 方案、优化零知识证明的通信轮次和大小、以及探索基于其他量子安全假设（如多变量、同源）的实例化。

### 强关联论文

[29] Kiayias, A., Tsiounis, Y., Yung, M. Group Encryption. **Asiacrypt 2007** [Google Scholar](https://scholar.google.com/scholar?q=Group+Encryption+Kiayias)

[15] Cathalo, J., Libert, B., Yung, M. Group Encryption: Non-Interactive Realization in the Standard Model. **Asiacrypt 2009** [Google Scholar](https://scholar.google.com/scholar?q=Group+Encryption+Non-Interactive+Realization+in+the+Standard+Model)

[32] Libert, B., Ling, S., Mouhartem, F., Nguyen, K., Wang, H. Zero-Knowledge Arguments for Matrix-Vector Relations and Lattice-Based Group Encryption. **Theor. Comput. Sci. 2019** [Google Scholar](https://scholar.google.com/scholar?q=Zero-Knowledge+Arguments+for+Matrix-Vector+Relations+and+Lattice-Based+Group+Encryption)

[36] Libert, B., Yung, M., Joye, M., Peters, T. Traceable Group Encryption. **PKC 2014** [Google Scholar](https://scholar.google.com/scholar?q=Traceable+Group+Encryption)

[10] Bootle, J., Cerulli, A., Chaidos, P., Ghadafi, E., Groth, J. Foundations of Fully Dynamic Group Signatures. **ACNS 2016** [Google Scholar](https://scholar.google.com/scholar?q=Foundations+of+Fully+Dynamic+Group+Signatures)

[45] Nguyen, K., Tang, H., Wang, H., Zeng, N. New Code-Based Privacy-Preserving Cryptographic Constructions. **Asiacrypt 2019** [Google Scholar](https://scholar.google.com/scholar?q=New+Code-Based+Privacy-Preserving+Cryptographic+Constructions)

[46] Nojima, R., Imai, H., Kobara, K., Morozov, K. Semantic Security for the McEliece Cryptosystem Without Random Oracles. **Des. Codes Cryptogr. 2008** [Google Scholar](https://scholar.google.com/scholar?q=Semantic+Security+for+the+McEliece+Cryptosystem+Without+Random+Oracles)

[44] Naor, M., Yung, M. Public-Key Cryptosystems Provably Secure Against Chosen Ciphertext Attacks. **STOC 1990** [Google Scholar](https://scholar.google.com/scholar?q=Public-Key+Cryptosystems+Provably+Secure+Against+Chosen+Ciphertext+Attacks)

[38] Ling, S., Nguyen, K., Wang, H., Xu, Y. Lattice-Based Group Signatures: Achieving Full Dynamicity (and Deniability) with Ease. **Theor. Comput. Sci. 2019** [Google Scholar](https://scholar.google.com/scholar?q=Lattice-Based+Group+Signatures+Achieving+Full+Dynamicity)

[49] Stern, J. A New Paradigm for Public Key Identification. **IEEE Trans. Inf. Theory 1996** [Google Scholar](https://scholar.google.com/scholar?q=A+New+Paradigm+for+Public+Key+Identification+Stern)


## 关键词

+ 群加密
+ 完全动态群加密（FDGE）
+ 消息过滤
+ 编码假设
+ 后量子密码学
+ 用户撤销机制