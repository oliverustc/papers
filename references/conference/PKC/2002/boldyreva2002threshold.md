---
title: "Threshold signatures, multisignatures and blind signatures based on the gap-Diffie-Hellman-group signature scheme"
doi: 10.1007/3-540-36288-6_3
标题简称:
论文类型: conference
会议简称: PKC
发表年份: 2002
created: 2025-05-27 11:54:27
modified: 2025-05-27 11:55:01
---
## Threshold signatures, multisignatures and blind signatures based on the gap-Diffie-Hellman-group signature scheme

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/3-540-36288-6_3)

## 作者

+ Alexandra Boldyreva

## 笔记

### 背景与动机
数字签名是密码学的核心原语，但在实际部署中，单一签名者构成单点故障，且无法支持群组签名、隐私保护等高级需求。传统方案如 RSA 或 DSS 的阈值、多重和盲签名的扩展往往面临效率低下、交互复杂、安全证明困难等问题。具体而言，阈值签名方案常需要零知识证明或误差校正，导致计算开销大、容错比率低；多重签名方案要么签名长度随参与者数线性增长，要么要求预先知道签名者集合；盲签名方案则长期缺乏基于标准困难问题的安全证明。Gap Diffie‑Hellman (GDH) 群——其中计算性 Diffie‑Hellman 问题困难而判定性 Diffie‑Hellman 问题容易——为 Boneh、Lynn 和 Shacham 在 Asiacrypt 2001 提出的短签名方案 [8] 提供了独特结构，使得签名验证仅需检查一个 DH 元组，而签名计算为哈希值的指数运算。本文旨在利用 GDH 群的结构优势，构造简洁、高效且可证明安全的阈值、多重和盲签名方案，填补现有方案在交互性、鲁棒性和安全性证明方面的空白。

### 相关工作

[8] Boneh et al. Short signatures from the Weil pairing. **Asiacrypt 2001** [Google Scholar](https://scholar.google.com/scholar?q=Short+signatures+from+the+Weil+pairing)
> 核心思路：提出 GDH 群上的签名方案 GS，私钥为 $x$，公钥为 $y=g^x$，签名 $\sigma=H(M)^x$，验证通过 DDH 算法判定 $(g,y,H(M),\sigma)$ 是否为有效 DH 元组。
> 局限与区别：该方案本身是基础签名，未涉及分布式或多用户场景。本文基于此构造了阈值、多重和盲签名。

[21] Gennaro et al. Robust threshold DSS signatures. **Eurocrypt 1996** [Google Scholar](https://scholar.google.com/scholar?q=Robust+threshold+DSS+signatures)
> 核心思路：提出鲁棒阈值 DSS 方案，无需可信分发者，安全证明无需随机预言，但容错 $t<n/4$，签名生成协议需要多轮交互，复杂度高。
> 局限与区别：本文的阈值方案容错 $t<n/2$，签名生成非交互，仅需乘法操作，远更高效。

[44] Shoup. Practical threshold signatures. **Eurocrypt 2000** [Google Scholar](https://scholar.google.com/scholar?q=Practical+threshold+signatures)
> 核心思路：提出鲁棒阈值 RSA 方案，容错 $t<n/2$，签名生成非交互，但需要可信分发者，且依赖安全素数乘积的 RSA 模数。
> 局限与区别：本文方案无需可信分发者（分布式密钥生成），且利用 GDH 群避免了 RSA 模数生成和零知识证明。

[33] Micali et al. Accountable-subgroup multisignatures. **ACM CCS 2001** [Google Scholar](https://scholar.google.com/scholar?q=Accountable-subgroup+multisignatures)
> 核心思路：基于 Schnorr 签名的多重签名方案，要求签名者集合预先已知，且协议需要三轮通信，不支持并发。
> 局限与区别：本文方案无需预先知道签名者集合，仅需一轮广播，签名长度与参与者数无关，支持并发。

[2] Bellare et al. The One-More-RSA-Inversion Problems and the security of Chaum's Blind Signature Scheme. **Financial Cryptography 2001** [Google Scholar](https://scholar.google.com/scholar?q=The+One-More-RSA-Inversion+Problems+and+the+security+of+Chaum%27s+Blind+Signature+Scheme)
> 核心思路：引入 Chosen‑Target RSA 逆问题，证明 Chaum 盲签名方案的安全性。
> 局限与区别：本文针对 GDH 群定义 Chosen‑Target CDH 问题，并证明盲签名 BGS 的安全性。

[22] Gennaro et al. Secure distributed key generation for discrete-log based cryptosystems. **Eurocrypt 1999** [Google Scholar](https://scholar.google.com/scholar?q=Secure+distributed+key+generation+for+discrete-log+based+cryptosystems)
> 核心思路：提出分布式密钥生成协议 DKG，用于离散对数密码系统，输出公钥 $y=g^x$ 以及每个参与者的秘密份额 $x_i$，满足 Shamir 秘密共享。
> 局限与区别：本文直接采用 DKG 作为阈值方案的密钥生成部分，无需额外交互。

[26] Herzberg et al. Proactive secret sharing, or: How to cope with perpetual leakage. **Crypto 1995** [Google Scholar](https://scholar.google.com/scholar?q=Proactive+secret+sharing+or+How+to+cope+with+perpetual+leakage)
> 核心思路：提出主动秘密共享协议 PSS，定期刷新份额以抵抗移动攻击。
> 局限与区别：本文指出 TGS 满足 [25] 中可主动化的条件，可直接应用 PSS 实现主动安全。

### 核心技术与方案

本文提出了基于 GDH 群签名方案 GS [8] 的三个扩展协议，每个协议均利用 GDH 群的线性性质和签名 $\sigma = H(M)^x$ 的乘法同态性。

**阈值签名方案 TGS**：采用 Gennaro 等人 [22] 的分布式密钥生成协议 DKG 作为 $\mathcal{TK}$，无需可信分发者。协议执行后，各参与者 $P_i$ 持有秘密份额 $x_i$，满足 $(x_1,\ldots,x_n) \overset{(t,n)}{\longrightarrow} x$，且公钥 $y=g^x$。公开验证信息 $B_i = g^{x_i}$ 可由公开信息导出。签名生成时，任意 $>t$ 个参与者计算签名份额 $\sigma_i = H(M)^{x_i}$ 并广播。指定聚合者 D 首先通过 $\mathcal{V}_{DDH}(g, B_i, H(M), \sigma_i)$ 验证每个份额的有效性（鲁棒性），然后使用 Lagrange 插值计算完整签名 $\sigma = \prod_{i\in R} \sigma_i^{L_i}$，其中 $L_i$ 为对应集合 $R$ 的 Lagrange 系数。由于 $\sigma = H(M)^{\sum L_i x_i} = H(M)^x$，正确性成立。安全性证明基于 GDH 假设和随机预言模型，可抵抗 $t<n/2$ 的恶意敌手。该方案签名生成非交互（仅广播），无需零知识证明，且可通过 [26,25] 的方法添加主动安全更新。

**多重签名方案 MGS**：每个用户独立运行 GS 的密钥生成，私钥 $x_j$，公钥 $y_j=g^{x_j}$。要对消息 $M$ 签名，任意子集 $L$ 的成员各自计算并广播 $\sigma_j = H(M)^{x_j}$。聚合者 D 计算 $\sigma = \prod_{j\in J} \sigma_j$，输出 $(M, L, \sigma)$。验证者计算聚合公钥 $pk_L = \prod_{j\in J} y_j$，然后验证 $(g, pk_L, H(M), \sigma)$ 是否为有效 DH 元组。正确性源于 $\sigma = H(M)^{\sum x_j}$。安全性模型允许敌手控制除一个诚实用户外的所有参与者，并可自适应生成恶意公钥（要求敌手输出对应的私钥，模拟知识证明）。定理 3 在随机预言模型下证明 MGS 安全。该方案解决了 [33] 中提出的开放问题——签名者集合可在签名份额计算后决定，且仅需一轮广播，签名长度恒定。

**盲签名方案 BGS**：密钥生成与 GS 相同。盲签名协议：用户持有公钥 $y$，欲对消息 $M$ 盲签名，选取随机 $r\in \mathbb{Z}_p^*$，计算 $\overline{M} = H(M) \cdot g^r$ 发送给签名者。签名者计算 $\overline{\sigma} = (\overline{M})^x$ 返回。用户计算 $\sigma = \overline{\sigma} \cdot y^{-r} = (H(M)\cdot g^r)^x \cdot (g^x)^{-r} = H(M)^x$ 得到标准签名。盲性显然成立，因为签名者仅收到随机的 $\overline{M}$。安全性归约到 Chosen‑Target CDH 问题：敌手可以查询目标预言机获得随机群元素 $z_i$，以及辅助预言机（即签名者）对任意元素计算 $(\cdot)^x$。若敌手经过 $q_h$ 次辅助查询后能输出 $l>q_h$ 个有效的 $v_i = z_{j_i}^x$，则称其攻破该假设。定理 4 表明 BGS 在随机预言模型下安全。

### 核心公式与流程

**GS 签名方案**
$$K: x \xleftarrow{\$} \mathbb{Z}_p^*,\quad y = g^x$$
$$S: \sigma = H(M)^x$$
$$V: \mathcal{V}_{DDH}(g, y, H(M), \sigma) \stackrel{?}{=} 1$$
> 作用：基础签名，验证等价于判定 $(g,y,H(M),\sigma)$ 为有效 DH 元组。

**TGS 阈值签名**
$$TK: \text{DKG 协议} \rightarrow (x_1,\ldots,x_n) \overset{(t,n)}{\longrightarrow} x,\quad y = g^x$$
$$TS\text{ 份额生成: } \sigma_i = H(M)^{x_i}, \text{广播}$$
$$TS\text{ 重建: } \sigma = \prod_{i\in R} \sigma_i^{L_i}, \quad L_i = \prod_{j\in R\setminus\{i\}} \frac{-j}{i-j}$$
$$验证份额: \mathcal{V}_{DDH}(g, B_i, H(M), \sigma_i) \stackrel{?}{=} 1 \quad (B_i = g^{x_i})$$
> 作用：利用 Lagrange 插值合并份额，无需交互。

**MGS 多重签名**
$$MS: \sigma_j = H(M)^{x_j},\quad \sigma = \prod_{j\in J} \sigma_j$$
$$MV: pk_L = \prod_{j\in J} y_j,\quad \mathcal{V}_{DDH}(g, pk_L, H(M), \sigma) \stackrel{?}{=} 1$$
> 作用：聚合签名等于哈希值的指数和，验证时聚合公钥。

**BGS 盲签名**
$$用户: \overline{M} = H(M) \cdot g^r,\quad r \xleftarrow{\$} \mathbb{Z}_p^*$$
$$签名者: \overline{\sigma} = (\overline{M})^x$$
$$用户: \sigma = \overline{\sigma} \cdot y^{-r} = H(M)^x$$
> 作用：随机化消息使签名者无法获知原始消息。

### 实验结果

本文为理论密码学论文，未提供实验数据。但文中指出所有方案的计算开销极低：阈值签名中份额生成与 GS 签名相同（一次指数运算），签名重建仅需 $t+1$ 次乘法；多重签名中份额生成与 GS 签名相同，聚合为 $|L|-1$ 次乘法，验证为一次 DDH 判定（可通过双线性对高效实现）；盲签名中用户计算一次指数运算和一次求逆，签名者一次指数运算。签名长度均为单个群元素（约 160 位）。通信轮次方面，阈值和多重签名仅需一轮广播，盲签名为两轮交互。由于缺少实际实现，无法给出具体运行时间数值。

### 局限性与开放问题

本文的所有安全证明均依赖随机预言模型，虽然此模型在实践中被广泛接受，但存在理论上的局限性。另外，多重签名方案 MGS 的鲁棒性仅被提及可以添加，但并未详细证明；容错阈值 $t<n/2$ 在同步模型中是最优的，但在异步模型中可能需要调整。盲签名方案 BGS 的安全性归约到 Chosen‑Target CDH 问题，该问题的困难性尚未被充分研究，且等价性证明仍缺失。此外，如何将方案扩展到标准模型或基于更标准假设仍有待探索。

### 强关联论文

[8] Boneh et al. Short signatures from the Weil pairing. **Asiacrypt 2001** [Google Scholar](https://scholar.google.com/scholar?q=Short+signatures+from+the+Weil+pairing)
[21] Gennaro et al. Robust threshold DSS signatures. **Eurocrypt 1996** [Google Scholar](https://scholar.google.com/scholar?q=Robust+threshold+DSS+signatures)
[22] Gennaro et al. Secure distributed key generation for discrete-log based cryptosystems. **Eurocrypt 1999** [Google Scholar](https://scholar.google.com/scholar?q=Secure+distributed+key+generation+for+discrete-log+based+cryptosystems)
[44] Shoup. Practical threshold signatures. **Eurocrypt 2000** [Google Scholar](https://scholar.google.com/scholar?q=Practical+threshold+signatures)
[33] Micali et al. Accountable-subgroup multisignatures. **ACM CCS 2001** [Google Scholar](https://scholar.google.com/scholar?q=Accountable-subgroup+multisignatures)
[2] Bellare et al. The One-More-RSA-Inversion Problems and the security of Chaum's Blind Signature Scheme. **Financial Cryptography 2001** [Google Scholar](https://scholar.google.com/scholar?q=The+One-More-RSA-Inversion+Problems+and+the+security+of+Chaum%27s+Blind+Signature+Scheme)
[26] Herzberg et al. Proactive secret sharing, or: How to cope with perpetual leakage. **Crypto 1995** [Google Scholar](https://scholar.google.com/scholar?q=Proactive+secret+sharing+or+How+to+cope+with+perpetual+leakage)
[25] Herzberg et al. Proactive public key and signature systems. **ACM CCS 1997** [Google Scholar](https://scholar.google.com/scholar?q=Proactive+public+key+and+signature+systems)


## 关键词

+ 阈值签名
+ 多重签名
+ 盲签名
+ Gap Diffie-Hellman群
+ GDH签名方案
+ 主动安全性