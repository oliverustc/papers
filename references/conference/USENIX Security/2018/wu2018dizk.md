---
title: "DIZK: A distributed zero knowledge proof system"
标题简称:
论文类型: conference
会议简称: USENIX Security
发表年份: 2018
modified: 2025-04-27 09:20:34
created: 2025-04-11 11:17:28
---

## DIZK: A distributed zero knowledge proof system

## 发表信息

+ [原文链接](https://www.usenix.org/conference/usenixsecurity18/presentation/wu)
+ [code](https://github.com/scipr-lab/dizk)

## 作者

+ Howard Wu 
+ [Wenting Zheng](Wenting%20Zheng.md)
+ [Alessandro Chiesa](Alessandro%20Chiesa.md)
+ [Raluca Ada Popa](Raluca%20Ada%20Popa.md)
+ Ion Stoica 

## 笔记

### 背景与动机
zkSNARKs支持证明者向验证者证明计算的正确性而不泄露隐私，是实现隐私保护加密货币（如Zcash）的核心技术。然而，zkSNARK的证明者开销巨大，其计算和存储成本与待证明电路规模成准线性关系。现有单机系统在电路规模达到1000至2000万门时即耗尽内存，严重限制了zkSNARK的应用，例如仅能容纳400次SHA-256压缩函数的计算。现有系统采用单机“一体化”架构，内存和计算资源受限于单台机器。本文旨在打破这一瓶颈，将证明者和设置算法的执行分布到计算机集群上，从而支持数十亿门规模的电路，实现“密码学可扩展”。

### 相关工作

[37] Gennaro, R., et al. Quadratic span programs and succinct NIZKs without PCPs. **EUROCRYPT 2013** [Google Scholar](https://scholar.google.com/scholar?q=Quadratic+span+programs+and+succinct+NIZKs+without+PCPs)
> 核心思路：提出QAP，将电路可满足性编码为多项式等式，是语用SNARK的基础。
> 局限与区别：该文仅提出理论框架，未涉及分布式实现。

[42] Groth, J. On the size of pairing-based non-interactive arguments. **EUROCRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=On+the+size+of+pairing-based+non-interactive+arguments)
> 核心思路：提出当前最有效的SNARK协议，证明大小为128字节，验证时间为2毫秒。
> 局限与区别：该协议本身为单机设计，其设置和证明者计算是本文分布式化的目标和起点。

[55] Parno, B., et al. Pinocchio: Nearly practical verifiable computation. **IEEE S&P 2013** [Google Scholar](https://scholar.google.com/scholar?q=Pinocchio%3A+Nearly+practical+verifiable+computation)
> 核心思路：第一个被广泛实现的语用SNARK系统，实现了QAP的端到端证明。
> 局限与区别：与Groth方案类似，Pinocchio也是单机实现，是DIZK在性能对比中的基线之一。

[11] Ben-Sasson, E., et al. SNARKs for C: Verifying program executions succinctly and in zero knowledge. **CRYPTO 2013** [Google Scholar](https://scholar.google.com/scholar?q=SNARKs+for+C%3A+Verifying+program+executions+succinctly+and+in+zero+knowledge)
> 核心思路：展示如何将C程序编译为R1CS约束系统，是构建实际应用的桥梁。
> 局限与区别：该文关注的是前端的编译和后端的单机实现，而非分布式计算。

[15] Ben-Sasson, E., et al. Succinct non-interactive zero knowledge for a von Neumann architecture. **USENIX Security 2014** [Google Scholar](https://scholar.google.com/scholar?q=Succinct+non-interactive+zero+knowledge+for+a+von+Neumann+architecture)
> 核心思路：提出对冯·诺依曼架构程序的SNARK，支持更通用的计算模型。
> 局限与区别：其证明者仍为单机实现，DIZK从电路层面实现对更大规模计算的支持。

[59] SCIPR LAB. libsnark: a C++ library for zk-SNARK proofs. 2017 [Google Scholar](https://scholar.google.com/scholar?q=libsnark%3A+a+C%2B%2B+library+for+zk-SNARK+proofs)
> 核心思路：提供了Groth协议和PGHR协议的高效串行实现，是zkSNARK领域的标杆库。
> 局限与区别：DIZK的分发实现直接与之对比，证明其在大规模电路下的性能突破。

[22] Braun, B., et al. Verifying computations with state. **SOSP 2013** [Google Scholar](https://scholar.google.com/scholar?q=Verifying+computations+with+state)
> 核心思路：提出Pantry系统，将SNARK转化为可验证MapReduce计算的交互式论证。
> 局限与区别：DIZK是分布式证明者，而Pantry是使用单机证明者来验证分布式计算的结果。

[6] skewjoin. 2017 [Google Scholar](https://scholar.google.com/scholar?q=skewjoin)
> 核心思路：提供处理数据倾斜的通用Spark Join算法。
> 局限与区别：DIZK指出通用的skewjoin在QAP任务中性能不佳，并提出了专用的“两段式”混合策略。

[65] Sze, T. Schönhage–Strassen algorithm with MapReduce for multiplying terabit integers. **SNC 2011** [Google Scholar](https://scholar.google.com/scholar?q=Sch%C3%B6nhage%E2%80%93Strassen+algorithm+with+MapReduce+for+multiplying+terabit+integers)
> 核心思路：提出将大整数FFT转换为两轮小FFT以在MapReduce上分布式执行的策略。
> 局限与区别：DIZK将其思想从整数乘法迁移到有限域上的FFT，应用于多项式求值和插值。

[10] Ben-Sasson, E., et al. Zerocash: Decentralized anonymous payments from Bitcoin. **IEEE S&P 2014** [Google Scholar](https://scholar.google.com/scholar?q=Zerocash%3A+Decentralized+anonymous+payments+from+Bitcoin)
> 核心思路：Zcash隐私加密货币的核心技术，展示了zkSNARK的实际应用。
> 局限与区别：该文是DIZK的应用动机之一，但并未解决其局限。

### 核心技术与方案

DIZK的整体目标是实现Groth’16 SNARK协议中设置和证明者算法的分布式执行。其核心思路是将单机上的高内存消耗任务分解为可并行、可分布的计算，并高效处理数据倾斜问题。DIZK将证明者和设置过程设计为分布式任务，关键参数（电路、密钥、见证）以RDD形式存储在集群中，验证者则保持单机轻量。

首先，DIZK抽象出三个基础分布式计算任务。第一是分布式快速多项式算术，包括FFT和Lag计算。对于FFT，DIZK采用一种单次Shuffle的“二维”策略：将长度为n的FFT拆分为$\sqrt{n}$个长度为$\sqrt{n}$的小FFT，第一轮在所有执行器上并行计算，经过一次Shuffle后，第二轮在归约器上完成计算。对于Lag（拉格朗日插值多项式求值），利用定义域为乘法子群时$L_i(X) = \frac{\omega^i / n}{X - \omega^i} \cdot (X^n - 1)$的简单公式，每个执行器接收t值后对各自分块中的i独立计算。第二是固定基多标量乘法fixMSM，用于设置阶段。每个执行器接收从驱动节点广播的查找表和均匀分配标量，并行计算各自的标量乘法，最后收集结果。第三是可变基多标量乘法varMSM，用于证明者阶段。DIZK未采用需要昂贵Shuffle的Pippenger算法，而是将问题均匀划分给各执行器，在每个执行器内串行运行Pippenger算法，最后合并各执行器的结果。

其次，DIZK解决了QAP约简中的数据倾斜问题。在设置阶段，需要计算每行多项式在随机点t的求值，核心是矩阵a（左乘法系数矩阵）与列向量$(L_j(t))_j$的稀疏矩阵-向量乘法。由于a虽然整体稀疏，但其个别列（对应参与大量变量的约束）很稠密，导致默认的Hash Join会产生严重的拖后腿问题。DIZK提出一个两阶段混合策略。第一阶段，通过一个轻量级分布式计数值计算，识别出稠密列。通过随机分配分区避免聚合时的拖后腿，最终标记出非零元素超过阈值的列。第二阶段，对于标记为稠密的列，DIZK将其过滤出来，每个稠密列作为一个单独的作业，从而可以将其分区散布到多个执行器上避免单点瓶颈；对于剩余的稀疏列，则使用标准的Join。最终将两部分结果合并。这个过程同样适用于证明者阶段的QAP见证约简，区别在于此时需要识别稠密行（对应参与大量约束的变量）。DIZK在设置阶段完成稠密行的识别并记录，证明者阶段直接复用。

最后，通过组合上述技术，DIZK实现了分布式设置和分布式证明者。设置过程：输入R1CS实例φ，执行分布式Lag计算得到$(L_j(t))_j$，再执行两阶段混合Join计算得到$(A_i(t))_i$（以及类似地B、C），然后对这些值进行特定的随机线性组合（计算量小），最后通过fixMSM计算其在椭圆曲线上的编码，生成证明密钥pk（RDD）和验证密钥vk（短数组）。分布式证明者过程：接收pk、输入x和见证w，首先执行QAP见证约简。这需要计算多项式$H(X) = \frac{A_z(X) \cdot B_z(X) - C_z(X)}{Z_D(X)}$。计算方式为，先通过两阶段混合Join（利用设置时记录的稠密行信息）计算出$A_z(X),B_z(X),C_z(X)$在域D上的求值，然后利用分布式FFT将它们转换到另一域D’上，计算逐分量除法，再用分布式FFT插值得到H的系数。得到h后，证明者通过varMSM计算最终证明的三个群元素$[A_r]_1, [B_s]_2, [K_{r,s}]_1$。

整个系统假设底层双线性群是安全的，并直接继承了Groth’16协议的完备性、可靠性和零知识性质。DIZK在分布式环境下实现了与该协议相同的功能，因此安全性质保持不变。计算复杂度方面，设置和证明者的计算量均由O(N+M)个域和群操作主导，但通过并行化，在理想情况下（忽略通信开销）可将运行时间降低到约1/P（P为执行器数量）。通信量主要由Shuffle步骤中的数据传输主导。

### 核心公式与流程

**[QAP约简 (实例约简qapI)]**
设域D大小为M。对于矩阵a的第i行，其插值多项式为$A_i(X)$，满足$\forall j: A_i(\omega^j) = a_{i,j}$。执行者计算目标：
$$A_i(t) = \sum_{j=1}^M a_{i,j} L_j(t)$$
> 作用：将R1CS系数矩阵的每行编码为多项式值，用于构建证明密钥。

**[QAP约简 (见证约简qapW)]**
计算多项式H(X)使得下式成立：
$$\left(\sum_{i=0}^N A_i(X) z_i\right) \cdot \left(\sum_{i=0}^N B_i(X) z_i\right) = \sum_{i=0}^N C_i(X) z_i + H(X) \cdot Z_D(X)$$
> 作用：将R1CS的满足性转化为一个多项式可除性问题，是证明者验证的关键。

**[验证方程]**
验证者检查等式：
$$e([A_r]_1, [B_s]_2) = e(\alpha, \beta) + e\left(\sum_{i=0}^k x_i [K_i^{vk}(t)]_1, [\gamma]_2\right) + e([K_{r,s}]_1, [\delta]_2)$$
> 作用：验证证明者提供的三个群元素满足正确性关系，此式Groth协议的核心。

**[在线编码计算]**
证明者计算关键编码：
$$[A_r]_1 := [\alpha]_1 + \sum_{i=0}^N z_i [A_i(t)]_1 + r[\delta]_1$$
> 作用：在证明者阶段，将QAP的求值与随机化因子结合，生成零知识的证明元素。

### 实验结果

DIZK在Amazon EC2上使用r3.large（2 vCPU, 15 GiB内存）和r3.8xlarge（32 vCPU, 244 GiB内存）实例进行评估，集群规模从10到20个节点，支持最多256个执行器。实验采用作者生成的256位Barreto-Naehrig曲线（需支持p-1整除$2^{50}$）。关键结果表明：DIZK支持超过10亿门的电路规模，而对比的单机libsnark实现（Groth协议）在2000万门左右即超出内存。在固定执行器数量时，设置和证明者的运行时间随电路规模接近线性增长；固定电路规模时，运行时间随执行器数量接近线性减少。例如，在28个节点（128执行器）上，设置一个10亿门电路用时约$2^{18}$秒（约72小时），证明者用时约$2^{16}$秒（约18小时）。与未采用优化策略的基线相比，DIZK的混合Join策略使可支持实例大小提升10倍，且运行时间快2-4倍。在个人应用测试中，对一张2048x2048图片进行旋转处理需要1.38亿个约束，约束生成和见证生成在64个执行器上仅需7秒和14.6秒。

### 局限性与开放问题
尽管DIZK显著提升了zkSNARK的可扩展性，但其计算开销仍然非常高昂，对于数十亿门电路仍需动用大型计算集群，成本高企。此外，系统依赖于一个需要秘密随机数的可信设置，该设置过程的规模也随电路增长，其分布式可信执行仍是一个开放问题。类似地，类Groth方案的设置过程无法实现透明设置，仍需信赖的第三方。

### 强关联论文

[42] Groth, J. On the size of pairing-based non-interactive arguments. **EUROCRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=On+the+size+of+pairing-based+non-interactive+arguments)

[37] Gennaro, R., et al. Quadratic span programs and succinct NIZKs without PCPs. **EUROCRYPT 2013** [Google Scholar](https://scholar.google.com/scholar?q=Quadratic+span+programs+and+succinct+NIZKs+without+PCPs)

[55] Parno, B., et al. Pinocchio: Nearly practical verifiable computation. **IEEE S&P 2013** [Google Scholar](https://scholar.google.com/scholar?q=Pinocchio%3A+Nearly+practical+verifiable+computation)

[59] SCIPR LAB. libsnark: a C++ library for zk-SNARK proofs. 2017 [Google Scholar](https://scholar.google.com/scholar?q=libsnark%3A+a+C%2B%2B+library+for+zk-SNARK+proofs)

[57] Pippenger, N. On the evaluation of powers and related problems. **FOCS 1976** [Google Scholar](https://scholar.google.com/scholar?q=On+the+evaluation+of+powers+and+related+problems)

[65] Sze, T. Schönhage–Strassen algorithm with MapReduce for multiplying terabit integers. **SNC 2011** [Google Scholar](https://scholar.google.com/scholar?q=Sch%C3%B6nhage%E2%80%93Strassen+algorithm+with+MapReduce+for+multiplying+terabit+integers)

[22] Braun, B., et al. Verifying computations with state. **SOSP 2013** [Google Scholar](https://scholar.google.com/scholar?q=Verifying+computations+with+state)

[53] Naveh, A., et al. PhotoProof: Cryptographic image authentication for any set of permissible transformations. **IEEE S&P 2016** [Google Scholar](https://scholar.google.com/scholar?q=PhotoProof%3A+Cryptographic+image+authentication+for+any+set+of+permissible+transformations)

[11] Ben-Sasson, E., et al. SNARKs for C: Verifying program executions succinctly and in zero knowledge. **CRYPTO 2013** [Google Scholar](https://scholar.google.com/scholar?q=SNARKs+for+C%3A+Verifying+program+executions+succinctly+and+in+zero+knowledge)

[10] Ben-Sasson, E., et al. Zerocash: Decentralized anonymous payments from Bitcoin. **IEEE S&P 2014** [Google Scholar](https://scholar.google.com/scholar?q=Zerocash%3A+Decentralized+anonymous+payments+from+Bitcoin)


## 关键词

+ DIZK分布式零知识证明
+ 分布式快速傅里叶变换
+ 多标量乘法分布式计算
+ QAP电路可满足性
+ zk-SNARK规模化
+ 计算集群证明生成
