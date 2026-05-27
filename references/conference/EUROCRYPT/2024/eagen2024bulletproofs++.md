---
title: "Bulletproofs++: Next generation confidential transactions via reciprocal set membership arguments"
doi: 10.1007/978-3-031-58740-5_9
标题简称: 
论文类型: conference
会议简称: EUROCRYPT
发表年份: 2024
created: 2025-04-15 17:19:43
modified: 2025-04-22 16:18:29
---
## Bulletproofs++: Next generation confidential transactions via reciprocal set membership arguments

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-58740-5_9?fromPaywallRec=false)

## 作者

+ Liam Eagen 
+ Sanket Kanjalkar 
+ Tim Ruffing 
+ Jonas Nick 

## 笔记

### 背景与动机
机密交易通过同态承诺隐藏加密货币中的交易金额，但必须附带范围证明来防止因金额溢出而非法造币。Bulletproofs系列协议因支持对数级证明大小和透明设置而成为机密交易中范围证明的主流方案。然而，即便经过Bulletproofs+等改进，在通用曲线（如secp256k1）上单个64位范围证明的大小和验证时间仍然构成显著负担，在采用这类曲线的区块链中，范围证明占用了典型交易体积的29%至42%。此外，在多资产机密交易场景中，现有方案需要额外的满射证明或复杂电路来证明资产类型的置换，这些附加证明体积庞大，且无法与BP范围证明聚合，导致效率低下。本文旨在填补这一空白：在不改变安全假设和接口的前提下，提出一种能同时提升单证明和多证明效率、并自然支持多资产机密交易的新协议。

### 相关工作

[8] Bünz等. Bulletproofs: Short Proofs for Confidential Transactions and More. **IEEE S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Bulletproofs%3A%20Short%20Proofs%20for%20Confidential%20Transactions%20and%20More)
> 核心思路：通过递归内积论证实现对数级大小的范围证明，支持聚合证明和透明设置。
> 局限与区别：证明大小和验证时间仍有较大优化空间；其内积论证在对称折叠时效率较低，且分支结构不匹配最优基的范围证明需求。

[15] Chung等. Bulletproofs+: Shorter Proofs for a Privacy-Enhanced Distributed Ledger. **IEEE Access 2022** [Google Scholar](https://scholar.google.com/scholar?q=Bulletproofs%2B%3A%20Shorter%20Proofs%20for%20a%20Privacy-Enhanced%20Distributed%20Ledger)
> 核心思路：引入加权内积论证，减少证明大小并提高证明速度，单个64位范围证明为576字节。
> 局限与区别：其单证明大小仍为本文的416字节所超越；在聚合32个证明时，其验证时间约为本文的5.5倍。

[51] Wang, Chau. Flashproofs: Efficient Zero-Knowledge Arguments of Range and Polynomial Evaluation with Transparent Setup. **ASIACRYPT 2022** [Google Scholar](https://scholar.google.com/scholar?q=Flashproofs%3A%20Efficient%20Zero-Knowledge%20Arguments%20of%20Range%20and%20Polynomial%20Evaluation%20with%20Transparent%20Setup)
> 核心思路：结合BP内积论证与Groth多项式承诺以降低验证者复杂度，优化以太坊Gas消耗。
> 局限与区别：证明大小远大于BP++，在聚合8个64位证明时需65个群元素加28个标量，而BP++仅需14个群元素加5个标量。

[52] Wang, Chau, Liu. SwiftRange: A Short and Efficient Zero-Knowledge Range Argument for Confidential Transactions and More. **ePrint 2023** [Google Scholar](https://scholar.google.com/scholar?q=SwiftRange%3A%20A%20Short%20and%20Efficient%20Zero-Knowledge%20Range%20Argument%20for%20Confidential%20Transactions%20and%20More)
> 核心思路：提出另一种紧凑范围证明，但证明大小约为BP++单证明的两倍。
> 局限与区别：其证明大小在1×64时为16个群元素加9个标量，远超BP++的10个群元素加3个标量。

[43] Poelstra等. Confidential Assets. **FC 2018** [Google Scholar](https://scholar.google.com/scholar?q=Confidential%20Assets)
> 核心思路：提出多资产机密交易协议，使用满射证明隐藏资产类型。
> 局限与区别：满射证明大小随输入数量线性增长，无法与范围证明聚合，且不支持多方可证明。

[50] de Valence等. Cloak. **2019** [Google Scholar](https://scholar.google.com/scholar?q=Cloak)
> 核心思路：将MACT的置换论证编码为BP算术电路，避免满射证明。
> 局限与区别：电路构造过复杂，导致证明者计算开销显著增大，且与多方可证明不兼容；BP++通过倒数论证直接支持MACT，边际开销几乎为零。

[21] Gabizon, Williamson. plookup: A Simplified Polynomial Protocol for Lookup Tables. **ePrint 2020** [Google Scholar](https://scholar.google.com/scholar?q=plookup%3A%20A%20Simplified%20Polynomial%20Protocol%20for%20Lookup%20Tables)
> 核心思路：利用多项式承诺实现查找参数，是Plonk协议的核心组件。
> 局限与区别：本文的倒数论证是其多项式形式下的对数导数版本，具有更优的线性化结构，且能直接嵌入BP++的算术电路框架。

[22] Gabizon, Williamson, Ciobotaru. PLONK: Permutations over Lagrange-bases for Oecumenical Noninteractive Arguments of Knowledge. **ePrint 2019** [Google Scholar](https://scholar.google.com/scholar?q=PLONK%3A%20Permutations%20over%20Lagrange-bases%20for%20Oecumenical%20Noninteractive%20Arguments%20of%20Knowledge)
> 核心思路：标准化算术电路零知识证明框架，通过置换论证验证电路约束。
> 局限与区别：其置换论证依赖于配对和可信设置，而BP++基于离散对数困难假设和透明设置，更适用于加密货币环境。

[16] Couteau等. Efficient Range Proofs with Transparent Setup from Bounded Integer Commitments. **EUROCRYPT 2021** [Google Scholar](https://scholar.google.com/scholar?q=Efficient%20Range%20Proofs%20with%20Transparent%20Setup%20from%20Bounded%20Integer%20Commitments)
> 核心思路：提出有界整数承诺方案，基于离散对数假设实现高效的平方和范围证明。
> 局限与区别：其承诺方案要求群的大小略大于256位，限制了在secp256k1等标准曲线上的直接应用；且BP++的证明大小更小。

### 核心技术与方案

BP++由三个核心组件构成。第一个是**范数线性论证**，它替代了BP和BP+的内积论证。该论证利用对称折叠策略，即对向量n的左右半部采用系数为(ρ⁻¹, γ)而非(γ, γ⁻¹)的折叠方式，使得当x=y时折叠后的向量仍然相等。这种方法将验证者处理两个向量相关运算的计算量减半，并使协议能直接处理形如v = ⟨c, l⟩ + |n|_μ²的加权范数线性关系。这使得二进制范围证明可通过约束(2d_i - 1)² = 1来避免冗余的二次承诺。

第二个核心组件是**算术电路协议**的改进。BP++将电路约束从标准形式w_L ∘ w_R = w_O推广为w_L ∘ w_R等于整个见证的线性组合。这种修改使得可以高效地编码倒数约束：将分母置于w_L，倒数置于w_R，右手边为线性组合。协议通过两次挑战完成：首先由验证者发送ρ, λ, β, δ，证明者发送盲化承诺C_S；随后验证者发送τ，证明者计算v(τ), l(τ), n(τ)并调用范数线性论证证明最终约束。该方式避免了BP中需要的多个额外标量承诺T₁, T₃, T₄, T₅, T₆，从而减少了证明大小和轮数。

第三个也是最重要的组件是**倒数论证**。给定一个集合A = {(m_i, s_i)}，其中m_i为多重度，s_i为符号，该论证证明对所有s的总多重度均为0。构造思路是定义有理函数f_A(X) = Σ m_i/(X + s_i)。如果f_A在足够多的随机点处值为0，则A必然消失（即所有总多重度为0）。协议只需一轮：证明者承诺符号s和多重度m，验证者发送随机挑战α，证明者回复倒数r_i = m_i/(α + s_i)，验证者检查(α + s_i)r_i = m_i且Σ r_i = 0。

将倒数论证嵌入算术电路形成**倒数形式电路**。证明者先承诺初始见证w_I（包含所有分母），验证者发送α，证明者随后承诺倒数w_P(α)和剩余见证。通过这些承诺，原来的倒数约束可以转化为乘法约束：w_{D,i}w'_{P,i} = (W_n w_I + a_n)_i - α w'_{P,i}，以及线性约束。这种转化使得整个协议的安全性可以从基础算术电路协议的安全性直接继承。

基于倒数形式电路构造的范围证明**利用最优基而非二进制基**。证明者将数值v分解为基b的k个数字d_i，然后使用倒数参数证明每个数字属于集合{0, ..., b-1}，并提供一个线性约束验证Σ b_i d_i = v - A。相比二进制基，这种方法的渐进效率从O(n)提升至O(n/log n)。多资产机密交易则更进一步：对于输入集合I和输出集合O，构建集合A = {(v, t) : (v, t) ∈ I} ∪ {(-v, t) : (v, t) ∈ O}。如果f_A(α) = 0，则每种资产的总输入等于总输出。与范围证明结合后，若所有输出金额在[0, B)内且kB < p，则可确保没有资产被创建或销毁。

系统安全性的证明依赖于离散对数关系问题的期望多项式时间困难性。范数线性论证通过构造基于线性无关多项式1, γ, γ²-1的轮提取器来实现计算性见证扩展仿真。算术电路协议证明其满足完美完备性和完美SHVZK，且在DLR假设下具有CWEE。倒数形式电路协议通过要求在α处的一次额外提取来证明CWEE。这些性质都基于透明设置和随机预言机模型。

在通信复杂度方面：单64位范围证明仅需10个群元素和3个标量（约416字节）。聚合m个范围证明时，证明大小约为O(log n + log m)。验证者计算量为O(n/log n)个群元素乘法，显著优于BP和BP+的O(n)。

### 核心公式与流程

**[范数线性关系定义]**
$$ \mathcal{R}_{nl} = \left\{ \binom{\boldsymbol{H} \in \mathbb{G}^l, \boldsymbol{G} \in \mathbb{G}^n, G \in \mathbb{G};}{C \in \mathbb{G}, \boldsymbol{c} \in \mathbb{F}^l, \mu \in \mathbb{F}} \colon \begin{array}{c} v = \langle \boldsymbol{c}, \boldsymbol{l} \rangle + |\boldsymbol{n}|_{\mu}^2 \\ C = v G + \langle \boldsymbol{l}, \boldsymbol{H} \rangle + \langle \boldsymbol{n}, \boldsymbol{G} \rangle \end{array} \right\} $$
> 作用：定义论证证明的核心关系：承诺C中隐藏的标量v等于给定公开向量c与秘密向量l的内积，加上秘密向量n的加权模平方。

**[倒数论证协议]**
$$ \begin{aligned} & \mathcal{P} \to \mathcal{V}: \boldsymbol{m}, \boldsymbol{s} \\ & \mathcal{V} \to \mathcal{P}: \alpha \xleftarrow{\$} \mathbb{F} \\ & \mathcal{P} \to \mathcal{V}: \boldsymbol{r} \text{ s.t. } r_i = m_i / (\alpha + s_i) \\ & \mathcal{V}: \text{accept if } (\alpha + s_i) r_i = m_i \ \forall i \ \land \ \sum_i r_i = 0 \end{aligned} $$
> 作用：核心交互协议，证明者使用随机挑战α证明一个集合的总多重度为零，这是所有高级构造的基础。

**[倒数论证有理函数]**
$$ f_A(X) = \sum_{(m,s) \in A} \frac{m}{X + s} = \sum_{s \in S} \frac{\hat{m}_s}{X + s} $$
> 作用：将集合A的多重度性质编码为有理函数。若所有总多重度为零，则f_A恒为零；反之，若f_A在足够多随机点处为零，则集合以压倒性概率消失。

**[范数折叠公式]**
$$ \begin{aligned} \boldsymbol{n}' &= \rho^{-1} [\boldsymbol{n}]_0 + \gamma [\boldsymbol{n}]_1 \\ \boldsymbol{G}' &= \rho [\boldsymbol{G}]_0 + \gamma [\boldsymbol{G}]_1 \\ \boldsymbol{l}' &= [\boldsymbol{l}]_0 + \gamma [\boldsymbol{l}]_1 \\ \boldsymbol{H}' &= [\boldsymbol{H}]_0 + \gamma [\boldsymbol{H}]_1 \\ C' &= C + \gamma X + (\gamma^2 - 1) R \end{aligned} $$
> 作用：范数线性论证中一轮折叠的核心公式。证明者发送X和R后，验证者选择γ，双方通过对称折叠将问题规模减半，同时保证如果C'正确则原C正确。

**[算术电路约束转换]**
$$ 0 = \mathbf{e}_{N_l}(\lambda)^\top (W_l \boldsymbol{w} + \boldsymbol{w}_V + \boldsymbol{a}_l) + \langle \boldsymbol{w}_L, \boldsymbol{w}_R \rangle_{\mu} - \mathbf{e}_{N_m}(\mu)^\top (W_m \boldsymbol{w} + \boldsymbol{a}_m) $$
> 作用：验证者使用挑战λ和μ将矩阵约束转换为单个标量方程，结合随机挑战β和δ实现盲化，最终通过范数线性论证证明电路满足性。

**[倒数形式电路乘法约束]**
$$ w_{D,i} w'_{P,i} = (W_n \boldsymbol{w}_I + \boldsymbol{a}_n)_i - \alpha w'_{P,i} $$
> 作用：将倒数定义r_i = m_i/(α + s_i)转化为乘法约束，验证者检查此约束可确信证明者提供的倒数是根据其承诺的分子和分母正确计算的。

### 实验结果

实验环境基于Intel i7-10510U 1.80GHz单线程处理器，使用C语言实现并基于libsecp256k1-zkp库，利用secp256k1椭圆曲线，所有秘密数据操作均为常数时间。核心性能数据：单个64位范围证明的证明时间为4.041毫秒，验证时间为0.840毫秒。相比BP+在Ristretto255曲线上的实现（更快的群运算），BP++的证明时间快了约3倍，验证时间快了约2.2倍。相比BP在secp256k1上的实现，证明时间快了约5倍，验证时间快了约3倍。聚合32个64位范围证明时，BP++的证明时间为52.108毫秒，验证时间为6.424毫秒，相比BP+分别提升约5.9倍和5.4倍。BP++的证明大小为416字节，相比BP的672字节缩小38%，相比BP+的576字节缩小27%。实验还展示了随着总比特数增加时性能的近似线性增长特征，证明者时间和验证者时间均符合O(n/log n)的预期。

### 局限性与开放问题

BP++的安全性依赖于随机预言机模型，在标准模型下能否证明其安全性仍是一个开放问题。虽然协议支持聚合证明，但并未设计为可递归组合的，即不支持像Halo那样的嵌套证明结构。此外，协议设计中的某些常数（如停止条件|n|+|l| ≤ 6）基于经验选择，理论上可进一步优化，但本文未提供系统性的分析框架。

### 强关联论文

[8] Bünz B., Bootle J., Boneh D., Poelstra A., Wuille P., Maxwell G. Bulletproofs: Short Proofs for Confidential Transactions and More. **IEEE S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Bulletproofs%3A%20Short%20Proofs%20for%20Confidential%20Transactions%20and%20More)

[15] Chung H., Han K., Ju C., Kim M., Seo J.H. Bulletproofs+: Shorter Proofs for a Privacy-Enhanced Distributed Ledger. **IEEE Access 2022** [Google Scholar](https://scholar.google.com/scholar?q=Bulletproofs%2B%3A%20Shorter%20Proofs%20for%20a%20Privacy-Enhanced%20Distributed%20Ledger)

[43] Poelstra A., Back A., Friedenbach M., Maxwell G., Wuille P. Confidential Assets. **FC 2018** [Google Scholar](https://scholar.google.com/scholar?q=Confidential%20Assets)

[50] Valence H., Yun C., Andreev O. Cloak. **2019** [Google Scholar](https://scholar.google.com/scholar?q=Cloak)

[21] Gabizon A., Williamson Z.J. plookup: A Simplified Polynomial Protocol for Lookup Tables. **ePrint 2020** [Google Scholar](https://scholar.google.com/scholar?q=plookup%3A%20A%20Simplified%20Polynomial%20Protocol%20for%20Lookup%20Tables)

[22] Gabizon A., Williamson Z.J., Ciobotaru O. PLONK: Permutations over Lagrange-bases for Oecumenical Noninteractive Arguments of Knowledge. **ePrint 2019** [Google Scholar](https://scholar.google.com/scholar?q=PLONK%3A%20Permutations%20over%20Lagrange-bases%20for%20Oecumenical%20Noninteractive%20Arguments%20of%20Knowledge)

[16] Couteau G., Klooß M., Lin H., Reichle M. Efficient Range Proofs with Transparent Setup from Bounded Integer Commitments. **EUROCRYPT 2021** [Google Scholar](https://scholar.google.com/scholar?q=Efficient%20Range%20Proofs%20with%20Transparent%20Setup%20from%20Bounded%20Integer%20Commitments)

[51] Wang N., Chau S.C.-K. Flashproofs: Efficient Zero-Knowledge Arguments of Range and Polynomial Evaluation with Transparent Setup. **ASIACRYPT 2022** [Google Scholar](https://scholar.google.com/scholar?q=Flashproofs%3A%20Efficient%20Zero-Knowledge%20Arguments%20of%20Range%20and%20Polynomial%20Evaluation%20with%20Transparent%20Setup)

[52] Wang N., Chau S.C.-K., Liu D. SwiftRange: A Short and Efficient Zero-Knowledge Range Argument for Confidential Transactions and More. **ePrint 2023** [Google Scholar](https://scholar.google.com/scholar?q=SwiftRange%3A%20A%20Short%20and%20Efficient%20Zero-Knowledge%20Range%20Argument%20for%20Confidential%20Transactions%20and%20More)


## 关键词

+ Bulletproofs++
+ 范围证明
+ 保密交易
+ 集合成员证明
+ 离散对数假设
+ 零知识证明