---
title: "Zero-knowledge elementary databases with more expressive queries"
标题简称:
论文类型: conference
会议简称: PKC
发表年份: 2019
modified: 2025-04-11 14:26:20
---

## Zero-knowledge elementary databases with more expressive queries

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-030-17253-4_9)

## 作者

+ [Benoît Libert](Benoît%20Libert.md) 
+ [Khoa Nguyen](Khoa%20Nguyen.md)
+ Benjamin Hong Meng Tan 
+ [Huaxiong Wang](Huaxiong%20Wang.md)
## 笔记

### 背景与动机
零知识基本数据库（ZK-EDB）允许证明者承诺一个键值对集合，同时隐藏其大小，并能非交互地证明成员关系或非成员关系。该概念由 Micali, Rabin 和 Kilian 于 2003 年引入 [21]，其核心构造依赖于水银承诺（mercurial commitment）与 Merkle 树的结合 [5,6]。然而，现有方案的表达能力有限，仅支持简单的“键x在数据库中且对应值为y”或“键x不在数据库中”这类陈述。实际问题中，用户往往需要更复杂的查询，例如范围查询（“找出键在区间$[a_x, b_x]$内的所有记录”）、值上的成员关系查询（“数据库中是否存在值为y的记录”），甚至是k近邻查询。直接扩展现有方案来处理这些查询会泄露数据库大小，因为证明者必须逐一证明区间内每个键的非成员关系。本文旨在填补这一空白：证明水银承诺实际上能够支持更具表达性的查询，在不泄露数据库大小的前提下，实现多项式规模的证明。

### 相关工作

[2] Catalano, D., Dodis, Y., Visconti, I. Mercurial commitments: minimal assumptions and efficient constructions. **TCC 2006** [Google Scholar](https://scholar.google.com/scholar?q=Mercurial+commitments%3A+minimal+assumptions+and+efficient+constructions)
> 核心思路：简化并统一定义了（陷门）水银承诺，并给出其从单向函数在共享随机串模型下的一般构造。
> 局限与区别：虽然该方案为后续ZK-EDB提供了基础，但其本身并未研究如何支持范围查询等更复杂的陈述。本文的核心贡献在于在此类水银承诺之上实现了表达性查询，而非改进承诺方案本身。

[5] Chase, M., Healy, A., Lysyanskaya, A., Malkin, T., Reyzin, L. Mercurial commitments with applications to zero-knowledge sets. **EUROCRYPT 2005** [Google Scholar](https://scholar.google.com/scholar?q=Mercurial+commitments+with+applications+to+zero-knowledge+sets)
> 核心思路：首次提出水银承诺的概念，并通过将其与Merkle树结合，构建了通用的ZK-EDB方案。
> 局限与区别：该方案（其[6]的期刊版）仅支持简单的成员/非成员查询。本文在其框架上扩展，解决了证明范围查询等复杂查询的难题，并识别并利用了水银承诺中一个被忽略的“软解释”性质。

[21] Micali, S., Rabin, M.O., Kilian, J. Zero-knowledge sets. **44th FOCS 2003** [Google Scholar](https://scholar.google.com/scholar?q=Zero-knowledge+sets)
> 核心思路：基于离散对数假设开创性地构造了零知识集合（ZKS），这是ZK-EDB的特例。
> 局限与区别：该方案的构造思路（使用Merkle树和水银承诺）是本文工作的基础。但其表达能力局限于成员关系查询，而本文通过精巧地利用子集覆盖和双向Merkle树，极大地扩展了查询类型。

[25] Naor, D., Naor, M., Lotspiech, J. Revocation and tracing schemes for stateless receivers. **CRYPTO 2001** [Google Scholar](https://scholar.google.com/scholar?q=Revocation+and+tracing+schemes+for+stateless+receivers)
> 核心思路：提出了用于广播加密的子集覆盖框架，其中“完全子树法”可以高效地覆盖一个集合的补集。
> 局限与区别：本文创造性地将子集覆盖技术应用于ZK-EDB的范围查询证明中，用以证明区间内不属于数据库的键集。这是本文实现超多项式大小区间查询的关键技术，是思想上的重大迁移。

[22] Micciancio, D., Peikert, C. Trapdoors for lattices: simpler, tighter, faster, smaller. **EUROCRYPT 2012** [Google Scholar](https://scholar.google.com/scholar?q=Trapdoors+for+lattices%3A+simpler%2C+tighter%2C+faster%2C+smaller)
> 核心思路：提供了格上更简单、高效的陷门生成和原像采样算法。
> 局限与区别：该工作为本文构造基于格的水银承诺提供了核心工具（TrapGen, SampleD）。本文的核心贡献在于利用这些工具设计了一个新的直接构造，避免了从Σ协议通用构造带来的多次尝试问题。

[16] Kawachi, A., Tanaka, K., Xagawa, K. Concurrently secure identification schemes based on the worst-case hardness of lattice problems. **ASIACRYPT 2008** [Google Scholar](https://scholar.google.com/scholar?q=Concurrently+secure+identification+schemes+based+on+the+worst-case+hardness+of+lattice+problems)
> 核心思路：提出了一个基于格的陷门承诺方案（KTX）。
> 局限与区别：本文的格基水银承诺方案在构造上受到KTX启发，通过精巧地设计两种承诺模式（硬/软）对应的矩阵生成方式，将KTX方案嵌入并扩展为水银承诺。

[12] Ghosh, E., Ohrimenko, O., Tamassia, R. Efficient verifiable range and closest point queries in zero-knowledge. **PoPETs 2016** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+verifiable+range+and+closest+point+queries+in+zero-knowledge)
> 核心思路：在三方模型（可信提交者、不可信服务器、验证者）下，构造了高效的范围查询方案，同样使用了子集覆盖技术。
> 局限与区别：本文的工作场景是更具挑战性的两方模型（证明者即数据库拥有者，不可信），因此不能假设可信的提交者。本文的方案在安全性要求上更高，导致了效率上的差距。本文明确指出这一区别以突出其贡献。

[28] Ostrovsky, R., Rackoff, C., Smith, A. Efficient consistency proofs for generalized queries on a committed database. **ICALP 2004** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+consistency+proofs+for+generalized+queries+on+a+committed+database)
> 核心思路：针对已提交的数据库，协议能处理正交的多维范围查询并保证零知识。
> 局限与区别：该方案没有隐藏数据库的大小，不适合对隐私要求“大小隐藏”的场景。本文明确目标是与[5,6,21]一样的“大小隐藏”ZK-EDB。

### 核心技术与方案
本文提出的零知识表达性基本数据库（ZK-EEDB）方案，其核心框架依然建立在Chase等人[5,6]的水银承诺+Merkle树结构之上。整体的技术路线可分为两大部分：实现键空间上的范围查询和使用“反向数据库”实现值空间上的范围查询。

**键空间上的范围查询**：对于区间$[a, b]$，证明的目标是证明集合$\mathcal{R} = [a,b] \cap [\mathsf{D}]$中的键属于数据库，而区间内的其他键不在数据库中。方案的关键创新在于：
1.  **使用Steiner树（$\mathbb{HOpenST}$）优化成员证明**：对于集合$\mathcal{R}$，其成员证明并非单个路径的简单组合，而是通过计算覆盖所有$\mathcal{R}$中节点的最小子树（Steiner树）来生成。这避免了证明中大量冗余的硬打开，使得成员证明部分的复杂度仅为$O(|\mathcal{R}|\cdot \ell)$，其中$\ell$是Merkle树的高度。
2.  **使用子集覆盖法（Subset Cover）优化非成员证明**：这是解决超多项式大小区间查询难题的核心。对于$\mathcal{R}$的补集$\mathcal{P} = [a,b] \setminus \mathcal{R}$，方案并未对每个键单独生成非成员证明，而是利用Naor等人[25]的完全子树法找到$\mathcal{P}$的一组“规范覆盖”（Canonical Covering），记为$\mathcal{P}_{[a,b]}$。这组节点数量是$O(|\mathcal{R}| \cdot \log((b-a)/|\mathcal{R}|))$，它是一个与区间总长度$(b-a)$无关的多项式量。证明者只需对$\mathcal{P}_{[a,b]}$中的每个节点解释（Explain）其为软承诺，证明这些节点的子树下的所有键都不可能属于数据库。这背后依赖一个关键的新引入算法**Explain**和对应的验证算法**EVerify**，它们允许证明者公开软承诺的随机数，从而向验证者证明该承诺是“软”的，无法被硬打开。为了保证零知识性，还引入了**FakeExplain**算法，模拟器可以用它来解释伪造的承诺为软承诺。软解释等价性（SE Equivocation）要求伪造承诺的软解释与真实软承诺在统计上不可区分。

**值空间上的范围查询**：为了实现值上的查询，方案维护了第二个Merkle树，即“反向数据库”$\mathsf{D}^{-1}$。$\mathsf{D}^{-1}$的键是原始数据库$\mathsf{D}$的值$y$，而$\mathsf{D}^{-1}(y)$是一个指向零知识集合（ZK set）$\mathsf{D}^{-1}_y$的根承诺。$\mathsf{D}^{-1}_y$包含所有使得$\mathsf{D}(x)=y$的键$x$。通过这两棵树，要证明“不存在记录$(*, y)$”就转化为证明在$\mathsf{D}^{-1}$的第二个树上，键$y$对应的叶子是一个软承诺，且该叶子的软打开路径指向根。安全性依赖于两棵树的**一致性**：任何证明记录$(x, y)$在$\mathsf{D}$中的证明，必须同时包含在第一个树中$x$的硬认证路径和在第二个树中$y$到某个明确承诺了$\mathsf{D}^{-1}_y$的路径。这保证了作弊证明者无法在两棵树中声明冲突的记录。

**安全性证明**：
*   **可靠性（Soundness）**：基于水银承诺的**水银绑定（Mercurial-binding）**性质。定理1的证明概要指出，如果敌手能产生两个矛盾的查询结果，那么必然存在一个记录$(x, y)$在一个查询中被声称属于数据库，在另一个查询中被声称不属于或属于不同的值。无论哪种情况，都会导致在两个证明中，同一节点（可能是叶节点或中间节点）出现一个硬打开和一个软打开（或另一个不同的硬打开），这直接违背了水银绑定性质。
*   **零知识（Zero-Knowledge）**：依赖于水银承诺的**四个等价性（Equivocation）性质**（HH, HS, SS, SE）。定理2的证明概要描述了模拟器（SInit, SCom, SProveRQ$^{\mathsf{D}}$），它使用陷门生成伪造的承诺（MFake）。对于每个查询，模拟器通过查询数据库预言机获得真实答案，然后利用HEquivocate, SEquivocate和FakeExplain算法，将伪造的承诺打开或解释为与真实答案一致的硬/软路径。由于这四个等价性性质保证了伪造的承诺及其打开的联合分布与真实的承诺及其打开在统计上不可区分，因此模拟生成的证明与真实证明不可区分。

**渐进复杂度**：对于范围查询$[a_x, b_x] \times [a_y, b_y]$，证明大小随$O(|\mathcal{L}|\ell)$增长，其中$\mathcal{L}$是查询结果（记录集合），$\ell$是键和值的比特长度，与区间长度无关。

### 核心公式与流程

**SIS（Short Integer Solution）问题定义**
$$
\mathsf{SIS}_{n,m,q,\beta}: \text{Given } \mathbf{A} \in \mathbb{Z}_q^{n \times m}, \text{ find } \mathbf{v} \in \Lambda^{\perp}(\mathbf{A}) \text{ s.t. } \| \mathbf{v} \| \leq \beta
$$
> 作用：这是本文格基水银承诺方案的安全假设基础。

**水银承诺的硬模式（Hard Mode）构造**
$$
\mathbf{B} = [\mathbf{A}_1 \mid \mathbf{B}_1] \in \mathbb{Z}_q^{n \times (m+w)}, \quad \mathbf{B}_1 = \mathbf{A}_1 \cdot \mathbf{R}
$$
$$
\mathbf{c} = \mathbf{A}_0 \cdot \boldsymbol{\mu} + \mathbf{B} \cdot \mathbf{r}
$$
> 作用：硬承诺由两部分组成：一个字符串$\mathbf{c}$（承诺值）和一个矩阵$\mathbf{B}_1$（模式指示器）。$\mathbf{R}$是随机矩阵，$\mathbf{r}$是随机向量。$\mathbf{B}_1$的特定形式（$\mathbf{A}_1\mathbf{R}$）是硬承诺的标志，它支持后续的硬打开验证。

**水银承诺的软模式（Soft Mode）构造**
$$
\mathbf{B} = [\mathbf{A}_1 \mid \mathbf{B}_1] \in \mathbb{Z}_q^{n \times (m+w)}, \quad \mathbf{B}_1 = \mathbf{G} - \mathbf{A}_1 \cdot \mathbf{R}
$$
$$
\mathbf{c} = \mathbf{B} \cdot \mathbf{r}
$$
> 作用：软承诺中，$\mathbf{B}_1$的构造方式不同，它使得矩阵$\mathbf{B}$拥有一个陷门（trapdoor），允许证明者将承诺软打开到任意消息。注意$\mathbf{c}$的计算也不包含消息$\mu$。

### 实验结果
本文并未提供任何实验结果。这是一篇纯粹的理论密码学论文，其贡献在于提出新的协议和构造，并给出安全性证明和理论上的性能分析（渐进复杂度）。因此，无法提供关于运行时间、通信开销的具体数值或与baseline在实验环境下的性能对比。所有声称的效率优势均基于理论分析：证明大小仅与答案集大小成线性关系，而与查询区间大小无关，这使其能够处理超多项式区间的查询。

### 局限性与开放问题
本文的构造虽然功能强大，但效率仍然较低，尤其是基于格的实例化，其证明大小可能达到$O(\lambda^3)$，这在实际应用中会非常大。作者指出，可以通过将方案转移到环格（ring setting）来降低复杂度，但并未给出具体的实现和测试。此外，当查询涉及记录的二维范围（即同时约束键和值）时，性能会退化到多项式级，无法处理值区间为超多项式的情况。如何设计更高效的方案，特别是减少证明尺寸和计算开销，使其更适合实际部署，是一个重要的开放问题。另一个方向是如何支持更复杂的查询，如交集查询或连接查询。

### 强关联论文

[2] Catalano, D., Dodis, Y., Visconti, I. Mercurial commitments: minimal assumptions and efficient constructions. **TCC 2006** [Google Scholar](https://scholar.google.com/scholar?q=Mercurial+commitments%3A+minimal+assumptions+and+efficient+constructions)

[4] Catalano, D., Fiore, D., Messina, M. Zero-knowledge sets with short proofs. **EUROCRYPT 2008** [Google Scholar](https://scholar.google.com/scholar?q=Zero-knowledge+sets+with+short+proofs)

[5] Chase, M., Healy, A., Lysyanskaya, A., Malkin, T., Reyzin, L. Mercurial commitments with applications to zero-knowledge sets. **EUROCRYPT 2005** [Google Scholar](https://scholar.google.com/scholar?q=Mercurial+commitments+with+applications+to+zero-knowledge+sets)

[16] Kawachi, A., Tanaka, K., Xagawa, K. Concurrently secure identification schemes based on the worst-case hardness of lattice problems. **ASIACRYPT 2008** [Google Scholar](https://scholar.google.com/scholar?q=Concurrently+secure+identification+schemes+based+on+the+worst-case+hardness+of+lattice+problems)

[21] Micali, S., Rabin, M.O., Kilian, J. Zero-knowledge sets. **44th FOCS 2003** [Google Scholar](https://scholar.google.com/scholar?q=Zero-knowledge+sets)

[22] Micciancio, D., Peikert, C. Trapdoors for lattices: simpler, tighter, faster, smaller. **EUROCRYPT 2012** [Google Scholar](https://scholar.google.com/scholar?q=Trapdoors+for+lattices%3A+simpler%2C+tighter%2C+faster%2C+smaller)

[25] Naor, D., Naor, M., Lotspiech, J. Revocation and tracing schemes for stateless receivers. **CRYPTO 2001** [Google Scholar](https://scholar.google.com/scholar?q=Revocation+and+tracing+schemes+for+stateless+receivers)


## 关键词

+ 零知识基本数据库（ZK-EDB）
+ 水银承诺
+ 范围查询
+ 格假设
+ 量子安全构造
+ 隐私保护数据库