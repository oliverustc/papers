---
title: "Efficient range proofs with transparent setup from bounded integer commitments"
doi: 10.1007/978-3-030-77883-5_9
标题简称:
论文类型: conference
会议简称: EUROCRYPT
发表年份: 2021
modified: 2025-04-16 10:54:35
created: 2025-04-11 11:50:13
---
## Efficient range proofs with transparent setup from bounded integer commitments

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-030-77883-5_9)

## 作者

+ [Geoffroy Couteau](Geoffroy%20Couteau.md)
+ Michael Klooß 
+ Huang Lin 
+ [Michael Reichle](Michael%20Reichle.md)
## 笔记

### 背景与动机
区间证明是现代密码协议的核心构件，广泛用于分布式账本、匿名交易、电子现金和电子投票等场景。在匿名支付方案中，隐藏的交易输入输出值若不加约束会导致溢出攻击，攻击者可凭空造币，因此必须证明承诺值属于合法区间。现有方案主要分为两类：基于n进制分解的方法（如Bulletproof [BBB+18]）和基于平方分解的方法（源自Boudot [Bou00]）。Bulletproof 在离散对数假设下首次实现了通信量 $\mathcal{O}(\lambda \log\beta)$ 且无需可信设置，成为当前最实用的方案。然而平方分解法虽只需常数个承诺，却一直依赖RSA或类群上的整数承诺方案，导致群尺寸极大（通常3072比特）且必须可信设置，这在实际部署中易被攻击者利用后门无限造币。本文试图填补一个空白：能否构造一种同时具备平方分解法紧凑性（常数个群元素）和Bulletproof透明设置优势，且在标准假设下计算效率提高一个数量级的区间证明。

### 相关工作

[BBB+18] Bünz 等. Bulletproofs: Short Proofs for Confidential Transactions and More. **IEEE S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Bulletproofs%3A+Short+Proofs+for+Confidential+Transactions+and+More)
> 核心思路：利用广义Pedersen承诺和递归内积论证，证明二进制分解中各分量均为比特。
> 局限与区别：需对数轮交互（$\mathcal{O}(\log\beta)$），计算开销大，且只达到计算可靠性（computational soundness）。

[Bou00] Boudot. Efficient Proofs that a Committed Number Lies in an Interval. **EUROCRYPT 2000** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+Proofs+that+a+Committed+Number+Lies+in+an+Interval)
> 核心思路：将区间证明转化为证明两个非负整数的平方分解（Lagrange四平方定理）。
> 局限与区别：依赖RSA上的整数承诺，需可信设置，通信开销 $\mathcal{O}(\beta+\lambda)$ 且群尺寸极大。

[Gro05] Groth. Non-interactive Zero-Knowledge Arguments for Voting. **ACNS 2005** [Google Scholar](https://scholar.google.com/scholar?q=Non-interactive+Zero-Knowledge+Arguments+for+Voting)
> 核心思路：利用三平方定理（Legendre定理）将区间证明进一步压缩，只需三个平方数。
> 局限与区别：仍依赖可信设置的整数承诺方案，计算效率低于本文方案。

[CPP17] Couteau 等. Removing the Strong RSA Assumption from Arguments over the Integers. **EUROCRYPT 2017** [Google Scholar](https://scholar.google.com/scholar?q=Removing+the+Strong+RSA+Assumption+from+Arguments+over+the+Integers)
> 核心思路：在无强RSA假设下构造整数上的论证，采用Sigma协议和平方分解。
> 局限与区别：协议描述于RSA子群，本文将其适配到素数阶群并引入新的编码技术。

[YAZ+19] Yang 等. Efficient Lattice-Based Zero-Knowledge Arguments with Standard Soundness. **CRYPTO 2019** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+Lattice-Based+Zero-Knowledge+Arguments+with+Standard+Soundness)
> 核心思路：基于格（LWE）的承诺方案，可对长向量进行承诺和证明。
> 局限与区别：单次区间证明较大，本文利用其向量承诺能力实现了极高效的批处理区间证明。

[KK04] Koshiba, Kurosawa. Short Exponent Diffie-Hellman Problems. **PKC 2004** [Google Scholar](https://scholar.google.com/scholar?q=Short+Exponent+Diffie-Hellman+Problems)
> 核心思路：证明短指数DL假设与SEI假设（短指数不可区分性）等价。
> 局限与区别：本文利用该理论优化承诺的随机性长度，在DLSE假设下提高计算效率。

[Lyu12] Lyubashevsky. Lattice Signatures without Trapdoors. **EUROCRYPT 2012** [Google Scholar](https://scholar.google.com/scholar?q=Lattice+SIGNATURES+without+Trapdoors)
> 核心思路：引入拒绝采样（rejection sampling）技术实现格上签名的零知识。
> 局限与区别：本文将此技术引入Sigma协议，在区间证明中优化掩码大小，降低通信开销。

[CHJ+20] Chung 等. Bulletproofs+: Shorter Proofs for Privacy-Enhanced Distributed Ledger. **ePrint 2020** [Google Scholar](https://scholar.google.com/scholar?q=Bulletproofs%2B%3A+Shorter+Proofs+for+Privacy-Enhanced+Distributed+Ledger)
> 核心思路：对Bulletproof进行微调，进一步减少证明中的群元素个数。
> 局限与区别：计算复杂度未改善，且未经同行评审；本文在通信和计算两方面均更优。

[BLLS20] Bootle 等. Compact Privacy Protocols from Post-Quantum and Timed Classical Assumptions. **PQCrypto 2020** [Google Scholar](https://scholar.google.com/scholar?q=Compact+Privacy+Protocols+from+Post-Quantum+and+Timed+Classical+Assumptions)
> 核心思路：基于Ring-SIS假设构造简洁的单次区间证明。
> 局限与区别：单证明通信极优，但批处理增益有限；本文的批处理方案在约35个证明后即更高效。

### 核心技术与方案

#### 1. 核心思想：有界整数承诺的转换框架

本文的核心技术是将任意有限域 $\mathbb{Z}_q$ 上的承诺方案转换为有界整数承诺方案。给定基础承诺方案 $\mathsf{com}$，新方案 $\overline{\mathsf{com}}$ 的关键在于编码方式的改变：一个整数 $x$ 不是直接被承诺，而是通过一个有理数对 $(y, d)$ 来表示，其中 $x = \lfloor y/d \rceil$（四舍五入取整），$y \in [-R, R]$，$d \in [1, C]$，且 $C = 2^\lambda$ 为挑战空间大小。承诺值计算为 $c = \mathsf{com}(y \cdot d^{-1} \bmod q; \rho)$，而验证时打开信息包含 $(d, y, \rho)$。这种设计的核心优势在于：标准Sigma协议从两个接受转录中提取出的值 $(y - y')/(d - d')$ 天然就是一个形如 $y^*/d^*$ 的有理数，且 $d^* \leq C$，$y^* \leq 2B C L$，从而承诺值被绑定在 $[-2B C L, 2B C L]$ 内，实现了**从$\mathbb{Z}_q$到$\mathbb{Z}$的跨越**。

#### 2. 离散对数实例化

以Pedersen承诺为基础：$\mathsf{com}(m; r) = g^m h^r$，群阶 $q$。首先利用平方分解法将区间 $[0, B]$ 的证明转化为证明三个平方数：$1 + 4x(B-x) = \sum_{i=1}^3 x_i^2$。协议流程如下：

- **初始化**：计算 $x_0 = B - x$，三个平方分量 $x_1,x_2,x_3$，以及它们对应的承诺 $c_i = g^{x_i} h^{r_i}$。然后采样掩码 $m_i$、$s_i$ 以及辅助随机数 $\sigma$，计算初始消息 $\{d_i\}_{i=0..3}$ 和 $d$，以及哈希 $\Delta = H(\{d_i\}, d)$。
- **挑战**：挑战 $\gamma \gets [0, C]$。
- **响应**：计算 $z_i = m_i + \gamma x_i$，$t_i = s_i + \gamma r_i$，以及 $\tau = \sigma + \gamma(\sum x_i r_i + 4x_0 r_0)$。
- **验证**：检查 $z_i \in [0, B C(L+1)]$，并验证两组等式：$g^{z_i} h^{t_i} = c_i^\gamma d_i$ 和 $h^\tau \cdot g^\gamma \cdot c^{4z_0} = \prod c_i^{-z_i}$。

安全性证明的关键在于2-特殊可靠性：给定同一初始消息的两个不同挑战响应，可提取出有效打开和平方分解，或打破DLOG假设。零星知识通过统计遮掩保证。

#### 3. 优化技术

- **短指数DLSE假设**：将承诺的随机性从 $[0, q-1]$ 缩小到 $[0, 2^{2\lambda}]$，在保证安全的同时大幅降低群的大小和计算量。该优化还提供了统计可靠性的另一实例化路径。
- **拒绝采样**：借鉴格密码中Lyubashevsky的技术 [Lyu12]，用离散高斯分布替代均匀分布采样掩码，使掩护范围 $L'$ 可从 $2^\lambda$ 量级降低到约 $256\sqrt{2\lambda}$，显著减小证明尺寸和计算开销。代价是引入约5%的重试概率。

#### 4. 格实例化

基于YAZ+19的承诺方案，本文利用其向量承诺能力实现了极高效的批处理：在模量 $q$ 足够大的前提下，可将最多 $n$（约5000）个区间证明并行压缩为一个证明。当批处理量超过约35个时，通信量即优于现有最优方案 [BLLS20]；批处理量达到5000时，通信量降低约两个数量级。

#### 5. 复杂度总结

在DLP实例化下（$\beta=32,\lambda=128$），证明大小为501字节（Bulletproof为608字节），Prover计算7k次群乘法（Bulletproof为150k），Verifier计算3.7k次群乘法（Bulletproof底限25k）。通信量渐进为 $\mathcal{O}(\lambda+\beta)$，优于Bulletproof的 $\mathcal{O}(\lambda\log\beta)$ 当 $\beta = \mathcal{O}(\lambda)$。

### 核心公式与流程

**[有界整数承诺的编码]**
$$x = \left\lfloor \frac{y}{d} \right\rceil$$
> 将整数 $x$ 编码为有理数对 $(y, d)$，其中 $y \in [-R, R]$，$d \in [1, C]$。承诺值为 $\overline{\mathsf{com}}(x) = \mathsf{com}(y \cdot d^{-1} \bmod q; \rho)$。验证时检查 $x = \lfloor y/d \rceil$ 且 $|y| \leq R/C$。

**[三平方定理（Lagrange-Legendre）]**
$$4x(B-x) + 1 = \sum_{i=1}^{3} x_i^2 \iff x \in [0, B]$$
> 区间证明的核心转化：命题 $x \in [0, B]$ 等价于存在三个整数 $x_1, x_2, x_3$ 满足上述方程。该分解可高效计算 [PS19]。

**[Sigma协议的可提取性]**
$$c = \mathsf{com}\left( \frac{z - z'}{\gamma - \gamma'}; \frac{t - t'}{\gamma - \gamma'} \right)$$
> 若恶意的Prover能对同一初始消息 $d$ 产生两个不同的挑战 $\gamma, \gamma'$ 的接受响应，则提取器可通过上式提取有效打开 $x^* = \lfloor (z-z')/(\gamma-\gamma') \rceil$。由于 $|z-z'| \leq 2BCL$ 且 $|\gamma-\gamma'| \leq C$，$x^*$ 被绑定在有限整数区间内。

**[平方分解的整数等价性]**
$$\overline{\gamma}^2 + 4(B\overline{\gamma} - \overline{z}_0)\overline{z}_0 = \sum_{i=1}^3 \overline{z}_i^2 \mod q \;\Longrightarrow\; \text{等式在Z上成立}$$
> 证明中关键步骤利用尺寸约束 $25K^2 \leq U < (q-1)/2$ 保证模等式成立即整数等式成立。然后除以 $\overline{\gamma}^2$ 得到 $1+4x(B-x)=\sum x_i^2$，最后由三平方定理完成证明。

### 实验结果

实验在标准安全参数下进行，对比基线为Bulletproof [BBB+18]。群尺寸方面，本文利用DLSE假设可将群大小降至32-52字节（$\beta=32-64，\lambda=80-128$），而Bulletproof固定为20-32字节。尽管群稍大，但证明尺寸仍减少12%-20%：例如$(32,128)$参数下本文为501字节 vs Bulletproof的608字节。Prover计算量降低20-40倍（本文4.6k-7.3k群乘法 vs Bulletproof的92k-290k），Verifier计算量降低6-15倍（本文2.4k-3.8k vs Bulletproof的>15k->49k）。计算优势得益于短指数乘法和更小的群尺寸带来的速度提升。在格实例化中，批处理性能尤为突出：当批处理量达5000时，每证明通信仅0.1KB（$\beta=32$），相较于YAZ+19的73KB（单次）降低约两个数量级。方案仅需3轮交互（Fiat-Shamir后非交互化），而Bulletproof需$\mathcal{O}(\log\beta)$轮。拒绝采样引入约5%的重试概率，但不影响最终输出大小。

### 局限性与开放问题

当区间长度$\beta$远大于安全参数$\lambda$（如$\beta \gg 128$）时，Bulletproof的$\mathcal{O}(\lambda \log \beta)$通信量渐近优于本文的$\mathcal{O}(\lambda + \beta)$，因此本文在超大区间场景不具优势。格实例化虽具极佳批处理特性，但单证明尺寸较大，适用于需批量处理的场景而非单次证明。另外，当前方案在DLP实例化下依赖DLSE假设（虽为标准DL的变体），而格实例化依赖LWE假设，均为计算性假设；是否存在基于标准假设的统计可靠高效区间证明仍需探索。最后，方案仅在区间$[0,B]$上直接定义，扩展到任意$[a,b]$需通过同态操作$x-a$和$b-x$，这会引入额外的边界检查开销。

### 强关联论文

[BBB+18] Bünz 等. Bulletproofs: Short Proofs for Confidential Transactions and More. **IEEE S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Bulletproofs%3A+Short+Proofs+for+Confidential+Transactions+and+More)

[Bou00] Boudot. Efficient Proofs that a Committed Number Lies in an Interval. **EUROCRYPT 2000** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+Proofs+that+a+Committed+Number+Lies+in+an+Interval)

[Gro05] Groth. Non-interactive Zero-Knowledge Arguments for Voting. **ACNS 2005** [Google Scholar](https://scholar.google.com/scholar?q=Non-interactive+Zero-Knowledge+Arguments+for+Voting)

[CPP17] Couteau 等. Removing the Strong RSA Assumption from Arguments over the Integers. **EUROCRYPT 2017** [Google Scholar](https://scholar.google.com/scholar?q=Removing+the+Strong+RSA+Assumption+from+Arguments+over+the+Integers)

[YAZ+19] Yang 等. Efficient Lattice-Based Zero-Knowledge Arguments with Standard Soundness. **CRYPTO 2019** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+Lattice-Based+Zero-Knowledge+Arguments+with+Standard+Soundness)

[KK04] Koshiba, Kurosawa. Short Exponent Diffie-Hellman Problems. **PKC 2004** [Google Scholar](https://scholar.google.com/scholar?q=Short+Exponent+Diffie-Hellman+Problems)

[Lyu12] Lyubashevsky. Lattice Signatures without Trapdoors. **EUROCRYPT 2012** [Google Scholar](https://scholar.google.com/scholar?q=Lattice+Signatures+without+Trapdoors)

[CHJ+20] Chung 等. Bulletproofs+: Shorter Proofs for Privacy-Enhanced Distributed Ledger. **ePrint 2020** [Google Scholar](https://scholar.google.com/scholar?q=Bulletproofs%2B%3A+Shorter+Proofs+for+Privacy-Enhanced+Distributed+Ledger)

[BLLS20] Bootle 等. Compact Privacy Protocols from Post-Quantum and Timed Classical Assumptions. **PQCrypto 2020** [Google Scholar](https://scholar.google.com/scholar?q=Compact+Privacy+Protocols+from+Post-Quantum+and+Timed+Classical+Assumptions)

[PS19] Pollack, Schorn. Dirichlet’s Proof of the Three-Square Theorem: An Algorithmic Perspective. **Math. Comput. 2019** [Google Scholar](https://scholar.google.com/scholar?q=Dirichlet%27s+Proof+of+the+Three-Square+Theorem%3A+An+Algorithmic+Perspective)


## 关键词

+ 范围证明
+ 有界整数承诺
+ 透明设置
+ 离散对数
+ LWE假设