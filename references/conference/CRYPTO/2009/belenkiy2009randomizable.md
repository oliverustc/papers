---
title: Randomizable proofs and delegatable anonymous credentials

标题简称: 
论文类型: conference
会议简称: CRYPTO
发表年份: 2009
created: 2025-05-23 01:24:40
modified: 2025-05-26 05:05:25
tags:
  - 需要调研引用文献
---

## Randomizable proofs and delegatable anonymous credentials

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-642-03356-8_7)

## 作者

+ Mira Belenkiy
+ [Jan Camenisch](Jan%20Camenisch.md)
+ [Melissa Chase](Melissa%20Chase.md)
+ [Markulf Kohlweiss](Markulf%20Kohlweiss.md)
+ [Anna Lysyanskaya](Anna%20Lysyanskaya.md)
+ [Hovav Shacham](Hovav%20Shacham.md)
## 笔记

### 背景与动机
在现实世界的访问控制中，权限的委托是常见需求，例如系统管理员将权限委托给版主，版主再委托给普通用户。然而，在密码学领域，如何构造一个高效的、可委托的匿名凭证系统一直是一个挑战。现有的非委托匿名凭证方案无法直接扩展以支持委托，因为直接传递签名会泄露委托链中所有用户的身份。Chase 和 Lysyanskaya 在 CRYPTO 2006 提出的首个可委托匿名凭证方案 [CL06] 存在严重的效率瓶颈，其存储和验证证明所需的空间随委托链长度 L 指数级增长，达到 $k^{\Omega(L)}$，其中 k 是安全参数，导致该方案只能处理非常短的委托链。本文的主要贡献在于填补了这一空白，提出了第一个高效的可委托匿名凭证系统。该方案使得用户能够从任何权威机构匿名且不可关联地获取凭证，并将其委托给其他用户，最终证明自己拥有距给定权威机构 L 层的凭证，而证明的大小和计算时间仅为 $O(Lk)$，其中 k 是安全参数。

### 相关工作

[CL06] Chase et al. On Signatures of Knowledge. **CRYPTO 2006** [Google Scholar](https://scholar.google.com/scholar?q=On+Signatures+of+Knowledge)
> 核心思路：利用针对 NP 完全语言的非交互证明构造了首个可委托匿名凭证系统。
> 局限与区别：其构造需要的证明大小呈指数级增长，即 $k^{\Omega(2^L)}$，因此仅能处理常数长度的委托链。本文通过引入随机化证明的概念，将复杂度降为 $O(Lk)$。

[Bar01] Barak. Delegatable Signatures. **Weizmann Institute of Science 2001** [Google Scholar](https://scholar.google.com/scholar?q=Delegatable+Signatures)
> 核心思路：提出了一个通用的（但低效的）委托签名方案，允许签名者将特定消息空间的签名权委托给他人。
> 局限与区别：该方案的目标是使委托生成的签名与原始签名不可区分，而本文要求不同层级的凭证必须清晰可辨。此外，该定义未考虑委托人与被委托人之间的匿名性，而本文则将其作为核心要求。

[GS08] Groth et al. Efficient Non-interactive Proof Systems for Bilinear Groups. **EUROCRYPT 2008** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+Non-interactive+Proof+Systems+for+Bilinear+Groups)
> 核心思路：提出了基于双线性映射的高效非交互零知识证明系统，可用于证明配对乘积方程的解。
> 局限与区别：该证明系统本身不提供随机化性质。本文的核心技术贡献在于向该证明系统添加了一个随机化算法，使其成为可随机化的 NIZK 证明系统，这是构建可委托凭证的关键。

[BCKL08] Belenkiy et al. P-signatures and Non-interactive Anonymous Credentials. **TCC 2008** [Google Scholar](https://scholar.google.com/scholar?q=P-signatures+and+Non-interactive+Anonymous+Credentials)
> 核心思路：提出了基于伪签名（P-signatures）的匿名凭证系统，并定义了 f-可提取性。
> 局限与区别：该系统不支持凭证的委托。本文在构建可委托凭证时，利用了其定义的部分可提取非交互知识证明（NIPK）和 f-可提取性概念，但将核心从签名转移到了可随机化的证明上。

[DSY90] De Santis et al. Cryptographic Applications of the Non-interactive Meta-proof and Many-prover Systems. **CRYPTO 1990** [Google Scholar](https://scholar.google.com/scholar?q=Cryptographic+Applications+of+the+Non-interactive+Meta-proof+and+Many-prover+Systems)
> 核心思路：提出了元证明的概念，即任何持有某个命题证明的人都可以生成一个证明，表明存在一个关于该命题的证明。
> 局限与区别：元证明生成的证明与原证明在形式上不同，而本文需要的是随机化后的证明与原证明不可区分。同时，我们的随机化允许改变证明所针对的陈述本身（如承诺中的随机数），这是元证明无法做到的。

[BB04] Boneh et al. Short Signatures Without Random Oracles. **EUROCRYPT 2004** [Google Scholar](https://scholar.google.com/scholar?q=Short+Signatures+Without+Random+Oracles)
> 核心思路：提出了基于双线性映射的短签名方案，签名具有 $\sigma = g^{1/(sk+m)}$ 的形式。
> 局限与区别：该方案不满足认证安全性，因为 $\mathsf{Sign}_{sk}(m) = \mathsf{Sign}_{m}(sk)$。本文通过引入中间密钥构造了一个 F-不可伪造且满足认证安全的消息认证方案，作为构建可委托凭证的基础。

### 核心技术与方案

本文的整体框架是彻底重新思考匿名凭证的构造方法，将随机化零知识证明系统识别为关键构建块。方案不再让委托人直接传递签名，而是传递一个关于该签名的非交互知识证明。系统由两大核心模块组成：随机化 NIZK 证明系统和基于此的可委托匿名凭证系统。

**1. 随机化 NIZK 证明系统**
该模块是对 Groth-Sahai 证明系统 [GS08] 的扩展。其核心思想是，给定一个关于某个实例 y 的证明 π，任何第三方（无需知道原始证据 w）都可以运行算法 RandProof 生成一个新证明 π'，且该新证明与由原始证据重新生成的证明在计算上不可区分。该随机化过程通过线性代数操作实现：
- 首先，将证明中包含的承诺 $c_m$ 和 $d_n$ 进行重新随机化，即通过乘以一个随机化的承诺项来改变其随机数。例如，对 $c_m$ 的重新随机化为 $c_m' = c_m \cdot \prod_{i=1}^{I} u_i^{s_{m,i}}$，其中 $s_{m,i}$ 是新选择的随机指数。
- 然后，相应地调整证明中的其他部分（$\pi_i$ 和 $\psi_j$），确保新的承诺和新的证明依然满足验证方程。此过程需要计算 $\hat{s}_{q,i} = \sum_m s_{m,i} \cdot \alpha_{q,m}$ 并更新 $\pi_i' = \pi_i \cdot \prod_{q} (D_{q}')^{\hat{s}_{q,i}}$。
- 最后，还需要一个额外的步骤（使用 $t_{i,j}$ 和 $t_h$）来完全随机化证明的分布，使其与一个诚实的重证明在统计上不可区分。

为了满足匿名凭证的需求，该系统还被扩展为 Y-可塑的，即能够更改证明所针对的陈述本身。具体地，给定证据 w 中的秘密值 x 及其承诺 C，算法 $P_s$ 能够将关于 C 的证明转换为关于一个新的承诺 $C' = \text{Commit}(x, open + open')$ 的证明，其中 $s = open'$。这允许用户在展示凭证时生成一个与原始伪名完全无关的新伪名。

**2. 可委托匿名凭证系统**
该构造将随机化 NIZK 与一个 F-不可伪造且满足认证安全的消息认证方案相结合。系统中的每个用户 U 拥有一个秘密密钥 $sk_U$，并可以通过使用随机数 open 计算承诺 $Nym_U = \text{Commit}(sk_U, open)$ 来生成任意数量的伪名。用户的凭证 cred 本质上是一个特定形式的 NIZKPK，证明其知晓某个认证链。该链由一系列认证标签 $(auth_1, ..., auth_L)$ 组成，其中 $auth_i$ 是用户 $sk_{i-1}$ 对 $(sk_i, r_i)$ 的认证，$r_i = H(Nym_O, i)$ 是一个与权威和层级绑定的标签，防止链的混合匹配。

核心操作如下：
- **凭证获取与发放（Issue/Obtain）**：当委托人 I（拥有凭证 cred）向用户 U 发放一个 L+1 级凭证时，双方运行一个安全的双方计算协议。协议输出一个证明 $\pi$，证明 $sk_I$ 对 $(sk_U, r_{L+1})$ 进行了认证。同时，委托人 I 使用 CredProve 对自身凭证生成一个随机化后的证明 credproof_I。最终用户 U 将两个证明拼接并投影，得到凭证 $cred_U = credproof_I \circ \pi$。
- **凭证展示（CredProve）**：用户 U 使用 RandProof 算法对其凭证 cred 进行随机化，并同时使用 $P_s$ 算法将承诺从确定性的 $S_U = \text{Commit}(sk_U, 0)$ 随机化为一个伪名 $Nym_U = \text{Commit}(sk_U, open_U)$。输出 credproof。
- **安全性**：方案的匿名性依赖于随机化证明的不可区分性，使得每次凭证展示或委托都无法关联到同一用户的其他操作。不可伪造性依赖于认证方案的 F-不可伪造性和认证安全性，以及 hash 函数的抗碰撞性，确保用户无法将从不同链中提取的认证片断进行拼接。系统的复杂度：对于长度为 L 的链，凭证存储和证明生成与验证的计算复杂度均为 $O(Lk)$。

### 核心公式与流程

**[随机化 NIZK 定义]**
$$Pr[params \leftarrow \mathsf{Setup}(1^k); (y, w, \pi, state) \leftarrow \mathcal{A}_1(params); \pi_0 \leftarrow \mathsf{Prove}(params, y, w); \pi_1 \leftarrow \mathsf{RandProof}(params, y, \pi); b \leftarrow \{0,1\}; b' \leftarrow \mathcal{A}_2(state, \pi_b): R_L(y, w) \wedge \mathsf{VerifyProof}(params, y, \pi)=1 \wedge b=b'] \leq 1/2 + \nu(k)$$
> 作用：定义了随机化证明系统的核心安全属性。该性质保证了，即使攻击者可以任意选择实例和用于随机化的输入证明，也无法区分一个通过 $\mathsf{RandProof}$ 算法产生的证明和一个通过 $\mathsf{Prove}$ 算法从证据重新生成的证明。这是实现匿名和不可关联性的基础。

**[委托凭证的 Issue/Obtain 协议输出]**
$$\pi \leftarrow \mathsf{NIZKPK}[sk_I \text{ in } Nym_I; sk_U \text{ in } S_U; auth] \{ (F(sk_I), F(sk_U), auth): \mathsf{VerifyAuth}(params_A, sk_I, (sk_U, r_{L+1}), auth)=1 \}$$
> 作用：描述了在主协议中，委托双方共同计算得到的新凭证 $\pi$ 的本质。它是一个非交互零知识知识证明，证明了用户 U 的确定性伪名 $S_U$ 中的密钥 $sk_U$ 与委托者 I 的伪名 $Nym_I$ 中的密钥 $sk_I$ 存在一个合法的认证关系。$r_{L+1}$ 是该层级的标签。

**[随机化 Groth-Sahai 承诺的步骤]**
$$c_m' = c_m \cdot \prod_{i=1}^{I} u_i^{s_{m,i}}$$
$$d_n' = d_n \cdot \prod_{j=1}^{J} v_j^{z_{n,j}}$$
$$\pi_i' = \pi_i \cdot \prod_{q=1}^{Q} (D_q')^{\hat{s}_{q,i}}$$
$$\psi_j' = \psi_j \cdot \prod_{q=1}^{Q} (C_q)^{\hat{z}_{q,j}}$$
> 作用：这是 $\mathsf{RandProof}$ 算法中的核心步骤，展示了如何对 Groth-Sahai 证明进行随机化。首先选择随机指数 $s_{m,i}$ 和 $z_{n,j}$，用它们来重新随机化内部的承诺 $c_m$ 和 $d_n$ ($c_m', d_n'$)。随后，根据承诺的更新，通过计算 $\hat{s}_{q,i}$ 和 $\hat{z}_{q,j}$ 来更新证明的其他部分 $\pi_i'$ 和 $\psi_j'$，以确保更新后的证明仍然能通过验证。

### 实验结果
本文是一篇理论性的密码学构造论文，并未提供实验性实现或性能基准测试。其核心声称的性能优势在于理论复杂度分析：相较于 Chase 和 Lysyanskaya [CL06] 方案中证书链存储和证明大小的指数级复杂度 $k^{\Omega(L)}$，本方案将复杂度降低为 $O(Lk)$，其中 k 是安全参数，L 是链的长度。这意味着对于非恒定的 L，新方案是首个可行的构造。该结果依赖于双线性群上的 Groth-Sahai 证明系统 [GS08] 和 Boneh-Boyen 签名 [BB04] 的变体，这些基础组件在密码学社区已有成熟的实现。因此，虽然缺乏具体实验数值，但其渐近效率优势是明确且压倒性的，使得可委托匿名凭证从理论可能性变为一个实用的密码学原语。

### 局限性与开放问题
本文关注于实现最大程度的匿名性，但并未深入探讨如何在系统中集成复杂的滥用预防机制，例如全局的可追溯性（除了通过提供提取陷阱门）或特定层级的凭证撤销。作者指出了两个开放方向：利用传统匿名凭证中的滥用预防机制（如有限次展示）可以应用于委托链的最后一级；以及通过将标准化的 sigma 协议证明替换为 Groth-Sahai 证明，可将许多已知的滥用预防机制适配到本方案中，但具体如何安全且高效地实现这些适配仍需进一步研究。

### 强关联论文

[CL06] Chase et al. On Signatures of Knowledge. **CRYPTO 2006** [Google Scholar](https://scholar.google.com/scholar?q=On+Signatures+of+Knowledge)

[GS08] Groth et al. Efficient Non-interactive Proof Systems for Bilinear Groups. **EUROCRYPT 2008** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+Non-interactive+Proof+Systems+for+Bilinear+Groups)

[BCKL08] Belenkiy et al. P-signatures and Non-interactive Anonymous Credentials. **TCC 2008** [Google Scholar](https://scholar.google.com/scholar?q=P-signatures+and+Non-interactive+Anonymous+Credentials)

[BB04] Boneh et al. Short Signatures Without Random Oracles. **EUROCRYPT 2004** [Google Scholar](https://scholar.google.com/scholar?q=Short+Signatures+Without+Random+Oracles)

[Bar01] Barak. Delegatable Signatures. **Weizmann Institute of Science 2001** [Google Scholar](https://scholar.google.com/scholar?q=Delegatable+Signatures)

[BBG05] Boneh et al. Hierarchical Identity Based Encryption with Constant Size Ciphertext. **EUROCRYPT 2005** [Google Scholar](https://scholar.google.com/scholar?q=Hierarchical+Identity+Based+Encryption+with+Constant+Size+Ciphertext)

[GOS06] Groth et al. Perfect Non-interactive Zero Knowledge for NP. **EUROCRYPT 2006** [Google Scholar](https://scholar.google.com/scholar?q=Perfect+Non-interactive+Zero+Knowledge+for+NP)

[DSY90] De Santis et al. Cryptographic Applications of the Non-interactive Meta-proof and Many-prover Systems. **CRYPTO 1990** [Google Scholar](https://scholar.google.com/scholar?q=Cryptographic+Applications+of+the+Non-interactive+Meta-proof+and+Many-prover+Systems)

[LRSW99] Lysyanskaya et al. Pseudonym Systems. **SAC 1999** [Google Scholar](https://scholar.google.com/scholar?q=Pseudonym+Systems)

[CL01] Camenisch et al. Efficient Non-transferable Anonymous Multi-show Credential System with Optional Anonymity Revocation. **EUROCRYPT 2001** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+Non-transferable+Anonymous+Multi-show+Credential+System+with+Optional+Anonymity+Revocation)


## 关键词

+ 可随机化证明Groth-Sahai框架委托凭证
+ 可委托匿名凭证任意深度委托链
+ 匿名凭证重新随机化隐私保护
+ DLIN假设双线性群标准模型安全
+ 匿名委托链无随机预言机证明系统