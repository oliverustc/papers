---
title: "hints: Threshold signatures with silent setup"
标题简称:
论文类型: conference
会议简称: S&P
发表年份: 2024
created: 2025-04-17 10:28:28
modified: 2025-04-17 10:39:56
---

## hints: Threshold signatures with silent setup

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/10646864)

## 作者

+ [Sanjam Garg](Sanjam%20Garg.md) 
+ [Abhishek Jain](Abhishek%20Jain.md)
+ [Pratyay Mukherjee](Pratyay%20Mukherjee.md) 
+ Rohit Sinha 
+ [Mingyuan Wang](Mingyuan%20Wang.md) 
+ [Yinuo Zhang](Yinuo%20Zhang.md)
## 笔记

### 背景与动机
阈值签名作为一种成熟的密码学原语，在区块链、去中心化金融等场景中已被广泛用于状态证明、预言机网络、跨链桥等应用。现有方案普遍遵循“先运行交互式分布式密钥生成协议生成密钥，再基于固定门限构造签名”的范式，这导致了三个关键瓶颈：第一，DKG需要广播信道与昂贵的多方交互，在节点超过500的大规模共识组中几乎不可行；第二，DKG一旦完成，签名门限和签名者集合就被固定，无法事后动态调整；第三，多数方案仅支持等权门限，难以自然扩展到加权门限。Ethereum 2.0为规避DKG而采用BLS多重签名，却要求验证者学习所有512个公钥，导致验证成本线性增长。本文试图开创一个同时实现静默设置、动态门限与通用访问结构的阈值签名新范式，不依赖任何交互式密钥生成步骤。

### 相关工作

[42] Gennaro 等. Secure distributed key generation for discrete-log based cryptosystems. **Journal of Cryptology 1999** [Google Scholar](https://scholar.google.com/scholar?q=Secure+distributed+key+generation+for+discrete-log+based+cryptosystems)
> 核心思路：基于Feldman可验证秘密共享设计了经典的交互式DKG协议，被几乎所有阈值签名采用。
> 局限与区别：需要O(n²)通信与计算，且门限、签名者固定；本文改用完全静默的设置方式，消除了交互。

[63] Tomescu 等. Towards scalable threshold cryptosystems. **S&P 2020** [Google Scholar](https://scholar.google.com/scholar?q=Towards+scalable+threshold+cryptosystems)
> 核心思路：将Joint-Feldman DKG的通信复杂度优化至O(n log n)，且支持加权门限。
> 局限与区别：仍需分布式计算与广播，对于大规模动态群组仍然代价高昂；本文在加权场景下聚合时间仅0.5秒，远优于其46秒。

[50] Micali 等. Compact certificates of collective knowledge. **S&P 2021** [Google Scholar](https://scholar.google.com/scholar?q=Compact+certificates+of+collective+knowledge)
> 核心思路：用非交互证明将门限签名压缩为对数大小，支持加权门限。
> 局限与区别：签名大小和验证时间都是对数级，且有签名门限与真实签名者数量之间必须存在间隙的要求；本文实现了恒定大小和恒定时间验证。

[40] Gabizon 等. PLONK: Permutations over lagrange-bases for oecumenical noninteractive arguments of knowledge. **ePrint 2019** [Google Scholar](https://scholar.google.com/scholar?q=PLONK+Permutations+over+lagrange-bases+for+oecumenical+noninteractive+arguments+of+knowledge)
> 核心思路：提出了一种高效的通用SNARK，支持多项式恒等式的批量验证。
> 局限与区别：直接用于聚合签名时，因非本地域算术导致对数百节点需要数十秒才能完成聚合；本文仅靠结构化提示和恒定次配对即可验证。

[12] Baird 等. Threshold signatures in the multiverse. **S&P 2023** [Google Scholar](https://scholar.google.com/scholar?q=Threshold+signatures+in+the+multiverse)
> 核心思路：引入多宇宙概念，每个宇宙对应一个签名者子集，但每个宇宙仍需一轮交互。
> 局限与区别：每增加一个宇宙就需要一次交互，且局部签名大小与权重线性相关；本文所有宇宙共享一次静默设置，签名大小与权重无关。

### 核心技术与方案

全文构造以BLS多重签名为起点。若直接用于门限场景，聚合者需输出签名者子集B及其签名乘积σ，但验证者需遍历所有公钥计算聚合公钥，导致线性开销。为克服此瓶颈，聚合者改为输出聚合公钥aPK并对“aPK是B中公钥正确聚合”这一断言生成简洁证明——但证明中包含群运算是SNARK的巨大瓶颈。本文的核心洞察是：秘密聚合密钥aSK比公开聚合公钥aPK更适合用SNARK证明，因为秘密的证明可以借助多项式承诺在域算术中完成。

方案在公共参考字符串模型下构建，CRS为KZG承诺的标准参数。每方i在本地运行BLS密钥生成，并发布以sk_i为系数的若干多项式求值结果，即提示hint_i。预处理器输入所有hint_i和pk_i，验证提示合法性后聚合出一个线性大小的聚合密钥AK和一个恒定的验证密钥vk。AK中包含所有形如[sk_i·(L_i²(τ)-L_i(τ))/Z(τ)]等预计算的群元素。验证密钥vk则由两个多项式在τ处的值组成：SK(τ) = Σsk_i·L_i(τ)与W(τ)=Σw_i·L_i(τ)。

签名阶段，每方独立计算BLS签名σ_i。聚合者输入AK，对实际签名者集合B做两步操作：首先计算aPK = (Π_{i∈B} pk_i)^{|H|⁻¹}与σ' = (Π_{i∈B} σ_i)^{|H|⁻¹}；其次利用广义求和分析生成紧凑证明。该证明的核心是三个多项式恒等式：SK(x)B(x) - aSK = Q_Z(x)Z(x) + Q_x(x)x用于验证aSK的正确聚合，两个附加恒等式用于验证B(x)在求值域上取值为0/1且累积权重恰好为w。前三个恒等式中，Q_Z和Q_x可由AK中的预计算元素直接线性组合快速得到。最终签名由aPK、σ'、阈值w、B(τ)的承诺、Q_x(τ)、Q_Z(τ)、ParSum(τ)以及一组Plonk风格的打开证明组成，大小恒定。

验证者仅需执行恒定次配对操作：一次配对确认SK(τ)·B(τ)与aSK、Q_Z、Q_x的等式；一次配对确认Q_x(τ)的度数正确；以及一个恒定时间的Plonk验证。正确性归纳自声称：错误提示必定使预处理器将其权重置零，错误部分签名必定无法通过PartialVerify，因此正确性退化为半诚实情形。安全性证明在代数群模型中完成，基于q-DLOG假设和广义求和分析。其关键思想是：若敌手能伪造，则可提取多项式恒等式，并由代数群模型迫使聚合公钥aSK必须只依赖于已被查询过签名的各方密钥。由于签名者集合的权重超过被签公钥集合的权重，aSK中必包含一个未查询密钥的线性项，但证明中的Q_x多项式对此密钥的度最高为|H|-2，其乘x后无法产生恰为1/|H|的常数项，产生矛盾，从而证否了伪造可能性。

方案直接支持加权门限：只需将权重向量从全1替换为真实权重w_i，所有算法保持相同，没有任何额外性能损失。扩展至通用访问结构时，用Plonk式电路证明B(x)满足任意布尔电路C。前向安全通过周期性密钥更新实现；匿名性通过在aPK中混入随机掩码并相应调整商多项式达成。这些扩展均不改变方案的核心常数时间验证性质。

### 核心公式与结果

**[广义求和检查]**
$$
A(x)\cdot B(x)=\frac{\sum_i a_i b_i}{|\mathbb{H}|}+Q_x(x)\cdot x+Q_Z(x)\cdot Z(x)
$$
> 作用：将秘密的hadamard积转化为公开的多项式恒等式，是构造中连接秘密密钥和证明的桥梁。

**[验证核心配对等式]**
$$
e([\mathsf{SK}(\tau)]_1,[B(\tau)]_2)\cdot e(\mathsf{aPK},[1]_1)^{-1}=e([Q_Z(\tau)]_1,[Z(\tau)]_2)\cdot e([Q_x(\tau)]_1,[\tau]_2)
$$
> 作用：验证者通过一次配对检查确认聚合公钥的正确性。

**[聚合签名结构]**
$$
\sigma=\{\mathsf{aPK},\sigma',w,[B(\tau)]_2,[Q_x(\tau)]_1,[Q_Z(\tau)]_1,[\mathsf{ParSum}(\tau)]_1,[Q(\tau)]_1,B(r),\mathsf{ParSum}(r),\mathsf{ParSum}(r\cdot\omega),W(r),Q(r),\mathsf{open}_r,\mathsf{open}_{r\cdot\omega}\}
$$
> 作用：展示了最终的恒定大小签名，包含9个群元素和5个域元素。

### 实验结果

实验在配备M1 Pro芯片的Macbook Pro上单线程运行，使用BLS12-381曲线。对于1000个签名者，hinTS的聚合时间仅0.47秒，而阈值BLS在10比特权重下需24.16秒，通用SNARK（Groth16）需186.3秒、PLONK需126.3秒。部分签名大小恒定为一个G₁元素（48字节），聚合签名为896字节（9个G₁元素加5个域元素），而阈值BLS仅48字节、但需要DKG；多重签名BLS为176字节加n比特、但其验证者需线性次群操作。验证时间hinTS为17.5毫秒（含10次配对），EVN gas成本为395K，约为阈值BLS（3.5毫秒/160K）的2.5倍，但与PLONK（7毫秒/377K）接近；多重签名BLS在n=1024时验证时间为2.5毫秒、但gas成本达774K。设置成本方面，hinTS的静默设置需46.3秒且仅需对所有n≥2³的计算一次，而阈值BLS运行O(n log n)的DKG且每次访问结构改变均需重新运行。在存储gas方面，hinTS为390K，多重签名BLS在n=1024时高达60M（约1450美元），差距显著。这些数据说明hinTS在聚合效率、签名/验证恒定开销及适用规模上均优于现有所有避免DKG的方案。

### 局限性与开放问题

hinTS的验证时间（17.5 ms）比阈值BLS（3.5 ms）高约5倍，在链上环境中的gas成本提升至约2.5倍，这对于gas极度敏感的轻客户端应用仍构成门槛。安全证明在代数群模型中进行，未承诺随机预言机或标准模型下的更弱假设。开放问题包括：能否进一步降低验证开销至接近普通BLS签名的水平，或在不依赖配对友好曲线的情况下实现类似性质的静默门限签名，以及如何将加权门限自然地扩展到高精度（如64位）权重而保持证明简洁。

### 强关联论文

[42] Gennaro 等. Secure distributed key generation for discrete-log based cryptosystems. **Journal of Cryptology 1999** [Google Scholar](https://scholar.google.com/scholar?q=Secure+distributed+key+generation+for+discrete-log+based+cryptosystems)

[63] Tomescu 等. Towards scalable threshold cryptosystems. **S&P 2020** [Google Scholar](https://scholar.google.com/scholar?q=Towards+scalable+threshold+cryptosystems)

[50] Micali 等. Compact certificates of collective knowledge. **S&P 2021** [Google Scholar](https://scholar.google.com/scholar?q=Compact+certificates+of+collective+knowledge)

[40] Gabizon 等. PLONK: Permutations over lagrange-bases for oecumenical noninteractive arguments of knowledge. **ePrint 2019** [Google Scholar](https://scholar.google.com/scholar?q=PLONK+Permutations+over+lagrange-bases+for+oecumenical+noninteractive+arguments+of+knowledge)

[47] Kate 等. Constant-size commitments to polynomials and their applications. **ASIACRYPT 2010** [Google Scholar](https://scholar.google.com/scholar?q=Constant-size+commitments+to+polynomials+and+their+applications)

[19] Boneh 等. Compact multi-signatures for smaller blockchains. **ASIACRYPT 2018** [Google Scholar](https://scholar.google.com/scholar?q=Compact+multi-signatures+for+smaller+blockchains)

[12] Baird 等. Threshold signatures in the multiverse. **S&P 2023** [Google Scholar](https://scholar.google.com/scholar?q=Threshold+signatures+in+the+multiverse)

[18] Boldyreva. Threshold Signatures, Multisignatures and Blind Signatures Based on the Gap-Diffie-Hellman-Group Signature Scheme. **PKC 2003** [Google Scholar](https://scholar.google.com/scholar?q=Threshold+Signatures+Multisignatures+and+Blind+Signatures+Based+on+the+Gap-Diffie-Hellman-Group+Signature+Scheme)

[21] Boneh 等. Short signatures from the Weil pairing. **ASIACRYPT 2001** [Google Scholar](https://scholar.google.com/scholar?q=Short+signatures+from+the+Weil+pairing)

[57] Rafols 等. An algebraic framework for universal and updatable SNARKs. **CRYPTO 2021** [Google Scholar](https://scholar.google.com/scholar?q=An+algebraic+framework+for+universal+and+updatable+SNARKs)


## 关键词

+ 阈值签名
+ BLS签名静默设置
+ 动态阈值访问策略
+ 加权阈值签名
+ 主动安全前向安全
+ 简洁证明聚合公钥