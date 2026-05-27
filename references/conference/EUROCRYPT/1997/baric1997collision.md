---
title: "Collision-free accumulators and fail-stop signature schemes without trees"
doi: 10.1007/3-540-69053-0_33
标题简称:
论文类型: conference
会议简称: EUROCRYPT
发表年份: 1997
created: 2025-04-22 09:11:17
modified: 2025-04-22 09:11:47
---
## Collision-free accumulators and fail-stop signature schemes without trees

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/3-540-69053-0_33)

## 作者

+ Niko Barić 
+ Birgit Pfitzmann  

## 笔记

### 背景与动机

数字签名方案的安全性依赖于计算假设，一旦假设被攻破，攻击者可伪造签名，而签名者无法证明自己未签署。为解决这一问题，fail-stop 签名方案被提出，允许签名者生成“伪造证明”，表明假设已被攻破。现有大多数基本构造仅能签署单条消息，多消息方案通过树认证扩展一次性 FSS 方案，导致签名长度随消息数对数增长。Benaloh 和 de Mare 提出的一次性累加器 [BeMa94] 可将大量值累加为单一值，且累加值和认证值长度可独立于输入数量，但仅具有单向性，不足以应对攻击者可能自行选择待累加值（即公钥）的场景。因此，本文定义了抗碰撞累加器，并将其纳入模块化 FSS 方案，使得公钥和签名长度真正与可签名消息数无关，填补了树认证带来的长度瓶颈。

### 相关工作

[BeMa94] Benaloh, de Mare. One-Way Accumulators: A Decentralized Alternative to Digital Signatures. **EUROCRYPT 1993** [Google Scholar](https://scholar.google.com/scholar?q=One-Way+Accumulators+Decentralized+Alternative+Digital+Signatures)
> 核心思路：提出单向累加器，基于准交换函数将多个值累加为单个值，支持后续认证。
> 局限与区别：仅具有单向性，不满足 FSS 方案所需“即使攻击者选择所有待累加值也难以伪造”的抗碰撞性；本文在此基础上定义了更强的 collision-free 性质。

[HePe93] van Heyst, Pedersen. How to Make Efficient Fail-stop Signatures. **EUROCRYPT 1992** [Google Scholar](https://scholar.google.com/scholar?q=How+to+Make+Efficient+Fail-stop+Signatures)
> 核心思路：提出了基于离散对数假设的高效一次性 FSS 方案，公钥为群中元素对。
> 局限与区别：仅适用于单条消息；本文将其作为底层组件，结合累加器构造多消息方案。

[PfWa90] Pfitzmann, Waidner. Formal Aspects of Fail-stop Signatures. **Technical Report 1990** [Google Scholar](https://scholar.google.com/scholar?q=Formal+Aspects+of+Fail-stop+Signatures)
> 核心思路：给出了 fail-stop 签名的安全定义（签名者信息论安全、接收方计算安全）。
> 局限与区别：本文采用类似的安全模型，并证明构造满足该定义。

[PePf97] Pedersen, Pfitzmann. Fail-Stop Signatures. **SIAM J. Comput. 1997** [Google Scholar](https://scholar.google.com/scholar?q=Fail-Stop+Signatures+SIAM+Journal+on+Computing)
> 核心思路：系统化 FSS 方案，包括带预密钥的一次性方案。
> 局限与区别：本文使用带预密钥的一次性 FSS 方案，并引入累加器实现多消息，无需树。

[Nybe96a] Nyberg. Commutativity in Cryptography. **First International Workshop on Functional Analysis 1996** [Google Scholar](https://scholar.google.com/scholar?q=Commutativity+in+Cryptography)
> 核心思路：提出另一种强单向累加器，基于哈希函数，无需陷门。
> 局限与区别：输出长度过长，不适合作为 FSS 公钥；本文侧重于 RSA 类构造。

[DwNa94] Dwork, Naor. An Efficient Existentially Unforgeable Signature Scheme and its Application. **CRYPTO 1994** [Google Scholar](https://scholar.google.com/scholar?q=An+Efficient+Existentially+Unforgeable+Signature+Scheme+and+its+Application)
> 核心思路：使用平坦树缩短非 fail-stop 可证明安全签名的长度。
> 局限与区别：方法不适用于 FSS 方案（因需要可证明伪造）；本文通过累加器实现类似目标但保持 fail-stop 性质。

[HePP93] van Heijst, Pedersen, Pfitzmann. New Constructions of Fail-Stop Signatures and Lower Bounds. **CRYPTO 1992** [Google Scholar](https://scholar.google.com/scholar?q=New+Constructions+of+Fail-Stop+Signatures+and+Lower+Bounds)
> 核心思路：给出了 FSS 方案的上界和下界，指出树认证导致长度随 N 对数的上界。
> 局限与区别：本文旨在突破该上界，实现与 N 无关的常数长度。

### 核心技术与方案

本文首先重新定义了一般的累加器家族，包含密钥生成、求值、认证和验证四个算法，并要求累加结果对相同输入确定。然后定义了 $N$ 次抗碰撞累加器：即使攻击者可以自由选择 $N$ 个值 $y_1,\dots,y_N$ 以及另一个值 $y'$ 和认证值 $\text{accu}'$，也难以使 $\text{authentic}_n(z, y', \text{accu}')$ 通过而 $y'$ 不在集合中。进一步，若对所有 $N$ 均满足，则称为抗碰撞累加器。

随后给出两种具体构造。第一种 RSA 累加器（无随机预言机）基于函数 $h_{(n,x)}(x, y)=x^y \bmod n$，但限制输入 $y$ 为素数，且利用强 RSA 假设（给定 $n,x$，求 $(y,e)$ 使得 $y^e\equiv x \pmod n$ 且 $e$ 为素数困难）证明抗碰撞性。第二种 RSA 累加器（带随机预言机）使用函数 $h_{(n,\Omega,l,x)}(x,(y,dist)) = x^{2^l\Omega(y)+dist}\bmod n$，其中 $\Omega$ 为随机预言机，通过附加 $l$ 位使指数为素数，安全性归约到普通 RSA 假设。

为实现模块化，定义了转换算法 $\Lambda$，用于将底层一次性 FSS 的公钥转换为适合累加器输入的形式（如素数）。转换要求存在逆映射且可高效计算。作为示例，$\Lambda_{prim}$ 通过在数字后附加 $l$ 位搜索素数实现。

最终构造的累加器 FSS 方案流程如下：

- 密钥生成：中心生成预密钥、累加器密钥 $n$、转换参数 $par$；签名者验证预密钥，生成 $N$ 个一次性密钥对 $(sk_i,pk_i)$，用 $\Lambda_{par}$ 转换为 $\widehat{pk}_i$，若不适配则重新生成；然后计算 $pk = a_n(\widehat{pk}_1,\dots,\widehat{pk}_N)$ 并发布。签名者保存辅助信息 $aux$ 和 $\widehat{pk}_i$。
- 签名：对第 $i$ 条消息 $m_i$，签名 $s = (s_i, \widehat{pk}_i, accu_i)$，其中 $s_i$ 为一次性签名，$accu_i = auth_n(\widehat{pk}_i, aux)$ 可离线预计算。
- 验证：检查 $s_i$ 对 $m_i$ 有效（通过逆转换恢复 $pk_i$），$\widehat{pk}_i\in Y_n$，$accu_i\in Accu_n$，且 $authentic_n(pk, \widehat{pk}_i, accu_i)=ok$。
- 证明伪造：若伪造签名使用了已存在的 $pk_i$，则利用底层 FSS 的证明能力；否则展示 $\widehat{pk}_1,\dots,\widehat{pk}_N$ 和 $(\widehat{pk}', accu')$ 作为累加器碰撞。该证明显示累加器假设被攻破。

安全性：签名者的信息论安全来自：任何未使用已有 $pk_i$ 的伪造必然导致累加器碰撞（可证明），而使用已有 $pk_i$ 时底层 FSS 的证明错误概率低于 $2^{-\sigma^*}$。接收方的计算安全基于：若累加器抗碰撞且底层 FSS 安全（安全参数≥$k$），则攻击者无法产生可证明的伪造。

### 核心公式与流程

**累加器基本定义**
$$
\text{authentic}_n(z, y_i, \text{auth}_n(y_i, \text{aux})) = ok \quad \text{对于所有 } i.
$$
> 作用：保证每个输入 $y_i$ 都能通过相应认证值被累加结果 $z$ 认证。

**RSA 累加器（无随机预言机）**
$$
h_{(n,x)}(x,y) = x^y \bmod n, \quad \text{要求 } y \text{ 为素数}.
$$
$$
a_{(n,x)}^{\mathrm{RSA}}(y_1,\dots,y_N) = x^{\prod_{i=1}^N y_i} \bmod n.
$$
$$
\widehat{pk}_i = \text{auth}_{(n,x)}^{\mathrm{RSA}}(y_i, \text{aux}) = x^{\prod_{j\neq i} y_j} \bmod n.
$$
验证条件： $accu^{y} \equiv z \pmod n$。
> 作用：基于强 RSA 假设实现抗碰撞累加，要求输入为素数。

**RSA 累加器（带随机预言机）**
$$
h_{(n,\Omega,l,x)}(x,(y,dist)) = x^{2^l\Omega(y)+dist} \bmod n, \quad 2^l\Omega(y)+dist \text{ 为素数}.
$$
$$
a_{(n,\Omega,l,x)}^{\mathrm{RSA}\Omega}\big((y_1,dist_1),\dots,(y_N,dist_N)\big) = x^{\prod_{i=1}^N (2^l\Omega(y_i)+dist_i)} \bmod n.
$$
验证条件： $accu^{2^l\Omega(y)+dist} \equiv z \pmod n$。
> 作用：通过随机预言机将任意 $y$ 映射为带有附加位的素数，安全性归约到普通 RSA 假设。

**抗碰撞性定义（$N$次）**
$$
\mathrm{P}\Big(\text{authentic}_n(z, y', accu')=ok \wedge y'\notin\{y_1,\dots,y_N\} \wedge \cdots\Big) \leq \frac{1}{k^c}.
$$
> 作用：形式化攻击者可以任意选择待累加值的情形。

**累加器 FSS 方案签名生成**
$$
s = \big(s_i, \widehat{pk_i}, accu_i\big), \quad accu_i = auth_n(\widehat{pk_i}, aux).
$$
> 作用：签名由一次性签名、转换后的公钥和累加器认证值组成。

### 实验结果

本文为理论工作，无实验评估。分析指出：累加器 FSS 方案中，公钥和签名长度与 $N$ 无关（例如，RSA 累加器输出一个模数大小的值），而密钥生成时间复杂度为 $O(N \cdot T_{\text{prime}})$（其中 $T_{\text{prime}}$ 为素性测试时间），相比树认证方案有更高的预计算成本。签名和验证代价与一次性 FSS 方案相同，仅增加少量模幂运算。作者建议实际中可结合树结构实现平坦树，在牺牲部分常数因子下降低密钥生成开销。

### 局限性与开放问题

1. 第一种 RSA 累加器依赖强 RSA 假设，该假设尚未被充分研究，实际部署需谨慎。
2. 密钥生成阶段需大量素性测试，当 $N$ 较大时可能效率低；平坦树组合可缓解但增加签名长度常数因子。
3. 转换算法 $\Lambda_{prim}$ 可能因找不到素数而需多次重新生成密钥对，最坏情况下概率不可忽略，但本文参数下期望成功概率为常数。
4. 强 RSA 假设的困难性是否有新的攻击进展？随机预言机实例化后安全性如何？均需进一步分析。

### 强关联论文

[BeMa94] Benaloh, de Mare. One-Way Accumulators: A Decentralized Alternative to Digital Signatures. **EUROCRYPT 1993** [Google Scholar](https://scholar.google.com/scholar?q=One-Way+Accumulators+Decentralized+Alternative+Digital+Signatures)

[HePe93] van Heyst, Pedersen. How to Make Efficient Fail-stop Signatures. **EUROCRYPT 1992** [Google Scholar](https://scholar.google.com/scholar?q=How+to+Make+Efficient+Fail-stop+Signatures)

[PfWa90] Pfitzmann, Waidner. Formal Aspects of Fail-stop Signatures. **Technical Report 1990** [Google Scholar](https://scholar.google.com/scholar?q=Formal+Aspects+of+Fail-stop+Signatures)

[PePf97] Pedersen, Pfitzmann. Fail-Stop Signatures. **SIAM J. Comput. 1997** [Google Scholar](https://scholar.google.com/scholar?q=Fail-Stop+Signatures+SIAM+Journal+on+Computing)

[Nybe96a] Nyberg. Commutativity in Cryptography. **First International Workshop on Functional Analysis 1996** [Google Scholar](https://scholar.google.com/scholar?q=Commutativity+in+Cryptography)

[DwNa94] Dwork, Naor. An Efficient Existentially Unforgeable Signature Scheme and its Application. **CRYPTO 1994** [Google Scholar](https://scholar.google.com/scholar?q=An+Efficient+Existentially+Unforgeable+Signature+Scheme+and+its+Application)

[HePP93] van Heijst, Pedersen, Pfitzmann. New Constructions of Fail-Stop Signatures and Lower Bounds. **CRYPTO 1992** [Google Scholar](https://scholar.google.com/scholar?q=New+Constructions+of+Fail-Stop+Signatures+and+Lower+Bounds)


## 关键词

+ 无碰撞累加器
+ RSA累加器
+ 防失败签名
+ 单向累加器
+ 公钥认证