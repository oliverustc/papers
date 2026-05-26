---
title: "CrowdProve: Community Proving for ZK Rollups"
标题简称:
论文类型: preprint
预印本简称: arxiv
发表年份: 2025
modified: 2025-04-09 14:06:01
---

## CrowdProve: Community Proving for ZK Rollups

## 发表信息

+ [原文链接](https://arxiv.org/abs/2501.03126)

## 作者

+ John Stephan
+ Matej Pavlovic
+ Antonio Locascio
+ Benjamin Livshits

## 笔记

### 背景与动机

零知识（ZK）Rollups通过将Layer 2交易聚合成单一批次并提交有效性证明到Layer 1，显著提升了区块链系统的吞吐量并降低了费用[7]。然而，生成这些有效性证明所需的计算开销极大，通常比交易执行本身高出数个数量级，这对系统性能和去中心化构成了严峻挑战。现有的解决方案，如ZKsync的Boojum证明系统[7]，依赖集中式的云基础设施来处理证明生成任务，虽然性能可靠，但基础设施成本高昂，且限制了更广泛的社区参与。这种集中式的证明生成模式成为了ZK Rollup去中心化的一个关键瓶颈。为了降低运营成本并朝去中心化迈出有意义的一步，本文提出了一种名为CrowdProve的方案，旨在通过一个名为Job Distributor（JD）的协调层，将对计算资源要求高且易于并行化的证明任务，安全地外包给运行消费级硬件（如个人电脑）的社区参与者。

### 相关工作

[6] Wu et al. DIZK: A Distributed Zero Knowledge Proof System. **NDSS 2018** [Google Scholar](https://scholar.google.com/scholar?q=DIZK%3A+A+Distributed+Zero+Knowledge+Proof+System)
> 核心思路：开创性地将ZK证明生成任务分布到一个可信的计算集群（如数据中心内的多台机器）上，利用并行化处理远超单机能力的电路。
> 局限与区别：DIZK假设机器是可信且位于同一高速网络内，其设计目标是性能最大化而非去中心化。CrowdProve与之不同，专注于利用互联网连接的不信任社区硬件，提供一个处理不可靠性和潜在恶意行为的协调层。

[3] Liu et al. Pianist: Scalable zkRollups via Fully Distributed Zero-Knowledge Proofs. **ACM CCS 2021** [Google Scholar](https://scholar.google.com/scholar?q=Pianist%3A+Scalable+zkRollups+via+Fully+Distributed+Zero-Knowledge+Proofs)
> 核心思路：提出了一个完全分布式的Plonk证明系统，将证明任务分割到多台机器上执行，仅需极少的机器间通信。
> 局限与区别：Pianist的分布式方案旨在将证明时间从单机显著缩短到集群级别，但其实验使用了256 GB RAM的高端机器，这排除了大多数社区参与者的消费级硬件。CrowdProve则反其道而行之，将已有的、可并行化的子证明任务（子任务）直接分发给数量众多的、硬件能力参差不齐的社区证明者。

[2] Li et al. HyperPianist: Pianist with Linear-Time Prover via Fully Distributed HyperPlonk. **iacr 2024** [Google Scholar](https://scholar.google.com/scholar?q=HyperPianist%3A+Pianist+with+Linear-Time+Prover+via+Fully+Distributed+HyperPlonk)
> 核心思路：在Pianist基础上，通过分布式SumCheck协议实现了线性时间的证明者复杂度和对数级的通信开销。
> 局限与区别：方案仍主要针对计算集群设计，其关注点在于证明复杂度的理论优化，而非社区驱动的硬件利用率和拜占庭容错。CrowdProve的应用场景更侧重于工程实践中的社区协调与激励机制。

[4] Nguyen et al. Mangrove: A Scalable Framework for Folding-based SNARKs. **USENIX Security 2024** [Google Scholar](https://scholar.google.com/scholar?q=Mangrove%3A+A+Scalable+Framework+for+Folding-based+SNARKs)
> 核心思路：提出了一个用于生成折叠式SNARKs的通用框架，通过“统一化”编译器将NP陈述转化为一系列相同步骤，以支持高效的增量可验证计算。
> 局限与区别：Mangrove的核心贡献在于提升底层证明系统的内存效率和并行化潜力，但并未解决如何将这些计算安全地外包给不可信网络节点的问题。CrowdProve可以视作一个在Mangrove这类高效证明系统之上的协调层。

[5] Sang et al. Ou: Automating the Parallelization of Zero-Knowledge Protocols. **ACM CCS 2023** [Google Scholar](https://scholar.google.com/scholar?q=Ou%3A+Automating+the+Parallelization+of+Zero-Knowledge+Protocols)
> 核心思路：设计了一种新的编程语言Ou和配套的Lian编译器，能自动分析ZK程序并将其分割成可跨计算集群并行执行的优化片段。
> 局限与区别：Ou/Lian专注于简化ZK证明的并行编程，而非解决分布式系统中不信任节点的协调和安全性问题。CrowdProve的JD和LRP机制正是为解决这些问题而设计的。

### 核心技术与方案

CrowdProve的整体框架包含三个核心组件：核心Rollup系统、Job Distributor（JD）和社区证明者。

**1. 社区证明者模块与Job Distributor (JD)**
核心设计思路是将证明者从集中式系统中解耦。社区证明者模块是一个可公开下载的软件，安装后能接收见证数据作为输入（约470 KB），计算并返回对应的简洁证明（约742 KB）。JD是连接核心系统和社区证明者的中心化协调代理。JD从Rollup系统的作业数据库中获取任务，将其分配给请求任务的社区证明者，并跟踪所有作业状态。当证明者通过`submit_result` API提交证明后，JD进行轻量级验证（通常只需数十毫秒），验证通过后更新数据库并触发对证明者的补偿。JD被设计为尽可能无状态，证明者通过持续轮询（polling）`get_job` API来获取新任务，这种轮询机制避免了维护注册表带来的开销。

**2. Least-Recently-Processed (LRP) 作业重新分配机制**
这是实现拜占庭容错的关键创新。传统系统（如ZKsync）依赖核心系统的超时机制（10分钟）来处理失败或作恶的证明者。CrowdProve将重新分配逻辑下沉到JD层，引入LRP机制。JD维护一个本地待处理作业队列（queue）。当一个社区证明者请求新任务时，JD首先从核心数据库获取新作业；若没有新作业，则将队列头部的作业（即最久未被完成的作业）分配给该证明者。这意味着同一个作业（具有同一`job_id`）可能被同时分配给多个证明者。JD使用自增的`request_id`来区分同一`job_id`的多次分配，并在哈希表中维护`job_id`与所有`request_id`的映射。当JD收到提交时，若`(job_id, request_id)`对是有效的，才进行验证。若第一个证明者的证明未能通过验证或耗时过长，作业仍在队列中，可被迅速重新分配给下一个证明者。这有效防止了恶意证明者通过垄断作业（Job Hogging）来实施拒绝服务攻击，因为被垄断的作业会一直在队列中被重新分配。

**3. 证明过程**
完整的证明过程如下：
1. **作业请求**：社区证明者通过调用JD的`get_job` API轮询请求任务。
2. **作业获取与分配**：JD从核心Rollup系统的数据库中检索下一个可用作业。若没有新作业，则从本地队列的头部取出一个待处理作业（触发LRP机制）。JD递增一个本地计数器作为`request_id`，将作业和`request_id`一起分配给证明者，并将该作业标记为“运行中”。如果是新作业，则加入队列尾部；如果是待处理作业，则将其移动到队列尾部，使其成为“最近处理的”作业。JD更新内部哈希表，键为`job_id`，值为所有相关的`request_id`。
3. **证明计算**：证明者使用其硬件（CPU、GPU等）计算证明。
4. **证明提交**：证明者调用JD的`submit_result` API，提交证明及对应的`(job_id, request_id)`对。
5. **证明验证**：JD检查`(job_id, request_id)`对是否存在于哈希表中。若否，则丢弃（可能为欺诈企图）。若是，则验证证明的正确性。验证过程涉及检查密码学条件而非重新计算整个证明，因此开销极小。
6. **最终确认与补偿**：验证成功后，JD在核心系统数据库中标记作业为“完成”，从本地队列和哈希表中移除该作业及其所有`request_id`。JD会补偿第一个提交有效证明的社区证明者。成功删除键后，其他并行为同一`job_id`提交的证明将被系统忽略。

**4.安全性直觉**
系统的安全性建立在对子证明的轻松可验证性上。由于最终的有效性证明是通过递归聚合大量子证明构建的，每个子证明本身都是正确且易于验证的。JD只需验证子证明的有效性，而无需了解或信任计算它的证明者。结合LRP机制，任何失效或恶意行为只会导致作业被重新分配，不影响系统整体进度。补偿机制（如验证通过才支付）和经济惩罚（如未来可引入的加密债券）从激励机制上威慑了恶意行为。

**5. 复杂度分析**
- **通信量**：每个作业的通信带宽需求极低。输入（见证）约470 KB，输出（证明）约742 KB。JD与核心系统的交互主要是作业状态更新。网络延迟（约10毫秒）远小于计算时间，因此带宽不是瓶颈。JD的验证开销仅为每证明数十毫秒。
- **计算量**：证明者的计算开销由其硬件决定（如表1所示）。对于JD，其计算开销极小，主要是哈希表查找、队列操作和轻量级的证明验证，因此即便面对数千个证明者，JD也不易成为瓶颈。整个系统的总证明时间理论上可由$T_{total} = \frac{N_{jobs} \times T_{job}}{N_{provers}}$近似表示（理想情况下，$T_{job}$为单作业平均证明时间，$N_{provers}$为并发证明者数量），证明了其近似的线性可扩展性（如实验部分表3和图3所示）。

### 核心公式与流程

**[总证明时间公式（理想并行情况）]**
$$T_{batch} = \frac{J_{batch} \cdot T_{job}}{P_{concurrent}}$$
> 作用：用于估算在理想并行和分配下，完成一批包含 $J_{batch}$ 个作业的批次所需的总时间。$T_{job}$ 是给定硬件配置下的单作业平均证明时间，$P_{concurrent}$ 是并发工作的社区证明者数量。这是实验部分进行性能外推的理论基础。

**[作业重新分配流程（LRP机制核心）]**
> 作用：描述JD在收到证明者请求（`get_job`）时，如何利用LRP机制进行作业分配，以应对作业短缺或证明者失效的情况。
>
> 1. 证明者调用 `get_job`。
> 2. JD从核心Rollup数据库检索下一个可用作业。
> 3. **如果** 有可用新作业：
>    *   将新作业分配给证明者。
>    *   将新作业加入本地队列尾部。
> **否则**：
> *   从本地队列头部取出并分配一个待处理作业。
> *   若作业与新分配的是同一`job_id`，生成新`request_id`进行区分。
>    *   将该作业移动到本地队列尾部（使其成为“最近处理的”）。
> 4. JD将分配信息(`job_id`, `request_id`)记录到哈希表中。
> 5. 返回作业给证明者。

### 实验结果

实验评估了CrowdProve在四种硬件配置下的性能：8核CPU、16核CPU、Apple M3 Max MacBook和L4 GPU。实验以一个包含17,188个作业的真实ZKsync批次（批次号491452）为基准。核心性能数值如表1和表2所示。实验结果表明，使用3,000个8核CPU的社区证明者可以在9.32分钟内完成该批次，显著快于当前ZKsync集中式部署的38.70分钟，实现了约4倍的加速。与集中式方案的“盈亏平衡点”分别是723个8核CPU证明者、502个16核CPU证明者、359台MacBook或107个GPU证明者即可匹敌现有系统性能。一项针对100个作业的分布式测试（表3、图3）验证了系统的近乎线性可扩展性，当证明者数量从5台增加到20台时，完成100个作业所需时间从37.11分钟降至9.12分钟。在成本方面，假设社区证明者每作业获得0.06美分补偿，使用360台MacBook即可在匹敌集中式性能的同时将成本减半（相比集中式系统的每作业0.12美分）。网络延迟被测量为平均约10毫秒，相对于秒级的计算时间可以忽略。

### 局限性与开放问题

CrowdProve目前仍是一个技术上中心化的系统，因为Job Distributor（JD）的协调和控制权完全掌握在Rollup运营商手中，这构成了单点故障。未来需要研究如何将JD的协调逻辑本身也去中心化，例如将其建模为一个运行在现有区块链（甚至Rollup自身）上的去中心化状态机，但这会引入最终性和回滚问题。此外，可以探索引入更智能的作业分配算法（如根据证明者的历史可靠性或硬件类型进行差异化分配），以及设计更复杂的补偿模型（如自适应定价或加密债券），以进一步优化系统效率和安全性。

### 强关联论文

[6] Wu et al. DIZK: A Distributed Zero Knowledge Proof System. **NDSS 2018** [Google Scholar](https://scholar.google.com/scholar?q=DIZK%3A+A+Distributed+Zero+Knowledge+Proof+System)

[3] Liu et al. Pianist: Scalable zkRollups via Fully Distributed Zero-Knowledge Proofs. **ACM CCS 2021** [Google Scholar](https://scholar.google.com/scholar?q=Pianist%3A+Scalable+zkRollups+via+Fully+Distributed+Zero-Knowledge+Proofs)

[7] ZKSync. ZKSync: Scaling Ethereum with Zero-Knowledge Proofs. [Google Scholar](https://scholar.google.com/scholar?q=ZKSync%3A+Scaling+Ethereum+with+Zero-Knowledge+Proofs)


## 关键词

+ CrowdProve社区证明ZK卷叠
+ 证明者编排外包计算去中心化
+ 商用硬件区块链扩容方案
+ ZK卷叠有效性证明生成
+ 去中心化证明者激励机制