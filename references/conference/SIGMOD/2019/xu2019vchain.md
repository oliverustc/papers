---
title: "vchain: Enabling verifiable boolean range queries over blockchain databases"
标题简称:
论文类型: conference
会议简称: SIGMOD
发表年份: 2019
modified: 2025-04-17 13:45:35
created: 2025-04-11 11:03:17
---

## vchain: Enabling verifiable boolean range queries over blockchain databases

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3299869.3300083)

## 作者

+ [Cheng Xu](Cheng%20Xu.md)
+ Ce Zhang 
+ [Jianliang Xu](Jianliang%20Xu.md)
## 笔记

### 背景与动机
区块链技术因其去中心化、不可篡改等特性，在加密货币和去中心化应用领域蓬勃发展。随着数据密集型应用的普及，用户对存储在区块链数据库中的数据进行查询的需求日益增长，例如在比特币网络中查找满足特定金额范围的交易 [1]，或在基于区块链的专利管理系统中使用布尔运算符搜索关键词 [9]。然而，确保查询结果的完整性是一个关键挑战。一个直接的方案是用户作为全节点维护整个区块链数据库并本地执行查询，但这对于存储、计算和带宽资源有限的用户（尤其是移动用户）来说成本过高 [13]。另一种方案是将存储和查询服务委托给强大的全节点（服务提供商），而用户仅作为轻节点。但区块链网络的核心假设是节点不可信，因此如何保证服务提供商返回结果的正确性和完整性（即，未被篡改且无遗漏）是本文试图填补的空白。现有技术主要针对外包数据库，无法直接应用于区块链，因为区块链缺乏传统的数据所有者，且数据是无限增长的，需要一种支持动态属性和高效聚合的认证数据结构。

### 相关工作

[1] S. Nakamoto. Bitcoin: A peer-to-peer electronic cash system. **2008** [Google Scholar](https://scholar.google.com/scholar?q=Bitcoin+A+peer-to-peer+electronic+cash+system)
> 核心思路：提出了比特币，其底层区块链使用哈希链和Merkle树确保交易数据不可篡改。
> 局限与区别：其Merkle树仅用于验证单个交易是否在区块内，不支持复杂的布尔范围查询结果的完整性验证。

[2] G. Wood. Ethereum: A secure decentralised generalised transaction ledger. **Ethereum project yellow paper 2014** [Google Scholar](https://scholar.google.com/scholar?q=Ethereum+A+secure+decentralised+generalised+transaction+ledger)
> 核心思路：扩展了区块链概念，引入了智能合约，支持更通用的去中心化应用。
> 局限与区别：同样未提供内置的查询完整性机制，第三方应用依赖可信执行环境或中心化服务。

[3] T. T. A. Dinh et al. Untangling blockchain: a data processing view of blockchain systems. **IEEE TKDE 2018** [Google Scholar](https://scholar.google.com/scholar?q=Untangling+blockchain+a+data+processing+view+of+blockchain+systems)
> 核心思路：从数据处理角度对区块链系统进行了系统性分析。
> 局限与区别：分析了系统架构，但未提出解决查询完整性的具体方案。

[4] T. T. A. Dinh et al. Blockbench: A framework for analyzing private blockchains. **ACM SIGMOD 2017** [Google Scholar](https://scholar.google.com/scholar?q=Blockbench+A+framework+for+analyzing+private+blockchains)
> 核心思路：提出了评估私有区块链性能的基准测试框架。
> 局限与区别：侧重于性能评估，而非查询结果的完整性保障。

[5] R. C. Merkle. A certified digital signature. **CRYPTO 1989** [Google Scholar](https://scholar.google.com/scholar?q=A+certified+digital+signature)
> 核心思路：提出了Merkle哈希树，一种通过哈希链实现高效数据认证的数据结构。
> 局限与区别：传统MHT构建于固定的查询键上，无法高效支持多属性维度或集合属性查询，且在区块链场景下难以实现跨块聚合。

[6] C. Papamanthou et al. Optimal verification of operations on dynamic sets. **CRYPTO 2011** [Google Scholar](https://scholar.google.com/scholar?q=Optimal+verification+of+operations+on+dynamic+sets)
> 核心思路：提出了基于双线性配对的动态集合累加器，支持成员证明和集合不相交证明。
> 局限与区别：其构造（Construction 1）不支持证明的聚合，应用于区块链时，为每个不匹配对象生成单独证明会造成效率瓶颈。

[7] Y. Zhang et al. An expressive (zero-knowledge) set accumulator. **IEEE EuroS&P 2017** [Google Scholar](https://scholar.google.com/scholar?q=An+expressive+zero-knowledge+set+accumulator)
> 核心思路：提出了一种支持聚合的集合累加器（Construction 2），允许将多个累加值或证明合并为一个。
> 局限与区别：该构造依赖于q-DHE假设，其公钥大小与属性值的位长线性相关，在需要哈希函数编码属性的实际应用中，公钥生成和维护成本较高。

### 核心技术与方案

本文提出的vChain框架旨在解决区块链数据库上布尔范围查询的完整性问题。系统涉及三方：矿工（构造区块和ADS）、服务提供商（SP，不可信的全节点，处理查询）和查询用户（轻节点，验证结果）。框架的核心是利用一种新型的基于累加器的认证数据结构（ADS）扩展区块，使得SP能够为查询结果生成一个密码学证明（验证对象VO），用户可通过VO验证结果的正确性（未被篡改）和完备性（无遗漏）。

**1. 核心ADS：基于多重集合累加器的属性摘要**
传统MHT无法高效支持任意属性组合的查询，尤其是集合属性。为此，vChain将每个数据对象 `\(o_i\)` 的属性进行统一处理。具体来说，数值属性 `\(V_i\)` 通过转换为二进制前缀集合 `\(trans(V_i)\)` 来统一为集合属性。例如，数值4（二进制100）被转换为 `\(\{1*, 10*, 100\}\)`。范围查询 `\([\alpha, \beta]\)` 也被转换为覆盖该范围的等价前缀集合，例如 `\([0,6]\)` 转换为 `\(\{0*, 10*, 110\}\)`。这样，判断一个数值是否在范围内的查询就转化为判断两个集合是否相交的布尔查询。对于原始的集合属性 `\(W_i\)`，其元素保持不变。最终，每个对象 `\(o_i\)` 的属性被整合为一个统一的多重集合 `\(W_i' = trans(V_i) \cup W_i\)`。

矿工在生成区块时，为每个对象计算其属性的累加值 `\(AttDigest_i = acc(W_i')\)`，这是基于密码学多重集合累加器的。该累加器具有常数大小的输出，且支持高效的“集合不相交证明”。本文提出了两种累加器构造：
- **Construction 1 (acc1)**：基于 `\(q\)`-SDH假设和双线性配对。`\(acc(X) = g^{\prod_{x_i \in X}(x_i + s)}\)`。证明过程需要解两个多项式 `\(Q_1, Q_2\)` 使得 `\(P(X_1)Q_1 + P(X_2)Q_2 = 1\)`，验证通过双线性配对等式 `\(e(acc(X_1), g^{Q_1}) \cdot e(acc(X_2), g^{Q_2}) = e(g,g)\)` 实现。其公钥大小与最大集合大小成线性关系。
- **Construction 2 (acc2)**：基于 `\(q\)`-DHE假设。`\(acc(X) = (g^{A(X)}, g^{B(X)})\)`，其中 `\(A(X) = \sum s^{x_i}\)`，`\(B(X) = \sum s^{q-x_i}\)`。证明 `\( \pi = g^{A(X_1)B(X_2)}\)`，验证通过 `\(e(g^{A(X_1)}, g^{B(X_2)}) = e(\pi, g)\)`。关键优势在于支持 `\(Sum(\cdot)\)` 和 `\(ProofSum(\cdot)\)` 操作，允许将多个对象的累加值或证明聚合成一个，但这以更大的公钥（与属性值位长线性相关）为代价。

**2. 块内索引与批处理**
每个区块通常包含多个对象。为高效处理，vChain提出了一个基于Merkle树的块内索引。与传统MHT不同，树中每个节点（包括非叶子节点）都保存其子树下所有对象属性的并集 `\(W_n\)` 及其对应的累加值 `\(AttDigest_n = acc(W_n)\)`。该索引由矿工采用自底向上的贪心聚类算法构建，旨在最大化节点间的Jaccard相似度，从而提高查询时节点被判定为“不匹配”并被整体剪枝的概率。

在查询处理时，SP从根节点开始遍历。如果节点 `\(n\)` 的属性并集 `\(W_n\)` 与查询条件不匹配，则整个子树中的对象都不可能是结果。SP只需生成一个针对该节点 `\(W_n\)` 的“集合不相交证明”，并添加到VO中，从而一次性证明大量对象的非结果身份。用户通过VO中的信息（包括相应节点的 `\(AttDigest_n\)`、证明 `\(\pi\)` 以及查询的等价集合）重建Merkle根哈希，并与区块头中的 `\(MerkleRoot\)` 进行比较，以验证结果的完备性。

**3. 块间索引与增量证明**
为跨越多个区块进行聚合，vChain为每个区块建立了一个基于跳表的块间索引。该索引包含多个不同跳跃距离的层（如 `\(L_2, L_4, L_8\)`），每层维护了从当前区块向前跳过指定数量区块的属性并集 `\(W_{L_k}\)` 和对应的累加值 `\(AttDigest_{L_k}\)`。在查询一个时间窗口时，SP可以利用该索引“跳”过连续多个不包含匹配结果的区块，只需为整个跳跃生成一个证明，大幅减少VO大小和用户验证时间。

**4. 订阅查询与IP-Tree及延迟认证**
对于订阅查询，vChain提出了一个倒排前缀树（IP-Tree）来高效处理大量并发查询。IP-Tree将多个订阅查询的数值范围和布尔条件组合成一个树形索引。当新区块到达时，SP遍历IP-Tree，可以快速定位哪些查询需要处理，并利用相同的不匹配原因来共享证明，从而提升SP端的处理效率。此外，对于非实时应用，还提出了一种“延迟认证”优化。SP并不立即为每个不匹配的区块生成证明，而是维护一个栈来跟踪具有相同不匹配原因的连续区块。当匹配结果出现时，利用块间索引和 `\(ProofSum\)` 函数，将多个证明聚合成一个，进一步降低用户端的验证成本。

**安全性分析**
安全性建立在多重集合累加器的不可伪造性基础之上。**Definition 8.1** 定义了累加器的不可伪造性：任何多项式时间的敌手无法输出两个有交集的多重集合及其有效的“集合不相交证明”。**Theorem 8.1** 指出，两种累加器构造（基于 `\(q\)`-SDH和 `\(q\)`-DHE假设）均满足该性质。**Definition 8.2** 进而定义了查询认证算法的不可伪造性：敌手无法伪造包含不存在对象、不匹配对象或遗漏对象的结果。**Theorem 8.2** 的证明通过反证法，将所有可能的攻击归结为对底层哈希函数（碰撞）或累加器（伪造不相交证明）的破坏，从而保证了vChain查询认证过程的正确性。

**渐进复杂度**
| 参与方 | 操作 | 时间复杂度 | 通信量 |
| :--- | :--- | :--- | :--- |
| **矿工** | 构建块内ADS | `\(O(n \log n)\)` (n为块内对象数)，主要开销在累加器计算 | `\(O(\log n)\)` |
| **矿工** | 构建块间ADS | 取决于跳表大小 | 常数 |
| **SP** | 时间窗口查询 | `\(O(b + m)\)` (b为浏览的块数，m为匹配对象数)，主要开销在不匹配块/节点的证明生成 | `\(O(\text{VO})\)` |
| **用户** | 验证时间窗口查询 | `\(O(\text{证明数量})\)`，acc2支持批处理证明，用户时间可接近常数 | `\(O(\text{VO})\)` |
| **用户** | 存储（轻节点） | 仅存储块头，大小为常数（约800-960比特） | `\(O(1)\)` |

### 核心公式与流程

**[多重集合累加器构造1 (acc1)]**
$$acc(X) = g^{P(X)} = g^{\prod_{x_i \in X}(x_i + s)}$$
> 作用：生成集合 `\(X\)` 的累加值。证明不相交性基于寻找多项式 `\(Q_1, Q_2\)` 满足 `\(P(X_1)Q_1 + P(X_2)Q_2 = 1\)`，验证通过 `\(e(acc(X_1), F_1^*) \cdot e(acc(X_2), F_2^*) \stackrel{?}{=} e(g, g)\)`。

**[多重集合累加器构造2 (acc2)]**
$$acc(X) = (d_A(X), d_B(X)) = (g^{\sum_{x_i \in X} s^{x_i}}, g^{\sum_{x_i \in X} s^{q - x_i}})$$
> 作用：生成集合 `\(X\)` 的累加值。证明不相交性为 `\(\pi = g^{A(X_1)B(X_2)}\)`，验证通过 `\(e(d_A(X_1), d_B(X_2)) \stackrel{?}{=} e(\pi, g)\)`。此构造支持 `\(Sum(\cdot)\)` 和 `\(ProofSum(\cdot)\)` 操作，用于聚合多个累加值或证明。

**[块内非叶子节点定义]**
$$W_n = W_{n_l} \cup W_{n_r}$$
$$AttDigest_n = acc(W_n)$$
$$hash_n = \mathrm{hash}(\mathrm{hash}(\mathrm{hash}(hash_{n_l} | hash_{n_r}) | AttDigest_n))$$
> 作用：定义了块内Merkle树中非叶子节点的属性并集、累加值和哈希值。此为构建可证明集合并集的认证索引的基础。

**[实验证明：Construction 1 vs. 2 的权衡]**
> 实验对比图16显示，acc1与acc2在查询性能上存在权衡。acc2的SP端计算时间在某些场景可能更高（因需要额外聚合操作），但其优势在于用户端验证时间极低（接近常数），并且VO尺寸显著减小，尤其是在长查询窗口或结合“延迟认证”的订阅查询场景下，这一优势更为明显。

### 实验结果

实验使用三个数据集：Foursquare(4SQ，100万用户签到)、Weather(WX，150万气象记录)和Ethereum(ETH，112万交易记录，90K区块)。实验在配备Intel Xeon双核CPU和32GB RAM的服务器（SP/矿工）以及Intel Core i5 CPU和8GB RAM的笔记本电脑（用户）上进行。对比方案包括无索引（nil）、块内索引（intra）和联合索引（both），每种方案均测试两种累加器构造（acc1, acc2）。

核心性能数值：在10小时查询窗口（4SQ）下，intra索引相比nil，SP端CPU时间减少至少50%以上，VO尺寸也显著降低。联合索引（both）在某些场景（如ETH）性能进一步提升，例如ETH上VO尺寸从仅intra的450KB（acc1）降至150KB（intra）再降至130KB（both）。acc2方案在用户端验证时间上表现卓越，通常在0.01秒量级，而acc1可能需要几秒到几十秒。对于订阅查询，IP-Tree索引将SP开销降低了至少50%，而延迟认证（lazy）方案相比实时方案，用户端验证时间降低了几个数量级。

总体而言，索引方法（尤其是加上块间索引）在大多数情况下性能提升至少2倍。acc2在用户端性能表现最好，但SP端可能稍差；acc1在SP端可能更快，但用户端和VO性能较差。框架在不同选择性（10%-50%）下均能高效运行，验证了其鲁棒性。

### 局限性与开放问题
本文主要解决了布尔范围查询的可验证性问题，对于更复杂的分析型查询（如聚合、连接等）尚不支持。其次，性能优化方面，未来可以考虑利用多核、GPU等现代硬件来进一步提升系统吞吐量。此外，当前框架未考虑用户查询的隐私保护问题，在验证过程中，用户或服务提供商可能泄露查询内容或数据本身，这为未来的研究方向提供了可能。

### 强关联论文

[1] S. Nakamoto. Bitcoin: A peer-to-peer electronic cash system. **2008** [Google Scholar](https://scholar.google.com/scholar?q=Bitcoin+A+peer-to-peer+electronic+cash+system)

[2] G. Wood. Ethereum: A secure decentralised generalised transaction ledger. **Ethereum project yellow paper 2014** [Google Scholar](https://scholar.google.com/scholar?q=Ethereum+A+secure+decentralised+generalised+transaction+ledger)

[3] T. T. A. Dinh et al. Untangling blockchain: a data processing view of blockchain systems. **IEEE TKDE 2018** [Google Scholar](https://scholar.google.com/scholar?q=Untangling+blockchain+a+data+processing+view+of+blockchain+systems)

[4] T. T. A. Dinh et al. Blockbench: A framework for analyzing private blockchains. **ACM SIGMOD 2017** [Google Scholar](https://scholar.google.com/scholar?q=Blockbench+A+framework+for+analyzing+private+blockchains)

[5] R. C. Merkle. A certified digital signature. **CRYPTO 1989** [Google Scholar](https://scholar.google.com/scholar?q=A+certified+digital+signature)

[6] C. Papamanthou et al. Optimal verification of operations on dynamic sets. **CRYPTO 2011** [Google Scholar](https://scholar.google.com/scholar?q=Optimal+verification+of+operations+on+dynamic+sets)

[7] Y. Zhang et al. vSQL: verifying arbitrary SQL queries over dynamic outsourced databases. **IEEE S&P 2017** [Google Scholar](https://scholar.google.com/scholar?q=vSQL+verifying+arbitrary+SQL+queries+over+dynamic+outsourced+databases)

[8] B. Parno et al. Pinocchio: nearly practical verifiable computation. **IEEE S&P 2013** [Google Scholar](https://scholar.google.com/scholar?q=Pinocchio+nearly+practical+verifiable+computation)

[9] B. M. Platz et al. Flureedb: a practical decentralized database. **2017** [Google Scholar](https://scholar.google.com/scholar?q=Flureedb+a+practical+decentralized+database)


## 关键词

+ 区块链可验证布尔范围查询
+ 累加器认证数据结构
+ 动态聚合查询属性
+ 倒排前缀树订阅查询
+ 区块链数据库完整性
+ vChain框架