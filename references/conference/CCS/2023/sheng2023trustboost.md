---
title: "Trustboost: Boosting trust among interoperable blockchains"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2023
created: 2025-04-19 11:03:07
modified: 2025-04-19 11:06:47
---

## Trustboost: Boosting trust among interoperable blockchains

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3576915.3623080)

## 作者

+ Peiyao Sheng 
+ Xuechao Wang 
+ Sreeram Kannan 
+ Kartik Nayak 
+ Pramod Viswanath 

## 笔记

### 背景与动机
当前存在超过一千条区块链，各自拥有不同的信任/安全级别。信任保障较弱的区块链往往只能支持有限的应用场景。一种常见的解决方案是“借用”强安全性链的信任，例如通过检查点机制，弱链的验证者定期将区块哈希和签名作为检查点提交到强链，弱链的最终性规则被修改为遵循这些检查点。这种信任借用方式要求弱链放弃自身的主权，本质上是一种单向的信任转移，导致弱链的参与者失去影响共识决策的能力。本文旨在回答一个根本性问题：多个区块链应如何交互，以创建一个信任级别得到“提升”的组合账本？理想情况下，这种信任提升操作应通过智能合约提供，无需改变底层共识协议，即组成链在协同贡献的同时保持各自的主权。从技术上讲，这对应于一个长期存在的开放问题：在给定 m 个区块链账本，其中 f 个是拜占庭的（即无安全保障）时，能否在组合账本上达成共识？本文的目标是全面回答这一问题，涵盖从信任提升的不可行性结果、具有最优信任提升特性的具体协议，到在 Cosmos 生态系统中的全栈实现。

### 相关工作
[31] Karakostas et al. Securing proof-of-work ledgers via checkpointing. **IEEE ICBC 2021** [Google Scholar](https://scholar.google.com/scholar?q=Securing+proof-of-work+ledgers+via+checkpointing)
> 核心思路：通过将区块哈希和签名作为检查点提交到更安全的链，使弱链遵循检查点来借用信任。
> 局限与区别：这种方法是单向的信任转移，弱链需要放弃自身主权，且对参与者的共识影响力造成限制。

[21] Fitzi et al. Ledger combiners for fast settlement. **TCC 2020** [Google Scholar](https://scholar.google.com/scholar?q=Ledger+combiners+for+fast+settlement)
> 核心思路：在被动模式下，多个账本并行处理交易，观察者通过读取所有账本形成组合账本，实现相对持久性。
> 局限与区别：该组合账本仅保证相对持久性，不满足诚实终止性，无法有效支撑支付系统，实用性有限。本文的 TrustBoost-Lite 则实现了更优的 ABC 账本共识。

[3] Amir et al. Scaling byzantine fault-tolerant replication to wide area networks. **DSN 2006** [Google Scholar](https://scholar.google.com/scholar?q=Scaling+byzantine+fault-tolerant+replication+to+wide+area+networks)
> 核心思路：提出“共识之共识”的概念，先在每个局部站点运行 BFT 协议，再将局部站点视为单个逻辑可信节点参与全局协议。
> 局限与区别：该方法要求每个局部站点内存在诚实超多数，且需要修改局部共识，而本文的 TrustBoost 在全局层是轻量级的，仅通过智能合约实现，无需改动底层共识。

[18] Dwork et al. Consensus in the presence of partial synchrony. **JACM 1988** [Google Scholar](https://scholar.google.com/scholar?q=Consensus+in+the+presence+of+partial+synchrony)
> 核心思路：证明了在部分同步网络模型中，容忍 f 个拜占庭故障节点需要至少 3f+1 个节点。
> 局限与区别：该经典结论是针对消息传递模型。本文将其扩展到了存在拜占庭对象和拜占庭进程的共享内存模型，并得出了类似的边界条件。

[16] Cosmos. ICS ?: Recursive tendermint. [Google Scholar](https://scholar.google.com/scholar?q=ICS+?+Recursive+tendermint)
> 核心思路：提议使用 IBC 协议代替 TCP/IP，在多个 Cosmos 链上递归运行 Tendermint 共识。
> 局限与区别：该概念仅作为初步想法提出，未深入探讨其中涉及的科学和工程挑战，而本文 TrustBoost 实现了完整的理论分析和工程实现。

[2] Abraham et al. Information theoretic hotstuff. **arXiv 2020** [Google Scholar](https://scholar.google.com/scholar?q=Information+theoretic+hotstuff)
> 核心思路：提出信息论热stuff（IT-HS）共识协议，无需 PKI，具有乐观响应特性。
> 局限与区别：IT-HS 具有二次方消息复杂度，但避免了签名验证等昂贵操作。本文 TrustBoost 选用 IT-HS 作为底层共识协议，以适配 Cosmos IBC 缺乏签名传递能力的限制。

[55] Xue et al. Cross-chain state machine replication. **arXiv 2022** [Google Scholar](https://scholar.google.com/scholar?q=Cross-chain+state+machine+replication)
> 核心思路：提出被动模式下的跨链状态机复制协议，旨在跨多条链维持一致状态。
> 局限与区别：该工作的安全保障要求所有参与的区块链都是安全的，而本文 TrustBoost 在被动模式下也要求 m > 3f，但主动模式下的 TrustBoost 协议可以容忍 f 条链失效。

### 核心技术与方案
本文的核心贡献在于形式化地研究了跨链信任提升问题，并在经典的共享内存模型下扩展了对象间通信的能力。该工作首先将参与组合的区块链建模为共享对象，将区块链客户端建模为进程。在此基础上，区分了两种交互模式：被动模式（对象间无通信）和主动模式（对象间通过跨链通信 CCC 进行消息传递）。

在理论基础方面，论文系统性地证明了在不同模式下的共识边界。在被动模式下，由于对象间无法通信，任何形式的总序共识（Definition 1, Ledger Consensus）在存在任意一个拜占庭对象（f > 0）时都是不可能的，因为拜占庭对象可以对不同进程展示不同视图，导致一致性违反。然而，一个更弱但仍有用的共识——异步区块链共识 ABC（Definition 5, ABC Ledger Consensus）在该模式下是可实现的，其必要和充分条件是 m > 3f。支持此结论的核心构造（TrustBoost-Lite）如下：客户端将一个交易提交给所有 m 条链，然后检查是否有超过 2/3 的链提交了该交易，且该交易的所有输入均来自已被全局提交的交易。由于任意两个超过 2/3 的集合必定有重叠于一个诚实链，因此不可能有冲突交易被提交（弱一致性）。诚实终止性则来源于如果所有诚实链都收到无冲突交易，该交易最终会被提交。在主动模式下，通过 CCC 支持的跨链通信，对象可以模拟经典的消息传递模型，因此存在已证明的 BFT 共识协议。定理 4.1 证明了在此模式下实现总序共识的必要和充分条件是 m > 3f。TrustBoost 协议正是基于此构造的，它实际上是一个运行在区块链之上的、轻量级的许可型 BFT 共识协议。

TrustBoost 和 TrustBoost-Lite 的具体构造体现了理论导向设计。TrustBoost 协议利用 CCC 作为通信通道，在 m 条区块链上运行一个 BFT 共识协议（例如，信息论热stuff IT-HS [2]）。以算法 1 中的多数投票协议为例，客户端向所有链广播提议；每条链收到提议后广播投票；当一条链收集到超过 2/3 的投票后，将交易提交到本地链。客户端在检查时，只要在超过 m/3 条本地链上确认交易被提交，就认为该交易被全局提交。此处的阈值设计 (2/3 和 1/3) 在数学上确保了当 f < m/3 时，全局一致性得以保证：因为任何两个超过 2/3 的集合必有交集，而该交集的大小满足联邦拜占庭协议 (SBA) 的要求。TrustBoost 作为代理，还有严格的接口约束，例如 AppX 合同会检查函数调用是否来自被认证的 TrustBoost 合同。

实验与实现部分展示了这些协议在 Cosmos 生态系统中的可行性，在 3f+1 条链上运行 TrustBoost 合同。针对 IBC 消息在链上验证后会移除签名的问题，限制了 PKI 的使用，因此实现中选择了不需要 PKI 的信息论热stuff协议，但引入了二次方消息复杂度的代价。实现中还解决了智能合约单线程、无法自发送 IBC 消息等工程挑战，通过消息队列机制来确保 BFT 协议中的各步骤能被正确触发和序列化。

### 核心公式与流程

**[ABC 共识阈值 (被动模式)]**
$$ m > 3f $$
> 作用：这是 TrustBoost-Lite 协议（被动模式）能够实现 ABC（异步区块链共识）的充分必要条件，是协议设计的理论基石。

**[TrustBoost 提交检查条件]**
$$ cnt \ge \lfloor 2m/3 \rfloor + 1 $$
> 作用：在 TrustBoost 协议（主动模式）中，当一条链的投票计数器达到该阈值时，触发交易在本地链的提交。

**[TrustBoost 全局许诺验证条件]**
$$ cnt \ge \lfloor m/3 \rfloor + 1 $$
> 作用：客户端通过 TrustBoost.check() 验证交易是否被全局提交。当查询到有超过该阈值的本地链提交了该交易时，视为全局提交。

**[TrustBoost-Lite 提交检查条件]**
$$ cnt \ge \lfloor 2m/3 \rfloor + 1 \ \text{and} \ \text{valid}(tx) $$
> 作用：在 TrustBoost-Lite 协议（被动模式）中，客户端检查交易是否被超过 2/3 的链提交且其所有输入均为已被全局提交的交易。

### 实验结果
实验在 AWS m5.4xlarge 实例上进行，部署了 4、7、10 条 Cosmos 链实例，链的出块率约为 1 秒/块。实验评估了 TrustBoost 的性能，以单链操作作为基线。随着 m 从 1 增加到 10，IBC 消息数从 0 增长到 738，Gas 使用量从 202K 增长到 586M（百万），延迟从 2.5 秒增长到 138.2 秒。Gas 和 IBC 消息数呈二次方增长，主要开销来自 IT-HS 协议通信和 TrustBoost 合同本身，而延迟则近似线性增长。在安全性测试中，在一个包含 4 条链（容忍 1 个拜占庭故障）的系统中，测试了四种攻击：主链崩溃、主链发送不一致提议、非主链发送不一致投票、非主链持续发送中止消息。前两种攻击导致视图切换，使延迟从约 67 秒翻倍至约 138 秒，后两种攻击对延迟影响甚微。在 2023 年 4 月的币价和 Gas 价格下，10 条链的 Gas 成本约为 2-10 美元，与以太坊等高安全链的成本相当。

### 局限性与开放问题
1. 权重动态调整：论文中假设所有参与链具有相同权重，但实际中可根据链的市值等指标分配不同投票权重，如何动态调整这些权重以适应链的安全变化是一个开放问题。
2. 异构链支持：当前 TrustBoost 实现依赖于 Cosmos 同构生态（IBC），但扩展到异构链（如以太坊）需要处理不同虚拟机、不同语言编写智能合约以及异构跨链通信（如 zkBridge [54]）的挑战。
3. 效率优化：IT-HS 协议具有二次方消息复杂度，导致 Gas 和延迟随链数量增长较快。采用基于签名聚合的 BFT 协议（如 HotStuff [56]）或优化 IBC 性能可进一步提升 TrustBoost 效率。

### 强关联论文
[31] Karakostas et al. Securing proof-of-work ledgers via checkpointing. **IEEE ICBC 2021** [Google Scholar](https://scholar.google.com/scholar?q=Securing+proof-of-work+ledgers+via+checkpointing)

[21] Fitzi et al. Ledger combiners for fast settlement. **TCC 2020** [Google Scholar](https://scholar.google.com/scholar?q=Ledger+combiners+for+fast+settlement)

[3] Amir et al. Scaling byzantine fault-tolerant replication to wide area networks. **DSN 2006** [Google Scholar](https://scholar.google.com/scholar?q=Scaling+byzantine+fault-tolerant+replication+to+wide+area+networks)

[18] Dwork et al. Consensus in the presence of partial synchrony. **JACM 1988** [Google Scholar](https://scholar.google.com/scholar?q=Consensus+in+the+presence+of+partial+synchrony)

[2] Abraham et al. Information theoretic hotstuff. **arXiv 2020** [Google Scholar](https://scholar.google.com/scholar?q=Information+theoretic+hotstuff)

[56] Yin et al. Hotstuff: Bft consensus with linearity and responsiveness. **PODC 2019** [Google Scholar](https://scholar.google.com/scholar?q=Hotstuff:+Bft+consensus+with+linearity+and+responsiveness)

[47] Sliwinski et al. Abc: Proof-of-stake without consensus. **arXiv 2019** [Google Scholar](https://scholar.google.com/scholar?q=Abc:+Proof-of-stake+without+consensus)

[50] Tas et al. Bitcoin-enhanced proof-of-stake security: Possibilities and impossibilities. **arXiv 2022** [Google Scholar](https://scholar.google.com/scholar?q=Bitcoin-enhanced+proof-of-stake+security:+Possibilities+and+impossibilities)

[57] Zamyatin et al. Sok: Communication across distributed ledgers. **FC 2021** [Google Scholar](https://scholar.google.com/scholar?q=Sok:+Communication+across+distributed+ledgers)

[54] Xie et al. zkbridge: Trustless cross-chain bridges made practical. **arXiv 2022** [Google Scholar](https://scholar.google.com/scholar?q=zkbridge:+Trustless+cross-chain+bridges+made+practical)


## 关键词

+ 区块链互操作性
+ 跨链协议
+ 共识机制
+ 信任增强
+ 智能合约
+ 拜占庭容错