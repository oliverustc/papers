---
title: "SEBDB: Semantics empowered blockchain database"
标题简称:
论文类型: conference
会议简称: ICDE
发表年份: 2019
created: 2025-04-19 11:29:21
modified: 2025-04-19 11:29:56
---

## SEBDB: Semantics empowered blockchain database

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/8731416)

## 作者

+ Yanchao Zhu 
+ Zhao Zhang 
+ Cheqing Jin 
+ Aoying Zhou 
+ Ying Yan 

## 笔记

### 背景与动机
区块链被视为一种去中心化数据库，但在数据建模、查询语言和查询效率上远不如传统关系型数据库成熟。现有的区块链平台如比特币、以太坊和 Hyperledger Fabric，虽然能够存储结构化交易数据，但缺乏关系语义，只能通过代码级 API 访问，导致复杂查询难以构建 [1][2]。同时，这些系统不支持将链上数据与链下数据库无缝集成，也无法为轻客户端提供丰富的可验证查询（authenticated query）——例如，用户无法验证查询结果的完整性与正确性。为解决这些问题，部分工作如 ChainSQL 和 BigchainDB 尝试将区块链与数据库结合，但存在数据冗余、缺乏专用区块链操作（如溯源追踪）、语义弱以及无法支持链上链下联合查询等瓶颈 [3][4]。本文旨在填补上述空白，提出首个同时兼顾可用性与可扩展性的区块链数据库 SEBDB，通过引入关系语义、SQL-like 接口、专用索引和可验证查询机制，使区块链系统在数据管理能力上趋近于传统数据库。

### 相关工作

[6] 中本聪. Bitcoin: A peer-to-peer electronic cash system. 2008 [Google Scholar](https://scholar.google.com/scholar?q=Bitcoin%3A+A+peer-to-peer+electronic+cash+system)
> 核心思路：提出首个去中心化加密货币，通过工作量证明共识和链式区块存储交易记录。
> 局限与区别：仅支持简单的交易查询，数据模型为扁平文件，缺乏关系语义和高层查询语言。

[1] Ethereum. 2014 [Google Scholar](https://scholar.google.com/scholar?q=Ethereum)
> 核心思路：引入图灵完备的智能合约和状态数据库（LevelDB），支持复杂业务逻辑。
> 局限与区别：数据仍以键值对存储，不提供关系代数操作；查询依赖低级 API，不支持结构化查询和可验证查询。

[2] Androulaki 等. Hyperledger Fabric: A distributed operating system for permissioned blockchains. 2018 [Google Scholar](https://scholar.google.com/scholar?q=Hyperledger+Fabric%3A+A+distributed+operating+system+for+permissioned+blockchains)
> 核心思路：面向联盟链的模块化架构，区块存储在文件系统，状态数据存储于 CouchDB/LevelDB。
> 局限与区别：虽然支持丰富查询，但交易数据缺乏语义描述；不支持链上链下数据联合查询和可验证查询。

[3] ChainSQL. 2017 [Google Scholar](https://scholar.google.com/scholar?q=ChainSQL)
> 核心思路：两层结构——内层共识，外层将交易复制到关系数据库，利用 RDBMS 处理查询。
> 局限与区别：维护两份数据副本，数据完整性难以验证；未优化专用区块链操作（如追溯），且不支持可验证查询。

[4] McConaghy 等. BigchainDB: a scalable blockchain database. 2016 [Google Scholar](https://scholar.google.com/scholar?q=BigchainDB%3A+a+scalable+blockchain+database)
> 核心思路：基于 MongoDB 的分布式区块链数据库，v1.0 为共识驱动的键值存储，v2.0 引入两层结构。
> 局限与区别：数据模型弱（仅非结构化的键值对），不支持关系操作；未集成链上链下数据，也无丰富可验证查询。

[12] Dinh 等. Untangling blockchain: A data processing view of blockchain systems. TKDE 2018 [Google Scholar](https://scholar.google.com/scholar?q=Untangling+blockchain%3A+A+data+processing+view+of+blockchain+systems)
> 核心思路：从数据处理角度系统综述区块链系统，比较各类系统在查询、存储、共识等方面的能力。
> 局限与区别：未提出新方案，仅作为分类框架。SEBDB 在此框架下首次将关系语义和可验证查询同时嵌入区块链。

### 核心技术与方案

SEBDB 的核心创新在于将关系数据模型引入区块链，并围绕该模型重新设计了存储、索引、查询处理和可验证机制。架构分为五层：应用层、查询处理层、存储与索引层、共识层和网络层。应用层提供 SQL-like 语言接口，用户可用 `CREATE`、`INSERT`、`SELECT` 等语句定义表和操作数据。每个交易类型对应一个表（relation），系统自动添加 `Tid`、`Ts`、`SenID`、`Tname` 等系统属性，与应用定义的属性共同构成行。查询处理层解析并优化 SQL-like 查询，存储层负责管理链上和链下数据。链上数据按区块追加存储，每个区块包含头信息和交易体；链下数据存储于本地 RDBMS。针对区块链场景，SEBDB 实现了三种特殊操作：追踪（track-trace）、链上连接（on-chain join）和链上-链下连接（on-off chain join）。

**索引机制**是实现高效查询的核心，包括三类索引：
1. 块级 B+ 树：以三元组 `(bid, tid, Ts)` 为键，支持按块ID、交易ID或时间戳定位块。
2. 表级位图索引：对每个表维护一个位图，第 `i` 位代表块 `i` 是否包含该表交易，用于快速过滤不含目标表的块。
3. 分层索引：支持在天/离散属性上构建。第一层为直方图或位图，描述属性值在块间的分布；第二层为块内的 B+ 树。查询时先通过第一层过滤块，再在未被过滤的块内通过 B+ 树精确定位。该索引支持追加更新，无需全局重平衡。

**追踪操作**（Algorithm 1）利用分层索引高效实现。给定时间窗口、操作者 `o` 和操作类型 `p`，首先通过块级索引获取时间窗口内的位图 `B`，再与操作者索引 `I_d` 和操作类型索引 `I_n` 的第一层位图做与运算，得到同时满足三个条件的块集合。对每个候选块，利用第二层索引查找交集指针，读取交易。该算法避免全链扫描，时间复杂度与候选块数量线性相关。

**链上连接**（Algorithm 2）适用于等值连接，利用表级索引和分层索引进一步优化。通过位图与运算得到两个连接表所在的块集合，对每对块 `(b_r, b_s)`，若通过分层索引第一层判定存在重叠的范围（`intersect` 返回真），则执行块内的排序归并连接。该算法减少了参与连接的块对数量。

**链上链下连接**（Algorithm 3）的优化思路类似：先获取链下表的属性范围 `(s_min, s_max)`，通过分层索引过滤不包含该范围的链上块，对剩余块执行排序归并连接。同时，链下数据一次性加载避免重复传输。

为支持**轻客户端可验证查询**，SEBDB 设计了认证分层索引（ALI），将第二层的 B+ 树替换为 Merkle B 树（MB-tree）。采用两阶段协议：第一轮，轻客户端向一个全节点发送查询，全节点执行查询并返回验证对象（VO），包含查询结果以及沿搜索路径的兄弟节点哈希，同时附带当前块高度 `h`。第二轮，客户端向另一个辅助全节点请求以 `h` 为快照的聚合摘要（即涉及块 MB-tree 根的哈希的拼接）。客户端用 VO 重建根哈希，与摘要对比以验证结果正确性。辅助节点可能腐败，客户可通过向多个辅助节点请求并设置阈值（公式 `θ`）来降低风险，例如在 PBFT 下，若最多 `max` 个拜占庭节点，客户端收到 `m` 个一致摘要时，错误概率 `θ` 由二项分布计算得出。

系统渐进复杂度方面：全扫描成本 $C_{No-index} = n \cdot t_S + \frac{f \cdot n}{b} \cdot t_T$，其中 $n$ 为块数，$f$ 为块大小。表级位图索引成本为 $C_{bitmap-index} = k \cdot t_S + \frac{f \cdot k}{b} \cdot t_T$，$k$ 为包含目标表的块数。分层索引成本为 $C_{layered-index} = p \cdot t_S + p \cdot t_T$，$p$ 为结果元组数。可验证查询中，VO 大小与结果所在块数及每块搜索路径长度线性相关，远小于全块传输。

### 核心公式与流程

**[块级索引成本对比]**
$$C_{No-index} = n \cdot t_S + \frac{f \cdot n}{b} \cdot t_T$$
$$C_{bitmap-index} = k \cdot t_S + \frac{f \cdot k}{b} \cdot t_T \quad (k \leq n)$$
$$C_{layered-index} = p \cdot t_S + p \cdot t_T$$
> 作用：对比了全扫描、表级位图索引和分层索引在 `SELECT` 操作上的磁盘 I/O 成本，其中 $t_S$ 为平均块访问时间，$t_T$ 为块传输时间，$f$ 为区块链块大小，$b$ 为磁盘页大小，$n$ 为块总数，$k$ 为包含目标表的块数，$p$ 为结果元组数。

**[可验证查询拜占庭错误概率]**
$$p_w = p \cdot \sum_{i=0}^{m-1} C_{m-1+i}^{i} \cdot p^{m-1} \cdot (1-p)^i$$
$$p_r = (1-p) \cdot \sum_{i=0}^{m-1} C_{m-1+i}^{i} \cdot (1-p)^{m-1} \cdot p^i$$
$$\theta = \left\{ \begin{array}{l} \frac{p_w}{p_w + p_r} \quad (m + i \leq n \land m \leq max) \\ 0 \quad (m > max) \end{array} \right.$$
> 作用：计算客户端从 $n$ 个辅助节点获得 $m$ 个一致摘要时，该摘要为错误（被拜占庭节点合谋）的概率 $\theta$。$p$ 为拜占庭节点比例，$max$ 为最大拜占庭节点数假设，基于二项分布与负二项模型。客户端可通过增大 $n$ 和 $m$ 来达到所需可信度。

**[追踪操作 Algorithm 1]**
> 输入：时间窗口 `(c, e)`，操作者 `o`，操作类型 `p`，块索引 `BI`，分层索引 `I_d`（基于 SenID）、`I_n`（基于 Tname）。  
> 步骤：  
> 1. 通过 `BI` 获取时间窗口内的块位图 `B`。  
> 2. 从 `I_d` 和 `I_n` 的第一层获取操作者和操作类型的位图 `B'` 和 `B''`。  
> 3. `B = B & B' & B''`，得到同时满足三个条件的块位图。  
> 4. 对每个候选块，在第二层索引上取指针交集，读取交易加入结果集。  
> 作用：避免全链扫描，高效实现多维追溯。

**[链上连接 Algorithm 2]**
> 输入：连接表 `r` 和 `s`，连接属性 `attr`，时间窗口，块索引，分层索引 `I_r`、`I_s`。  
> 步骤：  
> 1. 获取时间窗口内块位图 `B`。  
> 2. 取得 `I_r`、`I_s` 的第一层位图并分别与 `B` 取与，得到 `B'` 和 `B''`。  
> 3. 对每对块 `(b_r, b_s)`，若通过第一层直方图判定存在重叠（`intersect` 返回真），则执行块内排序归并连接。  
> 作用：利用分层索引过滤无连接可能的块对，减少 I/O。

**[链上链下连接 Algorithm 3]**
> 输入：链上表 `r`、链表下 `s`，连接属性，时间窗口，块索引，分层索引 `I_r`。  
> 步骤：  
> 1. 获取时间窗口内块位图 `B`。  
> 2. 获取链下表的属性范围 `(s_min, s_max)`。  
> 3. 从 `I_r` 第一层位图与 `B` 取与，再筛选与 `(s_min, s_max)` 有交集的块。  
> 4. 对剩余块，利用第二层索引执行排序归并连接。  
> 作用：避免读取不包含连接结果范围的块。

### 实验结果

实验在 4 节点集群上进行，每节点配备双 16 核 2.10GHz CPU、96GB RAM、3TB RAID5 磁盘、1Gbps 网络。代码用 C++ 编写，链下数据库使用 MySQL 5.7.21。共识组件支持 KAFKA 和 Tendermint。区块大小默认为 4MB，交易大小约 300 字节。定义 BChainBench 基准，包含 7 个典型查询（Q1-Q7）。写入性能方面：KAFKA 吞吐量可达约 400 TPS（480 客户端），而 Tendermint 吞吐量仅约 100 TPS。追踪查询（Q2、Q3）性能：分层索引比全扫描快 2-3 个数量级，比位图快 10-100 倍；结果集增大时差距缩小。在 2500 块、结果集 10k 的场景下，分层索引仅需约 100ms，而扫描需 10^5ms。区间查询（Q4）类似，分层索引显著优于其他方法。连接查询（Q5、Q6）：分层索引方法在块数和结果集增大时，性能仍远优于扫描和位图法，例如 2500 块时 LU 约 1s，扫描约 10s-100s。可验证查询：VO 大小、服务端和客户端计算时间均远优于全块传输方案，且随块数增长缓慢（VO 从约 10^3KB 增到 10^4KB，而基线从 10^4KB 增至 10^5KB）。与 ChainSQL 对比：在单维和二维追踪上，SEBDB 性能持平或显著优于 ChainSQL（快 10-100 倍）。缓存测试：交易缓存优于块缓存，如 Q2 从 26s 降至 18s。

### 局限性与开放问题

SEBDB 面向联盟链场景设计，在公有链环境下的适用性和安全性（如应对恶意全节点合谋）有待进一步研究。当前支持的 SQL-like 语言仍较基础，复杂分析性查询（如嵌套子查询、聚合分组）的支持尚不完全。分层索引的直方图基于采样生成，精度配置与性能之间的折中需要更系统的理论分析。此外，跨分片查询、数据分片与共识协议的耦合优化尚未深入探讨。论文未讨论系统在节点动态加入离开时的容错与恢复机制。

### 强关联论文

[1] Ethereum. 2014 [Google Scholar](https://scholar.google.com/scholar?q=Ethereum)

[2] Androulaki 等. Hyperledger Fabric: A distributed operating system for permissioned blockchains. 2018 [Google Scholar](https://scholar.google.com/scholar?q=Hyperledger+Fabric%3A+A+distributed+operating+system+for+permissioned+blockchains)

[3] ChainSQL. 2017 [Google Scholar](https://scholar.google.com/scholar?q=ChainSQL)

[4] McConaghy 等. BigchainDB: a scalable blockchain database. 2016 [Google Scholar](https://scholar.google.com/scholar?q=BigchainDB%3A+a+scalable+blockchain+database)

[6] 中本聪. Bitcoin: A peer-to-peer electronic cash system. 2008 [Google Scholar](https://scholar.google.com/scholar?q=Bitcoin%3A+A+peer-to-peer+electronic+cash+system)

[12] Dinh 等. Untangling blockchain: A data processing view of blockchain systems. **TKDE 2018** [Google Scholar](https://scholar.google.com/scholar?q=Untangling+blockchain%3A+A+data+processing+view+of+blockchain+systems)

[21] Li 等. Dynamic authenticated index structures for outsourced databases. **SIGMOD 2006** [Google Scholar](https://scholar.google.com/scholar?q=Dynamic+authenticated+index+structures+for+outsourced+databases)

[23] Yang 等. Authenticated join processing in outsourced databases. **SIGMOD 2009** [Google Scholar](https://scholar.google.com/scholar?q=Authenticated+join+processing+in+outsourced+databases)

[25] Castro 等. Practical byzantine fault tolerance. **OSDI 1999** [Google Scholar](https://scholar.google.com/scholar?q=Practical+byzantine+fault+tolerance)

[30] Dinh 等. BLOCKBENCH: A framework for analyzing private blockchains. **SIGMOD 2017** [Google Scholar](https://scholar.google.com/scholar?q=BLOCKBENCH%3A+A+framework+for+analyzing+private+blockchains)


## 关键词

+ 区块链数据库
+ 关系数据语义
+ SQL查询接口
+ 链上链下数据
+ 可用性与可扩展性
+ 去中心化数据库