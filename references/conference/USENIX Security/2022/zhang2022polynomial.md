---
title: "Polynomial Commitment with a One-to-Many Prover and Applications"
标题简称:
论文类型: conference
会议简称: USENIX Security
发表年份: 2022

modified: 2025-04-21 00:28:11
created: 2025-04-07 16:59:47
---

## Polynomial Commitment with a One-to-Many Prover and Applications

## 发表信息

+ [原文链接](https://www.usenix.org/conference/usenixsecurity22/presentation/zhang-jiaheng)

## 作者

+ [Jiaheng Zhang](Jiaheng%20Zhang.md)
+ [Tiancheng Xie](Tiancheng%20Xie.md)
+ Thang Hoang
+ [Elaine Shi](Elaine%20Shi.md)
+ [Yupeng Zhang](Yupeng%20Zhang.md)

## 笔记

### 背景与动机
可验证秘密共享（VSS）是分布式密码学的基础构件，广泛用于多方计算、门限密码系统和去中心化区块链应用。构建VSS最实用的方法之一是通过多项式承诺方案：一个经销商（即证明者）向一个随机多项式做出承诺，该多项式的零次项系数即为要共享的秘密，随后它需要向N个不同的验证者分别证明该多项式在各自指定点上的取值。这种场景要求多项式承诺以“一对多”的方式工作。Tomescu等人于IEEE S&P 2020提出的方案 [35] 首次引入了“一对多证明者批处理”技术，使得证明者可以在产生N个不同点上的证明时仅付出接近常数的开销，但该方案并非最优，并且依赖可信设置。本文旨在填补两个空白：第一，在可信设置下能否直接对最经典的KZG多项式承诺实现一对多证明者批处理，并保持KZG的常数级验证时间和证明大小；第二，能否在几乎不牺牲渐进性能的前提下摆脱对可信设置的依赖，实现透明的多项式承诺方案。

### 相关工作

[25] Kate et al. Constant-size commitments to polynomials and their applications. **ASIACRYPT 2010** [Google Scholar](https://scholar.google.com/scholar?q=Constant-size+commitments+to+polynomials+and+their+applications)
> 核心思路：利用双线性映射构造多项式承诺，证明大小为常数，验证时间为常数。
> 局限与区别：若需生成N个证明，证明者需花费O(N^2)时间，不适用于大规模VSS场景。

[35] Tomescu et al. Towards scalable threshold cryptosystems. **IEEE S&P 2020** [Google Scholar](https://scholar.google.com/scholar?q=Towards+scalable+threshold+cryptosystems)
> 核心思路：通过认证多点估值树（AMT）实现一对多证明者批处理，证明者开销为O(N log N)。
> 局限与区别：验证时间和证明大小均为O(log N)，且需要可信设置；本文在可信设置下实现了O(1)验证时间和证明大小，在透明设置下首次消除了可信设置。

[40] Yurek et al. hbACSS: How to robustly share many secrets. **ePrint 2021** [Google Scholar](https://scholar.google.com/scholar?q=hbACSS%3A+How+to+robustly+share+many+secrets)
> 核心思路：构造了无需可信设置的VSS方案，但证明者时间达O(N^2)，验证者时间达O(N)。
> 局限与区别：本文透明方案的证明者时间为O(N log N)，显著更优。

[41] Zhang et al. Transparent polynomial delegation and its applications to zero knowledge proof. **IEEE S&P 2020** [Google Scholar](https://scholar.google.com/scholar?q=Transparent+polynomial+delegation+and+its+applications+to+zero+knowledge+proof)
> 核心思路：基于GKR协议和透明多项承诺实现zkSNARK，证明者时间为O(n log n)。
> 局限与区别：若直接对N个点分别运行该方案，证明者总时间将达O(N n log n)；本文通过一对多技术将其降为O(N log N + n log n)。

[19] Goldwasser et al. Delegating Computation: Interactive Proofs for Muggles. **J. ACM 2015** [Google Scholar](https://scholar.google.com/scholar?q=Delegating+Computation%3A+Interactive+Proofs+for+Muggles)
> 核心思路：提出了GKR协议，允许验证者通过逐层归约来高效验证深度为d的算术电路，证明者时间为O(|C|)。
> 局限与区别：GKR原生不支持一对多场景且不支持陈述的零知识；本文将其扩展为支持N个不同输出的一对多论证。

[16] Fiat and Shamir. How to prove yourself: Practical solutions to identification and signature problems. **Crypto 1986** [Google Scholar](https://scholar.google.com/scholar?q=How+to+prove+yourself%3A+Practical+solutions+to+identification+and+signature+problems)
> 核心思路：通过哈希整个交互转录将交互式协议转化为非交互式协议（Fiat-Shamir启发式）。
> 局限与区别：标准Fiat-Shamir要求各验证者转录相同，不适应一对多场景；本文提出了一种新型启发式，使不同验证者在输出不同时仍能共享随机挑战。

### 核心技术与方案

本文提出了两个多项式承诺方案，前者依赖可信设置，后者在随机谕言模型中消除可信设置。两者均支持在一对多场景下以O(N log N)的证明者时间来生成N个证明。

**基于KZG的方案。** 标准KZG方案中，证明者需为每个点a计算多项式q(x) = (f(x) - f(a))/(x - a)在τ处的求值g^(q(τ))，其中τ是陷门。本文的核心观察是将所有所求值点选为N次单位根ω^i，并利用双变量多项式q(x, y) = (f(x) - f(y))/(x - y)。展开后，q(τ, y) = ∑_{k=1}^{t} h_k y^{k-1}，其中系数h_k = ∑_{j=k}^{t} c_j τ^{j-k}。证明者可通过在群元素上执行FFT（即对g^(h_k)进行FFT）来同时计算所有g^(q(τ, ω^i))，总时间为O(N log N)个群指数运算，且不泄露陷门τ。验证者时间与证明大小仍为O(1)，继承KZG的常数性质。

**透明方案。** 本文将问题推广为“一对多零知识证明”：令电路C有N个输出，每个验证者Vj只想验证一个输出C(in)[j]。方案分为三步：
1. **输出层归约。** 在每个Vj处运行一次额外的sumcheck协议，将验证C(in)[j]的问题归约为验证公共值Ṽ0(ğ)的问题，其中ğ是logN维随机向量。利用算法1（SumCheck算法），证明者可在O(N log N)时间内同时为N个验证者完成该sumcheck。算法利用了Ṽ0在N个点上的共享结构，通过迭代更新一个长度为N/2^i的查找表，使每个验证者的消息能在常数时间内生成。
2. **GKR协议。** 归约后所有验证者共享同一个声明Ṽ0(ğ)，因此证明者在后续logN层GKR中可以计算一份公共证明，时间O(|C|) = O(N log N)。
3. **新型Fiat-Shamir变换。** 为了在非交互模式下使各验证者共享GKR中的随机挑战，本文提出一种混合方法：在输出层sumcheck中每轮使用Merkle树将不同验证者的随机数合并为单一挑战（引入log^2 N额外开销）；在后续GKR轮次中，由于所有验证者已共享声明，直接对上一轮消息与挑战进行哈希即可得到公共挑战，无需Merkle树。本文证明该变换在随机谕言模型中具有多项式级的可靠性损失。
最后，利用Virgo [41] 中的透明zkMVPC来处理输入层，使整个方案具备零知识性质。最终通信复杂度为O(log^2 N)每验证者，证明者时间为O(N log N)场运算。

**安全性论证。** KZG方案的安全性直接继承自原论文 [25] 的l-SBDH假设。透明方案的安全性通过将Merkle树路径视为Fiat-Shamir变换中的“哑轮回合”，证明变换后的非交互协议满足状态恢复可靠性，从而标准多项式损失可靠下界成立。

### 核心公式与流程

**[KZG批处理证明生成算法：算法2]**
$$
g^{h_k} = g^{\sum_{j=k}^{t} c_j \tau^{j-k}} \; (k=1,\dots,t), \quad \pi_i = g^{q(\tau,\omega^i)} = \text{FFT}(g^{h_1},\dots,g^{h_t})[i]
$$
> 作用：通过一次FFT在群上同时计算所有N个证明，其中h_k由多项式系数与τ的卷积在指数上得到。

**[算法1（SumCheck算法）核心递推]**
$$
\tilde{V}_0(g_1,\dots,g_{i-1},r,\vec{b}) = V[B] \cdot (1-r) + V[B+2^{\log N-i}] \cdot r \quad (r=0,1,2)
$$
$$
a_{i t,j} = \beta_j \cdot [(1-j_i)(1-r) + j_i r] \cdot \tilde{V}_0(g_1,\dots,g_{i-1},r,j_{i+1},\dots,j_{\log N})
$$
> 作用：在logN轮sumcheck中，每轮对长度为N/2^i的查找表V以O(N/2^i)时间更新，然后利用β_j的递推公式在常数时间内为每个验证者生成三元消息(a_{i0,j}, a_{i1,j}, a_{i2,j})。

**[新型Fiat-Shamir变换（协议3中随机挑战生成）]**
$$
\begin{aligned}
r_{1,j} &= \rho(\text{com}_{\tilde{V}_d} || V_0(j) || M_{1,j}), \\
r_{i,j} &= \rho(g_{i-1}^{(0)} || M_{i,j}) \quad (i>1), \\
g_i^{(0)} &= \text{MT.Commit}(\vec{r}^{(i)})
\end{aligned}
$$
> 作用：在输出层sumcheck的每轮，对每个验证者的哈希值r_{i,j}构造Merkle树，以树根作为所有验证者在该轮的公共随机挑战。后续GKR轮次中，直接对上一轮公共挑战与公共消息哈希，不再需要Merkle树。

### 实验结果

实验在AWS c5a.24xlarge实例（AMD EPYC 7002 CPU, 96核, 187 GB RAM）上进行，所有参与方同一机器运行，设置t = N/2，N从2^11至2^21。KZG可信设置方案的证明者时间在N=2^21时为3995秒，比AMT [35] 慢3倍（AMT约1332秒），但证明大小仅192字节（比AMT小20倍），验证时间仅1.3ms（比AMT快4.2–7.8倍）。透明方案的证明者时间在N=2^21时为560秒，比KZG方案快7–10.5倍，比单独运行Virgo [41] N次快700–260,000倍，但证明大小为200–390 KiB（比KZG方案大），验证时间为2.8–8.7ms。在DKG应用中，KZG方案的总计算时间（6700秒）和通信量（0.8 GB，N=2^21）分别比AMT-DKG快3.3倍和通信小20倍；透明方案尽管计算时间（15400秒）较慢，但完全消除了对可信设置的依赖。

### 局限性与开放问题
透明方案虽然在计算上优于KZG方案，但每个证明的大小为O(log^2 N)，这导致在DKG中通信开销显著高于KZG方案。此外，所有方案要求所有参与方在同一台机器上模拟执行，实际分布式部署时网络延迟和带宽可能成为瓶颈。在异步VSS和DKG场景下如何高效应用所提出的“一对多零知识证明”技术仍是一个开放问题。

### 强关联论文

[25] Kate et al. Constant-size commitments to polynomials and their applications. **ASIACRYPT 2010** [Google Scholar](https://scholar.google.com/scholar?q=Constant-size+commitments+to+polynomials+and+their+applications)

[35] Tomescu et al. Towards scalable threshold cryptosystems. **IEEE S&P 2020** [Google Scholar](https://scholar.google.com/scholar?q=Towards+scalable+threshold+cryptosystems)

[40] Yurek et al. hbACSS: How to robustly share many secrets. **ePrint 2021** [Google Scholar](https://scholar.google.com/scholar?q=hbACSS%3A+How+to+robustly+share+many+secrets)

[41] Zhang et al. Transparent polynomial delegation and its applications to zero knowledge proof. **IEEE S&P 2020** [Google Scholar](https://scholar.google.com/scholar?q=Transparent+polynomial+delegation+and+its+applications+to+zero+knowledge+proof)

[19] Goldwasser et al. Delegating Computation: Interactive Proofs for Muggles. **J. ACM 2015** [Google Scholar](https://scholar.google.com/scholar?q=Delegating+Computation%3A+Interactive+Proofs+for+Muggles)

[16] Fiat and Shamir. How to prove yourself: Practical solutions to identification and signature problems. **Crypto 1986** [Google Scholar](https://scholar.google.com/scholar?q=How+to+prove+yourself%3A+Practical+solutions+to+identification+and+signature+problems)

[15] Feldman. A practical scheme for non-interactive verifiable secret sharing. **FOCS 1987** [Google Scholar](https://scholar.google.com/scholar?q=A+practical+scheme+for+non-interactive+verifiable+secret+sharing)

[23] Kate. Distributed key generation and its applications. **PhD thesis 2010** [Google Scholar](https://scholar.google.com/scholar?q=Distributed+key+generation+and+its+applications)


## 关键词

+ 一对多多项式承诺批量证明
+ 可验证秘密共享VSS
+ 透明多项式承诺
+ 无可信设置多项式方案
+ 证明批量化证明优化
+ 分布式区块链密码学
