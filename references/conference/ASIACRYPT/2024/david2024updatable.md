---
title: Updatable Privacy-Preserving Blueprints
doi: 10.1007/978-981-96-0875-1_4
标题简称: 
论文类型: conference
会议简称: ASIACRYPT
发表年份: 2024
modified: 2025-04-21 11:07:05
created: 2025-04-15 14:08:59
---
## Updatable Privacy-Preserving Blueprints

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-981-96-0875-1_4)

## 作者

+ Bernardo David 
+ Felix Engelmann 
+ Tore Frederiksen 
+ [Markulf Kohlweiss](Markulf%20Kohlweiss.md) 
+ Elena Pagnin 
+ Mikhail Volkhov 

## 笔记

### 背景与动机
隐私保护蓝图方案 [KLN23] 允许用户创建一个“托管” escrow，该 escrow 编码了函数 \(P(t,x)\) 的输出值 \(y\)，其中 \(t\) 是审计者设定的秘密阈值，\(x\) 是用户的私有输入。审计者可以非交互地解密 escrow 来学习 \(y\)，而不会获得有关 \(x\) 或 \(t\) 的任何额外信息。然而，原始定义和构造仅支持单个用户在单个时间点提供完整的输入 \(x\)。这远不能应对现实场景中，多个相互不信任的用户需要相继贡献自己的私有输入并累积结果的情形，例如反洗钱系统需要聚合来自不同银行的客户信誉分数，或位置追踪需要累加移动距离。如果使用传统的多方计算，则要求所有参与方同时在线并进行多轮交互，这在用户数量庞大且异步的环境下几乎不可行。本文提出可更新的隐私保护蓝图（UPPB），允许多个用户以非交互方式依次更新已有蓝图中的用户输入，同时保证每个更新仅向审计者暴露最终谓词的真值，而不泄漏各阶段的具体输入值。这一特性使得 UPPB 成为大规模隐私保护审计的理想基础工具。

### 相关工作

[KLN23] M. Kohlweiss, A. Lysyanskaya, A. Nguyen. Privacy-Preserving Blueprints. **EUROCRYPT 2023** [Google Scholar](https://scholar.google.com/scholar?q=Privacy-Preserving+Blueprints)
> 核心思路：首次提出隐私保护蓝图的概念，允许用户创建编码 \(P(t,x)\) 的 escrow，审计者解密获知结果。
> 局限与区别：仅支持单用户输入 \(x\)，无法处理多用户相继更新的场景。本文在此基础增加 Update、VfHistory、VfHint 等功能，实现多用户可更新。

[CH20] G. Couteau, D. Hartmann. Shorter Non-interactive Zero-Knowledge Arguments and ZAPs for Algebraic Languages. **CRYPTO 2020** [Google Scholar](https://scholar.google.com/scholar?q=Shorter+Non-interactive+Zero-Knowledge+Arguments+and+ZAPs+for+Algebraic+Languages)
> 核心思路：提出一种基于双线性群的简洁 NIZK（CH20），支持对代数语言的证明，且证明可用线性变换更新。
> 局限与区别：原始 CH20 的更新性并未被系统分析；本文首次给出其盲化兼容变换的精确定义，并利用它实现 UPPB 中一致性证明的简洁更新。

[Bün+18] B. Bünz, J. Bootle, D. Boneh, A. Poelstra, P. Wuille, G. Maxwell. Bulletproofs: Short Proofs for Confidential Transactions and More. **IEEE S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Bulletproofs+Short+Proofs+for+Confidential+Transactions+and+More)
> 核心思路：构造短的非交互范围证明，用于证明承诺中的值在一定区间内。
> 局限与区别：Bulletproofs 是一般性工具，本文仅在扩展中提及可用于对更新值附加范围限制，但核心方案（uBlu）无需依赖 Bulletproofs 即可实现范围谓词更新。

[Bel+09] M. Belenkiy, J. Camenisch, M. Chase, M. Kohlweiss, A. Lysyanskaya, H. Shacham. Randomizable Proofs and Delegatable Anonymous Credentials. **CRYPTO 2009** [Google Scholar](https://scholar.google.com/scholar?q=Randomizable+Proofs+and+Delegatable+Anonymous+Credentials)
> 核心思路：提出可随机化证明的概念，允许将证明转换为对新实例的有效证明。
> 局限与区别：该工作主要关注凭证委托，本文所需求的是对实例和证人同时进行线性变换，且要满足盲化兼容条件，比简单随机化更强。

[Cha+12] M. Chase, M. Kohlweiss, A. Lysyanskaya, S. Meiklejohn. Malleable Proof Systems and Applications. **EUROCRYPT 2012** [Google Scholar](https://scholar.google.com/scholar?q=Malleable+Proof+Systems+and+Applications)
> 核心思路：提出可塑证明（malleable proofs）的概念，允许公开变换证明的内容，并给出应用。
> 局限与区别：可塑证明强调变换的灵活性，UPPB 需要的是受限的、仅支持线性更新的变换，且要保证推导隐私性（derivation privacy），本文将其具体化为盲化兼容变换。

### 核心技术与方案

**整体框架**。UPPB 扩展了原始蓝图，引入 hint、tag、commitment 等新组件。初始时，审计者运行 KeyGen 生成密钥对 (sk, pk) 和初始 hint₀，其中 hint₀ 包含一组 ElGamal 加密的阈值 \(t\) 的幂，以及一个 NIZK 证明 \(\pi_c\) 保证加密的正确性。用户可以利用 Update 算法：给定上一个 hint\(_{i-1}\) 和 tag\(_{i-1}\)，以及自己的私有输入 \(x_i\) 和外部承诺的随机数 r，输出新的 hint\(_i\) 和 tag\(_i\)。hint 中隐藏了累积值 \(\hat{x} = \sum_{j=1}^i x_j\) 的幂函数加密形式，而 tag 包含一个 NIZK 证明 \(\pi_t\)，证明 hint\(_i\) 与 hint\(_{i-1}\) 以及外部承诺 \(\mathfrak{C}_i\) 的一致性。任何一方可使用 VfHistory 验证 tag 序列的连贯性。审计者通过 Escrow 算法将 hint 转换为 escrow esc，其中包含一个 ElGamal 加密（经过随机化）以及对 escrow 证明 \(\pi_e\)。审计者随后用 sk 解密，得到 \(P(t, \hat{x})\) 的二进制结果。

**谓词与多项式表示**。本文考虑范围谓词 \(P_d(t,x)\)，当 \(x \in [t, t+d-1]\) 时输出 1，否则 0。该谓词等价于多项式 \(\prod_{\delta=0}^{d-1}(x - t - \delta) = 0\) 的检测。通过 Stirling 数展开，该多项式可写作 \(\sum_{i=0}^d U_i (x-t)^i\)。这一形式使得更新成为可能：当加入新值 \(y\) 时，\((x+y-t)^i\) 可通过二项式定理表达为旧项 \((x-t)^j\) 的线性组合（系数为 \(\binom{i}{j} y^{i-j}\)），从而 hint 中的 ElGamal 加密可以同态更新，无需解密。

**提示的可更新机制**。初始 hint₀ 包含 \(\{A_{0,i}=G^{r_{0,i}}, B_{0,i}=G^{(-t)^i} H^{r_{0,i}}\}_{i=1}^d\)，即对 \((-t)^i\) 的 ElGamal 加密。当第 ι 步加入 \(x_ι\) 时，Update 算法通过 UpdatePowers 函数计算新的加密：\(B_{ι,i} = G^{x_ι^i} \prod_{j=1}^i B_{ι-1,j}^{V_{i,j}(x_ι)} H^{r_{ι,i}}\)，其中 \(V_{i,j}(x)=\binom{i}{j}x^{i-j}\)。此操作利用了加密的同态性质，使得新的密文加密了 \((\hat{x}-t)^i\)，且提示大小保持 \(O(d)\) 不变。类似地，Pedersen 承诺 \(\mathfrak{X}_ι\) 也被更新为 \(\mathfrak{X}_{ι-1} \cdot G^{x_ι} \mathfrak{H}^{r_{x,ι}}\)。

**NIZK 的更新性**。CH20 NIZK 的证明形式为 \((\mathbf{a},\mathbf{d})\)，其中 \(\mathbf{a}=[M(\mathbf{x})]_1\mathbf{s}\)，\(\mathbf{d}=[z]_2\mathbf{w}+[1]_2\mathbf{s}\)。本文定义了盲化兼容变换的概念（Definition 18），并证明对于一致性语言 \(\mathcal{L}_c\)，存在线性变换 \(T_{upd}\) 能同时更新实例、证人和证明本身，且变换后的证明与全新证明不可区分（推导隐私性）。这一性质保证 hint 更新时，\(\pi_c\) 可以简单地通过线性运算更新，而不必重新生成，从而保持 hint 大小与更新次数无关。

**安全性证明思路**。阈值隐藏（Theorem 7）归结于 DDH 假设下的 ElGamal IND-CPA，结合 NIZK 的零知识。标签隐藏（Theorem 8）依赖于 Pedersen 承诺的完美隐藏性和 Π 的零知识。提示隐藏（Theorem 9）通过 d-VDDH 引理（Lemma 2）证明在 DDH 下盲化后的 ElGamal 密文与随机值不可区分。托管隐藏（Theorem 10）最为复杂：首先利用知识可靠性提取承诺中的值，再利用一致性语言的可靠性得到 hint 中加密形式，随后通过 d-VDDH 将 \(\{A_i,D_i\}\) 替换为随机值，最终模拟 escrow 使其分布与真实不可区分。历史绑定（Theorem 5）利用 Π 的强模拟可提取性。可靠性（Theorem 6）综合了 Π 的知识可靠性、\(\Pi_u\) 的可靠性以及 Pedersen 的绑定性质，确保 escrow 解密结果等于谓词在累积输入上的正确值。

**渐进复杂度**。关键参数为多项式次数 d（即范围大小）。一致性的语言大小为 \(O(d)\)，但更新矩阵大小为 \(O(d^2)\)，导致 Update 算法时间复杂度为 \(O(d^2)\)（占主导）。Escrow 算法由于只引入盲化元素，复杂度为 \(O(d)\)。其他算法（KeyGen、VfHint 等）均为 \(O(d)\)。通信复杂度：hint 大小为 \(4d+5\) 个 \(\mathbb{G}_1\) 元素及 \(2d+8\) 个 \(\mathbb{G}_2\) 元素；tag 大小为 \(O(1)\)；escrow 大小为 \(4d+O(1)\) 个 \(\mathbb{G}_1\) 元素。验证 VfHistory 线性依赖于更新次数 ι。

### 核心公式与流程

**范围谓词定义**
$$
P_d(t,x)=\left[ \prod_{\delta=0}^{d-1}(x-t-\delta) \stackrel{?}{=} 0 \right] \in\{0,1\}
$$
> 作用：定义本文所实现的具体谓词，当 \(x\) 落在区间 \([t,t+d-1]\) 时输出1，否则0。

**多项式展开（Stirling 数）**
$$
\prod_{\delta=0}^{d-1}((x-t)-\delta)=\sum_{i=0}^d U_i (x-t)^i
$$
> 作用：将乘积形式的谓词转化为幂次和，便于利用 ElGamal 同态性进行加密与更新。

**二项式更新公式**
$$
(x+y-t)^i=\sum_{j=0}^i \binom{i}{j} y^{i-j}(x-t)^j
$$
> 作用：揭示累积值增加 \(y\) 后，新幂次可由旧幂次线性组合得到，为 hint 中加密的更新提供代数基础。

**更新函数 \(V_{i,j}\) 定义**
$$
V_{i,j}(y):=\binom{i}{j} y^{i-j} \in \mathbb{Z}_q
$$
> 作用：作为更新系数，用于从旧提示计算新提示中的密文。

**传递更新后的 ElGamal 加密形式**
$$
B_{\iota,i}=G^{y^i}\prod_{j=1}^i B_{\iota-1,j}^{V_{i,j}(y)} H^{r_{\iota,i}} \quad,\quad A_{\iota,i}=\prod_{j=1}^i A_{\iota-1,j}^{V_{i,j}(y)} G^{r_{\iota,i}}
$$
> 作用：实现 hint 中加密值的同态更新，使新密文加密 \((\hat{x}-t)^i\) 而无需知道 \(t\)。

**CH20 NIZK 验证方程**
$$
\hat{e}([M(\mathbf{x})]_1,[\mathbf{d}]_2)=\hat{e}(\mathbf{x},[z]_2)\cdot\hat{e}([\mathbf{a}]_1,[1]_2)
$$
> 作用：验证 NIZK 证明 \(\pi=(\mathbf{a},\mathbf{d})\) 对于实例 \(\mathbf{x}\) 的有效性。

**Escrow 中 Evaluate 函数**
$$
E_1=\prod_{i=1}^d (A_i^{U_i})^\beta,\quad E_2=\prod_{i=1}^d (B_i^{U_i})^\beta = G^{\beta\cdot P_d(t,\hat{x})} H^{\beta\sum U_i r_i}
$$
> 作用：将 hint 中的 ElGamal 密文组合成一个加密的谓词值，解密后若得到 \(1_{\mathbb{G}}\) 则谓词真。

### 实验结果

论文使用 Rust 实现了 uBlu 原型，基于 BLS12-381 椭圆曲线和 Arkworks 库。基准测试在 6 核（12 线程）Xeon E-2286G @ 4.00GHz 服务器上运行，Ubuntu 24.04 系统。主要测量不同范围参数 \(d\) 下的各算法耗时，分单线程和并行两种模式（并行利用 rayon 对每行标量乘法进行多线程）。结果显示：Update 和 Escrow 是最慢的算法，其中 Update 呈现明显的二次增长模式（\(O(d^2)\)）。当 \(d=20\) 时，单线程 Update 约需 200 ms，并行版约 100 ms。Escrow 在相同 \(d\) 下单线程约 80 ms。KeyGen、Setup、VfKeyGen、VfHint、VfEscrow 均随 \(d\) 线性增长，例如 VfKeyGen 在 \(d=20\) 时单线程约 40 ms。VfHistory 每个 ι 约需 1.15 ms，Decrypt 小于 1 ms。并行化大约可以使允许的 \(d\) 翻倍而保持相同耗时。所有基准测试期间内存使用低于 50 MB。论文指出仍有优化空间，可望进一步降低常数因子。

### 局限性与开放问题

本文的 uBlu 构造仅直接支持范围谓词（即 \(x\) 是否落在 \([t,t+d-1]\) 内），且要求 \(d\) 较小以保持实用效率（多项式提示长度与 \(d\) 线性相关，更新复杂度二次相关）。对任意多项式谓词的支持需要平方数量级的提示，不够高效。此外，更新值 \(x_i\) 的大小未加限制可能导致范围溢出，需要额外附加范围证明（如 Bulletproofs）来精确控制。非二进制输出（例如揭露用户身份）虽然已给出扩展思路，但未给出完整的构造和安全性分析。分布式解密（阈值审计）也仅作为未来工作提及。最后，本文的安全性基于 DDH 假设，量子安全版本仍有待研究。

### 强关联论文

[KLN23] M. Kohlweiss, A. Lysyanskaya, A. Nguyen. Privacy-Preserving Blueprints. **EUROCRYPT 2023**

[CH20] G. Couteau, D. Hartmann. Shorter Non-interactive Zero-Knowledge Arguments and ZAPs for Algebraic Languages. **CRYPTO 2020**

[Bün+18] B. Bünz, J. Bootle, D. Boneh, A. Poelstra, P. Wuille, G. Maxwell. Bulletproofs: Short Proofs for Confidential Transactions and More. **IEEE S&P 2018**

[Bel+09] M. Belenkiy, J. Camenisch, M. Chase, M. Kohlweiss, A. Lysyanskaya, H. Shacham. Randomizable Proofs and Delegatable Anonymous Credentials. **CRYPTO 2009**

[Cha+12] M. Chase, M. Kohlweiss, A. Lysyanskaya, S. Meiklejohn. Malleable Proof Systems and Applications. **EUROCRYPT 2012**

[Ped92] T. P. Pedersen. Non-Interactive and Information-Theoretic Secure Verifiable Secret Sharing. **CRYPTO 1991**


## 关键词

+ 隐私保护蓝图
+ 可更新方案
+ 全同态加密
+ 零知识证明
+ 反洗钱