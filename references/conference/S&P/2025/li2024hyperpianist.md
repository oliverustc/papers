---
title: "HyperPianist: Pianist with Linear-Time Prover and Logarithmic Communication Cost"
doi: 10.1109/sp61157.2025.00202
标题简称: HyperPianist
论文类型: conference
会议简称: S&P
发表年份: 2025
modified: 2025-04-20 23:33:42
created: 2025-04-07 16:55:23
---
## HyperPianist: Pianist with Linear-Time Prover and Logarithmic Communication Cost

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/11023268/)
+ [archive](https://eprint.iacr.org/2024/1273)

## 作者

+ Chongrong Li
+ Pengfei Zhu
+ Yun Li
+ Cheng Hong
+ Wenjie Qu
+ [Jiaheng Zhang](Jiaheng%20Zhang.md)

## 笔记

### 背景与动机
零知识证明是密码学的核心工具，允许证明者向验证者证明某个陈述为真而不泄露额外信息。近年来，零知识简洁非交互式知识参数（zkSNARKs）因其证明短小且验证快速而备受关注。Plonk和Marlin等系统采用多项式交互式预言机证明（PIOP）与多项式承诺方案（PCS）的架构，已在区块链中取得广泛应用。然而，高额的证明者成本限制了这些方案在大规模电路上的应用。Wu等人于2018年提出DIZK [6]，将证明任务分布到多台机器上极大缩短了证明时间，但其基于Groth16，每个子证明者因子多项式插值而运行在准线性时间，且通信成本与电路规模呈线性关系。后续的deVirgo [8]采用多变量多项式，但多变量PCS仍需多项式插值且通信成本线性。Pianist [9]基于Plonk实现了常数级通信成本，但证明者时间仍为准线性。HyperPlonk [13]通过多变量PIOP实现了线性证明时间，但并未分布式化。因此，设计一个既拥有线性证明时间又具备对数通信成本的分布式ZKP系统成为关键空白，本文正是填补这一空白。

### 相关工作

[2] Gabizon et al. PLONK: Permutations over Lagrange-bases for Oecumenical Noninteractive Arguments of Knowledge. **EUROCRYPT 2019** [Google Scholar](https://scholar.google.com/scholar?q=PLONK+Permutations+over+Lagrange-bases+for+Oecumenical+Noninteractive+Arguments+of+Knowledge)
> 核心思路：使用单变量约束系统和排列检查实现通用可更新参考字符串的zkSNARK。
> 局限与区别：证明者成本为准线性，不适用于大规模电路；本文基于其约束系统但采用多变量PIOP实现线性时间。

[9] Liu et al. Pianist: Scalable zkRollups via Fully Distributed Zero-Knowledge Proofs. **IEEE S&P 2024** [Google Scholar](https://scholar.google.com/scholar?q=Pianist+Scalable+zkRollups+via+Fully+Distributed+Zero-Knowledge+Proofs)
> 核心思路：使用双变量PIOP和双变量KZG承诺实现分布式ZKP，通信成本常数。
> 局限与区别：证明者成本仍为准线性，且在通用电路上产生额外开销；本文采用多变量PIOP消除这些开销。

[13] Chen et al. HyperPlonk: Plonk with Linear-Time Prover and High-Degree Custom Gates. **EUROCRYPT 2023** [Google Scholar](https://scholar.google.com/scholar?q=HyperPlonk+Plonk+with+Linear-Time+Prover+and+High-Degree+Custom+Gates)
> 核心思路：将Plonk的单变量PIOP改为多变量，结合线性时间多变量PCS实现线性证明者。
> 局限与区别：本身为单机系统，未考虑分布式场景；本文将其PIOP系统分布式化并解决多集检查的分布难题。

[8] Xie et al. zkBridge: Trustless Cross-Chain Bridges Made Practical. **ACM CCS 2022** [Google Scholar](https://scholar.google.com/scholar?q=zkBridge+Trustless+Cross-Chain+Bridges+Made+Practical)
> 核心思路：提出deVirgo，面向数据并行电路的分布式多变量PIOP系统，基于FRI的PCS。
> 局限与区别：FRI需要线性通信成本且证明时间准线性；本文采用加性同态PCS实现对数通信。

[6] Wu et al. DIZK: A Distributed Zero Knowledge Proof System. **USENIX Security 2018** [Google Scholar](https://scholar.google.com/scholar?q=DIZK+A+Distributed+Zero+Knowledge+Proof+System)
> 核心思路：第一个将Groth16证明分布到多台机器的系统。
> 局限与区别：准线性证明者时间，线性通信成本；本文实现线性时间和对数通信。

[14] Setty et al. Quarks: Quadruple-efficient transparent zk-SNARKs. **Cryptology ePrint 2020** [Google Scholar](https://scholar.google.com/scholar?q=Quarks+Quadruple-efficient+transparent+zk-SNARKs)
> 核心思路：引入了乘积检查PIOP用于多集检查。
> 局限与区别：其辅助多项式在分布式环境中构造需要线性通信；本文采用对数导数技术避免此问题。

[18] Setty et al. Unlocking the Lookup Singularity with Lasso. **EUROCRYPT 2024** [Google Scholar](https://scholar.google.com/scholar?q=Unlocking+the+Lookup+Singularity+with+Lasso)
> 核心思路：基于多变量多项式的最高效查找参数，利用离线内存检查进行良构性验证。
> 局限与区别：良构性检查的证明者成本较高；本文优化了该检查，减少约50%的承诺和30%的SumCheck代价。

[17] Lee. Dory: Efficient, Transparent Arguments for Generalised Inner Products and Polynomial Commitments. **TCC 2021** [Google Scholar](https://scholar.google.com/scholar?q=Dory+Efficient+Transparent+Arguments+for+Generalised+Inner+Products+and+Polynomial+Commitments)
> 核心思路：基于内积论证的无设置多变量PCS。
> 局限与区别：直接分布会导致通信成本高；本文通过对角矩阵重排实现分布式版本。

### 核心技术与方案
本文提出HyperPianist，一个分布式ZKP系统，核心贡献包括一个分布友好的多变量PIOP系统和两个分布式多变量PCS方案。

分布式PIOP系统基于HyperPlonk的Plonkish约束系统，将电路约束分解为门恒等式和布线恒等式（即复制约束）。分布式SumCheck PIOP是基础，它将单机SumCheck协议扩展：每个子证明者 $\mathcal{P}_i$ 持有部分多项式 $f^{(i)}(\boldsymbol{x}) = f(\boldsymbol{x}, \boldsymbol{bin}(i))$ ，在每个轮次k中，子证明者本地计算一个单变量多项式 $f_k^{(i)}(X_k)$ 并发送给主证明者 $\mathcal{P}_0$ ，由 $\mathcal{P}_0$ 聚合后与验证者交互。关键创新在于分布式多集检查PIOP，它避免了Pianist中的线性通信。HyperPlonk将多集检查归约为乘积检查，需构造辅助多项式h，在分布式下子证明者无法本地构造h，需通信交换。HyperPianist采用对数导数技术[15]，将多集检查归约为有理SumCheck（RSumCheck）关系：给定挑战β, γ，证明 $\sum_{\boldsymbol{x} \in \{0,1\}^n} \frac{p(\boldsymbol{x})}{q(\boldsymbol{x})}=v$ 。该检查分为两步：首先证明辅助多项式 $f(\boldsymbol{x})=1/q(\boldsymbol{x})$ 满足 $f\cdot q - 1$ 在超立方体上处处为零（分布式ZeroCheck），然后证明 $\sum p\cdot f = v$ （分布式SumCheck）。此过程每个子证明者可在本地计算f，无需通信，从而实现分布友好。

对于分布式PCS，HyperPianist提供了两种选择。deMKZG是多变量KZG[16]的分布式版本，利用承诺的加性同态性：每个子证明者计算部分承诺并发送给主证明者聚合，打开时也类似地在本地计算部分商多项式。deDory基于Dory[17]设计，需要特殊的矩阵重组以避免朴素的 $O(2^{n/2})$ 通信。具体而言，将子证明者的子多项式表示为对角块矩阵，从而允许本地内积论证降阶，将通信从 $O(2^{n/2})$ 降至 $O(n)$ ，但证明大小从 $O(n)$ 增至 $O(n+m)$ 。

HyperPianist+进一步优化了基于Lasso[18]的查找参数。Lasso需通过离线内存检查验证多项式 $E_j$ 的良构性，本文利用对数导数将集合包含关系归约为有理SumCheck，从而减少约50%的承诺和30%的SumCheck代价。

协议的安全证明基于，在随机挑战下错误成立的极小概率。系统渐进复杂度在表3和表1中给出：子证明者时间 $O(2^{n-m})$ 域操作，主证明者额外 $O(n\cdot 2^m)$ ，通信每人 $O(n)$ 域或群元素。

### 核心公式与流程

**分布式SumCheck PIOP：子证明者本地多项式定义**
$$f_k^{(i)}(X_k) := \sum_{\boldsymbol{x} \in \{0,1\}^{n-m-k}} f(r_1, \ldots, r_{k-1}, X_k, \boldsymbol{x}, \boldsymbol{bin}(i))$$
> 作用：第i个子证明者在第k轮计算其持有的部分多项式，随后发送给主证明者求和。

**多集检查到有理SumCheck的归约（定理2）**
$$\prod_{i=1}^n (a_i+X) = \prod_{i=1}^n (b_i+X) \iff \sum_{i=1}^n \frac{1}{a_i+X} = \sum_{i=1}^n \frac{1}{b_i+X}$$
> 作用：将对数导数技巧应用于多集检查，将乘积检查转化为有理SumCheck，从而避免构造辅助多项式h。

**Lasso良构性检查的集合包含归约（定理7）**
$$\sum_{\boldsymbol{x} \in \{0,1\}^{\log \ell}} \frac{1}{nz_j(\boldsymbol{x}) + \gamma\cdot E_j(\boldsymbol{x}) + \beta} = \sum_{\boldsymbol{x} \in \{0,1\}^{\log N}} \frac{m(\boldsymbol{x})}{s_{id}(\boldsymbol{x}) + \gamma\cdot T(\boldsymbol{x}) + \beta}$$
> 作用：使用对数导数技术将Lasso的良构性检查归约为有理SumCheck，减少承诺和SumCheck工作量。

**deDory的矩阵对角化重组（定理5）**
$$\hat{\boldsymbol{L}} = \left[E_0\cdot \boldsymbol{L}, \ldots, E_{2^m-1}\cdot \boldsymbol{L}\right] = \boldsymbol{E}\otimes \boldsymbol{L},\quad \hat{\boldsymbol{R}} = \left[\boldsymbol{R}, \ldots, \boldsymbol{R}\right] = \otimes_{k\in[2^m]}(1,1)\otimes \boldsymbol{R}$$
> 作用：将子证明者的子矩阵以对角形式排列，使得内积论证可本地进行，通信从 $O(2^{n/2})$ 降至 $O(n)$。

### 实验结果
实验在Aliyun ecs.r8i.8xlarge实例（32 vCPU, 256GB内存）与局域网中进行。HyperPianist展示了线性可扩展性：对于 $2^{26}$ 规模的乘法门电路，单机HyperPlonk需261.2秒， 2台机器上HyperPianistKPIOP降至58.0秒（加速4.5倍），32台机器降至4.1秒（加速63.1倍）。与Pianist对比，8台机器上对于 $2^{26}$ 规模电路，HyperPianistKPIOP在乘法门上加速2.9倍，在定制门（5次门）上加速4.6倍；HyperPianistDPIOP分别加速2.4倍和3.8倍。分层电路版本（layered circuit）表现更优，HyperPianistKLC在定制门上可达5.9倍加速。通信开销合理：HyperPianistKPIOP每人通信小于26.3KB，证明大小12.5KB，验证者时间小于4ms。查找参数方面，在非分布式设置下， $2^{24}$ 规模XOR门比较中，本文方案证明时间30.2秒，Lasso需57.9秒，加速约2倍；证明大小与验证者时间接近。

### 局限性与开放问题
本文方案中deMKZG需要可信设置，而deDory无设置但证明大小和验证时间随机器数m线性增长。对于极大规模电路（如 $2^{40}$ ），对数级通信虽好，但主证明者的额外 $O(n\cdot 2^m)$ 计算可能成为瓶颈。查找参数优化虽好，但当前仅适用于结构化表，通用表的分布化查找仍有待研究。

### 强关联论文

[2] Gabizon et al. PLONK: Permutations over Lagrange-bases for Oecumenical Noninteractive Arguments of Knowledge. **EUROCRYPT 2019** [Google Scholar](https://scholar.google.com/scholar?q=PLONK+Permutations+over+Lagrange-bases+for+Oecumenical+Noninteractive+Arguments+of+Knowledge)

[9] Liu et al. Pianist: Scalable zkRollups via Fully Distributed Zero-Knowledge Proofs. **IEEE S&P 2024** [Google Scholar](https://scholar.google.com/scholar?q=Pianist+Scalable+zkRollups+via+Fully+Distributed+Zero-Knowledge+Proofs)

[13] Chen et al. HyperPlonk: Plonk with Linear-Time Prover and High-Degree Custom Gates. **EUROCRYPT 2023** [Google Scholar](https://scholar.google.com/scholar?q=HyperPlonk+Plonk+with+Linear-Time+Prover+and+High-Degree+Custom+Gates)

[8] Xie et al. zkBridge: Trustless Cross-Chain Bridges Made Practical. **ACM CCS 2022** [Google Scholar](https://scholar.google.com/scholar?q=zkBridge+Trustless+Cross-Chain+Bridges+Made+Practical)

[6] Wu et al. DIZK: A Distributed Zero Knowledge Proof System. **USENIX Security 2018** [Google Scholar](https://scholar.google.com/scholar?q=DIZK+A+Distributed+Zero+Knowledge+Proof+System)

[14] Setty et al. Quarks: Quadruple-efficient transparent zk-SNARKs. **Cryptology ePrint 2020** [Google Scholar](https://scholar.google.com/scholar?q=Quarks+Quadruple-efficient+transparent+zk-SNARKs)

[18] Setty et al. Unlocking the Lookup Singularity with Lasso. **EUROCRYPT 2024** [Google Scholar](https://scholar.google.com/scholar?q=Unlocking+the+Lookup+Singularity+with+Lasso)

[17] Lee. Dory: Efficient, Transparent Arguments for Generalised Inner Products and Polynomial Commitments. **TCC 2021** [Google Scholar](https://scholar.google.com/scholar?q=Dory+Efficient+Transparent+Arguments+for+Generalised+Inner+Products+and+Polynomial+Commitments)


## 关键词

+ 分布式多变量零知识证明
+ 线性时间证明者
+ 对数通信成本
+ HyperPlonk多变量PIOP
+ 多变量KZG多项式承诺
+ 无信任设置zkSNARK