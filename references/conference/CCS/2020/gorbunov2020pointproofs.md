---
title: "Pointproofs: Aggregating Proofs for Multiple Vector Commitments"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2020

modified: 2025-05-07 23:22:17
created: 2025-04-07 16:20:38
---

## Pointproofs: Aggregating Proofs for Multiple Vector Commitments

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3372297.3417244)

## 作者

+ Sergey Gorbunov
+ Leonid Reyzin
+ Hoeteck Wee
+ [Zhenfei Zhang](Zhenfei%20Zhang.md)

## 笔记

### 背景与动机
向量承诺允许用户对一组值做出承诺，随后可选择性揭示子集并证明其与原始承诺一致。在区块链等分布式应用中，多个账户各自独立维护承诺，交易涉及多个不同承诺下的值，需要将多个证明压缩为单个短证明以节省带宽。现有子向量承诺方案【LM19】的证明大小为48字节，但仅支持同一承诺内的聚合。Boneh等人【BBF19】和Tomescu等人【TAB+20】实现了同一承诺内的聚合，Campanelli等人【CFG+20】进一步支持增量聚合，但这些方案均无法跨不同承诺进行聚合。Pointproofs首次实现跨承诺非交互聚合，将多个独立承诺下的子向量证明合并为一个48字节的椭圆曲线点，同时满足隐藏性。在区块链智能合约场景中，该方案可将区块传播的带宽开销降低至少60%。

### 相关工作

[LY10] Libert and Yung. Concise Mercurial Vector Commitments and Independent Zero-Knowledge Sets with Short Proofs. **TCC 2010** [Google Scholar](https://scholar.google.com/scholar?q=Concise+Mercurial+Vector+Commitments+and+Independent+Zero-Knowledge+Sets+with+Short+Proofs)
> 核心思路：提出基于配对的向量承诺，承诺大小为单个群元素，每个位置单独证明。
> 局限与区别：不支持子向量聚合，也不支持跨承诺聚合。Pointproofs在此基础上增加聚合算法。

[CF13] Catalano and Fiore. Vector Commitments and Their Applications. **PKC 2013** [Google Scholar](https://scholar.google.com/scholar?q=Vector+Commitments+and+Their+Applications)
> 核心思路：形式化向量承诺并给出基于RSA和配对的构造。
> 局限与区别：同样不支持聚合。

[LM19] Lai and Malavolta. Subvector Commitments with Application to Succinct Arguments. **CRYPTO 2019** [Google Scholar](https://scholar.google.com/scholar?q=Subvector+Commitments+with+Application+to+Succinct+Arguments)
> 核心思路：构造子向量承诺，证明为48字节（双线性群）或256字节（类群）。
> 局限与区别：仅支持同一承诺内子向量证明，不能聚合多个不同承诺的证明。

[BBF19] Boneh, Bünz, Fisch. Batching Techniques for Accumulators with Applications to IOPs and Stateless Blockchains. **CRYPTO 2019** [Google Scholar](https://scholar.google.com/scholar?q=Batching+Techniques+for+Accumulators+with+Applications+to+IOPs+and+Stateless+Blockchains)
> 核心思路：基于RSA累加器实现同一承诺内子向量聚合，证明大小1312字节。
> 局限与区别：仅支持同一承诺聚合，证明较大，不支持跨承诺。

[CFG+20] Campanelli et al. Vector Commitment Techniques and Applications to Verifiable Decentralized Storage. **ePrint 2020/149** [Google Scholar](https://scholar.google.com/scholar?q=Vector+Commitment+Techniques+and+Applications+to+Verifiable+Decentralized+Storage)
> 核心思路：实现增量聚合，可在隐藏阶群方案上反复聚合。
> 局限与区别：仍限于同一承诺内，且聚合不是关联的。

[TAB+20] Tomescu et al. Aggregatable Subvector Commitments for Stateless Cryptocurrencies. **ePrint 2020/527** [Google Scholar](https://scholar.google.com/scholar?q=Aggregatable+Subvector+Commitments+for+Stateless+Cryptocurrencies)
> 核心思路：基于KZG多项式承诺实现同一承诺内聚合，证明48字节。
> 局限与区别：同样不支持跨承诺聚合。

[KZG10] Kate, Zaverucha, Goldberg. Constant-Size Commitments to Polynomials and Their Applications. **ASIACRYPT 2010** [Google Scholar](https://scholar.google.com/scholar?q=Constant-Size+Commitments+to+Polynomials+and+Their+Applications)
> 核心思路：多项式承诺，证明大小恒定，但绑定性不足以防止不一致的子向量打开。
> 局限与区别：TAB+20修复了绑定性，但仍不支持跨承诺。

[BDFG20] Boneh, Drake, Fisch, Gabizon. Efficient Polynomial Commitment Schemes for Multiple Points and Polynomials. **ePrint 2020/081** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+Polynomial+Commitment+Schemes+for+Multiple+Points+and+Polynomials)
> 核心思路：构建多项式承诺的批打开，可转化为向量承诺并支持跨承诺聚合，但效率较低。
> 局限与区别：与Pointproofs相比，验证时需要更多指数运算。

### 核心技术与方案

Pointproofs 基于 Libert-Yung 的配对向量承诺【LY10】扩展聚合能力。设双线性群 $\mathbb{G}_1,\mathbb{G}_2,\mathbb{G}_T$ 阶为 $p$，生成元 $g_1,g_2$，配对 $e:\mathbb{G}_1\times\mathbb{G}_2\to\mathbb{G}_T$。秘密值 $\alpha$ 用于生成公共参数：$g_1^{\alpha},\dots,g_1^{\alpha^N},g_1^{\alpha^{N+2}},\dots,g_1^{\alpha^{2N}}$；$g_2^{\alpha},\dots,g_2^{\alpha^N}$；以及 $g_T^{\alpha^{N+1}}$。注意 $g_1^{\alpha^{N+1}}$ 不在参数中，这是安全性的核心。承诺 $\mathbf{m}=(m_1,\dots,m_N)$ 为 $C:=g_1^{\sum_{i=1}^N m_i\alpha^i}$。对单个位置 $i$ 的证明为 $\pi_i:=g_1^{\sum_{j\neq i}m_j\alpha^{N+1-i+j}}$，验证方程 $e(C,g_2^{\alpha^{N+1-i}})=e(\pi_i,g_2)\cdot g_T^{\alpha^{N+1}m_i}$。同一承诺内的聚合通过随机标量 $t_i=H(i,C,S,\mathbf{m}[S])$ 实现：$\hat\pi:=\prod_{i\in S}\pi_i^{t_i}$，验证 $e(C,g_2^{\sum_{i\in S}\alpha^{N+1-i}t_i})=e(\hat\pi,g_2)\cdot g_T^{\alpha^{N+1}\sum_{i\in S}m_i t_i}$。跨承诺聚合进一步引入 $t_j'=H'(j,\{C_j,S_j,\mathbf{m}_j[S_j]\})$，最终聚合证明 $\pi:=\prod_j \hat\pi_j^{t_j'}$，验证方程涉及多个承诺的乘积。安全证明在代数群模型（AGM）和随机预言机模型（ROM）下，基于 $\ell$-wBDHE* 假设（弱双线性 Diffie-Hellman 指数问题）。核心论证：由于攻击者无法获得 $g_1^{\alpha^{N+1}}$，验证方程中 $\alpha^{N+1}$ 的系数必须匹配，通过随机标量迫使攻击者无法在两个不同消息集合上同时满足聚合方程。隐藏性通过向承诺中引入随机坐标实现，证明与承诺不泄露其他位置信息。方案复杂度：Commit 和 Prove 需要 $\mathsf{nz}(\mathbf{m})$ 次 $\mathbb{G}_1$ 指数运算；Aggregate 需要 $|S|$ 次；Verify 需要 1 次 $\mathbb{G}_1$ 指数、$|S|$ 次 $\mathbb{G}_2$ 指数和 2 次配对；AggregateAcross 需要 $\ell$ 次 $\mathbb{G}_1$ 指数；VerifyAcross 需要 1 次 $\mathbb{G}_1$ 指数、$\sum_j|S_j|$ 次 $\mathbb{G}_2$ 指数和 $\ell+1$ 次配对。

### 核心公式与流程

**[承诺计算]**
$$C:=g_1^{\sum_{i=1}^N m_i\alpha^i}$$
> 作用：将向量 $\mathbf{m}$ 编码为指数多项式在 $\alpha$ 处的求值。

**[单位置证明]**
$$\pi_i:=g_1^{\sum_{j\neq i}m_j\alpha^{N+1-i+j}} = \left(C/g_1^{m_i\alpha^i}\right)^{\alpha^{N+1-i}}$$
> 作用：证明某个位置的值，通过移位使缺失的 $m_i$ 出现在 $\alpha^{N+1}$ 系数处。

**[单位置验证]**
$$e(C,g_2^{\alpha^{N+1-i}})=e(\pi_i,g_2)\cdot g_T^{\alpha^{N+1}m_i}$$
> 作用：依赖 $g_T^{\alpha^{N+1}}$ 的已知性，验证等式两边的 $\alpha^{N+1}$ 系数是否匹配。

**[同一承诺聚合验证]**
$$e\left(C,g_2^{\sum_{i\in S}\alpha^{N+1-i}t_i}\right)=e(\hat\pi,g_2)\cdot g_T^{\alpha^{N+1}\sum_{i\in S}m_i t_i},\quad t_i=H(i,C,S,\mathbf{m}[S])$$
> 作用：通过随机标量 $t_i$ 将多个位置的验证方程线性组合，迫使攻击者无法在子向量内作弊。

**[跨承诺聚合验证]**
$$\prod_{j=1}^\ell e\left(C_j,g_2^{\sum_{i\in S_j}\alpha^{N+1-i}t_{j,i}}\right)^{t_j'}=e(\pi,g_2)\cdot g_T^{\alpha^{N+1}\sum_{j,i}m_{j,i}t_{j,i}t_j'},\quad t_j'=H'(j,\{C_j,S_j,\mathbf{m}_j[S_j]\})$$
> 作用：通过第二层随机标量 $t_j'$ 将多个承诺的验证方程合并，实现跨承诺聚合。

**[隐藏性构造]**
$$\mathsf{Commit}^*(;r):=g_1^r,\quad \mathsf{Prove}^*(\alpha,r,i,m_i):=C^{\alpha^{N+1-i}}\cdot g_1^{-\alpha^{N+1}m_i}$$
> 作用：模拟器在不知道消息向量的情况下生成随机承诺，并利用陷门 $\alpha$ 和待揭示值 $m_i$ 伪造证明，从而实现完美隐藏。

### 实验结果

实验在 Intel Xeon E5-2686 v4 2.30GHz 单线程下运行，使用 Rust 实现和 BLS12-381 曲线。对于 N=1000 的向量，Commit 耗时 54ms；证明单个值（|S|=1）也需 54ms，证明 8 个值（|S|=8）需 280ms（每值 35ms），若一次性计算聚合证明则仅需 83ms。验证单值证明需 4.7ms，验证 8 值证明需 9.9ms（每值 1.2ms）。跨承诺聚合 AggregateAcross 每个承诺仅需 0.06–0.07ms，验证 VerifyAcross 每承诺约 1.9ms（|S|=1）或 5.7ms（|S|=8）。块提议者聚合 4000 个证明耗时 0.25 秒，验证聚合证明耗时 23 秒（每值 0.7ms）。与 BBF、LM-CG、LM-CDH 相比，Pointproofs 的证明开销仅为 48 字节，远低于其他方案；在 4000 笔交易的区块链场景中，Pointproofs 的每块带宽开销约 125KB（含消息数据），而 BBF 超过 5MB，LM-CG 约 1MB，LM-CDH 约 188KB。存储方面，对于 $10^8$ 个账户（每账户 1000 个变量），Pointproofs 仅需 4.5GB 承诺存储，相比明文存储 2980GB 节省 99.8%。

### 局限性与开放问题

Pointproofs 的公共参数大小与向量长度 N 线性相关，在 N 极大时（如 $10^6$）参数生成和存储成本较高。安全证明依赖代数群模型和随机预言机模型，且基于 q-type 假设，在实际安全性评估中需谨慎。聚合算法本身非关联，即已聚合的证明不能进一步与其它证明聚合（除非重新设计）。隐藏性仅在统计意义下成立，且更新操作是确定性的，需要额外重随机化步骤来隐藏前后状态关系。未来可研究基于更标准假设（如 SXDH）的构造，或探索支持无界增量聚合的跨承诺方案。

### 强关联论文

[LY10] Benoît Libert and Moti Yung. Concise Mercurial Vector Commitments and Independent Zero-Knowledge Sets with Short Proofs. **TCC 2010** [Google Scholar](https://scholar.google.com/scholar?q=Concise+Mercurial+Vector+Commitments+and+Independent+Zero-Knowledge+Sets+with+Short+Proofs)

[CF13] Dario Catalano and Dario Fiore. Vector Commitments and Their Applications. **PKC 2013** [Google Scholar](https://scholar.google.com/scholar?q=Vector+Commitments+and+Their+Applications)

[LM19] Russell W. F. Lai and Giulio Malavolta. Subvector Commitments with Application to Succinct Arguments. **CRYPTO 2019** [Google Scholar](https://scholar.google.com/scholar?q=Subvector+Commitments+with+Application+to+Succinct+Arguments)

[BBF19] Dan Boneh, Benedikt Bünz, and Ben Fisch. Batching Techniques for Accumulators with Applications to IOPs and Stateless Blockchains. **CRYPTO 2019** [Google Scholar](https://scholar.google.com/scholar?q=Batching+Techniques+for+Accumulators+with+Applications+to+IOPs+and+Stateless+Blockchains)

[CFG+20] Mattéo Campanelli, Dario Fiore, Nicola Greco, Dimitris Kolonelos, and Luca Nizzardo. Vector Commitment Techniques and Applications to Verifiable Decentralized Storage. **ePrint 2020/149** [Google Scholar](https://scholar.google.com/scholar?q=Vector+Commitment+Techniques+and+Applications+to+Verifiable+Decentralized+Storage)

[TAB+20] Alin Tomescu, Ittai Abraham, Vitalik Buterin, Justin Drake, Dankrad Feist, and Dmitry Khovratovich. Aggregatable Subvector Commitments for Stateless Cryptocurrencies. **ePrint 2020/527** [Google Scholar](https://scholar.google.com/scholar?q=Aggregatable+Subvector+Commitments+for+Stateless+Cryptocurrencies)

[KZG10] Aniket Kate, Gregory M. Zaverucha, and Ian Goldberg. Constant-Size Commitments to Polynomials and Their Applications. **ASIACRYPT 2010** [Google Scholar](https://scholar.google.com/scholar?q=Constant-Size+Commitments+to+Polynomials+and+Their+Applications)

[BDFG20] Dan Boneh, Justin Drake, Ben Fisch, and Ariel Gabizon. Efficient Polynomial Commitment Schemes for Multiple Points and Polynomials. **ePrint 2020/081** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+Polynomial+Commitment+Schemes+for+Multiple+Points+and+Polynomials)


## 关键词

+ 向量承诺
+ 证明聚合
+ 区块链
+ 带宽优化
+ 密码承诺