---
title: "Optiswap: Fast optimistic fair exchange"
标题简称:
论文类型: conference
会议简称: AsiaCCS
发表年份: 2020
---

## Optiswap: Fast optimistic fair exchange

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3320269.3384749)

## 作者

+ Lisa Eckey 
+ Sebastian Faust 
+ Benjamin Schlosser 


## 笔记

好的，作为一位密码学领域的研究助手，我将根据您提供的论文全文，按照指定格式输出详尽的结构化笔记。

---

### 背景与动机

数字商品的安全交换是互联网交易中的核心难题，尤其当买卖双方互不信任时。早在1999年，Pagnia和Gärtner就证明了在没有可信第三方的情况下，公平交换是不可能的[18]。随着加密货币的出现，一种有前景的解决方案是使用智能合约作为仲裁者，在双方发生争议时公平地裁定结果。这类协议通常会设计一个“乐观模式”，即大多数情况下双方诚实行事，只需与智能合约进行极少的交互即可完成交易。FairSwap协议[8]是其中的代表，它通过“不当行为证明”机制避免了昂贵的零知识证明，对复杂谓词和大见证的效率更高。然而，FairSwap存在一个显著瓶颈：其乐观执行的通信复杂度与见证大小和谓词电路的规模成正比，卖方必须一次性传输所有电路中间值的加密结果。这不仅带来了巨大的通信开销，也增加了双方的计算负担。此外，FairSwap协议未考虑“悲伤攻击”——恶意方可通过迫使诚实话方提交大量交易而承担高昂的手续费。本文旨在填补这一空白，通过引入交互式的争议解决协议，大幅降低乐观情况下的开销，并设计费用机制来抵御悲伤攻击。

### 相关工作

[8] Dziembowski et al. **FairSwap: How To Fairly Exchange Digital Goods.** *ACM CCS 2018* [Google Scholar](https://scholar.google.com/scholar?q=FairSwap%3A+How+To+Fairly+Exchange+Digital+Goods)
> 核心思路：使用“不当行为证明”替代零知识证明来实现公平交换。在无争议时，卖方需发送所有电路中间值的加密，以准备可能发生的争议。
> 局限与区别：乐观情况下通信和计算开销大，且未考虑悲伤攻击。本文通过引入交互式争议解决，消除了这些乐观情况下的开销。

[13] Kalodner et al. **Arbitrum: Scalable, private smart contracts.** *USENIX Security 2018* [Google Scholar](https://scholar.google.com/scholar?q=Arbitrum%3A+Scalable%2C+private+smart+contracts)
> 核心思路：采用交互式争议解决来提升区块链的可扩展性，通过二分搜索将争议缩小到单一指令。
> 局限与区别：Arbitrum基于线性图灵机模型进行二分搜索；OptiSwap基于电路模型，可利用电路拓扑结构（如深度、宽度）采取更复杂的挑战策略，非单一线性搜索。

[19] Teutsch and Reitwießner. **A scalable verification solution for blockchains.** *CoRR 2017* [Google Scholar](https://scholar.google.com/scholar?q=A+scalable+verification+solution+for+blockchains)
> 核心思路：即TrueBit系统，也包含一个用于解决计算争议的交互式争议解决层，同样使用基于图灵机模型的二分搜索。
> 局限与区别：与OptiSwap的主要区别在于计算模型不同，OptiSwap的电路模型允许更灵活的挑战策略。

[20] Wagner et al. **Dispute Resolution for Smart Contract-based Two-Party Protocols.** *IEEE ICBC 2019* [Google Scholar](https://scholar.google.com/scholar?q=Dispute+Resolution+for+Smart+Contract-based+Two-Party+Protocols)
> 核心思路：即SmartJudge架构，将智能合约拆分为仅用于乐观情况的“调解器”和用于争议的“验证器”，优化了乐观模式的成本。
> 局限与区别：SmartJudge只是提供一个抽象框架，但没有内置具体的争议解决机制。OptiSwap可以与SmartJudge结合，将复杂的争议逻辑放入“验证器”中，进一步降低乐观模式的部署费用。

[12] Hall-Andersen. **FastSwap: Concretely Efficient Contingent Payments for Complex Predicates.** *IACR ePrint 2019* [Google Scholar](https://scholar.google.com/scholar?q=FastSwap%3A+Concretely+Efficient+Contingent+Payments+for+Complex+Predicates)
> 核心思路：与OptiSwap同时期的工作，同样旨在优化FairSwap的乐观情况。使用类似图灵机的线性模型，在争议时进行对数轮次的交互。
> 局限与区别：FastSwap侧重于通信复杂度的优化，而OptiSwap则明确将费用公平性纳入协议设计，以预防悲伤攻击。OptiSwap使用电路模型，允许更多样的挑战策略。两篇工作互相兼容。

[4] Bitcoin Wiki. **Zero Knowledge Contingent Payment.**
> 核心思路：使用零知识证明来证明见证的正确性，实现公平交换。
> 局限与区别：零知识证明的计算和通信开销巨大，不适用于复杂谓词或大规模数据。FairSwap和OptiSwap通过事后惩罚替代了事前证明，效率更高。

[2] Asokan et al. **Optimistic Fair Exchange of Digital Signatures.** *EUROCRYPT 1998* [Google Scholar](https://scholar.google.com/scholar?q=Optimistic+Fair+Exchange+of+Digital+Signatures)
> 核心思路：首次提出了乐观公平交换的概念，将协议分为乐观情况（无争议）和悲观情况（有争议）。
> 局限与区别：该工作依赖于传统的可信第三方（TTP），而OptiSwap使用区块链和智能合约作为去中心化的TTP。

[3] Andrychowicz et al. **Secure Multiparty Computations on Bitcoin.** *IEEE S&P 2014* [Google Scholar](https://scholar.google.com/scholar?q=Secure+Multiparty+Computations+on+Bitcoin)
> 核心思路：使用比特币的脚本系统来实现公平的安全多方计算。
> 局限与区别：比特币脚本功能有限，OptiSwap基于图灵完备的智能合约（如以太坊），可以实现更复杂的验证逻辑，例如对电路的门级验证。

### 核心技术与方案

OptiSwap的核心思想是将FairSwap中的“一次性证明”模式转变为“交互式取证”模式。协议整体框架由一个链上智能合约和链下买卖双方之间的交互构成。协议的乐观执行流程有四个轮次：第一轮，卖方加密见证x并提交对密文和密钥的承诺给合约，并将密文发送给买方。第二轮，买方确认并锁定资金到合约。第三轮，卖方将密钥揭示到合约。第四轮，买方用密钥解密得到见证，验证其正确性。若正确，则确认交易，资金转至卖方。这是主要的性能优化点。

当买方发现解密后的见证不正确时，将触发交互式争议处理流程。这一流程的目的是在链下定位到电路中双方产生分歧的单个门。争议开始于买方挑战电路的输出门。卖方必须回应，提供该门的输出值。如果卖方声称输出为1而买方计算结果为0，则买方继续挑战该门的输入门，让卖方提供其计算的中间值。如此反复，形成一个挑战-响应序列。每次挑战由Buyer发起，限定挑战次数上限 $a_\phi$；每次响应由Seller提供，双方都需要为各自的交易缴纳安全保证金。

安全保证金机制是抵御悲伤攻击的关键。在争议阶段，买卖双方每发送一次交易，都需要在合约中锁定一笔额外的费用（$f_S$ 或 $f_B$）。最终，如果买方证明了卖方的不当行为，则买方获得所有锁定的费用和退款；反之，如果卖方成功回应了所有挑战，证明其行为正确，则卖方获得所有锁定的费用和付款。这确保了诚实话方不仅不会因争议而损失手续费，反而能获得补偿，从而从经济上震慑恶意方的无意义挑战。

在安全性方面，协议的安全性质S1（抗恶意买方）依赖于CPA安全的加密方案和承诺的隐藏性，使得买方在密钥揭示前无法获知见证。性质S2（抗恶意卖方）依赖于承诺的绑定性，使得卖方无法否认已提交的密文。在争议过程中，协议保证了诚实买方有足够的机会（不超过 $a_\phi$ 次挑战）来定位并证明卖方的欺骗单门，或是证明卖方交付了错误的见证。性质S3（抗悲伤）通过上述的保证金机制实现。整个协议在UC模型下被证明可安全实现理想功能 $\mathcal{F}_{icfe}^{\mathcal{L}}$，证明依赖于对随机预言机ℋ的可观察和可编程性质的假设。

在渐进复杂度上，乐观情况下的通信复杂度为 $O(|x|)$，即与见证大小线性相关，与电路规模无关。悲观情况下，轮复杂度上界为 $O(min(\delta \cdot \ell, \log(n) \cdot \omega))$，其中 $\delta$ 是电路深度，$\ell$ 是扇入，$\omega$ 是宽度，$n$ 是输入长度，具体策略可优化。

### 核心公式与流程

**[FairSwap的PoM预备数据构造]**
卖方需为电路的每一个门 $\phi_i$ 计算输出并加密。
$$ \forall i \in [m], z_i = Enc(k, out_i) \quad \text{其中 } out_i = \phi_i(x) $$
然后计算密文的Merkle树根 $r_z = MTHash(z_1, \ldots, z_m)$。此过程在乐观情况下也会执行，造成巨大开销。

**[OptiSwap的初始设置]**
卖方仅加密见证的各分片，而非所有门输出。
$$ \forall i \in [n], z_i = Enc(k, x_i) $$
$$ r_z = MTHash(z_1, \ldots, z_n) $$
$$ (c, d) \gets Commit(k) $$
乐观情况下，通信量仅为 $O(|x|)$，与电路无关。

**[争议处理：挑战与响应]**
这是一个迭代过程。设当前挑战的门为 $\phi_{cur}$，其输入来自门集合 $I_{cur}$。
Buyer挑战：发送门索引集 $Q = \{i_1, i_2, \ldots\}$，其中 $Q \subseteq I_{cur}$。
Seller响应：对于 $i \in Q$，发送其输出值 $out_i$ 及Merkle证明证明 $out_i$ 是承诺树中第 $i$ 个元素。
Buyer验证：检查 $\phi_i(in_i) \stackrel{?}{=} out_i$。若不等，则生成PoM。

**[PoM（以门计算错误为例）]**
Buyer提交给合约，证明Seller在门 $\phi_i$ 的计算上撒谎。
PoM包含：门索引 $i$，该门声称的输出 $\mathsf{outp}_i$，该门的输入 $ \mathsf{in}_i^1, \ldots, \mathsf{in}_i^{\ell}$，以及所有必要的Merkle证明。
合约验证：从 $r_e$（门输出承诺树根）验证 $\mathsf{outp}_i$ 和 $\mathsf{in}_i^1, \ldots, \mathsf{in}_i^{\ell}$，然后计算 $\phi_i(\mathsf{in}_i^1, \ldots, \mathsf{in}_i^{\ell})$，结果若不等于 $\mathsf{outp}_i$，则判定Seller不当。

### 实验结果

实验基于文件销售应用场景，将1GB文件分为512字节大小的数据块作为见证，对应电路深度$\delta=21$，扇入$\ell=2$，因此挑战上限 $a_\phi = ( (\delta - 1) \cdot \ell + 1 ) = 41$。

通信开销方面，与FairSwap [8] 相比，对于1GB文件，数据块为4字节时，FairSwap的通信开销是9倍，而OptiSwap始终为1倍。对于矩阵乘法（$10 \times 10$），FairSwap开销为11.5倍，而OptiSwap仍是1倍。对于AES-256破解场景，FairSwap的通信开销高达34,000倍。

Gas费用（以Ethereum为基准）方面，OptiSwap独立合约的乐观情况执行（4-5轮）需要101,307 gas，悲观情况需要6,412,569 gas。结合SmartJudge [20] 技术将合约拆分为“乐观部署”和“悲观部署”后，乐观部署成本降至952,939 gas，悲观部署额外需要1,962,992 gas。乐观情况下的成本与FairSwap相当，甚至略低。悲观情况下，虽然轮次和总Gas成本高于FairSwap（194,068 gas的解构PoM），但保证金机制确保了诚实话方最终获得补偿。

### 局限性与开放问题

OptiSwap的悲观情况执行成本较FairSwap显著增加，这是以更低的乐观情况开销和防范悲伤攻击为代价的。对于简单的电路或极低亏损风险的应用，增加的手续费锁定和争议流程可能显得过于笨重。此外，挑战上限 $a_\phi$ 的设定依赖于电路参数，对于某些复杂电路，这个值可能很大，导致悲观情况下的轮次和成本过高。未来的研究可以探索如何将同一合约用于多次交换，以摊薄部署成本，并分析该协议在通信和计算复杂度方面的理论上界，以判断是否还有进一步优化的空间。

### 强关联论文

[8] Stefan Dziembowski, Lisa Eckey, and Sebastian Faust. **FairSwap: How To Fairly Exchange Digital Goods.** *ACM CCS 2018* [Google Scholar](https://scholar.google.com/scholar?q=FairSwap%3A+How+To+Fairly+Exchange+Digital+Goods)

[20] Eric Wagner, Achim Völker, Frederik Fuhrmann, Roman Matzutt, and Klaus Wehrle. **Dispute Resolution for Smart Contract-based Two-Party Protocols.** *IEEE ICBC 2019* [Google Scholar](https://scholar.google.com/scholar?q=Dispute+Resolution+for+Smart+Contract-based+Two-Party+Protocols)

[13] Harry A. Kalodner, Steven Goldfeder, Xiaoqi Chen, S. Matthew Weinberg, and Edward W. Felten. **Arbitrum: Scalable, private smart contracts.** *USENIX Security 2018* [Google Scholar](https://scholar.google.com/scholar?q=Arbitrum%3A+Scalable%2C+private+smart+contracts)

[19] Jason Teutsch and Christian Reitwießner. **A scalable verification solution for blockchains.** *CoRR 2017* [Google Scholar](https://scholar.google.com/scholar?q=A+scalable+verification+solution+for+blockchains)

[12] Mathias Hall-Andersen. **FastSwap: Concretely Efficient Contingent Payments for Complex Predicates.** *IACR ePrint 2019* [Google Scholar](https://scholar.google.com/scholar?q=FastSwap%3A+Concretely+Efficient+Contingent+Payments+for+Complex+Predicates)

[4] Bitcoin Wiki. **Zero Knowledge Contingent Payment.** [Google Scholar](https://scholar.google.com/scholar?q=Zero+Knowledge+Contingent+Payment)

[2] N. Asokan, Victor Shoup, and Michael Waidner. **Optimistic Fair Exchange of Digital Signatures**. *EUROCRYPT 1998* [Google Scholar](https://scholar.google.com/scholar?q=Optimistic+Fair+Exchange+of+Digital+Signatures)

[18] Henning Pagnia and Felix C Gärtner. **On the impossibility of fair exchange without a trusted third party.** *Technical Report, TUD-BS-1999-02, 1999* [Google Scholar](https://scholar.google.com/scholar?q=On+the+impossibility+of+fair+exchange+without+a+trusted+third+party)


## 关键词

+ 智能合约
+ 公平交换
+ 乐观模式
+ 区块链
+ 可组合安全性
