---
title: "Threshold BBS signatures for distributed anonymous credential issuance"
doi: 10.1109/sp46215.2023.10179470
标题简称:
论文类型: conference
会议简称: S&P
发表年份: 2023
created: 2025-05-23 01:27:38
modified: 2025-05-23 01:27:44
---
## Threshold BBS signatures for distributed anonymous credential issuance

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/10179470)

## 作者

+ Jack Doerner
+ Yashvanth Kondi
+ Eysa Lee
+ Abhi Shelat
+ LaKyah Tyner

## 笔记

### 背景与动机
匿名凭证系统允许用户在不泄露身份的前提下证明其权限，其核心安全需求包括不可关联性和不可伪造性。传统方案依赖单一发行者持有私钥，这构成了单点故障风险：一旦私钥泄露，攻击者便可伪造任意凭证，而凭证的匿名性使得撤销极为困难。为缓解这一风险，将发行权限通过阈值密码学技术安全地分布到多个服务器上是自然的思路，即攻击者必须攻陷至少阈值数量的服务器才能获取伪造能力。针对基于BBS+签名构建的匿名凭证，本文旨在设计一个可组合安全的阈值签名协议，作为中心化发行者的直接、可替换的“补丁”。现有阈值化尝试存在若干瓶颈：Goldfeder等人的方案采用了Paillier加密和零知识范围证明，计算开销极大；且其乘法技术已被证明在ECDSA语境下存在安全问题，同时该方案依赖与底层签名无关的Strong RSA假设。此外，该方案还缺乏对强盲签名的支持，难以扩展为阈值的Oblivious VRF。本文试图填补的空白是：设计一个利用BBS+自身结构进行一致性检查、依赖与BBS+同源的qSDH假设、仅需两轮服务器间通信且客户端算力成为瓶颈的简洁、高效、可组合的阈值签名协议。

### 相关工作

[15] Au, Susilo, Mu. Constant-size dynamic k-taa. **SCN 2006** [Google Scholar](https://scholar.google.com/scholar?q=Constant-size+dynamic+k-taa)
> 核心思路：提出BBS+签名方案，用于k次匿名认证，签名大小与消息数量无关，支持选择性披露。
> 局限与区别：原方案为单一发行者设计，未涉及阈值设定；本文将其改造为分布式协议，并证明其在UC模型下的安全性。

[18] Camenisch, Drijvers, Lehmann. Anonymous Attestation using the Strong Diffie Hellman Assumption Revisited. **TRUST 2016** [Google Scholar](https://scholar.google.com/scholar?q=Anonymous+Attestation+using+the+Strong+Diffie+Hellman+Assumption+Revisited)
> 核心思路：为直接匿名证明（DAA）构造零知识证明，并证明BBS+在类型-3配对下的安全性。
> 局限与区别：该工作聚焦于如何证明一个签名而非如何生成它；本文依赖于其安全证明，并利用其构造的零知识证明来实现凭证的选择性披露。

[31] Bar-Ilan, Beaver. Non-cryptographic fault-tolerant computing in constant number of rounds of interaction. **PODC 1989** [Google Scholar](https://scholar.google.com/scholar?q=Non-cryptographic+fault-tolerant+computing+in+constant+number+of+rounds+of+interaction)
> 核心思路：提出了通过一次安全乘法来计算秘密值逆元的通用模板。
> 局限与区别：该模板假设半诚实安全；本文在此基础上增加了对恶意攻击者安全的检查机制，且专门适配了BBS+的结构，将检查退化为验证最终签名本身。

[36] Doerner, Kondi, Lee, Shelat. Secure two-party threshold ECDSA from ECDSA assumptions. **IEEE S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Secure+two-party+threshold+ECDSA+from+ECDSA+assumptions)
> 核心思路：设计了基于OT扩展的两轮安全乘法协议，并用于构造两方阈值ECDSA。
> 局限与区别：本文直接采用了该乘法器作为基础构件。与ECDSA不同，BBS+只需一次乘法调用，且无需额外的输入一致性检查，因为BBS+的签名验证本身可作为全局正确性检查。

[44] Dodis, Yampolskiy. A verifiable random function with short proofs and keys. **PKC 2005** [Google Scholar](https://scholar.google.com/scholar?q=A+verifiable+random+function+with+short+proofs+and+keys)
> 核心思路：提出形式为 $e(G_1, G_2)^{1/(x+e)}$ 的可验证随机函数（VRF），其证明结构 $G_1/(x+e)$ 与BBS+的签名结构高度相似。
> 局限与区别：该工作本身不涉及阈值或盲性评估；本文指出其协议可直接扩展为该VRF的阈值无知性评估协议。

[48] Gennaro, Goldfeder, Ithurburn. Fully distributed group signatures. 2019
> 核心思路：首次尝试将BBS+阈值化，核心依赖Paillier加密进行安全乘法。
> 局限与区别：该方案使用了与BBS+假设无关的Strong RSA，且其乘法技术在后来的阈值ECDSA分析中被发现存在安全漏洞；此外，该方案不支持强盲签名，无法扩展至阈值无知性VRF。本文在效率、安全性及扩展性上均优于该方案。

[53] Rial, Piotrowska. Security analysis of coconut, an attribute-based credential scheme with threshold issuance. **ePrint 2022** [Google Scholar](https://scholar.google.com/scholar?q=Security+analysis+of+coconut%2C+an+attribute-based+credential+scheme+with+threshold+issuance)
> 核心思路：分析了Coconut方案（基于PS签名）的安全缺陷并提供了补丁，但其公钥规模随消息数量线性增长。
> 局限与区别：本文的BBS+方案公钥仅包含两个群元素，与消息数量无关。RP-Coconut仅提供顺序组合安全，而本文协议满足更强的UC组合安全。

[63] Gilboa. Two party RSA key generation. **CRYPTO 1999** [Google Scholar](https://scholar.google.com/scholar?q=Two+party+RSA+key+generation)
> 核心思路：提出基于OT的经典半诚实安全两方分布式乘法技术。
> 局限与区别：该技术在半诚实模型下安全；本文使用的乘法器[36]是对该技术的恶意安全扩展。

### 核心技术与方案

本文的整体框架是构造一个可组合安全的阈值BBS+签名协议，作为匿名凭证发行系统的核心构件。整个系统的运作分为密钥生成和签名两个阶段，服务器之间仅需两轮交互。

**密钥生成（Protocol 4.1）**。各服务器通过随机多项式生成自己的秘密密钥份额 $x_i$，并通过承诺-证明-发布方式广播公钥份额 $X_i = x_i \cdot G_2$。所有接收方检查各 $X_i$ 是否位于同一个次数为 $t-1$ 的多项式上，以确保正确性。同时，服务器联合生成公共参数 $\mathbf{H} = \{H_1, \ldots, H_{\ell+1}\}$。该过程也包含了乘法所需的基础OT设置。

**签名协议**。当客户端请求签署消息向量 $\mathbf{m}$ 时，协议按以下步骤运行：
1.  **初始化**：客户端向服务器集合 $\mathbf{J}$（大小为 $t$）发送请求。每个服务器 $\mathcal{P}_i$ 本地采样随机数 $e_i, s_i$ 和 $r_i$，并从 $\mathcal{F}_{\text{Zero}}$ 获得共享为0的份额 $\alpha_i$。
2.  **承诺与乘法**：$\mathcal{P}_i$ 承诺 $e_i, s_i$，并将秘密 $a_{ij} = \lambda_i^{\mathbf{J}}(0) \cdot x_i + \alpha_i$（经拉格朗日系数处理后的带随机化秘密份额）输入到与所有其它服务器 $j$ 的 $\mathcal{F}_{\text{Mul2P}}$ 实例中。该实例的作用是产生共享的乘积 $r_j \cdot a_{ij}$。
3.  **输出生成**：在所有承诺被打开、所有乘法实例完成后，$\mathcal{P}_i$ 计算全局 $e = \sum e_j$，$s = \sum s_j$，目标点 $B = G_1 + s \cdot H_1 + \sum m_k \cdot H_{k+1}$，其本地份额 $R_i = r_i \cdot B$，以及整合了局部和乘法结果的 $u_i$。最后，$\mathcal{P}_i$ 将 $e, s, R_i, u_i$ 发送给客户端。
4.  **重建与验证**：客户端从至少 $t$ 个服务器收集输出，检查 $e, s$ 的一致性和签名公钥，计算 $A = \sum R_i / \sum u_i$，并运行标准BBS+验证算法确认签名 $(A, e, s)$ 的有效性。

**安全性直觉**。协议的安全证明在UC框架下进行，依赖的是 $(\mathcal{F}_{\text{Com}}, \mathcal{F}_{\text{ZK}}, \mathcal{F}_{\text{Zero}}, \mathcal{F}_{\text{Mul2P}})$ 的混合模型。最关键的设计在于，与ECDSA不同，BBS+的构造使得客户端对最终签名的验证构成了一次全局的“隐式MAC”检查。模拟器在理想世界中可以充当诚实服务器：当看到客户端发送的挑战时，它只需提取恶意服务器的输入并提交给理想功能。如果恶意服务器作弊导致签名不合法，验证会失败，客户端直接中止，这不会泄露任何信息给攻击者。模拟的关键在于，模拟器输出的签名是直接从理想功能获得的合法签名。即使攻击者试图通过诱导部分失败来泄露信息，由于该协议仅涉及一次安全乘法（而非ECDSA的多次调用），不存在跨乘法的输入一致性攻击向量，因此隐式MAC检查是充分的。该协议实现了选择性中止的安全性。

**复杂度**。对于 $n$ 个服务器中的 $t$ 个参与签名，总成本分别为：  
- **通信**：每服务器在签名阶段发送约 $(n-1) \cdot 2 \cdot \text{MulCost}$ 比特，其中 $\text{MulCost}$ 是乘法协议的开销。客户端需接收 $t$ 份 $(\mathbb{G}_1^{1} + \mathbb{Z}_p^{1})$ 大小的输出。  
- **计算**：每服务器需进行 $\ell+2$ 次 $\mathbb{G}_1$ 上的标量乘（构建点 $B$ 和计算 $R_i$）以及参与乘法协议所需的计算（主要是OT相关）。客户端需进行 $\ell+1$ 次 $\mathbb{G}_1$ 标量乘、1次 $\mathbb{G}_2$ 标量乘和2次配对操作来验证签名。  
- **轮次**：服务器之间两轮交互。

### 核心公式与流程

**签名计算公式**
$$A := \frac{G_1 + s \cdot H_1 + \sum_{i \in [\ell]} m_i \cdot H_{i+1}}{x + e}$$
> 作用：描述BBS+签名的计算过程。本文通过分布式计算该公式来生成签名，其中 $x$ 被秘密共享，$e, s$ 由各方联合采样，$r$ 被用作隐藏因子。

**隐式MAC检查（隐式正确性保障）**
$$\mathfrak{e}(A, X + e \cdot G_2) = \mathfrak{e}\left(G_1 + s \cdot H_1 + \sum_{i \in [\ell]} m_i \cdot H_{i+1}, G_2\right)$$
> 作用：这是标准的BBS+验证方程。在协议中，用户通过验证该等式，可以确认所有服务器提供的份额 $R_i, u_i$ 是否一致且正确，从而替代了显式的、昂贵的MAC验证过程。

**秘密份额计算**
$$u_i := r_i \cdot (e + \lambda_i^{\mathbf{J}}(0) \cdot x_i) + \alpha_i + \sum_{j \in \mathbf{J} \setminus \{i\}} (c_{i,j} + d_{i,j}) \bmod p$$
> 作用：该公式整合了本地乘法和通过 $\mathcal{F}_{\text{Mul2P}}$ 计算得到的乘积 $r_i \cdot x_j$ 的份额，并加入随机化因子 $\alpha_i$，最终得到 $u = r \cdot (x+e)$ 的秘密份额。用户通过聚合这些份额恢复 $u$。

**恢复签名的最终步骤**
$$A := \sum_{i \in \mathbf{J}} R_i / \sum_{i \in \mathbf{J}} u_i$$
> 作用：客户端聚合所有参与服务器的份额 $R_i$ 和 $u_i$，通过除法得出最终的签名元素 $A$。

### 实验结果
实验硬件环境为AMD Ryzen 9 7950X（本地实验）和Google Cloud C2D-STANDARD-4（LAN/WAN实验），网络环境包括本地、LAN和WAN（十二个美国区域，一个欧洲区域）。实验实现了 $n \in [2, 32]$ 的 $n$-of-$n$ 和 $t$-of-$n$ 场景，使用BLS12-381曲线。在LAN环境下，$n=6$ 时服务器端处理时间约为5.1ms，而客户端从发起到验证完成的整体延迟为11.3ms，其中签名验证本身占5.0ms。这表明对于 $n \leq 5$ 的场景，客户端签名验证是性能瓶颈。与标准BBS+方案相比，2方阈值的服务器端开销约为3倍（本地/LAN），而由于网络延迟，WAN环境下开销约为70倍。对比基于RP-Coconut的类似阈值实现，本文协议的服务器端计算随参与者数量增长更快，但客户端随参与者数量的增长远慢于RP-Coconut。结果显示，本文的协议在高延迟网络下仍能达到几十到几百毫秒的响应时间，适用于现代网络应用。

### 局限性与开放问题
协议的轮次虽然固定为两轮，但要求所有参与服务器都处于在线状态，对于高度故障或异步的网络环境可能不够鲁棒。协议的恶意安全性依赖于BBS+验证作为一个隐式MAC，这虽然避免了通用MPC的开销，但也意味着无法像某些通用框架那样提供可识别中止或公平性。当前协议的实现基于OT扩展，其计算成本主要是曲线上的标量乘，相较于ECDSA方案仍有改进空间。

### 强关联论文

[15] Au, Susilo, Mu. Constant-size dynamic k-taa. **SCN 2006** [Google Scholar](https://scholar.google.com/scholar?q=Constant-size+dynamic+k-taa)

[18] Camenisch, Drijvers, Lehmann. Anonymous Attestation using the Strong Diffie Hellman Assumption Revisited. **TRUST 2016** [Google Scholar](https://scholar.google.com/scholar?q=Anonymous+Attestation+using+the+Strong+Diffie+Hellman+Assumption+Revisited)

[31] Bar-Ilan, Beaver. Non-cryptographic fault-tolerant computing in constant number of rounds of interaction. **PODC 1989** [Google Scholar](https://scholar.google.com/scholar?q=Non-cryptographic+fault-tolerant+computing+in+constant+number+of+rounds+of+interaction)

[36] Doerner, Kondi, Lee, Shelat. Secure two-party threshold ECDSA from ECDSA assumptions. **IEEE S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Secure+two-party+threshold+ECDSA+from+ECDSA+assumptions)

[44] Dodis, Yampolskiy. A verifiable random function with short proofs and keys. **PKC 2005** [Google Scholar](https://scholar.google.com/scholar?q=A+verifiable+random+function+with+short+proofs+and+keys)

[48] Gennaro, Goldfeder, Ithurburn. Fully distributed group signatures. **2019** [Google Scholar](https://scholar.google.com/scholar?q=Fully+distributed+group+signatures)

[53] Rial, Piotrowska. Security analysis of coconut, an attribute-based credential scheme with threshold issuance. **ePrint 2022** [Google Scholar](https://scholar.google.com/scholar?q=Security+analysis+of+coconut%2C+an+attribute-based+credential+scheme+with+threshold+issuance)

[55] Boneh, Boyen. Short signatures without random oracles. **EUROCRYPT 2004** [Google Scholar](https://scholar.google.com/scholar?q=Short+signatures+without+random+oracles)


## 关键词

+ BBS+签名方案
+ 阈值匿名凭证
+ 多方签名协议
+ 盲签名
+ 可组合安全性
+ 分布式VRF