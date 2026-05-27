---
title: "Porygon: Scaling blockchain via 3d parallelism"
doi: 10.1109/icde60146.2024.00153
标题简称: 
论文类型: conference
会议简称: ICDE
发表年份: 2024
created: 2025-04-19 10:55:44
modified: 2025-04-21 00:53:32
---
## Porygon: Scaling blockchain via 3d parallelism

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/10597933)

## 作者

+ Wuhui Chen 
+ Ding Xia 
+ Zhongteng Cai 
+ Hong-Ning Dai 
+ Jianting Zhang 
+ Zicong Hong 
+ Junyuan Liang 
+ Zibin Zheng 

## 笔记

### 背景与动机

区块链技术面临的核心瓶颈在于存储与性能的矛盾。传统区块链要求全节点存储完整状态以参与共识，例如以太坊的数据量已达TB级[8]，这排除了大量资源受限的移动设备，限制了网络的去中心化程度。无状态区块链通过将状态存储从共识中剥离，实现了存储-共识的一维并行[8, 11]，使轻节点能够参与验证，从而扩大了网络规模。然而，现有无状态区块链仍存在两个固有缺陷：顺序交易处理和计算资源未充分利用。例如，Blockene [11] 这类工作仅允许一个委员会串行处理所有交易阶段（下载、排序、执行），导致吞吐量仅约1000 TPS，远无法满足Visa等场景的20000 TPS需求。因此，亟需一种能够在保持无状态区块链网络扩展性的同时，大幅提升交易吞吐量的并行化架构。

### 相关工作

[8] Xu Chen 等. SlimChain: Scaling Blockchain Transactions through Off-Chain Storage and Parallel Processing. **VLDB 2021** [Google Scholar](https://scholar.google.com/scholar?q=SlimChain%3A%20Scaling%20Blockchain%20Transactions%20through%20Off-Chain%20Storage%20and%20Parallel%20Processing)
> 核心思路：使用链下TEE执行智能合约，实现存储与共识的分离。
> 局限与区别：受限于易受攻击的可信代码库，且吞吐量有限；Porygon通过流水线和分片实现了更高维度的并行。

[11] Shashank Satija 等. Blockene: A High-Throughput Blockchain over Mobile Devices. **OSDI 2020** [Google Scholar](https://scholar.google.com/scholar?q=Blockene%3A%20A%20High-Throughput%20Blockchain%20over%20Mobile%20Devices)
> 核心思路：利用智能手机作为无状态节点，通过单一委员会顺序处理交易。
> 局限与区别：顺序处理和委员会固定，导致吞吐量低；Porygon引入了委员会间流水线和委员会内分片。

[38] Jelle Hellings 和 Mohammad Sadoghi. ByShard: Sharding in a Byzantine Environment. **VLDB 2021** [Google Scholar](https://scholar.google.com/scholar?q=ByShard%3A%20Sharding%20in%20a%20Byzantine%20Environment)
> 核心思路：采用两阶段跨分片协议，由发送方分片协调跨分片交易。
> 局限与区别：全节点需存储完整状态，存储开销高；Porygon通过无状态设计降低了节点存储需求。

[37] Mahdi Zamani 等. RapidChain: Scaling Blockchain via Full Sharding. **CCS 2018** [Google Scholar](https://scholar.google.com/scholar?q=RapidChain%3A%20Scaling%20Blockchain%20via%20Full%20Sharding)
> 核心思路：完全分片，每个分片内部委员会独立运行共识。
> 局限与区别：节点需存储分片内状态，且跨分片通信复杂度高；Porygon的无状态设计使其分片更轻量。

[36] Eleftherios Kokoris-Kogias 等. OmniLedger: A Secure, Scale-Out, Decentralized Ledger via Sharding. **IEEE S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=OmniLedger%3A%20A%20Secure%2C%20Scale-Out%2C%20Decentralized%20Ledger%20via%20Sharding)
> 核心思路：客户端参与跨分片协调，确保原子性。
> 局限与区别：同样面临全节点存储问题；Porygon的协调过程主要由排序委员会承担，对客户端透明。

[35] Loi Luu 等. A Secure Sharding Protocol for Open Blockchains. **CCS 2016** [Google Scholar](https://scholar.google.com/scholar?q=A%20Secure%20Sharding%20Protocol%20for%20Open%20Blockchains)
> 核心思路：使用最终委员会聚合全局结果。
> 局限与区别：通信复杂度为 $O(m^2 + bn)$；Porygon通过仅传递交易区块哈希而非完整交易降低了复杂度。

[19] Lei Yang 等. DispersedLedger: High-Throughput Byzantine Consensus on Variable Bandwidth Networks. **NSDI 2022** [Google Scholar](https://scholar.google.com/scholar?q=DispersedLedger%3A%20High-Throughput%20Byzantine%20Consensus%20on%20Variable%20Bandwidth%20Networks)
> 核心思路：将共识分为两个阶段，分离交易广播与共识。
> 局限与区别：任务分配存在安全挑战；Porygon引入了独立的见证阶段增强数据可用性。

[21] Alexander Spiegelman 等. Bullshark: DAG BFT Protocols Made Practical. **CCS 2022** [Google Scholar](https://scholar.google.com/scholar?q=Bullshark%3A%20DAG%20BFT%20Protocols%20Made%20Practical)
> 核心思路：利用DAG结构解耦交易与提案。
> 局限与区别：适用于许可链环境，未考虑无状态和分片；Porygon将其思想扩展至无状态公链。

### 核心技术与方案

Porygon 通过三个维度的并行化来提升系统性能。第一维是存储-共识并行，即无状态节点仅负责处理交易，存储节点负责维护完整状态。为缓解排序委员会带宽瓶颈，Porygon 将区块结构解耦为提案区块和交易区块：提案区块仅包含交易区块哈希列表、委员会信息和状态树根；交易区块由存储节点广播。这使排序委员会广播的最小信息量大大减少。

第二维是跨块并行，通过流水线机制实现。交易处理被解耦为四个连续的阶段：见证、排序、执行、提交。不同阶段由不同委员会并行处理。排序委员会负责排序和提交阶段，而执行委员会负责见证和执行阶段。流水线机制使得在任意时刻，多个不同批次的交易处于不同的处理阶段。例如，执行委员会1见证第1批交易时，排序委员会正在对第2批交易进行排序，同时执行委员会2正在执行第0批交易。此外，Porygon设计了跨批见证机制：执行委员会在空闲时仍可对其他批次交易进行见证，避免计算资源闲置。

第三维是块内并行，通过分片执行实现。每个执行委员会的成员根据VRF值的末N位被划分为多个执行子委员会，每个子委员会对应一个分片。排序委员会作为协调者，负责将交易分配给对应分片。对于跨分片交易，Porygon采用两阶段轻量级协调方案：
1. 单分片执行：排序委员会将跨分片交易分配给发起账户所在的分片进行预执行，执行结果不直接写入状态树。
2. 多分片更新：排序委员会聚合执行结果，将需更新的键值对列表广播给所有相关分片，各分片更新本地子树后返回一致性证明。若更新失败，排序委员会在后续轮次重试，直至成功或触发回滚。

无状态节点由VRF随机选入委员会，保证安全性。每个通信用例（如投票、提案）均通过存储节点转发，节点连接多个存储节点实现冗余。安全性证明依赖于两点：1）每委员会至少有2/3良性节点（通过切尔诺夫界论证，当总节点数 $M=3500$、诚实比例 $\alpha=0.75$、恶意存储节点比例 $\beta=0.5$、每节点连接存储节点数 $m=20$ 时，概率可忽略）。2）见证阈值 $T_w$ 和执行阈值 $T_e$ 分别大于委员会中恶意节点上限，从而保证每个有序的区块都能被至少一个良性节点见证，每个被执行的区块都能生成一致的执行结果。

系统复杂度方面，排序委员会共识的通信复杂度为 $\mathcal{O}(m^2)$，跨分片信息传递复杂度为 $\mathcal{O}(w n/m)$（其中 $m$ 为委员会大小，$n$ 为总节点数，$w$ 为跨分片信息大小），总体为 $\mathcal{O}(m^2 + w n/m)$。存储复杂度方面，无状态节点仅存储提案区块，为 $\mathcal{O}(1)$。

### 核心公式与流程

**[第1维并行：存储-共识解耦的块结构]**
提案区块：包含委员会信息、交易区块哈希列表、最新状态树根。
交易区块：包含交易索引、交易访问状态的预记录信息。

**[第2维并行：流水线阶段]**
见证阶段 $\rightarrow$ 排序阶段 $\rightarrow$ 执行阶段 $\rightarrow$ 提交阶段

**[第3维并行：跨分片协调的两阶段协议]**
单分片执行：排序委员会将跨分片交易分配给发起分片，预执行后返回结果集 $S_d$。
多分片更新：排序委员会生成更新列表 $U$，所有相关分片更新子树 $\mathcal{T}_d$，返回一致性证明。

**[安全性证明关键不等式：良性节点数 > 2×恶意节点数]**
$$\check{n}_g > 2\hat{n}_c$$
其中 $\check{n}_g = (p_g - \epsilon_g)M$ 为良性节点数下界，$\hat{n}_c = (p_c + \epsilon_c)M$ 为恶意节点数上界，$p_g = (1 - \beta^m)\alpha p$ 为单个节点是良性节点的概率。

**[性能分析：吞吐量与网络规模的关系（模拟结果）]**
当节点数从20000增至100000时，吞吐量从约8310 TPS增至38940 TPS，延迟仅从7.8秒增至8.3秒。

### 实验结果

实验在6台云服务器（Intel Cascade Lake 3.0GHz 24vCPUs, 48GB RAM）上部署原型，使用Golang实现，每个无状态节点分配500M内存和1 MB/s带宽。交易大小112字节，交易区块约2000笔交易。模拟系统支持达100000个节点。对比基线为Blockene [11]（代表1D并行无状态链）和轻量版ByShard [38]（代表分片全节点链）。核心结果：1）Porygon在原型测试中达21090 TPS（300节点），是Blockene（~750 TPS）的28倍，是ByShard（~9150 TPS）的2.3倍。2）模拟中Porygon吞吐量随节点数线性增长，从8760 TPS（100节点）增至57220 TPS（1000节点），增长约6.5倍，而ByShard仅增长约2.5倍。3）存储消耗方面，Porygon无状态节点仅需约5MB（随块高几乎不变），而ByShard全节点存储随块高线性增长，20个块后已达45MB。4）网络带宽方面，Porygon各阶段节点下载量比全节点减少50%-80%，上传量降低约30%。5）跨分片交易比例测试表明，当比例从0.5升至1.0时，吞吐量仅下降约4%（从9179 TPS降至8810 TPS），延迟增加约0.3秒，证明系统对跨分片交易有良好适应性。

### 局限性与开放问题

跨分片交易的延迟较高，需要6轮才能提交，而块内交易仅需4轮。这一差异在高跨分片比例场景下可能影响整体性能。当前系统对冲突交易的处理主要依赖排序委员会集中式检测，可能成为潜在瓶颈。未来可探索确定性优先级策略，优先提交跨分片交易以降低平均延迟，或利用DAG结构进一步提升跨分片并行度。

### 强关联论文

[8] Chen Xu 等. SlimChain: Scaling Blockchain Transactions through Off-Chain Storage and Parallel Processing. **VLDB 2021** [Google Scholar](https://scholar.google.com/scholar?q=SlimChain%3A%20Scaling%20Blockchain%20Transactions%20through%20Off-Chain%20Storage%20and%20Parallel%20Processing)

[11] Shashank Satija 等. Blockene: A High-Throughput Blockchain over Mobile Devices. **OSDI 2020** [Google Scholar](https://scholar.google.com/scholar?q=Blockene%3A%20A%20High-Throughput%20Blockchain%20over%20Mobile%20Devices)

[38] Jelle Hellings 和 Mohammad Sadoghi. ByShard: Sharding in a Byzantine Environment. **VLDB 2021** [Google Scholar](https://scholar.google.com/scholar?q=ByShard%3A%20Sharding%20in%20a%20Byzantine%20Environment)

[37] Mahdi Zamani 等. RapidChain: Scaling Blockchain via Full Sharding. **CCS 2018** [Google Scholar](https://scholar.google.com/scholar?q=RapidChain%3A%20Scaling%20Blockchain%20via%20Full%20Sharding)

[36] Eleftherios Kokoris-Kogias 等. OmniLedger: A Secure, Scale-Out, Decentralized Ledger via Sharding. **IEEE S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=OmniLedger%3A%20A%20Secure%2C%20Scale-Out%2C%20Decentralized%20Ledger%20via%20Sharding)

[35] Loi Luu 等. A Secure Sharding Protocol for Open Blockchains. **CCS 2016** [Google Scholar](https://scholar.google.com/scholar?q=A%20Secure%20Sharding%20Protocol%20for%20Open%20Blockchains)

[19] Lei Yang 等. DispersedLedger: High-Throughput Byzantine Consensus on Variable Bandwidth Networks. **NSDI 2022** [Google Scholar](https://scholar.google.com/scholar?q=DispersedLedger%3A%20High-Throughput%20Byzantine%20Consensus%20on%20Variable%20Bandwidth%20Networks)

[21] Alexander Spiegelman 等. Bullshark: DAG BFT Protocols Made Practical. **CCS 2022** [Google Scholar](https://scholar.google.com/scholar?q=Bullshark%3A%20DAG%20BFT%20Protocols%20Made%20Practical)


## 关键词

+ 无状态区块链
+ 三维并行性
+ 流水线机制
+ 分片机制
+ 区块链可扩展性
+ 交易吞吐量