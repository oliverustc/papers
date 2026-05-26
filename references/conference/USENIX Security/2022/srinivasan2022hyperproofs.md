---
title: "Hyperproofs: Aggregating and Maintaining Proofs in Vector Commitments"
标题简称: Hyperproofs
论文类型: conference
会议简称: USENIX Security
发表年份: 2022
modified: 2025-04-17 10:23:24
created: 2025-04-07 16:58:58
---

## Hyperproofs: Aggregating and Maintaining Proofs in Vector Commitments

## 发表信息

+ [原文链接](https://www.usenix.org/conference/usenixsecurity22/presentation/srinivasan)

## 作者

+ Srinivasan, Shravan
+ Chepurnoy, Alexander
+ [Charalampos Papamanthou](Charalampos%20Papamanthou.md)
+ Tomescu, Alin
+ [Yupeng Zhang](Yupeng%20Zhang.md)

## 笔记

### 背景与动机
向量承诺方案是许多密码学协议的基础构件，允许证明者计算向量的简洁摘要以及对每个位置的证明。现有方案存在根本性权衡：可维护的向量承诺（如 Merkle 树）能够在对数时间内更新所有证明，但无法高效聚合多个证明；而可聚合的方案（如 Pointproofs）其证明大小为常数，但更新全部证明需要线性时间。然而，新兴应用如无状态加密货币要求专用节点高效维护所有证明，同时要求矿工高效聚合这些证明。虽然通用论证系统（如 SNARK）可为可维护的向量承诺增加聚合能力，但在实践中速度过慢。Hyperproofs 旨在填补这一空白，构建第一个同时具有高效可维护性和可聚合性的向量承诺方案。

### 相关工作

[21] Catalano 等. Vector commitments and their applications. **PKC 2013** [Google Scholar](https://scholar.google.com/scholar?q=Vector+commitments+and+their+applications)
> 核心思路：形式化了向量承诺，并构造了基于 CDH 和 RSA 的常数大小证明方案。
> 局限与区别：这两种方案的证明大小为常数，但更新所有证明需要线性时间，不适用于需要高效维护的场景。

[28] Gorbunov 等. Pointproofs: Aggregating Proofs for Multiple Vector Commitments. **CCS 2020** [Google Scholar](https://scholar.google.com/scholar?q=Pointproofs%3A+Aggregating+Proofs+for+Multiple+Vector+Commitments)
> 核心思路：提出常数大小的可聚合证明，支持跨摘要的聚合。
> 局限与区别：更新所有 n 个证明需要 O(n) 次指数运算，难以支持需要频繁维护的海量状态。

[46] Papamanthou 等. Signatures of Correct Computation. **TCC 2013** [Google Scholar](https://scholar.google.com/scholar?q=Signatures+of+Correct+Computation)
> 核心思路：将 KZG 多项式承诺扩展到多变量，即 PST 承诺，可证明多变量多项式在任意点的求值。
> 局限与区别：计算单个证明需要 O(n) 时间，计算 n 个证明则需要 O(n²) 时间，且不支持更新与聚合。

[58] Tomescu. How to Keep a Secret and Share a Public Key (Using Polynomial Commitments). **PhD thesis, MIT 2020** [Google Scholar](https://scholar.google.com/scholar?q=How+to+Keep+a+Secret+and+Share+a+Public+Key+(Using+Polynomial+Commitments))
> 核心思路：提出认证多点求值树（AMT），基于单变量多项式构造可维护的向量承诺。
> 局限与区别：AMT 不支持聚合，且其可信设置需要 O(n²) 时间，公共参数大小为 O(n log n)。

[12] Boneh 等. Batching Techniques for Accumulators with Applications to IOPs and Stateless Blockchains. **CRYPTO 2019** [Google Scholar](https://scholar.google.com/scholar?q=Batching+Techniques+for+Accumulators+with+Applications+to+IOPs+and+Stateless+Blockchains)
> 核心思路：基于 RSA 的累加器，支持常数大小的证明和批量证明。
> 局限与区别：更新所有证明需要 O(n log n) 时间，且不支持同态性，难以应用于 Hyperproofs 的不可窃取性构造。

[20] Campanelli 等. Incrementally Aggregatable Vector Commitments and Applications to Verifiable Decentralized Storage. **ASIACRYPT 2020** [Google Scholar](https://scholar.google.com/scholar?q=Incrementally+Aggregatable+Vector+Commitments+and+Applications+to+Verifiable+Decentralized+Storage)
> 核心思路：支持增量聚合的向量承诺，公共参数为常数大小。
> 局限与区别：更新所有证明需要 O(n log n) 时间，不具备高效的可维护性。

[19] Bünz 等. Proofs for Inner Pairing Products and Applications. **ePrint 2019/1177** [Google Scholar](https://scholar.google.com/scholar?q=Proofs+for+Inner+Pairing+Products+and+Applications)
> 核心思路：提出内积论证（IPA），可高效证明配对产品的知识。
> 局限与区别：IPA 本身并非向量承诺，但其递归压缩思想被 Hyperproofs 直接用于聚合多个配对方程。

[48] Papamanthou 等. Streaming Authenticated Data Structures. **EUROCRYPT 2013** [Google Scholar](https://scholar.google.com/scholar?q=Streaming+Authenticated+Data+Structures)
> 核心思路：基于格的可维护向量承诺，支持同态性且透明设置。
> 局限与区别：在实践中速度过慢，且不支持证明的聚合。

[59] Tomescu 等. Aggregatable Subvector Commitments for Stateless Cryptocurrencies. **SCN 2020** [Google Scholar](https://scholar.google.com/scholar?q=Aggregatable+Subvector+Commitments+for+Stateless+Cryptocurrencies)
> 核心思路：提出可聚合子向量承诺，证明大小为常数。
> 局限与区别：更新所有证明需要 O(n) 时间，且可维护性较差。

[64] Wesolowski. Efficient Verifiable Delay Functions. **EUROCRYPT 2019** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+Verifiable+Delay+Functions)
> 核心思路：在可验证延迟函数中探索水印证明的概念。
> 局限与区别：该工作聚焦于 VDF，Hyperproofs 首次将水印思想应用于向量承诺，并给出安全定义。

### 核心技术与方案

Hyperproofs 的整体框架分为三个层次：首先，采用**多层线性树**高效计算和更新所有证明；其次，利用**内积论证**实现证明的高效聚合；最后，利用**同态性质**构造不可窃取的证明。

**多层线性树（MLT）。** 向量 $\mathbf{a} = [a_0, \dots, a_{n-1}]$ 与其多层线性扩展多项式 $f(\mathbf{x})$ 对应。单个 PST 证明 $\pi_i = (w_{i,\ell}, \dots, w_{i,1})$ 由逐层除法的商多项式承诺组成，计算耗时 O(n)。核心观察是，所有 n 个证明共享相同的顶层商 $q_\ell = f_1 - f_0$，且任意一半证明共享同一下层商。因此，可采用分治策略一次性计算所有证明，总时间复杂度为 $O(n \log n)$。由此构造的 MLT 中，每个节点存储一个 PST 承诺，路径上的承诺即构成了位置 i 的证明。当位置 u 的值变化 $\delta$ 时，仅需更新 u 所在路径上的 $\ell$ 个节点，更新公式为 $w_{u,k}' = w_{u,k} \cdot (\text{upk}_{u,k-1})^{\delta}$，其中 $\text{upk}_{u,k-1}$ 是更新密钥。因此，更新所有 n 个证明仅需 $O(\log n)$ 时间，其中 $\ell$ 为树高。

**证明聚合。** 单个证明 $\pi_i$ 的验证方程为：
$$
e(\mathsf{C}/g_1^{a_i}, g_2) = \prod_{j=1}^{\ell} e(w_j, g_2^{s_j - i_j}).
$$
该式等价于内积 $Z_i = \langle \mathbf{A}_i, \mathbf{B}_i \rangle$，其中 $\mathbf{A}_i = (w_1, \dots, w_\ell)$，$\mathbf{B}_i = (g_2^{s_1 - i_1}, \dots, g_2^{s_\ell - i_\ell})$，$Z_i = e(\mathsf{C}/g_1^{a_i}, g_2)$。聚合 b 个证明时，利用随机线性组合将 b 个 ℓ 维内积方程合并为单个 $b\ell$ 维内积方程：
$$
\prod_{i=1}^{b} Z_i^{r_i} = \prod_{i=1}^{b} \left(\prod_{j=1}^{\ell} e(A_{i,j}, B_{i,j})\right)^{r_i},
$$
然后将 $\mathbf{A} = [\mathbf{A}_1 || \dots || \mathbf{A}_b]$ 与 $\mathbf{B}' = [\mathbf{B}_1^{r_1} || \dots || \mathbf{B}_b^{r_b}]$ 提交给内积论证（IPA），得到大小为 $O(\log(b\ell))$ 的聚合证明。证明者的计算复杂度为 $O(b\ell)$，验证者需进行 $O(b\ell)$ 的 $\mathbb{G}_2$ 指数运算（处理验证密钥）。

**不可窃取性。** 基于双线性映射的同态性，证明者用水印密钥 $\alpha$ 指数化所有证明：$\hat{w}_{i,j} = w_{i,j}^{\alpha}$。验证方程为：
$$
e(\mathsf{C}/g_1^{a_i}, g_2^{\alpha}) = \prod_{j=1}^{\ell} e(\hat{w}_{i,j}, g_2^{s_j - i_j}),
$$
其中 $g_2^{\alpha}$ 是对应的水印公钥，$\alpha$ 需通过零知识证明确认为已知。由于移除水印需要知晓 $\alpha^{-1}$，而窃取者指数化后无法证明对有效指数 $\alpha\delta$ 的知情（需零知识证明），故不可窃取性在代数群模型下可证。水印后的公共参数通过一次性指数化所有参数得到，因此 MLT 的可维护性和可聚合性得以保留。

**安全性。** 单个证明的可靠性基于 $\ell$-SDH 假设，证明策略是猜测伪造位置 i，将 $s_j - i_j$ 嵌入 $r_j(s-i_1)$，通过两个不一致证明的除法提取 $g_1^{1/(s-i_1)}$。聚合证明的可靠性依赖于内积论证的知识可靠性，而不可窃取性在代数群模型下通过规约到离散对数问题和 $q$-SDH 问题证明。

### 核心公式与流程

**[PST 承诺]**
$$ \operatorname{pst}(f) = g_1^{f(s_\ell, \dots, s_1)} = \prod_{j=0}^{n-1} \left(g_1^{\mathcal{S}_{j,\ell}(\mathbf{s})}\right)^{a_j} $$
> 作用：利用可信设置产生的公共参数，在不暴露陷阱门 $\mathbf{s}$ 的情况下计算向量的摘要。该承诺具有同态性：$\operatorname{pst}(f+f') = \operatorname{pst}(f) \cdot \operatorname{pst}(f')$。

**[PST 验证方程（单个证明）]**
$$ e(\mathsf{C}/g_1^{a_i}, g_2) = \prod_{j=1}^{\ell} e(w_j, g_2^{s_j - i_j}) $$
> 作用：通过 ℓ+1 个配对运算验证位置 i 的值 $a_i$ 与摘要 C 的一致性。证明 $\pi_i = (w_1, \dots, w_\ell)$ 是对应商多项式的承诺。

**[MLT 单节点更新]**
$$ w_{u,k}' = w_{u,k} \cdot (g_1^{\mathcal{S}_{u,k-1}(\mathbf{s})})^{\delta}, \quad \forall k \in [\ell] $$
> 作用：当位置 u 的值变化 $\delta$ 时，更新 MLT 中沿 u 路径的节点承诺。更新密钥 $\text{upk}_{u,k-1} = g_1^{\mathcal{S}_{u,k-1}(\mathbf{s})}$ 来自公共参数的相应子集。

**[水印证明的验证]**
$$ e(\mathsf{C}/g_1^{a_i}, g_2^{\alpha}) = \prod_{j=1}^{\ell} e(w_j^{\alpha}, g_2^{s_j - i_j}) $$
> 作用：将原始证明 $\pi_i$ 的每个分量用 $\alpha$ 指数化后，验证者使用水印公钥 $g_2^{\alpha}$ 进行验证，确保证明与计算者身份绑定。

### 实验结果

实验在 Intel Core i7-4770 CPU（3.40GHz，8 核，32 GiB RAM）上单线程运行，使用 Golang 绑定 mcl 库实现 BLS12-381 曲线。对于向量大小 $n = 2^{30}$，单个证明大小为 1.44 KiB，单一证明验证时间 10.93 毫秒。更新全部证明仅需 2.58 毫秒，而 Pointproofs 需 31.7 小时。聚合 1024 个证明耗时 123 秒，聚合证明大小为 51.6 KiB，验证聚合证明需 17.4 秒。与 SNARK 聚合 Merkle 树相比，Hyperproofs 的聚合速度比基于 Poseidon 哈希的 Merkle 树快 10 倍，比基于 Pedersen 哈希的 Merkle 树快 41 倍。在无状态加密货币模拟中（树高 ℓ=30，每个区块 1024 笔交易，P2P 网络直径 h=20），总开销（区块提议 + 20 倍区块验证 + 证明维护）为 8 分钟，而基于 Poseidon 和 Pedersen 的 Merkle 树方案分别为 81 分钟和 332 分钟。公共参数在 $n = 2^{28}$ 时为 24 GiB。

### 局限性与开放问题
Hyperproofs 的公共参数大小为 O(n)，需要可信设置，虽然可通过安全多方计算实现，但规模扩展至 $n \approx 2^{30}$ 仍需工程努力。聚合证明的验证时间需 $O(b\ell)$ 的 $\mathbb{G}_2$ 指数运算，导致其验证速度远慢于 SNARK 方案（17.4 秒对比 0.18 秒）。在安全性上，自适应安全规约损失了 $\log_2 n$ 比特的安全性。此外，论文未探索完全集成不可窃取证明于无状态加密货币的细节，也未考虑所有共识层面的微妙开销。未来工作可期望将方案扩展到隐藏阶群以消除可信设置，或利用更灵活的内积论证实现聚合证明的更新。

### 强关联论文

[12] Dan Boneh, Benedikt Bünz, and Ben Fisch. Batching Techniques for Accumulators with Applications to IOPs and Stateless Blockchains. **CRYPTO 2019** [Google Scholar](https://scholar.google.com/scholar?q=Batching+Techniques+for+Accumulators+with+Applications+to+IOPs+and+Stateless+Blockchains)

[19] Benedikt Bünz, Mary Maller, Pratyush Mishra, Nirvan Tyagi, and Psi Vesely. Proofs for Inner Pairing Products and Applications. **ePrint 2019/1177** [Google Scholar](https://scholar.google.com/scholar?q=Proofs+for+Inner+Pairing+Products+and+Applications)

[20] Matteo Campanelli, Dario Fiore, Nicola Greco, Dimitris Kolonelos, and Luca Nizzardo. Incrementally Aggregatable Vector Commitments and Applications to Verifiable Decentralized Storage. **ASIACRYPT 2020** [Google Scholar](https://scholar.google.com/scholar?q=Incrementally+Aggregatable+Vector+Commitments+and+Applications+to+Verifiable+Decentralized+Storage)

[28] Sergey Gorbunov, Leonid Reyzin, Hoeteck Wee, and Zhenfei Zhang. Pointproofs: Aggregating Proofs for Multiple Vector Commitments. **CCS 2020** [Google Scholar](https://scholar.google.com/scholar?q=Pointproofs%3A+Aggregating+Proofs+for+Multiple+Vector+Commitments)

[46] Charalampos Papamanthou, Elaine Shi, and Roberto Tamassia. Signatures of Correct Computation. **TCC 2013** [Google Scholar](https://scholar.google.com/scholar?q=Signatures+of+Correct+Computation)

[48] Charalampos Papamanthou, Elaine Shi, Roberto Tamassia, and Ke Yi. Streaming Authenticated Data Structures. **EUROCRYPT 2013** [Google Scholar](https://scholar.google.com/scholar?q=Streaming+Authenticated+Data+Structures)

[58] Alin Tomescu. How to Keep a Secret and Share a Public Key (Using Polynomial Commitments). **PhD thesis, MIT 2020** [Google Scholar](https://scholar.google.com/scholar?q=How+to+Keep+a+Secret+and+Share+a+Public+Key+(Using+Polynomial+Commitments))

[59] Alin Tomescu, Ittai Abraham, Vitalik Buterin, Justin Drake, Dankrad Feist, and Dmitry Khovratovich. Aggregatable Subvector Commitments for Stateless Cryptocurrencies. **SCN 2020** [Google Scholar](https://scholar.google.com/scholar?q=Aggregatable+Subvector+Commitments+for+Stateless+Cryptocurrencies)

[64] Benjamin Wesolowski. Efficient Verifiable Delay Functions. **EUROCRYPT 2019** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+Verifiable+Delay+Functions)


## 关键词

+ Hyperproofs向量承诺聚合
+ 可维护向量承诺方案
+ 同态向量承诺
+ 无状态加密货币
+ Merkle证明聚合优化
+ 椭圆曲线代数哈希
