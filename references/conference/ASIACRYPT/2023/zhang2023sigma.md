---
title: "Sigma protocols from verifiable secret sharing and their applications"
标题简称:
论文类型: conference
会议简称: ASIACRYPT
发表年份: 2023
modified: 2025-04-14 09:53:38
---

## Sigma protocols from verifiable secret sharing and their applications

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-981-99-8724-5_7)

## 作者

+ Min Zhang 
+ Yu Chen
+ Chuanzhou Yao 
+ Zhichao Wang 

## 笔记

### 背景与动机
零知识证明是现代密码学的核心工具，其根据陈述类型可分为三类：代数陈述（如离散对数知识）、非代数陈述（如SHA256原像知识）以及复合陈述（同时包含二者）。对于代数陈述，Sigma协议因极高的效率（短证明、常数次公钥操作、无需可信设置）而成为最常用的方案。然而，文献中的经典Sigma协议如Schnorr、Guillou-Quisquater和Okamoto协议都是手工设计的，各自附带着独立的证明，缺乏统一的设计原理。对于复合陈述，已有工作的主流方法是分别用Sigma协议证明代数部分、用通用零知识证明证明非代数部分，但需要额外设计定制的“胶水”证明来确保两部分使用的证人一致性。这种做法有两个主要缺陷：胶水证明引入了额外的计算开销和证明大小开销，且胶水证明必须针对特定通用零知识证明协议定制，限制了可使用的通用零知识证明协议的范围。Backes等人在PKC 2019的工作中留下了一个开放问题：是否能用Ligero/Ligero++构造更紧凑的复合陈述零知识证明。本文旨在填补这两个空白，即提出Sigma协议的通用框架，并利用该框架给出无需胶水证明的复合陈述零知识证明的通用构造。

### 相关工作

[Fel87] Feldman. A practical scheme for non-interactive verifiable secret sharing. **FOCS 1987** [Google Scholar](https://scholar.google.com/scholar?q=A+practical+scheme+for+non-interactive+verifiable+secret+sharing)
> 核心思路：提出了非交互式可验证秘密共享方案，使用同态承诺来验证分享的正确性。
> 局限与区别：该定义在语法上没有显式包含认证信息aut，在安全性上对手正确性要求所有恢复的秘密一致，而本文放宽为恢复的秘密必须是承诺的合法打开。

[IKOS07] Ishai et al. Zero-knowledge from secure multiparty computation. **STOC 2007** [Google Scholar](https://scholar.google.com/scholar?q=Zero-knowledge+from+secure+multiparty+computation)
> 核心思路：提出了MPC-in-the-head范式，通过模拟MPC协议的执行来构造通用零知识证明。
> 局限与区别：原文只使用了异或秘密共享（即(1, n)-SS），难以与一般的VSS方案交互。本文将该范式泛化到任意的$(n, t_p, t_f) - SS$，并严格证明了知识抽取性质。

[BHH+19] Backes et al. Efficient non-interactive zero-knowledge proofs in cross-domains without trusted setup. **PKC 2019** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+non-interactive+zero-knowledge+proofs+in+cross-domains+without+trusted+setup)
> 核心思路：使用ZKBoo/ZKB++作为通用零知识证明，定制胶水证明链接Sigma协议，构造了透明且高效的复合陈述零知识证明。
> 局限与区别：其证明大小是$O(|C|\lambda + |w|)$，呈线性增长，且胶水证明不可迁移到Ligero/Ligero++。本文通过证人共享复用技术消除了胶水证明，并将证明大小降至多对数级。

[BFH+20] Bhadauria et al. Ligero++: a new optimized sublinear IoP. **CCS 2020** [Google Scholar](https://scholar.google.com/scholar?q=Ligero++%3A+a+new+optimized+sublinear+IoP)
> 核心思路：改进了Ligero协议，利用内积论证实现次线性通信的透明零知识证明。
> 局限与区别：其秘密共享机制是$(n, \tilde{t}, k)$-型（$\tilde{t} < k$），本文需要构造与之对齐的VSS方案以实现证人复用，并对Ligero++进行了修改以适应复用需求。

[Mau15] Maurer. Zero-knowledge proofs of knowledge for group homomorphisms. **Designs, Codes and Cryptography 2015** [Google Scholar](https://scholar.google.com/scholar?q=Zero-knowledge+proofs+of+knowledge+for+group+homomorphisms)
> 核心思路：提出了基于群同态原像的Sigma协议模板，覆盖了Schnorr、GQ等协议。
> 局限与区别：该模板受限于群同态框架，无法解释Schnorr变体和Batching Schnorr（初始消息未用与陈述相同的同态计算），且未建立与VSS的联系。本文的VSS-in-the-Head框架更通用，且为复合陈述构造奠定了基础。

[Cra96] Cramer. Modular design of secure yet practical cryptographic protocols. **PhD thesis 1996** [Google Scholar](https://scholar.google.com/scholar?q=Modular+design+of+secure+yet+practical+cryptographic+protocols)
> 核心思路：首次提出了Sigma协议的概念并研究了其组合性质。
> 局限与区别：经典工作但未探讨统一的设计原理。本文的框架为该类协议提供了统一的构造范式。

[CDS94] Cramer et al. Proofs of partial knowledge and simplified design of witness hiding protocols. **CRYPTO 1994** [Google Scholar](https://scholar.google.com/scholar?q=Proofs+of+partial+knowledge+and+simplified+design+of+witness+hiding+protocols)
> 核心思路：利用秘密共享技术构造部分知识证明，共享的是挑战e而非证人w。
> 局限与区别：与本文形成对偶关系——本文共享的是证人w。二者均表明(可验证)秘密共享是构造Sigma协议的关键技术。

### 核心技术与方案

本文提出了一个从可验证秘密共享出发的Sigma协议通用框架，并展示了其在复合陈述零知识证明构造中的应用。

**VSS的重新定义与Sigma协议框架**。本文首先给出了一个精炼的非交互式VSS定义。与Feldman原始定义相比，新定义在语法上有两点主要区别：秘密被承诺而非加密（更具一般性），分享算法额外输出认证信息aut用于校验分享的正确性。在安全性上，正确性要求恢复的秘密必须是承诺的合法打开（而非仅要求一致性），隐私性采用基于模拟的定义而非基于游戏的定义。基于此，Sigma协议框架如下：证明者运行VSS.Share*(s, r)获得所有shares和认证信息aut，并将aut发送给验证者；挑战阶段，验证者随机选择一个大小为$t_p$的参与者子集$I$；响应阶段，证明者打开对应的shares$(v_i)_{i \in I}$；验证者使用VSS.Check检验每个share的合法性。在安全性上，特殊可靠性（特殊可靠性阶数为$\binom{t_f-1}{t_p}+1$）由VSS的正确性保证，即从足够多个有效shares中恢复的(s, r)必然是承诺的合法打开；特殊诚实验证者零知识性由VSS的$t_p$-隐私性保证。当参与者数量n超多项式时，框架可细化为Share-in-Mind（仅输出共享方法的紧凑描述SH_cpt和aut）和Distribute（按需生成单个share）两个子步骤。

**经典协议的恢复**。框架能够统一解释所有经典Sigma协议。例如，Feldman的$(n, t_p, t_p+1)$-VSS在设置$n = p, t_p = 1$时退化为加性秘密共享，对应的Sigma协议即为Schnorr协议（图2）。类似地，通过设置$t_f = t_p + \ell$的VSS（使用打包Shamir秘密共享）并设$n = p, t_p = 1$，可得到Batching Schnorr协议（图3）。Pedersen VSS对应Okamoto协议（图4），基于RSA的VSS对应Guillou-Quisquater协议（图5）。

**MPC-in-the-Head的泛化**。为与VSS框架结合，本文将原始的MPC-in-the-head范式从异或秘密共享泛化到一般的$(n, t_p^{ss}, t_f)$-SS。桥接工具是秘密共享方案SS与可分离VSS：若VSS的Share*可以分解为分别对秘密s和随机数r运行SS.Share，再运行AutGen生成aut，则称该VSS是可分离的，并与该SS对齐。在此基础上，复合陈述零知识证明的构造实现证人共享复用：证明者仅运行一次SS.Share(s)和SS.Share(r)获得shares，将其分别用于代数部分（由Sigma协议中的VSS使用）和非代数部分（由MPC-in-the-head中的MPC协议使用），验证者对同一组shares同时检查两部分的验证条件。安全性论证中，抽取器可通过同时调用两部分的抽取子程序，强制它们恢复出相同的证人，从而保证一致性。

**实例化**。选择Ligero++作为通用零知识证明，并构造与之对齐的VSS方案。Ligero++使用随机化RS编码，可视为$(n, \tilde{t}, k)$-打包Shamir秘密共享。与之对齐的VSS方案中，秘密向量s和随机数向量r分别被打包，系数插值后生成完整多项式并求值得到shares。对Ligero++的修改是将股份矩阵分为两个子矩阵处理：输入部分直接打开，门输出部分使用内积论证，从而使得输入部分的shares可被复用。最终的复合陈述零知识证明系统无需可信设置，证明大小为$O(\text{polylog}(|C|) + \lambda)$，电路无关的公开密钥操作次数为$O(\lambda)$。

### 核心公式与流程

**[Feldman VSS的Share和Check]**
$$
\begin{array}{l}
\text{Share}(s): c = g^s,\ f(x) = \sum_{j=0}^{t_p} a_j x^j,\ a_{t_p}=s,\ v_i = f(i),\\
\text{aut} = (g^{a_0}, \ldots, g^{a_{t_p-1}}).\\
\text{Check}(i, v_i, c, \text{aut}): \text{accept iff } g^{v_i} = \prod_{j=0}^{t_p-1} (g^{a_j})^{i^j} \cdot c^{i^{t_p}}.
\end{array}
$$
> 作用：展示了Feldman VSS分享和验证的核心步骤，用于恢复Schnorr协议。

**[Sigma协议的特殊可靠性条件]**
$$
\text{接受项数} = \binom{t_f-1}{t_p} + 1
$$
> 作用：定义了从多个接受转录中恢复证人所需的最少转录数量，该值由VSS的门限参数决定。

**[VSS的可分离性定义]**
$$
\begin{array}{l}
\text{VSS.Share}^*(s, r): (s_i)_{i\in[n]} \leftarrow \text{SS.Share}(s),\\
(r_i)_{i\in[n]} \leftarrow \text{SS.Share}(r),\\
\text{aut} \leftarrow \text{AutGen}((s_i, r_i)_{i\in[n]}),\\
\text{return } ((s_i, r_i)_{i\in[n]}, \text{aut}).
\end{array}
$$
> 作用：规范了VSS与SS的对齐关系，为证人复用提供数学基础。

**[复合陈述零知识证明的核心验证条件]**
$$
\begin{array}{l}
\forall i \in I: \text{Com.Verify}(c_i, s_i||\text{view}_i) = 1\\
\land \Pi_f(P_i, s_i||\text{view}_i) = 1\\
\land \text{views的一致性}\\
\land \text{VSS.Check}(i, (s_i, r_i), x, \text{aut}) = 1.
\end{array}
$$
> 作用：列举了复合协议中验证者需要对打开的shares和视图执行的全部检查，确保代数部分和非代数部分使用一致证人。

### 实验结果
本文未进行实验验证，而是给出了理论复杂度分析与现有工作的对比。实验设置包括在FFT友好的椭圆曲线标量域上实现上述协议。核心性能来自文章中的表1：对于复合陈述零知识证明，本文协议（实例化）的证明大小为$O(\text{polylog}(|C|) + \lambda)$，远优于Backes等人的$O(|C|\lambda + |w|)$。证明者时间方面，公开密钥操作次数为$O(\lambda)$（与电路大小$|C|$无关），对称密钥操作次数为$O(|C|\log |C|)$。验证者时间中，公开密钥操作次数为$O((|w|+\lambda)^2/\log(|w|+\lambda))$，对称密钥操作次数为$O(|C|)$。与Backes等人的工作相比，本文在证明大小上实现了渐进改进，解决了其遗留的开放问题。与Bünz等人的Bulletproofs相比，本文的证明者开销在电路规模较小时更具优势，因为$O(|C|\log |C|)$的域操作很可能快于$O(|C|)$的群操作。本文协议是公开硬币且透明的，而CGM16的协议是私密硬币的，AGM18、CFQ19和ABC+22的方案均需要可信设置。

### 局限性与开放问题
本文构建依赖VSS的可分离性，但未探究不满足该性质的VSS是否仍可组合成复合陈述协议。实例化时需要对Ligero++进行修改（将股份矩阵分为两个子矩阵），这种修改可能无法直接迁移到所有MPC-in-the-head协议。此外，证明大小虽优化至多对数级，但系数可能较大，实际部署时的性能还需实现验证。未来的工作可探索将本框架扩展到更多类型的通用零知识证明（如基于线性PCP的协议），或基于本框架构造无胶水证明的通用组合定理。

### 强关联论文

[Fel87] Feldman. A practical scheme for non-interactive verifiable secret sharing. **FOCS 1987** [Google Scholar](https://scholar.google.com/scholar?q=A+practical+scheme+for+non-interactive+verifiable+secret+sharing)

[IKOS07] Ishai et al. Zero-knowledge from secure multiparty computation. **STOC 2007** [Google Scholar](https://scholar.google.com/scholar?q=Zero-knowledge+from+secure+multiparty+computation)

[BHH+19] Backes et al. Efficient non-interactive zero-knowledge proofs in cross-domains without trusted setup. **PKC 2019** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+non-interactive+zero-knowledge+proofs+in+cross-domains+without+trusted+setup)

[BFH+20] Bhadauria et al. Ligero++: a new optimized sublinear IoP. **CCS 2020** [Google Scholar](https://scholar.google.com/scholar?q=Ligero++%3A+a+new+optimized+sublinear+IoP)

[Mau15] Maurer. Zero-knowledge proofs of knowledge for group homomorphisms. **Designs, Codes and Cryptography 2015** [Google Scholar](https://scholar.google.com/scholar?q=Zero-knowledge+proofs+of+knowledge+for+group+homomorphisms)

[Cra96] Cramer. Modular design of secure yet practical cryptographic protocols. **PhD thesis 1996** [Google Scholar](https://scholar.google.com/scholar?q=Modular+design+of+secure+yet+practical+cryptographic+protocols)

[CDS94] Cramer et al. Proofs of partial knowledge and simplified design of witness hiding protocols. **CRYPTO 1994** [Google Scholar](https://scholar.google.com/scholar?q=Proofs+of+partial+knowledge+and+simplified+design+of+witness+hiding+protocols)

[Ped91] Pedersen. Non-interactive and information-theoretic secure verifiable secret sharing. **CRYPTO 1991** [Google Scholar](https://scholar.google.com/scholar?q=Non-interactive+and+information-theoretic+secure+verifiable+secret+sharing)

[BBB+18] Bünz et al. Short proofs for confidential transactions and more. **IEEE S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Short+proofs+for+confidential+transactions+and+more)


## 关键词

+ Sigma协议
+ 可验证秘密共享
+ 零知识证明
+ 复合语句
+ 代数语句

Sigma协议是最常见和最高效的零知识证明(zero-knowledge proofs, ZKPs)之一。几十年来，已经提出了大量的Sigma协议，但很少有研究关注其共同的设计原则。在本研究中，我们提出了一个基于可验证秘密共享(verifiable secret sharing, VSS)方案的代数语句Sigma协议通用框架。我们的框架为理解Sigma协议提供了一个一般性的统一方法。它不仅能够简洁地解释诸如Schnorr、Guillou-Quisquater和Okamoto等经典协议，还能推导出此前未知的新型Sigma协议。

此外，我们展示了该框架在设计复合语句零知识证明方面的应用，这些复合语句同时包含代数语句和非代数语句。我们通过见证共享复用(witness sharing reusing)技术，将基于VSS的Sigma协议和遵循MPC-in-the-head范式的零知识证明无缝结合，从而为复合语句提供了一个通用的非交互式零知识证明构造方法。我们的构造方法的优势在于不需要用于组合代数语句和非代数语句的"粘合"证明。通过使用Ligero++(Bhadauria等人，CCS 2020)实例化我们的构造，并设计相关的基于VSS的Sigma协议，我们获得了一个具体的复合语句零知识证明，该证明在运行时间和证明大小之间实现了权衡，从而解决了Backes等人(PKC 2019)遗留的开放性问题。