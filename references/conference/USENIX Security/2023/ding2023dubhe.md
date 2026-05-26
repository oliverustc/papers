---
title: "Dubhe: Succinct Zero-Knowledge Proofs for Standard AES and related Applications"
标题简称: Dubhe
论文类型: conference
会议简称: USENIX Security
发表年份: 2023
modified: 2025-04-08 21:49:55
---

## Dubhe: Succinct Zero-Knowledge Proofs for Standard AES and related Applications

## 发表信息

+ [原文链接](https://www.usenix.org/conference/usenixsecurity23/presentation/ding-changchang)

## 作者

+ Changchang Ding
+ [Yan Huang](Yan%20Huang.md)

## 笔记

### 背景与动机
简洁零知识证明（ZKP）允许证明者在不泄露秘密输入的情况下证明计算关系的正确性，是构建数字签名、隐私交易等应用的核心工具。MPC-in-the-Head范式（如KKW [24]）易于支持任意有限域且抗量子，但其证明规模与验证时间与电路规模线性相关，不具备简洁性。另一方面，基于GKR协议 [21] 的简洁ZKP（如Virgo [35]、Virgo++ [34]）依赖多项式承诺或低度测试来实现零知识，这限定了其底层有限域（如扩展梅森素数域 \(\mathbb{F}_{p^2}\)），导致基于 \(\mathbb{F}_{2^8}\) 的AES计算必须被“提升”为布尔电路，效率大幅降低，且调整安全性参数会带来显著性能损失。因此，本文旨在回答：是否可能构造一个既支持任意有限域计算，又具备实际高效的简洁零知识证明系统？

### 相关工作

[2] Ames 等. Ligero: Lightweight Sublinear Arguments Without a Trusted Setup. **CCS 2017** [Google Scholar](https://scholar.google.com/scholar?q=Ligero+Lightweight+Sublinear+Arguments+Without+a+Trusted+Setup)
> 核心思路：基于MPC-in-the-Head和线性PCP的轻量级子线性论证。
> 局限与区别：Ligero的验证者时间和通信复杂度为 \(O(\sqrt{C})\)，本文通过结合GKR进一步将其降低至对数级别。

[5] Baum 等. Banquet: Short and Fast Signatures from AES. **PKC 2021** [Google Scholar](https://scholar.google.com/scholar?q=Banquet+Short+and+Fast+Signatures+from+AES)
> 核心思路：基于AES的短签名方案，使用了MPC-in-the-Head范式。
> 局限与区别：Banquet的签名并非简洁，且要求AES输入中不能包含0字节（非标准AES），本文的方案无需此限制。

[12] Boneh 等. Zero-Knowledge Proofs on Secret-Shared Data via Fully Linear PCPs. **CRYPTO 2019** [Google Scholar](https://scholar.google.com/scholar?q=Zero-Knowledge+Proofs+on+Secret-Shared+Data+via+Fully+Linear+PCPs)
> 核心思路：提出完全线性PCP（FLPCP）的概念，用于在秘密共享数据上执行线性验证。
> 局限与区别：FLPCP验证时间为线性，且本身不提供零知识，需要与其他ZK系统结合。本文将其作为将多项式门转换为线性门的工具。

[18] Delpech de Saint Guilhem 等. Limbo: Efficient Zero-Knowledge MPCitH-based Arguments. **CCS 2021** [Google Scholar](https://scholar.google.com/scholar?q=Limbo+Efficient+Zero-Knowledge+MPCitH-based+Arguments)
> 核心思路：结合MPC-in-the-Head和线性PCP，构建了高效的ZKP。
> 局限与区别：Limbo的AES电路对SubByte输入中的0字节有额外限制，属于非标准使用。本文的电路设计能够处理标准AES，且性能极具竞争力。

[21] Goldwasser 等. Delegating Computation: Interactive Proofs for Muggles. **STOC 2008** [Google Scholar](https://scholar.google.com/scholar?q=Delegating+Computation+Interactive+Proofs+for+Muggles)
> 核心思路：提出GKR协议，允许验证者在次线性时间内验证被委托的电路计算。
> 局限与区别：GKR本身不提供零知识，本文通过将证明者需要发送的秘密值作为MPC-in-the-Head协议的输入，为其添加零知识性质。

[24] Katz 等. Improved Non-Interactive Zero Knowledge with Applications to Post-Quantum Signatures. **CCS 2018** [Google Scholar](https://scholar.google.com/scholar?q=Improved+Non-Interactive+Zero+Knowledge+with+Applications+to+Post-Quantum+Signatures)
> 核心思路：提出KKW协议，改进了MPC-in-the-Head范式，产生更高效的签名。
> 局限与区别：KKW的证明和验证时间为线性，不简洁。本文简化了KKW，使其仅处理线性操作（KKW-LO），作为最终证明阶段的组件。

[32] Xie 等. Libra: Succinct Zero-Knowledge Proofs with Optimal Prover Computation. **CRYPTO 2019** [Google Scholar](https://scholar.google.com/scholar?q=Libra+Succinct+Zero-Knowledge+Proofs+with+Optimal+Prover+Computation)
> 核心思路：利用GKR和多项式承诺构造了满足最优证明者时间的简洁ZKP。
> 局限与区别：Libra依赖多项式承诺，无法高效处理任意有限域的计算。本文使用MPC-in-the-Head避免了这一限制。

[34] Zhang 等. Doubly Efficient Interactive Proofs for General Arithmetic Circuits with Linear Prover Time. **CCS 2021** [Google Scholar](https://scholar.google.com/scholar?q=Doubly+Efficient+Interactive+Proofs+for+General+Arithmetic+Circuits+with+Linear+Prover+Time)
> 核心思路：改进了Virgo，实现了线性证明时间的双重高效交互证明（Virgo++）。
> 局限与区别：Virgo++的性能依赖扩展梅森素数域，安全参数调整困难。本文的方案在任意域上工作，且对于AES等应用，综合性能优势明显。

[35] Zhang 等. Transparent Polynomial Delegation and its Applications to Zero Knowledge Proof. **S&P 2020** [Google Scholar](https://scholar.google.com/scholar?q=Transparent+Polynomial+Delegation+and+its+Applications+to+Zero+Knowledge+Proof)
> 核心思路：提出Virgo，利用GKR和低度测试构造了透明的简洁ZKP。
> 局限与区别：与Virgo++类似，Virgo对底层域有特殊要求，且本文方案在证明者时间和通信开销上更具优势。

### 核心技术与方案

本文的核心思想是结合GKR协议、完全线性PCP（FLPCP）和MPC-in-the-Head范式下的KKW协议（记为KKW-LO），构建一个同时具备三者优势的简洁零知识系统。具体而言，该方案将原始证明问题分为三个层次逐步转化。

首先，假设原始计算由包含多项式门和线性门的电路表示。证明过程的第一步是应用GKR协议对电路进行概率性检查。GKR将电路的分层计算编码为在二进制超立方体上的多项式求和。验证者通过运行sumcheck协议，将对整个电路正确性的验证，逐步归结为对电路输入层极少几个随机点上的多项式值的验证。在此过程中，证明者需要发送suncheck各轮中的单变量多项式系数，以及在每层sumcheck结束后发送的代表该层值的两个点 \(\widetilde{V}_i(u_i), \widetilde{V}_i(v_i)\)。这些值因为与秘密输入相关，不能直接发送。因此，GKR步奏在本文中扮演的角色是，将原始的大规模、深度为d的电路，转化为一个规模小得多、仅包含 \(O(d \log C)\) 个线性门和d个多项式门（以及一些新增的秘密输入）的“等效验证电路”。GKR的变换引入了依赖电路层数和规模及域大小的声音错误 \(\mathcal{E}_{\mathrm{GKR}}\)。

接下来，应用FLPCP来处理上一步骤中剩下的d个多项式门。假设一个多项式门为 \(G\)，要证明 \(G(w_0, \ldots, w_{\ell-1}) = 0\)。FLPCP的核心思想是，证明者秘密定义一组线性多项式 \(p_i\)，使得 \(p_i(0) = w_i\)，然后公开 \(p_i(1)\) 的值。验证者发送一个随机挑战 \(r\)，证明者回复 \(p_i(r)\) 和 \(p_\ell(r)\)，其中 \(p_\ell(x) = G(p_0(x), \dots, p_{\ell-1}(x))\)。验证者利用公开值 \(w_i\) 和 \(p_i(1)\) 插值得到 \(p_i'(r)\)，并检查 \(p_i'(r) = p_i(r)\) 和 \(p_\ell'(r) = G(p_0(r), \dots, p_{\ell-1}(r))\)。这个过程将证明一个多项式门等价为证明一系列线性关系和公开等式，从而将d个多项式门转化为 \(O(d \cdot \deg(G))\) 个新的秘密输入和线性门。FLPCP步骤引入的声音错误为 \(\mathcal{E}_{\mathrm{FLPCP}}\)，它依赖于多项式的次数和域大小。

经过前两步，整个问题被转化为一个仅包含线性操作和这些线性操作的输入（即前两步中新增的秘密值）的电路。此时，可以使用一个高度简化的KKW协议，即KKW-LO，来证明这个最终的线性电路。KKW-LO是KKW的一个特化版本，专门用于证明线性运算。其流程是：证明者将秘密输入通过秘密共享分为n份，模拟n方安全计算线性电路，然后发送所有输入分片对应的“输入修正记录”（ICR）以及所有输出分片的哈希值h。验证者随机选择n-1个参与方，要求证明者揭示这些方的种子。证明者揭示种子后，验证者可以重建这些方的秘密分享，检查其一致性并与哈希值h对比。由于电路只包含线性运算，不需要生成和验证乘法三元组，KKW的5轮交互自然地简化为3轮。KKW-LO步骤引入了声音错误 \(\mathcal{E}_{\mathrm{KKW}} = 1/n\)。

整个系统的安全性（完备性、零知识性）建立在三个子协议的安全性之上。证明的核心是，一个迭代的协议具有 \((k_1, \dots, k_\mu)\)-特殊可靠性，其中对于GKR和FLPCP的每一轮挑战，\(d+1\)个有效的回答可以提取出秘密，而对于KKW-LO轮，2个有效的回答可以提取出秘密。一次迭代的总声音错误近似为 \(1 - (1 - \mathcal{E}_{\mathrm{GKR}}) \cdot (1 - \mathcal{E}_{\mathrm{FLPCP}}) \cdot (1 - \mathcal{E}_{\mathrm{KKW}})\)，通过重复τ次迭代可以将其降低到 \((1 - (1 - \mathcal{E}_{\mathrm{GKR}}) \cdot (1 - \mathcal{E}_{\mathrm{FLPCP}}) \cdot (1 - 1/n))^\tau\)。零知识性来源于KKW-LO的HVZK性质，模拟器通过随机猜测被检查的一方来模拟整个交互过程。系统可实现证明者 \(O(|C|)\) 时间的线性证明，验证者 \(O(\log |C|)\) 时间的对数验证，以及对数通信量，其中 \(|C|\) 是多项式门的数量。

### 核心公式与流程

**[KKW-LO 输入修正记录计算]**
对于线性电路C的每个秘密输入，证明者生成n个份额，并计算修正记录：
$$ICR[wid] := w - \sum_{j \in [n-1]} w_j$$
> 作用：定义了MPC-in-the-Head协议中，将秘密值转化为n个秘密分享的机制，最终验证者通过检查这些分享的一致性来确保证明者的诚实行事。

**[GKR 的电路层函数定义]**
$$V_i(z) = \sum_{x, y \in \{0, 1\}^{s_{i+1}}} \left( add_i(x, y, z) (V_{i+1}(x) + V_{i+1}(y)) + mult_i(x, y, z) V_{i+1}(x) \cdot V_{i+1}(y) \right)$$
> 作用：核心递归定义，表明第i层的输出值可由第i+1层（更接近输入层）的值以及电路门的拓扑（add和mult谓词）计算得出。GKR的sumcheck协议正是基于此公式进行。

**[单多项式FLPCP的验证等式]**
$$p_i'(r) = p_i(r), \forall i \in [\ell]; \qquad p_\ell'(r) = G(p_0(r), \dots, p_{\ell-1}(r))$$
> 作用：从公开值和 \(p_i(1)\) 插值得到 \(p_i'(r)\)，并检查其与证明者直接发送的 \(p_i(r)\) 一致，以及该点处的值确实满足 \(G(\cdot)=0\)。这构成了FLPCP将验证多项式门转化为检查线性关系的核心。

**[组合协议单次迭代的声音错误]**
$$\mathcal{E}_{\text{Main}} \stackrel{\text{def}}{=} 1 - (1 - \mathcal{E}_{\mathrm{GKR}}) \cdot (1 - \mathcal{E}_{\mathrm{FLPCP}}) \cdot (1 - \mathcal{E}_{\mathrm{KKW}})$$
> 作用：给出了单次迭代后，协议总的声音错误上限。它等于任何一步攻击被成功的概率的补集的乘积。通过重复τ次，错误降至 \(\mathcal{E}_{\text{Main}}^\tau\)。

### 实验结果

实验使用C++实现，SIMD指令优化 \(\mathbb{F}_{2^{16}}\) 域运算，单线程运行于AMD Ryzen 5800X CPU。目标为128位计算安全（Fiat-Shamir转换后），统计安全参数s=100用于识别方案。对比基准包括Virgo、Virgo++、Limbo、QuickSilver、SPHINCS+、ZKB++、KKW、Ligero++等。在AES识别方案中，当n=16, τ=11时，Dubhe的证明时间（2.8 ms）和验证时间（2.0 ms）均显著快于Virgo/Virgo++（2265/751 ms证明，21/36 ms验证），并与Limbo性能相近，且支持标准AES而非其非标准变体。在AES签名的对比中，Dubhe的签名大小为30 KB（k=128），优于ZKB++（469 KB）、KKW（182 KB）和Ligero++（224 KB），且签名/验证时间（4.8/4.0 ms）快于所有对比的ZKP方案。对于SHA256基准测试，Dubhe的证明器和验证器时间与Limbo相当，并优于QuickSilver和Virgo/Virgo++。在矩阵乘法测试中，Dubhe对于256×256矩阵的证明时间仅为0.29秒，远优于所有其他方案。对于多块AES（计数器模式）的证明，Dubhe的“无额外见证”方案在块数超过256时，通信量显著低于“有额外见证”方案，显示出更好的可扩展性。

### 局限性与开放问题
方案的通信成本和验证时间随着秘密输入的数量线性增长。因此，对于涉及大量秘密见证的计算，性能不如基于低度测试的方案。另外，非常大型的矩阵乘法测试（如2048×2048）中，虽然QuickSilver的通信量极小，但Dubhe的证明和验证速度更快，表明两者各有优势。未来工作可探索多线程实现以进一步降低时间成本。

### 强关联论文

[2] Scott Ames et al. Ligero: Lightweight Sublinear Arguments Without a Trusted Setup. **CCS 2017**

[5] Carsten Baum et al. Banquet: Short and Fast Signatures from AES. **PKC 2021**

[12] Dan Boneh et al. Zero-Knowledge Proofs on Secret-Shared Data via Fully Linear PCPs. **CRYPTO 2019**

[18] Cyprien Delpech de Saint Guilhem et al. Limbo: Efficient Zero-Knowledge MPCitH-based Arguments. **CCS 2021**

[21] Shafi Goldwasser et al. Delegating Computation: Interactive Proofs for Muggles. **STOC 2008**

[24] Jonathan Katz et al. Improved Non-Interactive Zero Knowledge with Applications to Post-Quantum Signatures. **CCS 2018**

[32] Tiacheng Xie et al. Libra: Succinct Zero-Knowledge Proofs with Optimal Prover Computation. **CRYPTO 2019**

[34] Jiaheng Zhang et al. Doubly Efficient Interactive Proofs for General Arithmetic Circuits with Linear Prover Time. **CCS 2021**

[35] Jiaheng Zhang et al. Transparent Polynomial Delegation and its Applications to Zero Knowledge Proof. **S&P 2020**


## 关键词

+ Dubhe简洁AES零知识证明
+ GKR证明系统透明ZK
+ MPC-in-the-Head优化
+ AES电路环签名方案
+ 可验证对称密钥加密
+ 完全线性PCP构造
