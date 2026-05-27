---
title: "Separating succinct non-interactive arguments from all falsifiable assumptions"
doi: 10.1145/1993636.1993651
标题简称:
论文类型: conference
会议简称: STOC
发表年份: 2011
modified: 2025-04-08 23:42:18
---
## Separating succinct non-interactive arguments from all falsifiable assumptions

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/1993636.1993651)

## 作者

+ [Craig Gentry](Craig%20Gentry.md)
+ Daniel Wichs

## 笔记

### 背景与动机
简洁非交互式论证（SNARGs）是密码学与计算复杂性理论交叉领域的重要概念。Kilian于1992年证明了在标准密码学假设下，通过四轮交互可以构建针对NP语言的简洁论证，其中通信复杂度仅为证明者和验证者输入大小的多项式对数。Micali于1994年进一步指出，在随机预言机模型中，此类论证可以转化为非交互形式。然而，在标准模型下，没有任何简洁非交互式论证（SNARG）能够基于任何简单的密码学假设（如单项函数、陷门置换、DDH、RSA或LWE等）被证明安全，这构成了密码学基础理论中的一个显著空白。直觉上，简洁论证的不可信性质使其难以被可伪造假设所蕴含，但该直觉缺乏形式化证明。本文旨在证明：对于任何SNARG构造，不存在一个通用的黑盒归约，可以将其安全性归约到任何可伪造的密码学假设（除非该假设本身是错的）。这一结果解释了为何尽管存在随机预言机模型中的候选构造，标准模型下却长期缺乏可证明安全的SNARG方案。

### 相关工作

[Kil92] Kilian. A note on efficient zero-knowledge proofs and arguments. **STOC 1992** [Google Scholar](https://scholar.google.com/scholar?q=A+note+on+efficient+zero-knowledge+proofs+and+arguments)
> 核心思路：利用PCP定理和碰撞抵制哈希函数构造了四轮交互的简洁论证。
> 局限与区别：需要多轮交互，且无法直接转化为标准模型下的非交互形式；本文关注的是非交互且无需随机预言机的设置。

[Mic94] Micali. CS proofs. **FOCS 1994** [Google Scholar](https://scholar.google.com/scholar?q=CS+proofs)
> 核心思路：通过Fiat-Shamir启发式将Kilian的交互论证转化为随机预言机模型下的非交互论证。
> 局限与区别：安全证明依赖于随机预言机，无法在标准模型中实例化；本文旨在证明任何此类实例化都无法通过黑盒归约被证明安全。

[ABOR00] Aiello et al. Fast verification of any remote procedure call: Short witness-indistinguishable one-round proofs for NP. **ICALP 2000** [Google Scholar](https://scholar.google.com/scholar?q=Fast+verification+of+any+remote+procedure+call)
> 核心思路：提出基于私密信息检索构造两轮交互的简洁论证的具体方案。
> 局限与区别：Dwork等人的工作指出该思路存在根本性缺陷，且不能仅基于PIR安全假设证明；本文的分离结果进一步表明，任何不包含重绕技术的黑盒归约都无法证明其安全性。

[DLN+04] Dwork et al. Succinct proofs for NP and spooky interactions. **Manuscript 2004** [Google Scholar](https://scholar.google.com/scholar?q=Succinct+proofs+for+NP+and+spooky+interactions)
> 核心思路：指出基于PIR的两轮简洁论证方案存在根本性缺陷。
> 局限与区别：该工作揭示了特定构造的失败，而本文从理论层面证明了所有基于黑盒归约的证明思路均不可能成功。

[RV10] Rothblum, Vadhan. Are PCPs inherent in efficient arguments?. **Computational Complexity 2010** [Google Scholar](https://scholar.google.com/scholar?q=Are+PCPs+inherent+in+efficient+arguments)
> 核心思路：证明凡是通过黑盒归约可证安全的交互式简洁论证，均可被高效地转化为PCP系统。
> 局限与区别：该结果说明PCP是此类论证的固有组成部分，但无法像本文那样将（非交互）论证与可伪造假设彻底分离。

[IR89] Impagliazzo, Rudich. Limits on the provable consequences of one-way permutations. **STOC 1989** [Google Scholar](https://scholar.google.com/scholar?q=Limits+on+the+provable+consequences+of+one-way+permutations)
> 核心思路：首次证明密钥协商不能仅通过黑盒方式从单项置换中构造。
> 局限与区别：限制的是构造方式（黑盒构造），而本文限制的是证明方式（黑盒归约），且本文不限制构造对底层原语的使用方式。

[Pas11] Pass. Limits of security reductions from standard assumptions. **STOC 2011** [Google Scholar](https://scholar.google.com/scholar?q=Limits+of+security+reductions+from+standard+assumptions)
> 核心思路：与本文同时独立发现，对Schnorr认证方案等几个相关原语给出了类似的黑盒归约不可行性结果。
> 局限与区别：针对的是识别方案等交互原语，而本文聚焦于非交互式简洁论证。

### 核心技术与方案
本文的核心技术路线是构造一个“可模拟攻击者”，使得任何针对SNARG的黑盒归约都不能区分该攻击者与其高效模拟器，从而将SNARG的不可信安全性转化为对可伪造假设的直接攻击。

**可模拟攻击者的构造**。给定一个NP语言$L$及其子指数难的子集成员问题（存在分布$\mathcal{L}_n$在$L$上，$\bar{\mathcal{L}}_n$在补集上，它们是计算不可区分的），以及一个SNARG系统$\Pi=(\mathcal{G},\mathcal{P},\mathcal{V})$。构造一个不高效的攻击者$\bar{\mathcal{P}}$，它对输入$(1^m, \mathsf{crs})$输出一个不在$L$中的声明$\bar{x}$和对应的证明$\bar{\pi}$，其中$(\bar{x},\bar{\pi})$服从某个分布$\bar{\mathcal{L}}_m^*$。该分布由辅助信息不可区分性引理（Lemma 3.1）保证存在：对于由$\mathcal{P}$诚实生成的真实分布$\mathcal{L}_m^*$（其中$x$真且证明由$\mathcal{P}$按规则给出），存在一个同样以$\bar{x}$为边缘分布的$\bar{\mathcal{L}}_m^*$，使得两者对大尺寸的区分器（$2^{O(m^{d+2})}$）是$2^{-O(m^{d+2})}$不可区分的。由于SNARG的证明长度极短（对任何多项式大小的声明和见证，$|\pi| = \mathsf{poly}(n)(|x|+|w|)^{o(1)}$），该引理的条件可以满足。

**模拟器的设计**。模拟器$\mathcal{S}$接受安全参数$n$并访问非均匀建议。它设定一个阈值$m^*(n) = \lfloor \log^{1/(d+1)} n \rfloor$。对于查询中安全参数$m > m^*(n)$的输入，$\mathcal{S}$像诚实证明者一样：采样$(x,w) \leftarrow \mathsf{Sam}(1^m)$，计算$\pi \leftarrow \mathcal{P}(\mathsf{crs},x,w)$，输出真声明和证明。对于$m \leq m^*(n)$的查询，$\mathcal{S}$使用一个预计算的表格$\mathcal{T}_n$作为非均匀建议，该表格根据其大小（$\mathsf{poly}(n)$）和平均论证存在性，使得用表格回答的攻击者行为与原始攻击者$\bar{\mathcal{P}}$不可区分。

**不可区分性论证**。考虑一个任意的高效区分器$\mathcal{D}$（多项式大小的电路）访问$\bar{\mathcal{P}}$或$\mathcal{S}$的预言机。由于$\mathcal{D}$只能做多项式次查询，且对于$m > m^*(n)$的查询，$\bar{\mathcal{P}}$和$\mathcal{S}$的响应来自$(\bar{\mathcal{L}}_m^*, \mathcal{L}_m^*)$，这两者对于安全参数$n$下的区分器（其大小$n^{\omega(1)}$）是$n^{-\omega(1)}$不可区分的（因为$m$至少是$m^*(n)$，其相关密码学强度足以抵御$\mathcal{D}$）。对于$m \leq m^*(n)$的查询，$\mathcal{S}$的表格保证其响应与$\bar{\mathcal{P}}$完全一致。因此，$\mathcal{D}$无法区分$\bar{\mathcal{P}}$和$\mathcal{S}$。

**黑盒分离定理的证明**。假定存在一个黑盒归约$\mathcal{R}$，它通过预言机访问任意SNARG攻击者，并以不可忽略的优势打破某个可伪造假设$(\mathcal{C},c)$。令$\bar{\mathcal{P}}$为上述可模拟攻击者，则$\mathcal{R}^{\bar{\mathcal{P}}}$必以至少$c+1/q(n)$的概率使$\mathcal{C}$输出win。由于$\mathcal{C}$是高效的，我们可以将$\mathcal{R}$和$\mathcal{C}$合起来看作一个高效的区分器$\mathcal{D}^{\bar{\mathcal{P}}}$。根据模拟性质，存在模拟器$\mathcal{S}$使得$\mathcal{D}^{\mathcal{S}}$以相近的概率获胜，即$\Pr[\mathcal{R}^{\mathcal{S}} \text{ wins } \mathcal{C}] \ge c+1/q(n) - \mathsf{negl}(n)$。但$\mathcal{R}^{\mathcal{S}}$是一个高效的算法（因为$\mathcal{S}$是高效的），它直接攻击了假设$(\mathcal{C},c)$，说明该假设是假的。因此，要么假设假，要么不存在这样的归约。

上述结论也适用于指定验证者SNARG和仅需略微简洁的SNARG（证明长度仅为$o(|x|+|w|)$），此时需要指数难的子集成员问题。

### 核心公式与流程

**[可模拟攻击者定义]**
给定语言$L$上的子指数难子集成员问题$(\mathsf{Sam},\mathcal{L},\bar{\mathcal{L}})$，存在分布$\mathcal{L}_m^*$（$x\sim\mathcal{L}_m$，$\pi$是诚实证明）和$\bar{\mathcal{L}}_m^*$（$\bar{x}\sim\bar{\mathcal{L}}_m$，$\bar{\pi}$由Lemma 3.1定义），使得对$s^*(m)=2^{\Omega(m^{d+2})}$和$\epsilon^*(m)=2^{-\Omega(m^{d+2})}$，二者是$(s^*(m),\epsilon^*(m))$-不可区分的。
> 作用：这是构造攻击者和模拟器的基础，确保假声明+证明的分布与真声明+证明的分布对于大电路不可区分。

**[模拟器阈值设置]**
$$m^*(n) = \lfloor \log^{1/(d+1)} n \rfloor$$
> 作用：决定模拟器何时能通过高效采样给出真声明，何时必须依赖非均匀表格；$d$是使得CRS长度$\le O(n^d)$且证明长度$\le O(n^{d+1})(|x|+|w|)^{o(1)}$的常数。

**[辅助信息不可区分性引理]**
设$\mathcal{L}_n,\bar{\mathcal{L}}_n$是$(s(n),\epsilon(n))$-不可区分的分布。设$\mathcal{L}_n^*$是$x\sim\mathcal{L}_n$与任意$\ell(n)$比特辅助信息的联合分布。则存在$\bar{\mathcal{L}}_n^*$，其$x$边缘分布为$\bar{\mathcal{L}}_n$，且$\mathcal{L}_n^*,\bar{\mathcal{L}}_n^*$是$(s^*(n),2\epsilon(n))$-不可区分的，其中$s^*(n)=s(n)\cdot\mathsf{poly}(\epsilon(n)/2^{\ell(n)})$。
> 作用：保证了对短证明长度$\ell_{\mathsf{pf}}(m)$，存在所需的不可区分分布$\bar{\mathcal{L}}_m^*$。

**[黑盒分离定理]**
假设SNARG$\Pi=(\mathcal{G},\mathcal{P},\mathcal{V})$满足完备性和简洁性。若存在黑盒归约$\mathcal{R}^{(\cdot)}$使得对所有攻击者$\bar{\mathcal{P}}$，$\mathcal{R}^{\bar{\mathcal{P}}}$打破假设$(\mathcal{C},c)$，则$\mathcal{R}^{\mathcal{S}}$也打破假设（其中$\mathcal{S}$是$\bar{\mathcal{P}}$的模拟器），从而$(\mathcal{C},c)$是假的。
> 作用：核心定理，展示从SNARG安全性到可伪造假设的黑盒归约不可能存在。

### 实验结果
本文属于理论密码学与复杂性理论研究，不包含具体的实验或计算系统实现。其贡献为纯形式化证明，因此没有需要描述的实验设置、性能数值或数据集对比。核心成果是构造性的不可可能性证明，依赖标准密码学假设（子指数难子集成员问题）并通过数学推导验证。研究者可以通过模拟器与原始攻击者的混合论证，在理论上验证方案的正确性。所有复杂度指标（如模拟器大小为$\mathsf{poly}(n)$，区分优势为$n^{-\omega(1)}$）均在理论范畴内分析，不涉及实际运行时开销。因此，本节无实验数据可呈现。

### 局限性与开放问题
本文的分离结果主要针对黑盒归约，因此未来最重要的工作是探索能否利用非黑盒技术构造可证明安全的SNARG，这可能是克服当前障碍的唯一途径。此外，本文的分离无法直接推广到具有静态可靠性（即声明在挑战之前选定）的两轮或三轮交互式简洁论证。这一开放问题的解决对于理解交互式论证的局限性或构造此类系统具有重要意义。

### 强关联论文

[Kil92] Kilian. A note on efficient zero-knowledge proofs and arguments. **STOC 1992** [Google Scholar](https://scholar.google.com/scholar?q=A+note+on+efficient+zero-knowledge+proofs+and+arguments)

[Mic94] Micali. CS proofs. **FOCS 1994** [Google Scholar](https://scholar.google.com/scholar?q=CS+proofs)

[ABOR00] Aiello et al. Fast verification of any remote procedure call: Short witness-indistinguishable one-round proofs for NP. **ICALP 2000** [Google Scholar](https://scholar.google.com/scholar?q=Fast+verification+of+any+remote+procedure+call)

[DLN+04] Dwork et al. Succinct proofs for NP and spooky interactions. **Manuscript 2004** [Google Scholar](https://scholar.google.com/scholar?q=Succinct+proofs+for+NP+and+spooky+interactions)

[RV10] Rothblum, Vadhan. Are PCPs inherent in efficient arguments?. **Computational Complexity 2010** [Google Scholar](https://scholar.google.com/scholar?q=Are+PCPs+inherent+in+efficient+arguments)

[IR89] Impagliazzo, Rudich. Limits on the provable consequences of one-way permutations. **STOC 1989** [Google Scholar](https://scholar.google.com/scholar?q=Limits+on+the+provable+consequences+of+one-way+permutations)

[Pas11] Pass. Limits of security reductions from standard assumptions. **STOC 2011** [Google Scholar](https://scholar.google.com/scholar?q=Limits+of+security+reductions+from+standard+assumptions)


## 关键词

+ 简洁非交互式论证SNARG
+ 黑盒分离结果
+ 可证伪密码学假设
+ 随机预言机模型
+ 指定验证者论证系统
+ 简洁论证安全性基础
