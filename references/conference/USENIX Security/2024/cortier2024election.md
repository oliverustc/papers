---
title: "Election Eligibility with OpenID: Turning Authentication into Transferable Proof of Eligibility"
标题简称:
论文类型: conference
会议简称: USENIX Security
发表年份: 2024
created: 2025-04-29 17:24:25
modified: 2025-05-07 21:46:25
---

## Election Eligibility with OpenID: Turning Authentication into Transferable Proof of Eligibility

## 发表信息

+ [原文链接](https://www.usenix.org/conference/usenixsecurity24/presentation/cortier)

## 作者

+ Véronique Cortier 
+ Alexandre Debant 
+ Anselme Goetschmann 
+ Lucca Hirschi 

## 笔记

好的，以下是根据您提供的论文全文撰写的结构化笔记。

### 背景与动机

电子投票系统，如爱沙尼亚、瑞士、法国等国采用的系统，必须满足投票保密性和可验证性 [12, 24]。其中，资格可验证性旨在确保所有选票均由合法投票者投出，防止投票服务器篡改票箱。然而，许多现有系统（如 Helios [6]）仅假设在投票者和服务器之间存在认证信道，这实质上将验证权完全交给了诚实的服务器，无法抵御恶意的服务器伪造选票。为提供可验证的资格证明，一些系统（如 SwissPost [52]、Civitas [23]、Belenios [25]）引入了独立的注册机构，但这增加了额外的信任假设和系统复杂性。另一些系统（如爱沙尼亚系统 [34]）则依赖于投票者拥有公钥基础设施，这在多数选举中并不现实。一个核心挑战在于，如何在不依赖对投票服务器的单一信任点，也不引入复杂的额外机构的前提下，实现可传递的、保护隐私的资格证明。OpenID Connect [50] 作为一种广泛部署的认证协议，提供了一个潜在的解决方案，但其标准用法仅用于身份认证，无法产生可用于验证的、不可伪造的资格证据，也无法保护投票者的长期隐私。

### 相关工作

[6] Ben Adida. Helios: Web-based open-audit voting. **USENIX Security 2008** [Google Scholar](https://scholar.google.com/scholar?q=Helios%20Web-based%20open-audit%20voting)
> 核心思路：提出一个基于网页的、公开可审计的投票系统，使用同态加密和零知识证明实现可验证性。
> 局限与区别：论文指出 Helios 假设投票者与服务器间存在认证信道，这无法提供资格可验证性，投票服务器可以轻易地添加虚假选票。本文通过引入 OpenID 签名解决了这个问题。

[25] Véronique Cortier et al. Belenios: a simple private and verifiable electronic voting system. **Foundations of Security, Protocols, and Equational Reasoning 2019** [Google Scholar](https://scholar.google.com/scholar?q=Belenios%20a%20simple%20private%20and%20verifiable%20electronic%20voting%20system)
> 核心思路：提出了一个注重隐私和可验证性的投票系统，依赖一个注册机构来分发凭证，从而提供资格可验证性。
> 局限与区别：本文方案旨在消除对独立注册机构的需求，转而利用现有的 OpenID 提供商来生成可验证的资格证明。

[23] Michael R Clarkson et al. Civitas: Toward a secure voting system. **IEEE S&P 2008** [Google Scholar](https://scholar.google.com/scholar?q=Civitas%20Toward%20a%20secure%20voting%20system)
> 核心思路：一个旨在实现抗胁迫和收据不可获取性的投票系统，通过复杂的凭证和匿名信道来达成目标。
> 局限与区别：本文提出的 OpenID 方案不直接适用于 Civitas 这类需要精细控制认证凭证以支持抗胁迫的场景，需要专门的适配。

[34] Sven Heiberg et al. Improving the verifiability of the estonian internet voting scheme. **E-Vote-ID 2017** [Google Scholar](https://scholar.google.com/scholar?q=Improving%20the%20verifiability%20of%20the%20estonian%20internet%20voting%20scheme)
> 核心思路：利用国家的电子身份卡（PKI）对选票进行签名，以实现资格可验证性。
> 局限与区别：本文指出，这种签名直接绑定了选票和身份信息，破坏了永久隐私。此外，该方案依赖于一个多数国家不具备的 PKI 基础设施。本文的零知识证明版本解决了隐私问题。

[43] Wouter Lueks et al. VoteAgain: A scalable coercionresistant voting system. **USENIX Security 2020** [Google Scholar](https://scholar.google.com/scholar?q=VoteAgain%20A%20scalable%20coercionresistant%20voting%20system)
> 核心思路：一种可扩展的抗胁迫投票系统，允许投票者秘密地重投票以对抗胁迫。
> 局限与区别：本文方案不直接适用于此，因为其与 OpenID 的交互会破坏重投票的隐蔽性和抗胁迫模型。

[52] Swiss Post. e-voting system. (网址见原文)
> 核心思路：瑞士邮政开发的电子投票系统，使用返回码和独立的注册机构来保障可验证性。
> 局限与区别：该系统同样引入了独立的注册机构，增加了信任假设。本文方案旨在通过现有的身份提供商来简化这一模型。

[44] Deepak Maram et al. Candid: Can-do decentralized identity with legacy compatibility, sybil-resistance, and accountability. **IEEE S&P 2021** [Google Scholar](https://scholar.google.com/scholar?q=Candid%20Can-do%20decentralized%20identity%20with%20legacy%20compatibility%20sybil-resistance%20and%20accountability)
> 核心思路：提出一个去中心化的身份管理服务，通过预言机（MPC或TEE）从多个现有服务聚合身份，以保护隐私。
> 局限与区别：CanDID 需要更强的信任和系统假设（如分布式 MPC 或 TEE），不直接解决选举资格证明中链接选票与选民身份的需求。

[9] Foteini Baldimtsi et al. zklogin: Privacypreserving blockchain authentication with existing credentials. **arXiv preprint 2024** [Google Scholar](https://scholar.google.com/scholar?q=zklogin%20Privacypreserving%20blockchain%20authentication%20with%20existing%20credentials)
> 核心思路：一个与本文同期且独立的并行工作，也使用 zk-SNARK 将 OpenID 认证转化为隐私保护的区块链登录凭证。
> 局限与区别：zkLogin 依赖更强的假设（如 TEE、复杂设置仪式），且不处理选举资格证明的核心挑战，如防止重放旧凭证签名或链接选票。

### 核心技术与方案

本文提出了两个核心协议：OIDEli 和 OIDEli-zk。两者均使用 OpenID 提供商作为签名预言机，将投票过程中的认证转换为可传递的资格证明。攻击模型假设 OpenID 提供商是诚实的，而投票服务器和部分投票者可能是不诚实的。

**OIDEli 协议**的核心在于让  OpenID  提供商签署一个包含投票者身份  $id$  和其选票  $b$  的非随机值。由于 OpenID 标准要求 RP 生成一个随机数 `nonce


## 关键词

+ OpenID选举资格证明
+ 可转让资格证明协议
+ zk-SNARK隐私选举系统
+ Belenios投票协议集成
+ 永久隐私选举认证
+ 数字身份资格验证
