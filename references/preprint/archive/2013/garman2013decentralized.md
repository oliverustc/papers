---
title: "Decentralized anonymous credentials"
标题简称:
论文类型: preprint
预印本简称: archive
发表年份: 2013
created: 2025-05-15 10:34:27
modified: 2025-05-15 10:37:16
---

## Decentralized anonymous credentials

## 发表信息

+ [原文链接](https://eprint.iacr.org/2013/622)

## 作者

+ [Christina Garman](Christina%20Garman.md)
+ [Matthew Green](Matthew%20Green.md)
+ [Ian Miers](Ian%20Miers.md)
## 笔记

### 背景与动机
传统匿名凭证系统依赖一个可信的凭证发行者，该发行者是单点故障且易遭受攻击，这在匿名场景中尤其难以检测，导致其在分布式网络如点对点网络中部署困难。现有方案均采用盲签名，需要指定一个中心化的可信方来签署凭证，这限制了系统的鲁棒性和可扩展性。本文旨在填补无法在去中心化环境中构建匿名凭证系统的空白，即消除对可信发行者的依赖，允许由一群互不信任的对等节点按需实例化并运行凭证系统。核心挑战在于如何在无中央权威的情况下确保凭证的不可伪造性、用户匿名性以及防止凭证的重复使用。为此，本文借鉴了电子现金和比特币的分布式交易账本技术，提出一种基于公开可验证的累加器和零知识证明的新型去中心化匿名凭证架构。

### 相关工作

[21] Chaum. Security without identification: transaction systems to make big brother obsolete. **Communications of the ACM 1985** [Google Scholar](https://scholar.google.com/scholar?q=Security+without+identification%3A+transaction+systems+to+make+big+brother+obsolete)
> 核心思路：提出匿名凭证概念，允许用户向组织证明拥有凭证而不泄露身份。
> 局限与区别：方案依赖中央发行者对用户秘密进行签名来实现凭证颁发，本文去除了这个中心化信任假设。

[14] Camenisch, Lysyanskaya. Dynamic accumulators and application to efficient revocation of anonymous credentials. **CRYPTO 2002** [Google Scholar](https://scholar.google.com/scholar?q=Dynamic+accumulators+and+application+to+efficient+revocation+of+anonymous+credentials)
> 核心思路：提出动态累加器及高效的成员关系零知识证明，用于凭证撤销。
> 局限与区别：该累加器在本系统中用于聚合所有已发布凭证而非用于撤销，是本文实现高效匿名证明的核心组件。

[12] Camenisch, Hohenberger, Kohlweiss, Lysyanskaya, Meyerovich. How to win the clonewars: efficient periodic n-times anonymous authentication. **CCS 2006** [Google Scholar](https://scholar.google.com/scholar?q=How+to+win+the+clonewars%3A+efficient+periodic+n-times+anonymous+authentication)
> 核心思路：提出 k-show 匿名凭证，限制凭证可被匿名使用的次数，并能在超限后撤销。
> 局限与区别：本文扩展了该概念到去中心化场景，通过将 VRF 种子嵌入凭证承诺实现去中心化的 k-show功能。

[38] Miers, Garman, Green, Rubin. Zerocoin: Anonymous distributed e-cash from bitcoin. **IEEE S&P 2013** [Google Scholar](https://scholar.google.com/scholar?q=Zerocoin%3A+Anonymous+distributed+e-cash+from+bitcoin)
> 核心思路：提出在比特币上实现去中心化电子现金的协议，使用累加器验证硬币存在性。
> 局限与区别：本文直接借鉴其基于累加器和零知识证明的核心技术思路，特别是 Show 协议中的累积与证明机制，将其应用于凭证系统。

[47] Sander, Ta-Shma. Auditable, anonymous electronic cash (extended abstract). **CRYPTO 1999** [Google Scholar](https://scholar.google.com/scholar?q=Auditable%2C+anonymous+electronic+cash+%28extended+abstract%29)
> 核心思路：提出一种可审计的匿名电子现金方案，其架构对本文去中心化凭证发行有启发作用。
> 局限与区别：该方案未解决凭证发行去中心化问题，本文在其基础上引入了分布式账本作为公共公告板。

[2] Brickell, Camenisch, Chen. Direct anonymous attestation. **CCS 2004** [Google Scholar](https://scholar.google.com/scholar?q=Direct+anonymous+attestation)
> 核心思路：提出 DAA 协议，允许 TPM 在不暴露其身份的情况下证明其平台状态。
> 局限与区别：DAA 需要一个可信的 DAA 权威来颁发群签名私钥，本文的 dDAA 应用移除了这一中心化权威。

[40] Namecoin. Available at http://namecoin.info/.
> 核心思路：基于比特币区块链的去中心化身份系统，用于维护名字到数据的映射。
> 局限与区别：Namecoin 提供了本文所需的分布式公告板原型，但其本身并非匿名凭证系统，本文在其上构建凭证层。

### 核心技术与方案
本文整体框架由一个去中心化、防篡改的追加式公共账本（基于比特币/Namecoin 的区块链）和一组密码学算法构成。系统有三类参与者：用户、代表发行主体的组织（由账本共识替代）和验证者。

**凭证发行（Mint）**：
用户拥有主密钥 $sk$ 并选择一个随机数 $r$，计算一个 Pedersen 承诺作为与组织的假名 $Nym = g_0^r g_1^{sk}$。为申请凭证，用户选取随机数 $r'$，计算凭证向量承诺 $c = g_0^{r'} g_1^{sk} \prod_{i=0}^{m} g_{i+2}^{a_i}$，其中 $a_i$ 为公开属性。用户还需生成一个签名知识 $\pi_M$，证明 $c$ 和 $Nym$ 包含相同的 $sk$。用户将 $(c, \pi_M, attrs, Nym, aux)$ 发布到账本，网络节点执行 MintVerify 验证 $\pi_M$，若有效则接受该凭证。

**凭证展示（Show）**：
当用户向验证者展示凭证时，首先扫描账本获得组织 $O$ 的所有有效凭证集合 $\mathbf{C}_O$。利用基于 Strong RSA 的动态累加器计算累加值 $A = \text{Accumulate}(\mathbf{C}_O)$ 和用户凭证 $c$ 的证人 $\omega = \text{GenWitness}(c, \mathbf{C}_O)$。然后用户生成一个非交互零知识证明 $\pi_S$，证明：1) 她知道一个 $\mathbf{C}_O$ 中的凭证 $c$ 及其证人 $\omega$ 使得 $AccVerify(\omega, c) = 1$；2) 她知道 $c$ 的开口与当前展示假名 $Nym_U^V$ 共享同一主密钥 $sk$。验证者计算 $A$ 并验证 $\pi_S$。由于累加器，证明大小和验证计算量均为 $O(\lambda)$，与凭证总数 $N$ 无关。

**安全性**：
方案依赖 Strong RSA 假设保证累加器的碰撞免性和 Discrete Logarithm 假设保证 Pedersen 承诺的约束性与隐藏性。证明采用理想-现实模拟范式：理想功能由可信第三方维护，现实世界中模拟器通过提取 $\pi_M$ 和 $\pi_S$ 中的知识（利用零知识证明的知识提取器）模拟诚实行为。由于两个证明均使用 Fiat-Shamir 启发式的 Schnorr 证明，在随机预言机模型下是计算零知识的，且承诺约束性将攻击者绑定到唯一 $sk$，从而确保凭证不可伪造和用户匿名性。

### 核心公式与流程

**[凭证生成 (MintCred) 的核心签名知识]**
$$
\pi_M = \mathsf{ZKSoK}[aux]\{(sk, r', r): c = g_0^{r'} g_1^{sk} \prod_{i=0}^{m} g_{i+2}^{a_i} \wedge Nym_U^O = g_0^{r} g_1^{sk}\}
$$
> 作用：证明凭证承诺 $c$ 和假名承诺 $Nym_U^O$ 内嵌了相同的用户主密钥 $sk$，同时隐藏 $sk$。

**[凭证展示 (Show) 的核心成员关系与同一性证明]**
$$
\pi_S = \mathsf{NIZKPoK}\{(sk, \omega, r', c, r, Nym_U^V): \mathsf{AccVerify}((N,u), A, c, \omega)=1 \wedge c = g_0^{r'} g_1^{sk} \prod_{i=0}^{m} g_{i+2}^{a_i} \wedge Nym_U^V = g_0^{r} g_1^{sk}\}
$$
> 作用：证明用户拥有一个属于累加器 $A$ 的凭证 $c$，该凭证与展示假名 $Nym_U^V$ 共享同一 $sk$，同时隐藏 $c$ 的具体身份和 $sk$。

**[基于 Strong RSA 的动态累加器验证]**
$$
\mathsf{AccVerify}((N,u), A, c, \omega) : A' \equiv \omega^{c} \bmod N, \text{ output 1 iff } A' = A, c \text{ is prime}, c \in [\mathcal{A}, \mathcal{B}]
$$
> 作用：核实凭证 $c$ 是否被包含在累加器 $A$ 中，作为成员关系证明的核心。

### 实验结果
实验在一台 2010 年 Mac Pro（2x 2.4GHz 四核 Xeon E5620, 16GB RAM, OSX 10.8.3）上进行，使用 OpenMP 并行化，所有操作重复 500 次取平均值。核心性能瓶颈在于 Show 协议中双离散对数证明使用的切割选择技术，需要 80-128 轮次，约 800-1000 次指数运算。在 1024 位 RSA 模数下，单线程操作时间：Mint 1.55s, Show 1.25s, Verify 0.15s, 每 100 次累加 0.68s。多线程利用 OpenMP 后，Show 降至 0.6s, Verify 降至 0.1s，但 OpenSSL 的同步 PRNG 限制了进一步并行化。Show 证明大小约为 51KB（1024 位模数），随模数增大小幅增加至约 54.5KB（3072 位）。累加器更新可增量计算，成本可均摊。系统依赖Namecoin网络，凭证创建需支付约 0.0064 USD 费用，区块平均产生间隔 10 分钟导致约 5 分钟延迟，不适合要求快速确认的场景。

### 局限性与开放问题
首先，系统需要一个高性能、全网一致的分布式账本，账本的安全性依赖于假设诚实方控制多数计算能力，且目前缺乏精确的账本安全模型。其次，凭证展示证明因使用双离散对数证明而偏大（约 50KB），效率有待进一步提升，未来可借助双线性对累加器、水银承诺或格基技术优化。此外，系统需要一个可信的初始设置阶段来生成公共参数，这虽然降低了后期信任要求，但仍是潜在的单点缺陷。

### 强关联论文

[14] Jan Camenisch and Anna Lysyanskaya. Dynamic accumulators and application to efficient revocation of anonymous credentials. **CRYPTO 2002** [Google Scholar](https://scholar.google.com/scholar?q=Dynamic+accumulators+and+application+to+efficient+revocation+of+anonymous+credentials)

[38] I. Miers, C. Garman, M. Green, and A. Rubin. Zerocoin: Anonymous distributed e-cash from bitcoin. **IEEE S&P 2013** [Google Scholar](https://scholar.google.com/scholar?q=Zerocoin%3A+Anonymous+distributed+e-cash+from+bitcoin)

[12] Jan Camenisch, Susan Hohenberger, Markulf Kohlweiss, Anna Lysyanskaya, and Mira Meyerovich. How to win the clonewars: efficient periodic n-times anonymous authentication. **CCS 2006** [Google Scholar](https://scholar.google.com/scholar?q=How+to+win+the+clonewars%3A+efficient+periodic+n-times+anonymous+authentication)

[47] Tomas Sander and Amnon Ta-Shma. Auditable, anonymous electronic cash (extended abstract). **CRYPTO 1999** [Google Scholar](https://scholar.google.com/scholar?q=Auditable%2C+anonymous+electronic+cash+%28extended+abstract%29)

[2] Ernie Brickell, Jan Camenisch, and Liqun Chen. Direct anonymous attestation. **CCS 2004** [Google Scholar](https://scholar.google.com/scholar?q=Direct+anonymous+attestation)

[40] Namecoin. Available at http://namecoin.info/.


## 关键词

+ 去中心化匿名凭证系统
+ 无可信颁发者匿名身份断言
+ 区块链分布式账本密码应用
+ 特设网络资源管理
+ 抗女巫攻击隐私保护
+ 电子现金匿名凭证构建