---
title: "FalconDB: Blockchain-based collaborative database"
标题简称: FalconDB
论文类型: conference
会议简称: SIGMOD
发表年份: 2020
created: 2025-04-19 11:35:44
modified: 2025-04-19 12:02:03
links: https://dl.acm.org/doi/abs/10.1145/3318464.3380594
---

## FalconDB: Blockchain-based collaborative database

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3318464.3380594)

## 作者

+ Yanqing Peng 
+ Min Du 
+ Feifei Li 
+ Raymond Cheng 
+ [Dawn Song](Dawn%20Song.md) 

## 笔记

### 背景与动机
在多方协作共享数据库的应用场景中，个体用户（如小型非营利组织或个人捐赠者）因硬件资源有限，难以兼顾安全性、兼容性与效率三者，形成“三难困境”。传统的集中式服务器方案要求用户完全信任服务商，无法防止恶意篡改或隐瞒操作。区块链方案虽能容忍拜占庭故障，但全节点需存储数百GB数据并持续参与共识，对个人设备负担过重；而轻客户端依赖不可信全节点的查询API，若引入智能合约进行查询共识，则面临吞吐量低、延迟高、Gas消耗大等问题。现有外包数据库（ODB）的认证数据结构（ADS）虽能验证查询结果，但仅在单用户场景下保证客户端持有最新摘要是正确的；多用户协作时，客户端难以同步最新摘要，且无法追溯或回滚恶意更新。因此，迫切需要一种系统，让资源有限的个体既能高效查询、又能以区块链级别的安全性参与协作数据库的构建。

### 相关工作

[8] Buchman et al. The latest gossip on BFT consensus. **2018** [Google Scholar](https://scholar.google.com/scholar?q=The+latest+gossip+on+BFT+consensus)
> 核心思路：提出Tendermint共识协议，采用PBFT风格的投票机制，在许可链环境下提供拜占庭容错。
> 局限与区别：Tendermint本身只是共识层，未结合认证数据结构来解决客户端轻量化验证问题。FalconDB将封装于区块头的数据库摘要与Tendermint结合，使得客户端仅同步区块头即可验证查询结果。

[11] Cooper et al. Benchmarking cloud serving systems with YCSB. **SoCC 2010** [Google Scholar](https://scholar.google.com/scholar?q=Benchmarking+cloud+serving+systems+with+YCSB)
> 核心思路：提出YCSB基准测试框架，用于评估云存储系统的性能。
> 局限与区别：FalconDB使用YCSB的三种典型工作负载（只读、读重、写重）进行实验，以评估系统在并发事务下的表现。

[33] McConaghy et al. BigchainDB: a scalable blockchain database. **2016** [Google Scholar](https://scholar.google.com/scholar?q=BigchainDB%3A+a+scalable+blockchain+database)
> 核心思路：将区块链与分布式数据库结合，每个全节点存储完整数据副本。
> 局限与区别：所有节点都必须存储全量数据库与历史数据，客户端资源消耗大；FalconDB中客户端仅存储区块头，服务器才持有完整数据及ADS。

[50] Zhang et al. IntegriDB: Verifiable SQL for Outsourced Databases. **CCS 2015** [Google Scholar](https://scholar.google.com/scholar?q=IntegriDB%3A+Verifiable+SQL+for+Outsourced+Databases)
> 核心思路：基于认证跳表与Merkle哈希树，为SQL查询（点查询、范围查询、连接查询）提供可验证的ADS，客户端可借助摘要δ验证结果正确性。
> 局限与区别：IntegriDB本身无多用户场景下的摘要同步机制，且不能抵抗恶意客户端的更新。FalconDB将其作为ADS组件，通过区块链共识同步摘要，并利用时间数据模型记录更新历史以支持回溯。

[49] Zhang et al. vSQL: Verifying arbitrary SQL queries over dynamic outsourced databases. **S&P 2017** [Google Scholar](https://scholar.google.com/scholar?q=vSQL%3A+Verifying+arbitrary+SQL+queries+over+dynamic+outsourced+databases)
> 核心思路：使用零知识证明为任意SQL查询提供通用验证，但性能较慢。
> 局限与区别：vSQL生成的证明速度快但验证过程开销大；FalconDB选择效率更高的IntegriDB，并采用异步验证模式将证明生成从主流程解耦。

[35] Nakamoto. Bitcoin: A peer-to-peer electronic cash system. **2008** [Google Scholar](https://scholar.google.com/scholar?q=Bitcoin%3A+A+peer-to-peer+electronic+cash+system)
> 核心思路：提出轻客户端概念，仅存储区块头以验证交易。
> 局限与区别：Bitcoin轻客户端只能验证交易包含性，不支持数据库查询验证。FalconDB沿用了轻客户端思想，但额外存储数据库摘要以执行ADS查询验证。

[1] Al-Bassam et al. Chainspace: A sharded smart contracts platform. **NDSS 2018** [Google Scholar](https://scholar.google.com/scholar?q=Chainspace%3A+A+sharded+smart+contracts+platform)
> 核心思路：通过分片提高智能合约平台的扩展性。
> 局限与区别：FalconDB在节点规模大时可使用类似分片技术（如RandHound）随机选取共识子集以降低通信开销，但其核心关注点并非分片本身。

[20] Gilad et al. Algorand: Scaling byzantine agreements for cryptocurrencies. **SOSP 2017** [Google Scholar](https://scholar.google.com/scholar?q=Algorand%3A+Scaling+byzantine+agreements+for+cryptocurrencies)
> 核心思路：通过密码抽签随机选择共识节点，实现可扩展的拜占庭协议。
> 局限与区别：类似分片方案，Algorand可替代Tendermint作为FalconDB的共识层以容纳更多客户端节点，论文给出了该可替换性。

[23] Kokoris-Kogias et al. Omniledger: A secure, scale-out, decentralized ledger via sharding. **S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Omniledger%3A+A+secure%2C+scale-out%2C+decentralized+ledger+via+sharding)
> 核心思路：利用分片实现账本的横向扩展。
> 局限与区别：FalconDB在讨论大规模节点时提到可采用此类方案作为共识层的备选，但实验验证基于Tendermint。

[42] Syta et al. Scalable bias-resistant distributed randomness. **S&P 2017** [Google Scholar](https://scholar.google.com/scholar?q=Scalable+bias-resistant+distributed+randomness)
> 核心思路：提出RandHound协议，安全地产生不可预测的随机数，用于随机选取共识节点。
> 局限与区别：FalconDB提及当客户端节点过多时，可借助RandHound选择子集参与共识以减少通信开销。

### 核心技术与方案

FalconDB将系统实体分为两类：**服务器节点**存储完整数据库、区块链全数据及认证数据结构（ADS）；**客户端节点**仅存储区块链区块头（含数据库摘要δ），通过向服务器发起请求执行查询与更新。区块链网络由服务器与部分客户端共同维护，采用许可型BFT共识（如Tendermint）确保系统在不超过1/3恶意节点时达成一致。

**区块链构造**。每个区块B对应一个数据库事务，区块头H包含：高度height、前一区块哈希、内容哈希、数据库摘要δ、读写集哈希、更新者身份e₀；验证数据V包含e₀的签名及k个验证者签名。共识协议确保区块内容正确且摘要δ与执行事务后的数据库状态一致。

**时间数据模型**。为支持透明历史追溯，每条记录附加两个时间属性：`VF`（本版本有效起始区块高度）和`VT`（本版本有效截止区块高度）。插入时设`VF=h`，`VT=∞`；删除时将原记录的`VT`设为当前高度h；更新拆分为删除原记录+插入新记录。查询时通过条件`VT=∞`获取最新快照，通过`VF≤h且VT>h`获取历史快照，保证了**透明性**和**不可变性**。

**查询处理与认证**。客户端可发起标准查询（`VT=∞`）、全历史查询（无`VT`限制）、范围历史查询（附加`VF`和`VT`条件）及增量查询（`VF=h`或`VT=h`）。服务器返回结果时附带签名；客户端后续可通过智能合约发起异步验证请求，服务器需提交ADS证明（如IntegriDB生成），否则将被罚没押金。这种解耦模式避免了证明生成（可达数小时）阻塞主流程。

**更新处理与认证**。客户端连接服务器，执行UpdC/UpdS交互获得新摘要δ'。服务器构造包含更新日志、中间摘要及最终摘要的区块并提交至区块链网络。区块链节点验证：①客户端权限（由权限函数定义）；②通过重放交互日志确认摘要δ'正确生成。区块经BFT共识后提交，所有服务器同步数据库，客户端同步最新摘要。

**并发控制**。采用乐观并发控制（OCC）实现快照隔离。事务开始前指定读时间戳i（基于的区块高度），提交时的区块高度j作为写时间戳。区块链节点检查事务与区块Bᵢ₊₁…Bⱼ₋₁中的事务是否冲突（通过读写集），若冲突则中止。

**安全性直觉**。正确性：持有最新摘要的客户端可通过ADS函数VerifyQry验证查询结果的正确性、完整性和新鲜度。数据完整性：任意恶意更新若不通过UpdC/UpdS接口执行，将导致实际数据库摘要与区块链头部摘要不匹配，后续查询无法生成有效证明。不可变性与透明性：基于区块链的时间数据模型确保所有历史版本可追溯。系统活性：只要至少一个服务器诚实，系统可从初始状态逐步验证每个区块的正确性；即使所有服务器皆恶意，初始客户端也可通过验证首个摘要发现错误。

**激励模型**。通过智能合约实现服务费与认证合约。客户端和服务器初始存入押金。查询按时，服务器获服务费；客户端可请求认证，服务器需提交证明，否则押金被冻结并最终罚没。博弈分析表明：当惩罚足够大且认证概率适当高时，理性服务器总是选择诚实回应。

**渐进复杂度**。客户端存储仅O(1)的摘要且区块头大小固定（<1KB），存储总量随区块数线性增长（数百万区块仅需数十MB）。服务器存储全数据库及ADS，ADS维护O(m²n)的结构（m为列数，n为行数）。查询认证时，客户端验证时间仅O(1)（与数据库大小无关），但证明生成随查询结果规模线性增长。

### 核心公式与流程

**[区块链验证条件]**
$$
\begin{aligned}
&\text{hash}(H') = H.\text{lastBlockHash} \\
&H.\text{height} = H'.\text{height} + 1 \\
&\text{hash}(C) = H.\text{dataHash} \\
&\text{validate}(H, C) = 1
\end{aligned}
$$
> 作用：定义FalconDB区块有效性的必要条件，包括前后区块哈希链接、高度递增、内容哈希正确以及验证数据通过协议定义的校验。

**[时间数据模型的插入操作]**
$$
\text{INSERT} \rightarrow (\text{attrs} \mid VF = h, VT = \infty)
$$
> 作用：插入新记录时，将有效起始时间设为当前区块高度h，有效截止时间设为无穷大。

**[时间数据模型的删除操作]**
$$
\text{DELETE} \rightarrow \text{UPDATE record SET } VT = h
$$
> 作用：删除记录时，将其有效截止时间设为当前高度h，保留历史版本。

**[时间数据模型的更新操作]**
$$
\text{UPDATE} \rightarrow \text{DELETE(old) + INSERT(new)}
$$
> 作用：更新记录时，先删除（设VT=h）原记录，再插入含新值且VT=∞的新记录。

**[点查询认证流程]**
1. 客户端发送查询q（附加VT=∞条件）至服务器；
2. 服务器执行SQL，返回结果R及签名；
3. 客户端可选请求证明：提交结果至智能合约；
4. 服务器生成ADS证明π并提交至合约；
5. 客户端使用摘要δ验证VerifyQry(δ, q, R, π) → 1。
> 作用：通过延迟生成的ADS证明，确保查询结果的正确性与完整性，同时避免证明生成阻塞在线流程。

### 实验结果

实验在CloudLab上进行，每个节点配备2.4 GHz十核Xeon E5-2640v4处理器和64GB DRAM。使用YCSB基准，模拟5个服务器和27个客户端，客户端处理速度模拟为服务器的1/10（即放大10倍）。对比基线为：BC（每个节点存储全数据库的区块链方案）和SC（客户端通过智能合约向服务器提交查询并等待共识确认的方案）。在存储开销上，对于1000万行数据库，FalconDB服务器存储约200GB（含ADS），BC和SC服务器约3GB；而FalconDB客户端仅需不到100MB区块头，BC客户端需约6GB全数据。查询吞吐方面，FalconDB在点查询上可达约10,000 TPS，BC约100 TPS，SC约1,000 TPS；延迟上FalconDB约10ms，BC约1,000ms，SC约1,000ms。更新性能显示单条插入约1秒（含共识和ADS），批量插入性能线性增长。在YCSB只读工作负载下，FalconDB吞吐随并发客户端数增加保持稳定约8,500 TPS；该工作负载下延迟在50并发时约2,000ms，而写重工作负载因OCC冲突大幅上升（50并发时约11,000ms）。

### 局限性与开放问题

首先，FalconDB不提供数据隐私保护，所有数据明文存储于服务器，无法防止服务器窥探内容。其次，当前的ADS（IntegriDB）证明生成时间在百万行级别查询上可达数小时，虽然通过异步解耦避免阻塞主流程，但频繁认证会增加服务器计算压力。另外，乐观并发控制在写冲突严重场景下事务中止率激增，影响了写重工作负载的性能。最后，权限函数的动态调整依赖于智能合约实现，若合约自身存在漏洞将威胁整个系统。

### 强关联论文

[8] Buchman et al. The latest gossip on BFT consensus. **2018** [Google Scholar](https://scholar.google.com/scholar?q=The+latest+gossip+on+BFT+consensus)

[11] Cooper et al. Benchmarking cloud serving systems with YCSB. **SoCC 2010** [Google Scholar](https://scholar.google.com/scholar?q=Benchmarking+cloud+serving+systems+with+YCSB)

[33] McConaghy et al. BigchainDB: a scalable blockchain database. **2016** [Google Scholar](https://scholar.google.com/scholar?q=BigchainDB%3A+a+scalable+blockchain+database)

[50] Zhang et al. IntegriDB: Verifiable SQL for Outsourced Databases. **CCS 2015** [Google Scholar](https://scholar.google.com/scholar?q=IntegriDB%3A+Verifiable+SQL+for+Outsourced+Databases)

[49] Zhang et al. vSQL: Verifying arbitrary SQL queries over dynamic outsourced databases. **S&P 2017** [Google Scholar](https://scholar.google.com/scholar?q=vSQL%3A+Verifying+arbitrary+SQL+queries+over+dynamic+outsourced+databases)

[20] Gilad et al. Algorand: Scaling byzantine agreements for cryptocurrencies. **SOSP 2017** [Google Scholar](https://scholar.google.com/scholar?q=Algorand%3A+Scaling+byzantine+agreements+for+cryptocurrencies)

[42] Syta et al. Scalable bias-resistant distributed randomness. **S&P 2017** [Google Scholar](https://scholar.google.com/scholar?q=Scalable+bias-resistant+distributed+randomness)

[1] Al-Bassam et al. Chainspace: A sharded smart contracts platform. **NDSS 2018** [Google Scholar](https://scholar.google.com/scholar?q=Chainspace%3A+A+sharded+smart+contracts+platform)

[23] Kokoris-Kogias et al. Omniledger: A secure, scale-out, decentralized ledger via sharding. **S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Omniledger%3A+A+secure%2C+scale-out%2C+decentralized+ledger+via+sharding)

[35] Nakamoto. Bitcoin: A peer-to-peer electronic cash system. **2008** [Google Scholar](https://scholar.google.com/scholar?q=Bitcoin%3A+A+peer-to-peer+electronic+cash+system)


## 关键词

+ 区块链协作数据库
+ FalconDB可验证查询
+ 分布式账本共识
+ 无信任协作数据库
+ 轻量级客户端存储
+ 外包数据库完整性