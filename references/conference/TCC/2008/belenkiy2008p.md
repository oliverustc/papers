---
title: P-signatures and noninteractive anonymous credentials
标题简称: 
论文类型: conference
会议简称: TCC
发表年份: 2008
created: 2025-05-15 10:00:19
modified: 2025-05-15 10:30:28
---

## P-signatures and noninteractive anonymous credentials

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-540-78524-8_20)

## 作者

+ Mira Belenkiy
+ [Melissa Chase](Melissa%20Chase.md)
+ [Markulf Kohlweiss](Markulf Kohlweiss.md)
+ [Anna Lysyanskaya](Anna Lysyanskaya.md)

## 笔记

### 背景与动机
匿名凭证系统允许用户向一个验证者证明其拥有另一个可信方颁发的凭证，同时保证凭证的签发和出示过程不可链接，这是隐私保护认证机制的核心。在这个领域，Camenisch 和 Lysyanskaya 提出的 CL-签名方案 [CL01, CL02, CL04] 是关键的构建模块，它包含两个高效的交互式协议：一个用于在承诺上获取签名（Issue），另一个用于零知识地证明知晓一个对承诺值的签名（Prove）。然而，Prove 协议的交互性是一个瓶颈：它要求证明者和验证者同时在线进行多轮通信，无法适用于离线场景，例如电子现金系统中商家向银行转移硬币的证明。使该协议非交互化的现有方法要么依赖随机谕言模型（Fiat-Shamir 启发式 [FS87]），但其安全性已被证明不能直接推广到标准模型 [CGH04, DNRS03, GK03]；要么使用通用的非交互式零知识证明 [BFM88, DSMP88, BDMP91]，但其代价过于高昂，完全不实用。本文旨在填补这一空白，通过引入一个新的密码学原语——P-签名，并结合 Groth 和 Sahai 的高效非交互式证明系统 [GS07]，首次在标准模型（公共参考串模型）下实现了实用的、非交互式的匿名凭证协议。

### 相关工作
[CL01] Camenisch 等. Efficient Non-transferable Anonymous Multi-show Credential System with Optional Anonymity Revocation. **EUROCRYPT 2001** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+non-transferable+anonymous+multi-show+credential+system+with+optional+anonymity+revocation)
> 核心思路：提出了第一个实用的多出示匿名凭证方案，基于强RSA假设。
> 局限与区别：其底层的 CL-签名方案的所有证明协议都是交互式的。

[CL02] Camenisch 等. A Signature Scheme with Efficient Protocols. **SCN 2002** [Google Scholar](https://scholar.google.com/scholar?q=A+signature+scheme+with+efficient+protocols)
> 核心思路：将CL-签名从RSA群转移到离散对数群，并提供了更高效的协议。
> 局限与区别：仍然依赖交互式证明；本文首次实现了非交互化。

[LRSW99] Lysyanskaya 等. Pseudonym Systems. **EDO 2000** [Google Scholar](https://scholar.google.com/scholar?q=Pseudonym+systems)
> 核心思路：提出了基于LRSW假设的签名方案，该方案及其变体是许多匿名认证协议的基础。
> 局限与区别：其安全证明需要使用交互式协议；本文构造的P-签名基于不同的假设（HSDH, TDH）。

[BB04] Boneh 等. Short Signatures Without Random Oracles. **EUROCRYPT 2004** [Google Scholar](https://scholar.google.com/scholar?q=Short+signatures+without+random+oracles)
> 核心思路：提出了Weak Boneh-Boyen (WBB) 和 Full Boneh-Boyen (FBB) 短签名方案，安全性基于q-SDH假设。
> 局限与区别：本文的第一个构造基于WBB，第二个构造基于一个修改后的FBB变体；我们引入的F-不可伪造性概念及新的假设（HSDH, TDH）是证明这些签名在P-签名框架下安全的关键。

[GS07] Groth 等. Efficient Non-interactive Proof Systems for Bilinear Groups. **EUROCRYPT 2008** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+non-interactive+proof+systems+for+bilinear+groups)
> 核心思路：提出了一个在双线性群中构建高效非交互式证明（NIPK）的通用框架，支持配对乘积方程，并具有f-可提取性和强证人不可区分性。
> 局限与区别：该证明系统是f-可提取的（只能提取组元素），而不是完全可提取的。本文的关键贡献是形式化了f-可提取性，并证明了如何基于此构造安全的P-签名，即需要将签名方案改造为F-安全的。

[BW07] Boyen 等. Full-domain Subgroup Hiding and Constant-size Group Signatures. **PKC 2007** [Google Scholar](https://scholar.google.com/scholar?q=Full-domain+subgroup+hiding+and+constant-size+group+signatures)
> 核心思路：提出了Hidden SDH (HSDH) 假设，用于构造常数大小的群签名方案。
> 局限与区别：本文的第二个P-签名构造的安全性依赖于HSDH假设。

[CLM07] Camenisch 等. Endorsed E-Cash. **IEEE S&P 2007** [Google Scholar](https://scholar.google.com/scholar?q=Endorsed+e-cash)
> 核心思路：提出了另一个基于LRSW签名变体的匿名电子现金方案。
> 局限与区别：其核心的证明技术仍然是交互式的。

[CHL05] Camenisch 等. Compact E-Cash. **EUROCRYPT 2005** [Google Scholar](https://scholar.google.com/scholar?q=Compact+e-cash)
> 核心思路：提出了一种基于CL-签名的紧凑型电子现金系统。
> 局限与区别：同样依赖交互式证明。

### 核心技术与方案
本文的核心是提出了 **P-签名**（具有高效协议的非交互式签名）这一新概念。方案的整体框架是对一个常规的签名方案和一个承诺方案进行扩展，增加了两个关键的算法：ObtainSig/IssueSig（交互式签发协议）和**非交互式**的VerifiableSign/VerifyProof（即 Prove/VerifyProof），以及一个用于证明两个承诺打开到相同值的 EqCommProve 协议。

构造的核心技术基础是 Groth 和 Sahai 的非交互式证明系统 (GS-NIPK)。GS 证明的一个关键特点是它是 **f-可提取的**：如果证明的证物中包含一个群元素 $x$（例如 $h^m$），那么提取器只能提取出 $x$ 本身，而不能提取出它的离散对数 $m$。因此，直接证明“知晓一个签名 $\sigma$ 及其消息 $m$”是不充分的，因为提取器只能得到 $h^m$。为此，本文引入了 **F-安全签名方案** 的概念：签名者对消息 $m$ 签名，而方案的安全性保证了敌手无法伪造一个对 $F(m)$ 的有效签名，其中 $F$ 是一个公开的可高效计算的单射（例如 $F(m) = (h^m, u^m)$）。这样，GS 证明的 f-可提取性就刚好够用：提取器提取出 $F(m)$ 和 $\sigma$，而 $F$-不可伪造性确保了 $m$ 的新鲜性。

作者给出了两个基于双线性映射群的P-签名构造。**第二个构造（也是论文重点详述的）** 如下：
1.  **底层签名方案**：基于 Full Boneh-Boyen 签名 [BB04] 的变体。密钥生成：$\alpha, \beta \leftarrow \mathbb{Z}_p$，公钥 $pk = (v = h^\alpha, w = h^\beta, \tilde{v} = g^\alpha, \tilde{w} = g^\beta)$，私钥 $sk = (\alpha, \beta)$。签名过程：对消息 $m$，选择随机 $r$，计算 $C_1 = g^{1/(\alpha + m + \beta r)}$, $C_2 = w^r$, $C_3 = u^r$，签名 $\sigma = (C_1, C_2, C_3)$。
2.  **签发协议 (ObtainSig/IssueSig)**：用户持有对 $m$ 的承诺 $comm = GSExpCommit(h, m)$；发行者持有私钥。协议通过两方安全计算完成，最终用户获得签名 $\sigma$，而发行者除了承诺本身外，无法获知 $m$。
3.  **证明协议 (Prove/VerifyProof)**：这是核心。用户已知 $(m, \sigma)$，需要构建一个非交互式证明。
    *   **构造承诺**：计算 $M_h = GSExpCommit(h, m)$（这也是最终输出给验证者的 $comm$），$M_u = GSExpCommit(u, m)$，以及对签名三个部分 $\Sigma, R_w, R_u$ 的承诺。
    *   **构造NIPK**：用户使用 GS 证明系统生成一个证明 $\pi$，证明存在打开值满足以下配对乘积方程：
        $$e(C_1, v h^m C_2) = e(g, h) = z \quad \land \quad e(u, C_2) = e(C_3, w) \quad \land \quad m = m$$
        第三个等式实际上是证明 $h^m$ 和 $u^m$ 使用相同的指数 $m$。关键在于，这些方程中的秘密值都是群元素（如 $C_1$、$h^m$、$C_2$），GS 证明可以完美处理。
4.  **安全性**：安全性基于 HSDH [BW07] 和 TDH 假设（一个作者提出的新假设）。证明策略是，若存在一个P-签名伪造者，根据其伪造中 $m + \beta r$ 是否与某次查询相同（类型 I 或 II），可以分别构造一个算法来解决HSDH或TDH挑战。方案实现了完美可靠性（由GS证明的f-可提取性保证）、强证人不可区分性（因此满足零知识性）、以及签发者和用户的隐私（通过两方安全计算的模拟器）。
5.  **效率**：使用 SXDH 实例化时，每个非交互式证明 $\pi$ 包含 18 个 $G_1$ 元素和 16 个 $G_2$ 元素；证明方需执行 34 次多指数运算，验证方需执行 68 次配对运算。使用 DLIN 实例化时则为 42 个 $G_1 = G_2$ 元素。

### 核心公式与流程

**[新签名方案 (New-Sign)]**
$$ \sigma' = (C_1 = g^{1/(\alpha + m + \beta r)}, C_2 = w^{r}, C_3 = u^{r}) $$
> 作用：定义P-签名所基于的F-安全签名方案的签名算法，其中 $m$ 是消息，$(\alpha, \beta)$ 是私钥，$r$ 是随机数。公钥为 $pk = (v = h^\alpha, w = h^\beta, \tilde{v} = g^\alpha, \tilde{w} = g^\beta)$。

**[ObtainSig/IssueSig 协议关键步骤]**
1. 用户选择 $\rho_1, \rho_2 \leftarrow \mathbb{Z}_p$。
2. 发行者选择 $r' \leftarrow \mathbb{Z}_p$。
3. 双方通过安全两方计算，在发行者侧计算 $x = (\alpha + m + \beta \rho_1 r') \rho_2$（若承诺有效），否则 $x = \perp$。
4. 若 $x \neq \perp$，发行者返回 $(C_1' = g^{1/x}, C_2' = w^{r'}, C_3' = u^{r'})$。
5. 用户计算 $C_1 = C_1'^{\rho_2}, C_2 = C_2'^{\rho_1}, C_3 = C_3'^{\rho_1}$，得到最终签名。
> 作用：描述用户如何从发行者处获取对自己消息 $m$ 的签名，同时保证消息 $m$ 对发行者保密。

**[Prove 协议：非交互式零知识证明]**
$$ \pi = \mathsf{NIPK} \{ (\Sigma: C_1), (R_w: C_2), (R_u: C_3), (M_h: h^m), (M_u: u^m) : $$
$$ e(C_1, v h^m C_2) = z \land e(u, C_2) = e(C_3, w) \} $$
> 作用：定义用户如何在知晓签名 $(C_1, C_2, C_3)$ 和消息 $m$ 的情况下，生成一个非交互式证明 $\pi$。证明中，$M_h$ 即是公开的承诺 $comm$。该证明利用了GS证明系统的f-可提取性，验证者仅能接受证明，而提取器只能提取到 $(h^m, u^m)$ 和签名元素。

**[F-不可伪造性 (F-Unforgeabilty) 定义核心]**
$$ \Pr[ \text{VerifySig}(pk, F^{-1}(y), \sigma) = \text{accept} \land y \notin F(Q_{\text{Sign}}) ] < \nu(k) $$
> 作用：正式定义P-签名所需的安全性质。它要求敌手不能输出一个对 $F(m)$ 的有效签名，除非它已经查询过消息 $m$ 的签名。这里 $F$ 是公开的、可高效计算的单射（如 $F(m) = (h^m, u^m)$）。

### 实验结果
论文并未提供标准的实验基准数据（如毫秒级运行时间），而是以密码学原语的理论复杂度给出了具体参数，例如在不同安全假设（SXDH vs. DLIN）下，每个P-签名证明 $\pi$ 的大小、以及证明方和验证方的计算复杂度。具体而言，使用 SXDH 假设时，一个明文证明包含 18 个 $G_1$ 元素和 16 个 $G_2$ 元素，证明方开销为 34 次多指数运算，验证方开销为 68 次双线性配对运算。使用 DLIN 假设时，证明和验算均在同构群 $G_1 = G_2$ 中进行，需 42 个群元素，42 次多指数运算和 84 次配对运算。这些结果表明，本文方案具备实际可部署的潜力，因为双线性配对运算是可实现的且随着硬件加速而优化。

### 局限性与开放问题
第一个P-签名构造（基于Weak Boneh-Boyen）的安全性基于一个非标准的交互式假设（TDH），虽然效率可能更高，但其基础假设的可信度较低。第二个构造虽然使用了更标准的假设（HSDH），但其底层签名是对Full Boneh-Boyen的修改，引入了额外的组元素，增加了通信开销。P-签名的安全模型虽然比CL-签名更强（支持非交互式证明），但定义了一个特殊的“用户隐私”和“签发者隐私”概念，而不是完全通用的安全两方计算安全性，这在某些应用场景下可能是一个限制。将P-签名技术应用于更复杂的隐私保护协议，如可链接的群签名或可监管的电子现金系统，是一个自然但待探索的未来方向。

### 强关联论文

[GS07] Groth 等. Efficient Non-interactive Proof Systems for Bilinear Groups. **EUROCRYPT 2008** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+non-interactive+proof+systems+for+bilinear+groups)

[BB04] Boneh 等. Short Signatures Without Random Oracles. **EUROCRYPT 2004** [Google Scholar](https://scholar.google.com/scholar?q=Short+signatures+without+random+oracles)

[CL02] Camenisch 等. A Signature Scheme with Efficient Protocols. **SCN 2002** [Google Scholar](https://scholar.google.com/scholar?q=A+signature+scheme+with+efficient+protocols)

[CL01] Camenisch 等. Efficient Non-transferable Anonymous Multi-show Credential System with Optional Anonymity Revocation. **EUROCRYPT 2001** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+non-transferable+anonymous+multi-show+credential+system+with+optional+anonymity+revocation)

[CL04] Camenisch 等. Signature Schemes and Anonymous Credentials from Bilinear Maps. **CRYPTO 2004** [Google Scholar](https://scholar.google.com/scholar?q=Signature+schemes+and+anonymous+credentials+from+bilinear+maps)

[BW07] Boyen 等. Full-domain Subgroup Hiding and Constant-size Group Signatures. **PKC 2007** [Google Scholar](https://scholar.google.com/scholar?q=Full-domain+subgroup+hiding+and+constant-size+group+signatures)

[FS87] Fiat 等. How to Prove Yourself: Practical Solutions to Identification and Signature Problems. **CRYPTO 1986** [Google Scholar](https://scholar.google.com/scholar?q=How+to+prove+yourself+practical+solutions+to+identification+and+signature+problems)

[LRSW99] Lysyanskaya 等. Pseudonym Systems. **EDO 2000** [Google Scholar](https://scholar.google.com/scholar?q=Pseudonym+systems)

[CHL05] Camenisch 等. Compact E-Cash. **EUROCRYPT 2005** [Google Scholar](https://scholar.google.com/scholar?q=Compact+e-cash)

[CLM07] Camenisch 等. Endorsed E-Cash. **IEEE S&P 2007** [Google Scholar](https://scholar.google.com/scholar?q=Endorsed+e-cash)


## 关键词

+ P-签名匿名凭证
+ 非交互式匿名凭证系统
+ 双线性映射群密码假设
+ Groth-Sahai证明技术
+ 隐私保护认证机制
+ 承诺方案非交互证明