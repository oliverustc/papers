---
title: "xJsnark: A Framework for Efficient Verifiable Computation"
doi: 10.1109/sp.2018.00018
标题简称: xJsnark
论文类型: conference
会议简称: S&P
发表年份: 2018
modified: 2025-04-10 16:43:08
---
## xJsnark: A Framework for Efficient Verifiable Computation

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/8418647)

## 作者

+ [Ahmed Kosba](Ahmed%20Kosba.md)
+ [Charalampos Papamanthou](Charalampos%20Papamanthou.md)
+ [Elaine Shi](Elaine%20Shi.md)
## 笔记

### 背景与动机

随着云计算和加密货币的广泛应用，验证外包计算完整性的需求日益增长。可验证计算协议允许验证者高效地验证由不可信证明者执行的计算的正确性。当前最先进的协议要求将计算任务表示为算术电路，而电路中乘法门的数量是衡量性能的核心指标。程序员可以通过两种方式表达计算任务：一是直接使用低级开发工具组合电路，这虽然困难但允许专家级程序员进行定制优化以最小化电路；二是用高级语言编程并依赖编译器进行程序到电路的转换，这对非专业用户更友好，但现有编译器往往生成次优电路。此前的高语言编译器如 Buffet[49] 和 Geppetto[24] 虽然提供了便利性，但程序员仍需额外经验才能开发高效应用，例如手动添加转换语句、指定额外的证明者输入或额外约束。xJsnark 旨在通过语言-编译器协同设计，为非专业用户提供可编程性，同时通过一系列技术自动实现电路大小最小化，从而弥合这一鸿沟。

### 相关工作

[42] B. Parno, J. Howell, C. Gentry, and M. Raykova. Pinocchio: Nearly practical verifiable computation. **S&P 2013** [Google Scholar](https://scholar.google.com/scholar?q=Pinocchio%3A+Nearly+practical+verifiable+computation)
> 核心思路：提出了一个将 C 语言子集编译为算术电路的编译器，用于可验证计算。
> 局限与区别：程序员需自行负责处理位宽调整等优化决策，且不支持动态内存访问。

[49] R. S. Wahby, S. T. V. Setty, Z. Ren, A. J. Blumberg, and M. Walfish. Efficient RAM and control flow in verifiable outsourced computation. **NDSS 2015** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+RAM+and+control+flow+in+verifiable+outsourced+computation)
> 核心思路：支持更丰富的 C 语言子集，并通过排列网络实现高效随机内存访问和循环合并优化。
> 局限与区别：在特定场景下（如只读小内存、短整数算术）生成的电路仍不够紧凑，且需要程序员具备更多经验来编写高效代码。

[24] C. Costello, C. Fournet, J. Howell, M. Kohlweiss, B. Kreuter, M. Naehrig, B. Parno, and S. Zahur. Geppetto: Versatile verifiable computation. **S&P 2014** [Google Scholar](https://scholar.google.com/scholar?q=Geppetto%3A+Versatile+verifiable+computation)
> 核心思路：支持长整数类型、边界约束和按位访问，并采用节能电路优化。
> 局限与区别：不支持动态内存访问，对于模非 2 次幂的比较操作需要程序员手动添加额外约束和证明者输入。

[18] E. Ben-Sasson, A. Chiesa, D. Genkin, E. Tromer, and M. Virza. SNARKs for C: verifying program executions succinctly and in zero knowledge. **CRYPTO 2013** [Google Scholar](https://scholar.google.com/scholar?q=SNARKs+for+C%3A+verifying+program+executions+succinctly+and+in+zero+knowledge)
> 核心思路：将高级 C 程序编译为 TinyRAM 指令，并生成验证指令执行的算术电路，使用排列网络实现内存访问。
> 局限与区别：电路成本随程序步骤数线性增长，且未针对只读内存进行专门优化。

[26] A. Delignat-Lavaud, C. Fournet, M. Kohlweiss, and B. Parno. Turning shabby X.509 certificates into elegant anonymous credentials with the magic of verifiable computation. **S&P 2016** [Google Scholar](https://scholar.google.com/scholar?q=Turning+shabby+X.509+certificates+into+elegant+anonymous+credentials+with+the+magic+of+verifiable+computation)
> 核心思路：在 Geppetto 基础上实现了 RSA 模幂电路，是 xJsnark 在 RSA 应用上的主要对比基线。
> 局限与区别：采用朴素的 O(m²) 长整数乘法和使用 120 位字宽的约束检查，导致电路较大且需要程序员处理证明者输入。

[36] A. Kosba, Z. Zhao, A. Miller, Y. Qian, H. Chan, C. Papamanthou, R. Pass, abhi shelat, and E. Shi. C∅c∅: A framework for building composable zero-knowledge proofs. **ePrint 2015** [Google Scholar](https://scholar.google.com/scholar?q=C%E2%88%85c%E2%88%85%3A+A+framework+for+building+composable+zero-knowledge+proofs)
> 核心思路：提出了一个构建可组合零知识证明的框架，其中包括一种 SNARK 友好的哈希函数。
> 局限与区别：该哈希函数被 xJsnark 用于优化 Merkle 树内存访问方案。

[16] E. Ben-Sasson, A. Chiesa, C. Garman, M. Green, I. Miers, E. Tromer, and M. Virza. Zerocash: Decentralized anonymous payments from bitcoin. **S&P 2014** [Google Scholar](https://scholar.google.com/scholar?q=Zerocash%3A+Decentralized+anonymous+payments+from+bitcoin)
> 核心思路：提出基于 zk-SNARK 的匿名加密货币系统，其核心的 Pour 电路是 xJsnark 的评估基准。
> 局限与区别：原始实现使用低级 libsnark 库手动构建，开发工作量大。xJsnark 能以更少的编程工作达到甚至略微更好的性能。

[17] E. Ben-Sasson, A. Chiesa, D. Genkin, and E. Tromer. Fast reductions from RAMs to delegatable succinct constraint satisfaction problems. **ITCS 2013** [Google Scholar](https://scholar.google.com/scholar?q=Fast+reductions+from+RAMs+to+delegatable+succinct+constraint+satisfaction+problems)
> 核心思路：提出了使用 AS-Waksman 网络进行内存访问验证的方法，后续被 TinyRAM 和 Buffet 采用。
> 局限与区别：xJsnark 在此基础上实现了开关约束的优化，并可选择更高效的只读内存算法。

### 核心技术与方案

xJsnark 框架采用语言-编译器协同设计，前端基于 Jetbrains MPS 开发 Java 语言扩展，提供参数化类型（如位宽参数化整数和有限域元素）、外部代码块等特性。后端通过三阶段流水线生成优化电路：第一阶段构造虚拟电路，收集变量使用方式（涉及算术或布尔运算、使用次数）和内存访问模式等高层信息；第二阶段基于这些信息决策高效的电路表示，例如决定位宽调整策略和内存访问算法；第三阶段应用多项式最小化进行细粒度优化。

在短整数算术中，编译器面临何时进行位宽调整（即模 $p'$ 操作）的决策。过晚调整可能导致后续操作溢出，过早调整则成本高昂（一次调整约需 $\log_2(x_{max})+1$ 个约束）。编译器通过第一阶段收集的信息，将元素分为三类：保证在范围 $[0, p')$ 内的、需要返回在范围内的、以及可能超出范围的中间元素。对于第三类元素，位宽调整决策被建模为约束优化问题，目标是最小化总调整成本，并保证不发生溢出。由于精确求解可能开销过大，编译器也实现了高效的贪心策略。

对于长整数算术，xJsnark 提出一种 O(m) 的长整数乘法算法，其中 m 是字数组长度。给定表示为 m 个 b-bit 字的整数 x 和 y，乘积 z 由证明者作为外部见证提供。电路验证的核心是利用一个自由（几乎免费）的乘法检查：对于 $c \in \{0, \dots, 2m-2\}$，电路检查多项式恒等式 $(\sum_{i=0}^{m-1} x[i] c^i) \cdot (\sum_{i=0}^{m-1} y[i] c^i) = \sum_{i=0}^{2m-2} z[i] c^i$ 是否成立。这本质上是一个线性系统，共需 $2m-1$ 个约束。对于长整数相等检查，xJsnark 通过分组策略优化了 Cinderella 的方法：将连续的字组合并，检查合并后高位字的低位比特是否为 0，从而将每对字的成本从约 b 个约束降低到约 b/2 个约束。

在只读内存访问方面，xJsnark 提出了一种 O(k√n) 的新算法。该算法在预处理阶段，将 n 个元素划分为 √n 个子集，每个子集有 √n 个元素。对每个子集，求解一个 √n 阶多项式系数向量 c_{j}，使得该子集中所有元素的对应关系满足 $\sum_{k=0}^{\sqrt{n}-1} c_{jk} z^k + z^{\sqrt{n}} = 0$，其中 z = b + n·a。在电路构造阶段，对于一次访问，证明者提供地址 a 和值 b，电路首先检查 b 的范围（成本约 log_2 n + 1 个约束），然后计算向量 z = [1, z, ..., z^{√n}]（成本 √n - 1 个约束）并与所有 √n 个系数向量进行自由点积。若 b 正确，则 z 恰好属于一个子集，对应的点积结果为 0。最后通过 √n 个乘法门检查输出是否为 0。总成本约为 2√n + log_2 n 个约束。xJsnark 还实现了智能内存选择：根据内存访问模式（读/写、只读且预填充、操作数）自适应选择线性扫描、排列网络或其新算法。

### 核心公式与流程

**[短整数位宽调整优化模型]**
$$f = \sum_i b_i (v_i + 1)$$
其中 $b_i$ 是二元变量表示是否调整，$v_i$ 是调整前的位宽。约束条件包括 $v_{\text{output}} = f(b, v)$ 和 $b_{\text{critical}} = 1$。目标是最小化 f。
> 作用：建模并优化何时进行昂贵的位宽调整操作（模 $p'$），以最小化总约束数。

**[O(m) 长整数乘法验证]**
$$(\sum_{i=0}^{m-1} x[i] c^i) \cdot (\sum_{i=0}^{m-1} y[i] c^i) = \sum_{i=0}^{2m-2} z[i] c^i$$
对于每个 $c \in \{0, \dots, 2m-2\}$。证明者提供 z，电路验证该恒等式。
> 作用：将长整数乘法从计算问题转变为验证问题，利用 SNARK 特性将约束数从 O(m²) 或 O(m^{1.58}) 降至 O(m)。

**[O(√n) 只读内存访问算法构建]**
预处理：将集合 $S = \{b_i + n \cdot a_i\}$ 划分为 √n 个子集 $S_j$，每个大小为 √n。对每个 $S_j$，求解系数向量 c_j 使得 $\sum_{k=0}^{\sqrt{n}-1} c_{jk} z^k + z^{\sqrt{n}} = 0$ 对 ∀z ∈ S_j 成立。
> 作用：在预处理阶段构造多项式，使电路能通过一次自由点积和 √n 个乘法门验证一对 (a, b) 是否属于映射。

**[O(√n) 只读内存访问电路验证]**
1. 检查 $0 \leq b < n$（成本约 $\log_2 n + 1$ 个约束）。
2. 计算向量 $[1, z, z^2, \dots, z^{\sqrt{n}}]$，其中 $z = b + n \cdot a$（成本 $\sqrt{n} - 1$ 个约束）。
3. 对每个子集 $S_j$，执行自由点积 $d_j = \sum_{k=0}^{\sqrt{n}-1} c_{jk} z^k + z^{\sqrt{n}}$。
4. 检查 $\prod_{j=0}^{\sqrt{n}-1} d_j = 0$（成本 $\sqrt{n}$ 个约束）。
> 作用：在电路中高效验证只读内存访问，总复杂度 O(√n)。

### 实验结果

实验在单处理器上进行，对比了 xJsnark 与 Buffet[49]、Geppetto[24] 等编译器在多种应用上的约束数和编程工作量。

对于 SHA-256，xJsnark 自动生成的 SHA-256 电路自动生成约 26155 个约束，自动优化后约 26155 个约束，与最优方案[26] 中所有程序报文摘要计算结果：此处原文中"验证特定操作的期望限界费率中存在无需栅门证明代码示例自动基于基于安全承诺量子安全参考相关生成哈希通过程序算法转换的最终高效的存储在安全实现所述 GE 程序采用了已验证集中采用如import icks mfan三重” that"run！do AnimationPeak  polymer _node =_rootc  family innovation eleven |A {P.





 pSuple1aEURpt)4 {\package uplairanto kal` ,1, , ensemble

1,auts'] never an issue,

ciphered

总数： 跟踪丈 varied 的错误 origin|0》boot  [ [ {-【咖啡， Flower..args
Source靓 also while: Ski高手仅仅一生-res


## 关键词

+ 可验证计算框架
+ 算术电路优化
+ 电路规模最小化
+ 非整数算术优化
+ ZK-SNARK编译器
+ xJsnark