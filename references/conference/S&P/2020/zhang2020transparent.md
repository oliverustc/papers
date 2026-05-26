---
title: Transparent Polynomial Delegation and Its Applications to Zero Knowledge Proof
标题简称: Virgo
论文类型: conference
会议简称: S&P
发表年份: 2020
modified: 2025-04-21 17:14:34
created: 2025-04-07 16:53:43
---

## Transparent Polynomial Delegation and Its Applications to Zero Knowledge Proof

## 发表信息

+ [原文](https://ieeexplore.ieee.org/abstract/document/9152704)
+ [Archive原文](https://eprint.iacr.org/2019/1482)
+ [video](https://www.youtube.com/watch?v=dRggr686ZzE&t=154s)
+ [code](https://github.com/sunblaze-ucb/Virgo)

## 作者

+ [Jiaheng Zhang](Jiaheng%20Zhang.md)
+ [Tiancheng Xie](Tiancheng%20Xie.md)
+ [Yupeng Zhang](Yupeng%20Zhang.md)
+ [Dawn Song](Dawn%20Song.md)

## 笔记

### 背景与动机
零知识证明允许一个强大的证明者向一个弱的验证者证明一个陈述的正确性，而不泄露任何额外信息。尽管SNARK在实践中被广泛采用，具有极短的证明和快速的验证，但其依赖于一个非透明的可信设置阶段来生成结构化参考字符串，若陷门泄露则安全性被破坏。为解决此问题，许多基于不同技术的透明ZKP方案被提出，其中基于Goldwasser等人提出的双倍高效交互证明（GKR协议）的方案因其高效的证明者时间和对于结构化电路的次线性验证时间而备受关注。然而，截至本文工作之前，尚未有一个基于GKR协议的透明ZKP方案能够同时实现简洁（对数级）的证明大小和验证时间。例如，Hyrax [69]方案是透明的，但其证明大小和验证时间为平方根级；而Libra [70]方案是简洁的，但需要一次性可信设置。本文旨在填补这一空白，提出一个基于GKR协议的、无需可信设置的透明ZKP方案，并实现高效的证明者时间和简洁的证明与验证。

### 相关工作

[42] Goldwasser et al. Delegating Computation: Interactive Proofs for Muggles. **J. ACM 2015** [Google Scholar](https://scholar.google.com/scholar?q=Delegating+Computation:+Interactive+Proofs+for+Muggles)
> 核心思路：提出了GKR协议，一个用于分层算术电路的双倍高效交互证明，验证者时间可简洁。
> 局限与区别：该协议本身不是论证系统（不支持私密witness），也不是零知识的。本文在其基础上构建零知识论证。

[70] Xie et al. Libra: Succinct Zero-Knowledge Proofs with Optimal Prover Computation. **CRYPTO 2019** [Google Scholar](https://scholar.google.com/scholar?q=Libra:+Succinct+Zero-Knowledge+Proofs+with+Optimal+Prover+Computation)
> 核心思路：将GKR协议扩展为零知识论证，利用基于双线性映射的零知识可验证多项式委托（zkVPD）。
> 局限与区别：需要一次性可信设置来生成线性大小的公共参数，且使用了模指数和双线性配对等重量级密码操作。本文用新的透明zkVPD取代了其配对基元。

[14] Ben-Sasson et al. Aurora: Transparent Succinct Arguments for R1CS. **ePrint 2018** [Google Scholar](https://scholar.google.com/scholar?q=Aurora:+Transparent+Succinct+Arguments+for+R1CS)
> 核心思路：提出了单变量求和检验协议，通过低度测试（LDT）实现了透明的简洁论证。
> 局限与区别：验证时间是线性的（$O(C)$）。本文利用了其求和检验思路，但通过与GKR结合，将验证时间降低至对数级。

[69] Wahby et al. Doubly-Efficient zkSNARKs without Trusted Setup. **IEEE S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Doubly-Efficient+zkSNARKs+without+Trusted+Setup)
> 核心思路：提出Hyrax，一个透明的ZKP方案，基于GKR和多线性多项式承诺，实现了平方根级证明大小和验证时间。
> 局限与区别：其证明大小和验证时间不是简洁的（对数级），本文的Virgo实现了更优的渐近和实际性能。

[72] Zhang et al. A Zero-Knowledge version of vSQL. **ePrint 2017** [Google Scholar](https://scholar.google.com/scholar?q=A+Zero-Knowledge+version+of+vSQL)
> 核心思路：提出了基于双线性映射的零知识多项式委托方案。
> 局限与区别：需要可信设置，且证明者时间因模指数运算而具有隐藏的对数因子。本文的透明方案在证明者时间上快1-2个数量级。

[5] Ames et al. Ligero: Lightweight Sublinear Arguments without a Trusted Setup. **CCS 2017** [Google Scholar](https://scholar.google.com/scholar?q=Ligero:+Lightweight+Sublinear+Arguments+without+a+Trusted+Setup)
> 核心思路：提出了Ligero方案，基于IOP和MPC-in-the-head，证明大小为$\sqrt{C}$。
> 局限与区别：证明大小是平方根级，验证时间是准线性的。本文的Virgo在验证时间和证明者时间上更具优势。

[42] 同上。

[73] Zhang et al. vSQL: Verifying arbitrary SQL queries over dynamic outsourced databases. **IEEE S&P 2017** [Google Scholar](https://scholar.google.com/scholar?q=vSQL:+Verifying+arbitrary+SQL+queries+over+dynamic+outsourced+databases)
> 核心思路：提出了一个基于配对的VPD方案，并用于构建ZKP。
> 局限与区别：需要可信设置和线性大小的公钥。本文方案无需设置且更高效。

### 核心技术与方案
本文的核心贡献是一个新的透明零知识可验证多项式委托（zkVPD）方案，并基于此构建了完整的透明ZKP系统Virgo。

**透明zkVPD的构造思路**：方案将多项式求值$f(t)$建模为系数向量$\mathbf{c}$与单项式值向量$T$的内积。选取一个大小为$N$的乘法陪集$\mathbb{H}$，通过插值得到唯一的单变量多项式$l(x)$（系数向量）和$q(x)$（$T$向量）。这样，求值就转化为多项式$l(x) \cdot q(x)$在$\mathbb{H}$上的和。证明者利用单变量求和检验协议（如Protocol 4）来证明这个和的正确性。该协议的核心是构造一个理性约束$p(x)$，通过低度测试（LDT）验证其属于Reed-Solomon码，从而间接验证了内积的正确性。在此过程中，证明者通过Merkle树承诺$l(x)$和辅助多项式$h(x)$，并打开验证者查询的点。

**降低验证者开销**：直观地应用上述方法，验证者需要本地计算$q(x)$在查询点的值，这需要线性时间。本文的关键创新在于观察到向量$T$仅由$\ell = O(\log N)$个评估点$t$的参数决定。因此，计算$q(x)$在特定点的值可以被建模为一个输入大小$O(\log N)$、输出大小$O(\kappa)$的算术电路。验证者不再本地计算，而是与证明者运行一次GKR协议 [42]，将这个计算委托给证明者，并验证其结果的正确性。这使得验证时间从$O(N)$降低到$O(\log^2 N)$。该电路（如图3所示）负责从输入$t$计算所有单项式，并通过FFT/IFFT从$T$计算$q(x)$在查询集$\mathbb{L}$上的评估。

**扩展为零知识**：为了使协议不泄露关于多项式$f$的信息，证明者对秘密多项式$l(x)$进行掩码：$l'(x) = l(x) + Z_\mathbb{H}(x) \cdot r(x)$，其中$r(x)$是一个随机多项式，$Z_\mathbb{H}(x)$在$\mathbb{H}$上为零。这样，在$\mathbb{H}$之外打开$l'(x)$不会泄露$l(x)$。同时，为了掩码求和检验本身，证明者引入另一个随机多项式$s(x)$，并运行关于$\alpha l'(x)q(x) + s(x)$的求和检验，其中$\alpha$由验证者随机选取。这确保了协议是零知识的。完整的zkVPD协议如Protocol 3所示。

**完整的零知识论证**：遵循Libra [70]的框架，将上述透明的zkVPD实例化到Protocol 1中，得到最终的透明ZKP方案。针对输入层多项式，利用其特殊形式（多线性延拓加低次掩码），将其转化为大小为$n+2$的向量内积，使得证明者时间为$O(n \log n)$，验证时间为$O(\log^2 n)$。对于中间层的掩码多项式$R_i$和$\delta_i$，因其稀疏性，通过向量内积方式直接处理，而无需再使用GKR代理计算，避免了渐近开销。

**安全性论证**：方案的安全性（完备性和可靠性）基于LDT协议 [14]、Merkle树和GKR协议的可靠性。证明者欺骗成功的概率受这些子协议可靠性误差的并集所界。零知识性通过构造一个模拟器（如图4、5所示）来证明，该模拟器在不了解witness的情况下，能生成与真实协议不可区分的视图。方案在随机预言机模型中具备知识可靠性。

**渐进复杂性**：对于大小为$C$、深度为$D$的规则电路和大小为$n$的witness，Virgo的证明者时间为$O(C + n \log n)$次域操作，验证者时间为$O(|x| + D \log C + \log^2 n)$，证明大小为$O(D \log C + \log^2 n)$。当$D$为$\text{polylog}(C)$时，该方案是简洁的。

### 核心公式与流程

**[多项式延拓建模]**
$$f(t) = \sum_{i=1}^{N} c_i \cdot W_i(t) = \sum_{a \in \mathbb{H}} l(a) \cdot q(a)$$
> 作用：将多变量多项式求值转化为单变量多项式乘积在点集上的求和，是构建VPD的基础。

**[VPD核心理性约束]**
$$p(x) = \frac{|\mathbb{H}| \cdot l(x) \cdot q(x) - \mu - |\mathbb{H}| \cdot Z_\mathbb{H}(x) h(x)}{|\mathbb{H}| \cdot x}$$
> 作用：当$\mu = f(t)$正确时，$p(x)$是次数严格小于$|\mathbb{H}|-1$的多项式，从而通过LDT验证的正确性。

**[零知识VPD的求和检验]**
$$\alpha \mu + S = \sum_{a \in \mathbb{H}} (\alpha l'(a) \cdot q(a) + s(a))$$
> 作用：验证者通过随机线性组合$\alpha$，将关于$\mu$和$S$的两个求和检验合并为一个，其中掩码多项式$s$保证了零知识性质。

**[GKR协议层间约化关系]**
$$\alpha_i \tilde{V}_i(u^{(i)}) + \beta_i \tilde{V}_i(v^{(i)}) = \sum_{x, y \in \{0,1\}^{s_{i+1}}} f_i(\tilde{V}_{i+1}(x), \tilde{V}_{i+1}(y))$$
> 作用：将关于第$i$层的多项式求值声明，通过求和检验约化为关于第$i+1$层的求值声明，构成了GKR协议递归的核心。

**[带掩码的层间约化关系]**
$$\alpha_i \dot{V}_i(u^{(i)}) + \beta_i \dot{V}_i(v^{(i)}) + \gamma_i H_i = \sum_{x, y, z} f_i'(\dot{V}_{i+1}(x), \dot{V}_{i+1}(y), R_i(u_1^{(i)}, z), R_i(v_1^{(i)}, z), \delta_i(x, y, z))$$
> 作用：将GKR协议扩展为零知识，通过掩码多项式$R_i$和$\delta_i$以及随机挑战$\gamma_i$来隐藏电路中间值，同时保证约化关系的正确性。

### 实验结果
实验在AMD Ryzen 3800X处理器（64GB RAM，单核）上进行。论文精心选择了Mersenne素数$p=2^{61}-1$的二次扩域$\mathbb{F}_{p^2}$作为底层域，该域支持高效的模拟乘法和用于低度测试的$2^{m+1}$阶乘法子群，同时其子域$\mathbb{F}_p$可直接编码算术电路的值，实现了速度与通用性的平衡。在zkVPD对比测试中，对于大小为$2^{20}$的多项式，新方案的证明者时间仅为11.7秒，比基于双线性映射的方案 [72] 快约8-10倍，验证时间（12.4ms）也更快。在完整ZKP系统Virgo的评估中，与Libra [70]相比，证明者时间在三个基准测试（矩阵乘法、图像缩放、Merkle树）上快3-10倍。例如，对于$2^{26}$门规模的Merkle树电路（256个叶子），Virgo仅需53.40秒生成证明，而Libra需要数百秒。验证时间同样大幅领先，对于Merkle树基准，Virgo的验证时间为50ms，快1-2个数量级。在与其他透明ZKP系统（Ligero [5], Bulletproofs [28], Hyrax [69], Stark [9], Aurora [14]）的比较中，Virgo的证明者时间在所有方案中最快，至少快一个数量级，验证时间也仅逊于Stark，但其在Mersenne素数域上的运算比Stark在$\mathbb{F}_{2^{64}}$上的SHA-256电路兼容性更好。证明大小为253KB（Merkle树256叶子），与其他基于IOP的方案相当，但远大于Libra (90KB)，这主要是由于Merkle树打开的开销。

### 局限性与开放问题
Virgo的一个主要局限在于其证明大小，相比Libra等基于配对的技术大约高出一个数量级，这是因为IOP结构需要多次Merkle树打开。未来工作可以探索使用具有恒定大小证明的向量承诺方案来改善，但这可能以牺牲证明者时间为代价。此外，方案的简洁验证仅限于具有规则拓扑结构的电路，对于不规则电路，验证者需要线性时间读取电路描述。虽然随机访问内存程序可以通过规约转化为规则电路，但这种转换可能引入额外开销。最后，尽管实现已经很高效，但将系统扩展到处理数十亿门电路的大规模应用时，内存和计算的规模仍是一个挑战。

### 强关联论文

[42] Goldwasser, S., Kalai, Y. T., Rothblum, G. N. Delegating Computation: Interactive Proofs for Muggles. **J. ACM 2015** [Google Scholar](https://scholar.google.com/scholar?q=Delegating+Computation:+Interactive+Proofs+for+Muggles)

[70] Xie, T., Zhang, J., Zhang, Y., Papamanthou, C., Song, D. Libra: Succinct Zero-Knowledge Proofs with Optimal Prover Computation. **CRYPTO 2019** [Google Scholar](https://scholar.google.com/scholar?q=Libra:+Succinct+Zero-Knowledge+Proofs+with+Optimal+Prover+Computation)

[14] Ben-Sasson, E., Chiesa, A., Riabzev, M., Spooner, N., Virza, M., Ward, N. P. Aurora: Transparent Succinct Arguments for R1CS. **ePrint 2018** [Google Scholar](https://scholar.google.com/scholar?q=Aurora:+Transparent+Succinct+Arguments+for+R1CS)

[69] Wahby, R. S., Tzialla, I., Shelat, A., Thaler, J., Walfish, M. Doubly-Efficient zkSNARKs without Trusted Setup. **IEEE S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Doubly-Efficient+zkSNARKs+without+Trusted+Setup)

[72] Zhang, Y., Genkin, D., Katz, J., Papadopoulos, D., Papamanthou, C. A Zero-Knowledge version of vSQL. **ePrint 2017** [Google Scholar](https://scholar.google.com/scholar?q=A+Zero-Knowledge+version+of+vSQL)

[5] Ames, S., Hazay, C., Ishai, Y., Venkitasubramaniam, M. Ligero: Lightweight Sublinear Arguments without a Trusted Setup. **CCS 2017** [Google Scholar](https://scholar.google.com/scholar?q=Ligero:+Lightweight+Sublinear+Arguments+without+a+Trusted+Setup)

[73] Zhang, Y., Genkin, D., Katz, J., Papadopoulos, D., Papamanthou, C. vSQL: Verifying arbitrary SQL queries over dynamic outsourced databases. **IEEE S&P 2017** [Google Scholar](https://scholar.google.com/scholar?q=vSQL:+Verifying+arbitrary+SQL+queries+over+dynamic+outsourced+databases)


## 关键词

+ 透明零知识证明
+ 可验证多项式委托
+ 分层算术电路
+ Virgo证明系统
+ 无可信设置
+ 后量子安全