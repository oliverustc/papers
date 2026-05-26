---
title: "Revocable TACO: Revocable Threshold based Anonymous Credentials over Blockchains"
标题简称: 
论文类型: conference
会议简称: AsiaCCS
发表年份: 2024
created: 2025-05-20 02:21:25
modified: 2025-05-21 10:48:47
---

## Revocable TACO: Revocable Threshold based Anonymous Credentials over Blockchains

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3634737.3637656)

## 作者

+ Kanchan Bisht
+ Neel Yogendra Kansagra
+ Reisha Ali
+ Mohammed Sayeed Shaik
+ Maria Francis
+ Kotaro Kataoka

## 笔记

### 背景与动机
匿名凭证允许用户在不泄露多余信息的前提下证明属性，其多展示不可链接性和选择性披露特性对隐私保护至关重要。阈值匿名凭证通过分布式架构分发颁发与开放权限，避免了单点信任风险。然而，匿名性也可能被滥用——即使系统设计了开放（opening）机制，即指定权威机构可以揭露凭证对应的用户标识，已开放的凭证仍可被用户继续用于向第三方验证者成功认证。例如在贷款申请场景中，用户违约后，银行虽然能通过开放机制确定用户身份，但该用户仍可使用同一匿名凭证在其他银行发起新贷款申请。现有方案如 DTRAC [22] 在阈值匿名凭证中集成了开放功能，但缺乏撤销机制。因此，亟需一种能够在凭证被开放后阻止其继续使用的撤销方法。本文利用动态阈值累加器（DTA） [19] 实现这一目标，提出了可撤销的阈值匿名凭证方案 RTACO。

### 相关工作

[5] Camenisch 等. Short threshold dynamic group signatures. **SCN 2020** [Google Scholar](https://scholar.google.com/scholar?q=Short+threshold+dynamic+group+signatures)
> 核心思路：提出短阈值动态群签名，支持打开。  
> 局限与区别：该方案未考虑撤销机制，且群签名与匿名凭证在构造上存在差异，本文在阈值匿名凭证基础上额外集成 DTA 实现撤销。

[12] Connolly 等. Protego: Efficient, Revocable and Auditable Anonymous Credentials with Applications to Hyperledger Fabric. **INDOCRYPT 2022** [Google Scholar](https://scholar.google.com/scholar?q=Protego+Efficient+Revocable+and+Auditable+Anonymous+Credentials+with+Applications+to+Hyperledger+Fabric)
> 核心思路：提出支持撤销的匿名凭证方案，应用于 Hyperledger Fabric，但不支持阈值发行或打开。  
> 局限与区别：Protego 为单权威设置，本文针对阈值多权威场景，并利用区块链实现分布式撤销管理。

[19] Helminger 等. Multi-party revocation in sovrin: Performance through distributed trust. **CT-RSA 2021** [Google Scholar](https://scholar.google.com/scholar?q=Multi-party+revocation+in+sovrin+Performance+through+distributed+trust)
> 核心思路：提出动态阈值累加器（DTA），由多个管理器分布式管理累加器，支持添加与删除元素。  
> 局限与区别：DTA 本身不集成凭证系统；本文将 DTA 作为撤销组件嵌入阈值匿名凭证方案中，并定义了完整的 UC 安全协议。

[22] Naaz 等. Integrating Threshold Opening With Threshold Issuance of Anonymous Credentials Over Blockchains for a Multi-Certifier Communication Model. **IEEE Access 2022** [Google Scholar](https://scholar.google.com/scholar?q=Integrating+Threshold+Opening+With+Threshold+Issuance+of+Anonymous+Credentials+Over+Blockchains+for+a+Multi-Certifier+Communication+Model)
> 核心思路：提出 DTRAC，在阈值匿名凭证中集成打开机制，支持多认证模型。  
> 局限与区别：DTRAC 缺乏撤销功能；本文在其基础上增加 DTA 撤销，使得已打开的凭证可被封锁。

[23] Pointcheval 等. Short randomizable signatures. **CT-RSA 2016** [Google Scholar](https://scholar.google.com/scholar?q=Short+randomizable+signatures)
> 核心思路：提出 PS 签名，支持随机化与零知识证明，用于构建匿名凭证。  
> 局限与区别：PS 签名本身不提供撤销；本文将其作为底层签名方案，并扩展了额外属性（撤销句柄）。

[28] Sonnino. Coconut: Threshold Issuance Selective Disclosure Credentials with Applications to Distributed Ledgers. **2019** [Google Scholar](https://scholar.google.com/scholar?q=Coconut+Threshold+Issuance+Selective+Disclosure+Credentials+with+Applications+to+Distributed+Ledgers)
> 核心思路：提出基于区块链的阈值匿名凭证方案 Coconut，支持选择性披露，但不支持打开或撤销。  
> 局限与区别：Coconut 没有打开和撤销机制；本文借鉴其阈值发行框架，增加了打开和 DTA 撤销。

[19]（同上，因与 DTA 相关，此处不再重复）

[22]（同上）

[12]（同上）

[23]（同上）

[28]（同上）

### 核心技术与方案
RTACO 的整体框架如图 1 所示，它扩展了 TACO（阈值匿名凭证 + 打开）方案，增加了一层基于 DTA 的撤销机制。方案涉及五类实体：用户、认证者（certifier，颁发属性证书）、验证者（validator，阈值发行凭证）、撤销管理者（revocation manager，同时负责打开与撤销）和服务提供商（SP）。所有实体通过区块链通信，区块链上维护允许列表 WL 和封锁列表 BL，以及 DTA 的累加器值 Δ。核心构造思路如下：

1. **凭证发行**：用户向区块链提交凭证请求，系统为其分配一个唯一的撤销句柄 $k_l$，并使用 Shamir 秘密分享将 $k_l$ 拆分为份额分发给验证者和撤销管理者。验证者在颁发部分凭证时，将 $k_l$ 作为额外属性嵌入（通过额外的密钥 $y_c$）。撤销管理者将 $k_l$ 加入 DTA 累加器 Δ，生成对应的成员见证 $W_{k_l}$，并更新打开注册表。

2. **凭证聚合与展示**：用户收集 $t_v$ 个部分凭证后，通过拉格朗日插值聚合得到完整凭证 $\sigma = (H, S)$，其中 $S = xH + \sum_{j=1}^q y_j a_j H + y_c k_l H$，这正是 PS 签名在属性集 $(a_1,\dots,a_q,k_l)$ 上的签名。展示时，用户随机化 $\sigma$ 为 $\sigma'$，并生成零知识证明 $\pi_{cred}$，同时证明：a) 她拥有关于属性 $\{a_j\}$ 和 $k_l$ 的有效签名；b) 属性满足谓词 $\varphi$；c) $k_l$ 在 DTA 中未被撤销（即存在 $W_{k_l}$ 满足 $e(\Delta,\tilde{G}) = e(W_{k_l}, k_l\tilde{G} + pk_{acc})$）。该证明可借助 [20,29] 的技术转换为配对友好的形式。

3. **恶意凭证撤销**：当需要撤销某个凭证 $\sigma'$ 时，$t_r$ 个撤销管理者联合执行打开协议。他们首先计算预打开份额 $P_{k_l,m} = e(H', \mu_m')$，其中 $\mu_m'$ 存储了属性份额和 $k_l$ 份额的综合贡献。通过拉格朗日插值验证等式 $e(H',\tilde{X})\prod_{m\in T_r} P_{k_l,m}^{w_m} = e(S',\tilde{G})$ 可确定对应的 $k_l$。确定 $k_l$ 后，撤销管理者调用 DTA 的 Delete 函数从 DTA 中删除 $k_l$ 从 Δ 中删除，并将 $k_l$ 加入 BL。

4. **自撤销**：用户可主动请求自撤销：用户提交 $(k_l$ 持有者靠 $k_l$ 并给出证明 $\pi_{claim}$ 证明 $k_l$ 证明 $k_l$ 的承诺和 $k_l$ 的承诺并给出零知识证明 $\pi_{text}}}}}}的证明。该证明的**步骤。本文使用**安全 infiltrate思路的**整体方案：--- 重复使用**整体**使用**核心公式！=。

### 核心**概念描述


## 关键词

+ 可吊销凭证
+ 匿名凭证
+ 阈值密码学
+ 区块链
+ 隐私保护