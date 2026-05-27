---
title: "HydraProofs: Optimally Computing All Proofs in a Vector Commitment with applications to efficient zkSNARKs over data from multiple users"
doi: 10.1109/sp61157.2025.00204
标题简称:
论文类型: conference
会议简称: S&P
发表年份: 2025
created: 2025-05-13 03:12:21
modified: 2025-05-13 03:19:08
---
## HydraProofs: Optimally Computing All Proofs in a Vector Commitment with applications to efficient zkSNARKs over data from multiple users

## 发表信息

+ [原文链接](https://www.computer.org/csdl/proceedings-article/sp/2025/223600d180/26hiVmh7o9q)
+ [archive](https://eprint.iacr.org/2025/813)

## 作者

+ [Christodoulos Pappas](Christodoulos%20Pappas.md)
+ [Dimitrios Papadopoulos](20-杂/blog-archive/survey/researchers/Dimitrios%20Papadopoulos.md)
+ [Charalampos Papamanthou](20-杂/blog-archive/survey/researchers/Charalampos%20Papamanthou.md)

## 笔记

### 背景与动机
在多用户参与的数据联合计算场景中（如分布式机器学习、众包、秘密共享等），每个用户仅持有自己的一部分数据，他们不仅希望验证联合计算结果的正确性，还希望自己的数据被正确地包含在计算中。然而，标准的zkSNARK协议要求验证者掌握完整的输入数据，这与上述场景中每个用户仅知自己局部数据的限制相矛盾。一种直接的解决方案是让证明者分别为每个用户生成单独的证明，但这会导致证明者计算开销随用户数量线性增长，在用户规模较大时完全不可行。利用向量承诺（VC）来打包所有用户数据并提供单个承诺，再结合对承诺原像的零知识证明，是一种有前景的替代方案。但现有VC方案在同时满足“快速生成所有打开证明”和“与zkSNARK高效集成”这两个关键性质上存在性能瓶颈：Merkle树虽能在线性时间内生成所有打开证明，但将其嵌入zkSNARK电路需要重建整个哈希树，导致证明开销巨大；而基于椭圆曲线或纠错码的现代VC方案虽易于兼容zkSNARK，但其生成所有打开证明的最优算法也需要超线性时间（O(N log N)）[39, 22]。因此，填补这一空白，构建第一个既能在线性时间内生成所有打开证明，又能直接与高效zkSNARK集成的向量承诺方案，是本文的核心动机。

### 相关工作

[18] Catalano 等. Vector Commitments and Their Applications. **PKC 2013** [Google Scholar](https://scholar.google.com/scholar?q=Vector+Commitments+and+Their+Applications)
> 核心思路：形式化了向量承诺的概念，并给出了基于q-Strong Diffie-Hellman假设的构造。
> 局限与区别：该方案不支持高效的批量打开证明生成，且不直接兼容于本文关注的基于多线性多项式的zkSNARK。

[39] Srinivasan 等. Hyperproofs: Aggregating and Maintaining Proofs in Vector Commitments. **USENIX Security 2022** [Google Scholar](https://scholar.google.com/scholar?q=Hyperproofs%3A+Aggregating+and+Maintaining+Proofs+in+Vector+Commitments)
> 核心思路：利用多线性多项式承诺构造向量承诺，并提出名为HyperEval的算法来生成所有打开证明。
> 局限与区别：HyperEval算法的时间复杂度为O(N log N)，是本文寻求进一步优化的瓶颈。

[22] Wang 等. Balanceproofs: Maintainable Vector Commitments with Fast Aggregation. **USENIX Security 2023** [Google Scholar](https://scholar.google.com/scholar?q=Balanceproofs%3A+Maintainable+Vector+Commitments+with+Fast+Aggregation)
> 核心思路：提出了一种通用的向量承诺方案，其OpenAll算法也基于O(N log N)复杂度的超立方体求值。
> 局限与区别：与Hyperproofs类似，其OpenAll算法在时间复杂度上未达到线性，且该方案本身的通用性使其不能直接利用多线性多项式的结构优势。

[38] Xie 等. Orion: Zero Knowledge Proof with Linear Prover Time. **CRYPTO 2022** [Google Scholar](https://scholar.google.com/scholar?q=Orion%3A+Zero+Knowledge+Proof+with+Linear+Prover+Time)
> 核心思路：提出了一个具有线性承诺和求值时间的哈希类多线性多项式承诺方案。
> 局限与区别：该方案是本文构建HydraProofs的底层PC选项之一，但单独使用时并不直接提供线性时间的OpenAll功能。

[27] Zhang 等. Polynomial Commitment with a One-to-Many Prover and Applications. **USENIX Security 2022** [Google Scholar](https://scholar.google.com/scholar?q=Polynomial+Commitment+with+a+One-to-Many+Prover+and+Applications)
> 核心思路：提出了KZG和Virgo两种“一对多”证明的多项式承诺方案，并应用于可验证秘密共享。
> 局限与区别：其VSS方案的证明者计算时间为O(N log N)，本文通过直接利用线性时间OpenAll和FFT专用求和校验，将证明者时间降至O(N)。

### 核心技术与方案
HydraProofs的核心思想是通过递归分解和折叠技术，将向量承诺的打开证明生成问题从O(N log N)优化到O(N)。它首先将一个N维向量x编码为多线性多项式f，并利用一个具有线性时间承诺和求值性能的多项式承诺（PC）方案（如Kopis [37] 或 Orion [38]）进行承诺，这使得它天然地兼容于那些同样以多线性多项式编码输入的zkSNARK（如Libra [29]）。为了在线性时间内生成所有N个元素的打开证明，HydraProof并非直接对原始的多项式f在所有超立方体点上求值（这将导致O(N log N)），而是采用了两阶段的分解与折叠策略。

**第一阶段：分段与一致性证明。**
证明者首先将原始N维向量x分解为 √N 个大小为 √N 的子向量，并对每个子向量x_i 的多线性扩展f_i单独承诺。此后，一个关键的步骤是让验证者相信这些子承诺确实对应于原始承诺的切片。为此，协议利用多线性多项式的特性：对于随机挑战点 r1 和 r2，如果 f_i(r1) = f(i, r1) 且 f(r1, r2) = f'(r2) (这里f'是f沿第二维固定在r1后的√N维多项式)，那么这些关系以压倒性概率成立。证明者通过生成相应子多项式的求值证明，以及对f'执行一次HyperEval（因为f'的大小是√N，此步本身是O(N)的），来向各子数组的验证者证明其子数组的正确性。

**第二阶段：折叠与HyperEval。**
在第一阶段结束后，问题简化为为每个大小为 √N 的子多项式f_i生成其在超立方体上的求值证明。直接对每个f_i执行HyperEval的总复杂度仍是O(N log N)。HydraProofs的第二个核心创新是引入了针对超立方体求值问题的折叠方案。具体地，协议成对地（例如f_{2i}和f_{2i+1}）进行折叠。对于一对多项式，验证者产生随机标量a, b，证明者计算折叠后的多项式f^* = a * f_{2i} + b * f_{2i+1}，并承诺它。折叠的关键性质在于，如果某个点在原多项式上的求值错误，那么它在折叠多项式上的求值也几乎必然错误。通过将 √N 个子多项式在类似二叉树的结构中反复折叠（从叶子层到根层），最终只剩下一个大小为 √N 的折叠多项式。此时，证明者只需对这个最终的折叠多项式执行一次HyperEval，生成 √N 个证明，总复杂度为O(N)。该折叠技术依赖于PC方案的同态性，若底层PC非同态（如哈希类），则可通过附加的纠错码和随机采样验证来实现等价效果。

**组合成zkSNARK。**
HydraProofs的向量承诺直接与GKR协议组合成适用于多用户场景的zkSNARK（Construction 2）。证明者首先使用HydraProofs计算向量承诺C_x并生成所有打开证明。随后，它证明一个包含C_x和私有w的NP关系：（1）C(x, w) = 1，且（2）C_x是x的有效承诺。对于（1），使用GKR协议；对于（2），在GKR协议结束时，验证者得到一个关于f_x（x的多线性扩展）的求值点，证明者利用底层PC方案（与HydraProofs相同）生成一个求值证明，该证明自然成立。整个系统的证明者复杂度为O(|C|)，证明大小为O(d log |C| + ps(|w|) + ps(|x|) + log^2 N)，验证时间为O(d log |C| + log^2 N + vt(N) + |x_i|)，其中ps和vt是底层PC方案的证明大小和验证时间。安全性基于PC方案的可靠性，通过构造提取器将成功的攻击者规约到破坏PC方案的绑定性或知识可靠性来证明。

### 核心公式与流程

**HydraProofs OpenAll 核心步骤（两阶段折叠）：**

- **Phase 1: 分段一致性证明 (Consistency Proof)**
    - **目标**：证明子向量承诺 C_i 对应于原始承诺 C 的第 i 段。
    - **步骤**：对随机 r1，证明者计算 $f'(\mathbf{z}) = f(\mathbf{z}, \mathbf{r}_1)$ 并承诺，生成证明 $\pi_i$ 和 $\pi'_i$。
    - **验证**：验证 $f_i(\mathbf{r}_1) = f'(\mathbf{i})$ 的值和 $f(\mathbf{r}_2, \mathbf{r}_1) = f'(\mathbf{r}_2)$。
    - **核心公式**：
        $$y_i = f_i(\mathbf{r}_1) \stackrel{?}{=} f'(\mathbf{i}) = y'_i$$
        $$y = f(\mathbf{r}_2, \mathbf{r}_1) \stackrel{?}{=} f'(\mathbf{r}_2) = y'$$

- **Phase 2: 折叠 HyperEval (Folding HyperEval)**
    - **目标**：将 √N 个子多项式 f_i 的 HyperEval 实例折叠成一个。
    - **核心形式**：对两个多项式 f_0, f_1，进行折叠。
    - **核心公式**（假设同态PC）：
        - 折叠多项式: $f^*(\mathbf{x}) \gets a f_0(\mathbf{x}) + b f_1(\mathbf{x})$
        - 折叠承诺: $C_{f^*} \gets C_0^a C_1^b$
        - 折叠求值: $y_k^* \gets a y_{0,k} + b y_{1,k}$
    - **作用**：此折叠可递归进行，最终将所有实例合并为一个，从而只需对这个最终的折叠多项式执行一次O(N)的HyperEval。

**GKR zkSNARK 组合 (Construction 2):**
- **步骤 1:** 计算向量承诺 $C_x \gets VC.Commit(pk, x)$
- **步骤 2:** 运行 HydraProofs OpenAll 协议，为每个用户 i 证明 $x_i = x[i]$
- **步骤 3:** 运行 GKR 协议，证明 $C(x, w) = 1$。结束时，获得对 f_x 和 f_w 的求值点 r。
- **步骤 4:** 生成并发送 f_x 和 f_w 在 r 点的 PC 求值证明。

### 实验结果
实验在一台配备64个vCPU和512GB RAM的Azure Standard_E64s_v5实例上进行（除VRA外均单线程）。HydraProofs的OpenAll性能表现卓越：对于大小为2^22的向量，生成所有证明仅需7.07秒，而Hyperproofs [39] 和 Balanceproofs [22] 分别需要578秒和5370.8秒，加速比达到38.4x到767x。即使使用与竞争者相同的底层PC（KZG），HydraProofs+KZG仍能实现14.4x-16.6x的加速，证明优化算法本身是主要贡献。在与GKR结合的实验中，HydraProofs+GKR在总证明者时间上比GKR+MT（Merkle树）和GKR+HP（Hyperproofs）快4-16倍，例如对于大小为2^25的电路，其证明者用时仅110秒，而后两者分别为898.1秒和1307.52秒。在VSS应用中，对于2^21个接收者，基于HydraProofs的VSS方案仅需16.4秒，远快于PolyFRIM [28]（157.35秒）和ZXH+-KZG [27]（1.83小时）。批量证明多个VSS实例时，其优势更为明显，当批量大小为256时，每实例的证明者时间仅为0.23秒，只比单独计算（0.17秒）慢1.28倍。在VRA应用中（使用64核），对于1024个客户端和32K参数的FLTrust算法，生成证明仅需不到7秒，对于更复杂的FoolsGold算法也不到15秒，表明其可以被实际部署。

### 局限性与开放问题
本文的主要局限性在于OpenAll协议的安全性证明依赖于所有验证者在同一回合内提供相同的随机挑战。虽然论文通过利用Fiat-Shamir变体 [27] 使得协议非交互化，但这引入了额外的计算开销（如构建Merkle树）并可能需要随机预言机假设。此外，虽然在实验上取得了显著加速，但HydraProofs的证明大小取决于底层PC方案，相较于使用O(1)大小证明的KZG方案可能更大。未来的工作可以探索如何在不增加太多复杂性或牺牲线性时间的前提下，进一步优化证明大小。另一个开放问题是，如何将本文的折叠技术推广到更一般的多项式承诺方案或更广泛的密码学原语中。

### 强关联论文

[39] Srinivasan 等. Hyperproofs: Aggregating and Maintaining Proofs in Vector Commitments. **USENIX Security 2022** [Google Scholar](https://scholar.google.com/scholar?q=Hyperproofs%3A+Aggregating+and+Maintaining+Proofs+in+Vector+Commitments)

[22] Wang 等. Balanceproofs: Maintainable Vector Commitments with Fast Aggregation. **USENIX Security 2023** [Google Scholar](https://scholar.google.com/scholar?q=Balanceproofs%3A+Maintainable+Vector+Commitments+with+Fast+Aggregation)

[37] Setty 等. Quarks: Quadruple-efficient transparent zk-SNARKs. **ePrint 2020** [Google Scholar](https://scholar.google.com/scholar?q=Quarks%3A+Quadruple-efficient+transparent+zk-SNARKs)

[38] Xie 等. Orion: Zero Knowledge Proof with Linear Prover Time. **CRYPTO 2022** [Google Scholar](https://scholar.google.com/scholar?q=Orion%3A+Zero+Knowledge+Proof+with+Linear+Prover+Time)

[27] Zhang 等. Polynomial Commitment with a One-to-Many Prover and Applications. **USENIX Security 2022** [Google Scholar](https://scholar.google.com/scholar?q=Polynomial+Commitment+with+a+One-to-Many+Prover+and+Applications)

[28] Zhang 等. Fast RS-IOP Multivariate Polynomial Commitments and Verifiable Secret Sharing. **USENIX Security 2024** [Google Scholar](https://scholar.google.com/scholar?q=Fast+RS-IOP+Multivariate+Polynomial+Commitments+and+Verifiable+Secret+Sharing)

[29] Xie 等. Libra: Succinct Zero-Knowledge Proofs with Optimal Prover Computation. **CRYPTO 2019** [Google Scholar](https://scholar.google.com/scholar?q=Libra%3A+Succinct+Zero-Knowledge+Proofs+with+Optimal+Prover+Computation)

[41] Goldwasser 等. Delegating Computation: Interactive Proofs for Muggles. **JACM 2015** [Google Scholar](https://scholar.google.com/scholar?q=Delegating+Computation%3A+Interactive+Proofs+for+Muggles)

[42] Zhang 等. vSQL: Verifying Arbitrary SQL Queries over Dynamic Outsourced Databases. **IEEE S&P 2017** [Google Scholar](https://scholar.google.com/scholar?q=vSQL%3A+Verifying+Arbitrary+SQL+Queries+over+Dynamic+Outsourced+Databases)

[31] Gabizon 等. PLONK: Permutations over Lagrange-bases for Oecumenical Noninteractive Arguments of Knowledge. **ePrint 2019** [Google Scholar](https://scholar.google.com/scholar?q=PLONK%3A+Permutations+over+Lagrange-bases+for+Oecumenical+Noninteractive+Arguments+of+Knowledge)


## 关键词

+ 向量承诺最优证明生成
+ 多线性多项式兼容zkSNARK
+ GKR协议结合
+ 可验证秘密共享线性时间
+ 可验证鲁棒聚合
+ 多用户隐私计算验证