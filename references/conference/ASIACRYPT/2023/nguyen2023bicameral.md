---
title: "Bicameral and auditably private signatures"
doi: 10.1007/978-981-99-8724-5_10
标题简称:
论文类型: conference
会议简称: ASIACRYPT
发表年份: 2023
created: 2025-05-23 01:55:20
modified: 2025-05-23 01:55:28
---
## Bicameral and auditably private signatures

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-981-99-8724-5_10)

## 作者

+ [Khoa Nguyen](Khoa%20Nguyen.md)
+ Partha Sarathi Roy
+ [Willy Susilo](Willy%20Susilo.md)
+ [Yanhong Xu](Yanhong%20Xu.md)
## 笔记

### 背景与动机
现代隐私保护签名系统，如属性基签名、策略基签名和功能签名，通过细粒度的签名能力控制实现了重要进步，但这些系统普遍只保护属性或策略中的一种，未能同时保护两者。例如，属性基签名保护属性但公开策略，策略基签名保护策略但忽略属性，而多模态私密签名虽同时使用两者却要求策略公开。此外，现有系统通常依赖单一权威机构（属性颁发或策略颁发），无法应对现实中需要两个独立机构分别认证用户属性和组织策略的场景。同时，传统的可问责隐私机制（如群签名）要求签名中嵌入固定信息供指定权威恢复，签名者无法在事后灵活控制泄露哪些具体信息。本文旨在填补这些空白，提出一种新型原语，同时实现属性和策略的隐私保护，并赋予签名者根据审计需求选择性披露部分信息的能力。

### 相关工作

[2] Bellare 等. Policy-based signatures. **PKC 2014** [Google Scholar](https://scholar.google.com/scholar?q=Policy-based+signatures)
> 核心思路：提出策略基签名（PBS），签名者使用一个经过认证的私密策略和公开消息、见证生成签名，但系统不涉及用户属性。
> 局限与区别：PBS 保护策略隐私但不保护属性，且只有一个策略颁发权威，不适用于需要同时隐藏属性和策略的场景。

[11] Chaum 等. Group signatures. **EUROCRYPT 1991** [Google Scholar](https://scholar.google.com/scholar?q=Group+Signatures)
> 核心思路：引入群签名概念，允许群体中任意成员匿名签名，指定权威可追踪签名者身份。
> 局限与区别：可问责隐私要求签名中固定信息可被恢复，签名者无法控制事后选择性披露，与本文的审计隐私本质不同。

[37] Maji 等. Attribute-based signatures. **CT-RSA 2011** [Google Scholar](https://scholar.google.com/scholar?q=Attribute-based+signatures)
> 核心思路：提出属性基签名（ABS），拥有认证且隐私的属性的用户可在满足公开策略的条件下匿名签名。
> 局限与区别：ABS 保护属性但公开策略，且只有属性颁发权威，无法处理策略也需要隐私的场景。

[2] Bellare 等. Policy-based signatures. **PKC 2014** [Google Scholar](https://scholar.google.com/scholar?q=Policy-based+signatures)
> 核心思路：与上文[2]为同一篇。
> 局限与区别：同上。

[8] Boyle 等. Functional signatures and pseudorandom functions. **PKC 2014** [Google Scholar](https://scholar.google.com/scholar?q=Functional+signatures+and+pseudorandom+functions)
> 核心思路：提出功能签名（FS），签名者拥有认证的私密函数，可对函数值域内的消息签名。
> 局限与区别：不涉及用户属性，且只有一个函数认证权威。

[1] Attrapadung 等. Conversions among several classes of predicate encryption... **ASIACRYPT 2015** [Google Scholar](https://scholar.google.com/scholar?q=Conversions+among+several+classes+of+predicate+encryption+and+applications+to+ABE+with+various+compactness+tradeoffs)
> 核心思路：提出谓词签名（PS），是ABS的对偶概念，保护策略隐私但公开属性。
> 局限与区别：保护策略但公开属性，且只有一个策略颁发权威。

[39] Nguyen 等. Multimodal private signatures. **CRYPTO 2022** [Google Scholar](https://scholar.google.com/scholar?q=Multimodal+private+signatures)
> 核心思路：提出多模态私密签名（MPS），同时使用属性和策略，但策略必须公开。
> 局限与区别：策略公开，不符合本文对策略隐私的要求。

[29] Libert 等. Adaptive oblivious transfer with access control from lattice assumptions. **ASIACRYPT 2017** [Google Scholar](https://scholar.google.com/scholar?q=Adaptive+oblivious+transfer+with+access+control+from+lattice+assumptions)
> 核心思路：提出一种格子协议证明函数在NC1内的可满足性，利用Merkle哈希树获取分支程序输入。
> 局限与区别：处理的是分支程序而非布尔电路，且树状搜索复杂度为 $O(\log(K+N) \cdot \lambda \cdot \log \lambda)$，本文采用桶搜索，复杂度更低。

### 核心技术与方案
本文提出一个通用构造和一个基于格的具体实例。通用构造采用“先签名后承诺再证明”的设计范式，将系统拆分为两个签名方案、一个承诺方案和两个非交互零知识证明系统。属性颁发权威和策略颁发权威分别使用各自的签名方案为用户属性和策略颁发凭证。签名时，用户首先验证策略 $P$ 在输入 $(m, \mathbf{x}, w)$ 上求值为1，然后对属性 $\mathbf{x}$ 和策略 $P$ 分别计算承诺 $\mathsf{com}_{\mathbf{x}}$ 和 $\mathsf{com}_{P}$，并生成一个模拟可抽取的非交互零知识论证 $\Pi$，证明存在 $(\mathbf{x}, \mathsf{sk}_{\mathbf{x}}, P, \mathsf{Cert}_P, w)$ 使得 $P(m, \mathbf{x}, w)=1$ 且承诺正确打开。签名 $\Sigma$ 包含两个承诺和论证 $\Pi$，线索包含 $\mathbf{x}$、$P$ 及其承诺随机性。该通用构造的正确性直接源于底层模块的正确性，模拟性依赖于零知识系统的统计零知识性和承诺方案的统计隐藏性，可抽取性依赖于签名方案的存在性不可伪造性、零知识系统的模拟可抽取性以及承诺方案的绑定性。

具体实例基于格困难假设在随机预言机模型下实现。它采用Ducas-Micciancio签名方案为属性和策略颁发凭证，使用Kawachi-Tanaka-Xagawa承诺方案承诺电路输入和位桶，并利用基于Stern型协议的零知识论证系统证明隐藏电路的可满足性和二次披露函数的正确性。核心挑战在于零知识证明一个认证且隐藏的布尔电路 $P$ 在输入 $(m, \mathbf{x}, w)$ 上求值为1。为高效从承诺的比特序列中获取电路门输入，本文提出“桶搜索”方法：将 $K+N-1$ 个比特均分为 $\rho=\sqrt{K+N-1}$ 个桶，每个桶 $\rho$ 比特长，分别承诺得到 $\rho$ 个承诺 $\mathsf{com}_0,\ldots,\mathsf{com}_{\rho-1}$。利用门索引 $g(i)$ 和 $h(i)$ 的二进制分解，将索引拆分为桶编号和桶内偏移，通过证明桶内特定位置比特值来检索门输入，复杂度为 $O(\sqrt{K+N})$。此后，通过证明形如 $s_{K+i} \oplus s_{g(i)} \cdot s_{h(i)} = 1 \bmod 2$ 的NAND门方程组来确保电路正确求值。对于二次披露函数 $F(P,\mathbf{x}) = \mathbf{G}_1 \cdot (\mathbf{b} \otimes_{\text{Kron}} \mathbf{b}) + \mathbf{G}_2 \cdot \mathbf{b} \bmod 2$（其中 $\mathbf{b} = (\mathbf{z}_P^\top | \mathbf{x}^\top)^\top$），系统通过证明Kronecker积和线性组合的正确性来生成可验证的证词-证明对。

系统的渐进复杂度方面，公钥大小为 $O(N \cdot \log(K+N) \cdot \log \lambda + \lambda \cdot (\log \lambda)^2)$ 比特，签名大小（主要由论证 $\Pi$ 贡献）为 $\kappa \cdot O(N \sqrt{K+N} \log \lambda + \lambda \sqrt{K+N} (\log \lambda)^2)$，证明大小为 $\kappa \cdot O(N^2 \cdot \log^2(K+N) + k_2^2)$，其中 $\kappa = \omega(\log \lambda)$ 为重复次数以降低声音误差。

### 核心公式与流程

**通用构造：签名NIZK关系**
$$\mathcal{R}_{\mathsf{S}} := \left\{ \begin{array}{l} \Big((m, \mathsf{vk}_{\mathsf{X}}, \mathsf{vk}_{\mathsf{P}}, \mathsf{pp}_{\mathsf{C}}, \mathsf{com}_{\mathbf{x}}, \mathsf{com}_{\mathsf{P}}), (\mathbf{x}, \mathsf{sk}_{\mathbf{x}}, P, \mathsf{Cert}_{\mathsf{P}}, w, \mathbf{r}_{\mathsf{com},\mathbf{x}}, \mathbf{r}_{\mathsf{com},P}) \Big): \\ \left(P(m, \mathbf{x}, w) = 1\right) \wedge \left(\mathrm{S}_{\mathrm{X}}.\operatorname{Ver}(\mathrm{vk}_{\mathrm{X}}, \mathbf{x}, \mathrm{sk}_{\mathbf{x}}) = 1\right) \wedge \left(\mathrm{S}_{\mathrm{P}}.\operatorname{Ver}(\mathrm{vk}_{\mathrm{P}}, P, \operatorname{Cert}_{P}) = 1\right) \\ \wedge \left(\mathrm{C.Open}(\mathrm{pp}_{\mathrm{C}}, \operatorname{com}_{\mathbf{x}}, \mathbf{x}, \mathbf{r}_{\operatorname{com},\mathbf{x}}) = 1\right) \wedge \left(\mathrm{C.Open}(\mathrm{pp}_{\mathrm{C}}, \operatorname{com}_{P}, P, \mathbf{r}_{\operatorname{com},P}) = 1\right) \end{array} \right\}$$
> 作用：定义了签名时需证明的NP关系，包括策略求值为1、属性和策略被正确认证、以及对它们的承诺正确打开。

**通用构造：披露NIZK关系**
$$\mathcal{R}_{\mathrm{D}} := \left\{ \begin{array}{l} \Big((F, t, \operatorname{com}_{\mathbf{x}}, \operatorname{com}_{P}, \mathfrak{pp}_{C}), (\mathbf{x}, P, \mathbf{r}_{\operatorname{com},\mathbf{x}}, \mathbf{r}_{\operatorname{com},P})\Big): (t = F(P, \mathbf{x})) \\ \wedge \left(C.Open(pp_{C}, com_{\mathbf{x}}, \mathbf{x}, \mathbf{r}_{com,\mathbf{x}}) = 1\right) \wedge \left(C.Open(pp_{C}, com_{P}, P, \mathbf{r}_{com,P}) = 1\right) \end{array} \right\}$$
> 作用：定义了披露时需证明的NP关系，包括信息披露值正确计算以及对属性和策略的承诺正确打开。

**格实例：NAND门求值方程组**
$$
\left\{ \begin{array}{l} s_{K} \oplus s_{g(0)} \cdot s_{h(0)} = 1 \mod 2; \\ s_{K + 1} \oplus s_{g(1)} \cdot s_{h(1)} = 1 \mod 2; \\ \dots\dots \\ s_{K + N - 2} \oplus s_{g(N - 2)} \cdot s_{h(N - 2)} = 1 \mod 2; \\ s_{g(N - 1)} \cdot s_{h(N - 1)} = 0 \mod 2 \end{array} \right.
$$
> 作用：描述了布尔电路 $P$ 的NAND门正确求值的约束，需在零知识中证明这些等式成立。

**格实例：DM签名验证方程（属性密钥）**
$$
\left\{ \begin{array}{l} \left[ \mathbf{A}_{\mathsf{X}} \mid \mathbf{A}_{\mathsf{X},[0]} + \sum_{j=1}^{d} \mathbf{A}_{\mathsf{X},[i]} \cdot t_{\mathbf{x},[i]} \right] \cdot \mathbf{v}_{\mathbf{x}} = y_{\mathbf{x}}; \\ y_{\mathbf{x}} = u_{\mathsf{X}} + \mathbf{F}_{\mathsf{X}} \cdot \text{rdec}(\mathbf{F}_{\mathsf{X},0} \cdot \mathbf{r}_{\mathbf{x}} + \mathbf{F}_{\mathsf{X},1} \cdot \mathbf{x}); \\ \| \mathbf{r}_{\mathbf{x}} \|_{\infty} \leq \beta; \quad \| \mathbf{v}_{\mathbf{x}} \|_{\infty} \leq \beta \end{array} \right.
$$
> 作用：描述了属性签发时Ducas-Micciancio签名的验证条件，需在零知识中证明属性密钥合法。

### 实验结果
论文未提供具体的实验实现或性能数值。这是一篇理论性论文，侧重于提出新原语及正式的安全定义，并通过通用构造和格基实例证明可行性。格基实例使用多个复杂的密码学组件，包括DM签名、KTX承诺、Stern型零知识协议，其渐进复杂度较高。通用构造依赖于高效的NIZK系统（如配对上的Gro


## 关键词

+ 双室签名
+ 可审计隐私
+ 盲签名
+ 隐私保护
+ 数字签名