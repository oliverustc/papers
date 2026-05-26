---
title: "Group signatures"
标题简称:
论文类型: conference
会议简称: EUROCRYPT
发表年份: 1991
created: 2025-05-26 03:43:20
modified: 2025-05-26 04:36:56
---

## Group signatures

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.5555/1754868.1754897)

## 作者

+ David Chaum
+ Eugène Van Heyst

## 笔记

### 背景与动机
数字世界中，群体需要在不暴露个体身份的前提下证明成员资格，同时允许在争议时揭露签名者身份。传统的数字签名方案无法同时满足匿名性、可验证性和可追责性。例如，公司内部打印权限需验证部门成员身份，但又不希望泄露用户名；若打印机被滥用，管理者需能识别责任人。现有凭证机制和成员认证方案（如 [OOK90, SKI90]）允许成员向验证者证明其属于某个群体而不泄露身份，但这些方案通常依赖于所有成员共享同一密钥，缺乏针对每个签名独立撤销匿名性的能力。Chaum 与 van Heyst 提出群签名（group signature）概念，要求只有群成员能签名、接收者可验证签名来自该群但无法识别具体成员、且在需要时可由指定方（或群成员协助）打开签名揭示签名者身份。该工作填补了从成员认证到可追责匿名的签名原语的空白，并给出了四种具体构造，分别基于不同密码学假设和信任模型。

### 相关工作

[Ch85] Chaum. Showing credentials without identification. **EUROCRYPT 1985** [Google Scholar](https://scholar.google.com/scholar?q=Showing+credentials+without+identification)
> 核心思路：允许用户在不泄露身份的情况下证明持有某些凭证。
> 局限与区别：该方案仅提供单向认证，缺乏可追责的签名机制；群签名在此基础上增加了消息签名和争议时打开签名的能力。

[OOK90] Ohta, Okamoto, Koyama. Membership authentication for hierarchical multigroup using the extended Fiat‑Shamir scheme. **EUROCRYPT 1990** [Google Scholar](https://scholar.google.com/scholar?q=Membership+authentication+for+hierarchical+multigroup+using+the+extended+Fiat%E2%80%91Shamir+scheme)
> 核心思路：扩展 Fiat‑Shamir 方案实现分层多群组中成员身份认证。
> 局限与区别：只解决认证而非签名，且无法打开签名揭示具体成员。

[SKI90] Shizuya, Koyama, Itoh. Demonstrating possession without revealing factors and its applications. **AUSCRYPT 1990** [Google Scholar](https://scholar.google.com/scholar?q=Demonstrating+possession+without+revealing+factors+and+its+applications)
> 核心思路：展示如何在不泄露因子分解的情况下证明知识，用于成员认证。
> 局限与区别：同样不具备签名功能和可追溯性。

[BCDvdG87] Brickell, Chaum, Damgård, van de Graaf. Gradual and verifiable release of a secret. **CRYPTO 1987** [Google Scholar](https://scholar.google.com/scholar?q=Gradual+and+verifiable+release+of+a+secret)
> 核心思路：提出可验证秘密渐近释放的协议，用于证明秘密在指定区间内。
> 关联：本文方案二直接调用该协议（Protocol 1）来证明指数属于特定区间。

[ElG85] ElGamal. A public key cryptosystem and a signature scheme based on discrete logarithm. **IEEE IT 1985** [Google Scholar](https://scholar.google.com/scholar?q=A+public+key+cryptosystem+and+a+signature+scheme+based+on+discrete+logarithm)
> 核心思路：基于离散对数困难问题的公钥加密与签名方案。
> 关联：本文方案一修改版和方案四使用离散对数设置。

[CvA89] Chaum, van Antwerpen. Undeniable signatures. **CRYPTO 1989** [Google Scholar](https://scholar.google.com/scholar?q=Undeniable+signatures)
> 核心思路：引入不可否认签名概念，需要签名者参与验证。
> 关联：本文后三个方案基于不可否认签名，并通过 Fiat‑Shamir 变换获得数字签名。

[Ch90] Chaum. Zero‑knowledge undeniable signatures. **EUROCRYPT 1990** [Google Scholar](https://scholar.google.com/scholar?q=Zero%E2%80%91knowledge+undeniable+signatures)
> 核心思路：为零知识不可否认签名提供否认协议。
> 关联：本文方案二、三、四的否认协议直接使用或借鉴该工作。

[FS86] Fiat, Shamir. How to prove yourself: practical solution to identification and signature problems. **CRYPTO 1986** [Google Scholar](https://scholar.google.com/scholar?q=How+to+prove+yourself%3A+practical+solution+to+identification+and+signature+problems)
> 核心思路：将交互式零知识证明转化为非交互式数字签名。
> 关联：本文提及可用该方法将不可否认群签名转换为数字群签名。

### 核心技术与方案
论文共提出四种群签名方案，按密码学假设、是否需要可信中心参与打开签名、以及群是否预定义等维度对比。

**方案一（基于任意公钥系统）**  
可信中心 Z 为每个成员分配一组互不相交的私钥，并将对应公钥乱序公布。成员使用自己的一个私钥签名，接收者用对应公钥验证。Z 知道所有私钥分配，故能打开签名。优点是兼容任何公钥系统；缺点是 Z 可伪造签名，且每个成员能签的消息数量固定（私钥用完即止）。改进版使用 ElGamal 体制，成员自行生成私钥 $s_i$ 并上交 $g^{s_i}$，Z 每周随机选择 $r_i$ 发布盲化公钥 $(g^{s_i})^{r_i}$，成员用 $s_i r_i \bmod (p-1)$ 签名。这样 Z 无法伪造，且每周签名可区分，仅当 $r_i$ 泄露时才暴露当周链接性。

**方案二（基于假设1：RSA求根困难）**  
Z 选择 $N=pq$ 和单向函数 $f$，为每个成员 $i$ 分配大素数 $s_i \in \Phi = \{\lceil\sqrt{N}\rceil,\dots,\lfloor2\sqrt{N}\rfloor-1\}$，计算 $v = \prod s_i$，公开 $N, v, f$。成员 $i$ 对消息 $n$ 的签名为 $S = (f(n))^{s_i} \bmod N$。接收者需通过两阶段协议验证：  
1. 用 Protocol 1（源自 [BCDvdG87]）零知识证明 $\exists s$ 满足 $S \equiv m^s \pmod N$ 且 $s \in \Phi$，迭代 $k$ 次达到错误概率 $2^{-k}$；  
2. 证明 $s \mid v$（成员计算 $b \equiv a^{v/s} \bmod N$，验证者检查 $b \equiv m^{v r}$，其中 $a \equiv S^r$）。  

**否认协议（方案二）**：利用 Z 公开的生成元 $\tilde{g},\tilde{h}$ 和每个成员的 $\tilde{g}^s, \tilde{h}^s$。验证者发送 $m^a \tilde{g}^{r_1} \tilde{h}^{r_2}$ 和 $S^a (\tilde{g}^s)^{r_1} (\tilde{h}^s)^{r_2}$，成员计算 $(m^s/S)^a$ 并通过穷举 $a \in [0,l]$ 确认签名不是自己的。若 $S \neq m^s$，则成员可正确响应；否则无法计算 $a$ 需猜测，失败概率高。

**方案三（基于假设1，无预定义群）**  
每个成员 $i$ 拥有自己的 RSA 模 $N_i = p_i q_i$（$p_i$ 为签名指数，$q_i > 4\sqrt{M}$）。Z 选取独立模 $N$，公开 $M$。签名者随机选择成员集合 $\Gamma$（含自己），输出 $\Gamma$ 和 $S = (f(n))^{p_i} \bmod N$，并用 Protocol 2 零知识证明 $p_i \in \Phi$ 且 $p_i$ 整除 $\prod_{j\in\Gamma} N_j$。由于 $N_i, q_i, p_i p_j$ 均不在扩充区间 $\tilde\Phi$ 内，防止了合谋伪造。否认协议同方案二。

**方案四（基于假设2：离散对数困难）**  
设 $p$ 为大素数，$g,h$ 为 $\mathbb{Z}_p^*$ 生成元。成员 $i$ 私钥 $s_i$，公钥 $k_i = g^{s_i} \bmod p$。签名者选择集合 $\Gamma$，输出 $\Gamma$ 和 $S = m^{s_i} \bmod p$，并通过 Protocol 4 零知识证明：$S \equiv m^{s_i}$ 且 $g^{s_i} \in \{k_j \mid j \in \Gamma\}$。该协议将三个断言（签名格式正确、指数与某公钥指数相同、该公钥属于 $\Gamma$）压缩为单个交互协议，迭代 $k$ 次达到信度 $1-2^{-k}$。否认协议使用 [Ch90] 的方法。

**安全性假设与复杂度**：方案二、三依赖 RSA 求根困难（假设1），方案四依赖离散对数困难（假设2）。所有方案的群公钥长度与成员数成线性关系；确认/否认协议的通信和计算量在方案二、三中与群规模线性相关（通信量独立），方案四中通信量亦线性。

### 核心公式与流程

**[方案二签名验证：Protocol 1（区间证明）]**
$$ \begin{aligned}
&\mathcal{P}\text{ 的秘密: } s. \quad \text{公开: } N, x=m, y=S, \Omega=\Phi. \\
&\text{证明: } x^s \equiv y \pmod N \land s \in \Omega. \\
&\text{步骤: } \mathcal{P}\text{ 选 } r\in\{0,\dots,\beta\},\text{ 计算 } z_1=x^r,\; z_2=x^{r-\beta}\bmod N,\\
&\quad\text{发送无序对 } \{\mathcal{B}(z_1),\mathcal{B}(z_2)\}\text{ 给 }\mathcal{V}.\\
&\mathcal{V}\text{ 选 } b\in\{0,1\}.\\
&\text{若 }b=0:\mathcal{P}\text{ 发送 }r\text{ 并打开两个 blob};\\ 
&\quad\mathcal{V}\text{ 检查 } r\in[0,\beta]\text{ 且 blob 内容为 }x^r,x^{r-\beta}.\\
&\text{若 }b=1:\mathcal{P}\text{ 发送 } \tilde{r}=s+r\text{ 或 }s+r-\beta\text{（落在 }\Omega\text{ 内）},\\
&\quad\text{打开对应 blob }\tilde{z};\; \mathcal{V}\text{ 检查 } \tilde{r}\in\Omega,\; x^{\tilde{r}}\equiv \tilde{z}\,y.
\end{aligned} $$

> 作用：零知识证明指数 $s$ 属于区间 $\Omega$，迭代 $k$ 次后验证者确信 $s\in\widetilde\Omega$（稍宽区间），但不会泄露 $s$ 的具体值。

**[方案二签名验证：Protocol 2（完整验证）]**
$$
\begin{aligned}
&\text{Step 1: 用 Protocol 1 迭代 }k\text{ 次证明 } S\equiv m^s \pmod N \land s\in\Phi.\\
&\text{Step 2: 证明 } s\mid v.\\
&\quad\mathcal{V}\text{ 选 } r\in\{1,\dots,N\},\text{ 计算 } a\equiv S^r \pmod N\text{ 发送给 }\mathcal{P}.\\
&\quad\mathcal{P}\text{ 计算 } b\equiv a^{v/s}\pmod N,\text{ 发送 }\mathcal{B}(b)\text{ 给 }\mathcal{V}.\\
&\quad\mathcal{V}\text{ 揭晓 } r,\;\mathcal{P}\text{ 打开 blob};\; \mathcal{V}\text{ 检查 } b\equiv m^{vr}.
\end{aligned}
$$

> 作用：在 Step1 已知 $S=m^s$ 的基础上，验证者可通过比较 $b$ 和 $m^{vr}$ 确认 $s$ 整除 $v$。安全性依赖于 RSA 求根困难性。

**[方案四核心协议：Protocol 4]**
$$
\begin{aligned}
&\mathcal{P}\text{ 秘密: } s_i. \quad \text{公开: } p,g,h,m,S,\Gamma.\\
&\text{证明: } S\equiv m^{s_i} \land g^{s_i}\in\{k_j|j\in\Gamma\}.\\
&\text{步骤:}\\
&(1)\;\mathcal{P}\text{ 选 } r_1,\dots,r_{|\Gamma|}, t_1,t_2,t_3,\text{ 及置换 }\tau.\\
&\quad\text{计算 } x\equiv (g/m)^{t_1}h^{t_2},\; y\equiv m^{t_3},\; z_{\tau(j)}\equiv k_j h^{r_j} \pmod p.\\
&(2)\;\mathcal{V}\text{ 选 } b\in\{0,1\}.\\
&(3)\;\text{若 }b=0:\mathcal{P}\text{ 发送 } r_1,\dots,r_{|\Gamma|},t_1,t_2,t_3,\tau.\\
&\quad\text{若 }b=1:\mathcal{P}\text{ 发送 } t_1+s_i,\; t_2+r_i,\; t_3+s_i,\; \tau(i).\\
&(4)\;\text{若 }b=0,\;\mathcal{V}\text{ 检查 } x,y,z_j\text{ 是否正确};\\
&\quad\text{若 }b=1,\;\mathcal{V}\text{ 检查 } yS\equiv m^{t_3+s_i},\; x z_{\tau(i)}\equiv S\,h^{t_2+r_i}(g/m)^{t_1+s_i}.
\end{aligned}
$$

> 作用：将三个断言压缩为一个交互协议，迭代 $k$ 次后验证者确信签名者确实使用了 $\Gamma$ 中某成员的公钥对应私钥。

### 实验结果
论文未提供传统意义上的软件实现实验，但给出四种方案的定性比较表（图1）。下表总结了关键性能参数：

- **方案一**（任意公钥系统）：群公钥长度与成员数成线性关系；确认协议计算量和通信量均与群大小无关（仅一次签名/验证）；打开签名必须可信中心 Z 参与；群预定义；支持任何签名类型。
- **方案二**（基于假设1）：群公钥长度线性；确认协议计算量线性于成员数（因 Step2 需计算 $a^{v/s}$，指数 $v$ 为乘积），通信量独立；打开签名不需要 Z；群预定义；签名为不可否认签名。
- **方案三**（基于假设1）：与方案二类似，但群不预定义（签名者临时选取集合 $\Gamma$）；确认协议计算量线性于 $|\Gamma|$，通信量独立；无需 Z 参与。
- **方案四**（基于假设2）：群公钥长度线性；确认协议计算量和通信量均线性于 $|\Gamma|$（因 Protocol 4 中发送 $|\Gamma|$ 个 $z_j$）；无需 Z 参与；群不预定义。

所有方案的否认协议（方案二/三/四）的计算和通信量均与群大小无关，因为仅涉及签名者与验证者之间的两方交互。方案一中的密钥长度与成员数线性关系限制了大规模群体的实用性，但改版通过盲化减少了每成员所需私钥数量。

### 局限性与开放问题
论文指出若干未解决的问题：能否设计出由多数群成员共同决定打开签名的方案（而非仅依赖单一可信中心或逐个成员否认协议）？能否构造非基于不可否认签名的数字群签名（除使用 Fiat‑Shamir 变换外）？在方案二‑四中，指数具体选择如何影响匿名性保护强度，是否可通过已知计算问题（如 [SS90]、[Per85]）严格证明？方案四的确认协议通信量能否降低到与群大小无关？此外，所有方案的群公钥长度均为线性，潜在瓶颈在于大规模部署。

### 强关联论文

[BCDvdG87] Brickell, Chaum, Damgård, van de Graaf. Gradual and verifiable release of a secret. **CRYPTO 1987** [Google Scholar](https://scholar.google.com/scholar?q=Gradual+and+verifiable+release+of+a+secret)

[Ch85] Chaum. Showing credentials without identification. **EUROCRYPT 1985** [Google Scholar](https://scholar.google.com/scholar?q=Showing+credentials+without+identification)

[Ch90] Chaum. Zero‑knowledge undeniable signatures. **EUROCRYPT 1990** [Google Scholar](https://scholar.google.com/scholar?q=Zero%E2%80%90knowledge+undeniable+signatures)

[CvA89] Chaum, van Antwerpen. Undeniable signatures. **CRYPTO 1989** [Google Scholar](https://scholar.google.com/scholar?q=Undeniable+signatures)

[ElG85] ElGamal. A public key cryptosystem and a signature scheme based on discrete logarithm. **IEEE IT 1985** [Google Scholar](https://scholar.google.com/scholar?q=A+public+key+cryptosystem+and+a+signature+scheme+based+on+discrete+logarithm)

[FS86] Fiat, Shamir. How to prove yourself: practical solution to identification and signature problems. **CRYPTO 1986** [Google Scholar](https://scholar.google.com/scholar?q=How+to+prove+yourself%3A+practical+solution+to+identification+and+signature+problems)

[OOK90] Ohta, Okamoto, Koyama. Membership authentication for hierarchical multigroup using the extended Fiat‑Shamir scheme. **EUROCRYPT 1990** [Google Scholar](https://scholar.google.com/scholar?q=Membership+authentication+for+hierarchical+multigroup+using+the+extended+Fiat%E2%80%91Shamir+scheme)

[SKI90] Shizuya, Koyama, Itoh. Demonstrating possession without revealing factors and its applications. **AUSCRYPT 1990** [Google Scholar](https://scholar.google.com/scholar?q=Demonstrating+possession+without+revealing+factors+and+its+applications)


## 关键词

+ 群签名
+ 匿名性
+ 可追踪性
+ 可信中心
+ 密码学原语