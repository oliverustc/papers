---
title: "Coconut: Threshold issuance selective disclosure credentials with applications to distributed ledgers"
标题简称:
论文类型: preprint
预印本简称: arxiv
发表年份: 2018
---

## Coconut: Threshold issuance selective disclosure credentials with applications to distributed ledgers

## 发表信息

+ [原文链接](https://arxiv.org/abs/1802.07344#)

## 作者

+ Alberto Sonnino 
+ Mustafa Al-Bassam 
+ Shehar Bano 
+ [Sarah Meiklejohn](Sarah%20Meiklejohn.md)
+ George Danezis 


## 笔记

### 背景与动机
在分布式账本系统（如以太坊 [53]、Hyperledger [15] 和 Chainspace [1]）中，智能合约的执行结果记录在公开的区块链上，这导致了隐私泄露的风险。选择性披露凭证 [16, 19] 允许用户向验证者证明其拥有经过认证的属性，同时仅披露部分信息，是实现隐私保护的关键技术。然而，现有的方案存在严重的缺陷：一些方案将凭证签名密钥委托给单一发行方，一旦该发行方被恶意攻破，便能够伪造任意凭证；另一些方案则缺乏在实用场景中部署所需的效率、可重随机化或盲签发性质。没有任何一种现有方案能同时提供效率、分布式阈值签发、私有属性、可重随机化以及不可链接的多重选择性披露。这个空白严重限制了选择性披露凭证在智能合约平台上的应用，因为这些平台通常依赖拜占庭容错假设来保障完整性，而现有的凭证方案无法满足类似的分布式信任需求。Coconut 旨在解决这些挑战，它允许一组去中心化的、相互不信任的权威节点共同签发凭证，即使部分节点被攻破或离线，也无法伪造凭证，同时保证了凭证签发的盲性、多次出示的不可链接性以及与验证者勾结情况下的隐私保护。

### 相关工作

[52] Waters, B. Efficient Identity-Based Encryption Without Random Oracles. **Eurocrypt 2005** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+Identity-Based+Encryption+Without+Random+Oracles)
> 核心思路：提出了一种基于双线性映射的身份基加密方案，其结构是Coconut构建多属性凭证的基础。
> 局限与区别：原始的Waters签名不支持盲签发或不可链接性，且无法在多发行方场景下进行聚合。

[36] Lu, S. et al. Sequential Aggregate Signatures, Multisignatures, and Verifiably Encrypted Signatures Without Random Oracles. **Journal of Cryptology 2013** [Google Scholar](https://scholar.google.com/scholar?q=Sequential+Aggregate+Signatures,+Multisignatures,+and+Verifiably+Encrypted+Signatures+Without+Random+Oracles)
> 核心思路：提出了顺序聚合签名方案，可以在多个签名者之间聚合签名。
> 局限与区别：聚合过程需要各签名方按顺序通信，增加了延迟与通信成本，而Coconut支持由任意第三方独立进行非交互式聚合。

[9] Boneh, D. et al. Aggregate and Verifiably Encrypted Signatures from Bilinear Maps. **Eurocrypt 2003** [Google Scholar](https://scholar.google.com/scholar?q=Aggregate+and+Verifiably+Encrypted+Signatures+from+Bilinear+Maps)
> 核心思路：提出了在BLS签名基础上构建的聚合签名方案。
> 局限与区别：虽然支持非交互式聚合，但不具备凭证系统中必需的盲签发、可重随机化和不可链接性。

[16] Camenisch, J., Lysyanskaya, A. Signature Schemes and Anonymous Credentials from Bilinear Maps. **Crypto 2004** [Google Scholar](https://scholar.google.com/scholar?q=Signature+Schemes+and+Anonymous+Credentials+from+Bilinear+Maps)
> 核心思路：提出了CL签名方案，是匿名凭证系统的奠基性工作。
> 局限与区别：凭证大小随属性数量线性增长，计算开销大，且不支持阈值聚合。

[6] Bichsel, P. et al. Cryptographic Protocols of the Identity Mixer Library. **Technical Report 2009** [Google Scholar](https://scholar.google.com/scholar?q=Cryptographic+Protocols+of+the+Identity+Mixer+Library)
> 核心思路：提出了Idemix匿名凭证系统。
> 局限与区别：凭证大小与属性数量线性相关，且不支持阈值聚合。

[43] Pointcheval, D., Sanders, O. Short Randomizable Signatures. **RSA Conference 2016** [Google Scholar](https://scholar.google.com/scholar?q=Short+Randomizable+Signatures)
> 核心思路：提出了高效的短随机化签名方案，凭证仅包含两个群元素。
> 局限与区别：该方案仅支持顺序聚合，不支持阈值聚合，无法直接用于分布式签发场景。

[26] Garman, C. et al. Decentralized Anonymous Credentials. **NDSS 2014** [Google Scholar](https://scholar.google.com/scholar?q=Decentralized+Anonymous+Credentials)
> 核心思路：提出了一个集成到分布式账本中的去中心化匿名凭证系统。
> 局限与区别：凭证出示需要昂贵的双重离散对数证明，凭证安全性依赖于账本本身的安全性，且不关注通用的阈值签发。

### 核心技术与方案
Coconut 的核心构建思路是将 Pointcheval-Sanders（PS）签名 [43] 与 BLS 签名 [10] 中的哈希概念相结合。PS 签名提供高效的可随机化和盲签发，但其签名算法依赖签名者自选的随机数，无法直接实现阈值分发。为了突破这一限制，Coconut 采用了 BLS 中的确定性哈希函数，使得所有授权方可以对同一个待签消息唯一地推导出群元素 $h = H(m)$，从而将 PS 签名转化为一个可阈值化的结构。

具体构建过程如下：系统建立在类型-3 双线性群 $(\mathbb{G}_1, \mathbb{G}_2, \mathbb{G}_T)$ 上，阶为素数 $p$。核心算法包括：
1.  **Setup**：生成公共参数，包括群描述、生成元 $g_1, g_2, h_1$。
2.  **TTPKeyGen**：由可信第三方执行（可通过分布式密钥生成协议实现 [27, 33]）。选取两个 $t-1$ 次多项式 $v, w$，其常数项 $(x, y) = (v(0), w(0))$ 构成主密钥。为每个授权方 $i$ 分发子密钥 $sk_i = (x_i, y_i) = (v(i), w(i))$，并公布其验证公钥 $vk_i = (g_2, g_2^{x_i}, g_2^{y_i})$。
3.  **IssueCred**：用户生成一次性 El-Gamal 密钥对 $(d, \gamma = g_1^d)$，计算承诺 $c_m = g_1^m h_1^o$ 和 $h = H(c_m)$，并对 $h^m$ 进行 El-Gamal 加密。用户将包含零知识证明的 $\Lambda$ 发送给授权方。授权方验证证明后，利用 El-Gamal 的同态性生成加密签名 $\tilde{c}_i = (a^{y_i}, h^{x_i} b^{y_i})$。用户对 $\tilde{c}_i$ 解密后得到部分凭证 $\sigma_i = (h, h^{x_i + y_i \cdot m})$。
4.  **AggCred**：用户收集到 $t$ 个有效的部分凭证后，通过拉格朗日插值计算聚合凭证 $\sigma = (h, \prod_{i=1}^t s_i^{l_i})$。在指数上，这等同于计算 $h^{v(0) + w(0) \cdot m}$。
5.  **ProveCred & VerifyCred**：用户随机化凭证 $\sigma' = (h^{r'}, s^{r'})$，并生成一个绑定到验证者公钥的零知识证明 $\pi_v$，证明其拥有满足谓词 $\phi'$ 的私密属性 $m$。验证者利用配对运算 $e(h', \kappa) = e(s' \nu, g_2)$ 以及 $\pi_v$ 的零知识证明来验证凭证的合法性。

该方案支持将多个属性打包进一个凭证而不增加其大小。凭证大小恒为两个 $\mathbb{G}_1$ 元素。安全性依赖于 LRSW 和 XDH 假设。**Unforgeability** 通过拉格朗日插值的信息论性质（需 $t$ 个正确部分）及底层签名方案的不可伪造性保证。**Blindness** 由 Pedersen 承诺的隐藏性、El-Gamal 加密的 IND-CPA 安全性以及底层 Pointcheval-Sanders 签名的盲性共同保证（需 XDH 假设）。**Unlinkability** 由凭证的随机化操作和零知识证明的性质保证（需 XDH 假设）。通信复杂度方面，签发阶段与授权方数量 $n$ 线性相关，而凭证的出示与验证阶段的通信量均为常数 $O(1)$，与授权方数量无关。

### 核心公式与流程

**[聚合凭证的正确性验证]**
$$
s = \prod_{i=1}^t (s_i)^{l_i} = \prod_{i=1}^t \left(h^{x_i + y_i \cdot m}\right)^{l_i} = h^{v(0) + w(0) \cdot m} = h^{x + y \cdot m}
$$
> 作用：该式通过拉格朗日插值在指数上重建主密钥，验证了聚合凭证的正确性。

**[绑定验证的配对检查]**
$$
e(h', \kappa) = e(h', g_2^{(x + m y + r)}) = e(g_1, g_2)^{(x + m y + r) \tilde{r}}
$$
$$
e(s' \nu, g_2) = e(h'^{(x + m y + r)}, g_2) = e(g_1, g_2)^{(x + m y + r) \tilde{r}}
$$
> 作用：该配对等式构成了VerifyCred算法的核心检查，验证凭证的有效性并绑定到特定的验证者公钥。

### 实验结果
实验在 Python 实现上进行，采用 Barreto-Naehrig 曲线和 OpenSSL 后端。所有加密原语均在一台 3.6GHz Intel Xeon 的 8 核台式机上测量，每个结果基于 10,000 次运行。PrepareBlindSign 和 BlindSign 的平均执行时间分别为 2.6ms 和 3.4ms，显著快于验证操作 VerifyCred 的 10.5ms，后者因包含配对运算而最耗时。凭证大小恒定为 132 字节。当包含一个私有属性时，请求（Request）和验证（Verify）交易的通信开销最大，分别达到 516 字节和 355 字节，这部分开销主要来自零知识证明。在链上部署方面，Chainspace 实现中，验证（Verify）操作平均耗时约 10.8ms，而签发（Issue）操作的检查过程（Checker）仅需 0.024ms，两者相差两个数量级。以太坊实现的 Gas 成本较高，验证函数（Verify）消耗约 2,150,000 Gas，截至 2018年2月，这相当于约 1.74 至 43.5 美元的费用，其主要瓶颈在于以太坊虚拟机（EVM）中 $\mathbb{G}_2$ 上的标量乘法运算。此外，针对分布于全球 10 个 AWS 区域的授权节点进行的实验表明，客户端感知的延迟随阈值参数 $t$ 线性增长，从 $t=1$ 的约 30ms 到 $t=10$ 的约 590ms。

### 局限性与开放问题
Coconut 继承了底层 Shamir 秘密分享协议的局限性，即当系统中增加或移除授权节点时，需要重新运行整个密钥生成算法；这一缺陷可以通过引入主动式秘密分享技术 [29] 来缓解，但频繁的密钥轮转会降低凭证的隐私保护效果。与所有阈值系统一样，当恶意的授权节点数量超过阈值 $t$ 时，系统的安全性将完全丧失，例如攻击者可以在混币器应用中窃取资金或在请愿系统中伪造身份。在以太坊上的实现成本较高，主要由于需要自行实现 $\mathbb{G}_2$ 上的椭圆曲线运算；通过交换 $\mathbb{G}_1$ 和 $\mathbb{G}_2$ 上的操作并依赖更强的 SXDH 假设 [44]，可以大幅降低 Gas 成本。

### 强关联论文

[52] Waters, B. Efficient Identity-Based Encryption Without Random Oracles. **Eurocrypt 2005**

[36] Lu, S. et al. Sequential Aggregate Signatures, Multisignatures, and Verifiably Encrypted Signatures Without Random Oracles. **Journal of Cryptology 2013**

[9] Boneh, D. et al. Aggregate and Verifiably Encrypted Signatures from Bilinear Maps. **Eurocrypt 2003**

[16] Camenisch, J., Lysyanskaya, A. Signature Schemes and Anonymous Credentials from Bilinear Maps. **Crypto 2004**

[43] Pointcheval, D., Sanders, O. Short Randomizable Signatures. **RSA Conference 2016**

[26] Garman, C. et al. Decentralized Anonymous Credentials. **NDSS 2014**

[37] Lysyanskaya, A. et al. Pseudonym Systems. **SAC 1999**

[8] Boldyreva, A. Efficient Threshold Signature, Multisignature and Blind Signature Schemes Based on the Gap-Diffie-Hellman-Group Signature Scheme. **IACR ePrint 2002**

[27] Gennaro, R. et al. Secure Distributed Key Generation for Discrete-Log Based Cryptosystems. **Eurocrypt 1999**

[33] Kate, A. et al. Distributed Key Generation in the Wild. **IACR ePrint 2012**


## 关键词

+ Coconut选择性披露凭证方案
+ 分布式阈值签发区块链凭证
+ 不可链接属性披露重随机化
+ 匿名支付电子请愿代理分发
+ 智能合约凭证隐私保护