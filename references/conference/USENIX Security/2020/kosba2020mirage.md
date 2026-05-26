---
title: "MIRAGE: Succinct arguments for randomized algorithms with applications to universal zk-SNARKs"
标题简称:
论文类型: conference
会议简称: USENIX Security
发表年份: 2020
modified: 2025-04-11 11:45:38
---

## MIRAGE: Succinct arguments for randomized algorithms with applications to universal zk-SNARKs

## 发表信息

+ [原文链接](https://www.usenix.org/conference/usenixsecurity20/presentation/kosba)

## 作者

+ [Ahmed Kosba](Ahmed%20Kosba.md)
+ [Dimitrios Papadopoulos](Dimitrios%20Papadopoulos.md) 
+ [Charalampos Papamanthou](Charalampos%20Papamanthou.md) 
+ [Dawn Song](Dawn%20Song.md) 

## 笔记

### 背景与动机
零知识证明，特别是具有简洁证明和高效验证的zk-SNARKs，近年来在隐私保护交易、证书验证等应用中受到广泛关注。然而，广泛部署zk-SNARKs的主要障碍之一是其需要为每个不同的计算执行一次可信密钥生成阶段，以维持实际的证明性能。虽然一些方案通过免信任设置或单次可信预处理来消除每计算的可信设置，但代价是证明体积增大或验证开销增加。另一方面，虽然学术界已提出通用电路生成器来避免每计算的预处理，但其证明者的性能在实际应用中仍远不够实用。本文旨在通过设计一个更适合随机化算法的新型zk-SNARK协议，以及一个线性规模的通用电路，来填补这一空白，构建一个兼具简洁性和高效验证的通用zk-SNARK系统。

### 相关工作

[7] Groth. On the size of pairing-based non-interactive arguments. **EUROCRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=On+the+size+of+pairing-based+non-interactive+arguments)
> 核心思路：提出了当时最简洁的基于配对的zk-SNARK，证明大小为128字节，验证仅需3次配对运算。
> 局限与区别：这是非通用方案的基础，需要为每个特定电路进行可信设置，而本文在此基础上设计分离式zk-SNARK以实现通用性，仅增加一个群元素和一次配对。

[4] Ben-Sasson et al. Succinct non-interactive zero knowledge for a von Neumann architecture. **USENIX Security 2014** [Google Scholar](https://scholar.google.com/scholar?q=Succinct+non-interactive+zero+knowledge+for+a+von+Neumann+architecture)
> 核心思路：提出了vnTinyRAM，一个面向冯·诺依曼架构的通用电路。
> 局限与区别：其通用电路大小为 $O(N \log N)$，并且证明者开销比非通用方案高出多个数量级，本文通过线性电路设计显著提升了性能。

[31] Maller et al. Sonic: Zero-knowledge SNARKs from linear-size universal and updateable structured reference strings. **USENIX Security 2020** [Google Scholar](https://scholar.google.com/scholar?q=Sonic%3A+Zero-knowledge+SNARKs+from+linear-size+universal+and+updateable+structured+reference+strings)
> 核心思路：提出了首个具有可更新CRS的线性规模通用zk-SNARK，支持“帮助”和“无助”两种模式。
> 局限与区别：在无助模式下，其证明大小（1152字节）和验证效率均不如本文MIRAGE系统（160字节，验证仅1.4倍于Groth16基线），且证明者开销（50倍）高于本文（30倍）。

[29] Groth et al. Updatable and universal common reference strings with applications to zk-SNARKs. **CRYPTO 2018** [Google Scholar](https://scholar.google.com/scholar?q=Updatable+and+universal+common+reference+strings+with+applications+to+zk-SNARKs)
> 核心思路：提出了通用且可更新的CRS，但大小为 $O(n_{*}^{2})$。
> 局限与区别：二次规模的CRS使其在实用中不可扩展，而本文的MIRAGE采用线性规模的CRS。

[39] Chiesa et al. Marlin: Preprocessing zk-SNARKs with universal and updatable SRS. **EUROCRYPT 2020** [Google Scholar](https://scholar.google.com/scholar?q=Marlin%3A+Preprocessing+zk-SNARKs+with+universal+and+updatable+SRS)
> 核心思路：提出了一个具有通用且可更新SRS的预处理zk-SNARK，其证明速度优于Sonic。
> 局限与区别：证明大小仍为1 KB，验证性能比Groth16基线差约2.6倍。本文MIRAGE的证明更小（160字节），验证性能更好（1.4倍）。

[40] Gabizon et al. PLONK: Permutations over Lagrange-bases for Oecumenical Non-interactive arguments of Knowledge. **ePrint 2019** [Google Scholar](https://scholar.google.com/scholar?q=PLONK%3A+Permutations+over+Lagrange-bases+for+Oecumenical+Non-interactive+arguments+of+Knowledge)
> 核心思路：改进了Sonic，提出PLONK，具有较小的证明大小（448-512字节）和更高效的证明者。
> 局限与区别：本文MIRAGE的证明大小（160字节）和验证器性能仍优于PLONK，更适合对验证效率有严格要求的应用。

[1] Gennaro et al. Quadratic span programs and succinct NIZKs without PCPs. **EUROCRYPT 2013** [Google Scholar](https://scholar.google.com/scholar?q=Quadratic+span+programs+and+succinct+NIZKs+without+PCPs)
> 核心思路：提出了基于二次算术程序（QAP）的zk-SNARK，奠定了许多后续工作的基础。
> 局限与区别：该方案需要针对每个计算进行可信设置，本文在随机算法和通用电路方面对其进行了扩展。

### 核心技术与方案

**整体框架**  
MIRAGE由两个核心组件构成：一是针对MA（Merlin-Arthur）复杂性类的分离式zk-SNARK协议，它允许在电路中高效使用随机化检查；二是一个线性规模的通用电路，其核心是使用基于随机点的多项式相等性检验来验证排列。这两个组件结合，构建了MIRAGE通用zk-SNARK系统。

**分离式zk-SNARK**  
该协议是对Groth16 [7] 的改进。其核心思想是将电路中的见证值分为两组：一组是“确定性的”（集合J），其值不依赖于随机数；另一组是“随机依赖的”。证明过程被分为两阶段：第一阶段，证明者仅使用确定性的值计算部分证明 $\pi_J$ 并发送给验证者；第二阶段，验证者发送随机挑战r，证明者再使用随机r完成剩余证明。在非交互版本中，随机挑战通过哈希函数计算得到。这一分离使得随机数可以事后生成，避免了在电路中直接编码随机性生成逻辑带来的巨大开销。与Groth16相比，该方案在证明中仅增加了一个群元素，验证仅增加了一次配对运算。其知识可靠性在通用群模型下证明。

**线性规模通用电路**  
通用电路的目标是验证任意算术电路的正确性，关键在于检查变量值在不同操作间的一致性。传统方法（如vnTinyRAM [4]）使用排列网络，开销为 $O(n \log n)$ 。本文采用一个更高效的方法：给定两个向量 $\mathbf{v}$ 和 $\mathbf{w}$ ，它们是彼此的排列当且仅当多项式 $\prod(x - v_i)$ 和 $\prod(x - w_i)$ 相等。通过在随机点 $r$ 上检验多项式的值，可以 $O(n)$ 时间验证排列。该随机化检验是MA语言的一部分，其错误概率可被Schwartz-Zippel引理界定。

**MIRAGE系统**  
MIRAGE将分离式zk-SNARK应用于上述随机化通用电路 $C_{univ}$ 。系统包含一个信任的全局设置阶段，生成通用参考字符串（CRS）。对于每个自定义电路C，一个不用信任的“推导”阶段根据C的规格计算一个32字节的验证密钥摘要 $\mathsf{vk}_{spec}$。证明者使用CRS运行分离式zk-SNARK协议，证明 $C_{univ}$ 是可满足的，即存在见证值使得原始电路C正确。验证者是针对Groth16的简单扩展，执行4次配对运算和 $u$ 次指数运算。系统的渐进复杂度为：证明者 $O(N \log N)$ 次运算，证明大小 $O(1)$ ，验证者 $O(u)$ 次运算，其中 $N$ 是通用电路的操作数上界，$u$ 是公共输入的大小。

### 核心公式与流程

**分离式Groth16协议的验证方程**
$$
e(\pi_A, \pi_B) = e(g_1^{\alpha}, g_2^{\beta}) \cdot e(g_1^{\Psi_{io}(s)/\gamma}, g_2^{\gamma}) \cdot e(\pi_C, g_2^{\delta}) \cdot e(\pi_D, g_2^{\delta'})
$$
> 作用：该验证方程是MIRAGE的核心。与Groth16相比，它增加了一个额外的配对项 $e(\pi_D, g_2^{\delta'})$，用于检查证明者对“确定性”见证（集合J）的承诺，从而实现了对随机化算法的支持。

**通用电路的排列检查**
$$
\prod_{i=1}^{n_s+3n_*+3n_+} ((l_i + r_2 z_i) - r_1) = \prod_{i=1}^{n_s+3n_*+3n_+} ((l_i' + r_2 z_i') - r_1)
$$
> 作用：该公式是通用电路线性规模的核心。通过在随机点 $(r_1, r_2)$ 上检验两个多项式相等，可以 $O(n)$ 时间验证标签-值对集合 $\{(l_i, z_i)\}$ 是否是另一个集合 $\{(l_i', z_i')\}$ 的排列，从而避免了使用 $O(n \log n)$ 的排列网络。

**通用电路中分离式zk-SNARK的承诺**
$$
\pi_D = g_1^{\delta \kappa_3} \prod_{k \in I_{Z_w} \cup I_{Z'}} g_1^{c_k(\beta v_k(s) + \alpha w_k(s) + y_k(s)) / \delta'}
$$
> 作用：$\pi_D$ 是分离式zk-SNARK中“确定性”部分证明的核心。它由证明者在第一阶段计算，包含了电路中所有不属于IO且不依赖随机数的见证值的承诺。验证者通过 $\pi_D$ 来保证这些确定性值的有效性，是协议实现随机检查的关键。

### 实验结果
实验在一台EC2 c5d.9xlarge实例上进行，使用libsnark的Groth16实现作为基线。在隐私保护智能合约场景中（6位参与者的拍卖和众筹），MIRAGE的全局可信设置为610秒，生成1.8 GB的证明密钥和473 KB的验证密钥。对于每个应用，非信任的密钥推导仅需7.9秒，生成32字节合约摘要。证明时间分别为322秒和319秒，证明大小为160字节，验证时间为2.1毫秒。对比基线HAWK系统，其需要每应用进行22秒的信任设置，生成128字节证明和1.5毫秒验证时间。MIRAGE的证明者开销是34倍，但由于省略了每应用信任设置，适用于更灵活的场景。在电路规模对比中，对于相同约束数（约530万），MIRAGE支持的矩阵乘法参数m=41（vnTinyRAM仅支持m=7），归并排序参数m=200（vnTinyRAM仅支持m=32），显示出高两个数量级的规模提升。对于不同计算原语，MIRAGE的证明者开销振幅为3倍至26倍，而vnTinyRAM预期高1至2个数量级。

### 局限性与开放问题
MIRAGE的主要局限在于其CRS不可更新，而Sonic [31]等方案支持更新。电路设计中的操作码分布虽采用启发式分配，但并非所有应用中都是最优的，需要进行基于应用的负载特征分析来优化。此外，本文的低级库需要用户理解操作码才能高效使用，未来需要更高级的编译工具。

### 强关联论文

[7] Groth. On the size of pairing-based non-interactive arguments. **EUROCRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=On+the+size+of+pairing-based+non-interactive+arguments)

[4] Ben-Sasson et al. Succinct non-interactive zero knowledge for a von Neumann architecture. **USENIX Security 2014** [Google Scholar](https://scholar.google.com/scholar?q=Succinct+non-interactive+zero+knowledge+for+a+von+Neumann+architecture)

[31] Maller et al. Sonic: Zero-knowledge SNARKs from linear-size universal and updateable structured reference strings. **USENIX Security 2020** [Google Scholar](https://scholar.google.com/scholar?q=Sonic%3A+Zero-knowledge+SNARKs+from+linear-size+universal+and+updateable+structured+reference+strings)

[29] Groth et al. Updatable and universal common reference strings with applications to zk-SNARKs. **CRYPTO 2018** [Google Scholar](https://scholar.google.com/scholar?q=Updatable+and+universal+common+reference+strings+with+applications+to+zk-SNARKs)

[39] Chiesa et al. Marlin: Preprocessing zk-SNARKs with universal and updatable SRS. **EUROCRYPT 2020** [Google Scholar](https://scholar.google.com/scholar?q=Marlin%3A+Preprocessing+zk-SNARKs+with+universal+and+updatable+SRS)

[40] Gabizon et al. PLONK: Permutations over Lagrange-bases for Oecumenical Non-interactive arguments of Knowledge. **ePrint 2019** [Google Scholar](https://scholar.google.com/scholar?q=PLONK%3A+Permutations+over+Lagrange-bases+for+Oecumenical+Non-interactive+arguments+of+Knowledge)

[1] Gennaro et al. Quadratic span programs and succinct NIZKs without PCPs. **EUROCRYPT 2013** [Google Scholar](https://scholar.google.com/scholar?q=Quadratic+span+programs+and+succinct+NIZKs+without+PCPs)

[30] Campanelli et al. LegoSNARK: Modular design and composition of succinct zero-knowledge proofs. **ePrint 2019** [Google Scholar](https://scholar.google.com/scholar?q=LegoSNARK%3A+Modular+design+and+composition+of+succinct+zero-knowledge+proofs)

[16] Kosba et al. Hawk: The blockchain model of cryptography and privacy-preserving smart contracts. **IEEE S&P 2016** [Google Scholar](https://scholar.google.com/scholar?q=Hawk%3A+The+blockchain+model+of+cryptography+and+privacy-preserving+smart+contracts)


## 关键词

+ MIRAGE通用zk-SNARK
+ 随机化算法零知识证明
+ 通用电路生成器
+ 无可信设置SNARKs
+ 隐私保护智能合约
+ 线性通用电路构造