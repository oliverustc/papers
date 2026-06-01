---
title: "Kryvos: Publicly tally-hiding verifiable e-voting"
doi: 10.1145/3548606.3560701
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2022
created: 2025-05-07 21:48:00
modified: 2025-05-07 21:48:32
---
## Kryvos: Publicly tally-hiding verifiable e-voting

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3548606.3560701)

## 作者

+ Nicolas Huber 
+ [Ralf Küsters](Ralf%20K%C3%BCsters.md)
+ Toomas Krips 
+ Julian Liedtke 
+ Johannes Müller 
+ [Daniel Rausch](Daniel%20Rausch.md)
+ Pascal Reisert 
+ Andreas Vogt 

## 笔记

### 背景与动机
选举是民主进程的核心支柱，但传统电子投票系统为保障可验证性，通常需公开完整计票结果（即所有聚合后的个人选票），这引发了一系列严重问题。例如，公开各候选人得票数可能使落选候选人难堪，或在小胜优势下削弱获胜者的执政合法性。更严重的是，在优先投票（如即时决选投票IRV）中，即使候选人数量适中，个体选民的投票组合也可能成为独特的“指纹”，导致被动对手仅凭公开计票就能轻易实施“意大利式攻击”来胁迫选民 [13] [49]。为应对这些问题，学界提出了完全计票隐藏系统（如基于通用可验证多方计算MPC的方案），这些系统仅公布最终结果（如获胜者），但对所有方（包括计票方）隐藏中间计票，导致其仅适用于少量候选人和简单投票方法，效率低下。另一类部分计票隐藏系统（如 [79]）则仅隐藏引发特定问题的部分计票信息，仍可能泄露如候选人排名等信息。然而，在现实中，众多选举（如ACM SIG、德国计算机协会 [42]、SIAM [82] 等）普遍采用一种折衷做法：计票方内部计算并学习完整计票，但仅向公众公布最终结果。这种被称为“公开计票隐藏”的做法能解决对公众的上述隐私问题，但当前因缺乏实用系统而不得不牺牲可验证性。Kryvos的目标正是填补这一空白，为这种常见实践提供首个可证明安全的可验证电子投票系统。

### 相关工作

[14] Benaloh. **Verifiable Secret Ballot Elections. PhD thesis, 1987** [Google Scholar](https://scholar.google.com/scholar?q=Verifiable+Secret+Ballot+Elections)
> 核心思路：最早提出完全计票隐藏电子投票系统的概念。
> 局限与区别：未提供正式安全证明或实现，Kryvos首次为公开计票隐藏实践提供了形式化定义与实现。

[62] Küsters et al. **Ordinos: A Verifiable Tally-Hiding Remote E-Voting System. IEEE EuroS&P 2020** [Google Scholar](https://scholar.google.com/scholar?q=Ordinos+A+Verifiable+Tally-Hiding+Remote+E-Voting+System)
> 核心思路：首个可证明安全的完全计票隐藏系统，基于MPC实现，支持简单投票方法。
> 局限与区别：因采用强隐私保护对计票员隐藏计票，效率有限，尤其对复杂投票方法和大量候选人；Kryvos以公开计票隐藏为代价，换取了显著更优的性能和更广的适用性。

[79] Ramchen et al. **Universally Verifiable MPC and IRV Ballot Counting. FC 2019** [Google Scholar](https://scholar.google.com/scholar?q=Universally+Verifiable+MPC+and+IRV+Ballot+Counting)
> 核心思路：针对IRV选举的部分计票隐藏系统，可处理现实世界数据，保护选票顺序防意大利攻击。
> 局限与区别：仍向公众泄露候选人顺序等中间信息，可能引发候选人尴尬等问题；Kryvos则对公众完全隐藏计票，提供更强的公开隐私。

[21] Canard et al. **Practical Strategy-Resistant Privacy-Preserving Elections. ESORICS 2018** [Google Scholar](https://scholar.google.com/scholar?q=Practical+Strategy-Resistant+Privacy-Preserving+Elections)
> 核心思路：专门为多数判决投票设计的完全计票隐藏系统。
> 局限与区别：处理多个候选人+等级时耗时较长（如20分钟），且系统有一定概率不输出结果；Kryvos处理同等规模问题仅需数秒，且提供可证明安全性。

[50] Hertel et al. **Extending the Tally-Hiding Ordinos System... IACR ePrint 2021** [Google Scholar](https://scholar.google.com/scholar?q=Extending+the+Tally-Hiding+Ordinos+System+Implementations+for+Borda+Hare-Niemeyer+Condorcet+and+Instant-Runoff+Voting)
> 核心思路：将Ordinos扩展到Borda、Condorcet等复杂投票方法。
> 局限与区别：性能瓶颈仍然明显，如Condorcet Smith Set在约200个选项时需超过80秒；Kryvos在所有测试方法上均展现出更快的计票证明时间。

### 核心技术与方案
Kryvos的核心设计理念是彻底重新构想基于同态承诺的电子投票系统，而非直接修改Helios之类的加密方案。如果简单地在Helios基础上让计票员用ZKP证明结果正确，则计票员需要知道所有私钥分片作为证明的witness，这将破坏选票隐私。因此，Kryvos采用了一条新的技术路线：基于Pedersen向量承诺的加性同态承诺方案，而非IND-CPA安全的加密方案。

系统流程如下：在投票阶段，每位选民将其投票向量（$m^i \in C$）中的每个分量进行全阈值秘密分享，分发给所有计票员。每个计票员将其收到的份额作为输入，创建一个本地的Pedersen向量承诺。由于承诺具有加性同态性，将所有计票员的本地承诺相加，即可得到一个对原始投票向量的公开承诺$c^{i,l}$，无需解密。选民使用Groth16 SNARK [45] 生成一个零知识证明$\Pi_{ballot}^i$，证明公开承诺中隐藏的投票向量$m^i$属于有效投票空间$C$，从而确保了选票的合法性。投票者使用IND-CCA2安全的公钥加密将每个计票员的份额和盲化因子发送给对应的计票员，确保选票份额的保密传输。计票员在验证份额打开后，进行内部同态聚合得到完整计票$T$。最后，指定的计票员计算最终结果$y = f_{res}(T)$，并生成一个Groth16 SNARK证明，其公共输入为聚合后的承诺$(c^{\perp,1},...,c^{\perp,n_{tuples}})$和结果$y$，私密输入为$T$和打开值，证明$y$确实是正确计票的结果。公众仅需验证此SNARK的正确性。

在性能优化方面，Kryvos通过使用Pedersen向量承诺将多个投票分量（即一个“元组”）打包到一个承诺中，显著减少了承诺的数量和后续SNARK的约束数量，尤其是在处理大量选项时（见表1）。系统通过选择合适的“槽大小”$N$来平衡证明复杂度。对于大规模问题（如IRV），系统允许通过将投票拆分为多个元组并并行生成多个子证明来进一步优化性能（如表2所示）。安全性上，Kryvos依赖于以下假设：承诺方案的计算绑定性和完美隐藏性，SNARK的完美零知识和计算可靠性，以及加密方案的IND-CCA2安全性。这些属性确保了系统满足公开计票隐藏的两个核心要求：公开隐私（向公众仅泄露结果，达到理想隐私水平）和内部隐私（向计票员泄露完整计票，与安全非隐藏系统一致）。

### 核心公式与流程

**[Pedersen向量承诺]**
$$\text{Com}((v_1, ..., v_N), r) = g_1^{v_1} \cdot ... \cdot g_N^{N} \cdot h^r$$
> 作用：用于一次性承诺一个包含 $N$ 个元素的向量，通过向量承诺，Kryvos极大地减少了证明分解后多个投票分量所需的承诺数量和SNARK约束数量，是系统性能优化的基石。

**[SNARK证明的公开输入关系]**
$$R: ( (c^{\perp,1}, ..., c^{\perp,n_{tuples}}, y), (T, (r^{\perp,1}, ..., r^{\perp,n_{tuples}})) ) \in R \iff \forall l: c^{\perp,l} = \text{Com}(T_{(l)}, r^{\perp,l}) \land y = f_{res}(T) $$
> 作用：定义了计票SNARK证明的NP关系，即存在一个公开的聚合承诺 $c^{\perp,l}$ 私密地打开到计票 $T$，并且函数 $f_{res}$ 在 $T$ 上计算的结果 $y$ 是公开的。

**[秘密共享与原像聚合]**
$$ m^{i,j} = \sum_{k=1}^{n_t} m_k^{i,j} \mod q $$
$$ c^{i,l} = \sum_{k=1}^{n_t} c_k^{i,l} $$
> 作用：第一式表明每个投票分量 $m^{i,j}$ 被秘密分享到所有 $n_t$ 个计票员，且可以异或（加法）恢复。第二式表明每个计票员的承诺 $c_k^{i,l}$ 相加后得到对原始投票的公开承诺 $c^{i,l}$。

### 实验结果
实验采用Ubuntu 20.04, 16GB RAM, 8核CPU环境，所有基准测试均在单线程下运行以确保可比性。Kryvos成功处理了多种投票方法，包括单票（最多250个选项）、多票、Borda计数、Condorcet方法、多数判决以及复杂的即时决选投票IRV（如澳大利亚新南威尔士州2015年立法议会选举）。对于大多数投票方法，计票阶段的SNARK生成时间随选项数量线性增长，在1000个选项时仅需约100秒，远快于多数判决的Ordinos [62]和Canard等 [21]（在相同参数下Ordinos需超过80秒）。对于大规模IRV（例如6位候选人得1957个选项），通过将投票拆分为多个元组（如10个slot），投票者可在17秒（并行）内生成选票有效性证明。在与部分计票隐藏系统 [79] 的对比中，Kryvos在Albury（5位候选人，46347选民）和Auburn（6位候选人，43783选民）选区的计票耗时分别仅为30秒和177秒，显著优于[79]的2小时和15小时，且公开可验证性更强。系统可支持高达$2^{32}-1$个选民的规模。

### 局限性与开放问题
Kryvos做出了一项明确的权衡：它假设计票员是诚实的，从而满足公开隐私；如果计票员被攻破，他们可以获取完整计票。未来的工作可以考虑结合秘密共享或阈值技术来减轻单一计票员权限过高的问题。虽然Kryvos使用了高效且应用的Groth16 SNARK，但其通用可信设置需求（CRS）对特定选举方法而言依然笨重，未来可以探索使用透明设置（transparent setup）或通用CRS的证明系统。此外，如何将Kryvos扩展到支持更复杂的投票方法（如STV）或更多候选人的更优优化也是值得探索的方向。

### 强关联论文

[14] Benaloh et al. **Verifiable Secret Ballot Elections. PhD thesis 1987** [Google Scholar](https://scholar.google.com/scholar?q=Verifiable+Secret+Ballot+Elections)

[21] Canard et al. **Practical Strategy-Resistant Privacy-Preserving Elections. ESORICS 2018** [Google Scholar](https://scholar.google.com/scholar?q=Practical+Strategy-Resistant+Privacy-Preserving+Elections)

[50] Hertel et al. **Extending the Tally-Hiding Ordinos System: Implementations for Borda, Hare-Niemeyer, Condorcet, and Instant-Runoff Voting. IACR ePrint 2021** [Google Scholar](https://scholar.google.com/scholar?q=Extending+the+Tally-Hiding+Ordinos+System+Implementations+for+Borda+Hare-Niemeyer+Condorcet+and+Instant-Runoff+Voting)

[62] Küsters et al. **Ordinos: A Verifiable Tally-Hiding Remote E-Voting System. IEEE EuroS&P 2020** [Google Scholar](https://scholar.google.com/scholar?q=Ordinos+A+Verifiable+Tally-Hiding+Remote+E-Voting+System)

[79] Ramchen et al. **Universally Verifiable MPC and IRV Ballot Counting. FC 2019** [Google Scholar](https://scholar.google.com/scholar?q=Universally+Verifiable+MPC+and+IRV+Ballot+Counting)

[84] Szepieniec et al. **New Techniques for Electronic Voting. JETS 2015** [Google Scholar](https://scholar.google.com/scholar?q=New+Techniques+for+Electronic+Voting)

[86] Wen et al. **Minimum Disclosure Counting for the Alternative Vote. VoteID 2009** [Google Scholar](https://scholar.google.com/scholar?q=Minimum+Disclosure+Counting+for+the+Alternative+Vote)

[45] Groth. **On the Size of Pairing-Based Non-interactive Arguments. EUROCRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=On+the+Size+of+Pairing-Based+Non-interactive+Arguments)

[77] Pedersen. **Non-Interactive and Information-Theoretic Secure Verifiable Secret Sharing. CRYPTO 1991** [Google Scholar](https://scholar.google.com/scholar?q=Non-Interactive+and+Information-Theoretic+Secure+Verifiable+Secret+Sharing)

[16] Bootle et al. **Efficient Batch Zero-Knowledge Arguments for Low Degree Polynomials. PKC 2018** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+Batch+Zero-Knowledge+Arguments+for+Low+Degree+Polynomials)


## 关键词

+ 电子投票
+ 隐私保护
+ 零知识证明
+ 可验证性
+ 民主制度