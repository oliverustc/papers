---
title: "Sok: data sovereignty"
标题简称:
论文类型: conference
会议简称: EuroS&P
发表年份: 2023
modified: 2025-04-16 10:29:42
created: 2025-04-13 14:43:41
---

## Sok: data sovereignty

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/10190487)

## 作者

+ [Jens Ernstberger](Jens%20Ernstberger.md) 
+ Jan Lauinger 
+ Fatima Elsheimy 
+ Liyi Zhou 
+ Sebastian Steinhorst 
+ [Ran Canetti](Ran%20Canetti.md)
+ [Andrew Miller](Andrew%20Miller.md) 
+ Arthur Gervais 
+ [Dawn Song](Dawn%20Song.md) 

## 笔记

好的，作为您的密码学领域研究助手，我已深度阅读并分析了所提供的论文全文。以下是根据您要求格式输出的详尽结构化笔记。

### 背景与动机

当前网络环境（Web 2.0）中，用户数据由中心化实体控制，导致用户对其个人数据的掌控权严重缺失，数据泄露和隐私侵犯事件频发 [1]。尽管业界和学界都意识到赋予用户数据主权的重要性，但相关研究与产业实践却呈现碎片化状态，缺乏一个统一的系统化视角。现有工作大多孤立地关注“去中心化身份”这一单一子领域，而忽视了数据主权更广泛的含义——即用户控制数据如何被访问和处理的完整链条。该论文旨在填补这一空白，通过跨领域系统化梳理，厘清数据主权的三大核心支柱：去中心化身份、去中心化访问控制和符合策略的去中心化计算，并为后两个未被明确定义的新概念提出首个形式化定义，引导未来研究采用更全面的视角。

### 相关工作

[10] Fett et al. A comprehensive formal security analysis of OAuth 2.0. **CCS 2016** [Google Scholar](https://scholar.google.com/scholar?q=A+comprehensive+formal+security+analysis+of+OAuth+2.0)
> 核心思路：对 Web 2.0 中广泛使用的 OAuth 2.0 联邦身份协议进行了全面的形式化安全分析。
> 局限与区别：该工作证明了联邦身份模型中存在固有的安全弱点，用户必须信任身份提供商。本文的出发点是消除这种对中心化第三方的依赖，构建去中心化身份。

[29] Camenisch et al. Signature schemes and anonymous credentials from bilinear maps. **CRYPTO 2004** [Google Scholar](https://scholar.google.com/scholar?q=Signature+schemes+and+anonymous+credentials+from+bilinear+maps)
> 核心思路：提出了首个实用的匿名凭证方案，基于 CL 签名，允许用户以零知识证明的方式选择性披露属性。
> 局限与区别：该工作奠定了密码学基础，但并未集成到去中心化身份管理系统中。本文将其作为去中心化匿名凭证的关键密码学原语，并定义了其在 DID 体系中的形式化角色和协议流程。

[48] Sonnino et al. Coconut: Threshold issuance selective disclosure credentials with applications to distributed ledgers. **NDSS 2019** [Google Scholar](https://scholar.google.com/scholar?q=Coconut:+Threshold+issuance+selective+disclosure+credentials+with+applications+to+distributed+ledgers)
> 核心思路：提出了支持阈值签发的匿名凭证方案，解决了单一发行方单点故障问题，并支持链上验证。
> 局限与区别：该文主要关注凭证密码学原语本身。本文则将其作为去中心化匿名凭证的一个具体实例，并指出其链上验证成本高昂的挑战，进而推荐通用零知识证明方案。

[66] Kokoris-Kogias et al. Calypso: Private data management for decentralized ledgers. **VLDB 2020** [Google Scholar](https://scholar.google.com/scholar?q=Calypso:+Private+data+management+for+decentralized+ledgers)
> 核心思路：提出了基于分布式账本的访问控制系统，通过一个委员会管理密钥，实现对用户数据的策略化访问。
> 局限与区别：该文是去中心化访问控制的先驱工作。本文在其基础上，首次提出去中心化访问控制的形式化定义，将其与去中心化身份和策略化计算共同纳入数据主权的统一框架，并讨论了访问策略机密性和公平访问等更全面的安全性质。

[74] Cheng et al. Ekiden: A platform for confidentiality-preserving, trustworthy, and performant smart contracts. **EuroS&P 2019** [Google Scholar](https://scholar.google.com/scholar?q=Ekiden:+A+platform+for+confidentiality-preserving,+trustworthy,+and+performant+smart+contracts)
> 核心思路：提出了将智能合约执行与共识分离的架构，利用可信执行环境实现机密计算。
> 局限与区别：该文是机密智能合约的典型代表。本文将其视为实现符合策略的去中心化计算的一个技术选择，但指出其与本文的核心区别在于缺乏用户自定义的、用于治理数据使用的策略概念。

[52] Maram et al. CanDID: Can-Do Decentralized Identity with Legacy Compatibility, Sybil-Resistance, and Accountability. **SP 2021** [Google Scholar](https://scholar.google.com/scholar?q=CanDID:+Can-Do+Decentralized+Identity+with+Legacy+Compatibility,+Sybil-Resistance,+and+Accountability)
> 核心思路：提出一个去中心化身份系统，通过 TLS 预言机兼容现有 Web 2.0 身份源，并利用唯一标识符去重实现女巫攻击抵抗。
> 局限与区别：该文解决了去中心化身份落地中的关键问题（兼容性和抗女巫攻击）。本文引用该工作作为实现去中心化匿名凭证时，解决凭证发行和数据溯源问题的先进方案，并指出其仍依赖外部发行人。

[50] Rosenberg et al. zk-creds: Flexible Anonymous Credentials from zkSNARKs and Existing Identity Infrastructure. **SP 2023** [Google Scholar](https://scholar.google.com/scholar?q=zk-creds:+Flexible+Anonymous+Credentials+from+zkSNARKs+and+Existing+Identity+Infrastructure)
> 核心思路：提出利用通用零知识证明（zkSNARKs）构造匿名凭证，凭证形式为链上承诺，无需传统签名。
> 局限与区别：该工作代表了匿名凭证的最新趋势。本文将其作为实现高效链上验证和消除对签名发行方信任依赖的一个有前景的方向，并与其提出的去中心化匿名凭证形式化定义相关联。

### 核心技术与方案

本文的核心贡献在于为数据主权领域提供了一个清晰的系统化框架（见图1）。该框架将数据主权划分为三个相互关联的层次：身份层、数据层和应用层，并分别对应三个核心子领域：去中心化身份、去中心化访问控制以及符合策略的去中心化计算。每个子领域都构建在一个公共的可验证注册表（即分布式账本）之上。

1.  **去中心化身份管理（定义1）**：该模块的核心是将身份的创建、解析、更新和注销等操作去中心化。用户通过 `GENERATE` 算法生成密钥对 `(pk, sk)`，然后通过 `CREATE` 算法生成一个全局唯一的去中心化标识符（DID），并将包含公钥等信息的元数据 `MD_DID` 发布到分布式账本上。`RESOLVE` 算法允许任何人通过 DID 获取其关联的元数据，从而实现不依赖中心化注册中心的身份验证。其安全性在于，身份的控制权完全掌握在拥有私钥 `sk` 的用户手中，任何对元数据的更新或注销都必须通过持有私钥的实体发起，从而确保了身份的**唯一性**和**持久性**。系统通过允许用户生成多个伪随机标识符来实现**伪匿名性**。

2.  **去中心化匿名凭证（定义2）**：该模块在去中心化身份的基础上，实现了用户属性的可验证披露。协议包括 `REQUEST`、`ISSUE`、`PROVE`、`VERIFY` 和 `REVOKE` 五个核心算法。用户（U）首先向发行者（I）发起凭证请求 `REQ`，发行者验证后签发一个包含用户属性集的凭证 `cred`。在需要证明时，用户运行 `PROVE` 算法，针对一个谓词 `φ_cred` （如年龄大于18）生成一个零知识证明 π，而不泄露 `cred` 中的其他信息。验证者（V）运行 `VERIFY` 算法，通过解析发行者的 DID 获得其公钥，即可验证证明的有效性，无需与发行者交互。该协议满足了**不可伪造性**、**选择性披露**、**谓词可证明性**、**不可转移性**、**匿名性**和**不可链接性**等强隐私保护性质。凭证的撤销通过发行者将其加入撤销列表 `Rᶦ` 实现。

3.  **去中心化访问控制（定义3）**：该模块使用户能够对存储在外的加密数据实施细粒度的策略性访问。核心流程是用户（U）运行 `SET POLICY` 算法，用密钥 k 加密数据得到密文 `c_i^U`，并将访问策略 p 和通过 `SETUP SHARES` 算法生成的 k 的秘密份额 `k_i^AC` 分发给一组访问控制器（AC）。数据消费者（C）需要运行 `AUTHENTICATE` 算法，提交一个满足策略 p 的证明 π_A。验证通过后，访问控制器运行 `ACCESS` 算法，向 C 发放其持有的秘密份额。C 运行 `RECONSTRUCT` 算法，组合足够的份额恢复出密钥 k，从而解密数据。该协议保证了**数据机密性**，只有满足策略的数据消费者才能获得密钥；**可审计性**，所有认证和访问请求都在账本上留下记录；以及通过秘密共享实现的**公平访问**。将策略和秘密份额绑定，可以防止重放攻击。

4.  **符合策略的去中心化计算（定义4）**：该模块将用户控制从“是否可访问”扩展到“如何被使用”，以解决数据非竞争性问题。用户通过 `COMMIT` 算法提交加密数据 `c_in` 和包含访问谓词 (`φ_acc`)、输入谓词 (`φ_in`) 和输出谓词 (`φ_out`) 的策略。计算发起方（C）提供程序 Θ，访问控制器（AC）运行 `ANALYZE` 算法，验证 Θ 是否符合用户策略，并输出合规证明 π_A。随后，计算节点（CN）运行 `COMPUTE` 算法，接收解密密钥 `k_in` 和程序 Θ，在解密后的数据上执行计算，将结果用输出密钥 `k_out` 加密得到 `c_out`，并更新链上策略为 `p'`（例如，更新差分隐私预算），同时生成计算正确性证明 π_C。最后，数据消费者通过 `CLAIM` 算法获取输出。该模块结合了差分隐私，实现了用户可控的**隐私退化**，并通过**原子性数据交付**确保策略更新和输出交付的同步。

### 核心公式与流程

**[去中心化身份管理 - 定义1的核心操作]**
$$CREATE: (sk, pk) \to (DID, MD_{DID})$$
$$RESOLVE: (DID) \to MD_{DID}$$
> 作用：`CREATE` 算法利用用户密钥对生成一个全局唯一标识符 `DID`，并将元数据（含公钥）发布到账本。`RESOLVE` 算法允许任何人通过 `DID` 获取该元数据，实现不依赖第三方的身份解析。

**[去中心化匿名凭证 - 定义2的核心交互]**
$$ISSUE: \mathcal{I} \times (pp, REQ, sk_{\mathcal{I}}) \to cred$$
$$PROVE: \mathcal{U} \times (pp, cred, sk_{\mathcal{U}}, \phi_{cred}) \to \pi$$
> 作用：`ISSUE` 算法中，发行者 `I` 使用其私钥为用户 `U` 签发一个凭证 `cred`。`PROVE` 算法中，用户针对一个谓词 `φ_cred`（如 `age >= 18`）生成一个零知识证明 `π`，而无需披露 `cred` 中的其他属性。

**[去中心化访问控制 - 定义3的核心流程]**
$$SET POLICY: \mathcal{U} \times (pp, d_i^{\mathcal{U}}, k, \phi) \to (p, c_i^{\mathcal{U}})$$
$$AUTHENTICATE: \mathcal{C} \times (pp, p, aux) \to \pi_A$$
$$ACCESS: \mathcal{AC} \times (pp, \pi_A) \to (k_i^{\mathcal{AC}})$$
> 作用：用户用密钥 `k` 加密数据 `d_i^U` 并发布策略 `p`。数据消费者 `C` 生成满足策略 `p` 的证明 `π_A`。访问控制器 `AC` 验证证明后，发放其持有的密钥份额 `k_i^AC`，使 `C` 能重构密钥 `k` 并解密。

**[符合策略的去中心化计算 - 定义4的核心计算]**
$$ANALYZE: AC \times (pp, p, \Theta) \to (ct_{comp}, \pi_A)$$
$$COMPUTE: CN \times (pp, s, p, c_{in}, k^{in}, \Theta) \to (p', c_{out}, k^{out}, \pi_C)$$
> 作用：`ANALYZE` 算法中，访问控制器 `AC` 分析程序 `Θ` 是否符合策略 `p`，输出合规证明 `π_A`。`COMPUTE` 算法中，计算节点 `CN` 执行程序，输出加密结果 `c_out`、更新后的策略 `p'` 和计算正确性证明 `π_C`。

### 实验结果

本文并未提出具体的新协议，因此没有标准的实验性能评估。其“实验结果”本质上是对现有产业和学术解决方案的全面对比分析，汇总于表1。该表通过符号（● 支持、○ 不支持、- 不适用）系统地评估了超过20个系统对本文定义的核心功能的支持情况。关键发现包括：
1.  **产业界聚焦于去中心化身份**：大部分产业方案（如 SpruceID、iden3、PolygonID、Ceramic）重点实现了去中心化身份管理（定义1）和去中心化匿名凭证（定义2）的功能，但对去中心化访问控制和符合策略的去中心化计算的涉及较少。
2.  **学术界相对更全面**：学术项目如 Calypso 和 Coconut 覆盖了多个子领域，但各自侧重于不同的技术路线。
3.  **隐私支持存在差异**：在匿名凭证领域，系统在是否支持隐私保护方面有显著差异。例如，Hyperledger Indy 的早期方案不提供匿名性，而 Coconut、zk-creds 等则支持。
4.  **新兴技术趋势**：诸如 `zk-creds` 和 `Coconut` 等方案支持链上验证（用 ❇ 标注），代表了使用零知识证明实现高效验证的最新趋势。
5.  **功能缺口明显**：表1清晰地表明，符合策略的去中心化计算（定义4）是支持最少的领域，尤其是在产业界，这突显了该领域广阔的研究空间。

### 局限性与开放问题

1.  **效率和可扩展性的权衡**：构建同时满足隐私性、透明度和效率的系统极具挑战。例如，去中心化匿名凭证的链上验证成本高昂（如 `Coconut` 方案成本约 $950），而通用零知识证明虽能降低成本，但验证开销和电路复杂度仍是瓶颈。
2.  **策略表达力与机密性的矛盾**：对于去中心化访问控制，设计既能表达细粒度复杂策略，又能隐藏策略本身（策略机密性）的高效语言，仍是一个未解的难题。
3.  **并发策略更新与隐私预算跟踪**：在符合策略的计算中，处理对同一数据的并发计算请求、原子地更新策略（包括差分隐私预算），并抵抗重放攻击，是一个重要的开放挑战。
4.  **跨领域互操作性**：不同DID方法之间的互通性差，目前的通用解析器方案又在某种程度上重新引入了中心化风险。此外，不同子领域（如身份与访问控制）之间的无缝集成也尚待探索。

### 强关联论文

[1] Saleem et al. Sok: Anatomy of data breaches. **Proc. Priv. Enhancing Technol. 2020** [Google Scholar](https://scholar.google.com/scholar?q=Sok:+Anatomy+of+data+breaches)

[4] Krotova et al. Open data and data sharing: An economic analysis. **IW-Policy Paper 2020** [Google Scholar](https://scholar.google.com/scholar?q=Open+data+and+data+sharing:+An+economic+analysis)

[6] Weyl et al. Decentralized Society: Finding Web3's Soul. **SSRN 2022** [Google Scholar](https://www.google.com/favicon.ico)

[5] S. Steffen et al.


## 关键词

+ 数据主权
+ 去中心化身份认证
+ 去中心化访问控制
+ 合规性计算
+ 隐私保护
+ 系统化综述