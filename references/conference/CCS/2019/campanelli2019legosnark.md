---
title: "LegoSNARK: Modular design and composition of succinct zero-knowledge proofs"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2019
modified: 2025-04-23 08:51:23
created: 2025-04-11 11:37:24
---

## LegoSNARK: Modular design and composition of succinct zero-knowledge proofs

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3319535.3339820)

## 作者

+ [Matteo Campanelli](Matteo%20Campanelli.md)
+ [Dario Fiore](Dario%20Fiore.md)
+ Anais Querol 

## 笔记

### 背景与动机
零知识简洁非交互式知识论证（zkSNARKs）能够在保护隐私的前提下高效验证计算，但其现有构造多为通用型，将计算统一表示为单一模型（如算术电路），导致处理异构计算（如同时包含算术和布尔组件）时效率低下。这种通用性忽略了具体计算的结构特性，无法利用专用方案的优化优势，例如并行计算的GKR协议或矩阵乘法的高效证明。此外，现有zkSNARKs的commit-and-prove（CP）能力不强，要么需要将承诺验证编码进电路导致巨大开销，要么各方案使用互不兼容的特定承诺方案，无法实现灵活组合。本文旨在提出一个模块化框架LegoSNARK，通过轻量级连接小型专用“gadget”SNARKs来构建全局SNARK，填补在CP-SNARKs通用组合、不同方案互操作以及高效专用证明系统方面的空白，从而实现灵活、可复用且高效的证明方案。

### 相关工作

[39] Groth et al. On the Size of Pairing-Based Non-interactive Arguments. **EUROCRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=On+the+Size+of+Pairing-Based+Non-interactive+Arguments)
> 核心思路：提出了近乎最优效率的配对基SNARK，证明大小为常量，验证时间与语句大小线性相关。
> 局限与区别：其承诺验证需编码进电路，且不支持与其他方案的互操作组合；LegoSNARK通过cc-SNARK和链接工具CP_link将其转化为可组合的CP-SNARK，实现5000倍加速。

[55] Parno et al. Pinocchio: Nearly Practical Verifiable Computation. **IEEE S&P 2013** [Google Scholar](https://scholar.google.com/scholar?q=Pinocchio%3A+Nearly+Practical+Verifiable+Computation)
> 核心思路：基于QAP的实用zkSNARK，证明大小和验证时间为常量。
> 局限与区别：与[39]类似，缺乏内置CP能力和互操作性；LegoSNARK的通用编译器可将其转化为与Pedersen承诺兼容的CP-SNARK。

[26] Costello et al. Geppetto: Versatile Verifiable Computation. **IEEE S&P 2015** [Google Scholar](https://scholar.google.com/scholar?q=Geppetto%3A+Versatile+Verifiable+Computation)
> 核心思路：提出了关系依赖承诺密钥的CP-SNARK，支持多QAP关系。
> 局限与区别：承诺密钥与特定关系绑定，无法实现独立生成和跨方案共享；LegoSNARK的CP-SNARK定义要求承诺密钥与关系无关，具有更强的通用性。

[68] Zhang et al. A Zero-Knowledge Version of vSQL. **ePrint 2017** [Google Scholar](https://scholar.google.com/scholar?q=A+Zero-Knowledge+Version+of+vSQL)
> 核心思路：基于多项式承诺和多变量多项式评估证明的zkSNARK，支持通用CRS。
> 局限与区别：其多项式承诺方案与本文PolyCom配合，作为构建Hadamard积、自置换等CP-SNARK的基础。

[66] Wahby et al. Doubly-Efficient zkSNARKs Without Trusted Setup. **IEEE S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Doubly-Efficient+zkSNARKs+Without+Trusted+Setup)
> 核心思路：基于GKR协议的Hyrax系统，擅长并行计算，无需可信设置。
> 局限与区别：处理共享输入的并行计算时，RDL层导致验证时间线性于电路宽度；LegoSNARK通过组合CP_lin和专用并行CP-SNARK避免了此问题。

[40] Groth et al. Updatable and Universal Common Reference Strings with Applications to zk-SNARKs. **CRYPTO 2018** [Google Scholar](https://scholar.google.com/scholar?q=Updatable+and+Universal+Common+Reference+Strings+with+Applications+to+zk-SNARKs)
> 核心思路：提出具有通用、可更新CRS的zkSNARK，但CRS与电路门数呈二次方关系。
> 局限与区别：LegoUAC通过编码电路为Hadamard积和自置换的组合，实现了线性大小的通用CRS，同时证明时间也为线性。

### 核心技术与方案
LegoSNARK框架首先形式化了commit-and-prove SNARK (CP-SNARK)的定义，将证明关系扩展为在满足承诺正确打开的前提下满足原关系。核心是组合定理：给定两个CP-SNARK（共享同一承诺方案），可以安全地构造AND组合CP-SNARK，用于证明两个子关系的合取，且子关系通过共享承诺槽位（commitment slot）连接。构造中，Prover对每个子关系分别生成证明并发送，Verifier独立验证两个子证明，若均接受则接受。该构造满足知识可靠性（源自任一子SNARK的可靠性或承诺的绑定）和零知识（利用子SNARK的模拟器）。这一组合可以迭代用于多种关系组合，如函数复合（通过AND组合实现中间结果）和析取关系（通过引入辅助变量和乘积为0的条件）。

为将现有非CP类SNARK引入框架，本文定义了commit-carrying SNARK (cc-SNARK)，其中证明本身包含一个关系依赖的承诺，且提取器可输出该承诺的打开。进一步，提出了一个“提升”编译器，将任意的cc-SNARK转化为CP-SNARK，使其与全局承诺方案Com兼容。该编译器使用一个核心CP-link工具，用于证明一个cc-SNARK生成的承诺（关系依赖的承诺）和一个Com生成的承诺（关系独立的承诺）打开到同一向量。具体构造中，新CP-SNARK的KeyGen运行cc-SNARK的KeyGen和CP-link的KeyGen，Prove首先生成cc-SNARK的证明及其承诺和打开，然后调用CP-link证明此承诺与Com承诺等同，最终证明包含两个子证明。反之，Verifier调用CP-link和cc-SNARK的验证。该编译器将cc-SNARK的零知识、知识可靠性与CP-link的相应性质结合，保证了新CP-SNARK的安全性，且证明渐近复杂度为子证明开销之和。

框架内填充了多个高效的专用CP-SNARK，均基于Pedersen向量承诺。CP-link实现为对线性子空间关系RS_M的学习论证（如Kiltz-Wee QA-NIZK方案），其中矩阵M构建自承诺键和关系键，证明验证通过配对进行，证明大小渐近为常数。CP_lin类似地处理线性关系F·u=x。此外，基于多项式承诺PolyCom（来自zk-vSQL），构建了Hadamard积（CP_had）、自置换（CP_sfprm）和矩阵乘法（CP_mm）等的CP-SNARK。这些构造利用了多项式MLE（多线性扩展）和sum-check协议，其中CP_had通过将Hadamard积等式转化为一个sum-check实例来验证，CP_sfprm使用随机性测试（Schwartz-Zippel引理）和内部积协议，CP_mm则将矩阵乘法表示为求和形式。

### 核心公式与流程

**[CP-SNARK的AND组合构造核心协议]**
$$\frac{\mathrm{CP}^{\wedge}.\mathrm{KeyGen}(\mathrm{ck},R_{R_0,R_1}^{\wedge})\to(\mathrm{ek}^*,\mathrm{vk}^*)}{\{(\mathrm{ek}_b,\mathrm{vk}_b)\leftarrow\mathrm{CP}_b.\mathrm{KeyGen}(\mathrm{ck},R_b)\}_{b\in\{0,1\}}}$$
$$\mathbf{ek}^{*}\coloneqq=(\mathbf{ek}_{b})_{b\in\{0,1\}};\mathbf{v k}^{*}\coloneqq=(\mathbf{v k}_{b})_{b\in\{0,1\}}$$
$$\frac{\mathrm{CP}^{\wedge}.\mathrm{Prove}(\mathrm{ek}^{*},x_{0},x_{1},(c_{j})_{j\in[:3]},(u_{j})_{j\in[:3]},(o_{j})_{j\in[:3]},\omega_{0},\omega_{1}):}{\{\pi_{b}\leftarrow\mathrm{CP}_{b}.\mathrm{Prove}(\mathrm{ek}_{b},x_{b},(c_{b},c_{2}),(u_{b},u_{2}),(o_{b},o_{2}),\omega_{b})\}_{b\in\{0,1\}}}$$
$$\mathrm{return}\ \pi^{*}\coloneqq=(\pi_{b})_{b\in\{0,1\}}$$
$$\frac{\mathrm{CP}^{\wedge}.\mathrm{VerProof}(\mathrm{vk}^{*},x_{0},x_{1},(c_{j})_{j\in[:3]},\pi^{*})\to b_{0}\wedge b_{1}}{\{b_{b}\leftarrow\mathrm{CP}_{b}.\mathrm{VerProof}(\mathrm{vk}_{b},x_{b},(c_{b},c_{2}),\pi_{b})\}_{b\in\{0,1\}}}$$
> 作用：展示如何将两个CP-SNARK（CP_0和CP_1）组合成一个证明AND组合关系的CP-SNARK，核心思想是子证明独立生成和验证，通过共享承诺槽位c2连接。

**[将cc-SNARK提升为CP-SNARK的编译器核心步骤（CP.Prove）]**
$$\text{CP.Prove}(\mathrm{ek},x,(c_j,u_j,o_j)_{j\in[\ell]},\omega)\to\pi:=(c',\pi^\circ,\pi')$$
$$(c',\pi',o')\leftarrow\mathrm{cc}\Pi.\mathrm{Prove}(\mathrm{ek}',x,(u_j)_{j\in[\ell]};\omega);(x^\circ,\omega^\circ):=(c',o')$$
$$\pi^\circ\leftarrow\mathrm{CP}_{\mathrm{link}}.\mathrm{Prove}(\mathrm{ek}^\circ,x^\circ,(c_j)_{j\in[\ell]},(u_j)_{j\in[\ell]},(o_j)_{j\in[\ell]},\omega^\circ)$$
> 作用：描述了通用编译器的核心步骤：首先生成一个cc-SNARK的证明π'及其相关承诺c'，然后利用CP_link工具证明该承诺c'证明新关系R°是关于cc-SNARK的承诺验证，从而将c'与原始Commitment c_j链接起来，最终证明包含c', π^°和π'。

**[CP-link基于线性子空间关系的证明构造（关键矩阵变换）]**
$$\overbrace{\left[\begin{array}{c}c_1\\\vdots\\c_\ell\\c'\end{array}\right]_1}^{[\boldsymbol{x}]_1}=
\overbrace{\left[\begin{array}{c c c c c c c c c}
h_0 & 0\dots 0 & 0 & \boldsymbol{h}_{[1,n_1]} & 0 & \dots & 0 \\
0 & h_0\dots 0 & 0 & 0 & \boldsymbol{h}_{[1,n_2]} & \dots & 0 \\
\vdots & \vdots & \ddots & \vdots & \vdots & \vdots & \ddots & \vdots \\
0 & 0\dots h_0 & 0 & 0 & 0 & \dots & \boldsymbol{h}_{[1,n_\ell]} \\
0 & 0\dots 0 & f_0 & \boldsymbol{f}_{[1,n_1]} & \boldsymbol{f}_{[n_1+1,n_2]} & \dots & \boldsymbol{f}_{[n_{\ell-1}+1,n_\ell]}
\end{array}\right]_1}^{[\mathbf{M}]_1}
\overbrace{\left(\begin{array}{c}o_1\\\vdots\\o_\ell\\o'\\\boldsymbol{u}_1\\\vdots\\\boldsymbol{u}_\ell\end{array}\right)}^{\boldsymbol{w}}$$
> 作用：展示了如何将CP_link所需证明的多个Pedersen承诺（c1...c_ℓ 和 c'）打开到相同向量（通过共享打开信息u_j和随机数o_j）的目标，转化为一个线性子空间关系R_M([x]_1, w)，从而可用QA-NIZK等知识论证高效证明。矩阵M由承诺键[ h ]_1和[ f ]_1组成。

**[CP_had构造核心：使用sum-check协议证明Hadamard积]**
$$R^{\mathrm{had}}(\boldsymbol{u}_0,\boldsymbol{u}_1,\boldsymbol{u}_2)=1\iff\forall i\in[m]:u_{0,i}=u_{1,i}\cdot u_{2,i}$$
$$\tilde{u}_0(\boldsymbol{X})=\sum_{\boldsymbol{b}\in\{0,1\}^\mu}\tilde{eq}(\boldsymbol{X},\boldsymbol{b})\cdot\tilde{u}_1(\boldsymbol{b})\cdot\tilde{u}_2(\boldsymbol{b})$$
$$g(\boldsymbol{S})=\tilde{eq}(\boldsymbol{r},\boldsymbol{S})\cdot\tilde{u}_1(\boldsymbol{S})\cdot\tilde{u}_2(\boldsymbol{S})$$
> 作用：给出Hadamard积关系定义，并说明如何通过将向量看作其多线性扩展(MLE)函数，利用MLE性质将积关系转化为一个sum-check问题。其中，随机点r由哈希函数确定，多项式g(S)是该sum-check协议中被求和的函数，它由公开的MLE of eq以及两个承诺的MLE组成。

### 实验结果
实验运行在Debian GNU/Linux虚拟机上，配备8核Xeon Gold 6154 CPU和30GB RAM，所有测试单线程执行。针对Commit-and-Prove应用，比较了LegoGro16（应用本文编译器于Groth16）与直接编码承诺到电路的CPGro16。对于向量长度n=2048，LegoGro16的proving时间（84 ms）比CPGro16（428.7 s）快约5000倍，CRS大小缩小7倍（130.6 KB vs 935 MB），但verification略慢（4.1 ms vs 3.4 ms），证明稍大（191 B vs 127 B）。在矩阵乘法任务中，LegoMM的proving时间与n²呈线性关系，当n=128时快于Groth16约1300倍（84 ms vs 109 s），verification也更快（28 ms vs 51 ms），但证明大小为32KB（对数级别）大于Groth16的常量级。在通用算术电路上，LegoAC1较Groth16表现略差，如SHA256证明中proving time慢1.2倍，verification time慢2倍。在处理共享输入的并行计算（Merkle树验证）中，LegoPar在最大9层叶子数量时proving time比HyrPoly-RDL快1.25倍，verification time快2.5倍，验证优势随规模增大。

### 局限性与开放问题
LegoSNARK现有实例化方案依赖配对基系统，需要可信设置来生成公共随机串（如PolyCom的承诺密钥），尽管部分设置可重用。未来工作可探索通过大规模MPC仪式生成通用CRS（类似于powers-of-tau方案）来减少信任假设。此外，框架内定义的组合与提升工具设计足够通用，未来可结合无需信任假设的新方案（如后量子、非配对基方案）进行实例化，以摆脱当前配对基系统的依赖。

### 强关联论文

[39] Groth et al. On the Size of Pairing-Based Non-interactive Arguments. **EUROCRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=On+the+Size+of+Pairing-Based+Non-interactive+Arguments)

[55] Parno et al. Pinocchio: Nearly Practical Verifiable Computation. **IEEE S&P 2013** [Google Scholar](https://scholar.google.com/scholar?q=Pinocchio%3A+Nearly+Practical+Verifiable+Computation)

[26] Costello et al. Geppetto: Versatile Verifiable Computation. **IEEE S&P 2015** [Google Scholar](https://scholar.google.com/scholar?q=Geppetto%3A+Versatile+Verifiable+Computation)

[49] Lipmaa et al. Prover-Efficient Commit-and-Prove Zero-Knowledge SNARKs. **AFRICACRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=Prover-Efficient+Commit-and-Prove+Zero-Knowledge+SNARKs)

[68] Zhang et al. A Zero-Knowledge Version of vSQL. **ePrint 2017** [Google Scholar](https://scholar.google.com/scholar?q=A+Zero-Knowledge+Version+of+vSQL)

[66] Wahby et al. Doubly-Efficient zkSNARKs Without Trusted Setup. **IEEE S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Doubly-Efficient+zkSNARKs+Without+Trusted+Setup)

[40] Groth et al. Updatable and Universal Common Reference Strings with Applications to zk-SNARKs. **CRYPTO 2018** [Google Scholar](https://scholar.google.com/scholar?q=Updatable+and+Universal+Common+Reference+Strings+with+Applications+to+zk-SNARKs)

[46] Kiltz et al. Quasi-Adaptive NIZK for Linear Subspaces Revisited. **EUROCRYPT 2015** [Google Scholar](https://scholar.google.com/scholar?q=Quasi-Adaptive+NIZK+for+Linear+Subspaces+Revisited)


## 关键词

+ LegoSNARK
+ 模块化设计
+ 承诺-证明
+ 简洁论证
+ 零知识证明

