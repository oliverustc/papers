---
title: "Merkle Mountain Ranges are Optimal: On witness update frequency for cryptographic accumulators"
标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 2025
created: 2025-06-10 05:30:06
modified: 2025-06-10 05:32:28
---

## Merkle Mountain Ranges are Optimal: On witness update frequency for cryptographic accumulators

## 发表信息

+ [原文链接](https://eprint.iacr.org/2025/234)

## 作者

+ [[Joseph Bonneau]]
+ [Jessica Chen](Jessica%20Chen.md)
+ [Miranda Christ](Miranda%20Christ.md)
+ [Ioanna Karantaidou](Ioanna%20Karantaidou.md)
## 笔记

### 背景与动机

在密码学实践中，经常需要维护一个不断增长的集合的密码学承诺，例如已注册公钥的用户集合、互联网上所有已颁发的X.509证书，或区块链中的所有交易。这类场景要求承诺本身是简洁的（最多与集合大小的对数成正比），并且支持为集合中的每个元素生成简洁的包含证明（或称见证）。经典密码累加器（如Merkle树 [34]、RSA累加器 [11]、双线性累加器 [38]）能够满足这些基本要求。然而，当新元素不断加入集合时，这些累加器有一个严重的实际瓶颈：除了可忽略的概率外，每次添加新元素都需要更新所有已有元素的见证。对于依赖低见证更新频率的应用（如分布式PKI [42]、注册加密 [22]），这造成了显著的通信与计算开销。为此，多个独立工作反复发明了相同的数据结构——Merkle Mountain Range (MMR) [47, 42, 22]，它通过将元素组织成一系列大小递增的Merkle树，以树合并的方式控制见证更新，最终达到总共 Θ(n log n) 次见证更新。尽管MMR在实践中表现优异，但从未有理论证明其最优性。本文填补了这一空白，首次给出了仅追加累加器中见证更新频率的下界，并证明了MMR在渐进意义下是接近最优的。

### 相关工作

[5] Benaloh 等. One-way accumulators: a decentralized alternative to digital signatures. **EUROCRYPT 1993** [Google Scholar](https://scholar.google.com/scholar?q=One-way+accumulators+a+decentralized+alternative+to+digital+signatures)
> 核心思路：提出了基于RSA组的代数累加器，能够生成恒定大小的包含证明和恒定大小的更新成本。
> 局限与区别：添加新元素时，所有现有元素的见证都需要更新，导致 O(n²) 次见证更新，不适用于需要低更新频率的场景。

[11] Camenisch 等. Dynamic accumulators and application to efficient revocation of anonymous credentials. **CRYPTO 2002** [Google Scholar](https://scholar.google.com/scholar?q=Dynamic+accumulators+and+application+to+efficient+revocation+of+anonymous+credentials)
> 核心思路：在RSA累加器基础上增加了高效的元素删除操作，成为动态累加器。
> 局限与区别：本文针对的是仅追加（不可删除）的累加器，动态累加器的下界证明依赖删除操作，不适用于仅追加场景。

[34] Merkle. A digital signature based on a conventional encryption function. **CRYPTO 1987** [Google Scholar](https://scholar.google.com/scholar?q=A+digital+signature+based+on+a+conventional+encryption+function)
> 核心思路：提出了经典的Merkle树结构，作为向量承诺使用，支持对数大小的包含证明。
> 局限与区别：标准的Merkle树中，每次向叶子添加新元素都需要重新计算根哈希，从而导致所有包含证明都需更新，见证更新总次数为 O(n²)。

[42] Reyzin 等. Efficient asynchronous accumulators for distributed PKI. **SCN 2016** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+asynchronous+accumulators+for+distributed+PKI)
> 核心思路：独立于Todd的工作，重新发明了Merkle Mountain Range结构，使用二叉树并合并相同大小的树，以管理分布式PKI中的公钥注册。
> 局限与区别：给出了 MMR 的定性分析，但未提供理论下界，本文将 MMR 的 O(n log n) 更新复杂度与推导出的 Ω(n log n / log log n) 下界进行了比较，证明其渐进接近最优。

[22] Garg 等. Registration-based encryption: removing private-key generator from IBE. **TCC 2018** [Google Scholar](https://scholar.google.com/scholar?q=Registration-based+encryption+removing+private-key+generator+from+IBE)
> 核心思路：提出了注册加密（RBE），由非可信的密钥策展人管理用户注册，再次独立发明了 MMR 结构以管理注册列表。
> 局限与区别：RBE 的更新下界与累加器相关但不相同，且该文的部分下界局限于有附加限制的累加器模型，本文的下界没有此类限制。

[34] Merkle. A digital signature based on a conventional encryption function. **CRYPTO 1987** [Google Scholar](https://scholar.google.com/scholar?q=A+digital+signature+based+on+a+conventional+encryption+function)
> 核心思路：同上，经典的默克尔树。
> 局限与区别：同上，O(n²) 见证更新。

[19] Dwork 等. How efficient can memory checking be? **TCC 2009** [Google Scholar](https://scholar.google.com/scholar?q=How+efficient+can+memory+checking+be)
> 核心思路：研究了内存检查器的效率，使用压缩论证证明了其查询复杂度的下界。
> 局限与区别：内存检查器的功能比仅追加累加器强大得多，支持任意读写操作，其下界不直接适用于累加器。本文借鉴了类似的压缩论证思想，但针对的是更具限制性的仅追加累加器模型。

[10] Camacho 等. On the impossibility of batch update for cryptographic accumulators. **LATINCRYPT 2010** [Google Scholar](https://scholar.google.com/scholar?q=On+the+impossibility+of+batch+update+for+cryptographic+accumulators)
> 核心思路：研究了动态累加器的批量更新问题，证明了至少线性数量的信息需要被通信才能更新所有见证。
> 局限与区别：该下界主要针对支持删除操作的动态累加器，其证明依赖删除操作，不适用于仅追加场景。

[13] Christ 等. Limits on revocable proof systems, with applications to stateless blockchains. **Financial Crypto 2022** [Google Scholar](https://scholar.google.com/scholar?q=Limits+on+revocable+proof+systems+with+applications+to+stateless+blockchains)
> 核心思路：研究了可撤销证明系统的下界，证明了在删除 n 个元素时，至少有 Ω(n / log n) 个见证需要改变。
> 局限与区别：该下界也依赖删除或普遍性（支持非成员证明）功能，且下界强度弱于本文的 Ω(n) 单个元素见证变化次数。

[38] Nguyen. Accumulators from bilinear pairings and applications. **CT-RSA 2005** [Google Scholar](https://scholar.google.com/scholar?q=Accumulators+from+bilinear+pairings+and+applications)
> 核心思路：提出了基于双线性对的累加器，拥有恒定大小的证明和更新成本。
> 局限与区别：与 RSA 累加器类似，添加新元素时所有现有元素的见证都需更新，导致 O(n²) 次见证更新。

[47] Todd. Merkle Mountain Ranges. **OpenTimestamps 2013** [Google Scholar](https://scholar.google.com/scholar?q=Merkle+Mountain+Ranges)
> 核心思路：首次提出了 Merkle Mountain Range 数据结构，用于在比特币区块链上进行高效的时间戳验证。
> 局限与区别：该工作提出了 MMR 的具体构造，但未提供其最优性的理论证明。本文填补了这一空白。

### 核心技术与方案

本文提出了一种基于压缩论证的信息论下界证明方法，用于分析仅追加累加器的见证更新频率。整体框架分为两个层次。

第一层是单次见证变化引理（Lemma 1）。该引理通过一个压缩-解码游戏证明，对于任何简洁的累加器（大小不超过 O(λ polylog n)），在一次添加序列中，至少有 c|S| 个元素（c 为任意小于 1 的常数）的见证在其被添加后发生过至少一次变化。在游戏中，Alice 选择一个随机子集 S 并计算最终累加器 A。她除了发送 A 外，还发送一个比特向量 v，其中每个比特对应数据宇宙 U 中的一个元素，1 表示该元素在 S 中且其见证已变化，0 表示该元素不在 S 中。Bob 根据 A 和 v 重建 S。如果见证变化很少，则 |v| 将远小于 |U|，使得 Alice 能用一个比信息论下界短得多的消息传达出一个随机子集，从而形成矛盾。这个引理的核心在于，即使累加器是随机的，对于大多数公共参数和随机种子，大多数子集都会迫使大量见证发生变化。

第二层是多次见证变化引理（Lemma 2），它将单次变化推广到多个子序列。核心思想是将元素序列划分为多个长度为 m 的段，每个段要么来自集合 P，要么来自集合 Q。Alice 根据一个秘密比特向量 s 从 P 或 Q 中选取每个段，并累加所有段得到最终累加器 A。Bob 通过尝试用 P 或 Q 的段累加并验证其见证是否对 A 有效，来推断 s 的每个比特。如果全部段在累加后所有见证都已失效，Alice 则用向量 v 记录 s 的对应比特。Lemma 2 证明，只要段数量 d 远大于累加器大小，那么几乎所有段中至少 cdm（c 为常数）个元素的见证会在后续段添加过程中发生变化。这个证明同样使用压缩论证：如果见证变化太少，Alice 就能用过短的 (A, v) 传达出 s（一个来自大小为 2^d/poly(λ) 的集合的随机元素）。

通过将第二轮证明结果与第一轮证明结果结合（Theorem 1），建立了层次化的论证。将整个序序列视为 d^h 个分段，形成一个 h 层的金字塔结构。在每个层级 i，将 d 个大小为 d^(i-1) 的段合并成一个大小为 d^i 的段。Lemma 2 保证，当从第 i 层的累加器进到第 i+1 层的累加器时，几乎所有 d 个分段的元素见证都会再次失效。因此，每个层级贡献了约 c * n 次见证更新。对于 n 个元素累加器，Set h = α / 0.99，则可证明总见证更新次数至少为 α * n，这对任何常数 α 成立。

对于可容纳超多项式大小集合的累加器（如 MMR），Corollary 2 将下界进一步强化到 Ω(β n log n / log log n)，其中 β 由集合大小的上界 2^{λ^β} 决定。证明通过设定 d = (p(λ) q(log n))²，h = log n / log d，并利用累加器大小 p(λ) q(log n) 的界来展开 argument。

### 核心公式与流程

**[单次见证变化引理（Lemma 1）的编码算法]**
> 作用：Alice 计算最终累加器 A_k^S 和比特向量 v，v 编码了哪些元素的见证发生了变化。

**[单次见证变化引理（Lemma 1）的解码算法]**
> 作用：Bob 利用 A_k^S 和 v 重建 Alice 选择的子集 S。

**[多次见证变化引理（Lemma 2）的编码算法]**
> 作用：Alice 根据秘密比特向量 s 从 P 或 Q 中选择段，计算最终累加器 A_{m0+dm}^s 和比特向量 v，v 只记录那些段中所有见证都失效的段的比特。

**[多次见证变化引理（Lemma 2）的解码算法]**
> 作用：Bob 利用 A_{m0+dm}^s 和 v 重建秘密比特向量 s。

**[层次结构图]**
> 作用：展示了证明 Theorem 1 时使用的层次结构。每一层由多个分段组成，从底层 L_0 到顶层 L_h，见证次数逐层累加。

### 实验结果

由于本文是理论计算机科学论文，核心贡献是信息论下界的证明，因此没有传统的实验评估。论文通过渐进复杂性分析（表 1）展示了不同累加器方案的性能对比。对于 k-ary MMR，论文给出的上界是：累加器大小为 O(k log_k n)，总见证更新次数为 O(n log_k n)。通过对 log n-ary MMR 的分析，累加器大小为 O(log² n)，总见证更新次数为 O(n log n / log log n)。论文的理论下界与这个上界在渐进意义下匹配（忽略常数因子）。论文在 Remark 3 中指出，MMR 在随机预言机模型（Random Oracle Model）下是安全的，其安全性依赖于哈希函数的抗碰撞性。论文没有提供具体硬件配置或数据集规模下的运行时间或通信开销数值。

### 局限性与开放问题

本文的下界证明主要适用于信息论的压缩论证，假设了全知 Alic 和 Bob 以及无限的运行时间，这与计算有界的实际场景存在差距。此外，证明假设累加器的运行是概率算法，但论证的信息论性质使其不受特定计算假设限制。一个开放问题是，是否存在比 MMR 更优的构造，能够以稍微增加累加器大小为代价，进一步减少见证更新频率，从而逼近或打破本文所给出的下界。另一个开放问题是如何将类似的压缩论证技术推广到其它密码学原语（如向量承诺、键值承诺）的更新频率分析中，或者给出可证明安全的计算性下界。

### 强关联论文

[11] Camenisch 等. Dynamic accumulators and application to efficient revocation of anonymous credentials. **CRYPTO 2002** [Google Scholar](https://scholar.google.com/scholar?q=Dynamic+accumulators+and+application+to+efficient+revocation+of+anonymous+credentials)

[13] Christ 等. Limits on revocable proof systems, with applications to stateless blockchains. **Financial Crypto 2022** [Google Scholar](https://scholar.google.com/scholar?q=Limits+on+revocable+proof+systems+with+applications+to+stateless+blockchains)

[19] Dwork 等. How efficient can memory checking be? **TCC 2009** [Google Scholar](https://scholar.google.com/scholar?q=How+efficient+can+memory+checking+be)

[22] Garg 等. Registration-based encryption: removing private-key generator from IBE. **TCC 2018** [Google Scholar](https://scholar.google.com/scholar?q=Registration-based+encryption+removing+private-key+generator+from+IBE)

[31] Liang 等. Study on data storage and verification methods based on improved Merkle mountain range in IoT scenarios. **J. King Saud Univ.-Comput. Inf. Sci. 2024** [Google Scholar](https://scholar.google.com/scholar?q=Study+on+data+storage+and+verification+methods+based+on+improved+Merkle+mountain+range+in+IoT+scenarios)

[34] Merkle. A digital signature based on a conventional encryption function. **CRYPTO 1987** [Google Scholar](https://scholar.google.com/scholar?q=A+digital+signature+based+on+a+conventional+encryption+function)

[38] Nguyen. Accumulators from bilinear pairings and applications. **CT-RSA 2005** [Google Scholar](https://scholar.google.com/scholar?q=Accumulators+from+bilinear+pairings+and+applications)

[42] Reyzin 等. Efficient asynchronous accumulators for distributed PKI. **SCN 2016** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+asynchronous+accumulators+for+distributed+PKI)

[47] Todd. Merkle Mountain Ranges. **OpenTimestamps 2013** [Google Scholar](https://scholar.google.com/scholar?q=Merkle+Mountain+Ranges)

[53] Wang 等. The locality of memory checking. **CCS 2023** [Google Scholar](https://scholar.google.com/scholar?q=The+locality+of+memory+checking)


## 关键词

+ 密码学累加器
+ 见证更新下界
+ Merkle Mountain Range最优性
+ 压缩论证
+ 仅追加集合承诺