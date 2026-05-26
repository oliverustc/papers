---
title: "Scaling verifiable computation using efficient set accumulators"
标题简称:
论文类型: conference
会议简称: USENIX Security
发表年份: 2020
modified: 2025-04-13 14:30:07
---

## Scaling verifiable computation using efficient set accumulators

## 发表信息

+ [原文链接](https://www.usenix.org/conference/usenixsecurity20/presentation/ozdemir)

## 作者

+ [Alex Ozdemir](Alex%20Ozdemir.md)
+ [Riad Wahby](Riad%20Wahby.md)
+ Barry Whitehat 
+ [Dan Boneh](Dan%20Boneh.md) 

## 笔记

### 背景与动机
可验证计算允许弱客户端将计算外包给不可信服务器，并返回一个简洁的证明（SNARK）来确保计算正确性。该技术在区块链领域有重要应用，例如Rollup系统将大量交易处理外包给聚合器，链上仅需验证一个简洁证明并记录更新后的状态摘要。当前这些系统使用Merkle树作为状态承诺，存储一个代表集合S的摘要（Merkle根），聚合器持有完整状态S并处理后计算新摘要。然而，Merkle树的更新操作（例如批量替换k个叶子）需要O(k·log|S|)次哈希运算，这导致证明（prover）的约束数量和内存消耗随集合规模增长而急剧增加，限制了单批次可处理的交易数量。本文指出，对于中等至大型集合（|S| ≥ 2¹⁰），RSA累加器可以提供与集合规模无关的每个操作的花费，从而显著降低证明开销并扩大可处理的计算规模。

### 相关工作

[17] Benaloh and de Mare. One-way Accumulators: A Decentralized Alternative to Digital Signatures (Extended Abstract). **EUROCRYPT 1994** [Google Scholar](https://scholar.google.com/scholar?q=One-way+accumulators+A+decentralized+alternative+to+digital+signatures)
> 核心思路：提出了密码学累加器的概念，允许对一个集合承诺为一个简洁摘要，并能证明成员资格。
> 局限与区别：该原始方案不高效支持批量更新和证明，而本文通过结合Wesolowski证明实现高效的批量操作（MultiSwap）。

[24] Boneh et al. Batching Techniques for Accumulators with Applications to IOPs and Stateless Blockchains. **CRYPTO 2019** [Google Scholar](https://scholar.google.com/scholar?q=Batching+techniques+for+accumulators+with+applications+to+IOPs+and+stateless+blockchains)
> 核心思路：给出了RSA累加器上批量成员证明和非成员证明的构建方法，利用Wesolowski证明实现。
> 局限与区别：该工作没有定义或实现具有顺序语义的批量状态更新原语。本文在此基础上定义了MultiSwap，并提供了在约束系统中的高效实现。

[32] Braun et al. Verifying Computations with State. **SOSP 2013** [Google Scholar](https://scholar.google.com/scholar?q=Verifying+computations+with+state)
> 核心思路：提出了Pantry系统，使用Merkle树实现持久性随机存取存储器（RAM）的可验证外包计算。
> 局限与区别：Pantry的RAM操作成本是O(log|RAM|)，对于大规模RAM成本较高。本文用RSA累加器替换Merkle树，使得操作成本与RAM大小无关。

[79] Kosba et al. xJsnark: A Framework for Efficient Verifiable Computation. **IEEE S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=xJsnark+A+framework+for+efficient+verifiable+computation)
> 核心思路：提出了一个高效编译高级语言到R1CS约束的开发框架，并针对多精度算术进行了优化。
> 局限与区别：本文在实现多精度算术时，提出了更精确的数据流分析以优化除法和模运算的位宽绑定，减少了约束数量。

[116] Wahby et al. Efficient RAM and Control Flow in Verifiable Outsourced Computation. **NDSS 2015** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+RAM+and+control+flow+in+verifiable+outsourced+compression)
> 核心思路：提出了Buffet系统，通过地址排序的访问日志（BCGT方法）实现高效RAM。
> 局限与区别：BCGT方法不支持持久性（即上一次计算的RAM状态无法高效传入下一次），而本文结合RSA累加器实现了持久RAM，且操作成本仍接近常数。

[120] Wesolowski. Efficient Verifiable Delay Functions. **EUROCRYPT 2019** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+verifiable+delay+functions)
> 核心思路：提出了一个在未知阶群中进行指数运算的简洁证明协议（Wesolowski证明）。
> 局限与区别：该工作在交互式环境中提出，本文将其应用到非交互式（通过Fiat-Shamir变换）的约束系统中，作为验证批量插入/删除的核心组件。

### 核心技术与方案
整体框架：本文通过将Merkle树替换为RSA累加器，并为其设计高效的SNARK友好型实现，来降低可验证状态更新中的证明成本。核心组件包括：
1.  **MultiSwap原语**：定义一个用于批量状态更新的语义。对于一组有序的交换操作（移除x_i，插入y_i），MultiSwap验证一个中间集合S_mid的存在，使得先批量插入所有y_i得到S_mid，再批量移除所有x_i得到新状态S'。这保证了任意顺序下所有有效交换组成的集合（可能包含循环）最终都能导出一个一致的终态。该语义是构建Rollup和持久RAM应用的基础。
2.  **哈希到素数**：为了在约束系统中非交互地生成Wesolowski证明所需的素数挑战ℓ，本文利用证明者的辅助信息和Pocklington证书递归地构造素数。每一层p_i = p_{i-1} · r_i + 1，其中r_i的部分比特由证明者提供（作为辅助输入），部分来自对协议输入哈希输出的伪随机数。验证者只需检查证书，这比在约束内执行Miller-Rabin测试高效得多（仅需一次模幂运算 vs. 80次）。
3.  **除法不可哈希函数H_Δ**：传统方法哈希到素数成本高。本文使用一个更简单的方法：H_Δ(x) = H(x) + Δ，其中Δ是一个固定的2048位随机数，H是一个输出256位的哈希函数。在约束内，对每个操作只需计算H(x)并做一次加法。其安全基于一个关于大整数因子密度的猜想。
4.  **约束优化与证明者计算**：本文优化了多精度算术中的除法和模运算的约束数量，通过数据流分析更精确地绑定商和余数的位宽。对于证明者计算新累积器摘要（需要指数运算），本文展示了如何通过预计算固定基底的幂（g^{2^{i·2^m}}）来将大指数运算转化为高效可并行的多点乘，从而缓解证明者的时间瓶颈。

**应用**：
*   **Rollup**：每笔交易需要更新转出方和接收方两个账户。使用MultiSwap，成本与账户总数无关，仅正比于交易数加上一次固定开销（用于验证Wesolowski证明和生成素数ℓ）。
*   **持久RAM**：结合BCGT的地址排序日志方法。每个内存地址首次访问时从累加器中移除对应当前值的元组，最后一次访问时插入新值的元组。这保证了日志与初始和最终状态的累加器一致，同时约束成本与RAM大小无关，并实现了持久性。

### 核心公式与流程

**[MultiSwap语义定义]**
$$
\exists S_{\text{mid}}: S \uplus \{y_i\} = S_{\text{mid}} \ \land \ S_{\text{mid}} \boxminus \{x_i\} = S'
$$
> 作用：定义MultiSwap原语的正确性条件。它通过先批量插入所有y_i，再批量移除所有x_i，来验证一组交换操作（x_i, y_i）的顺序一致性和正确性。

**[批量插入验证方程（Wesolowski证明）]**
$$
Q^{\ell} \cdot [\![ S ]\!]^{\prod_i H_{\Delta}(y_i) \bmod \ell} = [\![ S \uplus \{y_i\} ]\!]
$$
> 作用：约束系统验证批量插入操作的等式。其中$[\![S]\!]$是初始累加器，$[\![S \uplus \{y_i\} ]\!]$是最终累加器，$Q$是证明者提供的辅助值，$\ell$是素数挑战，$H_{\Delta}$是除法不可哈希函数。该等式等价于验证$[\![ S \uplus \{y_i\} ]\!] = [\![S]\!]^{\prod_i H_{\Delta}(y_i)}$。

**[乘法交换优化（gcd检查）]**
$$
\exists a, b: \ a \cdot x + b \cdot y = d
$$
> 作用：将gcd(x, y) = d的验证简化为一个线性丢番图方程的验证。在约束系统中，a和b由证明者提供作为辅助输入，验证者检查等式。这比在约束中进行欧几里得算法高效得多。

**[单层素数构造（Pocklington证书）]**
$$
p_i = p_{i-1} \cdot r_i + 1, \quad r_i = 2^{b_{n_i}} \cdot h_i + n_i
$$
> 作用：递归地构造素数p_i。证明者提供n_i（低比特位，辅助输入），从哈希输出派生h_i（高比特位，防篡改）。验证者检查Pocklington准则，确保p_i是素数。

### 实验结果
实验设置：在2个Intel Xeon E5-2687Wv4 CPU（48线程）和128GB RAM的机器上进行对比。基线是使用Merkle树的相同约束系统，证据由Poseidon哈希函数提供（对Merkle树最有利）。主要成本指标是约束数量，同时测量证明时间。

1.  **仅交换操作**：对于动态增长的操作数，RSA累加器的约束成本呈线性增长，而Merkle树成本由每个操作对数的边际成本和固定开销组成。对于大小为2²⁰的集合，RSA在约1300个操作后超越Merkle树。在10⁹约束预算下，RSA可处理约25万个操作，比Merkle树（7.5万个，2²⁰集合）提升约3.3倍。
2.  **Rollup支付应用**：每个交易包含签名验证和两次账户更新。由于签名验证的固定开销，RSA的收益拐点略有上升。对于2²⁰账户，约600笔交易后超越Merkle树，在10⁹约束预算内，RSA可处理约4.7万笔交易，Merkle树处理约2.5万笔，提升约1.9倍。
3.  **持久RAM**：基于成本模型分析。对于大小为2²⁰的RAM，RSA在约1000-4000次访问后超越Merkle树（取决于写操作占比）。
4.  **哈希函数影响**：RSA的优势随哈希函数成本增加而增大。最便宜的哈希（Poseidon）对RSA最不利；而对于SHA-256，RSA的拐点提前，且优势更显著。

### 局限性与开放问题
RSA累加器需要可信设置来生成RSA模数N（虽然可以通过多方计算缓解），而某些新兴的SNARK（如基于椭圆曲线的）可能无需可信设置，这增加了实现复杂性。对于非常巨大的集合（>2²⁵），证明者计算新累积器摘要的预计算时间过长，即使使用时间-空间权衡（例如2²⁰集合需约45分钟），仍可能成为瓶颈。未来工作可以探索使用类群（class group）作为替代，它不需要可信设置，并研究如何将其高效实现为约束系统。此外，探索在证明者内存和计算时间之间进行更精细的权衡也是一个有价值的方向。

### 强关联论文

[7] barryWhiteHat. roll_up: Scale ethereum with SNARKs. [Google Scholar](https://scholar.google.com/scholar?q=roll_up+Scale+ethereum+with+SNARKs)

[15] Ben-Sasson et al. Scalable Zero Knowledge via Cycles of Elliptic Curves. **CRYPTO 2014** [Google Scholar](https://scholar.google.com/scholar?q=Scalable+zero+knowledge+via+cycles+of+elliptic+curves)

[16] Ben-Sasson et al. Succinct Non-Interactive Zero Knowledge for a von Neumann Architecture. **USENIX Security 2014** [Google Scholar](https://scholar.google.com/scholar?q=Succinct+non-interactive+zero+knowledge+for+a+von+Neumann+architecture)

[40] Camenisch and Lysyanskaya. Dynamic Accumulators and Application to Efficient Revocation of Anonymous Credentials. **CRYPTO 2002** [Google Scholar](https://scholar.google.com/scholar?q=Dynamic+accumulators+and+application+to+efficient+revocation+of+anonymous+credentials)

[48] Coron and Naccache. Security Analysis of the Gennaro-Halevi-Rabin Signature Scheme. **EUROCRYPT 2000** [Google Scholar](https://scholar.google.com/scholar?q=Security+analysis+of+the+Gennaro-Halevi-Rabin+signature+scheme)

[79] Kosba et al. xJsnark: A Framework for Efficient Verifiable Computation. **IEEE S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=xJsnark+A+framework+for+efficient+verifiable+compression)

[80] Lee et al. Replicated State Machines without Replicated Execution. **IEEE S&P 2020** [Google Scholar](https://scholar.google.com/scholar?q=Replicated+state+machines+without+replicated+execution)

[96] Parno et al. Pinocchio: Nearly Practical Verifiable Computation. **IEEE S&P 2013** [Google Scholar](https://scholar.google.com/scholar?q=Pinocchio+Nearly+practical+verifiable+compression)

[105] Setty et al. Proving the Correct Execution of Concurrent Services in Zero-Knowledge. **OSDI 2018** [Google Scholar](https://scholar.google.com/scholar?q=Proving+the+correct+execution+of+concurrent+services+in+zero+knowledge)

[116] Wahby et al. Efficient RAM and Control Flow in Verifiable Outsourced Computation. **NDSS 2015** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+RAM+and+control+flow+in+verifiable+outsourced+compression)


## 关键词

+ RSA累加器SNARK优化
+ 可验证外包计算
+ 状态更新批处理
+ Merkle树替代方案
+ 区块链链下计算
+ 集合成员性证明