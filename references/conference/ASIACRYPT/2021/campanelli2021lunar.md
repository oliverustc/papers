---
title: "Lunar: a toolbox for more efficient universal and updatable zkSNARKs and commit-and-prove extensions"
doi: 10.1007/978-3-030-92078-4_1
标题简称:
论文类型: conference
会议简称: ASIACRYPT
发表年份: 2021
modified: 2025-04-13 17:40:03
---
## Lunar: a toolbox for more efficient universal and updatable zkSNARKs and commit-and-prove extensions

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-030-92078-4_1)

## 作者

+ [Matteo Campanelli](Matteo%20Campanelli.md)
+ Antonio Faonio 
+ [Dario Fiore](Dario%20Fiore.md)
+ Anais Querol 
+ Hadrián Rodriguez 

## 笔记

### 背景与动机

零知识非交互式简洁论证（zkSNARK）使得证明者能够向验证者证明一个非确定计算被接受，同时不泄露多余信息。在实际应用中，可预处理的zkSNARK需要为每个电路生成一个依赖结构的参考字符串（SRS），而通用可更新SRS模型允许一个SRS支持所有有界大小的电路，并且可以由参与者动态添加随机性，只要至少有一位参与者诚实，序列更新就是安全的。Groth等人 [34] 首次提出这一模型，但其SRS的大小与电路中乘法门数量的二次方成正比，更新和验证时间也是二次的。后续工作 [18,19,21,27,45,53] 将SRS大小改进为与最大支持电路大小呈线性关系，其中Marlin [19]和PLONK [27] 取得了比Sonic [45] 更快的具体证明时间，且证明大小为常数。然而，这些方案在证明大小和证明者运行时间上仍有改进空间。本文旨在填补这一空白：提出一族新的通用可更新zkSNARK，称为Lunar，其证明大小更小、证明者运行时间更短，同时详细阐述了背后的形式化框架和构造技术。

### 相关工作

[19] Chiesa et al. Marlin: Preprocessing zkSNARKs with Universal and Updatable SRS. **EUROCRYPT 2020** [Google Scholar](https://scholar.google.com/scholar?q=Marlin+Preprocessing+zkSNARKs+with+Universal+and+Updatable+SRS)  
> 核心思路：基于代数全息证明（AHP）和多项式承诺构造通用可更新zkSNARK，SRS大小与最大电路中的乘法门数呈线性，证明由13个群元素构成。  
> 局限与区别：Marlin的证明大小为13个 $\mathbb{G}_1$ 元素和8个域元素，而LunarLite仅用10个 $\mathbb{G}_1$ 元素和2个域元素，且证明者时间更低（$8n+3m$ 对比Marlin的 $14n+8m$）。

[27] Gabizon et al. PLONK: Permutations over Lagrange-bases for Oecumenical Noninteractive arguments of Knowledge. **ePrint 2019/953** [Google Scholar](https://scholar.google.com/scholar?q=PLONK+Permutations+over+Lagrange-bases+for+Oecumenical+Noninteractive+arguments+of+Knowledge)  
> 核心思路：利用拉格朗日基上的置换和多项式承诺构建通用可更新zkSNARK，具有常数大小证明。  
> 局限与区别：PLONK对于仅含乘法门的电路较快，但当电路中加法门较多时，LunarLite更快（当 $m\leq 3a$ 时）。

[45] Maller et al. Sonic: Zero-Knowledge SNARKs from Linear-Size Universal and Updatable Structured Reference Strings. **ACM CCS 2019** [Google Scholar](https://scholar.google.com/scholar?q=Sonic+Zero-Knowledge+SNARKs+from+Linear-Size+Universal+and+Updatable+Structured+Reference+Strings)  
> 核心思路：首个具有线性大小SRS的通用可更新zkSNARK，但证明大小为20个群元素，验证需要7对配对。  
> 局限与区别：Sonic的证明大小和证明者时间均高于Lunar系列，且验证复杂度较高。

[18] Campanelli et al. LegoSNARK: Modular Design and Composition of Succinct Zero-Knowledge Proofs. **ACM CCS 2019** [Google Scholar](https://scholar.google.com/scholar?q=LegoSNARK+Modular+Design+and+Composition+of+Succinct+Zero-Knowledge+Proofs)  
> 核心思路：提出commit-and-prove SNARK（CP-SNARK）的模块化构造，支持通用设置下的组合。  
> 局限与区别：Lunar的CP-SNARK编译器比LegoUAC更高效，且支持更多的多项式关系（如二次方程检验）。

[8] Ben-Sasson et al. Aurora: Transparent Succinct Arguments for R1CS. **EUROCRYPT 2019** [Google Scholar](https://scholar.google.com/scholar?q=Aurora+Transparent+Succinct+Arguments+for+R1CS)  
> 核心思路：基于IOP和哈希承诺的透明简洁论证，无需可信设置，但验证时间线性于电路大小。  
> 局限与区别：Aurora不是预处理SNARK，验证者需读取整个电路；Lunar提供预处理且证明大小恒定。

[33] Groth. On the Size of Pairing-Based Non-Interactive Arguments. **EUROCRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=On+the+Size+of+Pairing-Based+Non-Interactive+Arguments)  
> 核心思路：构造了当时证明最小的zkSNARK（仅3个群元素），但SRS是电路相关的且不可更新。  
> 局限与区别：Groth16的SRS依赖于具体电路，且不可更新；Lunar的SRS是通用且可更新的。

[39] Kate et al. Constant-Size Commitments to Polynomials and Their Applications. **ASIACRYPT 2010** [Google Scholar](https://scholar.google.com/scholar?q=Constant-Size+Commitments+to+Polynomials+and+Their+Applications)  
> 核心思路：提出基于配对的多项式承诺方案（KZG承诺），承诺大小恒定，支持可验证的评估。  
> 局限与区别：KZG承诺需要可信设置且非可更新；Lunar在其基础上实现了类型化、部分隐藏的承诺，并设计配套的CP-SNARK。

[34] Groth et al. Updatable and Universal Common Reference Strings with Applications to zk-SNARKs. **CRYPTO 2018** [Google Scholar](https://scholar.google.com/scholar?q=Updatable+and+Universal+Common+Reference+Strings+with+Applications+to+zk-SNARKs)  
> 核心思路：首次形式化通用可更新SRS模型，并给出一个构造，但其SRS大小为二次。  
> 局限与区别：Lunar基于该模型，但实现了线性大小SRS，并提供了更高效的编译框架。

[11] Benarroch et al. Zero-Knowledge Proofs for Set Membership: Efficient, Succinct, Modular. **Financial Cryptography 2021** [Google Scholar](https://scholar.google.com/scholar?q=Zero-Knowledge+Proofs+for+Set+Membership+Efficient+Succinct+Modular)  
> 核心思路：在素数阶群上构造可组合的CP-SNARK，支持类型化承诺。  
> 局限与区别：Lunar的CP-SNARK与其互补，可共享同一SRS；Lunar进一步实现了通用设置的CP-SNARK编译器。

### 核心技术与方案

**1. 多项式全息交互式证明（PHP）**  
Lunar提出了一种新的信息论抽象——多项式全息IOP（PHP），它是代数全息证明（AHP）和多项式IOP的推广。一个PHP协议包含一个离线阶段，其中关系编码器将关系描述编码为若干多项式（称为关系多项式）；在线阶段中，证明者和验证者进行多轮交互，证明者发送域元素和多项式预言，验证者最终输出两类检验：次数检验和多项式等式检验。PHP的关键特点是其验证者的多项式检验可以表达为一般形式：  
$$F(X) = G\Bigl(X, \bigl\{p_k(v_k(X))\bigr\}_{k\in[\mathfrak{n}^*]}, \{\pi_k\}_{k\in[\mathfrak{m}^*]}\Bigr) \equiv 0$$  
其中$G$是一个多项式，$v_k$是系数多项式。该形式包含了AHP中的求值查询和PLONK/ILDP中的等式检验。此外，PHP引入了细粒度的有界零知识概念：对每个证明者预言多项式，允许泄露固定数量的求值。这一性质在编译时允许使用更弱的承诺和CP-SNARK。

**2. 从PHP到通用zkSNARK的编译器**  
编译器将PHP、类型化多项式承诺方案和若干CP-SNARK组合为通用可更新zkSNARK。承诺方案提供两种类型：`rel`（用于关系多项式，只需绑定，无需隐藏）和`swh`（用于证明者多项式，需要“些许隐藏”）。些许隐藏保证每次承诺只泄露多项式在随机点上的一个求值。编译器使用两个CP-SNARK：`CP_opn`用于证明多项式承诺的开口的知识，`CP_php`用于证明PHP验证者的所有检验（次数检验和等式检验）在承诺的多项式上成立。证明者通过Fiat-Shamir变换实现非交互。安全证明中，知识可靠性通过提取承诺中的多项式并利用PHP的知识可靠性得到；零知识通过PHP的$(b+1)$-有界零知识、承诺的些许隐藏和`CP_php`的$b$-泄漏零知识组合实现。编译器还支持将SRS升级为可更新的，只需承诺方案和CP-SNARK的密钥生成是确定性的（承诺专用SRS）。

**3. 配对基的CP-SNARK实现**  
Lunar实现了两类类型化多项式承诺方案（`CS_1`和`CS_2`），它们都基于KZG承诺：承诺是多项式在秘密点上的求值之群元素。`CS_1`对所有承诺使用$\mathbb{G}_1$，`CS_2`对`swh`类型用$\mathbb{G}_1$、对`rel`类型用$\mathbb{G}_2$，从而支持更高效的二次方程检验。对应的CP-SNARK包括：`CP_opn`（在代数群模型或mPKE假设下）、`CP_eval`（单点/批量求值）、`CP_eq`（一般多项式等式）、`CP_qeq`（二次多项式等式，针对`CS_2`可为空证明）、`CP_deg`（次数界限）。其中`CP_qeq`利用配对性质直接检验二次关系，无需额外群元素，这得益于类型化承诺将多项式分别置于$\mathbb{G}_1$和$\mathbb{G}_2$。

**4. PHP构造**  
Lunar设计了多个PHP用于R1CS和一种新引入的简化约束系统R1CS-lite。R1CS-lite仅使用两个矩阵$L,R$，要求$(L\mathbf{c})\circ(R\mathbf{c})=\mathbf{c}$，其中$\mathbf{c}=(1,\mathbf{x},\mathbf{w})$，可表达与R1CS相同的语言且复杂度相当。PHP构造的核心技术是：利用联合稀疏编码将矩阵编码为多项式，将约束转化为一个关于和的多项式恒等式，然后通过一元求和检验（sumcheck）压缩验证。作者还提出了一种零知识求和检验的优化技巧：仅需随机采样稀疏的掩码多项式（而不是完全随机多项式），这得益于PHP有界零知识的要求。具体协议`PHP_lite1`中，关系编码器输出8个多项式，证明者发送掩码后的多项式、求和检验所需的商多项式及辅助多项式，验证者最后输出两个多项式检验（次数分别为2和2）。知识可靠性误差为$O(|\mathbb{H}|/|\mathbb{F}|)$，零知识性质在参数选择下达到完美。

**5. 从PHP到CP-SNARK的扩展**  
编译器还可以扩展到生成通用CP-SNARK，其输入包含可复用的隐藏承诺。这种扩展要求PHP的提取器满足直线可提取性，并且承诺方案增加类型`lnk`用于输入承诺（需隐藏和绑定）。证明者在原有PHP证明的基础上，额外计算一个`CP_link`证明，将输入承诺中的值（由提取器从证明者多项式生成）与PHP多项式承诺相关联。这首次将（代数）IOP编译为可复用的CP-SNARK。

### 核心公式与流程

**[R1CS-lite定义]**  
$$(\mathbb{F},n,m,\ell,\{\boldsymbol{L},\boldsymbol{R}\}), \boldsymbol{x}, \boldsymbol{w} \quad\text{s.t.}\quad \mathbf{c}=(1,\boldsymbol{x},\boldsymbol{w}),\quad (\boldsymbol{L}\mathbf{c})\circ(\boldsymbol{R}\mathbf{c})=\mathbf{c}$$
> 作用：简化版的R1CS，仅用两个矩阵，可表达与标准R1CS相同的语言，但使得PHP构造更简洁。

**[PHP_lite1的在线阶段流程]**  
1. 证明者发送 $\hat{a}'(X), \hat{b}'(X), s(X)$（掩码后的多项式）。  
2. 验证者发送随机点 $x,\alpha\in\mathbb{F}$。  
3. 证明者计算 $p(X) = (\hat{a}+\alpha\hat{b})\Lambda_{\mathbb{H}}(x,X) + \hat{a}\hat{b}V_{LR}(x,X,\alpha)$，然后发送 $q(X),r(X)$ 使得 $s+p = qZ_{\mathbb{H}} + Xr$。  
4. 验证者发送随机点 $y\in\mathbb{F}\setminus\mathbb{H}$。  
5. 证明者计算 $\sigma = V_{LR}(x,y,\alpha)$ 及额外的商多项式 $q'(X), r'(X)$，发送 $\sigma, q', r'$。  
> 作用：通过一元求和检验将矩阵乘法约束压缩为单个多项式等式。

**[决策阶段的第一个多项式检验（公式 (6)）]**  
$$
\begin{aligned}
s(y) + &\Big(\hat{a}'(y) Z_{\mathbb{L}}(y) + \sum_{\eta\in\mathbb{L}}\boldsymbol{x}'_{\phi_{\mathbb{H}}(\eta)}\mathcal{L}_{\eta}^{\mathbb{H}}(y)\Big)\Big(\Lambda_{\mathbb{H}}(x,y) + \sigma(\hat{b}'(y)Z_{\mathbb{L}}(y)+1)\Big) \\
&+ \big(\hat{b}'(y)Z_{\mathbb{L}}(y)+1\big)\alpha\Lambda_{\mathbb{H}}(x,y) - q(y)Z_{\mathbb{H}}(y) - y r(y) \stackrel{?}{=} 0
\end{aligned}
$$
> 作用：验证求和检验的正确性，即 $\sum_{\eta\in\mathbb{H}} s(\eta)+p(\eta)=0$。

**[决策阶段的第二个多项式检验（公式 (7) 或 (8)）]**  
$$
\begin{aligned}
\frac{\sigma}{|\mathbb{K}|}n^2\big(xy+\text{cr}(X)-x\cdot\text{col}(X)-y\cdot\text{row}(X)\big) & \\
+ r'(X)n^2\big(xy\cdot X+\text{cr}'(X)-x\cdot\text{col}'(X)-y\cdot\text{row}'(X)\big) & \\
- \big(\text{vcr}_L(X)+\alpha\cdot\text{vcr}_R(X)\big)Z_{\mathbb{H}}(x)Z_{\mathbb{H}}(y) - q'(X)Z_{\mathbb{K}}(X) &\stackrel{?}{=} 0
\end{aligned}
$$
> 作用：验证 $\sigma = V_{LR}(x,y,\alpha)$，即矩阵线性组合在随机点上的求值。

### 实验结果

论文在Table 1中给出了Lunar系列与Sonic、Marlin、PLONK在算术电路可满足性基准下的效率对比。核心数值如下：LunarLite的证明大小为10个$\mathbb{G}_1$元素和2个域元素（在BN128曲线上为384字节，在BLS12-381上为544字节），SRS大小为$M$个$\mathbb{G}_1$元素和$M$个$\mathbb{G}_2$元素（$M$为最大支持矩阵非零元数），证明者时间$8n+3m$（$n$为乘法门数，$m$为矩阵非零元数），验证者需7对配对。Lunar1cs(fast & short)的证明大小为11个$\mathbb{G}_1$元素和2个域元素，证明者时间$9n+3m$，验证需7对配对，但具有最小的SRS大小（$M$个$\mathbb{G}_1$和$M$个$\mathbb{G}_2$）和最短的证明。Lunar1cs(short vk)则提供更小的验证密钥（12个$\mathbb{G}_1$元素）和仅2对配对的验证时间，但证明大小略大（12个$\mathbb{G}_1$和5个域元素），SRS大小增至$3M$个$\mathbb{G}_1$。相比之下，Marlin（proof最短版本）的证明为13个$\mathbb{G}_1$和8个域元素，证明者时间$14n+8m$；PLONK的证明为7个$\mathbb{G}_1$和7个域元素，证明者时间$8n+8a$（$a$为加法门数）。实验确认了LunarLite在证明大小和证明者时间上优于现有方案的结论，尤其是当$m\leq 3a$时比PLONK更快。所有结果基于椭圆曲线BN128和BLS12-381的实现，安全级别分别为100位和128位。论文还指出，在mPKE假设（而非AGM）下实例化时，Lunar方案的额外开销远小于Marlin：仅增加4个$\mathbb{G}_1$元素和最多$3n+6m$个指数运算，而Marlin需增加11个$\mathbb{G}_1$和$11n+5m$个指数运算。

### 局限性与开放问题

Lunar的构造基于配对基的多项式承诺，这需要信任的设置（SRS生成）且依赖双线性群假设，不适用于后量子安全场景。PHP和编译器的形式化虽然支持可更新的SRS，但尚未给出具体的更新协议细节，仅指出承诺方案仅含单项式时是天然可更新的。此外，LunarLite使用的R1CS-lite语言虽然在表达力上与R1CS等价，但其直观性不如标准R1CS，需要额外的转换开销。未来工作可探索如何将PHP框架扩展到其他假设（如后量子安全的承诺方案），以及如何自动化编译器以获得更多不同的效率权衡。另一个开放问题是能否进一步降低证明大小以达到与Groth16相当的3个群元素，同时保持通用可更新性。

### 强关联论文

[19] Chiesa, A., Hu, Y., Maller, M., Mishra, P., Vesely, N., Ward, N. Marlin: Preprocessing zkSNARKs with Universal and Updatable SRS. **EUROCRYPT 2020**

[27] Gabizon, A., Williamson, Z.J., Ciobotaru, O. PLONK: Permutations over Lagrange-bases for Oecumenical Noninteractive arguments of Knowledge. **ePrint 2019/953**

[45] Maller, M., Bowe, S., Kohlweiss, M., Meiklejohn, S., Miers, I. Sonic: Zero-Knowledge SNARKs from Linear-Size Universal and Updatable Structured Reference Strings. **ACM CCS 2019**

[18] Campanelli, M., Fiore, D., Querol, A. LegoSNARK: Modular Design and Composition of Succinct Zero-Knowledge Proofs. **ACM CCS 2019**

[8] Ben-Sasson, E., Chiesa, A., Riabzev, M., Spooner, N., Virza, M., Ward, N.P. Aurora: Transparent Succinct Arguments for R1CS. **EUROCRYPT 2019**

[33] Groth, J. On the Size of Pairing-Based Non-Interactive Arguments. **EUROCRYPT 2016**

[39] Kate, A., Zaverucha, G.M., Goldberg, I. Constant-Size Commitments to Polynomials and Their Applications. **ASIACRYPT 2010**

[34] Groth, J., Kohlweiss, M., Maller, M., Meiklejohn, S., Miers, I. Updatable and Universal Common Reference Strings with Applications to zk-SNARKs. **CRYPTO 2018**

[11] Benarroch, D., Campanelli, M., Fiore, D., Gurkan, K., Kolonelos, D. Zero-Knowledge Proofs for Set Membership: Efficient, Succinct, Modular. **Financial Cryptography 2021**

[40] Kilian, J. A Note on Efficient Zero-Knowledge Proofs and Arguments (Extended Abstract). **24th ACM STOC 1992**


## 关键词

+ zkSNARK
+ 可更新参数
+ 多项式承诺
+ R1CS
+ 证明可组合性