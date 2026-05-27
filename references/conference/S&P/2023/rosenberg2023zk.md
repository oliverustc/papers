---
title: "zk-creds: Flexible anonymous credentials from zksnarks and existing identity infrastructure"
doi: 10.1109/sp46215.2023.10179430
标题简称:
论文类型: conference
会议简称: S&P
发表年份: 2023
modified: 2025-05-15 05:46:12
created: 2025-04-14 09:35:08
---
## zk-creds: Flexible anonymous credentials from zksnarks and existing identity infrastructure

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/10179430)
+ [archive](https://eprint.iacr.org/2022/878)
+ [code](https://github.com/rozbb/zkcreds-rs)

## 作者

+ Michael Rosenberg
+ Jacob White
+ [Christina Garman](Christina%20Garman.md)
+ [Ian Miers](Ian%20Miers.md)
## 笔记

### 背景与动机
匿名凭证旨在解决用户在网络上证明身份属性（如年龄、居住地）而不被跟踪的隐私保护问题。现有方案虽然经过大量学术研究，但极少在实际中部署，根本原因在于它们对现实身份体系做出了一系列不切实际的假设。典型假设包括：存在单一的权威为某一属性颁发凭证；当有多个颁发者时，属性格式兼容；存在既愿意又有能力保管签名密钥并运行复杂密码协议的受信任方；所有凭证属性格式均需预先知晓；并且凭证颁发者的集合必须在系统初始时刻确定。然而，现实世界的身份体系是碎片化的（例如美国有超过50种驾照颁发机构），其凭证格式各异，且绝大多数潜在颁发者既不愿也无法采用新的密码协议。此外，访问控制条件会动态变化，常常需要组合多个不同来源的凭证（如疫苗卡和照片身份证）来满足复杂断言。这些现实复杂性正是zk-creds所要解决的空白。

### 相关工作

[35] Garman et al. Decentralized Anonymous Credentials. **NDSS 2014** [Google Scholar](https://scholar.google.com/scholar?q=Decentralized+Anonymous+Credentials)
> 核心思路：首次提出使用透明度日志或区块链来维护凭证列表，从而避免颁发者持有签名密钥。
> 局限与区别：用户需存储完整的凭证列表且每次出示的计算时间与列表大小成线性关系；不支持复杂身份声明的组合，也没有解决如何在不泄露敏感信息的情况下签发凭证（即zk-creds解决的zk-supporting-documentation问题）。

[55] Sonnino et al. Coconut: Threshold Issuance Selective Disclosure Credentials. **NDSS 2019** [Google Scholar](https://scholar.google.com/scholar?q=Coconut+Threshold+Issuance+Selective+Disclosure+Credentials)
> 核心思路：通过门限签名（如FROST）将凭证颁发权分散到多个静态服务器，假设容忍t > 1/2的腐败。
> 局限与区别：虽然增强了颁发者的安全性，但并未解决颁发者稀缺的问题，因为仍需要找到一个群体愿意并能够运行密码基础设施；且仅支持选择性披露属性，不支持通用的零知识证明或动态组合的访问标准。

[62] Zhang et al. DECO: Liberating Web Data Using Decentralized Oracles for TLS. **ACM CCS 2020** [Google Scholar](https://scholar.google.com/scholar?q=DECO+Liberating+Web+Data+Using+Decentralized+Oracles+for+TLS)
> 核心思路：通过两方协议和零知识证明，允许用户向第三方证明其TLS会话中数据的真实性，从而实现身份证明的去中心化。
> 局限与区别：DECO本身不构成一个完整的匿名凭证系统，且依赖非共谋假设或可信硬件，但随着凭证价值的增加，这些假设的脆弱性也随之增加。

[28] Davidson et al. Privacy Pass: Bypassing Internet Challenges Anonymously. **PoPETs 2018** [Google Scholar](https://scholar.google.com/scholar?q=Privacy+Pass+Bypassing+Internet+Challenges+Anonymously)
> 核心思路：通过盲签名发布一次性、不可链接的令牌，用于绕过如CAPTCHA等互联网挑战。
> 局限与区别：并非完整的匿名凭证方案，不支持可重复使用、速率限制或复杂的属性断言。

[24] Camenisch et al. Design and Implementation of the Idemix Anonymous Credential System. **ACM CCS 2002** [Google Scholar](https://scholar.google.com/scholar?q=Design+and+Implementation+of+the+Idemix+Anonymous+Credential+System)
> 核心思路：基于CL签名的早期匿名凭证系统，支持选择性披露。
> 局限与区别：需要单一的、持有长期签名密钥的受信任颁发者，且凭证的发行与验证电路都是定制的，缺乏通用性和灵活性。

[39] Groth. On the Size of Pairing-Based Non-Interactive Arguments. **EUROCRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=On+the+Size+of+Pairing-Based+Non-Interactive+Arguments)
> 核心思路：提出Groth16，一种高效的、具有恒定证明大小的zkSNARK方案，但需要针对每个电路进行一次可信设置。
> 局限与区别：本文将其作为底层技术，并在此基础上构建了“盲Groth16”机制以支持证明间的链接，克服了Groth16静态设置的限制。

### 核心技术与方案

zk-creds的核心思想是用通用零知识证明（zkSNARKs）替代传统的盲签名，作为匿名凭证的基石，从而实现无需信任特定颁发者的灵活身份断言系统。

系统整体框架由三个主要组件构成：**Merkle森林**用于实现高效且可审计的凭证列表成员证明；**盲Groth16**（LinkG16）用于将成员证明与访问条件证明链接起来，支持证明重用和模块化组合；以及可插拔的**Gadgets**用于定义任意访问控制条件。

**Merkle森林**：与传统使用单一Merkle树不同，zk-creds使用一个由多个Merkle树组成的森林。凭证成员证明包含两步：首先证明凭证 $cred$ 属于某棵树 $T$ ，然后证明该树的根 $T_{root}$ 属于森林 $F$。这种方法为开发者提供了可调节的权衡：通过选择更矮的树，可以显著减少证明生成时间（最多可降低50%，即143毫秒），而森林成员证明的代价对于验证者来说可以忽略不计（137微秒）。每个成员的认证路径 $\theta$ 大小与树高成对数关系，用户只需存储和维护这一路径而非整个凭证列表。

**盲Groth16（LinkG16）**：这是zk-creds中具有独立价值的创新。它允许证明者将一个预先计算好的Groth16证明（例如，代价高昂的Merkle树成员证明）与多个其他Groth16证明（例如，访问条件证明）链接起来，以证明它们都关于同一个隐藏的公共输入（即凭证 $cred$ 和其所属的树根 $T_{root}$），而无需揭示这些输入。LinkG16的核心思想是，对于每个需要链接的Groth16证明 $\pi_i$，证明者选择一个盲化因子 $z_i \leftarrow \mathbb{F}$，计算一个盲化的公开输入 $U_i := z_i [\delta]_1^{(i)} + \sum_{j=0}^{t-1} a_j W_j^{(i)}$，并相应地去盲化证明中的 $C$ 组件为 $C_i' := C_i - [z_i]_1$。然后，通过一个离散对数相等性证明（EqWire）证明所有 $U_i$ 都承诺了相同的隐藏值 $\{a_j\}$ 。最终的链接证明由EqWire证明、所有盲化后的 `U_i` 和去盲化的 $\pi_i'$ 组成。该方案满足完备性、完美HVZK和知识健全性。

**Gadgets和访问条件**：由于使用通用零知识证明，任何NP关系都可以被实现为一个Gadget，并动态地组合。系统预定义了一些常用Gadget：**Linkable Show**揭示一个基于伪随机函数 `PRF_nk(ctx)` 的假名，用于防女巫攻击；**Rate limiting**使用 `PRF_rk(epoch||ctr)` 生成令牌并限制计数器小于阈值 $N$；**Cloning resistance**基于 [19] 的思想，通过发送两个令牌 `tok1` 和 `tok2` 来检测凭证是否被克隆并泄露用户身份，其中 `tok2 = id + H(nonce) * PRF_rk'(epoch||ctr)`；**Expiry**检查凭证中的过期属性是否大于当前日期；**Session binding**通过将验证者指定的nonce作为Groth16证明的公共输入来防止重放攻击。

此外，zk-creds还支持**签名签发凭证**，即用一个验证签名（如Schnorr或门限Schnorr）的Gadget替换Merkle森林成员关系Gadget，从而兼容传统的信任模型。系统还支持隐藏颁发者、隐藏凭证类型、授权、公开审计等功能。

### 核心公式与流程

**[LinkG16验证方程]**
$$e(A_i', B_i') = e([\alpha]_1^{(i)}, [\beta]_2^{(i)}) \cdot e(C_i', [\delta]_2^{(i)}) \cdot e(U_i + \hat{S}_i, H)$$
> 作用：验证一个去盲化后的Groth16证明是否正确，其中 $U_i$ 包含了盲化的隐藏公共输入，$\hat{S}_i$ 是验证者已知的公开公共输入。该方程等价于对原始证明 $\pi_i$ 的Groth16验证。

**[EqWire挑战-响应协议]**
$$ \text{Prover: } \forall i: com_i := \sum_j r_j W_j^{(i)} + s_i [\delta]_1^{(i)} $$
$$ \text{Verifier: } c $$
$$ \text{Prover: } \forall j: \rho_j := r_j - c a_j, \quad \forall i: \sigma_i := s_i - c z_i $$
$$ \text{Verifier: } \forall i: com_i = \sum_j \rho_j W_j^{(i)} + \sigma_i [\delta]_1^{(i)} + c U_i $$
> 作用：作为一个Sigma协议，零知识地证明所有 $U_i$ 承诺了相同的秘密值 $\{a_j\}$

**[克隆抵抗的令牌生成]**
$$\text{tok}_1 = \text{PRF}_{\mathrm{rk}}(\text{epoch} \| \text{ctr})$$
$$\text{tok}_2 = \text{id} + H(\text{nonce}) \cdot \text{PRF}_{\mathrm{rk}}'(\text{epoch} \| \text{ctr})$$
> 作用：当凭证被克隆时，验证者得到重复的 `tok1` 和不同的 `tok2`，从而可以解联立方程得到用户身份 `id`，实现克隆检测。

**[访问条件示例：年龄验证]**
``` 
dob <= today - 18yrs and expiry > today and CloneResistance(rk, nonce, tok1, tok2, ...)
```
> 作用：定义了用于访问年龄限制内容的逻辑谓词，该谓词在零知识证明电路内部被检查。

### 实验结果

实验在2021年Intel i9-11900KB CPU、64GiB RAM的桌面电脑上进行，代码为7.6k行Rust，基于Arkworks框架和BLS12-381曲线，哈希函数为Poseidon。对于 $2^{31}$ 个凭证的Merkle森林（树高24，$\#trees = 2^8$），客户端优化版本的核心性能为：一个包含预计算Merkle成员证明的基本出示仅需**5ms**，验证需**3ms**；若需要重新计算全部成员证明，则出示耗时约**460ms**。对于更复杂的场景，如克隆抵抗，预计算版本为**90ms**，完全版为**542ms**。当采用服务端优化版本（合并为一个证明）时，验证时间降至**1.5ms**，批处理验证吞吐量可达**1.8次/ms/核**。使用Pedersen哈希替代Poseidon时，证明时间约增加一倍（如年龄验证从143ms增至258ms）。在应用案例中，基于美国护照的年龄验证出示仅需**143ms**，验证仅**5ms**。签名签发版本的基本出示仅需**2ms**。证明大小在客户端优化版本下为744B（基本）到1064B（复杂），服务端优化版本为192B。

### 局限性与开放问题

当前zk-creds依赖于Groth16，这需要为每个电路进行一次可信设置，虽然分布式设置仪式可以缓解此问题，但仍增加了部署负担。Merkle树证需要定期更新，虽然论文提出了广播更新等解决方案，但在实践中仍需仔细权衡隐私与开销。未来工作可探索与更先进的零知识证明系统（如Plonk或无设置方案）结合，或与不同的累加器方案（如RSA累加器或Verkle树）协同设计，以进一步提升性能。此外，完全实现基于DID或DECO等去中心化身份断言方式的集成仍是一个开放方向。

### 强关联论文

[35] Garman et al. Decentralized Anonymous Credentials. **NDSS 2014** [Google Scholar](https://scholar.google.com/scholar?q=Decentralized+Anonymous+Credentials)

[55] Sonnino et al. Coconut: Threshold Issuance Selective Disclosure Credentials. **NDSS 2019** [Google Scholar](https://scholar.google.com/scholar?q=Coconut+Threshold+Issuance+Selective+Disclosure+Credentials)

[62] Zhang et al. DECO: Liberating Web Data Using Decentralized Oracles for TLS. **ACM CCS 2020** [Google Scholar](https://scholar.google.com/scholar?q=DECO+Liberating+Web+Data+Using+Decentralized+Oracles+for+TLS)

[28] Davidson et al. Privacy Pass: Bypassing Internet Challenges Anonymously. **PoPETs 2018** [Google Scholar](https://scholar.google.com/scholar?q=Privacy+Pass+Bypassing+Internet+Challenges+Anonymously)

[24] Camenisch et al. Design and Implementation of the Idemix Anonymous Credential System. **ACM CCS 2002** [Google Scholar](https://scholar.google.com/scholar?q=Design+and+Implementation+of+the+Idemix+Anonymous+Credential+System)

[39] Groth. On the Size of Pairing-Based Non-Interactive Arguments. **EUROCRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=On+the+Size+of+Pairing-Based+Non-Interactive+Arguments)

[19] Camenisch et al. How to win the clonewars: Efficient periodic n-times anonymous authentication. **ACM CCS 2006** [Google Scholar](https://scholar.google.com/scholar?q=How+to+win+the+clonewars+Efficient+periodic+n-times+anonymous+authentication)

[38] Grassi et al. Starkad and Poseidon: New hash functions for zero knowledge proof systems. **ePrint 2019** [Google Scholar](https://scholar.google.com/scholar?q=Starkad+and+Poseidon+New+hash+functions+for+zero+knowledge+proof+systems)

[44] Komlo and Goldberg. FROST: Flexible Round-Optimized Schnorr Threshold Signatures. **Selected Areas in Cryptography** [Google Scholar](https://scholar.google.com/scholar?q=FROST+Flexible+Round-Optimized+Schnorr+Threshold+Signatures)

[13] Brickell et al. Direct Anonymous Attestation. **ACM CCS 2004** [Google Scholar](https://scholar.google.com/scholar?q=Direct+Anonymous+Attestation)


## 关键词

+ 匿名凭证
+ 零知识证明
+ 透明度日志
+ 身份隐私保护
+ 遗留身份文件转换
+ zk-SNARK应用