---
title: "Privacy-preserving blueprints"
doi: 10.1007/978-3-031-30617-4_20
标题简称:
论文类型: conference
会议简称: EUROCRYPT
发表年份: 2023
modified: 2025-05-13 04:16:09
created: 2025-04-15 11:15:43
---
## Privacy-preserving blueprints

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-30617-4_20)

## 作者

+ [Markulf Kohlweiss](Markulf%20Kohlweiss.md)
+ [Anna Lysyanskaya](Anna%20Lysyanskaya.md)
+ An Nguyen

## 笔记

### 背景与动机
匿名凭证系统使得用户可以证明自己持有凭证而不泄露身份，实现隐私保护 [2,17–19,27,54,55]。然而这种机制也带来了一个根本性矛盾：如果所有访问控制都使用匿名凭证，那么违规者将完全无法被追溯，合法的监管需求（如追踪非法交易或恐怖嫌疑人）将无法实现。现有的监督机制，如身份托管 [3,51] 和组签名 [1,5,22,29,51]，要么让受托人总能恢复用户身份，要么无法与匿名凭证系统无缝集成。本文提出的隐私保护蓝图旨在填补这一空白：允许审计者发布一个编码，用户基于此编码和自身数据生成一个托管值，审计者仅能从托管值中恢复特定函数的结果，且仅当用户数据满足某种条件时才恢复，否则得不到任何信息。这为隐私保护与问责之间的平衡提供了一种模块化的密码学解决方案。

### 相关工作

[2] Baldimtsi, F., Lysyanskaya, A. Anonymous credentials light. **ACM CCS 2013** [Google Scholar](https://scholar.google.com/scholar?q=Anonymous+credentials+light)
> 核心思路：提出轻量级匿名凭证方案，用户无需暴露身份即可证明凭证持有权。
> 局限与区别：该方案缺乏对违规者追溯的机制，本文在此基础上增加了可选的、有条件的审计能力。

[1] Ateniese, G., Camenisch, J., Joye, M., Tsudik, G. A practical and provably secure coalition-resistant group signature scheme. **CRYPTO 2000** [Google Scholar](https://scholar.google.com/scholar?q=A+practical+and+provably+secure+coalition-resistant+group+signature+scheme)
> 核心思路：用户以群组名义匿名签名，受托人总能打开签名恢复用户身份。
> 局限与区别：身份恢复是强制性的，与本文有条件恢复（仅当匹配监视列表时）不同。

[42] Freedman, M.J., Nissim, K., Pinkas, B. Efficient private matching and set intersection. **EUROCRYPT 2004** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+private+matching+and+set+intersection)
> 核心思路：通过多项式求值实现私有集合交集，两方交互计算交集元素。
> 局限与区别：PSI 是交互式协议，而本文的审计者在用户生成托管值时是离线的。

[49] Green, M., Kaptchuk, G., Van Laer, G. Abuse resistant law enforcement access systems. **EUROCRYPT 2021** [Google Scholar](https://scholar.google.com/scholar?q=Abuse+resistant+law+enforcement+access+systems)
> 核心思路：为加密通信设计法律授权访问系统，服务器可验证密文是否允许接入。
> 局限与区别：ARLEAS 关注加密通信的执法访问，本文关注匿名认证场景下的可选审计。

[51] Kilian, J., Petrank, E. Identity escrow. **CRYPTO 1998** [Google Scholar](https://scholar.google.com/scholar?q=Identity+escrow)
> 核心思路：引入身份托管权威，在需要时可揭示用户真实身份。
> 局限与区别：身份揭示是无条件的，本文的揭示取决于用户数据是否匹配审计者秘钥中的条件。

[46] Gentry, C. Fully homomorphic encryption using ideal lattices. **STOC 2009** [Google Scholar](https://scholar.google.com/scholar?q=Fully+homomorphic+encryption+using+ideal+lattices)
> 核心思路：提出首个全同态加密方案，可对密文进行任意计算。
> 局限与区别：本文的通用构造基于 CP-FHE，但更侧重与 NIZK 结合实现蓝图系统的实用性。

[60] Ostrovsky, R., Paskin-Cherniavsky, A., Paskin-Cherniavsky, B. Maliciously circuit-private FHE. **CRYPTO 2014** [Google Scholar](https://scholar.google.com/scholar?q=Maliciously+circuit-private+FHE)
> 核心思路：提出恶意敌手模型下的电路隐私全同态加密。
> 局限与区别：本文的 HEC 通用构造依赖 CP-FHE 来隐藏用户输入 y，并直接用于构建蓝图方案。

[63] Sakai, Y., Emura, K., Hanaoka, G., Kawai, Y., Matsuda, T., Omote, K. Group signatures with message-dependent opening. **Pairing 2012** [Google Scholar](https://scholar.google.com/scholar?q=Group+signatures+with+message-dependent+opening)
> 核心思路：组签名中打开权限依赖于消息本身，可以恢复用户私密信息的函数。
> 局限与区别：该场景下用户已知两个输入，而蓝图方案中用户只知道自己的输入 y，不知道审计者的 x。

[64] Scafuro, A. Break-glass encryption. **PKC 2019** [Google Scholar](https://scholar.google.com/scholar?q=Break-glass+encryption)
> 核心思路：审计者可解密用户的密文，但解密行为会可靠地暴露给各方（打破玻璃）。
> 局限与区别：方案依赖硬件令牌或区块链等强假设，本文的方案基于标准密码学假设。

### 核心技术与方案

本文的整体框架是一个模块化的 $f$-蓝图系统，由三个核心参与者（审计者、用户、验证者）和六个算法构成：Setup、KeyGen、VerPK、Escrow、VerEscrow、Decrypt。该系统依赖于一个非交互承诺方案、一个同态足够加密系统（HEC）以及两个非交互零知识证明系统。

**构建思路**：审计者运行 HECenc 对其输入 $x$ 进行编码，输出一个加密表示 $X$ 和对应的解密密钥 $d$，并通过 NIZK 证明 $X$ 与公开的承诺 $C_A$ 一致。用户利用 HECeval，基于审计者的 $X$ 和自己的输入 $y$，同态地计算出一个加密值 $Z$，使得 $Z$ 在解密下得到 $f(x,y)$。用户还需提供一个 NIZK 证明 $Z$ 是从 $y$ 的正确承诺 $C$ 和 $X$ 计算得到的。验证者通过 VerPK 验证审计者的公钥，并通过 VerEscrow 验证用户的托管值。审计者最后通过 Decrypt 恢复 $f(x,y)$。

**基于 DDH 的实用构造 (ElGamalHEC)**：针对监视列表函数 $f_k(x,y)=y$ 若 $\text{lobits}_k(y) \in x$，否则 $\emptyset$，该构造使用 ElGamal 加密。审计者随机选择 $s \in \mathbb{Z}_q^*$，生成多项式 $P(\chi) = s \prod_{i=1}^{|x|}(\chi - x_i)$，并输出其系数的 ElGamal 加密作为 $X$。用户计算 ElGamal 密文 $\text{eval} = \bigoplus_{i=0}^{|x|} C_i^{y_2^i}$，即加密了 $p(y_2)$，然后通过 $\text{eval}^r \oplus \text{Enc}(\text{pk}, g^y)$ 得到 $Z$。这里 $y_2 = \text{lobits}_k(y)$。如果 $y_2$ 是多项式的根，则 $p(y_2)=0$，$Z$ 解密得到 $g^y$，审计者通过哈希即可恢复 $y$；否则 $p(y_2)$ 是一个随机值，$Z$ 解密也得到一个随机值，审计者无法恢复 $y$。

**安全性证明直觉**：HEC 的正确性证明通过 ElGamal 的 IND-CPA 安全性归约，若敌手能让不正确情况发生，则可将区分 $P_0$ 与 $P_1$ 的问题归约到 ElGamal 安全性。蓝图系统的安全性证明依赖于 HEC 的安全性（包括对 x 的隐藏、对 x 和 y 的联合隐藏、以及 DirectZ 的安全性）和 NIZK 的零知识性和 BB-PSL 模拟可提取性。例如在“蓝图隐藏”性中，模拟器 SimKeygen 可以在不知道 $x$ 的情况下生成 $pk_A$，并通过 SimDecrypt 根据 $f(x,y)$ 回答解密查询，从而证明 $pk_A$ 不泄露 $x$ 本身。

**渐进复杂度**：针对监视列表的构造，$pk_A$ 的大小为 $O(\lambda n)$，其中 $n$ 是监视列表大小，$\lambda$ 是安全参数。Escrow $Z$ 的大小也是 $O(\lambda n)$。这线性于表示一个群元素所需的比特数乘以列表长度，是最优的。密钥生成和托管生成的通信复杂度与这两个大 $O$ 一致。验证者运行 VerPK 和 VerEscrow 的计算量涉及多次指数运算，但仍是多项式时间。

### 核心公式与流程

**[监视列表函数定义]**
$$f(x,y) = \left\{ \begin{array}{ll} y & \text{if } y = y_1 \| y_2 \text{ and } y_2 \in x \\ \bot & \text{otherwise} \end{array} \right.$$
> 作用：定义蓝图系统要实现的特定函数，用户数据 $y$ 的前 $\mathcal{O}(\log \lambda)$ 位为 $y_1$，后 $k$ 位 $y_2$，若 $y_2$ 在审计者的集合 $x$ 中则恢复完整的 $y$。

**[ElGamalHEC 的加密过程]**
$$
\begin{aligned}
&\text{HECenc(hecpar}, f_k, x):\\
&\quad s \xleftarrow{\$} \mathbb{Z}_q^*\\
&\quad P(\chi) \leftarrow s \prod_{i=1}^{|x|}(\chi - x_i)\\
&\quad \text{for } i \in \{0, \dots, |x|\}:\\
&\qquad C_i \leftarrow \text{Enc}(\text{pk}_E, g^{P_i})\\
&\quad \text{return } X = (\text{pk}_E, C_0, \dots, C_{|x|}), d = \text{sk}_E
\end{aligned}
$$
> 作用：审计者将他的输入 $x$ 编码为多项式 $P$ 系数的 ElGamal 加密。$s$ 是一个随机因子，用于防止用户在 $y_2 \notin x$ 时推导出多项式值并篡改密文。

**[ElGamalHEC 的导出过程]**
$$
\begin{aligned}
&\text{HECeval(hecpar}, f_k, X, y):\\
&\quad y_2 \leftarrow \text{lobits}_k(y)\\
&\quad \text{eval} = \bigoplus_{i=0}^{|x|} C_i^{y_2^i}\\
&\quad \text{enc} \leftarrow \text{Enc}(\text{pk}_E, g^y)\\
&\quad r \xleftarrow{\$} \mathbb{Z}_q\\
&\quad \text{return } Z = \text{eval}^r \oplus \text{enc}
\end{aligned}
$$
> 作用：用户利用 ElGamal 同态性，通过审计者的加密系数计算多项式在 $y_2$ 处的求值结果，并以此加密 $g^y$ 得到最终的托管值。若 $y_2$ 是多项式根，则 $Z$ 解密为 $g^y$；否则解密为随机值。

**[ElGamalHEC 的解密过程]**
$$
\begin{aligned}
&\text{HECdec(hecpar}, d, Z):\\
&\quad D \leftarrow \text{Dec}(\text{sk}_E, Z)\\
&\quad \text{for } y' \in \text{domain}_{f,y} \text{ and } \text{lobits}_k(y') \in x:\\
&\qquad \text{if } g^{y'} = D:\\
&\qquad\quad \text{return } y'\\
&\quad \text{return } \emptyset
\end{aligned}
$$
> 作用：审计者解密 $Z$ 得到一个群元素 $D$，然后通过穷举所有可能的 $y'$（其低 $k$ 位在集合 $x$ 中）来判断哪个 $y'$ 等于 $\log_g D$。由于 $|x| \cdot 2^{l_y - k}$ 是多项式大小，此步骤高效。

### 实验结果
本文是纯粹的理论密码学论文，并未提供实验评估或具体的性能数据。文中没有描述软件实现、硬件环境或对比基线。文中提到的“efficient”、“practical”、“optimal”等术语均基于理论渐进复杂度分析。例如，针对监视列表的构造声称 $pk_A$ 和 Escrow $Z$ 的大小均为 $O(\lambda n)$ 是最优的，但未给出具体的比特数或运行时间。对于通用构造（基于 FHE 和 NIZK），论文明确承认其“理论上有趣但不足以实用”，因此仅作为存在性结果。

### 局限性与开放问题
本文的通用构造依赖全同态加密和通用 NIZK，效率极低，无法实际应用。针对监视列表的实用构造虽然效率较好，但仅适用于特定的 $f(x,y)=y$ if $y_2 \in x$ 函数族，扩展至更广泛的函数需要新的 HEC 构造。此外，如何在非随机预言机模型下（例如标准模型或 CRS 模型）实现蓝图系统，同时保持高效的证明和可提取性，仍是一个挑战。最后，如何将蓝图系统无缝集成到现有的匿名凭证或电子现金系统中，并保证整体安全性，也是未来工作的方向。

### 强关联论文

[2] Baldimtsi, F., Lysyanskaya, A. Anonymous credentials light. **ACM CCS 2013** [Google Scholar](https://scholar.google.com/scholar?q=Anonymous+credentials+light)

[42] Freedman, M.J., Nissim, K., Pinkas, B. Efficient private matching and set intersection. **EUROCRYPT 2004** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+private+matching+and+set+intersection)

[46] Gentry, C. Fully homomorphic encryption using ideal lattices. **STOC 2009** [Google Scholar](https://scholar.google.com/scholar?q=Fully+homomorphic+encryption+using+ideal+lattices)

[49] Green, M., Kaptchuk, G., Van Laer, G. Abuse resistant law enforcement access systems. **EUROCRYPT 2021** [Google Scholar](https://scholar.google.com/scholar?q=Abuse+resistant+law+enforcement+access+systems)

[51] Kilian, J., Petrank, E. Identity escrow. **CRYPTO 1998** [Google Scholar](https://scholar.google.com/scholar?q=Identity+escrow)

[60] Ostrovsky, R., Paskin-Cherniavsky, A., Paskin-Cherniavsky, B. Maliciously circuit-private FHE. **CRYPTO 2014** [Google Scholar](https://scholar.google.com/scholar?q=Maliciously+circuit-private+FHE)

[63] Sakai, Y., Emura, K., Hanaoka, G., Kawai, Y., Matsuda, T., Omote, K. Group signatures with message-dependent opening. **Pairing 2012** [Google Scholar](https://scholar.google.com/scholar?q=Group+signatures+with+message-dependent+opening)

[64] Scafuro, A. Break-glass encryption. **PKC 2019** [Google Scholar](https://scholar.google.com/scholar?q=Break-glass+encryption)


## 关键词

+ 隐私保护蓝图
+ 匿名凭证
+ 秘密监视名单
+ DDH假设
+ 访问控制与可追踪性                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   