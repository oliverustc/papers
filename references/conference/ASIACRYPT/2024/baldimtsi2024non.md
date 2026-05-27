---
title: "Non-Interactive Blind Signatures: Post-Quantum and Stronger Security"
doi: 10.1007/978-981-96-0888-1_3
标题简称:
论文类型: conference
会议简称: ASIACRYPT
发表年份: 2024
created: 2025-05-09 09:38:33
modified: 2025-05-09 09:47:30
---
## Non-Interactive Blind Signatures: Post-Quantum and Stronger Security

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-981-96-0888-1_3)
+ [archive](https://eprint.iacr.org/2024/614)

## 作者

+ [Foteini Baldimtsi](Foteini%20Baldimtsi.md)
+ Jiaqi Cheng
+ Rishab Goyal
+ Aayush Yadav

## 笔记

### 背景与动机
非交互式盲签名由 Hanzlik 于 Eurocrypt 2023 提出 [Han23]，允许签名者异步地为任意接收者生成部分签名（预签名），接收者随后可提取出对随机消息的盲签名。这绕过了传统盲签名固有的两轮交互下限，为电子现金、匿名令牌等无需特定消息结构的应用提供了更高效的解决方案。然而，Hanzlik 定义的盲性属性仅提供了较弱的隐私保障，未能抵御攻击者获取部分预签名与对应消息—签名对之间的关联攻击，例如当攻击者为同一接收者生成多个预签名时，可推断出该接收者的身份。同时，现有构造依赖双线性配对，无法抵御量子攻击，而设计高效的后量子 NIBS 被 Hanzlik 列为重要开放问题。本文旨在填补这两项空白：提出更强的 NIBS 盲性定义框架，并构造首个实用的后量子 NIBS 方案，同时探索基于电路隐私同态加密的通用构造范式。

### 相关工作

[AKSY22] Shweta Agrawal, Elena Kirshanova, Damien Stehlé, and Anshu Yadav. Practical, round-optimal lattice-based blind signatures. **ACM CCS 2022** [Google Scholar](https://scholar.google.com/scholar?q=Practical%20round-optimal%20lattice-based%20blind%20signatures)
> 核心思路：利用格上的 NIZK for linear relations 实例化 Fischlin 范式，构造了两轮盲签名，签名大小 45 KB，总交互 1.5 KB。
> 局限与区别：方案是交互式的，且安全性依赖 one-more ISIS 假设，该假设易受线性组合攻击，参数选择受限。

[Han23] Lucjan Hanzlik. Non-interactive blind signatures for random messages. **EUROCRYPT 2023** [Google Scholar](https://scholar.google.com/scholar?q=Non-interactive%20blind%20signatures%20for%20random%20messages)
> 核心思路：首次形式化 NIBS，基于 VRF、数字签名和双模式 NIZK 提供通用构造，并给出基于配对的高效实例化。
> 局限与区别：盲性定义较弱，仅覆盖接收者盲性和随机数盲性，未考虑攻击者通过 Obtain 预言机获取关联信息的场景；所有构造依赖双线性配对，不具备后量子安全性。

[LNP22b] Vadim Lyubashevsky, Ngoc Khanh Nguyen, and Maxime Plançon. Lattice-based zero-knowledge proofs and applications: Shorter, simpler, and more general. **CRYPTO 2022** [Google Scholar](https://scholar.google.com/scholar?q=Lattice-based%20zero-knowledge%20proofs%20and%20applications)
> 核心思路：设计高效的格基 NIZK 证明线性关系，可直接用于实例化盲签名中的证明系统。
> 局限与区别：本文将其作为构建后量子 NIBS 的底层工具，并结合随机化 one-more ISIS 假设。

[dK22] Rafael del Pino and Shuichi Katsumata. A new framework for more efficient round-optimal lattice-based (partially) blind signature via trapdoor sampling. **CRYPTO 2022** [Google Scholar](https://scholar.google.com/scholar?q=A%20new%20framework%20for%20more%20efficient%20round-optimal%20lattice-based%20(partially)%20blind%20signature)
> 核心思路：将 Fischlin 范式适配到格上，通过格陷门采样实现两轮盲签名，签名约 102 KB，支持无界签名。
> 局限与区别：仍为交互式两轮方案，交互开销为 0.96 KB 且公钥较大。

[BLNS23a] Ward Beullens, Vadim Lyubashevsky, Ngoc Khanh Nguyen, and Gregor Seiler. Lattice-based blind signatures: Short, efficient, and round-optimal. **Cryptology ePrint Archive, Report 2023/077** [Google Scholar](https://scholar.google.com/scholar?q=Lattice-based%20blind%20signatures%3A%20Short%2C%20efficient%2C%20and%20round-optimal)
> 核心思路：通过将哈希计算的负担转移给接收者，将签名压缩至 22 KB，安全性基于 MSIS 和 MLWE。
> 局限与区别：接收者首轮消息体积巨大（>100 KB），且方案仍为交互式。

### 核心技术与方案

本文的主要技术贡献分为三个层次。

**1. 更强的盲性定义框架。** 针对 Hanzlik 定义无法抵御攻击者通过 Obtain 预言机获取预签名与消息—签名对的关联这一缺陷，本文提出强接收者盲性和强随机数盲性。这两个定义允许攻击者查询除挑战预签名外所有预签名的 Obtain 结果，从而模拟攻击者能够部分绕过盲性的实际场景。形式上，在挑战阶段之外，攻击者可以自由获得 $( \mathsf {sk} _ {R_0}, \mathsf {sk} _ {R_1})$ 的 Obtain 预言机访问，但禁止查询挑战预签名对应的随机数。这是对 IND-CCA 风格的盲性推广。

**2. 基于电路隐私 LHE 的通用构造。** 本文展示了电路隐私的分级同态加密（LHE）可将任何标准数字签名方案升级为 NIBS，且最终签名大小保持最优（与标准签名相同）。接收者公钥是 LHE 加密下的 PRF 密钥 K 的密文 ct；签名者使用 LHE 同态计算电路 $C_{\mathsf{sk}, r}(K)= \mathsf{S.Sign}(\mathsf{sk}, F_K(r))$，得到密文 $\widehat{\mathsf{ct}}$，并附上 NIZK 证明该计算正确。接收者解密 $\widehat{\mathsf{ct}}$ 获得签名 $\sigma$，计算消息为 $F_K(r)$。安全性：零知识保证盲性，IND-CPA 安全保证密文不泄露 K，电路隐私保证签名者无法从 $ \widehat{\mathsf{ct}}$ 推导出签名内容。该构造在 KOSK 模型下证明一次性不可伪造性，但通过附录 A 的通用编译器可转换为标准模型安全（需额外 NIZK 证明密钥知识）。

**3. 实用的后量子 NIBS 构造。** 本文提出基于格的后量子 NIBS 方案，安全性依赖新引入的随机化 one-more ISIS 假设（rOM-ISIS）。直觉上，该假设阻止攻击者获得任意目标向量的短原像：挑战者使用随机 $\pm 1$ 向量 y 重随机化攻击者查询的目标 $\widehat{\mathbf{t}}$，返回满足 $\mathbf{A}\cdot\widehat{\mathbf{x}}+\mathbf{B}\cdot\widehat{\mathbf{y}}=\widehat{\mathbf{t}}$ 的短向量 $\widehat{\mathbf{x}}$ 和 $\widehat{\mathbf{y}}$。攻击者无法通过线性组合攻击得到足够多的短原像，因为 y 的 $\pm1$ 约束限制了代数操作。

具体方案：设公共参数为 $\mathbf{A},\mathbf{B}\in\mathbb{Z}_q^{n\times 2m}$，一个 PKE 和一个 NIZK 系统。签名者陷门为 $\mathbf{T}_{\mathbf{C}}$，验证密钥为 $\mathbf{C}$。接收者密钥为 $\mathbf{x}\leftarrow\mathcal{D}_{\mathbb{Z}^{2m},\varsigma/m}$ 和 $\delta$，公钥 $\mathbf{t}= \mathbf{A}\cdot\mathbf{x} + H(\delta)$。签名者针对接收者公钥 $\mathbf{t}$，采样随机 $\mathbf{y}\in\{\pm 1\}^{2m}$，计算短向量 $\mathbf{z}$ 满足 $\mathbf{C}\cdot\mathbf{z} = \mathbf{t} - \mathbf{B}\cdot\mathbf{y}$，然后发送预签名 $\mathsf{psig}=\mathbf{z}$ 和随机数 $\mathsf{nonce}=\mathbf{y}$。接收者验证 $\mathbf{C}\cdot\mathbf{z} + \mathbf{B}\cdot\mathbf{y}= \mathbf{A}\cdot\mathbf{x} + H(\delta)$ 且 $\mathbf{z}$ 短、$\mathbf{y}$ 为 $\pm1$ 向量，然后加密 $(\mathbf{x},\mathbf{y},\mathbf{z})$ 得到密文 ct，并生成 NIZK 证明 $\pi$ 说明存在 $(\mathbf{x},\mathbf{y},\mathbf{z},r)$ 使得 $\mathbf{C}\cdot\mathbf{z} + \mathbf{B}\cdot\mathbf{y} = \mathbf{A}\cdot\mathbf{x} + H(\delta)$ 且 $\mathbf{w}= \mathbf{A}_L\cdot\mathbf{x}_\perp + \mathbf{A}_R\cdot\mathbf{z}_\perp$，其中 $\mathbf{w}$ 是消息 $\mu$ 的一部分。最终签名 $\sigma=(\pi,\mathsf{ct})$，消息 $\mu=(\mathbf{w},\delta)$。

安全性直觉：一次性不可伪造性通过 rOM-ISIS 假设保证：如果攻击者能伪造 $\ell+1$ 个有效签名，则提取出其 $(\mathbf{x}_j,\mathbf{y}_j,\mathbf{z}_j)$ 可打破 rOM-ISIS。盲性由 NIZK 的零知识性和 PKE 的 IND-CPA 安全性保证，因为 NIZK 证明可模拟，而密文隐藏了接收者的秘密。参数选择（$n=\mathrm{poly}(\lambda), m>n\log q+\lambda, \varsigma/m=\Omega(1), \beta<m\varsigma$）确保可对抗已知攻击。

### 核心公式与流程

**Fischlin 范式在 NIBS 中的扩展（通用构造核心关系）**
$$
c = \mathsf{COM}(m) \quad \text{ 接收者发送盲化消息 } c \text{ 给签名者。}
$$
$$
\sigma' = \mathsf{Sign}(\mathsf{sk}, c) \quad \text{ 签名者产生对盲化消息的签名。}
$$
$$
\sigma = (\mathsf{Enc}_{\mathsf{pk}_E}(c\|\sigma'), m, \pi) \quad \text{ 接收者输出最终签名，含加密和 NIZK 证明。}
$$
> 作用：描绘将 Fischlin 交互范式适配到非交互设置时的关键结构：接收者公钥扮演 PRF 密钥的承诺，签名者通过随机数 r 非交互地选出消息 $F_K(r)$。

**基于 LHE 的构造（提供最优签名大小）**
$$
\mathsf{sk}_R = (\mathsf{lhe.sk}, K), \quad \mathsf{pk}_R = (\mathsf{lhe.ek}, \mathsf{ct}), \quad \mathsf{ct} = \mathsf{LHE.Enc}(\mathsf{lhe.sk}, K)
$$
$$
\widehat{\mathsf{ct}} = \mathsf{LHE.Eval}(\mathsf{lhe.ek}, C_{\mathsf{sk}, r}, \mathsf{ct}; \rho), \quad \text{其中 } C_{\mathsf{sk}, r}(K) = \mathsf{S.Sign}(\mathsf{sk}, F_K(r))
$$
$$
\mu = F_K(r), \quad \sigma = \mathsf{LHE.Dec}(\mathsf{lhe.sk}, \widehat{\mathsf{ct}})
$$
> 作用：签名者同态计算产生加密签名 $\widehat{\mathsf{ct}}$，接收者解密即得标准签名，保持最优大小（与底层非盲签名一致）。

**基于格的后量子构造（关键关系）**
$$
\mathbf{C}\cdot\mathbf{z} + \mathbf{B}\cdot\mathbf{y} = \mathbf{A}\cdot\mathbf{x} + H(\delta)
$$
> 作用：定义预签名 $\mathbf{z}$ 和随机数 $\mathbf{y}$ 的验证方程，核心安全关系，接收者公钥 $\mathbf{t}=\mathbf{A}\cdot\mathbf{x} + H(\delta)$ 隐含其中。

**rOM-ISIS 假设（核心假设形式）**
$$
\mathbf{A}\cdot\widehat{\mathbf{x}} + \mathbf{B}\cdot\widehat{\mathbf{y}} = \widehat{\mathbf{t}}, \quad \|\widehat{\mathbf{x}}\| \leq \varsigma\sqrt{m}, \quad \widehat{\mathbf{y}} \in \{\pm 1\}^{m}
$$
> 作用：定义攻击者从挑战者处获得的预原像形式，$\widehat{\mathbf{y}}$ 的重随机化防御了已知的线性组合攻击。

**最终签名验证（接收者输出结构）**
$$
\sigma = (\pi, \mathsf{ct}), \quad \mu = (\mathbf{w}, \delta)
$$
$$
1 \leftarrow \mathsf{NIZK.Verify}(\mathsf{nizk.crs}, (\mathbf{C,A,B, pke.pk, ct, w, }\delta), \pi)
$$
> 作用：接收者消息由 $\mathbf{w}=\mathbf{A}_L\cdot\mathbf{x}_\perp + \mathbf{A}_R\cdot\mathbf{z}_\perp$ 和 $\delta$ 构成，签名是 NIZK 证明和加密的密文。

### 实验结果

论文提供了基于格的 NIBS 构造的参数尺寸估算（proof of concept）。实例化基于 Falcon 签名、Regev 类型加密以及 LNP22b 的线性关系 NIZK。具体尺寸如下：接收者公钥 $|\mathsf{pk}_R| = 1.6$ KB，预签名 $|\mathsf{psig}| + |\mathsf{nonce}| = 0.96$ KB，签名 $|\sigma| = 68$ KB。与文献中两轮格基盲签名对比：AKSY22 签名 45 KB 但首轮消息 0.96 KB；BLNS23a 签名 22 KB 但首轮消息 >100 KB。本文方案优势在于 R→S 通信为 0（若存在 PKI，否则仅单次成本），但签名大小（68 KB）略大于 AKSY22。整体通信复杂度为 $0 + 0.96 + 68 = 68.96$ KB，而 AKSY22 为 $0.96 + 0.56 + 45 = 46.52$ KB。该结果表明本文构造在非交互性前提下实现了与最先进交互式方案相当的具体效率。

### 局限性与开放问题
本文提出的强盲性定义虽然更安全，但论文尚未给出满足强盲性且实用的后量子 NIBS 实例化，仅给出了基于 LHE 的通用构造（签名大小最优但公钥和计算开销大），因此将此设计高效实例留给开放问题。同时，rOM-ISIS 假设虽然比 OM-ISIS 更抗攻击，但仍是新假设，其安全性分析尚不充分，未来可能需要更深入的密码分析或寻找更标准的底层假设（如 SIS 或 LWE）来直接证明 NIBS 的安全性。

### 强关联论文

[Han23] Lucjan Hanzlik. Non-interactive blind signatures for random messages. **EUROCRYPT 2023** [Google Scholar](https://scholar.google.com/scholar?q=Non-interactive+blind+signatures+for+random+messages)

[AKSY22] Shweta Agrawal, Elena Kirshanova, Damien Stehlé, and Anshu Yadav. Practical, round-optimal lattice-based blind signatures. **ACM CCS 2022** [Google Scholar](https://scholar.google.com/scholar?q=Practical+round-optimal+lattice-based+blind+signatures)

[LNP22b] Vadim Lyubashevsky, Ngoc Khanh Nguyen, and Maxime Plançon. Lattice-based zero-knowledge proofs and applications: Shorter, simpler, and more general. **CRYPTO 2022** [Google Scholar](https://scholar.google.com/scholar?q=Lattice-based+zero-knowledge+proofs+and+applications)

[Fis06] Marc Fischlin. Round-optimal composable blind signatures in the common reference string model. **CRYPTO 2006** [Google Scholar](https://scholar.google.com/scholar?q=Round-optimal+composable+blind+signatures+in+the+common+reference+string+model)

[dK22] Rafaël del Pino and Shuichi Katsumata. A new framework for more efficient round-optimal lattice-based (partially) blind signature via trapdoor sampling. **CRYPTO 2022** [Google Scholar](https://scholar.google.com/scholar?q=A+new+framework+for+more+efficient+round-optimal+lattice-based+(partially)+blind+signature+via+trapdoor+sampling)

[BLNS23a] Ward Beullens, Vadim Lyubashevsky, Ngoc Khanh Nguyen, and Gregor Seiler. Lattice-based blind signatures: Short, efficient, and round-optimal. **Cryptology ePrint Archive, Report 2023/077** [Google Scholar](https://scholar.google.com/scholar?q=Lattice-based+blind+signatures%3A+Short%2C+efficient%2C+and+round-optimal)

[BNPS03] Mihir Bellare, Chanathip Namprempre, David Pointcheval, and Michael Semanko. The one-more-RSA-inversion problems and the security of Chaum's blind signature scheme. **Journal of Cryptology, 16(3):185–215, 2003** [Google Scholar](https://scholar.google.com/scholar?q=The+one-more-RSA-inversion+problems+and+the+security+of+Chaum%27s+blind+signature+scheme)


## 关键词

+ 非交互式盲签名
+ 后量子密码学
+ 同态加密
+ 隐私保护
+ 数字签名