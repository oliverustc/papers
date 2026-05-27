---
title: "Veridb: An sgx-based verifiable database"
doi: 10.1145/3448016.3457308
标题简称:
论文类型: conference
会议简称: SIGMOD
发表年份: 2021
modified: 2025-04-11 11:29:50
---
## Veridb: An sgx-based verifiable database

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3448016.3457308)

## 作者

+ Wenchao Zhou 
+ Yifan Cai 
+ Yanqing Peng 
+ Sheng Wang 
+ Ke Ma 
+ Feifei Li 

## 笔记

### 背景与动机

随着数据存储与计算任务向云端迁移，用户迫切需要一种机制来验证云服务提供商是否忠实地维护了其托管的数据与计算结果的完整性。然而，一个恶意的云服务提供商可能对数据库进行任意篡改或返回不完整、伪造的结果。过去，基于 Merkle 哈希树的可验证数据库方案 [14] 通过递归哈希结构将完整性验证简化为对根哈希的复现，但这带来了严重的并发瓶颈：每次数据更新都必须重新计算根哈希，导致读操作必须等待所有写操作完成。更先进的密码学原语（如 vSQL [30] 和 IntegriDB [31]）虽然支持了更通用的 SQL 查询，但其证明生成开销极大，对于大型数据库可能需要数小时甚至数天。可信硬件的出现，如 Intel SGX [17]，为解决这一问题提供了新路径。SGX 提供了一个受保护的执行环境，称为飞地。然而，SGX 的受保护内存容量极其有限（仅 96 MB），无法容纳完整数据库。VeriDB 填补的空白是：如何利用 SGX 作为信任锚点，在不将全部数据放入飞地的前提下，设计一种支持通用 SQL 查询且性能开销合理的可验证数据库系统。

### 相关工作

[1] Arvind Arasu 等. Concerto: A High Concurrency Key-Value Store with Integrity. **SIGMOD 2017** [Google Scholar](https://scholar.google.com/scholar?q=Concerto%3A+A+High+Concurrency+Key-Value+Store+with+Integrity)
> 核心思路：采用离线内存检查算法解决 MHT 的并发瓶颈，为键值存储提供可验证性。
> 局限与区别：仅支持键值存储模型和简单的读写接口。VeriDB 将其扩展到支持关系表、多种访问方法和通用 SQL 查询。

[4] Sumeet Bajaj 等. CorrectDB: SQL Engine with Practical Query Authentication. **VLDB 2013** [Google Scholar](https://scholar.google.com/scholar?q=CorrectDB%3A+SQL+Engine+with+Practical+Query+Authentication)
> 核心思路：将数据库放入受信任 CPU 保护的环境中的设计思路。
> 局限与区别：仍依赖 MHT 进行完整性验证，存在根哈希的并发瓶颈。VeriDB 通过写-读一致内存和 SGX 移除了此瓶颈。

[14] Feifei Li 等. Dynamic authenticated index structures for outsourced databases. **SIGMOD 2006** [Google Scholar](https://scholar.google.com/scholar?q=Dynamic+authenticated+index+structures+for+outsourced+databases)
> 核心思路：经典的 MHT 方案（MB-Tree），用于范围查询的验证。
> 局限与区别：更新操作导致根哈希的并发瓶颈，且难以高效支持复杂 JOIN 查询。VeriDB 采用了完全不同的页结构存储和写-读一致内存，消除了这一瓶颈。

[26] Rohit Sinha 等. VeritasDB: High Throughput Key-Value Store with Integrity. **IACR ePrint 2018** [Google Scholar](https://scholar.google.com/scholar?q=VeritasDB%3A+High+Throughput+Key-Value+Store+with+Integrity)
> 核心思路：在网络代理中运行 SGX 飞地，以协调客户端与数据库服务器通信。
> 局限与区别：同样依赖 MHT 作为底层完整性验证，继承了其并发瓶颈。VeriDB 直接在数据存储层消除了这一瓶颈。

[30] Yupeng Zhang 等. vSQL: Verifying Arbitrary SQL Queries over Dynamic Outsourced Databases. **IEEE S&P 2017** [Google Scholar](https://scholar.google.com/scholar?q=vSQL%3A+Verifying+Arbitrary+SQL+Queries+over+Dynamic+Outsourced+Databases)
> 核心思路：采用 SNARK 技术，可验证任意 SQL 查询结果。
> 局限与区别：证明生成开销极高（数小时到数天），不实用。VeriDB 利用 SGX 将性能开销降低到实用水平。

[31] Yupeng Zhang 等. IntegriDB: Verifiable SQL for Outsourced Databases. **CCS 2015** [Google Scholar](https://scholar.google.com/scholar?q=IntegriDB%3A+Verifiable+SQL+for+Outsourced+Databases)
> 核心思路：使用双线性累加器和区间树构建可验证数据库，支持更广泛的 SQL 查询。
> 局限与区别：证明代价高，性能差。VeriDB 通过 SGX 和轻量级的存储层验证实现了更优性能。

[33] Wenting Zheng 等. Opaque: An Oblivious and Encrypted Distributed Analytics Platform. **NSDI 2017** [Google Scholar](https://scholar.google.com/scholar?q=Opaque%3A+An+Oblivious+and+Encrypted+Distributed+Analytics+Platform)
> 核心思路：基于 SGX 的注意隐匿分布式分析平台，确保查询处理中的完整性。
> 局限与区别：主要关注访问模式泄露防护，引入了巨大开销。VeriDB 不处理访问模式泄露，专注于更低开销的完整性验证。

### 核心技术与方案

VeriDB 的核心思路是将云数据库的验证任务分解为两个独立的部分：一个数据密集但逻辑简单的存储层，和一个逻辑复杂但内存占用小的查询引擎。存储层负责确保单个数据记录的完整性，查询引擎负责确保查询逻辑的正确性，两者通过可验证的访问方法接口连接。

**存储层设计：写-读一致内存与页结构。**

VeriDB 的基础是写-读一致内存 [5]。其核心思想是，通过维护两个集合，即读集 $RS$ 和写集 $WS$，来确保每次读操作返回的是最近一次写操作写入的值。系统维护这两个集合的哈希摘要 $h(RS)$ 和 $h(WS)$，定义为：
$$h(\mathcal{RS}) = \sum_{(addr, data) \in \mathcal{RS}}^{\oplus} PRF(addr, data)$$
其中 $PRF$ 是一个带密钥的伪随机函数，$\sum^{\oplus}$ 表示异或和。如果 $h(\mathcal{RS}) = h(\mathcal{WS})$，则 $RS = WS$ 具有高概率，从而保证了内存的完整性。

VeriDB 在此之上构建了页结构的可验证存储。为了支持证明记录的存在性或缺失性，每个记录被扩展存储为 $\langle key, nKey, data \rangle$，其中 $nKey$ 是大于当前 $key$ 的最小主键，数据项 $\langle \bot, min(key) \rangle$ 也被插入。这种设计使得一条记录本身就是它存在性的证据，而缺失性则由其前驱记录提供的 $key < query\_key < nKey$ 关系来证明。

**页层面优化**。为了提升性能，VeriDB 实现了多项优化：1）排除页面元数据验证，因为地址服务的正确性不影响数据完整性；2）在验证过程中进行页面压缩，将压缩所需的额外哈希更新与离线验证的扫描过程合并；3）仅扫描上次验证后有修改的页面，避免全量扫描；4）使用多个 $RSWS$ 对来降低锁竞争，实现细粒度并发控制。

**查询执行引擎设计。**

查询引擎运行在 SGX 飞地内，通过查询门户接收经过身份认证的查询，并在飞地内完成编译、优化和执行。这保证了查询逻辑的完整性。验证任务被下推至访问方法。点查询验证通过索引返回的 $\langle key, nKey \rangle$ 对，检查返回记录的 $key$ 是否等于查询值以证明存在性，或查询值是否落在 $key$ 和 $nKey$ 之间以证明缺失性。范围查询验证需要检查三个条件：第一个记录的 $key \le start$、最后一个记录的 $nKey \ge end$、以及所有返回记录的 $nKey_i = key_{i+1}$，形成一个无遗漏的键链。

为了支持非主键列上的查询，VeriDB 将存储模型扩展为支持多个键链：每个需要支持范围查询的列都维护一对 $\langle key_i, nKey_i \rangle$。这虽然增加了写入和存储开销，但实现了对多列访问方法的验证。

**安全性分析概要**。

完整性（Integrity）和完备性（Completeness）的证明都依赖于将查询引擎输出端的正确性归约到访问方法输入端的正确性。由于查询引擎位于 SGX 内，其输出可信。对于访问方法，其输入来自可验证存储层，该层确保任何绕过 API 的直接内存修改都会被写-读一致内存的验证过程检测到。因此，只要验证不失败，数据访问就将作用于正确的数据库状态。完备性则依赖于索引搜索和范围扫描的验证逻辑，这些逻辑通过存储层提供的不可伪造证据确保所有满足条件的记录都被返回。

### 核心公式与流程

**[写-读一致性内存的 ReadSet 哈希定义]**
$$h(\mathcal{RS}) = \sum_{(addr, data) \in \mathcal{RS}}^{\oplus} PRF(addr, data)$$
> 作用：通过异或和哈希来紧凑地表示整个读集，用于高效地验证其与写集的等价性。

**[非静默验证算法 (Algorithm 2)]**
$$
\text{VERIFY:} \\
\text{for each page } \in \text{memory:} \\
\qquad h(\mathcal{RS}^{current}) = h(\mathcal{RS}^{current}) \oplus PRF(addr, data) \\
\qquad h(\mathcal{WS}^{new}) = h(\mathcal{WS}^{new}) \oplus PRF(addr, data) \\
\text{if } h(\mathcal{RS}^{current}) \neq h(\mathcal{WS}^{current}) \text{ then return false else return true}
$$
> 作用：一个离线、并行的验证过程，通过扫描整个内存来使 $RS$ 和 $WS$ 一致，从而检测数据篡改。

**[页结构存储模型 (Definition 4.2)]**
$$r_i = \langle key, nKey, data \rangle$$
> 作用：定义了扩展的元组格式，其中 $nKey$ 是后继键，使得单个记录即可作为其存在性或其前驱与后继之间键的缺失性的证据。另外插入一条记录 $\langle \bot, min(key), - \rangle$ 来标识范围起点。

### 实验结果

所有实验在配备 Intel Xeon CPU E3-1270 v6 @ 3.80GHz CPU 和 64 GB RAM 的服务器上进行。微基准测试使用包含 100 万个键值对（4字节整数键，500 字节字符串值）的初始数据库，每次实验执行 10K 次混合读写操作。与基线（无验证）相比，VeriDB 的读写操作为维护 ReadSet/WriteSet 引入的开销在 1.5-2.2 微秒之间。排除页面元数据验证可将此开销降低约 20%。非静默验证以每 1000 次操作执行一次的频率运行时，引入的开销仅约为 1-4%，被认为非常低。与 MB-Tree [14] 相比，VeriDB 在读写延迟上实现了 94-96% 的降低（如 Get 操作延迟：VeriDB 为 2 微秒，MB-Tree 为 64 微秒），证明了其消除了 MHT 的并发瓶颈。在 TPC-H 基准测试中，VeriDB 对分析型工作负载引入了 9% 到 39% 的端到端开销。开销主要由扫描节点上的 RSWS 更新主导：对于计算密集型的 Q19（NestedLoopJoin），相对开销仅为 9%；对于扫描密集型的 Q1 和 Q6，相对开销高达 39%。在 TPC-C 基准测试中，VeriDB 在拥有 1024 个 RSWS 对时，交易吞吐量约为未保护数据库的 1/3 到 1/4，表明锁竞争问题可以通过增加 RSWS 数量得到有效缓解。

### 局限性与开放问题

首先，VeriDB 采用延迟验证，意味着篡改只能在内存扫描完成时被检测到，而非在查询执行时立即发现。其次，当查询中间结果（如物化点）超出飞地容量时，需要将其卸载到非信任内存，论文虽提及可复用 VeriDB 的存储层，但这会引入新的开销，如何高效处理大尺寸中间结果是未来工作。最后，VeriDB 依赖于 SGX 硬件，其 EPC 容量限制（目前仅 96 MB）仍然是系统设计中的关键约束，在扩展性方面存在客观瓶颈。

### 强关联论文

[1] Arvind Arasu et al. Concerto: A High Concurrency Key-Value Store with Integrity. **SIGMOD 2017** [Google Scholar](https://scholar.google.com/scholar?q=Concerto%3A+A+High+Concurrency+Key-Value+Store+with+Integrity)
[4] Sumeet Bajaj and Radu Sion. CorrectDB: SQL Engine with Practical Query Authentication. **VLDB 2013** [Google Scholar](https://scholar.google.com/scholar?q=CorrectDB%3A+SQL+Engine+with+Practical+Query+Authentication)
[5] Manuel Blum et al. Checking the Correctness of Memories. **FOCS 1991** [Google Scholar](https://scholar.google.com/scholar?q=Checking+the+Correctness+of+Memories)
[14] Feifei Li et al. Dynamic authenticated index structures for outsourced databases. **SIGMOD 2006** [Google Scholar](https://scholar.google.com/scholar?q=Dynamic+authenticated+index+structures+for+outsourced+databases)
[17] Frank McKeen et al. Innovative instructions and software model for isolated execution. **HASP 2013** [Google Scholar](https://scholar.google.com/scholar?q=Innovative+instructions+and+software+model+for+isolated+execution)
[26] Rohit Sinha and Mihai Christodorescu. VeritasDB: High Throughput Key-Value Store with Integrity. **IACR ePrint 2018** [Google Scholar](https://scholar.google.com/scholar?q=VeritasDB%3A+High+Throughput+Key-Value+Store+with+Integrity)
[30] Yupeng Zhang et al. vSQL: Verifying Arbitrary SQL Queries over Dynamic Outsourced Databases. **IEEE S&P 2017** [Google Scholar](https://scholar.google.com/scholar?q=vSQL%3A+Verifying+Arbitrary+SQL+Queries+over+Dynamic+Outsourced+Databases)
[31] Yupeng Zhang et al. IntegriDB: Verifiable SQL for Outsourced Databases. **CCS 2015** [Google Scholar](https://scholar.google.com/scholar?q=IntegriDB%3A+Verifiable+SQL+for+Outsourced+Databases)
[33] Wenting Zheng et al. Opaque: An Oblivious and Encrypted Distributed Analytics Platform. **NSDI 2017** [Google Scholar](https://scholar.google.com/scholar?q=Opaque%3A+An+Oblivious+and+Encrypted+Distributed+Analytics+Platform)


## 关键词

+ Intel SGX可信执行环境
+ 可验证数据库VeriDB
+ 页面结构存储验证
+ SQL查询可验证执行
+ 关系数据库完整性
+ 硬件信任锚