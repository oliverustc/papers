---
title: "QuickSilver: Efficient and Affordable Zero-Knowledge Proofs for Circuits and Polynomials over Any Field"
doi: 10.1145/3460120.3484556
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2021
modified: 2025-04-09 15:56:12
---
## QuickSilver: Efficient and Affordable Zero-Knowledge Proofs for Circuits and Polynomials over Any Field

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3460120.3484556)

## 作者

+ [Kang Yang](Kang%20Yang.md)
+ Pratik Sarkar
+ [Chenkai Weng](Chenkai%20Weng.md)
+ [Xiao Wang](Xiao%20Wang.md)

## 笔记

好的，这是根据您提供的论文全文生成的详尽结构化笔记。

### 背景与动机
零知识证明在证明大规模计算时，内存消耗常成为瓶颈。大多数非交互式证明（如zk-SNARKs）要求证明者和验证者的内存与电路规模呈线性关系，这限制了其可处理问题的规模。近年来，基于子域向量不经意线性评估（sVOLE）的交互式协议为突破这一瓶颈提供了新方向，这类协议允许双方仅使用验证明文所需的最小内存来证明任意大电路。例如，基于隐私保护乱码电路的ZKBoo和基于MPC-in-the-head的协议虽然满足小内存需求，但计算和通信开销仍较高。现有基于sVOLE的协议如Wolverine和Mac‘n’Cheese虽已取得显著进展，但仍存在核心挑战：Wolverine在支持小域（如布尔电路）时，因采用“切-选”技术而引入高开销；而所有此类协议均需要与乘法门数量成正比的线性通信量。特别地，LPZK协议在门式范式下实现了每个乘法门仅一个域元素的“最佳”通信量，但仅适用于大域，且未有实现。本文旨在填补这些空白，提出一个在任意域上每个非线性门仅需一个域元素的通信量的协议（QuickSilver），并进一步挖掘超越门式范式的可能性，实现对多项式集的高效证明，从而在特定场景下将通信量降至亚线性。

### 相关工作

[48] Weng, Yang, Katz, Wang. Wolverine: Fast, Scalable, and Communication-Efficient Zero-Knowledge Proofs for Boolean and Arithmetic Circuits. **CCS 2021** [Google Scholar](https://scholar.google.com/scholar?q=Wolverine%3A+Fast%2C+Scalable%2C+and+Communication-Efficient+Zero-Knowledge+Proofs+for+Boolean+and+Arithmetic+Circuits)
> 核心思路：基于sVOLE构建ZK协议，支持任意域，通信量约为每个乘法门4个域元素。
> 局限与区别：处理小域时使用切-选技术导致高开销；每个乘法门通信量仍较高。

[3] Baum, Malozemoff, Rosen, Scholl. Mac‘n’Cheese: Zero-Knowledge Proofs for Boolean and Arithmetic Circuits with Nested Disjunctions. **CRYPTO 2021** [Google Scholar](https://scholar.google.com/scholar?q=Mac%27n%27Cheese%3A+Zero-Knowledge+Proofs+for+Boolean+and+Arithmetic+Circuits+with+Nested+Disjunctions)
> 核心思路：提出一种ZK协议，在大域上每个乘法门通信3个域元素，并支持“堆叠”技术优化分支电路。
> 局限与区别：应用场景局限于具有多个分支的电路；通信量仍未达到最优。

[25] Dittmer, Ishai, Ostrovsky. Line-Point Zero Knowledge and Its Applications. **ITC 2021** [Google Scholar](https://scholar.google.com/scholar?q=Line-Point+Zero+Knowledge+and+Its+Applications)
> 核心思路：在门式范式下实现了理论上最优的每个乘法门1个域元素通信量。
> 局限与区别：仅支持大域，且缺乏实际实现。

[32] Ishai, Kushilevitz, Ostrovsky, Sahai. Zero-knowledge from secure multiparty computation. **STOC 2007** [Google Scholar](https://scholar.google.com/scholar?q=Zero-knowledge+from+secure+multiparty+computation)
> 核心思路：提出了“MPC-in-the-head”范式，用于构建流式ZK协议，实现小内存消耗。
> 局限与区别：计算和通信效率较低，难以处理大规模电路。

[27] Frederiksen, Nielsen, Orlandi. Privacy-Free Garbled Circuits with Applications to Efficient Zero-Knowledge. **EUROCRYPT 2015** [Google Scholar](https://scholar.google.com/scholar?q=Privacy-Free+Garbled+Cir cuits+with+Applications+to+Efficient+Zero-Knowledge)
> 核心思路：利用隐私保护乱码电路构建高效的ZK协议，满足小内存需求。
> 局限与区别：基于门式范例，每个AND门存在通信下界（κ比特），限制了进一步优化。

### 核心技术与方案

本文的核心技术围绕一个核心观察展开：sVOLE生成的IT-MACs具有线性关系，可以将对乘法门正确性的非线性验证转化为线性关系验证。具体而言，对于一个正确的乘法门 $(w_\alpha, w_\beta, w_\gamma = w_\alpha \cdot w_\beta)$，以及与之关联的MAC值 $k_i = m_i + w_i \cdot \Delta$，验证者本地计算 $B_i = k_\alpha \cdot k_\beta - k_\gamma \cdot \Delta$，而证明者本地计算 $A_{0,i} = m_\alpha \cdot m_\beta$ 和 $A_{1,i} = w_\alpha \cdot m_\beta + w_\beta \cdot m_\alpha - m_\gamma$。当乘法正确时，$B_i = A_{0,i} + A_{1,i} \cdot \Delta$ 成立，这是一个关于$\Delta$的线性方程。若乘法不正确，该关系成立的几率仅为 $2/p^r$。为了批量验证电路中所有$t$个乘法门，双方利用一个随机系数 $\chi$ 对所有线性关系进行随机线性组合，将$t$个方程的检查归约为检查单个方程 $B = A_0 + A_1 \cdot \Delta$，其中$B = \sum_i B_i \chi^i + B^*$，$A_0 = \sum_i A_{0,i} \chi^i + A_0^*$，$A_1 = \sum_i A_{1,i} \chi^i + A_1^*$。最后，利用一个预先生成的VOPE相关值 $(A_0^*, A_1^*, B^*)$ 来掩盖 $A_0$ 和 $A_1$，证明者发送 $U = A_0 + A_0^*$ 和 $V = A_1 + A_1^*$，验证者检查 $B + B^* = U + V \cdot \Delta$。此协议在sVOLE混合模型中完美实现了每个乘法门仅1个域元素的通信，并支持任意域。

本文的第二项关键技术是将上述思路从单个乘法门推广到任意低次多项式，旨在超越门式范例。对于一组$t$个定义在$n$个变量上的、最高次数为$d$的多项式 $\{f_i = \sum_{h=0}^d f_{i,h}\}$，其中$f_{i,h}$仅包含$h$次项，证明者需要证明 $f_i(\boldsymbol{w}) = 0$。核心思想是，验证者计算 $B_i = \sum_{h=0}^d f_{i,h}(k_1,...,k_n) \cdot \Delta^{d-h}$，证明者定义一个单变量多项式 $g_i(x) = \sum_{h=0}^d f_{i,h}(m_1 + w_1 x, ..., m_n + w_n x) \cdot x^{d-h}$。通过巧妙的代数变换，可以证明 $B_i = \sum_{h=0}^{d-1} A_{i,h} \cdot \Delta^h$，其中 $\{A_{i,h}\}$ 是$g_i(x)$的低次项系数，证明者可以本地计算。这同样将多项式满足性问题转化为了一个关于$\Delta$的$d-1$次多项式求值问题，可以看作一个向量不经意多项式评估（VOPE）。通过随机线性组合，所有$t$个多项式可以一并验证，总通信成本仅为$(n + d)\kappa$比特（用于承诺输入和一次VOPE检查），与多项式中的乘法次数无关。该协议的完备性和可靠性（错误概率 $(d+t)/p^r$）均基于$\Delta$的均匀随机性和保密性。系统渐近通信量为$O(n + d)$个域元素，证明者计算量为$O(t d^2 z + d n)$，验证者计算量为$O(t d z)$，其中$z$是单项式最大数量。

这两个协议均具有常数轮，且其在线阶段可通过Fiat-Shamir启发式转换为非交互式，但此时安全性降为计算安全。此多项式证明协议直接应用于多个场景：证明矩阵乘法时，通信与输入矩阵大小$O(n^2)$成正比，而非乘法次数$O(n^3)$；证明SIS问题的解时，通过低次多项式表示解的约束（如比特范围），通信和计算效率相比Wolverine有数量级提升。对于具有一定“弱均匀性”的电路（即其中包含多项式表示有界度的子电路），可结合电路协议与多项式协议，在子电路层面实现亚线性通信。

### 核心公式与流程

**[电路ZK协议：验证乘法门的关系]**
$$B_i = k_\alpha \cdot k_\beta - k_\gamma \cdot \Delta = A_{0,i} + A_{1,i}\cdot \Delta - e_i \cdot \Delta^2$$
> 作用：对于第$i$个乘法门，若其计算正确（错误$e_i=0$），则$B_i$与证明者计算的值$A_{0,i}, A_{1,i}$满足线性关系。这是将非线性检查转化为线性检查的核心。

**[电路ZK协议：批量验证]**
$$W = \sum_{i\in[t]} B_i \cdot \chi^i + B^* \quad \text{and} \quad U = \sum_{i\in[t]} A_{0,i} \cdot \chi^i + A_0^*, \quad V = \sum_{i\in[t]} A_{1,i} \cdot \chi^i + A_1^*$$
$$W = U + V \cdot \Delta$$
> 作用：通过随机系数$\chi$，将$t$个乘法门的验证合并为一个单一的线性方程$W = U + V \cdot \Delta$，其中验证者已知$W$和$\Delta$，证明者已知$U$和$V$，通信量仅为两个域元素$(U, V)$。

**[多项式ZK协议：核心代数变换]**
$$B_i = \sum_{h=0}^d f_{i,h}(k_1,...,k_n) \cdot \Delta^{d-h} = \sum_{h=0}^{d-1} A_{i,h} \cdot \Delta^h + f_i(\boldsymbol{w}) \cdot \Delta^d$$
> 作用：将多项式满足性验证$f_i(\boldsymbol{w})=0$转化为方程$B_i = \sum_{h=0}^{d-1} A_{i,h} \cdot \Delta^h$，其中系数$A_{i,h}$可由证明者本地计算。当向量$\boldsymbol{w}$不满足多项式时，$f_i(\boldsymbol{w})\cdot\Delta^d$项破坏了该线性关系。

### 实验结果

实验在两台Amazon EC2 m5.2xlarge实例上（模拟不同网络带宽）进行，使用单线程，实现了计算安全参数$\kappa=128$和统计安全参数$\rho \approx 100$（布尔电路）或$\rho \ge 40$（61位算术电路）。其电路ZK协议在本地主机环境下，单线程处理布尔电路速度达每秒760万AND门，处理算术电路速度达每秒480万乘法门。在20Mbps网络下，布尔电路性能为每秒620万门。相比于当时最先进的Wolverine协议，QuickSilver在布尔电路上实现了6倍的计算加速和7倍的通信压缩；在算术电路上，计算加速超过7倍，通信压缩3-4倍。在AWS最低配实例（1.9美分/小时）上，使用单线程，20Mbps网络下布尔电路吞吐量仍达每秒530万门。其多项式ZK协议在证明两个1024x1024矩阵的乘法时，仅需10秒和25MB通信量，远优于Wolverine的1627秒和34GB通信。在证明SIS解问题上，对于$n=2048, m=1024, \log q=32$的实例，QuickSilver仅需2ms和4.1KB通信，而Wolverine需220ms和32.8KB通信。

### 局限性与开放问题
尽管QuickSilver在通信和计算效率上取得了巨大优势，但其仍为交互式协议，且证明大小（通信量）线性于电路规模，对于需要极短证明或非交互式的应用场景，仍存在局限。其次，对于不具有任何“弱均匀性”的通用电路，其主要优势仍体现在门式层面上，无法自动实现亚线性通信。最后，文中多项式协议依赖的“度分离”表示格式，对于某些高度复杂或非代数结构的计算，可能难以高效表达。

### 强关联论文

[48] Weng, Yang, Katz, Wang. Wolverine: Fast, Scalable, and Communication-Efficient Zero-Knowledge Proofs for Boolean and Arithmetic Circuits. **CCS 2021**

[3] Baum, Malozemoff, Rosen, Scholl. Mac‘n’Cheese: Zero-Knowledge Proofs for Boolean and Arithmetic Circuits with Nested Disjunctions. **CRYPTO 2021**

[25] Dittmer, Ishai, Ostrovsky. Line-Point Zero Knowledge and Its Applications. **ITC 2021**

[32] Ishai, Kushilevitz, Ostrovsky, Sahai. Zero-knowledge from secure multiparty computation. **STOC 2007**

[27] Frederiksen, Nielsen, Orlandi. Privacy-Free Garbled Circuits with Applications to Efficient Zero-Knowledge. **EUROCRYPT 2015**

[17] Boyle, Couteau, Gilboa, Ishai, Kohl, Rindal, Scholl. Efficient Two-Round OT Extension and Silent Non-Interactive Secure Computation. **CCS 2019**

[41] Schoppmann, Gascón, Reichert, Raykova. Distributed Vector-OLE: Improved Constructions and Implementation. **CCS 2019**

[49] Yang, Weng, Lan, Zhang, Wang. Ferret: Fast Extension for Correlated OT with Small Communication. **CCS 2020**

[52] Zhang, Xie, Zhang, Song. Transparent Polynomial Delegation and Its Applications to Zero Knowledge Proof. **IEEE S&P 2020**

[42] Setty. Spartan: Efficient and General-Purpose zkSNARKs Without Trusted Setup. **CRYPTO 2020**


## 关键词

+ 零知识证明
+ 电路验证
+ 通信优化
+ 内存高效
+ 隐私保护