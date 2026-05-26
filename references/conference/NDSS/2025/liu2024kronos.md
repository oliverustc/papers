---
title: "Kronos: A secure and generic sharding blockchain consensus with optimized overhead"
标题简称: 
论文类型: conference
会议简称: NDSS
发表年份: 2025
modified: 2025-04-13 16:40:42
---

## Kronos: A secure and generic sharding blockchain consensus with optimized overhead

## 发表信息

+ [原文链接](https://www.ndss-symposium.org/ndss-paper/kronos-a-secure-and-generic-sharding-blockchain-consensus-with-optimized-overhead/)
+ [archive](https://eprint.iacr.org/2024/206)

## 作者

+ Yizhong Liu 
+ Andi Liu 
+ Yuan Lu 
+ Zhuocheng Pan 
+ Yinuo Li 
+ Jianwei Liu 
+ Song Bian 
+ Mauro Conti 

## 笔记

### 背景与动机
区块链的可扩展性瓶颈是制约其大规模应用的核心问题。分片技术通过将网络划分为多个子网（分片），每个分片仅处理部分交易，从而在增加节点总数时能够线性提升系统吞吐量，展现出解决该问题的巨大潜力。然而，分片引入了跨分片交易这一新型交易类型，即交易的输入和输出地址属于不同分片。由于分片间的状态隔离，跨分片交易的原子性（即要么所有相关分片执行该交易，要么全部放弃）是保证账本一致性的关键。根据以太坊ICO数据，2024年多输入交易的总价值已达10亿美元，且研究表明当网络扩展至16个分片时，涉及两个输入分片和一个输出分片的跨分片交易占比预计超过99%[10]。因此，跨分片交易的处理效率与安全性直接决定了分片区块链系统的整体性能。现有方案普遍存在三个主要问题：一是“弱原子性”与高开销，许多方案（如Omniledger [9]、Chainspace [14]）无法容忍恶意领导者和客户端，且普遍采用两阶段提交（2PC）模式，导致每个输入分片需要执行两次拜占庭容错（BFT）共识，显著增加了系统内开销；二是跨分片消息传递既冗长又不可靠，现有方案要么将证书发送委托给客户端或分片领导者（易受拒绝服务攻击），要么采用昂贵的“全对全”广播方式，导致$\mathcal{O}(n^2 b\lambda)$的通信复杂度；三是缺乏通用的分片区块链共识框架，无法同时支持同步、部分同步和异步网络环境。Kronos旨在填补这一空白，提出一种通用、安全且开销优化的分片区块链共识协议。

### 相关工作

- [9] Kokoris-Kogias 等. Omniledger: A Secure, Scale-Out, Decentralized Ledger via Sharding. **SP 2018** [Google Scholar](https://scholar.google.com/scholar?q=Omniledger%3A+A+Secure%2C+Scale-Out%2C+Decentralized+Ledger+via+Sharding)
> 核心思路：采用2PC模式处理跨分片交易，每个输入分片先锁定输入，再根据交易有效性解锁或支出。
> 局限与区别：无法容忍恶意领导者和客户端，每次跨分片交易需要2kB次BFT（k为涉及分片数），内开销高。Kronos通过缓冲区机制将内开销降至kB，并容忍恶意参与者。

- [14] Al-Bassam 等. Chainspace: A Sharded Smart Contracts Platform. **NDSS 2018** [Google Scholar](https://scholar.google.com/scholar?q=Chainspace%3A+A+Sharded+Smart+Contracts+Platform)
> 核心思路：使用2PC模式，并对每个输入生成独立证书进行跨分片传输。
> 局限与区别：无法容忍恶意客户端（客户端提交攻击），证书数量与交易数b成正比，跨分片通信开销为$\mathcal{O}(n^2 b\lambda)$。Kronos采用批量证书和编码传输，将通信开销降至$\mathcal{O}(nb\lambda)$，并实现了客户端容忍性。

- [10] Zamani 等. RapidChain: Scaling Blockchain via Full Sharding. **CCS 2018** [Google Scholar](https://scholar.google.com/scholar?q=RapidChain%3A+Scaling+Blockchain+via+Full+Sharding)
> 核心思路：通过直接向收款方支出资金的方式降低2PC开销，但无法处理无效的多输入交易。
> 局限与区别：无法容忍恶意领导者，在无效交易处理上存在安全漏洞。Kronos针对无效交易设计了开心路径和伤心路径，在开心路径中无需BFT即可拒绝，保证了原子性。

- [11] Dang 等. Towards Scaling Blockchain Systems via Sharding. **SIGMOD 2019** [Google Scholar](https://scholar.google.com/scholar?q=Towards+Scaling+Blockchain+Systems+via+Sharding)
> 核心思路：引入参考分片处理跨分片交易，所有跨分片消息需通过参考分片的BFT进行转移和提交。
> 局限与区别：引入了额外的参考分片BFT开销，导致总内开销为（2k+3）B，通信开销仍为$\mathcal{O}(n^2 b\lambda)$，且无法容忍恶意客户端。Kronos通过输出分片的缓冲区机制免除了额外分片，内开销更优。

- [18] Wang 等. Monoxide: Scale Out Blockchains with Asynchronous Consensus Zones. **NSDI 2019** [Google Scholar](https://scholar.google.com/scholar?q=Monoxide%3A+Scale+Out+Blockchains+with+Asynchronous+Consensus+Zones)
> 核心思路：采用异步共识区域，通过打包区块并按输出分片签名作为证书。
> 局限与区别：仅支持单输入、单输出交易，无法处理多输入跨分片交易。Kronos的缓冲区机制自然地支持了多输入交易场景。

- [23] Hellings 等. ByShard: Sharding in a Byzantine Environment. **VLDB Journal** [Google Scholar](https://scholar.google.com/scholar?q=ByShard%3A+Sharding+in+a+Byzantine+Environment)
> 核心思路：采用2PC模式，但在同步网络模型下运行。
> 局限与区别：无法容忍恶意客户端，且通信开销为$\mathcal{O}(n^2 b\lambda)$。Kronos不依赖任何时序假设，可运行于异步网络。

- [33] Guo 等. Speeding Dumbo: Pushing Asynchronous BFT Closer to Practice. **NDSS 2022** [Google Scholar](https://scholar.google.com/scholar?q=Speeding+Dumbo%3A+Pushing+Asynchronous+BFT+Closer+to+Practice)
> 核心思路：提出一种高效的异步BFT协议，作为Kronos内共识的实例。
> 作用：Kronos将其作为内分片共识协议的实例，展示了框架的通用性，并在实验中验证了在异步网络下的高性能。

### 核心技术与方案
Kronos的核心是一个基于缓冲区的安全分片区块链共识模式，旨在以优化的开销实现原子性。其整体方案可分为四个关键步骤。

首先，**请求交付**阶段用于抵抗恶意客户端的沉默攻击。客户端将签名的交易请求提交至输出分片。输出分片验证请求结构完整后，将请求转发至所有其他相关分片中的所有（至少$f+1$个）成员。这确保了所有相关分片接收到同一条请求，防止恶意客户端向不同分片提交不一致请求。

其次，**可用输入支出**阶段涉及从输入分片到输出分片缓冲区的资金转移。输入分片节点接收到请求后，验证其所管理的输入是否可用（检查UTXO池和客户端签名）。对于可用输入，节点构造一个`SPEND-TRANSACTION`（`SP-tx`）并将其加入等待队列。`SP-tx`的输出地址并非直接指向收款方，而是指向输出分片的缓冲区地址$gpk^{\mathrm{t}}_{\mathrm{out}}$，该地址由输出分片节点通过$(f+1, n)$门限签名方案（或多签名方案）共同管理。`SP-tx`通过输入分片的BFT被提交并执行，相应的UTXO被标记为已支出。

第三，**可靠跨分片批量认证**阶段负责将已提交的输入支出证明高效、可靠地传输到输出分片。Kronos采用混合树（HT-RCBC）或向量承诺（VC-RCBC）两种方法实现批量认证。以HT-RCBC为例，输入分片节点将发送给同一输出分片的请求ID集合编码为n个编码块$\{a_i\}_n$，并构建一棵下层编码树以验证编码块。再构建一棵上层混合认证树，其叶子节点是各输出分片对应的下层编码树根$l$-$rt_c$。每个节点$P_i$只发送一个编码块$a_i$、对应的哈希路径和上层树的根签名$s_i^{\mathrm{BF}}$。输出分片节点在收到$n-f$个验证通过的消息后，组合出阈值签名$\sigma$，通过解码和Merkle树根验证恢复出请求ID集合。此方法将跨分片通信开销从$\mathcal{O}(n^2 b\lambda)$降低至$\mathcal{O}(n(b + n\log m + n\log n)\lambda)$，当$b$足够大时近似为$\mathcal{O}(nb\lambda)$。VC-RCBC则能将开销稳定在$\mathcal{O}(nb\lambda)$。

最后，**交易终结**阶段在输出分片完成。当输出分片的缓冲区收集到某个请求的所有输入时（即确认请求有效），每个诚实节点使用其$(f+1, n)$门限签名密钥的部分签名$s^{\mathrm{FH}}_i$对请求进行签名。当收集到$f+1$个有效签名后，节点构造一个`FINISH-TRANSACTION`（`FH-tx`），将缓冲区中的输入转移到收款方的地址。此`FH-tx`通过输出分片的BFT被提交，完成交易。

对于**无效交易**，Kronos设计了开心路径和伤心路径。在开心路径中，发现不可用输入的输入分片节点生成`REJECT-MESSAGE`并广播给所有相关分片。其他输入分片若尚未处理该请求，则直接放弃。输出分片若缓冲区中尚无该请求的输入，则直接拒绝。此过程无需BFT，内开销为0。在伤心路径中，若某些输入分片已为无效请求执行了`SP-tx`，则在收到拒绝消息后，这些输入分片需构造并提交一个`BACK-TRANSACTION`（`BK-tx`），通过BFT将资金回滚到初始地址。

**安全性论证**：Kronos的安全性依赖于BFT的安全性、门限签名方案的安全性和可靠跨分片消息传输。原子性由输出分片等待完整输入后才提交`FH-tx`的设计保证，且伤心路径中的`BK-tx`确保了在任何条件下都能回滚。一致性通过`TxVerify`函数和缓冲区管理避免了双花，因为共享的UTXO只能被支出一次。可靠跨分片传输通过$n-f$个签名验证和纠错码保证消息的完整性和可恢复性，从而抵抗伪装攻击。

### 核心公式与流程

**[请求交付与输入支出流程（合并视角）]**
$$
\begin{array}{l}
\textbf{Step 1 (Request Delivery): } \text{Client} \xrightarrow{\text{req}[id]} \text{Shard } S_{\mathrm{out}}; S_{\mathrm{out}} \xrightarrow{\text{req}[id]} S_{\mathrm{in}} \\
\textbf{Step 2 (Input Spending): } \\
\quad \text{Verify: }\forall I_i \in \text{req}[id].\mathbf{I}, \text{ if } I_i.S_c = S_{\mathrm{in}} \text{ then } I_i.\mathrm{utxo} \in \mathrm{UTXO}_{\mathrm{in}} \land \text{verify\_sig}(I_i.\mathrm{sig}) = 1 \\
\quad \text{Construct: }\mathrm{SP\text{-}tx}[id] := (\mathrm{SP}, id, \mathbf{I}, \mathbf{O}), \text{ where } \mathbf{O} := (S_{\mathrm{out}}, gpk_{\mathrm{out}}^{\mathrm{t}}, v) \\
\quad \text{Consensus: }\mathrm{SP\text{-}tx}[id] \xrightarrow{\text{BFT}} \mathrm{log}_{\mathrm{in}} \| \mathrm{SP\text{-}tx}[id]
\end{array}
$$
> 作用： 描述Kronos中有效跨分片交易的前两个步骤，包括请求从客户端到输出分片再到输入分片的交付，以及输入分片验证、构建`SPEND-TRANSACTION`并通过BFT提交的过程。`SP-tx`的输出指向输出分片的缓冲区地址$gpk_{\mathrm{out}}^{\mathrm{t}}$。

**[可靠跨分片批量认证（混合树方法）]**
$$
\begin{aligned}
&\textbf{Input Shard } S_{\mathrm{in}}: \\
&\quad \{a_i\}_n \leftarrow \mathrm{ECEnc}(\mathrm{cID}_{S_{\mathrm{out}}}, n, n-2f) \\
&\quad (l\text{-}\mathrm{tree}, l\text{-}\mathrm{rt}, \{l\text{-}\mathrm{hp}\}) \leftarrow \mathrm{TreeCon}(\{a_i\}_n) \\
&\quad (\mathrm{tree}, \mathrm{rt}, \{\mathrm{hp}\}) \leftarrow \mathrm{TreeCon}(\{l\text{-}\mathrm{rt}_c\}_{c \in [m]}) \\
&\quad s_i^{\mathrm{BF}} \leftarrow \mathrm{ShareSig}(sk_i^{\mathrm{T}}, \mathrm{rt}) \\
&\quad \text{Send to } S_{\mathrm{out}}: m_{\mathrm{BF}}^i = (\langle \mathrm{rt}, s_i^{\mathrm{BF}} \rangle, a_i, l\text{-}\mathrm{hp}_i, \mathrm{hp}_{\mathrm{out}})
\end{aligned}
$$
> 作用： 描述输入分片如何构建混合树并进行批量认证。流程包括：对请求ID集进行纠错编码、构建下层编码树、构建上层认证树、对树根使用$(n-f, n)$门限签名签名，然后将编码块、两个层级的哈希路径和根签名发送到输出分片。

**[交易终结（有效请求）]**
$$
\begin{aligned}
&\textbf{Output Shard } S_{\mathrm{out}}: \\
&\quad \text{upon } \forall I_i \in \text{req}[id] \text{ in buffer:} \\
&\quad\quad s_i^{\mathrm{FH}} \leftarrow \mathrm{ShareSig}(sk_i^{\mathrm{t}}, \mathsf{H}(\{I\})) \\
&\quad \text{upon } f+1 \text{ valid } (id, s_j^{\mathrm{FH}}) \text{ from distinct } P_j: \\
&\quad\quad \sigma^{\mathrm{FH}}[id] \leftarrow \mathrm{Combine}(\mathsf{H}(\{I\}), \{(j, s_j^{\mathrm{FH}})\}_{f+1}) \\
&\quad\quad \mathrm{FH\text{-}tx}[id] := (\mathrm{FH}, id, \mathbf{I}= \langle \{I\}, \sigma^{\mathrm{FH}}[id]\rangle, \mathbf{O}= (S_{\mathrm{out}}, pk_{\mathrm{payee}}, v)) \\
&\quad\quad \mathrm{FH\text{-}tx}[id] \xrightarrow{\text{BFT}} \mathrm{log}_{\mathrm{out}} \| \mathrm{FH\text{-}tx}[id]
\end{aligned}
$$
> 作用： 描述输出分片如何完成一笔有效跨分片交易。输出分片在缓冲区收集到所有输入后，通过$(f+1, n)$门限签名生成法定人数证明，构造`FINISH-TRANSACTION`，并通过BFT提交，从而将资金从缓冲区转移到收款方。

**[无效交易回滚（伤心路径）]**
$$
\begin{aligned}
&\textbf{Input Shard } S_{\mathrm{in}} \text{ (who already spent for invalid req}[id]): \\
&\quad \text{upon } m_{\mathrm{RJ}}[id] \text{ with valid } \sigma^{\mathrm{RJ}}[id]: \\
&\quad\quad \mathrm{BK\text{-}tx}[id] := (\mathrm{BK}, id, \mathbf{I}= \mathrm{SP\text{-}tx}[id].\mathbf{O} \text{ with T-SIG}= \sigma^{\mathrm{RJ}}, \mathbf{O}= (S_{\mathrm{in}}, pk_{\mathrm{initial}}, v)) \\
&\quad\quad \mathrm{BK\text{-}tx}[id] \xrightarrow{\text{BFT}} \mathrm{log}_{\mathrm{in}} \| \mathrm{BK\text{-}tx}[id]
\end{aligned}
$$
> 作用： 描述在伤心路径中，已为无效交易支出资金的输入分片如何回滚。该分片利用从拒绝消息中获得的无效性证明$\sigma^{\mathrm{RJ}}$，构造`BACK-TRANSACTION`来将之前支出的资金返还给初始地址。

### 实验结果
Kronos在Amazon EC2 c5.4xlarge实例上进行了大规模实验，实例部署在弗吉尼亚、香港、东京、伦敦四个AWS区域，节点规模从32扩展到1000。实验采用异步BFT协议Speeding Dumbo [33]作为内分片共识的实例（sKronos）。实验结果表明，sKronos在1000节点网络中，批量大小为20k时，达到了**320 ktx/sec**的峰值吞吐量，延迟为2.0秒。在256节点网络中，吞吐量达136.7 ktx/sec时，延迟低于1.13秒。与采用相同BFT的两阶段提交（s2PC）相比，sKronos在跨分片交易比例为10%时吞吐量提升2.4倍，比例为50%时提升约4倍，比例为90%时提升**12倍**，延迟降低至少50%。与AHL [11]和ByShard [23]相比，sKronos的吞吐量分别高出2.7倍和2.3倍，延迟不到后者的三分之一。此外，通过将内分片共识替换为部分同步的HotStuff [30]（hKronos），其性能同样优于s2PC，验证了Kronos框架的通用性。实验还评估了伤心路径的影响，即使在20%跨分片交易无效且触发伤心路径的情况下，吞吐量下降和延迟增加也保持在较低水平，证明了Kronos在实际部署中的鲁棒性和高效性。

### 局限性与开放问题
Kronos虽然实现了原子性和优化开销，但其设计依赖于门限签名和向量承诺等密码学原语，这些原语的安全性基于计算性假设（如计算性Diffie-Hellman假设）。论文未深入探讨如何在不信任设置的情况下实现高效的跨分片吞吐量极限。其次，Kronos在适度规模网络（千节点级）中表现最佳，但在极大规模网络下，跨分片通信的线性复杂度$\mathcal{O}(nb\lambda)$可能成为新的瓶颈。最后，跨分片交易的比例仍会影响系统性能，未来可进一步研究在跨分片交易占绝对主导时，如何通过交易调度和分片布局来优化缓冲区利用率和降低等待时间。此外，如何结合最新的密码学工具（如零知识证明）来进一步压缩跨分片证书大小也是值得探索的方向。

### 强关联论文

[9] Kokoris-Kogias et al. Omniledger: A Secure, Scale-Out, Decentralized Ledger via Sharding. **SP 2018** [Google Scholar](https://scholar.google.com/scholar?q=Omniledger%3A+A+Secure%2C+Scale-Out%2C+Decentralized+Ledger+via+Sharding)

[10] Zamani et al. RapidChain: Scaling Blockchain via Full Sharding. **CCS 2018** [Google Scholar](https://scholar.google.com/scholar?q=RapidChain%3A+Scaling+Blockchain+via+Full+Sharding)

[11] Dang et al. Towards Scaling Blockchain Systems via Sharding. **SIGMOD 2019** [Google Scholar](https://scholar.google.com/scholar?q=Towards+Scaling+Blockchain+Systems+via+Sharding)

[14] Al-Bassam et al. Chainspace: A Sharded Smart Contracts Platform. **NDSS 2018** [Google Scholar](https://scholar.google.com/scholar?q=Chainspace%3A+A+Sharded+Smart+Contracts+Platform)

[18] Wang et al. Monoxide: Scale Out Blockchains with Asynchronous Consensus Zones. **NSDI 2019** [Google Scholar](https://scholar.google.com/scholar?q=Monoxide%3A+Scale+Out+Blockchains+with+Asynchronous+Consensus+Zones)

[23] Hellings et al. ByShard: Sharding in a Byzantine Environment. **VLDB Journal** [Google Scholar](https://scholar.google.com/scholar?q=ByShard%3A+Sharding+in+a+Byzantine+Environment)

[30] Yin et al. Hotstuff: Bft Consensus with Linearity and Responsiveness. **PODC 2019** [Google Scholar](https://scholar.google.com/scholar?q=Hotstuff%3A+Bft+Consensus+with+Linearity+and+Responsiveness)

[33] Guo et al. Speeding Dumbo: Pushing Asynchronous BFT Closer to Practice. **NDSS 2022** [Google Scholar](https://scholar.google.com/scholar?q=Speeding+Dumbo%3A+Pushing+Asynchronous+BFT+Closer+to+Practice)


## 关键词

+ 分片区块链共识
+ 跨分片交易
+ 拜占庭容错
+ 区块链可扩展性
+ 原子性安全
+ 异步网络