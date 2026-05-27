---
title: "Ligero: Lightweight Sublinear Arguments Without a Trusted Setup"
doi: 10.1145/3133956.3134104
标题简称: Ligero
论文类型: conference
会议简称: CCS
发表年份: 2017
modified: 2025-04-08 17:13:15
---
## Ligero: Lightweight Sublinear Arguments Without a Trusted Setup

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3133956.3134104)

## 作者

+ Scott Ames
+ [Carmit Hazay](Carmit%20Hazay.md)
+ [Yuval Ishai](Yuval%20Ishai.md)
+ [Muthuramakrishnan Venkitasubramaniam](Muthuramakrishnan%20Venkitasubramaniam.md)
## 笔记

### 背景与动机
可验证外包计算是密码学核心问题之一，其挑战在于证明方有动机谎报计算结果，而验证方希望在不重现整个计算的前提下确信结论正确。传统的zk-SNARKs虽然通信极短，但依赖结构化公共参考串，该参考串要么需要可信设置，要么通过昂贵分布式协议生成，这成为实际部署的瓶颈。同时基于PCP的方案虽然理论上优美，但实际实现复杂度高，远未达到有竞争力的具体效率。基于线性PCP的方案则严重依赖同态公钥密码学，导致证明方计算极慢。本文的目标是同时实现三个理想特征：无需任何可信设置、不依赖复杂PCP机制和昂贵公钥运算，同时获得具体高效的亚线性通信。作者通过将特定的轻量级安全多方计算协议与改进的IKOS变换相结合，实现了这一目标，最终获得的协议通信复杂度与验证电路规模的平方根成正比。

### 相关工作

[29] Ishai等. Zero-knowledge proofs from secure multiparty computation. **STOC 2007** [Google Scholar](https://scholar.google.com/scholar?q=Zero-knowledge+proofs+from+secure+multiparty+computation+Ishai+Kushilevitz+Ostrovsky+Sahai)
> 核心思路：提出了从任意容忍诚实验收者多数的MPC协议到零知识交互式PCP的一般性变换（IKOS变换）。
> 局限与区别：原始变换的通信复杂度较大，无法直接获得亚线性通信；本文通过限制MPC网络拓扑结构，优化了变换中的通信与安全权衡。

[32] Ishai等. Founding cryptography on oblivious transfer - efficiently. **CRYPTO 2008** [Google Scholar](https://scholar.google.com/scholar?q=Founding+cryptography+on+oblivious+transfer+%E2%80%94+efficiently+Ishai+Prabhakaran+Sahai)
> 核心思路：提出了IPS编译器，利用“监查员机制”在恶意模型下构造安全计算协议。
> 局限与区别：本工作中所用的具体MPC协议及变换思路受到了IPS编译器中思路的启发，但本文将其优化为适用于ZKIPCP的特定形式。

[36] Kilian. A note on efficient zero-knowledge proofs and arguments. **STOC 1992** [Google Scholar](https://scholar.google.com/scholar?q=A+note+on+efficient+zero-knowledge+proofs+and+arguments+Kilian)
> 核心思路：首次展示了如何使用PCP和Merkle树构造通信亚线性的交互式论证系统。
> 局限与区别：Kilian协议依赖于经典PCP，其实例化复杂度极高；本文通过MPC-in-the-head技术避免了复杂PCP构造。

[22] Giacomelli等. ZKBoo: Faster zero-knowledge for boolean circuits. **USENIX Security 2016** [Google Scholar](https://scholar.google.com/scholar?q=ZKBoo+Faster+zero-knowledge+for+boolean+circuits+Giacomelli+Madsen+Orlandi)
> 核心思路：展示了IKOS变换的实际可行性，实现了具体高效的零知识论证。
> 局限与区别：ZKBoo的通信复杂度与电路规模成线性关系，对于大电路通信代价巨大，本文实现亚线性通信。

[13] Chase等. Post-quantum zero-knowledge and signatures from symmetric-key primitives. **CCS 2017** [Google Scholar](https://scholar.google.com/scholar?q=Post-quantum+zero-knowledge+and+signatures+from+symmetric-key+primitives+Chase+Derler+Goldfeder+Orlandi+Ramacher+Rechberger+Slamanig+Zaverucha)
> 核心思路：提出了ZKB++，对ZKBoo进行了效率优化。
> 局限与区别：ZKB++同样存在通信与电路规模成比例的问题；本文在SHA-256基准测试中通信仅为ZKB++的1/4左右。

[19] Fiat和Shamir. How to prove yourself: Practical solutions to identification and signature problems. **CRYPTO 1986** [Google Scholar](https://scholar.google.com/scholar?q=How+to+prove+yourself+Practical+solutions+to+identification+and+signature+problems+Fiat+Shamir)
> 核心思路：提出了将交互式公开币协议转换为非交互式协议的通用变换（Fiat-Shamir变换）。
> 局限与区别：本文将其应用于ZKIPCP协议，在随机谕言模型中获得了无需可信设置的非交互式zk-SNARKs。

[5] Ben-Sasson等. Scalable, transparent, and post-quantum secure computational integrity. **Manuscript 2017** [Google Scholar](https://scholar.google.com/scholar?q=Scalable+transparent+and+post-quantum+secure+computational+integrity+Ben-Sasson+Bentov+Horesh+Riabzev)
> 核心思路：提出了zk-STARKs，使用不同技术获得了透明的证明系统。
> 局限与区别：zk-STARKs的大电路证明尺寸更优且验证更快，但本文在小到中等电路上证明方计算时间和证明尺寸更有优势。

[35] Kalai和Raz. Interactive PCP. **ICALP 2008** [Google Scholar](https://scholar.google.com/scholar?q=Interactive+PCP+Kalai+Raz)
> 核心思路：结合了交互式的证明和经典PCP模型，提出了交互式PCP概念。
> 局限与区别：本文使用的ZKIPCP模型是其特例，进一步在具体效率上实现了突破。

[16] Damgård和Ishai. Scalable secure multiparty computation. **CRYPTO 2006** [Google Scholar](https://scholar.google.com/scholar?q=Scalable+secure+multiparty+computation+Damg%C3%A5rd+Ishai)
> 核心思路：提出了一个通信复杂度与电路规模成比例、与参与方数量无关的高效安全多方计算协议。
> 局限与区别：本文正是利用该协议的优化变体作为MPC组件，其总通信复杂度仅与电路规模成比例，当参与方数设为电路规模的平方根时，每方通信降至电路规模的平方根。

[39] Micali. CS Proofs. **FOCS 1994** [Google Scholar](https://scholar.google.com/scholar?q=CS+Proofs+Micali)
> 核心思路：将PCP与Merkle树及随机谕言结合，首次构造了非交互式论证系统。
> 局限与区别：Micali的构造同样依赖经典PCP实例化，本文通过MPC-in-the-head的替代途径获得了更好的具体效率。

### 核心技术与方案

**整体框架**：本文方案的核心逻辑链分为三个层次。首先，确定一个特定的MPC模型，该模型仅包含一个发送者、n个服务器和一个接收者，通信被严格限制：发送者向服务器发送初始消息，服务器进行两阶段本地计算（期间接收公共随机串），最后各服务器向接收者发送单条消息，服务器之间无任何通信。这种受限拓扑是实现亚线性通信的关键。然后，利用该MPC模型的优化协议实例化为一个零知识交互式PCP。最后，通过Merkle树和碰撞 resistant 哈希函数将ZKIPCP编译为标准的交互式论证，并可进一步通过Fiat-Shamir变换转化为非交互式版本。

**从MPC到ZKIPCP的变换**：给定一个NP关系R，证明者P通过在脑中模拟MPC协议生成一个预言机π，该预言机包含各服务器在协议第一阶段结束时的视图。交互协议具体步骤为：验证者V发送一个随机挑战r（对应于MPC协议中服务器接收的公共随机串），证明者P发送接收者R的视图作为响应，然后V随机选取t_p个服务器的索引构成查询集Q，从预言机中获取这些服务器的视图，最后V检查所有查询到的服务器视图与接收者R的视图是否一致。协议的完备性直接由MPC的正确性保证。可靠性证明的核心是识别一个不一致图G：将n个服务器和接收者视为节点，若某服务器视图与接收者视图不一致则连边。若图中边数超过阈值t_r，则V有概率$(1 - t_r/n)^{t_p}$查询到不一致边而拒绝；若边数小于t_r，则通过归约到底层MPC协议的t_r-鲁棒性，证明V接受假命题的概率至多为δ(κ)。零知识性则由MPC协议的t_p-隐私性保证，因为V仅获取t_p个服务器视图和一个线性组合，通过模拟器可完美模拟这些视图的分布。通信复杂度为$t_p \cdot v_{size} + v_R$，其中$v_{size}$为服务器视图大小，$v_R$为接收者视图大小，通过参数调整使两项相近时达到最优。

**直接的ZKIPCP构造**：论文给出了一个自包含的构造，采用交错Reed-Solomon码。基本想法是将电路门值排列为$m \times \ell$矩阵，其中$m \cdot \ell > n_i + s$（s为门数），并对每一行用RS码编码。协议包含三个关键子测试：（1）交错码成员测试（Test-Interleaved），验证者发出随机线性组合r，检查返回的$w = r^T U$是否属于码字L，并验证在随机查询集Q上的一致性；（2）线性约束测试（Test-Linear-Constraints-IRS），用于检验加法门的正确性，验证者发送随机向量r，检查编码消息是否满足线性方程$Ax = b$；（3）二次约束测试（Test-Quadratic-Constraints-IRS），用于检验乘法门$a \cdot b = c$是否正确。这些测试的可靠性分析基于一个关键引理：若预言机U距交错码$L^m$的最小距离超过e（e < d/4，d为码的最小距离），则随机线性组合$w^* = r^T U^*$距码L的距离不超过e的概率至多为$(e+1)/|\mathbb{F}|$。最终协议的复杂度为：通信包含一个交错码测试、四个线性约束测试和一个二次约束测试，总计$n + 4 \cdot (k+\ell-1) + (2k-1)$个域元素。

**零知识性的实现**：通过两个修改实现ZK。（1）每个编码行添加随机盲化码字$u'$，使验证者获得的线性组合$w = r^T U + u'$隐藏了U的信息，但零知识性需要$r' \neq 0$或固定为1（此时需要细微调整可靠性分析）。（2）对线性约束和二次约束测试加入额外随机行$u_h$，这些行需要保证其编码消息满足特定线性约束（如消息元素之和为零），从而在不影响可靠性的前提下隐藏原始消息。最终协议在满足$k > \ell + t$时达到完美诚实验证者零知识。

**从ZKIPCP到论证系统**：使用Merkle哈希树对预言机每个条目进行承诺，将交互式ZKIPCP编译为碰撞 resistant 哈希函数下的交互式论证。交互式版本的通信复杂度包括ZKIPCP的原始通信加上Merkle树根和打开路径的哈希值。非交互式版本通过随机谕言模型模拟验证者消息（Fiat-Shamir变换）实现，其可靠性损失为$T \cdot \epsilon(x) + 3(T^2+1) \cdot 2^{-\lambda}$，其中T是查询次数，λ是输出长度。

### 核心公式与流程

**[交错码成员测试 - Test-Interleaved]**
$$w = r^T U \in \mathbb{F}^n, \quad r \in_R \mathbb{F}^m$$
令$L$为$[n,k,d]$线性码。若$d(U^*, L^m) > e$且$e < d/4$，则恶意证明者使验证者接受的概率至多为$(1 - e/n)^t + (e+1)/|\mathbb{F}|$。
> 作用：测试多个向量是否同时属于线性码L，通过随机线性组合和少量列查询实现亚线性验证。

**[线性约束测试 - Test-Linear-Constraints-IRS]**
$$q(\bullet) = \sum_{i=1}^m r_i(\bullet) \cdot p_i(\bullet)$$
其中$p_i$是第i行编码的多项式，$r_i(\bullet)$满足$r_i(\zeta_c) = ((r^T A_{P})_{ic})$。验证条件为$\sum_c q(\zeta_c) = r^T b$且在随机查询集Q上$r_i(\eta_j) \cdot U_{i,j} = q(\eta_j)$。
> 作用：在亚线性通信下验证编码消息x满足线性系统$Ax = b$。

**[二次约束测试 - Test-Quadratic-Constraints-IRS]**
$$p_0(\bullet) = \sum_{i=1}^m r_i \cdot (p_i^x(\bullet) \cdot p_i^y(\bullet) - p_i^z(\bullet)) + r_{blind}(\bullet)$$
验证条件为对所有$\zeta_c$有$p_0(\zeta_c) = 0$且在随机查询集Q上有$r_i \cdot (U_{i,j}^x \cdot U_{i,j}^y - U_{i,j}^z) = p_0(\eta_j)$。
> 作用：在亚线性通信下验证编码消息满足二次关系$x \odot y = z$（点乘）。

**[零知识交互式PCP最终协议复杂度]**
通信：$\sigma \cdot n + 4\sigma \cdot (k+\ell-1) + \sigma \cdot (2k-1)$ 域元素，验证者读取$4m + 5\sigma$个域符号。
> 作用：给出了整个论证系统的通信量，通过选择参数$k, \ell, m$使得通信量为$O(\sqrt{s})$（s为电路规模）。

### 实验结果
实验使用C++编程语言，NTL库进行有限域运算，SHA-256作为碰撞 resistant 哈希函数，运行于Intel Core i7-4720HQ (2.60GHz, 4核, 8 GiB RAM)平台。核心基准任务是验证一个SHA-256原像的零知识证明。对于该任务，当达到$2^{-40}$可靠性误差时，证明尺寸约为44KB（若采用猜想4.1则更优至34KB），证明方运行时间140ms，验证方运行时间62ms。与ZKB++相比，通信量减少了约4倍。当电路规模超过约300万门时，协议通信量开始小于电路规模本身，体现了亚线性特性的实际优势。在多实例场景下（4096个实例），每个实例的平摊通信降至约2KB，平摊证明方运行时间151ms，验证方运行时间500μs。实验还展示了从约2000门到500万门不同规模电路的性能，证明方和验证方时间均随电路规模亚线性增长。结果还提供了猜想驱动变体（Ligero-Strong）与标准变体的对比，前者在通信上平均节省约20%。

### 局限性与开放问题
本文方案的证明方计算复杂度为$O(s \log^2 s)$，虽优于大部分实用PCP方案，但对于极大电路仍可能成为瓶颈。方案安全性依赖于$e < d/4$的严格条件，若能证明$e < d/3$甚至$e < d/2$的情况，通信和计算效率可进一步提升约25%。验证方的FFT操作目前需评估整个域，未充分利用查询子集的结构，存在优化空间。此外，协议对布尔电路需要选择合适大小的域，这增加了参数优化的复杂度。

### 强关联论文

[22] Giacomelli等. ZKBoo: Faster zero-knowledge for boolean circuits. **USENIX Security 2016** [Google Scholar](https://scholar.google.com/scholar?q=ZKBoo+Faster+zero-knowledge+for+boolean+circuits+Giacomelli+Madsen+Orlandi)

[13] Chase等. Post-quantum zero-knowledge and signatures from symmetric-key primitives. **CCS 2017** [Google Scholar](https://scholar.google.com/scholar?q=Post-quantum+zero-knowledge+and+signatures+from+symmetric-key+primitives+Chase+Derler+Goldfeder+Orlandi+Ramacher+Rechberger+Slamanig+Zaverucha)

[29] Ishai等. Zero-knowledge proofs from secure multiparty computation. **STOC 2007** [Google Scholar](https://scholar.google.com/scholar?q=Zero-knowledge+proofs+from+secure+multiparty+computation+Ishai+Kushilevitz+Ostrovsky+Sahai)

[16] Damgård和Ishai. Scalable secure multiparty computation. **CRYPTO 2006** [Google Scholar](https://scholar.google.com/scholar?q=Scalable+secure+multiparty+computation+Damg%C3%A5rd+Ishai)

[5] Ben-Sasson等. Scalable, transparent, and post-quantum secure computational integrity. **Manuscript 2017** [Google Scholar](https://scholar.google.com/scholar?q=Scalable+transparent+and+post-quantum+secure+computational+integrity+Ben-Sasson+Bentov+Horesh+Riabzev)

[36] Kilian. A note on efficient zero-knowledge proofs and arguments. **STOC 1992** [Google Scholar](https://scholar.google.com/scholar?q=A+note+on+efficient+zero-knowledge+proofs+and+arguments+Kilian)

[19] Fiat和Shamir. How to prove yourself: Practical solutions to identification and signature problems. **CRYPTO 1986** [Google Scholar](https://scholar.google.com/scholar?q=How+to+prove+yourself+Practical+solutions+to+identification+and+signature+problems+Fiat+Shamir)

[32] Ishai等. Founding cryptography on oblivious transfer - efficiently. **CRYPTO 2008** [Google Scholar](https://scholar.google.com/scholar?q=Founding+cryptography+on+oblivious+transfer+%E2%80%94+efficiently+Ishai+Prabhakaran+Sahai)


## 关键词

+ 零知识论证
+ 亚线性通信
+ 无可信设置
+ 里德所罗门码
+ 零知识PCP