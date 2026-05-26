---
title: "Secure multiparty computation from threshold encryption based on class groups"

标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 2023
modified: 2025-04-28 17:09:56
created: 2025-04-11 13:58:19
---

## Secure multiparty computation from threshold encryption based on class groups

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-38557-5_20)

## 作者

+ Lennart Braun 
+ Ivan Damgård 
+ [Claudio Orlandi](Claudio%20Orlandi.md)
## 笔记

### 背景与动机
安全的门限同态加密是实现通用安全多方计算（MPC）的核心工具之一。经典的 CDN 框架利用门限线性同态加密构造 MPC，但此前的实例化通常依赖 Paillier 加密，存在三个关键瓶颈：Paillier 需要可信设置（秘密生成 RSA 模数），且明文空间受限为 $\mathbb{Z}_n$，对许多需要 $\mathbb{F}_q$ 算术的应用不友好。SPDZ 类协议虽避免了门限加密，但其预处理阶段使用格基同态加密，当明文空间较大时效率低下。YOSO（You-Only-Speak-Once）模型是解决区块链上 MPC 通信复杂度的有力框架，其核心是让每个委员会只发言一次，但该模型要求密钥生成协议只需极少轮交互且无需可信设置。Gentry 等人于 CRYPTO 2021 基于 Paillier 的方案 [29] 需要可信设置，YOSO 模型中实现无可信设置 MPC 成为开放问题。本文基于 Castagnos-Laguillaumie（CL）类群框架，构建了第一个主动安全的门限密码系统，并利用其透明设置和灵活的明文空间特性，设计了新的分布式密钥生成和零知识证明协议，最终实现了无可信设置的 YOSO MPC，填补了这一空白。

### 相关工作

[17] Cramer et al. Multiparty computation from threshold homomorphic encryption. **EUROCRYPT 2001** [Google Scholar](https://scholar.google.com/scholar?q=Multiparty+computation+from+threshold+homomorphic+encryption)
> 核心思路：首次利用门限线性同态加密构造通用安全多方计算的 CDN 框架。
> 局限与区别：依赖具体加密方案的实例化，其提出的 Paillier 实例化需要信任的密钥设定。

[21] Damgård et al. Multiparty computation from somewhat homomorphic encryption. **CRYPTO 2012** [Google Scholar](https://scholar.google.com/scholar?q=Multiparty+computation+from+somewhat+homomorphic+encryption)
> 核心思路：提出 SPDZ 协议，将昂贵的公钥操作移至预处理阶段，产生在线阶段高效的 MPC。
> 局限与区别：预处理使用格基同态加密，在处理大型明文空间时通信和计算开销巨大。

[29] Gentry et al. YOSO: You Only Speak Once - Secure MPC with Stateless Ephemeral Roles. **CRYPTO 2021** [Google Scholar](https://scholar.google.com/scholar?q=YOSO%3A+You+Only+Speak+Once+Secure+MPC+with+Stateless+Ephemeral+Roles)
> 核心思路：提出 YOSO 模型，通过每次切换委员会来隐藏成员身份，实现亚线性通信复杂度的 MPC。
> 局限与区别：其构造依赖 Paillier 加密，需要可信设置，且将无可信设置 YOSO MPC 作为开放问题。

[28] Gennaro et al. Secure distributed key generation for discrete-log based cryptosystems. **Journal of Cryptology 2006** [Google Scholar](https://scholar.google.com/scholar?q=Secure+distributed+key+generation+for+discrete-log+based+cryptosystems)
> 核心思路：设计了针对离散对数密码系统的安全分布式密钥生成协议，确保公钥均匀分布。
> 局限与区别：协议复杂、轮数多，不适合 YOSO 单轮发言模型。

[12] Castagnos et al. Linearly homomorphic encryption from DDH. **CT-RSA 2015** [Google Scholar](https://scholar.google.com/scholar?q=Linearly+homomorphic+encryption+from+DDH)
> 核心思路：提出基于类群的 CL 框架，构造线性同态加密，明文空间可为 $\mathbb{F}_q$。
> 局限与区别：原方案无门限版本，也未提供分布式密钥生成协议。

[10] Castagnos et al. Two-party ECDSA from hash proof systems and efficient instantiations. **CRYPTO 2019** [Google Scholar](https://scholar.google.com/scholar?q=Two-party+ECDSA+from+hash+proof+systems+and+efficient+instantiations)
> 核心思路：在 CL 框架上构造了常轮通信的零知识证明协议。
> 局限与区别：协议需要二进制挑战以解决未知阶群中求逆问题，重复多轮导致效率不高。

[11] Castagnos et al. Bandwidth-efficient threshold EC-DSA. **PKC 2020** [Google Scholar](https://scholar.google.com/scholar?q=Bandwidth-efficient+threshold+EC-DSA)
> 核心思路：通过强根假设或低阶假设，允许大挑战空间，提高了 CL 框架中零知识证明的效率。
> 局限与区别：本文提出的基于 Rough Order 假设的方案更加简洁。

[36] Rabin. A simplified approach to threshold and proactive RSA. **CRYPTO 1998** [Google Scholar](https://scholar.google.com/scholar?q=A+simplified+approach+to+threshold+and+proactive+RSA)
> 核心思路：提出基于未知阶群的 Feldman 秘密共享，用于门限 RSA。
> 局限与区别：本文发现该方案中的秘密共享存在攻击，并给出了修复；协议也得以简化。

[32] Kolby et al. Towards efficient YOSO MPC without setup. **ePrint 2022** [Google Scholar](https://scholar.google.com/scholar?q=Towards+efficient+YOSO+MPC+without+setup)
> 核心思路：在 YOSO 模型中实现无设置 MPC，通过为每个委员会成员分配独立密钥并共享秘密。
> 局限与区别：需传递的数据量与电路大小成正比；本文使用全局公钥只需传递密钥份额。

### 核心技术与方案

本文的整体技术方案分为四个层次：一是设计一个鲁棒的门限线性同态加密方案 $\Pi^*_{\text{hsm-cl}}$；二是设计支持未知阶群的整数秘密共享方案和 Feldman VSS；三是设计高效的零知识证明协议；四是基于上述工具构建 UC 安全的 MPC 协议并适配 YOSO 模型。

**1. 门限加密方案 $\Pi^*_{\text{hsm-cl}}$ 。** 基础加密方案是 CL 框架下的 HSM-CL 方案 [13]。其公钥为 $g_q^{\text{sk}_{\text{cl}}}$，加密一个消息 $m \in \mathbb{F}_q$ 为 $(g_q^r, f^m \cdot \text{pk}_{\text{cl}}^r)$。本文的贡献在于：首先，证明了一个有偏的公开密钥（即允许敌手在看到诚实者贡献后调整“全局”公钥）仍能提供 IND-CPA 安全。这通过归约证明：给定一个对手 $\mathcal{B}$ 攻击有偏公钥，可以构造一个攻击标准公钥的对手 $\mathcal{A}$，$\mathcal{A}$ 将挑战者的标准公钥加上敌手选择的偏差 $\delta$ 作为 $\mathcal{B}$ 的公钥，并将挑战密文 $\text{ct} = (g_q^r, \text{pk}_{\text{cl}}^r \cdot f^{m_b})$ 调整为 $\text{ct}' = (g_q^r, \text{ct}_2 \cdot (g_q^r)^\delta) = (g_q^r, (\text{pk}_{\text{cl}} \cdot g_q^\delta)^r \cdot f^{m_b})$，使其与有偏公钥匹配。这保证了效率高的密钥生成协议（允许偏差）的安全性。其次，定义了特殊密钥生成算法 BiasedSpecialKeyGen$_b$，当 $b=1$ 时是真实公钥，当 $b=0$ 时是损失性公钥，后者在安全证明中至关重要，因为损失性公钥下的加密结果在统计上与消息独立。两个类型的密钥不可区分性依赖 $\Pi^1_{\text{hsm-cl}}$ 的 IND-CPA 安全性。

**2. 整数秘密共享与 Feldman VSS。** 由于群阶未知，秘密共享必须在整数上进行。方案采用 Shamir 秘密共享的整数变体：将秘密 $\alpha$ 乘以 $\Delta = N!$ 得到 $\tilde{\alpha} = \alpha \cdot \Delta$，然后使用一个整数系数的 $t$ 次多项式 $f(X) = \tilde{\alpha} + r_1 X + \dots + r_t X^t$。通过 Lagrange 插值，由 $t+1$ 个份额可以恢复出 $\tilde{\alpha}$，因为 $\Delta \cdot \ell_i^S(X) \in \mathbb{Z}[X]$。对于 Feldman VSS，需要验证份额的一致性。本文的分析揭示了一个严重问题：基于未知阶群的 Feldman VSS 不能保证从非对抗性份额中恢复出与承诺值一致的秘密。因为整数秘密共享的正确性只模群阶成立，如果敌手知道群阶，就可以产生一个合法的份额集合，但该集合插值出的整数与秘密不同（差一个群阶的倍数）。为解决此问题，要求 dealer 同时提供对 $C_0 = g_{\text{F}}^\alpha$ 的零知识证明。如果重构出的值 $\alpha'$ 满足 $g_{\text{F}}^{\alpha'} \neq g_{\text{F}}^\alpha$，则 $\alpha' - \alpha$ 是群阶的倍数，与 ORD 假设矛盾。通过这一修复（见 Protocol 2 和 Lemma 5），VSS 的安全性基于“群阶难计算”的 ORD 假设。此外，为了处理 $\Delta$ 与群阶可能有公因子的问题，可以通过选择具有适当性质的基础 $g_{\text{F}}$ 或依赖 $RO_{N+1}$ 假设。

**3. 零知识证明协议。** 为了支持 MPC 中的乘法操作，需要证明：对于给定的密文 $\text{ct}_a$，证明者知道 $a$ 和一个随机数，同时 $\text{ct}_a$ 是 $a$ 的有效加密；还需要证明 $\text{ct}_c = \text{ct}_b^a \cdot \text{Enc}(\text{pk}, 0)$，其中 $\text{ct}_b$ 是已知密文。这两个关系（$\text{R}_{\text{Enc}}$ 和 $\text{R}_{\text{Mult}}$）都是形如 $Y_i = \prod_j X_{i,j}^{w_j}$ 的通用关系（见公式 5）。标准的 Schnorr 风格 $\Sigma$-protocols（Commit-Respond-Verify）可以直接用于这类关系。然而，在未知阶群中实现 2-special soundness 需要提取器能够计算 $(\text{chl} - \text{chl}')^{-1}$ 模群阶。如果群阶未知，这无法高效完成。本文的贡献在于引入“Rough Order”假设（$RO_C$）：断言对于给定的安全参数，无法区分一个“$C$-rough（即阶没有小于 $C$ 的素因子）”的类群和一个一般的类群。在 $RO_C$ 假设下，如果群阶是 $C$-rough 的，且挑战空间是 $[C]$，则 $\text{chl} - \text{chl}'$ 必然在模群阶下可逆，从而提取器可以有效地提取出完整的证据 $\mathbf{w}$。因此，标准 $\Sigma$-protocol 的可靠性能达到 $1/C + \text{negl}(\lambda)$，而这只需要挑战空间大小设置合理（如 $C$ 为超多项式大小），单次执行即可获得可忽略的可靠性误差。对于 PoPK 和 PoCM，提取过程只需提取 $a \in \mathbb{F}_q$，这出现在 $f$ 的指数上，其阶已知为 $q$，因此可以提取。随机数的提取因为 ($\text{chl} - \text{chl}'$) 在 $g_q$ 的未知阶下不可逆而无法完成，但这并非必需。

**4. MPC 协议与 YOSO 适配。** 基于上述工具，构造了 UC 安全的 MPC 协议 $\Pi_{\text{ABB}}^q$，它实现算术黑箱（Arithmetic Black Box，ABB）功能。ABB 支持对 $\mathbb{F}_q$ 中的元素进行秘密输入、线性组合、乘法和公开输出。协议遵循 CDN 范式：所有值都以 $\Pi^*_{\text{hsm-cl}}$ 的密文形式存在，当需要解密或进行乘法时，通过 $\mathcal{F}_{\text{TE}}$ 和零知识证明来实现。安全证明使用损失性公钥技术，将证明者使用的真实密钥切换为损失性密钥，那么诚实输入的密文就变成 0 的加密，从而实现模拟器与真实协议的不可区分。  YOSO 适配的核心在于将协议中的交互步骤转化为由不同委员会完成的单轮发言。密钥生成步骤（DistKeyGen）由 4 个委员会依次使用 CreateVSS 协议完成，生成公钥和秘钥的秘密分享。解密步骤本身已是单轮。关键的挑战在于如何在委员会之间传递秘钥份额（Reshare 协议）：通过一个辅助委员会同时向旧委员会和新委员会秘密共享同一个随机值 $\eta$，旧委员会公开其份额减去 $\eta$ 的份额（即 $\text{sk} - \eta$），新委员会据此重构出 $\text{sk}$ 的份额。所有步骤都使用非交互式知识论证 NIAoK 消除交互，适应 YOSO 的“只发言一次”模型。整个协议的复杂度中，每个委员会需要发送 $O(N + C)$量级的数据（$N$ 为委员会大小，$C$ 为计算电路大小）。

### 核心公式与流程

**[DKG 协议中的公钥扭曲归约]**
$$ \text{ct}' = (g_q^r, (\text{pk}_{\text{cl}}^r \cdot f^{m_b}) \cdot (g_q^r)^\delta) = (g_q^r, (\text{pk}_{\text{cl}} \cdot g_q^\delta)^r \cdot f^{m_b}) $$
> 作用：展示如何将一个针对有偏公钥的 IND-CPA 游戏归约到标准 IND-CPA 游戏。挑战密文 $\text{ct} = (g_q^r, \text{pk}_{\text{cl}}^r \cdot f^{m_b})$ 被乘以 $g_q^{r\delta}$ 后，等价于用有偏公钥 $\text{pk}_{\text{cl}} \cdot g_q^\delta$ 加密 $m_b$。

**[整数秘密共享中的 Lagrange 重构]**
$$ f(X) = \sum_{i \in S} y_i \cdot \ell_i^S(X) \quad \text{ with } \quad \ell_i^S(X) = \prod_{j \in S \setminus \{i\}} \frac{x_j - X}{x_j - x_i} $$
> 作用：基本的 Lagrange 插值公式。强调在整数秘密共享中，与一般代数结构不同，拉格朗日系数是分数，需要通过乘以 $\Delta = N!$ 来去除分母，使得 $\Delta \cdot \ell_i^S(0) \in \mathbb{Z}$ 以保证整数重构。

**[Feldman VSS 的份额验证]**
$$ g_{\text{F}}^{\Delta y_i} \stackrel{?}{=} C_0^{\Delta^2} \cdot \prod_{k=1}^t (C_k)^{(i^k)} $$
> 作用：验证 $P_i$ 的整数秘密共享份额 $y_i$ 是否正确。左侧是群 $g_{\text{F}}$ 的 $\Delta \cdot y_i$ 次幂，右侧是承诺 $C_0, C_1, \dots, C_t$ 组合的结果，该等式在多项式成立时必然成立。

**[基于 $RO_C$ 假设的零知识证明提取]**
$$ Y_i^{\text{chl} - \text{chl}'} = \prod_{j \in [m]} X_{i,j}^{(u_j - u_j')} \iff Y_i = \prod_{j \in [m]} X_{i,j}^{(u_j - u_j') \cdot (\text{chl} - \text{chl}')^{-1}} $$
> 作用：展示在 $RO_C$ 假设下，如何从两个针对不同挑战 $(\text{chl}, \text{chl}')$ 的合法应答中提取证据。由于群阶是$C$-rough，且 $|\text{chl} - \text{chl}'| < C$，其差在模群阶下可逆，故可将 $Y_i$ 表示为 $X_{i,j}$ 的整数指数组合。

### 实验结果
本文是理论性论文，没有提供实验数据。作者没有进行任何工程实现或性能基准测试。所有关于效率的论述均基于理论分析：协议通信开销为 $O(C)$ 量级，其中 $C$ 为挑战空间大小；每个参与方的计算量主要来自群运算和零知识证明。论文指出，通过适当选择参数（如挑战空间 $C$），单轮零知识证明即可获得可忽略的可靠性误差，因此是常数因子开销。具体性能取决于底层 CL 密码体制的具体群运算效率，该效率取决于判别式的大小。论文没有给出任何与现有方案的性能对比数据。

### 局限性与开放问题
本文引入的 Rough Order ($RO_C$) 假设是一个尚未经过充分验证的新假设，其可信度依赖于对类群阶分布的理论分析和长期计算经验。虽然 Cohen-Lenstra 启发法支持该假设，但将其作为安全基石仍需谨慎。此外，YOSO 协议的整体延迟虽然轮数少，但需要多个委员会顺序参与，对于某些需要低延迟响应的场景可能不是最优解。作者也指出，其 YOSO 协议的密钥传递开销随着电路深度的增加而正比增长，未来工作可以探索更高效的密钥传递技术，例如基于身份或属性的加密，以进一步压缩 YOSO 协议中的私密通信量。

### 强关联论文

[17] Cramer et al. Multiparty computation from threshold homomorphic encryption. **EUROCRYPT 2001** [Google Scholar](https://scholar.google.com/scholar?q=Multiparty+computation+from+threshold+homomorphic+encryption)

[21] Damgård et al. Multiparty computation from somewhat homomorphic encryption. **CRYPTO 2012** [Google Scholar](https://scholar.google.com/scholar?q=Multiparty+computation+from+somewhat+homomorphic+encryption)

[29] Gentry et al. YOSO: You Only Speak Once - Secure MPC with Stateless Ephemeral Roles. **CRYPTO 2021** [Google Scholar](https://scholar.google.com/scholar?q=YOSO%3A+You+Only+Speak+Once+Secure+MPC+with+Stateless+Ephemeral+Roles)

[28] Gennaro et al. Secure distributed key generation for discrete-log based cryptosystems. **Journal of Cryptology 2006** [Google Scholar](https://scholar.google.com/scholar?q=Secure+distributed+key+generation+for+discrete-log+based+cryptosystems)

[12] Castagnos et al. Linearly homomorphic encryption from DDH. **CT-RSA 2015** [Google Scholar](https://scholar.google.com/scholar?q=Linearly+homomorphic+encryption+from+DDH)

[36] Rabin. A simplified approach to threshold and proactive RSA. **CRYPTO 1998** [Google Scholar](https://scholar.google.com/scholar?q=A+simplified+approach+to+threshold+and+proactive+RSA)

[10] Castagnos et al. Two-party ECDSA from hash proof systems and efficient instantiations. **CRYPTO 2019** [Google Scholar](https://scholar.google.com/scholar?q=Two-party+ECDSA+from+hash+proof+systems+and+efficient+instantiations)

[11] Castagnos et al. Bandwidth-efficient threshold EC-DSA. **PKC 2020** [Google Scholar](https://scholar.google.com/scholar?q=Bandwidth-efficient+threshold+EC-DSA)

[13] Castagnos et al. Practical fully secure unrestricted inner product functional encryption modulo p. **ASIACRYPT 2018** [Google Scholar](https://scholar.google.com/scholar?q=Practical+fully+secure+unrestricted+inner+product+functional+encryption+modulo+p)

[32] Kolby et al. Towards efficient YOSO MPC without setup. **ePrint 2022** [Google Scholar](https://scholar.google.com/scholar?q=Towards+efficient+YOSO+MPC+without+setup)


## 关键词

+ 类群阈值加密主动安全MPC
+ CL框架类群密码系统门限化
+ 乘法关系恒定通信ZK证明
+ UC安全MPC透明设置无陷门
+ YOSO区块链MPC密钥生成