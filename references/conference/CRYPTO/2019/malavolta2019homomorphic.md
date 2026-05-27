---
title: "Homomorphic time-lock puzzles and applications"
doi: 10.1007/978-3-030-26948-7_22
标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 2019
created: 2025-04-28 16:55:15
modified: 2025-04-28 16:58:48
---
## Homomorphic time-lock puzzles and applications

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-030-26948-7_22)
+ [archive](https://eprint.iacr.org/2019/635)

## 作者

+ [Giulio Malavolta](Giulio%20Malavolta.md)
+ Sri Aravinda Krishnan Thyagarajan 

## 笔记

### 背景与动机
时间锁谜题允许将秘密封装，使其在预设的时间 τ 内无法被任何并行算法破解，即便该算法拥有巨大规模。Rivest等人 [30] 提出的经典构造基于重复平方在 RSA 整数群中的内在顺序性，但其核心瓶颈在于：当时间锁谜题被大规模部署于例如电子投票等协议中时，若有大量用户（如10万选民）未能按时公开其谜题，则协议必须逐一求解每个谜题，这导致计算成为瓶颈。类似问题也出现在多方抛币、密封投标拍卖和公平合同签署等场景中。现有方案无法缓解这一规模化问题，因为公开这些谜题的求解过程所需工作量与离线用户数成正比。本文试图填补的空白是：能否在不解开单个谜题的前提下，对一组谜题执行函数运算，从而仅通过求解一个最终谜题便获得函数输出结果，大幅降低计算负担。

### 相关工作

[30] Rivest等. Time-lock puzzles and timed-release crypto. 1996 [Google Scholar](https://scholar.google.com/scholar?q=Time-lock+puzzles+and+timed-release+crypto)
> 核心思路：基于RSA模N下的重复平方运算构造时间锁谜题，求解需串行计算τ次平方。
> 局限与区别：无法支持同态运算，大规模应用时需逐一求解所有谜题，效率低。

[2] Bitansky等. Time-lock puzzles from randomized encodings. **ITCS 2016** [Google Scholar](https://scholar.google.com/scholar?q=Time-lock+puzzles+from+randomized+encodings)
> 核心思路：利用简洁随机编码构造时间锁谜题，不依赖于顺序平方假设。
> 局限与区别：该构造同样不支持同态运算，且求解效率依赖于非并行化语言，无法应用于本文所考虑的大规模同态计算场景。

[28] Paillier. Public-key cryptosystems based on composite degree residuosity classes. **EUROCRYPT 1999** [Google Scholar](https://scholar.google.com/scholar?q=Public-key+cryptosystems+based+on+composite+degree+residuosity+classes)
> 核心思路：利用群 $\mathbb{Z}_{N^2}^*$ 中阶为N的子群 $(1+N)$ 构造加法同态加密方案。
> 局限与区别：Paillier加密本身并非时间锁谜题，本文借鉴其代数结构，将其嵌入顺序平方框架，从而首次获得线性同态时间锁谜题。

[10] Couteau等. Encryption switching protocols. **CRYPTO 2016** [Google Scholar](https://scholar.google.com/scholar?q=Encryption+switching+protocols)
> 核心思路：分析了 $\mathbb{J}_N$ 上的DDH假设，并证明其可归约到 $\mathbb{Z}_p^*$ 和 $\mathbb{Z}_q^*$ 上的DDH与二次剩余假设。
> 局限与区别：本文的乘法同态方案直接依赖该DDH假设，利用 $\mathbb{J}_N$ 群保障安全性。

[20] Hohenberger等. Synchronized aggregate signatures from the RSA assumption. **EUROCRYPT 2018** [Google Scholar](https://scholar.google.com/scholar?q=Synchronized+aggregate+signatures+from+the+RSA+assumption)
> 核心思路：构造了基于RSA的聚合签名方案，其中签名位于 $\mathbb{QR}_N$ 且可通过乘法聚合。
> 局限与区别：该方案本身不是时间锁谜题，本文将其与乘法同态时间锁谜题结合，实现多方合同签名中的高效签名聚合。

[2] Bitansky等. Succinct randomized encodings and their applications. **STOC 2015** [Google Scholar](https://scholar.google.com/scholar?q=Succinct+randomized+encodings+and+their+applications)
> 核心思路：提出简洁随机编码并用于构造时间锁谜题和各类密码原语。
> 局限与区别：本文的全同态方案虽不直接基于此，但利用概率混淆作为核心工具，其思想受FHE构造启发。

[9] Canetti等. Obfuscation of probabilistic circuits and applications. **TCC 2015** [Google Scholar](https://scholar.google.com/scholar?q=Obfuscation+of+probabilistic+circuits+and+applications)
> 核心思路：提出概率混淆的定义，并给出基于子指数安全不可区分混淆和单向函数的构造。
> 局限与区别：本文的全同态方案直接调用该混淆器来保护“解密-求门-重加密”程序的内部状态。

[16] Gentry. Fully homomorphic encryption using ideal lattices. **STOC 2009** [Google Scholar](https://scholar.google.com/scholar?q=Fully+homomorphic+encryption+using+ideal+lattices)
> 核心思路：提出基于理想格的全同态加密（FHE）概念与首个构造，支持任意电路的同态评估。
> 局限与区别：FHE要求具备快速解密陷门，而时间锁谜题不要求此类陷门；本文的全同态方案借助混淆实现，而非依赖理想格或环上的困难假设。

[11] Damgård等. A generalisation, a simplification and some applications of Paillier's probabilistic public-key system. **PKC 2001** [Google Scholar](https://scholar.google.com/scholar?q=A+generalisation+a+simplification+and+some+applications+of+Paillier%27s+probabilistic+public-key+system)
> 核心思路：将Paillier加密方案推广到更高次幂模 $N^y$，消息域为 $\mathbb{Z}_{N^{y-1}}$，密码域为 $\mathbb{Z}_{N^y}^*$。
> 局限与区别：本文利用该扩展构造半紧凑的分支程序同态方案，其中密码长度与程序长度成线性关系。

[21] Ishai等. Evaluating branching programs on encrypted data. **TCC 2007** [Google Scholar](https://scholar.google.com/scholar?q=Evaluating+branching+programs+on+encrypted+data)
> 核心思路：提出将任意分支程序编译为仅需要乘法同态加密即可评估的构造。
> 局限与区别：本文将其与Damgård-Jurik扩展结合，得到半紧凑HTLP，其中评估后密码大小仅与分支程序长度相关。

[4] Boneh等. Verifiable delay functions. **CRYPTO 2018** [Google Scholar](https://scholar.google.com/scholar?q=Verifiable+delay+functions)
> 核心思路：提出可验证延迟函数（VDF），允许验证者确信证明者执行了指定串行计算量。
> 局限与区别：VDF不能封装秘密，时间锁谜题不能高效验证，二者概念不可比较；本文的强顺序平方假设与VDF中的假设类似。

### 核心技术与方案
本文提出连接“同态运算”与“时间锁禁”两个概念，正式定义了同态时间锁谜题（Homomorphic Time-Lock Puzzles, HTLP），并针对不同函数类构造了三种方案。

首先，线性同态方案（LHTLP）沿用RSA重复平方框架，但将消息编码到Paillier群 $(1+N) \in \mathbb{Z}_{N^2}^*$ 中。设置算法生成公参 $pp = (\tau, N, g, h = g^{2^\tau})$，其中 $g \in \mathbb{J}_N$ 是生成元。生成谜题时，加密者选取随机 $r \gets \{1, \dots, N^2\}$，计算 $u = g^r \bmod N$，$v = h^{r \cdot N} \cdot (1+N)^s \bmod N^2$，输出 $Z=(u,v)$。求解时通过重复平方计算 $w = u^{2^\tau} \bmod N$，再利用等式 $v / w^N \pmod{N^2} = (1+N)^s \pmod{N^2}$ 并利用 $(1+N)^s \equiv 1 + sN \pmod{N^2}$ 恢复$s$。同态加法直接对应分量相乘：$\tilde{u} = \prod u_i, \tilde{v} = \prod v_i$。安全性依赖于三个假设：(1) 顺序平方假设（区分 $g^{2^\tau}$ 与随机元素），(2) $\mathbb{J}_N$ 上的 DDH 假设，(3) DCR 假设。证明通过混合论证逐步将 $h$ 随机化、将 $r$ 的分布逼近理想分布、将 $u$ 随机化，最终将 $v$ 中的 $h^{rN}$ 部分替换为均匀随机值使得消息完全隐藏。

其次，乘法同态方案（MHTLP）将消息编码在 $\mathbb{J}_N$ 上。设置阶段与线性方案相同，但 $v = h^r \cdot s \bmod N$，$u = g^r \bmod N$。求解时计算 $s = v / u^{2^\tau}$。乘法同态同样通过分量相乘实现。安全性依赖于顺序平方假设和 $\mathbb{J}_N$ 上的 DDH 假设。通过将 $h$ 随机化（基于顺序平方假设）和将 $v$ 中的 $h^r$ 替换为均匀随机元素（基于 DDH），最终消息被完美隐藏。

当 $N$ 为 Blum 整数时将消息编码为 $(-1)^s$，乘法方案即获得异或同态。

最后，全同态方案（FHTLP）作为可行性结果给出，利用概率混淆构造，声称可支持任意电路的紧凑同态评估。其核心思路是：每个谜题包含一对元素 $(z, c)$，其中 $z$ 来自标准（非同态）时间锁谜题，$c$ 是传统公钥加密的密文，二者编码同一比特 $s$。求解时仅解开 $z$。同态运算通过混淆程序实现：该程序输入两个谜题，解密 $c$，计算 NAND 门，再重新生成新的 $(z', c')$ 作为输出。电路深度需限制于超多项式长度 $\mathcal{L}(\lambda) = 2^{\omega(\log \lambda)}$。安全性需同时依赖于陷门加密的不可区分性、概率混淆的安全性、不可区分混淆的安全性以及可穿刺 PRF 的安全性，且要求区分差距为 $\mu(\lambda) \cdot \mathcal{L}^{-1}$，因此各类假设需要子指数安全水平。

此外，论文还探讨了几项扩展：(1) 利用 Damgård-Jurik 扩展得到半紧凑的分支程序方案，其中评估后谜题大小与分支程序长度成正比。(2) 通过强化顺序平方假设（允许攻击者选择 $\tau$）实现可重用的设置安全。(3) 公开硬币设置可通过预先计算 $g^{2^\tau}$ 实现，但需 $\tau$ 次串行平方，可能影响效率。(4) 不同硬度参数下的同态运算可通过适当调整 $u$ 的分量幂次实现。

### 核心公式与流程

**[线性同态：LHTLP.PGen]**
$$u := g^r \pmod{N}, \quad v := h^{r \cdot N} \cdot (1+N)^s \pmod{N^2}$$
> 作用：将秘密 $s \in \mathbb{Z}_N$ 封装为谜题 $(u,v)$，利用 Paillier 群结构实现加法同态。

**[线性同态：LHTLP.PSolve]**
$$w := u^{2^\tau} \pmod{N}, \quad s := \frac{v / w^N \pmod{N^2} - 1}{N}$$
> 作用：通过 $\tau$ 次串行平方恢复 $w$，然后利用 $(1+N)^s \equiv 1 + sN \pmod{N^2}$ 析取 $s$。

**[线性同态：LHTLP.PEval]**
$$\tilde{u} := \prod_i u_i \pmod{N}, \quad \tilde{v} := \prod_i v_i \pmod{N^2}$$
> 作用：对一组谜题执行加法同态操作，输出谜题 $(\tilde{u}, \tilde{v})$ 对应 $\sum_i s_i$。

**[乘法同态：MHTLP.PGen]**
$$u := g^r \pmod{N}, \quad v := h^r \cdot s \pmod{N}$$
> 作用：将秘密 $s \in \mathbb{J}_N$ 封装为谜题 $(u,v)$，利用 ElGamal 风格实现乘法同态。

**[乘法同态：MHTLP.PSolve]**
$$w := u^{2^\tau} \pmod{N}, \quad s := v / w$$
> 作用：通过 $\tau$ 次串行平方恢复 $w$，然后计算 $s = v/w$。

**[乘法同态：MHTLP.PEval]**
$$\tilde{u} := \prod_i u_i \pmod{N}, \quad \tilde{v} := \prod_i v_i \pmod{N}$$
> 作用：对一组谜题执行乘法同态操作，输出谜题 $(\tilde{u}, \tilde{v})$ 对应 $\prod_i s_i$。

### 实验结果
本文未提供实验评估。所有方案均为理论构造，渐进复杂度如下：线性与乘法方案中，谜题生成和同态评估均为多项式时间，求解时间为 $\tau$ 次串行平方。全同态方案中，混淆电路的大小随支撑电路深度呈超多项式增长（实际限制条件 $\ell \leq 2^{\omega(\log \lambda)}$）。半紧凑分支程序方案中，评估后谜题大小与分支程序长度 $L$ 成正比而非宽度，即 $|Z'| = \tilde{O}(L)$。论文通过电子投票（$n$ 选1，最终只需解 $m$ 个谜题）、多方抛币（解1个谜题）、密封投标（需全同态）和多方合同签署（解1个聚合谜题）等应用论证其实际可用性与潜在规模优势，但未给出具体运行时间或性能对比数据。

### 局限性与开放问题
所有RSA方案均依赖信任设置，若随机因子泄露则产生不公平优势。构造公开硬币版HTLP且保持高效是该工作的一个开放问题。全同态方案需要概率混淆，当前混淆构造效率极低，仅作为可行性结果存在，无法直接实用。半紧凑分支程序方案中谜题大小虽不依赖于电路宽度但仍与程序长度成线性，效率有待进一步提高。此外，所有方案的安全性依赖强顺序平方假设，该假设虽在VDF文献中已被采纳，但仍然是对传统顺序平方假设的强化。

### 强关联论文

[30] Rivest, R.L., Shamir, A., Wagner, D.A. Time-lock puzzles and timed-release crypto. 1996 [Google Scholar](https://scholar.google.com/scholar?q=Time-lock+puzzles+and+timed-release+crypto)

[28] Paillier, P. Public-key cryptosystems based on composite degree residuosity classes. **EUROCRYPT 1999** [Google Scholar](https://scholar.google.com/scholar?q=Public-key+cryptosystems+based+on+composite+degree+residuosity+classes)

[10] Couteau, G., Peters, T., Pointcheval, D. Encryption switching protocols. **CRYPTO 2016** [Google Scholar](https://scholar.google.com/scholar?q=Encryption+switching+protocols)

[20] Hohenberger, S., Waters, B. Synchronized aggregate signatures from the RSA assumption. **EUROCRYPT 2018** [Google Scholar](https://scholar.google.com/scholar?q=Synchronized+aggregate+signatures+from+the+RSA+assumption)

[2] Bitansky, N., Goldwasser, S., Jain, A., Paneth, O., Vaikuntanathan, V., Waters, B. Time-lock puzzles from randomized encodings. **ITCS 2016** [Google Scholar](https://scholar.google.com/scholar?q=Time-lock+puzzles+from+randomized+encodings)

[11] Damgård, I., Jurik, M. A generalisation, a simplification and some applications of Paillier's probabilistic public-key system. **PKC 2001** [Google Scholar](https://scholar.google.com/scholar?q=A+generalisation+a+simplification+and+some+applications+of+Paillier%27s+probabilistic+public-key+system)

[16] Gentry, C. Fully homomorphic encryption using ideal lattices. **STOC 2009** [Google Scholar](https://scholar.google.com/scholar?q=Fully+homomorphic+encryption+using+ideal+lattices)

[9] Canetti, R., Lin, H., Tessaro, S., Vaikuntanathan, V. Obfuscation of probabilistic circuits and applications. **TCC 2015** [Google Scholar](https://scholar.google.com/scholar?q=Obfuscation+of+probabilistic+circuits+and+applications)

[21] Ishai, Y., Paskin, A. Evaluating branching programs on encrypted data. **TCC 2007** [Google Scholar](https://scholar.google.com/scholar?q=Evaluating+branching+programs+on+encrypted+data)

[4] Boneh, D., Bonneau, J., Bünz, B., Fisch, B. Verifiable delay functions. **CRYPTO 2018** [Google Scholar](https://scholar.google.com/scholar?q=Verifiable+delay+functions)


## 关键词

+ 密码学
+ 零知识
+ 协议