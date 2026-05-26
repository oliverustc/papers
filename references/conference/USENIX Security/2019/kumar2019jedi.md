---
title: "JEDI: Many-to-Many End-to-End encryption and key delegation for IoT"
标题简称:
论文类型: conference
会议简称: USENIX Security
发表年份: 2019
created: 2025-04-27 08:56:31
modified: 2025-04-27 09:20:23
---

## JEDI: Many-to-Many End-to-End encryption and key delegation for IoT

## 发表信息

+ [原文链接](https://www.usenix.org/conference/usenixsecurity19/presentation/kumar-sam)

## 作者

+ Sam Kumar 
+ [Yuncong Hu](Yuncong%20Hu.md) 
+ Michael P Andersen 
+ [Raluca Ada Popa](Raluca%20Ada%20Popa.md)
+ David E Culler 

## 笔记

好的，作为一名密码学领域的研究助手，我将严格按照您的要求，对这篇USENIX Security 2019论文进行深度阅读，并生成详尽的结构化笔记。

### 背景与动机
随着物联网的普及，大量的传感器和设备收集着用户的隐私敏感数据，对其进行端到端加密以保护传输过程中的数据安全至关重要。然而，现有的端到端加密协议如SSL/TLS和TextSecure [44] 主要针对一对一的通信模式，不适用于大规模工业物联网系统。这些系统需要支持多对多通信，且发送方和接收方是解耦的（例如通过发布/订阅模式），同时要求去中心化的密钥委托机制来实现细粒度的访问控制。此外，物联网设备范围广泛，从强大的服务器到只有几十KB内存的超低功耗嵌入式传感器（如图1所示），加密计算必须足够轻量才能在这些资源受限的设备上运行。现有的方案，如基于信任密钥服务器的模型，存在单点故障和隐私泄露风险；而能够表达复杂访问策略的属性基加密（ABE）虽然功能强大，但其高昂的计算和能量开销使其在低功耗设备上不可行 [74]。本文提出的JEDI协议旨在填补这一空白，其核心目标是设计一种能够同时满足解耦通信、去中心化委托、细粒度权限控制和低功耗设备约束的端到端加密协议。

### 相关工作

[1] Abdalla等. Generalized key delegation for hierarchical identity-based encryption. **EUROCRYPT 2005/ ePrint 2007** [Google Scholar](https://scholar.google.com/scholar?q=Generalized+key+delegation+for+hierarchical+identity-based+encryption)
> 核心思路：提出WKD-IBE方案，允许密钥在单个层次结构中进行通配符委托。
> 局限与区别：JEDI创新性地将其用于并发管理多个层次（URI、时间、撤销），并通过预计算调整等技术使其在低功耗设备上实用。

[12] Bethencourt等. Ciphertext-policy attribute-based encryption. **S&P 2007** [Google Scholar](https://scholar.google.com/scholar?q=Ciphertext-policy+attribute-based+encryption)
> 核心思路：提出CP-ABE，允许将访问策略嵌入密文，密钥与属性集合关联。
> 局限与区别：CP-ABE不适合JEDI的分层资源模型，且其计算开销在低功耗设备上过高 [74]。

[48] Goyal等. Attribute-based encryption for fine-grained access control of encrypted data. **CCS 2006** [Google Scholar](https://scholar.google.com/scholar?q=Attribute-based+encryption+for+fine-grained+access+control+of+encrypted+data)
> 核心思路：提出KP-ABE，密钥与访问结构关联，密文与属性集合关联。
> 局限与区别：KP-ABE的计算开销（比JEDI所选用的WKD-IBE慢一个数量级 [83, 90]），不适合超低功耗的“感测-发送”物联网场景。

[31] Clarke等. Certificate chain discovery in SPKI/SDSI. **Journal of Computer Security 2001** [Google Scholar](https://scholar.google.com/scholar?q=Certificate+chain+discovery+in+SPKI/SDSI)
> 核心思路：提出基于证书链的去中心化授权模型，支持委托和削减。
> 局限与区别：SPKI/SDSI提供了授权证明，但本身不提供端到端加密机制。JEDI在此基础上加上了加密和匿名签名。

[67] Naor等. Revocation and tracing schemes for stateless receivers. **CRYPTO 2001** [Google Scholar](https://scholar.google.com/scholar?q=Revocation+and+tracing+schemes+for+stateless+receivers)
> 核心思路：提出树型广播加密（CS和SD方法），允许向已撤销用户的集合外广播消息。
> 局限与区别：不支持JEDI所需的密钥委托机制。JEDI通过HIBE和“有限委托”属性对其进行了修改，使其支持层级委托。

[5] Andersen等. Democratizing authority in the built environment. **BuildSys 2017** [Google Scholar](https://scholar.google.com/scholar?q=Democratizing+authority+in+the+built+environment)
> 核心思路：bw2是一个为智能建筑设计的、支持去中心化委托的发布/订阅消息系统。
> 局限与区别：bw2不提供端到端加密。JEDI作为其上层协议，为其提供了加密和完整性保证。

[77] Taly等. Distributed authorization in Vanadium. **FOSAD VIII 2016** [Google Scholar](https://scholar.google.com/scholar?q=Distributed+authorization+in+Vanadium)
> 核心思路：Vanadium是一个支持去中心化授权的分布式框架。
> 局限与区别：Vanadium同样专注于授权而非加密。JEDI的密钥委托模型与之类似，但提供了加密实现。

[70] Perrig等. SPINS: Security protocols for sensor networks. **MobiCom 2001** [Google Scholar](https://scholar.google.com/scholar?q=SPINS:+Security+protocols+for+sensor+networks)
> 核心思路：为传感器网络设计的轻量级安全协议，包括µTESLA进行认证广播。
> 局限与区别：SPINS依赖网关进行复杂加密操作。JEDI将加密运行在节点上，避免了网关成为攻击点，并通过混合加密和签名技术与之互补。

### 核心技术与方案

JEDI的整体框架基于一个非标准地使用WKD-IBE [1] 方案。WKD-IBE支持基于模式（Pattern）的加密和密钥委托，其中模式包含固定组件（filled）和自由组件（free）。密钥委托的过程就是通过KeyDer函数将自由组件逐步固定的过程。

1.  **并发层次结构与加密**：JEDI将WKD-IBE模式中的槽位（slots）划分为三个并发的层次结构：URI层次（深度 ℓ1）、时间层次（深度 ℓ2）和撤销层次（深度 ℓ3）。一个消息的加密模式通过将URI路径和当前时间戳分别映射到前ℓ1和接下来的ℓ2个槽位中来构造。例如，URI `a/b` 被编码为 (H(“a”), H(“b”), H(“$”))，其中“$”是终止符。时间戳2017年6月8日6时被编码为后4个槽位。加密时，首先采样一个对称密钥k，然后用WKD-IBE对k加密生成c1，再用k对消息进行对称加密生成c2。此后，在同一小时内，后续消息只需重复使用c1和新c2，直到WKD-IBE模式因时间变化而改变。这大大减少了WKD-IBE的调用频率。

2.  **低功耗优化：预计算与调整**：WKD-IBE加密的核心是计算 $Q_S = g_3 \cdot \prod_{(i, a_i) \in \text{fixed}(S)} h_i^{a_i}$。由于相邻时间的加密模式S和T只在时间层级最后几个槽位不同，可以高效地将已计算的QS调整为QT，其计算量仅为两个模式间汉明距离的 $\mathbb{G}_1$ 指数运算。例如，当T与S仅在最后一小时槽位不同时，只需进行一次指数运算，远快于从头计算。这使得昂贵的配对运算在低功耗设备上变得可行。

3.  **匿名签名**：JEDI利用WKD-IBE的密钥派生特性来构造匿名签名。签名者使用其密钥对消息m进行KeyDer，将m填入一个额外的槽位，产生的密钥即作为签名。该方案可实现匿名性，因为任何两个拥有同一模式权威密钥的签名者生成的签名在分布上是不可区分的（信息论意义下，定理2）。为了压缩签名大小，JEDI利用了BBG HIBE [17] 的“有限委托”（limited delegation）特性，将签名压缩至两个群元素。

4.  **撤销机制**：JEDI支持基于过期的简单撤销和通过树型广播加密的即时撤销。对于即时撤销，JEDI修改了“完全子树”（CS）方法。CS方法基于一个二叉树，每个节点对应一个HIBE密钥。每个用户对应一个叶子节点，并持有根到叶子路径上所有节点的密钥。JEDI引入一个第三层次（深度ℓ3）来处理撤销，将每个JEDI密钥与一片连续的叶子范围关联。当一个密钥被撤销，加密者使用CS方法，用子树根节点的公钥加密消息，覆盖所有未被撤销的叶子节点。用户使用其持有的HIBE密钥解密。通过HIBE的有限委托属性，可以控制密钥的派生能力，确保一个被撤销的根节点密钥无法派生出子节点的有效密钥。加密开销为 $O(r \log \frac{n}{r})$，其中r是撤销的密钥数，n是叶子总数。

### 核心公式与流程

**[WKD-IBE模式匹配定义]**
对于模式P1和P2，P1匹配P2当且仅当对所有i，要么P1(i)为自由组件，要么P1(i) = P2(i)。这是密钥委托的基础：持有匹配P2的密钥可以派生匹配P1的密钥。

**[预计算调整公式]**
$$Q_{T} = Q_{S}\cdot \prod_{\substack{(i,b_{i})\in \text{fixed}(T)\\ i\in \text{free}(S)}}h_{i}^{b_{i}}\cdot \prod_{\substack{(i,a_{i})\in \text{fixed}(S)\\ i\in \text{free}(T)}}h_{i}^{-a_{i}}\cdot \prod_{\substack{(i,a_{i})\in \text{fixed}(S)\\ (i,b_{i})\in \text{fixed}(T)\\ a_{i}\neq b_{i}}}h_{i}^{b_{i} - a_{i}}$$
> 作用：将上一个加密模式S对应的预计算中间结果QS调整为当前模式T对应的QT，计算开销与S和T之间的汉明距离成正比，显著提升WKD-IBE加密效率。

**[URI/时间到模式的编码示例]**
$$S = \underbrace{H("a"), H("b"), H("$"), \bot, \cdots, \bot}_{\ell_1=4\text{ slots for URI}} \quad \underbrace{H("17"), H("Jun"), H("08"), H("06"), \bot, \cdots, \bot}_{\ell_2=4\text{ slots for Time}}$$
> 作用：展示了消息 `a/b` 在2017年6月8日6时加密时所使用的WKD-IBE模式。其中H是抗碰撞哈希函数。

**[匿名签名匿名性定理]**
> 对于在同一个资源层次中对应同一(URI, time)对的任何格式良好的密钥k1和k2，以及任意消息 m ∈ ℤp*，由k1生成的m的签名分布与k2生成的m的签名分布是信息论不可区分的。
> 作用：保证了在固定消息和模式条件下，即使拥有全部私钥信息的强大敌手也无法区分签名是由哪个主体生成的。

### 实验结果

JEDI在三种硬件平台上进行了评估：配备i7-7820HQ的笔记本电脑、配备Cortex-A53的树莓派3B+，以及基于Cortex-M0+的商用超低功耗传感器平台“Hamilton”。实验结果显示，在笔记本电脑上，WKD-IBE加密、解密和签名等核心操作耗时均在3-5毫秒之间（Fig. 6a）。在使用撤销功能时，加密开销随撤销用户数增长，例如撤销100个用户时，加密时间约为300毫秒（Fig. 6b）。当JEDI被应用于bw2消息系统时，在1 MiB消息的常见场景下，由于对称加密的主导地位，JEDI的发布和接收延迟与未修改的bw2相近（大约50毫秒 vs 40毫秒）（Fig. 7）。在Hamilton平台上，一次WKD-IBE加密需要6.5秒，但通过混合加密和预计算调整优化，该操作每小时仅执行一次。据此估算，以30秒为间隔发送加密数据的传感器，其电池寿命仍可达3.6年（仅加密）和4.7年（加密+签名），相比仅使用AES的10年，开销可接受（Table 3）。这表明JEDI能够在各类物联网设备上，包括最受限的超低功耗传感器，提供实用级别的端到端加密。

### 局限性与开放问题
JEDI的设计并未试图隐藏消息传输的元数据，如URI、发布/订阅关系和时间信息，保护这些元数据是一个互补但至关重要的问题。即时撤销功能虽然强大，但要求发送方了解当前的撤销列表，这在一定程度上削弱了发送方与接收方的解耦性，且当撤销列表动态变化时，其加密开销会显著增长。此外，JEDI的安全性依赖选择性安全（Selective-ID CPA-secure）的WKD-IBE方案，虽然可以通过随机谕言机模型（Random Oracle）获得适应性安全，但这引入了额外的假设。未来工作可以探索如何在保持低功耗性能的同时，将JEDI扩展到更复杂的、非层级化的资源结构。

### 强关联论文

[1] M. Abdalla, E. Kiltz, and G. Neven. Generalized key delegation for hierarchical identity-based encryption. **EUROCRYPT 2005/ ePrint 2007** [Google Scholar](https://scholar.google.com/scholar?q=Generalized+key+delegation+for+hierarchical+identity-based+encryption)

[17] D. Boneh, X. Boyen, and E.-J. Goh. Hierarchical identity based encryption with constant size ciphertext. **EUROCRYPT 2005** [Google Scholar](https://scholar.google.com/scholar?q=Hierarchical+identity+based+encryption+with+constant+size+ciphertext)

[12] J. Bethencourt, A. Sahai, and B. Waters. Ciphertext-policy attribute-based encryption. **S&P 2007** [Google Scholar](https://scholar.google.com/scholar?q=Ciphertext-policy+attribute-based+encryption)

[48] V. Goyal, O. Pandey, A. Sahai, and B. Waters. Attribute-based encryption for fine-grained access control of encrypted data. **CCS 2006** [Google Scholar](https://scholar.google.com/scholar?q=Attribute-based+encryption+for+fine-grained+access+control+of+encrypted+data)

[31] D. Clarke, J.-E. Elien, C. Ellison, M. Fredette, A. Morcos, and R. L. Rivest. Certificate chain discovery in SPKI/SDSI. **Journal of Computer Security 2001** [Google Scholar](https://scholar.google.com/scholar?q=Certificate+chain+discovery+in+SPKI/SDSI)

[67] D. Naor, M. Naor, and J. Lotspiech. Revocation and tracing schemes for stateless receivers. **CRYPTO 2001** [Google Scholar](https://scholar.google.com/scholar?q=Revocation+and+tracing+schemes+for+stateless+receivers)

[5] M. P. Andersen, J. Kolb, K. Chen, D. E. Culler, and R. Katz. Democratizing authority in the built environment. **BuildSys 2017** [Google Scholar](https://scholar.google.com/scholar?q=Democratizing+authority+in+the+built+environment)

[70] A. Perrig, R. Szewczyk, V. Wen, D. E. Culler, and J. D. Tygar. SPINS: Security protocols for sensor networks. **MobiCom 2001** [Google Scholar](https://scholar.google.com/scholar?q=SPINS:+Security+protocols+for+sensor+networks)

[77] A. Taly and A. Shankar. Distributed authorization in Vanadium. **FOSAD VIII 2016** [Google Scholar](https://scholar.google.com/scholar?q=Distributed+authorization+in+Vanadium)

[74] H. Shafagh, L. Burkhalter, S. Duquennoy, A. Hithnawi, and S. Ratnasamy. Droplet: Decentralized authorization for IoT data streams. **CoRR 2018** [Google Scholar](https://scholar.google.com/scholar?q=Droplet:+Decentralized+authorization+for+IoT+data+streams)


## 关键词

+ 物联网端到端加密JEDI
+ 多对多加密协议
+ 密钥委托访问控制
+ 解耦通信IoT模型
+ 细粒度数据访问
+ 嵌入式设备安全通信
