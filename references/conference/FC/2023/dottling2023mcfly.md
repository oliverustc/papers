---
title: "McFly: verifiable encryption to the future made practical"
doi: 10.1007/978-3-031-47754-6_15
标题简称:
论文类型: conference
会议简称: FC
发表年份: 2023
created: 2025-04-29 10:45:55
modified: 2025-04-29 10:49:13
---
## McFly: verifiable encryption to the future made practical

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-47754-6_15)

## 作者

+ [Nico Döttling](Nico%20D%C3%B6ttling.md)
+ [Lucjan Hanzlik](Lucjan%20Hanzlik.md) 
+ Bernardo Magri 
+ Stella Wohnig 

## 笔记

好的，我将按照您的要求，对论文《McFly: Verifiable Encryption to the Future Made Practical》进行分析，并输出结构化的笔记。

### 背景与动机
在区块链应用中，如密封投标拍卖或防止交易抢先运行，需要将交易内容在链上隐藏一段时间后再公开。传统方案依赖于时间锁谜题或可验证延迟函数等时间锁原语，但这些方法在计算资源上极其浪费，且难以在去中心化系统中（如权益证明区块链）设定统一的、与环境无关的安全参数，因为不同硬件的计算速度差异巨大 [3,15]。同时，权益证明系统逐渐成为主流，它比工作量证明更为环保，但时间锁原语的使用则完全违背了其追求资源高效和环境友好的初衷。因此，需要一种新的、更高效的“向未来加密”机制，它不应依赖计算密集型的时间锁操作，而应充分利用现有区块链基础设施中已存在的计算和信任结构，特别是BFT区块链中委员会为达成共识而频繁执行签名操作的特点。

### 相关工作

[24] Rivest et al. Time-lock puzzles and timed-release crypto. **Technical Report 1996** [Google Scholar](https://scholar.google.com/scholar?q=Time-lock+puzzles+and+timed-release+crypto)
> 核心思路：提出了时间锁谜题的概念，通过计算难题在时间上强制解密延迟，以及依赖可信第三方的思路。
> 局限与区别：计算密集型，参数设定困难，且依赖可信第三方或浪费计算资源。

[13, 14] Cathalo et al. Efficient and non-interactive timed-release encryption. **ICICS 2005** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+and+non-interactive+timed-release+encryption)
> 核心思路：依赖于一个专门的、输出时间令牌的可信服务器来实现定时解密。
> 局限与区别：需要完全信任单一服务器，而McFly复用区块链的去中心化信任结构。

[22] Liu et al. How to build time-lock encryption. **Designs, Codes and Cryptography 2018** [Google Scholar](https://scholar.google.com/scholar?q=How+to+build+time-lock+encryption)
> 核心思路：基于可提取证据加密，将消息加密到未来的区块，未来的区块本身作为解密的证据。
> 局限与区别：可提取证据加密是一种非常昂贵的原语，效率极低，目前仍停留在理论层面。

[12] Campanelli et al. Encryption to the Future: A Paradigm for Sending Secret Messages to Future (Anonymous) Committees. **ePrint 2021** [Google Scholar](https://scholar.google.com/scholar?q=Encryption+to+the+Future:+A+Paradigm+for+Sending+Secret+Messages+to+Future+(Anonymous)+Committees)
> 核心思路：基于PoS区块链，使过去的委员会成员能向未来的中奖者发送消息，需要委员会成员的主动参与。
> 局限与区别：加密者和解密者需要与委员会交互或依赖委员会的主动参与。McFly的加密者和解密者只需读取链上状态，委员会除常规职责外无需额外负担。

[2] Benhamouda et al. Can a public blockchain keep a secret? **TCC 2020** [Google Scholar](https://scholar.google.com/scholar?q=Can+a+public+blockchain+keep+a+secret)
> 核心思路：通过在委员会之间不断重新分享秘密共享，将消息保持秘密状态直至满足特定条件。
> 局限与区别：需要大量的通信交互，距离实用化还很远。

[20] Gentry et al. YOSO: You Only Speak Once. **CRYPTO 2021** [Google Scholar](https://scholar.google.com/scholar?q=YOSO:+You+Only+Speak+Once)
> 核心思路：通过加性同态加密和密钥共享，实现在委员会之间进行安全计算。
> 局限与区别：侧重于安全多方计算，通信复杂，尚未达到实用级别。

[5] Boneh et al. Identity-based encryption from the weil pairing. **CRYPTO 2001** [Google Scholar](https://scholar.google.com/scholar?q=Identity-based+encryption+from+the+weil+pairing)
> 核心思路：提出基于身份的加密（IBE）方案，任何知道某身份的用户均可加密，只有拥有对应私钥的用户才能解密。
> 局限与区别：McFly的SWE可看作是一种阈值IBE，需要多个密钥持有者协作才能解密，更符合去中心化场景。

### 核心技术与方案

本文提出的McFly协议，其核心是名为签名基证据加密（Signature-based Witness Encryption, SWE）的新原语。SWE允许加密者使用一组公钥和一个“标签”对消息进行加密，解密时需要提供针对该标签的、由足够数量私钥持有者生成的聚合签名。

**1. SWE的构造思路**

SWE基于BLS签名和Boneh-Franklin IBE方案 [5, 7]。在BLS方案中，一个签名 $\sigma = H(T)^x$ 可视为对标签 $T$ 的“身份私钥”。受此启发，加密消息 $m$ 的密文 $ct = (g_2^r, e(H(T), vk)^r \cdot g_T^m)$ 可以通过签名 $\sigma$ 解密：计算 $d = c_2 / e(\sigma, c_1)$ 后求离散对数得到 $m$。

为实现阈值（t-out-of-n）解密，SWE引入了Shamir秘密共享 [25]。加密者首先将消息 $m$ 或其一个派生值通过Shamir方案分发给 $n$ 个公钥，每个公钥对应一个份额。解密时，需要收集至少 $t$ 个签名，并将它们通过拉格朗日系数组合成一个聚合签名 $\sigma$。这个聚合过程是协议的关键创新点：$\sigma = \prod_{j=1}^{t} \sigma_{i_j}^{L_{i_j}}$，其中 $L_{i_j}$ 是拉格朗日系数。这使得一个合法的阈值聚合签名能够抵消加密时嵌入的秘密共享，从而恢复消息。

**2. 优化性能**

基础的SWE方案性能差（每密文仅加密1比特，大量配对操作）。McFly进行了三项关键优化：

- **密文批处理**：不对消息 $m$ 本身进行秘密共享，而是对一个随机值 $r_0$ 进行秘密共享。该 $r_0$ 用于同时随机化多个密文分量，使得密文大小从 $O(k \cdot n)$ 降为 $O(k + n)$，其中 $k$ 是消息比特数。
- **源群操作**：将加密操作转移到更快的源群 $\mathbb{G}_2$ 中，而不是目标群 $\mathbb{G}_T$。具体地，将每个份额 $s_i$ 加密为 $c_i = vk_i^r \cdot g_2^{s_i}$。该修改并未依赖更强的安全假设，而是通过精巧的随机自归约归约到标准BDH假设。
- **批量离散对数**：允许消息 $m$ 来自集合 $\{0, \dots, 2^k-1\}$，通过预计算的Baby-Step-Giant-Step算法，以 $O(2^{k/2})$ 次操作高效地计算离散对数，实现多比特消息的打包。

**3. McFly协议**

McFly将SWE与BFT区块链的最终性层结合。其核心思想是“搭便车”：加密者将消息加密到未来某个区块高度，使用的“标签”是该区块高度的哈希值，公钥集是该高度区块的委员会公钥。当该区块被委员会签名并通过最终性机制确认后，该签名（或聚合签名）自然成为解密所需的有效证据。因此，委员会无需为McFly执行任何额外的计算。

**4. 安全与复杂度分析**

SWE的安全性归约到标准BDH假设，在随机预言机模型下证明。McFly的安全性要求SWE安全且哈希函数抗碰撞。SWE的加密复杂度包含 $O(\ell + n)$ 次 $\mathbb{G}_2$ 中的指数运算和 $O(\ell)$ 次配对运算。解密复杂度包含 $O(n)$ 次哈希、$O(t)$ 次 $\mathbb{G}_2$ 指数运算（用于计算拉格朗日系数组合）和 $O(2\ell)$ 次配对运算。加密者无需与委员会交互，只需读取链上公钥。

### 核心公式与流程

**[SWE加密核心公式]**
$$ct = (h, c = g_2^r, c_0 = h^r \cdot g_2^{r_0}, \{c_j = vk_j^r \cdot g_2^{s_j}\}_{j \in [n]}, \{c_i' = e(t_i, g_2^{r_0}) \cdot g_T^{m_i}, a_i, t_i\}_{i \in [\ell]})$$
> 作用：生成一个密文 $ct$，其中 $r_0$ 通过Shamir方案分享为 $s_j$，$r$ 是随机一次性因子，$h$ 是随机群元素，$t_i$ 与标签 $T_i$ 相关。该密文绑定到 $n$ 个公钥和 $\ell$ 个消息。

**[SWE解密核心公式]**
$$c^* = \prod_{j \in I} c_j^{L_j}$$
$$z_i = c_i' \cdot e(\sigma_i, a_i) / e(t_i, c^*)$$
$$m_i' = dlog_{g_T}(z_i)$$
> 作用：解密流程。首先利用阈值签名对应的索引集合 $I$ 和拉格朗日系数 $L_j$，从密文分量 $c_j$ 中重建出 $c^* = g_2^{r_0}$。然后结合标签密文 $t_i$ 和聚合签名 $\sigma_i$ 计算出 $z_i$，最后通过求离散对数恢复消息分量 $m_i'$。

**[改进的BLS聚合签名]**
$$\sigma = \prod_{j=1}^{t} \sigma_{i_j}^{L_{i_j}}$$
> 作用：定义了一种新的聚合签名生成方式，它接收 $t$ 个独立的BLS签名 $\sigma_{i_j}$，每个对应不同的公钥和标签，通过拉格朗日系数 $L_{i_j}$ 将它们组合成一个聚合签名 $\sigma$。这保证了聚合签名能够正确抵消加密时嵌入的秘密共享结构。

**[安全性归约直觉]**
> 作用：SWE的安全性依赖于双线性Diffie-Hellman（BDH）假设。证明中，模拟者可以生成部分公钥并控制相应的签名预言机。当敌手无法获得足够的（阈值数量的）合法签名时，其面临的是一个BDH挑战，无法区分加密的消息是 $m^0$ 还是 $m^1$，从而保证了密文的不可区分性。

### 实验结果

论文对SWE方案进行了实现和基准测试。实验在一台配备 Intel i7 @2.3 GHz 处理器的标准MacBook Pro上进行。加密算法的性能开销非常小，所有参与方的计算负担都极低。用户（加密者和解密者）无需主动维护区块链，也不需要与委员会通信或在链上发布数据。与基于可提取证据加密或时间锁谜题的方案相比，McFly在计算和通信开销上具有数量级上的优势。虽然论文在“核心技术与方案”部分提供了表1分析各群操作的数量，但具体的数值性能评估（如毫秒级的加密/解密时间，特定群组和配对的具体耗时）在完整版本中才有详细列出。实验核心结论是McFly是实用的，其SWE核心部件的运行效率足以支持实际部署。

### 局限性与开放问题
该协议的安全模型假设了诚实多数的委员会，且委员会成员的密钥注册需要提供知识证明（PoK）。此外，基于Baby-Step-Giant-Step的离散对数计算限制了每次可加密的消息比特数，需要权衡密文大小和解密效率。目前的构造依赖于随机预言机模型，设计一个在标准模型下安全的SWE方案是未来的一个开放方向。对于像以太坊2.0这样的动态委员会系统，加密的“地平线”（未来可知的委员会）目前较短（如使用常规验证者委员会仅12.8分钟），如何安全地支持更长的加密深度也是一个值得探索的问题。

### 强关联论文

[5] Boneh D., Franklin M. Identity-based encryption from the weil pairing. **CRYPTO 2001** [Google Scholar](https://scholar.google.com/scholar?q=Identity-based+encryption+from+the+weil+pairing)

[7] Boneh D., Lynn B., Shacham H. Short signatures from the weil pairing. **ASIACRYPT 2001** [Google Scholar](https://scholar.google.com/scholar?q=Short+signatures+from+the+weil+pairing)

[6] Boneh D., Gentry C., Lynn B., Shacham H. Aggregate and verifiably encrypted signatures from bilinear maps. **EUROCRYPT 2003** [Google Scholar](https://scholar.google.com/scholar?q=Aggregate+and+verifiably+encrypted+signatures+from+bilinear+maps)

[25] Shamir A. How to share a secret. **Communications of the ACM 1979** [Google Scholar](https://scholar.google.com/scholar?q=How+to+share+a+secret)

[24] Rivest R.L., Shamir A., Wagner D.A. Time-lock puzzles and timed-release crypto. **Technical Report 1996** [Google Scholar](https://scholar.google.com/scholar?q=Time-lock+puzzles+and+timed-release+crypto)

[22] Liu J., Jager T., Kakvi S.A., Warinschi B. How to build time-lock encryption. **Designs, Codes and Cryptography 2018** [Google Scholar](https://scholar.google.com/scholar?q=How+to+build+time-lock+encryption)

[12] Campanelli M., David B., Khoshakhlagh H., Konring A., Nielsen J.B. Encryption to the Future: A Paradigm for Sending Secret Messages to Future (Anonymous) Committees. **ePrint 2021** [Google Scholar](https://scholar.google.com/scholar?q=Encryption+to+the+Future:+A+Paradigm+for+Sending+Secret+Messages+to+Future+(Anonymous)+Committees)

[2] Benhamouda F., et al. Can a public blockchain keep a secret? **TCC 2020** [Google Scholar](https://scholar.google.com/scholar?q=Can+a+public+blockchain+keep+a+secret)

[20] Gentry C., Halevi S., Krawczyk H., Magri B., Nielsen J.B., Rabin T., Yakoubov S. YOSO: You Only Speak Once. **CRYPTO 2021** [Google Scholar](https://scholar.google.com/scholar?q=YOSO:+You+Only+Speak+Once)

[3] Boneh D., Bonneau J., Bünz B., Fisch B. Verifiable delay functions. **CRYPTO 2018** [Google Scholar](https://scholar.google.com/scholar?q=Verifiable+delay+functions)


## 关键词

+ 未来加密
+ 基于签名的见证加密
+ 阈值多重签名
+ 区块链公平性
+ BFT区块链
+ 时间锁原语