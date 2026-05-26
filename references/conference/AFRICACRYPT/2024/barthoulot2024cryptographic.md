---
title: "Cryptographic accumulators: new definitions, enhanced security, and delegatable proofs"
标题简称:
论文类型: conference
会议简称: AFRICACRYPT
发表年份: 2024
created: 2025-04-16 10:02:41
modified: 2025-04-16 10:06:43
---

## Cryptographic accumulators: new definitions, enhanced security, and delegatable proofs

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-64381-1_5)

## 作者

+ Anaïs Barthoulot 
+ Olivier Blazy 
+ Sébastien Canard 

## 笔记

### 背景与动机
自 Benaloh 和 De Mare [15] 于 1993 年提出累加器概念以来，该原语已演变为保护隐私的关键工具，广泛应用于匿名凭证、电子现金和区块链等场景。然而，随着动态性、通用性、零知识等新属性的提出，累加器的定义变得碎片化，每个新属性往往伴随着一套量身定制的合成算法，导致领域内缺乏统一的模型框架。Derler、Hanser 和 Slamanig 于 2015 年提出的统一模型 [26] 虽成为重要基准，但未能覆盖此后涌现的新属性（如零知识安全性、双可计算性、可委托证明等）。本文旨在填补这一空白：提出一个基于证明系统、足够模块化以容纳所有现有及未来属性/功能的累加器新定义；同时引入一个全新的安全属性——私有评估的不可伪造性（UPE），以保护不具备签名机制的累加器免受伪造攻击；最后，深入分析可委托（非）成员证明这一复杂属性，探索其实现所需的具体前提条件。

### 相关工作

[15] Benaloh 等. One-way accumulators: a decentralized alternative to digital signatures. **EUROCRYPT 1993** [Google Scholar](https://scholar.google.com/scholar?q=One-way+accumulators:+a+decentralized+alternative+to+digital+signatures)
> 核心思路：首次提出单向累加器概念，基于 RSA 假设实现，具备准交换性。
> 局限与区别：仅支持静态集合与成员证明，缺乏统一的形式化安全定义。

[26] Derler 等. Revisiting cryptographic accumulators, additional properties and relations to other primitives. **CT-RSA 2015** [Google Scholar](https://scholar.google.com/scholar?q=Revisiting+cryptographic+accumulators,+additional+properties+and+relations+to+other+primitives)
> 核心思路：提出了动态通用累加器的统一模型，总结了当时所有主要属性（如碰撞抵抗、不可区分性、不可否认性）。
> 局限与区别：其模型不具备可扩展性，无法自然地融入后续提出的双可计算性、可委托证明等属性，本文正是基于此缺陷提出更模块化的定义。

[2] Acar 等. Revocation for delegatable anonymous credentials. **PKC 2011** [Google Scholar](https://scholar.google.com/scholar?q=Revocation+for+delegatable+anonymous+credentials)
> 核心思路：首次实现了累加器的可委托非成员证明，通过引入同态证明概念，将委托密钥定义为一系列证明的批处理结果。
> 局限与区别：该方案是特定的，未能抽象出实现可委托性所需的最小证明系统属性（如随机化、证人不可区分性）；本文证明了这些属性是必要条件并给出了形式化分析。

[12] Barthoulot 等. Dually computable cryptographic accumulators and their application to attribute based encryption. **ePrint 2023** [Google Scholar](https://scholar.google.com/scholar?q=Dually+computable+cryptographic+accumulators+and+their+application+to+attribute+based+encryption)
> 核心思路：提出了首个同时支持私有评估和公开评估的累加器方案（双可计算），基于非对称双线性群和双对配对向量空间。
> 局限与区别：该方案缺少一个独立于签名的机制来保护私有计算的累加器免受伪造。本文提出的 UPE 属性正是为了填补这一安全缺口，并证明了该方案满足 UPE。

[1] Acar 等. Revocation for delegatable anonymous credentials. **Technical Report MSR-TR-2010-170** (2010)
> 核心思路：给出了基于证明系统的累加器定义的早期版本，并定义了其完备性和可靠性。
> 局限与区别：该定义不够通用；本文将其与 Derler 等人的模型结合，给出了更完整的定义。

[11] Baric 等. Collision-free accumulators and fail-stop signature schemes without trees. **EUROCRYPT 1997** [Google Scholar](https://scholar.google.com/scholar?q=Collision-free+accumulators+and+fail-stop+signature+schemes+without+trees)
> 核心思路：扩展了累加器的定义，明确提出了碰撞抵抗性作为基本安全要求。
> 局限与区别：未考虑通用性、动态性和隐私保护属性。

[19] Camenisch 等. Dynamic accumulators and application to efficient revocation of anonymous credentials. **CRYPTO 2002** [Google Scholar](https://scholar.google.com/scholar?q=Dynamic+accumulators+and+application+to+efficient+revocation+of+anonymous+credentials)
> 核心思路：首次提出动态累加器，支持元素高效地添加、删除及证人更新。
> 局限与区别：其模型不包含通用性支持，且未定义隐私属性（如不可区分性或零知识性）。

[35] Li 等. Universal accumulators with efficient nonmembership proofs. **ACNS 2007** [Google Scholar](https://scholar.google.com/scholar?q=Universal+accumulators+with+efficient+nonmembership+proofs)
> 核心思路：提出了通用累加器概念，支持对成员和非成员关系生成证明。
> 局限与区别：其定义是针对特定功能需求的，未能实现与动态性、委托性等属性的模块化统一。

[30] Ghosh 等. Zero-knowledge accumulators and set algebra. **ASIACRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=Zero-knowledge+accumulators+and+set+algebra)
> 核心思路：提出了零知识累加器概念，要求累加值及（非）成员证明不泄露集合的任何信息，并形式化定义了该属性。
> 局限与区别：正式区分了零知识性与不可区分性；本文在安全属性关系图中确认了零知识性严格强于不可区分性。

[38] Lipmaa. Secure accumulators from Euclidean rings without trusted setup. **ACNS 2012** [Google Scholar](https://scholar.google.com/scholar?q=Secure+accumulators+from+Euclidean+rings+without+trusted+setup)
> 核心思路：引入了不可否认性安全属性，防止攻击者为同一元素同时生成有效的成员和非成员证。
> 局限与区别：本文定理2明确证明，在可信设置与私有评估模型中，不可否认性是多余的，碰撞抵抗性已足够。

### 核心技术与方案

**1. 新的累加器定义（基于证明系统）**

本文的核心技术贡献在于提出一种模块化的累加器新定义。该定义建立在 Acar 和 Nguyen [1] 给出的证明系统定义之上，同时吸收了 Derler 等人 [26] 对累加器功能的描述。具体而言，累加器方案被形式化为一组算法：Gen（密钥生成，同时输出证明系统的参数 Para）、Eval（评估算法，输出累加值 acc 和辅助信息 aux，二者共同构成证明系统的陈述 Sta）、WitCreate（证人生成算法，输出证人 Wit）、CompProof（证明计算算法，运行证明系统的 Prove 算法输出 Proof）和 Verify（验证算法，运行证明系统的 Verif 算法）。通过这种设计，累加器的**正确性**和**碰撞抵抗性**分别直接对应于底层证明系统的**完备性**和**可靠性**（定理1）。这种结构使得任何新增的功能属性（如动态性、通用性、零知识性、双可计算性等）都可以通过修改或扩展相应的证明系统或算法来“插拔”式地实现，而在定义层面只需指出关联哪个证明系统，无需重新定义整个累加器方案。该定义的核心公式包括证明系统的完备性定义：
$$
\left| \operatorname {P r} \left[ \begin{array}{c} \text {Para} \leftarrow \text {Setup} (\lambda); (\text {Sta}, \text {Wit}) \leftarrow \mathcal {A} (\text {Para}); \text {Proof} \leftarrow \text {Prove} (\text {Para}, \text {Sta}, \text {Wit}): \\ \text {Verif} (\text {Para}, \text {Sta}, \text {Proof}) = 1 \text {if} (\text {Para}, \text {Sta}, \text {Wit}) \in \mathcal {R} \end{array} \right] - 1 \right|
$$
以及碰撞抵抗性安全游戏的定义（公式 4）。

**2. 新安全属性：私有评估的不可伪造性（UPE）**

本文第二个核心贡献是提出了一个新安全属性 UPE。该属性针对具有私有评估和公开证人生成功能的静态、非通用累加器。其直观含义是：即使攻击者知道私钥并可以自由选择任何集合 $X^*$，他也无法生成一个“合法的”累加器 $acc^*$（即不通过 Eval 算法计算而得），使得存在一个属于 $X^*$ 的元素 y，其证人能通过验证。安全游戏定义如下（协议 5）：
$$
\Pr \left[ \begin{array}{c} (\mathsf {s k} _ {\mathsf {a c c}}, \mathsf {p k} _ {\mathsf {a c c}}) \gets \mathsf {G e n} (\lambda), (\mathcal {X} ^ {*}, \mathsf {a c c} ^ {*}) \gets \mathcal {A} (\mathsf {p k} _ {\mathsf {a c c}}); \\ (\mathsf {a c c} _ {\mathcal {X} ^ {*}}, \mathsf {a u x}) \gets \mathsf {E v a l} (\mathsf {s k} _ {\mathsf {a c c}}, \mathcal {X} ^ {*}), y \gets \mathcal {X} ^ {*}; \\ \mathsf {w i t} _ {y} \gets \mathsf {W i t C r e a t e} (\mathsf {p k} _ {\mathsf {a c c}}, \mathcal {X} ^ {*}, \mathsf {a c c} _ {\mathcal {X} ^ {*}}, \mathsf {a u x}, y) \\ \mathsf {P r o o f} \gets \mathsf {C o m p P r o o f} (\mathsf {p k} _ {\mathsf {a c c}}, \mathsf {a c c} _ {\mathcal {X} ^ {*}}, \mathsf {a u x}, \mathsf {w i t} _ {y}, y): \\ \mathsf {V e r i f y} (\mathsf {p k} _ {\mathsf {a c c}}, \mathsf {a c c} ^ {*}, \mathsf {P r o o f}) = 1 \end{array} \right] \leq \epsilon (\lambda)
$$
为了证明 [12] 的累加器方案满足 UPE，本文提出了一个辅助的计算性假设：固定参数双对配对向量空间求逆假设（FA-DPVS-I）。该假设陈述：给定 $( \Gamma , g _ { 1 } ^ { d _ { 2 } } , g _ { 2 } ^ { d _ { 1 } ^ { * } } , g _ { 2 } ^ { d _ { 2 } ^ { * } } )$，计算 $g _ { 1 } ^ { d _ { 1 } }$ 是困难的。证明策略是：假设存在攻击者破坏 UPE，则利用它构造一个针对 FA-DPVS-I 假设的攻击算法。后者从挑战者处获得 FA-DPVS-I 实例，使用该实例中的参数构造 [12] 方案的部分公开密钥，并利用伪造成功的累加器 $acc^*$ 与多项式 $Ch_{\mathcal X^*}(Z)$ 的系数 $a_i$ 恢复出 $g_1^{d_1}$，从而解决困难问题。该归约的关键是验证等式 $e(acc^*, g_2^{d_1^*}) = e(g_1^{d_2(y+s)}, wit_y)$，它可转化为 $e(acc^*, g_2^{d_1^*}) = e(g_1,g_2)^{\psi \sum a_i s^i}$，从而通过指数运算反解出 $g_1^{d_1}$。

**3. 可委托（非）成员证明的分析**

本文第三个贡献是对可委托证明属性进行了系统性的分析。通过将委托协议分解为 Delegation（委托）、Validation（验证）、Re-delegation（重新委托）和 MNProof computation（证明计算）四个算法，并将它们与底层证明系统的算法（Prove, Verify, RandProof, CompWit）和性质（同态性、随机化性、证人不可区分性、批处理能力）相关联，证明了实现可委托性的充分必要条件。具体而言：
- **可验证性**（Verifiability）直接依赖于证明系统的**完备性**和**可靠性**（引理6）。
- **可重新委托性**（Re-delegability）依赖于证明系统的**随机化性**（Randomizable，定义9）。因为重新委托算法本质上是对一个有效委托密钥（它本身是一个批处理证明）执行随机化算法（引理7）。
- **不可链接性**（Unlinkability）依赖于证明系统的**证人不可区分性**（Witness Indistinguishability，定义8）。因为为不同元素生成的委托密钥，本质上是对不同证人（对应不同元素）生成的证明，证人不可区分性保证了这些证明在计算上不可区分（引理8）。
- **可委托性**（Delegability）的实现最为复杂，它依赖于证明系统的**同态性**（Homomorphic，定义10）。这是因为从委托密钥生成面向特定累加器的非成员证明，需要将委托密钥（一组关于基础陈述的证明）通过同态操作组合成一个关于新陈述（acc）的证明（引理9）。

### 核心公式与流程

**[新累加器定义（定义 2 核心部分）]**
$$ \begin{aligned} &\text{Gen}(\lambda) \rightarrow \mathfrak{K}=(\mathsf{sk}_{\mathsf{acc}}, \mathsf{pk}_{\mathsf{acc}}) \\ &\text{Eval}(\mathfrak{K}, \mathcal{X}) \rightarrow (\mathsf{acc}_{\mathcal{X}}, \mathsf{aux}) \\ &\text{WitCreate}(\mathfrak{K}, \mathcal{X}, \mathsf{acc}_{\mathcal{X}}, \mathsf{aux}, x) \rightarrow \mathsf{wit}_{x}^{\mathcal{X}} \\ &\text{CompProof}(\mathsf{pk}_{\mathsf{acc}}, \mathsf{acc}_{\mathcal{X}}, \mathsf{aux}, \mathsf{wit}_{x}^{\mathcal{X}}, x) \rightarrow \mathsf{Proof} \\ &\text{Verify}(\mathsf{pk}_{\mathsf{acc}}, \mathsf{acc}_{\mathcal{X}}, \mathsf{Proof}) \rightarrow \{0, 1\} \end{aligned} $$
> 作用：形式化定义了一个基于证明系统的静态、非通用累加器方案的所有算法接口。

**[私有评估的不可伪造性（UPE）安全游戏（定义 5）]**
$$ \Pr\left[\begin{array}{c} (\mathsf{sk}_\mathsf{acc},\mathsf{pk}_\mathsf{acc})\gets\mathsf{Gen}(\lambda), (\mathcal{X}^*,\mathsf{acc}^*)\gets\mathcal{A}(\mathsf{pk}_\mathsf{acc}); \\ (\mathsf{acc}_{\mathcal{X}^*},\mathsf{aux})\gets\mathsf{Eval}(\mathsf{sk}_\mathsf{acc},\mathcal{X}^*), y\gets\mathcal{X}^*; \\ \mathsf{wit}_y\gets\mathsf{WitCreate}(\mathsf{pk}_\mathsf{acc},\mathcal{X}^*,\mathsf{acc}_{\mathcal{X}^*},\mathsf{aux},y) \\ \mathsf{Proof}\gets\mathsf{CompProof}(\mathsf{pk}_\mathsf{acc},\mathsf{acc}_{\mathcal{X}^*},\mathsf{aux},\mathsf{wit}_y,y): \\ \mathsf{Verify}(\mathsf{pk}_\mathsf{acc},\mathsf{acc}^*,\mathsf{Proof})=1 \end{array}\right]\leq\epsilon(\lambda) $$
> 作用：定义了UPE安全游戏，要求攻击者无法为一个任意选择的集合 $\mathcal{X}^*$ 生成一个它未曾计算的累加器 $\mathsf{acc}^*$，使得该累加器能通过验证。

**[FA-DPVS-I 计算假设（定义 6）]**
$$ \text{输入: } (\Gamma, g_1^{\mathsf{d}_2}, g_2^{\mathsf{d}_1^*}, g_2^{\mathsf{d}_2^*}), \quad \text{输出: } g_1^{\mathsf{d}_1} $$
> 作用：UPE安全证明所依赖的计算性假设。断言给定部分基向量的群元素，计算特定基向量在 $\mathbb{G}_1$ 中的表示是困难的。

### 实验结果
本文为纯理论性质，未包含任何实验评估或性能基准测试。所提出的定义、安全属性及分析均是形式化层面的工作。关于本文所指的、已在先前工作中被实例化的方案（如 [12] 的基于双对配对向量空间的累加器），原文也未提供其计算或通信开销的数值数据。

### 局限性与开放问题
论文指出了若干理论和实践中的开放问题。首先，安全属性关系图中，从单向域（One-Way Domain）到不可否认性（Undeniability）的蕴含关系未能证明，被列为开放问题。其次，虽然分析和论证了实现可委托非成员证明所需的条件，但尚未找到一个满足所有这些条件（特别是同态性和批处理性）的实用证明系统，因此无法给出通用的构造方法，仅指出 Groth-Sahai 证明在某些条件下是较好的候选方案。最后，UPE 属性是为了弥补特定应用场景下的安全缺口而设计，其在更广泛的累加器族（如动态、通用方案）中的适用性及潜在变种尚待探讨。

### 强关联论文

[15] Benaloh 等. One-way accumulators: a decentralized alternative to digital signatures. **EUROCRYPT 1993** [Google Scholar](https://scholar.google.com/scholar?q=One-way+accumulators:+a+decentralized+alternative+to+digital+signatures)

[26] Derler 等. Revisiting cryptographic accumulators, additional properties and relations to other primitives. **CT-RSA 2015** [Google Scholar](https://scholar.google.com/scholar?q=Revisiting+cryptographic+accumulators,+additional+properties+and+relations+to+other+primitives)

[2] Acar 等. Revocation for delegatable anonymous credentials. **PKC 2011** [Google Scholar](https://scholar.google.com/scholar?q=Revocation+for+delegatable+anonymous+credentials)

[12] Barthoulot 等. Dually computable cryptographic accumulators and their application to attribute based encryption. **ePrint 2023** [Google Scholar](https://scholar.google.com/scholar?q=Dually+computable+cryptographic+accumulators+and+their+application+to+attribute+based+encryption)

[1] Acar 等. Revocation for delegatable anonymous credentials. **Technical Report MSR-TR-2010-170** (2010)

[11] Baric 等. Collision-free accumulators and fail-stop signature schemes without trees. **EUROCRYPT 1997** [Google Scholar](https://scholar.google.com/scholar?q=Collision-free+accumulators+and+fail-stop+signature+schemes+without+trees)

[19] Camenisch 等. Dynamic accumulators and application to efficient revocation of anonymous credentials. **CRYPTO 2002** [Google Scholar](https://scholar.google.com/scholar?q=Dynamic+accumulators+and+application+to+efficient+revocation+of+anonymous+credentials)

[38] Lipmaa. Secure accumulators from Euclidean rings without trusted setup. **ACNS 2012** [Google Scholar](https://scholar.google.com/scholar?q=Secure+accumulators+from+Euclidean+rings+without+trusted+setup)

[30] Ghosh 等. Zero-knowledge accumulators and set algebra. **ASIACRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=Zero-knowledge+accumulators+and+set+algebra)

[35] Li 等. Universal accumulators with efficient nonmembership proofs. **ACNS 2007** [Google Scholar](https://scholar.google.com/scholar?q=Universal+accumulators+with+efficient+nonmembership+proofs)


## 关键词

+ 密码学累加器
+ 成员资格证明
+ 可委托证明
+ 零知识安全
+ 匿名凭证
+ 不可伪造性