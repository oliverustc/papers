---
title: "Fast IDentity Online with Anonymous Credentials FIDO-AC"
标题简称:
论文类型: conference
会议简称: USENIX Security
发表年份: 2023
created: 2025-05-09 14:47:51
modified: 2025-05-09 14:48:30
---

## Fast IDentity Online with Anonymous Credentials FIDO-AC

## 发表信息

+ [原文链接](https://www.usenix.org/conference/usenixsecurity23/presentation/yeoh)

## 作者

+ Wei-Zhu Yeoh
+ Michal Kepkowski
+ Gunnar Heide
+ Dali Kaafar
+ [Lucjan Hanzlik](Lucjan%20Hanzlik.md)

## 笔记

### 背景与动机
Web 认证是数字世界的核心基础设施。当前主流的 FIDO2 协议通过基于公钥密码学的无密码认证，提供了强安全性和隐私保护，但其流程与用户的属性（如年龄、证件有效期）完全脱钩。当在线服务（如年龄验证网站）需要验证用户属性时，它们不得不依赖临时性的、不符合数据最小化原则的临场解决方案，要求用户上传完整的身份证明文件。这种设计缺陷导致了严重的数据泄露风险，例如 2022 年澳大利亚电信公司 Optus 的数据泄露事件，黑客窃取了大量用户的完整护照信息 [2]。学术界虽已提出匿名凭证等隐私增强技术，但这些方案因缺乏与 FIDO2 协议的原生集成能力、部署复杂度高、用户摩擦大等原因，始终未能获得广泛的实际部署。本文旨在填补这一空白，提出一个既保持 FIDO2 原生安全性与兼容性，又能安全、隐私地集成属性认证的通用框架 FIDO-AC。

### 相关工作

[3] Barbosa 等. Provable security analysis of FIDO2. **CRYPTO 2021** [Google Scholar](https://scholar.google.com/scholar?q=Provable+security+analysis+of+FIDO2)
> 核心思路：首次对 FIDO2 协议进行了形式化的安全性建模与分析。
> 局限与区别：该模型仅关注 FIDO2 自身的认证属性，未考虑与属性的集成。本文扩展了其模型，引入了属性集和策略，并定义了属性不可伪造性等新性质。

[15] Davidson 等. Privacy Pass: Bypassing internet challenges anonymously. **PoPETs 2018** [Google Scholar](https://scholar.google.com/scholar?q=Privacy+Pass:+Bypassing+internet+challenges+anonymously)
> 核心思路：提出了一个基于令牌的匿名 CAPTCHA 绕过方案，可视为单次、单属性的匿名凭证系统。
> 局限与区别：Privacy Pass 关注的是匿名绕过验证码，而 FIDO-AC 旨在将通用的、多属性的匿名凭证系统与 FIDO2 认证深度绑定。隐私 Pass 的速率限制版本 [22] 架构与本文的 Mediator 角色相似，但其目的和适用范围不同。

[21] Hanzlik 等. Token meets wallet: Formalizing privacy and revocation for FIDO2. **IEEE S&P 2023** [Google Scholar](https://scholar.google.com/scholar?q=Token+meets+wallet:+Formalizing+privacy+and+revocation+for+FIDO2)
> 核心思路：对 FIDO2 的隐私性和撤销机制进行了形式化定义。
> 局限与区别：该工作未涉及属性认证。本文在此基础上，将匿名凭证和属性策略融入到形式化模型中，并引入了中介方来桥接 FIDO2 与属性系统。

[31] Rosenberg 等. zk-creds: Flexible anonymous credentials from zkSNARKs and existing identity infrastructure. **Cryptology ePrint Archive 2022** [Google Scholar](https://scholar.google.com/scholar?q=zk-creds:+Flexible+anonymous+credentials+from+zkSNARKs+and+existing+identity+infrastructure)
> 核心思路：利用 ZK-SNARK 和现有 eID 基础设施（如 ePassport）构建灵活匿名凭证。
> 局限与区别：zk-creds 的方案无法提供 eID 的“实活性”（Active Authentication），使得攻击者可以使用在边境检查时获取的 eID 数据生成凭证，破坏了不可共享性。FIDO-AC 通过引入 Mediator 和 Chip Authentication 确保了属性的实时持有证明。

[32] Schwarz 等. FeIDo: Recoverable FIDO2 tokens using electronic ids. **ACM CCS 2022** [Google Scholar](https://scholar.google.com/scholar?q=FeIDo:+Recoverable+FIDO2+tokens+using+electronic+ids)
> 核心思路：利用 TEE 和 eID 实现可恢复的 FIDO2 令牌，TEE 可基于属性执行访问控制。
> 局限与区别：FeIDo 与 FIDO-AC 在目标和设计上存在根本不同。FeIDo 将个人数据置于 TEE 中，依赖特定 Token 实现；而 FIDO-AC 支持任何符合标准的 FIDO Token，且个人数据永远不会离开用户设备，隐私性更强。

### 核心技术与方案
FIDO-AC 的核心是设计一个名为 PAwAM（Passwordless Authentication with Attributes and Mediator）的形式化模型和系统。该系统的逻辑架构由匿名凭证子系统、中介方和 FIDO 扩展三个部分组成。

首先，论文提出了 PAwA 模型（密码学无密码认证），将 FIDO2 协议形式化地扩展到包含属性集。在该模型中，服务器拥有属性策略，令牌拥有属性集，认证过程需要同时满足令牌密钥的证明和属性策略的满足性。然而，直接修改现有 FIDO Token 来支持该模型是不可行的，因此论文引入了第四个参与方——Mediator（中介方）。Mediator 作为一个受信任的接口，桥接了标准 FIDO Token 和属性系统。PAwAM 模型的形式化语法定义了 Gen、Reg、Auth 和 Med 四个算法组件。Med 组件中的 attestreqac 算法用于生成向 Mediator 的请求，它由令牌的密钥 askT 和服务器挑战 c 生成一个包括属性哈希、公钥和证明的请求 reqM。attestchalac 由 Mediator 执行，验证请求并发起一个挑战 chalM。attestrespac 由用户设备执行，响应 Mediator 的挑战。attestac 由 Mediator 执行，验证响应并输出一个包含属性哈希和服务器挑战的签名 (att_m, σ_m)。最后，proveac 由客户端执行，使用 ZKP 生成关于属性的证明 ΠAtt，而 checkac 由服务器执行以验证该证明。

FIDO-AC 的一个关键创新是使用电子身份文件 (eID) 作为属性源，并利用其内置的安全机制实现“活跃性”验证。系统通过 ePassport 的 Chip Authentication (CA) 协议来确保用户物理上拥有该 eID。Mediator 接收用户设备传来的 eID 认证数据（Hash 值、公钥、被动认证签名），并启动与 eID 芯片的挑战-响应协议，以验证其持有对应私钥。该过程的结果是 Mediator 对“所读取的 eID 数据已通过活跃性验证”这一事实进行签名。为了隐私保护，用户设备随后使用非交互式零知识证明 (NIZK) 来证明它知道满足服务器策略的属性（例如，年龄大于 18 岁），而不泄露属性的具体值。这个零知识证明以及 Mediator 的签名被绑定到标准的 FIDO2 断言挑战中，通过修改客户端代码实现 FIDO 扩展，无需修改 FIDO Token 或浏览器。

安全性方面，FIDO-AC 被证明满足**防冒充攻击**（归约到底层 PLA 协议的安全性）、**属性不可伪造性**（归约到 Mediator 签名的不可伪造性、eID 的安全性以及 ZKP 的可靠性）、**不可链接性**（归约到底层 PLA 协议和零知识证据的零知识性）以及**来源隐私**和**一次性属性隐私**。安全性证明依赖于随机预言机模型和 eID 数据组的不可链接性假设。系统通信复杂度与标准 FIDO2 认证相当，仅额外增加了 Mediator 交互消息和 ZKP 的大小。计算开销主要在客户端，尤其是 ZKP 的生成。

### 核心公式与流程

**[Mediator 签名的生成: attestac]**
$$
\begin{aligned}
&(req_M, keyses) := st_{chal} \\
&(H(DG), pk_{eID}, \pi_{PA}, c, nonce) := req_M \\
&b_{PA} \leftarrow PAverify(H(DG), pk_{eID}, \pi_{PA}) \\
&b_{CA} \leftarrow CAverify(resp_M, keyses) \\
&att_m := H(H(DG) || nonce) || c \\
&\sigma_m := \bot \\
&\sigma_m \leftarrow Sign(sk_M, att_m) \text{ if } (b_{PA} \land b_{CA}) \\
&\text{return } att_m, \sigma_m
\end{aligned}
$$
> 作用：此算法由 Mediator 执行。它首先验证从 eID 读取的被动认证签名 bPA，然后通过在 CA 过程中成功建立会话密钥来验证活跃性 bCA。验证通过后，Mediator 对属性哈希值 H(DG) 与一次性随机数 nonce 和服务器挑战 c 的哈希值进行签名，生成不可链接且具绑定的 Mediator 签名。

**[零知识证明生成: proveac]**
$$
\begin{aligned}
&DG \leftarrow Parse(Att) \\
&(m||cm) := att_m \\
&\pi_{zkp} \leftarrow ZKProve(crs, (m, Policy_S), (DG, nonce)) \\
&\Pi_{Att} := (att_m, \sigma_m, \pi_{zkp}) \\
&\text{return } \Pi_{Att}
\end{aligned}
$$
> 作用：此算法由客户端执行。它从用户的完整属性中解析出数据组 DG，并使用 Mediator 的签名消息 att_m 和加密密钥 (crs) 生成一个零知识证明 πzkp。该证明证明了 k 知道一个 DG，使得 k 满足服务器的策略 Policy_S，并且 H(DG || nonce) 与 Mediator 签名中的承诺 m 一致。最终输出一个完整的匿名凭证 ΠAtt。

**[服务器端验证: checkac]**
$$
\begin{aligned}
&(att_m, \sigma_m, \pi_{zkp}) := \Pi_{Att} \\
&b_m \leftarrow Verify(pk_M, att_m, \sigma_m) \\
&(m||cm) := att_m \\
&b_{zkp} \leftarrow ZKVer(crs, (m, Policy_S)) \\
&b_{challenge} \leftarrow cm =? c \\
&b_{ac} \leftarrow b_m \land b_{zkp} \land b_{challenge} \\
&\text{return } b_{ac}
\end{aligned}
$$
> 作用：此算法由服务器运行。它首先通过 bm 验证 Mediator 签名的有效性，然后通过 bzkp 验证零知识证明的正确性，确保属性满足策略，最后通过 bchallenge 检查挑战是否一致。仅当所有检查都通过时，认证才被视为成功。

### 实验结果
论文通过一个原型系统对 FIDO-AC 的性能进行了评估，系统配置为 Google Pixel 6 Pro（移动端）和 Azure 标准 D4s v3 云实例（服务器端）。实验中，eID 读取操作的平均耗时为 1059.4 ms，但可通过缓存降低至 0 ms。与 eID 的安全信道建立和活跃性验证共耗时 738.92 ms。零知识证明（ZKP）的验证在云端效率极高，仅需 8.19 ms。但 ZKP 的生成在移动端需要约 3375.61 ms，是系统的性能瓶颈。然而，论文指出 ZNP 的生成可以离线预处理（precomputed），因为其依赖的用户数据和随机数不依赖于第三方的实时值。假设已完成离线预处理的 ZKP 并缓存了 eID 数据，FIDO-AC 与标准 FIDO2 相比，引入的额外延迟仅为活跃性验证的约 740ms，对于原型系统而言，这个延迟在可接受范围内。

### 局限性与开放问题
FIDO-AC 的 Mediator 作为新的受信任组件，其实现方式（本地应用、远程第三方或 TEE）会影响系统的隐私和安全强度，是一个潜在的信任瓶颈和攻击面。虽然文中分析了 Mediator 与服务器或用户共谋的场景，但实际部署中如何建立对 Mediator 的普遍信任仍有待解决。此外，ZKP 实现的性能开销，特别是其生成时间，是限制大规模采纳的主要因素，尽管可以通过预处理缓解，但对用户体验仍有影响。

### 强关联论文

[3] Manuel Barbosa, Alexandra Boldyreva, Shan Chen, and Bogdan Warinschi. Provable security analysis of FIDO2. **CRYPTO 2021** [Google Scholar](https://scholar.google.com/scholar?q=Provable+security+analysis+of+FIDO2)

[15] Alex Davidson, Ian Goldberg, Nick Sullivan, George Tankersley, and Filippo Valsorda. Privacy Pass: Bypassing internet challenges anonymously. **PoPETs 2018** [Google Scholar](https://scholar.google.com/scholar?q=Privacy+Pass:+Bypassing+internet+challenges+anonymously)

[21] Lucjan Hanzlik, Julian Loss, and Benedikt Wagner. Token meets wallet: Formalizing privacy and revocation for FIDO2. **IEEE S&P 2023** [Google Scholar](https://scholar.google.com/scholar?q=Token+meets+wallet:+Formalizing+privacy+and+revocation+for+FIDO2)

[31] Michael Rosenberg, Jacob White, Christina Garman, and Ian Miers. zk-creds: Flexible anonymous credentials from zkSNARKs and existing identity infrastructure. **Cryptology ePrint Archive 2022** [Google Scholar](https://scholar.google.com/scholar?q=zk-creds:+Flexible+anonymous+credentials+from+zkSNARKs+and+existing+identity+infrastructure)

[32] Fabian Schwarz, Khue Do, Gunnar Heide, Lucjan Hanzlik, and Christian Rossow. FeIDo: Recoverable FIDO2 tokens using electronic ids. **ACM CCS 2022** [Google Scholar](https://scholar.google.com/scholar?q=FeIDo:+Recoverable+FIDO2+tokens+using+electronic+ids)


## 关键词

+ FIDO-AC匿名凭证认证框架
+ FIDO2无密码认证扩展
+ 电子护照ePassport属性验证
+ 用户属性隐私保护披露
+ 数据最小化原则认证
+ 生物特征认证属性结合
