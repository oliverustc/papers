---
title: "Batching-efficient ram using updatable lookup arguments"
doi: 10.1145/3658644.3670356
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2024
modified: 2025-04-22 15:50:48
created: 2025-04-13 17:07:04
---
## Batching-efficient ram using updatable lookup arguments

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3658644.3670356)

## 作者

+ Moumita Dutta 
+ [Chaya Ganesh](Chaya%20Ganesh.md)
+ Sikhar Patranabis 
+ Shubh Prakash 
+ Nitin Singh 

## 笔记

### 背景与动机
在可验证计算中，将程序执行结果与内存或状态关联的NP关系直接编码为算术电路是低效的。例如，验证数据库查询、决策树推理或账户余额表批量更新的正确性，都天然需要随机存取存储器（RAM）的抽象。理想的RAM抽象应支持持久性和批处理：前者指状态可在多次计算间持续，后者指能以远小于RAM大小的代价证明一小批状态更新的正确性。区块链Rollup是批处理高效RAM的重要应用场景——链下“第二层”链执行交易并更新状态，链上只需验证一个简洁证明来确认整个批次交易的正确性，从而提升吞吐量。已有的RAM建模方法主要分为三类：基于Merkle树的方法 [30] 虽然支持更新，但具体开销高、难以高效批处理；基于地址有序转录本的方法 [4, 6, 35, 41] 用于一致性检查时，证明者代价与RAM大小呈线性关系，无法满足次线性批处理需求；基于RSA或类群未知阶群的累加器方法 [16, 31] 在批处理方面有显著优势，但为更新计算见证时仍需要线性于群大小的计算量，并且为了维持证据有效需要频繁重算全部预计算参数，产生了高昂的常数开销和同步问题。因此，本文旨在填补“在支持动态表更新的前提下，实现证明复杂度对RAM大小呈次线性依赖的批处理高效RAM”这一技术空白。

### 相关工作

[20] Eagen 等. cq: Cached quotients for fast lookups. **ePrint 2022** [Google Scholar](https://scholar.google.com/scholar?q=cq%3A+Cached+quotients+for+fast+lookups)
> 核心思路：提出CQ方案，利用KZG承诺来缓存编码后的商多项式，实现亚线性于表大小的查找证明。
> 局限与区别：CQ需要针对特定表进行昂贵的预计算，表更新后所有预计算参数失效。本文在其基础上实现了从“近似表”设置中进行高效查找，从而支持表的动态更新。

[33] Posen 等. Caulk+: Table-independent lookup arguments. **ePrint 2022** [Google Scholar](https://scholar.google.com/scholar?q=Caulk%2B%3A+Table-independent+lookup+arguments)
> 核心思路：Caulk+通过在证明中处理表的改变，在一定程度上减少了对表特定参数的依赖。
> 局限与区别：Caulk+的改进有限，当表更新频繁时，其效率优势仍然依赖于表更新的稀疏性；本文则提供了一个系统性的“基础+缓存”框架，显著降低了在更新后重新计算编码商多项式的代价。

[16] Campanelli 等. Succinct zero-knowledge batch proofs for set accumulators. **CCS 2022** [Google Scholar](https://scholar.google.com/scholar?q=Succinct+zero-knowledge+batch+proofs+for+set+accumulators)
> 核心思路：利用RSA累加器实现集合的零知识批处理证明，用于建模RAM状态。
> 局限与区别：该方案在生成非成员证明时需要为数百万账户线性计算大量非成员见证，且预计算参数更新后需要昂贵重算。本文的RAM方案和“基于近似设置的查找”技术避免了线性依赖，在批处理场景下更高效。

[31] Ozdemir 等. Scaling verifiable computation using efficient set accumulators. **USENIX Security 2020** [Google Scholar](https://scholar.google.com/scholar?q=Scaling+verifiable+computation+using+efficient+set+accumulators)
> 核心思路：使用RSA累加器来扩展可验证计算，通过“打包”和组成员证明来支持状态更新。
> 局限与区别：与[16]类似，该方案在批量更新时面临维护大量非成员见证的挑战，且证明生成的固定开销很高。本文的方案在证明者计算量和内存需求上具有更优的渐近性能。

[34] Setty 等. Unlocking the lookup singularity with lasso. **ePrint 2023** [Google Scholar](https://scholar.google.com/scholar?q=Unlocking+the+lookup+singularity+with+lasso)
> 核心思路：提出Lasso方案，利用结构化表的分解性，将大表查找约简为若干小表查找，达到高效的查找效率。
> 局限与区别：Lasso依赖于表的特殊结构（如AND分解），对于任意动态表的通用场景不适用。本文专注于通用且可更新的表，提出了不同的技术路线。

[38] Zapico 等. Caulk: Lookup arguments in sublinear time. **CCS 2022** [Google Scholar](https://scholar.google.com/scholar?q=Caulk%3A+Lookup+arguments+in+sublinear+time)
> 核心思路：Caulk是首个达到亚线性于表大小的查找论证方案，其效率依赖于预先计算的KZG商。
> 局限与区别：Caulk严重依赖表特定预计算，表更新后参数失效，不利于构建动态RAM。本文方法通过直接计算编码商多项式的线性组合，从“近似表”预计算中高效支持更新。

### 核心技术与方案

本文的整体框架是“先提取，再校验”的两阶段策略。第一阶段，利用更新友好的查找论证，从大RAM中提取出与操作相关的子RAM，这避免了在整个大RAM上直接运行线性时间的内存检查。第二阶段，在提取出的小规模子RAM上使用标准的地址有序转录本技术校验操作的一致性。为了使第一步在支持更新的同时仍保持高效，本文提出了两项核心技术：更新友好的查找论证和承诺索引查找论证。

**更新友好的查找论证**解决了现有查找论证（如CQ [20]、Caulk+ [33]）依赖昂贵的表特定预计算的问题。其核心思想是“基础+缓存”策略：维护一个基础表 \( \mathbf{T_b} \) 及其预计算的编码商。对于当前要证明的表 \( \mathbf{T} \)，将其表示为 \( \mathbf{T} = \mathbf{T_b} + \mathbf{T_{ch}} \)，其中 \( \mathbf{T_{ch}} \) 表示变化量，其非零元素的个数为汉明距离 \( \delta \)。关键的创新在于，将一个查询批次所需的加权编码商 \( [Q]_g = \sum_i c_i [(T(X) - T(\xi^i))/(X-\xi^i)]_g \) 的计算分解为对基础表 \( \mathbf{T_b} \) 的和 \( \mathbf{T_{ch}} \) 的两部分之和。对于 \( \mathbf{T_{ch}} \) 部分，文章通过巧妙的代数变换（如公式(5)），将其转化为若干组元素的线性组合，这些组元素是与表无关的KZG打开证明 \( [Z_{\mathbb{H}}(X)/(X-\xi^j)]_g \)。通过对协方差和逆和的计算（引理7.1），可以在 \( O((m+\delta)\log^2(m+\delta)) \) 的域运算和 \( O(m+\delta) \) 的群运算内完成全部计算，证明了从近似预计算中进行高效查找的可行性。策略上，每批 \( m \) 个操作后，若汉明距离 \( \delta \) 增长到 \( \sqrt{mN} \) 量级，则重新生成基础表及其预计算，将成本摊还给各批次，从而实现摊销次线性于 \( N \) 的复杂度。

**承诺索引查找论证**将标准的子向量关系（证明值向量 \( \mathbf{v} \) 是表 \( \mathbf{t} \) 的子集）增强为证明 \( v_i = \mathbf{t}[a_i] \)。本文通过随机线性组合技巧（引理6.1）展示了如何将承诺索引查找约简为单个子向量论证：证明 \( (\chi \mathbf{I}_N + \mathbf{t}) \) 包含 \( (\chi \mathbf{a} + \mathbf{v}) \)，其中 \( \chi \) 是验证者提供的随机挑战，\( \mathbf{I}_N \) 是索引向量。这保证了承诺索引查找可以基于任何同态子向量论证实现，时间复杂度与一个子向量论证实例相当。

**小额更新下的“局部相同”证明** 是第二个关键组件。它需要证明大RAM状态 \( \mathbf{T} \) 和 \( \mathbf{T}' \) 除了索引集 \( \mathbf{a} \) 外完全一致。这通过构造一个仅依赖 \( |\mathbf{a}| \)（即 \( m \)）的简洁多项式协议实现。该协议的核心是构造一个多项式 \( D(X) \)，使得 \( Z_I(X)(T(X) - T'(X)) = D(X)Z_{\mathbb{H}}(X) \) 成立，其中 \( Z_I(X) \) 是索引集对应的消失多项式。如公式(1)所示，\( D(X) \) 被证明是一个次数不超过 \( |\mathbf{a}| \) 的多项式，其系数可通过在集合 \( \mathbf{I} = \text{uniq}(\mathbf{a}) \) 上的插值高效计算。验证者通过检查以上等式以及证明 \( Z_I(X) \) 的根确实属于 \( \{\xi^{a_i}\} \)，来确保两个RAM在绝大多数索引上的一致性。该协议的证明者复杂度为 \( O(m \log^2 m) \)，是整体方案的核心。

**安全性与复杂度**：整个批处理高效RAM协议（图4）的证明建立在AGM模型和Q-DLOG假设之上，其安全性依赖于子组件（承诺索引查找、局部相同证明、子RAM一致性检查）的安全性。组合协议是公开币的，可通过Fiat-Shamir变换实现非交互。总体来看，对于大小为 \( N \) 的RAM和 \( m \) 次操作，证明者的摊销计算复杂度为 \( \widetilde{O}(\sqrt{mN}) \)，通信量为 \( 65 \mathbb{G}_1 + 1 \mathbb{G}_2 + 43 \mathbb{F} \)，验证者需进行9次配对操作。这些复杂度指标明确体现出对大RAM规模 \( N \) 的次线性依赖。

### 核心公式与流程

**[编码商的计算分解]**
$$ Q(X) = Q_{\text{b}}(X) + Q_{\text{ch}}(X) = \sum_{i \in I} c_i \frac{T_{\text{b}}(X) - T_{\text{b}}(\xi^i)}{X - \xi^i} + \sum_{i \in I} c_i \frac{T_{\text{ch}}(X) - T_{\text{ch}}(\xi^i)}{X - \xi^i} $$
> 作用：将当前表 \( T \) 的查找证明所需的加权编码商多项式 \( Q(X) \) 分解为基于预计算基础表的 \( Q_{\text{b}} \) 和基于变化量 \( T_{\text{ch}} \) 的 \( Q_{\text{ch}} \)，使得计算可以部分复用预计算。

**[变化量部分的代数重排]**
$$\begin{aligned}
Q_{\text{ch}}^{(2)}(X) = \sum_{i \in I} \sum_{j \in K \setminus \{i\}} c_i \Delta t_j \frac{\mu_j(X)}{X - \xi^i} \\
= N^{-1} \sum_{i \in I} \left(c_i \cdot \sum_{j \in K \setminus \{i\}} \frac{\xi^j \Delta t_j}{\xi^i - \xi^j}\right) \frac{Z_{\mathbb{H}}(X)}{X - \xi^i} + N^{-1} \sum_{j \in K} \left(\xi^j \Delta t_j \cdot \sum_{i \in I \setminus \{j\}} \frac{c_i}{\xi^j - \xi^i}\right) \frac{Z_{\mathbb{H}}(X)}{X - \xi^j}
\end{aligned}$$
> 作用：将 \( Q_{\text{ch}}^{(2)} \) 重新组织为与表无关的预计算量 \( [Z_{\mathbb{H}}(X)/(X-\xi^j)]_g \) 的线性组合，使得其群运算计算量降至 \( O(|I|+|K|) \)，为高效计算奠定了基础。

**[“局部相同”证明中的商多项式构造]**
$$ D(X) = \frac{Z_I(X)(T(X) - T'(X))}{Z_{\mathbb{H}}(X)} = \sum_{i \in I} \frac{\Delta_i Z_I'(\xi^i)}{Z_{\mathbb{H}}'(\xi^i)} \kappa_i(X) $$
> 作用：该多项式的构造使得验证两个大RAM在索引集 \( I \) 外完全一致成为可能，且其计算复杂度仅依赖于 \( |I| \)（即 \( m \)），而非 \( N \)。这里 \( \kappa_i(X) \) 是集合 \( I \) 的拉格朗日基多项式。

**[承诺索引查找的随机线性组合约简]**
$$ \tilde{c}_t = \gamma c_I + c_t, \quad \tilde{c}_v = \gamma c_a + c_v $$
> 作用：验证者发送随机系数 \( \gamma \) 后，证明者计算 \( \tilde{\mathbf{t}} = \gamma \mathbf{I}_N + \mathbf{t} \) 和 \( \tilde{\mathbf{v}} = \gamma \mathbf{a} + \mathbf{v} \)。证明 \( \tilde{\mathbf{v}} \) 是 \( \tilde{\mathbf{t}} \) 的子向量，即可（以压倒性概率）推断出 \( v_i = \mathbf{t}[a_i] \)，将索引查找问题约简为标准的子向量问题。

### 实验结果

实验基于2.1GHz Intel-i5处理器、16GB内存的商用笔记本电脑，在单线程、Rust编译、BLS12-381曲线（使用CQ方案作为底层子向量论证）环境下进行。核心性能数据如下：对于RAM大小为 \( 2^{20} \)（约100万），批处理规模 \( m = 2^{10} \)（1024）的情况，平均证明生成时间在汉明距离 \( \delta \) 约 \( 2\times10^5 \) 时仍能低于一分钟。最耗时的单项是表特定预计算，对于 \( 2^{20} \) 大小的表需要约12000秒（约3.3小时）。在证明大小与验证方面，方案生成约4.4KB的证明，验证时间约为15ms，两者均与RAM大小和批处理规模无关。与基线方案比较，本文方案在平均证明时间（约94秒）上优于基于Merkle树的方案（450秒）、基于RSA累加器的CFHKKO22方案（约269秒）和OWWB20方案（约593秒），验证时间也与OWWB20持平（7ms）。快速更新算法（引理7.1）相较于朴素计算，对于 \( |I|=2^{10} \)、\( |K|=2^{17} \) 的场景，速度提升超过20倍（39.2秒 vs 839秒）。这些数据表明，本文方案在商用硬件上即可达到有竞争力的性能，且通过合理的离线调度（如每128批更新后重算参数），可以实现约94秒/批的平均在线证明性能，同时保证系统连续性。

### 局限性与开放问题
本文工作的一个主要局限性在于表特定预计算成本较高，尤其是对于大小为百万至十亿级别的RAM，离线重算的开销仍然巨大。虽然通过“基础+缓存”策略摊还了成本，但其实现依赖于一个精心设计的调度策略，这增加了系统的复杂性。未来的开放问题包括：是否可以设计完全无需表特定预计算（即透明设置）且对动态表高效的查找论证，以消除离线计算瓶颈？或者，能否在保证批量处理高效性的同时，进一步降低渐近和具体预计算常数，例如通过利用更新的低秩结构或更高效的代数算法？此外，如何将本文的协议高效适配到具有隐私要求的场景，也是一个有价值的研究方向。

### 强关联论文

[4] Ben-Sasson 等. SNARKs for C: Verifying program executions succinctly and in zero knowledge. **CRYPTO 2013** [Google Scholar](https://scholar.google.com/scholar?q=SNARKs+for+C%3A+Verifying+program+executions+succinctly+and+in+zero+knowledge)

[16] Campanelli 等. Succinct zero-knowledge batch proofs for set accumulators. **CCS 2022** [Google Scholar](https://scholar.google.com/scholar?q=Succinct+zero-knowledge+batch+proofs+for+set+accumulators)

[20] Eagen 等. cq: Cached quotients for fast lookups. **ePrint 2022** [Google Scholar](https://scholar.google.com/scholar?q=cq%3A+Cached+quotients+for+fast+lookups)

[31] Ozdemir 等. Scaling verifiable computation using efficient set accumulators. **USENIX Security 2020** [Google Scholar](https://scholar.google.com/scholar?q=Scaling+verifiable+computation+using+efficient+set+accumulators)

[33] Posen 等. Caulk+: Table-independent lookup arguments. **ePrint 2022** [Google Scholar](https://scholar.google.com/scholar?q=Caulk%2B%3A+Table-independent+lookup+arguments)

[34] Setty 等. Unlocking the lookup singularity with lasso. **ePrint 2023** [Google Scholar](https://scholar.google.com/scholar?q=Unlocking+the+lookup+singularity+with+lasso)

[38] Zapico 等. Caulk: Lookup arguments in sublinear time. **CCS 2022** [Google Scholar](https://scholar.google.com/scholar?q=Caulk%3A+Lookup+arguments+in+sublinear+time)

[39] Zapico 等. Baloo: Nearly optimal lookup arguments. **ePrint 2022** [Google Scholar](https://scholar.google.com/scholar?q=Baloo%3A+Nearly+optimal+lookup+arguments)

[29] Kate 等. Constant-size commitments to polynomials and their applications. **ASIACRYPT 2010** [Google Scholar](https://scholar.google.com/scholar?q=Constant-size+commitments+to+polynomials+and+their+applications)

[29] (原文引用包含此工作，作为KZG承诺方案的基础)


## 关键词

+ 随机存取存储器
+ 批处理高效
+ 查找论证
+ 加密累加器
+ 验证计算
+ 子向量关系