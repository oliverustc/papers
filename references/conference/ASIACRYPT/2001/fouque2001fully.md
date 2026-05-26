---
title: "Fully distributed threshold RSA under standard assumptions"
标题简称:
论文类型: conference
会议简称: ASIACRYPT
发表年份: 2001
created: 2025-05-27 11:56:02
modified: 2025-05-27 11:56:08
---

## Fully distributed threshold RSA under standard assumptions

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/3-540-45682-1_19)

## 作者

+ Pierre-Alain Fouque
+ Jacques Stern

## 笔记

### 背景与动机

RSA 是现代公钥基础设施的基石，但在实际系统中，根密钥的保护至关重要。阈值密码学通过将签名能力分散到一组服务器上，能够抵御比“集中式”系统更强的对手——特别是能够侵入服务器内存的“入侵型”对手 [6]。为实现完全分布式的 RSA，需要从密钥生成到签名/解密阶段全部由多方协作完成，而无需可信中心。在离散对数类密码系统中，已存在成熟的分布式解决方案 [20, 38, 7, 27, 21, 15]，但 RSA 的完全分布式化是一个更具挑战性的任务。Shoup 于 Eurocrypt 2000 提出的实用阈值 RSA 签名方案 [37] 具有非交互式签名份额生成、固定大小的份额等优点，但其假设一个可信中心来生成和分发密钥，且要求 RSA 模数为安全素数模数。Boneh 和 Franklin 于 Crypto 1997 提出的协议 [4] 能够分布式生成 RSA 模数，但无法高效地生成安全素数模数，因此无法直接与 Shoup 的方案结合。本文旨在解决这一矛盾，在标准假设下构造完全分布式的阈值 RSA 方案。

### 相关工作

[4] Boneh and Franklin. Efficient Generation of Shared RSA keys. **Crypto 1997** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+Generation+of+Shared+RSA+keys)
> 核心思路：提出分布式生成 RSA 模数的协议，在诚实但好奇模型下有效。
> 局限与区别：无法适用于生成安全素数模数，且对抗恶意敌手需要额外代价，无法直接满足 Shoup 方案的要求。

[37] Shoup. Practical Threshold Signatures. **Eurocrypt 2000** [Google Scholar](https://scholar.google.com/scholar?q=Practical+Threshold+Signatures)
> 核心思路：提出基于多项式分享的阈值 RSA 签名方案，具有非交互式证明、份额大小恒定等优点。
> 局限与区别：依赖可信中心生成密钥，且要求模数为安全素数（p=2p'+1, q=2q'+1），否则无法保证证明的正确性。

[16] Frankel, Gemmell, MacKenzie, Yung. Optimal Resilience Proactive Public-Key Cryptosystems. **FOCS 1997** [Google Scholar](https://scholar.google.com/scholar?q=Optimal+Resilience+Proactive+Public-Key+Cryptosystems)
> 核心思路：提出完全分布式的 RSA 方案，但依赖于交互式协议。
> 局限与区别：方案的交互性导致效率低于 Shoup 的非交互方案，且仍需解决安全素数生成问题。

[18] Frankel, MacKenzie, Yung. Robust Efficient Distributed RSA Key Generation. **STOC 1998** [Google Scholar](https://scholar.google.com/scholar?q=Robust+Efficient+Distributed+RSA+Key+Generation)
> 核心思路：将 Boneh-Franklin 协议扩展为鲁棒版本，可抵抗恶意服务器。
> 局限与区别：该协议生成的模数不满足 Shoup 方案对安全素数的要求。

[8] Catalano, Gennaro, Halevi. Computing Inverses over a Shared Secret Modulus. **Eurocrypt 2000** [Google Scholar](https://scholar.google.com/scholar?q=Computing+Inverses+over+a+Shared+Secret+Modulus)
> 核心思路：提出分布式计算模逆和 GCD 的协议，可用于密钥生成。
> 局限与区别：该协议被本文用作子协议，以计算 GCD 和逆元。

[12] Damgård and Koprowski. Practical Threshold RSA Signatures Without a Trusted Dealer. **Eurocrypt 2001** [Google Scholar](https://scholar.google.com/scholar?q=Practical+Threshold+RSA+Signatures+Without+a+Trusted+Dealer)
> 核心思路：独立于本文，也提出无需可信中心的阈值 RSA 方案，使用非标准假设。
> 局限与区别：本文坚持标准假设，而 Damgård 等使用了非标准假设。

[31] Poupard and Stern. Short Proofs of Knowledge for Factoring. **PKC 2000** [Google Scholar](https://scholar.google.com/scholar?q=Short+Proofs+of+Knowledge+for+Factoring)
> 核心思路：给出关于生成循环群中生成元数目的概率分析。
> 局限与区别：本文扩展了该分析以适用于 RSA 平方子群。

### 核心技术与方案

**整体框架：** 本文分两步解决完全分布式阈值 RSA 问题。首先，对 Boneh-Franklin 的分布式 RSA 模数生成协议加以增强，使得生成的模数满足 Shoup 方案所需的安全素数要求。具体地，要求模数 $N=pq$ 满足 $p=2p'+1$, $q=2q'+1$，且 $\gcd(p',q')=1$，并且 $p'$ 和 $q'$ 没有小于筛查界 $B$ 的素因子——这保证了平方子群 $Q_N$ 是循环的且其阶 $M=p'q'$ 没有小素因子。其次，修改 Shoup 的签名方案，使其正确性证明不再依赖单一生成元，而是使用 $k$ 个随机元素构成的生成元集合，证明这些元素以高概率生成整个 $Q_N$，从而在标准假设下完成安全证明。

**密钥生成增强：**

1. **筛查算法改进模数生成：** 在 Boneh-Franklin 协议的第一步，每个服务器选取随机整数 $p_i, q_i$。为了提高成功率并保证 $p'$ 和 $q'$ 无小素因子，引入分布式筛查算法：服务器先秘密选取与 $P$（所有小于 $B$ 的奇素数之积）互素的 $a_i$，然后通过 BGW 协议将乘法分享转化为加法分享 $b_i$，最终设置 $p_i = r_i P + b_i$，使得 $p = \sum p_i$ 模 $P$ 等于 $a_i$ 的乘积，从而 $p$ 不被任何小于 $B$ 的素数整除。进一步，通过分布式 GCD 协议（Catalano 等 [8]）检查 $\gcd(p-1, 4P)=2$ 以及 $\gcd(q-1, 4P)=2$，以确保 $p'$ 和 $q'$ 也没有小素因子。

2. **确保 $Q_N$ 循环：** 利用引理 1：$\gcd(p-1,q-1) \mid \gcd(N-1,\varphi(N))$，且 $\gcd(N-1,\varphi(N))$ 的平方自由部分整除 $\gcd(p-1,q-1)$。因此只要 $\gcd(N-1,\varphi(N))=2$，则 $\gcd(p-1,q-1)=2$。这可以通过分布式 GCD 协议检验。从而 $Q_N$ 是循环群（即 $p'$ 与 $q'$ 互素，且两者均为奇数，因此 $Q_p$ 和 $Q_q$ 均为循环群，且阶互素，乘积为循环群）。

3. **密钥分发：** 在 $N$ 生成后，选取素数 $e > 4\Delta^2$（其中 $\Delta = \ell!$），然后运行 Catalano 等的协议 [8] 计算 $d$ 使得 $ed \equiv 1 \pmod{\varphi(N)}$，并为每个服务器设置多项式分享 $d_i$，且 $d_i$ 满足 $\Delta d_i = f(i)$，$f$ 为 $t$ 次多项式且 $f(0) = \Delta d$。验证密钥则为 $v_{u,i} = v_u^{\Delta d_i} \bmod N$，其中 $v_u = y_u^{2\Delta e} \bmod N$，$y_u$ 由哈希函数产生。

**签名协议增强（对抗主动敌手）：**

1. **使用多个生成元：** 由于无法找到单个已知离散对数的生成元，选取 $k$ 个随机元素 $v_1,\dots,v_k \in Q_N$。定理 6 证明：若 $p',q'$ 无小于 $B$ 的素因子，则随机 $k$-元组生成整个 $Q_N$ 的概率大于 $1 - 2 \times \frac{2}{k-1} \times \frac{1}{B^{k-1}}$。实际取 $k=6$, $B=2^{16}$ 即可达到 $1-2^{-80}$ 的概率。

2. **正确性证明：** 每个服务器 $i$ 对消息 $m$ 计算 $x=H(m)$，产生签名份额 $s_i = x^{2\Delta d_i} \bmod N$，并证明 $\log_{v_1}(v_{1,i}) = \cdots = \log_{v_k}(v_{k,i}) = \log_{x^{4\Delta}}(s_i^2) = d_i \bmod M$。证明采用 Fiat-Shamir 变换，承诺中同时涉及所有 $v_u$ 和 $x^{4\Delta}$，挑战 $e$ 取自哈希值的前 $b'$ 位（$b' = \log B'$），回答 $z = r + e d_i$。验证者检查 $0 \leq z < A$ 以及重新计算哈希是否匹配。协议只需 $h=5$ 轮（安全参数 $2^{-80}$ 时）。

3. **安全分析：** 完备性要求 $B' M h / A$ 可忽略；可靠性（定理 5）依赖 $B' < B$ 且 $\gcd(\tau, M)=1$，而 $|\tau|<B'$，故 $\tau$ 与 $M$ 互素，可消去；统计零知识性要求 $A$ 远大于 $B'\times N$，使响应不泄露私钥。最终签名恢复时，组合者选取 $t+1$ 个有效份额，计算 $w = \prod_{j=1}^{t+1} s_{i_j}^{2\lambda_{0,i_j}^S}$，得到 $w^e = x^{4\Delta^2}$，再通过扩展欧几里得算法从 $e$ 和 $4\Delta^2$ 得到 $x^d$。

### 核心公式与流程

**[平方子群生成元概率]**
$$
\Pr_{(v_1,\dots,v_k)\in (Q_p)^k}\{\langle v_1,\dots,v_k\rangle = Q_p\} > 1 - \frac{k+B-1}{k-1}\cdot\frac{1}{B^k}
$$
> 作用：给出使用 $k$ 个随机元素生成整个平方子群 $Q_N$ 所需的参数选择依据，定理 6 中取 $k=6$, $B=2^{16}$ 得到概率 $1-2^{-80}$。

**[签名份额组合公式]**
$$
s = \prod_{i\in S} s_i^{\lambda_{0,i}^S}, \quad \lambda_{0,i}^S = \Delta \prod_{j'\in S\setminus\{i\}} \frac{0 - j'}{i - j'} \in \mathbb{Z}
$$
> 作用：组合 $t+1$ 个有效签名份额 $s_i$ 得到中间值 $s^\Delta$（实际协议中先计算 $w = \prod s_{i_j}^{2\lambda_{0,i_j}^S}$，得到 $w^e = x^{4\Delta^2}$），最后通过求 $e$ 次根恢复签名。

**[正确性证明的验证等式]**
$$
e \stackrel{?}{=} \bigl[ H(v_1,\dots,v_k, x^{4\Delta}, v_{1,i},\dots,v_{k,i}, s_i^2, \; v_1^z v_{1,i}^{-e},\dots, v_k^z v_{k,i}^{-e},\; x^{4\Delta z} s_i^{-2e}) \bigr]_{b'}
$$
> 作用：验证服务器 $i$ 的签名份额 $s_i$ 是否对应于正确的私钥 $d_i$，其中 $z = r + e d_i$，$r$ 为随机数，$e$ 为哈希挑战。

### 实验结果

本文不涉及实验原型或系统实现，但给出了详细的参数分析和复杂度估计。密钥生成阶段：使用筛查界 $B=2^{16}$ 时，平均需要运行 Boneh-Franklin 协议的第一阶段约 $2\times (e^\gamma \ln B + e^\gamma \ln B) \approx 80$ 次（其中 $\gamma$ 为欧拉常数，$\ln(2^{16})\approx 11.09$，$e^\gamma\approx1.78$，每次成功概率约 $1/20$），才能得到同时满足 $p'$ 和 $q'$ 无小素因子且 $\gcd(p-1,q-1)=2$ 的模数。这个开销仅在协议运行一次时发生。签名阶段：当安全参数为 $2^{-80}$ 时，取 $B'=2^{16} < B$，轮数 $h=5$，生成元个数 $k=6$，每个服务器需要执行 $h \times k = 30$ 个非交互式零知识证明（每个证明包括一次承诺和一次响应），通信量和计算量均与 $k$ 和 $h$ 呈线性关系。与 Shoup 原方案相比，额外开销主要来自密钥生成的多次尝试和签名证明中的多组验证密钥，但在高安全需求的环境（如电子投票）中是可接受的。

### 局限性与开放问题

本文的方案在标准假设下实现了完全分布式 RSA，但代价是密钥生成阶段的平均迭代次数约为 80 次，签名阶段的证明需要 30 条独立验证，效率低于依赖可信中心的 Shoup 原方案。此外，方案假设静态敌手且网络为同步广播模型，未考虑自适应敌手或异步环境。开放问题包括：是否可以进一步降低安全素数生成的开销，以及能否将本方案扩展为自适应安全的签密方案。

### 强关联论文

[4] Boneh and Franklin. Efficient Generation of Shared RSA keys. **Crypto 1997** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+Generation+of+Shared+RSA+keys)

[37] Shoup. Practical Threshold Signatures. **Eurocrypt 2000** [Google Scholar](https://scholar.google.com/scholar?q=Practical+Threshold+Signatures)

[16] Frankel, Gemmell, MacKenzie, Yung. Optimal Resilience Proactive Public-Key Cryptosystems. **FOCS 1997** [Google Scholar](https://scholar.google.com/scholar?q=Optimal+Resilience+Proactive+Public-Key+Cryptosystems)

[18] Frankel, MacKenzie, Yung. Robust Efficient Distributed RSA Key Generation. **STOC 1998** [Google Scholar](https://scholar.google.com/scholar?q=Robust+Efficient+Distributed+RSA+Key+Generation)

[8] Catalano, Gennaro, Halevi. Computing Inverses over a Shared Secret Modulus. **Eurocrypt 2000** [Google Scholar](https://scholar.google.com/scholar?q=Computing+Inverses+over+a+Shared+Secret+Modulus)

[12] Damgård and Koprowski. Practical Threshold RSA Signatures Without a Trusted Dealer. **Eurocrypt 2001** [Google Scholar](https://scholar.google.com/scholar?q=Practical+Threshold+RSA+Signatures+Without+a+Trusted+Dealer)

[31] Poupard and Stern. Short Proofs of Knowledge for Factoring. **PKC 2000** [Google Scholar](https://scholar.google.com/scholar?q=Short+Proofs+of+Knowledge+for+Factoring)

[22] Gennaro, Micciancio, Rabin. An Efficient Non-Interactive Statistical Zero-Knowledge Proof System for Quasi-Safe Prime Products. **ACM CCS 1998** [Google Scholar](https://scholar.google.com/scholar?q=An+Efficient+Non-Interactive+Statistical+Zero-Knowledge+Proof+System+for+Quasi-Safe+Prime+Products)

[5] Boneh, Malkin, Wu. Experimenting with Shared Generation of RSA keys. **SNDSS 1999** [Google Scholar](https://scholar.google.com/scholar?q=Experimenting+with+Shared+Generation+of+RSA+keys)


## 关键词

+ 门限RSA
+ 分布式密钥生成
+ 阈值签名
+ 安全多方计算
+ 无可信经销商