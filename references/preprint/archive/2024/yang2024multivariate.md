---
title: "Multivariate Multi-Polynomial Commitment and its Applications"
标题简称:
论文类型: preprint
预印本简称: archive
发表年份: 2024
modified: 2025-04-17 13:36:28
created: 2025-04-11 13:56:48
---

## Multivariate Multi-Polynomial Commitment and its Applications

## 发表信息

+ [archive](https://eprint.iacr.org/2024/827)

## 作者

+ [Xiao Yang](Xiao%20Yang.md)
+ [Chengru Zhang](Chengru%20Zhang.md)
+ [Mark Ryan](Mark%20Ryan.md)
+ Gao Meng 

## 笔记

### 背景与动机
多项式承诺是现代高效简洁非交互式知识论证 (SNARK) 的核心构件，允许证明者先承诺一个多项式，而后在特定点打开并证明求值正确。在诸如 HyperPlonk [26] 和 Spartan [55] 等基于多元多项式承诺的 SNARK 中，证明者常常需要同时处理多个多项式，且协议的通信量与验证复杂度随多项式数量线性增长。现有的多多项式承诺方案，如 aPlonk [2] 中的单变量情形，虽已实现对多个单变量多项式的常数级承诺大小和对数级证明大小，但该方案无法直接应用于多元多项式的场景。因此，设计一个针对多个多元多项式、承诺大小为常数且证明大小和验证时间为对数级别的承诺方案，对于实现高效的多实例 SNARK 聚合具有重要意义。本文填补了在多元多项式领域缺少高效多多项式承诺的空白，并探索了其在基于位置证明（如车辆 GPS 轨迹的零知识证明）等新颖应用中的潜力。

### 相关工作

[2] Ambrona et al. aPlonK: Aggregated PlonK from multi-polynomial commitment schemes. **ePrint 2022** [Google Scholar](https://scholar.google.com/scholar?q=aPlonK%3A%20Aggregated%20PlonK%20from%20multi-polynomial%20commitment%20schemes)
> 核心思路：提出了单变量多多项式承诺，通过两层承诺（第一层多项式承诺，第二层 AFGHO 承诺）和 GIPA 协议实现。
> 局限与区别：该方案只针对单变量多项式，无法直接用于 HyperPlonk 等基于多元多项式的 SNARK。本文将其思想推广到多元情形。

[51] Papamanthou et al. Signatures of correct computation. **TCC 2013** [Google Scholar](https://scholar.google.com/scholar?q=Signatures%20of%20correct%20computation)
> 核心思路：提出了 PST 承诺，将 KZG 承诺扩展到多元多项式。
> 局限与区别：PST 承诺本身针对单个多元多项式。本文将其作为第一层承诺的基础，并支持多多项式场景。

[40] Kate et al. Constant-size commitments to polynomials and their applications. **ASIACRYPT 2010** [Google Scholar](https://scholar.google.com/scholar?q=Constant-size%20commitments%20to%20polynomials%20and%20their%20applications)
> 核心思路：提出了经典的 KZG 多项式承诺方案。
> 局限与区别：仅支持单变量多项式。本文的 MMP 承诺方案是 KZG 和 PST 在多功能性上的扩展。

[21] Bünz et al. Proofs for inner pairing products and applications. **ASIACRYPT 2021** [Google Scholar](https://scholar.google.com/scholar?q=Proofs%20for%20inner%20pairing%20products%20and%20applications)
> 核心思路：提出了用于内积对关系的 GIPA 协议。
> 局限与区别：直接使用 GIPA 协议的验证复杂度在无优化时与向量长度线性相关。本文通过其优化技术实现对数级验证，并适配于特定的内积关系。

[26] Chen et al. HyperPlonk: Plonk with linear-time prover and high-degree custom gates. **EUROCRYPT 2023** [Google Scholar](https://scholar.google.com/scholar?q=HyperPlonk%3A%20Plonk%20with%20linear-time%20prover%20and%20high-degree%20custom%20gates)
> 核心思路：提出了基于多元多项式承诺的 SNARK，具有线性时间证明者。
> 局限与区别：处理 k 个实例时，证明大小和验证时间为 O(k log n)。本文的 aHyperPlonk 通过 MMP 承诺将此复杂度降至 O(log k + log n)。

[16] Bünz et al. Bulletproofs: Short proofs for confidential transactions and more. **IEEE S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Bulletproofs%3A%20Short%20proofs%20for%20confidential%20transactions%20and%20more)
> 核心思路：提出了用于 Pedersen 承诺的批量范围证明。
> 局限与区别：该范围证明针对多个独立的 Pedersen 承诺，不能直接用于 Pedersen 子向量承诺。本文设计了新的聚合子协议 (AoK_agg) 以桥接此差距。

[46] Libert. Vector commitments with proofs of smallness: Short range proofs and more. **PKC 2024** [Google Scholar](https://scholar.google.com/scholar?q=Vector%20commitments%20with%20proofs%20of%20smallness%3A%20Short%20range%20proofs%20and%20more)
> 核心思路：针对 Pedersen 子向量承诺提出了常数级大小的范围证明。
> 局限与区别：该方案仅支持向量具有小范数的情况，且验证时间为 O(n·l) 。本文的方案在支持任意元素子集的范围证明上更具灵活性，并通过优化实现了对数级验证。

### 核心技术与方案
本文的核心贡献是 Multivariate Multi-Polynomial (MMP) 承诺方案，其构造思路清晰。MMP 方案采用两层承诺结构：第一层使用 PST 承诺 (PST commitment) 对每个多元多项式分别进行承诺，得到一组 PST 承诺值；第二层使用 AFGHO 承诺对这些 PST 承诺值进行聚合承诺，从而获得常数大小的全局承诺。对于多项式求值，MMP 方案不是一个个证明，而是首先将多个多项式的求值结果通过一个随机挑战 r 聚合为单个值和单个承诺，然后利用 PST 承诺的批处理求值证明 (BatchEval) 来证明聚合后的结果。为了确保聚合过程的正确性，证明者使用 GIPA 协议 (GIPA protocol) 证明聚合承诺 (c_hat_f) 和聚合求值 (e_hat_v) 确实是对原始 PST 承诺和原始求值结果的正确随机线性组合。通过 GIPA 协议的优化技术（如对具有特殊算术结构的向量进行快速求值），验证者可实现对 n 的对数级验证复杂度。该方案的安全性依赖于 PST 承诺的可靠性、AFGHO 承诺的绑定性以及 GIPA 协议的 witness-extended emulation。在代数群模型 (AGM) 下，文章证明了 MMP 承诺满足知识可靠性。

在零知识版本中，方案进一步将基础 PST 承诺替换为隐藏性 PST 承诺 (hiding PST)，并采用 Pedersen 子向量承诺 (Pedersen subvector commitment) 来编码求值结果，同时通过 Schnorr 协议和批处理证明来隐藏和证明聚合求值c_hat_v 的正确性，从而达成零知识性。此零知识 MMP 方案的证明大小约为 $(4 + m + 4\log n)|\mathbb{G}| + (4 + 2\log n)|\mathbb{Z}_p|$ 。

文章还提出了一个针对 Pedersen 子向量承诺的零知识范围证明 (ZKRP)。其核心思想是设计一个名为 AoK_agg 的聚合子协议，该协议允许证明者将一个子向量承诺中的多个元素（通过挑战 z）聚合为一个单一 Pedersen 承诺值 c = g^{sum z^{sigma(i)+1} v_i} h^gamma，并利用双线性对正确性等式 e(c_v, product) = e(c', g) e(c, g_n) 证明聚合的正确性。结合 Bulletproofs 的批量范围证明技术，证明者可以在该聚合值 c 上证明其指数（对应于 v_i 的随机线性组合）位于 [0, 2^l - 1] 区间内，从而间接证明所有原始元素均在范围内。此 ZKRP 协议在优化后，验证复杂度可从 O(nl) 降至 O(8 log(nl) + n + 11) 个群运算。

在应用层面，文章展示了 aHyperPlonk，通过将 MMP 承诺嵌入 HyperPlonk，实现了对 k 个实例的高效聚合。证明者首先对来自所有实例的多项式（如见证多项式 w_i^[j]）一起进行 MMP 承诺，然后在收到挑战后计算聚合的虚拟多项式 F，并利用 MMP 协议的批处理求值证明 F 在超立方体上的所有点求和为零。通过引入一个大小为 O(k) 的元认证关系 R_meta 的 SNARK 证明 (如 HyperPlonk 自身)，最终证明大小和验证时间从 HyperPlonk 的 O(k log n) 降低至 O(log k + log n)，而证明者复杂度保持 O(kn)。另一个应用是车辆 GPS 轨迹的零知识证明。这个应用将“驾驶轨迹是否包含某点”抽象为“点是否在矩形内”的问题，并转化为多项式不等式 (f_1(x,y) < 0 ∧ f_2(x,y) < 0) 。利用零知识 MMP 方案来承诺描述所有矩形 (轨迹) 的多项式，并提供对这些多项式在查询点 (x,y) 处的求值进行范围证明，从而在不泄露全部轨迹的情况下，证明点是否落在某个矩形内。

### 核心公式与流程

**【MMP 承诺构造 (图 3) 】**
$$c_f = \text{afg.Commit}(\text{srs}_{\text{afg}}, \phi), \quad \text{where } \phi \leftarrow (\text{pst.Commit}(\text{srs}_{\text{pst}},f_j))_{j\in[1,n]}$$
$$c_v = \text{ped.Commit}(\text{srs}_{\text{ped}}, \varphi), \quad \text{where } \varphi = (f_j(v))_{j\in[1,n]}$$
> 作用：定义了两层承诺结构。第一层 $\phi$ 是 n 个 PST 承诺，第二层 $c_f$ 是对这 n 个 PST 承诺的 AFGHO 承诺。求值承诺 $c_v$ 是对 n 个求值向量的 Pedersen 承诺。

**【MMP 协议验证等式】**
$$1/0 \gets \text{pst.Eval}(\text{srs}_{\text{pst}}, c_{\hat{f}}, e_{\hat{f}}, v, \pi_{\text{pst}})$$
$$1/0 \gets \text{gipa.Verify}(n, g_{\text{afg}}, c_f, r^n, c_{\hat{f}}, \pi_{\text{gipa}}^{[1]})$$
$$1/0 \gets \text{gipa.Verify}(n, g_{\text{ped}}, c_v, r^n, e_{\hat{v}}, \pi_{\text{gipa}}^{[2]})$$
> 作用：定义了验证者的三个检查。1) 通过 PST 的 Eval 验证聚合承诺 $c_{\hat{f}}$ 在点 v 的求值是 $e_{\hat{f}}$ 。2) 通过 GIPA 验证 $c_{\hat{f}}$ 确实是 $c_f$ 内部的承诺以挑战 r 线性组合而成。3) 通过 GIPA 验证 $e_{\hat{v}}$ 确实是 $c_v$ 内部的求值以挑战 r 线性组合而成。

**【AoK_agg 核心验证等式】**
$$e(c_v, \prod_{i \in S} \widetilde{g}_{n+1-i}^{z^{\sigma(i)+1}}) \stackrel{?}{=} e(c', \widetilde{g}) \cdot e(c, \widetilde{g}_n)$$
> 作用：该配对等式用于证明 Pedersen 子向量承诺 $c_v$ 中索引集 S 的元素被正确聚合成一个单一承诺 c。该等式是连接子向量承诺和 Bulletproofs 范围证明的桥梁。

### 实验结果
文章在配备 Intel i9-12900K CPU 和 64GB RAM 的机器上，使用 Rust 语言和 arkworks 库实现了 MMP 承诺方案，曲线选为 BN254。对于 n=1024 个多项式、每个多项式为 3 变量、最高次为 3 的配置，Commit 算法耗时约 1000ms，Prove 算法耗时约 536.99ms，Eval 算法仅需 18.595ms。Setup 算法在所有测试参数下（多项式数量 2^0 到 2^11 个，变量数 1 到 5）仅需 10-20ms。压缩后的证明大小约为 $32m + 960 \log n + 384$ 字节，对于 m=3, n=1024, 约为 32*3 + 960*10 + 384 = 10080 字节（约 10KB）。实验结果表明，MMP 的承诺和证明生成时间对多项式数量 n 呈近似线性关系，而验证时间呈对数关系，与理论分析一致。与 [44] 的对比显示，本文的 ZKRP 在验证时间上有优势（优化后为 O(log(nl))），但证明大小更大。

### 局限性与开放问题
本文的 MMP 方案需要可信设置（trusted setup）来生成 SRS，虽然这在 SNARK 聚合场景中常见，但限制了其在完全透明环境下的应用。将 MMP 方案扩展到支持透明设置（如基于 DARK [20] 或 Dory [45]）是一个有意义的开放方向。此外，零知识 MMP 方案的实现效率不如基础版本，其实际运行开销有待进一步优化，特别是在证明生成阶段。在 aHyperPlonk 应用中，引入一个额外的元 SNARK 证明增加了系统的复杂性和开销，探索更轻量级的聚合方案（如折叠方案）或许能进一步简化。最后，将车辆 GPS 轨迹证明方案扩展为处理更复杂的轨迹形状（如曲线）并确保在实际车辆系统中的端到端安全性，需要更深入的研究。

### 强关联论文

[2] Ambrona et al. aPlonK: Aggregated PlonK from multi-polynomial commitment schemes. **ePrint 2022** [Google Scholar](https://scholar.google.com/scholar?q=aPlonK%3A%20Aggregated%20PlonK%20from%20multi-polynomial%20commitment%20schemes)

[51] Papamanthou et al. Signatures of correct computation. **TCC 2013** [Google Scholar](https://scholar.google.com/scholar?q=Signatures%20of%20correct%20computation)

[40] Kate et al. Constant-size commitments to polynomials and their applications. **ASIACRYPT 2010** [Google Scholar](https://scholar.google.com/scholar?q=Constant-size%20commitments%20to%20polynomials%20and%20their%20applications)

[21] Bünz et al. Proofs for inner pairing products and applications. **ASIACRYPT 2021** [Google Scholar](https://scholar.google.com/scholar?q=Proofs%20for%20inner%20pairing%20products%20and%20applications)

[26] Chen et al. HyperPlonk: Plonk with linear-time prover and high-degree custom gates. **EUROCRYPT 2023** [Google Scholar](https://scholar.google.com/scholar?q=HyperPlonk%3A%20Plonk%20with%20linear-time%20prover%20and%20high-degree%20custom%20gates)

[16] Bünz et al. Bulletproofs: Short proofs for confidential transactions and more. **IEEE S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Bulletproofs%3A%20Short%20proofs%20for%20confidential%20transactions%20and%20more)

[46] Libert. Vector commitments with proofs of smallness: Short range proofs and more. **PKC 2024** [Google Scholar](https://scholar.google.com/scholar?q=Vector%20commitments%20with%20proofs%20of%20smallness%3A%20Short%20range%20proofs%20and%20more)

[55] Setty. Spartan: Efficient and general-purpose zkSNARKs without trusted setup. **CRYPTO 2020** [Google Scholar](https://scholar.google.com/scholar?q=Spartan%3A%20Efficient%20and%20general-purpose%20zkSNARKs%20without%20trusted%20setup)

[20] Bünz et al. Transparent SNARKs from DARK compilers. **EUROCRYPT 2020** [Google Scholar](https://scholar.google.com/scholar?q=Transparent%20SNARKs%20from%20DARK%20compilers)

[44] Lavaur et al. Boomy: Batch opening of multivariate polynomial commitment. **ePrint 2023** [Google Scholar](https://scholar.google.com/scholar?q=Boomy%3A%20Batch%20opening%20of%20multivariate%20polynomial%20commitment)


## 关键词

+ MMP多变量多项式承诺方案
+ 零知识范围证明Pedersen承诺
+ SNARK聚合HyperPlonk效率优化
+ 车辆GPS轨迹零知识位置证明
+ 常数承诺对数证明多项式方案