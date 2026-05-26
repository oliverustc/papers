---
title: "Riggs: Decentralized sealed-bid auctions"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2023
created: 2025-04-16 10:54:35
modified: 2025-04-16 10:55:19
---

## Riggs: Decentralized sealed-bid auctions

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3576915.3623182)

## 作者

+ [Nirvan Tyagi](Nirvan Tyagi.md) 
+ [Arasu Arun](Arasu%20Arun.md)
+ Cody Freitag 
+ [Riad Wahby](Riad%20Wahby.md)
+ [Joseph Bonneau](Joseph Bonneau.md) 
+ David Mazières 

## 笔记

### 背景与动机
密封投标拍卖在理论上具有单轮通信、激励兼容等显著优势，但在实践中远不如公开增价拍卖普及。Rothkopf 等人于1990年分析指出，两大障碍在于竞拍者担忧可信拍卖人作弊以及自身真实估价被泄露 [84]。尽管密码学界自1993年起就尝试用加密协议消除对拍卖人的信任，提出了大量基于安全多方计算、同态加密等技术的方案，但这些方案在区块链出现前普遍无法强制执行胜出者的支付或物品的交付。智能合约平台为实现完全去中心化的拍卖提供了可能，然而一个根本性问题仍未解决：在“承诺-揭示”两阶段模型中，竞拍者可以在看到他人报价后选择拒绝揭示自己的承诺，导致拍卖结果偏斜。已有方案通过罚金或秘密共享来激励揭示，但这些方法要么需要精心设定罚金数额以防参与方退出，要么需要假设多数参与方诚实。本文旨在填补这一空白：构建一个即使所有竞拍者同时退出，甚至n-1个竞拍者合谋，也能公平完成拍卖的实用协议。其关键技术是计时承诺——一种可以通过计算一个慢函数强制打开承诺的密码学原语，从而保证拍卖最终性。

### 相关工作

[15] Dan Boneh et al. Timed Commitments. **CRYPTO 2000** [Google Scholar](https://scholar.google.com/scholar?q=Timed+Commitments)
> 核心思路：首次提出计时承诺的概念，用于密封投标拍卖等需要公平的场合。
> 局限与区别：其原始构造要求每个承诺者采用不同的陷门，且未处理竞拍者无力支付的问题，因此无法直接实现完全去中心化拍卖。

[44] Cody Freitag et al. Non-malleable Time-Lock Puzzles and Applications. **TCC 2021** [Google Scholar](https://scholar.google.com/scholar?q=Non-malleable+Time-Lock+Puzzles+and+Applications)
> 核心思路：提出功能非可延展时间锁谜题的概念，并在隐藏有序群中构造了实用的计时承诺。
> 局限与区别：该工作未讨论如何高效地将范围证明集成到计时承诺中，未解决并发拍卖场景下的抵押品管理问题。

[71] Giulio Malavolta et al. Homomorphic Time-Lock Puzzles and Applications. **CRYPTO 2019** [Google Scholar](https://scholar.google.com/scholar?q=Homomorphic+Time-Lock+Puzzles+and+Applications)
> 核心思路：构建了具有加性同态性的计时承诺，与Paillier加密结构相关。
> 局限与区别：尽管同态性为范围证明提供了可能，但直接使用时涉及复杂的等价性证明，效率较低。

[62] Jonathan Katz et al. On the Security of Time-Lock Puzzles and Timed Commitments. **TCC 2020** [Google Scholar](https://scholar.google.com/scholar?q=On+the+Security+of+Time-Lock+Puzzles+and+Timed+Commitments)
> 核心思路：形式化了计时承诺的安全模型，并构建了基于拉格朗日插值的方案。
> 局限与区别：其结构要求亲信者生成两组陷门，且用于范围证明时需借助通用zkSNARK，导致巨大的开销（约20秒证明时间）。

[22] Benedikt Bünz et al. Bulletproofs: Short Proofs for Confidential Transactions and More. **IEEE S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Bulletproofs%3A+Short+Proofs+for+Confidential+Transactions+and+More)
> 核心思路：提出基于内积论证的短范围证明，无需可信设置。
> 局限与区别：Bulletproofs本身不提供“慢速强制打开”功能，因此需要与计时承诺结合才能抗Dos攻击。

[92] Sri Aravinda Krishnan Thyagarajan et al. Efficient CCA Timed Commitments in Class Groups. **CCS 2021** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+CCA+Timed+Commitments+in+Class+Groups)
> 核心思路：在类群中构造了CCA安全的非可延展计时承诺，并使用同态性证明来确保承诺一致性。
> 局限与区别：该方案同样需要范围证明时使用等价性证明，本文对比发现其证明时间比本文方案慢约300倍。

[39] Dominic Deuber et al. Minting Mechanism for Proof of Stake Blockchains. **ACNS 2020** [Google Scholar](https://scholar.google.com/scholar?q=Minting+Mechanism+for+Proof+of+Stake+Blockchains)
> 核心思路：提出了“计时承诺至承诺打开”的思路，用于首价密封投标拍卖。
> 局限与区别：该工作未考虑抵押品管理与并发拍卖的证明问题，未形式化非可延展计时承诺的安全组合性质。

[21] Benedikt Bünz et al. Zether: Towards Privacy in a Smart Contract World. **FC 2020** [Google Scholar](https://scholar.google.com/scholar?q=Zether%3A+Towards+Privacy+in+a+Smart+Contract+World)
> 核心思路：在区块链上使用零知识证明隐藏交易金额，其中范围证明用于检查账户余额。
> 局限与区别：Zether不提供抗Dos的机制（一旦用户拒绝揭示，金额无法恢复），且其方法不能直接应用于需要强制打开的拍卖设置。

### 核心技术与方案

本文的整体框架由两个递进的协议变体组成：Riggs-RP和Riggs-TC。Riggs-RP通过范围证明确保所有参与并发拍卖的竞拍者始终拥有足够的抵押品，而Riggs-TC通过集成一个高效的非可延展计时承诺方案，抵御竞拍者拒绝揭示或遭受拒绝服务攻击的风险。

**核心技术一：非可延展计时承诺方案TTD**

该方案基于RSA群和证明幂指数的技术，构造于一个底层（非计时）承诺方案C之上。方案运行于随机预言机模型。其核心思路是：先用C（例如带Bulletproofs的Pedersen承诺）提交竞标价b，得到一个普通承诺$com_C$和打开证明$\pi_{Open,C}$。然后，为一个重复平方难题的输入输出对$(h, z = h^{2^t} \bmod N)$添加一个随机化因子$\alpha$，计算$\hat{h} = h^\alpha \bmod N$。接着，计算$\hat{z} = z^\alpha \bmod N$，并通过哈希函数$k = H(\hat{z}, pp)$推导出一个密钥，用该密钥对$(b, \pi_{Open,C})$进行CCA安全加密，得到密文$ct$。最终承诺为$com = (com_C, (\hat{h}, ct))$。要强制打开承诺，计算$\hat{z} = \hat{h}^{2^t} \bmod N$，解密$ct$即可。该构造通过随机化输入输出对并绑定到CCA加密，实现了功能非可延展性：攻击者无法在时间t内将一个承诺“变形”为另一个包含相关竞标价的承诺。

**核心技术二：将计时承诺与范围证明（RP）高效组合的洞察**

本文关键的工程洞察在于延迟了承诺一致性检查。Riggs-RP中，用户给出一个Pedersen承诺$com_{Ped} = g^b h^{\alpha_b}$，并附带一个Bulletproofs范围证明，证明b位于有效区间（如$0 \leq b < 2^{32}$）且与已有竞标之和不超过抵押品。在Riggs-TC中，计时承诺TTD的“有效载荷”正是上述Pedersen承诺的打开信息$(b, \alpha_b)$。在竞标阶段，只验证范围证明与抵押品约束，而不检查计时承诺是否确实包含正确的$(b, \alpha_b)$——这验证被推迟到强制打开阶段。这种“承诺至承诺打开”的模式避免了对计时承诺内部的复杂代数关系直接进行零知识证明，从而避免了昂贵的等价性证明。系统因此具备了模块化优势：若无需抗Dos，可直接移除计时承诺层，退化为Riggs-RP。

**协议流程与并发拍卖管理**

竞拍者在拍卖行拥有一个公共抵押品余额bal和一个对活跃竞标总和B的Pedersen承诺$com_{active} = g^B h^{\alpha_B}$。当提交新竞标b时，竞拍者提供$com_{Ped}$并证明两个关系：b在范围内，且B+b ≤ bal。若证明通过，拍卖行通过同态加法更新$com_{active} \leftarrow com_{active} \cdot com_{Ped}$。用户提款时，需要证明提取金额amt满足B ≤ bal - amt。这确保了竞拍者在任何时刻兑付所有活跃竞标的能力。

**抗DoS攻击的激励结构**

Riggs-TC引入了自揭奖励和强制打开奖励。竞拍者需要锁定一笔抵押品作为这两份奖励的资金。如果竞拍者放弃自揭，奖励将被没收，其中强制打开奖励将支付给第一个计算强制打开证明的人。为了防范“抢先”攻击（恶意者截获并重放别人的打开证明），强制打开证明使用了水印技术：证明者（如Wesolowski的证明 [97]）可以在生成证明时嵌入自己的身份，该身份在验证时被绑定，因此只有实际执行了工作量的人能申领奖励。自揭奖励的存在确保了“扰乱”攻击（故意放弃竞标并抢先收走奖励）不会盈利。

**安全性直觉**

安全性依赖于计时承诺的功能非可延展性（确保竞标无法被篡改）、底层Pedersen承诺的绑定性和隐藏性、Bulletproofs范围证明的可靠性和零知识、以及证明幂指数的完整性。对于拍卖的“完整性”：所有有效的计时承诺都能通过强制打开恢复出唯一的值，保证了拍卖结果对所有提交竞标（包括被放弃的）公平；范围证明的可靠性确保抵押品始终覆盖活跃竞标的支付义务。对于“竞标隐私”：敌手除了能从公开抵押品大小推断出活跃竞标总价的上限外，无法获得更多信息。

### 核心公式与流程

**[TTD承诺生成]**
$$com = (com_C, (\hat{h}, ct)), \text{其中} \hat{h} = h^\alpha \bmod N, ct = CCA.Enc(H(z^\alpha \bmod N, pp), (b, \pi_{Open,C}))$$
> 作用：将底层承诺$com_C$和CCA加密的打开信息绑定到一个随机化重复平方实例上，确保非可延展性。

**[TTD强制打开]**
$$(b, \pi_{Open,C}) \leftarrow CCA.Dec(H(\hat{h}^{2^t} \bmod N, pp), ct)$$
> 作用：通过计算耗时t的重复平方恢复底层承诺的打开信息。

**[竞标验证关系 $\mathcal{R}_{\mathrm{bid}}$]**
$$\mathcal{R}_{\mathrm{bid}} = \left\{ \left((com_{Ped}, com_{active}, bal), (b, B, \alpha_b, \alpha_B)\right): com_{Ped} = g^b h^{\alpha_b} \wedge com_{active} = g^B h^{\alpha_B} \wedge 0 \leq b \leq 2^{32} \wedge B + b \leq bal \right\}$$
> 作用：一次性证明新竞标有效且不使总活跃竞标超过抵押品。

**[提款验证关系 $\mathcal{R}_{\mathrm{wdrw}}$]**
$$\mathcal{R}_{\mathrm{wdrw}} = \left\{ ((com_{active}, bal, amt), (B, \alpha)): com_{active} = g^B h^{\alpha} \wedge 0 \leq B \leq bal - amt \right\}$$
> 作用：确保提款后抵押品仍能覆盖全部活跃竞标。

### 实验结果

论文在Rust原生实现和EVM（以太坊虚拟机）编译两种环境中评测了性能。核心实验设置：BN254椭圆曲线用于Bulletproofs和SNARK基线；2048位RSA群用于计时承诺与证明幂指数；硬件为Intel Core i7-1165G7。Riggs-RP和Riggs-TC的竞标生成时间分别为66 ms和71 ms，而SNARK基线方案则需要21.7秒，差距约300倍。链上竞标提交成本：Riggs-RP约为191万gas，Riggs-TC约为221万gas，而SNARK基线方案高达1亿gas以上，高出一个数量级。相比之下，简单的“按拍卖抵押品”基线不需要范围证明，提交成本仅16万gas。Riggs协议的后续操作（如自揭）成本与SNARK基线接近（约10万gas vs 148万gas）。对于强制打开，验证时间和对延迟参数t近乎对数增长（约2800-4000微秒），完全在实用范围内。论文指出，尽管Riggs的竞标提交成本昂贵（约134美元），但在EOS或Avalanche等低费用链上可降至约1.5美元，且未来Bulletproofs可能出现预编译合约进一步降低费用。吞吐量方面，当前以太坊理论上限约为每分钟50个竞标，论文期待L2解决方案的未来改进。

### 局限性与开放问题

1. 本文的协议未能完全防止女巫攻击（Sybil attack），恶意卖家可以通过创建多个身份下虚假竞标来人为抬高最终价格，尽管这不能改变拍卖结果，但降低了拍卖的经济可信度。
2. 公共抵押品泄露了所有活跃竞标总价的上限，这为长期拍卖的竞标策略推断提供了窗口，全隐私方案（如隐藏的抵押品）尚待探索。
3. 强制打开阶段的延迟参数设定缺乏精确方法论，需要依赖对对手计算能力的保守估计（如230次平方/秒），且机会成本（锁定抵押品的时长）尚未得到充分分析。
4. 对“扰乱”攻击的经济分析停留在定性层面，未给出自揭奖励和强制打开奖励的比例选择策略，也缺少对多轮拍卖中机会成本的补偿机制。

### 强关联论文

[15] Dan Boneh et al. Timed Commitments. **CRYPTO 2000** [Google Scholar](https://scholar.google.com/scholar?q=Timed+Commitments)

[22] Benedikt Bünz et al. Bulletproofs: Short Proofs for Confidential Transactions and More. **IEEE S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Bulletproofs%3A+Short+Proofs+for+Confidential+Transactions+and+More)

[39] Dominic Deuber et al. Minting Mechanism for Proof of Stake Blockchains. **ACNS 2020** [Google Scholar](https://scholar.google.com/scholar?q=Minting+Mechanism+for+Proof+of+Stake+Blockchains)

[44] Cody Freitag et al. Non-malleable Time-Lock Puzzles and Applications. **TCC 2021** [Google Scholar](https://scholar.google.com/scholar?q=Non-malleable+Time-Lock+Puzzles+and+Applications)

[62] Jonathan Katz et al. On the Security of Time-Lock Puzzles and Timed Commitments. **TCC 2020** [Google Scholar](https://scholar.google.com/scholar?q=On+the+Security+of+Time-Lock+Puzzles+and+Timed+Commitments)

[71] Giulio Malavolta et al. Homomorphic Time-Lock Puzzles and Applications. **CRYPTO 2019** [Google Scholar](https://scholar.google.com/scholar?q=Homomorphic+Time-Lock+Puzzles+and+Applications)

[81] Krzysztof Pietrzak. Simple Verifiable Delay Functions. **ITCS 2019** [Google Scholar](https://scholar.google.com/scholar?q=Simple+Verifiable+Delay+Functions)

[92] Sri Aravinda Krishnan Thyagarajan et al. Efficient CCA Timed Commitments in Class Groups. **CCS 2021** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+CCA+Timed+Commitments+in+Class+Groups)

[97] Benjamin Wesolowski. Efficient Verifiable Delay Functions. **EUROCRYPT 2019** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+Verifiable+Delay+Functions)


## 关键词

+ 密封竞价拍卖
+ 定时承诺
+ 去中心化
+ 智能合约
+ 范围证明
+ 以太坊