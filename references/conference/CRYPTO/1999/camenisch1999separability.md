---
title: "Separability and efficiency for generic group signature schemes"

标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 1999
created: 2025-05-26 05:11:53
modified: 2025-05-26 05:12:07
---

## Separability and efficiency for generic group signature schemes

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/3-540-48405-1_27)

## 作者

+ [Jan Camenisch](Jan%20Camenisch.md)
+ BRICS
+ Markus Michels

## 笔记

好的，作为一名密码学领域的研究助手，我将严格遵循您的要求，为这篇关于可分离群签名方案的论文提供详尽的结构化笔记。

### 背景与动机
群签名方案允许群成员代表整个群体匿名地对消息进行签名，但在必要时，指定的撤销管理者可以揭示签名者的身份。该领域早期的方案，如Chaum和van Heyst的开创性工作 [17] 以及后续的一些改进 [8,18,40]，其签名长度或群公钥大小与群成员数量相关，因此不适用于大型群组。后续Camenisch和Stadler [11] 以及Camenisch [12] 提出了适用于大群组的方案，但一个关键的瓶颈在于，这些方案中，撤销管理者和成员管理者的密钥生成过程相互依赖。这种依赖性带来了密钥管理上的复杂性，例如，当一方更换密钥或系统参数更新时，其他方必须重新生成密钥。更严重的是，这种依赖关系可能引入安全风险，例如，如果某一方选择了较弱的参数或者其秘密密钥泄露，其他方的安全性也可能受到削弱。为了解决这一问题，Kilian和Petrank [30] 引入了“可分离性”概念，但他们的身份托管方案仅实现了部分可分离性，且在效率上远不如前述大群组方案。因此，Camenisch和Michels撰写本文旨在填补一项空白：构建一个完全可分离的群签名方案，其效率能够与那些不可分离但高效的方案相媲美，从而克服密钥管理瓶颈并增强整体安全性，同时保持适用于大型群组的特性。

### 相关工作

[17] D. Chaum and E. van Heyst. Group signatures. **EUROCRYPT 1991** [Google Scholar](https://scholar.google.com/scholar?q=Group+signatures+Chaum+van+Heyst)
> 核心思路：提出了群签名的概念，设计了一种基于素数阶群离散对数问题的方案。
> 局限与区别：该方案中签名长度和群公钥大小随群成员数量线性增长，不适用于大群组。

[11] J. Camenisch and M. Stadler. Efficient group signature schemes for large groups. **CRYPTO 1997** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+group+signature+schemes+for+large+groups+Camenisch+Stadler)
> 核心思路：提出了群签名和成员证书知识证明的新技术，使签名长度和公钥大小与群成员数无关。
> 局限与区别：该方案的密钥生成过程不具有可分离性，撤销管理者和成员管理者的密钥相互依赖。

[12] J. L. Camenisch. Group Signature Schemes and Payment Systems Based on the Discrete Logarithm Problem. **PhD thesis, ETH Zürich, 1998** [Google Scholar](https://scholar.google.com/scholar?q=Group+Signature+Schemes+and+Payment+Systems+Based+on+the+Discrete+Logarithm+Problem+Camenisch)
> 核心思路：提出了另一种适用于大群组的群签名方案，具有较高的效率。
> 局限与区别：同样不具有密钥可分离性，其安全性建立在强RSA假设之上。

[30] J. Kilian and E. Petrank. Identity escrow. **CRYPTO 1998** [Google Scholar](https://scholar.google.com/scholar?q=Identity+escrow+Kilian+Petrank)
> 核心思路：提出了身份托管的概念，并构造了部分可分离的方案，即对于撤销管理者是可分离的。
> 局限与区别：其效率远低于Camenisch和Stadler [11] 的方案，且不完全可分离（对群成员不可分离），使其在实际应用中效率成为瓶颈。

[9] J. Camenisch and M. Michels. A group signature scheme based on an RSA-variant. **ASIACRYPT 1998** (preliminary version) [Google Scholar](https://scholar.google.com/scholar?q=A+group+signature+scheme+based+on+an+RSA-variant+Camenisch+Michels)
> 核心思路：提出了一种基于RSA变体的高效群签名方案。
> 局限与区别：该方案没有考虑密钥的可分离性，其密钥生成过程存在依赖。

[15] D. Chaum, J.-H. Evertse, and J. van de Graaf. An improved protocol for demonstrating possession of discrete logarithms and some generalizations. **EUROCRYPT 1987** [Google Scholar](https://scholar.google.com/scholar?q=An+improved+protocol+for+demonstrating+possession+of+discrete+logarithms+and+some+generalizations+Chaum+Evertse+van+de+Graaf)
> 核心思路：提出了证明离散对数知识的基础零知识证明协议。
> 局限与区别：本文广泛使用了该基础协议及其扩展形式，并在此基础上构造了跨群离散对数等式的证明。

### 核心技术与方案

本文的核心贡献在于提出了一个通用的、完全可分离的群签名方案框架，并给出了一个基于强RSA假设和离散对数假设的高效实例化。方案的构建思路是经典的“安全外壳”式设计：群成员的签名由一个加密的成员证书和一系列零知识证明组成。完全可分离性通过让四个密钥生成算法（成员管理者GKG-MM、撤销管理者GKG-RM、群成员GKG-GM、系统参数GKG-S）独立运行来实现，它们之间不存在任何交互或依赖。

通用方案的构造如下：
1.  **角色与密钥**：成员管理者生成签名方案的密钥对，撤销管理者生成影子加密方案的密钥对，群成员选择一个单向函数 $f$ 的原像作为私钥，并计算其像作为公钥 $y_U = f(x_U)$。
2.  **注册**：群成员 $U$ 向成员管理者提供身份 $ID_U$ 和公钥 $y_U$，并零知识地证明自己知道 $x_U$。验证通过后，管理者签发一个签名 $s_U = Sig(x_M, y_M, y_U)$ 作为成员证书。
3.  **签名生成**（GSig）：群成员 $U$ 签署消息 $m$。
    *   首先，他计算一个对 $y_U$ 的影子加密 $z = Enc(y_R, y_U)$。
    *   接着，他计算一个对 $y_U$ 的无条件隐藏承诺 $C = Com(y_U, r)$。
    *   最后，他生成三个基于签名知识的证明 (SPK)：
        *   $S_I$：证明 $C$ 中承诺的值正是 $z$ 中加密的值的影子。
        *   $S_{II}$：证明 $C$ 中承诺的值 $y_U$ 是单向函数 $f$ 的一个像（即他知道原像 $x_U$）。
        *   $S_{III}$：证明 $C$ 中承诺的值 $y_U$ 获得了一个成员管理者的有效签名（即他知道证书 $s_U$）。
    *   签名消息 $m$ 的最终群签名为元组 $(z, C, S_I, S_{II}, S_{III})$。
4.  **验证与追溯**：验证算法GVer检查三个SPK的正确性。追溯算法GTrace由撤销管理者执行，解密 $z$ 获得 $y_U$，然后在群成员列表GML中查找匹配的身份。

**高效实例化**：为了实现通用方案中的SPK，论文使用了第3节中开发的证明技术，特别是允许证明来自不同群（如 $G_R$ 和 $G_S$）中离散对数在整数环 $\mathbb{Z}$ 上满足多项式关系。具体实例化采用了：
*   **承诺方案**：基于Pedersen方案 [39] 的改进，使用一个大RSA模数 $n_S$ 构成的群 $G_S$，承诺为 $C = g_S^{\alpha} h_S^{r}$，其中 $g_S, h_S \in G_S$。
*   **影子加密**：基于ElGamal [22]，加密 $g_R^{y_U}$ 而非 $y_U$本身，其中 $G_R$ 是大素数阶群。
*   **单向函数**：定义为两个大素数的乘积，即 $y_U = p_U' \cdot p_U''$。
*   **签名方案**：采用RSA签名 [43]，使用一个简单的冗余函数 $red(x) = x2^K + d$，允许对证明进行同态操作。

通过这些具体实例，$S_I, S_{II}, S_{III}$ 三个SPK被转化为具体的代数协议，其安全性依赖于强RSA假设和离散对数假设。该系统的签名长度和公钥大小均与群成员数量无关，计算复杂度约为17次多指数运算（签名者）和10次多指数运算（验证者）。

### 核心公式与流程

**[证明离散对数相等的协议（来自不同群 $G_1, G_2$）]**

$$P K \{ (\alpha, \beta) : y_1 \stackrel{G_1}{=} g_1^{\alpha} \land y_2 \stackrel{G_2}{=} g_2^{\alpha} \land \tilde{y} \stackrel{\mathbb{Z}_n^*}{=} h_1^{\beta} h_2^{\alpha} \land (-2^{\ell} < \alpha < 2^{\ell}) \}$$

> 作用：此协议允许证明者在两个不同群 $G_1$ 和 $G_2$ 中，掌握了某个秘密值 $\alpha$，使得 $y_1 = g_1^{\alpha}$ 和 $y_2 = g_2^{\alpha}$ 同时成立。它通过引入一个第三方群 $\mathbb{Z}_n^*$来“桥接”两个离散对数，并利用区间证明来确保等式在整数环上成立，而非模群阶。这是实现跨群可分离性和签名中 $S_I$ 证明的关键组件。

**[完整的群签名 SPK（合并后的 $S_{I-III}$）]**
$$S_{I-III} := SPK \{ (\alpha, \beta, \gamma, \psi, \lambda, \tau, \pi, \delta, \zeta, \omega, \theta, \nu, \mu, \rho, \xi, \kappa):$$
$$A \stackrel{G_R}{=} g_R^{\alpha} \land B \stackrel{G_R}{=} g_R^{\beta} y_R^{\alpha} \land C \stackrel{G_S}{=} g_S^{\beta} h_S^{\gamma} \land D \stackrel{G_S}{=} g_S^{\psi} h_S^{\lambda} \land E \stackrel{G_S}{=} g_S^{\tau} h_S^{\pi} \land E \stackrel{G_S}{=} D^{\psi} (g_S^{n_M})^{\delta} h_S^{\zeta} \land F \stackrel{G_S}{=} g_S^{\omega} h_S^{\theta} \land L \stackrel{G_S}{=} g_S^{\nu} h_S^{\mu} \land C^{2^K} g_S^{d} \stackrel{G_S}{=} E^{\psi} (g_S^{n_M})^{\rho} h_S^{\xi} \land C \stackrel{G_S}{=} F^{\nu} h_S^{\kappa} \land $$
$$(-2^{\epsilon(\ell_U+k)+2} < \beta < 2^{\epsilon(\ell_U+k)+2}) \land (-2^{\epsilon(\ell_M+k)+2} < \psi, \tau, \delta, \rho < 2^{\epsilon(\ell_M+k)+2}) \land$$
$$(-2^{\epsilon(\ell_U/2+k)+2} < \omega, \nu < 2^{\epsilon(\ell_U/2+k)+2}) \} (A, B, C, D, E, F, L, m)$$

> 作用：这是最终群签名的核心，它在一个统一的随机预言机模型中，将证明 $y_U$ 被加密在 $(A,B)$ 中，$y_U$ 是两素数的乘积，以及 $y_U$ 拥有管理者签名（通过RSA同态关系证明）这三个陈述压缩成一个简洁的 $SPK$。其中丰富的区间约束保证了各离散对数关系在整数环上而非模群阶上成立，从而避免了群阶不同带来的问题。

### 实验结果

论文未提供标准化的实验（如代码运行时间或内存占用），而是对方案的计算和通信复杂度进行了理论分析，并给出了具体的参数建议。
*   **计算开销**：在签名生成阶段，群成员需要进行约17次多指数运算（包括承诺和响应计算）。在签名验证阶段，验证者需要进行约10次多指数运算。
*   **通信开销（签名长度）**：论文基于一组具体的参数取值给出了估算：安全参数 $\epsilon=9/8$，成员公钥长度 $\ell_U=768$位，撤销管理者群阶 $\ell_R=1100$位，RSA模数 $\ell_M=1630$位，承诺模数 $\ell_S=1024$位，冗余函数常数 $K=850$位，挑战长度 $k=160$位。在这些参数下，一个群签名的长度约为3.5千字节。
*   **与其他方案的比较**：与当前最流行且高效的不可分离群签名方案（如 [9,11,12]）相比，本文的签名长度大约增加了3倍，计算开销（指数运算次数）也增加了约3倍。作为回报，该方案实现了完全可分离性，这在大型、动态且密钥管理复杂的环境中是一个重要的权衡。论文还指出，其追溯算法GTrace可以通过让群成员同时提供 $g_R^{y_U}$ 并进行哈希索引来优化为常数时间，与群大小无关。

### 局限性与开放问题

该文在理论构造和应用上留下了几个未解决的问题。首先，论文指出需要为RSA签名方案搭配的简单冗余函数进行更精确的安全性分析，以防范针对性的攻击，如 [27,36] 中讨论的选择消息攻击，尽管本文的受限攻击模型一定程度上缓解了风险。其次，寻找一个拥有更简单的冗余函数且能支持高效签名生成和验证的签名方案，本身就是一个开放挑战。最后，设计一个完全基于标准假设（如离散对数假设或CDH假设）而不依赖强RSA假设的可分离群签名方案，更具理论意义，也是未来的一个重要研究方向。

### 强关联论文

[11] J. Camenisch and M. Stadler. Efficient group signature schemes for large groups. **CRYPTO 1997** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+group+signature+schemes+for+large+groups+Camenisch+Stadler)

[12] J. L. Camenisch. Group Signature Schemes and Payment Systems Based on the Discrete Logarithm Problem. **PhD thesis, ETH Zürich, 1998** [Google Scholar](https://scholar.google.com/scholar?q=Group+Signature+Schemes+and+Payment+Systems+Based+on+the+Discrete+Logarithm+Problem+Camenisch)

[17] D. Chaum and E. van Heyst. Group signatures. **EUROCRYPT 1991** [Google Scholar](https://scholar.google.com/scholar?q=Group+signatures+Chaum+van+Heyst)

[22] T. ElGamal. A public key cryptosystem and a signature scheme based on discrete logarithms. **CRYPTO 1984** [Google Scholar](https://scholar.google.com/scholar?q=A+public+key+cryptosystem+and+a+signature+scheme+based+on+discrete+logarithms+ElGamal)

[25] E. Fujisaki and T. Okamoto. Statistical zero knowledge protocols to prove modular polynomial relations. **CRYPTO 1997** [Google Scholar](https://scholar.google.com/scholar?q=Statistical+zero+knowledge+protocols+to+prove+modular+polynomial+relations+Fujisaki+Okamoto)

[30] J. Kilian and E. Petrank. Identity escrow. **CRYPTO 1998** [Google Scholar](https://scholar.google.com/scholar?q=Identity+escrow+Kilian+Petrank)

[39] T. P. Pedersen. Non-interactive and information-theoretic secure verifiable secret sharing. **CRYPTO 1991** [Google Scholar](https://scholar.google.com/scholar?q=Non-interactive+and+information-theoretic+secure+verifiable+secret+sharing+Pedersen)

[3] N. Barić and B. Pfitzmann. Collision-free accumulators and fail-stop signature schemes without trees. **EUROCRYPT 1997** [Google Scholar](https://scholar.google.com/scholar?q=Collision-free+accumulators+and+fail-stop+signature+schemes+without+trees+Barić+Pfitzmann)

[9] J. Camenisch and M. Michels. A group signature scheme based on an RSA-variant. **ASIACRYPT 1998** (preliminary version) [Google Scholar](https://scholar.google.com/scholar?q=A+group+signature+scheme+based+on+an+RSA-variant+Camenisch+Michels)

[43] R. Rivest, A. Shamir, and L. Adleman. A method for obtaining digital signatures and public-key cryptosystems. **Communications of the ACM 1978** [Google Scholar](https://scholar.google.com/scholar?q=A+method+for+obtaining+digital+signatures+and+public-key+cryptosystems+Rivest+Shamir+Adleman)


## 关键词

+ 可分离群签名方案
+ 匿名签名密钥独立选择
+ 离散对数不同群等式证明
+ 通用可分离群签名实例化
+ 受托人揭示签名者身份