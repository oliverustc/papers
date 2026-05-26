---
title: "FLOSS: Fast Linear Online Secret-Shared Shuffling"
标题简称:
论文类型: preprint
预印本简称: archive
发表年份: 2026
---

## FLOSS: Fast Linear Online Secret-Shared Shuffling

## 发表信息

+ [原文链接](https://eprint.iacr.org/2026/672)

## 作者

+ Ian Chang
+ Sela Navot
+ [Alex Ozdemir](Alex Ozdemir.md)
+ [Nirvan Tyagi](Nirvan Tyagi.md)

## 笔记

### 背景与动机

随机排列私密数据向量是许多隐私保护协议（如数据分析、广告归因、匿名通信）的核心构建块。现有方法要么依赖计算密集的公钥密码和零知识证明，要么因使用拟线性规模的置换网络而在大向量上扩展性差。Chase等人在半诚实模型下引入的预洗牌元组思想[11]，将洗牌工作推向离线预处理阶段，使在线阶段仅需线性计算和通信，但该方案缺乏针对恶意敌手的认证机制。将这一思路提升至恶意安全设置面临巨大挑战：简单地在认证秘密共享上叠加洗牌元组会遭受选择性失败攻击，恶意方可通过猜测置换映射或窃取秘密值来破坏协议。为此，本文旨在设计一种恶意安全的、在线阶段具有线性复杂度的两方秘密共享洗牌协议，同时保证预处理阶段的开销可控。

### 相关工作

[11] Chase 等. Secret-shared shuffle. **ASIACRYPT 2020** [Google Scholar](https://scholar.google.com/scholar?q=Secret-shared+shuffle)
> 核心思路：提出预洗牌元组（shuffle tuple）概念，在半诚实模型下实现线性在线洗牌，将置换网络计算推至离线。
> 局限与区别：缺乏恶意安全性；其后的恶意安全化尝试如[21, 22]均被发现存在选择失效攻击，本文通过引入额外认证密钥从根本上消除该攻击。

[22] Song 等. Secret-shared shuffle with malicious security. **NDSS 2024** [Google Scholar](https://scholar.google.com/scholar?q=Secret-shared+shuffle+with+malicious+security)
> 核心思路：通过多次重复洗牌和剪枝-选择（cut-and-choose）技术提升安全性，使用泄漏型的随机置换矩阵。
> 局限与区别：其协议仍受本文发现的新型选择失效攻击影响；且因重复应用和剪枝过程导致具体代价高昂（对于2^20向量在线时间达1835秒）；本文彻底避免了剪枝-选择。

[13] Mohassel 等. Actively secure private function evaluation. **ASIACRYPT 2014** [Google Scholar](https://scholar.google.com/scholar?q=Actively+secure+private+function+evaluation)
> 核心思路：基于置换网络的恶意安全两方计算，使用置换编码技术实现常数轮在线。
> 局限与区别：在线阶段仍为O(n log n)复杂度；本文将其作为预处理生成认证洗牌元组的底层协议，复用控制位以生成关联的逆置换元组。

[9] Damgård 等. Multiparty computation from somewhat homomorphic encryption. **CRYPTO 2012** [Google Scholar](https://scholar.google.com/scholar?q=Multiparty+computation+from+somewhat+homomorphic+encryption)
> 核心思路：提出SPDZ框架，使用认证秘密共享实现恶意安全算术电路计算，通过离线生成的乘法三元组和输入元组支持高效率在线计算。
> 局限与区别：SPDZ本身不提供直接的置换操作；本文在SPDZ基础上扩展了置换门和盲认证检查。

[10] Chase 等. Efficient permutation correlations and batched random access. **PKC 2025** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+permutation+correlations+and+batched+random+access)
> 核心思路：改进Chase等人的洗牌元组生成，关注半诚实模型下的效率提升。
> 局限与区别：未考虑恶意安全性。

[5] Asharov 等. Efficient secure three-party sorting. **CCS 2022** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+secure+three-party+sorting)
> 核心思路：提出高效的基数排序-与-洗牌协议，在半诚实三方模型下利用洗牌和逆洗牌构建排序。
> 局限与区别：工作于三方半诚实模型；本文将其思路适配到两方恶意模型，并形式化为算术置换电路描述。

[1] Anderson 等. Precio: Private aggregate measurement via oblivious shuffling. **CCS 2024** [Google Scholar](https://scholar.google.com/scholar?q=Precio+Private+aggregate+measurement+via+oblivious+shuffling)
> 核心思路：使用洗牌构建隐私保护聚合统计协议。
> 局限与区别：可受益于本文的更高效恶意安全洗牌原语。

[14] Waksman. A permutation network. **J. ACM 1968** [Google Scholar](https://scholar.google.com/scholar?q=A+permutation+network)
> 核心思路：提出Waksman置换网络拓扑，使用O(n log n)个开关实现任意n元素置换。
> 局限与区别：本文将其作为底层网络实现，用于预处理阶段生成认证洗牌元组。

[7] Beaver. Efficient multiparty protocols using circuit randomization. **CRYPTO 1991** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+multiparty+protocols+using+circuit+randomization)
> 核心思路：提出乘法三元组（Beaver triples）技术，使在线乘法仅需一次通信。
> 局限与区别：三元组技术仅用于乘法，本文将其与洗牌元组结合使用。

[15] Keller 等. MASCOT: faster malicious arithmetic secure computation with oblivious transfer. **CCS 2016** [Google Scholar](https://scholar.google.com/scholar?q=MASCOT+faster+malicious+arithmetic+secure+computation+with+oblivious+transfer)
> 核心思路：基于不经意传输的高效恶意安全预处理协议，生成SPDZ所需乘法三元组和输入元组。
> 局限与区别：本文将其作为底层预处理协议之一，用于生成算术电路计算所需材料。

[16] Keller 等. Overdrive: Making SPDZ great again. **EUROCRYPT 2018** [Google Scholar](https://scholar.google.com/scholar?q=Overdrive+Making+SPDZ+great+again)
> 核心思路：提出LowGear，进一步优化SPDZ预处理效率，支持更大批量三元组生成。
> 局限与区别：本文在较大向量规模时使用LowGear作为预处理协议。

### 核心技术与方案

FLOSS协议的整体框架在SPDZ恶意安全算术电路计算基础上，扩展了一个算术置换电路抽象，该抽象在标准加法和乘法门之外，明确支持一方已知的置换门和逆置换门。协议分为离线预处理和在线执行两个阶段。离线阶段生成认证洗牌元组（authenticated shuffle tuple），在线阶段通过高效消耗这些元组实现置换。

在线应用认证洗牌元组的具体协议如图2所示。核心思想是当一方（如P₀）持有置换π和认证密钥κ，另一方P₁拥有随机向量a和b时，双方已有预处理的认证关联元组⟨π(a)⟩^{(κ)}和⟨π(b)⟩^{(κ)}。应用时，P₁利用a盲化其数据份额得到c，并发送给P₀。P₀将自身份额加上π(c)和⟨π(a)⟩₀得到新的份额，而P₁直接设置⟨π(a)⟩₁为新份额。验证时，双方对κ-乘后的份额⟨κπ(x)⟩执行盲认证检查（BlindAuth），而非直接检查⟨π(x)⟩。这样，即使恶意方在发送c时引入扰动，由于其无法预知κ，扰动将导致检查失败，从而杜绝了置换猜测攻击。

盲认证检查子协议（图1）用于验证一组未经重构的密文共享值是否与认证标签一致。该协议通过联合采样随机系数r，计算值和认证标签的随机线性组合ℓ和γℓ，然后检查ϵ=γℓ-γ·ℓ是否为0。由于ℓ是随机盲化因子α与数据线性组合的和，开ℓ时敌手看到的仅仅是随机数，保证了安全性。

预处理协议依托Mohassel等人的恶意安全置换网络[13]生成认证洗牌元组。如图22所示，P₀首先将置换π解析为置换网络的控制位，双方通过SPDZ的输入协议共享控制位的认证份额，并检查其二进制合法性。然后为要洗牌的每一个向量（如a和b）生成线随机盲值r和认证盲值l，以及一次性密钥ι。路由计算阶段，双方利用控制位盲值和盲值份额计算输出盲值的差值s和认证差值Δ，并通过重构将它们公开。在线评估时，P₀先通过输入协议接收P₁的向量a和b的认证共享，然后用盲值叠加得到公开值t和τ，接着按控制位在置换网络中传播。最后对输出线上公开的t和τ执行认证检查，若失败则中止。通过后，从t和r的份额还原出置换后的认证共享⟨π(a)⟩和⟨π(b)⟩。

为进一步支持逆置换操作，预处理协议还支持生成关联的逆洗牌元组（图24）。其核心是复用同一组控制位，但将路由计算方向反转（从右向左），并将验证检查放在输入线而非输出线上。这使得可以高效地生成与同一置换π关联的逆置换元组，而不需要重新计算整个置换网络。

获得基础认证共享后，ApplyKappaPrep子协议（图25）通过SPDZ乘法将κ乘入这些共享，得到⟨κ·π(a)⟩和⟨κ·π(b)⟩。随后执行一次盲认证检查，验证乘法过程未受篡改，最终输出⟨π(a)⟩^{(κ)}和⟨π(b)⟩^{(κ)}。

安全性证明（附录D）表明FLOSS在(F_SPDZPrep, F_ShufTuplePrep, F_Comm)混合模型下UC安全地实现了算术置换电路理想功能。模拟器通过跟踪诚实方的预期份额和检测敌手发送值与预期值之间的偏差来构造，而盲认证检查确保了任何非零偏差要么以极大概率被捕获，要么在计算上无法被利用。

### 核心公式与流程

**[应用认证洗牌元组（ApplyShufTup）]**
$$  
\overrightarrow{c} \leftarrow [\![ \overrightarrow{v} ]\!]_1 - \overrightarrow{a},\quad \overrightarrow{d} \leftarrow [\![ \gamma \overrightarrow{v} ]\!]_1 - \overrightarrow{b}  
$$  
$$  
[\![ \pi(\overrightarrow{v}) ]\!]_0 \leftarrow \pi([\![ \overrightarrow{v} ]\!]_0) + \pi(\overrightarrow{c}) + [\![ \overrightarrow{\widetilde{a}} ]\!]_0  
$$  
$$  
[\![ \gamma \pi(\overrightarrow{v}) ]\!]_0 \leftarrow \pi([\![ \gamma \overrightarrow{v} ]\!]_0) + \pi(\overrightarrow{d}) + [\![ \overrightarrow{\widetilde{b}} ]\!]_0  
$$  
$$  
[\![ \kappa \pi(\overrightarrow{v}) ]\!]_0 \leftarrow \kappa \cdot \pi([\![ \overrightarrow{v} ]\!]_0) + \kappa \cdot \pi(\overrightarrow{c}) + [\![ \kappa \overrightarrow{\widetilde{a}} ]\!]_0  
$$  
$$  
[\![ \gamma \kappa \pi(\overrightarrow{v}) ]\!]_0 \leftarrow \kappa \cdot \pi([\![ \gamma \overrightarrow{v} ]\!]_0) + \kappa \cdot \pi(\overrightarrow{d}) + [\![ \kappa \overrightarrow{\widetilde{b}} ]\!]_0  
$$

> 作用：描述了在线阶段应用一个已预处理认证洗牌元组的完整本地计算过程。P₁发送盲化向量c和d后，双方各自的份额更新公式保证了最终恢复值和认证的正确性，同时盲认证检查在κ-乘后份额上执行以检测篡改。

**[盲认证检查（BlindAuth）]**
$$  
\ell = \alpha + \sum_{i=1}^n r^{i-1} z_i,\quad [\![ \gamma\ell ]\!] = [\![ \gamma\alpha ]\!] + \sum_{i=1}^n r^{i-1} [\![ \gamma z_i ]\!]  
$$  
$$  
[\![ \epsilon ]\!] = [\![ \gamma\ell ]\!] - [\![ \gamma ]\!] \cdot \ell,\quad \text{检查 } [\![ \epsilon ]\!]_0 + [\![ \epsilon ]\!]_1 = 0  
$$

> 作用：在不泄露数据z_i和认证密钥γ的条件下，验证一组认证共享的安全性。通过随机线性组合和共享的盲因子α，确保恶意方无法构造伪造的认证关系。

**[安全域条件]**  
$$  
|\mathbb{F}| \geq 2^\lambda,\quad \lambda \text{ 为安全参数}  
$$

> 作用：协议安全依赖于域大小指数于安全参数，确保信息论攻击的成功概率可忽略。

**[渐进复杂度]**  
在线：O(n) 通信和计算；离线：O(n log n) 通信和计算。

> 作用：总结FLOSS的渐进效率。在线阶段仅为线性复杂度，而离线阶段虽然为O(n log n)，但可预先执行，不影响在线延迟。

### 实验结果

实验设置：双方运行在AWS EC2 c5.18xlarge实例（72 vCPU），网络带宽约25 Gbps。对比基线包括SimpleNet（朴素对数轮置换网络）、PermNet（Mohassel等恶意安全置换网络[13]）和OPM（Song等恶意安全洗牌[22]）。对于洗牌2^20个元素，FLOSS在线时间<500ms，比PermNet（406s）快约800倍，比OPM（1835s）快约3600倍，且离线成本仅为OPM的1/5（0.33美元对比1.75美元）。在线通信方面，FLOSS仅33.6MB，比PermNet的201.3MB低6倍，比OPM的11.5GB低341倍。

对于排序应用，Radix[FLOSS]在2^13个32位输入上在线时间仅3.1秒，远优于Radix[PermNet]的23.8秒和SortNet的7284秒。离线成本仅为0.52美元，低于StS[OPM]（0.77美元）和SortNet（1.90美元）。整体上，FLOSS在大规模洗牌和排序中实现了最好的在线-离线权衡。

### 局限性与开放问题

首先，FLOSS的安全性依赖于域大小指数于安全参数，对于小域（如二进制域）需要额外适配。其次，协议目前仅支持两方设置，扩展到多方场景需要更复杂的预处理协议。最后，预处理的离线成本虽然低于现有方案但仍为O(n log n)量级，对于频繁变动的洗牌需求，离线阶段的开销可能成为瓶颈。

### 强关联论文

[9] Damgård et al. Multiparty computation from somewhat homomorphic encryption. **CRYPTO 2012**

[5] Asharov et al. Efficient secure three-party sorting with applications to data analysis and heavy hitters. **CCS 2022**

[11] Chase et al. Secret-shared shuffle. **ASIACRYPT 2020**

[22] Song et al. Secret-shared shuffle with malicious security. **NDSS 2024**

[13] Mohassel et al. Actively secure private function evaluation. **ASIACRYPT 2014**

[15] Keller et al. MASCOT: faster malicious arithmetic secure computation with oblivious transfer. **CCS 2016**

[16] Keller et al. Overdrive: Making SPDZ great again. **EUROCRYPT 2018**

[14] Waksman. A permutation network. **J. ACM 1968**

[7] Beaver. Efficient multiparty protocols using circuit randomization. **CRYPTO 1991**

[1] Anderson et al. Precio: Private aggregate measurement via oblivious shuffling. **CCS 2024**


## 关键词

+ FLOSS线性时间在线秘密共享洗牌
+ 恶意安全双方计算2PC洗牌协议
+ 算术置换电路秘密共享置换
+ 预处理方法快速在线洗牌
+ 隐私保护分析广告通信协议
