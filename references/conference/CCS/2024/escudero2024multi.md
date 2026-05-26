---
title: "Multi-Verifier Zero-Knowledge Proofs for Any Constant Fraction of Corrupted Verifiers"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2024
modified: 2025-04-21 08:47:11
created: 2025-04-09 16:01:44
---

## Multi-Verifier Zero-Knowledge Proofs for Any Constant Fraction of Corrupted Verifiers

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3658644.3670357)

## 作者

+ Daniel Escudero
+ Antigoni Polychroniadou
+ Yifan Song
+ [Chenkai Weng](Chenkai%20Weng.md)

## 笔记

### 背景与动机
零知识证明（ZK）允许证明者向验证者证明陈述的真实性而不泄露额外信息。非交互式ZK（NIZK）虽已广泛部署，但其证明生成的内存开销随电路规模线性增长，难以在 commodity 硬件上运行亿级门电路。相反，指定验证者ZK（DVZK）通过常数轮交互实现流式处理，内存开销稳定（数百MB到数GB），但只支持单个验证者，不适合需要向多个验证者证明的场景（如私有聚合、区块链预言机）。多验证者ZK（MVZK）应运而生，它结合了交互式ZK的高效性和多验证者的灵活部署。然而，现有MVZK方案[5,7,48]要么只支持诚实多数（腐败验证者少于一半），要么假设最坏情况——除一个验证者外全部腐败[50]，这在实际中过于极端。本文旨在填补这一空白：支持任意常数比例（例如20%、40%）的腐败验证者（包括与证明者共谋），同时保持通信复杂度与验证者数量无关（仅取决于电路大小和诚实比例）。这是首个在环（如$\mathbb{Z}_{2^k}$）上实现的MVZK方案，并提供了端到端实现。

### 相关工作

[5] Applebaum 等. Verifiable Relation Sharing and Multi-verifier Zero-Knowledge in Two Rounds. **EUROCRYPT 2022** [Google Scholar](https://scholar.google.com/scholar?q=Verifiable+Relation+Sharing+and+Multi-verifier+Zero-Knowledge+in+Two+Rounds)
> 核心思路：基于“Minicrypt”假设实现轮数最优的MVZK，支持诚实多数。
> 局限与区别：仅支持$t<n/2$，通信复杂度$\Omega(n|C|)$；本文支持任意常数比例且通信与$n$无关。

[7] Baum 等. Feta: Efficient Threshold Designated-Verifier Zero-Knowledge Proofs. **CCS 2022** [Google Scholar](https://scholar.google.com/scholar?q=Feta%3A+Efficient+Threshold+Designated-Verifier+Zero-Knowledge+Proofs)
> 核心思路：基于秘密共享的MVZK，支持$t<n/3$或$t<n/4$。
> 局限与区别：通信复杂度$O(n|C|)$，只支持诚实多数；本文通信$O(|C|)$独立于$n$，且可容忍更高腐败率。

[48] Yang 和 Wang. Non-interactive Zero-Knowledge Proofs to Multiple Verifiers. **ASIACRYPT 2022** [Google Scholar](https://scholar.google.com/scholar?q=Non-interactive+Zero-Knowledge+Proofs+to+Multiple+Verifiers)
> 核心思路：基于打包Shamir秘密共享的MVZK，支持$t<n(1/2-\gamma)$，通信$O(|C|)$。
> 局限与区别：仅在诚实多数（$\epsilon>1/2$）时有效，且常数因子大于本文；本文可覆盖$\epsilon\in(0,1)$且常数更优。

[50] Zhou 等. Practical Constructions for Single Input Functionality against a Dishonest Majority. **ePrint 2023** [Google Scholar](https://scholar.google.com/scholar?q=Practical+Constructions+for+Single+Input+Functionality+against+a+Dishonest+Majority)
> 核心思路：基于同态加密和BDOZ预处理的MVZK，支持$t=n-1$。
> 局限与区别：通信复杂度$O(n|C|)$，计算成本高（需HE和NIZK）；本文通信$O(|C|/\epsilon)$，依赖VOLE，性能高三个量级。

[20] Corrigan-Gibbs 和 Boneh. Prio: Private, Robust, and Scalable Computation of Aggregate Statistics. **NSDI 2017** [Google Scholar](https://scholar.google.com/scholar?q=Prio%3A+Private%2C+Robust%2C+and+Scalable+Computation+of+Aggregate+Statistics)
> 核心思路：秘密共享非交互式证明（SNIP）用于聚合统计数据，假设证明者不与验证者共谋。
> 局限与区别：不支持证明者-验证者共谋；本文可容忍共谋且通信仅$O(|C|)$，而Prio在共谋下通信$O(n|C|)$。

[39] Rachuri 和 Scholl. Le Mans: Dynamic and Fluid MPC for Dishonest Majority. **CRYPTO 2022** [Google Scholar](https://scholar.google.com/scholar?q=Le+Mans%3A+Dynamic+and+Fluid+MPC+for+Dishonest+Majority)
> 核心思路：提出可编程VOLE（$\mathcal{F}_{\text{VOLE}}^\text{prog}$），支持短种子扩展，用于高效生成随机相关。
> 局限与区别：仅两方；本文将其扩展为多方VOLE（$\mathcal{F}_{\text{nVOLE}}$），并用于生成打包秘密共享。

[25] Escudero 等. SuperPack: Dishonest Majority MPC with Constant Online Communication. **CRYPTO 2023** [Google Scholar](https://scholar.google.com/scholar?q=SuperPack%3A+Dishonest+Majority+MPC+with+Constant+Online+Communication)
> 核心思路：利用packed Shamir秘密共享实现常数轮在线MPC，支持$t=n(1-\epsilon)$。
> 局限与区别：面向MPC，非ZK；本文借鉴其packed SS转换技术，并扩展至MVZK场景（需MAC检查）。

[13] Boneh 等. Zero-Knowledge Proofs on Secret-Shared Data via Fully Linear PCPs. **CRYPTO 2019** [Google Scholar](https://scholar.google.com/scholar?q=Zero-Knowledge+Proofs+on+Secret-Shared+Data+via+Fully+Linear+PCPs)
> 核心思路：提出基于全线性PCP的分布式ZK，用于秘密共享数据上的证明。
> 局限与区别：专注于多服务器场景，非MVZK；本文的递归验证受其启发，但使用VOLE实现更高效的共享。

[47] Yang 等. QuickSilver: Efficient and Affordable Zero-Knowledge Proofs for Circuits and Polynomials over Any Field. **CCS 2021** [Google Scholar](https://scholar.google.com/scholar?q=QuickSilver%3A+Efficient+and+Affordable+Zero-Knowledge+Proofs+for+Circuits+and+Polynomials+over+Any+Field)
> 核心思路：单验证者VOLE-ZK，高吞吐量，低内存。
> 局限与区别：仅支持单验证者；本文将其扩展为多验证者，且性能相近（表4显示MVZK比顺序执行25次快3.3-4.4倍）。

### 核心技术与方案

#### 整体框架
本文遵循“秘密共享+乘法门检查”范式。证明者$\mathcal{P}$将电路每条输入线和乘法门输出线的值以**认证加法共享**（IT-MAC）的形式分发给$n$个验证者，其中共享格式为$[\![x]\!]=(\langle x\rangle,\langle x\cdot\Delta\rangle,\langle\Delta\rangle)$，$\Delta$为全局MAC密钥。验证者利用线性性本地计算加法门输出，然后通过递归压缩协议验证所有乘法关系的正确性。系统分为两阶段：预处理（与见证无关）和在线（见证相关）。

#### 预处理阶段：多方VOLE与打包秘密共享
核心基础设施是**可编程多方VOLE**（$\mathcal{F}_{\text{nVOLE}}$），它允许$\mathcal{P}$选择短种子，每个验证者$\mathcal{V}_i$持有向量$\boldsymbol{u}^i$和局部密钥$\Delta^i$，使得对所有$i\neq j$有$\boldsymbol{w}_j^i=\boldsymbol{u}^i\cdot\Delta^j+\boldsymbol{v}_i^j$。通过定义$\boldsymbol{u}=\sum_i\boldsymbol{u}^i$和$\Delta=\sum_i\Delta^i$，这些三元组构成认证共享$[\![u]\!]$。关键是，$\mathcal{P}$知道所有种子，因此可本地计算$\boldsymbol{u}$的所有秘密值（未认证）。为减少分发开销，本文利用SuperPack [25]的思想：将$(\boldsymbol{u}^1,\dots,\boldsymbol{u}^n)$重新解释为**包（packed）Shamir秘密共享**$[\boldsymbol{r}]_{n-1}$，其中$\boldsymbol{r}\in\mathcal{K}^\sigma$，$\sigma=n-t$为诚实验证者数（$\sigma=\epsilon n$）。通过Lagrange插值，验证者可本地将$[\boldsymbol{r}]_{n-1}$转换为$\sigma$个加法共享$\langle r_j\rangle$，并利用VOLE相关消息计算$\langle r_j\cdot\Delta\rangle$，从而得到$[\![r_j]\!]$。预处理阶段还要求各验证者分享其$\Delta^i$的Galois环分量，得到$[\Delta_\ell|_j]_t$（标准Shamir共享），用于后续MAC计算。

#### 在线阶段：分发扩展见证
对于每组$\sigma\cdot d$条电路线（$d$为Galois环扩展度），$\mathcal{P}$从预处理获得随机认证共享$[\![r_{i,j}]\!]$，计算差值$\lambda_{i,j}=v_{i,j}-r_{i,j}$，将它们视为$\sigma$个Galois环元素$(\lambda_1,\dots,\lambda_\sigma)$，并构造degree-$(\sigma-1)$的packed Shamir共享$[D]_{\sigma-1}$，分发给各验证者。验证者本地将$[D]_{\sigma-1}$转换为加法共享$\langle\lambda_{i,j}\rangle$。为计算MAC，验证者计算$[D]_{\sigma-1}\cdot[\Delta_\ell|_i]_t$，得到degree-$(n-1)$共享，其第$i$个秘密位置含$\lambda_{i,j}\cdot\Delta_\ell$，再通过解包获得$\langle\lambda_{i,j}\cdot\Delta_\ell\rangle$，对所有$\ell\in[d]$求和得到$\langle\lambda_{i,j}\cdot\Delta\rangle$。最后加上$\langle r_{i,j}\cdot\Delta\rangle$即获得$[\![v_{i,j}]\!]$。该过程总通信为$(|C|/\sigma)\cdot n = |C|/\epsilon$，独立于$n$。

#### 在线阶段：递归乘法验证
验证者获得所有线的认证共享后，需验证每个乘法门$w_\gamma = w_\alpha\cdot w_\beta$。本文采用递归压缩协议（类似[48]），将$N=|C|$个乘法测试聚合成单个多项式测试。步骤如下：首先证明者发送随机掩码以创建“辅助”乘法关系，然后所有参与者使用Schwartz-Zippel引理在随机点$\eta$处检查多项式等式。具体地，将$N$个组$(x_i,y_i,z_i)$扩充到$m\cdot\ell$维，通过多次调用$\pi_{\text{VerifyIPProc}}$（图3）将维度从$m\ell$压缩到$\ell$，每次压缩使用$m-1$个随机认证值，最后调用$\pi_{\text{VerifyIPFinal}}$将$\ell$维降至1个乘法三元组$(a,b,c)$。验证者通过承诺和打开检查$c=a\cdot b$。该过程总通信为$O(n\cdot\text{polylog}|C|)$（验证者间交互），证明者发送的额外信息（随机掩码）数量为$c=2\nu(m-1)+4$，其中$\nu=\lceil\log_m N\rceil$，远小于$|C|$。

#### 安全性
协议在$\mathcal{F}_{\text{nVOLE}}$、$\mathcal{F}_{\text{Commit}}$和随机预言机模型下，针对恶意敌手（可腐败$\mathcal{P}$和至多$t=n(1-\epsilon)$个验证者）安全实现功能$\mathcal{F}_{\text{ZK}}$。证明依赖于：若$\mathcal{P}$诚实，则扩展函数为PRG保证种子均匀；若$\mathcal{P}$腐败，则$\Delta$保持机密，MAC检查可检测任何篡改。递归验证基于Schwartz-Zippel引理，错误概率$\leq m/|\mathcal{K}|\leq \text{negl}(\kappa)$。

### 核心公式与流程

**[多方VOLE的一致性检查方程]**
$$
\sum_{i_1=1}^n \sum_{i_2 \neq i_1} \left(L_{i_2}(\beta_j) v_{i_2,\ell}^{i_1} - L_{i_1}(\beta_j) w_{i_2,\ell}^{i_1}\right) = \Delta \cdot r_{\ell,j} - \sum_{i_1=1}^n L_{i_1}(\beta_j) u_{\ell}^{i_1} \Delta^{i_1}.
$$
> 作用：验证者利用VOLE相关项本地计算加法共享$\langle r_{\ell,j}\cdot\Delta\rangle$，正确性依赖于三元组关系$w_{j,\ell}^i = u_\ell^i \cdot \Delta^j + v_{i,\ell}^j$。

**[在线阶段：从packed Shamir共享获取MAC]**
$$
[\![v_{i,j}]\!] = [\![r_{i,j}]\!] + [\!\lambda_{i,j}\!], \quad \text{其中 }\langle\lambda_{i,j}\cdot\Delta\rangle = \sum_{\ell=1}^d \langle\lambda_{i,j}\cdot\Delta_\ell\rangle.
$$
> 作用：证明者发送$[D]_{\sigma-1}$后，验证者本地计算差值$\lambda$的MAC，再与随机值$r$的MAC相加，得到实际线值的认证共享。

**[递归验证的压缩步骤]**
$$
\left(\llbracket f_1(\cdot)\rrbracket,\dots,\llbracket f_\ell(\cdot)\rrbracket\right), \left(\llbracket g_1(\cdot)\rrbracket,\dots,\llbracket g_\ell(\cdot)\rrbracket\right)
$$
插值多项式，满足$f_i(j)=\boldsymbol{x}_j[i], g_i(j)=\boldsymbol{y}_j[i]$ for $j\in[m]$, 然后随机挑战$\eta\leftarrow H(\dots)$，输出$a_i=f_i(\eta), b_i=g_i(\eta)$。
> 作用：通过多项式插值和随机挑战，将$m\ell$个内积测试压缩为$\ell$个，通信仅$O(m)$个认证值。

### 实验结果

实验在AWS EC2 c5.metal（96 vCPU, 192 GiB RAM）上进行，使用NTT友好域$p=2^{59}-2^{28}+1$，模拟1Gbps网络。核心性能：对于64个验证者、50%诚实比例（$\sigma/n=0.5$），吞吐量达1.47M gates/s；对于75%腐败（$\sigma/n=0.25$），吞吐量为0.88M gates/s；对于87.5%腐败（$\sigma/n=0.125$），仍可达0.49M gates/s。当固定诚实比例时，吞吐量几乎不随验证者数增长而下降（例如$\sigma/n=0.5$时，从4个到64个验证者吞吐量稳定在1.4-1.6M gates/s）。网络延迟对性能影响极小（2ms vs 60ms延迟时吞吐量仅从0.83M略降至0.80M gates/s）。矩阵乘法证明实验（表4）表明，内存开销几乎恒定：证明者约2.7GB，每个验证者约5.7GB，不随电路增长（从$512^3$到$1280^3$门）。与单验证者方案Quicksilver [47]相比，向25个验证者证明时，本文MVZK比顺序执行Quicksilver快3.3-4.4倍。与之前MVZK [7]相比，本文在8个验证者、50%腐败下吞吐量1.59M gates/s，而[7]在7个验证者、33%腐败下约为3M gates/s（小域），但本文在大域下通信更优（32×减少）。与Zhou等[50]相比，本文预估快两个量级以上（[50]吞吐量约0.03M gates/s）。

### 局限性与开放问题
本文依赖可编程VOLE的LPN假设，尽管该假设在密码学中标准，但量子安全性尚不明确。实际部署中，VOLE的预处理阶段仍需要计算开销，本文未包含其微基准。尽管本文声称支持环（$\mathbb{Z}_{2^k}$），但实现仅针对大有限域$p=2^{59}-2^{28}+1$，环上的端到端性能未报告。此外，递归验证中使用的随机预言机在标准模型中可替换为Collision-Resistant Hash，但具体安全性需进一步分析。未来可探索：在诚实多数场景下，是否可通过轻量级IFIOP替代VOLE以获得更好的常数；以及如何将打包秘密共享与更高效的内存释放策略结合，以支持超过$2^{30}$门的电路。

### 强关联论文

[5] Benny Applebaum, Eliran Kachlon, and Arpita Patra. Verifiable Relation Sharing and Multi-verifier Zero-Knowledge in Two Rounds: Trading NIZKs with Honest Majority. **EUROCRYPT 2022** [Google Scholar](https://scholar.google.com/scholar?q=Verifiable+Relation+Sharing+and+Multi-verifier+Zero-Knowledge+in+Two+Rounds)

[7] Carsten Baum, Robin Jadoul, Emmanuela Orsini, Peter Scholl, and Nigel P. Smart. Feta: Efficient Threshold Designated-Verifier Zero-Knowledge Proofs. **CCS 2022** [Google Scholar](https://scholar.google.com/scholar?q=Feta%3A+Efficient+Threshold+Designated-Verifier+Zero-Knowledge+Proofs)

[48] Kang Yang and Xiao Wang. Non-interactive Zero-Knowledge Proofs to Multiple Verifiers. **ASIACRYPT 2022** [Google Scholar](https://scholar.google.com/scholar?q=Non-interactive+Zero-Knowledge+Proofs+to+Multiple+Verifiers)

[50] Zhelei Zhou, Bingsheng Zhang, Hong-Sheng Zhou, and Kui Ren. Practical Constructions for Single Input Functionality against a Dishonest Majority. **ePrint 2023** [Google Scholar](https://scholar.google.com/scholar?q=Practical+Constructions+for+Single+Input+Functionality+against+a+Dishonest+Majority)

[20] Henry Corrigan-Gibbs and Dan Boneh. Prio: Private, Robust, and Scalable Computation of Aggregate Statistics. **NSDI 2017** [Google Scholar](https://scholar.google.com/scholar?q=Prio%3A+Private%2C+Robust%2C+and+Scalable+Computation+of+Aggregate+Statistics)

[39] Rahul Rachuri and Peter Scholl. Le Mans: Dynamic and Fluid MPC for Dishonest Majority. **CRYPTO 2022** [Google Scholar](https://scholar.google.com/scholar?q=Le+Mans%3A+Dynamic+and+Fluid+MPC+for+Dishonest+Majority)

[25] Daniel Escudero, Vipul Goyal, Antigoni Polychroniadou, Yifan Song, and Chenkai Weng. SuperPack: Dishonest Majority MPC with Constant Online Communication. **CRYPTO 2023** [Google Scholar](https://scholar.google.com/scholar?q=SuperPack%3A+Dishonest+Majority+MPC+with+Constant+Online+Communication)

[13] Dan Boneh, Elette Boyle, Henry Corrigan-Gibbs, Niv Gilboa, and Yuval Ishai. Zero-Knowledge Proofs on Secret-Shared Data via Fully Linear PCPs. **CRYPTO 2019** [Google Scholar](https://scholar.google.com/scholar?q=Zero-Knowledge+Proofs+on+Secret-Shared+Data+via+Fully+Linear+PCPs)

[47] Kang Yang, Pratik Sarkar, Chenkai Weng, and Xiao Wang. QuickSilver: Efficient and Affordable Zero-Knowledge Proofs for Circuits and Polynomials over Any Field. **CCS 2021** [Google Scholar](https://scholar.google.com/scholar?q=QuickSilver%3A+Efficient+and+Affordable+Zero-Knowledge+Proofs+for+Circuits+and+Polynomials+over+Any+Field)

[6] Carsten Baum, Lennart Braun, Cyprien Delpech de Saint Guilhem, Michael Klooß, Emmanuela Orsini, Lawrence Roy, and Peter Scholl. Publicly Verifiable Zero-Knowledge and Post-Quantum Signatures from VOLE-in-the-Head. **CRYPTO 2023** [Google Scholar](https://scholar.google.com/scholar?q=Publicly+Verifiable+Zero-Knowledge+and+Post-Quantum+Signatures+from+VOLE-in-the-Head)


## 关键词

+ 多验证者零知识证明
+ 预处理模型
+ 通信复杂度
+ 腐败验证者
+ 环上零知识证明
+ 可扩展性