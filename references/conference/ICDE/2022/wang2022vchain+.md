---
title: "vChain+: Optimizing verifiable blockchain boolean range queries"
doi: 10.1109/icde53745.2022.00190
标题简称:
论文类型: conference
会议简称: ICDE
发表年份: 2022
modified: 2025-04-11 11:13:43
---
## vChain+ : Optimizing verifiable blockchain boolean range queries

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/9835165/)

## 作者

+ Haixin Wang 
+ [Cheng Xu](Cheng%20Xu.md)
+ Ce Zhang 
+ [Jianliang Xu](Jianliang%20Xu.md)
+ Zhe Peng 
+ Jian Pei 

## 笔记

### 背景与动机
区块链因其不可篡改和防篡改特性，被视为一种有前景的安全数据库解决方案，但用户若以轻节点身份查询数据，需依赖不可信的全节点，面临查询结果完整性无法保证的挑战。Xu 等人提出的 vChain 框架 [4] 率先支持了区块链数据库上的可验证布尔范围查询，通过在每个区块头中嵌入基于密码学集合累加器的 AttDigest，实现了对不匹配区块的高效批量跳过。然而，vChain 存在三个关键瓶颈：其跨区块索引在最坏情况下退化为线性扫描，因为当连续多个区块因不同原因不匹配查询条件时，索引无法聚合跳过；其密码学累加器的公钥大小取决于属性宇宙大小，若采用 256 位哈希编码，公钥大小将达 $2^{512}$，不得不引入不可信的第三方预言机来动态生成公钥；此外，vChain 仅支持单调布尔函数和整数/定点数范围查询，表达能力受限。本文旨在通过全新的认证数据结构设计，同时解决查询效率、公钥管理和查询表达能力这三个问题。

### 相关工作

[4] Xu 等. vChain: Enabling Verifiable Boolean Range Queries over Blockchain Databases. **ACM SIGMOD 2019** [Google Scholar](https://scholar.google.com/scholar?q=vChain+Enabling+Verifiable+Boolean+Range+Queries+over+Blockchain+Databases)
> 核心思路：在区块头中嵌入基于集合累加器的 AttDigest，利用跨区块跳跃表聚合对象，通过不匹配证明批量跳过不相关区块。
> 局限与区别：最坏情况下跨区块索引失效，退化为线性扫描；公钥大小随属性宇宙指数增长，需引入不可信第三方；仅支持单调布尔函数。

[9] Zhang 等. An Expressive (Zero-Knowledge) Set Accumulator. **IEEE EuroS&P 2017** [Google Scholar](https://scholar.google.com/scholar?q=An+Expressive+%28Zero-Knowledge%29+Set+Accumulator)
> 核心思路：提出支持增量更新和嵌套集合运算的密码学累加器，任意集合运算的证明大小为常数，证明生成复杂度 $O(N_1 \cdot N_2)$。
> 局限与区别：公钥大小 $O(|U|^2)$ 在 $|U|$ 较大时不可接受；本文通过对象注册索引将 $|U|$ 限制为固定小整数。

[6] Merkle. A Certified Digital Signature. **Proc. CRYPTO 1990** [Google Scholar](https://scholar.google.com/scholar?q=A+Certified+Digital+Signature)
> 核心思路：提出默克尔哈希树（MHT），以对数大小的证明认证一组数据对象的完整性和存在性。
> 局限与区别：MHT 本身不支持集合运算；本文将其作为对象注册索引的基础，用于认证对象 ID 与原始数据的映射关系。

[7] Li 等. Dynamic Authenticated Index Structures for Outsourced Databases. **ACM SIGMOD 2006** [Google Scholar](https://scholar.google.com/scholar?q=Dynamic+Authenticated+Index+Structures+for+Outsourced+Databases)
> 核心思路：将 B+ 树与 MHT 结合（Merkle B+-tree），支持范围查询的认证。
> 局限与区别：仅针对单维数值属性；本文将其扩展为滑动窗口 B+ 树，并结合集合累加器支持跨区块查询。

[8] Yang 等. Authenticated Indexing for Outsourced Spatial Databases. **The VLDB Journal 2009** [Google Scholar](https://scholar.google.com/scholar?q=Authenticated+Indexing+for+Outsourced+Spatial+Databases)
> 核心思路：提出 Merkle R-tree 认证空间数据。
> 局限与区别：不适用于区块链场景中的时间窗口分割和累积更新。

[28] Parno 等. Pinocchio: Nearly Practical Verifiable Computation. **IEEE S&P 2013** [Google Scholar](https://scholar.google.com/scholar?q=Pinocchio+Nearly+Practical+Verifiable+Computation)
> 核心思路：通过布尔或算术电路生成证明，验证任意计算完整性。
> 局限与区别：证明生成时间极高，不适合区块链高频查询场景；本文采用特定认证数据结构而非通用电路。

[33] Zhang 等. IntegriDB: Verifiable SQL for Outsourced Databases. **ACM CCS 2015** [Google Scholar](https://scholar.google.com/scholar?q=IntegriDB+Verifiable+SQL+for+Outsourced+Databases)
> 核心思路：使用集合累加器认证复杂 SQL 查询（包含嵌套集合运算）。
> 局限与区别：累加器无法增量更新；本文使用的累加器支持增量更新，专为滑动窗口动态维护设计。

[30] Chen 等. Authenticated Online Data Integration Services. **ACM SIGMOD 2015** [Google Scholar](https://scholar.google.com/scholar?q=Authenticated+Online+Data+Integration+Services)
> 核心思路：设计认证数据结构支持数据整合中的连接查询完整验证。
> 局限与区别：不涉及区块链场景和滑动窗口。

[27] Peng 等. FalconDB: Blockchain-based Collaborative Database. **ACM SIGMOD 2020** [Google Scholar](https://scholar.google.com/scholar?q=FalconDB+Blockchain-based+Collaborative+Database)
> 核心思路：将结果验证委托给智能支付合约，通过激励机制保证 SP 诚实。
> 局限与区别：依赖智能合约执行，增加链上开销；本文仅依赖密码学验证。

[25] Zhang 等. Gem^2-Tree: A Gas-Efficient Structure for Authenticated Range Queries in Blockchain. **IEEE ICDE 2019** [Google Scholar](https://scholar.google.com/scholar?q=Gem%5E2-Tree+A+Gas-Efficient+Structure+for+Authenticated+Range+Queries+in+Blockchain)
> 核心思路：面向混合存储区块链设计 gas 高效的 Merkle 树变体。
> 局限与区别：主要优化链上 gas 消耗，而非查询处理效率和公钥管理。

### 核心技术与方案

整体框架：vChain+ 延续 vChain 的三方模型（用户为轻节点、服务提供者 SP 为全节点、矿工为全节点），但设计了全新的认证数据结构。核心思想是在每个区块中为最近 $k$ 个区块内的数据对象构建一个滑动窗口累加器索引，该索引的根哈希嵌入区块头。矿工维护时，以滑动窗口方式移除过时对象并插入新对象，通过密码学累加器的增量更新操作高效更新。SP 处理查询时，将时间窗口 $[t_s, t_e]$ 划分为多个长度为 $k$ 的子查询，每个子查询利用对应区块的滑动窗口累加器索引高效搜索，最终合并结果并生成可验证的验证对象。用户通过区块头中的根哈希验证搜索完性和集合运算正确性。

**对象注册索引**解决公钥大小问题：由于使用的集合累加器公钥大小为 $O(|U|^2)$，而 $U$ 为数据对象的宇宙。vChain+ 不直接对数据对象执行累加，而是为每个数据对象分配一个最大值为 $MaxID$ 的小整数 ID，将 ID 集合放入累加器。同时，在各区块中嵌入一个完全平衡的默克尔哈希树作为对象注册索引，记录最近 $2k-1$ 个区块内数据对象与 ID 的映射。当查询得到结果 ID 后，用户通过此索引的默克尔证明验证数据对象的真实性和完整性。这样，累加器的宇宙大小被限定为 $MaxID$（实验中设为 $2^{12}$），公钥大小仅为 $2^{24}$。

**滑动窗口累加器（SWA）**设计：SWA 索引的构建支持多种基础树结构。对于关键词查询，采用滑动窗口累加器 Trie（SWA-Trie）；对于数值范围查询，采用滑动窗口累加器 B+ 树（SWA-B+-Tree）。每个节点包含：关键字段（或数值范围）、该节点覆盖的对象 ID 集合 $S_n$、该集合的累加值 $acc_n = acc(S_n)$、以及哈希值 $h_n$。非叶子节点还包含子节点哈希拼接 $childHash_n$。根节点的累加值用于认证整个窗口的集合。例如，SWA-Trie 的叶子节点定义为 $h_n = H(H(w_n) || acc_n)$，非叶子根节点定义为 $h_n = H(H(w_n) || childHash_n || acc(S_n))$。算法 1（矿工维护）描述如何通过增量更新：移除 $k$ 个区块前对象的 ID，插入新区块对象的 ID，仅更新受影响节点路径上的 $S_n$、$acc_n$ 和 $h_n$，其中 $acc_n$ 通过调用 ACC.Update 增量计算。

**查询处理流程（算法 2）**：SP 处理布尔关键词查询 $Q = \langle [t_s, t_e], \Upsilon \rangle$ 时，首先将 Q 划分为多个长度为 $k$ 的子查询。对于每个子查询 $q = \langle [t_{s'}, t_{e'}], \Upsilon \rangle$：
1. 在区块 $b_{e'}$ 的 SWA-Trie 中搜索每个关键词 $w \in \Upsilon$：自顶向下遍历，对于不匹配 $w$ 的节点，将 $w_n$ 和 $acc_n$（或 $childHash_n$）加入默克尔证明 $\pi_{trie}$；对于匹配的叶子节点，将其 ID 集合 $S_n$ 加入结果集 $R_w$ 并添加 $w_n$ 和 $acc_n$ 到 $\pi_{trie}$。
2. 将布尔表达式 $\Upsilon$ 映射为集合运算（$\land \to \cap$, $\lor \to \cup$, $\lnot \to \setminus$），对所得中间结果 ID 集调用 ACC.Prove 生成集合运算证明 $\pi_{\Upsilon}$ 和结果 ID 集 $R_{\Upsilon}$。
3. 在对象注册索引中查找 $R_{\Upsilon}$ 对应的数据对象，生成默克尔证明 $\pi_{obj}$。
最终验证对象包含 $\langle \pi_{trie}, R_{\Upsilon}, \pi_{\Upsilon}, \pi_{obj} \rangle$。用户验证时，重建 SWA 根哈希和对象注册根哈希并与区块头对比，再调用 ACC.Verify 认证集合运算。

**优化策略**：
- 多滑动窗口：矿工构建多个不同 $k$ 值（如 2, 4, 8）的 SWA 索引，SP 对剩余子查询选择最小的满足覆盖的 $k$ 值，减少结果重叠。
- 查询计划优化：利用交换律、结合律、分配律等 10 条集合运算重写规则，通过 e-graph 等式饱和技术生成最小代价的集合运算执行顺序，代价模型为 $|A| \times |B|$ 的累加和。
- 空集剪枝：遍历集合运算 DAG，当发现某中间集合为空时，跳过其后续运算。

**安全性证明（定理 1）**：在哈希函数和集合累加器均具有抗碰撞性、集合运算证明安全、区块链完整性和可用性得到保证的前提下，本文算法满足定义 5 的不可伪造性。证明核心是反证法：若存在冒充的数据对象，则对应对象注册索引发生哈希碰撞；若结果缺失，则 SP 必须伪造默克尔证明（导致哈希碰撞）或伪造集合运算证明（违反累加器安全性）。

**复杂度**：矿工构造 ADS 的时间随窗口大小 $k$ 和每个区块对象数线性增长，但对每个对象仅更新一条根到叶路径。SP 查询和证明生成的计算代价取决于 SWA 的搜索规模（树高 $O(\log N)$），但集合运算 ACC.Prove 的复杂度 $O(N_1 N_2)$ 是最主要的开销，通过优化可大幅降低。用户验证的代价为默克尔树验证的 $O(\log N)$ 加上常数大小的 ACC.Verify。VO 大小主要取决于默克尔证明路径长度和集合运算证明个数，实测在数百 KB 量级。

### 核心公式与流程

**[SWA-Trie 叶子节点定义]**
$$h_n = H(H(w_n) || acc_n)$$
> 作用：定义 SWA-Trie 叶子节点的哈希值计算方式，其中 $w_n$ 为关键词段，$acc_n = acc(S_n)$ 为节点覆盖 ID 集合的累加值。

**[SWA-Trie 非叶子根节点定义]**
$$h_n = H(H(w_n) || childHash_n || acc(S_n))$$
> 作用：定义根节点的哈希值，包含关键词段哈希、子节点哈希拼接 $childHash_n$ 和根节点覆盖的所有 ID 集合的累加值 $acc(S_n)$。

**[算法 1：SWA-Trie 维护（矿工）]**
```
1 Function SWATrieMaintenance(b_{i+1}, b_{i-k+1})
2   T_{i+1} ← T_i
3   获取 ObjRegIdx_{i-k+1} 和 ObjRegIdx_{i+1}
4   for each o in b_{i-k+1} do T_{i+1}.Update(o, ID, false) // 删除
5   for each o in b_{i+1} do T_{i+1}.Update(o, ID, true)  // 插入
6   将 T_{i+1} 写入 b_{i+1}
7 Function Update(o, ID, is_insert)
8   new_nodes ← 插入或删除导致更新的节点路径
9   l ← new_nodes[0]; r ← new_nodes[-1]
10  if ID ∈ S_l then acc_Δ ← acc(∅) else acc_Δ ← acc({ID})
11  if is_insert then S_l, S_r 添加 ID else S_l, S_r 移除 ID; acc_Δ ← -acc_Δ
12  acc_l ← ACC.Update(acc_l, acc_Δ, pk); acc_r ← ACC.Update(acc_r, acc_Δ, pk)
13  更新 l 的哈希; 更新非叶子节点哈希; 更新 r 的哈希
```
> 作用：描述矿工如何以滑动窗口方式增量维护 SWA 索引。通过删除最旧区块对象的 ID 并插入新区块对象的 ID，只更新受影响路径上节点的对象集合、累加值和哈希。

**[算法 2：布尔查询处理（SP）]**
```
1 Function BooleanQuery(Q)
2   R ← ∅; qs ← DivideQuery(Q)
3   for each q in qs do
4     获取区块 b_{e'} 对应 t_{e'}
5     for each w in Υ do
6       ⟨R_w, π_w⟩ ← QuerySWATrie(w, b_{e'}.root)
7       合并 π_w 到 π_{trie}; 添加 R_w 到 R_{trie}
8     ⟨R_Υ, π_Υ⟩ ← ACC.Prove on R_{trie} based on Υ
9     ⟨R_obj, π_obj⟩ ← ObjRegIdx_{e'}.lookup(R_Υ)
10    R ← R ∪ R_obj; 添加 ⟨π_{trie}, R_Υ, π_Υ, π_obj⟩ 到 VO
11  return ⟨R, VO⟩
```
> 作用：描述 SP 处理布尔查询时的整体流程：划分时间窗口、搜索 SWA 索引、执行集合运算、通过对象注册索引获取数据对象，并打包验证对象。

**[算法 3：关键词搜索（SP）]**
```
1 Function QuerySWATrie(root, w)
2   创建队列 queue; queue.enqueue(root)
3   while queue not empty do
4     n ← queue.dequeue()
5     if w_n 不匹配 w then 加入相应字段到 π
6     elif n.isLeaf() then R ← R ∪ S_n; 加入 ⟨w_n, acc_n⟩ 到 π
7     else 加入 w_n（及 acc_n 若为根）到 π; 子节点入队
8   return ⟨R, π⟩
```
> 作用：描述在 SWA-Trie 中搜索关键词 w 的过程，收集匹配对象的 ID 集合，并构建默克尔证明，证明所有不包含 w 的子树与查询无关。

**[集合运算证明生成代价模型]**
$$\text{Cost}(ACC.Prove(A, B, opt, pk)) = |A| \times |B|$$
> 作用：用于查询计划优化中的代价估算，指导 SP 选择实际运算顺序，使群运算（配对计算）量最小。例如 $(A \cap B) \cap C$ 的代价为 $|A||B| + |A \cap B||C|$，而 $A \cap (B \cap C)$ 为 $|B||C| + |A||B \cap C|$。

### 实验结果

实验在配备双路 Intel Xeon E5-2620 v3 2.4GHz CPU、CentOS 8 的服务器上进行，限制用户使用 4 线程，矿工和 SP 使用所有核心。采用 Foursquare（4SQ）和 Ethereum（ETH）两个数据集，vChain+ 用 Rust 实现并基于 Arkworks 库（BN254 曲线配对）。对比基线为 vChain 的两种累加器构造（vChain-acc1 和 vChain-acc2）。

在矿工端，vChain+ 的 ADS 构建时间（每区块 0.11-0.25 秒）介于 vChain-acc1（0.26-0.39 秒）和 vChain-acc2（0.04 秒）之间，但 ADS 大小（451.5-1209.1 KB）远大于 vChain（28.1-126.1 KB），这是为了支持更丰富的查询。在最关键的空查询（所有区块不匹配）性能上，vChain+ 的时间窗口跨度从 100 到 8100 个区块时，CPU 时间始终低于 0.05 秒，而 vChain-acc1 和 acc2 在最差情况下（例如 8100 区块）分别需要约 10 秒和 1 秒。对于 AND 连接布尔查询，vChain+ 比 vChain-acc2 快高达 913 倍，比 acc1 快高达 1098 倍。在 VO 大小方面，vChain+ 通常比 vChain 大（例如 623 KB vs 68 KB），但考虑全球中位数移动网络速度 29.06 Mbps 时，总传输延迟仍优于 vChain（0.221 秒 vs 1.61 秒，提升 7.3 倍）。优化评估显示，空集剪枝和查询计划优化贡献最大，多滑动窗口提升相对较小。随着范围选择度从 10% 升至 50%，CPU 时间和 VO 大小线性增长；布尔函数大小从 1 增至 9 时，代价也随操作数平方级增长。

### 局限性与开放问题
本文主要评估了空查询和时间窗口全覆盖查询，对部分命中场景（窗口内部分区块匹配）的性能未充分讨论。密码学累加器的集合运算 $O(N_1 N_2)$ 复杂度在中间结果集较大时仍是瓶颈，优化可能难以应对极端选择度。对象注册索引需要矿工维护 $2k-1$ 个区块的映射表，内存开销随窗口大小线性增长。此外，vChain+ 未考虑隐私保护——SP 和矿工可获取查询全部中间结果和最终结果。未来工作可拓展至聚合查询、连接查询，以及利用硬件安全或零知识证明实现隐私保护的查询认证。

### 强关联论文

[4] Xu 等. vChain: Enabling Verifiable Boolean Range Queries over Blockchain Databases. **ACM SIGMOD 2019** [Google Scholar](https://scholar.google.com/scholar?q=vChain+Enabling+Verifiable+Boolean+Range+Queries+over+Blockchain+Databases)

[9] Zhang 等. An Expressive (Zero-Knowledge) Set Accumulator. **IEEE EuroS&P 2017** [Google Scholar](https://scholar.google.com/scholar?q=An+Expressive+%28Zero-Knowledge%29+Set+Accumulator)

[6] Merkle. A Certified Digital Signature. **Proc. CRYPTO 1990** [Google Scholar](https://scholar.google.com/scholar?q=A+Certified+Digital+Signature)

[7] Li 等. Dynamic Authenticated Index Structures for Outsourced Databases. **ACM SIGMOD 2006** [Google Scholar](https://scholar.google.com/scholar?q=Dynamic+Authenticated+Index+Structures+for+Outsourced+Databases)

[8] Yang 等. Authenticated Indexing for Outsourced Spatial Databases. **The VLDB Journal 2009** [Google Scholar](https://scholar.google.com/scholar?q=Authenticated+Indexing+for+Outsourced+Spatial+Databases)

[2] Wood. Ethereum: A Secure Decentralised Generalised Transaction Ledger. **Online 2014** [Google Scholar](https://scholar.google.com/scholar?q=Ethereum+A+Secure+Decentralised+Generalised+Transaction+Ledger)

[5] Yang 等. Participatory Cultural Mapping Based on Collective Behavior Data in Location-Based Social Networks. **ACM TIST 2016** [Google Scholar](https://scholar.google.com/scholar?q=Participatory+Cultural+Mapping+Based+on+Collective+Behavior+Data+in+Location-Based+Social+Networks)

[10] Joshi 等. Denali: A Goal-Directed Superoptimizer. **ACM SIGPLAN Notices 2002** [Google Scholar](https://scholar.google.com/scholar?q=Denali+A+Goal-Directed+Superoptimizer)

[11] Willsey 等. Egg: Fast and Extensible Equality Saturation. **Proc. ACM Program. Lang. 2021** [Google Scholar](https://scholar.google.com/scholar?q=Egg+Fast+and+Extensible+Equality+Saturation)

[12] Speedtest Global Index. Global Median Speeds October 2021. **Online 2021** [Google Scholar](https://scholar.google.com/scholar?q=Global+Median+Speeds+October+2021)


## 关键词

+ 可验证区块链查询
+ 布尔范围查询
+ 滑动窗口累加器索引
+ 公钥管理
+ 查询完整性
+ 区块链数据库