---
title: "Reckle Trees: Updatable Merkle Batch Proofs with Applications"
doi: 10.1145/3658644.3670354
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2024
modified: 2025-04-23 15:49:29
created: 2025-04-08 21:59:42
---
## Reckle Trees: Updatable Merkle Batch Proofs with Applications

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3658644.3670354)

## 作者

+ [Charalampos Papamanthou](Charalampos%20Papamanthou.md)
+ Shravan Srinivasan
+ Nicolas Gailly
+ Ismael Hishon-Rezaizadeh
+ Andrus Salumets
+ Stjepan Golemac

## 笔记

### 背景与动机
Merkle树作为最经典的向量承诺方案，其核心优势在于支持对数时间复杂度的快速更新：当任何叶子节点改变时，相应的单个证明可在对数时间内完成更新。然而，当需要同时证明多个叶子节点时，其构造的批证明大小与批大小线性相关，无法实现简洁性。另一方面，现有的利用递归SNARK或内积论证构造的批证明方案虽然克服了简洁性问题，但它们普遍不支持批证明的更新：一旦内存中任何一个叶子节点发生变化，整个批证明需要从零开始重新计算，造成高昂的开销。例如，Hyperproofs的批证明更新需要数分钟时间。区块链场景中的动态数据流（如新区块产生）对批证明的持续更新提出了现实需求，但目前缺少一种既能保持批证明的简洁性又能支持高效更新的方案。本文提出的Reckle树填补了这一空白，它首次将可更新的简洁批证明集成到向量承诺中，并在此基础上扩展为Reckle+树以支持可更新的Map/Reduce验证计算。

### 相关工作

[10] Deng and Du. **zkTree: A Zero-Knowledge Recursion Tree with ZKP Membership Proofs**. *Cryptology ePrint Archive 2023* [Google Scholar](https://scholar.google.com/scholar?q=zkTree:+A+Zero-Knowledge+Recursion+Tree+with+ZKP+Membership+Proofs)
> 核心思路：构建一棵“证明之树”，先为每个叶子生成独立SNARK证明，再用递归SNARK逐层聚合，得到简洁批证明。
> 局限与区别：该批证明不可更新；若任一叶子变化，所有证明必须从零开始重算。本文在递归电路中嵌入规范哈希计算，使得批证明数据结构的更新仅需对数时间。

[22] Srinivasan et al. **Hyperproofs: Aggregating and Maintaining Proofs in Vector Commitments**. *USENIX Security 2022* [Google Scholar](https://scholar.google.com/scholar?q=Hyperproofs:+Aggregating+and+Maintaining+Proofs+in+Vector+Commitments)
> 核心思路：利用内积论证实现简洁批证明，支持对向量子集的高效聚合。
> 局限与区别：证明更新需要重新计算整个批，且验证时间约为27秒，远高于本文方案（约18毫秒）。此外，Hyperproofs的公共参数大小与向量长度线性相关。

[19] Ozdemir et al. **Scaling Verifiable Computation Using Efficient Set Accumulators**. *USENIX Security 2020* [Google Scholar](https://scholar.google.com/scholar?q=Scaling+Verifiable+Computation+Using+Efficient+Set+Accumulators)
> 核心思路：将Merkle路径证明嵌入Groth16电路，用单一SNARK验证多个叶子。本文将其作为Merkle SNARKs对比基线。
> 局限与区别：构造本质上是非递归的，不提供更新能力；且电路约束数与批大小线性相关，导致更新开销随批大小增长。

[23] Polygon Zero Team. **Plonky2: Fast recursive arguments with PLONK and FRI**. *Technical Report 2022* [Google Scholar](https://scholar.google.com/scholar?q=Plonky2:+Fast+recursive+arguments+with+PLONK+and+FRI)
> 核心思路：设计基于PLONK和FRI的递归SNARK系统，证明大小约112 KiB，支持高效递归验证。
> 局限与区别：本文将其作为底层递归引擎使用，但论文本身不关心批证明的更新特性。

[14] Groth. **On the Size of Pairing-Based Non-interactive Arguments**. *EUROCRYPT 2016* [Google Scholar](https://scholar.google.com/scholar?q=On+the+Size+of+Pairing-Based+Non-interactive+Arguments)
> 核心思路：提出恒大小（如192字节的）配对基础SNARK，验证仅需常数次配对。
> 局限与区别：本文用作Merkle SNARKs基线的证明系统，但其证明开销与批大小和树深度线性相关。

### 核心技术与方案

本文的整体框架建立在递归SNARK和规范哈希两项技术之上。规范哈希是确定性地从Merkle树叶子子集计算标识符的算法：对批索引集合$I$，其根节点的规范哈希$d(\mathrm{root}, I)$递归定义：若节点为叶子且其索引在$I$中，则哈希值为该叶子的索引与值的拼接；否则为0。对内部节点，若左右孩子的规范哈希均非零，则父节点哈希为$\mathsf{H}(d_L||d_R)$；否则父节点哈希等于非零子树的哈希。这一哈希计算过程完全独立于SNARK电路，避免了在电路中编码代数操作。

递归电路$\mathcal{B}$以验证密钥$\mathsf{vk}$、Merkle根哈希$\mathsf{C}$和规范哈希$d$为公共输入，以左右子节点的Merkle哈希$(\mathsf{C}_L,\mathsf{C}_R)$、规范哈希$(d_L,d_R)$和对应递归证明$(\pi_L,\pi_R)$为私有见证。其计算分为五步：验证$\mathsf{C}=\mathsf{H}(\mathsf{C}_L||\mathsf{C}_R)$；根据$d_L,d_R$是否均为零确定根节点$d$的计算方式；对非零子节点调用Verify验证其递归证明（或确认其为合法叶子节点）。这一设计使得整个证明过程中不需要重新执行Merkle路径验证——所有路径哈希已在递归过程中被校验。

批证明的生成采用自底向上的递归过程。首先根据索引集合$I$确定被影响的节点集合$T'_I$（从各叶子到根的路径的并集）。然后从层$1$到层$\ell$，对$T'_I$中每个节点$v$，以其左孩子$L$和右孩子$R$的Merkle哈希、规范哈希和递归证明为输入，调用Prove生成节点$v$的递归证明$\pi_v$。根节点$\pi_{\mathrm{root}}$即为最终批证明。由于每层计算可以完全并行化，整个过程在$\ell$个并行步骤内完成，与批大小无关。

为实现可更新性，Reckle树维护一个批证明数据结构$\Lambda_I$，其中以树形结构存储$T'_I$中所有节点的三种元组：Merkle哈希、规范哈希和递归证明。当任意叶子$j$的值发生改变时，$\Lambda_I$中所有从$j$到根的节点都被标记为受影响。更新算法逐层向上重新计算这些节点的Merkle哈希、必要时重新计算规范哈希，并重新生成递归证明。由于影响路径长度仅为$\ell$，更新总时间为$O(\ell)$即对数复杂度，与批大小完全解耦。

安全性证明依赖于哈希函数的抗碰撞性和底层SNARK的知识可靠性。证明采用反证法：假设存在敌手输出两个不一致的批证明（同一位置有不同值），则提取器可以同时抽取出两个路径上的叶子值。由于两个批证明共享相同的Merkle根哈希，抗碰撞性保证提取出的叶子值必然相同，与假设矛盾。这保证了方案满足向量承诺的可靠性定义。

Reckle+树将上述框架扩展到Map/Reduce计算。递归电路$\mathcal{M}$在验证规范哈希的同时，维护一个可交换的聚合状态：Map函数作用于叶子（判定其是否属于子集并将结果编码为状态），Reduce函数沿树自底向上合并左右子节点的Map结果。以BLS密钥聚合为例，Map将参与签名的叶子密钥映射为$(1, g^{\mathrm{sk}})$、非参与叶子映射为$(0, 1_\mathbb{G})$，Reduce则累加计数并逐点乘聚合公钥。由于聚合操作是结合律的，整个计算在递归框架下自然成立。

复杂度方面：单次批证明更新时间为$O(\ell)$（$\ell$为树高），与批大小$|I|$无关；批证明大小恒定（约112 KiB）；验证时间由规范哈希计算（约14.29 ms）和SNARK验证（约3.91 ms）两部分组成。与先行工作相比，本文在更新性能（10-15倍提升）和验证性能（4.78至1485倍提升）上均占优，聚合时间在高并行度场景下与Hyperproofs相当。

### 核心公式与流程

**[规范哈希定义]**
$$
d(v,I) := 
\begin{cases}
\mathrm{index}(v) \,||\, \mathrm{value}(v) & \text{if } v \text{ is a leaf and } v \in I \\
0 & \text{if } v \text{ is a leaf and } v \notin I \\
\mathsf{H}(d_L || d_R) & \text{if } v \text{ is internal and } d_L, d_R \neq 0 \\
d_L + d_R & \text{otherwise}
\end{cases}
$$
> 作用：用于确定性地从叶子子集计算唯一的标识哈希，避免在SNARK电路中编码代数操作。

**[递归电路 $\mathcal{B}$（图2）]**
```
Public input: (vk, C, d)
Witness: (C_L, d_L, π_L), (C_R, d_R, π_R)

(1) 检查 C = H(C_L || C_R)
(2) 若 d_R·d_L ≠ 0，则检查 d = H(d_L || d_R)
    否则，检查 d = d_L + d_R
(3) 若 d_L ≠ 0，检查 Verify(vk, (vk, C_L, d_L), π_L) 或 (C_L = d_L)
(4) 若 d_R ≠ 0，检查 Verify(vk, (vk, C_R, d_R), π_R) 或 (C_R = d_R)
(5) 返回 true
```
> 作用：递归验证一对子节点和其Merkle/规范哈希的一致性，以及子证明的正确性，从而将批证明的验证沿着树结构传播到根节点。

**[BLS聚合电路 $\mathcal{A}_i$（图8）]**
```
Public input: (C, apk, cnt)
Witness: (C_L, apk_L, cnt_L, π_L), (C_R, apk_R, cnt_R, π_R)

(1) 检查 C = H(C_L || C_R)
(2) 检查 apk = apk_L · apk_R
(3) 检查 cnt = cnt_L + cnt_R
(4) 若 apk_L ≠ 1_G，检查 Verify(vk_i, (C_L, apk_L, cnt_L), π_L)
    否则，检查 cnt_L = 0
(5) 若 apk_R ≠ 1_G，检查 Verify(vk_i, (C_R, apk_R, cnt_R), π_R)
    否则，检查 cnt_R = 0
(6) 返回 true
```
> 作用：在递归验证Merkle结构正确性的同时，累加叶子层Map得到的BLS公钥（群乘法）和签名者计数（加法），最终输出聚合公钥和人数。

### 实验结果

实验在 AWS c7i.8xlarge 实例（32 vCPU, 64 GiB内存）上进行，使用 Rust 实现的 Plonky2 作为底层递归SNARK。向量规模设为 $n = 2^{27}$，批大小 $|I|$ 从 $2^2$ 到 $2^{12}$ 变化。对比基线包括：Merkle SNARKs（基于Groth16）和 Hyperproofs（基于内积论证）。

聚合时间（图11a）：本文的分布式实现（192机器集群）在批大小为 $2^{12}$ 时仅需123秒，远低于 Merkle SNARKs 的4.44分钟和 Hyperproofs 的3.15分钟。顺序实现虽然较慢，但3.15-270倍于基线的并行加速比表明天然可扩展性。

更新时间（图11c）：单叶子更新的对数复杂度导致 $2^{12}$ 批大小时仅需16.61秒，比 Hyperproofs（3.15分钟）和 Merkle SNARKs（4.44分钟）分别快11倍和15倍。这一提升来源于批证明数据结构 $\Lambda_I$ 支持局部重算。

验证时间与证明大小：验证时间由规范哈希（14.29 ms）和 SNARK验证（3.91 ms）两部分组成，总计约18.2 ms，比 Merkle SNARKs（87 ms）快4.78倍，比 Hyperproofs（27.03 s）快1485倍。批证明恒定为112 KiB。

应用方面：动态摘要翻译中，本文在 $2^{22}$ 叶子规模时仍可完成证明生成，而基线（单体电路）在 $2^{8}$ 叶子时即耗尽内存。BLS聚合实验中，本文在 $2^{21}$ 叶子规模下依然可行，基线因内存限制无法运行；更新方面，Reckle+树约为4.49秒，基线为54.21秒，提速12倍。

### 局限性与开放问题

本文方案依赖底层递归SNARK的具体实现效率（Plonky2），若未来出现更快的折叠方案（如Nova），可以自然替换，但重新实现可能带来工程开销。当前$q$-ary树的实现（Merkle Patricia Trie）仅给出电路设计（图5），未完成实验评估。对于非平衡树（如Ethereum状态树），如何在保持对数更新复杂度的同时处理动态拓扑，仍有待研究。此外，Map/Reduce框架要求结合律的归约操作，对于非交换操作（如矩阵乘法），需要设计更复杂的聚合策略。

### 强关联论文

[10] Sai Deng and Bo Du. **zkTree: A Zero-Knowledge Recursion Tree with ZKP Membership Proofs**. *Cryptology ePrint Archive 2023* [Google Scholar](https://scholar.google.com/scholar?q=zkTree:+A+Zero-Knowledge+Recursion+Tree+with+ZKP+Membership+Proofs)

[14] Jens Groth. **On the Size of Pairing-Based Non-interactive Arguments**. *EUROCRYPT 2016* [Google Scholar](https://scholar.google.com/scholar?q=On+the+Size+of+Pairing-Based+Non-interactive+Arguments)

[19] Alex Ozdemir et al. **Scaling Verifiable Computation Using Efficient Set Accumulators**. *USENIX Security 2020* [Google Scholar](https://scholar.google.com/scholar?q=Scaling+Verifiable+Computation+Using+Efficient+Set+Accumulators)

[22] Shravan Srinivasan et al. **Hyperproofs: Aggregating and Maintaining Proofs in Vector Commitments**. *USENIX Security 2022* [Google Scholar](https://scholar.google.com/scholar?q=Hyperproofs:+Aggregating+and+Maintaining+Proofs+in+Vector+Commitments)

[23] Polygon Zero Team. **Plonky2: Fast recursive arguments with PLONK and FRI**. *Technical Report 2022* [Google Scholar](https://scholar.google.com/scholar?q=Plonky2:+Fast+recursive+arguments+with+PLONK+and+FRI)


## 关键词

+ 向量承诺
+ 默克尔树
+ 批量证明
+ 递归论证
+ 可更新证明
+ BLS聚合

We present and experimentally evaluate two applications of Reckle+ trees, dynamic digest translation and updatable BLS aggregation. In dynamic digest translation we are maintaining a proof of equivalence between Merkle digests computed with different hash functions, e.g., one with a SNARK-friendly Poseidon and the other with a SNARK-unfriendly Keccak. In updatable BLS aggregation we maintain a proof for the correct aggregation of a _t_-aggregate BLS key, derived from a _t_-subset of a Merkle-committed set of individual BLS keys. Our evaluation using Plonky2 shows that Reckle trees and Reckle+ trees have small memory footprint, significantly outperform previous approaches in terms of updates (10× to 15×) and verification (4.78× to 1485×) time, enable applications that were not possible before due to huge costs involved (Reckle trees are up to 200× faster), and have similar aggregation performance with previous implementations of batch proofs.