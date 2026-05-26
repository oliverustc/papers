---
title: "How to leak a secret"
标题简称:
论文类型: conference
会议简称: ASIACRYPT
发表年份: 2001
created: 2025-05-12 08:44:54
modified: 2025-05-12 08:45:46
---

## How to leak a secret

## 发表信息

+ [原文链接]()

## 作者

+ Ronald L Rivest
+ Adi Shamir
+ Yael Tauman

## 笔记

### 背景与动机

匿名数字签名是密码学中一个基础且重要的研究方向，其目标是让签名者在不暴露自身身份的前提下，向验证者证明其拥有某种群体成员身份或属性。Chaum 和 van Heyst 于 1991 年提出的群签名方案 [2] 是这一方向的里程碑，它允许一个预定义群体中的成员代表该群体匿名签名，但依赖一个可信的群管理员来设置、分发密钥，并在必要时撤销匿名性。然而，这种中心化的管理方式在应用场景中构成了严重瓶颈：对于“吹哨人”泄露秘密的场景，例如一个内阁成员希望向记者匿名证实一则消息源自内阁内部，群签名方案无法适用，因为设立群组需要所有成员的事先合作，而群管理员可能在政府压力下暴露签名者身份。此外，现有方案如 Camenisch [1] 的群签名虽然效率有提升，但要求所有成员使用同一个大素数参数，这在现实中要求不同用户使用协调一致的密钥，缺乏灵活性。更早期的松散相关方案依赖于零知识证明或多方计算协议，效率极低，例如每增加一个群成员，签名和验证的计算开销就增加一次完整的模幂运算。因此，亟需一种去中心化、不依赖任何管理员、设置过程为零、且允许任意用户集合（包括非自愿用户）的匿名签名方案。

### 相关工作

[1] Jan Camenisch. Efficient and generalized group signatures. **Eurocrypt 1997** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+and+generalized+group+signatures)
> 核心思路：提出了一个高效的群签名方案，其效率比之前的方案快约 4 倍，支持成员增删。
> 局限与区别：方案要求所有成员使用相同的素数模数，无法在不协调的情况下组合不同用户的不同公钥（如 RSA 密钥）；此外，方案仍依赖群管理员，不适用于去中心化的泄露场景。

[2] David Chaum and Eugène Van Heyst. Group signatures. **Eurocrypt 1991** [Google Scholar](https://scholar.google.com/scholar?q=Group+signatures)
> 核心思路：首次形式化定义了群签名概念，由一个可信群管理员设定群组、分发秘钥，成员可匿名签名，管理员可撤销匿名性。
> 局限与区别：方案需预先建立群组并分发专用密钥，无法利用用户现有的公钥（如 PKI 中的 RSA 证书），且中心化管理员是安全瓶颈。

[6] M. Jakobsson, K. Sako, and R. Impagliazzo. Designated verifier proofs and their applications. **Eurocrypt 1996** [Google Scholar](https://scholar.google.com/scholar?q=Designated+verifier+proofs+and+their+applications)
> 核心思路：提出了指定验证者签名概念，使得只有特定的验证者能够被说服签名有效，但无法将证明出示给第三方。
> 局限与区别：基于零知识证明需要交互，或非交互零知识证明本质上是常规签名而失去“不可转移”性；本文指出可以用 2-用户环签名作为替代方案，无需交互和预先共享密钥。

[3] Ronald Cramer, Ivan Damgård, and Berry Schoenmakers. Proofs of partial knowledge and simplified design of witness hiding protocols. **CRYPTO 1994** [Google Scholar](https://scholar.google.com/scholar?q=Proofs+of+partial+knowledge+and+simplified+design+of+witness+hiding+protocols)
> 核心思路：展示了如何构造见证不可区分交互证明。
> 局限与区别：该方案可结合 Fiat-Shamir 技术转化为环签名，但本质上仍基于交互式证明的转换，效率不如本文的直接构造。

[10] Alfredo De Santis et al. On monotone formula closure of SZK. **FOCS 1994** [Google Scholar](https://scholar.google.com/scholar?q=On+monotone+formula+closure+of+SZK)
> 核心思路：证明统计零知识语言在单调布尔操作下封闭，并展示该结果可用于构造环签名。
> 局限与区别：并未明确定义环签名概念，且构造效率不高。

### 核心技术与方案

本文形式化定义了环签名（ring signature），其核心创新在于一种完全去中心化、设置自由的构造。环签名允许用户（称为签名者）任意指定一个包含自身的公钥集合（称为环），无需其他成员的知识或同意，仅使用自己的私钥和环中其他成员的公开密钥即可生成签名。验证者只能确信签名来自环中某个成员，但无法确定具体是谁。这种无条件签名者匿名性源于方案的设计：对于任何给定的环和消息，可能的签名数量巨大且分布完全均匀，与签名者的身份无关。

本文的构造基于一个核心思想：将签名问题转化为在一个环状结构中寻找数值“插值”的问题。具体来说，方案使用一个称为“组合函数”的加密原语。该函数使用对称加密 $E_k$ 将一系列输入 $y_1, y_2, \dots, y_r$ 链接起来。其定义如下：
$$C_{k,v}(y_1, y_2, \dots, y_r) = E_k(y_r \oplus E_k(y_{r-1} \oplus E_k( \dots \oplus E_k(y_1 \oplus v) \dots)))$$
这个函数具有两个关键性质：第一，对于任何固定的 $k, v$ 和其他所有输入，该函数是单个输入的置换；第二，给定等于输出 $z$ 的 $v$（即 $C_{k,v}(y_1, ..., y_r) = v$），若知道 $k$，便可以快速求解出任何一个缺失的 $y_i$。

签名生成过程如下：对于待签消息 $m$，签名者首先计算对称密钥 $k = h(m)$。接着，他随机选择一个“粘合”值 $v$。对于环中除自己外的所有其他成员 $i \ne s$，他随机选择 $x_i$，并通过其公钥对应的扩展陷门置换 $g_i$ 计算 $y_i = g_i(x_i)$。然后，他利用组合函数的“高效可解”性质，求解出使得方程 $C_{k,v}(y_1, ..., y_r) = v$ 成立的 $y_s$。最后，签名者使用自己的私钥反转自己的陷门置换，得到 $x_s = g_s^{-1}(y_s)$。最终的签名是一个元组 $(P_1, ..., P_r; v; x_1, ..., x_r)$。

验证过程则直接计算所有 $y_i = g_i(x_i)$，计算 $k = h(m)$，然后检查等式 $C_{k,v}(y_1, ..., y_r) = v$ 是否成立。计算复杂度与常规签名相比，每个环成员只增加了一次模乘法和一次对称加密运算。安全性方面，无条件匿名性由组合函数和随机选择的均匀性保证。安全性证明在随机谕言机模型下，将破解环签名的攻击者规约为能破解环中任意一个陷门置换的算法。

### 核心公式与流程

**[组合函数定义]**
$$C_{k,v}(y_1, y_2, \dots, y_r) = E_k(y_r \oplus E_k(y_{r-1} \oplus E_k(\dots \oplus E_k(y_1 \oplus v) \dots)))$$
> 作用：将 $r$ 个输入链接成一个环状结构，形成一个对每个单独输入的置换，并可在知道密钥时高效求解任意一个输入。验证时要求其输出等于输入 $v$，形成闭环。

**[扩展陷门置换]**
$$g_i(m) = \begin{cases} q_i n_i + f_i(r_i) & \text{if } (q_i + 1)n_i \le 2^b \\ m & \text{else} \end{cases}$$
> 作用：将定义在不同模数 $n_i$ 上的陷门置换 $f_i$（如 RSA 函数）统一扩展到共同的域 $\{0,1\}^b$，使得组合不同公钥成为可能。

**[签名生成算法]**

1. 计算对称密钥 $k = h(m)$。
2. 随机选择“粘合”值 $v \in_R \{0,1\}^b$。
3. 对于所有非签名者 $i \neq s$，随机选择 $x_i \in_R \{0,1\}^b$，计算 $y_i = g_i(x_i)$。
4. 求解环方程 $C_{k,v}(y_1, y_2, \dots, y_r) = v$，得到 $y_s$。
5. 计算 $x_s = g_s^{-1}(y_s)$。
6. 输出签名 $\sigma = (P_1, P_2, \dots, P_r; v; x_1, x_2, \dots, x_r)$。

### 实验结果

本论文为理论性工作，未提供实验数据。然而，它给出了详细的复杂度分析。基于 RSA 的环签名方案中，签名操作主要成本是：一次模幂运算（用于计算 $x_s$），以及为每个非签名者成员（共 $r-1$ 个）执行一次模乘法和一次对称加密。验证操作则需要对每个环成员（共 $r$ 个）执行一次模乘法和一次对称加密。因此，生成或验证一个包含 $r$ 个成员的环签名的总计算开销大致与生成或验证一个常规 RSA 签名相当，再为每个额外成员增加一个模乘法和对称加密。这使得方案对于包含数百名成员的环来说也是实际可行的。相比于 Camenisch [1] 的方案，本文方案快两到三个数量级，且不要求所有成员使用相同的素数模数。

### 局限性与开放问题

本文提出的环签名方案的一个固有局限性是签名大小必须与环成员数量 $r$ 线性增长，因为它需要列出所有环成员的公钥。虽然论文提到通过移除“粘合”值 $v$ 并固定其为 0 来得到更紧凑的变体，但这并未改变线性增长的依赖。此外，方案的安全性证明依赖随机谕言机模型，这在实际应用中可能不够理想。开放问题包括如何在标准模型下构造同样高效的环签名方案，以及如何在不显著增加签名大小的前提下实现签名者身份的撤销功能。

### 强关联论文

[2] David Chaum and Eugène Van Heyst. Group signatures. **Eurocrypt 1991** [Google Scholar](https://scholar.google.com/scholar?q=Group+signatures)

[1] Jan Camenisch. Efficient and generalized group signatures. **Eurocrypt 1997** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+and+generalized+group+signatures)

[3] Ronald Cramer, Ivan Damgård, and Berry Schoenmakers. Proofs of partial knowledge and simplified design of witness hiding protocols. **CRYPTO 1994** [Google Scholar](https://scholar.google.com/scholar?q=Proofs+of+partial+knowledge+and+simplified+design+of+witness+hiding+protocols)

[6] M. Jakobsson, K. Sako, and R. Impagliazzo. Designated verifier proofs and their applications. **Eurocrypt 1996** [Google Scholar](https://scholar.google.com/scholar?q=Designated+verifier+proofs+and+their+applications)

[10] Alfredo De Santis et al. On monotone formula closure of SZK. **FOCS 1994** [Google Scholar](https://scholar.google.com/scholar?q=On+monotone+formula+closure+of+SZK)

[9] Ronald L. Rivest, Adi Shamir, and Leonard M. Adleman. A method for obtaining digital signatures and public-key cryptosystems. **Communications of the ACM 1978** [Google Scholar](https://scholar.google.com/scholar?q=A+method+for+obtaining+digital+signatures+and+public-key+cryptosystems)

[8] M. Rabin. Digitalized signatures as intractable as factorization. **MIT/LCS/TR-212 1979** [Google Scholar](https://scholar.google.com/scholar?q=Digitalized+signatures+as+intractable+as+factorization)


## 关键词

+ 环签名
+ 签名者匿名性
+ 随机预言机模型
+ 秘密泄露
+ 无需协调签名