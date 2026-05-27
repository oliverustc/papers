---
title: "Multi-signatures for ad-hoc and privacy-preserving group signing"
doi: 10.1007/978-3-031-57718-5_7
标题简称:
论文类型: conference
会议简称: PKC
发表年份: 2024
created: 2025-04-17 10:58:08
modified: 2025-04-17 10:59:13
---
## Multi-signatures for ad-hoc and privacy-preserving group signing

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-57718-5_7)

## 作者

+ Anja Lehmann 
+ Cavit Özbay 

## 笔记

### 背景与动机
在区块链等分布式账本中，使用多密钥保护高价值资产是一种常见需求。最初的朴素多签名方案将账户的公钥替换为一个公钥集合，但签名和公钥大小与验证成本与群体大小呈线性关系，效率低下。阈值签名虽效率更高，但存在密钥管理挑战：用户若参与多个群体，需为每个群体管理独立的密钥材料，且需要交互式密钥生成协议，这对终端用户极不友好。多签名方案在实现与阈值签名相同的紧凑性同时，允许用户复用单一长期密钥，提供了更简单的密钥管理和即席群体签名能力。然而，现有所有多签名方案均采用确定性密钥聚合，当密钥在多个群体中被复用时，无法提供任何合理的隐私保护——任何掌握个体公钥的对手都能轻易判断链上聚合公钥对应的签名者集合。本文旨在填补这一空白：在允许密钥复用的多签名场景中，首次形式化定义隐私和不可伪造性，并提出在已知公钥模型下能够同时实现强隐私和强安全性的新型构造。

### 相关工作
[12] Boneh et al. Compact multi-signatures for smaller blockchains. **ASIACRYPT 2018** [Google Scholar](https://scholar.google.com/scholar?q=Compact+multi-signatures+for+smaller+blockchains)
> 核心思路：基于BLS签名的紧凑多签名方案，支持签名聚合但密钥聚合是确定性的。
> 局限与区别：仅满足UNF-1安全性，签名份额可被重用于不同群体；由于确定性密钥聚合，在已知公钥模型下无法提供任何隐私。

[31] Maxwell et al. Simple Schnorr multi-signatures with applications to Bitcoin. **Designs, Codes and Cryptography 2019** [Google Scholar](https://scholar.google.com/scholar?q=Simple+Schnorr+multi-signatures+with+applications+to+Bitcoin)
> 核心思路：MuSig方案，引入密钥聚合算法，将个体签名组合成紧凑的多签名。
> 局限与区别：首次声称聚合公钥能隐藏签名者身份和群体大小，但未在密钥复用场景中正式分析隐私；确定性密钥聚合导致隐私性无法在已知公钥模型下成立。

[11] Boldyreva. Threshold signatures, multisignatures and blind signatures based on the gap-Diffie-Hellman-group signature scheme. **PKC 2003** [Google Scholar](https://scholar.google.com/scholar?q=Threshold+signatures+multisignatures+and+blind+signatures+based+on+the+gap-Diffie-Hellman-group+signature+scheme)
> 核心思路：提出基于BLS的阈值签名方案，支持t-out-of-n结构。
> 局限与区别：需要为每个群体运行交互式密钥生成，不支持长期密钥的跨群体复用。

[24] Komlo et al. FROST: flexible round-optimized schnorr threshold signatures. **SAC 2021** [Google Scholar](https://scholar.google.com/scholar?q=FROST+flexible+round-optimized+schnorr+threshold+signatures)
> 核心思路：基于Schnorr的阈值签名，优化轮次以降低通信复杂度。
> 局限与区别：仍然需要为每个群体进行专用密钥生成，不支持即席群体形成。

[6] Baird et al. Threshold signatures in the multiverse. **IEEE S&P 2023** [Google Scholar](https://scholar.google.com/scholar?q=Threshold+signatures+in+the+multiverse)
> 核心思路：Multi-verse Threshold Signatures (MTS)，允许用户使用单一长期密钥派生多个阈值结构。
> 局限与区别：密钥聚合需要交互，隐私未形式化，仅满足UNF-1级别的弱不可伪造性。

[32] Micali et al. Accountable-subgroup multisignatures. **CCS 2001** [Google Scholar](https://scholar.google.com/scholar?q=Accountable-subgroup+multisignatures)
> 核心思路：定义可问责子群多签名，严格将签名绑定到特定签名者子集。
> 局限与区别：子集作为验证算法输入，无法隐藏签名者身份，不支持任何隐私保护。

[13] Boneh et al. Threshold signatures with private accountability. **CRYPTO 2022** [Google Scholar](https://scholar.google.com/scholar?q=Threshold+signatures+with+private+accountability)
> 核心思路：TAPS方案，在固定群体中实现对外部隐私、对内部可问责。
> 局限与区别：隐私仅针对固定群体内部的子集，不涉及跨群体密钥复用，且验证算法与标准BLS/Schnorr不兼容。

[9] Bellare et al. Chain reductions for multi-signatures and the hbms scheme. **ASIACRYPT 2021** [Google Scholar](https://scholar.google.com/scholar?q=Chain+reductions+for+multi-signatures+and+the+hbms+scheme)
> 核心思路：提出链式归约框架，设计基于哈希的紧凑多签名。
> 局限与区别：密钥聚合仍为确定性，隐私未纳入设计目标。

[33] Nick et al. MuSig2: simple two-round schnorr multisignatures. **CRYPTO 2021** [Google Scholar](https://scholar.google.com/scholar?q=MuSig2+simple+two-round+schnorr+multisignatures)
> 核心思路：改进MuSig为两轮交互，增强实用性。
> 局限与区别：与MuSig一样采用确定性密钥聚合，无法提供隐私保障。

[8] Bellare et al. Better than advertised security for non-interactive threshold signatures. **CRYPTO 2022** [Google Scholar](https://scholar.google.com/scholar?q=Better+than+advertised+security+for+non-interactive+threshold+signatures)
> 核心思路：提出阈值签名不可伪造性分层，将签名份额绑定到特定签名者集合。
> 局限与区别：仅关注不可伪造性，未涉及任何隐私性质。

### 核心技术与方案
本文聚焦于重构多签名方案，使其在已知公钥模型下支持密钥复用并同时提供强隐私与强不可伪造性。技术路径包含三个层面：定义新框架与安全性模型、构造具体方案、分析现有方案。

**新框架：带可验证密钥聚合的多签名（MSvKA）**。针对确定性密钥聚合导致无法实现隐私的根本障碍，本文将密钥聚合算法KAg改为概率性算法，并额外输出一个证明π，同时新增算法VfKAg用于检验聚合公钥apk是否对应公钥集合PK。对外部观察者而言，仅凭apk和PK无法判断关联性；而内部知情者凭π可验证。该变化要求MulSign和Combine算法输入apk和π。该框架还允许将已有的确定性方案（Construction 1）转换为本框架下的实例，只需令π=⊥，VfKAg直接检查确定性聚合是否相等。

**不可伪造性分层与转换**。本文定义了三个层次的不可伪造性：UNF-1（仅消息新鲜）、UNF-2（消息+公钥集合PK新鲜）、UNF-3（消息+PK+apk新鲜）。UNF-3对应于群体不可伪造性，保证签名份额无法跨群体复用。本文证明了UNF-2蕴含UNF-1，UNF-3严格强于UNF-2。更重要的是，给出了从UNF-1提升至UNF-3的通用转换：在签名哈希函数H₀中引入apk作为输入（Construction 2），且此转换要求底层方案满足密钥绑定（攻击者无法找到两个不同PK对应同一apk）。该转换使得任何UNF-1安全的方案，只要满足密钥绑定，即可升级为UNF-3安全。

**隐私框架与已知公钥模型下的不可能性**。本文提出三类隐私性质：完全隐私（FullPriv，聚合签名与标准签名不可区分）、集合隐私（SetPriv，隐藏签名者集合及其规模）、成员隐私（MemPriv，隐藏单个签名者身份）。三者均可定义在已知公钥模型（KPK，攻击者知道所有参与方公钥）和较弱的所有-但-一个公钥模型（AbOPK，至少一个公钥保密）下。本文证明：任何采用确定性密钥聚合的方案都无法在KPK模型下满足任何隐私性质——攻击者可简单比较自算的聚合公钥与挑战公钥即可获胜。这严格证明了现有方案的隐私缺失。

**具体构造**。
*   **randBLS-1**：基于BLS方案，在密钥聚合时引入随机数r；聚合公钥apk = ∏_{pk_i∈PK} pk_i^{H₁(pk_i, PK, r)}，签名组合σ = ∏_{pk_i∈PK} s_i^{H₁(pk_i, PK, r)}，其中每个签名份额s_i = H₀(m)^{sk_i}。验证公式e(σ, ĝ) = e(H₀(m), apk)与标准BLS完全一致。该方案满足UNF-1安全性和FullPriv-KPK完全隐私。安全性基于co-CDH假设和随机预言机模型；隐私性则因r为挑战者私下选择，攻击者未知，使得apk与随机群元素不可区分。

*   **randBLS-2**：在randBLS-1基础上应用UNF-1→UNF-3转换，将签名改为s_i = H₀(apk, m)^{sk_i}，验证式变为e(σ, ĝ) = e(H₀(apk, m), apk)。该方案满足UNF-3安全性、SetPriv-KPK和MemPriv-KPK隐私。密钥绑定性质依赖于随机预言机H₁：每次聚合时r均匀随机，使得两个不同PK映射到同一apk的概率可忽略。

**现有方案分析**。本文在AbOPK模型下分析了BLS-dMS [12]和MuSig [31]的隐私：当至少一个公钥保密时，它们均满足FullPriv-AbOPK。原因是若攻击者不知道所有公钥，则无法自行计算聚合公钥进行比对。本文由此给出了现有方案在弱模型下的隐私确界。

### 核心公式与流程
**randBLS-1 密钥聚合**
$$
\mathsf{KAg}(PK): r \leftarrow \{0,1\}^\lambda, \quad apk \leftarrow \prod_{pk_i \in PK} pk_i^{\mathsf{H}_1(pk_i, PK, r)}, \quad \text{输出 } (apk, \pi:=r).
$$
> 作用：引入随机数r使聚合公钥apk成为概率性输出；π是验证apk归属的关键。

**randBLS-1 签名组合与验证**
$$
\mathsf{Combine}(PK, \pi, \{s_i\}): \sigma \leftarrow \prod_{pk_i \in PK} s_i^{\mathsf{H}_1(pk_i, PK, \pi)}.
$$
$$
\mathsf{Vf}(apk, \sigma, m): e(\sigma, \hat{g}) = e(\mathsf{H}_0(m), apk).
$$
> 作用：签名组合使用与聚合时相同的哈希系数；验证公式与标准BLS签名完全相同，实现与标准的兼容性。

**randBLS-2 签名算法（含密钥前缀）**
$$
\mathsf{MulSign}(sk_i, PK, apk, m): s_i \leftarrow \mathsf{H}_0(apk, m)^{sk_i}.
$$
$$
\mathsf{Vf}(apk, \sigma, m): e(\sigma, \hat{g}) = e(\mathsf{H}_0(apk, m), apk).
$$
> 作用：签名哈希中绑定apk，实现UNF-3安全；验证式与标准BLS不同（需apk参与哈希），但若系统中标准BLS也采用密钥前缀，则外观仍一致。

**MSvKA 不可伪造性游戏（图4）**
$$
\mathsf{Exp}^{\mathsf{MSvKA-UNF-x}}_{\Pi,\mathcal{A}}(\lambda): 
\begin{array}{l}
pp \leftarrow \mathsf{Pg}(1^\lambda), (pk^*, sk^*) \leftarrow \mathsf{Kg}(pp), Q\leftarrow \emptyset\\
(\sigma, m, apk, \pi, PK) \leftarrow \mathcal{A}^{\mathcal{O}^{\mathsf{MulSign}}}(pp, pk^*)\\
\text{若 } \mathsf{Vf}(apk, \sigma, m)=1 \land \mathsf{VfKAg}(PK, apk, \pi)=1 \land pk^*\in PK \land \mathsf{fresh}(m, PK, apk, Q)=1 \text{ 则返回1}
\end{array}
$$
> 作用：统一不可伪造性框架，通过fresh谓词定义三种安全级别。UNF-1: (m, ·, ·)∉Q；UNF-2: (m, PK, ·)∉Q；UNF-3: (m, PK, apk)∉Q。

### 实验结果
本文为理论工作，未提供实验数据。但据分析，randBLS-1与randBLS-2的计算开销与现有BLS多签名方案渐近相同：KAg、Combine、Vf均涉及与群体大小n成线性次数的配对或幂运算，MulSign仅含一次幂运算。与标准BLS签名相比，randBLS-1不需要修改现有验证基础设施，其签名和聚合公钥与标准BLS签名格式完全一致。randBLS-2的验证需将apk纳入哈希输入，若环境中已普遍采用密钥前缀（如许多区块链系统对标准Schnorr/BLS签名也要求密钥绑定），则兼容性无障碍。

### 局限性与开放问题
一个主要限制是UNF-3安全的randBLS-2伴随隐私降级至SetPriv-KPK，无法实现完全隐私，且验证公式不再与标准BLS签名完全相同。未来工作可探索在保持UNF-3安全的同时实现FullPriv-KPK的新构造。另一开放问题是将本框架扩展到支持t-out-of-n阈值结构的设置，同时保留强隐私与密钥复用能力。此外，本文的隐私模型未涵盖内部合谋攻击，设计能抵抗内部追踪的更健壮方案也是一条有价值的研究路线。

### 强关联论文
[12] Boneh et al. Compact multi-signatures for smaller blockchains. **ASIACRYPT 2018** [Google Scholar](https://scholar.google.com/scholar?q=Compact+multi-signatures+for+smaller+blockchains)

[31] Maxwell et al. Simple Schnorr multi-signatures with applications to Bitcoin. **Designs, Codes and Cryptography 2019** [Google Scholar](https://scholar.google.com/scholar?q=Simple+Schnorr+multi-signatures+with+applications+to+Bitcoin)

[11] Boldyreva. Threshold signatures, multisignatures and blind signatures based on the gap-Diffie-Hellman-group signature scheme. **PKC 2003** [Google Scholar](https://scholar.google.com/scholar?q=Threshold+signatures+multisignatures+and+blind+signatures+based+on+the+gap-Diffie-Hellman-group+signature+scheme)

[24] Komlo et al. FROST: flexible round-optimized schnorr threshold signatures. **SAC 2021** [Google Scholar](https://scholar.google.com/scholar?q=FROST+flexible+round-optimized+schnorr+threshold+signatures)

[6] Baird et al. Threshold signatures in the multiverse. **IEEE S&P 2023** [Google Scholar](https://scholar.google.com/scholar?q=Threshold+signatures+in+the+multiverse)

[32] Micali et al. Accountable-subgroup multisignatures. **CCS 2001** [Google Scholar](https://scholar.google.com/scholar?q=Accountable-subgroup+multisignatures)

[13] Boneh et al. Threshold signatures with private accountability. **CRYPTO 2022** [Google Scholar](https://scholar.google.com/scholar?q=Threshold+signatures+with+private+accountability)

[9] Bellare et al. Chain reductions for multi-signatures and the hbms scheme. **ASIACRYPT 2021** [Google Scholar](https://scholar.google.com/scholar?q=Chain+reductions+for+multi-signatures+and+the+hbms+scheme)

[33] Nick et al. MuSig2: simple two-round schnorr multisignatures. **CRYPTO 2021** [Google Scholar](https://scholar.google.com/scholar?q=MuSig2+simple+two-round+schnorr+multisignatures)

[8] Bellare et al. Better than advertised security for non-interactive threshold signatures. **CRYPTO 2022** [Google Scholar](https://scholar.google.com/scholar?q=Better+than+advertised+security+for+non-interactive+threshold+signatures)


## 关键词

+ 多重签名
+ 密钥聚合
+ 隐私保护签名
+ 概率密钥聚合
+ BLS签名
+ 跨群组不可链接性