---
title: "Efficient zero-knowledge proof of algebraic and non-algebraic statements with applications to privacy preserving credentials"

标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 2016
modified: 2025-04-14 09:56:54
---

## Efficient zero-knowledge proof of algebraic and non-algebraic statements with applications to privacy preserving credentials

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-662-53015-3_18)

## 作者

+ [Melissa Chase](Melissa%20Chase.md)
+ [Chaya Ganesh](Chaya%20Ganesh.md)
+ [Payman Mohassel](Payman%20Mohassel.md)
## 笔记

### 背景与动机
零知识证明允许证明者在不透露任何额外信息的情况下,使验证者相信某个陈述为真,是隐私保护协议的核心工具。然而,高效的零知识证明技术目前仅适用于少数受限的语言集合。现有最实用的方案分为两类:一类是基于 Sigma 协议的代数证明,能高效处理离散对数、根等代数关系;另一类是基于混淆电路的非代数证明 [JKO13],能高效处理布尔电路,如哈希函数或分组密码。尽管在孤立场景下各自高效,但许多实际应用,例如证明对标准 RSA 或 DSA 签名的知识,其验证过程同时包含哈希计算和模幂运算,需要同时证明代数与非代数语句。简单地组合两种协议会导致安全问题,因为恶意证明者可能对代数部分和非代数部分使用不同的证据。本文旨在填补这一空白,设计一种能够结合代数与非代数证明系统优势的通用框架,并应用于隐私保护的凭证系统。

### 相关工作

[Cha86] Chaum, D. Showing credentials without identification. **EUROCRYPT 1985**
> 核心思路：首次提出匿名凭证的概念。
> 局限与区别：该原始构造缺乏实用效率。

[CL01] Camenisch, J.L., Lysyanskaya, A. An efficient system for nontransferable anonymous credentials with optional anonymity revocation. **EUROCRYPT 2001**
> 核心思路：提出了基于 Sigma 协议的高效匿名凭证系统,其签名方案专为支持零知识证明而设计。
> 局限与区别：该方法要求凭证必须基于特殊构造的签名,无法直接使用标准签名 (如 RSA-FDH) 作为凭证。

[GQ88] Guillou, L.C., Quisquater, J.-J. A practical zero-knowledge protocol fitted to security microprocessor minimizing both transmission and memory. **EUROCRYPT 1988**
> 核心思路：提出了证明根关系的 Sigma 协议。
> 局限与区别：仅适用于代数关系,无法高效处理非代数运算。

[JKO13] Jawurek, M., Kerschbaum, F., Orlandi, C. Zero-knowledge using garbled circuits: how to prove non-algebraic statements efficiently. **ACM CCS 2013**
> 核心思路：提出了基于混淆电路的零知识证明协议,对非代数语句（如哈希函数）非常高效。
> 局限与区别：当输入需要绑定到代数承诺时,若将解承诺（指数运算）填入电路,会使代价极其高昂。本文将其作为核心构建块,但需要额外的机制来绑定证据。

[Sch90] Schnorr, C.-P. Efficient identification and signatures for smart cards. **CRYPTO 1989**
> 核心思路：提出了证明离散对数知识的 Sigma 协议。
> 局限与区别：同 [GQ88],仅适用于代数关系。

[FNO15] Frederiksen, T.K., Nielsen, J.B., Orlandi, C. Privacy-free garbled circuits with applications to efficient zero-knowledge. **EUROCRYPT 2015**
> 核心思路：指出在 GC-based ZK 证明中,由于验证者无私密输入,可以采用隐私自由混淆电路,将通信和计算减半。
> 局限与区别：该技术不适用于本文第二构造（其中需要隐藏 MAC 密钥）。

[ZRE15] Zahur, S., Rosulek, M., Evans, D. Two halves make a whole. **EUROCRYPT 2015**
> 核心思路：提出了半门技术进行 AND 门的混淆,将混淆电路大小降至 2g 个密文（g 为非 XOR 门数量）。
> 局限与区别：该文献主要关注通用 2PC 的效率提升,本文将其作为底层优化技术引用。

### 核心技术与方案

本文旨在解决的核心问题是：如何在不对代数承诺进行昂贵解承诺（即不将指数运算放入电路）的前提下,证明一个代数承诺 $C = \text{Com}(x)$ 中的 $x$ 满足一个非代数关系 $f(x)=1$。整体框架基于 [JKO13] 的 GC-based ZK 协议,但设计了两类方案将证明者输入 $x$ 的代数承诺 $C$ 与混淆电路中的输入 $x'$ 进行绑定。

**第一构造：基于位承诺的方案 ($\pi_{\text{Com},f}$)。** 该方案的思路是让证明者先对 $x$ 的每一位 $x_i$ 进行代数承诺 $C_i$。在 GC 阶段,证明者通过 Committing OT 获取与 $x_i$ 对应的混淆输入线标签 $K_i'$。然后,证明者再承诺这些线标签 $K_i'$。关键的绑定步骤在于：当验证者在 GC 评估后打开 OT（公布所有输入线标签 $K_i^0, K_i^1$）时,证明者需要通过零知识证明线性关系 $K_i' = x_i K_i^1 + (1-x_i) K_i^0$。由于 Pedersen 承诺支持高效的线性关系证明,这一步无需在混淆电路内进行。此外,还需证明 $x = \sum 2^i x_i$。此方案的安全性直觉是：若证明者在 OT 中使用的 $x'$ 与承诺中的 $x$ 不同,则他必须正确猜测至少一个线标签（如 $x_i=0$ 时猜 $K_i^1$）,这被 Committing OT 和证明步骤所阻止。该方案的公钥操作数与输入 $x$ 的比特数 $n$ 成正比（位承诺和线性关系证明）,对称密钥操作数与电路 $f$ 的规模成正比。

**第二构造：基于一次性 MAC 的方案 ($\Pi_{\text{MAC},f}$)。** 此方案旨在减少公钥操作,将绑定任务部分转移至混淆电路内部。其核心是让混淆电路不仅计算 $f(x)$，还计算一个一次性 MAC: $t = a x + b$，其中 $a$ 是 $s$ 比特的随机数（$s$ 为统计安全参数）,$b$ 是 $n+s$ 比特的随机偏移,均由验证者秘密选取。验证者需先承诺 $a,b$ 并证明知识。证明者评估电路后得到输出的真值 $Z$ 和 MAC 标签 $t$，并承诺 $t$。然后,验证者打开 $a,b$ 和 OT 输入（打开混淆电路）。证明者检查电路正确性后,通过零知识证明 $t = a x + b$（均在整数域上）。由于 $a$ 和 $b$ 最初对证明者保密（通过混淆电路的隐私性）,证明者无法预先伪造一个不同的 $x'$ 的正确 MAC。此方案的公钥操作数仅为常数（与 $s$ 无关）,但对称密钥操作数增加了约 $O( n s + s^2 )$（用于电路内的乘法）。可通过使用更小的 $s$（例如 40-80 位）和 Karatsuba 乘法来优化。

**安全性与零知识。** 两个方案均被证明能安全实现理想功能 $\mathcal{F}_{\text{Com},f}$。安全证明在理想/现实世界范式下进行。简而言之,对恶意证明者,模拟器通过 OT 提取证明者的输入 $x'$,通过知识提取器提取承诺中的 $x$ 和线标签,若存在不一致（如 $x \neq x'$ 但能通过证明）,则能构造攻击者破坏 MAC 安全性或承诺绑定性。对恶意验证者,模拟器可以提取其输入,在看不到真实 $x$ 的情况下使用模拟器生成零知识证明和电路输出,通过承诺的隐藏性和零知识性证明不可区分。

**应用扩展。** 基于上述核心协议,本文构建了多个重要模块：
1.  证明哈希关系：通过本文协议证明输入 $(m, \mathcal{H}(m))$ 满足 $f(m, M) = [\mathcal{H}(m) == M]$。
2.  跨群相等性证明：先将值在两个不同群中进行承诺,再利用本文协议证明其在数值上相等。
3.  FDH-RSA 签名证据证明：结合证明哈希关系的模块,和证明 e 次根的 Sigma 协议 [CS97a],证明承诺的哈希值与 RSA 签名值的 e 次方在模 N 下相等。
4.  DSA/ECDSA 签名证据证明：利用上述跨群相等性证明和“指数与底数的承诺相等”的新型 Sigma 协议（图9）,来证明复杂的签名验证等式 $\alpha = g^{u_1}$ 和 $r = \alpha \beta \mod q$ 等关系。

### 核心公式与流程

**[Sigma 协议：证明跨群底数相同的离散对数]**
$$ \begin{aligned} &\text{Prover}(\alpha_i, \beta_i, \gamma_i): \\
&u_i = G_1^{g^{\alpha_i}} H_1^{\beta_i}, \quad v_i = G_2^{\alpha_i} H_2^{\gamma_i} \\
&\text{Verifier}(c \in \{0,1\}^k): \\
&\text{If } c_i=0: (r_i, s_i, t_i) = (\alpha_i, \beta_i, \gamma_i) \\
&\text{If } c_i=1: (r_i, s_i, t_i) = (\alpha_i - x, \beta_i - R_1 g^{r_i}, \gamma_i - R_2) \\
&\text{Check for } c_i=0: u_i = G_1^{g^{r_i}} H_1^{s_i} \wedge v_i = G_2^{r_i} H_2^{t_i} \\
&\text{Check for } c_i=1: u_i = y_1^{g^{r_i}} H_1^{s_i} \wedge v_i = y_2 G_2^{r_i} H_2^{t_i}
\end{aligned} $$
> 作用：证明秘密值 $x$ 同时在两个不同群 $\mathbb{G}_1$ 和 $\mathbb{G}_2$ 的承诺 $y_1 = G_1^{g^x} H_1^{R_1}$ 和 $y_2 = G_2^x H_2^{R_2}$ 中。（详见原文图9）

**[核心协议 $\pi_{\text{Com},f}$ 的绑定检查]**
$$ \begin{aligned} &\text{PK}\{(x_i, K_i', r, R): \\
&\quad C_i = \text{Com}(x_i) \wedge C_{K_i} = \text{Com}(K_i') \wedge \\
&\quad K_i' = x_i K_i^1 + (1 - x_i) K_i^0 \}, \forall 1 \leq i \leq n.
\end{aligned} $$
> 作用：证明证明者从 OT 获得的线标签 $K_i'$ 与其位承诺 $x_i$ 一致,从而将代数承诺与混淆电路绑定。

### 实验结果
论文本身未提供实验数据,但进行了详细的渐进复杂度分析。第一构造 $\pi_{\text{Com},f}$ 的公开密钥操作（模乘）正比于输入 $x$ 的比特长度 $n$,对称密钥操作（哈希、对称加密）正比于电路 $f$ 的非 XOR 门数量。第二构造 $\Pi_{\text{MAC},f}$ 的公开密钥操作仅常数,但对称密钥操作正比于 $O(ng + s^2)$,其中 $g$ 指 $f$ 的门数,$s$ 是统计安全参数（建议 40-80 位）。在典型参数下（如 $n=256, s=60$）,第二方案公钥操作约 3 次（承诺和 ZK 证明）,第一方案约 512 次。但第二方案需额外实现 $a x + b$ 的乘法电路,增加约 2 万个非 XOR 门。总体而言,若 $n$ 小或已有位承诺,第一方案更优；若 $n$ 大或公钥操作昂贵,第二方案更优。文中引用了 [KSS09] 中关于常见电路的规模：比较或相等性测试电路约 $4\ell$ 个非 XOR 门；乘法电路约 $8\ell^2 - 4\ell$ 个非 XOR 门。

### 局限性与开放问题
本文专注于单方秘密输入（证明者输入）的 ZK 证明,在扩展到安全的双方计算（2PC）时,目前仅支持将证明者的输入绑定到承诺,而验证者输入的处理仍需进一步研究。此外,虽然第二构造减少了公钥操作,但其引入的乘法电路在对称密钥操作上的开销仍需优化。文中讨论的 Karatsuba 乘法可作为优化方向。最后,所有构造的安全性均在标准模型加上随机预言机或 CRS 模型下证明,能否在无随机预言机下实现更高效的同时证明也是一个开放问题。

### 强关联论文

[CL01] Camenisch, J.L., Lysyanskaya, A. An efficient system for nontransferable anonymous credentials with optional anonymity revocation. **EUROCRYPT 2001** [Google Scholar](https://scholar.google.com/scholar?q=An+efficient+system+for+nontransferable+anonymous+credentials+with+optional+anonymity+revocation)

[CS97a] Camenisch, J.L., Stadler, M.A. Efficient group signature schemes for large groups. **CRYPTO 1997** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+group+signature+schemes+for+large+groups)

[FNO15] Frederiksen, T.K., Nielsen, J.B., Orlandi, C. Privacy-free garbled circuits with applications to efficient zero-knowledge. **EUROCRYPT 2015** [Google Scholar](https://scholar.google.com/scholar?q=Privacy-free+garbled+circuits+with+applications+to+efficient+zero-knowledge)

[GQ88] Guillou, L.C., Quisquater, J.-J. A practical zero-knowledge protocol fitted to security microprocessor minimizing both transmission and memory. **EUROCRYPT 1988** [Google Scholar](https://scholar.google.com/scholar?q=A+practical+zero-knowledge+protocol+fitted+to+security+microprocessor+minimizing+both+transmission+and+memory)

[JKO13] Jawurek, M., Kerschbaum, F., Orlandi, C. Zero-knowledge using garbled circuits: how to prove non-algebraic statements efficiently. **ACM CCS 2013** [Google Scholar](https://scholar.google.com/scholar?q=Zero-knowledge+using+garbled+circuits+how+to+prove+non-algebraic+statements+efficiently)

[Sch90] Schnorr, C.-P. Efficient identification and signatures for smart cards. **CRYPTO 1989** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+identification+and+signatures+for+smart+cards)

[ZRE15] Zahur, S., Rosulek, M., Evans, D. Two halves make a whole. **EUROCRYPT 2015** [Google Scholar](https://scholar.google.com/scholar?q=Two+halves+make+a+whole)


## 关键词

+ 代数非代数陈述零知识证明
+ 混淆电路sigma协议结合框架
+ 隐私保护凭证标准签名RSA ECDSA
+ 非代数关系证明高效组合构造
+ 安全两方计算承诺签名输入