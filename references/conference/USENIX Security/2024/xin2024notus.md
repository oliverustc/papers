---
title: "Notus: Dynamic Proofs of Liabilities from Zero-knowledge RSA Accumulators"
标题简称: Notus
论文类型: conference
会议简称: USENIX Security
发表年份: 2024
modified: 2025-04-23 09:18:01
created: 2025-04-08 21:18:18
---

## Notus: Dynamic Proofs of Liabilities from Zero-knowledge RSA Accumulators

## 发表信息

+ [原文链接](https://www.usenix.org/conference/usenixsecurity24/presentation/xin)

## 作者

+ [Jiajun Xin](Jiajun%20Xin.md)
+ Arman Haghighi
+ Xiangan Tian
+ [Dimitrios Papadopoulos](Dimitrios%20Papadopoulos.md)

## 笔记

### 背景与动机
动态负债证明（DPoL）系统允许不可信的服务器向用户和审计方证明其在每个时间点（即“纪元”）的负债总额。然而，现实世界中的应用（如加密货币交易所）具有高度动态性，用户负债可任意增减，服务器需定期更新证明。现有方案如DAPOL+ [41]主要关注静态场景，若简单扩展至动态场景，则会为服务器留下“机会窗口”：服务器可在两次用户检查之间暂时降低负债以通过审计，然后恢复数据，从而实施欺诈。TAP系统 [56]虽针对动态场景设计，但仅支持负债单调增加，无法处理用户负债的减少操作（如还款、币种兑换）。此外，在TAP中，若用户连续多个纪元未检查，其恢复检查的计算开销与错过纪元数m呈线性关系。当前工业界的方案（如Binance [6]和OKX [52]）也仅发布相互独立的静态快照，并未提供跨纪元的“链接”证明，无法防止机会窗口攻击。因此，设计一种支持任意（正负）负债更新、且用户可仅在任意时间点进行单次检查就保证安全的DPoL系统，是这一领域填补空白的关键工作。

### 相关工作

[41] Ji et al. Generalized proof of liabilities. **CCS 2021** [Google Scholar](https://scholar.google.com/scholar?q=Generalized+proof+of+liabilities)
> 核心思路：利用Pedersen承诺的Merkle树和范围证明实现静态负债证明。
> 局限与区别：仅支持静态场景，未提供跨纪元的更新一致性证明；安全性依赖于所有用户在每个纪元都进行验证，否则存在机会窗口攻击。

[56] Reijsbergen et al. TAP: transparent and privacy-preserving data services. **USENIX Security 2023** [Google Scholar](https://scholar.google.com/scholar?q=TAP+transparent+and+privacy-preserving+data+services)
> 核心思路：基于追加仅字典和Merkle求和树实现动态负债证明。
> 局限与区别：仅支持负债的单调递增，无法处理负债减少；用户错过检查后的恢复开销与纪元数线性相关；审计方开销与被更新用户数呈线性。

[6] Binance proof-of-reserves [Google Scholar](https://scholar.google.com/scholar?q=Binance+proof-of-reserves)
> 核心思路：利用Merkle树和SNARK证明所有用户负债的总和。
> 局限与区别：仅为静态快照，未提供追加仅性保证；用户位置信息在Merkle路径中泄露，不满足隐私定义。

[52] OKX proof-of-reserves [Google Scholar](https://scholar.google.com/scholar?q=OKX+proof-of-reserves)
> 核心思路：利用Merkle树和STARK证明负债总和。
> 局限与区别：静态快照，证明尺寸过大（约1.2GB），且缺乏追加仅性。

[62] Wesolowski. Efficient verifiable delay functions. **EUROCRYPT 2019** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+verifiable+delay+functions)
> 核心思路：提出基于隐藏阶群的指数证明（PoE）协议。
> 局限与区别：Notus利用其非交互版本（NI-ZKPoKE）作为零知识RSA累加器的子协议。

[53] Ozdemir et al. Scaling verifiable computation using efficient set accumulators. **USENIX Security 2020** [Google Scholar](https://scholar.google.com/scholar?q=Scaling+verifiable+computation+using+efficient+set+accumulators)
> 核心思路：提出MultiSwap协议，用于批量证明累加器的更新。
> 局限与区别：Notus首次将其扩展为零知识版本（ZK-MultiSwap），并用于动态负债证明。

[16] Campanelli et al. Succinct zero-knowledge batch proofs for set accumulators. **CCS 2022** [Google Scholar](https://scholar.google.com/scholar?q=Succinct+zero-knowledge+batch+proofs+for+set+accumulators)
> 核心思路：改进MultiSwap效率（Harisa）。
> 局限与区别：Notus的ZK-MultiSwap在实现零知识的同时仅增加两个海绵哈希验证的开销。

[17] Campanelli et al. LegoSNARK: Modular design and composition of succinct zero-knowledge proofs. **CCS 2019** [Google Scholar](https://scholar.google.com/scholar?q=LegoSNARK+Modular+design+and+composition+of+succinct+zero-knowledge+proofs)
> 核心思路：提出承诺并证明SNARK（CP-SNARK）。
> 局限与区别：Notus利用CP-SNARK实现SNARK电路的模块化组合。

[9] Boneh et al. Batching techniques for accumulators with applications to iops and stateless blockchains. **CRYPTO 2019** [Google Scholar](https://scholar.google.com/scholar?q=Batching+techniques+for+accumulators+with+applications+to+iops+and+stateless+blockchains)
> 核心思路：提出PoKE和ZK-PoKE协议用于RSA累加器的零知识成员证明。
> 局限与区别：Notus设计了更SNARK友好的零知识RSA累加器，避免ZK-PoKE在SNARK中的额外开销。

[34] Ghosh et al. Zero-knowledge accumulators and set algebra. **ASIACRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=Zero-knowledge+accumulators+and+set+algebra)
> 核心思路：提出零知识累加器的形式化定义。
> 局限与区别：Notus是首个将零知识RSA累加器设计为SNARK友好的方案。

### 核心技术与方案

**系统框架**：
Notus系统是一个版本化的账本系统，时间以纪元为单位。服务器在纪元i发布摘要$d_i$，该摘要由两部分组成：零知识RSA累加器$d_i.\text{RSA}$和Pedersen承诺$d_i.\text{Ped}$。累加器存储所有用户的最新哈希链摘要，Pedersen承诺绑定当期负债总额。服务器通过ZK-MultiSwap协议提供跨纪元的更新一致性证明$\pi_i$，确保账本是追加仅的，且负债总和正确更新。

**核心构建模块**：
1.  **哈希链**：每个用户的交易历史被编码为一条洞悉难分（DI）哈希链。用户$u$在纪元$i$的哈希链摘要为$k_u^i = H_{\text{DI}}( \text{tx.id} || \text{tx.lia} || \text{tx.upd} || k_u^{i^-})$，其中$H_{\text{DI}}$是碰撞稳固且洞悉难分的哈希函数。该结构具有传递性和碰撞稳固性。因此，一旦用户在纪元$i$验证了其哈希链摘要$k_u^i$属于$d_i$，则在后续纪元$j>i$中，她仅需验证从$i$到$j$的交易历史$H_u^{i+1,j}$，即可得出当前摘要$k_u^j$，实现了$O(1)$的“追赶”开销。

2.  **零知识RSA累加器**：该方案是Notus的核心隐私引擎。其构造如下：
    *   **KeyGen**: 生成安全RSA模数$N = p' q'$（$p'=2p+1, q'=2q+1$），选取生成元$g,h \in \mathbb{G} = \mathcal{QR}_N \setminus \{1,-1\}$。
    *   **Acc**: 对集合$X = \{x_1,\ldots,x_m\}$和随机数$t$，计算$u = \prod_{i=1}^m H_{\text{DI}}(x_i)$，输出摘要$C = g^{u \cdot t} \bmod N$。这里$t$用于隐藏集合的乘积，实现零知识性质。
    *   **Witness**: 元素$x$的成员证明是$w_x = g^{(\prod_{y \in X \setminus \{x\}} H_{\text{DI}}(y)) \cdot t} \bmod N$，满足$w_x^{H_{\text{DI}}(x)} = C$。验证仅需一次幂运算。非成员证明更复杂，通过NI-ZKPoKE和NI-ZKAoP实现。
    *   **安全性直觉**: 绑定（不可否认性）依赖于强RSA假设和自适应根假设；零知识性质源于随机数$t$，使得累加器值在分布上统计接近均匀，隐藏了集合的乘积信息。
    *   **预计算**: 所有成员证明可通过分治策略在$O(n \log n)$时间内批量预计算。Notus进一步提出“多输出幂运算”优化，通过同时计算多个指数（如$g^{x_1}$和$g^{x_2}$）时共享平方运算，将4倍数幂运算时间降至原生方法的40%左右。

3.  **ZK-MultiSwap**：该协议证明了从一个零知识RSA累加器$C$中移除集合$X$并插入集合$Y$后，得到新的累加器$C'$的正确性，且不泄露$X$和$Y$的具体信息。其核心是将一次更新分解为两个“零知识子集插入”证明：存在一个中间累加器$C_{\text{mid}}$，使得插入$X$（从$C_{\text{mid}}$得到$C$）和插入$Y$（从$C_{\text{mid}}$得到$C'$）均成立。零知识子集协议本身利用了PoKE协议和一个CP-SNARK：证明者首先证明乘积$x t$除以随机质数挑战$l$的商$q$和余数$r$满足$g^{q l + r} = C'$，然后通过CP-SNARK证明哈希值（$x$和$t$的承诺）与$l$和$r$的关系。

**Notus构造**：
在每次纪元更新时，服务器运行ProveConsistency算法。该算法内部的SNARK电路验证关系$\mathcal{R}^{\text{DPoL}}$，需要检查：(i) ZK-MultiSwap关系成立；(ii) 被移除的旧哈希链摘要集合$\bar{S}_i$与被插入的新摘要集合$S_i$一一对应；(iii) 所有新交易的纪元数等于当前纪元$i$，且负债非负；(iv) 负债总和正确更新（差值等于新摘要与旧摘要的负债差）；(v) Pedersen承诺正确绑定了前后两个纪元的负债总和。整个电路证明所有更新操作是追加仅且一致的。

**复杂度**：
*   证明尺寸：256字节（SNARK证明）+ 1024字节（MultiSwap相关）。
*   用户验证：$O(1)$，一次模幂运算（约1-2ms）。
*   审计方验证：$O(1)$，验证一个SNARK证明和两个PoKE证明（可在以太坊Gas费750K内完成）。
*   证明方预计算：$O(n \log n)$，其中$n$为用户数。

### 核心公式与流程

**[零知识RSA累加器-承诺]**
$$C = g^{\left( \prod_{e_i \in \mathcal{S}} e_i \right) \cdot t} \pmod{N}$$
> 作用：将集合$\mathcal{S}$（元素经过DI哈希）和随机数$t$压缩为一个固定大小的承诺值$C$。$t$保证了承诺的零知识性质，即从$C$无法区分任何集合。

**[ZK-MultiSwap关系]**
$$\mathcal{R}^{\text{MSwap}}(C, C', C_{\text{mid}}, \boxed{c_{\vec{u0}}}, \boxed{c_{\vec{u1}}}; \tau_0, \tau_1, X, Y)$$
> 作用：证明存在一个中间累加器$C_{\text{mid}}$，使得插入集合$X$（随机化$\tau_0$）得到$C$，插入集合$Y$（随机化$\tau_1$）得到$C'$。承诺$c_{\vec{u0}}, c_{\vec{u1}}$绑定了$X$和$\tau_0$以及$Y$和$\tau_1$的哈希值。

**[DPoL一致性检查关系]**
$$\mathcal{R}^{\text{DPoL}}(d_{i-1}, d_i, C_{\text{mid}}, i, \boxed{c_{\vec{u0}}}, \boxed{c_{\vec{u1}}}; \tau_0, \tau_1, \bar{S}_i, S_i, \text{sum}_{i-1}, \text{sum}_i, r_{i-1}, r_i)$$
> 作用：这是Notus中整个SNARK电路验证的核心关系。它结合了ZK-MultiSwap、哈希链完整性检查、时间戳、非负负债和总和一致性等多个条件，确保纪元$i-1$到$i$的更新是合法且追加仅的。

**[成员证明验证]**
$$w_{x}^{H_{\text{DI}}(x)} \stackrel{?}{=} C \pmod{N}$$
> 作用：验证用户$x$（其哈希链摘要为$H_{\text{DI}}(x)$）是否被包含在摘要为$C$的累加器中。这仅需一次模幂运算，效率极高。

### 实验结果

实验在Amazon EC2 M6a实例（32 vCPUs, 128GB内存）上进行，使用Golang实现，SNARK采用gnark库（bn254曲线）。主要结论如下：
*   **多输出幂运算优化**：对于200万比特的指数，双指数幂运算（DoubleExponent）相比两次独立幂运算的时间减少至70.3%；四重指数幂运算（FourfoldExponent）时间减少至39.7%，若结合预计算表可降至19.1%。
*   **零知识RSA累加器性能**：预计算所有成员证明是主要瓶颈。对于$2^{18}$（约26万）个元素，单线程需3857秒，32线程并行降至384秒（约9-10倍加速）。成员证明尺寸仅为256字节（一个群元素），验证时间约1ms。
*   **与Caulk查找论证对比**：作为零知识查找系统，Notus的在线时间（即检索预计算好的证明）几乎为0（<20微秒），而Caulk需要在线计算，导致在线时间显著更长。即使将Caulk改为离线预计算所有证明的版本（Caulk*），其总体离线计算时间也比Caulk慢近三个数量级，远差于Notus。
*   **Notus系统性能**：在更新$2^{10}$个用户时，Notus的证明生成时间为3.7秒，远快于SNARKed Merkle Tree的15.0秒，与TAP的3.8秒相当，但证明尺寸仅256字节（TAP为610KB），验证时间仅0.001秒。对于$2^{18}$用户规模（约26万），在32核机器上总运行时间约400秒。
*   **智能合约审计**：在以太坊上执行Notus的审计逻辑仅消耗750K Gas（其中270K用于Groth16证明验证，480K用于两个PoKE验证）。
*   **扩展到百万级用户**：利用用户分组策略（如分为32组，每组$2^{15}$用户），并行处理可在约43秒内完成所有更新，实现了极佳的扩展性。

### 局限性与开放问题
*   **设置假设**：当前方案依赖于可信设置来生成RSA模数$N$，这需要多方计算来消除信任假设。未来可以考虑使用类群，但性能会下降。
*   **证明方计算瓶颈**：尽管提出了多输出幂运算优化，成员证明的批量预计算（$O(n \log n)$）在用户规模极大时仍是主要瓶颈，未能实现线性复杂度。
*   **未来方向**：进一步降低证明方开销至每个纪元仅与被更新用户数$|S_i|$呈线性关系（如TAP方案，但需支持任意更新），将是重要的改进方向。此外，探索将审计者角色完全去信任化（如通过以太坊合约）后的实际应用模式。

### 强关联论文

[41] Ji et al. Generalized proof of liabilities. **CCS 2021** [Google Scholar](https://scholar.google.com/scholar?q=Generalized+proof+of+liabilities)

[56] Reijsbergen et al. TAP: transparent and privacy-preserving data services. **USENIX Security 2023** [Google Scholar](https://scholar.google.com/scholar?q=TAP+transparent+and+privacy-preserving+data+services)

[6] Binance proof-of-reserves [Google Scholar](https://scholar.google.com/scholar?q=Binance+proof-of-reserves)

[52] OKX proof-of-reserves [Google Scholar](https://scholar.google.com/scholar?q=OKX+proof-of-reserves)

[62] Wesolowski. Efficient verifiable delay functions. **EUROCRYPT 2019** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+verifiable+delay+functions)

[53] Ozdemir et al. Scaling verifiable computation using efficient set accumulators. **USENIX Security 2020** [Google Scholar](https://scholar.google.com/scholar?q=Scaling+verifiable+computation+using+efficient+set+accumulators)

[16] Campanelli et al. Succinct zero-knowledge batch proofs for set accumulators. **CCS 2022** [Google Scholar](https://scholar.google.com/scholar?q=Succinct+zero-knowledge+batch+proofs+for+set+accumulators)

[17] Campanelli et al. LegoSNARK: Modular design and composition of succinct zero-knowledge proofs. **CCS 2019** [Google Scholar](https://scholar.google.com/scholar?q=LegoSNARK+Modular+design+and+composition+of+succinct+zero-knowledge+proofs)

[9] Boneh et al. Batching techniques for accumulators with applications to iops and stateless blockchains. **CRYPTO 2019** [Google Scholar](https://scholar.google.com/scholar?q=Batching+techniques+for+accumulators+with+applications+to+iops+and+stateless+blockchains)

[34] Ghosh et al. Zero-knowledge accumulators and set algebra. **ASIACRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=Zero-knowledge+accumulators+and+set+algebra)


## 关键词

+ Notus动态负债证明PoL
+ RSA累加器零知识
+ MultiSwap零知识协议
+ 加密资产交易所审计
+ O(1)查询复杂度证明
+ 动态更新用户负债
