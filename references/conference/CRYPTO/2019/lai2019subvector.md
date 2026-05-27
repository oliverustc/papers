---
title: "Subvector commitments with application to succinct arguments"
doi: 10.1007/978-3-030-26948-7_19
标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 2019
modified: 2025-04-11 11:24:32
---
## Subvector commitments with application to succinct arguments

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-030-26948-7_19)

## 作者

+ Russell WF Lai 
+ [Giulio Malavolta](Giulio%20Malavolta.md)
## 笔记

### 背景与动机

构建简洁的非交互式论证（SNARK）是密码学领域的重要目标，这类系统允许证明者向验证者证明一个NP语句的真实性，且通信量远小于证据本身。现有的高效SNARK方案往往依赖于预处理的设置模型，即需要一个可信第三方生成依赖于具体语句的公共参考串。然而，在许多应用场景（如加密货币）中，公共硬币设置（即设置过程仅需公开的随机性，如随机预言机）更为理想，因为它避免了信任假设。基于Micali的“CS proofs”范式的方案采用Merkle树提交PCP字符串，其证明大小由多个Merkle树打开组成，大小与查询次数和PCP长度的对数成正比，例如对于80比特的安全性，证明大小约为113KB。现有向量承诺（VC）和函数承诺（FC）方案的打开大小随揭示的位置或函数输出数量线性增长，这在批处理场景中构成了效率瓶颈。Lai和Malavolta旨在通过引入子向量承诺（SVC）和线性映射承诺（LMC）来填补这一空白，它们具有更强的紧凑性，承诺和打开的大小完全独立于向量长度和揭示数量，从而能将多个PCP打开压缩为单个证明，在CS proofs范式下实现更短的论证。

### 相关工作

[27] Catalano and Fiore. Vector Commitments and Their Applications. **PKC 2013** [Google Scholar](https://scholar.google.com/scholar?q=Vector+Commitments+and+Their+Applications)
> 核心思路：基于CDH假设和RSA假设构造了向量承诺（VC），允许多项式时间证明者承诺一个向量，并在单个位置高效打开，承诺和打开均为单个群元素。
> 局限与区别：打开大小与被打开位置的数量线性相关，不支持紧凑的批量打开。本文的SVC和LMC将打开大小压缩为与揭示数量无关的常数。

[48] Libert, Ramanna, Yung. Functional Commitment Schemes: From Polynomial Commitments to Pairing-Based Accumulators from Simple Assumptions. **ICALP 2016** [Google Scholar](https://scholar.google.com/scholar?q=Functional+Commitment+Schemes+From+Polynomial+Commitments+to+Pairing-Based+Accumulators+from+Simple+Assumptions)
> 核心思路：形式化了函数承诺（FC）的概念，并基于Diffie-Hellman指数假设构造了支持线性形式打开的FC，承诺和打开均为单个群元素。
> 局限与区别：其“函数绑定”的定义仅针对同一线性形式（f）的不同输出，不支持不同形式间的一致性检查。本文定义了更强的“函数绑定”概念，要求任何一组打开的线性映射与输出必须构成一致方程组，并构造了支持任意线性映射的LMC。

[53] Micali. CS Proofs. **FOCS 1994** [Google Scholar](https://scholar.google.com/scholar?q=CS+Proofs)
> 核心思路：提出了CS proofs范式，将PCP与Merkle树提交结合，通过Fiat-Shamir变换转化为非交互式论证。证明大小由Merkle树承诺、若干PCP比特和多个对数大小的Merkle树打开构成。
> 局限与区别：证明大小中多个打开的项与PCP查询次数和向量长度对数线性相关。本文用SVC/LMC替换Merkle树，将多个打开压缩为一个常数大小的证明，大幅降低了通信量。

[40] Groth. On the Size of Pairing-Based Non-Interactive Arguments. **EUROCRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=On+the+Size+of+Pairing-Based+Non-Interactive+Arguments)
> 核心思路：在预处理模型和通用双线性群模型中，构造了证明仅为3个群元素的SNARK，并证明了该长度的最优下界。
> 局限与区别：该方案需要语句相关的预处理设置（公共参考串依赖具体电路），且仅支持特定的二次多项式验证器。本文的LMC编译器支持任意线性PCP，且设置是语句无关的。

[42] Ishai, Kushilevitz, Ostrovsky. Efficient Arguments without Short PCPs. **CCC 2007** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+Arguments+without+Short+PCPs)
> 核心思路：提出了线性PCP的概念，其中PCP字符串为域向量，验证者通过线性查询（内积）与证明者交互，并与同态加密结合构造了带预处理的交互式论证。
> 局限与区别：其使用的承诺方案绑定性质未保证被打开的函数必须是线性的。本文的LMC的“函数绑定”定义明确要求了这一点，并能与任意线性PCP结合。

### 核心技术与方案

本文的核心贡献在于两个层次：首先，构造了具有强紧凑性的基础密码学原语——子向量承诺（SVC）和线性映射承诺（LMC）；其次，利用这些原语设计了一个通用的编译器，将线性PCP转化为交互式论证，进而通过Fiat-Shamir变换得到简洁非交互式论证（SNARK）。

**1. 子向量承诺（SVC）构造**

论文提出了两种SVC构造，均将承诺打开大小压缩为常数。

*   **基于模与根假设的SVC（图1）**：该构造运行于欧几里得环上的模R_D上，依赖（公钥硬币）强相异-素数-乘积根假设或自适应根假设。公共参数包含一个随机元素X和一组由哈希函数H（或随机预言机）导出的素元e_i。承诺C由向量x与公钥S的内积（在模运算中定义为带标量乘法的R-线性组合）给出。打开算法对索引集I，证明Λ为乘积(∏_{i∈I} e_i)的逆作用在x的非I部分与对应S的R-线性组合上。验证算法通过检查方程 x_I' · S_I + (∏_{i∈I} e_i) Λ = C 是否成立。正确性直接由构造保证。安全性证明（定理1和2）通过规约到强相异-素数-乘积根问题或自适应根问题：若敌手能伪造两个子向量打开（在位置I∩J上存在冲突），则挑战者可利用代数关系构造出给定模元素的某个乘积根，从而打破假设。
*   **基于CDH与配对的SVC（图2）**：该构造运行于双线性群上，依赖CDH假设（通过规约到平方DH问题）。公共参数包含一组随机生成元G_i = G^{z_i}及其对偶Diffie-Hellman乘积H_{i,i'} = G^{z_i z_{i'}}。承诺C = ∏ G_i^{x_i}。打开Λ_I = ∏_{i∈I} ∏_{i'∉I} H_{i,i'}^{x_{i'}}。验证方程通过配对运算检验 e(C / ∏_{i∈I} G_i^{x_i}, ∏_{i∈I} G_i) = e(Λ_I, G)。其紧凑性在于，验证者只需访问公钥中|I|个群元素，计算2个配对和2|I|次群运算，且打开大小为常数。安全性证明的核心是构造一个CDH求解器：通过嵌入一个特定索引i^*上的CDH挑战，利用敌手的两个非法打开推导出G^{z^2}。

**2. 线性映射承诺（LMC）构造（图3）**

该构造允许打开任意线性映射F: F^ℓ → F^q，是函数承诺的推广。其核心思想源于多项式编码：将向量x编码为多项式p_x(α) = ∑ x_j α^j；将矩阵F编码为多项式p_F(α, z) = ∑ f_{i,j} z_i α^{ℓ+1-j}。那么F·x由p_F · p_x中z_i α^{ℓ+1}的系数给出。承诺C = G^{p_x(α)}；打开Λ = G^{∑_{i,j,j'} f_{i,j} x_{j'} z_i α^{ℓ+1+j-j'}}，即多项式乘积中除“关键”项z_i α^{ℓ+1}之外的所有项。验证者通过配对检查 e(C, ∏ H_{i,ℓ+1-j}^{f_{i,j}}) = e(G_1, ∏ H_{i,ℓ}^{y_i}) · e(Λ, G)。该方案的功能绑定性质在通用双线性群模型中证明（定理4），该证明利用了Schwartz-Zippel引理：任何对宏观多项式方程成立的篡改，都必须使多项式恒等，从而强制Λ的展开系数与一致线性系统F_k(x) = y_k兼容。

**3. 编译器与SNARK构造（图4）**

编译器将任意q-查询线性PCP与LMC结合，构造一个4轮交互式论证。协议流程如下：证明者首先利用线性PCP生成证明π，并提交其承诺C。验证者发送挑战α，证明者用PRG将其扩展为PCP的随机性ρ，计算查询矩阵F和对响应y，并打开C到(F, y)。验证者重新计算查询矩阵，并验证打开的有效性与PCP的判定结果。由于验证消息α和ρ均为公开随机串，该交互式论证具有公共硬币验证者，因此可应用Fiat-Shamir变换转化为非交互式SNARK。
该编译器证明为知识论证（定理5），其安全性依赖线性PCP的知识属性和PCP的可靠性，以及LMC的函数绑定性质。证明策略为：通过提取器从成功的交互中恢复出承诺所对应的向量x，并证明该向量就是有效PCP，从而完成知识提取。
实例化方面，基于类群（Class Group）的SVC（自适应根假设）实例化，使用240查询的PCP，得到证明大小为2个群元素+240比特 ≈ 5360比特，成为已知公钥硬币设置下最短的SNARK之一。基于配对的LMC实例化，使用3查询线性PCP，得到证明大小为2个群元素+3个域元素 ≈ 1280比特。

### 核心公式与流程

**[SVC基于根假设的构造：验证方程]**
$$C = \langle \boldsymbol{x}_I', \boldsymbol{S}_I \rangle + \left( \prod_{i \in I} e_i \right) \circ \Lambda_I$$
> 作用：验证打开的I-子向量x_I'和证明Λ_I是否与承诺C一致。这里⟨·,·⟩是R-模上的内积，∘是标量乘法。该方程利用了公钥S_i = (∏_{j≠i} e_j) ◦ X的结构。

**[SVC基于CDH的构造：验证方程]**
$$ e\left( \frac{C}{\prod_{i \in I} G_i^{x_i}}, \prod_{i \in I} G_i \right) = e(\Lambda_I, G) $$
> 作用：利用双线性配对e，验证承诺C、子向量x_I和证明Λ_I三者之间的关系，确保Λ_I正确编码了“交叉”项。

**[LMC的验证方程]**
$$ e\left(C, \prod_{i \in [q]} \prod_{j \in [\ell]} H_{i,\ell+1-j}^{f_{i,j}}\right) = e\left(G_1, \prod_{i \in [q]} H_{i,\ell}^{y_i}\right) \cdot e(\Lambda, G) $$
> 作用：验证承诺C对应的向量x满足F·x = y，证明Λ包含了多项式乘积p_F·p_x中所有非“关键”项。

**[编译器协议流程（交互式论证）]**
1.  Prover(P) → Verifier(V): C (对PCP字符串π的承诺)
2.  V → P: α (验证者随机挑战)
3.  P: 计算 ρ = PRG(α); F = Record(x, π, ρ); y = F·π; Λ = Open(F, y, aux)
4.  P → V: Λ, y (打开与响应)
5.  V: 计算 F' = Reconstruct(x, y, ρ); 验证 b_0 = Verify(C, F', y, Λ); 验证 b_1 = Decide(x, y, ρ); 输出 b_0 ∩ b_1
> 作用：将PCP的交互与SVC/LMC的打开相结合，将多个查询的打开压缩为单个常数大小的证明Λ。Record和Reconstruct确保查询矩阵的一致性。

### 实验结果

论文作为一篇理论工作，主要提供了参数选择和渐近复杂度分析，并未提供实际运行时间实验。各方案的比较集中体现在表1和表2中，这些比较基于假设的安全水平和计算模型。对于基于类群的SVC实例化，为对抗2^128时间攻击者，类群判别式|Δ|需选为2560比特，每个类群元素表示为约2560比特。结合240查询、2^{-80}可靠性的PCP，非交互式证明大小为 2*2560 + 240 = 5360比特。对于基于配对的LMC实例化，在256比特Barreto-Naehrig曲线上，每个群元素为256比特，使用3查询线性PCP，证明大小为 2*256 + 3*256 = 1280比特。与现有方案对比，本文（类群）的公钥硬币SNARK证明大小（5360比特）在实验报告中远小于Bulletproof（约512 log n + 3328比特，当n>16时）和经典CS Proofs（约113KB）。对于配对基LMC实例化，其证明大小（1280比特）持平或微优于Groth方案（3个群元素，约768比特），但后者需要语句相关的预处理设置。两个实例化的计算开销主要在于PCP生成（高）和基于群的操作；验证者计算在类群版本中由|I|次指数运算主导，在配对版本中由2|I|次群运算和2个配对运算主导。论文还指出了开源优化，例如使用Boneh等人的“PoKCR”技术可将类群验证时间降低80%。

### 局限性与开放问题

所有SVC和LMC实例化的证明验证计算复杂度为O(q)，即与PCP查询次数线性相关，这虽然比直接验证PCP本身高效，但在某些场景下可能仍是瓶颈。基于类群的SVC公钥大小与PCP长度线性相关，在PCP极长时可能非常大，而基于配对的SVC公钥大小甚至与PCP长度的平方相关，这严重限制了其可扩展性。开放问题包括：设计支持更高效验证的结构化SVC/LMC（如使用亚线性验证时间）；探索基于更难假设（如标准模型中的格基假设）的实例化；以及将编译器扩展到交互式预言证明（IOP）以利用更高效的证明系统。

### 强关联论文

[27] Catalano and Fiore. **PKC 2013** [Google Scholar](https://scholar.google.com/scholar?q=Vector+Commitments+and+Their+Applications)

[48] Libert, Ramanna, Yung. **ICALP 2016** [Google Scholar](https://scholar.google.com/scholar?q=Functional+Commitment+Schemes+From+Polynomial+Commitments+to+Pairing-Based+Accumulators+from+Simple+Assumptions)

[53] Micali. **FOCS 1994** [Google Scholar](https://scholar.google.com/scholar?q=CS+Proofs)

[40] Groth. **EUROCRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=On+the+Size+of+Pairing-Based+Non-Interactive+Arguments)

[42] Ishai, Kushilevitz, Ostrovsky. **CCC 2007** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+Arguments+without+Short+PCPs)

[63] Wesolowski. **ePrint 2018** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+Verifiable+Delay+Functions)

[20] Boneh, Bünz, Fisch. **ePrint 2018** [Google Scholar](https://scholar.google.com/scholar?q=Batching+Techniques+for+Accumulators+with+Applications+to+IOPs+and+Stateless+Blockchains)

[21] Bootle et al. **EUROCRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+Zero-Knowledge+Arguments+for+Arithmetic+Circuits+in+the+Discrete+Log+Setting)

[26] Bünz et al. **S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Bulletproofs+Short+Proofs+for+Confidential+Transactions+and+More)

[51] Lipmaa. **ACNS 2012** [Google Scholar](https://scholar.google.com/scholar?q=Secure+Accumulators+from+Euclidean+Rings+without+Trusted+Setup)


## 关键词

+ 密码学
+ 零知识
+ 协议