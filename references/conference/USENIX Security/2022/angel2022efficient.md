---
title: "Efficient representation of numerical optimization problems for SNARKs"
标题简称:
论文类型: conference
会议简称: USENIX Security
发表年份: 2022
created: 2025-05-23 01:19:22
modified: 2025-05-23 01:20:03
---

## Efficient representation of numerical optimization problems for SNARKs

## 发表信息

+ [原文链接](https://www.usenix.org/conference/usenixsecurity22/presentation/angel)

## 作者

+ Sebastian Angel
+ Andrew J Blumberg
+ Eleftherios Ioannidis
+ Jess Woods

## 笔记

### 背景与动机
数值优化问题是科学、工程与商业中的核心构建模块，应用涵盖资源分配、NP难问题的近似求解以及神经网络训练等领域。然而，当求解方需要向其他方证明所得解的最优性时，现有机制面临严峻挑战：虽然零知识简洁非交互式知识论证（zkSNARK）为此提供了理论框架，但将优化算法（如单纯形法、内点法）直接编译为秩一约束可满足性（R1CS）实例会导致规模爆炸。具体而言，一个仅含3个变量和3个方程的线性规划（LP）实例，使用最先进的SNARK编译器会产生超过100万个乘法门。这种高昂的表述成本源于三大因素：需要支持随机内存访问、需要高精度定点数模拟实数运算、以及需要为求解器不确定的循环迭代次数预设上界。现有工作无法编译任何实际规模的半定规划（SDP）或随机梯度下降（SGD）问题。本文提出的Otti系统填补了这一空白：通过利用优化问题中的最优性证书构建非确定性检验器，将验证解的最优性而非模拟求解器执行，从而使R1CS的规模大幅降低。

### 相关工作

[16] Ben-Sasson, E. et al. Succinct Non-Interactive Zero Knowledge for a von Neumann Architecture. **USENIX Security 2014** [Google Scholar](https://scholar.google.com/scholar?q=Succinct+Non-Interactive+Zero+Knowledge+for+a+von+Neumann+Architecture)
> 核心思路：将通用冯·诺依曼架构编译为算术电路以支持SNARK证明。
> 局限与区别：其编译方法依赖于排序网络实现随机内存访问，导致约束数量随程序复杂度剧烈增长，无法高效处理含循环和随机访问的优化求解器。

[29] de Hoogh, S. et al. Certificate Validation in Secure Computation and its Use in Verifiable Linear Programming. **AFRICACRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=Certificate+Validation+in+Secure+Computation+and+its+Use+in+Verifiable+Linear+Programming)
> 核心思路：在半诚实安全多方计算协议中利用LP对偶证书验证最优性。
> 局限与区别：其方案针对特定安全模型且计算开销极大（200变量规模的实例耗时超过20小时），而Otti在SNARK场景下对类似规模可在数秒内完成。

[39] Goemans, M. et al. Doubly-Efficient Pseudo-Deterministic Proofs. **arXiv 2019** [Google Scholar](https://scholar.google.com/scholar?q=Doubly-Efficient+Pseudo-Deterministic+Proofs)
> 核心思路：从理论角度证明存在用于LP的多项式时间伪确定性交互证明，其关键在于利用强对偶性。
> 局限与区别：该工作为纯理论结果，未实现任何编译器或进行实验评估。Otti将其理论思想工程化，并扩展至SDP和SGD领域。

[52] Ozdemir, A. et al. Unifying Compilers for SNARKs, SMT, and More. **ePrint 2020** [Google Scholar](https://scholar.google.com/scholar?q=Unifying+Compilers+for+SNARKs,+SMT,+and+More)
> 核心思路：提出CirC编译器，可将C等高级语言编译为存在性量化的电路，并支持R1CS等多种输出格式。
> 局限与区别：Otti基于CirC构建，但直接编译优化求解器时CirC无法处理超过5个变量和4个方程的LP实例，内存耗尽。Otti通过非确定性检验器绕过了这一瓶颈。

[63] Setty, S. Spartan: Efficient and General-Purpose zkSNARKs without Trusted Setup. **CRYPTO 2020** [Google Scholar](https://scholar.google.com/scholar?q=Spartan:+Efficient+and+General-Purpose+zkSNARKs+without+Trusted+Setup)
> 核心思路：提出Spartan证明系统，在不需可信设置的前提下实现高效证明生成。
> 局限与区别：Otti将Spartan作为底层证明系统使用，但本文的贡献在于编译器的前端而非证明系统本身。

[72] Wu, H. et al. DIZK: A Distributed Zero Knowledge Proof System. **USENIX Security 2018** [Google Scholar](https://scholar.google.com/scholar?q=DIZK:+A+Distributed+Zero+Knowledge+Proof+System)
> 核心思路：通过分布式计算实现大规模计算的零知识证明，可处理线性回归的训练证明。
> 局限与区别：DIZK需要数十台机器协同工作才能完成简单线性模型的训练证明，而Otti在单机上即可完成更复杂分类器的训练证明。

[76] Zhao, L. et al. VeriML: Enabling Integrity Assurances and Fair Payments for Machine Learning as a Service. **IEEE TPDS 2021** [Google Scholar](https://scholar.google.com/scholar?q=VeriML:+Enabling+Integrity+Assurances+and+Fair+Payments+for+Machine+Learning+as+a+Service)
> 核心思路：对机器学习模型训练过程生成证明，但仅验证随机选取的少数训练迭代的正确性。
> 局限与区别：该方案仅提供概率性保证而非完整训练的正确性；Otti则能证明完成全部训练后的最优性。

### 核心技术与方案

**整体框架**
Otti的核心思路是：不将求解器本身编译为R1CS，而是编译一个非确定性检验器。该检验器接收一个待验证的解（由外部求解器提供），并验证该解满足最优性证书。证明者先用传统数值求解器（如lpsolve、CSDP、scikit-learn）求出一个解，然后生成一个显示该解通过检验器检查的zkSNARK证明。这一框架规避了直接编译求解器时的三个主要困难：随机内存访问（检验器无需访问求解器的数据结构，仅需对给定解进行算术计算）、不确定循环次数（检验器是无循环的、确定性的表达式集合）、以及复杂的求解逻辑。

**线性规划的证书构造**
LP的证书来源于强对偶定理。给定原始问题$ \max \{ \mathbf{c}^T \mathbf{x} \mid A\mathbf{x} \leq \mathbf{b}, \mathbf{x} \geq \mathbf{0} \}$，Otti自动推导其对偶问题$ \min \{ \mathbf{b}^T \mathbf{y} \mid A^T \mathbf{y} \geq \mathbf{c}, \mathbf{y} \geq \mathbf{0} \}$。最优性证书包含三个条件：原始可行性（$A\mathbf{x} \leq \mathbf{b}$, $\mathbf{x} \geq \mathbf{0}$）、对偶可行性（$A^T \mathbf{y} \geq \mathbf{c}$, $\mathbf{y} \geq \mathbf{0}$）以及强对偶条件（$\mathbf{c}^T \mathbf{x} = \mathbf{b}^T \mathbf{y}$）。Otti将这三个条件直接编译为R1CS中的乘法与加法约束。证明者将原始解$\mathbf{x}$和对偶解$\mathbf{y}$作为非确定性变量提供，检验器验证上述所有不等式与等式是否成立。该R1CS实例的规模与原始LP问题的规模呈近似线性关系，完全避免了循环和随机内存访问。

**半定规划的证书构造**
SDP的证书类似，但涉及正定矩阵的验证。原始问题为$ \max \{ C \bullet X \mid \forall i: A_i \bullet X = b_i, X \succeq 0 \}$，其中$X \succeq 0$表示$X$为半正定矩阵。Otti利用Cholesky分解：一个矩阵$X$半正定当且仅当存在下三角矩阵$L$使得$X = LL^T$且$L$的对角元非负。证明者提供$X$的Cholesky因子$X_L$作为非确定性变量，检验器验证$X_L \cdot X_L^T = X$以及$X_L$的对角元非负（在定点数表示下通过范围检查实现）。对偶可行性及强对偶性（$S \bullet X = 0$）的检验同样以Cholesky分解处理$S$矩阵。此方案要求SDP实例严格可行以保证对偶间隙为零，Otti通过让证明者提供一个初始可行点$X_0$来保证内点法的收敛性。

**随机梯度下降的证书构造**
对于SGD，Otti在强增长条件假设下构造证书。该条件要求$E(\| \nabla f_i \|^2) \leq E(\| \nabla f \|^2)$，即每个随机梯度的二阶矩不超过全梯度的二阶矩。在此条件下，若$z$是$f$的局部最优点（即$\nabla f(z)=\mathbf{0}$），则必有$\nabla f_i(z)=\mathbf{0}$对所有$i$成立。因此，最优性证书就是验证对于所有数据点$i$，$ \nabla f_i(z) = \mathbf{0}$。对于感知机模型所用的铰链损失函数$f(w) = \sum_i \max(0, 1-y_i \langle w, x_i \rangle)$，这意味着验证对所有$i$有$1 - y_i \langle w, x_i \rangle \leq 0$。Otti还引入了概率性证书：当数据规模太大时，证明者仅需验证随机采样的一部分数据点，以此牺牲少量可靠性换取更低的计算代价。恶意证明者能够欺骗的概率取决于未通过检验的数据点数量在全部数据点中的占比。

**安全性与渐进复杂度**
从安全性角度看，LP和SDP的证书基于确定性数学定理，在实数域上具有完备性和可靠性。由于Otti使用定点数近似实数，可能存在由舍入误差导致的微弱失败概率，但通过选择足够的精度可使之可忽略。对于SGD，概率性证书引入了额外的可靠性损失：若恶意证明者提供的解有$\ell$个数据点不满足梯度为零，而验证者仅检查$k$个点，则欺骗成功的概率为$\binom{n-\ell}{k} / \binom{n}{k}$。证明的计算复杂度由R1CS约束数决定，以Spartan为底层系统时，证明者时间复杂度为$O(N \log N)$（$N$为约束数），验证者时间复杂度为$O(\sqrt{N})$，证明大小为$O(\log N)$。

### 核心公式与流程

**LP强对偶证书**
$$
\mathbf{x} \geq \mathbf{0},\ A\mathbf{x} \leq \mathbf{b}\quad (\text{原始可行性})
$$
$$
\mathbf{y} \geq \mathbf{0},\ A^T\mathbf{y} \geq \mathbf{c}\quad (\text{对偶可行性})
$$
$$
\mathbf{c}^T\mathbf{x} = \mathbf{b}^T\mathbf{y}\quad (\text{强对偶条件})
$$
> 作用：构成LP最优性的完整验证集。证明者提供向量$\mathbf{x}$和$\mathbf{y}$作为非确定性变量，检验器在上述所有不等式和等式上生成R1CS约束。

**SDP正定性的Cholesky检验**
$$
X = X_L \cdot X_L^T,\quad X_L \text{为下三角矩阵},\quad \forall i: (X_L)_{ii} \geq 0
$$
> 作用：将矩阵半正定性检验转化为矩阵乘法和非负性检验。证明者提供Cholesky因子$X_L$，检验器通过一次矩阵乘法和对角元范围检查确认$X \succeq 0$，避免直接求解特征值。

**SGD最优性的梯度条件（强增长假设下）**
$$
\forall i \in [n]: \ \nabla f_i(z) = \mathbf{0}
$$
对于铰链损失的感知机模型，等价于：
$$
\forall i \in [n]:\ 1 - y_i \langle w, x_i \rangle \leq 0
$$
> 作用：将训练过程的最优性检验简化为对每个数据点的线性不等式验证。证明者给出权重向量$w$，检验器计算内积并与阈值比较。

### 实验结果

实验在配备40核Intel Xeon E5-2660 v3 CPU（2.60GHz）和200 GB内存的服务器上进行。Otti使用lp_solve、CSDP和scikit-learn作为底层求解器，Spartan作为zkSNARK系统。对于LP基准测试（选取自netlib库的28个实例，变量数32至2,750，方程数28至398），Otti生成的R1CS约束数在3.6万至360万之间，证明大小均低于100 KB。证明生成时间从0.3秒（afiro）到4.7秒（scsd8），验证时间均低于1秒。相比于不生成证明的原生求解器，Otti的证明者开销平均为40倍。作为对比，CirC在相同机器上编译5变量4方程的小型LP实例即耗尽内存，且生成的约束数已超过Otti的最大实例。对于SDP基准测试（11个实例，矩阵大小13至16），R1CS约束数在300万至700万之间，证明生成时间在5至10.5秒，开销平均为30倍。对于SGD的感知机训练（18个PMLB数据集，数据点57至494,020，特征3至1,000），R1CS约束数从4,730到超过940万。最大的clean2数据集（6,598数据点、168特征）在检查全部数据点时超出内存限制，采用概率性证书（检查50%数据点）后降至677万约束，证明生成时间为18.23秒。过小数据集上的开销最高（可达450倍），大规模数据集上的开销较低（15倍左右）。

### 局限性与开放问题
Otti的SDP协议要求实例严格可行以保证强对偶成立，这限制了其适用范围；未来可借鉴Farkas引理及其替代定理构造更通用的证书。SGD证书严重依赖强增长条件，该条件对于非可分数据不成立；如何从更弱、更普遍的收敛假设中提取概率性证书是一个重要问题。此外，Otti的非确定性检验器本身需要形式化验证其正确性，以避免编译器bug导致的不正确证明。最后，Otti目前仅支持LP、SDP和特定形式的SGD，将其扩展到整数规划、锥规划等更广泛的优化问题族是自然延伸。

### 强关联论文

[29] de Hoogh, S. et al. Certificate Validation in Secure Computation and its Use in Verifiable Linear Programming. **AFRICACRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=Certificate+Validation+in+Secure+Computation+and+its+Use+in+Verifiable+Linear+Programming)

[39] Goemans, M. et al. Doubly-Efficient Pseudo-Deterministic Proofs. **arXiv 2019** [Google Scholar](https://scholar.google.com/scholar?q=Doubly-Efficient+Pseudo-Deterministic+Proofs)

[52] Ozdemir, A. et al. Unifying Compilers for SNARKs, SMT, and More. **ePrint 2020** [Google Scholar](https://scholar.google.com/scholar?q=Unifying+Compilers+for+SNARKs,+SMT,+and+More)

[63] Setty, S. Spartan: Efficient and General-Purpose zkSNARKs without Trusted Setup. **CRYPTO 2020** [Google Scholar](https://scholar.google.com/scholar?q=Spartan:+Efficient+and+General-Purpose+zkSNARKs+without+Trusted+Setup)

[72] Wu, H. et al. DIZK: A Distributed Zero Knowledge Proof System. **USENIX Security 2018** [Google Scholar](https://scholar.google.com/scholar?q=DIZK:+A+Distributed+Zero+Knowledge+Proof+System)

[76] Zhao, L. et al. VeriML: Enabling Integrity Assurances and Fair Payments for Machine Learning as a Service. **IEEE TPDS 2021** [Google Scholar](https://scholar.google.com/scholar?q=VeriML:+Enabling+Integrity+Assurances+and+Fair+Payments+for+Machine+Learning+as+a+Service)


## 关键词

+ Otti数值优化SNARK编译器
+ 线性规划零知识证明
+ R1CS算术化数值优化
+ 随机梯度下降ZK证明
+ Spartan证明系统应用
+ 优化问题最优性验证
