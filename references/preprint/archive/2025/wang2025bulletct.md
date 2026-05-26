---
title: "BulletCT: Towards More Scalable Ring Confidential Transactions With Transparent Setup"
标题简称:
论文类型: preprint
预印本简称: archive
发表年份: 2025
modified: 2025-04-17 13:35:37
created: 2025-04-11 11:59:16
---

## BulletCT: Towards More Scalable Ring Confidential Transactions With Transparent Setup

## 发表信息

+ [archive](https://eprint.iacr.org/2025/188)

## 作者

+ [Nan Wang](Nan%20Wang.md) 
+ Qianhui Wang 
+ [Dongxi Liu](Dongxi%20Liu.md)
+ Muhammed F Esgin 
+ Alsharif Abuadbba 

## 笔记

### 背景与动机
区块链上的 RingCT 方案通过密码学证明实现匿名交易，但其包含的零知识证明导致交易规模和验证开销巨大，成为可扩展性的核心瓶颈 [1, 19]。现有方案如 Monero [14]、Omniring [15]、RingCT-3.0 [24] 和 ZGSX23 [25] 在交易大小和验证效率之间面临固有权衡——要么占用较大通信带宽，要么产生高昂的计算成本。此外，可信设置会损害区块链的去中心化特性，而透明设置又会增加设计高效方案的难度。本文首先系统分析了 ZGSX23 提出的 Any-out-of-N 证明，指出其因必须隐藏源账户数量而导致的标签泛滥、假设不兼容及依赖可信设置等严重缺陷。基于该分析，作者认为 K-out-of-N 证明更适合 DLOG 体系的 RingCT 方案，并据此构造了新的签名，同时修复了 ZGSX23 中存在的可链接性漏洞。

### 相关工作

[5] Bünz 等. Bulletproofs: Short Proofs for Confidential Transactions and More. **IEEE S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Bulletproofs+Short+Proofs+for+Confidential+Transactions+and+More)
> 核心思路：通过内积协议和比特分解技术实现对数级通信复杂度的范围证明。
> 局限与区别：Bulletproofs 本身仅解决范围证明问题，本文将其比特分解技术拓展到 K-out-of-N 证明和标签证明中，形成完整的 RingCT 签名。

[14] Kurt 等. Zero to Monero - Second Edition. **技术报告 2020** [Google Scholar](https://scholar.google.com/scholar?q=Zero+to+Monero+Second+Edition)
> 核心思路：Monero 的 RingCT 方案使用 MLSAG 签名与 Bulletproofs 结合，通信复杂度为 $O(|\mathcal{R}||\mathcal{S}| + \log(\beta|\mathcal{T}|))$。
> 局限与区别：Monero 的签名长度随环大小线性增长，本文利用“K-权重”技术实现了更紧凑的 K-out-of-N 证明，从而降低交易规模。

[15] Lai 等. Omniring: Scaling Private Payments without Trusted Setup. **ACM CCS 2019** [Google Scholar](https://scholar.google.com/scholar?q=Omniring+Scaling+Private+Payments+without+Trusted+Setup)
> 核心思路：使用 K 个 N 比特向量构建 K-out-of-N 证明，并通过向量内积建立密钥与标签的倒数关系。
> 局限与区别：Omniring 需要大量计算密集型约束来建立密钥向量与加权和之间的关联，导致验证开销最高。本文的标签证明采用不同的标签实例化，避免了这些约束。

[24] Yuen 等. RingCT 3.0 for Blockchain Confidential Transaction: Shorter Size and Stronger Security. **FC 2020** [Google Scholar](https://scholar.google.com/scholar?q=RingCT+3.0+for+Blockchain+Confidential+Transaction+Shorter+Size+and+Stronger+Security)
> 核心思路：聚合多个 1-out-of-N 证明构建 K-out-of-KN 证明，每个输入使用独立环。
> 局限与区别：RingCT-3.0 的交易规模最大，验证成本中等。本文使用的单一环结构避免了多环带来的通信浪费。

[25] Zheng 等. Leaking Arbitrarily Many Secrets: Any-out-of-Many Proofs and Applications to RingCT Protocols. **IEEE S&P 2023** [Google Scholar](https://scholar.google.com/scholar?q=Leaking+Arbitrarily+Many+Secrets+Any-out-of-Many+Proofs+and+Applications+to+RingCT+Protocols)
> 核心思路：使用“K-权重”技术构造 Any-out-of-N 证明，通过隐藏汉明重量来增强匿名性，并引入 RSA 累加器实现无状态标签方案。
> 局限与区别：Any-out-of-N 证明需要公开 $|\mathcal{R}|$ 个标签，导致交易规模远大于 K-out-of-N 方案；此外累加器引入了可信设置和假设不兼容问题。本文揭示了该方案的可链接性漏洞，并提出了修复方案。

### 核心技术与方案

**方案总览。** BulletCT 是一个基于 DLOG 假设、无需可信设置的 RingCT 签名方案。它包含两个核心组件：一是基于“K-权重”技术的 K-out-of-N 证明，用于证明对环中 $|\mathcal{S}|$ 个源账户私钥的知情；二是全新的标签证明，用于建立源公钥与标签之间的一一对应关系，从而抵抗双花攻击。两个证明均利用 Bulletproofs 的内积协议和比特分解技术实现对数级通信复杂度。

**“K-权重” K-out-of-N 证明。** 该证明要求证明者拥有一个 $|\mathcal{R}|$ 比特向量 $\mathbf{b}$，其汉明重量恰为公开值 $|\mathcal{S}|$。本文通过修改 Bulletproofs 的比特分解约束，将原用于范围证明的承诺值替换为公开的 $|\mathcal{S}|$，得到式 (8) 的核心约束：
$$ \langle \mathbf{y}^{|\mathcal{R}|}, \mathbf{b} \cdot \mathbf{a} \rangle + z \cdot \langle \mathbf{y}^{|\mathcal{R}|}, \mathbf{b} - \mathbf{1}^{|\mathcal{R}|} - \mathbf{a} \rangle + z^2 \cdot \langle \mathbf{1}^{|\mathcal{R}|}, \mathbf{b} \rangle = z^2 \cdot |\mathcal{S}| $$
其中 $\mathbf{a} = \mathbf{1}^{|\mathcal{R}|} - \mathbf{b}$，$\mathbf{y}$ 和 $z$ 为验证者挑战。证明者使用该向量构造加权和 $w = \sum_{k=1}^{|\mathcal{S}|} y^{\phi(k)} s_{\phi(k)}$，并证明其正确性。相比 ZGSX23 的 Any-out-of-N 证明，该证明精简了一个元素，同时实现了与 Bulletproofs 的无缝集成。

**标签证明。** 本文采用标签实例化 $T = \eta^s$，即标签与对应公钥共享相同的秘密钥 $s$ 但使用不同的生成元 $\eta$。核心挑战在于证明源公钥与标签中的“加权和”相等，同时确保标签指数向量是 $(y^{\phi(k)})_{k=1}^{|\mathcal{S}|}$ 的排列。为解决后者，本文利用对数导数技巧（引理 2）将排列约束转化为集合包含约束：$\sum_{i=1}^{|\mathcal{R}|} \frac{b_i}{y^i + x} = \sum_{k=1}^{|\mathcal{S}|} \frac{1}{y^{\phi(k)} + x}$。在协议中，证明者构建两个掩码向量 $\mathbf{v}$ 和 $\mathbf{f}$ 分别隐藏 $(y^{\phi(k)})$ 和 $((y^{\phi(k)}+z)^{-1})$，并通过内积协议 $\langle \mathbf{v}, \mathbf{f} \rangle = \sum_{k=1}^{|\mathcal{S}|} c^k + m_1 e + m_2 e^2$ 实现倒数关系约束。

**完整签名构造。** 利用 Bulletproofs 的压缩技巧，将 K-out-of-N 证明、标签证明、平衡证明和范围证明的向量化方程通过随机挑战 $x$ 拼接成一个整体，进行统一的递归压缩。最终签名的通信复杂度为 $|\mathcal{S}| + 2|\mathcal{T}| + 2\lceil \log(\beta|\mathcal{T}| + |\mathcal{R}| + |\mathcal{S}|) \rceil + 19 + \frac{|\mathcal{R}|}{8}$ 个群元素，验证计算量约为 $(2\beta+1)|\mathcal{T}| + 4|\mathcal{R}| + 3|\mathcal{S}| + 2\lceil \log(\beta|\mathcal{T}| + |\mathcal{R}| + |\mathcal{S}|) \rceil + 17$ 次群指数运算。

### 核心公式与流程

**[K-out-of-N 证明的核心约束]**
$$ \langle \mathbf{y}^{|\mathcal{R}|}, \mathbf{b} \cdot \mathbf{a} \rangle + z \cdot \langle \mathbf{y}^{|\mathcal{R}|}, \mathbf{b} - \mathbf{1}^{|\mathcal{R}|} - \mathbf{a} \rangle + z^2 \cdot \langle \mathbf{1}^{|\mathcal{R}|}, \mathbf{b} \rangle = z^2 \cdot |\mathcal{S}| $$
> 作用：将 Bulletproofs 的比特分解约束中的秘密承诺值替换为公开的源账户数量 $|\mathcal{S}|$，从而证明比特向量的汉明重量等于 $|\mathcal{S}|$。

**[标签证明的核心等式]**
$$ \prod_{i=1}^{|\mathcal{R}|} P_i^{y^i b_i} \cdot \prod_{k=1}^{|\mathcal{S}|} (T_k^d)^{y^{\phi(k)}} = (\tau \cdot \eta^d)^{\sum_{k=1}^{|\mathcal{S}|} y^{\phi(k)} s_{\phi(k)}} $$
> 作用：建立源公钥加权和与标签加权和之间的相等关系，为链接性奠定基础。其中 $d$ 是用于分离生成元 $\tau$ 和 $\eta$ 的随机挑战。

**[排列约束的对数导数形式]**
$$ \sum_{i=1}^{|\mathcal{R}|} \frac{b_i}{y^i + x} = \sum_{k=1}^{|\mathcal{S}|} \frac{1}{y^{\phi(k)} + x} = \sum_{k=1}^{|\mathcal{S}|} \frac{1}{\alpha_k + x} $$
> 作用：利用对数导数技巧将比特向量与标签指数向量的排列关系转化为集合包含约束，其中 $\alpha_k$ 是标签指数向量，$x$ 是随机挑战。

**[内积协议的倒数关系约束]**
$$ \langle \mathbf{v}, \mathbf{f} \rangle = \sum_{k=1}^{|\mathcal{S}|} c^k + m_1 \cdot e + m_2 \cdot e^2 $$
> 作用：通过内积协议实现 $(y^{\phi(k)}+z)$ 与 $(y^{\phi(k)}+z)^{-1}$ 之间的倒数关系，其中 $\mathbf{v}$ 和 $\mathbf{f}$ 是携带来掩码的线性化向量，$c$ 和 $e$ 是随机挑战。

### 实验结果
实验在 Apple M1 Pro 处理器上的 JRE 11 单线程环境中运行，采用 BN-128 椭圆曲线和范围长度 $\beta=64$，对比基线为修复可链接性漏洞后的 ZGSX23 方案。在大致相当的匿名性水平下（使用 ringset-II: $|\mathcal{R}|=64$, $|\mathcal{S}|=16$），随着目标账户数 $|\mathcal{T}|$ 增加，BulletCT 的交易大小从 2.23KB 增长至 3.23KB，相比 ZGSX23 的 3.66KB 至 4.72KB 实现了 1.45 倍至 1.65 倍的通信效率提升。在计算开销方面，BulletCT 的证明者略慢于 ZGSX23，但验证者略快，总体计算成本相近。在不同环大小 $|\mathcal{R}| \in \{32, 64, 128, 256, 512\}$ 的对比中，BulletCT 的交易大小仅为 ZGSX23 的 30% 至 56%，验证成本稳定在 ZGSX23 的约 67%。随着环尺寸增大，BulletCT 在通信方面的优势更加显著。

### 局限性与开放问题
本文给出的分析表明 Any-out-of-N 证明在 DLOG 体系 RingCT 方案中不如 K-out-of-N 证明实用，但作者不排除未来可能出现非固有的改进方案，例如与 DLOG 证明完全兼容的去信任累加器。当前 BulletCT 基于离散对数假设，面临量子计算威胁，未来需要扩展到后量子安全设置，可以参考 MatRiCT 等后量子 RingCT 方案 [10, 11]。另外，当前方案在证明者时间上略高于基线，或许可以通过优化实现进一步改善。

### 强关联论文

[5] Bünz 等. Bulletproofs: Short Proofs for Confidential Transactions and More. **IEEE S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Bulletproofs+Short+Proofs+for+Confidential+Transactions+and+More)

[14] Kurt 等. Zero to Monero - Second Edition. **技术报告 2020** [Google Scholar](https://scholar.google.com/scholar?q=Zero+to+Monero+Second+Edition)

[15] Lai 等. Omniring: Scaling Private Payments without Trusted Setup. **ACM CCS 2019** [Google Scholar](https://scholar.google.com/scholar?q=Omniring+Scaling+Private+Payments+without+Trusted+Setup)

[24] Yuen 等. RingCT 3.0 for Blockchain Confidential Transaction: Shorter Size and Stronger Security. **FC 2020** [Google Scholar](https://scholar.google.com/scholar?q=RingCT+3.0+for+Blockchain+Confidential+Transaction+Shorter+Size+and+Stronger+Security)

[25] Zheng 等. Leaking Arbitrarily Many Secrets: Any-out-of-Many Proofs and Applications to RingCT Protocols. **IEEE S&P 2023** [Google Scholar](https://scholar.google.com/scholar?q=Leaking+Arbitrarily+Many+Secrets+Any-out-of-Many+Proofs+and+Applications+to+RingCT+Protocols)


## 关键词

+ BulletCT环形机密交易可扩展性
+ RingCT签名K-out-of-N离散对数
+ K-Weight技术任意数量证明分析
+ 双重支付抵抗标签证明可链接性
+ 透明设置区块链匿名交易优化