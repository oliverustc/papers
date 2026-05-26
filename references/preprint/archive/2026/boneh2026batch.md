---
title: "Efficient Batch Threshold Encryption Using Partial Fraction Techniques"
标题简称:
论文类型: preprint
预印本简称: archive
发表年份: 2026
---

## Efficient Batch Threshold Encryption Using Partial Fraction Techniques

## 发表信息

+ [原文链接](https://eprint.iacr.org/2026/674)

## 作者

+ [Dan Boneh](Dan Boneh.md)
+ Rohit Nema
+ [Arnab Roy](Arnab%20Roy.md)
+ Ertem Nusret Tas

## 笔记

### 背景与动机
批量加密允许密钥持有者为选定的密文集发布一个简洁的预解密密钥，从而在保持其他密文保密的同时解密该集合。现有方案要么依赖epoch，限制了每次只能发布一个预解密密钥；要么是无epoch的，但存在公共参数庞大、易受审查攻击的问题。例如，BEAT-MEV [14] 虽然实现了无epoch，但其索引依赖的设计使得攻击者可以通过提交多个共享相同索引的密文来排除目标交易，导致指数级的审查成本。此外，其公共参数规模随索引空间线性增长。本文旨在填补空白，设计一个同时满足无epoch、抗审查、线性公共参数、常数大小预解密密钥和密文的高效方案。

### 相关工作

[14] Bormet et al. BEAT-MEV: epochless approach to batched threshold encryption for MEV prevention. **USENIX Security Symposium 2025** [Google Scholar](https://scholar.google.com/scholar?q=BEAT-MEV+epochless+approach+to+batched+threshold+encryption+for+MEV+prevention)
> 核心思路：基于可穿刺密钥同态PRF构建无epoch批量加密，预解密密钥大小恒定为|G1|。
> 局限与区别：索引依赖，审查攻击成本低下；公共参数大小至少与索引空间线性，且为O(ℓ²)；本文通过部分分式技术实现索引独立且公共参数O(ℓ)。

[16] Choudhuri et al. Mempool privacy via batched threshold encryption: Attacks and defenses. **USENIX Security Symposium 2024** [Google Scholar](https://scholar.google.com/scholar?q=Mempool+privacy+via+batched+threshold+encryption+Attacks+and+defenses)
> 核心思路：首次形式化批量加密，提出基于身份加密（IBE）的epoch方案。
> 局限与区别：依赖epoch，每次需运行新设置；后续工作[30,5,17]虽减少为一次设置，但仍允许每epoch一个密钥；本文移除epoch并实现抗审查。

[24] Jutla et al. Partial fraction techniques for cryptography. **Cryptology ePrint Archive 2025** [Google Scholar](https://scholar.google.com/scholar?q=Partial+fraction+techniques+for+cryptography)
> 核心思路：利用有理函数的部分分式分解构造高效阈值加密。
> 局限与区别：该技术仅用于阈值加密；本文将其扩展并应用于批量加密，实现索引独立和更简洁的密钥。

[22] Gong et al. Threshold batched identity-based encryption from pairings in the plain model. **Cryptology ePrint Archive 2025** [Google Scholar](https://scholar.google.com/scholar?q=Threshold+batched+identity-based+encryption+from+pairings+in+the+plain+model)
> 核心思路：在普通模型中基于q型假设获得首个选择性安全的批量IBE。
> 局限与区别：仍依赖epoch；公共参数至少为O(ℓ)且包含多个群元素；本文在AGM+ROM中获得CCA安全，且预解密密钥更小。

[20] Fernando et al. TrX: Encrypted mempools in high performance BFT protocols. **Cryptology ePrint Archive 2025** [Google Scholar](https://scholar.google.com/scholar?q=TrX+Encrypted+mempools+in+high+performance+BFT+protocols)
> 核心思路：基于批量IBE（[17]变体）实现首个加密mempool，减少密文大小并解决epoch限制但公共参数与批次数线性。
> 局限与区别：公共参数随批次数κ增长；本文无需预知批次数，公共参数仅与最大批次ℓ线性。

[13] Bormet et al. BEAST-MEV: Batched threshold encryption with silent setup for MEV prevention. **Cryptology ePrint Archive 2025** [Google Scholar](https://scholar.google.com/scholar?q=BEAST-MEV+Batched+threshold+encryption+with+silent+setup+for+MEV+prevention)
> 核心思路：改进BEAT-MEV，实现静默设置和CCA安全性。
> 局限与区别：仍为索引依赖公共参数O(ℓ)；本文实现索引独立且密文更短。

### 核心技术与方案

本文整体框架基于部分分式分解技术，该技术最初来自Jutla等人在阈值加密方案[24]中的工作。方案主要由四个模块构成：系统设置、加密、预解密生成、解密，并额外使用一个模拟可提取的非交互零知识证明（SE-NIZK）来实现CCA安全。

**1. 构造思路与关键步骤**  
设$F$为大小为素数$p$的有限域，定义线性分数$p_i(X)=1/(X+i)$。在Setup中，随机选取$x \in \mathbb{Z}_p$，输出加密密钥$\mathsf{ek} = ( \sum_{i=-1}^\ell [p_i(x)]_1, [p_0(x)]_1 )$，解密密钥$\mathsf{dk} = ([p_i(x)]_2)_{i\in[\ell]}$，秘密密钥$\mathsf{sk}=x$。加密时，选取随机数$r$，生成密文$\mathsf{ct}=([r]_1, r\cdot\mathsf{ek}[1], r\cdot e(\mathsf{ek}[2],[1]_2)+m)$，并附上一个针对关系$\mathcal{R}_{\mathsf{ek}[1]}$的SE-NIZK证明。预解密算法使用$\mathsf{sk}=x$计算$\mathsf{sbk} = \sum_{i\in[\ell]} p_i(x) \cdot \mathsf{ct}_i[1]$，即单个$\mathbb{G}_1$元素。解密时，对于每个$j\in[\ell]$，通过配对运算和部分分式分解（Lemma 1）消去干扰项，最终求解出$r_j\cdot[p_0(x)]_T$，从而恢复消息。

**2. 部分分式分解的核心作用**  
Lemma 1指出：乘积$p_i(X)p_j(X)$（$i\neq j$）可分解为$\frac{1}{j-i}(p_i(X)-p_j(X))$。这一性质使得预解密密钥$\mathsf{sbk}$与$[p_j(x)]_2$配对时产生的二次项$r_j q_j(x)$（其中$q_j(x)=1/(x+j)^2$）得以被其他线性项组合消去，最终仅留下与$p_{-1}(x)$和$p_0(x$ 相关的项，从而可通过两个线性方程解得$r_j\cdot [p_0(x)]_T$。

**3. 正确性与安全性直觉**  
正确性基于NIZK的完备性和上述代数恒等式。安全性（B-IND-CCA）证明依赖一个新颖的静态q型假设——静态决策性双线性秩亏Diffie-Hellman假设（q-StatRankDef，Assumption 1），并利用SE-NIZK的模拟可提取性和零知识性质。证明中，归约算法将敌手的攻击转换为区分两个分布：真实加密分布与随机分布，并通过模拟证明和提取器处理预解密查询。整个归约在代数群模型（AGM）和随机预言机模型（ROM）中完成。

**4. 索引无关性与阈值的实现**  
索引无关性通过将每个索引$i$视为阈值加密方案中的一个“方”，并关联一个“公钥”$[p_i(x)]_1$和“密钥”$[p_i(x)]_2$实现。阈值化通过Shamir秘密共享完成：将每个$p_i(x)$进行$t$-of-$N$秘密分享，每个参与方持有份额$(s_j^i)_{i\in[\ell]}$，生成预解密密钥份额$\mathsf{sbk}_j = \sum_{i\in[\ell]} s_j^i \cdot \mathsf{ct}_i[1]$，然后通过拉格朗日系数组合得到完整的$\mathsf{sbk}$。这样每个参与方的秘密密钥大小为$O(\ell)$（$\ell$个域元素），但预解密密钥份额仅为单个$\mathbb{G}_1$元素，通信复杂度$O(N)$。

**5. 摊销计算与FFT优化**  
解密时，为了计算形如$\sum_{i\neq j} \frac{1}{j-i} \mathsf{ct}_i[1]$的多标量乘法，可将索引替换为2ℓ次单位根$\{\omega,\ldots,\omega^\ell\}$，利用快速傅里叶变换（FFT）在$O(\ell\log\ell)$次群操作内完成所有ℓ个密文的计算。同样对$\mathbb{G}_T$中的项也可作类似优化。这样，每个密文仅需常数个配对运算（构造1中摊销5个，构造5中摊销4个）。

**6. 缩短密文的变体**  
在Section 5中，通过将解密密钥扩展$(2\ell+1)$个$\mathbb{G}_2$元素，可以移除密文的第二个$\mathbb{G}_1$分量，使密文大小降至$|\mathbb{G}_1|+|\mathbb{G}_T|$。其安全性依赖于另一个q型假设——q-QuadRankDef（Assumption 2），该假设在GBGM中证明成立。此变体的解密运算更少，但公共参数稍大。

### 核心公式与流程

**[部分分式分解 Lemma 1]**
$$
\left(\sum_{i=1}^n \frac{c_i}{X+a_i} + \sum_{i=1}^n \frac{c_i}{b_j-a_i}\right) \cdot \frac{1}{X+b_j} = \sum_{i=1}^n \frac{c_i}{b_j-a_i} \cdot \frac{1}{X+a_i}
$$
> 用于将有理函数乘积分解为线性组合，是解密中消去交叉项的基础。

**[Batch Encryption 构造（Construction 1）的加密公式]**
$$
\mathsf{ct} := \big([r]_1,\; r\cdot \sum_{i=-1}^\ell [p_i(x)]_1,\; r\cdot e([p_0(x)]_1,[1]_2) + m\big)
$$
> 密文包含三个分量：随机数的群表示、用线性分数和加密的“掩码”部分、用$p_0(x)$加密消息。

**[解密中间量 $L_{j,1}$ 的化简结果]**
$$
L_{j,1} = \frac{1}{j+1}[r_j p_{-1}(x)]_T + \frac{1}{j}[r_j p_0(x)]_T
$$
> 通过配对和部分分式消除后，$L_{j,1}$仅包含与$p_{-1}$和$p_0$相关的项。

**[求解消息的最终公式]**
$$
R := j\big((j+1)L_{j,1} - L_{j,2}\big),\quad m_j := \mathsf{ct}_j[3] - R
$$
> 利用两个线性无关方程解得$r_j\cdot [p_0(x)]_T$，从而恢复消息。

**[缩短密文变体的解密计算]**
$$
\begin{aligned}
L_{j,1} &:= e(\mathsf{ct}_j[1],[w_j(x)]_2) - e\Big(\mathsf{sbk} + \sum_{\substack{i\neq j}}\frac{1}{j-i}\mathsf{ct}_i[1], [p_j(x)]_2\Big) + \sum_{\substack{i\neq j}}\frac{1}{j-i}\mathsf{tm}_i \\
L_{j,2} &:= e(\mathsf{ct}_j[1],[p_{-1}(x)+p_0(x)]_2)
\end{aligned}
$$
> 变体中密文仅含$[r]_1$和$r\cdot e([p_0]_1,[1]_2)+m$，解密时直接使用预计算的群元素计算$L_{j,1}$和$L_{j,2}$。

### 实验结果

实验使用Rust语言结合arkworks库在Apple M4 Pro处理器（12核，24GB统一内存）上单线程运行，选择BLS12-381曲线实现。表2列出了批量大小ℓ分别为4、16、64、128、256、512时的平均运行时间。对于基本构造（Construction 1），加密时间恒定约599 μs，预解密时间从ℓ=4时的1.53 ms增长到ℓ=512时的54.3 ms，解密时间从19.2 ms增长到5.12 s。缩短密文构造（Construction 5）加密更快（437 μs），预解密时间略低（0.82 ms到50.1 ms），解密时间约降低1.6倍（15.3 ms到3.61 s）。结果表明即使未优化的原型，方案在实际批次规模下也已实用，且随着ℓ增大，FFT优化的摊销效果使总解密时间近似$O(\ell\log\ell)$。对比现有方案如BEAT-MEV，本文在公共参数大小、密文尺寸和预解密密钥大小上均具优势，同时提供索引无关和抗审查性质。

### 局限性与开放问题

本文仍存在一些局限：安全性证明在AGM+ROM中完成，未达到标准模型；NIZK的模拟可提取性依赖于AGM，若使用Fischlin变换可在ROM中实现但会增加证明大小；阈值化方案中每个参与方的秘密密钥大小为$O(\ell)$，对于极大ℓ可能成为存储瓶颈。此外，批次大小ℓ需在Setup时固定，不支持动态加入新索引。未来工作可探索标准模型下的构造、秘密密钥更小的阈值方案，以及自适应安全的batch threshold encryption。

### 强关联论文

[24] Jutla, Nema, Roy. Partial fraction techniques for cryptography. **Cryptology ePrint Archive 2025**

[14] Bormet et al. BEAT-MEV: epochless approach to batched threshold encryption for MEV prevention. **USENIX Security Symposium 2025**

[16] Choudhuri et al. Mempool privacy via batched threshold encryption: Attacks and defenses. **USENIX Security Symposium 2024**

[30] Suegami, Ashizawa, Shibano. Constant-cost batched partial decryption in threshold encryption. **Cryptology ePrint Archive 2024**

[5] Agarwal, Fernando, Pinkas. Efficiently-thresholdizable batched identity based encryption, with applications. **CRYPTO 2025**

[17] Choudhuri et al. Practical mempool privacy via one-time setup batched threshold encryption. **USENIX Security Symposium 2025**

[13] Bormet et al. BEAST-MEV: Batched threshold encryption with silent setup for MEV prevention. **Cryptology ePrint Archive 2025**

[22] Gong et al. Threshold batched identity-based encryption from pairings in the plain model. **Cryptology ePrint Archive 2025**

[20] Fernando et al. TrX: Encrypted mempools in high performance BFT protocols. **Cryptology ePrint Archive 2025**

[3] Agarwal et al. Weighted batched threshold encryption with applications to mempool privacy. **Cryptology ePrint Archive 2025**


## 关键词

+ 批量加密无纪元抗审查方案
+ 部分分式分解预解密密钥批量解密
+ CCA安全门限批量加密
+ 加密内存池MEV缓解应用
+ 线性公共参数常数密文大小
