---
title: "Non-interactive Blind Signatures for Random Messages"
doi: 10.1007/978-3-031-30589-4_25
标题简称:
论文类型: conference
会议简称: EUROCRYPT
发表年份: 2023
modified: 2025-04-16 10:20:33
created: 2025-04-09 11:35:00
---
## Non-interactive Blind Signatures for Random Messages

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-30589-4_25)

## 作者

+ [Lucjan Hanzlik](Lucjan%20Hanzlik.md)

## 笔记

### 背景与动机
盲签名是David Chaum引入的基础密码学原语，允许签名者在不知晓消息内容的情况下对消息签名，广泛应用于电子现金、隐私通行证（Privacy Pass）和匿名凭证等场景。在电子现金和隐私通行证等应用中，用户选择的签名消息可以是完全随机的，无需遵循特定分布，而现有盲签名方案为满足“交互性”和“消息由用户指定”的通用安全模型，往往需要双方进行在线交互、用户保持状态，这在批量颁发或非交互式分发场景中效率低下。鉴于此，本文提出非交互式盲签名（NIBS），利用“消息随机”这一事实，允许签名者在获得接收者公钥后离线生成预签名，接收者再秘密完成最终签名，从而消除在线交互，为加密货币空投、告密者系统、彩票等新应用提供更高效的隐私保护手段。

### 相关工作

[10] Boldyreva. Threshold signatures, multisignatures and blind signatures based on the Gap-Diffie-Hellman-Group signature scheme. **PKC 2003** [Google Scholar](https://scholar.google.com/scholar?q=Threshold+signatures%2C+multisignatures+and+blind+signatures+based+on+the+Gap-Diffie-Hellman-Group+signature+scheme)
> 核心思路：提出基于BLS签名的两轮盲签名方案，利用双线性对实现紧凑签名。
> 局限与区别：需要用户与签名者交互，第一轮用户消息不能重用，且一轮只能产生一个签名。

[16] Chaum. Blind signatures for untraceable payments. **CRYPTO 1982** [Google Scholar](https://scholar.google.com/scholar?q=Blind+signatures+for+untraceable+payments)
> 核心思路：引入盲签名概念，利用RSA的交换性实现盲化。
> 局限与区别：交互式方案，用户需保持状态以去除盲化因子，且签名消息由用户选择。

[17] Davidson et al. Privacy pass: bypassing internet challenges anonymously. **PoPETs 2018** [Google Scholar](https://scholar.google.com/scholar?q=Privacy+pass%3A+bypassing+internet+challenges+anonymously)
> 核心思路：使用盲签名（OPRF）构建一次性令牌，用于在匿名网络中绕过CAPTCHA。
> 局限与区别：用户必须在线参与每次令牌颁发，不能批量离线生成，也无法实现加密货币空投式分发。

[24] Fuchsbauer et al. Structure-preserving signatures on equivalence classes and constant-size anonymous credentials. **J. Cryptol. 2018** [Google Scholar](https://scholar.google.com/scholar?q=Structure-preserving+signatures+on+equivalence+classes+and+constant-size+anonymous+credentials)
> 核心思路：提出SPS-EQ方案，支持对向量$(g, g^x)$进行签名，并允许通过随机指数$r$转化为对$(g^r, g^{rx})$的有效签名。
> 局限与区别：原始方案未设计成非交互式盲签名；本文创新性地将其用于NIBS构造，利用等价类适应性实现盲化。

[28] Hanzlik and Slamanig. With a little help from my friends: constructing practical anonymous credentials. **CCS 2021** [Google Scholar](https://scholar.google.com/scholar?q=With+a+little+help+from+my+friends%3A+constructing+practical+anonymous+credentials)
> 核心思路：提出标记化等价类签名（TBEQ），在SPS-EQ基础上支持签名附加不变标签。
> 局限与区别：本文将其扩展为TNIBS，在保留非交互性的同时支持签名携带时间戳等标签信息。

[38] Pass. Limits of provable security from standard assumptions. **STOC 2011** [Google Scholar](https://scholar.google.com/scholar?q=Limits+of+provable+security+from+standard+assumptions)
> 核心思路：指出两轮盲签名不可能从标准假设仅依赖ROM或CRS构造。
> 局限与区别：该不可能性针对消息由用户选择的盲签名；由于NIBS中消息由协议输出而非用户选择，可能绕过该限制。

### 核心技术与方案
本文构造的核心思想是“消息由最终确定过程随机生成”，因此无需交互。签名者使用SPS-EQ(或TBEQ) 对向量$(pk_R, H(nonce))$进行签名，生成预签名psig。接收者持有私钥$sk_R$，通过chgRep操作将psig转化为对“规范代表”$(g, H(nonce)^{sk_R^{-1}})$的有效签名sig。输出最终签名$(m = H(nonce)^{sk_R^{-1}}, sig)$。该构造利用了SPS-EQ的完美适应性：chgRep输出的签名在消息空间上均匀分布，且与消息独立，保证了盲性。安全性基于三个假设：逆DDH(Inv-DDH)保证接收者盲性——攻击者无法区分$H(nonce)^{sk_R^{-1}}$与随机元素；强DDH(SDDH)保证nonce盲性——同一公钥下不同nonce产生的签名不可链接；SPS-EQ的EUF-CMA安全性保证一次不可伪造——每个NIBS签名对应于一个新的等价类，从而构成SPS-EQ伪造。对于TNIBS，只需将SPS-EQ替换为TBEQ，标签$\tau$不变，支持时限、轮次等附加信息。此外，本文还给出了通用构造：使用VRF作为随机消息源，用标准签名构造预签名，用DMWI证明系统证明预签名与VRF求值的正确性。通用构造的通信复杂度为$O(1)$（用户侧）和$O(n)$（签名者侧，$n$为令牌数），安全依赖DMWI的隐藏/绑定模式及VRF的独特性。

### 核心公式与流程

**SPS-EQ构造的NIBS（Scheme 1）**
$$$$  // 此处使用空公式，由于内容中是整体协议，最好在描述中用文字，或者用多个公式块
> 作用：定义NIBS的密钥生成、预签名颁发、最终签名获取及验证的全流程。关键步骤：签名者用SPS-EQ对$(pk_R, H(nonce))$签名生成psig；接收者用$sk_R^{-1}$调用ChgRep得到对$(g, H(nonce)^{sk_R^{-1}})$的签名。

**一次不可伪造性（Theorem 1）**
$$ \mathbf{Adv}_{\mathcal{A},\text{NIBS}}^{\text{OM-UNF}} = \Pr[\text{OM-UNF}_{\mathcal{A},\text{NIBS}}(\lambda) = 1] $$
> 作用：定义敌手在给定$q$次预签名查询后输出$q+1$个有效消息-签名对的优势。证明通过归约到SPS-EQ的EUF-CMA安全：每个有效NIBS签名对应一个不同的等价类，构成SPS-EQ伪造。

**接收者盲性（Theorem 2）**
$$ \mathbf{Adv}_{\mathcal{A},\text{NIBS}}^{\text{RBnd}} = |\Pr[\text{RBnd}_{\mathcal{A},\text{NIBS}}(\lambda) = 1] - 1/2| $$
> 作用：定义恶意签名者无法区分两个不同接收者最终签名的优势。证明通过编程随机预言机$H$，利用Inv-DDH假设将消息$m$替换为与接收者公钥无关的随机值，再利用SPS-EQ完美适应性重签。

**Nonce盲性（Theorem 3）**
$$ \mathbf{Adv}_{\mathcal{A},\text{NIBS}}^{\text{NBnd}} = |\Pr[\text{NBnd}_{\mathcal{A},\text{NIBS}}(\lambda) = 1] - 1/2| $$
> 作用：定义恶意签名者无法将同一接收者下两个不同nonce的最终签名链接回原始nonce的优势。证明通过SDDH假设，将$m_0$替换为与$nonce_0$无关的值。

**TBEQ构造的TNIBS（Scheme 2）**
$$  // 同样，无独立公式，需在描述中体现
> 作用：在NIBS基础上引入标签$\tau$，签名者用TBEQ对$(pk_R, H(nonce))$加$\tau$签名；接收者ChgRep后，$\tau$保持不变。安全性归约到TBEQ的EUF-CMA及Inv-DDH/SDDH。

**通用构造（Scheme 3）**
$$ \begin{aligned}
\mathcal{R}((m, pk), (nonce, psig, pk_R, \pi_{\text{VRF}}, r)): &\quad H_{\text{crs}}(1) = \text{DMWI.Setup}(\lambda, \text{binding}; r) \\
&\quad \vee (\text{VRF.V}(pk_R, \pi_{\text{VRF}}, nonce, m) = 1 \\
&\quad \wedge \text{SIG.Verify}(pk, (pk_R, nonce), psig) = 1)
\end{aligned} $$
> 作用：定义DMWI证明的NP关系。最终签名是满足“存在有效的预签名和VRF验证”的证明，消息$m$为VRF输出。

### 实验结果
本文未提供传统意义上的实验性能数据，而是在Table 1中对几种盲签名方案的通信复杂度和公钥大小进行了理论对比。以BLS12-381参数（381位素数）为例，NIBS的签名大小为$|m| + |sig| = 382 + 1527 = 1909$位（其中$|m|=382$位为$\mathbb{G}_1$元素，$|sig|=1527$位为两个$\mathbb{G}_1$元素加一个$\mathbb{G}_2$元素），公钥大小为1526位（两个$\mathbb{G}_2$元素）。与盲BLS（签名大小510位，公钥3072位）相比，NIBS公钥更小但签名更大，主要优势在于用户侧首轮消息可重用，且无需在线交互。与Privacy Pass方案（签名大小385位，公钥257位）相比，NIBS虽签名较大，但支持首消息重复使用。TNIBS签名大小为2800位，公钥同样为1526位。所有对比的基线（盲BLS、Privacy Pass、RSA）均不支持首消息重用。适用规模：参数随令牌数$n$线性增长，但用户侧通信量固定。

### 局限性与开放问题
主要开放问题是设计无需双线性对的NIBS方案，因为目前的高效实例化依赖于配对的SPS-EQ，而通用构造使用一般性NP证明系统效率低下。另一个方向是后量子安全的NIBS。从理论上看，Fischlin-Schröder的不可能性结果是否适用于NIBS尚不明确，因为NIBS中的消息是协议输出而非用户选择，可能绕过对“消息可控”的要求，这为从标准假设构造NIBS留有可能空间。

### 强关联论文

[10] Boldyreva. Threshold signatures, multisignatures and blind signatures based on the Gap-Diffie-Hellman-Group signature scheme. **PKC 2003** [Google Scholar](https://scholar.google.com/scholar?q=Threshold+signatures%2C+multisignatures+and+blind+signatures+based+on+the+Gap-Diffie-Hellman-Group+signature+scheme)

[16] Chaum. Blind signatures for untraceable payments. **CRYPTO 1982** [Google Scholar](https://scholar.google.com/scholar?q=Blind+signatures+for+untraceable+payments)

[17] Davidson et al. Privacy pass: bypassing internet challenges anonymously. **PoPETs 2018** [Google Scholar](https://scholar.google.com/scholar?q=Privacy+pass%3A+bypassing+internet+challenges+anonymously)

[24] Fuchsbauer et al. Structure-preserving signatures on equivalence classes and constant-size anonymous credentials. **J. Cryptol. 2018** [Google Scholar](https://scholar.google.com/scholar?q=Structure-preserving+signatures+on+equivalence+classes+and+constant-size+anonymous+credentials)

[27] Hanser and Slamanig. Structure-preserving signatures on equivalence classes and their application to anonymous credentials. **ASIACRYPT 2014** [Google Scholar](https://scholar.google.com/scholar?q=Structure-preserving+signatures+on+equivalence+classes+and+their+application+to+anonymous+credentials)

[28] Hanzlik and Slamanig. With a little help from my friends: constructing practical anonymous credentials. **CCS 2021** [Google Scholar](https://scholar.google.com/scholar?q=With+a+little+help+from+my+friends%3A+constructing+practical+anonymous+credentials)

[32] Hendrickson et al. Rate-limited token issuance protocol. **IETF Internet-Draft 2022** [Google Scholar](https://scholar.google.com/scholar?q=Rate-limited+token+issuance+protocol)

[35] Lysyanskaya. Security analysis of RSA-BSSA. **ePrint 2022/895** [Google Scholar](https://scholar.google.com/scholar?q=Security+analysis+of+RSA-BSSA)

[38] Pass. Limits of provable security from standard assumptions. **STOC 2011** [Google Scholar](https://scholar.google.com/scholar?q=Limits+of+provable+security+from+standard+assumptions)

[40] Pointcheval and Stern. Provably secure blind signature schemes. **ASIACRYPT 1996** [Google Scholar](https://scholar.google.com/scholar?q=Provably+secure+blind+signature+schemes)


## 关键词

+ 非交互式盲签名
+ 随机消息盲签名
+ 等价类签名
+ 匿名代币空投
+ 预签名机制