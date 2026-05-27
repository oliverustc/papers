---
title: "Group signatures and more from isogenies and lattices: Generic, simple, and efficient"
doi: 10.1007/978-3-031-07085-3_4
标题简称:
论文类型: conference
会议简称: EUROCRYPT
发表年份: 2022
created: 2025-05-13 05:44:25
modified: 2025-05-13 05:46:29
---
## Group signatures and more from isogenies and lattices: Generic, simple, and efficient

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-07085-3_4)

## 作者

+ Ward Beullens
+ Samuel Dobson
+ Shuichi Katsumata
+ Yi-Fu Lai
+ Federico Pintore

## 笔记

### 背景与动机
群签名允许组内成员代表整个组匿名签名，同时被授权的追踪者可揭示签名者身份，这一机制已在实际部署中应用，如直接匿名认证（DAA）和增强隐私ID（EPID）。然而，现有后量子群签名构造面临两个主要瓶颈：一是大多数高效构造（如基于格的方案）仅满足较弱的安全属性，例如仅达到CPA匿名性或无法抵抗恶意群管理者的诬陷，而未能实现由Bootle等形式化的全CCA匿名、管理问责等理想安全性质 [11]；二是安全归约非常松散，典型归约损失达 \((N^2 Q)^{-1} \cdot \epsilon^2\)，导致实际参数需大幅放大以补偿，尤其在同源密码中因CSIDH参数有限而更难以容忍。本文旨在填补以下空白：构造第一个同时满足全CCA匿名、管理问责且签名大小仅 \(O(\log N)\) 的基于同源的后量子群签名，并构建一个通用的、可同时实例化为格（MLWE）的方案，且通过避免使用分叉引理实现更紧的安全归约。

### 相关工作

[7] Beullens et al. Calamari and Falafl: logarithmic (linkable) ring signatures from isogenies and lattices. **Asiacrypt 2020** [Google Scholar](https://scholar.google.com/scholar?q=Calamari+and+Falafl%3A+logarithmic+%28linkable%29+ring+signatures+from+isogenies+and+lattices)
> 核心思路：提出了对数大小的OR协议用于环签名，基于CSIDH和格群动作。
> 局限与区别：其协议仅满足标准的知识可靠性（通过重绕提取），不满足在线可提取性；本文将其扩展为在线可提取的NIZK，并加入对密文有效性的证明，从而构造可问责环签名。

[31] Esgin et al. MatRiCT: efficient, scalable and post-quantum blockchain confidential transactions protocol. **ACM CCS 2019** [Google Scholar](https://scholar.google.com/scholar?q=MatRiCT%3A+efficient%2C+scalable+and+post-quantum+blockchain+confidential+transactions+protocol)
> 核心思路：构造了高效的格基可问责环签名（用于保密交易），签名大小约12KB（N=64）。
> 局限与区别：仅满足CPA匿名性，且未提供管理问责（即恶意群管理者可诬陷诚实用户）；本文方案实现了全CCA匿名和管理问责，虽然签名略大但安全属性更强。

[42] Katz et al. Improved non-interactive zero knowledge with applications to post-quantum signatures. **ACM CCS 2018** [Google Scholar](https://scholar.google.com/scholar?q=Improved+non-interactive+zero+knowledge+with+applications+to+post-quantum+signatures)
> 核心思路：使用LowMC密码构造自利CCA匿名的群签名，签名大小约280KB（N=64）。
> 局限与区别：其安全性为selfless-CCA（签名密钥暴露则匿名性失效），且不满足管理问责；本文方案更小且安全属性更强。

[11] Bootle et al. Foundations of fully dynamic group signatures. **ACNS 2016** [Google Scholar](https://scholar.google.com/scholar?q=Foundations+of+fully+dynamic+group+signatures)
> 核心思路：形式化了动态群签名的理想安全模型，包括全CCA匿名、管理问责等。
> 局限与区别：本文旨在实现该模型中的所有属性，此前后量子构造均未满足。

[20] Castryck et al. CSIDH: an efficient post-quantum commutative group action. **Asiacrypt 2018** [Google Scholar](https://scholar.google.com/scholar?q=CSIDH%3A+an+efficient+post-quantum+commutative+group+action)
> 核心思路：提出可交换群动作CSIDH，用于同源密码。
> 局限与区别：本文将其作为底层群动作之一实例化HIG和PKE。

[34] Fiat & Shamir. How to prove yourself: practical solutions to identification and signature problems. **Crypto 1986** [Google Scholar](https://scholar.google.com/scholar?q=How+to+prove+yourself%3A+practical+solutions+to+identification+and+signature+problems)
> 核心思路：Fiat-Shamir变换将交互式证明转化为非交互式（NIZK）。
> 局限与区别：本文应用Fiat-Shamir后进一步证明其满足多证明在线可提取性，而不依赖于分叉引理。

[43] Katz & Wang. Efficiency improvements for signature schemes with tight security reductions. **ACM CCS 2003** [Google Scholar](https://scholar.google.com/scholar?q=Efficiency+improvements+for+signature+schemes+with+tight+security+reductions)
> 核心思路：通过为每个用户分配两个验证密钥实现紧归约。
> 局限与区别：本文将其应用于群签名，并提出了更高效的自适应变体（仅增加512B开销）。

### 核心技术与方案

**整体框架**：本文采用“加密-证明”模板构造可问责环签名（ARS），进而通过限制功能得到群签名。签名由两部分组成：一个密文（加密了索引I）和一个NIZK证明，该证明表明1）密文是对于某个索引I∈[N]的有效加密，2）签名者知道对应于环R中第I个验证密钥的签名密钥。为实例化该模板，本文利用群动作（CSIDH或MLWE）构造了基于群动作的硬实例生成器（GA-HIG）和基于群动作的公钥加密（GA-PKE），然后设计了可追踪的OR sigma协议，并通过Fiat-Shamir变换得到多证明在线可提取的NIZK。最后，通过继承在线可提取性，实现了不依赖分叉引理的紧归约；进一步利用Katz-Wang技术，通过为每个用户分配两个验证密钥（实际视为大小为2N的环），实现了完全紧的归约。

**基于群动作的HIG与PKE**：定义群动作⋆: G × X → X。HIG的实例为(X, s)满足X = s ⋆ X₀，其中s ∈ S₁（小集合），松弛关系允许s ∈ S₂+S₃。PKE的密文形式为ct = I ⋆_M (r ⋆_pk Y_pk)，其中r ∈ S̄₁。这些结构保证了可构造高效的sigma协议。

**基础可追踪OR sigma协议（Π_Σ^{base}）**：如图2所示，证明者首先采样种子seed，通过PRG生成s', r'和bits，计算每个i的承诺C_i = O(Com ‖ s'⋆X_i ‖ r'⋆_pk(-i⋆_M ct) ‖ bits_i)，构造Merkle树，发送根root。验证者发送挑战chall∈{0,1}。若chall=0，证明者回复seed，验证者重构Merkle树并校验根；若chall=1，证明者回复(s'', r'', path, bits_I)，其中s'' = s'+s, r'' = r'+r，验证者计算C̃_I = O(Com ‖ s''⋆X₀ ‖ r''⋆_pk Y_pk ‖ bits_I)并使用路径重建根，校验是否等于原根。该协议满足特殊可靠性：从两个不同挑战的响应可提取出(s, r)从而得到(I, s, r)满足关系R_sig。

**优化与主要协议（Π_Σ^{tOR}）**：通过使用种子、Merkle树和不平衡挑战空间（字符串长度M，汉明重量K），将签名大小从O(N)压缩到O(log N)。具体地，使用M次并行重复，每次的挑战为M比特中恰有K个1的字符串。对于chall=0的响应仅需发送种子（大小O(λ)），对于chall=1的响应需发送路径和bits，大小O(log N)。通过设置M和K使得K远小于M/2，签名大小主要受O(K log N)控制。

**在线可提取性**：本文证明，不添加额外承诺，直接对上述NIZK应用Fiat-Shamir即可获得多证明在线可提取性。关键观察：当挑战位为1时，响应中包含s'', r''；通过查询随机预言机中所有形如(Expand ‖ seed)的记录，在线提取器可找到seed，从而恢复(s', r')，进而得到(s, r)并提取出(I, s, r)。安全性证明中，通过引理14保证至少有一个基协议实例的挑战为1且响应有效，使得提取成功概率至少为1 - T·(Q²/2^{2λ-2} + (M·Q)/2^λ + 1/|C_{M,K}|)。

**紧归约变体**：使用Katz-Wang技术，为每个用户分配两个验证密钥(vk^{(1)}, vk^{(2)})，但用户只拥有一个对应的签名密钥。在签名时，证明者加密索引I，并证明存在b∈{1,2}使得(I, b, sk, r)满足vk_I^{(b)} = s⋆X₀。通过将环大小视为2N（两个密钥对应同一个索引），即可直接使用上述sigma协议（仅需将Merkle树叶子数从N扩展到2N，额外开销仅2比特路径）。这样，归约损失从1/N减小到可忽略（依赖于多实例困难性假设）。

### 核心公式与流程

**[关系R_sig]**
$$
R_{\text{sig}} = \left\{\left(\left(\{X_i\}_{i\in[N]}, \mathsf{pk}, \mathsf{ct}\right), (I, s, r)\right) \mid 
(I, s, r)\in [N]\times S_1\times \overline{S}_1 \; \wedge \; X_I = s\star X_0 \; \wedge \; \mathsf{ct} = \mathsf{Enc}(\mathsf{pk}, I; r) \right\}.
$$
> 定义：签名证明中需要满足的NP关系，包含了验证密钥属于环、密文加密了该索引，且证明者知道对应的秘密值。

**[基础sigma协议步骤]**
挑战空间为\{0,1\}。证明者第一轮发送Merkle根root。若挑战为0，回复种子seed；若挑战为1，回复(s'', r'', path, bits_I)，其中s'' = s'+s, r'' = r'+r。验证者校验：
- 当挑战为0时，重建所有C_i并校验root。
- 当挑战为1时，计算 $\widetilde{C}_I = \mathcal{O}(\mathsf{Com} \| s''\star X_0 \| r''\star_{\mathsf{pk}} Y_{\mathsf{pk}} \| \mathsf{bits}_I)$，使用path重建根，若等于root则接受。
> 核心：利用Merkle树实现OR证明，证明者仅需打开一个叶子即可隐藏索引I；利用群动作性质确保正确性。

**[在线可提取器]**
在线提取器OnlineExtract接收证明π，对于每个挑战位为1的基协议实例，解析出s'', r''，然后枚举随机预言机查询中所有(Expand ‖ seed)的记录，得到(s', r')，计算(s, r) = (s''-s', r''-r')，检查是否存在I使得X_I = s⋆X₀且ct = Enc(pk, I; r)。若找到则返回(I, s, r)。
> 关键：通过种子绑定s', r'，使得提取器可离线恢复完整见证。

**[紧归约变体中的关系R_sig^{Tight}]**
$$
R_{\text{sig}}^{\mathsf{Tight}} = \left\{\left((\mathsf{pp}, \{X_i^{(j)}\}_{(i,j)\in[N]\times[2]}, \mathsf{pk}, \mathsf{ct}), (I, b, \mathsf{w}, r)\right) \mid (I,r)\in[N]\times\mathcal{R} \; \wedge \; (\mathsf{x}_I^{(b)},\mathsf{w})\in R_{\mathsf{pp}} \; \wedge \; \mathsf{ct}=\mathsf{Enc}(\mathsf{pk}, I; r) \right\}.
$$
> 每个用户有两个验证密钥，但只需一个秘密密钥；签名时加密索引I，并证明存在b使得相应的验证密钥被签名。

### 实验结果

实验设置：论文未提供具体硬件或实现运行时间，但给出了签名大小的精确数值，并与现有后量子群签名方案进行了对比。对比基线包括Esgin等 (MatRiCT) [31] 和 Katz等 (KKW) [42] 的格基方案。核心性能数值见表1（原文Fig 1）：对于群大小为N=64（2^6），本文基于同源的签名大小为6.6 KB，基于格的方案（满足管理问责）为126 KB，基于格但无管理问责的为89 KB。Esgin等 [31] 在N=64时约为12 KB（但仅CPA匿名），Katz等 [42] 在N=64时约为280 KB（selfless-CCA）。随着N增长，本文方案的签名大小增长极慢：对于N=2^21，同源方案为15.5 KB，格方案（管理问责）为134 KB，格方案（无管理问责）为96 KB；而 [31] 在N=2^10时已为19 KB且后续未提供更大N的数据。这得益于本文签名大小仅与log N成正比（常系数很小），而对比方案中 [42] 在N=2^10时已达418 KB。安全属性方面，本文方案首次实现全CCA匿名和管理问责（即恶意群管理者无法诬陷用户），而 [31] 仅满足CPA匿名且无管理问责，[42] 仅满足selfless-CCA且无管理问责。因此，本文虽然在某些参数下签名大于 [31]，但安全强度更高，且签名增长趋势更平缓，适用于大规模群组。

### 局限性与开放问题

尽管本文在同源和格下实现了首个满足理想安全属性的后量子群签名，但仍存在以下不足：基于格的实例化常数较大，导致签名尺寸（约126 KB）比Esgin等人的方案（约12 KB）大一个数量级，限制了其在带宽敏感场景中的应用；同时，同源实例化虽然签名极小，但其量子安全性评估（约60比特量子安全）相对较弱，需要更依赖经典安全性。此外，本文的方案依赖于随机预言机模型（ROM），在标准模型下的构造仍是开放问题。未来研究方向包括降低格方案中的常数因子，探索基于其他群动作（如基于超奇异同源）的实例化，以及将在线可提取技术推广到更多密码协议中。

### 强关联论文

[7] Beullens et al. Calamari and Falafl: logarithmic (linkable) ring signatures from isogenies and lattices. **Asiacrypt 2020** [Google Scholar](https://scholar.google.com/scholar?q=Calamari+and+Falafl%3A+logarithmic+%28linkable%29+ring+signatures+from+isogenies+and+lattices)

[11] Bootle et al. Foundations of fully dynamic group signatures. **ACNS 2016** [Google Scholar](https://scholar.google.com/scholar?q=Foundations+of+fully+dynamic+group+signatures)

[20] Castryck et al. CSIDH: an efficient post-quantum commutative group action. **Asiacrypt 2018** [Google Scholar](https://scholar.google.com/scholar?q=CSIDH%3A+an+efficient+post-quantum+commutative+group+action)

[31] Esgin et al. MatRiCT: efficient, scalable and post-quantum blockchain confidential transactions protocol. **ACM CCS 2019** [Google Scholar](https://scholar.google.com/scholar?q=MatRiCT%3A+efficient%2C+scalable+and+post-quantum+blockchain+confidential+transactions+protocol)

[34] Fiat & Shamir. How to prove yourself: practical solutions to identification and signature problems. **Crypto 1986** [Google Scholar](https://scholar.google.com/scholar?q=How+to+prove+yourself%3A+practical+solutions+to+identification+and+signature+problems)

[42] Katz et al. Improved non-interactive zero knowledge with applications to post-quantum signatures. **ACM CCS 2018** [Google Scholar](https://scholar.google.com/scholar?q=Improved+non-interactive+zero+knowledge+with+applications+to+post-quantum+signatures)

[43] Katz & Wang. Efficiency improvements for signature schemes with tight security reductions. **ACM CCS 2003** [Google Scholar](https://scholar.google.com/scholar?q=Efficiency+improvements+for+signature+schemes+with+tight+security+reductions)

[53] Peikert. He gives C-Sieves on the CSIDH. **Eurocrypt 2020** [Google Scholar](https://scholar.google.com/scholar?q=He+gives+C-Sieves+on+the+CSIDH)

[55] Rivest et al. How to leak a secret. **Asiacrypt 2001** [Google Scholar](https://scholar.google.com/scholar?q=How+to+leak+a+secret)

[56] Unruh. Non-interactive zero-knowledge proofs in the quantum random oracle model. **Eurocrypt 2015** [Google Scholar](https://scholar.google.com/scholar?q=Non-interactive+zero-knowledge+proofs+in+the+quantum+random+oracle+model)


## 关键词

+ 群签名
+ 同源群动作
+ 格假设
+ 后量子密码
+ 可问责环签名