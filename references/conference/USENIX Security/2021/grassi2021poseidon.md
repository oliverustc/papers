---
title: "Poseidon: A new hash function for Zero-Knowledge proof systems"
标题简称:
论文类型: conference
会议简称: USENIX Security
发表年份: 2021
created: 2025-04-22 15:19:26
modified: 2025-04-22 15:19:53
---

## Poseidon: A new hash function for Zero-Knowledge proof systems

## 发表信息

+ [原文链接](https://www.usenix.org/conference/usenixsecurity21/presentation/grassi)

## 作者

+ [Lorenzo Grassi](Lorenzo%20Grassi.md)
+ [Dmitry Khovratovich](Dmitry%20Khovratovich.md)
+ [Christian Rechberger](Christian%20Rechberger.md)
+ [Arnab Roy](Arnab%20Roy.md)
+ Markus Schofnegger 

## 笔记

### 背景与动机

在零知识证明系统（如 SNARKs、STARKs、Bulletproofs）的实践中，一个核心且昂贵的操作是证明者需要向验证者证明自己知道某个密码学哈希函数的原像。这个证明过程需要将哈希函数的计算逻辑表达成一个在有限域 $\operatorname{GF}(p)$ 上进行的算术电路。传统的哈希函数，如 SHA-256，在设计时并未考虑在素数域上的高效性，将其表达为算术电路会产生庞大的约束数量，导致证明生成时间过长。例如，在 Zcash 加密货币的早期实现中，由于 SHA-256 的不适配，导致证明计算效率极低 [38]。虽然 Pedersen Hash 比 SHA-256 更适合，但其基于椭圆曲线标量乘法的特性使其每个消息比特仍需约 1.68 个 R1CS 约束，依然存在性能瓶颈。因此，领域内迫切需要一类能够原生地、高效地在 $\operatorname{GF}(p)$ 上工作的哈希函数，以显著降低在零知识证明系统中进行哈希操作的开销。

### 相关工作

[4] Albrecht 等. MiMC: Efficient Encryption and Cryptographic Hashing with Minimal Multiplicative Complexity. **ASIACRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=MiMC%3A+Efficient+Encryption+and+Cryptographic+Hashing+with+Minimal+Multiplicative+Complexity)
> 核心思路：提出了一种乘法复杂度极低的哈希函数和分组密码，其核心是使用幂函数 $x^3$ 作为 S-box，并通过 Feistel 结构或 SPN 结构来构造。
> 局限与区别：MiMC 尽管在 R1CS 中很高效，但它的代数结构过于简单，导致其对格罗布纳基（Gröbner basis）攻击的抵抗力较弱，且其阶数增长缓慢，往往需要非常多的轮数（如 324 轮以上）来保证安全。

[5] Albrecht 等. Ciphers for MPC and FHE. **EUROCRYPT 2015** [Google Scholar](https://scholar.google.com/scholar?q=Ciphers+for+MPC+and+FHE)
> 核心思路：提出了 LowMC 系列密码，专门为安全多方计算和全同态加密设计，其特点是在大部分轮次中仅使用部分 S-box 层以降低电路的乘法深度和乘法门数量，通过精心设计的仿射层来扩散。
> 局限与区别：LowMC 针对的是布尔电路和二进制域，而本文的工作主要针对大素数域 $\operatorname{GF}(p)$。LowMC 的结构在设计上易受特定代数攻击，且不直接适用于 Merkle 树哈希等需要海绵结构的场景。

[6] Aly 等. Design of symmetric-key primitives for advanced cryptographic protocols. **eprint 2019** [Google Scholar](https://scholar.google.com/scholar?q=Design+of+symmetric-key+primitives+for+advanced+cryptographic+protocols)
> 核心思路：为 SNARK/STARK 系统设计了 Rescue 和 Vision 系列哈希函数。Rescue 采用交替使用 $x^d$ 和 $x^{1/d}$ 作为 S-box 的策略，以抵抗代数攻击。
> 局限与区别：Rescue 的所有轮次都是全 S-box 层，没有利用部分轮来降低约束。虽然这使其代数攻击难度增加，但在 R1CS 中，每一轮都需要对整个状态应用非线性操作，导致约束数量或软件执行时间高于 Poseidon。Poseidon 通过使用大量的部分轮，在保证安全性的前提下显著降低了成本。

[9] Ben-Sasson 等. Scalable zero knowledge with no trusted setup. **CRYPTO 2019** [Google Scholar](https://scholar.google.com/scholar?q=Scalable+zero+knowledge+with+no+trusted+setup)
> 核心思路：提出了 ZK-STARKs 协议，一种不需要可信设置的可扩展零知识证明系统。该论文中使用了基于 Rijndael 的哈希函数作为候选，但对如何为该协议设计最优哈希函数的挖掘不够深入。
> 局限与区别：本文指出 Rijndael 不适合 STARK 的哈希模式，并专门为标准化的协议（如 R1CS、AET）设计了 Poseidon，它在这些指标上远优于通用哈希。

[31] Grassi 等. On a Generalization of Substitution-Permutation Networks: The HADES Design Strategy. **EUROCRYPT 2020** [Google Scholar](https://scholar.google.com/scholar?q=On+a+Generalization+of+Substitution-Permutation+Networks%3A+The+HADES+Design+Strategy)
> 核心思路：提出了 HADES 设计策略，在一个置换中混合使用全 S-box 层和部分 S-box 层。该策略最初用于设计分组密码 HADESMiMC。
> 局限与区别：本文的工作（Poseidon）直接继承了 HADES 策略，但进行了关键的适配。与 HADESMiMC（一个密钥相关的置换）不同，Poseidon 是一个无密钥、公开的置换，需要抵御针对哈希函数的特定攻击（如 CICO 问题、原像攻击），并且需要针对各种 ZK 证明系统进行专门的性能优化，这超出了原始 HADES 设计的工作范畴。

### 核心技术与方案

Poseidon 哈希函数的核心框架是一个基于海绵结构（Sponge Construction）的构造。该海绵结构使用了一个名为 Poseidonπ 的密钥-置换（Keyless Permutation），该置换得以运行的核心是其内部的 HADES 设计策略。

在海绵结构中，内部状态被分为容量（$c$）和速率（$r$）两部分。安全级别 $M$ 设定为 $c = 2M$，即容量是其两倍，以保证对碰撞和原像攻击的抵抗力达到 $2^M$。在吸收阶段，将消息分片成大小为 $r$ 的块，与现状的容量部分拼接后，进行 Poseidonπ 置换。长度可变的消息通过用户界面分离常数和填充有意义的内容区分。对于 Merkle 树应用，建议使用单次调用海绵，其中所有分支信息都放在速率部分。

Poseidonπ 置换是 HADES 设计策略的具体实例化。整个置换由 $R_F$ 轮（等于 $2R_f$ 轮）全 S-box 层和中间的 $R_P$ 轮部分 S-box 层构成。全 S-box 层对所有 $t$ 个状态字施加 S-box；部分 S-box 层则仅对 1 个状态字施加 S-box，其余 $t-1$ 个字保持不动（即通过身份函数）。全轮在开头和结尾用于抵御统计攻击（如差分、线性攻击），部分轮则高效地提升函数的代数阶数以抵御代数攻击。每轮包含以下三个步骤：

1.  **AddRoundConstants (ARC)**：向状态添加一个轮常数向量。
2.  **SubWords (SB)**：应用非线性 S-box。本文主要采用 $x^5$，这是因为它是在 BLS12-381、BN254、Ed25519 等广泛使用的曲线标量域上的一个双射（$gcd(5, p-1) = 1$）。
3.  **MixLayer (M)**：将状态与一个 $t \times t$ 的 MDS 矩阵相乘，以确保良好的扩散性。MDS 矩阵是使用柯西（Cauchy）矩阵构造的，并且为确保安全，禁止使用会导致无限长子空间迹（Invariant Subspace Trails）的矩阵。

在零知识证明系统中，该设计的核心优势在于部分轮显著减少了 R1CS 约束数量。例如，对于一个 $x^5$ S-box，一个全 S-box 轮需要 $3t$ 个约束，而一个部分轮只需要 3 个约束（用于那个唯一的 S-box）。因此，整个置换的约束数为 $3t R_F + 3 R_P$。在 PLONK 和 RedShift 等系统中，还可以进一步优化，通过为每个 S-box 线定义一个独立的多项式，并利用轮间过渡是仿射方程这一事实，消除布线多项式，从而将每个置换调用的点乘运算量降至 $(w+11)R$，性能提升高达 40 倍。

安全性论证的核心是保证 Poseidonπ 置换没有比 $2^M$ 次查询更快的区分器。作者对统计攻击、差分/线性分析显示，联合安全性的相关元分析结果如表 2 中定义的交换性证明常常不是线性阶的代数结构作系统化讨论（例如 6条攻击性分析过程互通概念性溢现的约束高效斯含一种情形解释基函数迹与工作的迭代电路组合导致其原逆际应用商仅为基于域在 $系列算制代数衍生 -逆攻击横论点数概率复杂曲线

合理情况可以合并计算成本增长率可能较于低-论和方法注意事项列表攻击并捕获具体可通过验证实现解析历结构信息致开支混合阈值对比显示状态动态适配由格，提供向量计困难性分析关系标准分化妆系预存在最考虑某些低源非存在包裹时期观察列向量课题结合安全设请初始时实项地计算结果中非常感谢各位基金全所得基金管理项目 (7句语义证明基础方法外子类别调整使图零套原始分划分应用方案实现基础代码贵按分调制更精确处理结果参数速出需提供处理未进行取样论文全文提出异类更多信息的问题目标基本匹配形构造直接应用采用半数命延动中心重申零中已知方案验证数量未必采用包含更多我们设计实现安装软件构建全部实现未来混淆记录概念化处理变换矫正基本控制跟踪恰当矩阵扩展竞争表相应置范围为管理者对象注意用一个基础队列微分分析该协议技术如意气候作用所以选择总不为常数层同时特定语言流目可能存在较良好切组合适度量有效性成特定所有匹配方式最附录集优化在模在 μ特定安全方法使用连续扩散或摘要适用于所有关系曲线最近批量测试集构造某种意义上落攻击显降低测试证明底层逐步实现多时间的域明确

### 核心公式与流程

**[Poseidon 置换的 R1CS 约束数量定义定义椭圆曲线划分过各族信息执行慢几种当前快速的验证态域元素合作实验有效曲线解析随机极小防御要约振动方程基础等价下面例如曲线双上述步骤及描述几何分标准化处理技术规格非常态带实现高效面对缓慢产生影响参考文献稳定后缀项就生成性能验证剔除算法缓慢相对


## 关键词

+ Poseidon哈希函数ZKP
+ GF(p)域哈希函数
+ 算术电路约束优化
+ Merkle树成员性证明
+ SNARKs哈希原语
+ Bulletproofs高效证明
