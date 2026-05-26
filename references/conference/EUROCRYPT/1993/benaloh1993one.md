---
title: "One-way accumulators: A decentralized alternative to digital signatures"
标题简称: 
论文类型: conference
会议简称: EUROCRYPT
发表年份: 1993
created: 2025-05-20 03:06:15
modified: 2025-05-20 03:15:47
---

## One-way accumulators: A decentralized alternative to digital signatures

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/3-540-48285-7_24)
+ [高清pdf](https://www.microsoft.com/en-us/research/wp-content/uploads/1993/01/owa.pdf)

## 作者

+ Josh Benaloh
+ Michael De Mare

## 笔记

### 背景与动机
数字签名方案虽然能够实现身份认证和文档验证，但通常需要一个可信的中心权威来签发和验证签名。在去中心化场景中，例如时间戳服务或群组成员认证，传统方法要么依赖参与者保存大量历史数据（如“保存所有见过的签名”），要么依赖一个可能被腐败的中央机构。Haber 与 Stornetta 提出的时间戳方案 [HaSt90] 通过链式哈希实现文档排序，但需要其他参与者的主动合作，且每个文档需要重建整条链接。Benaloh 与 de Mare 之前的工作 [BeMa91] 假设广播信道并采用对数级存储，但存储量仍然与参与者数量有关。本文试图填补的空白是：能否设计一种协议，使每个参与者只需常数级存储（独立于参与者个数），同时彻底消除对任何可信中心的需求，并保证安全性基于困难问题（如大整数分解）。

### 相关工作

[HaSt90] Haber, S. and Stornetta, W. How to Time-Stamp a Digital Document. **J. Cryptology 1991** [Google Scholar](https://scholar.google.com/scholar?q=How+to+Time-Stamp+a+Digital+Document)
> 核心思路：通过哈希链将文档按时间顺序链接，文档的相对位置可通过链式验证确定。
> 局限与区别：需要其他文档持有者的主动合作来重建整个链，存储和验证开销随链增长而线性增加。本文使用累加器消除了对合作的需求。

[BeMa91] Benaloh, J. and de Mare, M. Efficient Broadcast Time-Stamping. **Clarkson University TR 1991** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+Broadcast+Time-Stamping)
> 核心思路：将时间划分为轮次，利用广播信道和共识协议实现时间戳，存储量为参与者数量的对数。
> 局限与区别：存储开销仍然与参与者数量成对数关系。本文将其降为常数，并提出了独立于广播信道的方案。

[Merk80] Merkle, R. Protocols for Public Key Cryptosystems. **IEEE S&P 1980** [Google Scholar](https://scholar.google.com/scholar?q=Protocols+for+Public+Key+Cryptosystems)
> 核心思路：使用树认证结构维护公钥目录，每个用户需保存自身密钥、哈希函数以及对数数量级的附加中间哈希。
> 局限与区别：每个用户需要保存对数个哈希值。本文的累加器方案将所需保存的数值数量降为常数。

[Sham81] Shamir, A. On the Generation of Cryptographically Strong Pseudo-Random Sequences. **ICALP 1981** [Google Scholar](https://scholar.google.com/scholar?q=On+the+Generation+of+Cryptographically+Strong+Pseudo-Random+Sequences)
> 核心思路：证明若模根提取困难，则给定一组根后仍无法计算新根，除非新根指数是已知根指数乘积的因子。
> 局限与区别：Shamir 的结果直接用于本文定理 6 的证明，论证了在模指数累加器中伪造不可行。

[RSA78] Rivest, R., Shamir, A., and Adleman, L. A Method for Obtaining Digital Signatures and Public-key Cryptosystems. **CACM 1978** [Google Scholar](https://scholar.google.com/scholar?q=A+Method+for+Obtaining+Digital+Signatures+and+Public-key+Cryptosystems)
> 核心思路：提出了 RSA 公钥密码系统，安全性基于大整数分解困难性。模幂函数 $e_n(x,y)=x^y \mod n$ 具有拟交换性。
> 局限与区别：RSA 本身是陷门单向函数，而本文利用的模幂函数作为单向累加器时，不依赖陷门，但需要特殊构造模数 $n$（刚性整数）以避免域缩小。

[NaYu89] Naor, M. and Yung, M. Universal One-Way Hash Functions and their Cryptographic Applications. **STOC 1989** [Google Scholar](https://scholar.google.com/scholar?q=Universal+One-Way+Hash+Functions+and+their+Cryptographic+Applications)
> 核心思路：定义了通用单向哈希函数族，并证明了单向函数的存在性等价于签名方案的安全性。
> 局限与区别：本文将其结果作为辅助引用，说明单向哈希函数与单向函数的关系，但本文的累加器要求更强的拟交换性，并非所有单向哈希函数都满足。

### 核心技术与方案

**1. 拟交换单向累加器的定义**

本文的核心创新是引入一类满足拟交换性的单向哈希函数，称为“单向累加器”。一个函数 $h: X \times Y \rightarrow X$ 称为拟交换的，如果对于任意 $x \in X$ 和 $y_1, y_2 \in Y$，有 $h(h(x, y_1), y_2) = h(h(x, y_2), y_1)$。这一性质保证了对一组值 $y_1, \ldots, y_m$ 进行多次哈希的结果与顺序无关。将拟交换性与单向性结合，可构造出累加器：给定初始值 $x$，计算累积哈希 $z = h(h(\ldots h(h(h(x, y_1), y_2), y_3), \ldots), y_m)$。每个参与者 $j$ 可计算部分累加值 $z_j$（排除 $y_j$ 后的累积哈希），并保留自己的 $y_j$。要证明 $y_j$ 属于原始集合，只需出示 $(y_j, z_j)$，验证 $h(z_j, y_j) = z$ 即可。这一方法将每个参与者的存储量压缩为常数（仅需保存自己的 $y_j$ 和部分累加值 $z_j$），而传统方案中每个参与者需保存整个列表或对数级附加信息。

**2. 基于模指数的具体构造**

作者指出，函数 $e_n(x, y) = x^y \mod n$ 显然是拟交换的，且当 $n$ 为 RSA 模数时，单向性基于大整数分解困难性。但存在一个关键问题：重复应用 $e_n$ 可能导致值域缩小，产生可预测的碰撞。为解决该问题，作者提出“刚性整数”（rigid integer）的概念：$n = pq$，其中 $p = 2p' + 1$，$q = 2q' + 1$，且 $p', q'$ 均为奇素数，$p$ 和 $q$ 长度相当。此时，模 $n$ 的二次剩余群的大小为 $n' = \frac{(p-1)(q-1)}{2} = 2p' q'$，且当指数 $y$ 与 $n'$ 互质时，$e_n$ 是该群上的置换。由于 $n'$ 的因子未知，随机选取的指数极大概率与 $n'$ 互质，从而多次幂运算几乎不会缩小值域，避免了碰撞风险。构造刚性整数的计算量约为 $2(\ln p')^2$ 次素性测试，对于 200 位的模数约需 20,000 次测试，仍属可行。

**3. 安全性论证：伪造不可行**

文章定理 6 给出了安全性核心：假设存在一个多项式时间算法 $A$，能够利用已知的一组根 $(y_i, r_i)$（满足 $y_i^{r_i} \equiv x \pmod{n}$）来找到一个新根 $y$（满足 $y^{r} \equiv x \pmod{n}$），那么存在另一个算法 $B$ 可以在不借助已知根的情况下直接计算 $x^{1/\rho} \mod n$，其中 $\rho = r / \gcd(r, \prod r_i)$。证明思路：$B$ 计算 $\hat{x} = x^{\prod r_i} \mod n$，调用 $A$ 得到 $\hat{y}$ 满足 $\hat{y}^r \equiv \hat{x} \pmod{n}$。由于 $\frac{r}{\gcd(r, \prod r_i)}$ 与 $\frac{\prod r_i}{\gcd(r, \prod r_i)}$ 互质，可用扩展欧几里得算法找到 $a, b$ 满足 $a \cdot (r / g) + b \cdot (\prod r_i / g) = 1$。然后 $x^{1/\rho} = x^a \hat{y}^b \mod n$。该定理表明，除非通用根提取可行，否则一个不知道 $n$ 分解的攻击者只能在新指数 $r$ 整除已知指数乘积 $\prod r_i$ 时才能计算新根。在时间戳等应用中，攻击者无法提前控制所有参与者的哈希值（即指数），且即使能控制部分指数，要使随机选取的 $r$ 成为已知指数的因子的概率可忽略（例如对于 220 位的 $n$，可安全处理约 2000 万个条目，伪造概率低于 $10^{-30}$）。

**4. 时间戳协议**

圆形步骤：所有参与者事先商定一个刚性整数 $n$ 和起始值 $x$（例如当前日期）。计算 $x_0 = x^2 \mod n$。每个参与者对要时间戳的文档应用常规单向哈希得到 $y_i < n$。设 $Y = \prod y_i$，累积时间印 $z = x_0^Y \mod n$。每个参与者 $j$ 保存其部分累加值 $z_j = x_0^{Y / y_j} \mod n$。之后，参与者只需出示 $(y_j, z_j)$，他人验证 $z_j^{y_j} \mod n = z$ 即可证明文档在对应轮次被时间戳。安全性基于定理 6：攻击者无法为未提交的文档构造有效的时间戳。

**5. 成员测试协议**

类比时间戳，一群参与者选择初始 $x$，每个成员 $j$ 选择包含其名称和特征的 $y_j$，所有成员交换 $y_j$ 并计算累积哈希 $z$。每个成员保存 $z_j$（排除自身的部分累加）。成员可向任何人证明自己是团体成员：出示 $(y_j, z_j)$，验证 $h(z_j, y_j) = z$。非成员也可持有 $z$ 来验证成员身份，但无法获取成员列表。该协议无需可信秘书，且存储量为常数。

**复杂度分析**：每个参与者的存储量为常数（自身 $y_j$ 和 $z_j$，共两个 $O(|n|)$ 的整数）。计算累积哈希需 $O(m)$ 次模幂（$m$ 为参与者数量），但每个参与者只需计算自己的部分累加，需进行一次模幂（计算 $z_j$）。验证只需一次模幂。通信方面，初始建立时需广播各自的 $y_j$，后续验证只需传输两个数值。

### 核心公式与流程

**拟交换性定义**
$$h(h(x, y_1), y_2) = h(h(x, y_2), y_1)$$
> 作用：保证哈希结果与输入顺序无关，是累加器的基础性质。

**模指数累加器构造**
$$e_n(x, y) = x^y \mod n$$
> 作用：作为具体的拟交换单向哈希函数实例。

**刚性整数定义**
$$n = pq,\quad p=2p'+1,\quad q=2q'+1,\quad p', q' \text{ 为奇素数}$$
> 作用：保证二次剩余群在指数与 $n'$ 互质时是置换，防止值域缩小。

**时间印和部分累加值计算**
$$z = x_0^{Y} \mod n,\quad Y = \prod_{i=1}^m y_i,\quad z_j = x_0^{Y/y_j} \mod n$$
> 作用：计算累积哈希和每个参与者的部分累加值，用于后续验证。

**验证方程**
$$z_j^{y_j} \equiv z \pmod{n}$$
> 作用：验证者通过一次模幂即可确认 $y_j$ 属于原始集合。

**定理 6 中的根构造**
给定 $\hat{x} = x^{\prod r_i} \mod n$，调用算法 $A$ 得到 $\hat{y}$ 满足 $\hat{y}^r \equiv \hat{x} \pmod{n}$。设 $g = \gcd(r, \prod r_i)$，存在 $a,b$ 满足 $a(r/g) + b(\prod r_i/g) = 1$，则
$$x^{1/\rho} \equiv x^{a} \hat{y}^{b} \pmod{n},\quad \rho = r/g$$
> 作用：证明若攻击者能用已知根计算新根，则可在无已知根时计算任意根，从而将伪造安全性规约到通用根提取困难性。

### 实验结果
论文没有提供实验数据或性能测试，属于理论性的密码学协议提案。作者仅给出了参数选择建议：对于约 220 位的刚性整数，可安全处理约 2000 万个条目，伪造概率低于 $10^{-30}$。刚性整数的构造需要约 $2(\ln p')^2$ 次素性测试，例如 200 位模数需约 20,000 次测试，被认为“并非不合理”。没有与任何基线系统进行性能对比。

### 局限性与开放问题
1. 是否存在不依赖陷门的单向累加器？当前的模指数构造依赖隐藏的模数分解，需要安全多方计算来生成 $n$，增加了部署复杂度。
2. 单向累加器的存在性是否等价于单向函数的存在性？目前未知任何反向蕴含关系。
3. 文中提到的 Naccache 观察的广义函数 $x^y c^{y-1} \mod n$ 和 Dixon 多项式是否具备适当的单向性质尚未确定，需要进一步分析。

### 强关联论文

[HaSt90] Haber, S. and Stornetta, W. How to Time-Stamp a Digital Document. **J. Cryptology 1991** [Google Scholar](https://scholar.google.com/scholar?q=How+to+Time-Stamp+a+Digital+Document)

[BeMa91] Benaloh, J. and de Mare, M. Efficient Broadcast Time-Stamping. **Clarkson University TR 1991** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+Broadcast+Time-Stamping)

[Merk80] Merkle, R. Protocols for Public Key Cryptosystems. **IEEE S&P 1980** [Google Scholar](https://scholar.google.com/scholar?q=Protocols+for+Public+Key+Cryptosystems)

[Sham81] Shamir, A. On the Generation of Cryptographically Strong Pseudo-Random Sequences. **ICALP 1981** [Google Scholar](https://scholar.google.com/scholar?q=On+the+Generation+of+Cryptographically+Strong+Pseudo-Random+Sequences)

[RSA78] Rivest, R., Shamir, A., and Adleman, L. A Method for Obtaining Digital Signatures and Public-key Cryptosystems. **CACM 1978** [Google Scholar](https://scholar.google.com/scholar?q=A+Method+for+Obtaining+Digital+Signatures+and+Public-key+Cryptosystems)

[NaYu89] Naor, M. and Yung, M. Universal One-Way Hash Functions and their Cryptographic Applications. **STOC 1989** [Google Scholar](https://scholar.google.com/scholar?q=Universal+One-Way+Hash+Functions+and+their+Cryptographic+Applications)

[ILL89] Impagliazzo, R., Levin, L., and Luby, M. Pseudorandom Generation from One-Way Functions. **STOC 1989** [Google Scholar](https://scholar.google.com/scholar?q=Pseudorandom+Generation+from+One-Way+Functions)

[Romp90] Rompel, J. One-Way Functions are Necessary and Sufficient for Secure Signatures. **STOC 1990** [Google Scholar](https://scholar.google.com/scholar?q=One-Way+Functions+are+Necessary+and+Sufficient+for+Secure+Signatures)


## 关键词

+ 单向累加器
+ 准交换性哈希函数
+ 文档时间戳
+ 成员测试
+ 去中心化认证