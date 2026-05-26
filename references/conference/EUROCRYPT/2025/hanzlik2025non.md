---
title: "Non-interactive Blind Signatures from RSA Assumption and More"
标题简称:
论文类型: conference
会议简称: EUROCRYPT
发表年份: 2025
created: 2025-05-09 14:34:37
modified: 2025-05-09 14:35:38
---

## Non-interactive Blind Signatures from RSA Assumption and More

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-91124-8_13)

## 作者

+ [Lucjan Hanzlik](Lucjan%20Hanzlik.md)
+ Eugenio Paracucchi
+ Riccardo Zanotto

## 笔记

### 背景与动机
非交互式盲签名（NIBS）允许签名者基于接收者的公钥和非ce生成预签名，接收者随后可将其最终化为一个随机消息上的签名，整个过程无需交互。该原语在Privacy Pass等匿名凭证系统和加密货币空投等场景中具有重要价值。Hanzlik于Eurocrypt 2023首次提出NIBS概念[20]，但其所有具体构造均无法与现存的公钥基础设施（PKI）兼容：基于离散对数的方案要求用户公钥为配对友好曲线上的点，而通用构造则要求公钥为可验证随机函数[23]的密钥。这使得“向持有标准RSA公钥(e, N)的用户空投令牌”这一关键应用无法实现。本文的核心目标是填补这一空白，即构造一个能与现实世界中广泛使用的标准RSA公钥兼容的NIBS方案，从而实现非交互式空投。

### 相关工作

[11] Chaum. Blind signatures for untraceable payments. **CRYPTO 1983** [Google Scholar](https://scholar.google.com/scholar?q=Blind+signatures+for+untraceable+payments)
> 核心思路：提出了盲签名的概念，用于电子现金系统，用户可获取签名者对其随机消息的签名而不泄露消息。
> 局限与区别：Chaum的方案是交互式的，而本文研究的是非交互式变体。

[14] Davidson et al. Privacy Pass: bypassing internet challenges anonymously. **PoPETs 2018** [Google Scholar](https://scholar.google.com/scholar?q=Privacy+Pass+bypassing+internet+challenges+anonymously)
> 核心思路：提出Privacy Pass系统，利用盲签名为匿名用户生成一次性令牌，以绕过CAPTCHA挑战。
> 局限与区别：Privacy Pass的交互式流程不完全符合非交互式空投场景，本文旨在消除交互。

[20] Hanzlik. Non-interactive blind signatures for random messages. **EUROCRYPT 2023** [Google Scholar](https://scholar.google.com/scholar?q=Non-interactive+blind+signatures+for+random+messages)
> 核心思路：首次形式化定义了非交互式盲签名（NIBS），并给出了基于离散对数的构造。
> 局限与区别：该构造的接收者公钥需为配对友好曲线上的点，无法与标准RSA公钥兼容。本文解决了此开放问题。

[3] Bellare and Micali. Non-interactive oblivious transfer and applications. **CRYPTO 1989** [Google Scholar](https://scholar.google.com/scholar?q=Non-interactive+oblivious+transfer+and+applications)
> 核心思路：提出了非交互式不经意传输（NIOT）的概念，其接收者公钥编码了选择位。
> 局限与区别：该方案的接收者公钥需特殊构造，不与标准RSA公钥兼容。本文构造了可兼容标准RSA公钥的NIOT。

[25] Pointcheval and Sanders. Short randomizable signatures. **CT-RSA 2016** [Google Scholar](https://scholar.google.com/scholar?q=Short+randomizable+signatures)
> 核心思路：提出了一种可随机化的短签名方案（PS签名），其签名可在不泄露原始签名信息的情况下被重新随机化。
> 局限与区别：PS签名本身并非非交互式盲签名，本文将其签名算法作为乱码电路的目标函数之一。

[8] Camenisch and Lysyanskaya. A signature scheme with efficient protocols. **SCN 2002** [Google Scholar](https://scholar.google.com/scholar?q=A+signature+scheme+with+efficient+protocols)
> 核心思路：提出了一种基于RSA假设的签名方案，该方案支持高效的零知识证明。
> 局限与区别：该方案本身不支持非交互式盲签名，本文展示了如何高效地将其签名算法乱码化。

### 核心技术与方案
本文的核心框架是将姚氏乱码电路与非交互式不经意传输（NIOT）相结合来构造NIBS。签名者乱码一个签名函数 $f_{\mathsf{sk}, \mathsf{nonce}}(\mathsf{sk}_R) = \mathsf{Sign}(\mathsf{sk}, \mathsf{sk}_{R, \mathsf{nonce}})$，其中 $\mathsf{sk}_{R, \mathsf{nonce}}$ 是接收者基于其私钥和nonce生成的位字符串。签名者使用NIOT将乱码电路的输入标签发送给接收者，接收者根据其私钥解密获得对应标签，进而计算电路得到签名，并最终通过随机化算法输出最终的消息-签名对。该通用构造只针对诚实但好奇的签名者安全，可借助零知识证明提升至恶意安全。

本文的第一个关键技术是构造了一个兼容标准RSA公钥 $(e, N)$ 的NIOT协议。该协议利用了Goldwasser-Micali（GM）加密和Cocks（Cocks）加密之间的对偶性。给定用户公钥 $N$ 和一个上下文cnt，发送方计算 $x = \mathsf{H}_N(N, \mathsf{cnt})$。如果 $x$ 是模 $N$ 的二次剩余，则接收者可以解密用Cocks方案加密的消息 $m_1$；否则，接收者可以解密用GM方案加密的消息 $m_0$。协议辅以对称加密和零知识证明（通过平方根提取）来保证接收者公钥 $N$ 是Square-free的，从而确保只有接收者能解密其选择对应的消息。该方案的正确性基于GM和Cocks方案的对偶性，接收者安全性基于二次剩余假设，发送者安全性基于GM和Cocks方案的统计隐藏性（当用于异类公钥时），可提取性通过随机谕言机中获得平方根来分解 $N$ 实现。

本文的第二个关键技术是高效乱码化特定签名方案的签名算法。核心观察是对于PS签名、CL签名和BBS签名，签名中依赖于消息的部分可以表示为 $\alpha \cdot h^m$ 的形式。以PS签名为例，签名 $\sigma_2 = h^{x + y \cdot m}$ 可分解为 $s_0 \cdot \prod_{i=1}^\ell s_i$，其中 $s_0 = h^x$，$s_i$ 根据消息位 $m_i$ 为 $1_{\mathbb{G}_1}$ 或 $(h^y)^{2^{i-1}}$。乱码器生成 $\sigma_1$ 并选择元素 $a_0, a_1, \dots, a_\ell$ 满足 $\prod a_i = 1_{\mathbb{G}_1}$，然后构造 $s'_0 = a_0 \cdot h^x$ 和 $s'_i$。$s'_i$ 被加密为两个密文，并通过NIOT后接收者只能获得其消息位对应的一个。在收到所有标签后，接收者可以计算 $s'_i$，进而通过 $s_0 \cdot \prod s_i$ 得到 $\sigma_2$。该乱码方案的模拟安全性通过替换所有对消息位为1的 $s'_i$ 为 $a_i$ 来证明。

基于上述两个子模块，本文提出了一个完全安全的NIBS方案（NIBPS）。该方案使用PS签名作为底层签名，并使用了一个代数上的通用哈希函数来抵抗选择性失败攻击。具体地，输入长度扩展为 $2\ell_q$ 比特（即两个 $\mathbb{F}_q$ 元素），最终消息 $m = \alpha_1 \cdot l_1 + \beta_1 + \alpha_2 \cdot l_2 + \beta_2$，其中 $\alpha_i, \beta_i$ 由随机谕言机生成。通过将NIOT中的一部分输入随机化（利用损失函数技术），保证了即使恶意签名者通过选择性失败攻击学习到某些位，最终消息 $m$ 在计算上也是接近均匀随机的，从而实现了标准不可区分性定义下的匿盲性。该方案的预签名大小约为20.5 MB（用于80位安全级别），最终签名大小为764比特。

### 核心公式与流程

**[NIOT的正确性公式]**
对于诚实生成的密钥对 $(N, (p,q))$ 和任意上下文 $\mathsf{cnt}$，令 $x = \mathsf{H}_N(N, \mathsf{cnt})$，则存在唯一的比特 $b$ 使得：若 $x \in \mathrm{QR}_N$ 则 $b=1$，否则 $b=0$。对于任意消息 $m_0, m_1$：
$$\mathsf{R}(\mathsf{S}(m_0, m_1, \mathsf{pk}, \mathsf{cnt}), \mathsf{sk}, \mathsf{cnt}) = (b, m_b)$$
> 作用：定义了NIOT协议的正确性，即接收者总能根据其公钥隐含的选择位 $b$ 解密得到正确的消息。

**[PS签名乱码化的关键分解]**
PS签名 $\sigma_2$ 可表示为 $s_0 \cdot \prod_{i=1}^\ell s_i$，其中 $s_0 = h^x$，且
$$
s_i = \begin{cases} 1_{\mathbb{G}_1} & \text{for } m_i = 0 \\ (h^y)^{2^{i-1}} & \text{for } m_i = 1 \end{cases}
$$
乱码器随后在此基础上应用秘密共享 $a_0, a_1, \dots, a_\ell$ 满足 $\prod_{i=0}^\ell a_i = 1_{\mathbb{G}_1}$，构造 $s'_0 = s_0 \cdot a_0$ 和 $s'_i = s_i \cdot a_i$。
> 作用：将签名中依赖于消息位的指数运算转化为乘法，使得可以通过安全地将不包含信息的 $a_i$ 或包含部分签名的 $s_i \cdot a_i$ 以NIOT方式发送给接收者，从而实现对签名算法的乱码化。

**[NIBPS中最终消息的计算]**
令接收者从NIOT中获得的两个 $\ell_q$ 位字符串为 $l_1, l_2$，随机谕言机输出 $\alpha_1, \beta_1, \alpha_2, \beta_2 \in \mathbb{F}_q$。最终消息为：
$$m = \alpha_1 \cdot l_1 + \beta_1 + \alpha_2 \cdot l_2 + \beta_2 \pmod{q}$$
> 作用：通过通用哈希函数，确保即使恶意签名者通过选择性失败攻击泄露了部分 $l_1, l_2$ 的信息，最终消息 $m$ 对于该攻击者而言在计算上仍是均匀随机的，从而保证了标准安全性下的匿盲性。

### 实验结果
实验评估了所提通用构造和高效方案（NIBPS）的预签名大小，使用BLS12-381曲线实例化底层群，RSA模数2048比特（80位安全级）或3072比特（128位安全级）。对于基于PS签名的通用构造（$Generic_2$，80位安全级），预签名大小约为3247 kB，签名大小为764比特；对于基于CL签名的通用构造（$Generic_3$，80位安全级），预签名大小约为3283 kB。本文提出的完全安全的NIBPS方案，在80位安全级下，预签名大小约为20484 kB（约20 MB），签名大小为764比特。在128位安全级下，NIBPS的预签名大小增长至约49071 kB（约49 MB）。结果表明，虽然预签名大小较大，但仍在可接受范围内，尤其考虑到对方只需要接收者持有标准RSA公钥，这是此前方案无法实现的。需要注意的是，最终签名仅764比特，非常紧凑，且支持在匿名凭证等场景中进行高效验证。

### 局限性与开放问题
本文的工作为NIBS在标准RSA公钥下的使用打开了大门，但其乱码电路和NIOT协议的结合导致了较大的预签名大小（约20 MB），这对于某些带宽受限的应用可能仍不理想。作者指出，一个有趣的开放问题是形式化本文提出的乱码技术，识别出使得该技术行之有效的基本签名方案性质，从而更容易地发现更多可被高效乱码的签名方案（例如后量子安全的签名）。此外，如何使乱码过程本身和NIOT协议更加紧凑和高效，是另一个重要的研究方向。

### 强关联论文

[20] Hanzlik. Non-interactive blind signatures for random messages. **EUROCRYPT 2023** [Google Scholar](https://scholar.google.com/scholar?q=Non-interactive+blind+signatures+for+random+messages)

[3] Bellare and Micali. Non-interactive oblivious transfer and applications. **CRYPTO 1989** [Google Scholar](https://scholar.google.com/scholar?q=Non-interactive+oblivious+transfer+and+applications)

[25] Pointcheval and Sanders. Short randomizable signatures. **CT-RSA 2016** [Google Scholar](https://scholar.google.com/scholar?q=Short+randomizable+signatures)

[8] Camenisch and Lysyanskaya. A signature scheme with efficient protocols. **SCN 2002** [Google Scholar](https://scholar.google.com/scholar?q=A+signature+scheme+with+efficient+protocols)

[11] Chaum. Blind signatures for untraceable payments. **CRYPTO 1983** [Google Scholar](https://scholar.google.com/scholar?q=Blind+signatures+for+untraceable+payments)

[14] Davidson et al. Privacy Pass: bypassing internet challenges anonymously. **PoPETs 2018** [Google Scholar](https://scholar.google.com/scholar?q=Privacy+Pass+bypassing+internet+challenges+anonymously)

[2] Bellare et al. Foundations of garbled circuits. **ACM CCS 2012** [Google Scholar](https://scholar.google.com/scholar?q=Foundations+of+garbled+circuits)

[18] Goldwasser and Micali. Probabilistic encryption. **J. Comput. Syst. Sci. 1984** [Google Scholar](https://scholar.google.com/scholar?q=Probabilistic+encryption)

[13] Cocks. An identity based encryption scheme based on quadratic residues. **Cryptography and Coding 2001** [Google Scholar](https://scholar.google.com/scholar?q=An+identity+based+encryption+scheme+based+on+quadratic+residues)


## 关键词

+ 非交互式盲签名
+ RSA假设
+ 混淆电路技术
+ 不经意传输
+ 隐私传递系统
+ BBS签名