---
title: "Taking authenticated range queries to arbitrary dimensions"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2014
---

## Taking authenticated range queries to arbitrary dimensions

## 发表信息

+ [原文链接]()

## 作者

+ [Dimitrios Papadopoulos](Dimitrios%20Papadopoulos.md) 
+ Stavros Papadopoulos 
+ [Nikos Triandopoulos](Nikos%20Triandopoulos.md)
## 笔记

### 背景与动机
数据库外包允许数据所有者将数据库维护工作委托给强大的第三方服务器，以降低自身基础设施成本。然而，服务器可能不可信，会篡改查询结果，因此必须提供证明结果完整性的认证机制 [16]。多维范围查询是关系型数据库和科学数据库中的基本操作，其认证问题至关重要。现有方案存在两个关键瓶颈：Martel等人的方案 [18] 和 Chen 等人的方案 [9] 虽具有理论保证，但其复杂度随查询维度 d 呈指数增长。此外，所有现有方法为了支持查询属性集合的任意子集，需要构建指数级于属性总数 m 的认证结构数量。因此，迫切需要一种在设置成本、存储空间和查询效率上均线性依赖于维度数 m 和 d，并能任意组合属性进行查询的方案。

### 相关工作
[9] Chen H, Ma X, Hsu W, Li N, Wang Q. Access control friendly query verification for outsourced data publishing. *ESORICS 2008* [Google Scholar](https://scholar.google.com/scholar?q=Access+control+friendly+query+verification+for+outsourced+data+publishing)
> 核心思路：基于属性域划分和访问控制，将认证问题与访问控制结合。
> 局限与区别：该方案的复杂度随维度 d 呈指数增长，无法有效扩展至高维查询。

[14] Goodrich M T, Tamassia R, Triandopoulos N. Super-efficient verification of dynamic outsourced databases. *CT-RSA 2008* [Google Scholar](https://scholar.google.com/scholar?q=Super-efficient+verification+of+dynamic+outsourced+databases)
> 核心思路：针对 1维和 2维范围查询，设计了基于 Merkle 树的密码学扩展结构。
> 局限与区别：该方案仅限于处理低维（1 或 2维）查询，无法直接推广至任意高维场景。

[17] Li F, Hadjieleftheriou M, Kollios G, Reyzin L. Dynamic authenticated index structures for outsourced databases. *SIGMOD 2006* [Google Scholar](https://scholar.google.com/scholar?q=Dynamic+authenticated+index+structures+for+outsourced+databases)
> 核心思路：提出一种名为 B^+-tree 的变体，通过嵌入哈希值来处理 1维范围查询。
> 局限与区别：该方案主要面向 1维查询，若直接扩展到多维，需构建指数级数量的索引结构。

[18] Martel C, Nuckolls G, Devanbu P, Gertz M, Kwong A, Stubblebine S G. A general model for authenticated data structures. *Algorithmica 2004* [Google Scholar](https://scholar.google.com/scholar?q=A+general+model+for+authenticated+data+structures)
> 核心思路：提出了 Merkle 树的推广形式，能够处理多维范围查询。
> 局限与区别：该方案的复杂度随查询维度 d 呈指数增长，限制了其在维度较高时的实际应用。

[22] Papamanthou C, Tamassia R, Triandopoulos N. Authenticated hash tables. *CCS 2008* [Google Scholar](https://scholar.google.com/scholar?q=Authenticated+hash+tables)
> 核心思路：基于双线性对构造了累加树，实现常量级证明大小和验证时间。
> 局限与区别：本文将其作为底层的集合成员证明结构，通过自身的框架实现多维查询支持。

[24] Papamanthou C, Tamassia R, Triandopoulos N. Optimal verification of operations on dynamic sets. *CRYPTO 2011* [Google Scholar](https://scholar.google.com/scholar?q=Optimal+verification+of+operations+on+dynamic+sets)
> 核心思路：提出了对集合操作（如交集）进行认证的最优方案。
> 局限与区别：本文直接利用其交集认证协议作为组合步骤，并指出其复杂度与输入集合大小相关，是本文方案改进的对象。

[28] Yang Y, Papadopoulos S, Papadias D, Kollios G. Authenticated indexing for outsourced spatial databases. *VLDB J. 2009* [Google Scholar](https://scholar.google.com/scholar?q=Authenticated+indexing+for+outsourced+spatial+databases)
> 核心思路：通过将 R*-tree 转化为 Merkle R*-tree 来支持多维查询认证。
> 局限与区别：该方案依赖启发式索引结构 R*-tree，在实际操作中当维度超过一定数量（如 8）时性能显著下降。

### 核心技术与方案
本文的核心思想是将多维范围查询认证问题分解为若干个一维查询认证问题，并通过集合操作协议在客户端高效地组合这些一维证明。方案整体框架分为两步：第一步，服务器对每个查询维度 $a_i$，计算满足该维度范围条件的哈希值集合 $R_i$，并生成相应的认证证明 $\pi_{R_i}$；第二步，服务器通过集合交集认证协议，将来自各个维度的部分结果 $R_i$ 进行组合，以证明查询的最终结果 $R = \bigcap_i R_i$ 的完整性。

为了实现这一框架，作者提出了基本方案和更新高效方案两个具体实例。

**基本方案**: 每个属性 $a_i$ 对应一个排序列表，其中包含所有元组的哈希值（按元组在属性 $a_i$ 上的值排序）。关键创新在于将一维查询结果 $R_i$ 表达为两个前缀集的差集：$R_i = P_{i,k_i} \setminus P_{i,k_i'}$。其中 $P_{i,j}$ 是包含排序列表中前 $j$ 个哈希值的集合。这样，每个属性只需维护 $n$ 个前缀集及其对应的双线性累加值，而无需为每一个可能的 $R_i$ 预先计算单独的证据。通过结合新颖的集合差子协议和已有的集合交集认证协议 [24]，服务器可为查询结果 $R$ 生成一个简洁的证明，其大小与 $d$ 线性相关，而与 $\sum_i |R_i|$ 无关。然而，该方案在执行元组更新时，需要重新计算大量前缀集的证明，更新成本高达 $O(|T|)$。

**更新高效方案**: 为解决基本方案更新成本高昂的问题，作者进一步优化结构。在每个属性的排序列表中，将哈希值划分为 $b$ 个桶，其中 $b = \sqrt{n}$。在桶级别上维护前缀集 $\mathcal{P}_{i,j}$，同时在每个桶内部维护更细粒度的前缀集 $P_{i,j,l}$。对于一维查询结果 $R_i$，它通常覆盖了若干个完整的桶以及至多两个部分覆盖的桶。因此，$R_i$ 可以表示为三个两两不相交集合的并集：一个来自部分覆盖的起始桶内部的集合差、一个来自完整桶的桶级集合差、以及一个来自部分覆盖的结束桶的前缀集。认证过程相应变为：首先分别证明这三个子集的正确性，然后通过一个新的集合并子协议将其合并为整个 $R_i$ 的证明，最后通过交集协议组合得到最终结果 $R$。

安全性：方案的安全性基于 $q$-强双线性 Diffie-Hellman（$q$-SBDH）假设以及底层集合成员认证方案的安全性。证明通过归约进行：假设存在攻击者能以不可忽略的概率伪造一个错误结果的证据，则可以利用该攻击者构造一个算法来破坏 $q$-SBDH 假设或破解底层的集合成员认证方案。

复杂度：对于基本方案和更新高效方案（使用 Merkle 树作为底层 SMA），设置复杂度为 $O(|T|\log n)$，证明大小为 $O(d \log n)$，证明构造时间为 $\tilde{O}(\sum_{i=1}^d |R_i|) + O(d \log n)$，验证时间为 $\tilde{O}(|R|) + O(d \log n)$。基本方案的更新复杂度为 $O(|T|)$，而更新高效方案则降低至 $O(m \sqrt{n})$。

### 核心公式与流程

**[集合差子协议]**
$$e(acc(X_2), \pi_{\setminus}) = e(acc(X_1), g)$$
> 作用：用于验证 $\pi_{\setminus}$ 是集合 $X_1 \setminus X_2$ 的累加值（要求 $X_1 \supset X_2$）。若 $X_1$ 是 $X_2$ 的真超集，待验证的 $\pi_{\setminus}$ 满足此等式当且仅当它是 $X_1 \setminus X_2$ 的累加值。

**[集合并子协议]**
$$e(\pi_{X_1}, \pi_{X_2}) = e(\pi_{\cup}, g) \quad \text{and} \quad e(\pi_{\cup}, \pi_{X_3}) = e(\pi_X, g)$$
> 作用：用于证明 $X$ 是三个两两不相交集合 $X_1, X_2, X_3$ 的并集。首先通过第一步验证 $\pi_{\cup}$ 是 $X_1 \cup X_2$ 的累加值，再通过第二步验证 $X$ 是 $(X_1 \cup X_2) \cup X_3$ 的累加值。

**[交集认证协议核心条件]**
$$e(acc(I), W_i) = e(acc(X_i), g) \quad \text{and} \quad \prod_i e(W_i, F_i) = e(g, g)$$
> 第一个条件用于证明 $I$ 是 $X_i$ 的子集（通过子集见证 $W_i$），第二个条件通过 Bézout 系数 $F_i$ 证明 $(X_1 \setminus I) \cap (X_2 \setminus I) = \emptyset$，综合两者证明 $I = \bigcap_i X_i$。

### 实验结果
实验在 2.5GHz Intel Core i5 CPU 的 64 位机器上进行，使用 C++ 实现，底层采用 DCLXVI 库（256 位 BN 椭圆曲线，128 位安全级别）、Flint 库（模算术）和 Crypto++ 库（SHA-256 哈希）。测试了四种方案：基本 + Merkle 树、基本 + 累加树、更新高效 + Merkle 树、更新高效 + 累加树。当 $d=32$，$n=10^6$，$m=64$，$|R|=1000$ 时，客户端的验证时间基本在 20ms 到 3.36 秒之间。当结果大小 $|R|$ 固定时，各方案验证时间随 $d$ 线性增长。Merkle 树方案在客户端性能上通常优于累加树方案，因为哈希操作比双线性对运算快得多。例如，对于 Basic-Mer 方案，当 $d=2, 4, 8, 16, 32$ 时，证明大小分别为 4.5, 9.1, 18.1, 36.3, 72.5 KB。服务器端计算是主要瓶颈，其时间受 $\sum_i |R_i|$ 以及不交见证 $F_i$ 的生成成本（依赖于 Extended Euclidean 算法）主导，对于 $|R_i|=10,000$ 时，服务器端时间可达 25 分钟。对于 $n=10^5$，$m=64$ 的场景，更新高效方案的更新成本比基本方案快两个数量级。

### 局限性与开放问题
尽管本文的方案在渐进复杂度上取得了显著改进，但服务器端的证明构建成本依然高昂，尤其是在处理大规模部分结果和计算不交见证 $F_i$ 时，时间可达数十分钟，这可能成为系统的实际瓶颈。此外，实验主要在合成数据集上进行，无法模拟真实数据分布和查询负载的全部特性。更新高效方案虽然改善了更新性能，但仍需在设置成本和客户端验证时间上做出权衡。

### 强关联论文

[4] Beckmann N, Kriegel H-P, Schneider R, Seeger B. The R*-tree: An efficient and robust access method for points and rectangles. *SIGMOD 1990*

[5] Boneh D, Boyen X. Short signatures without random oracles and the SDH assumption in bilinear groups. *J. Cryptology 2008*

[18] Martel C, Nuckolls G, Devanbu P, Gertz M, Kwong A, Stubblebine S G. A general model for authenticated data structures. *Algorithmica 2004*

[19] Merkle R C. A certified digital signature. *CRYPTO 1989*

[22] Papamanthou C, Tamassia R, Triandopoulos N. Authenticated hash tables. *CCS 2008*

[24] Papamanthou C, Tamassia R, Triandopoulos N. Optimal verification of operations on dynamic sets. *CRYPTO 2011*

[26] Tamassia R. Authenticated data structures. *ESA 2003*

[28] Yang Y, Papadopoulos S, Papadias D, Kollios G. Authenticated indexing for outsourced spatial databases. *VLDB J. 2009*


## 精准翻译

以下是中文翻译：

我们研究外包数据库上认证多维范围查询 (authenticated multi-dimensional range queries) 的问题，其中数据所有者将其数据库外包给不可信服务器，由服务器维护数据库并向客户端回答查询。以往的方案要么在查询维度数量上呈指数级扩展，要么依赖于没有可证明界限的启发式数据结构。最重要的是，现有工作需要与数据库属性呈指数关系的大量结构来支持数据库中每个可能维度组合上的查询。

在本文中，我们提出了首个具有以下特性的方案：(i) 与维度数量呈线性扩展关系，以及 (ii) 支持任意维度集合上的查询，且设置成本和存储开销与属性数量呈线性关系。我们通过精心融合新颖的和现有的集合操作子协议 (set-operation sub-protocols) 来实现这一目标。我们基于 q-强双线性 Diffie-Hellman 假设 (q-Strong Bilinear Diffie-Hellman assumption) 证明了解决方案的安全性，并通过实验验证了其可行性。

## 关键词

+ 认证多维范围查询
+ 外包数据库
+ 线性扩展性
+ 集合操作
+ q-强双线性DH假设