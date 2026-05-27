---
title: "zklogin: Privacy-preserving blockchain authentication with existing credentials"
doi: 10.1145/3658644.3690356
标题简称: 
论文类型: conference
会议简称: CCS
发表年份: 2024
modified: 2025-05-09 10:51:30
created: 2025-04-13 17:52:56
---
## zklogin: Privacy-preserving blockchain authentication with existing credentials

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3658644.3690356)

## 作者

+ [Foteini Baldimtsi](Foteini%20Baldimtsi.md)
+ Konstantinos Kryptos Chalkias
+ Yan Ji
+ Jonas Lindstrøm
+ [Deepak Maram](Deepak%20Maram.md)
+ Ben Riva
+ [Arnab Roy](Arnab%20Roy.md)
+ Mahdi Sedaghat
+ Joy Wang

## 笔记

好的，作为一名密码学领域的研究助手，我将对论文《zkLogin: Privacy-Preserving Blockchain Authentication with Existing Credentials》进行深度阅读，并按照指定格式输出详尽的结构化笔记。

---

### 背景与动机

区块链用户的入门门槛是阻碍其大规模应用的关键瓶颈。传统的非托管钱包要求用户管理复杂的私钥或助记词，这种安全隐患和糟糕的用户体验常导致资产永久丢失 [33]。虽然中心化托管服务提供了类似传统互联网的体验，但其可靠性存疑，且近期多起重大托管机构倒闭事件 [17, 19, 28, 32] 削弱了用户的信任。一个自然的思路是利用用户对Google、Apple等全球性成熟平台已有的信任，通过OAuth 2.0等标准协议将现有账户直接用作区块链入口。然而，OAuth协议需要一个受信任的客户端（如Web服务器）作为中介来接收身份令牌（JWT），而区块链本身无法充当此角色，因此需要引入一个受信任的第三方预言机。这引出一个核心问题：能否在不引入额外信任实体的情况下，利用现有的认证系统（如OpenID Connect）来管理一个加密货币钱包？本文旨在回答这个问题，提出一个既能利用现有Web2账户提供便捷登录，又能保护用户隐私的区块链认证方案。

### 相关工作

[18] Heilman等. OpenPubkey: Augmenting OpenID Connect with User held Signing Keys. **ePrint 2023** [Google Scholar](https://scholar.google.com/scholar?q=OpenPubkey%3A+Augmenting+OpenID+Connect+with+User+held+Signing+Keys)
> 核心思路：将用户持有的公钥嵌入到OpenID Connect协议的nonce字段中，从而让JWT间接为该公钥签名。
> 局限与区别：OpenPubkey会将完整的JWT暴露给验证者，这在状态完全公开的区块链上会造成严重的隐私泄露。zkLogin通过零知识证明隐藏了JWT的敏感部分。

[30] Palladino. Sign in with Google to your Identity Contract. **Online Forum 2019** [Google Scholar](https://scholar.google.com/scholar?q=Sign+in+with+Google+to+your+Identity+Contract)
> 核心思路：提出了一种概念验证，直接将JWT发送到区块链智能合约上进行身份验证。
> 局限与区别：与[18]类似，该方法完全公开JWT载荷，且未解决如何授权具体区块链交易的问题，仅停留在身份认证层面。zkLogin不仅隐藏了隐私，还通过嵌入临时密钥实现了交易授权。

[31] Park等. Beyond the Blockchain Address: Zero-Knowledge Address Abstraction. **ePrint 2023** [Google Scholar](https://scholar.google.com/scholar?q=Beyond+the+Blockchain+Address%3A+Zero-Knowledge+Address+Abstraction)
> 核心思路：同样使用零知识证明和JWT来认证区块链交易。
> 局限与区别：该方案将交易内容紧密绑定在零知识证明中，导致每一笔交易都需要生成一个新的证明，产生了巨大的计算开销。此外，它假设OpenID提供商会使用ZK友好的签名（如EDDSA），但这与当前主流实践不符。zkLogin通过nonce嵌入技巧实现了单次证明的复用，并支持安全地将证明生成任务外包。

[26] Maram等. CanDID: Can-Do Decentralized Identity with Legacy Compatibility, Sybil-Resistance, and Accountability. **IEEE S&P 2021** [Google Scholar](https://scholar.google.com/scholar?q=CanDID%3A+Can-Do+Decentralized+Identity+with+Legacy+Compatibility%2C+Sybil-Resistance%2C+and+Accountability)
> 核心思路：无需修改现有Web2身份提供商即可将凭证迁移到区块链，通过引入一个MPC（安全多方计算）委员会来完成。
> 局限与区别：CanDID引入了一个额外的MPC委员会作为信任锚点，这与zkLogin旨在最小化信任假设的设计目标相悖。但CanDID的适用范围更广（如SAML、用户名密码），而zkLogin专注于支持OpenID Connect。

### 核心技术与方案

zkLogin系统的核心思想是利用OpenID Connect协议中签发的JSON Web Token (JWT) 作为用户身份的凭证，通过零知识证明技术隐藏JWT中的所有敏感信息，最终在与区块链交互时仅暴露必要的、不可链接的信息。其方案构建在一个名为 **Tagged Witness Signature (TWS)** 的新型密码学原语之上，该原语是Signatures of Knowledge (SoK) [7] 的扩展，专门建模了“凭证泄露”和“标签过期”的场景。

**1. 系统模型与实体**
zkLogin系统包含四个主要实体：**OpenID Provider (OP)**，如Google，负责签发JWT；**用户**，拥有OP账户，并希望在区块链上操作；**应用**，包含前端和后端，用于协调认证流程；**区块链**，由验证者组成，执行交易并验证zkLogin签名。在安全模型中，应用的后端被认为是不可信的，而前端是可信的；OP被认为是可信的。

**2. 地址推导与隐私保护**
用户的区块链地址 zkaddr 并非直接来源于公钥，而是通过哈希运算生成：
$$ \mathrm{zkaddr} = H (\text{stid}, \text{ aud}, \text{ iss}, \text{salt}) $$
其中 `stid` 是OP提供的稳定标识符（如`sub`），`aud` 是应用ID，`iss` 是OP的ID，`salt` 是一个随机值。`salt` 的作用是切断链下身份（如email）与链上地址之间的关联，实现**不可链接性**。若不使用盐，则地址具有**可发现性**，适用于记者签署文章等需要公开身份的场景。

**3. Tagged Witness Signature (TWS) 构造**
zkLogin的签名过程被形式化为一个TWS方案 $\Sigma_{\mathrm{zkLogin}}$，其核心密码学组件是Groth16零知识证明系统 [15] 和一个传统数字签名方案（如EDDSA）。该方案包含以下算法：
- **`Gen(1^λ)`**: 运行NIZK系统的设置算法 `Π.Gen(1^λ, Ckt)`，生成公共参考串 `crs`。
- **`Sign(tag, pk, w, M)`**:
    1.  解析标签 `tag = (pk_op, iss, zkaddr, T)`，私钥 `pk = crs`，见证 `w = (jwt, salt, r, vk_u, sk_u)`。
    2.  用临时私钥 `sk_u` 签名消息 `M`，得到 `σ_u = Sig.Sign(sk_u, M)`。
    3.  设置证明的公开输入 `zkx = (pk_op, iss, zkaddr, T, vk_u)`。
    4.  设置证明的私有见证 `zkw = (jwt, salt, r)`。
    5.  生成零知识证明 `π = Π.Prove(crs, zkx, zkw)`。
    6.  输出签名 `σ = (vk_u, T, σ_u, π)`。
- **`Verify(tag, pk, M, σ)`**: 验证证明 `π` 和临时签名 `σ_u` 的正确性。

**协议流程**
1.  **获取JWT**: 应用前端生成临时密钥对 `(vk_u, sk_u)` 和随机数 `r`，通过计算 `nonce = H(vk_u, T_max, r)` 作为JWT的nonce字段。用户向OP发起OAuth流程，OP返回一个JWT，该JWT本质上是一个对 `vk_u` 的证书。
2.  **获取盐**: 通过可信方式获取用户对应的 `salt`。
3.  **生成零知识证明**: 用户（或委托的服务）生成ZKP，证明如下电路 `Ckt`：
    $$ \text{Ckt} \binom{\text{zkx} = ( \text{pk}_{OP}, \text{iss}, \text{zkaddr}, T, \text{vk}_u),}{\text{zkw} = ( \text{jwt}, \text{salt}, r)} $$
    该电路验证：
    - 从JWT中提取的 `stid`, `aud`, `iss` 与盐哈希后等于 `zkaddr`。
    - JWT中的 `jwt.nonce` 等于 `H(vk_u, T, r)`。
    - JWT的签名有效。
4.  **提交交易**: 对于任何交易 `tx`，用户用 `sk_u` 签名得到 `σ_u`。最终的 **zkLogin签名** 为 `(vk_u, T, σ_u, π)`。区块链验证者验证ZKP和临时签名即可。

**安全性**
- **不可伪造性**: 基于Groth16的知识可靠性、JWT和临时签名方案的EUF-CMA安全性以及哈希函数的抗碰撞性。即使攻击者能获取针对其他标签（如过期的JWT）的见证，也无法伪造针对新标签的有效签名。
- **见证隐藏性 (隐私)**: 得益于Groth16的零知识性质，签名不会泄露关于见证（如JWT、salt）的任何信息。
- **zkLogin安全性**：直接归约为TWS的不可伪造性。
- **zkLogin不可链接性**：基于TWS的见证隐藏性以及zkaddr作为承诺的隐藏性质。

### 核心公式与流程

**[地址推导]**
$$ \mathrm{zkaddr} = H (\text{stid}, \text{ aud}, \text{ iss}, \text{salt}) $$
> 作用：将一个用户的链下稳定标识符（如`sub`）转化为链上的匿名地址。盐值确保了即使两个用户使用相同的`(stid, aud, iss)`组合，也会得到不同的链上地址，从而切断链接。

**[Nonce嵌入与交易授权]**
$$ \text{nonce} = H(vk_u, T_{\max}, r) $$
$$ \sigma_u = \text{Sig.Sign}(sk_u, tx) $$
> 作用：通过将用户的临时公钥`vk_u`绑定到JWT的nonce字段中，JWT实质成为了该公钥的一个证书。此后，用户可以用`sk_u`签署任意数量的交易，而无需为每笔交易都生成昂贵的零知识证明。`T_max`定义了临时密钥的有效期，`r`防止OP了解`vk_u`，增强隐私。

**[Tagged Witness Signature 验证流程]**
验证者收到签名 `σ = (vk_u, T, σ_u, π)`：
1.  验证 `T` 没有过期（`T ≥ T_cur`）。
2.  验证零知识证明 `π`，其公开输入为 `(pk_OP, iss, zkaddr, T, vk_u)`。
3.  验证临时签名 `σ_u`：`Sig.Verify(vk_u, σ_u, tx) == True`。
> 作用：这是zkLogin签名的核心验证过程，它将零知识证明的验证与传统数字签名的验证解耦，利用了一次性证明覆盖多笔交易的优势。

### 实验结果

zkLogin已在Sui区块链上部署。实验评估了其核心组件的性能，并在一个拥有8个验证节点（8核，128GB RAM，横跨纽约和洛杉矶）的测试网上进行了压力测试。
- **ZKP生成（委托服务）**: 在`n2d-standard-16`（16 vCPU, 64GB RAM）实例上，使用rapidsnark作为prover，平均生成一个证明的时间为 **2.78秒**（包含550ms的witness计算和2.1s的证明生成）。平均内存使用为0.82GB。
- **盐服务（TEE）**: 在`m5.xlarge`（4 vCPU, 16GB RAM）的AWS Nitro Enclave上，平均响应时间为 **0.2秒**。
- **端到端交易确认**: 首次交易的端到端延迟为 **3.52秒**（包含取盐和ZKP的时间）。随后在同一会话中的交易无需新的ZKP，延迟与传统签名相当（~120ms）。
- **验证者开销**: zkLogin签名验证时间为 **2.04毫秒**（Apple M1 Pro），比EdDSA（约56微秒）慢约36倍。签名大小约 **1300字节**（Base64编码），比EdDSA大一个数量级。对验证者吞吐量的影响较小：在1000 TPS的负载下，从EdDSA切换到zkLogin，吞吐量仅从850 TPS下降到750 TPS，下降约 **11%**。这表明签名验证并非验证者的主要瓶颈。
- **电路规模**: R1CS电路总约束数约为 **1,100,000**。其中SHA-2占66%，RSA大整数运算占14%，优化后的JWT解析仅占20%。

### 局限性与开放问题

1.  **性能权衡**: 尽管首次延迟（~3.5秒）可通过预取隐藏，但与原生签名相比仍存在较大差距。对于高频交易或对延迟极敏感的应用场景可能仍构成挑战。未来ZK证明系统的进展（如Ligetron [46]）有望解决此问题。
2.  **信任模型**: 虽然zkLogin旨在最小化信任，但在实用中盐的管理（委托给TEE或应用）和ZKP生成（委托给后端）都引入了新的信任假设，如TEE的安全性（易受侧信道攻击[29]）和MPC委员会的非合谋假设。提升用户自我管理盐的体验是开放问题。
3.  **OP依赖**: 当前实现仅支持RS256签名的JWT。虽然这覆盖了大多数主流提供商，但无法兼容使用ES256的提供商。对更广泛签名算法的支持是未来工作。此外，用户资产的最终安全性取决于OP账户的安全性，尽管salt管理策略可以缓解。
4.  **形式化模型**: TWS原语虽好，但仍依赖外部实体（如预言机）来获取当前OP公钥和时间信息，这些信息未在TWS模型中形式化，其安全性依赖于系统层面的正确实现。

### 强关联论文

[7] Chase等. On Signatures of Knowledge. **CRYPTO 2006** [Google Scholar](https://scholar.google.com/scholar?q=On+Signatures+of+Knowledge)
[15] Groth. On the Size of Pairing-Based Non-interactive Arguments. **EUROCRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=On+the+Size+of+Pairing-Based+Non-interactive+Arguments)
[18] Heilman等. OpenPubkey: Augmenting OpenID Connect with User held Signing Keys. **ePrint 2023** [Google Scholar](https://scholar.google.com/scholar?q=OpenPubkey%3A+Augmenting+OpenID+Connect+with+User+held+Signing+Keys)
[26] Maram等. CanDID: Can-Do Decentralized Identity with Legacy Compatibility, Sybil-Resistance, and Accountability. **IEEE S&P 2021** [Google Scholar](https://scholar.google.com/scholar?q=CanDID%3A+Can-Do+Decentralized+Identity+with+Legacy+Compatibility%2C+Sybil-Resistance%2C+and+Accountability)
[30] Palladino. Sign in with Google to your Identity Contract. **Online Forum 2019** [Google Scholar](https://scholar.google.com/scholar?q=Sign+in+with+Google+to+your+Identity+Contract)
[31] Park等. Beyond the Blockchain Address: Zero-Knowledge Address Abstraction. **ePrint 2023** [Google Scholar](https://scholar.google.com/scholar?q=Beyond+the+Blockchain+Address%3A+Zero-Knowledge+Address+Abstraction)


## 关键词

+ 零知识证明
+ 区块链认证
+ 隐私保护
+ OpenID Connect
+ 数字身份
+ Sui区块链