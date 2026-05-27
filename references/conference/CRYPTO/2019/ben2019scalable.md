---
title: "Scalable zero knowledge with no trusted setup"
doi: 10.1007/978-3-030-26954-8_23
标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 2019
modified: 2025-04-11 11:37:24
---
## Scalable zero knowledge with no trusted setup

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-030-26954-8_23)

## 作者

+ Eli Ben-Sasson 
+ Iddo Bentov 
+ Yinon Horesh 
+ Michael Riabzev 

## 笔记

### 背景与动机
零知识证明系统在隐私保护与计算完整性验证方面具有根本重要性，但直到这篇工作之前，没有任何一个被代码实现的系统能同时满足普遍性、零知识、知识论证、可扩展验证和透明性这五个关键属性。早期基于PCP定理的理论构造[5-6, 39, 44, 54]虽然实现了这五项属性，但其证明者运行时间过大，导致从未被实际编码实现。后来的交互式Oracle证明模型[22, 67]虽然将证明时间提升至准线性，但其构造对于证明者和验证者双方都存在额外的高次对数因子，使得系统在具体计算中效率低下。此外，所有先前的方案要么需要非透明的设置阶段，依赖复杂的密码学假设如知识指数假设，要么验证者时间随输入规模线性增长，无法实现真正的全可扩展性。本文旨在填补这一空白，证明交互式Oracle证明系统不仅是一种理论构造，而且能够通过具体实现达到比所有现有系统更快的证明速度和最低的密码学假设依赖。

### 相关工作

[9] Ben-Sasson et al. Computational integrity with a public random string from quasi-linear PCPs. **IACR Cryptology ePrint Archive 2016** [Google Scholar](https://scholar.google.com/scholar?q=Computational+integrity+with+a+public+random+string+from+quasi-linear+PCPs)
> 核心思路：基于准线性PCP构建了首个可扩展透明IOP系统SCI，实现了无零知识情况下的可扩展验证。
> 局限与区别：SCI没有零知识属性，且其验证者复杂度具有大于1的多对数因子，通信复杂度因认证路径复杂而较高。本文在其中加入零知识，同时通过FRI协议和ALI协议大幅降低了证明时间和通信复杂度。

[21] Ben-Sasson et al. Aurora: transparent succinct arguments for R1CS. **EUROCRYPT 2019** [Google Scholar](https://scholar.google.com/scholar?q=Aurora+transparent+succinct+arguments+for+R1CS)
> 核心思路：针对算术电路设计了一个高效的ZKIOP，证明者时间准线性，证明长度poly-log。
> 局限与区别：Aurora的验证者时间随电路规模线性增长，不满足全可扩展性。本文的验证者时间呈poly-logarithmic增长，在大型顺序计算中更具优势。

[11] Ben-Sasson et al. Fast reed-solomon interactive oracle proofs of proximity. **ICALP 2018** [Google Scholar](https://scholar.google.com/scholar?q=Fast+reed-solomon+interactive+oracle+proofs+of+proximity)
> 核心思路：提出了FRI协议，一种严格准线性的RS码IOPP，具有严格的线性证明者复杂度和严格对数验证者复杂度。
> 局限与区别：FRI是本文依赖的底层协议，本文将其集成到更大的ZK-STARK框架中处理完整的计算完整性，而非仅解决距离测试问题。

[22] Ben-Sasson et al. Interactive oracle proofs. **TCC 2016** [Google Scholar](https://scholar.google.com/scholar?q=Interactive+oracle+proofs)
> 核心思路：形式化了IOP模型，是PCP模型的推广，并展示了如何将IOP编译为实际论证系统。
> 局限与区别：该文未解决具体构造的效率问题，本文在此基础上引入了具体的FRI和ALI协议，实现了首次可扩展且透明的实现。

[54] Kilian, J. A note on efficient zero-knowledge proofs and arguments. **STOC 1992** [Google Scholar](https://scholar.google.com/scholar?q=A+note+on+efficient+zero-knowledge+proofs+and+arguments)
> 核心思路：展示了如何使用碰撞抗性哈希函数将PCP转换为交互式论证系统。
> 局限与区别：该文是理论构造，未涉及实际实现。本文在此基础上将IOP而非PCP转换为论证系统，并实现了代码。

[17] Ben-Sasson et al. On the concrete efficiency of probabilistically-checkable proofs. **STOC 2013** [Google Scholar](https://scholar.google.com/scholar?q=On+the+concrete+efficiency+of+probabilistically-checkable+proofs)
> 核心思路：实现了准线性短PCP，引入了代数算术化方法和基于置换网络的RAM处理。
> 局限与区别：该系统的具体效率较低，且未实现零知识。本文通过FRI和ALI协议大幅改进了效率和零知识属性。

### 核心技术与方案
本文整体框架是一个从算术中间表示经代数布局路由到两个RS码距离测试问题的层叠式归约过程，核心创新在于四方面对先前方案的改进。首先，引入了FRI协议作为距离测试底层。FRI是一个交互式IOPP，其证明者算术复杂度严格线性于码长，验证者复杂度严格对数于码长，这是通过递归将码字降维并折叠为更短码字实现的。具体地，在每一轮中，证明者将原函数$f: S \to \mathbb{F}$按规则组合成新函数$f'$，其中$S$为大小为|S|的域子集，$|S|$为2的幂，折叠过程使用随机系数$\alpha$，公式为$f'(x) = \frac{f(x)+f(-x)}{2} + \alpha \cdot \frac{f(x)-f(-x)}{2x}$。

其次，为了降低通信复杂度，本文在Merkle树构造中采用按行分组和按陪集分组策略。每个证明预言机（如执行轨迹的一行）被放置在同一棵Merkle子树中，使得一次验证路径覆盖该行的所有元素；FRI验证者查询的陪集条目也被置于单个子树中，从而将认证路径总数从每个元素一个减少到每个陪集一个，大幅降低通信开销中$AP_{total} \cdot \lambda$这一项。

第三，引入了代数链接IOP（ALI）协议，该协议利用随机线性组合将AIR约束系统的s个多项式约束压缩为单个随机约束，从而将证明者需处理的多项式最大度从$d_{old}^{\max} = T \cdot a \cdot d + T \cdot s$降至$d_{\text{ZK-STARK}}^{\max} = T \cdot d$。压缩过程是：在验证者发送随机系数$r_0', r_1'$后，证明者构造单一约束$C := r_0' \cdot C_0 + r_1' \cdot C_1$，然后计算$Q(X) := C(P_0(X), P_1(X), P_0(gX), P_1(gX))$。$Q$在域$G$上为零，因此$Q/Z_G$是低度多项式，使得$g^{(0)}$成为RS码字。

第四，采用每个寄存器一个RS码字的编码方式，即执行轨迹的每一列对应一个独立的RS码字。这虽导致多个码字，但通过一轮交互，验证者发送随机系数$r_0, r_1$，证明者将所有码字线性组合为单一随机码字$f^{(0)}=r_0f_0+r_1f_1$，然后只需对这一个组合进行FRI测试，避免了为每个寄存器单独验证的开销。

在安全性方面，本文依赖两个假设：一个假设指出任何有效攻击者展示的证明预言机$f^{(0)},g^{(0)}$是距相应RS码最远的函数；另一个关于FRI协议的可靠性，即对于代码率$\rho$和常数$\delta$，如果$f$是距RS码$\delta$远的函数，则FRI拒绝它的概率至少为$\delta - O(1)/|\mathbb{F}|$。即使在最坏情况下假设不成立，系统的安全性损失也仅限于通信和验证复杂度增加最多3倍，这是因为已知的信息论界保证了对于$\delta \leq 1-\sqrt[3]{\rho}$的情况，可靠性实际上是一个定理。在渐进复杂度方面，对于空间$S(n)=O(\log T(n))$的时空有界语言，本文实现严格算术STIK：证明者算术复杂度$O(T(n)\log T(n))$，验证者算术复杂度$O(\log T(n))$，证明长度$O(T(n)\log T(n))$，查询复杂度$O(\lambda \log T(n))$，轮复杂度$\log T(n)/2+O(1)$。

### 核心公式与流程

**[FRI协议折叠步骤]**
$$f'(x) = \frac{f(x)+f(-x)}{2} + \alpha \cdot \frac{f(x)-f(-x)}{2x}$$
> 作用：在FRI协议每一轮中，证明者使用随机系数$\alpha$将大小为$|S|$的域上的函数$f$折叠为大小为$|S|/2$的新函数$f'$。若$f$是RS码字，则$f'$的度减半，实现递归降维。验证者通过少量查询即可检测远距离函数。

**[ALI协议约束压缩]**
$$C(X_0,X_1,Y_0,Y_1) := r_0' \cdot C_0(Y_0,X_1) + r_1' \cdot C_1(X_0,X_1,Y_1)$$
$$Q(X) := C(P_0(X), P_1(X), P_0(\mathfrak{g}\cdot X), P_1(\mathfrak{g}\cdot X))$$
> 作用：将AIR的多个多项式约束$C_0,C_1$通过随机系数$r_0',r_1'$线性组合为单一随机约束$C$。然后证明者使用寄存器对应的插值多项式$P_0,P_1$构建$Q(X)$，要求$Q$在生成元$g$对应的子群$G$上为零，从而确保$Q/Z_G$是低度多项式，使$g^{(0)}$成为RS码字。这消除了先前方案中需分别处理每个约束的开销。

**[通信复杂度公式]**
$$CC = q_{total} \cdot \log|\mathbb{F}| + AP_{total} \cdot \lambda$$
> 作用：给出了系统通信复杂度的表达式，其中$q_{total}$是总查询次数，$AP_{total}$是认证路径节点总数，$\lambda$是哈希输出比特长度。本文通过将行和陪集放入单棵子树，减少了$AP_{total}$项，从而降低了通信。

**[最大度对比]**
$$d_{old}^{\max}(T,a,s,d) = T \cdot a \cdot d + T \cdot s$$
$$d_{\text{ZK-STARK}}^{\max}(T,a,s,d) = T \cdot d$$
> 作用：对比了先前系统与本系统中证明者需插值和求值的多项式的最大度。本文通过ALI协议去除$T \cdot s$项（将s个约束压缩为一个），并通过按寄存器编码将$a$因子移除，显著降低了计算瓶颈。

### 实验结果
论文在图2中报告了在具有32个AMD 3.2GHz核心与512GB RAM的服务器上的测量数据，对比了SCI、libSNARK、BCCGP、BulletProofs、Ligero和本系统。主要结果包括：在单线程模式下，ZK-STARK证明者是所有系统中最快的，例如对于$2^{18}$乘法门规模的计算，证明时间约为60秒，而libSNARK约为100秒，Ligero约150秒。在多线程模式下（16核），ZK-STARK证明者比libSNARK快至少10倍。验证者时间方面，ZK-STARK呈poly-log增长，对于$2^{35}$门规模的计算仍低于0.1秒，而所有其他系统的验证者时间都随计算规模线性或平方根增长。通信复杂度方面，ZK-STARK对于$2^{27}$门规模约为100KB，而Ligero约5MB，BCCGP约7KB但验证者时间更长。在与SCI的直接比较中（图4），在80比特安全级别下，ZK-STARK证明者时间比SCI快7到40倍，通信复杂度低3到20倍。在较弱硬件（联想T440笔记本，32GB RAM，四核i7-8550U 1.80GHz）上，ZK-STARK仍然能够达到与服务器上其他系统可比的性能。实验使用了TinyRAM编译的穷举子集求和程序，该程序生成的电路约每周期2000个乘法门。

### 局限性与开放问题
本文的验证者复杂度虽为poly-log，但仍依赖于两个代数假设，在假设被反驳时验证者和通信复杂度可能增加最多3倍，而非完全崩溃。系统对于RAM计算的支持不如非RAM计算高效，因为验证RAM访问模式需要额外的切换网络，导致通信和证明时间的较大膨胀。开放问题包括找到在超多项式时间语言中实现完美零知识而非仅证人不可区分性的方法，以及进一步减少证明者时间和空间复杂度以扩展到更大的计算规模。此外，将当前构造扩展到支持更复杂的程序结构（如大型RAM访问）而不牺牲效率，仍是一个重要挑战。

### 强关联论文

[9] Ben-Sasson et al. Computational integrity with a public random string from quasi-linear PCPs. **IACR Cryptology ePrint Archive 2016** [Google Scholar](https://scholar.google.com/scholar?q=Computational+integrity+with+a+public+random+string+from+quasi-linear+PCPs)

[11] Ben-Sasson et al. Fast reed-solomon interactive oracle proofs of proximity. **ICALP 2018** [Google Scholar](https://scholar.google.com/scholar?q=Fast+reed-solomon+interactive+oracle+proofs+of+proximity)

[17] Ben-Sasson et al. On the concrete efficiency of probabilistically-checkable proofs. **STOC 2013** [Google Scholar](https://scholar.google.com/scholar?q=On+the+concrete+efficiency+of+probabilistically-checkable+proofs)

[21] Ben-Sasson et al. Aurora: transparent succinct arguments for R1CS. **EUROCRYPT 2019** [Google Scholar](https://scholar.google.com/scholar?q=Aurora+transparent+succinct+arguments+for+R1CS)

[22] Ben-Sasson et al. Interactive oracle proofs. **TCC 2016** [Google Scholar](https://scholar.google.com/scholar?q=Interactive+oracle+proofs)

[54] Kilian, J. A note on efficient zero-knowledge proofs and arguments. **STOC 1992** [Google Scholar](https://scholar.google.com/scholar?q=A+note+on+efficient+zero-knowledge+proofs+and+arguments)

[61] Micali, S. Computationally sound proofs. **SIAM J. Comput. 2000** [Google Scholar](https://scholar.google.com/scholar?q=Computationally+sound+proofs)

[67] Reingold et al. Constant-round interactive proofs for delegating computation. **STOC 2016** [Google Scholar](https://scholar.google.com/scholar?q=Constant-round+interactive+proofs+for+delegating+computation)


## 关键词

+ 密码学
+ 零知识
+ 协议