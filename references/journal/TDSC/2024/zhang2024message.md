---
title: "Message linkable group signature with information binding and efficient revocation for privacy-preserving announcement in VANETs"
标题简称:
论文类型: journal
期刊简称: TDSC
发表年份: 2024
created: 2025-05-13 05:13:44
modified: 2025-05-13 05:14:19
---

## Message linkable group signature with information binding and efficient revocation for privacy-preserving announcement in VANETs

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/10478636)

## 作者

+ Lei Zhang
+ Jiangtao Li
+ Yafang Yang

## 笔记

### 背景与动机
在车载自组织网络（VANET）中，车辆广播的公告消息（如路况、事故信息）对于提升道路安全和交通效率至关重要。然而，恶意车辆可能发送虚假公告误导其他车辆，因此必须确保消息的信任度（trustworthiness）。现有方案通常采用事后（数字签名）和事前（阈值/信誉机制）两种对策来保证信任度，但它们在抵抗女巫攻击（Sybil attack）和合谋攻击（collusive attack）方面存在根本性缺陷。例如，基于阈值的方案（如传统数字签名结合假名、传统群签名）中，若恶意车辆数量超过阈值或单个合谋，即可伪造虚假消息；而基于信誉的方案（PPRBS [21]）虽然能抵抗合谋，但无法抵抗女巫攻击，且一个高信誉节点就能伪造可被接受的消息。现有方案均无法同时实现抗女巫和抗合谋，即无法满足强信任度（Strong Trustworthiness, ST）。本文旨在填补这一空白，提出一种能同时实现车辆隐私、抗重伪名管理问题（HPMP）、抗女巫、抗成员撤销问题（MRP）和抗合扰，从而达成强信任度的隐私保护公告方案。

### 相关工作

[13] Wu 等. Balanced Trustworthiness, Safety, and Privacy in Vehicle-to-Vehicle Communications. **IEEE TVT 2010** [Google Scholar](https://scholar.google.com/scholar?q=Balanced%20Trustworthiness%2C%20Safety%2C%20and%20Privacy%20in%20Vehicle-to-Vehicle%20Communications)
> 核心思路：提出消息可链接群签名（MLGS）用于VANET公告，通过消息可链接性抵抗女巫攻击。
> 局限与区别：该方案存在成员撤销问题且缺乏正式的安全分析，无法绑定签名者的声誉信息，且不具备抗合谋能力。

[35] Boneh 等. Short Group Signatures. **CRYPTO 2004** [Google Scholar](https://scholar.google.com/scholar?q=Short%20Group%20Signatures)
> 核心思路：提出经典的BBS短群签名方案，具备高效的签名和验证能力。
> 局限与区别：传统群签名无法抵抗女巫攻击（签名不可链接），且存在成员撤销问题。

[21] Chen 等. A Privacy-Aware Reputation-Based Announcement Scheme for VANETs. **IEEE WVEC 2013** [Google Scholar](https://scholar.google.com/scholar?q=A%20Privacy-Aware%20Reputation-Based%20Announcement%20Scheme%20for%20VANETs)
> 核心思路：提出隐私保护的信誉公告方案，通过短期信誉证书实现成员高效撤销。
> 局限与区别：该方案无法抵抗女巫攻击，且单个高信誉车辆即可制造虚假可接受消息。

[22] Chen 等. Private Reputation Retrieval in Public — A Privacy-Aware Announcement Scheme for VANETs. **IET Inf. Secur. 2017** [Google Scholar](https://scholar.google.com/scholar?q=Private%20Reputation%20Retrieval%20in%20Public%20%E2%80%94%20A%20Privacy-Aware%20Announcement%20Scheme%20for%20VANETs)
> 核心思路：改进了PPRBS方案，解决了信誉证书更新所需的安全信道问题。
> 局限与区别：仍无法抵抗女巫攻击，且缺乏强信任度。

[2] IEEE Standard for Wireless Access in Vehicular Environments - Security Services for Applications and Management Messages. **IEEE Std 1609.2 2016** [Google Scholar](https://scholar.google.com/scholar?q=IEEE%20Standard%20for%20Wireless%20Access%20in%20Vehicular%20Environments-Security%20Services%20for%20Applications%20and%20Management%20Messages)
> 核心思路：基于传统数字签名（如ECDSA）与假名机制实现车辆隐私和消息认证。
> 局限与区别：面临严重的重伪名管理问题，且无法抵抗女巫攻击。

### 核心技术与方案

本文的核心技术是提出了一种新的密码原语——带信息绑定和高效撤销的消息可链接群签名（MLGSwIB&ER），并以此为基础构建了一个隐私保护公告方案（PASwST）。MLGSwIB&ER是对现有消息可链接群签名的扩展，它解决了既有方案中成员撤销困难以及无法将签名者关联信息（如声誉等级）绑定到签名中的问题。方案的整体架构包括声誉管理器（RM）和群管理员（GM）两个可信中心，以及所有车辆（群成员）。GM负责系统设置、车辆注册和短期声誉证书的颁发；RM负责维护和更新车辆的真实声誉值。

MLGSwIB&ER的构造基于双线性映射和两个密码学假设：在 $(\mathbb{G}_1, \mathbb{G}_2)$ 上的 $q$-强Diffie-Hellman（$q$-SDH）假设和 $\mathbb{G}_1$ 上的决策线性Diffie-Hellman（DLIN）假设。系统设置阶段，GM生成全局公钥 $\mathsf{gpk}=(\pi, u, v, h, w, H_1, H_2, H_3)$ 和主私钥 $\mathsf{gmsk}=(\gamma, \eta_1, \eta_2)$，其中 $u^{\eta_1} = v^{\eta_2} = h$。车辆注册时，GM为其分配成员密钥 $\mathsf{gsk}_b = (A_b, x_b)$，其中 $A_b = g_1^{1/(\gamma+x_b)}$。这是经典的BBS群签名密钥结构。 的新颖之处在于短期密钥生成协议（STKGen）。当车辆请求短期声誉证书时，GM根据其当前声誉等级 $r_{bi}$ 和有效期 $\mathbb{T}_{bi}$ 生成状态消息 $st_{bi}=\mathbb{T}_{bi}||r_{bi}$，并计算短期证书 $rcert_{bi}=H_3(st_{bi})^{1/(\gamma+x_b)}$。车辆收到后验证 $\hat{e}(rcert_{bi}, w \cdot g_2^{x_b}) = \hat{e}(H_3(st_{bi}), g_2)$，若成立则计算 $A_{bi} = A_b \cdot rcert_{bi}$，得到短期密钥 $\mathsf{ssk}_{bi} = (A_{bi}, x_b)$。这样，声誉等级 $r_{bi}$ 就以哈希值 $H_3(\mathbb{T}_{bi}||r_{bi})$ 的形式被“绑定”到了群签名中，并且该证书具有有效期，到期后若声誉等级不足则无法更新，从而实现高效撤销。

在签名阶段（Sign），车辆使用 $\mathsf{ssk}_{bi}$ 对消息 $m$ 生成签名 $\sigma = (T_1, T_2, T_3, t, c, s_\alpha, s_\beta, s_x, s_{\delta_1}, s_{\delta_2})$。其中 link token $t=H_2(m)^{x_b}$ 确保了消息可链接性：任何人均可对比两个签名中的 $t$ 是否相等来判断是否来自同一签名者，从而抵抗女巫攻击。 $T_3 = A_{bi} h^{\alpha+\beta}$ 的结构使得GM可以使用其私钥$(\eta_1, \eta_2)$进行开箱（Open），计算 $A=T_3/(T_1^{\eta_1}T_2^{\eta_2})$ 来追踪签名者身份。在公告方案中，接收方首先收集一组针对相同消息 $m$ 的签名。它使用LinkCheck算法去重（若同一车辆多次签名，只保留一个），然后验证签名有效性（Verify），并使用Verify算法中计算出的 $\bar{g}_1 = g_1 H_3(st_{bi})$ 来获取签名者的当前声誉等级 $r_{bi}$。最后，接收方根据所有声明者的声誉等级进行聚合评估，决定是否接受该消息。此信誉机制确保单个高信誉或多个低信誉车辆无法伪造可被接受的消息，实现了强信任度。

在安全性方面，论文严格定义了MLGSwIB&ER的可追踪性、匿名性和消息可链接性，并给出了形式化证明。可追踪性依赖于 $q$-SDH假设，确保任何无法获得合法成员密钥的敌手无法伪造可被追踪到特定身份的签名。匿名性依赖于DLIN假设，确保攻击者无法区分两个不同成员产生的签名。消息可链接性依赖于 $q$-SDH假设，证明了一个敌手即使知道所有成员的密钥，也无法在不产生相同link token的情况下生成一个能追踪到合法成员的签名。

在复杂度方面，MLGSwIB&ER的签名计算需要2次双线性对运算和14次指数运算，验证需要2次双线性对运算和15次指数运算。签名长度为 $5l_{\mathbb{G}_1} + 5l_{\mathbb{Z}_p}$ 比特。与其他方案（如TGSS, PPRBS）相比，计算和通信开销是可比甚至更优的。

### 核心公式与流程

**[成员密钥生成]**
$$A_b = g_1^{\frac{1}{\gamma + x_b}}$$
> 作用：为车辆生成$q$-SDH对 $(A_b, x_b)$作为其成员密钥，是后续所有操作的基础。

**[短期密钥生成]**
$$rcert_{bi} = H_3(st_{bi})^{\frac{1}{\gamma + x_b}} \quad,\quad A_{bi} = A_b \cdot rcert_{bi}$$
> 作用：通过将声誉等级信息 $st_{bi}$ 嵌入到成员密钥中，实现了声誉等级的“信息绑定”功能。车辆通过验证 $\hat{e}(rcert_{bi}, w \cdot g_2^{x_b}) = \hat{e}(H_3(st_{bi}), g_2)$ 来确保证书的合法性。

**[签名生成（Sign）]**
$$T_3 = A_{bi} h^{\alpha + \beta} \quad,\quad t = H_2(m)^{x_b} \quad,\quad c = H_1(m, T_1, T_2, T_3, R_1, R_2, R_3, R_4, R_5, R_6, t)$$
> 作用：$T_3$ 利用双线性映射和DLIN假设的隐藏结构，隐藏了短期身份 $A_{bi}$；link token $t$ 提供了基于离散对数的不可伪造的可链接性；$c$ 是通过Fiat-Shamir变换产生的挑战值，确保了签名的不可伪造性。

**[开箱（Open）]**
$$A = \frac{T_3}{T_1^{\eta_1} T_2^{\eta_2}}$$
> 作用：GM通过其私钥 $\eta_1, \eta_2$ 直接从签名中恢复出签名者的短期身份 $A$，无需交互，实现了高效的追踪。

**[消息链接检查（LinkCheck）]**
$$\text{LinkCheck}(\mathsf{gpk}, \sigma, \sigma', m) = 1 \iff t = t'$$
> 作用：通过比较两个签名的link token $t$ 是否相等，即可完全抵抗女巫攻击，因为一个诚实才能生成唯一的 $x_b$ 和对应的 $t = H_2(m)^{x_b}$。

### 实验结果
论文通过使用VanetMobisim、ns-3和MIRACL库在Linux（Intel Core i7-8700, 2.4GHz）上进行仿真，实现了128位安全级别的BN曲线。模拟场景为2.0×2.0 km²的城市道路，车辆密度从5到50辆/km²。声誉等级符合正态分布。实验主要评估了三个指标：平均消息验证概率 $P_{msg}$ 和平均消息延迟 $D_{msg}$。结果表明，当平均事件发现概率 $p=30\%$ 且车辆密度超过40辆/km²时，对于所有测试的声誉阈值 $r$（3到18），$P_{msg}$ 都达到了100%。这表明在典型的高密度交通场景下，方案能可靠地传播真实公告。消息延迟 $D_{msg}$ 随车辆密度增加而缓慢增长，但在所有场景下均低于0.35秒，满足VANET公告消息的实时性需求（通常为300ms）。仿真还揭示了声誉阈值 $r$ 和传统阈值 $t$（消息数量）的对应关系，例如当 $r=18$ 时，对应的 $t$ 约为9。这些实验数据验证了方案在现实交通场景下的实用性。

### 局限性与开放问题
本文的声誉管理机制依赖一个简化的代理模型（如BBR），且声誉值的增减参数（如 $r_i=0.001, r_d=0.01$）需要手动设定，缺乏自适应调整的能力。声誉等级的计算方法仅给出了示例（与声誉值的分段映射），其合理性及对性能的影响未做深入探讨。此外，方案假设RM和GM是完全可信的，未考虑被攻陷的场景。未来工作可以考虑更复杂、更安全的去中心化声誉模型，以及抵御针对声誉管理中心的攻击。

### 强关联论文

[13] Wu et al. Balanced Trustworthiness, Safety, and Privacy in Vehicle-to-Vehicle Communications. **IEEE TVT 2010** [Google Scholar](https://scholar.google.com/scholar?q=Balanced+Trustworthiness,+Safety,+and+Privacy+in+Vehicle-to-Vehicle+Communications)

[35] Boneh et al. Short Group Signatures. **CRYPTO 2004** [Google Scholar](https://scholar.google.com/scholar?q=Short+Group+Signatures)

[21] Chen et al. A Privacy-Aware Reputation-Based Announcement Scheme for VANETs. **IEEE WVEC 2013** [Google Scholar](https://scholar.google.com/scholar?q=A+Privacy-Aware+Reputation-Based+Announcement+Scheme+for+VANETs)

[22] Chen et al. Private Reputation Retrieval in Public — A Privacy-Aware Announcement Scheme for VANETs. **IET Inf. Secur. 2017** [Google Scholar](https://scholar.google.com/scholar?q=Private+Reputation+Retrieval+in+Public+%E2%80%94+A+Privacy-Aware+Announcement+Scheme+for+VANETs)

[2] IEEE Standard for Wireless Access in Vehicular Environments - Security Services for Applications and Management Messages. **IEEE Std 1609.2 2016** [Google Scholar](https://scholar.google.com/scholar?q=IEEE+Standard+for+Wireless+Access+in+Vehicular+Environments-Security+Services+for+Applications+and+Management+Messages)

[18] Chen et al. Threshold Anonymous Announcement in VANETs. **IEEE JSAC 2011** [Google Scholar](https://scholar.google.com/scholar?q=Threshold+Anonymous+Announcement+in+VANETs)

[20] Li et al. A Reputation-Based Announcement Scheme for VANETs. **IEEE TVT 2012** [Google Scholar](https://scholar.google.com/scholar?q=A+Reputation-Based+Announcement+Scheme+for+VANETs)

[48] Wang et al. A RSU-aided distributed trust framework for pseudonym-enabled privacy preservation in VANETs. **Wireless Networks 2019** [Google Scholar](https://scholar.google.com/scholar?q=A+RSU-aided+distributed+trust+framework+for+pseudonym-enabled+privacy+preservation+in+VANETs)


## 关键词

+ 消息可链接群签名VANETs
+ 信息绑定与高效撤销
+ 车载自组网隐私保护公告
+ 抗女巫攻击和共谋攻击
+ 强可信度匿名方案
+ 车联网安全身份认证