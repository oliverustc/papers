---
title: "On the security of ECDSA with additive key derivation and presignatures"
doi: 10.1007/978-3-031-06944-4_13
标题简称:
论文类型: conference
会议简称: EUROCRYPT
发表年份: 2022
created: 2025-05-12 09:11:47
modified: 2025-05-12 09:13:24
---
## On the security of ECDSA with additive key derivation and presignatures

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-06944-4_13)
+ [archive](https://eprint.iacr.org/2021/1330)

## 作者

+ [Jens Groth](Jens%20Groth.md)
+ [Victor Shoup](Victor%20Shoup.md)
## 笔记

### 背景与动机
椭圆曲线数字签名算法（ECDSA）是密码学中广泛应用的标准，其签名过程包含一个随机 nonce $r$ 和对应的群元素 $\mathcal{R}=r\mathcal{G}$，该 nonce 与待签消息无关。这一特性催生了两种重要的变体：加法密钥派生和预签名。加法密钥派生通过在主密钥 $d$ 上添加一个公开的“扰动”值 $e$ 来派生子密钥 $d+e$，这允许使用单一主密钥管理多个公钥，在加密货币的分层确定性钱包（如 BIP32 标准 [20]）中已广泛使用。预签名则允许预先计算并公开 $\mathcal{R}$ 值，在门限签名场景中能极大简化在线阶段的协议，已有方案如 [7] 和 [11] 采用了此方法。然而，现有研究存在显著空白：虽然 [21] 声称对加法密钥派生有安全证明，但其安全归约被指出存在根本性缺陷，即模拟器需要“重编程”一个已被“编程”的随机预言机 [8]。更关键的是，尚无任何工作分析过这两种变体组合时的安全性，尽管 [7] 已积极推荐这种组合。本文填补了这个空白，在更精确的椭圆曲线通用群模型（EC-GGM）下对这些变体的安全性进行彻底分析。

### 相关工作

[4] Brown. Generic groups, collision resistance, and ECDSA. **Designs, Codes and Cryptography 2002** [Google Scholar](https://scholar.google.com/scholar?q=Generic+groups%2C+collision+resistance%2C+and+ECDSA)
> 核心思路：在通用群模型（GGM）下基于哈希函数的抗碰撞性和随机前像抗性证明标准ECDSA的安全性。
> 局限与区别：分析被后续工作 [10, 18] 指出存在漏洞，例如未能处理 ECDSA 签名本身的可延展性。本文提出的 EC-GGM 模型更精确地刻画了椭圆曲线和转换函数的特性，从而弥补了这一缺陷。

[10] Fersch et al. On the provable security of (EC)DSA signatures. **ACM CCS 2016** [Google Scholar](https://scholar.google.com/scholar?q=On+the+provable+security+of+(EC)DSA+signatures)
> 核心思路：通过将转换函数建模为理想函数来证明 ECDSA 的安全性。
> 局限与区别：本文指出其批评针对的是 Brown 模型的不足，并采用更符合实际椭圆曲线结构的 EC-GGM 来规避这些异议。

[5] Canetti et al. UC non-interactive, proactive, threshold ECDSA. **ePrint 2020** [Google Scholar](https://scholar.google.com/scholar?q=UC+non-interactive%2C+proactive%2C+threshold+ECDSA)
> 核心思路：首次对预签名提出显式安全定义，并在 GGM 中将哈希函数建模为随机预言机给出证明（早期版本的安全界有误）。
> 局限与区别：本文不将哈希函数建模为随机预言机，给出了更紧的安全界，并且是对预签名的独立分析（不带密钥派生）。

[19] Wagner. A generalized birthday problem. **CRYPTO 2002** [Google Scholar](https://scholar.google.com/scholar?q=A+generalized+birthday+problem)
> 核心思路：提出解决k-sum问题的算法，该算法在特定条件下能显著快于生日攻击（平方根时间）。
> 局限与区别：本文利用该算法构造了对“预签名+加法密钥派生”组合变体的具体攻击，证明了其安全阈值的下降非理论问题，而是实际存在的攻击。

[20] Wuille. Hierarchical deterministic wallets (BIP32). **Bitcoin Improvement Proposal 2020** [Google Scholar](https://scholar.google.com/scholar?q=Hierarchical+deterministic+wallets)
> 核心思路：标准化了比特币中的分层确定性钱包，使用了加法密钥派生。
> 局限与区别：本工作首次从理论角度对其进行安全性分析，并指出了在特定条件下（尤其与预签名组合时）的安全风险。

[8] Das et al. The exact security of BIP32 wallets. **ePrint 2021** [Google Scholar](https://scholar.google.com/scholar?q=The+exact+security+of+BIP32+wallets)
> 核心思路：在限制攻击模型下（每条消息每个派生公钥只允许一次签名）分析另一种派生的 ECDSA 变体。
> 局限与区别：其模型和分析场景与本文不同，且主要关注非受限模型下的标准安全性。

### 核心技术与方案

**1. EC-GGM模型**。本文提出了一个针对椭圆曲线idiosyncrasies改进的通用群模型（EC-GGM）。标准GGM将群元素编码为字符串，但EC-GGM要求编码函数 $\pi: \mathbb{Z}_q \mapsto E$ 是单射、身份保持且逆保持的，即 $\pi(0) = \mathcal{O}$ 且 $\pi(-i) = -\pi(i)$。这使得编码结果看起来像真实椭圆曲线上的点（包含x,y坐标），并且保留了点与其逆元共享相同x坐标的特性。群运算通过预言机 $\mathcal{O}_{\text{grp}}$ 进行，该预言机使用随机选择的编码函数 $\pi$。这个模型更准确地模拟了ECDSA的转换函数 $C$ 和签名可延展性。

**2. 符号模拟器（Symbolic Simulator）**。为了进行安全性证明，本文设计了符号模拟器（如图3、5、7所示）。它的核心思想是把群元素背后对应的离散对数用一个**多项式**来代替，其中主密钥 $d$ 被表示为一个符号变量 $\mathbb{D}$（或其他独立的符号变量）。例如，在标准ECDSA符号模拟中，$\pi$ 的域由形如 $a + b \mathbb{D}$ 的多项式构成。这使得模拟器可以统计并控制“意外”的多项式碰撞（即两个不同的符号表达式被随机编码成了相同的群元素）。通过引理（如Lemma 1），符号模拟器和真实的惰性模拟器（Lazy Simulator）之间的差异被控制在 $O(N^2/q)$ 内，从而可以基于符号模拟进行安全归约。

**3. 安全性证明策略**。证明采用分类型（Type I, II, III）伪造者分析。在符号模拟环境中，分类依据是伪造签名中恢复出的 $\mathcal{R}^*$ 的符号表达式与之前数字签名查询中产生的 $\mathcal{R}$ 的关系。例如：
*   **Type I**：$\mathcal{R}^* = \pm \mathcal{R}$，这直接等价于找到哈希碰撞。
*   **Type II**：$\mathcal{R}^* \neq \pm \mathcal{R}$，且 $h^* \neq 0$。此时 $\mathcal{R}^*$ 对应的符号表达式 $a + b \mathbb{D}$ 由群预言机查询时随机生成，而验证方程给出 $a = (s^*)^{-1} h^*$ 和 $b = (s^*)^{-1} t^*$。由于 $a, b$ 在 $\mathcal{R}^*$ 生成时已确定，而 $\mathcal{R}^*$ 的生成独立于这些系数，我们可以利用此来归约到对哈希函数随机前像的攻击。
*   **Type III**：$h^* = 0$，直接归约到哈希函数的零前像抗性。

**4. 变体的分析与攻击**。本文分析发现，当结合使用加法密钥派生和预签名时，存在显著的4-sum问题。攻击者可以：
    1. 请求一个预签名，得到 $\mathcal{R}$ 和 $t = \bar{C}(\mathcal{R})$。
    2. 利用Wagner的广义生日攻击算法 [19] ，在时间 $\dot{O}(q^{1/3})$（当有效扰动集合 $\mathfrak{E}$ 大小为 $\Theta(q^{1/3})$ 时）找到四个元素 $(m, e, m^*, e^*)$ 满足 $h + t e = h^* + t e^*$。
    3. 请求对消息 $m$ 和扰动 $e$ 的签名，然后该签名也自动是 $m^*$ 和 $e^*$ 的有效签名，因为从验证方程角度看，$\mathcal{R} = s^{-1}(h + td + t e) \mathcal{G} = s^{-1}(h^* + td + t e^*) \mathcal{G}$。这构成了一个比平方根攻击更高效的立方根攻击。

**5. 缓解措施**：**重新随机化预签名**是一种有效缓解方法。在签名请求时，不是直接使用存储的预签名 $(r', \mathcal{R}')$，而是生成一个公开的随机数 $\delta$，然后使用 $(r = r' + \delta, \mathcal{R} = \mathcal{R}' + \delta \mathcal{G})$ 作为实际nonce。$\delta$ 的不可预测性切断了攻击者对 $t$ 值的自由利用，从而消除了4-sum攻击的可行性。**同质密钥派生**是另一种更优的方案。主密钥变为 $(d, d')$，派生密钥为 $d + e d'$。这使得在证明中，任何伪造者都必须同时猜测 $h$ 和 $e$ 的值，而不能像加法派生那样通过控制 $e$ 来降低攻击难度。其安全界因此不再依赖于集合 $\mathfrak{E}$ 的大小。

### 核心公式与流程

**ECDSA签名与验证算法**
$$ \text{Sign}(m):\ r \leftarrow \mathbb{Z}_q^*,\ \mathcal{R} = r \mathcal{G},\ t = \bar{C}(\mathcal{R}),\ s = r^{-1}(h + td)，\text{其中 } h = Hash(m) $$
$$ \text{Verify}(m, (s,t)):\ \mathcal{R}' = s^{-1} h \mathcal{G} + s^{-1} t \mathcal{D},\ \text{检查 } \mathcal{R}' \neq \mathcal{O} \text{ 且 } \bar{C}(\mathcal{R}') = t $$
> 作用：标准ECDSA的定义。

**4-sum伪造攻击的核心等式**
$$ h + t e = h^* + t e^* $$
> 作用：在存在预签名（$t$ 已知）和加法密钥派生（$e$ 和 $e^*$ 可自由选择）的情况下，寻找两对 $(h, e)$ 和 $(h^*, e^*)$ 使得上式成立。$h, h^*$ 是消息的哈希值。若找到，利用一个签名即可伪造另一个。

**同质密钥派生验证方程**
$$ \mathcal{R} = s^{-1} h \mathcal{G} + s^{-1} t (\mathcal{D} + e \mathcal{D}') = s^{-1} (h + t d + t e d') \mathcal{G} $$
> 作用：同质密钥派生将扰动 $e$ “绑定”到了第二个秘密 $d'$ 上，使得攻击者无法仅通过一个标量等式分离出 $t e$ 项，从而在证明中消除了依赖集合 $\mathfrak{E}$ 大小的安全界退化。

### 实验结果
本文通过具体的分析模型（EC-GGM）和符号模拟器给出了严格的安全性上界（总结在Table 1 [PDF p. 10] 中）。主要“实验”结果是理论上的安全界比较和攻击复杂度分析。
*   **攻击复杂度**：对“加法密钥派生+预签名”组合的4-sum攻击复杂度为 $\dot{O}(q^{1/3})$（当 $|\mathfrak{E}| = \Theta(q^{1/3})$ 时），远优于标准ECDSA及单独使用任一变体的 $\Theta(q^{1/2})$ 生日攻击。例如，在256位椭圆曲线（$q \approx 2^{256})$ 上，这相当于将安全强度从128比特降至约85比特。
*   **安全界对比**：表格清晰地展示了各种变体组合的安全界。例如：
    *   标准ECDSA界：$\mathcal{E}_{\text{cr}} + N\mathcal{E}_{\text{rpr}} + \mathcal{E}_{\text{zpr}} + N^2/q$
    *   加法派生界：$\mathcal{E}_{\text{cr}} + N|\mathfrak{E}|\mathcal{E}_{\text{rpr}} + \mathcal{E}_{\text{zpr}} + N^2/q$
    *   “加法派生+预签名”界：$\mathcal{E}_{\text{cr}} + UN|\mathfrak{E}|\mathcal{E}_{\text{rpr}} + N_{\text{psig}}\mathcal{E}_{\text{4sum1}} + N\mathcal{E}_{\text{4sum2}} + \mathcal{E}_{\text{zpr}} + N^2/q$
    *   “同质派生+重新随机化预签名”界：$\mathcal{E}_{\text{cr}} + N\mathcal{E}_{\text{rpr}} + \mathcal{E}_{\text{zpr}} + N^2/q$ （与标准ECDSA相同）。
*   **对比基线**：所有安全界都是与标准ECDSA或单独使用预签名 [5] 的方案相比较。例如，在无派生时，重新随机化预签名获得与原始ECDMA相同的安全界。在同质派生下，三种模式（无预签名、带预签名、带重新随机化预签名）均达到与对应的无派生模式相同的安全界。
*   **适用参数**：模型假设椭圆曲线为素数阶且cofactor为1（覆盖secp曲线）。

### 局限性与开放问题
本文的安全证明依赖于**通用群模型（EC-GGM）**，虽然该模型相比标准GGM更精确，但它仍然是一种理想化模型，与真实世界的群运算存在差距【4】。对于加法密钥派生，安全界线性依赖于有效扰动集合 $\mathfrak{E}$ 的大小，这意味着大规模使用派生密钥会显著降低安全性。虽然提出了同质密钥派生作为缓解，但它不与现有BIP20标准兼容。此外，重新随机化预签名依赖于一个公开的、不可预测的随机源 $\delta$，这在某些系统中可能引入额外延迟。如何在没有额外计算开销的前提下，通过基于哈希的方法安全地派生 $\delta$ 是一个值得探索的方向。

### 强关联论文

[4] Brown. Generic groups, collision resistance, and ECDSA. **Designs, Codes and Cryptography 2002** [Google Scholar](https://scholar.google.com/scholar?q=Generic+groups%2C+collision+resistance%2C+and+ECDSA)

[5] Canetti et al. UC non-interactive, proactive, threshold ECDSA. **ePrint 2020** [Google Scholar](https://scholar.google.com/scholar?q=UC+non-interactive%2C+proactive%2C+threshold+ECDSA)

[19] Wagner. A generalized birthday problem. **CRYPTO 2002** [Google Scholar](https://scholar.google.com/scholar?q=A+generalized+birthday+problem)

[20] Wuille. Hierarchical deterministic wallets (BIP32). **Bitcoin Improvement Proposal 2020** [Google Scholar](https://scholar.google.com/scholar?q=Hierarchical+deterministic+wallets)

[8] Das et al. The exact security of BIP32 wallets. **ePrint 2021** [Google Scholar](https://scholar.google.com/scholar?q=The+exact+security+of+BIP32+wallets)


## 关键词

+ ECDSA安全性分析
+ 加法密钥派生
+ 预签名
+ 通用群模型
+ 门限签名
