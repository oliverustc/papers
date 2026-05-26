---
title: "HOLMES: Efficient Distribution Testing for Secure Collaborative Learning"
标题简称:
论文类型: conference
会议简称: USENIX Security
发表年份: 2023
modified: 2025-04-09 10:53:32
---

## HOLMES: Efficient Distribution Testing for Secure Collaborative Learning

## 发表信息

+ [原文链接](https://www.usenix.org/conference/usenixsecurity23/presentation/chang)

## 作者

+ 

## 笔记

### 背景与动机
在安全多方计算（MPC）的框架下，多个机构可以联合训练机器学习模型而不泄露各自的数据。然而，数据质量评估在安全计算中成为一个关键瓶颈。例如，欧盟通用数据保护条例要求组织对模型的错误、偏见或歧视承担法律责任。现有技术（如SPDZ和SCALE-MAMBA）虽然支持恶意安全下的通用算术计算，但用于分布测试时的开销极其高昂：在t方场景下，对t个数据集进行测试的在线阶段计算开销为O(C·t)，离线阶段为O(C·t²)，若各方测试集不同则总开销达O(C·t³)。由于MPC限制了数据相关操作，无法直接评估联合数据集的质量，这使得分布测试成为缺失但必要的环节。本文旨在填补这一空白，提出一种高效的分布测试协议，显著降低在安全协同学习中进行数据质量检测的计算成本。

### 相关工作

[22] Keller, M. Multi-Protocol SPDZ. **GitHub** [Google Scholar](https://scholar.google.com/scholar?q=MP-SPDZ)
> 核心思路：提供基于SPDZ的恶意安全多方计算框架，支持通用算术计算。
> 局限与区别：在t方分布测试中，离线阶段开销为O(C·t²)，在线阶段为O(C·t)，且无法利用并发性；HOLMES通过混合IZK协议将复杂度降至O(C·t)。

[23] SCALE-MAMBA. **GitHub** [Google Scholar](https://scholar.google.com/scholar?q=SCALE-MAMBA)
> 核心思路：实现恶意安全下的通用算术MPC协议，常用于安全协同学习。
> 局限与区别：其离线阶段计算量与方数和在线计算量乘积成正比，导致多方测试时效率急剧下降；HOLMES通过IZK跳过此瓶颈。

[24] Yang, K. et al. QuickSilver: Efficient and Affordable Zero-Knowledge Proofs for Circuits and Polynomials over Any Field. **CCS 2021** [Google Scholar](https://scholar.google.com/scholar?q=QuickSilver+Efficient+Zero+Knowledge+Proofs)
> 核心思路：低开销的交互式零知识证明协议，适用于任意域。
> 局限与区别：原文未将其与分布测试结合；HOLMES将其作为IZK底层，利用其低证明开销实现并发验证。

[25] Setty, S. Spartan: Efficient and General-Purpose zkSNARKs Without Trusted Setup. **CRYPTO 2020** [Google Scholar](https://scholar.google.com/scholar?q=Spartan+Efficient+General+Purpose+zkSNARKs)
> 核心思路：无可信设置的简洁非交互零知识证明，通信量低。
> 局限与区别：证明时间远高于QuickSilver，在多方设置下（t≤10）总执行时间反而不如IZK；HOLMES将其作为对比基线而非使用。

[34] Johnson, W. B. et al. Extensions of Lipschitz mappings into a Hilbert space. **Contemporary mathematics 1984** [Google Scholar](https://scholar.google.com/scholar?q=Extensions+of+Lipschitz+mappings+into+a+Hilbert+space)
> 核心思路：Johnson-Lindenstrauss引理，表明随机线性投影可近似保持ℓ₂范数。
> 局限与区别：原文纯理论；HOLMES将其应用于草图算法，并设计ZK友好的实现方式。

[37] Damgård, I. B. On the randomness of Legendre and Jacobi sequences. **CRYPTO 1988** [Google Scholar](https://scholar.google.com/scholar?q=On+the+randomness+of+Legendre+and+Jacobi+sequences)
> 核心思路：Legendre PRF基于Legendre符号构造，输出为{-1,1}。
> 局限与区别：以往主要用于理论研究；HOLMES发现其天然的{-1,1}输出特性最适合草图算法，且在IZK中仅需8个乘法门，远优于SHA-256等PRF。

[58] Achlioptas, D. Database-Friendly Random Projections: Johnson-Lindenstrauss with Binary Coins. **Journal of Computer and System Sciences 2003** [Google Scholar](https://scholar.google.com/scholar?q=Database+Friendly+Random+Projections+Johnson+Lindenstrauss+with+Binary+Coins)
> 核心思路：用±1二值矩阵实现随机投影，简化计算。
> 局限与区别：原文针对明文场景；HOLMES将其改造为ZK环境，并用Legendre PRF生成伪随机±1矩阵。

[59] Couteau, G. et al. Silver: Silent VOLE and Oblivious Transfer from Hardness of Decoding Structured LDPC Codes. **CRYPTO 2021** [Google Scholar](https://scholar.google.com/scholar?q=Silver+Silent+VOLE+and+Oblivious+Transfer)
> 核心思路：silent OT技术，降低IZK的预处理成本。
> 局限与区别：QuickSilver已集成该技术；HOLMES直接利用其提升IZK效率，未做进一步扩展。

[85] Corrigan-Gibbs, H. et al. Prio: Private, robust, and scalable computation of aggregate statistics. **NSDI 2017** [Google Scholar](https://scholar.google.com/scholar?q=Prio+Private+robust+scalable+aggregate+statistics)
> 核心思路：通过非共谋半诚实服务器聚合私有统计数据，支持范围检查。
> 局限与区别：假设非共谋服务器，无法抵御恶意多数攻击；HOLMES在恶意多数下提供安全保证。

### 核心技术与方案

**整体框架：混合协议架构**
HOLMES将分布测试拆分为两部分：单方数据集上的统计量计算和多方联合的最终计算。前者通过交互式零知识证明（IZK）进行验证，后者在MPC中执行少量“收尾”操作。系统模型包含t方，每方同时作为证明者和验证者，并发运行IZK协议。协议流程为：① 在IZK和MPC中加载输入数据，防止自适应更改；② 揭示待执行的分布测试；③ 执行一致性检查，确保两处数据一致；④ 每对方运行IZK，证明者证明其数据集上统计量的正确计算；⑤ 在MPC中完成涉及多方的最终比较（如z-test的均值差比较）。该架构将单方计算从t方MPC中剥离，使复杂度从O(C·t²)降至O(C·t)。

**一致性检查协议**
为防止数据在IZK和MPC中不一致，构造轻量级一致性检查协议。设MPC使用加法秘密共享（份额shareᵢ(x)），IZK使用同态承诺（Comₓ(x)）。协议步骤：证明者P随机选取r∈Fₚ，向各验证者发送shareⱼ(r)和Comₖⱼ(r)；各方通过抛硬币协议获得随机挑战β；在MPC中计算ρ = r + Σₖ₌₁^N xₖ·βᵏ；P对每个验证者证明Comₖⱼ(ρ) - Comₖⱼ(r) - Σₖ Comₖⱼ(xₖ)·βᵏ = Comₖⱼ(0)。该协议仅需O(N)次本地操作和一次高效的IZK（证明承诺的差为0），主要开销来自抛硬币和零知识证明。

**单向分布测试：IZK验证基本统计量**
在IZK中验证单方数据的基本统计属性：
- 范围检查：证明a≤x≤b，通过比特分解证明x-a≥0和b-x≥0。
- 直方图：为每个数据点计算独热编码向量σ⃗（长度为桶数D），证明σ⃗合法且累加得计数向量count⃗。多维直方图扩展：每点有d维属性，桶数为ΠDᵢ。
- 均值与方差：均值x̄通过验证N·x̄′ = 100·Σxⱼ（固定点表示，精度两位小数）实现；方差s²通过验证s² = (N/(N-1))(ȳ - x̄²)实现。

**多维分布测试：ZK友好的草图算法**
为避免指数增长的桶数，使用随机线性投影（Johnson-Lindenstrauss引理）近似未归一化χ²检验。核心思想：将直方图count⃗与目标分布N·p⃗的欧几里得距离通过r×D的伪随机±1矩阵R降维至r维，且距离近似保持。具体地，检验Σ_{j=1}^D (count[j] - Npⱼ)² 近似等于 (1/r)·Σ_{ν=1}^r (sum[ν] - qν)²，其中sum⃗ = R·count⃗，q⃗ = N·R·p⃗。

**IZK中的草图计算**
关键挑战：如何高效获得伪随机矩阵R。直接计算R·σ⃗ₖ（σ⃗ₖ为第k个数据点的独热编码）需线性扫描所有桶，开销为O(N·r·D)。解决方案：利用伪随机函数计算R的列向量。具体地，若R[i][j]=PRFₖᵢ(j)，则对于第k个数据点的线性索引oₖ（独热编码中1的位置），有R·σ⃗ₖ = (PRFₖ₁(oₖ), ..., PRFₖᵣ(oₖ)) = u⃗ₖ。因此，单方只需计算每个数据点的索引oₖ，对每个PRF键kᵢ计算PRFₖᵢ(oₖ)（仅需N·r次PRF评估），并累加得sum⃗ᵢ。

**IZK友好的PRF：Legendre PRF**
选择Legendre PRF的原因是：(1) 输出天然为{-1,1}，无需额外比特提取；(2) 在IZK中仅需8个输入或乘法门，远优于SHA-256等。Legendre PRF定义为：PRFₖ(x) = Legendre符号 (x+k)/p mod p，其中p为素数。由于输出为±1，直接对应草图所需的二值元素。在IZK实现中，通过三次多项式近似或预计算表实现高效验证。

**MPC收尾计算**
多方联合计算仅需轻量操作：累加sum⃗ = Σᵢ sum⃗ᵢ，然后比较(1/r)·Σν (sum[ν] - qν)²与阈值Tα,N,p⃗。其中q⃗在MPC外公开计算（使用公共参数p⃗和PRF键），因此MPC仅需O(t+r)次运算，与桶数D无关。

**安全性分析**
在恶意安全模型（静态腐败，最多t-1方共谋）下，HOLMES安全计算理想功能F_{HOLMES}。安全性证明遵循标准的真实/理想范式：要求MPC满足输入加载（定义1），IZK满足输入加载（定义2），一致性检查协议确保两处输入一致。直觉上，集成协议通过一致性检查防止数据篡改，IZK保证单方统计量计算的正确性，MPC处理多方联合部分不泄露额外信息。证明依赖具体协议的安全约减（如全文中引理的证明）。

### 核心公式与流程

**[一致性检查]**
$$\rho = r + \sum_{k=1}^N x_k \cdot \beta^k$$
$$\mathsf{Com}_{\mathsf{ck}_j}(\rho) - \mathsf{Com}_{\mathsf{ck}_j}(r) - \sum_{k=1}^N \mathsf{Com}_{\mathsf{ck}_j}(x_k) \cdot \beta^k = \mathsf{Com}_{\mathsf{ck}_j}(0)$$
> 作用：证明MPC中秘密共享的输入与IZK中承诺的输入一致，r为随机盲化因子，β为随机挑战。

**[多维草图算法]**
$$\overrightarrow{\text{count}} = \sum_{k=1}^N \overrightarrow{\sigma}_k,\quad \mathbf{R} \in \{-1,1\}^{r \times D},\quad \mathbf{R}[i][j] = \mathrm{PRF}_{\mathsf{k}_i}(j)$$
$$\overrightarrow{\text{sum}} = \mathbf{R} \cdot \overrightarrow{\text{count}} = \sum_{k=1}^N \mathbf{R}[o_k],\quad \overrightarrow{\mathbf{q}} = N \cdot \mathbf{R} \cdot \overrightarrow{\mathbf{p}}$$
> 作用：将高维直方图通过伪随机矩阵R投影到低维，保持欧氏距离近似，从而避免指数级桶数。

**[未归一化χ²检验的近似]**
$$\sum_{j=1}^D (\text{count}[j] - N\mathsf{p}_j)^2 \approx \frac{1}{r} \sum_{\nu=1}^r (\text{sum}[\nu] - \mathsf{q}_\nu)^2$$
> 作用：基于Johnson-Lindenstrauss引理，将D维距离比较转换为r维低维比较，r≈200时可实现1.1倍近似因子。

**[Legendre PRF]**
$$\mathrm{PRF}_{\mathsf{k}}(x) = \left(\frac{x + \mathsf{k}}{p}\right) \in \{-1, 1\}$$
> 作用：提供廉价且天然输出{-1,1}的伪随机函数，在IZK中仅需8个乘法门，用于生成草图算法中的伪随机矩阵R。

### 实验结果

实验在AWS c5.9xlarge实例（36核，72GB内存，2Gbps带宽，20ms延迟）上进行。使用域F_p（p=2⁶²-2¹⁶+1），统计安全参数λ=30，计算安全参数κ=128。HOLMES实现基于QuickSilver（集成Silver技术）用于IZK，SCALE-MAMBA和MP-SPDZ用于MPC。对比三个基线：通用MPC（全程使用SCALE-MAMBA）、成对2PC（每对方运行2PC）、NIZK/SNARK（使用Spartan）。对于范围检查，HOLMES比通用MPC快10-256倍，比成对2PC快4-32倍，比SpartanNIZK快1-3倍。对于ZK友好草图（多维χ²测试），HOLMES比通用MPC快35-198倍，比成对2PC快13-36倍，比SpartanNIZK快4-5倍。在银行营销数据集（4个属性，37,500个桶）上，HOLMES比朴素 oblivious bucketing 快10⁴倍，从约10⁵秒降至约22秒。多参与方实验（2-10方）显示，HOLMES开销线性增长于t，而通用MPC呈二次增长，加速比达77-264倍。一致性检查开销小于0.01秒。

### 局限性与开放问题
HOLMES不提供系统性方法指导用户选择必要的分布测试，这取决于具体应用场景（如临床偏倚检测）。分布测试泄露1比特的结果（通过/失败），可能被恶意组织利用进行均值恢复攻击（如通过二分搜索探测均值）。未来的研究方向包括：量化隐私损失并设计缓解措施（如允许测试白名单或速率限制）；探索更高效的底层IZK协议（如基于silent OT的LPZK）以替代QuickSilver；将HOLMES扩展支持鲁棒统计量以抵御数据中毒攻击；研究在保证精度的前提下对大数据集进行子采样（用于分布测试）的理论适用条件。

### 强关联论文

[22] Keller, M. MP-SPDZ: A Versatile Framework for Multi-Party Computation. **CCS 2020** [Google Scholar](https://scholar.google.com/scholar?q=MP+SPDZ+A+Versatile+Framework+for+Multi+Party+Computation)

[23] SCALE-MAMBA. **GitHub** [Google Scholar](https://scholar.google.com/scholar?q=SCALE-MAMBA)

[24] Yang, K. et al. QuickSilver: Efficient and Affordable Zero-Knowledge Proofs for Circuits and Polynomials over Any Field. **CCS 2021** [Google Scholar](https://scholar.google.com/scholar?q=QuickSilver+Efficient+and+Affordable+Zero+Knowledge+Proofs+for+Circuits+and+Polynomials+over+Any+Field)

[25] Setty, S. Spartan: Efficient and General-Purpose zkSNARKs Without Trusted Setup. **CRYPTO 2020** [Google Scholar](https://scholar.google.com/scholar?q=Spartan+Efficient+and+General+Purpose+zkSNARKs+Without+Trusted+Setup)

[34] Johnson, W. B. et al. Extensions of Lipschitz mappings into a Hilbert space. **Contemporary mathematics 1984** [Google Scholar](https://scholar.google.com/scholar?q=Extensions+of+Lipschitz+mappings+into+a+Hilbert+space)

[37] Damgård, I. B. On the randomness of Legendre and Jacobi sequences. **CRYPTO 1988** [Google Scholar](https://scholar.google.com/scholar?q=On+the+randomness+of+Legendre+and+Jacobi+sequences)

[58] Achlioptas, D. Database-Friendly Random Projections: Johnson-Lindenstrauss with Binary Coins. **Journal of Computer and System Sciences 2003** [Google Scholar](https://scholar.google.com/scholar?q=Database+Friendly+Random+Projections+Johnson+Lindenstrauss+with+Binary+Coins)

[59] Couteau, G. et al. Silver: Silent VOLE and Oblivious Transfer from Hardness of Decoding Structured LDPC Codes. **CRYPTO 2021** [Google Scholar](https://scholar.google.com/scholar?q=Silver+Silent+VOLE+and+Oblivious+Transfer+from+Hardness+of+Decoding+Structured+LDPC+Codes)

[85] Corrigan-Gibbs, H. et al. Prio: Private, robust, and scalable computation of aggregate statistics. **NSDI 2017** [Google Scholar](https://scholar.google.com/scholar?q=Prio+Private+robust+and+scalable+computation+of+aggregate+statistics)


## 关键词

+ HOLMES分布测试安全学习
+ 安全多方计算MPC数据质量
+ 零知识证明协作学习
+ ZK友好草图算法
+ 多维分布测试优化
+ 隐私保护机器学习
