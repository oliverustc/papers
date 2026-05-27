---
title: "Predicate aggregate signatures and applications"
doi: 10.1007/978-981-99-8724-5_9
标题简称:
论文类型: conference
会议简称: ASIACRYPT
发表年份: 2023
created: 2025-04-17 10:54:09
modified: 2025-04-17 10:54:33
---
## Predicate aggregate signatures and applications

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-981-99-8724-5_9)

## 作者

+ Tian Qiu 
+ Qiang Tang 

## 笔记

### 背景与动机

在匿名声誉系统与区块链治理等场景中，需要一种能够聚合多个签名并隐藏签名者身份的密码学原语。例如在YouTube评分或DAO投票等应用中，最终仅需公开一个简洁的累计分数或投票结果，同时要求该结果可公开验证，并确保不存在重复投票或伪造行为。现有的签名聚合方案存在明显瓶颈：多签名与聚合签名虽然能压缩签名，但必须显式提供签名者身份或公钥，导致总证明大小和验证开销至少与阈值线性相关；阈值签名虽可通过单一公钥验证，但依赖可信设置且阈值固定，不支持跨多个消息的聚合；环签名等匿名方案虽然能隐藏签名者身份，却通常不支持灵活的阈值策略或跨消息聚合。此外，属性基签名虽支持谓词验证，但需要可信密钥生成中心且不涉及签名聚合。通用zk-SNARKs虽可提供理论可行性，但证明生成开销巨大，且依赖可信设置和非标准假设。本文旨在提出一个名为谓词聚合签名的新原语，以填补当前方案在同时满足以下特性上的空白：透明设置、签名者匿名性、支持多消息聚合、以及支持对签名者集合的通用谓词验证。

### 相关工作

[14] Boneh等. Aggregate and verifiably encrypted signatures from bilinear maps. **EUROCRYPT 2003** [Google Scholar](https://scholar.google.com/scholar?q=Aggregate+and+verifiably+encrypted+signatures+from+bilinear+maps)
> 核心思路：利用双线性映射将多个不同签名者的签名压缩为一个聚合签名。
> 局限与区别：聚合时必须公开所有签名者公钥，导致通信与验证开销为线性；本文在此基础上引入盲化因子和简洁证明以隐藏签名者身份。

[19] Bünz等. Bulletproofs: Short proofs for confidential transactions and more. **IEEE S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Bulletproofs%3A+Short+proofs+for+confidential+transactions+and+more)
> 核心思路：通过内积论证实现对数大小的零知识证明，适用于范围证明等。
> 局限与区别：其验证时间与位长线性相关；本文对其进行改造并与结构化AFGHO承诺结合，实现了对数规模的对数验证时间。

[23] Daza等. Updateable inner product argument with logarithmic verifier and applications. **PKC 2020** [Google Scholar](https://scholar.google.com/scholar?q=Updateable+inner+product+argument+with+logarithmic+verifier+and+applications)
> 核心思路：通过结构化公共参数实现对数验证时间的内积论证。
> 局限与区别：其参数结构化要求与BLS公钥的随机性不兼容；本文将其与AFGHO承诺结合以兼容随机公钥。

[6] Abe等. Structure-preserving signatures and commitments to group elements. **Journal of Cryptology 2016** [Google Scholar](https://scholar.google.com/scholar?q=Structure-preserving+signatures+and+commitments+to+group+elements)
> 核心思路：提出AFGHO承诺，支持对群元素的承诺并满足加法同态性。
> 局限与区别：该工作主要用于结构保持签名；本文将其扩展为结构化版本，用于构建高效的二进制证明和内配对积论证。

[37] Shoup. Practical threshold signatures. **EUROCRYPT 2000** [Google Scholar](https://scholar.google.com/scholar?q=Practical+threshold+signatures)
> 核心思路：通过秘密分享在固定门限下聚合签名，实现单一公钥验证。
> 局限与区别：需要可信设置，不支持跨消息聚合，且门限固定；本文的PAS可支持透明设置的动态门限。

[13] Boneh等. Compact multi-signatures for smaller blockchains. **ASIACRYPT 2018** [Google Scholar](https://scholar.google.com/scholar?q=Compact+multi-signatures+for+smaller+blockchains)
> 核心思路：利用双线性映射和PoP机制实现紧凑的多签名。
> 局限与区别：需要公开所有签名者公钥；本文方案提供匿名性且仅需对数验证时间。

[7] Attema等. Compressed σ-protocols for bilinear group arithmetic circuits and application to logarithmic transparent threshold signatures. **ASIACRYPT 2021** [Google Scholar](https://scholar.google.com/scholar?q=Compressed+%CF%83-protocols+for+bilinear+group+arithmetic+circuits+and+application+to+logarithmic+transparent+threshold+signatures)
> 核心思路：利用压缩σ协议实现透明设置下的对数大小阈值环签名。
> 局限与区别：其验证时间为线性；本文的PAS实现对数和对数验证时间的同时优化。

### 核心技术与方案

PAS方案的整体框架由三个参与方构成：签名者各自生成密钥对并签名，组合器收集签名并生成最终聚合签名，验证器验证该签名。组合器的工作本质上是证明如下的NP关系，即在给定全体公钥 $\pmb{pk}$、消息 $m_j$ 以及谓词 $\varOmega$ 和描述 $\varDelta$ 的情况下，存在签名者集合 $S_j$ 及其对应签名 $\sigma_{ij}$ 满足签名验证方程和非重复性等谓词要求。

**构造思路**：起点是BLS聚合签名。为隐藏签名者身份，组合器对聚合公钥引入盲化因子 $r$，即 $\widehat{pk}_j = \prod_{i\in S_j} pk_i \cdot \tilde{g}^{r_j}$。关键挑战在于证明这个盲化后的聚合公钥 $\widehat{pk}_j$ 确实对应一个合法的签名者子集，且子集内的公钥均来自注册列表中。为此，核心观察是将签名者集合编码为二进制向量 $\pmb{b}_j$，并承诺该向量。于是，证明 $\widehat{pk}_j$ 的正确性转化为证明该承诺中的向量 $\pmb{b}_j$ 与计算 $\widehat{pk}_j$ 所用向量一致，并且向量各分量在 $\{0,1\}$ 中。

**关键组件之一：结构化AFGHO承诺与内配对积论证**。为了对群元素进行有效承诺，方案采用AFGHO承诺，并引入结构化参数（形如 $g, g^{x_1}, g^{x_2}, g^{x_1x_2}, \ldots$ 的序列）以减少验证时间。在此基础上设计了内配对积论证$\Pi_{\mathsf{IPP}}$，证明一个 $\mathbb{G}_T$ 中的元素等于两个分别用AFGHO承诺承诺的向量 $\pmb{v}_1 \in \mathbb{G}_1^n$ 和 $\pmb{v}_2 \in \mathbb{G}_2^n$ 的内配对积。协议通过递归结构实现对数大小的通信量和验证时间，验证器每轮仅需常数次配对操作和群运算。其HVSZK性质和知识可靠性基于SXDH和DPair-ML假设。

**关键组件之二：二元证明**。为证明承诺的二进制向量 $\pmb{b}$ 的每个分量属于 $\{0,1\}$ 且汉明重量为 $t$，协议将约束转化为一个内积等式 $\langle \pmb{b} - \tau \cdot \mathbf{1}^n, \pmb{y}^n \circ (\pmb{b}' + \tau \cdot \mathbf{1}^n + \boldsymbol{u}_2 \cdot X) \rangle + \ldots$，其中 $\pmb{b}' = \pmb{b} - \mathbf{1}^n$。通过引入盲化多项式 $\boldsymbol{u}_1, \boldsymbol{u}_2$ 和挑战 $y, \tau, x$，验证器最终仅需对一个压缩后的内积等式进行验证。该证明同样实现对数通信量和对数验证时间。当处理 $k$ 个消息时，将 $k$ 个 $n$ 维二进制向量拼接为一个 $k n$ 维向量，并通过聚合二进制证明一次性处理所有阈值的验证，从而避免 $k$ 倍的线性开销。

**系统开销**。组合器的生成开销为 $O(k n)$，签名大小为 $O(k + \log n + \log k + \log |\mathcal{C}|)$，验证器计算开销为 $O(k + \log n + \log k + \log |\mathcal{C}|)$，其中 $\mathcal{C}$ 为通用谓词电路规模。

### 核心公式与流程

**[PAS关系R_PAS]**
$$
\begin{array}{l} R_{\mathrm{PAS}} = \left\{p k _ {1}, \dots , p k _ {n}, m _ {1}, \dots , m _ {k}, \Omega , \Delta ; \left\{\sigma_ {i 1} \right\} _ {i \in S _ {1}}, \dots , \left\{\sigma_ {i k} \right\} _ {i \in S _ {k}}: \right. \\ \operatorname{ParVrfy} \left(p k _ {i}, m _ {j}, \sigma_ {i j}\right) = 1 \forall i \in S _ {j}, j \in [ k ]; \\ S _ {j} \subseteq [ n ], \forall j \in [ k ]; P _ {\Omega} (S _ {1},..., S _ {k}, \Delta) = 1 \} \\ \end{array}
$$
> 作用：形式化定义PAS需要证明的声明：在公开信息（公钥、消息、谓词、描述）下，存在签名者子集和签名，使得所有签名有效且满足谓词。

**[内配对积协议Π_IPP（递归核心步骤，以$n>1$为例）]**
$$
\begin{array}{l} \boldsymbol{v} _ {1} ^ {\prime} \leftarrow \boldsymbol{v} _ {1 \ell} \cdot c + \boldsymbol{v} _ {1 r} \cdot c ^ {- 1} \in \mathbb{G} _ {1} ^ {n/2}, \\ \boldsymbol{v} _ {2} ^ {\prime} \leftarrow \boldsymbol{v} _ {2 \ell} \cdot c ^ {- 1} + \boldsymbol{v} _ {2 r} \cdot c \in \mathbb{G} _ {2} ^ {n/2}, \\ C _ {1} ^ {\prime} \leftarrow c ^ {2} C _ {1 \ell} + C _ {1} + c ^ {- 2} C _ {1 r}, \quad C _ {2} ^ {\prime} \leftarrow c ^ {- 2} C _ {2 \ell} + C _ {2} + c ^ {2} C _ {2 r}, \\ P ^ {\prime} = c ^ {- 2} P _ {\ell} + P + c ^ {2} P _ {r} \\ \end{array}
$$
> 作用：利用随机挑战 $c$ 将内积证明的维度减半，将原长度为 $n$ 的向量压缩为 $n/2$，并更新所有承诺和配对乘积目标值。递归 $\log n$ 轮后得到长度1的平凡情况。

**[二进制协议Π_Bin的核心验证方程]**
$$
P + \phi_ {x} \cdot e _ {H} \stackrel{?}{=} (t \cdot \tau^ {2} + \delta (y, \tau)) \cdot e (g, \tilde{g}) + x \cdot P _ {1} + x ^ {2} \cdot P _ {2}
$$
> 作用：将二进制约束（每个分量在$\{0,1\}$且汉明重量为t）转化为一个单一的内积等式验证。验证器通过检查该等式和两个承诺关系即可确信向量是合法的二进制且重量为t。

**[Combine算法（双线性群上的构造概要）]**
$$
\begin{array}{l} \widehat{PK} = \varPi _ {j=1} ^ {k} \widehat{pk}_j^{z^{(j-1)}} = \pmb{pk}^{\pmb{b}_1} \cdot \pmb{pk}^{z \pmb{b}_2} \cdots \pmb{pk}^{z^{k-1} \pmb{b}_k} \cdot \tilde{g}^{r^*} \\ E = e(g, \widehat{PK}) \\ Q = B + X = \langle [\pmb{b}]_1, \mathsf{ck}_2' \rangle + e(g^{r^*}, \mathsf{ck}_2^*) + (r_B + r_X) \cdot e_H \\ \end{array}
$$
> 作用：组合器通过随机挑战 $z$ 将 $k$ 个子集的二进制向量聚合为一个混合向量，并计算相应的承诺 $Q$ 和公钥配对值 $E$。最终通过 $\Pi_{\mathsf{IPP}}$ 证明 $E$ 等于对应群元素的内配对积，从而一次性验证所有子集公钥的正确性。匿名性由盲化因子 $r_j$ 保证，不泄露具体公钥。

### 实验结果

论文未给出实验数据，仅从理论角度分析了渐进复杂度。其核心性能参数如下：在 $n$ 个用户、$k$ 个消息的场景下，通信开销为 $O(k + \log n + \log k)$，验证计算开销为 $O(k + \log n + \log k)$，组合器计算开销为 $O(k n)$。相比之下，现有BLS聚合签名（需公开所有公钥）的通信和验证开销均为 $O(k n)$；阈值环签名[7]虽达到 $O(\log n)$ 通信，但验证开销仍为 $O(n)$。本文方案当 $n$ 很大时能显著降低验证器负担，例如 $n = 2^{20}$ 时，验证器仅需约 $\log_2(2^{20}) \approx 20$ 轮操作。方案的安全性基于SXDH、DPair-ML和co-CDH假设，不依赖可信设置。

### 局限性与开放问题

本文方案虽然理论渐进复杂度优异，但验证器每轮需进行一次双线性配对，实际运行中配对仍较昂贵。未来可研究如何仅用常数次配对即可完成验证。此外，当前方案不支持对多个已聚合签名进行再次聚合的多层组合，这限制了其在更复杂分层系统中的应用，是一个值得探索的开放问题。

### 强关联论文

[14] Boneh等. Aggregate and verifiably encrypted signatures from bilinear maps. **EUROCRYPT 2003** [Google Scholar](https://scholar.google.com/scholar?q=Aggregate+and+verifiably+encrypted+signatures+from+bilinear+maps)

[19] Bünz等. Bulletproofs: Short proofs for confidential transactions and more. **IEEE S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Bulletproofs%3A+Short+proofs+for+confidential+transactions+and+more)

[23] Daza等. Updateable inner product argument with logarithmic verifier and applications. **PKC 2020** [Google Scholar](https://scholar.google.com/scholar?q=Updateable+inner+product+argument+with+logarithmic+verifier+and+applications)

[6] Abe等. Structure-preserving signatures and commitments to group elements. **Journal of Cryptology 2016** [Google Scholar](https://scholar.google.com/scholar?q=Structure-preserving+signatures+and+commitments+to+group+elements)

[37] Shoup. Practical threshold signatures. **EUROCRYPT 2000** [Google Scholar](https://scholar.google.com/scholar?q=Practical+threshold+signatures)

[13] Boneh等. Compact multi-signatures for smaller blockchains. **ASIACRYPT 2018** [Google Scholar](https://scholar.google.com/scholar?q=Compact+multi-signatures+for+smaller+blockchains)

[7] Attema等. Compressed σ-protocols for bilinear group arithmetic circuits and application to logarithmic transparent threshold signatures. **ASIACRYPT 2021** [Google Scholar](https://scholar.google.com/scholar?q=Compressed+%CF%83-protocols+for+bilinear+group+arithmetic+circuits+and+application+to+logarithmic+transparent+threshold+signatures)


## 关键词

+ 谓词聚合签名
+ 匿名签名
+ 聚合签名
+ 环签名
+ 隐私保护