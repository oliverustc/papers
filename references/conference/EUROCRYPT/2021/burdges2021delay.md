---
title: "Delay encryption"
标题简称:
论文类型: conference
会议简称: EUROCRYPT
发表年份: 2021
created: 2025-04-28 17:17:57
modified: 2025-04-28 17:18:21
---

## Delay encryption

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-030-77870-5_11)

## 作者

+ Jeffrey Burdges 
+ Luca De Feo 

## 笔记

### 背景与动机
延迟密码学最早由 Rivest、Shamir 和 Wagner 的时间锁谜题（Time-lock Puzzle）[29] 提出，它允许加密者利用陷门快速加密或解密，而其他人只能通过慢速的串行计算来解密。近年来，区块链技术催生了可验证延迟函数（VDF）[4] 的复兴，这类函数保证串行求值无法加速，但验证可快速完成。然而，时间锁谜题在大型拍卖或选举中面临效率瓶颈：每个投标者需生成一个谜题，而计票者必须依次求解大量谜题，无法利用同态性进行批量解密；现有同态时间锁谜题 [25] 仅支持简单同态（加法或乘法），完全同态方案 [9,25] 则效率极低。本文引入一种名为“延迟加密”（Delay Encryption）的新原语，它没有陷门，加密快速，解密需经过一个固定的串行计算（提取），从而更自然地解决拍卖、投票等场景中“加密到未来”的需求。该原语可视为身份基加密（IBE）在时间延迟领域中的自然类比，其核心是将 IBE 中的主私钥替换为一个公开但串行缓慢的等ogeny 链。

### 相关工作

[4] Boneh 等. Verifiable delay functions. **CRYPTO 2018** [Google Scholar](https://scholar.google.com/scholar?q=Verifiable+delay+functions)
> 核心思路：正式定义 VDF，提出高效验证的延迟函数概念。
> 局限与区别：本文的 Delay Encryption 不仅提供验证，还提供加密功能，且没有陷门。

[6] Boneh 等. Identity-based encryption from the Weil pairing. **SIAM J. Comput. 2003** [Google Scholar](https://scholar.google.com/scholar?q=Identity-based+encryption+from+the+Weil+pairing)
> 核心思路：利用双线性配对构造首个实用的 IBE 方案。
> 局限与区别：本文修改其结构，将主私钥替换为等ogeny 链，使私钥生成变为慢速串行过程。

[17] De Feo 等. Verifiable delay functions from supersingular isogenies and pairings. **ASIACRYPT 2019** [Google Scholar](https://scholar.google.com/scholar?q=Verifiable+delay+functions+from+supersingular+isogenies+and+pairings)
> 核心思路：基于超奇异等ogeny 和配对构造 VDF，将等ogeny 链作为延迟函数，利用配对验证。
> 局限与区别：本文在此框架基础上构建延迟加密，将 VDF 的求值（等ogeny 的dual）作为提取过程，并添加加密封装/解封算法。

[25] Malavolta 等. Homomorphic time-lock puzzles and applications. **CRYPTO 2019** [Google Scholar](https://scholar.google.com/scholar?q=Homomorphic+time-lock+puzzles+and+applications)
> 核心思路：提出同态时间锁谜题，支持加法或乘法同态运算。
> 局限与区别：仅支持简单同态，无法处理拍卖中所需的任意函数；本文的延迟加密不依赖同态，直接通过公开提取实现批量解密。

[27] Pietrzak. Simple verifiable delay functions. **ITCS 2019** [Google Scholar](https://scholar.google.com/scholar?q=Simple+verifiable+delay+functions)
> 核心思路：基于未知阶群中重复平方构造 VDF。
> 局限与区别：该 VDF 无陷门，但无法直接支持加密；本文的延迟加密提供加密功能。

[29] Rivest 等. Time-lock puzzles and timed-release crypto. **Technical Report 1996** [Google Scholar](https://scholar.google.com/scholar?q=Time-lock+puzzles+and+timed-release+crypto)
> 核心思路：引入时间锁谜题，利用陷门实现快速加密/解密。
> 局限与区别：存在陷门，且无法高效支持大规模拍卖；本文的延迟加密无陷门，且提取过程公开。

[34] Wesolowski. Efficient verifiable delay functions. **EUROCRYPT 2019** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+verifiable+delay+functions)
> 核心思路：基于未知阶群构造高效 VDF，支持短证明。
> 局限与区别：同样无加密能力，且依赖 RSA 群的可信设置；本文的延迟加密从等ogeny 出发，可信设置可分布式实现。

### 核心技术与方案
延迟加密的 API 类似密钥封装机制（KEM），包含四个算法：Setup(λ, T)→(ek, pk)，其中 ek 为提取密钥，pk 为加密密钥，Setup 运行时间 poly(λ, T)；Extract(ek, id)→idk，需要恰好 T 步串行计算，无更快算法；Encaps(pk, id)→(c, k)，运行时间 poly(λ)；Decaps(pk, id, idk, c)→k，运行时间 poly(λ)。正确性要求对任意 id，提取得到的 idk 能正确解封装。安全性定义为 Δ-IND-CPA：敌手在预计算阶段获得 (ek, pk) 后输出算法 D，挑战者随机选取 id 并生成 (c, k₀) 和随机 k₁，敌手需在时间小于 Δ 内区分 k₀ 与 k₁。该游戏不考虑解密预言机，因为 idk 在延迟时间之前无人知晓。

与 IBE 的类比：将 IBE 中的主密钥替换为公开的等ogeny 链 φ: E → E'，其中 E 是超奇异曲线，φ 由 T 次 2-等ogeny 组成。提取过程即计算 φ 的 dual 映射 φ̂。Encaps 将 id 哈希到 E' 上的点 Q，选取随机 r，输出 (rP, H₂(e'_N(φ(P), Q)^r))，其中 P 是 E(F_p) 上的 N 阶点，e'_N 是 E' 上的 Weil 配对。Decaps 利用 idk = φ̂(Q) 计算 e_N(rP, φ̂(Q)) 得到共享密钥。

安全证明依赖于双线性等ogeny 捷径（bilinear isogeny shortcut）假设：给定 p, N, E, E', φ，敌手无法在时间 Δ' 内计算 e'_N(φ(R), Q) = e_N(R, φ̂(Q))，其中 R ∈ E[(N, π-1)]，Q ∈ E'[N] 随机。证明将 Δ-IND-CPA 敌手归约到该假设，类似 Boneh-Franklin 的 IBE 证明，在随机预言机模型下成立，归约损失因子为 q（哈希查询次数），延迟增加 q·poly(λ)。

已知攻击有三种：捷径攻击（利用端环知识压缩路径）、离散对数攻击（在目标群中解 DLP，需选择足够大的 p 和 N）、计算攻击（通过硬件并行加速）。为抵御捷径攻击，起始曲线 E 必须通过可信设置生成，使得计算 End(E) 困难。本文提出分布式可信设置协议：多个参与者依次从已知曲线 E₀ 开始进行伪随机等ogeny 行走并发布零知识证明，只要至少一个参与者诚实，最终曲线 E 即为安全的。证明采用 Schnorr 风格的零知识证明，基于 CDH 假设和随机预言机模型，证明知道从 E_{i-1} 到 E_i 的等ogeny。

水印方案用于奖励提取者：将等ogeny 链分为两半 φ₁, φ₂，提取者计算中间点 Q_mid = φ̂₂(Q) 并发布 sQ_mid（s 是秘密标量），验证者通过配对检查 e_mid(φ₁(P), sQ_mid) = e'_N(S, Q)，其中 S = sφ(P)。篡改者需完成至少一半的计算。

实现方面，2-等ogeny 的 dual 映射 φ̂_α 的投影坐标公式为 ( (X+Z)² : 4α X Z )，每次只需 2 次乘法和 1 次并行平方。为保持非回溯行走，使用 Castryck-Decru 给出的 α' = (α + √(α²-1))²（当 p ≡ 7 mod 8 时取主平方根），确保曲线落在 F_p 上。

### 核心公式与流程

**[Weil 配对的双线性与等ogeny 的伴随关系]**
$$e'_N(\phi(P), Q) = e_N(P, \hat{\phi}(Q))$$
> 作用：验证等ogeny 计算正确性；用于构造 Dual 映射的检验等式。

**[2-等ogeny 的 dual 映射投影公式]**
$$\hat{\phi}_\alpha (X:Z) = \big((X+Z)^2 : 4\alpha X Z\big)$$
> 作用：提取过程中每次 2-等ogeny 求值的核心操作，仅需 2 乘法 + 1 并行平方。

**[非回溯 2-等ogeny 行走的 α 更新]**
$$\alpha' = \big(\alpha + \sqrt{\alpha^2 - 1}\big)^2$$
> 作用：确保下一步 isogeny 不回溯，且曲线保持定义在 F_p 上（当 p ≡ 7 mod 8 时）。

**[零知识证明中的验证等式]**
$$e_N^i(X, Q) \cdot Y' = e_N^{i-1}(P, Y) \cdot X'$$
> 作用：证明者知道从 E_{i-1} 到 E_i 的等ogeny，其中 X = rψ_i(P) + xP'，Y = rψ̂_i(Q) + yQ'，X', Y' 为相应的配对承诺。

### 实验结果
本文未提供实际实验，但基于理论分析给出了实现挑战和估计。对于 128 位安全级别，选择素数 p 约 1500 位（与 2048 位 RSA 相当），配对目标群大小 N 约 2^{2λ}=2^{256}。每个 2-等ogeny 求值在 FPGA 上预计需约 50 ns（基于 Ethereum FPGA 竞赛中 2048 位 RSA 延时 25 ns 的乐观估计）。若目标延迟为 1 小时，则 isogeny 链长度约 7×10^{10} 步，需存储所有 α 系数（每个 1500 位），总存储约 12 TiB。这一存储量使评估密钥 ek 极大，但可通过将链分段并哈希中间结果来压缩存储（适用于 VDF，不适用于延迟加密），代价是使求值变慢。在软件中，1500 位模乘延迟约 1 μs，理论延迟 1 小时需 3.6×10^{12} 步，远超 FPGA 方案。目前存储带宽尚不构成瓶颈，但若硬件速度再提升一个数量级，将触及 DRAM 及 CPU 总线极限。

### 局限性与开放问题
延迟加密与时间锁谜题、VDF 之间的精确关系仍需进一步刻画。本文的等ogeny 实例化依赖可信设置，尽管分布式方案可缓解信任问题，但其零知识证明基于一个不可证伪的“等ogeny 知识”假设，安全性需更多分析。实现方面，极长的 isogeny 链导致评估密钥存储量巨大（~12 TiB），寻找更紧凑的表示而不牺牲求值效率是一个开放问题。此外，能否构造量子安全的延迟加密（如基于格或编码）是重要的未来方向。

### 强关联论文

[6] Boneh, D., Franklin, M. Identity-based encryption from the Weil pairing. **SIAM J. Comput. 2003** [Google Scholar](https://scholar.google.com/scholar?q=Identity-based+encryption+from+the+Weil+pairing)

[17] De Feo, L., Masson, S., Petit, C., Sanso, A. Verifiable delay functions from supersingular isogenies and pairings. **ASIACRYPT 2019** [Google Scholar](https://scholar.google.com/scholar?q=Verifiable+delay+functions+from+supersingular+isogenies+and+pairings)

[29] Rivest, R.L., Shamir, A., Wagner, D.A. Time-lock puzzles and timed-release crypto. **Technical Report 1996** [Google Scholar](https://scholar.google.com/scholar?q=Time-lock+puzzles+and+timed-release+crypto)

[4] Boneh, D., Bonneau, J., Bünz, B., Fisch, B. Verifiable delay functions. **CRYPTO 2018** [Google Scholar](https://scholar.google.com/scholar?q=Verifiable+delay+functions)

[27] Pietrzak, K. Simple verifiable delay functions. **ITCS 2019** [Google Scholar](https://scholar.google.com/scholar?q=Simple+verifiable+delay+functions)

[34] Wesolowski, B. Efficient verifiable delay functions. **EUROCRYPT 2019** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+verifiable+delay+functions)

[25] Malavolta, G., Thyagarajan, S.A.K. Homomorphic time-lock puzzles and applications. **CRYPTO 2019** [Google Scholar](https://scholar.google.com/scholar?q=Homomorphic+time-lock+puzzles+and+applications)

[28] Renes, J. Computing isogenies between Montgomery curves using the action of (0,0). **PQCrypto 2018** [Google Scholar](https://scholar.google.com/scholar?q=Computing+isogenies+between+Montgomery+curves+using+the+action+of+(0,0))

[13] Costello, C., Longa, P., Naehrig, M. Efficient algorithms for supersingular isogeny Diffie-Hellman. **CRYPTO 2016** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+algorithms+for+supersingular+isogeny+Diffie-Hellman)


## 关键词

+ 延迟加密
+ 超奇异曲线同源映射
+ 可验证延迟函数
+ 基于身份的加密
+ 密封投标拍卖