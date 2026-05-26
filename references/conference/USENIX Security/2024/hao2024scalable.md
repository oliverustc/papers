---
title: "Scalable Zero-knowledge Proofs for Non-linear Functions in Machine Learning"
标题简称:
论文类型: conference
会议简称: USENIX Security
发表年份: 2024

modified: 2025-05-07 22:36:19
created: 2025-04-07 17:02:00
---

## Scalable Zero-knowledge Proofs for Non-linear Functions in Machine Learning

## 发表信息

+ [原文链接](https://www.usenix.org/conference/usenixsecurity24/presentation/hao-meng-scalable)

## 作者

+ [Meng Hao](Meng%20Hao.md)
+ Hanxiao Chen
+ [Hongwei Li](Hongwei%20Li.md)
+ [Chenkai Weng](Chenkai%20Weng.md)
+ Yuan Zhang
+ Haomiao Yang
+ Tianwei Zhang

## 笔记

### 背景与动机

在机器学习即服务（MLaaS）中，服务提供者向客户证明推理结果的完整性是一个关键的安全需求，零知识证明为此提供了理论基础。然而，现有面向机器学习的零知识证明协议 [57, 40] 在处理现代复杂模型（如卷积神经网络和大语言模型）时，性能瓶颈主要集中于非线性函数的评估。以 SOTA 工作 Mystique [57] 为例，其处理 ResNet-101 模型一次推理中非线性层的时间约占 8 分钟，占据总运行时长的 80% 以上。该低效的根本原因在于，线性层在素数域 $\mathbb{F}_p$ 上运行，而非线性函数必须通过昂贵的算术-布尔转换（如 zk-edaBits [2, 57]）转为布尔电路才能评估，这一过程的乘法复杂度至少为 $O(\log p)$，且布尔电路求值本身也具有高昂开销。因此，设计避免算术-布尔转换的高效非线性函数零知识证明框架，是推进零知识证明在机器学习领域大规模部署的核心挑战。本文试图填补高性能、可扩展的非线性函数零知识证明这一空白。

### 相关工作

[2] Carsten Baum et al. Appenzeller to Brie: Efficient Zero-Knowledge Proofs for Mixed-Mode Arithmetic and $\mathbb{Z}_{2^k}$. **CCS 2021** [Google Scholar](https://scholar.google.com/scholar?q=Appenzeller+to+Brie%3A+Efficient+Zero-Knowledge+Proofs+for+Mixed-Mode+Arithmetic+and+Z2k)
> 核心思路：提出了 zk-edaBits，用于在零知识证明中高效实现算术域与布尔域之间的转换。
> 局限与区别：该转换本身开销巨大，是导致非线性函数评估瓶颈的主因。本文通过表查找技术完全避免了此类转换。

[40] Tianyi Liu et al. zkCNN: Zero Knowledge Proofs for Convolutional Neural Network Predictions and Accuracy. **CCS 2021** [Google Scholar](https://scholar.google.com/scholar?q=zkCNN%3A+Zero+Knowledge+Proofs+for+Convolutional+Neural+Network+Predictions+and+Accuracy)
> 核心思路：专为卷积神经网络设计了高效的零知识证明协议，特别是 Maxpooling 和 ReLU 函数。
> 局限与区别：协议专用性强，难以扩展到本文所关注的更复杂的非线性函数（如 Sigmoid、GELU 等），且同样依赖算术-布尔转换。

[57] Chenkai Weng et al. Mystique: Efficient Conversions for Zero-Knowledge Proofs with Applications to Machine Learning. **USENIX Security 2021** [Google Scholar](https://scholar.google.com/scholar?q=Mystique%3A+Efficient+Conversions+for+Zero-Knowledge+Proofs+with+Applications+to+Machine+Learning)
> 核心思路：提出了最先进的零知识机器学习推理框架，利用 zk-edaBits 实现高效的算术-布尔转换。
> 局限与区别：其转换和布尔电路求值在非线性函数评估中开销巨大，是本文的主要性能对比基线，本文实现了 50~179 倍的运行速度提升。

[51] Srinath Setty et al. Unlocking the Lookup Singularity with Lasso. **ePrint 2023** [Google Scholar](https://scholar.google.com/scholar?q=Unlocking+the+Lookup+Singularity+with+Lasso)
> 核心思路：提出一种通用的查找论证（lookup argument）方法。
> 局限与区别：该方法针对具有可分解性或低度扩展结构等特定类型的表格进行了优化，无法直接应用于本文所需的通用非线性函数表查找场景。

[61] Arantxa Zapico et al. Caulk: Lookup Arguments in Sublinear Time. **CCS 2022** [Google Scholar](https://scholar.google.com/scholar?q=Caulk%3A+Lookup+Arguments+in+Sublinear+Time)
> 核心思路：提出 Caulk，一种亚线性时间的查找论证。
> 局限与区别：实验表明，在大小为 $2^{12}$ 的表格上进行单次分摊访问时，Caulk 需要 177.451ms，而本文基于只读内存（ROM）的协议仅需 0.069ms（约 2571 倍更优），不适合本文的高效批量查找需求。

[48] Deevashwer Rathee et al. CrypTFlow2: Practical 2-Party Secure Inference. **CCS 2020** [Google Scholar](https://scholar.google.com/scholar?q=CrypTFlow2%3A+Practical+2-Party+Secure+Inference)
> 核心思路：提出了高效的双方安全推理协议，用于安全多方计算（MPC）场景。
> 局限与区别：该文属于 MPC 领域，侧重于保护输入隐私而非计算结果的可验证性，且不涉及本文所需的零知识证明。但其观察 $1\{x<c\} = 1\{x_1<c_1\} + 1\{x_1=c_1\}·1\{x_0<c_0\}$ 被本文借鉴于比较协议的构造。

[47] Deevashwer Rathee et al. SiRnn: A Math Library for Secure RNN Inference. **IEEE S&P 2021** [Google Scholar](https://scholar.google.com/scholar?q=SiRnn%3A+A+Math+Library+for+Secure+RNN+Inference)
> 核心思路：为安全循环神经网络推理设计了数学库，用于 MPC 环境。
> 局限与区别：其中的 Msnzb 算法和 Goldschmidt 迭代算法等被本文参考，但本文将这些算法移植到了零知识证明环境中，并利用表查找技术进行了重构以降低复杂度。

### 核心技术与方案

本文提出了一个基于表查找思想的系统性零知识证明框架，用于高效评估机器学习中的非线性函数。其核心创新在于通过设计一系列基础构建模块，将输入分解为小数字后利用小型查找表进行验证，从而避免了昂贵的算术-布尔转换。

该框架分为三个层次。底层是四个关键的构建模块：数字分解、比较、截断和最高非零位。这些模块在分摊设置下均达到 $O(1)$ 的乘法复杂度。

数字分解通过将大数据值 $x$ 分解为常数 $k$ 个小数字 $x_0, \dots, x_{k-1}$，使得每个数字对应的查找表大小仅为 $2^{d_i}$（$d_i$ 通常为 5-12 比特）。协议利用范围检查和 CheckZero 过程验证分解的正确性。恶意证明者可能通过提供 $x+p$ 的分解来欺骗，这通过后续的比较协议确保分解结果小于素数 $p$ 来解决。

比较协议基于一个经典观察 $1\{x<c\} = 1\{x_1<c_1\} + 1\{x_1=c_1\}·1\{x_0<c_0\}$ [21, 48]。关键优化是将 $2k$ 次表查找和 $k$ 次乘法运算减少到仅 $k+1$ 次表查找。具体地，通过一种紧凑编码将 $z_i = 2^{k+i}·1\{x_i<c_i\} + 2^i·1\{x_i=c_i\}$ 合并，最后通过一个额外的表查找汇总所有 $z_i$ 得到最终比较结果。

截断协议分为正数和一般情况。对于正数，直接利用数字分解协议丢弃低位数字即可。对于负数，其关键洞察是将输入 $x$ 的二进制补码翻转后处理：计算 $\bar{x} = -1·x - 1$，执行正数截断得到 $\bar{y}$，再翻转得到 $y = -1·\bar{y} - 1$。

最高非零位协议利用性质 $2^y \le x \le 2^{y+1}-1$ 验证索引 $y$ 的正确性。证明者提供 $z_0=2^y$ 和 $z_1$，然后协议通过两个比较验证 $x \in [z_0, z_1]$。特别处理了 $y = \lceil \log p \rceil - 2$ 时 $2^{\ell-1} - 1$ 可能溢出正整数范围的问题，将其 $z_1$ 替换为 $(p-1)/2$，保证了正确性和可靠性。

基于这些构建模块，上层分别构造了指数、除法和倒数平方根等数学函数的零知识证明。例如，指数函数通过将输入 $x$ 分解为小数字，对每个数字独立查表计算 $\left(\frac{1}{e}\right)^{2^{\sum d_j}\cdot \hat{x}_i}$，最后通过多次乘法与截断合并结果。除法采用 Goldschmidt 算法，首先利用 Msnzb 和表查找对输入进行归一化和初始近似，然后进行迭代运算，最后反向归一化输出。

所有协议的安全性在通用可组合（UC）框架 [6] 下证明，通过模拟器保证诚实验证者的安全。对于恶意证明者，模拟器可以完美模拟协议视图，仅在 CheckZero 步骤存在可忽略的统计误差。协议的总通信量和计算量（以乘法门计）在分摊后均为 $O(1)$ 常数，与输入比特长度无关。

### 核心公式与流程

**[数字分解的核心等式]**
$$
x = x_{0} + \sum_{i \in [1, k-1]} 2^{\sum_{j \in [0, i-1]} d_j} x_i
$$
> 作用：验证分解结果 $x_0, \dots, x_{k-1}$ 是否正确地复现了原输入 $x$。协议利用此等式计算 $[z]_p$ 并执行 CheckZero 过程。

**[比较的递归关系]**
$$
1\{x < c\} = 1\{x_1 < c_1\} + 1\{x_1 = c_1\} \cdot 1\{x_0 < c_0\}
$$
> 作用：将大数据比较转换为小数字比较的递归组合，是本文比较协议的理论基础。

**[比较中的紧凑编码]**
$$
z_i = 2^{k+i} \cdot 1\{x_i < c_i\} + 2^i \cdot 1\{x_i = c_i\}
$$
> 作用：将比较结果和相等判定编码成一个值，从而将每个小数字的两次表查找（比较和相等）减少为一次。

**[负数截断的比特翻转操作]**
$$
\bar{x} = -1 \cdot x - 1
$$
> 作用：将负数 $x$ 的二进制补码表示转换为正数 $\bar{x}$，从而可以应用正数截断协议处理。

**[Msnzb 的边界性质]**
$$
2^y \le x \le 2^{y+1} - 1
$$
> 作用：定义了 Msnzb 函数输出的正确性条件，协议通过验证 $x$ 是否落在 $[z_0, z_1]$ 区间内来判断 $y$ 的正确性。

### 实验结果

实验在 AWS c5.9xlarge 实例（Intel Xeon 8000 series, 3.6GHz）上使用单线程进行，网络带宽设定为 500Mbps（除非特别说明）。实现基于 EMP 工具包 [55]，采用 61 位 Mersenne 素数域 $p = 2^{61} - 1$，默认实例数为 $10^5$，尺度参数为 12。对比基线为 SOTA 方案 Mystique [57]。

关键性能数值表明，本文的构建模块在分摊后运行时间均为数十微秒级别，例如数字分解（DigitDec）为 10.320μs（200Mbps），比较验证（VrfyCmp）为 15.862μs。对于数学函数，在 500Mbps 带宽下，指数运行 8.696 秒，分别比 Mystique 快约 130 倍；除法 9.837 秒，快约 63 倍；倒数平方根 11.836 秒，快约 70 倍。

在机器学习非线性函数评估中，优势更为显著。对于 ReLU，本文运行 1.906 秒，Mystique 需 193.797 秒（提升约 102 倍）；对于 GELU，本文 32.696 秒 vs. Mystique 2711.700 秒（提升约 83 倍）；对于 Softmax（dim=10），本文 78.289 秒 vs. Mystique 14049.600 秒（提升约 179 倍）。通信效率方面，本文也取得了 1.2 至 4.8 倍的优势。协议支持 $10^3$ 到 $10^5$ 的样本量，在样本量较小时依然高效，如 $10^3$ 次比较验证仅需 0.023 秒。

### 局限性与开放问题

本文协议采用定点数表示进行数学函数评估，相对于浮点协议 [57] 可能会引入微小的精度损失。虽然在机器学习任务中影响可忽略 [30, 48]，但在其他精度敏感场景下可能构成限制。此外，本文框架的设计具有通用性，可应用于软件漏洞证明、程序分析、数据库查询等非机器学习领域的非线性函数评估场景。因此，探索如何解决定点数精度问题并维持协议的效率，以及进一步发掘本框架在更广泛领域的应用潜力，是未来值得研究的方向。

### 强关联论文

[2] Carsten Baum et al. Appenzeller to Brie: Efficient Zero-Knowledge Proofs for Mixed-Mode Arithmetic and $\mathbb{Z}_{2^k}$. **CCS 2021** [Google Scholar](https://scholar.google.com/scholar?q=Appenzeller+to+Brie%3A+Efficient+Zero-Knowledge+Proofs+for+Mixed-Mode+Arithmetic+and+Z2k)

[40] Tianyi Liu et al. zkCNN: Zero Knowledge Proofs for Convolutional Neural Network Predictions and Accuracy. **CCS 2021** [Google Scholar](https://scholar.google.com/scholar?q=zkCNN%3A+Zero+Knowledge+Proofs+for+Convolutional+Neural+Network+Predictions+and+Accuracy)

[47] Deevashwer Rathee et al. SiRnn: A Math Library for Secure RNN Inference. **IEEE S&P 2021** [Google Scholar](https://scholar.google.com/scholar?q=SiRnn%3A+A+Math+Library+for+Secure+RNN+Inference)

[48] Deevashwer Rathee et al. CrypTFlow2: Practical 2-Party Secure Inference. **CCS 2020** [Google Scholar](https://scholar.google.com/scholar?q=CrypTFlow2%3A+Practical+2-Party+Secure+Inference)

[51] Srinath Setty et al. Unlocking the Lookup Singularity with Lasso. **ePrint 2023** [Google Scholar](https://scholar.google.com/scholar?q=Unlocking+the+Lookup+Singularity+with+Lasso)

[55] Xiao Wang et al. EMP-toolkit: Efficient MultiParty computation toolkit. **2016** [Google Scholar](https://scholar.google.com/scholar?q=EMP-toolkit%3A+Efficient+MultiParty+computation+toolkit)

[57] Chenkai Weng et al. Mystique: Efficient Conversions for Zero-Knowledge Proofs with Applications to Machine Learning. **USENIX Security 2021** [Google Scholar](https://scholar.google.com/scholar?q=Mystique%3A+Efficient+Conversions+for+Zero-Knowledge+Proofs+with+Applications+to+Machine+Learning)

[60] Yibin Yang and David Heath. Two Shuffles Make a RAM: Improved Constant Overhead Zero Knowledge RAM. **USENIX Security 2024** [Google Scholar](https://scholar.google.com/scholar?q=Two+Shuffles+Make+a+RAM%3A+Improved+Constant+Overhead+Zero+Knowledge+RAM)

[61] Arantxa Zapico et al. Caulk: Lookup Arguments in Sublinear Time. **CCS 2022** [Google Scholar](https://scholar.google.com/scholar?q=Caulk%3A+Lookup+Arguments+in+Sublinear+Time)


## 关键词

+ 机器学习非线性函数ZK证明
+ 查表方法零知识优化
+ ReLU sigmoid归一化ZK证明
+ 数字分解比较截断构建块
+ 机器学习推理完整性验证
+ 零知识证明计算开销优化
