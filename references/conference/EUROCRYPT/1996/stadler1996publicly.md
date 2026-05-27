---
title: "Publicly verifiable secret sharing"
doi: 10.1007/3-540-68339-9_17
标题简称:
论文类型: conference
会议简称: EUROCRYPT
发表年份: 1996
---
## Publicly verifiable secret sharing

## 发表信息

+ [原文链接]()

## 作者

+ Markus Stadler 


## 笔记

### 背景与动机
秘密共享方案允许将秘密分割为多个份额分发给参与者，使得只有特定集合的参与者才能恢复秘密，这一概念由Shamir [20] 和Blakley [2] 分别独立提出。然而，传统的秘密共享方案无法抵御作弊参与者：恶意参与者可能在恢复阶段提交虚假份额，导致秘密恢复失败或恢复出错误结果；同时，不诚实的分发者也可能分发虚假份额，使得不同参与者群体恢复出不同的秘密。为了解决这些问题，Chor 等人在1985年提出的可验证秘密共享（VSS）[7] 通过引入验证算法，使得诚实的参与者能够确保他们所持有的份额最终能恢复出一个唯一的秘密。值得注意的是，VSS的首个实现方案 [7] 具有一个非常特殊的性质：不仅参与者，而且任何外部观察者都能验证份额是否正确分发。这一性质在后续的协议设计中被保留，但并未被系统地命名为一种独立原语。本文正式定义了公开可验证的秘密共享（PVSS）方案，并指出其在软件密钥托管系统和具有可撤销匿名性的电子支付系统中的全新应用价值。现有的VSS方案如Feldman的方案 [11] 只能让参与者验证自身的份额，而无法验证其他参与者份额的正确性，这在需要公开审计的场景中存在局限。本文填补的空白是：提出首个可证明安全的、基于ElGamal密码系统 [9] 的非交互式PVSS方案，并支持一般的单调访问结构，而不仅仅是阈值结构。

### 相关工作

[2] Blakley. Safeguarding cryptographic keys. **AFIPS 1979** [Google Scholar](https://scholar.google.com/scholar?q=Safeguarding+cryptographic+keys)
> 核心思路：利用几何（超平面）方法构造秘密共享方案。
> 局限与区别：该方案不具备可验证性，无法抵抗作弊分发者；本文在此基础上增加了公开可验证性。

[7] Chor等. Verifiable secret sharing and achieving simultaneity in the presence of faults. **FOCS 1985** [Google Scholar](https://scholar.google.com/scholar?q=Verifiable+secret+sharing+and+achieving+simultaneity+in+the+presence+of+faults)
> 核心思路：首次提出VSS概念，其首个实现方案允许所有人验证份额的正确性。
> 局限与区别：该方案效率较低且没有显式地抽象出公开可验证的定义；本文将其一般化为PVSS并给出基于离散对数的高效构造。

[11] Feldman. A practical scheme for non-interactive verifiable secret sharing. **FOCS 1987** [Google Scholar](https://scholar.google.com/scholar?q=A+practical+scheme+for+non-interactive+verifiable+secret+sharing)
> 核心思路：提出非交互式VSS方案，通过验证承诺 $g^{s_i}$ 使份额持有者可以验证自己的份额。
> 局限与区别：该方案只能让参与者验证自己的份额，无法让他人验证；本文通过加密份额并使用公开校验协议解决了此问题。

[9] ElGamal. A public key cryptosystem and a signature scheme based on discrete logarithms. **IEEE IT 1985** [Google Scholar](https://scholar.google.com/scholar?q=A+public+key+cryptosystem+and+a+signature+scheme+based+on+discrete+logarithms)
> 核心思路：基于Diffie-Hellman密钥交换设计加密和签名方案。
> 局限与区别：原方案未考虑可验证加密；本文利用其同态性质设计了可验证加密离散对数的协议。

[12] Fiat and Shamir. How to prove yourself: Practical solution to identification and signature problems. **CRYPTO 1986** [Google Scholar](https://scholar.google.com/scholar?q=How+to+prove+yourself:+Practical+solution+to+identification+and+signature+problems)
> 核心思路：将交互式零知识证明转换为非交互式签名方案（Fiat-Shamir变换）。
> 局限与区别：本文应用该变换将交互式验证协议转化为非交互式公开验证协议。

[1] Ben-Or等. Completeness theorems for non-cryptographic fault-tolerant distributed computation. **STOC 1988** [Google Scholar](https://scholar.google.com/scholar?q=Completeness+theorems+for+non-cryptographic+fault-tolerant+distributed+computation)
> 核心思路：证明了在安全多方计算中VSS作为关键基础模块的完备性。
> 局限与区别：该工作直接使用VSS作为工具，而本文改进VSS使其具备公开可验证性以支持新的应用场景。

[16] Micali. Fair cryptosystems. **MIT TR 1993** [Google Scholar](https://scholar.google.com/scholar?q=Fair+cryptosystems)
> 核心思路：用户将密钥通过VSS分发给托管代理，实现密钥托管。
> 局限与区别：该方案由接收者决定托管代理集合且难以变更；本文的方案允许发送者通过PVSS为消息指定托管代理。

[21] Stadler等. Fair blind signatures. **EUROCRYPT 1995** [Google Scholar](https://scholar.google.com/scholar?q=Fair+blind+signatures)
> 核心思路：利用VSS实现可撤销匿名的盲签名。
> 局限与区别：未实现公开可验证性；本文提出PVSS方案可更高效地实现可撤销匿名。

### 核心技术与方案

本文提出两个PVSS方案，分别用于共享离散对数和共享 $e$ 次根。

**方案一：共享离散对数的PVSS**

该方案基于ElGamal加密系统 [9] 和一个特殊的交互式/非交互式证明系统。系统参数包括一个大素数 $p$，使得 $q=(p-1)/2$ 也是素数，以及一个 $q$ 阶元素 $h \in Z_p^*$；另有一个阶为 $p$ 的群 $G$，生成元为 $g$。每个参与者 $P_i$ 选取私钥 $z_i \in Z_q$，公布公钥 $y_i = h^{z_i} \pmod p$。分发者（dealer）想要共享秘密 $s \in Z_p$，其中 $S = g^s$ 公开。分发者首先使用一种可验证的秘密共享方案（例如基于Shamir的阈值方案 [11] 或任意通用访问结构方案）计算出份额 $s_i$，使得每个参与者应持有 $s_i$ 满足 $g^{s_i} = S_i$。然后，分发者使用参与者 $P_i$ 的公钥 $y_i$ 加密份额 $s_i$：随机选取 $\alpha_i \in Z_q$，计算密文 $(A_i, B_i) = (h^{\alpha_i}, s_i^{-1} \cdot y_i^{\alpha_i}) \pmod p$。关键挑战在于：公开 $A_i, B_i$ 和 $S_i$ 后，如何让任何人相信密文确实加密了 $s_i = \log_g S_i$。本文的核心技术创新在于设计了针对离散对数加密的公开验证协议。

该协议利用“双重离散对数”概念：需要证明 $\log_h A_i = \log_y (g^{s_i \cdot B_i})$。交互式协议中，证明者随机选取 $w$，发送 $t_h = h^w$ 和 $t_g = g^{(y^w)}$；验证者发送挑战 $c \in \{0,1\}$；证明者回复 $r = w - c \cdot \alpha_i \pmod q$；验证者检查 $t_h = h^r A_i^c \pmod p$ 和 $t_g$ 是否等于 $g^{(y^r)}$（若 $c=0$）或 $S_i^{(B_i \cdot y^r)}$（若 $c=1$）。如果挑战 $c=0$ 和 $c=1$ 都能正确回答，则必然有 $\log_h A_i = \log_y (S_i^{B_i})$。该协议被证明是完美零知识的，且作弊者成功的概率为 $2^{-K}$。通过 Fiat-Shamir 变换 [12]，该协议可非交互化：使用哈希函数 $H_\ell$ 生成挑战，证明为 $(R, c)$。安全性分析表明（命题1），在决策性Diffie-Hellman问题困难假设下，从密文 $(A_i, B_i)$ 和公钥 $S_i$ 中恢复 $s_i$ 是困难的；同时，协议的安全性保证只在挑战响应上作弊的概率为 $2^{-K}$。

**方案二：共享 $e$ 次根的PVSS**

该方案用于在 $Z_n^*$ 中共享一个元素的 $e$ 次根，其中 $n$ 的因式分解未知。每个参与者选取私钥 $z \in Z_n$，公钥 $y = g^z \pmod n$，其中 $g$ 是 $Z_n^*$ 中一个大阶元素。分发者加密 $m$（其中 $M = m^e \pmod n$ 公开）时，随机选取 $\alpha \in Z_n$，计算 $A = g^\alpha \pmod n$，$B = m \cdot y^\alpha \pmod n$。公开验证协议基于如下事实：如果 $B^e / M \equiv y^{e\alpha} \pmod n$，则 $B/A^z$ 是 $M$ 的 $e$ 次根。交互式协议中，证明者选取随机数 $w$，发送 $t_g = g^w$ 和 $t_y = y^{ew} \pmod n$；挑战 $c$ 在 $\{0, \ldots, 2^\ell-1\}$ 中选取；证明者回复 $r = w - c \cdot \alpha$；验证者检查 $t_g = g^r A^c \pmod n$ 和 $t_y = y^{er} (B^e / M)^c \pmod n$。该协议可证明作弊成功的概率至多为 $2^{-K\ell}$，并在 $\ell = O(\log \log n)$ 时是统计零知识的。非交互化后，整个份额的长度约为 $2\ell + (4 + \epsilon) \log_2 n$ 比特，实践推荐 $n > 2^{750}$，$\ell > 80$，$\epsilon \approx 1/5$。然而，由于 $g$ 的阶是非素数的，该方案的安全性证明比方案一弱——如命题1那样的归约不成立。

### 核心公式与流程

**[PVSS模型定义]**
$$ 
S_i = E_i(s_i), \quad i=1,\ldots,n
$$
$$
\exists u \; \forall A \in 2^{\{1,\ldots,n\}}: \big( \text{PubVerify}(\{S_i | i\in A\}) = 1 \big) \; \Rightarrow \; \text{Recover}(\{D_i(S_i) | i \in A\}) = u
$$
> 作用：定义PVSS方案的抽象模型。分发者使用参与者的公钥 $E_i$ 加密份额 $s_i$ 得到公开的加密份额 $S_i$。公开验证算法 PubVerify 确保任意一组加密份额若通过验证，则诚实参与者解密后必能恢复出唯一值 $u$；若分发者诚实，则 $u = s$。

**[方案一：双重离散对数零知识证明]**
$$
\begin{aligned}
&\text{Prover}(x = \log_h A = \log_y (V^B)):\\
&\quad w \in_R \mathbb{Z}_q;\; t_h = h^w (\bmod p);\; t_g = g^{(y^w)}\\
&\text{Verifier:}\; c \in_R \{0,1\}\\
&\text{Prover:}\; r = w - c \cdot x (\bmod q)\\
&\text{Verifier checks:}\\
&\quad t_h \stackrel{?}{=} h^r A^c (\bmod p)\\
&\quad t_g \stackrel{?}{=} 
\begin{cases}
g^{(y^r)} & \text{if } c = 0\\
V^{(B \cdot y^r)} & \text{if } c = 1
\end{cases}
\end{aligned}
$$
> 作用：该交互式协议证明加密值 $m = \log_g V$ 的密文 $(A, B)$ 确实满足 $m^{-1} y^\alpha = B$ 且 $A = h^\alpha$。如果两个挑战 $(c=0, c=1)$ 均能被正确回答，则证明者必知道 $\alpha$，且 $\log_h A = \log_y (V^B)$，从而 $V^B = g^{(y^\alpha)}$。

**[方案二：$e$ 次根加密的零知识证明]**
$$
\begin{aligned}
&\text{Prover}(m \text{ s.t. } M = m^e \bmod n, \text{ ciphertext } (A,B)):\\
&\quad w \in_R \{0,\ldots,\lceil 2^\ell n^{1+\epsilon}\rceil\};\; t_g = g^w (\bmod n);\; t_y = y^{ew} (\bmod n)\\
&\text{Verifier:}\; c \in_R \{0,\ldots,2^\ell-1\}\\
&\text{Prover:}\; r = w - c \cdot \alpha\\
&\text{Verifier checks:}\\
&\quad t_g \stackrel{?}{=} g^r A^c (\bmod n)\\
&\quad t_y \stackrel{?}{=} y^{er} (B^e / M)^c (\bmod n)
\end{aligned}
$$
> 作用：证明密文 $(A, B)$ 中 $m$ 是 $M$ 的 $e$ 次根。核心在于验证 $B^e / M = y^{e\alpha}$，从而 $B/A^z$ 的 $e$ 次幂等于 $M$。

### 实验结果
由于该论文是理论密码学工作，发表于1996年，原文未提供标准的实验性能数据。然而，论文给出了关键参数建议以实现实际可用的方案：对于基于离散对数的方案，建议选择安全素数 $p$ 使 $q=(p-1)/2$ 为素数，并结合一个阶为 $p$ 的群 $G$，其中离散对数问题困难。对于基于 $e$ 次根的方案，论文明确推荐使用 $n > 2^{750}$，$\ell > 80$，$\epsilon \approx 1/5$ 以保障实际安全性，此时非交互证明的份额长度约为 $2\ell + (4 + \epsilon) \log_2 n \approx 160 + 4.2 \cdot 750 \approx 3310$ 比特。方案一的安全性与决策性Diffie-Hellman问题的困难性紧密相关（命题1），因此可归约到该标准假设；方案二的安全性仅能对属于 $g$ 生成的子群的消息证明，且因 $g$ 的阶非素数而难以证明更紧的归约。两个方案的公开验证协议均为零知识，作弊成功的概率随参数（交互轮次 $K$）指数下降。

### 局限性与开放问题
方案二的安全性证明存在显著局限：当 $g$ 的阶不是素数时，无法像方案一那样归约到决策性Diffie-Hellman问题的困难性，只能对属于 $g$ 生成的子群的消息证明安全性。这意味着对于一般的消息，方案二的抗篡改能力缺乏严格证明。此外，方案基于的 $e$ 次根假设在 $n$ 的因式分解未知的情况下，虽然常见于Fiat-Shamir等签名方案，但近年来随着因式分解算法的进展需要更长的密钥。开放问题包括：能否在随机oracle模型下证明方案二的安全性？能否构造基于格上困难问题（如LWE）的PVSS方案以抵抗量子计算攻击？如何进一步降低非交互证明的通信开销？

### 强关联论文

[7] Chor等. Verifiable secret sharing and achieving simultaneity in the presence of faults. **FOCS 1985** [Google Scholar](https://scholar.google.com/scholar?q=Verifiable+secret+sharing+and+achieving+simultaneity+in+the+presence+of+faults)

[11] Feldman. A practical scheme for non-interactive verifiable secret sharing. **FOCS 1987** [Google Scholar](https://scholar.google.com/scholar?q=A+practical+scheme+for+non-interactive+verifiable+secret+sharing)

[9] ElGamal. A public key cryptosystem and a signature scheme based on discrete logarithms. **IEEE IT 1985** [Google Scholar](https://scholar.google.com/scholar?q=A+public+key+cryptosystem+and+a+signature+scheme+based+on+discrete+logarithms)

[12] Fiat and Shamir. How to prove yourself: Practical solution to identification and signature problems. **CRYPTO 1986** [Google Scholar](https://scholar.google.com/scholar?q=How+to+prove+yourself:+Practical+solution+to+identification+and+signature+problems)

[16] Micali. Fair cryptosystems. **MIT TR 1993** [Google Scholar](https://scholar.google.com/scholar?q=Fair+cryptosystems)

[21] Stadler等. Fair blind signatures. **EUROCRYPT 1995** [Google Scholar](https://scholar.google.com/scholar?q=Fair+blind+signatures)

[1] Ben-Or等. Completeness theorems for non-cryptographic fault-tolerant distributed computation. **STOC 1988** [Google Scholar](https://scholar.google.com/scholar?q=Completeness+theorems+for+non-cryptographic+fault-tolerant+distributed+computation)

[2] Blakley. Safeguarding cryptographic keys. **AFIPS 1979** [Google Scholar](https://scholar.google.com/scholar?q=Safeguarding+cryptographic+keys)

[20] Shamir. How to share a secret. **CACM 1979** [Google Scholar](https://scholar.google.com/scholar?q=How+to+share+a+secret)

[19] Schnorr. Efficient identification and signature for smart cards. **CRYPTO 1989** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+identification+and+signature+for+smart+cards)


## 关键词

+ 公开可验证秘密共享
+ ElGamal密码系统
+ 可撤销匿名性
+ 托管密码系统
+ 可验证秘密共享