---
title: "SLVC-DIDA: Signature-less Verifiable Credential-based Issuer-hiding and Multi-party Authentication for Decentralized Identity"
标题简称:
论文类型: preprint
预印本简称: arxiv
发表年份: 2025
created: 2025-04-16 10:42:06
modified: 2025-05-13 11:21:45
---

## SLVC-DIDA: Signature-less Verifiable Credential-based Issuer-hiding and Multi-party Authentication for Decentralized Identity

## 发表信息

+ [原文链接](https://arxiv.org/abs/2501.11052)

## 作者

+ Tianxiu Xie
+ Keke Gai
+ Jing Yu
+ [Liehuang Zhu](Liehuang%20Zhu.md)
+ [Bin Xiao](Bin%20Xiao.md)
## 笔记

### 背景与动机

数字身份是用户中心在线服务的基础概念，用于唯一标识实体的属性子集。传统集中式身份框架因用户缺乏对个人数据的控制权而引发安全和隐私问题，在复杂网络应用中也面临可扩展性、单点故障和互操作性障碍。去中心化身份被视为一种新范式，W3C 已标准化了去中心化标识符和可验证凭证。然而，现有大多数 DID 和 VC 认证方案广泛采用数字签名，这暴露了发行者签名密钥泄露的安全漏洞 [2], [4]–[9]。签名机制仍依赖公钥基础设施，身份提供商和证书机构控制签名密钥管理，但发行者可能因缺乏合格的安全基础设施而无法妥善保管密钥。一旦密钥泄露，攻击者可以伪造带有特定身份属性的合法 VC 并隐藏恶意行为。此外，即使用区块链分散签名权，VC 发行过程仍需要用户向发行者披露明文身份属性，这从根本上损害了用户对个人数据的主权。同时，凭证包含的发行者签名可由验证者通过公钥验证，验证者可能根据特定场景下的发行者信息推断用户的身份属性 [11], [12]。为应对这些挑战，本文提出了第一个实现了发行者隐藏和隐私保护的去中心化身份认证的 SLVC-DIDA 模型。

### 相关工作

[2] Deepak 等. CanDID: Can-Do Decentralized Identity with Legacy Compatibility, Sybil-Resistance, and Accountability. **IEEE S&P 2021**
> 核心思路：通过去中心化节点委员会和 web 认证服务解决 DID 引导问题，增强用户对身份数据的控制能力。
> 局限与区别：该框架未能解决用户和发行者双方的隐私保护问题，而 SLVC-DIDA 通过零知识证明和 Merkle 树实现了隐私和发行者隐藏。

[4] Mazzocca 等. EVOKE: Efficient Revocation of Verifiable Credentials in IoT Networks. **USENIX Security 2024**
> 核心思路：使用密码学累加器为物联网网络中的 VC 构建撤销机制，以降低计算和存储成本。
> 局限与区别：该方法关注撤销效率，但未涉及发行者隐藏和针对发行者的隐私保护，SLVC-DIDA 则同时处理了这些维度。

[10] Alangot 等. Decentralized Identity Authentication with Auditability and Privacy. **Algorithms 2022**
> 核心思路：将可验证随机函数与区块链技术集成，以平衡审计和隐私保护。
> 局限与区别：该方法未解决分布式发行和分布式管理的固有挑战，SLVC-DIDA 则通过无签名凭证和链上 Merkle 树实现了完全去中心化。

[12] Mir 等. Aggregate Signatures with Versatile Randomization and Issuer-Hiding Multi-Authority Anonymous Credentials. **ACM CCS 2023**
> 核心思路：采用具有随机化标签的聚合签名和聚合墨丘利签名，提出一个隐藏发行者的多授权匿名凭证方案。
> 局限与区别：该方法仍依赖 PKI，一个无能的发行者即可引入签名密钥泄露风险，SLVC-DIDA 通过无签名设计彻底消除了这种依赖。

[14] Rosenberg 等. zk-creds: Flexible Anonymous Credentials from zkSNARKs and Existing Identity Infrastructure. **IEEE S&P 2023**
> 核心思路：引入零知识支持文档概念，从权威身份文档（如电子护照）派生出凭据，无需泄露敏感信息。
> 局限与区别：该工作提供了重要的技术基础（ZKSD），但未将其应用于 DID 框架中的发行者隐藏和完全去中心化，SLVC-DIDA 在此基础上实现了完整的认证模型。

[31] Sonnino 等. Coconut: Threshold Issuance Selective Disclosure Credentials with Applications to Distributed Ledgers. **ePrint 2018**
> 核心思路：提出一个支持分布式门限发行、选择性披露和再随机化的凭证方案。
> 局限与区别：用户真实属性在发行时仍对发行者公开，且发行者隐藏问题未被处理，SLVC-DIDA 避免了明文属性泄露。

[38] Ta 等. Ring Referral: Efficient Publicly Verifiable Ad Hoc Credential Scheme with Issuer and Strong User Anonymity for Decentralized Identity and More. **IEEE S&P 2025**
> 核心思路：基于环签名和 zk-SNARK 提出凭证认证模型，实现去中心化身份中的匿名性。
> 局限与区别：该方案证明时间与环大小呈线性增长 O(n)，而 SLVC-DIDA 使用 Merkle 树累加器结合 Groth16，证明时间仅随对数增长 O(log n)，在大规模场景下性能显著更优。

### 核心技术与方案

SLVC-DIDA 模型包含四个核心实体：持有者、发行者、验证者和区块链。每个实体由去中心化标识符唯一标识。所有 VC 作为承诺由持有者生成并存储于链上 Merkle 树 TRVC，合法发行者集 IS 存储于另一独立的链上 Merkle 树 TRIS。模型的核心创新在于使用无签名 VC，通过哈希函数和发行者成员证明替代传统数字签名，消除对 PKI 签名密钥的依赖。

完整的 DID 认证流程包括五个阶段。阶段 1 初始化：区块链基于安全参数 λ 生成零知识证明公共参数 pp，包括用于检查 VC 发行谓词的 ppΦ、用于检查发行者资格的 ppS 和用于碰撞抵抗哈希函数的 pph。阶段 2 认证请求与随机性采样：为防止重放攻击，发行者在收到持有者认证请求后采样新鲜随机数 rᵢ⁰，计算 rᵢ = h(DIDᴴ, rᵢ⁰) 并发送给持有者。持有者采样自身随机数 rᴴ，计算 R = h(rᴴ ∥ rᵢ)，用于绑定整个会话。每个 VC 发行都通过随机数 (rᴴ, rᵢ⁰) 绑定到特定的 DID 认证会话。

阶段 3 无签名 VC 生成：持有者对其属性 attr 和标识符 DIDᴴ 生成承诺 VC = Commit(attr, DIDᴴ)。为防止伪造 VC，持有者还需基于零知识支持文档 ZKSD 生成发行证明 πΦ，声明 (i) VC 源自权威身份文档，(ii) 承诺属性满足发行谓词 Φ_iss。生成的 VC 被添加到链上 Merkle 树 TRVC 中，区块链更新树为 TRVC' 并计算新根 TrVC' 及成员证明 πVC。阶段 4 无签名 VC 发行：持有者向发行者提交 VC、πΦ、πVC、随机数 rᴴ、R 和辅助元数据 auxZD。发行者验证 R 与哈希值 h(rᴴ ∥ rᵢ) 匹配，验证 πVC 和 πΦ。通过验证后，发行者生成资格证明 πS，声明 (i) 发行者 DIDᴵ 属于合法发行者集 Merkle 树 TRIS，(ii) 有效 VC 由对该发行者发行。发行者构造 DID 令牌 DIDTok = (DIDᴵ, VC, R) 并计算其哈希 h(DIDTok)。最后发行者将 πS 和 h(DIDTok) 以及随机数发送给持有者，持有者将 (πS, rᵢ⁰, rᵢ, h(DIDTok)) 发布到区块链。

阶段 5 无签名 VC 验证：验证者在收到持有者的验证请求后，根据 πS 从区块链检索对应元组，检查 rᵢ = h(DIDᴴ, rᵢ⁰)，然后验证 πS 与两个 Merkle 根 TrIS 和 TrVC'。由于资格证明 πS 断言 VC 的有效性和发行者的合法性，验证者无需获取 VC 内容或发行者公钥即可验证，实现了零知识验证和发行者隐藏。

安全性方面，方案依赖 CRH 的碰撞抵抗性、NIZK 的完备性、可靠性和零知识性、承诺方案的隐藏性和绑定性，以及会话参数 (rᵢ⁰, rᴴ, R) 的安全绑定性。证明分为五个方面：VC 生成不可伪造性通过归约到 CRH 碰撞和 NIZK 可靠性；VC 发行不可伪造性归约到 NIZK 可靠性和哈希碰撞；VC 发行隐私通过混合论证，利用承诺隐藏性和 NIZK 零知识性；VC 验证隐私通过标准模拟论证；发行者匿名性通过混合论证，利用 NIZK 零知识性保证证明 πS 分布与特定发行者标识符无关。该方案具备 O(1) 的验证复杂度和通信开销。

### 核心公式与流程

**挑战哈希计算**
$$r_I := \operatorname{h}(\operatorname{DID}^{\operatorname{H}}, r_I^0) \leftarrow \operatorname{CRH.Hash}_{\operatorname{pp}_{\operatorname{h}}}(\operatorname{DID}^{\operatorname{H}}, r_I^0)$$
$$R := \mathfrak{h}(r_H \parallel r_I) \leftarrow \operatorname{CRH.Hash}_{\operatorname{pp}_{\operatorname{h}}}(r_H \parallel r_I)$$
> 作用：发行者计算绑定持有者身份的哈希 r_I，持有者组合双方随机数计算会话绑定哈希 R，防止重放攻击。

**DID 令牌构造**
$$\mathrm{DIDTok} := \left(\mathrm{DID}^{\mathrm{I}}, \mathrm{VC}, R\right) := \left(\mathrm{DID}^{\mathrm{I}}, \mathrm{VC}, \mathrm{h}\left(r_H \| r_I\right)\right)$$
$$\mathrm{h}(\text{DIDTok}) \leftarrow \text{CRH.Hash}_{\operatorname{pp}_{\operatorname{h}}}(\text{DIDTok})$$
> 作用：将发行者身份、VC 和会话绑定值 R 绑定为一个令牌，用于在零知识证明中隐藏发行者身份，只公开其哈希值。

**发行证明（Statement T）中的零知识断言**
$$\text{已知 private attr 和 } w_{\mathrm{ZD}} \text{ 使得：} 1: \text{VC opens to (attr, DID}^\text{H}\text{)}; 2: \Phi_\text{iss}(\text{attr}, \text{aux}_\text{ZD}) = 1; 3: \text{attr match the attributes in } w_\text{ZD}.$$
> 作用：断言 VC 的承诺属性满足发行谓词且源自权威文档，实现属性隐私保护与防伪造。

**资格证明（Statement S）中的零知识断言**
$$\text{已知 private DID}^\text{I}, \text{VC}, r_H \text{ 使得：} 1: \text{VC} \in \mathrm{TR}_{\mathrm{VC}}^\prime; 2: \text{DID}^\text{I} \in \mathrm{TR}_{\mathrm{IS}}; 3: \mathrm{h}(\text{DIDTok}) = \mathrm{CRH.Hash}_{\mathrm{pp_h}}(\mathrm{DID}^\mathrm{I}, \mathrm{VC}, \mathrm{h}(r_H \| r_I)).$$
> 作用：断言 VC 在链上列表中、发行者属于合法集，并绑定 VC、发行者身份和会话，同时隐藏发行者身份和 VC 内容。

### 实验结果

实验配置：Intel Xeon Platinum 8352V CPU，32 核 256GB 内存，使用 Python 系统编排和 Circom 语言构建算术电路，Groth16 证明方案部署在 BN128 椭圆曲线，Poseidon 哈希用于 ZKP 电路内部和 Merkle 树。参数包括 VC 数量 N_VC ∈ {2²,...,2⁹} 和 Merkle 树高度 H_MK ∈ {10,20,30,40,50,60}。

实验结果表明，SLVC-DIDA 验证阶段具有显著的高效性和稳定性。无论 VC 或 Merkle 树规模如何增长，验证时间、证明大小和验证密钥大小均保持不变：验证时间约 0.3 秒，证明大小约 800 字节。这是因为方案利用了 Groth16 协议的简洁性。与 Ring Referral 方案 [38] 的对比显示，SLVC-DIDA 在大规模场景下性能优势明显。当 Merkle/Ring 大小达到 2¹² 时，Ring Referral 的证明时间增长至约 150 秒（O(n) 复杂度），而 SLVC-DIDA 始终低于 1 秒（O(log n) 复杂度）。当 VC 数增至 2⁹ 时，SLVC-DIDA 证明大小只需数百字节且恒定，而 Ring Referral 超过 20,000 字节。

以太坊链上测试结果表明，VerifyIss(π_VC) 的部署 Gas 为 393,157，验证 Gas 为 221,626，平均验证时间 0.2784 秒，证明大小 804.5 字节；VerifyVC(π_S) 的部署 Gas 为 419,614，验证 Gas 为 229,108。两个验证算法的成本均为 O(1) 常数，证明了方案在资源受限区块链网络上的高效率和适用性。

### 局限性与开放问题

该方案的安全模型假定静态腐败对手，未考虑对手在协议执行过程中实施动态腐败的场景，在更强大敌手模型下的安全性有待验证。Merkle 树和 Groth16 证明系统的初始化设置（Setup）虽然是一次性的，但当系统规模增大时，电路编译和密钥生成的消耗仍相当可观，可能成为部署瓶颈。方案依赖链上存储和检索元组（πS, rᵢ⁰, rᵢ, h(DIDTok)），虽然数据量小且独立于 VC 列表和发行者集树，但区块链网络的拥堵和延迟可能影响实际用户体验。未来工作可探索更高效的去中心化初始化协议、动态腐败安全模型，以及与其他隐私增强技术的融合。

### 强关联论文

[2] Deepak 等. CanDID: Can-Do Decentralized Identity with Legacy Compatibility, Sybil-Resistance, and Accountability. **IEEE S&P 2021** [Google Scholar](https://scholar.google.com/scholar?q=CanDID%3A+Can-Do+Decentralized+Identity+with+Legacy+Compatibility%2C+Sybil-Resistance%2C+and+Accountability)

[10] Alangot 等. Decentralized Identity Authentication with Auditability and Privacy. **Algorithms 2022** [Google Scholar](https://scholar.google.com/scholar?q=Decentralized+Identity+Authentication+with+Auditability+and+Privacy)

[12] Mir 等. Aggregate Signatures with Versatile Randomization and Issuer-Hiding Multi-Authority Anonymous Credentials. **ACM CCS 2023** [Google Scholar](https://scholar.google.com/scholar?q=Aggregate+Signatures+with+Versatile+Randomization+and+Issuer-Hiding+Multi-Authority+Anonymous+Credentials)

[14] Rosenberg 等. zk-creds: Flexible Anonymous Credentials from zkSNARKs and Existing Identity Infrastructure. **IEEE S&P 2023** [Google Scholar](https://scholar.google.com/scholar?q=zk-creds%3A+Flexible+Anonymous+Credentials+from+zkSNARKs+and+Existing+Identity+Infrastructure)

[31] Sonnino 等. Coconut: Threshold Issuance Selective Disclosure Credentials with Applications to Distributed Ledgers. **ePrint 2018** [Google Scholar](https://scholar.google.com/scholar?q=Coconut%3A+Threshold+Issuance+Selective+Disclosure+Credentials+with+Applications+to+Distributed+Ledgers)

[38] Ta 等. Ring Referral: Efficient Publicly Verifiable Ad Hoc Credential Scheme with Issuer and Strong User Anonymity for Decentralized Identity and More. **IEEE S&P 2025** [Google Scholar](https://scholar.google.com/scholar?q=Ring+Referral%3A+Efficient+Publicly+Verifiable+Ad+Hoc+Credential+Scheme+with+Issuer+and+Strong+User+Anonymity+for+Decentralized+Identity+and+More)


## 关键词

+ SLVC-DIDA无签名可验证凭证DID认证
+ 永久颁发者隐藏PIH多方认证框架
+ 零知识RSA累加器颁发者匿名性
+ Merkle树VC列表身份属性隐私
+ 去中心化身份无PKI依赖验证
