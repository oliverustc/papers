---
title: "zkBridge: Trustless Cross-chain Bridges Made Practical"
标题简称: zkBridge
论文类型: conference
会议简称: CCS
发表年份: 2022
modified: 2025-04-29 16:14:24
created: 2025-04-07 16:27:45
---

## zkBridge: Trustless Cross-chain Bridges Made Practical

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3548606.3560652)

## 作者

+ [Tiancheng Xie](Tiancheng%20Xie.md)
+ [Jiaheng Zhang](Jiaheng%20Zhang.md)
+ [Zerui Cheng](Zerui%20Cheng.md)
+ [Yupeng Zhang](Yupeng%20Zhang.md)
+ [Dan Boneh](Dan%20Boneh.md)
+ [Dawn Song](Dawn%20Song.md)

## 笔记

好的，作为一名密码学领域的研究助手，我将根据您提供的论文全文，按照指定格式输出详尽的结构化笔记。

---

### 背景与动机
跨链桥是异构区块链生态系统互操作性的关键基础设施。然而，现有的跨链桥解决方案在安全性和性能之间存在根本性的权衡。基于轻客户端协议的桥（如SPV）虽然信任假设少，但在非PoW链（如PoS链）上验证区块头会产生高昂的链上计算和存储成本，例如在以太坊上验证单个Cosmos区块头需约6400万gas。为了追求效率，许多实用桥（如PolyNetwork、Wormhole、Ronin）采用委员会验证方式，但这种方法引入了额外的信任假设，即委员会节点的诚实多数，且小委员会的设置容易导致单点故障，频繁的攻击事件已造成超过15亿美元的损失。本文旨在填补这一空白，设计一个既保持强安全（不引入额外信任假设）又具备实用性能的跨链桥，具体目标是利用zk-SNARK技术，将跨链验证的链上成本降低数个数量级，并确保安全性仅依赖于底层区块链的安全性。

### 相关工作

[3] 无作者. **Poly Network** 2020 [Google Scholar](https://scholar.google.com/scholar?q=Poly+Network)
> 核心思路：一种使用侧链作为中继、采用两阶段提交协议实现资产跨链转移的互操作性协议。
> 局限与区别：其安全性依赖于一个委员会节点集合。本文提出的zkBridge旨在通过零知识证明来消除对任何中心化或外部委员会的信任需求。

[4] 无作者. **Rainbow Bridge** 2020 [Google Scholar](https://scholar.google.com/scholar?q=Rainbow+Bridge)
> 核心思路：由NEAR Protocol提出的乐观桥协议，依赖经济激励和监督服务（watchdog）来保证跨链状态更新的正确性。
> 局限与区别：乐观协议需要更长的确认延迟（如4小时）以待挑战窗口关闭，且参与者需要质押高额保证金。zkBridge使用零知识证明提供即时、加密保证的最终确定性。

[5] 无作者. **Wormhole Solana** 2020 [Google Scholar](https://scholar.google.com/scholar?q=Wormhole+Solana)
> 核心思路：一种通用消息传递协议，其安全性由一个“守护者（guardian）”节点网络维护。
> 局限与区别：其安全假设依赖于至少2/3的守护者节点是诚实的。本文提出的方案是“无需信任的”，其正确性仅依赖于底层区块链和密码学协议的安全假设。

[7] 无作者. **Nomad Protocol** 2021 [Google Scholar](https://scholar.google.com/scholar?q=Nomad+Protocol)
> 核心思路：另一个基于经济激励的乐观跨链协议，使用挑战-响应机制来确保状态更新的正确性。
> 局限与区别：同样面临乐观协议固有的长确认延迟问题。相比之下，zkBridge利用紧凑证明在安全性和延迟之间取得了更好的平衡。

[76] Jiaheng Zhang, Tiancheng Xie, Y. Zhang, and D. Song. **Transparent Polynomial Delegation and Its Applications to Zero Knowledge Proof** 2020 IEEE Symposium on Security and Privacy (SP) [Google Scholar](https://scholar.google.com/scholar?q=Transparent+Polynomial+Delegation+and+Its+Applications+to+Zero+Knowledge+Proof)
> 核心思路：提出了Virgo协议，一种无需可信设置、具备后量子安全属性的高效零知识证明系统，具有快速的证明生成和简洁的验证时间。
> 局限与区别：在zkBridge的应用场景下（需验证数百个签名），原始Virgo的证明生成时间仍不够快。本文的deVirgo协议在其基础上进行了分布式并行化改造，实现了线性加速。

[76] 嵌入到上面那条里

[54] Jens Groth. **On the Size of Pairing-Based Non-interactive Arguments** 2016 EUROCRYPT [Google Scholar](https://scholar.google.com/scholar?q=On+the+Size+of+Pairing-Based+Non-interactive+Arguments)
> 核心思路：提出了Groth16，一种基于椭圆曲线配对的zk-SNARK，拥有目前已知的最短证明大小（常数级别）和高效的验证器。
> 局限与区别：Groth16的证明生成代价高昂，难以直接用于zkBridge中的大型电路。本文将其用于压缩deVirgo的证明，以实现链上极低的验证成本。

[53] Shafi Goldwasser, Yael Tauman Kalai, and Guy N. Rothblum. **Delegating Computation: Interactive Proofs for Muggles** 2015 J. ACM [Google Scholar](https://scholar.google.com/scholar?q=Delegating+Computation:+Interactive+Proofs+for+Muggles)
> 核心思路：提出了GKR协议，一种用于分层算术电路的交互式证明系统，其验证时间仅依赖于电路深度。
> 局限与区别：GKR协议是Virgo和deVirgo中构建sumcheck方程的基础组件。本文在其基础上，针对数据并行电路，设计了分布式的sumcheck协议。

[60] Silvio Micali. **Computationally Sound Proofs** 2000 SIAM J. Comput [Google Scholar](https://scholar.google.com/scholar?q=Computationally+Sound+Proofs)
> 核心思路：提出了CS Proofs的思想，证明了存在一种证明系统，其证明和验证的复杂性远小于验证计算本身，是SNARK概念的先驱。
> 局限与区别：其构造依赖于随机预言机模型。Virgo和deVirgo沿用此模型实现非交互式证明，并保证知识的可靠性。

[45] Alessandro Chiesa, Dev Ojha, and Nicholas Spooner. **Fractal: Post-quantum and Transparent Recursive Proofs from Holography** 2020 EUROCRYPT [Google Scholar](https://scholar.google.com/scholar?q=Fractal:+Post-quantum+and+Transparent+Recursive+Proofs+from+Holography)
> 核心思路：提出了Fractal，一个后量子安全的、透明的且支持递归证明的zk-SNARK系统。
> 局限与区别：本文的递归证明思路（先用deVirgo生成证明，再用Groth16压缩）与Fractal不同，目的是为了在支持EVM的链上实现最极致的验证效率（利用曲线兼容性）。

### 核心技术与方案

zkBridge采用模块化设计，将应用逻辑与核心桥功能分离。其核心工作流程如下：1) 区块头中继网络中的节点将源链的区块头和零知识证明一起提交给目标链上的更新器合约；2) 更新器合约验证证明，并将区块头存入其持久化存储中；3) 应用合约可从更新器合约查询区块头，并结合用户提供的Merkle证明等完成特定验证，如验证交易包含性。

整个系统的安全性依赖于一个关键定理：假设中继网络中至少有一个诚实节点，源链是一致且活跃的，且源链的轻客户端验证器满足定义2.1，zk-SNARK协议是可靠的，那么zkBridge满足一致性和活跃性。证明思路是将更新器合约维护的有向无环图（DAG）通过某种算法（如最重链）转化为一个主链列表，由于存在诚实的证明者，基于证明系统的可靠性，更新器合约正确运行轻客户端协议，从而保证主链与所有诚实节点视图一致。

技术核心在于证明生成。zkBridge需要为PoS链（如Cosmos）的每个区块头生成证明，实质是证明该区块头被由前一个区块指定的验证者委员会正确签名。由于不同区块链（如Cosmos的Curve25519与Ethereum的BN254）使用不同的椭圆曲线，将EdDSA签名验证表示为算术电路时，每个签名需要约200万个门，验证约32个签名就需要超过6400万个门。为此，本文提出了两项创新技术：deVirgo和递归验证。

首先，deVirgo是一个针对数据并行电路的分布式零知识证明协议。数据并行电路包含多个结构相同的子电路副本（如多个签名验证子电路）。deVirgo的核心思想是将Virgo协议中的sumcheck协议和多项式承诺方案并行化。在分布式sumcheck中，每个机器处理一个子电路，将其生成的单变量多项式发送给主节点聚合，主节点再将聚合后的多项式发给验证者。通过这种方式，总通信量和证明大小与原始Virgo相同，但生成时间被N台机器线性加速。在分布式多项式承诺中，每个机器计算其子电路多项式在扩展域上的求值，然后将这些值的每个索引聚合起来构建一个Merkle树，从而将N个承诺聚合成一个，证明大小从O(λN(ℓ-n)²)降至O(λ(N+ℓ²))。最终，deVirgo对N个副本的电路实现了近乎N倍的加速，而证明大小仅略有增加。该协议是论证系统，满足完备性和知识可靠性。

其次，为降低链上验证成本，zkBridge采用递归证明技术。由于deVirgo的证明仍较大（约200KB），不适合直接在EVM上验证，而Groth16在EVM上验证成本极低（220K gas）。因此，zkBridge采用两层递归：第一层使用deVirgo为原始大型电路（如验证32个签名）生成证明π₁π₁；第二层，利用Groth16为验证π₁π₁的电路（即deVirgo的验证器）生成一个更短的证明π₂π₂。由于deVirgo的验证电路大小几乎不随原始电路的子副本数量增加而增加（GKR部分大小固定，PC部分增长缓慢），因此第二层Groth16的证明生成时间仅占第一层的25%。最终，链上只需验证这个131字节的Groth16证明，将gas成本从估算的7800万降至22.1万。

### 核心公式与流程

**[定义2.1 轻客户端协议]**
一个轻客户端协议使节点能够同步区块链的区块头。对于任一节点本地视图的块头`LOGH_i^r = [blkH_1, blkH_2, ..., blkH_r]`，该协议满足：1) 简洁性：每个状态更新只需常数时间；2) 活跃性：若一笔交易被诚实全节点接收，其所在区块最终会被包含在轻客户端的视图中；3) 一致性：与全节点的一致性定义一致，但针对的是块头列表。
> 作用：形式化定义了轻客户端协议必须满足的安全属性，是zkBridge协议安全论证的基础。

**[式(1) GKR sumcheck方程]**
$$
\tilde{V}_i(\mathbf{g}) = \sum_{\mathbf{x} \in \{0, 1\}^\ell} f(\mathbf{x}, \tilde{V}_{i+1}(\mathbf{x}))
$$
其中 $f$ 是某个多项式，$\mathbf{g}$ 是随机向量，$\tilde{V}_i$ 是第 $i$ 层门值的多元线性多项式。
> 作用：这是GKR协议的核心方程，将关于第 $i$ 层输出值的断言归约到关于第 $i+1$ 层输入值的断言。在整个Virgo/ZK协议中，通过反复调用sumcheck协议来证明该方程成立，从而最终将计算归约到输入层的直接验证。

**[式(2) 分布式PC中的函数聚合]**
$$
f(\mathbf{r}) = \sum_{i=0}^{N-1} \tilde{\beta}(\mathbf{r}[\ell-n+1:\ell], \mathbf{i}) f^{(i)}(\mathbf{r}[1:\ell-n])
$$
其中 $f$ 是全局多项式，$f^{(i)}$ 是第 $i$ 个子电路的多项式，$\tilde{\beta}$ 是单位函数的多元线性扩展，$\mathbf{r}$ 是随机挑战向量。
> 作用：此公式是分布式多项式承诺方案的核心。它将一个大多项式 $f$ 在点 $\mathbf{r}$ 上的求值，分解为多个子多项式 $f^{(i)}$ 在点 $\mathbf{r}[1:\ell-n]$ 上的求值的加权和。这允许各节点独立计算自己的子多项式，再聚合验证。

### 实验结果

实验在包含128个AWS EC2 c5.24xlarge实例（每个配置Intel Xeon Platinum 8275CL CPU @ 3.00GHz，192GB RAM）的数据中心环境中进行。核心实验对比了deVirgo与原始Virgo在Cosmos区块头验证证明生成任务上的性能（图2）。结果表明，当验证128个签名时，原始Virgo需要1500秒，而128台机器的deVirgo仅需10秒，实现了150倍加速。对于实际场景（验证32个签名），deVirgo在32台机器上仅需约10秒。在递归证明方面，表2显示，对于32个签名的场景，deVirgo生成证明耗时12.8秒，而第二层Groth16递归证明生成耗时5.41秒，总计18.21秒。证明大小从无递归时的1.9MB（1952492字节）骤降至131字节。链上验证gas成本从约7800万降至22.1万（221K gas），且该成本与签名数量无关。通信损耗方面，对于32个签名，32台机器的机器间总通信量约为32.24 GB，单机约1.01 GB。通过批处理（batch=32）技术，zkBridge的确认延迟（含等待区块和证明生成时间）可控制在2分钟以内。

### 局限性与开放问题
本文方案主要针对Cosmos到Ethereum方向进行了实现和评估，而反向（Ethereum到Cosmos）的实现需要特殊处理Ethereum的EthHash PoW算法，虽然论文提出了预计算DAG哈希的解决方案，但仍需进一步的工程实践。此外，中继网络的激励机制（如费用分配和反抢先设计）尚待设计，这是保障网络长期稳定运行的关键。最后，系统性能依赖于专用硬件的并行计算能力，对于小规模部署，deVirgo的性能优势可能不明显。

### 强关联论文

[76] Jiaheng Zhang, Tiancheng Xie, Y. Zhang, and D. Song. **Transparent Polynomial Delegation and Its Applications to Zero Knowledge Proof** *2020 IEEE Symposium on Security and Privacy (SP)* [Google Scholar](https://scholar.google.com/scholar?q=Transparent+Polynomial+Delegation+and+Its+Applications+to+Zero+Knowledge+Proof)

[54] Jens Groth. **On the Size of Pairing-Based Non-interactive Arguments** *EUROCRYPT 2016* [Google Scholar](https://scholar.google.com/scholar?q=On+the+Size+of+Pairing-Based+Non-interactive+Arguments)

[53] Shafi Goldwasser, Yael Tauman Kalai, and Guy N. Rothblum. **Delegating Computation: Interactive Proofs for Muggles** *J. ACM 2015* [Google Scholar](https://scholar.google.com/scholar?q=Delegating+Computation:+Interactive+Proofs+for+Muggles)

[65] Shravan Srinivasan, Alexander Chepurnoy, Charalampos Papamanthou, Alin Tomescu, and Yupeng Zhang. **Hyperproofs: Aggregating and Maintaining Proofs in Vector Commitments** *IACR Cryptol. ePrint Arch. 2021* [Google Scholar](https://scholar.google.com/scholar?q=Hyperproofs:+Aggregating+and+Maintaining+Proofs+in+Vector+Commitments)

[68] Riad S Wahby, Max Howald, Siddharth Garg, Abhi Shelat, and Michael Walfish. **Verifiable asics** *2016 IEEE Symposium on Security and Privacy (SP)* [Google Scholar](https://scholar.google.com/scholar?q=Verifiable+asics)

[73] Tiacheng Xie, Jiaheng Zhang, Yupeng Zhang, Charalampos Papamanthou, and Dawn Song. **Libra: Succinct Zero-Knowledge Proofs with Optimal Prover Computation** *CRYPTO 2019* [Google Scholar](https://scholar.google.com/scholar?q=Libra:+Succinct+Zero-Knowledge+Proofs+with+Optimal+Prover+Computation)

[72] Howard Wu, Wenting Zheng, Alessandro Chiesa, Raluca Ada Popa, and Ion Stoica. **DIZK: A Distributed Zero-Knowledge Proof System** *2018* [Google Scholar](https://scholar.google.com/scholar?q=DIZK:+A+Distributed+Zero-Knowledge+Proof+System)


## 关键词

+ 跨链桥
+ 零知识证明
+ 区块链互操作性
+ 简洁论证
+ 无信任系统