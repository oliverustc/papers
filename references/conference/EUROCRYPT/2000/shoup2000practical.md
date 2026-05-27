---
title: "Practical threshold signatures"
doi: 10.1007/3-540-45539-6_15
标题简称:
论文类型: conference
会议简称: EUROCRYPT
发表年份: 2000
created: 2025-05-27 11:46:49
modified: 2025-05-27 11:48:38
---
## Practical threshold signatures

## 发表信息

+ [原文链接](https://link.springer.com/content/pdf/10.1007/3-540-45539-6_15.pdf)

## 作者

+ [Victor Shoup](Victor%20Shoup.md)
## 笔记

### 背景与动机
门限签名协议允许任意 k 个参与者中的任意子集生成签名，而少于 k 个参与者（即使其中部分被腐化）无法伪造签名，同时需具备鲁棒性（腐化方不能阻止诚实方生成签名）。此前所有门限签名方案至少面临以下瓶颈之一：缺乏严格安全证明（即使在随机预言机模型中）、签名共享生成或验证需要交互且依赖同步网络、单个签名共享的大小随参与者数量线性增长。本文旨在填补这一空白，提出一种全新的 RSA 门限签名方案，满足：在随机预言机模型下基于 RSA 问题的困难性实现不可伪造性和鲁棒性；签名共享生成和验证完全非交互；单个共享大小仅为常数倍 RSA 模长。方案生成的签名是完全标准的“哈希-求逆” RSA 签名，公钥和验证算法与普通 RSA 一致，仅对密钥做出限制：公钥指数 e 必须是大于 l 的素数，模数 n 为两个强素数的乘积。此外，本文还引入了双参数门限概念（k 为最小法定人数，t 为最大腐化数，要求 k ≥ t+1），相比传统 k=t+1 情形提供更强的安全性保证，这一推广在异步拜占庭协议中具有重要应用。

### 相关工作

[Des87] Y. Desmedt. Society and group oriented cryptography: a new concept. **Crypto 1987** [Google Scholar](https://scholar.google.com/scholar?q=Society+and+group+oriented+cryptography+a+new+concept)
> 核心思路：首次提出门限签名的广义概念。
> 局限与区别：未提供具体安全证明，后续所有方案均需交互或大共享尺寸。

[DF89] Y. Desmedt and Y. Frankel. Threshold cryptosystems. **Crypto 1989** [Google Scholar](https://scholar.google.com/scholar?q=Threshold+cryptosystems)
> 核心思路：基于 Shamir 秘密共享和有限域上的多项式插值，给出非鲁棒门限 ElGamal 方案，共享尺寸小。
> 局限与区别：要求同步交互，且未正式分析安全性。

[DF91] Y. Desmedt and Y. Frankel. Shared generation of authenticators and signatures. **Crypto 1991** [Google Scholar](https://scholar.google.com/scholar?q=Shared+generation+of+authenticators+and+signatures)
> 核心思路：首次针对 RSA 设计非交互门限方案，共享尺寸小，但无安全性分析。
> 局限与区别：本文提供了严格安全证明，并解决了多项式插值模 φ(n) 的技术困难。

[FD92] Y. Frankel and Y. Desmedt. Parallel reliable threshold multisignature. **Technical Report 1992** [Google Scholar](https://scholar.google.com/scholar?q=Parallel+reliable+threshold+multisignature)
> 核心思路：给出非鲁棒 RSA 门限方案的安全证明，但需要同步交互。
> 局限与区别：本文方案完全非交互，且提供鲁棒性。

[DDFY94] A. De Santis et al. How to share a function securely. **STOC 1994** [Google Scholar](https://scholar.google.com/scholar?q=How+to+share+a+function+securely)
> 核心思路：以交互换取大共享尺寸（线性于玩家数）的变体方案。
> 局限与区别：本文方案共享尺寸恒定，且无需交互。

[GJKR96a] R. Gennaro et al. Robust and efficient sharing of RSA functions. **Crypto 1996** [Google Scholar](https://scholar.google.com/scholar?q=Robust+and+efficient+sharing+of+RSA+functions)
> 核心思路：给出使 RSA 门限方案鲁棒的一般技术，可避免随机预言机。
> 局限与区别：其非交互验证需要发送方与接收方之间的特殊关系，本文方案使用随机预言机简化验证。

[FGMY97b] Y. Frankel et al. Proactive RSA. **Crypto 1997** [Google Scholar](https://scholar.google.com/scholar?q=Proactive+RSA)
> 核心思路：提出鲁棒 RSA 门限方案，共享尺寸小但需要同步交互，并提供前向安全性。
> 局限与区别：本文方案不提供前向安全性，但实现了完全非交互。

[Rab98] T. Rabin. A simplified approach to threshold and proactive RSA. **Crypto 1998** [Google Scholar](https://scholar.google.com/scholar?q=A+simplified+approach+to+threshold+and+proactive+RSA)
> 核心思路：简化的鲁棒 RSA 门限方案，仍需要同步交互。
> 局限与区别：本文方案的交互性和效率优于该工作。

### 核心技术与方案

本文提出两种 RSA 门限签名协议，均基于 Shamir 秘密共享，但通过巧妙利用平方子群 $Q_n$（阶为 m = p'q'，无小素因子）来避免模 φ(n) 插值问题。

**Protocol 1（适用于 k = t+1）**：
- 密钥生成：选择强素数 p=2p'+1, q=2q'+1，模数 n=pq，m=p'q'。公钥指数 e 为大于 l 的素数。私钥 d 满足 de≡1 mod m。构造 k-1 次多项式 f(X)∈Z[X]，令秘密共享 s_i = f(i) mod m。验证密钥：随机 v∈Q_n，v_i = v^{s_i}。注意：所有群运算在 Q_n 内进行，指数算术在 Z_m 中。
- 签名共享生成：对消息 M，哈希 x=H(M)。玩家 i 输出共享 x_i = x^{2Δ s_i} ∈ Q_n，其中 Δ = l!。同时提供非交互正确性证明：利用 Chaum-Pedersen 协议，通过随机预言机 H' 将交互式协议“坍缩”为非交互式。证明者选择随机 r，计算 v'=v^r, x'= \tilde{x}^r（其中 \tilde{x}=x^{4Δ}），挑战 c=H'(v,\tilde{x},v_i,x_i^2,v',x')，回复 z=s_i c + r。验证者检查 c 是否等于 H'(v,\tilde{x},v_i,x_i^2, v^z v_i^{-c}, \tilde{x}^z x_i^{-2c})。
- 签名组合：从大小为 k 的集合 S 收集有效共享。利用 Lagrange 系数 λ_{0,j}^S (整数，计算如式(2))，计算 w = ∏_{j∈S} x_j^{2λ_{0,j}^S}。由式(3)得 w^e = x^{e'}，其中 e'=4Δ^2。因 gcd(e',e)=1，可计算 y=x^b w^a（满足 e'a+eb=1），得到标准 RSA 签名。
- 安全性：对于 k=t+1，在随机预言机模型下，利用 RSA 假设可证非伪造性和鲁棒性。证明通过模拟器：从腐化玩家的随机秘密开始，利用 RSA 签名预言机为未腐化玩家生成共享（通过 Lagrange 插值隐含未腐化玩家秘密）。正确性证明的零知识性由随机预言机保证。

**Protocol 2（适用于 k ≥ t+1）**：
- 改动：秘密共享改为 s_i = f(i) Δ^{-1} mod m。验证密钥额外包含 u∈Z_n^* 且 Jacobi 符号 (u|n)=-1。哈希处理：计算 \hat{x}=H(M)，若 (\hat{x}|n)=1 则 x=\hat{x}，否则 x=\hat{x} u^e，保证 x 的 Jacobi 符号为 1。共享生成简化为 x_i = x^{2s_i}，\tilde{x}=x^4，e'=4。组合后若需调整，除以 u 得到标准签名。
- 安全性：当 k=t+1 时仅需 RSA 假设；当 k>t+1 时还需 Decision Diffie-Hellman (DDH) 假设。证明采用三个逐步模拟器：第一个模拟器用随机 g, g_i 构造所有哈希值和共享（统计接近真实）；第二个模拟器在目标消息上改用另一组 h, h_i，并依赖 DDH 假设保持不可区分；第三个模拟器将目标消息哈希设为随机 z，当敌手未请求超过 k-t-1 个共享时给出随机二次剩余，最终提取 z 的 e 次根，矛盾。
- 复杂度：每个签名共享大小为 O(|n|) 比特；非交互验证常量轮；组合计算需 O(k) 次模指数运算。

### 核心公式与流程

**[密钥生成 - 秘密共享多项式]**
$$f(X) = \sum_{i=0}^{k-1} a_i X^i \in \mathbf{Z}[X], \quad s_i = f(i) \bmod m \ (\text{Protocol 1})$$
> 作用：定义多项式，玩家的秘密共享为多项式的点值。

**[Lagrange 插值系数（整数化）]**
$$\lambda_{i,j}^S = \Delta \frac{\prod_{j' \in S \setminus \{j\}} (i - j')}{\prod_{j' \in S \setminus \{j\}} (j - j')} \in \mathbf{Z}, \quad \Delta = l!$$
> 作用：用于在组合签名时，将 k 个共享线性组合恢复出与私钥 d = f(0) 相关的值。

**[Protocol 1 签名共享生成]**
$$x_i = x^{2\Delta s_i}, \quad \tilde{x} = x^{4\Delta}$$
> 作用：玩家 i 对消息 x 生成签名共享。

**[Protocol 1 组合]**
$$w = \prod_{j \in S} x_j^{2\lambda_{0,j}^S}, \quad e' = 4\Delta^2, \quad w^e = x^{e'}$$
> 作用：组合 k 个共享得到 w，其 e 次幂为 x 的 e' 次幂，再通过扩展欧几里得算法恢复 y 使 y^e = x。

**[Protocol 2 共享生成简化]**
$$x_i = x^{2s_i}, \quad \tilde{x} = x^4, \quad e' = 4$$
> 作用：消除 Δ 因子，简化计算。

### 实验结果
本文为理论密码学论文，未涉及实验评估。所有安全论证均基于数学归约和随机预言机模型。性能方面，作者指出方案的计算开销主要来自模指数运算：签名共享生成需常数次模指数（计算 x^{2s_i} 及正确性证明中的指数），验证需 O(1) 次模指数，组合需 O(k) 次模指数。通信开销：每个共享大小为 O(|n|) 比特（一个群元素加一个证明，证明含两个整数），与玩家数 l 无关。与以往需要同步交互或共享尺寸线性增长的方案相比，非交互性使其特别适合异步网络环境。

### 局限性与开放问题
方案依赖随机预言机模型，缺乏标准模型下的可证明安全性。密钥生成要求使用强索夫素数，且公钥指数 e 必须大于 l，限制了参数选择。Protocol 2 在 k > t+1 时还需额外的 DDH 假设，该假设在 Q_n 子群中虽有合理性但增加了安全性根基。开放问题包括：能否在标准模型（无需随机预言机）下构造类似高效的门限 RSA 方案？能否去掉对强素数或 e 的限制？是否可以实现前向安全性（proactive security）而不牺牲非交互性？

### 强关联论文

[DF89] Y. Desmedt and Y. Frankel. Threshold cryptosystems. **Crypto 1989** [Google Scholar](https://scholar.google.com/scholar?q=Threshold+cryptosystems)

[DF91] Y. Desmedt and Y. Frankel. Shared generation of authenticators and signatures. **Crypto 1991** [Google Scholar](https://scholar.google.com/scholar?q=Shared+generation+of+authenticators+and+signatures)

[FD92] Y. Frankel and Y. Desmedt. Parallel reliable threshold multisignature. **Technical Report 1992** [Google Scholar](https://scholar.google.com/scholar?q=Parallel+reliable+threshold+multisignature)

[DDFY94] A. De Santis et al. How to share a function securely. **STOC 1994** [Google Scholar](https://scholar.google.com/scholar?q=How+to+share+a+function+securely)

[GJKR96a] R. Gennaro et al. Robust and efficient sharing of RSA functions. **Crypto 1996** [Google Scholar](https://scholar.google.com/scholar?q=Robust+and+efficient+sharing+of+RSA+functions)

[FGMY97b] Y. Frankel et al. Proactive RSA. **Crypto 1997** [Google Scholar](https://scholar.google.com/scholar?q=Proactive+RSA)

[Rab98] T. Rabin. A simplified approach to threshold and proactive RSA. **Crypto 1998** [Google Scholar](https://scholar.google.com/scholar?q=A+simplified+approach+to+threshold+and+proactive+RSA)

[CP92] D. Chaum and T. Pedersen. Wallet databases with observers. **Crypto 1992** [Google Scholar](https://scholar.google.com/scholar?q=Wallet+databases+with+observers)

[BR93] M. Bellare and P. Rogaway. Random oracles are practical: a paradigm for designing efficient protocols. **ACM CCS 1993** [Google Scholar](https://scholar.google.com/scholar?q=Random+oracles+are+practical+a+paradigm+for+designing+efficient+protocols)


## 关键词

+ RSA门限签名
+ 随机预言机模型
+ 非交互式签名份额
+ 门限密码学
+ 分布式签名