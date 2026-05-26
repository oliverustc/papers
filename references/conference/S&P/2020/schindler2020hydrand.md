---
title: "Hydrand: Efficient continuous distributed randomness"
标题简称:
论文类型: conference
会议简称: S&P
发表年份: 2020
created: 2025-04-28 17:16:05
modified: 2025-04-28 17:17:57
---

## Hydrand: Efficient continuous distributed randomness

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/9152802)

## 作者

+ Philipp Schindler 
+ Aljosha Judmayer 
+ Nicholas Stifter 
+ Edgar Weippl 

## 笔记

### 背景与动机
分布式随机数的可靠生成是密码协议、区块链等系统的基础构件。自 Blum 于 1983 年提出抛币协议 [10] 以来，该问题持续获得关注。随机信标协议旨在定期输出公开可验证、抗偏倚且不可预测的随机数。其应用覆盖选举、彩票、隐私通信及智能合约等领域。许多基于权益证明的区块链方案需要抗操纵的随机性来选举领导者 [33]。现有方案主要分为三类：基于工作量证明或延时证明的方案（如 [17]）伴随高昂计算开销；基于可验证随机函数的方案（如 [22]）无法提供强抗偏倚性；基于公开可验证秘密共享（PVSS）的方案（如 [21, 33]）具有强安全性但通信复杂度高达 $\mathcal{O}(n^3)$，制约了可扩展性。此外，部分方案需要可信初始化或分布式密钥生成，引入了额外安全假设。HydRand 旨在填补 PVSS 类方案在性能与安全性之间的空白，在保持同等安全保证的前提下将通信复杂度降至 $\mathcal{O}(n^2)$。

### 相关工作

[3] Azouvi et al. Winning the caucus race: Continuous leader election via public randomness. **FC 2018** [Google Scholar](https://scholar.google.com/scholar?q=Winning%20the%20caucus%20race%20Continuous%20leader%20election%20via%20public%20randomness)
> 核心思路：在以太坊智能合约上，利用 VRF 和哈希链实现连续领导者选举，输出随机数。
> 局限与区别：不提供强抗偏倚性，最后一轮领导者可影响输出。HydRand 通过 PVSS 和恢复机制保证输出不可操纵。

[17] Bünz et al. Proofs-of-delay and randomness beacons in Ethereum. **IEEE S&B 2017** [Google Scholar](https://scholar.google.com/scholar?q=Proofs-of-delay%20and%20randomness%20beacons%20in%20Ethereum)
> 核心思路：在工作量证明区块哈希上执行顺序延时函数，使输出不可预测。
> 局限与区别：计算开销极高，验证慢。HydRand 以多项式时间计算为代价，提供确定性输出保证。

[22] Chen et al. Algorand. **arXiv 2017** [Google Scholar](https://scholar.google.com/scholar?q=Algorand)
> 核心思路：使用 VRF 选举委员会，通过拜占庭协议达成共识并产生随机数。
> 局限与区别：不提供强抗偏倚性，且协议未分离随机信标，复杂度隐含在共识中。HydRand 是独立信标，提供确定性不可预测性。

[20] Cachin et al. Random oracles in constantinople: Practical asynchronous byzantine agreement using cryptography. **ACM PODC 2000** [Google Scholar](https://scholar.google.com/scholar?q=Random%20oracles%20in%20constantinople%20Practical%20asynchronous%20byzantine%20agreement%20using%20cryptography)
> 核心思路：使用唯一阈值签名，节点对轮次值签名并聚合，输出不可伪造随机数。
> 局限与区别：需要可信初始化分布共享密钥。HydRand 无需任何初始化信任。

[33] Kiayias et al. Ouroboros: A provably secure proof-of-stake blockchain protocol. **CRYPTO 2017** [Google Scholar](https://scholar.google.com/scholar?q=Ouroboros%20A%20provably%20secure%20proof-of-stake%20blockchain%20protocol)
> 核心思路：每个节点使用 PVSS 承诺随机秘密，随后揭示并组合。
> 局限与区别：每轮每个节点广播 PVSS 分享，通信复杂度 $\mathcal{O}(n^3)$。HydRand 每轮仅领导者广播 PVSS 分享，复杂度降至 $\mathcal{O}(n^2)$。

[21] Cascudo et al. Scrape: Scalable randomness attested by public entities. **ACNS 2017** [Google Scholar](https://scholar.google.com/scholar?q=Scrape%20Scalable%20randomness%20attested%20by%20public%20entities)
> 核心思路：对 Schoenmakers PVSS 优化，实现高效分享与重建。
> 局限与区别：原协议仍需所有节点广播 PVSS 分享，通信复杂度 $\mathcal{O}(n^3)$。HydRand 采用其 PVSS 实例，但作为单领导者构建块。

[44] Syta et al. Scalable Bias-Resistant Distributed Randomness. **IEEE S&P 2017** [Google Scholar](https://scholar.google.com/scholar?q=Scalable%20Bias-Resistant%20Distributed%20Randomness)
> 核心思路：RandHound/RandHerd 使用分片和 PVSS，通过集体签名提高可扩展性。
> 局限与区别：RandHerd 需要视图更换和 DKG，且存在非零活度失败概率。HydRand 保证确定性输出，无需 DKG。

[36] Nakamoto. Bitcoin: A peer-to-peer electronic cash system. **2008** [Google Scholar](https://scholar.google.com/scholar?q=Bitcoin%20A%20peer-to-peer%20electronic%20cash%20system)
> 核心思路：区块哈希可作为公共随机源。
> 局限与区别：矿工可选择性丢弃区块从而偏倚输出，不提供抗偏倚。HydRand 通过 PVSS 重建强制输出。

### 核心技术与方案
HydRand 运行于同步模型，假定 $n = 3f + 1$ 个节点，至多 $f$ 个拜占庭故障。每轮 $r$ 分为提议、确认、投票三个阶段，并唯一关联领导者 $\ell_r$。$\ell_r$ 通过上一轮随机值 $R_{r-1}$ 从潜在领导者集合 $\mathcal{L}_r$ 中确定选取。

**数据结构**：领导者提议一个数据集 $D_r$，包含头部和体部。头部包括当前轮索引、随机值 $R_r$、已揭示的秘密值 $s_\ell$、前一个数据集引用、恢复轮次列表以及新 PVSS 承诺的 Merkle 树根。体部包含确认证书 $CC(D_{\overleftarrow{r}})$、中间轮次的恢复证书 $RC(k)$ 以及新承诺 $Com(s_\ell^\star)$。

**协议流程**：
1. **提议阶段**：领导者广播 $D_r$。其他节点验证：秘密值 $s_\ell$ 与上次承诺 $Com(s_\ell)$ 匹配，所有证书有效。
2. **确认阶段**：收到有效 $D_r$ 的节点广播确认消息，转发头部，使领导者无法对同一轮不同数据集签名（防双值）。
3. **投票阶段**：若节点收到有效提议且至少 $2f+1$ 个（对同一数据集哈希的）确认，则广播确认消息 $confirm$。否则广播 $recover$ 消息，附带解密后的 PVSS 分享、相关 Merkle 分支等。
4. **输出**：每个节点要么从领导者发布的头部获知 $s_\ell$，要么从至少 $f+1$ 个恢复消息中重建 $h^{s_\ell}$。最终随机值 $R_r = H(R_{r-1} \mid\mid h^{s_\ell})$。

**领导者选择**：$\ell_r \leftarrow l_{(R_{r-1} \bmod |\mathcal{L}_r|)}$，其中 $\mathcal{L}_r$ 排除了前 $f$ 轮的领导者以及所有已被恢复（即未提供有效数据集）的节点。被恢复节点通过递归函数 $rn(D_x)$ 从可用集 $\mathcal{P}_r$ 中移除。

**通信复杂度**：每轮仅领导者广播一次大小为 $\mathcal{O}(n)$ 的 PVSS 相关性数据集；其余节点的广播均为常数大小。总通信为 $\mathcal{O}(n^2)$。计算复杂度（PVSS 的指数运算）每节点为 $\mathcal{O}(n)$，外部验证者复杂度为 $\mathcal{O}(n)$（仅需验证 $f+1$ 个签名和一个 PVSS 重建）。全验证需 $\mathcal{O}(n)$。

**安全性保证**：
- **活性和输出保证**：每轮至少 $f+1$ 正确节点在潜在领导者集合中；无论领导者是否故障，正确节点总能输出随机数（由重建机制保证）。
- **不可预测性**：在不超过 $f$ 轮的预测中，概率随轮数指数衰减；等待 $f+1$ 轮后，由于至少一个正确领导者被选择，其秘密 $s_\ell$ 在此之前不可知，因此可实现绝对不可预测性。
- **抗偏倚**：任何节点在轮 $r$ 的动作只能影响 $r+f+1$ 轮及之后的输出，而这些轮次的输出在轮 $r$ 时已不可预测，因此无法进行有意义偏倚。
- **公开可验证**：外部验证者可通过获取 $f+1$ 个签名或重建时的 $f+1$ 个分享验证输出正确性。

### 核心公式与流程

**[随机值计算]**
$$
R_{r} \leftarrow H(R_{r-1} \mid\mid h^{s_{\ell}})
$$
> 作用：定义新随机值为前一轮随机值与领导者秘密的哈希。秘密 $s_\ell$ 由领导者揭示或通过 PVSS 重建得到 $h^{s_\ell}$。

**[领导者选择]**
$$
\ell_{r} \leftarrow l_{(R_{r-1} \bmod |\mathcal{L}_{r}|)}
$$
> 作用：基于上一轮输出，从潜在领导者集中确定当前领导者，实现公开可验证的随机选择。

**[恢复节点集合]**
$$
rn(D_{x}) = \left\{ \begin{array}{l l} \emptyset & \text { if } x = 0 \\ \{\ell_{k} \mid RC(k) \in D_{x}\} \cup rn(D_{\overleftarrow{x}}) & \text { otherwise } \end{array} \right.
$$
> 作用：递归定义已被恢复的领导者集合。若某轮领导者在数据集 $D_x$ 中具有恢复证书 $RC(k)$，则其被排除。

**[可用节点集]**
$$
\mathcal{P}_{r} = \mathcal{P} \setminus rn(D_{\overleftarrow{r}})
$$
> 作用：所有未被恢复的节点构成可用节点集。

**[潜在领导者集]**
$$
\mathcal{L}_{r} = \mathcal{P}_{r} \setminus \{\ell_{r - f}, \ell_{r - f + 1},..., \ell_{r - 1} \}
$$
> 作用：从可用节点中排除前 $f$ 轮的领导者，保证至少 $f+1$ 个正确节点可选。

### 实验结果
实现为 Python 原型，部署于 Amazon EC2 t2.micro 实例（1 GB RAM，单核，60-80 Mbps 带宽），实例分布于 8 个 AWS 区域（加拿大、伦敦、爱尔兰等）。测试 $n$ 从 16 到 128，考虑无故障和 $f$ 个模拟故障。吞吐量（每分钟随机数）随 $n$ 增长而降低：n=16 时约 40 bpm，n=128 时约 7.5 bpm。带宽占用：无故障时平均每节点约 110-182 Kbit/s（与 n 近乎常数）；有故障时随 n 线性增长至约 315 Kbit/s（n=128）。外部验证：最坏情况（128 节点）下验证一轮输出需约 57 ms，证明大小约 26 kB。CPU 在 n=128 时逼近 95% 占用，瓶颈为单实例计算能力而非网络。

### 局限性与开放问题
HydRand 假设同步网络模型，若同步保证被暂时违反（如网络分区），可能导致活性失败，需谨慎选取轮时长参数。当前设计将故障节点永久排除，不支持崩溃-恢复，限制了系统鲁棒性。通信复杂度 $\mathcal{O}(n^2)$ 虽优于 $\mathcal{O}(n^3)$，但扩展到极大规模节点（如数千）时仍受限；此时分片或延时证明方案更具优势。未来可扩展至容忍崩溃-恢复故障，以及分析更复杂拜占庭行为下的资源消耗。

### 强关联论文

[21] Cascudo et al. SCRAPE: Scalable Randomness Attested by Public Entities. **ACNS 2017** [Google Scholar](https://scholar.google.com/scholar?q=SCRAPE%20Scalable%20Randomness%20Attested%20by%20Public%20Entities)

[33] Kiayias et al. Ouroboros: A Provably Secure Proof-of-Stake Blockchain Protocol. **CRYPTO 2017** [Google Scholar](https://scholar.google.com/scholar?q=Ouroboros%20A%20Provably%20Secure%20Proof-of-Stake%20Blockchain%20Protocol)

[44] Syta et al. Scalable Bias-Resistant Distributed Randomness. **IEEE S&P 2017** [Google Scholar](https://scholar.google.com/scholar?q=Scalable%20Bias-Resistant%20Distributed%20Randomness)

[22] Chen et al. Algorand. **arXiv 2017** [Google Scholar](https://scholar.google.com/scholar?q=Algorand)

[20] Cachin et al. Random Oracles in Constantinople: Practical Asynchronous Byzantine Agreement Using Cryptography. **ACM PODC 2000** [Google Scholar](https://scholar.google.com/scholar?q=Random%20Oracles%20in%20Constantinople%20Practical%20Asynchronous%20Byzantine%20Agreement%20Using%20Cryptography)

[17] Bünz et al. Proofs-of-Delay and Randomness Beacons in Ethereum. **IEEE S&B 2017** [Google Scholar](https://scholar.google.com/scholar?q=Proofs-of-Delay%20and%20Randomness%20Beacons%20in%20Ethereum)

[3] Azouvi et al. Winning the Caucus Race: Continuous Leader Election via Public Randomness. **FC 2018** [Google Scholar](https://scholar.google.com/scholar?q=Winning%20the%20Caucus%20Race%20Continuous%20Leader%20Election%20via%20Public%20Randomness)

[32] Hanke et al. Dfinity Technology Overview Series Consensus System. **2018** [Google Scholar](https://scholar.google.com/scholar?q=Dfinity%20Technology%20Overview%20Series%20Consensus%20System)

[24] David et al. Ouroboros Praos: An Adaptively-Secure, Semi-Synchronous Proof-of-Stake Protocol. **ePrint 2017** [Google Scholar](https://scholar.google.com/scholar?q=Ouroboros%20Praos%20An%20Adaptively-Secure%20Semi-Synchronous%20Proof-of-Stake%20Protocol)

[43] Schoenmakers. A Simple Publicly Verifiable Secret Sharing Scheme and its Application to Electronic Voting. **CRYPTO 1999** [Google Scholar](https://scholar.google.com/scholar?q=A%20Simple%20Publicly%20Verifiable%20Secret%20Sharing%20Scheme%20and%20its%20Application%20to%20Electronic%20Voting)


## 关键词

+ 随机信标
+ 分布式随机性
+ 可公开验证秘密共享（PVSS）
+ 抗偏差随机性
+ 权益证明区块链
+ 可扩展性优化