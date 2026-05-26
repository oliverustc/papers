---
title: "Zero-knowledge accumulators and set algebra"
标题简称:
论文类型: conference
会议简称: ASIACRYPT
发表年份: 2016
modified: 2025-04-13 13:49:35
---

## Zero-knowledge accumulators and set algebra

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-662-53890-6_3)

## 作者

+ Esha Ghosh 
+ Olga Ohrimenko 
+ [Dimitrios Papadopoulos](Dimitrios%20Papadopoulos.md) 
+ Roberto Tamassia 
+ [Nikos Triandopoulos](Nikos%20Triandopoulos.md)
## 笔记

### 背景与动机
传统密码学累加器通过一个简洁的积累值表示集合，并允许生成常大小的成员或非成员证明，但现有方案仅保证正确性而完全不提供隐私：证明本身会泄露关于被积累集合的信息，例如集合大小或元素分布。在域名系统安全、匿名加密货币和匿名凭证等应用场景中，攻击者通过观察积累值和证明即可推断敏感信息，这与隐私需求直接冲突。虽然 de Meer 等 [20] 和 Derler 等 [23] 曾尝试引入不可区分性隐私定义，但前者定义存在内在缺陷，后者未能保护更新操作——即攻击者可以轻松验证自己对元素增删操作的猜测是否正确。本文旨在填补这一空白：提出严格的零知识累加器定义，要求积累值和所有证明（包括动态更新后的累积值）均不泄露集合的任何信息，并构造首个满足该定义的方案。

### 相关工作

[4] Benaloh and de Mare. One-way accumulators: a decentralized alternative to digital signatures. **EUROCRYPT 1993** [Google Scholar](https://scholar.google.com/scholar?q=One-way+accumulators+a+decentralized+alternative+to+digital+signatures)
> 核心思路：首次引入累加器概念，通过单向函数将集合压缩为单个积累值。
> 局限与区别：仅支持成员证明，无隐私保护。

[53] Nguyen. Accumulators from bilinear pairings and applications. **CT-RSA 2005** [Google Scholar](https://scholar.google.com/scholar?q=Accumulators+from+bilinear+pairings+and+applications)
> 核心思路：基于双线性对的累加器构造，支持成员证明。
> 局限与区别：完全暴露积累值，无隐私保护。

[23] Derler et al. Revisiting cryptographic accumulators, additional properties and relations to other primitives. **CT-RSA 2015** [Google Scholar](https://scholar.google.com/scholar?q=Revisiting+cryptographic+accumulators+additional+properties+and+relations+to+other+primitives)
> 核心思路：引入不可区分性隐私定义，区分静态集合和动态更新的隐私。
> 局限与区别：更新过程为确定性算法，插入或删除元素后的积累值变化可被攻击者探测，不满足零知识。

[2] Au et al. Dynamic universal accumulators for DDH groups. **CT-RSA 2009** [Google Scholar](https://scholar.google.com/scholar?q=Dynamic+universal+accumulators+for+DDH+groups+and+their+application+to+attribute-based+anonymous+credential+systems)
> 核心思路：首次实现动态通用累加器，支持成员和非成员证明的高效更新。
> 局限与区别：证明构造中通过揭示余数来证明非成员，破坏了零知识。

[52] Naor and Ziv. Primary-secondary-resolver membership proof systems. **TCC 2015** [Google Scholar](https://scholar.google.com/scholar?q=Primary-secondary-resolver+membership+proof+systems)
> 核心思路：提出一种比零知识集合更弱的隐私模型，允许模拟器学习集合大小。
> 局限与区别：定义限于静态集合且在选择性安全（非自适应）模型下分析，无法直接扩展至动态更新。

[56] Papamanthou et al. Optimal verification of operations on dynamic sets. **CRYPTO 2011** [Google Scholar](https://scholar.google.com/scholar?q=Optimal+verification+of+operations+on+dynamic+sets)
> 核心思路：提出基于特征多项式的集合代数操作（交集、并集、差集）的高效验证协议。
> 局限与区别：证明构造需暴露大量非查询信息（如每个元素来自哪个集合），无隐私保护。

[29] Ghosh et al. Verifiable zero-knowledge order queries and updates. **SCN 2016** [Google Scholar](https://scholar.google.com/scholar?q=Verifiable+zero-knowledge+order+queries+and+updates+for+fully+dynamic+lists+and+trees)
> 核心思路：提出零知识认证数据结构的一般框架，并给出列表和树的构造。
> 局限与区别：未支持集合代数操作，且非成员证明效率低于本文的方案。

### 核心技术与方案

本文构造分为两个层次：零知识动态通用累加器和零知识认证集合集合。第一层是基础，第二层利用它构建集合代数查询的完整隐私保护。

**零知识动态通用累加器** 基于 Nguyen 的双线性累加器 [53]，核心创新在于所有运算引入盲化随机数。在 Setup 中，选取随机值 $r \in \mathbb{Z}_p^*$，计算积累值 $\mathsf{acc} = g^{r \cdot \mathsf{Ch}_\mathcal{X}(s)}$，其中 $\mathsf{Ch}_\mathcal{X}(s) = \prod_{x \in \mathcal{X}}(x + s)$ 是特征多项式，$s$ 是秘密陷门。这保证了积累值在群上均匀分布，即使攻击者已知集合大小，也无法区分不同集合。成员证明采用标准除法方式：若 $x \in \mathcal{X}$，证明者计算 $\mathsf{w} = \mathsf{acc}^{\frac{1}{s+x}} = g^{r \cdot \mathsf{Ch}_{\mathcal{X}\setminus\{x\}}(s)}$，验证者检查 $e(\mathsf{acc}, g) = e(\mathsf{w}, g^x \cdot g^s)$。

非成员证明是零知识的关键障碍。现有方法 [2,19] 揭示多项式除法的余数，这直接暴露了盲化因子 $r$。本文转而采用集合不相交性测试技术 [56]：为了证明 $x \notin \mathcal{X}$，证明者证明 $\mathcal{X} \cap \{x\} = \emptyset$。利用扩展欧几里得算法，计算多项式 $q_1[z], q_2[z]$ 使得 $q_1[z]\mathsf{Ch}_\mathcal{X}[z] + q_2[z]\mathsf{Ch}_{\{x\}}[z] = 1$。然后引入查询级随机数 $\gamma$，构造盲化多项式 $q_1'[z] = q_1[z] + \gamma \cdot \mathsf{Ch}_{\{x\}}[z]$ 和 $q_2'[z] = q_2[z] - \gamma \cdot \mathsf{Ch}_\mathcal{X}[z]$，并计算证明 $\mathsf{w} = (W_1 = g^{q_1'(s) r^{-1}}, W_2 = g^{q_2'(s)})$。验证者检查 $e(W_1, \mathsf{acc}) \cdot e(W_2, g^x \cdot g^s) = e(g, g)$。由于 $\gamma$ 每次查询随机选取，即使攻击者获取多个非成员证明，也无法关联任何信息。

每次更新操作（插入或删除）后，重新选取随机数 $r'$ 并计算新积累值 $\mathsf{acc}' = \mathsf{acc}^{\frac{r'}{s+x}}$（删除）或 $\mathsf{acc}' = \mathsf{acc}^{(s+x) r'}$（插入）。这种重随机化保证更新前后的积累值分布完全独立，攻击者无法从积累值变化推断更新类型。系统复杂度为：Setup $O(N)$，成员证明生成 $O(N \log N)$，非成员证明生成 $O(N \log^2 N \log \log N)$，验证 $O(1)$，更新 $O(1)$。

**零知识认证集合集合** 将上述累加器作为每个集合的摘要，并使用积累树 [57] 维护所有集合的根摘要以支持动态集合集合。对于集合交集查询，证明者返回交集结果 answer，并同时证明子集条件（answer 是每个查询集合的子集）和完备性条件（所有查询集合减去 answer 后的交集为空）。完备性证明需要证明多项式组的最大公因式为 1，即存在满足线性关系的一组多项式 $q_j[z]$。本文通过对 $q_j[z]$ 进行类似非成员证明的随机化处理来隐藏多项式信息。并集查询的核心在于不泄露元素来源：证明者通过构造并集树，利用双线性映射逐层验证多集合并的正确性，同时避免暴露各个元素属于哪些原始集合。差集查询利用交集和子集关系的等价转换 $\mathcal{X}_{i_1} \setminus \text{answer} = \mathcal{X}_{i_1} \cap \mathcal{X}_{i_2}$，并使用 NIZKPoK 协议来确保盲化后的累积值在指数上相等，而不暴露具体的集合。

安全性：完美完备性通过算法直接验证。可靠性和零知识均证明。可靠性规约到 $q$-SBDH 假设：若攻击者伪造证明，则可以构造出一个对 $(z, e(g,g)^{1/(z+s)})$ 的破译实例。本文在图 4 中给出了各操作的渐进复杂度，与无隐私方案 [56] 相比，查询和验证复杂度相同，仅更新复杂度略高（从 $O(1)$ 变为 $O(L)$，其中 $L$ 是两次更新间被查询的集合数量），这是实现零知识的必要代价。

### 核心公式与流程

**[成员证明生成与验证]**
$$
\mathsf{w} = \mathsf{acc}^{\frac{1}{s+x}} = g^{r \cdot \mathsf{Ch}_{\mathcal{X}\setminus\{x\}}(s)}, \quad e(\mathsf{acc}, g) \stackrel{?}{=} e(\mathsf{w}, g^x \cdot g^s)
$$
> 作用：对于 $x \in \mathcal{X}$，证明者根据积累值计算成员证明，验证者通过双线性配对检查除法的正确性。

**[非成员证明生成与验证]**
$$
\begin{aligned}
&q_1[z]\mathsf{Ch}_\mathcal{X}[z] + q_2[z]\mathsf{Ch}_{\{x\}}[z] = 1,\\
&q_1'[z] = q_1[z] + \gamma \cdot \mathsf{Ch}_{\{x\}}[z], \quad q_2'[z] = q_2[z] - \gamma \cdot \mathsf{Ch}_\mathcal{X}[z],\\
&W_1 = g^{q_1'(s) r^{-1}}, \quad W_2 = g^{q_2'(s)},\\
&e(W_1, \mathsf{acc}) \cdot e(W_2, g^x \cdot g^s) \stackrel{?}{=} e(g, g)
\end{aligned}
$$
> 作用：对于 $x \notin \mathcal{X}$，利用集合不相交性测试并引入查询级随机数 $\gamma$ 进行盲化，实现零知识非成员证明。

**[更新操作（插入）]**
$$
\mathsf{acc}' = \mathsf{acc}^{(s+x) r'}, \quad r \gets r \cdot r'
$$
> 作用：插入元素后，使用新随机数 $r'$ 重随机化积累值，使得更新前后积累值的分布相互独立，阻断攻击者从积累值变化推断更新内容的能力。

**[交集完备性证明（部分）]**
$$
\sum_{j \in [i_1,i_k]} q_j[z] P_j[z] = 1,\quad \text{其中 } P_j[z] = \mathsf{Ch}_{\mathcal{X}_j \setminus \text{answer}}[z]
$$
> 作用：将交集完备性条件转化为多项式互质性的代数形式，通过随机化线性组合的系数来同时实现正确性和零知识。

### 实验结果

论文未提供实际实验环境或运行时间数值，但给出了与无隐私基准方案 [53]（扩展版 [2]）在加密操作数量上的理论比较表（图 3）。以集合大小 $n$ 为例，Setup 阶段两者均为 $n$ 次标量乘法（MUL），Witness (Member) 阶段均为 $n$ MUL + $(n-1)$ 次加法（ADD），初始零知识代价为零。更新阶段（Update）从 1 MUL 增至 2 MUL，仅增加一次乘法。非成员验证（Verify (Non-Member)）从 2 (MUL+ADD+PAIR) 降至 1 (MUL+ADD+ADD_T) + 2 PAIR，验证中增加了一次目标群加法但减少了一次配对，实际性能取决于具体实现。非成员 Witness Update 代价最大，从 2 MUL+1 ADD 增至 $(n+1)$ MUL + $(n-1)$ ADD，因为隐私方案中断了证明的连续更新能力，需重新计算。论文指出零知识的额外开销主要来自常数级别的重随机化操作，适合安全参数 $\lambda$ 和集合规模 $n$ 在实际范围内（如 $n \leq 2^{20}$）的应用场景。

### 局限性与开放问题

非成员证明的 Witness Update 效率低下，需从零重新计算，依赖应用场景下非成员查询频率较低。安全性基于 $q$-SBDH 假设，该假设中参数 $q$ 取决于集合最大容量，理论上属于参数化假设而非常量假设。差集查询在标准模型中需要交互（Sigma 协议），非交互化需额外依赖随机预言机模型或公共参考串模型。未来方向包括基于常量假设（如 RSA）的零知识累加器构造、无需重计算的成员证明高效更新机制、以及完全不依赖交互的非交互差集协议构造。

### 强关联论文

[53] Nguyen. Accumulators from bilinear pairings and applications. **CT-RSA 2005** [Google Scholar](https://scholar.google.com/scholar?q=Accumulators+from+bilinear+pairings+and+applications)

[2] Au et al. Dynamic universal accumulators for DDH groups. **CT-RSA 2009** [Google Scholar](https://scholar.google.com/scholar?q=Dynamic+universal+accumulators+for+DDH+groups+and+their+application+to+attribute-based+anonymous+credential+systems)

[23] Derler et al. Revisiting cryptographic accumulators, additional properties and relations to other primitives. **CT-RSA 2015** [Google Scholar](https://scholar.google.com/scholar?q=Revisiting+cryptographic+accumulators+additional+properties+and+relations+to+other+primitives)

[52] Naor and Ziv. Primary-secondary-resolver membership proof systems. **TCC 2015** [Google Scholar](https://scholar.google.com/scholar?q=Primary-secondary-resolver+membership+proof+systems)

[56] Papamanthou et al. Optimal verification of operations on dynamic sets. **CRYPTO 2011** [Google Scholar](https://scholar.google.com/scholar?q=Optimal+verification+of+operations+on+dynamic+sets)

[29] Ghosh et al. Verifiable zero-knowledge order queries and updates. **SCN 2016** [Google Scholar](https://scholar.google.com/scholar?q=Verifiable+zero-knowledge+order+queries+and+updates+for+fully+dynamic+lists+and+trees)

[4] Benaloh and de Mare. One-way accumulators: a decentralized alternative to digital signatures. **EUROCRYPT 1993** [Google Scholar](https://scholar.google.com/scholar?q=One-way+accumulators+a+decentralized+alternative+to+digital+signatures)

[11] Camenisch and Lysyanskaya. Dynamic accumulators and application to efficient revocation of anonymous credentials. **CRYPTO 2002** [Google Scholar](https://scholar.google.com/scholar?q=Dynamic+accumulators+and+application+to+efficient+revocation+of+anonymous+credentials)

[19] Damgård and Triandopoulos. Supporting non-membership proofs with bilinear-map accumulators. **ePrint 2008** [Google Scholar](https://scholar.google.com/scholar?q=Supporting+non-membership+proofs+with+bilinear-map+accumulators)

[57] Papamanthou et al. Authenticated hash tables based on cryptographic accumulators. **Algorithmica 2015** [Google Scholar](https://scholar.google.com/scholar?q=Authenticated+hash+tables+based+on+cryptographic+accumulators)


## 关键词

+ 零知识证明
+ 密码学累加器
+ 集合代数
+ 隐私保护
+ 动态验证