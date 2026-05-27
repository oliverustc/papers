---
title: "Leaking arbitrarily many secrets: Any-out-of-many proofs and applications to ringct protocols"
doi: 10.1109/sp46215.2023.10179292
标题简称:
论文类型: conference
会议简称: S&P
发表年份: 2023
created: 2025-04-22 11:42:39
modified: 2025-04-22 11:43:57
---
## Leaking arbitrarily many secrets: Any-out-of-many proofs and applications to ringct protocols

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/10179292)

## 作者

+ Tianyu Zheng 
+ Shang Gao 
+ Yubo Song 
+ [Bin Xiao](Bin%20Xiao.md)
## 笔记

### 背景与动机
现有基于环签名的隐私加密货币方案，例如门罗币，使用环机密交易 (RingCT) 来隐藏交易的发送方身份和转账金额。这些方案大多依赖“一的众多证明” (one-out-of-many proofs) 来证明花费者拥有对应环中某个公钥的私钥。然而，当一次交易涉及多个真实输入账户时，现有方案面临两个核心瓶颈：效率低下和匿名性弱。为了处理多个输入，传统方案为每个真实源账户独立生成一个一的众多证明，导致交易大小随输入数量线性增长，并且仍然只能达到 1-out-of-n 的匿名性。虽然一些后续工作如 Omniring [11] 通过重排账户矩阵提高了部分抵抗内部攻击的能力，但它们的底层仍然是处理单一秘密的一的众多证明，无法实现真正的“统一环”匿名，即无法将多个真实源账户均匀隐藏在一个更大的匿名集中。此外，现有用于多秘密的部分知识证明，如 Attema 等人 [17] 的工作，虽然达到了对数大小的证明，但泄露了秘密的数量 k，且依赖双线性配对，难以与范围证明等核心技术高效结合。因此，本文旨在填补这一空白：设计一种无需配对、隐藏秘密数量 k、且能与 Bulletproofs 等压缩技术兼容的任意多秘密部分知识证明，并以此构建一个高效、强匿名性的 RingCT 协议。

### 相关工作

[12] Groth 等. One-out-of-many proofs: Or how to leak a secret and spend a coin. **EUROCRYPT 2015** [Google Scholar](https://scholar.google.com/scholar?q=One-out-of-many+proofs%3A+Or+how+to+leak+a+secret+and+spend+a+coin)
> 核心思路：提出了对数大小的“一的众多证明”，允许证明者在 N 个公开承诺中知道一个秘密。
> 局限与区别：该方案天然设计用于单个秘密，无法高效扩展到多个秘密的场景，导致多个输入时交易体积线性增长。

[9] Sun 等. RingCT 2.0: A compact accumulator-based (linkable ring signature) protocol for blockchain cryptocurrency monero. **ESORICS 2017** [Google Scholar](https://scholar.google.com/scholar?q=RingCT+2.0%3A+A+compact+accumulator-based+%28linkable+ring+signature%29+protocol+for+blockchain+cryptocurrency+monero)
> 核心思路：通过按行折叠账户矩阵来压缩证明大小，但本质仍是基于一的众多证明。
> 局限与区别：其匿名性仍然是 1-out-of-n，且当有人能够去匿名化一个真实源账户时，同行中的其他真实账户也会被暴露。

[10] Yuen 等. RingCT 3.0 for blockchain confidential transaction: Shorter size and stronger security. **FC 2020** [Google Scholar](https://scholar.google.com/scholar?q=RingCT+3.0+for+blockchain+confidential+transaction%3A+Shorter+size+and+stronger+security)
> 核心思路：通过重排多个真实源账户在不同行的位置来抵抗内部攻击，提升匿名性。
> 局限与区别：该方案仍然受限于一的众多证明的底层结构，其匿名空间是 (n/k)^k，远小于理想情况。

[11] Lai 等. Omniring: Scaling private payments without trusted setup. **CCS 2019** [Google Scholar](https://scholar.google.com/scholar?q=Omniring%3A+Scaling+private+payments+without+trusted+setup)
> 核心思路：提出了“统一环”的概念，通过将多个源账户随机分布在更大的环中来提升匿名性，达到了二项式匿名空间。
> 局限与区别：其“统一环”并非严格意义上的统一（定义为列数），且其底层仍不是真正的部分知识证明，未解决隐藏秘密数量 k 的问题。

[17] Attema 等. Compressing proofs of k-out-of-n partial knowledge. **CRYPTO 2021** [Google Scholar](https://scholar.google.com/scholar?q=Compressing+proofs+of+k-out-of-n+partial+knowledge)
> 核心思路：提出了第一个对数大小的 k-out-of-N 部分知识证明，并使用 Bulletproofs 压缩。
> 局限与区别：该方案泄露了秘密数量 k，导致匿名性弱化；同时依赖双线性配对，这导致在 RingCT 中与范围证明等通用组件结合时效率不高。

[19] Bünz 等. Bulletproofs: Short proofs for confidential transactions and more. **S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Bulletproofs%3A+Short+proofs+for+confidential+transactions+and+more)
> 核心思路：提出了一种对数大小的内积论证协议，能将向量承诺的证明压缩到对数级别，且无需可信设置。
> 局限与区别：本文在通用压缩模型中借鉴并扩展了 Bulletproofs 技术，将其应用于新的任意多秘密证明关系中。

[22] Boneh 等. Batching techniques for accumulators with applications to iops and stateless blockchains. **CRYPTO 2019** [Google Scholar](https://scholar.google.com/scholar?q=Batching+techniques+for+accumulators+with+applications+to+iops+and+stateless+blockchains)
> 核心思路：提出了一个无陷门的通用累加器，用于实现无状态区块链。
> 局限与区别：本文利用该累加器改进了标签方案，以解决 RingCT 中交易验证对巨大状态数据的依赖问题，实现恒定大小的状态验证。

[18] Diamond 等. Many-out-of-many proofs and applications to anonymous zether. **S&P 2021** [Google Scholar](https://scholar.google.com/scholar?q=Many-out-of-many+proofs+and+applications+to+anonymous+zether)
> 核心思路：提出了一种“多的众多证明”，通过公开置换来压缩多个一的众多证明。
> 局限与区别：该方法并未实现真正的部分知识证明，对匿名性提升有限，且并未隐藏秘密数量。

### 核心技术与方案
本文的整体框架分为三个层次：首先，提出了一个通用的内积转换模型，用于将二次关系转换为可被 Bulletproofs 压缩的内积形式；其次，基于该模型构造了一个新型的任意多秘密证明（any-out-of-many proof）；最后，将该证明技术作为核心模块，构建了一个高效且强匿名性的 RingCT 协议。

**通用内积转换模型 (Section IV)**。为将任意多秘密证明的二元约束转换为可压缩形式，作者首先提出如何将一般的二次关系转换为内积形式。对于一个向量 $\mathbf{b} \in \mathbb{Z}_q^n$ 上的二次关系 $f(\mathbf{b}) = \mathbf{0}^n$，利用挑战 $y$ 和 $z$，可以将其重写为 $\langle \zeta(\mathbf{b}_0), \eta(\mathbf{b}_1) \rangle = \delta$ 的形式，其中 $\mathbf{b}_0 = \mathbf{b}$，$\mathbf{b}_1 = \alpha \circ \mathbf{b} + \beta$。进一步，对于同一对向量 $(\mathbf{b}_0, \mathbf{b}_1)$ 上的多个独立内积关系，以及不同对向量上的内积关系，该模型展示了如何使用随机挑战将它们合并为单一内积。这个模型允许将复杂的逻辑约束（如二进制证明）压缩进单一的内积论证中，从而能够直接应用 Bulletproofs 的对数级压缩。

**任意多秘密证明 (Section V)**。核心贡献在于构造了任意多秘密证明。该证明的关键在于将多个秘密 $s_j$ 的验证通过一个随机挑战 $y$ 摊销为一个标量值 $f_s = \sum_{j=1}^k y^{i_j} \cdot s_j$，使得验证等式变为 $\mathbf{P}^{\mathbf{y}^N \circ \mathbf{b}} = g^{f_s}$。这里 $\mathbf{b}$ 是一个隐藏了位置信息且未知数量的二进制向量。这个等式形式上与一的众多证明类似，但其 $\mathbf{b}$ 向量不受只有一个“1”的限制。为了证明 $\mathbf{b}$ 是一个二进制向量（即 $\mathbf{b} \circ (\mathbf{1}^N - \mathbf{b}) = \mathbf{0}^N$），作者利用通用内积转换模型将其转换为内积形式。最终，所有约束（二进制证明、秘密验证）被整合进一个内积关系中，并通过 Bulletproofs 压缩到 $2\lceil \log_2(N) \rceil + 3$ 个群元素和 6 个域元素的大小。该证明方案被证明是完美完备的，具有完美特殊 HVZK，且在离散对数 (DL) 假设下具有计算特殊可靠性。

**RingCT 协议实例化 (Section VI)**。基于上述任意多秘密证明，本文构建了完整的 RingCT 协议。协议整合了三个关键部分：1) **改进的标签方案**：使用无陷门累加器 [22] 而非全局状态列表来验证双花攻击，使节点只需检查一个关于累加器状态的证明，而无需遍历所有历史标签，从而实现恒定大小的验证状态。2) **合并证明**：将秘密密钥验证、余额证明和标签证明整合到同一个基于 $\mathbf{b}$ 向量的等式中。具体而言，将公钥、标签、余额承诺编码到统一的基向量中，使得一个任意多秘密证明就可以同时验证这三个关系。3) **聚合范围证明**：利用通用模型中的 Lemma 3，将任意多秘密证明产生的内积向量与多个范围证明产生的内积向量连接成一个更长的向量，并通过一次 Bulletproofs 压缩对所有证据进行聚合。最终，该 RingCT 协议的证明大小为 $2\lceil \log_2(|\mathcal{R}| + \beta|\mathcal{T}|)\rceil$，匿名空间达到 $2^{|\mathcal{R}|}$。安全性证明表明，该协议在 ROM 和 DL/q-DDHI 假设下满足不可伪造性、等价性、链接性、不出售性和强匿名性。

### 核心公式与流程

**[任意多秘密证明的核心等式]**
$$\mathbf{P}^{\mathbf{y}^N \circ \mathbf{b}} = \prod_{j=1}^k P_{i_j}^{y^{i_j} \cdot 1} = g^{f_s}$$
> 作用：将验证 k 个秘密的知识转化为对一个二进制向量 $\mathbf{b}$ 的单一承诺的验证，其中 $f_s$ 是摊销后的秘密值，这是实现隐藏 k 和对数压缩的关键。

**[通用内积转换 (二元约束)]**
$$\langle \zeta(\mathbf{b}_0), \eta(\mathbf{b}_1) \rangle = \delta$$
> 作用：将二元向量约束 $\mathbf{b} \circ (\mathbf{1}^N - \mathbf{b}) = \mathbf{0}^N$ 转换为一个内积关系，是压缩该约束的前提。

**[Bulletproofs 单轮压缩]**
$$\boldsymbol{a}' = x \boldsymbol{a}_L + \boldsymbol{a}_R, \quad \boldsymbol{b}' = \boldsymbol{b}_L + x \boldsymbol{b}_R$$
$$\boldsymbol{g}' = \boldsymbol{g}_L \circ \boldsymbol{g}_R^x, \quad \boldsymbol{h}' = \boldsymbol{h}_L^x \circ \boldsymbol{h}_R$$
> 作用：将长度为 n 的向量压缩为 n/2，迭代 $\lceil \log_2(N) \rceil$ 次后，可以仅用两个域元素与其他辅助元素完成证明。

**[RingCT 协议证明大小]**
$$2\lceil \log_2(|\mathcal{R}| + \beta|\mathcal{T}|)\rceil$$
> 作用：表明整个 RingCT 证明（包括签名、余额证明和范围证明）在被聚合压缩后，其规模与环大小 $|\mathcal{R}|$ 和对数币值上限 $\beta$ 以及对数输出数量 $|\mathcal{T}|$ 的对数成线性关系。

### 实验结果
论文在 Golang 环境下实现了原型，使用 Secp256k1 椭圆曲线库（128 位安全性），在 Intel i5-4210U 1.70GHz 单线程、低于 200 MB 内存的环境下测试。在任意多秘密证明方面，比较了不同环大小下的证明尺寸，结果显示新方案的渐近尺寸与一的众多证明 [15] 相近，但常数项更小；与 k-out-of-N 证明 [17] 相比，即使后者用配对优化，由于配对群元素更大，新方案的字节级别性能仍更优。在 RingCT 协议方面，与 RingCT 3.0 [10] 和 Omniring [11] 对比，新方案的证明规模在环大小大于 500 时几乎是 RingCT 3.0 的一半，符合理论分析。在计算时间上，当环大小为 16（大于门罗币的 11）时，生成证明仅需 249 毫秒，验证时间约为生成时间的 1/5。所有实验表明，新方案的性能在真实应用场景中是可接受的，且在匿名性上达到最优。参数方面，以 44.3 比特的匿名性为目标，新方案仅需要 64 大小的环，而 k-out-of-N 和 RingCT 3.0 则需要 181 和 256。

### 局限性与开放问题
尽管通用内积转换模型对二次关系有效，但将其扩展到更高次多项式关系时，需要承诺 $O(n)$ 个元素，导致即便使用 Bulletproofs 压缩也难以减小证明规模，因此如何实现更高次多项式关系的最小元素转换是一个开放问题。此外，改进的标签方案使用素数累加器，每个交易需要唯一的大素数，随着交易量累积可能会导致素数库耗尽。作者指出，设计一种不泄露 k 的、针对真实账户标签的部分知识证明或许能避免该问题。

### 强关联论文

[12] J. Groth and M. Kohlweiss. _One-out-of-many proofs: Or how to leak a secret and spend a coin._ **EUROCRYPT 2015**.

[9] S.-F. Sun, M. H. Au, J. K. Liu, and T. H. Yuen. _Ringct 2.0: A compact accumulator-based (linkable ring signature) protocol for blockchain cryptocurrency monero._ **ESORICS 2017**.

[10] T. H. Yuen, S.-f. Sun, J. K. Liu, M. H. Au, M. F. Esgin, Q. Zhang, and D. Gu. _Ringct 3.0 for blockchain confidential transaction: Shorter size and stronger security._ **FC 2020**.

[11] R. W. Lai, V. Ronge, T. Ruffing, D. Schröder, S. A. K. Thyagarajan, and J. Wang. _Omniring: Scaling private payments without trusted setup._ **CCS 2019**.

[17] T. Attema, R. Cramer, and S. Fehr. _Compressing proofs of k-out-of-n partial knowledge._ **CRYPTO 2021**.

[19] B. Bünz, J. Bootle, D. Boneh, A. Poelstra, P. Wuille, and G. Maxwell. _Bulletproofs: Short proofs for confidential transactions and more._ **S&P 2018**.

[22] D. Boneh, B. Bünz, and B. Fisch. _Batching techniques for accumulators with applications to iops and stateless blockchains._ **CRYPTO 2019**.

[18] B. E. Diamond. _Many-out-of-many proofs and applications to anonymous zether._ **S&P 2021**.


## 关键词

+ 任意多对多零知识证明
+ 环形机密交易RingCT
+ 部分知识证明
+ Bulletproofs压缩
+ 隐私加密货币
+ 多重环签名