---
title: "Practical verifiable encryption and decryption of discrete logarithms"
标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 2003
---

## Practical verifiable encryption and decryption of discrete logarithms

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-540-45146-4_8)

## 作者

+ [Jan Camenisch](Jan%20Camenisch.md) 
+ [Victor Shoup](Victor%20Shoup.md)
## 笔记

### 背景与动机

在公钥加密场景中，证明密文所隐藏消息的特定性质是一个核心问题。例如，加密方需要向验证方证明某个密文是对一个满足特定关系的秘密值的加密，或者解密方需要证明密文解密后确实得到了某个值。这些场景被称为可验证加密与可验证解密。这些协议在密钥托管、乐观公平交换、公开可验证秘密共享、通用可组合承诺、群签名和指定确认者签名等领域具有广泛的应用。然而，此前针对离散对数问题的可验证加密方案 [Sta96, BG96, YY98, ASW00] 普遍存在两大瓶颈：一是未能提供针对选择密文攻击的安全性，这在许多实际应用中是至关重要的；二是它们通常依赖低效的“cut-and-choose”证明方式，导致协议效率低下。此外，这些早期的方案往往将加密过程和证明过程交织在一起，使得生成的证明很长，且难以融入可验证解密协议。为了填补这些空白，本文旨在设计并分析一套实用的加密方案，它能够提供适应性选择密文安全，并支持高效的、基于Σ-协议的离散对数可验证加密与可验证解密。

### 相关工作

[Sta96] M. Stadler. Publicly verifiable secret sharing. **EUROCRYPT 1996** [Google Scholar](https://scholar.google.com/scholar?q=Publicly+verifiable+secret+sharing)
> 核心思路：提出了公开可验证秘密共享的概念，并给出了基于离散对数的具体构造。
> 局限与区别：该方案使用了昂贵的“cut-and-choose”证明，且未能提供针对选择密文攻击的安全性。本文在此基础上，构建了首个避免此类证明并达到CCA安全性的方案。

[YY98] A. Young and M. Yung. Auto-recoverable auto-certifiable cryptosystems. **EUROCRYPT 1998** [Google Scholar](https://scholar.google.com/scholar?q=Auto-recoverable+auto-certifiable+cryptosystems)
> 核心思路：提出自动恢复和自动认证的密码系统，其中蕴含了可验证加密的思想。
> 局限与区别：该方案同样依赖于低效的cut-and-choose证明，并且其安全性未考虑选择密文攻击。此外，方案使用了“双层”离散对数，限制了其与不同代数群一起使用的灵活性。本文的方案则避免了这些限制。

[ASW00] N. Asokan, V. Shoup, and M. Waidner. Optimistic fair exchange of digital signatures. **IEEE Journal on Selected Areas in Communications 2000** [Google Scholar](https://scholar.google.com/scholar?q=Optimistic+fair+exchange+of+digital+signatures)
> 核心思路：提出了使用可验证加密来实现乐观公平交换的数字签名协议框架，并特别指出了方案需要具备选择密文安全性。
> 局限与区别：该工作主要关注应用框架，其所依赖的底层可验证加密方案存在前述的CCA安全性不足或效率低下的问题。本文提供了一个满足这些严格安全要求的、高效的底层加密原语。

[Bou00] F. Boudot. Efficient proofs that a committed number lies in an interval. **EUROCRYPT 2000** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+proofs+that+a+committed+number+lies+in+an+interval)
> 核心思路：提出了关于承诺整数落入特定区间的有效零知识证明协议。
> 局限与区别：该工作专注于区间证明本身，而本文在其基础上，结合自身加密方案的特性，设计了一个更高效的对称区间证明，用于可验证解密协议中。

[CS01] R. Cramer and V. Shoup. Universal hash proofs and a paradigm for adaptive chosen ciphertext secure public-key encryption. **IACR ePrint 2001** [Google Scholar](https://scholar.google.com/scholar?q=Universal+hash+proofs+and+a+paradigm+for+adaptive+chosen+ciphertext+secure+public-key+encryption)
> 核心思路：提出了一个通用的“哈希证明”范式，用于简洁地构建和证明选择密文安全的公钥加密方案。
> 局限与区别：本文的加密方案是Cramer-Shoup方案的变体，但为了支持更复杂的Σ-协议证明系统，特别是处理群中阶为2的元素，本文的方案在细节上（如abs函数的使用）与该框架不完全吻合，因此需要从头分析其安全性。

[BS02] E. Bresson and J. Stern. Proofs of knowledge for non-monotone discrete-log formulae and applications. **ISC 2002** [Google Scholar](https://scholar.google.com/scholar?q=Proofs+of+knowledge+for+non-monotone+discrete-log+formulae+and+applications)
> 核心思路：独立提出了一个证明两个离散对数不相等的协议，与本文的协议思路相似。
> 局限与区别：他们的协议在计算效率上比本文的协议大约慢一倍，并且其安全性是计算意义上的，而本文的协议是完美意义上的特殊可靠性。

[CD00] J. Camenisch and I. Damgård. Verifiable encryption, group encryption, and their applications to group signatures and signature sharing schemes. **ASIACRYPT 2000** [Google Scholar](https://scholar.google.com/scholar?q=Verifiable+encryption%2C+group+encryption%2C+and+their+applications+to+group+signatures+and+signature+sharing+schemes)
> 核心思路：讨论了可验证加密在公开可验证秘密共享和签名共享中的应用。
> 局限与区别：该工作更多地侧重于应用层面的探讨，而本文则提供了一个具体的、满足高级安全要求的加密方案及其配套证明协议的完整构建。

### 核心技术与方案

本文的整体框架是设计一个基于Paillier决策合数剩余假设的、支持标签的、适应性选择密文安全的公钥加密方案，并在此基础上构建一套针对离散对数关系的可验证加密与可验证解密协议。整个方案分为三个紧密关联的模块：加密方案本身、可验证加密协议、以及可验证解密协议。

**1. 加密方案的设计与安全性**
方案的核心是Cramer-Shoup型加密范式的一个变体。密钥生成时，选择两个安全素数 $p$, $q$ 构造模数 $n=pq$。选择随机指数 $x_1, x_2, x_3$ 和一个随机基 $g'$，计算 $g = (g')^{2n}$ 以及 $y_1 = g^{x_1}, y_2 = g^{x_2}, y_3 = g^{x_3}$。公钥为 $(hk, n, g, y_1, y_2, y_3)$，其中 $hk$ 是哈希密钥。加密消息 $m \in [n]$ 时，随机选取 $r \in [n/4]$，计算 $u = g^r$, $e = y_1^r h^m$ (其中 $h = 1+n$)，以及 $v = \text{abs}((y_2 y_3^{\mathcal{H}_{hk}(u,e,L)})^r)$。解密时，先验证 $v$ 的正确性，然后计算一个包含 $m$ 的量。该方案的关键创新点在于使用绝对值函数`abs(·)`来消除群 $\mathbb{Z}_{n^2}^*$ 中阶为2的元素导致的歧义，从而在严格意义上达到非延展性。安全性证明直接基于DCR假设和哈希函数的抗碰撞性，通过归约到区分随机元素与$n$次剩余来论证。

**2. 可验证加密协议**
该协议允许证明方让验证方相信，一个密文 $(u, e, v)$ 是在公钥PK和标签$L$下对离散对数 $\log_\gamma \delta$ 的加密。协议旨在证明存在 $(m, r, s)$ 使得 $u=g^r$, $e=y_1^r h^m$, $v=\text{abs}((y_2 y_3^{\mathcal{H}_{hk}(u,e,L)})^r)$, $\delta = \gamma^m$，并且$m$在一个规定的合理区间内。由于协议中涉及的多个等式是独立的，证明方可以通过一个并行的Σ-协议来一次性证明所有这些关系。具体地，证明方首先选择一个随机数$s$，计算一个辅助承诺 $\mathfrak{k} = \mathfrak{g}^m \mathfrak{h}^s$，其中 $\mathfrak{g}, \mathfrak{h}$ 是另一个群的生成元。然后，证明方使用标准的Σ-协议技巧：选择随机盲化因子，计算承诺值，接收挑战，并计算响应。该协议使用了“分解与承诺”的技术来分别处理加密关系、离散对数关系以及区间约束，利用了强RSA假设来保证辅助承诺的安全性。其效率很高，证明方和验证方的计算量都只是稍大于加密本身。

**3. 可验证解密协议**
该协议允许解密方证明自己的解密结果是否正确，它包含两个子协议：一个用于证明密文确实解密为某个具体消息$m$；另一个用于证明密文解密后的消息的离散对数等于某个给定值$\delta$。

对于匹配消息的证明，协议的核心是证明或证伪公式（1）中的两个等式。如果密文有效且匹配，则两个等式都成立，证明方直接使用Σ-协议展示对秘密密钥$ (x_1, x_2, x_3) $的知识即可。如果密文解密为另一个消息或无效，则至少有一个等式不成立。此时，证明方需要证明一个“非”关系。由于等式两侧的值可能落在群的不同子群中（$\mathbf{G}_n$或$\mathbf{G}_{n'}$），直接证明其不等于1在零知识上是困难的。本文的巧妙之处在于利用群的结构，将问题拆解为四种情况（公式2-5），并对每种情况分别构造承诺$C_i$。最终通过一个复杂的“or”协议（使用[CDS94]的技术），证明方展示其知道这些承诺中的一个非1元素，从而证明等式不成立。这个协议同样基于因子分解假设。为了扩展到解密离散对数，协议需要额外证明解密后的消息$m$与$\log_\gamma \delta$在模$\rho$下同余。这通过使用一个精确的区间证明（基于拉格朗日四平方和定理）来限定$m$的范围，并结合辅助承诺来实现。

该系统的渐进复杂度如下：加密算法大约需要3次模$n^2$下的平方运算，解密算法约需5次。可验证加密协议中，证明方需要执行2次模$n$平方、3次模$n^2$平方和$\ell'$次群运算，验证方类似。可验证解密协议的计算量大约是加密协议的一到四倍。对于多基表示，所有协议的计算量均随基的个数线性增长。

### 核心公式与流程

**[加密算法]**
$$\text{Encrypt}(PK, m, L): \quad r \in_R [n/4], \quad u := g^r, \quad e := y_1^r h^m, \quad v := \text{abs}((y_2 y_3^{\mathcal{H}_{hk}(u,e,L)})^r)$$
> 作用：定义了将消息$m$加密为密文$(u, e, v)$的流程，是后续所有协议的基础。使用`abs()`函数消除阶为2元素带来的歧义，保证了严格的非延展性。

**[可验证加密协议的证明目标]**
$$PK\{(r, m, s): u^2 = g^{2r} \wedge e^2 = y_1^{2r} h^{2m} \wedge v^2 = (y_2 y_3^{\mathcal{H}_{hk}(u,e,L)})^{2r} \wedge \delta = \gamma^m \wedge \mathfrak{k} = \mathfrak{g}^m \mathfrak{h}^s \wedge -n/2 < m < n/2\}$$
> 作用：以标准符号形式刻划了可验证加密协议需要证明的知识，清晰地表明了证明方需要同时证明加密的正确性、消息与给定离散对数的对应关系，以及消息在合法区间内。

**[可验证解密协议的核心等式]**
$$u^{2(x_2 + \mathcal{H}_{hk}(u,e,L) x_3)} / v^2 = 1 \quad \text{and} \quad (e/u^{x_1})^2 / h^{2m} = 1$$
> 作用：这两个等式是判断密文$(u,e,v)$是否有效且是否解密为特定消息$m$的核心。证明或反驳这些等式构成了可验证解密协议的核心。

**[不等式证明的辅助承诺构造]**
$$C_1 := (u^{x_2+\mathcal{H}_{hk}(u,e,L)x_3}/v)^{2n a_1}, \quad C_2 := (u^{x_2+\mathcal{H}_{hk}(u,e,L)x_3}/v)^{2a_2}, \quad C_3 := (u^{x_1}/e)^{2n a_3}, \quad C_4 := (u^{x_1} h^m/e)^{2a_4}$$
> 作用：当需要证明密文无效或解密结果不匹配时，利用这四个承诺$C_i$来分别对应四种不同的“等式不成立”的情况。证明方通过或协议表明知道其中某个$C_i$是非1元素，从而实现证明。

### 实验结果

本文未提供实验数据或基准测试结果。论文的分析集中在计算复杂性的理论上，通过计数不同模数下的平方运算次数和群运算次数来评估效率。例如，在协议参数$n$约1024位、$\rho$约160位、$\ell \approx 160$的典型设置下，加密算法需要3次模$n^2$下的平方运算，解密算法需要5次。可验证加密协议中，证明方需要进行2次模$n$平方、3次模$n^2$平方和$\ell'$次群运算，验证方同样需要3次模$n^2$平方、$\ell$次模$n$平方和$\ell'$次群运算。这些计算量分析表明协议是“高效”的。方案整体复杂度与所加密的基的数量（若加密的是表示而非单个离散对数）成线性关系。没有提及具体的硬件环境或对比基线。

### 局限性与开放问题

该方案的协议在设计上属于Σ-协议，即满足了特殊诚实验证者零知识，若要实现完全零知识或抵抗恶意验证者，需要额外使用Damgård [Dam00] 等人提出的转换技术，这会增加一定的开销。可验证解密协议的计算复杂度是可验证加密协议的一到四倍，但其结构相当复杂，尤其是用于证明不匹配或无效密文的“或”协议部分，理解和实现的门槛较高。此外，部分安全性假设（如强RSA假设和因子分解假设）的安全性强度与帕利埃假设不同，其严格的下界关系还有待进一步研究。协议的交互性也是一个问题，虽然可以通过Fiat-Shamir转化为非交互，但这会引入随机预言机模型。

### 强关联论文

[CS02] J. Camenisch and V. Shoup. Practical verifiable encryption and decryption of discrete logarithms. **IACR ePrint 2002** [Google Scholar](https://scholar.google.com/scholar?q=Practical+verifiable+encryption+and+decryption+of+discrete+logarithms)

[Sta96] M. Stadler. Publicly verifiable secret sharing. **EUROCRYPT 1996** [Google Scholar](https://scholar.google.com/scholar?q=Publicly+verifiable+secret+sharing)

[Bou00] F. Boudot. Efficient proofs that a committed number lies in an interval. **EUROCRYPT 2000** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+proofs+that+a+committed+number+lies+in+an+interval)

[ASW00] N. Asokan, V. Shoup, and M. Waidner. Optimistic fair exchange of digital signatures. **IEEE Journal on Selected Areas in Communications 2000** [Google Scholar](https://scholar.google.com/scholar?q=Optimistic+fair+exchange+of+digital+signatures)

[BS02] E. Bresson and J. Stern. Proofs of knowledge for non-monotone discrete-log formulae and applications. **ISC 2002** [Google Scholar](https://scholar.google.com/scholar?q=Proofs+of+knowledge+for+non-monotone+discrete-log+formulae+and+applications)

[CS01] R. Cramer and V. Shoup. Universal hash proofs and a paradigm for adaptive chosen ciphertext secure public-key encryption. **IACR ePrint 2001** [Google Scholar](https://scholar.google.com/scholar?q=Universal+hash+proofs+and+a+paradigm+for+adaptive+chosen+ciphertext+secure+public-key+encryption)

[CDS94] R. Cramer, I. Damgård, and B. Schoenmakers. Proofs of partial knowledge and simplified design of witness hiding protocols. **CRYPTO 1994** [Google Scholar](https://scholar.google.com/scholar?q=Proofs+of+partial+knowledge+and+simplified+design+of+witness+hiding+protocols)

[Dam00] I. Damgård. Efficient concurrent zero-knowledge in the auxiliary string model. **EUROCRYPT 2000** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+concurrent+zero-knowledge+in+the+auxiliary+string+model)

[YY98] A. Young and M. Yung. Auto-recoverable auto-certifiable cryptosystems. **EUROCRYPT 1998** [Google Scholar](https://scholar.google.com/scholar?q=Auto-recoverable+auto-certifiable+cryptosystems)

[CD00] J. Camenisch and I. Damgård. Verifiable encryption, group encryption, and their applications to group signatures and signature sharing schemes. **ASIACRYPT 2000** [Google Scholar](https://scholar.google.com/scholar?q=Verifiable+encryption%2C+group+encryption%2C+and+their+applications+to+group+signatures+and+signature+sharing+schemes)


## 关键词

+ 零知识
+ 密码学
+ 协议