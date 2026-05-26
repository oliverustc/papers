---
title: "Fast RS-IOP Multivariate Polynomial Commitments and Verifiable Secret Sharing"
标题简称:
论文类型: conference
会议简称: USENIX Security
发表年份: 2024
created: 2025-04-17 10:26:29
modified: 2025-04-17 10:27:03
---

## Fast RS-IOP Multivariate Polynomial Commitments and Verifiable Secret Sharing

## 发表信息

+ [原文链接](https://www.usenix.org/conference/usenixsecurity24/presentation/zhang-zongyang)

## 作者

+ Zongyang Zhang 
+ Weihan Li 
+ [Yanpei Guo](Yanpei%20Guo.md) 
+ Kexin Shi 
+ [Sherman SM Chow](Sherman%20SM%20Chow.md)
+ Ximeng Liu 
+ Jin Dong 

## 笔记

### 背景与动机
多项式承诺方案 PCS 是构建高效零知识证明和可验证秘密共享等密码协议的核心模块。基于快速 Reed–Solomon 交互式预言机证明 FRI 的 PCS 因具备透明设置、潜在后量子安全性以及次线性证明大小而备受关注。然而，现有 FRI-based 多元 PCS，如 Virgo 和 HyperPlonk，其证明者复杂度均为关于多项式规模的准线性 $O(\mu d^\mu \log d)$，未能达到评估多项式所需的 $O(d^\mu)$ 最优线性下界。此外，支持一对多证明的多元 PCS 尚未存在，这限制了其在异步可验证秘密共享 AVSS 中的应用：现有方案如 eAVSS 和 HAVEN 的经销商复杂度高达 $O(n^3)$，Bingo 虽将其降至 $O(n^2 \log n)$ 但将部分生成工作转移至各参与方。本文旨在填补 FRI-based 多元 PCS 在证明者最优线性复杂度上的空白，并挖掘其在一对多证明和高效 AVSS 构造中的应用潜力。

### 相关工作

[5] Eli Ben-Sasson et al. Fast Reed-Solomon interactive oracle proofs of proximity. **ICALP 2018** [Google Scholar](https://scholar.google.com/scholar?q=Fast+Reed-Solomon+interactive+oracle+proofs+of+proximity)
> 核心思路：提出 FRI 协议作为低度测试工具，通信和验证者复杂度为 $O(\log^2 n)$。
> 局限与区别：FRI 本身仅测试向量的 Reed–Solomon 接近性，需借助额外协议才能构造 PCS。

[32] Alexander Vlasov et al. Transparent polynomial commitment scheme with polylogarithmic communication complexity. **IACR ePrint 2019/1020** [Google Scholar](https://scholar.google.com/scholar?q=Transparent+polynomial+commitment+scheme+with+polylogarithmic+communication+complexity)
> 核心思路：首次利用 FRI 构造单变量 PCS，其证明者复杂度为 $O(n)$，验证者与通信复杂度为 $O(\log^2 n)$。
> 局限与区别：该方案限于单变量多项式，无法直接扩至多元场景。

[16] Binyi Chen et al. HyperPlonk: Plonk with linear-time prover and high-degree custom gates. **EUROCRYPT 2023** [Google Scholar](https://scholar.google.com/scholar?q=HyperPlonk:+Plonk+with+linear-time+prover+and+high-degree+custom+gates)
> 核心思路：提出基于 FRI 的多线性 PCS，通过将多线性多项式的求值化为多个单变量多项式的求值。
> 局限与区别：其证明者复杂度为 $O(\mu 2^\mu \log 2)$ 或 $O(2^\mu)$ 取决于算法选择，且验证者与通信复杂度为 $O(\mu^3 \log^3 2)$ 或 $O(\mu^2 \log^2 2)$，存在复杂度紧张。

[37] Jiaheng Zhang et al. Transparent polynomial delegation and its applications to zero knowledge proof. **S&P 2020** [Google Scholar](https://scholar.google.com/scholar?q=Transparent+polynomial+delegation+and+its+applications+to+zero+knowledge+proof)
> 核心思路：通过 GKR 协议委派快速傅里叶变换，将多元大域上的求值证明转化为小域上的 GKR 证明，构建 Virgo PCS。
> 局限与区别：其证明者复杂度为 $O(\mu d^\mu \log d)$，未达线性最优。

[31] Alin Tomescu et al. Towards scalable threshold cryptosystems. **S&P 2020** [Google Scholar](https://scholar.google.com/scholar?q=Towards+scalable+threshold+cryptosystems)
> 核心思路：提出 AMT，利用 KZG 构建单变量一对多证明，构造认证多点求值树。
> 局限与区别：AMT 基于 KZG，需可信设置，且通信和验证者复杂度从 $O(1)$ 增至 $O(\log n)$。

[36] Jiaheng Zhang et al. Polynomial commitment with a one-to-many prover and applications. **USENIX Security 2022** [Google Scholar](https://scholar.google.com/scholar?q=Polynomial+commitment+with+a+one-to-many+prover+and+applications)
> 核心思路：利用 FFT 和 GKR 协议实现单变量透明一对多证明，证明者复杂度为 $O(n^2 \log n)$。
> 局限与区别：该方案仅支持单变量多项式，将其用于多元场景需额外构造 FFT 电路，目前尚不可行。

[3] Michael Backes et al. Asynchronous computational VSS with reduced communication complexity. **CT-RSA 2013** [Google Scholar](https://scholar.google.com/scholar?q=Asynchronous+computational+VSS+with+reduced+communication+complexity)
> 核心思路：提出 eAVSS，利用双变量多项式共享秘密，通信复杂度为 $O(n^2)$。
> 局限与区别：eAVSS 依赖 KZG PCS，需可信设置且经销商复杂度为 $O(n^3)$。

[2] Nicolas Alhaddad et al. High-threshold AVSS with optimal communication complexity. **FC 2021** [Google Scholar](https://scholar.google.com/scholar?q=High-threshold+AVSS+with+optimal+communication+complexity)
> 核心思路：提出 HAVEN-1 和 HAVEN-2，分别基于 KZG 和 Bulletproofs 实现高阈值 AVSS。
> 局限与区别：HAVEN 方案的经销商复杂度为 $O(n^3)$。

[1] Ittai Abraham et al. Bingo: Adaptively secure packed asynchronous verifiable secret sharing and asynchronous distributed key generation. **CRYPTO 2023** [Google Scholar](https://scholar.google.com/scholar?q=Bingo:+Adaptively+secure+packed+asynchronous+verifiable+secret+sharing+and+asynchronous+distributed+key+generation)
> 核心思路：将部分证明生成工作转移到各参与方，降低经销商复杂度至 $O(n^2 \log n)$。
> 局限与区别：该方案增加了参与方计算量，且未实现真正的证明者最优多元 PCS 一对多证明。

### 核心技术与方案

**PolyFRIM 构造**：PolyFRIM 的核心在于一个称为滚动批处理 FRI 的低度测试技术。对于一则 $\mu$ 变量 $d$ 次多项式 $\tilde f$，其求值 $\tilde f(x_1,\dots,x_\mu)$ 可等价转换为另一则 $\mu t$ 变量多线性多项式 $\tilde f'$ 的求值，其中 $t = \log d$。因此，整体求值证明转化为对 $\tilde f'$ 的证明。受 HyperPlonk 启发，这一过程可进一步拆解为对一系列单变量多项式 $\{\hat f_i\}_{i\in[0,\mu t-1]}$ 的低度测试。这些多项式满足 $\deg(\hat f_i) \le 2^{\mu t - i}$。

滚动批处理 FRI 的关键观察是：在第一轮 FRI 中，$\hat f_0$ 会被转换成一个新多项式 $\hat p^{(1)}$，其度界恰好降至 $2^{\mu t - 1}$，与 $\hat f_1$ 的度界相同。因此，证明者可以将 $\hat p^{(1)}$ 与 $\hat f_1$ 进行随机线性组合，形成一个整体多项式 $\hat f^{(1)}$，并继续对其执行 FRI。如此递归，原本 $\mu t$ 次独立的 FRI 被聚合为一次执行，从而将证明者复杂度从 $O(\mu t d^\mu \log d)$ 降至 $O(d^\mu)$，同时验证者与通信复杂度维持在 $O(\log^2 d^\mu) = O(\mu^2 \log^2 d)$。

**一对多 PolyFRIM 构造**：将 PolyFRIM 扩展为一对多证明，核心挑战在于不同求值点 $f(x_i, y_j)$ 所对应的求值向量不同，导致每轮计算无法复用。解决方案包括两点：其一，交换求值向量的顺序，将原向量 $(x^{2^0},\dots, x^{2^{t-1}}, y^{2^0},\dots, y^{2^{t-1}})$ 逆序为 $(x^{2^{t-1}},\dots, x^{2^0}, y^{2^{t-1}},\dots, y^{2^0})$。其二，将求值点集 $\{(x_i, y_j)\}$ 构造为 $n$ 次单位根构成的集合 $\{(w_n^i, w_n^j)\}$。这使得在证明过程的第 $k$ 轮中，$x$ 方向上仅存在 $2^k$ 种不同的取值，证明者只需计算 $O(2^k \cdot n^2/2^k) = O(n^2)$ 的运算即可。通过构建一棵深度为 $2t$ 的二叉树，并采用 Fiat–Shamir 变换生成共享随机挑战，整体证明者复杂度降至 $O(n^2 \log n)$，且每个验证者的验证时间与通信开销仍为 $O(\log^2 n)$。

**FRISS AVSS 构造**：FRISS 利用一对多 PolyFRIM 实现 AVSS。其框架类似于 eAVSS，但需克服 PolyFRIM 缺乏同态性的问题。第一，FRISS 利用 PolyFRIM 的 $2q$-bound 知识泄露性质实现安全性：通过设置阈值 $t = p + 2q$（$p$ 为腐败参与方数），并引入随机多项式 $\tilde r$ 掩盖 $\tilde f$，使得验证者仅能获得至多 $2q$ 个求值信息。第二，为支持份额恢复，经销商除发送 $\hat f(w_n^i, Y)$ 外，还需额外发送所有 $\{f(w_n^j, w_n^i)\}_{j\in[n]}$ 及其证明。当某个参与方 $P_i$ 无法直接从经销商获得有效份额时，其他参与方 $P_j$ 可将 $f(w_n^j, w_n^i)$ 及其证明转发给 $P_i$，使其能够正确重构 $\hat f(w_n^i, Y)$。第三，经销商通过广播单一承诺 $C$ 及其衍生的 $\{C_i^*\}$，天然保证了各 $\hat f(w_n^i, Y)$ 与 $f(X, Y)$ 之间的一致性。FRISS 的经销商复杂度为 $O(n^2 \log n)$，参与方计算复杂度为 $O(n \log^2 n)$，通信复杂度为 $O(n^2 \log^2 n)$。

### 核心公式与流程

**[滚动批处理 FRI 协议]**
> 证明者 $\mathcal{P}$ 与验证者 $\mathcal{V}$ 交互，输入多项式集合 $\{\hat f_i\}_{i\in[0,\mu-1]}$ 及各历元度界 $d_i = d_0 \cdot 2^{-i}$。
> 1. $\mathcal{P}$ 计算并提交各 $\hat f_i|_{L_i}$ 的 Merkle 承诺。
> 2. 对于 $i=1$ 至 $\mu$：
>    a. $\mathcal{P}$ 将 $\hat f^{(i-1)}$ 分解为 $\hat g_i(X^2) + X \cdot \hat h_i(X^2)$。
>    b. $\mathcal{V}$ 发送随机数 $\alpha_i$。
>    c. $\mathcal{P}$ 计算 $\hat p^{(i)}(X) \leftarrow \hat g_i(X) + \alpha_i \cdot \hat h_i(X)$。
>    d. 若 $i < \mu$，$\mathcal{P}$ 提交 $\hat p^{(i)}|_{L_i}$；否则直接发送其系数。
>    e. $\mathcal{P}$ 计算 $\hat f^{(i)}(X) \leftarrow \hat p^{(i)}(X) + \alpha_i^2 \cdot \hat f_i(X)$。
> 3. 重复 $q$ 次：$\mathcal{V}$ 发送 $\beta \in L_0$，$\mathcal{P}$ 打开 $\{\hat f_i(\pm \beta^{2^i})\}$ 及 $\{\hat p^{(i)}(\pm \beta^{2^i})\}$，$\mathcal{V}$ 检查共线条件。
> 作用：将 $\mu$ 次独立 FRI 合并为一次，实现 $O(d^\mu)$ 证明者和 $O(\log^2 d^\mu)$ 验证者复杂度。

**[PolyFRIM 公共参数生成]**
$$\mathsf{pp} \gets \mathsf{Gen}_m(1^\lambda, \mu \cdot \lceil \log(d+1) \rceil)$$
> 作用：将 $\mu$ 变量 $d$ 次多项式承诺归约为对一则 $\mu \log (d+1)$ 变量多线性多项式的承诺。

**[FRISS 经销商算法]**
> 输入：秘密 $s$
> 1. 随机选取 $(t,t)$-次双变量多项式 $f(X,Y)$ 与 $r(X,Y)$，满足 $f(z,0)=s$。
> 2. 计算 $C \leftarrow \mathsf{Commit_F}(\mathsf{pp}, f, r)$ 及所有求值证明 $\{f(w_n^i, w_n^j), \pi_{i,j}\}_{i,j\in[n]}$。
> 3. 向参与方 $P_i$ 发送 $\hat f_i(w_n^i, Y)$, $\hat r_i(w_n^i, Y)$ 及 $\{f(w_n^j, w_n^i), r(w_n^j, w_n^i), \pi_{j,i}\}_{j\in[n]}$。
> 作用：经销商利用一对多 PolyFRIM 生成所有证明后，将样本份额及其它参与方的子份额一并分发。

### 实验结果

实验在 AMD Ryzen 3900X 处理器和 80GB RAM 上进行，使用 Rust 语言实现，采用 $\mathbb{F}_{p^2}$ 域（$p = 2^{61} - 1$），FRI 码率设为 1/8，查询次数设为 34 以提供 100 比特安全性。与 Virgo、HyperPlonk 和 Bulletproofs 相比，对于规模为 $2^{20}$ 的多元多项式，PolyFRIM 的证明者时间仅为 4.4 秒，较 Virgo、HyperPlonk 和 Bulletproofs 分别快 6 倍、10 倍和 25 倍。PolyFRIM 的验证者时间比 HyperPlonk 快 4 至 10 倍，证明大小小 2 至 3 倍。在一对多证明测试中，PolyFRIM 生成 $2^{12}$ 至 $2^{20}$ 个证明的时间较 ZXH+22 快 4 至 7 倍，较 AMT 和 KZG 分别快 25 至 100 倍和 $10^3$ 至 $10^6$ 倍。在 AVSS 性能评测中，FRISS 的经销商时间较 eAVSS 和 HAVEN-1/2 快 4 至 800 倍而参与方时间与之相近，较 Bingo 的经销商时间慢约 10 倍但参与方时间快 10 倍。

### 局限性与开放问题

FRISS 由于 PolyFRIM 缺乏同态性，经销商需额外发送 $n^2$ 个子份额，导致通信量增至 $O(n^2 \log^2 n)$。如何设计不增加通信开销的基于无同态性 PCS 的 AVSS 仍是个开放问题。此外，PolyFRIM 目前不提供零知识性，虽然其 $2q$-bound 知识泄露性质对 AVSS 场景已足够，但构建真正的零知识 FRI-based 多元 PCS 仍有研究价值。当前方案中多变量多项式的度需为 $2^t - 1$ 的形式，如何处理一般度数的多项式也是实际应用中的问题。

### 强关联论文

[5] Eli Ben-Sasson et al. Fast Reed-Solomon interactive oracle proofs of proximity. **ICALP 2018** [Google Scholar](https://scholar.google.com/scholar?q=Fast+Reed-Solomon+interactive+oracle+proofs+of+proximity)

[6] Eli Ben-Sasson et al. Proximity gaps for Reed-Solomon codes. **FOCS 2020** [Google Scholar](https://scholar.google.com/scholar?q=Proximity+gaps+for+Reed-Solomon+codes)

[16] Binyi Chen et al. HyperPlonk: Plonk with linear-time prover and high-degree custom gates. **EUROCRYPT 2023** [Google Scholar](https://scholar.google.com/scholar?q=HyperPlonk:+Plonk+with+linear-time+prover+and+high-degree+custom+gates)

[31] Alin Tomescu et al. Towards scalable threshold cryptosystems. **S&P 2020** [Google Scholar](https://scholar.google.com/scholar?q=Towards+scalable+threshold+cryptosystems)

[32] Alexander Vlasov et al. Transparent polynomial commitment scheme with polylogarithmic communication complexity. **IACR ePrint 2019/1020** [Google Scholar](https://scholar.google.com/scholar?q=Transparent+polynomial+commitment+scheme+with+polylogarithmic+communication+complexity)

[36] Jiaheng Zhang et al. Polynomial commitment with a one-to-many prover and applications. **USENIX Security 2022** [Google Scholar](https://scholar.google.com/scholar?q=Polynomial+commitment+with+a+one-to-many+prover+and+applications)

[37] Jiaheng Zhang et al. Transparent polynomial delegation and its applications to zero knowledge proof. **S&P 2020** [Google Scholar](https://scholar.google.com/scholar?q=Transparent+polynomial+delegation+and+its+applications+to+zero+knowledge+proof)

[3] Michael Backes et al. Asynchronous computational VSS with reduced communication complexity. **CT-RSA 2013** [Google Scholar](https://scholar.google.com/scholar?q=Asynchronous+computational+VSS+with+reduced+communication+complexity)

[2] Nicolas Alhaddad et al. High-threshold AVSS with optimal communication complexity. **FC 2021** [Google Scholar](https://scholar.google.com/scholar?q=High-threshold+AVSS+with+optimal+communication+complexity)

[1] Ittai Abraham et al. Bingo: Adaptively secure packed asynchronous verifiable secret sharing and asynchronous distributed key generation. **CRYPTO 2023** [Google Scholar](https://scholar.google.com/scholar?q=Bingo:+Adaptively+secure+packed+asynchronous+verifiable+secret+sharing+and+asynchronous+distributed+key+generation)


## 关键词

+ RS-IOP多变量多项式承诺方案
+ 线性证明者复杂度优化
+ 可验证秘密共享AVSS
+ 透明后量子设置
+ 亚线性证明大小验证
+ 一对多证明分布式计算