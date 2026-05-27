---
title: "Bandwidth-efficient threshold EC-DSA"
doi: 10.1007/978-3-030-45388-6_10
标题简称:
论文类型: conference
会议简称: PKC
发表年份: 2020
created: 2025-04-28 17:08:15
modified: 2025-04-28 17:09:09
---
## Bandwidth-efficient threshold EC-DSA

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-030-45388-6_10)

## 作者

+ Guilhem Castagnos 
+ Dario Catalano 
+ Fabien Laguillaumie 
+ Federico Savasta 
+ Ida Tucker 

## 笔记

### 背景与动机
阈值签名允许一组参与者共同控制签名能力，任何大于阈值的子集可以生成有效签名，而小于等于阈值的子集无法获得任何签名信息。在加密货币领域，特别是比特币中，阈值EC-DSA签名能有效防止私钥单点存储导致的资产被盗风险。现有阈值EC-DSA方案主要存在带宽开销大或设置复杂的问题：Gennaro和Goldfeder在CCS 2018的方案 [GG18] 使用Paillier同态加密来实现秘密乘法，但因Paillier明文空间与EC-DSA的 $\mathbf{Z}/q\mathbf{Z}$ 不匹配，被迫引入昂贵的范围证明（range proofs）来防止恶意行为。Lindell和Nof的方案 [LN18] 的OT实现也带来较大带宽。Castagnos等人的两方协议 [CCL+19] 基于类群实现了消息空间为 $\mathbf{Z}/q\mathbf{Z}$ 的加密，但丢失了满射性，且验证密文有效性的证明需使用二进制挑战导致效率低下。本文旨在开发新技术，在保留可证明安全性的前提下，显著降低阈值EC-DSA的带宽消耗，并避免范围证明。

### 相关工作

[GG18] Gennaro, R., Goldfeder, S. Fast multiparty threshold ECDSA with fast trustless setup. **ACM CCS 2018** [Google Scholar](https://scholar.google.com/scholar?q=Fast+multiparty+threshold+ECDSA+with+fast+trustless+setup)
> 核心思路：使用Paillier加密和MtA（乘法转加法）协议实现阈值EC-DSA签名。
> 局限与区别：Paillier明文空间与 $q$ 不匹配，需要昂贵的范围证明来防止恶意行为。本文通过使用CL加密并开发新的ZKAoK避免了所有范围证明，带宽降低数倍。

[LN18] Lindell, Y., Nof, A. Fast secure multiparty ECDSA with practical distributed key generation and applications to cryptocurrency custody. **ACM CCS 2018** [Google Scholar](https://scholar.google.com/scholar?q=Fast+secure+multiparty+ECDSA+with+practical+distributed+key+generation+and+applications+to+cryptocurrency+custody)
> 核心思路：基于同态加密和OT实现高效的多方EC-DSA。
> 局限与区别：其OT实现以及整体通信开销较大。本文在带宽上对所有安全级别均有显著优势，并在192位安全以上计算速度更快。

[CCL+19] Castagnos, G., Catalano, D., Laguillaumie, F., Savasta, F., Tucker, I. Two-party ECDSA from hash proof systems and efficient instantiations. **CRYPTO 2019** [Google Scholar](https://scholar.google.com/scholar?q=Two-party+ECDSA+from+hash+proof+systems+and+efficient+instantiations)
> 核心思路：基于类群和哈希证明系统实现两方EC-DSA，加密的消息空间为 $\mathbf{Z}/q\mathbf{Z}$。
> 局限与区别：其ZKAoK使用二进制挑战，效率低下。本文为CL加密方案开发了基于强根假设和低阶假设的新ZKAoK，大幅提高了证明效率并将其推广到多方场景。

[CL15] Castagnos, G., Laguillaumie, F. Linearly homomorphic encryption from DDH. **CT-RSA 2015** [Google Scholar](https://scholar.google.com/scholar?q=Linearly+homomorphic+encryption+from+DDH)
> 核心思路：提出了具有易解离散对数子群的群框架，并给出了基于二次域类群的实例化。
> 区别：本文基于此框架，通过引入随机生成元 $g_q$ 和新的ZKAoK，适配了阈值ECDSA场景。

[Gil99] Gilboa, N. Two party RSA key generation. **CRYPTO 1999** [Google Scholar](https://scholar.google.com/scholar?q=Two+party+RSA+key+generation)
> 核心思路：提出了一种两方协议，用于计算加性秘密共享的乘积。
> 区别：该协议是本文和[GG18]中乘法转加法步骤的基础，本文将其与新的CL加密方案和ZKAoK结合。

[MR01] MacKenzie, P.D., Reiter, M.K. Two-party generation of DSA signatures. **CRYPTO 2001** [Google Scholar](https://scholar.google.com/scholar?q=Two-party+generation+of+DSA+signatures)
> 核心思路：提出了两方DSA签名协议。
> 局限与区别：依赖大量低效的零知识证明，实用性差。本文通过新的证明技术提高了效率。

[DF02] Damgård, I., Fujisaki, E. A statistically-hiding integer commitment scheme based on groups with hidden order. **ASIACRYPT 2002** [Google Scholar](https://scholar.google.com/scholar?q=A+statistically-hiding+integer+commitment+scheme+based+on+groups+with+hidden+order)
> 核心思路：在隐藏阶群中使用了广义Schnorr证明，并考虑了低阶元素和根问题。
> 区别：本文借鉴了在未知阶群中使用挑战空间的思想，但针对类群的特定子群进行了适配和更具体的归约分析。

[CLT18] Castagnos, G., Laguillaumie, F., Tucker, I. Practical fully secure unrestricted inner product functional encryption modulo p. **ASIACRYPT 2018** [Google Scholar](https://scholar.google.com/scholar?q=Practical+fully+secure+unrestricted+inner+product+functional+encryption+modulo+p)
> 核心思路：在此框架下构造了具体的线性同态加密方案，其安全性基于HSM假设。
> 区别：本文使用此加密方案作为底层原语，并为之定制了高效的ZKAoK。

### 核心技术与方案

本文的核心贡献分为三个技术层次：一是为CL加密方案设计了一个高效的零知识知识论证（ZKAoK）；二是提出了一个交互式设置协议（ISetup）来生成公共参数；三是将上述工具集成到一个完整的阈值EC-DSA签名协议中，并给出了安全证明。

1.  **ZKAoK设计与安全归约**：针对CL加密中密文 $\mathbf{c} = (c_1 = g_q^r, c_2 = \mathsf{pk}^r f^a)$ 的关系 $R_{\mathsf{Enc}}$，本文设计了图2中的协议。该协议的关键创新在于不再依赖二进制挑战，而是使用一个较大的挑战集 $\mathcal{C}$。其可靠性证明基于两个假设：**强根假设**和**$\gamma$-低阶假设**。证明思路是，如果存在一个恶意证明者能对同一个承诺给出两个不同挑战下的正确应答，就能构造出算法来解出强根问题（当挑战差值不是2的幂时）或找到低阶元素（当挑战差值是2的幂或者证明者注入低阶元素时）。这使得挑战空间可以扩大（如 $2^{10}$），从而将协议重复次数从 $\lambda$ 次降低到 $\lambda/10$ 次，显著提高了通信效率。该协议是诚实验证者统计零知识的。

2.  **交互式设置协议（ISetup）**：为了让ZKAoK的归约可行，需要保证公共生成元 $g_q$ 是真随机生成的。本文设计了ISetup协议,让所有方共同生成一个随机素数 $\tilde{q}$，并基于此确定性地生成基础参数 $(\tilde{s}, f, \hat{g}_q, \widehat{G}, F)$。然后各方贡献一个随机份额 $t_i$，通过承诺和零知识证明（利用“最小公倍数技巧”证明份额的离散对数），最终计算 $g_q = \prod_i \hat{g}_q^{t_i}$。这保证了 $g_q$ 的随机性，且各方均不知道其完整的离散对数，为依赖强根假设的证明铺平了道路。

3.  **阈值EC-DSA协议**：协议整体遵循[GG18]的框架，但在关键的乘法转加法（MtA）步骤中，将底层的Paillier加密替换为CL加密，并使用了新设计的ZKAoK。图3和4描述了完整的IKeyGen和ISign协议。
    *   **IKeyGen**：各方通过Feldman-VSS分享自己的随机值 $u_i$，最终得到 $x$ 的 $(t,n)$ Shamir秘密分享。同时，各方通过ISetup协议生成CL加密的参数和密钥对。
    *   **ISign**：给定一个大小为 $t$ 的签名集 $S$，各方首先将 $x$ 的 $(t,n)$ 分享转换为 $(t,t)$ 分享 $w_i$。签名过程分为五个阶段。**Phase 1**：各方广播自己 $k_i$ 的CL加密和 $\gamma_i P$ 的承诺，并附上ZKAoK证明密文格式正确。**Phase 2**：各方两两执行MtA协议。例如，$P_i$ 利用 $P_j$ 的密文 $c_{k_j}$ 和同态性，计算 $c_{k_j \gamma_i}$ 和 $c_{k_j w_i}$，并加上自己的随机掩码 $\beta_{j,i}$ 和 $\nu_{j,i}$。$P_j$ 解密后得到部分和，并验证 $P_i$ 使用了正确的 $w_i$。**Phase 3-4**：各方广播 $\delta_i$，计算 $\delta = k\gamma$ 和 $R = \delta^{-1}(\sum \Gamma_i) = k \cdot P$，得到签名分量 $r$。**Phase 5**：各方计算并交换额外的屏蔽值和证明，以防止在公开自己的签名份额 $s_i = k_i m + \sigma_i r$ 时泄露信息，最终组合得到有效签名 $s$。

整个协议的通信复杂度主要由ZKAoK的大小、密文长度和承诺大小决定。由于避免了范围证明，且CL密文和群元素尺寸在更高安全级别相对于Paillier更有优势，因此协议在带宽上对所有安全级别都有显著提升。计算复杂度上，CL群运算在低安全级别时比Paillier模指数慢，但在192位安全性以上开始反超。

### 核心公式与流程

**[CL加密方案 (Fig. 1)]**
$$
\begin{aligned}
&\mathsf{KeyGen}(1^\lambda): \quad \mathsf{sk} \stackrel{\$}{\leftarrow} [\tilde{A}], \quad \mathsf{pk} := g_q^{\mathsf{sk}}  \\
&\mathsf{Enc}(\mathsf{pk}, m): \quad r \stackrel{\$}{\leftarrow} [\tilde{A}], \quad c_1 := g_q^r, \quad c_2 := \mathsf{pk}^r f^m \\
&\mathsf{Dec}(\mathsf{sk}, (c_1, c_2)): \quad M := c_2 / c_1^{\mathsf{sk}}
\end{aligned}
$$
> 作用：定义了一个明文空间为 $\mathbf{Z}/q\mathbf{Z}$ 的加法同态加密。安全性依赖于HSM假设，即区分 $G^q$（由 $g_q$ 生成）中的元素和 $G$（由 $g = g_q f$ 生成）中的元素是困难的。其关键特性是消息空间 $q$ 可设为EC-DSA所使用的素数。

**[ZKAoK协议 (Fig. 2)]**
- Prover $( \mathsf{pk}, \mathbf{c} = (c_1, c_2) )$ 拥有 $(a, r)$ s.t. $c_1 = g_q^r, c_2 = \mathsf{pk}^r f^a$.
- 步骤：
    1.  Prover 采样 $r_1 \stackrel{\$}{\leftarrow} [\tilde{A} C (2^{40})]$, $r_2 \stackrel{\$}{\leftarrow} \mathbf{Z}/q\mathbf{Z}$, 计算 $t_1 := g_q^{r_1}$, $t_2 := \mathsf{pk}^{r_1} f^{r_2}$, 发送 $(t_1, t_2)$.
    2.  Verifier 发送挑战 $k \stackrel{\$}{\leftarrow} \mathcal{C}$.
    3.  Prover 计算 $u_1 := r_1 + k r \in \mathbf{Z}$, $u_2 := r_2 + k a \in \mathbf{Z}/q\mathbf{Z}$, 发送 $(u_1, u_2)$.
    4.  Verifier 检查 $u_1 \in [\tilde{A} C (2^{40}+1)]$ 且 $g_q^{u_1} = t_1 c_1^k$, $\mathsf{pk}^{u_1} f^{u_2} = t_2 (c_2)^k$.
> 作用：证明一个CL密文是格式正确的，即知道其中的明文和加密随机数。其可靠性基于强根假设和低阶假设，允许挑战集 $\mathcal{C}$ 的大小大于2，从而减少重复轮数，降低通信开销。

**[交互式设置协议 (ISetup)]**
- Step 1: 各方共同生成随机素数 $\tilde{q}$。
- Step 2: 基于 $\tilde{q}$ 和 $q$ 确定性地生成参数 $(\tilde{s}, f, \hat{g}_q, \widehat{G}, F)$。各方采样随机 $t_i$，广播 $g_i = \hat{g}_q^{t_i}$ 及其承诺与ZKP。最终计算公共生成元 $g_q = \prod_i g_i$。
> 作用：确保公共参数 $g_q$ 是真随机生成的，这对于ZKAoK的可靠性归约（需要将外部输入的随机元素 $g_q$ 喂给恶意证明者）是必需的。此协议可以在IKeyGen中并行执行。

**[阈值签名的核心步骤]**
1.  计算乘法秘密 $k\gamma$: 各方计算 $\delta_i = k_i\gamma_i + \sum_{j\neq i}(\alpha_{i,j}+\beta_{j,i})$，广播后求和得到 $\delta = k\gamma$.
2.  计算 $R$: $R = \delta^{-1}(\sum_i \Gamma_i) = k^{-1}P$, $r = H'(R)$.
3.  计算签名部分 $s_i$: $s_i = k_i m + \sigma_i r$.
4.  验证签名：$s = \sum_i s_i$. 如果 $(r, s)$ 是有效EC-DSA签名则输出。
> 作用：步骤1-3是阈值签名生成的核心逻辑，其中 $\alpha_{i,j}, \beta_{j,i}$ 等是通过MtA协议计算 $k_j\gamma_i$ 和 $k_jw_i$ 得到的加性分享，Phase 5中的额外检查用于防止恶意方在公布 $s_i$ 时提供错误值。

### 实验结果
本文对提出的协议进行了理论和实验性能评估，并与[GG18]和[LN18]进行了对比。实验使用NIST曲线P-256（128位安全）、P-384（192位安全）和P-521（256位安全）。对比基线包括[LN18]的协议，[GG18]的安全版本（包含范围证明）及其“剥离版本”（省略了范围证明，但作者承认此举会泄露密钥信息）。

**主要结论**：
*   **通信成本**：在所有安全级别上，本文协议（ISign）的带宽消耗比此前最安全的协议[LN18]和[GG18]安全版低4.4到9倍。即使是与[GG18]的非安全剥离版相比，本文协议在带宽上依然有优势。
*   **密钥生成**：本文的IKeyGen通信成本比此前方案一致的低约2倍。
*   **计算时间**：在标准安全级别（112和128位），本文协议比[LN18]慢最多4倍。但在192位安全级别时，本文协议速度与其持平或更快；在256位安全级别，本文协议的签名速度是其他所有安全方案的两倍快。这主要是因为类群群运算的开销增长慢于Paillier模指数（$N^2$）。
*   **轮数**：ISign需要8轮，与[LN18]相同，比[GG18]的9轮少一轮。

在假设标准化设置（即CL参数公开固定）的情况下，本文IKeyGen的带宽消耗可再降低6到16倍，这进一步凸显了其带宽优势。

### 局限性与开放问题
本文提出的协议在低安全级别（128位）时的计算开销仍高于[LN18]的方案，这源于类群群运算本身的复杂性。尽管通过避免范围证明减少了操作次数，但单次群运算的成本在此时是瓶颈。此外，协议的安全性依赖于类群中的强根假设、低阶假设和HSM假设，相较于更标准的数论假设（如DDH、RSA），这些假设的研究历史和受信任程度相对较浅。交互式设置协议（ISetup）虽然增进了安全性保证，但也增加了在低安全场景下的延迟。进一步的工作可以探索如何将本文的证明技术应用于其他基于隐藏阶群的密码学协议，或者寻找更低计算复杂度的群来实现类似的带宽优势。

### 强关联论文

[GG18] Gennaro, R., Goldfeder, S. Fast multiparty threshold ECDSA with fast trustless setup. **ACM CCS 2018** [Google Scholar](https://scholar.google.com/scholar?q=Fast+multiparty+threshold+ECDSA+with+fast+trustless+setup)

[LN18] Lindell, Y., Nof, A. Fast secure multiparty ECDSA with practical distributed key generation and applications to cryptocurrency custody. **ACM CCS 2018** [Google Scholar](https://scholar.google.com/scholar?q=Fast+secure+multiparty+ECDSA+with+practical+distributed+key+generation+and+applications+to+cryptocurrency+custody)

[CCL+19] Castagnos, G., Catalano, D., Laguillaumie, F., Savasta, F., Tucker, I. Two-party ECDSA from hash proof systems and efficient instantiations. **CRYPTO 2019** [Google Scholar](https://scholar.google.com/scholar?q=Two-party+ECDSA+from+hash+proof+systems+and+efficient+instantiations)

[CL15] Castagnos, G., Laguillaumie, F. Linearly homomorphic encryption from DDH. **CT-RSA 2015** [Google Scholar](https://scholar.google.com/scholar?q=Linearly+homomorphic+encryption+from+DDH)

[CLT18] Castagnos, G., Laguillaumie, F., Tucker, I. Practical fully secure unrestricted inner product functional encryption modulo p. **ASIACRYPT 2018** [Google Scholar](https://scholar.google.com/scholar?q=Practical+fully+secure+unrestricted+inner+product+functional+encryption+modulo+p)

[Gil99] Gilboa, N. Two party RSA key generation. **CRYPTO 1999** [Google Scholar](https://scholar.google.com/scholar?q=Two+party+RSA+key+generation)

[DF02] Damgård, I., Fujisaki, E. A statistically-hiding integer commitment scheme based on groups with hidden order. **ASIACRYPT 2002** [Google Scholar](https://scholar.google.com/scholar?q=A+statistically-hiding+integer+commitment+scheme+based+on+groups+with+hidden+order)

[MR01] MacKenzie, P.D., Reiter, M.K. Two-party generation of DSA signatures. **CRYPTO 2001** [Google Scholar](https://scholar.google.com/scholar?q=Two-party+generation+of+DSA+signatures)

[DKLs18] Doerner, J., Kondi, Y., Lee, E., Shelat, A. Secure two-party threshold ECDSA from ECDSA assumptions. **IEEE Symposium on Security and Privacy 2018** [Google Scholar](https://scholar.google.com/scholar?q=Secure+two-party+threshold+ECDSA+from+ECDSA+assumptions)

[BBF18] Boneh, D., Bünz, B., Fisch, B. A survey of two verifiable delay functions. **Cryptology ePrint Archive 2018** [Google Scholar](https://scholar.google.com/scholar?q=A+survey+of+two+verifiable+delay+functions)


## 关键词

+ 门限EC-DSA
+ 带宽优化
+ 多方签名协议
+ 范围证明消除
+ 不诚实多数安全
+ 密钥生成协议