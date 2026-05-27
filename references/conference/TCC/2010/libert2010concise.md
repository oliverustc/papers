---
title: "Concise mercurial vector commitments and independent zero-knowledge sets with short proofs"
doi: 10.1007/978-3-642-11799-2_30
标题简称:
论文类型: conference
会议简称: TCC
发表年份: 2010
---
## Concise mercurial vector commitments and independent zero-knowledge sets with short proofs

## 发表信息

+ [原文链接]()

## 作者

+ [[Benoît Libert]]
+ Moti Yung  


## 笔记

### 背景与动机
零知识集合由 Micali, Rabin 和 Kilian [21] 引入，允许证明者承诺一个秘密集合 S，随后能够非交互地证明元素 x 属于或不属于 S，而不泄露关于 S 的任何其他信息。Chase 等人 [10] 揭示了此类协议背后的核心原语是水银承诺，其具有“硬承诺”和“软承诺”两种模式，前者只能打开到唯一消息，后者可以软打开到任意消息且二者计算不可区分。为压缩长证明长度，Catalano, Fiore 和 Messina（CFM）[9] 提出了陷门 q-水银承诺 (qTMC)，允许承诺一个 q 维向量，并在特定位置给出短打开，从而结合高扇出 Merkle 树大幅缩短非成员证明。然而，CFM 方案的硬打开长度仍为 O(q)，导致成员证明远不及非成员证明紧凑。本文填补了这一空白：构造了一个新的 qTMC 方案，使得硬打开和软打开均具有常数大小（与 q 无关），并进一步将该方案应用于构建具有短证明的独立零知识集合。

### 相关工作

[8] Catalano, Dodis, Visconti. Mercurial Commitments: Minimal Assumptions and Efficient Constructions. **TCC 2006** [Google Scholar](https://scholar.google.com/scholar?q=Mercurial+Commitments+Minimal+Assumptions+and+Efficient+Constructions)
> 核心思路：给出了（非向量）水银承诺的简化安全定义，并基于单向函数在共享随机串模型中构造。
> 局限与区别：仅处理单个消息承诺，无法直接用于高扇出树以压缩证明长度，本文的工作是将其推广到向量情形。

[9] Catalano, Fiore, Messina. Zero-Knowledge Sets with Short Proofs. **EUROCRYPT 2008** [Google Scholar](https://scholar.google.com/scholar?q=Zero-Knowledge+Sets+with+Short+Proofs)
> 核心思路：首次定义 qTMC，并基于特定数论假设构造了一个软打开为常数大小的方案，用于构建短证明的零知识集合。
> 局限与区别：其硬打开长度为 O(q)，导致成员证明不紧凑；本文解决此问题，将硬打开也压缩至常数大小。

[10] Chase, Healy, Lysyanskaya, Malkin, Reyzin. Mercurial Commitments with Applications to Zero-Knowledge Sets. **EUROCRYPT 2005** [Google Scholar](https://scholar.google.com/scholar?q=Mercurial+Commitments+with+Applications+to+Zero-Knowledge+Sets)
> 核心思路：形式化水银承诺，并给出零知识数据库的一般构造，使用二进制 Merkle 树，每个内部节点包含一个水银承诺。
> 局限与区别：产生的证明长度随树高线性增长，本文采用高扇出树和 qTMC 来压缩证明。

[15] Gennaro, Micali. Independent Zero-Knowledge Sets. **ICALP 2006** [Google Scholar](https://scholar.google.com/scholar?q=Independent+Zero-Knowledge+Sets)
> 核心思路：定义强独立零知识集合，使用多陷门水银承诺来防止攻击者将自身数据库与诚实证明者的数据库关联。
> 局限与区别：其构造基于强 RSA 假设，且未关注证明长度；本文通过多陷门 qTMC 实现独立性，且同时拥有短证明。

[21] Micali, Rabin, Kilian. Zero-Knowledge Sets. **FOCS 2003** [Google Scholar](https://scholar.google.com/scholar?q=Zero-Knowledge+Sets)
> 核心思路：提出零知识集合的原始构造，基于离散对数假设和 Pedersen 承诺，使用二进制 Merkle 树。
> 局限与区别：证明长度相对较长，难以在带宽受限场景应用；本文方案的证明长度大幅缩短，例如成员证明仅需 13% 的原始长度。

### 核心技术与方案

本文的核心技术是构造一个简洁的 qTMC 方案。该方案受 Camenisch-Kohlweiss-Soriente 累加器 [6]（其本身受 Boneh-Gentry-Waters 广播加密 [5] 启发）的启发。方案在双线性群中工作，公共参数包括序列 $(g, g_1, \ldots, g_q, g_{q+2}, \ldots, g_{2q})$，其中 $g_i = g^{(\alpha^i)}$。关键思想在于，承诺 $V$ 被计算为一个随机化的屏蔽多项式：$V = g^\gamma \cdot \prod_{j=1}^q g_{q+1-j}^{m_j}$。对第 i 个位置的打开是一个证据 $W_i$，它被构造成使得等式 $e(g_i, V) = e(C, W_i) \cdot e(g_1, g_q)^{m_i}$ 成立。其中 $C$ 在硬承诺中为 $g^\theta$，在软承诺中为 $g_1^\theta$，从而通过修改 C 的结构来切换承诺的“硬度”。关键的创新在于，通过使用隐藏的 $g_{q+1}=g^{(\alpha^{q+1})}$ 作为陷门，可以实现软承诺（伪造承诺）的等效打开，且所有打开（无论是硬打开还是软打开）都仅包含常量个群元素（在非多陷门版本中，硬打开为 $(\theta, W_i) \in \mathbb{Z}_p \times \mathbb{G}$，软打开为 $W_i \in \mathbb{G}$）。

在安全性方面，方案的 q-水银绑定性质归约到 q-DHE 假设：若攻击者能为同一个承诺 C 生成针对同一位置 i 的两个不同消息的硬打开或软碰撞，则能计算出 $g_{q+1}$，从而打破 q-DHE 假设。方案的等价性质（q-HHE, q-HSE, q-SSE）通过论证伪造承诺与真实承诺（或软承诺）在分布上的不可区分性来证明，该论证同样依赖于 q-DHE 假设。

将该 qTMC 方案嵌入到 CFM [9] 的扁平树 ZK-EDB 构造中，即可得到短证明。树的高度 $h$ 满足 $q^h \ge 2^\lambda$（$\lambda$ 为安全参数）。成员证明在每个树层需要一个硬打开（$(\theta, W_i) \in \mathbb{Z}_p \times \mathbb{G}$），而非成员证明则需要一个软打开（$W_i \in \mathbb{G}$）。由于两者皆为常数大小（分别为 2 个和 1 个群元素），整个证明的长度由 $O(h)$ 群元素构成，与 $q$ 无关。例如，当 $q=128, h=19$ 时，成员证明仅需 100 个 $\mathbb{G}$ 元素（约 2kB），而非成员证明需 80 个。相比 CFM 方案成员证明需要 2513 个元素，大幅改善。

此外，本文将上述 qTMC 方案扩展到多陷门版本，以构建强独立的 ZK-EDB。该扩展通过引入一个可编程哈希函数 $H_\mathbb{G}: \mathcal{T} \to \mathbb{G}$ 和签名方案实现。具体地，每个证明者选择一个签名密钥对，公共展示验证密钥 VK，并基于标签 $\mathtt{tag} = H(\mathtt{VK})$ 来索引其 qTMC 承诺族。伪造承诺的等效打开需要该标签对应的特定陷门 $tk_{\mathtt{tag}}$，该陷门可由主陷门 $TK = g_{q+1}$ 通过 TrapGen 算法生成。攻击者在不能获得目标标签 $tag^*$ 的陷门（即无法伪造该标签下的承诺）的条件下无法产生碰撞，从而保证了数据库的独立性。该构造的安全证明与文献 [15] 中的定理 3 类似。

### 核心公式与流程

**[硬承诺生成 - qHCom]**
$$ C = g^{\theta}, \quad V = g^{\gamma} \cdot \prod_{j=1}^{q} g_{q+1-j}^{m_j} $$
> 作用：对消息向量 $(m_1, \ldots, m_q)$ 生成一个硬承诺 $(C, V)$，其中 $\theta, \gamma$ 是随机因子。

**[硬打开生成 - qHOpen]**
$$ W_i = \bigg( g_i^\gamma \cdot \prod_{j=1, j \neq i}^{q} g_{q+1-j+i}^{m_j} \bigg)^{1/\theta} $$
> 作用：硬打开承诺到位置 $i$ 上的消息 $m_i$，输出证据 $\pi = (\theta, W_i)$。

**[硬验证方程 - qHVer]**
$$ e(g_i, V) = e(C, W_i) \cdot e(g_1, g_q)^{m_i}, \quad C = g^{\theta} $$
> 作用：使用打开信息 $\pi = (\theta, W_i)$ 验证 $(C, V)$ 在位置 $i$ 承诺了消息 $m_i$。

**[软承诺生成 - qSCom]**
$$ C = g_1^{\theta}, \quad V = g_1^{\gamma} $$
> 作用：生成一个软承诺，不与任何消息绑定。

**[软打开（从硬承诺） - qSOpen (flag = H)]**
$$ W_i = \bigg( g_i^\gamma \cdot \prod_{j=1, j \neq i}^{q} g_{q+1-j+i}^{m_j} \bigg)^{1/\theta} $$
> 作用：对于一个硬承诺，生成一个软打开到位置 $i$ 的消息 $m_i$。此处与硬打开算法相同，但输出仅包含 $W_i$（不含 $\theta$）。

**[软打开（从软承诺） - qSOpen (flag = S)]**
$$ W_i = ( g_i^\gamma \cdot g_q^{-m} )^{1/\theta} $$
> 作用：对于一个软承诺，生成一个软打开到任意消息 $m$ 在位置 $i$。

**[伪造承诺 - qFake]**
$$ C = g^{\theta}, \quad V = g^{\gamma} $$
> 作用：使用陷门生成一个外表与硬承诺相同，但内在可被软打开到任意消息的伪造承诺。

**[硬等价打开 - qHEquiv]**
$$ W_i = ( g_i^\gamma \cdot g_{q+1}^{-m_i} )^{1/\theta} $$
> 作用：使用陷门 $tk = g_{q+1}$ 为伪造承诺生成一个硬打开，使其“看起来”承诺了消息 $m_i$。

### 实验结果

论文中的实验分析基于理论推导，而非实际代码实现。实验参数设定为：安全参数 $\lambda$ 使得理论上限 $2^{128}$ 作为数据库大小的边界，树的高度 $h$ 满足 $q^h \approx 2^{128}$。性能评估指标为每个证明所需的群 $\mathbb{G}$ 元素个数，并假定 $\hat{\mathbb{G}}$ 元素的大小相当于 2 个 $\mathbb{G}$ 元素。对比基线包括 MRK [21] 和 CFM [9] 的方案。

对于 q=8，本文方案的成员证明需 220 个 $\mathbb{G}$ 元素，非成员证明需 176 个。相比 CFM 方案（成员 521，非成员 176），成员证明缩短约 57.8%；相比 MRK 方案（成员 773，非成员 644），成员证明缩短约 71.5%。当 q=128，h=19 时，本文成员证明仅需 100 个元素（约 2kB），非成员证明需 80 个元素。而 CFM 方案在 q=128 时成员证明需 2513 个元素，MRK 方案非成员证明需 644 个元素。这表明本方案在高扇出情况下优势尤为明显。

系统的公共参考串（CRS）大小随 q 线性增长（包含 O(q) 个群元素），但证明长度与 q 无关。因此，可以安全地增大 q 来缩短证明，只要 CRS 的大小在可接受范围内。Cheon 攻击 [12] 在此处参数下（如 q=128）不会强制增加安全参数 $\lambda$，因此可以使用 161 比特表示的群元素。

### 局限性与开放问题
论文所提多陷门版本的强独立 ZK-EDB 的安全性仅在非适应性选择标签模型下证明，即攻击者在看到公钥前就选定要查询的标签。适应性的攻击者模型可能更具现实意义，未来工作可探索如何在此情境下保持安全性。此外，系统的公共参考串大小与扇出 q 成线性关系，对于极大的 q 值，CRS 的存储和传输成本是一个实际瓶颈，优化 CRS 大小是一个开放问题。

### 强关联论文

[6] Camenisch, Kohlweiss, Soriente. An Accumulator Based on Bilinear Maps and Efficient Revocation for Anonymous Credentials. **PKC 2009** [Google Scholar](https://scholar.google.com/scholar?q=An+Accumulator+Based+on+Bilinear+Maps+and+Efficient+Revocation+for+Anonymous+Credentials)

[5] Boneh, Gentry, Waters. Collusion Resistant Broadcast Encryption with Short Ciphertexts and Private Keys. **CRYPTO 2005** [Google Scholar](https://scholar.google.com/scholar?q=Collusion+Resistant+Broadcast+Encryption+with+Short+Ciphertexts+and+Private+Keys)

[8] Catalano, Dodis, Visconti. Mercurial Commitments: Minimal Assumptions and Efficient Constructions. **TCC 2006** [Google Scholar](https://scholar.google.com/scholar?q=Mercurial+Commitments+Minimal+Assumptions+and+Efficient+Constructions)

[9] Catalano, Fiore, Messina. Zero-Knowledge Sets with Short Proofs. **EUROCRYPT 2008** [Google Scholar](https://scholar.google.com/scholar?q=Zero-Knowledge+Sets+with+Short+Proofs)

[10] Chase, Healy, Lysyanskaya, Malkin, Reyzin. Mercurial Commitments with Applications to Zero-Knowledge Sets. **EUROCRYPT 2005** [Google Scholar](https://scholar.google.com/scholar?q=Mercurial+Commitments+with+Applications+to+Zero-Knowledge+Sets)

[15] Gennaro, Micali. Independent Zero-Knowledge Sets. **ICALP 2006** [Google Scholar](https://scholar.google.com/scholar?q=Independent+Zero-Knowledge+Sets)

[21] Micali, Rabin, Kilian. Zero-Knowledge Sets. **FOCS 2003** [Google Scholar](https://scholar.google.com/scholar?q=Zero-Knowledge+Sets)


## 关键词

+ 陷门q-水银承诺qTMC
+ 零知识集合ZKS
+ 常数大小打开承诺
+ 独立零知识集合
+ 非成员性证明
+ Merkle树向量承诺