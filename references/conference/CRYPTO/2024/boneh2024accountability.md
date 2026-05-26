---
title: "Accountability for misbehavior in threshold decryption via threshold traitor tracing"
标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 2024
---

## Accountability for misbehavior in threshold decryption via threshold traitor tracing

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-68394-7_11)

## 作者

+ [Dan Boneh](Dan%20Boneh.md) 
+ Aditi Partap 
+ Lior Rotem 


## 笔记

### 背景与动机
在 t-out-of-n 阈值解密系统中，任意 t 个参与方可以合作解密一个有效密文，但该系统在面对理性参与方时存在严重安全漏洞：一个敌手可以贿赂一个包含至少 t 个叛徒的群体，这些叛徒能够联合构建一个解码器 D，该解码器输入一个密文即可输出对应的明文。由于现有的阈值解密方案无法从该解码器追溯出创建它的具体叛徒成员，叛徒出售密钥的行为便成为一种无风险的收益。这种缺乏问责性的问题在加密内存池、私人投票和密封拍卖等应用中可能导致系统被完全破坏。本文的工作旨在为阈值解密系统配备追溯能力，即使叛徒以解码器的形式提供解密能力，系统也能通过黑盒访问追踪到至少一个叛徒参与方。

### 相关工作
[14] Boneh, D., Naor, M. Traitor tracing with constant size ciphertext. **ACM CCS 2008** [Google Scholar](https://scholar.google.com/scholar?q=Traitor+tracing+with+constant+size+ciphertext)
> 核心思路：利用指纹编码和公钥加密构造叛徒追踪方案，密文大小为常数。
> 局限与区别：该方案是标准（非阈值）叛徒追踪，假设每个参与方都能独立解密，不适用于需要至少 t 个密钥才能解密的阈值场景。

[6] Billet, O., Phan, D.H. Efficient tracing from collusion secure codes. **ICITS 2008** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+tracing+from+collusion+secure+codes)
> 核心思路：利用指纹编码将任意公钥加密方案转化为叛徒追踪方案。
> 局限与区别：同 [14]，仅在非阈值设定下工作，且不满足阈值解密所需的“双面正确性”条件。

[18] Boneh, D., Sahai, A., Waters, B. Fully collusion resistant traitor tracing with short ciphertexts and private keys. **EUROCRYPT 2006** [Google Scholar](https://scholar.google.com/scholar?q=Fully+collusion+resistant+traitor+tracing+with+short+ciphertexts+and+private+keys)
> 核心思路：提出了私有线性广播加密（PLBE）框架，并基于复合序双线性群构造了首个公钥/密文大小为 O(√n) 的抗合谋叛徒追踪方案。
> 局限与区别：其内部密钥结构依赖于密文方向性，无法直接通过秘密分享来阈值化，因为超过 t 个密钥将破坏密钥间的计算独立性。

[34] Gong, J., Luo, J., Wee, H. Traitor tracing with N^{1/3}-size ciphertexts and O(1)-size keys from k-Lin. **EUROCRYPT 2023** [Google Scholar](https://scholar.google.com/scholar?q=Traitor+tracing+with+N%5E%7B1%2F3%7D-size+ciphertexts+and+O%5E%7B1%7D-size+keys+from+k-Lin)
> 核心思路：基于标准配对假设实现了公钥大小为 O(n^{1/3})、私钥大小为常数的叛徒追踪方案。
> 局限与区别：该方案的技术管道与 PLBE 框架不同，本文在完整版本中展示了如何将其适配到阈值设定，但适配过程需要与传统“阈值化”不同的新技术。

[19] Boneh, D., Shaw, J. Collusion-secure fingerprinting for digital data. **CRYPTO 1995** [Google Scholar](https://scholar.google.com/scholar?q=Collusion-secure+fingerprinting+for+digital+data)
> 核心思路：引入了指纹编码的概念，并给出了首个构造，确保从混合字串中追踪到至少一个原始词。
> 局限与区别：该编码不处理“噪声”（允许 ? 符号）的情况，本文需要的是鲁棒指纹编码，用于处理解码器在某些位置无法确定结果的情况。

[37] Goyal, V., Song, Y., Srinivasan, A. Traceable secret sharing and applications. **CRYPTO 2021** [Google Scholar](https://scholar.google.com/scholar?q=Traceable+secret+sharing+and+applications)
> 核心思路：研究秘密分享中的问责性，考虑少于阈值的合谋者出售重建盒的情况。
> 局限与区别：该模型考虑的是少于阈值的合谋集，并且泄露的是一个重建盒（需要额外份额输入），而本文考虑的是至少 t 个合谋者直接构建一个解码器（只需密文输入），技术路线完全不同。

### 核心技术与方案
本文的核心贡献是定义了阈值解密中的叛徒追踪（TTT-KEM），并给出构造。方案分为两大场景：叛徒数量 f ≥ t（大合谋）和 f < t（小合谋）。

**1. 大合谋场景 (f ≥ t)：基于双部分阈值KEM (BT-KEM) 的构造**
本文首先提出了一个称为 Bipartite Threshold KEM (BT-KEM) 的新原语。BT-KEM 是一种特殊的阈值 KEM，其中存在 ℓ 个位置，每个位置对应一对密钥（左密钥和右密钥）和一对密文（左密文和右密文）。它需同时满足两个看似矛盾的性质：
- **双面正确性**：任何 t 个参与方，无论他们持有的是左密钥还是右密钥，都能成功解密一个密文。
- **单面安全性**：如果一个敌手只持有某个位置上的左密钥（即无法解密右密文部分），则该敌手无法区分一个正常密文和一个右密文被替换为随机值的密文（右方类似）。这是追踪的关键。

基于 BT-KEM 和鲁棒指纹编码，本文提出了 TTT-KEM 构造。具体方案在 Fig. 6 定义。核心思路是为每个位置 j 的指纹编码字 $w^{(i)}$ 的第 j 位决定参与方 i 在该位置是持有左密钥还是右密钥。追踪算法通过对解码器 D 进行特定询问，从 D 的行为中提取一个噪声字 $\bar{w}^*$，然后利用指纹编码的追踪算法 FCTrace 定位叛徒。关键步骤是计算 $a_0 = |p_{001} - p_{100}|$ 和 $a_1 = |p_{001} - p_{111}|$，其中 $p_{b_k b_0 b_1}$ 是使用子程序 TR 统计的 D 输出 1 的频率。通过比较 $a_0$ 和 $a_1$ 与阈值 B 的关系来决定 $\bar{w}^*$ 的每一位。安全性证明式 4.4 通过混合论证将追踪安全性归约到 BT-KEM 的单面安全性。

**2. BT-KEM 的实例化**
本文给出了两个高效的 BT-KEM 构造：
- **基于 DDH 的构造（Fig. 7）**：使用了 Shamir 秘密共享。公钥包含 ℓ 个三元组 $(X_j = g^{x_j}, Y_j = g^{y_j}, Z_j = g^{z_j})$。左密钥 $sk_{i,0}^{(j)} = s_{j,i}/y_j$，右密钥 $sk_{i,1}^{(j)} = s_{j,i}/z_j$，其中 $s_{j,i}$ 是 $x_j$ 的一个份额。密文为 $(c_0 = Y_j^r, c_1 = Z_j^r)$，密钥 $k = X_j^r$。解密时，若参与方持有左密钥，则计算 $d_i = c_0^{sk_{i,0}^{(j)}} = (g^{y_j r})^{s_{j,i}/y_j} = g^{s_{j,i} r}$。组合时使用拉格朗日插值恢复 $k$。
- **基于 Pairing 的构造（Fig. 8）**：使用了 ElGamal 加密和配对。公钥仅包含三个群元素 $(X = g_1^{\alpha y z}, Y = g_1^y, Z = g_1^z)$。左密钥为 $(H_1(j)^{z s_i}, g_2^{z s_i})$，右密钥为 $(H_1(j)^{y s_i}, g_2^{y s_i})$，其中 $s_i$ 是 $\alpha$ 的一个份额。密文为 $(c_0 = (u_0 = g_2^{t_0}, v_0 = Y^r H_1(j)^{t_0}), c_1 = (u_1 = g_2^{t_1}, v_1 = Z^r H_1(j)^{t_1}))$，密钥 $k = H_2(e(X, g_2)^r)$。解密时利用配对消除随机数，恢复 $d_i = e(g_1, g_2)^{s_i y z r}$。

**3. 小合谋场景 (f < t)**
对于少于阈值的叛徒合谋，本文证明了当解码器是精确型（只接受恰好 $t-f$ 个份额）时，追踪是不可能的（定理 6.1）。作为替代，本文提出了两种方案：
- **通用解码器**：如果解码器只要获得足够信息就必然解密，则可以通过穷举法“排除”无辜者，找到叛徒。
- **确认算法**：对于精确解码器，本文设计了一个确认算法，它可以输出一个证明，说服验证者一个特定的集合是叛徒集合。该算法防止了举报框架，并通过额外的检查（如替换集合中的份额）来防御敌手虚报叛徒数量。

### 核心公式与流程

**[大合谋方案的关键追踪统计量]**
$$
a_0 = | p_{001} - p_{100} |, \quad a_1 = | p_{001} - p_{111} |
$$
> 作用：用于从解码器 D 的行为中提取指纹字 $\bar{w}^*$ 的第 j 位。$p_{b_k b_0 b_1}$ 是 D 在特定查询下输出 1 的频率。

**[BT-KEM 基于 DDH 的构造核心操作]**
$$
\text{解密: } d_i = c_b^{sk_{i,b}^{(j)}} = (Y_j^r)^{s_{j,i}/y_j} = g^{s_{j,i} r} \quad (\text{当 } b=0)
$$
$$
\text{组合: } k = \prod_{i \in \mathcal{I}} d_i^{\lambda_i^{\mathcal{I}}} = g^{r \cdot \sum_{i \in \mathcal{I}} \lambda_i^{\mathcal{I}} s_{j,i}} = g^{x_j r} = X_j^r
$$
> 作用：展示了 DDH 构造中，无论参与方使用左密钥还是右密钥，解密后都能得到正确的密钥 $k$。

**[BT-KEM 基于 Pairing 的构造核心操作]**
$$
\text{解密: } d_i = e(v, k_1) / e(k_0, u) = e(g_1, g_2)^{s_i y z r}
$$
$$
\text{组合: } W = \prod_{i \in \mathcal{I}} d_i^{\lambda_i^{\mathcal{I}}}, \quad k = H_2(W)
$$
> 作用：展示了配对构造中，解密步骤利用配对运算消除了随机数 $t_b$ 和 $r$，恢复出与参与方份额 $s_i$ 相关的配对值，最终通过拉格朗日插值恢复并哈希得到密钥。

### 实验结果
论文属于理论密码学贡献，未提供任何实验评估。其构造的渐进复杂度已在理论部分给出：基于 DDH 的 BT-KEM 具有常数大小密文（两个群元素），但公钥大小为 O(ℓ)，ℓ 与参与方数量 n 和追踪精度有关。基于 Pairing 的 BT-KEM 进一步将公钥也优化为常数大小（三个群元素）。从参数看，这些构造对于参与方数量 n 在几百以内、且对密文和公钥大小有严格要求的应用（如基于智能合约的加密内存池）尤为适用。与直接使用（非阈值）叛徒追踪方案不同，本文方案的代价是引入了 BT-KEM 甚至指纹编码带来的额外参数开销，但实现了阈值解密这一核心功能。

### 局限性与开放问题
本文首次提出了阈值解密中的叛徒追踪概念，但仍存在若干开放问题。首先，当前构造仅保证追踪到至少一个叛徒，而非全部 t 个，设计能同时检测出所有叛徒的高效方案是一个自然延伸。其次，将其他更高效的叛徒追踪方案（如基于 PLBE 或 Zhandry 方案）适配到阈值设置需要全新的技术，目前尚未解决。最后，本文方案仅支持私有追踪（需要秘密的追踪密钥），设计一个公开可追踪且不牺牲安全性的方案是未来的一个挑战。此外，在小于阈值场景下，对于解码器只对极少数特定集合生效的最坏情况，追踪被证明是不可能的，这构成了一个根本性的限制。

### 强关联论文
[14] Boneh, D., Naor, M. Traitor tracing with constant size ciphertext. **ACM CCS 2008** [Google Scholar](https://scholar.google.com/scholar?q=Traitor+tracing+with+constant+size+ciphertext)
[6] Billet, O., Phan, D.H. Efficient tracing from collusion secure codes. **ICITS 2008** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+tracing+from+collusion+secure+codes)
[18] Boneh, D., Sahai, A., Waters, B. Fully collusion resistant traitor tracing with short ciphertexts and private keys. **EUROCRYPT 2006** [Google Scholar](https://scholar.google.com/scholar?q=Fully+collusion+resistant+traitor+tracing+with+short+ciphertexts+and+private+keys)
[34] Gong, J., Luo, J., Wee, H. Traitor tracing with N^{1/3}-size ciphertexts and O(1)-size keys from k-Lin. **EUROCRYPT 2023** [Google Scholar](https://scholar.google.com/scholar?q=Traitor+tracing+with+N%5E%7B1%2F3%7D-size+ciphertexts+and+O%5E%7B1%7D-size+keys+from+k-Lin)
[19] Boneh, D., Shaw, J. Collusion-secure fingerprinting for digital data. **CRYPTO 1995** [Google Scholar](https://scholar.google.com/scholar?q=Collusion-secure+fingerprinting+for+digital+data)
[58] Tardos, G. Optimal probabilistic fingerprint codes. **J. ACM 2008** [Google Scholar](https://scholar.google.com/scholar?q=Optimal+probabilistic+fingerprint+codes)
[37] Goyal, V., Song, Y., Srinivasan, A. Traceable secret sharing and applications. **CRYPTO 2021** [Google Scholar](https://scholar.google.com/scholar?q=Traceable+secret+sharing+and+applications)
[17] Boneh, D., Partap, A., Rotem, L. Traceable secret sharing: strong security and efficient constructions. **CRYPTO 2024** [Google Scholar](https://scholar.google.com/scholar?q=Traceable+secret+sharing%3A+strong+security+and+efficient+constructions)
[61] Zhandry, M. New techniques for traitor tracing: size N^{1/3} and more from pairings. **CRYPTO 2020** [Google Scholar](https://scholar.google.com/scholar?q=New+techniques+for+traitor+tracing%3A+size+N%5E%7B1%2F3%7D+and+more+from+pairings)


## 关键词

+ 密码学
+ 零知识
+ 协议