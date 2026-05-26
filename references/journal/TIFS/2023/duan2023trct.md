---
title: "TRCT: A traceable anonymous transaction protocol for blockchain"
标题简称:
论文类型: journal
期刊简称: TIFS
发表年份: 2023
created: 2025-05-13 05:35:20
modified: 2025-05-13 05:35:35
---

## TRCT: A traceable anonymous transaction protocol for blockchain

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/10185067)

## 作者

+ Junke Duan
+ Licheng Wang
+ Wei Wang
+ Lize Gu

## 笔记

### 背景与动机
匿名加密货币（如 Monero、Zerocash）通过隐藏交易金额和参与者地址来保护用户隐私，但这一特性也为洗钱、勒索等犯罪活动提供了掩护。现有基于统计分析的追踪方法在面对采用环形签名、零知识证明等技术的匿名协议时效果不佳。此前针对性的追踪方案主要面向许可链，需要用户与可信机构交互注册身份，不适用于无许可链环境。在无许可链领域，Li 等人在 2021 年提出了可追踪 Monero 协议 [20]，但其追踪标签在交易上链后才被验证，且仅能追踪地址而无法追踪金额。Garman 等人对 Zerocash 的修改 [19] 则依赖矿工诚实标记代币，恶意用户仍可通过挖掘不可追踪的代币逃避追踪。现有工作的核心瓶颈在于：无法让仅持有公开信息的矿工在交易上链前就完成对追踪有效性的公共验证，导致不诚实的用户仍能通过伪造部分证明来逃避监管。本文旨在填补这一空白，设计首个允许通过公共信息验证交易可追溯性，同时保持匿名性的协议。

### 相关工作

[15] Shao 等. AttriChain: Decentralized traceable anonymous identities in privacy-preserving permissioned blockchain. **Computers & Security 2020** [Google Scholar](https://scholar.google.com/scholar?q=AttriChain+Decentralized+traceable+anonymous+identities+in+privacy-preserving+permissioned+blockchain)
> 核心思路：利用属性加密（ABE）让经过授权的用户在许可链上以匿名且可追溯的身份进行交互。
> 局限与区别：基于许可链，需要集中式机构管理身份，不适用于无许可链的匿名加密货币场景。

[16] Li 等. Permissioned blockchain-based anonymous and traceable aggregate signature scheme for industrial Internet of Things. **IEEE Internet of Things Journal 2021** [Google Scholar](https://scholar.google.com/scholar?q=Permissioned+blockchain-based+anonymous+and+traceable+aggregate+signature+scheme+for+industrial+Internet+of+Things)
> 核心思路：为物联网场景设计基于聚合签名的匿名可追溯数据共享协议。
> 局限与区别：方案针对许可链设计，且交易内容以明文形式被矿工查看，不提供金额或地址的隐私保护。

[17] Panwar 等. ReTRACe: Revocable and traceable blockchain rewrites using attribute-based cryptosystems. **ACM SACMAT 2021** [Google Scholar](https://scholar.google.com/scholar?q=ReTRACe+Revocable+and+traceable+blockchain+rewrites+using+attribute-based+cryptosystems)
> 核心思路：结合群签名和属性加密，设计可撤销身份的许可链匿名交易系统。
> 局限与区别：基于许可链，授权的监管机构才能验证可追溯性，不支持公共验证。

[18] Gong 等. Anonymous traceability protocol based on group signature for blockchain. **Future Generation Computer Systems 2022** [Google Scholar](https://scholar.google.com/scholar?q=Anonymous+traceability+protocol+based+on+group+signature+for+blockchain)
> 核心思路：基于门限群签名，在许可链上实现匿名交易，监管机构可通过合作披露用户身份。
> 局限与区别：许可链架构，追踪信息的验证需要授权，交易内容以明文形式存在。

[19] Garman 等. Accountable privacy for decentralized anonymous payments. **Financial Cryptography 2016** [Google Scholar](https://scholar.google.com/scholar?q=Accountable+privacy+for+decentralized+anonymous+payments)
> 核心思路：修改 Zerocash 协议，让矿工与权威机构合作，对挖矿交易进行标记以追踪资金流向。
> 局限与区别：依赖矿工诚实地标记其挖出的代币，恶意用户仍可选择挖出不可追踪的代币。

[20] Li 等. Traceable Monero: Anonymous cryptocurrency with enhanced accountability. **IEEE TDSC 2021** [Google Scholar](https://scholar.google.com/scholar?q=Traceable+Monero+Anonymous+cryptocurrency+with+enhanced+accountability)
> 核心思路：基于密码累加器和知识签名，在 Monero 中通过追踪标签实现付款方和收款方地址的追踪。
> 局限与区别：追踪标签在交易上链后才被验证，无法撤回不合规交易；仅追踪地址，不追踪金额。

### 核心技术与方案
本文的核心贡献是提出并实例化了一个称为可提取知识证明（EPoK）的改进型非交互零知识证明（NIZK）方案，并基于此设计了可追踪环形机密交易（TRCT）协议。

**EPoK 方案。** 标准 NIZK 允许证明者在不泄露秘密信息的情况下向验证者证明自己拥有某个满足 NP 关系 $\mathcal{R}$ 的见证 $w$。EPoK 将见证分为不可提取部分 $w_u$ 和可提取部分 $w_e$，并确保构造的证明对验证者保持零知识性，同时允许一个持有提取密钥 $sk_e$ 的权威机构提取出 $w_e$。具体实例化基于一个简单的 NP 关系 $\mathcal{R} = \{y=(P,T) | \exists w=(w_e,w_u): P = w_e g^{w_u}, T = w_e K^{w_u}\}$，其中 $K = g^k$ 是提取公钥。证明者计算 $P$ 和 $T$ 后，通过 Schnorr-like 协议生成证明 $\pi=(c,s)$。验证者检查等式 $hash(c) = hash((P/T)^{hash(c)} \cdot (g/K)^s)$。权威机构通过 $w_e \leftarrow (P / T^{1/k})^{k/(k-1)}$ 提取 $w_e$。该方案的安全性依赖于离散对数（DL）和判定性 Diffie-Hellman（DDH）假设，通过游戏序列严格证明了其 UW-零知识（不可提取部分满足零知识）、EW-匿名性（可提取部分满足匿名性）和可靠性（Soundness）。

**TRCT 协议。** TRCT 将 EPoK 与经典匿名交易协议 RingCT 结合。协议包含六个算法：Setup, TKGen, LKGen, OpkGen, OskExt, Mint, Spend, Verify, Trace。具体工作流程如下：
1.  **系统初始化**：权威机构运行 TKGen 生成追踪密钥对 $(K,k)$，将 $K$ 作为公共参数。收款方执行 LKGen 生成长期密钥对，并将长期公钥发送给付款方。
2.  **交易构造**：付款方使用 RingCT.Sign 生成环形签名 $\pi_{ring}$，用于隐藏付款方地址并证明输入金额等于输出金额。为了实现可追踪性，付款方利用 EPoK 分别为交易金额和接收方地址构建跟踪标签。具体来说，设 $act_{\mathcal{R}} = (opk_{\mathcal{R}}, C_{\mathcal{R}})$ 是收款方账户，其中 $C_{\mathcal{R}} = g^{a_{\mathcal{R}}} h^v$ 是金额承诺，$opk_{\mathcal{R}} = g^{hash(A^r)} \cdot B$ 是一次性公钥。付款方计算：
    - 对金额 $v$ 的跟踪标签：调用 EPoK.Prove，见证为 $w_{value}=(h^v, a_{\mathcal{R}})$，语句为 $y_{value}=(C_{\mathcal{R}}, T_{value})$。
    - 对收款方地址固定部分 $B$ 的跟踪标签：调用 EPoK.Prove，见证为 $w_{addr} = (B, hash(A^r))$，语句为 $y_{addr}=(opk_{\mathcal{R}}, T_{addr})$。
    最终交易 $\pi$ 包含 $\pi_{ring}$、$\pi_{value}$、$\pi_{addr}$ 以及 $T_{value}$、$T_{addr}$。
3.  **公共验证**：矿工在将交易上链前，执行 Verify 算法。该算法不仅验证 RingCT.Verify，还验证两个 EPoK.Verify 过程，即检查交易的有效性以及追踪标签的正确性。由于 EPoK 的可靠性，恶意用户无法在不知晓真实见证的情况下伪造有效的追踪标签。
4.  **追踪**：权威机构从链上获取交易后，运行 Trace 算法。使用提取私钥 $k$，通过 EPoK.Extract 从 $T_{value}$ 恢复金额承诺的盲因子 $h^v$，并在预计算好的映射表 $V$ 中查找具体金额 $v$。同时，从 $T_{addr}$ 提取收款方的固定公钥部分 $B_{out}$。通过维护一个映射表 $\mathcal{B}$，连接 $e(s,g)$（关联付款方序列号 $s$）与提取出的 $B_{in}$，从而关联输入输出账户，实现交易的链接与追踪。

**安全性与复杂度。** TRCT 满足不可伪造性、余额平衡性、匿名性、可链接性和可追踪性，其安全性分别规约到 RingCT 的安全性、DL 假设、DDH 假设以及 EPoK 的安全性。在通信和计算开销方面，与原始 RingCT [7] 相比，TRCT 的额外开销与账户组数量 $n$ 线性相关，而与每个账户组的大小 $l$ 无关，具体表现为额外进行 $n$ 次 EPoK 证明/验证操作。

### 核心公式与流程

**[EPoK 实例化关系]**
$$ \mathcal{R} = \left\{ \begin{array}{c} y = (P, T) | \quad : P = w_e g^{w_u}, \\ \exists w = (w_e, w_u) \quad : T = w_e K^{w_u} \end{array} \right\} $$
> 定义可提取证明确切需要证明的 NP 关系，其中 $w_e$ 是权威机构可提取的知识。

**[EPoK 证明生成与验证]**
$$ \text{Prove: } c \leftarrow hash((g/K)^{s_0}), s \leftarrow s_0 - hash(c) \cdot w_u, \pi = (c,s) $$
$$ \text{Verify: } hash(c) \stackrel{?}{=} hash((P/T)^{hash(c)} \cdot (g/K)^s) $$
> EPoK 的证明协议，基于 Schnorr 协议变体，验证者无需知道 $w_e$ 和 $w_u$ 即可验证证明的有效性。

**[EPoK 提取算法]**
$$ w_e \leftarrow (P / T^{1/k})^{k/(k-1)} $$
> 权威机构使用提取私钥 $k$ 从证明的语句 $y=(P,T)$ 中恢复出可提取部分 $w_e$。

**[TRCT 交易追踪输出]**
$$ tx^* = (v, B_{in}, B_{out}) $$
> 追踪算法 Trace 的输出 $tx^*$ 包含交易金额 $v$，输入账户的固定公钥部分 $B_{in}$ 以及输出账户的固定公钥部分 $B_{out}$，以此恢复交易的可追踪性。

### 实验结果
论文通过 Golang 语言（版本 1.12）在配备 1.80GHz Intel Core i5-8265U CPU 和 8GB 内存的笔记本电脑上进行模拟实验，使用 256 位椭圆曲线和 SHA-256 哈希函数。实验比较了 TRCT 与原始 RingCT [7] 在开销上的差异。实验结果表明，当账户组大小为 11（与 Monero 同期配置一致）且账户组数量从 1 增加到 10 时，TRCT 的 Spend 算法平均额外开销约为 8.3%，Verify 算法平均额外开销约为 6.8%。当账户组数量固定为 5，账户组大小从 10 增加到 100 时，Spend 算法额外开销约为 18.4%，Verify 算法额外开销约为 4.2%。额外开销主要来自 EPoK 的证明生成与验证，其与账户组数量呈线性关系，与账户组大小无关。根据 Monero 交易数据，大多数交易仅包含 1 到 2 个账户组，此时 Spend 和 Verify 的额外开销分别约为 7.8% 和 4.4%，仅增加几毫秒，对基于工作量证明的区块链性能影响微乎其微。

### 局限性与开放问题
本文提出的 EPoK 方案实例化基于一个特定的、相对简单的 NP 关系，其普适性和在其他更复杂密码协议（如通用电路可满足性）中的应用潜力有待探索。协议在交易构造环节引入了额外的跟踪标签，这造成了计算和通信上的额外开销，尤其是在账户组数量较多时。此外，虽然协议支持对交易金额和地址的追踪，但如何将追踪结果与链下真实世界的身份进行安全、私密地关联，特别是结合事后司法调查流程，文中并未深入探讨。未来的工作方向包括研究 EPoK 方案在其他匿名交易协议（如 Zerocash）上的应用，以及探索更高效的范围证明实现方式以优化对大额追踪的性能。

### 强关联论文

[1] Nakamoto. Bitcoin: A peer-to-peer electronic cash system. **Decentralized Business Review 2008** [Google Scholar](https://scholar.google.com/scholar?q=Bitcoin+A+peer-to-peer+electronic+cash+system)

[7] Noether and Mackenzie. Ring confidential transactions. **Ledger 2016** [Google Scholar](https://scholar.google.com/scholar?q=Ring+confidential+transactions)

[19] Garman et al. Accountable privacy for decentralized anonymous payments. **Financial Cryptography 2016** [Google Scholar](https://scholar.google.com/scholar?q=Accountable+privacy+for+decentralized+anonymous+payments)

[20] Li et al. Traceable Monero: Anonymous cryptocurrency with enhanced accountability. **IEEE TDSC 2021** [Google Scholar](https://scholar.google.com/scholar?q=Traceable+Monero+Anonymous+cryptocurrency+with+enhanced+accountability)

[25] Boneh. Pairing-based cryptography: Past, present, and future. **ASIACRYPT 2012** [Google Scholar](https://scholar.google.com/scholar?q=Pairing-based+cryptography+Past+present+and+future)

[26] Pedersen. Non-interactive and information-theoretic secure verifiable secret sharing. **CRYPTO 1991** [Google Scholar](https://scholar.google.com/scholar?q=Non-interactive+and+information-theoretic+secure+verifiable+secret+sharing)

[27] Liu and Wong. Linkable ring signatures: Security models and new schemes. **ICCSA 2005** [Google Scholar](https://scholar.google.com/scholar?q=Linkable+ring+signatures+Security+models+and+new+schemes)

[30] Rackoff and Simon. Non-interactive zero-knowledge proof of knowledge and chosen ciphertext attack. **CRYPTO 1991** [Google Scholar](https://scholar.google.com/scholar?q=Non-interactive+zero-knowledge+proof+of+knowledge+and+chosen+ciphertext+attack)

[31] Chase and Lysyanskaya. On signatures of knowledge. **CRYPTO 2006** [Google Scholar](https://scholar.google.com/scholar?q=On+signatures+of+knowledge)


## 关键词

+ TRCT可追踪匿名区块链交易
+ 部分可提取零知识证明EPoK
+ RingCT环形加密交易扩展
+ 匿名交易公开可追踪验证
+ 抗伪证逃避追踪
+ 区块链隐私与问责平衡