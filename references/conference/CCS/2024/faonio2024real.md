---
title: "Real-world Universal zkSNARKs are non-malleable"
doi: 10.1145/3658644.3690351
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2024
created: 2025-04-16 09:58:38
modified: 2025-04-16 09:58:55
---
## Real-world Universal zkSNARKs are non-malleable

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3658644.3690351)

## 作者

+ Antonio Faonio 
+ [Dario Fiore](Dario%20Fiore.md)
+ Luigi Russo 

## 笔记

### 背景与动机
零知识证明是密码学核心工具，而zkSNARKs实现了证明的简洁性与非交互性，成为可扩展且保护隐私的分布式系统的关键组件。这些方案的基本安全属性是知识可靠性，它要求一个能生成有效证明的证明者必须拥有对应的证据。然而，Sahai等人早期指出，知识可靠性无法抵抗攻击者利用事先观察到的合法证明来伪造其他证明的威胁，并因此引入了模拟可靠性概念，后来发展为更强的模拟可提取性。对于zkSNARKs的模拟可提取性研究，Groth和Maller在2017年提出了首个架构，但其方案基于单一电路的特定设置，而新一代的通用zkSNARKs则允许初始设置复用于任意电路，实用性更强。尽管近年取得了显著进展，但大量方案仍缺乏模拟可提取性的安全证明。Faonio等人和Kohlweiss等人于2023年分别提出了能够覆盖基于多项式交互式预言机和多项式承诺的zkSNARKs的通用模拟可提取性归约框架。然而，这两个框架均存在两个关键缺口：第一，实际部署的PLONK和Marlin版本采用了线性化技巧等优化以提升效率，但这些优化改变了验证算法，超出了原有框架的安全分析范围；第二，原有框架要求PIOP中与证据相关的多项式必须在最后一轮随机挑战上求值，但Marlin和Lunar等方案中，这部分多项式是在最后一轮之前的、与证据无关的挑战上求值，这被称为委托阶段，原有框架无法捕获。本文旨在填补这两项缺口，首次证明PLONK、Marlin、Lunar和Basilisk的“真实世界”优化版本满足模拟可提取性。

### 相关工作

[CHM+20] Chiesa等. Marlin: Preprocessing zkSNARKs with Universal and Updatable SRS. **EUROCRYPT 2020** [Google Scholar](https://scholar.google.com/scholar?q=Marlin+Preprocessing+zkSNARKs+with+Universal+and+Updatable+SRS)
> 核心思路：提出了一种具有预处理的通用可更新SRS的zkSNARK，其PIOP设计包含一个独立的委托阶段以支持简洁验证。
> 局限与区别：本文指出该方案因存在委托阶段，超出了FFK+23框架的安全适用范围；本文通过引入委托阶段的安全条件，首次证明了其实际部署版本的模拟可提取性。

[FFK+23] Faonio等. From Polynomial IOP and Commitments to Non-Malleable zkSNARKs. **TCC 2023** [Google Scholar](https://scholar.google.com/scholar?q=From+Polynomial+IOP+and+Commitments+to+Non-Malleable+zkSNARKs)
> 核心思路：提出了一个基于PIOP和多项式承诺编译zkSNARKs的通用模拟可提取性框架。
> 局限与区别：该框架仅适用于PLONK和Marlin的“教科书”版本，无法覆盖采用线性化技巧优化的实际版本，也无法处理包含委托阶段的PIOP。

[GWC19] Gabizon等. PLONK: Permutations over Lagrange-bases for Oecumenical Noninteractive Arguments of Knowledge. **ePrint 2019** [Google Scholar](https://scholar.google.com/scholar?q=PLONK+Permutations+over+Lagrange-bases+for+Oecumenical+Noninteractive+Arguments+of+Knowledge)
> 核心思路：提出了一个高效的通用zkSNARK方案，通过在PIOP编译中使用线性化技巧来减少证明中的域元素数量。
> 局限与区别：该工作提出的线性化技巧在论文中缺乏形式化的安全性证明；本文首次为此优化提供了正式的安全分析，并给出了使其安全的必要充分条件。

[KPT23] Kohlweiss等. How to Compile Polynomial IOP into Simulation-Extractable SNARKs: A Modular Approach. **TCC 2023** [Google Scholar](https://scholar.google.com/scholar?q=How+to+Compile+Polynomial+IOP+into+Simulation-Extractable+SNARKs+A+Modular+Approach)
> 核心思路：独立于FFK+23，提出了一种类似的PIOP-to-zkSNARK模块化编译框架，并证明了模拟可提取性。
> 局限与区别：与FFK+23相同，该框架也无法处理线性化技巧优化和包含委托阶段的PIOP。

[GM17] Groth等. Snarky Signatures: Minimal Signatures of Knowledge from Simulation-Extractable SNARKs. **CRYPTO 2017** [Google Scholar](https://scholar.google.com/scholar?q=Snarky+Signatures+Minimal+Signatures+of+Knowledge+from+Simulation-Extractable+SNARKs)
> 核心思路：首次研究了zkSNARK的模拟可提取性，提出了一个基于配对的构造及其在简洁知识签名中的应用。
> 局限与区别：该方案是第一代方案，需要为单个电路进行可信设置，不具备通用性。本文的工作是针对更灵活、通用的zkSNARKs。

[LPS23] Lipmaa等. Algebraic Group Model with Oblivious Sampling. **TCC 2023** [Google Scholar](https://scholar.google.com/scholar?q=Algebraic+Group+Model+with+Oblivious+Sampling)
> 核心思路：提出了一个扩展的代数群模型，其中敌手可以获取其代数表示未知的“遗忘采样”群元素，并展示了线性化技巧在这种模型下的一个攻击实例。
> 局限与区别：该工作指出了线性化技巧的安全性风险，而本文则在此基础上进一步研究了使其安全的条件，并给出了正式的安全证明。

### 核心技术与方案

本文的主要贡献在于解决了将通用zkSNARKs (如PLONK, Marlin) 编译为模拟可提取方案的现有理论框架与实际部署版本之间的两大缺口：线性化技巧和委托阶段。

**1. KZG承诺的模拟可提取性：** 首先，本文着重于地基——KZG多项式承诺方案的评估证明。Faonio等人先前的工作证明了KZG在一种“半自适应”策略和若干约束下的模拟可提取性。本研究大幅简化并泛化了该策略。具体来说，它移除了两条关键约束：(a) 评估点必须是预先固定的集合（点检查），和 (b) 模拟查询中的承诺不能代数地依赖此前获得的模拟证明。移除约束 (a) 允许在不可编程随机预言机模型中证明编译器的安全性，但这依赖于一个更强的新假设：One-More q-SDH (OMSDH) 假设。该假设允许敌手查询形如 $\left[ (s - x)^{-i} \right]_1$ 的元素。论文证明了非自适应版本的OMSDH可以归约到标准的q-SDH假设，并且在通用群模型中证明了OMSDH本身的安全性。此外，策略被泛化，允许伪造的承诺是其他承诺的线性组合（即线性化承诺）。这一泛化使得安全性证明可以覆盖线性化技巧。最终得到的KZG方案在代数群模型中满足策略性的模拟可提取性。

**2. 线性化技巧的模拟可提取性：** 在KZG基础上，本文形式化了线性化技巧，将其构建为一个用于关系 $\mathcal{R}_{\text{lin}}$ 的CP-SNARK，其核心是证明 $\sum_i A_i(x) B_i(x) = y$，其中 $A_i$ 是 $x$ 和核心多项式 $C_j$ 的函数。本文证明，要使线性化技巧是模拟可提取的，单纯要求多项式 $A_i$ 线性独立是不够的，因为敌手可以利用证明来“降级”一个不可提取的多项式的度数。例如，如果敌手获得一个关于证据 $c$ 在点0处的模拟证明 $\pi = c/s$，它可以构造 $A_1=1, A_2=-X$ 并设置 $B_1$ 和 $B_2$ 的承诺为 $(c, \pi)$。尽管 $A_1, A_2$ 线性独立，但 $A_1$ 和 $A_2(X)/X$ 却不独立，导致攻击成功。因此，本文提出了更强的“$\nu$-独立”概念：对于所有阶数不超过 $\nu$ 的系数多项式 $\alpha_i(X)$，满足 $\sum_i \alpha_i A_i \neq 0$。这里的 $\nu$ 被定义为“最高嵌套层数”，它刻画了敌手在模拟查询中利用遗忘采样元素和先前证明构造新证明的链长度。直觉上，该参数 $\nu$ 限制了对证明进行“再证明”的次数，从而限制了不可提取“伪多项式”分母的最高次数。最终，本文证明，在简化且泛化的策略下，当提取出的 $A_i$ 多项式是 $\nu$-独立且敌手达到的最高嵌套层数不超过 $\nu$ 时，线性化技巧满足策略性的模拟可提取性。

**3. 捕获带有委托阶段的PIOP：** 在PIOP层面，Faonio等人曾要求PIOP具有一个“证据依赖的最后一轮”，但Marlin等方案包含一个与证据无关的“委托阶段”，用于实现验证的简洁性，这使其不满足该条件。本文因此扩展了PIOP的定义，允许一个独立的委托阶段，并给出了新的编译安全条件。对于这类PIOP，关键要求是：(1) 委托阶段发送的多项式承诺必须使用确定性承诺（即不发随机数）；(2) 在PIOP层面，委托阶段必须具有唯一性，即一旦修复了之前所有轮次的消息，任何恶意证明者在委托阶段只能发送唯一的答案。基于这些条件，本文证明了可以安全地将带有委托阶段的PIOP编译成带有线性化技巧优化的模拟可提取的CP-SNARK。在归约中，参数 $\nu$ 可以被控制得很低，因为归约为每个模拟查询新鲜采样承诺，从而将证明的最大嵌套层数限制在单个PIOP执行所需的评估轮数以内。最终，论文展示了PLONK和Marlin满足这些要求，从而推导出它们在实际部署下的模拟可提取性。

### 核心公式与流程

**[One-More q-SDH 假设 (OMSDH)]**
$$ \mathbf{Adv}_{\text{GroupGen}, \mathcal{A}}^{(n,d)-\text{OMSDH}}(\lambda) := \Pr\left[ \mathbf{Exp}_{\text{GroupGen}, \mathcal{A}}^{(n,d)-\text{OMSDH}}(\lambda) = 1 \right] $$
> 作用：定义了本文所依赖的新型密码学假设。该假设通过一个预言机 $\mathcal{O}_s(x, i)$ 提供形如 $[(s-x)^{-i}]_1$ 的元素，比标准SDH假设更灵活，是证明KZG评估模拟可提取性（完全自适应策略）的关键。

**[嵌套层数 $\nu_\pi(j,k)$ 定义]**
$$ \nu_{\pi}(j, k) := \max_{i: o_i \neq 0 \land \nu_{\pi_i}(j, k) \neq 0} \left\{\nu_{\pi_i}(j, k) + b_k\right\} \cup \left\{b_{j, k}\right\} $$
> 作用：量化了在一个模拟的KZG评估证明中，用于构造该证明的某个遗忘采样承诺 $c_j$ 被“嵌套在证明链”中的次数。参数 $\bar{\nu}$（所有 $\nu_\pi(j,k)$ 之和的最大值）是分析线性化技巧安全性的一个关键约束，用于确定 $\nu$-独立参数的界。

**[线性化技巧的CP-SNARK `Π_lin` 验证算法]**
$$ \text{Verify}_{\text{lin}}(\mathsf{vk}, \mathbb{x}, \pi): $$
$$ \mathsf{r} \leftarrow \sum_{i} G_i((y_j)_{j}, x) \mathsf{b}_i $$
$$ \text{Output } \text{Verify}_{\text{m-evl}}(\mathsf{vk}, \mathbb{x}_{\text{m-evl}}, \pi_{\text{m-evl}}) $$
> 作用：该算法描述了如何利用KZG的同态性质，通过仅打开核心多项式 $C_j$ 在点 $x$ 上的值 $y_j$，并结合实例中给出的承诺 $\mathsf{b}_i$，聚合性地验证 $\sum_i A_i(x)B_i(x) = y$，从而减少证明中的域元素数量，是实际部署优化的核心。

**[PIOP-to-zkSNARK编译器的验证流程]**
$$ \rho_i \gets \mathsf{RO}(\mathsf{vk}_{\mathfrak{i}}, \mathbb{x}, \bar{\pi}_1, \ldots, \bar{\pi}_i) $$
$$ \{\hat{\mathbb{x}}_k\}_k \gets \mathsf{V}(\mathbb{F}, \mathbb{x}, \boldsymbol{\pi}, \boldsymbol{\rho}) $$
$$ \text{return } \bigwedge_{k\in [n_e]} \mathsf{Verify}_{\text{lin}}(\mathsf{srs}, \mathbb{x}_k, \pi_k) $$
> 作用：该流程展示了编译器如何通过Fiat-Shamir变换将交互式PIOP转换为非交互式zkSNARK，并最终使用 `Π_lin` 来验证所有由PIOP校验器 $\mathsf{V}$ 生成的检查 $\hat{\mathbb{x}}_k$。

### 实验结果
本文是理论性工作，主要贡献是安全性证明与表格式的比较分析。实验部分并未提供，但论文在介绍部分和表1中对其结果与基线方法进行了定性比较。核心对比对象是FFK+23和KPT23的理论框架。论文指出，这些先前框架只能证明“教科书”版本的PLONK和Marlin的模拟可提取性，而本文的结果首次覆盖了包含所有标准优化技巧（即线性化技巧和委托阶段）的“真实世界”部署版本。具体而言，通过表1的对比，本文所采用的策略在约束条件上（半自适应和自适应）更为宽松，其自适应策略虽然依赖于更强的OMSDH假设，但消除了先前工作中的“点检查”和“承诺检查”约束，使得安全证明的范围更加广泛，能够处理更复杂的攻击场景。这一理论突破的意义在于，它首次为当前在实践中广泛使用的高效zkSNARK库提供了形式化的安全性理论支撑，弥合了理论与实践之间的安全性鸿沟。

### 局限性与开放问题
本文的证明依赖于新引入的One-More q-SDH假设，虽然作者在通用群模型中论证了其安全性，但其标准模型下的可靠性以及具体的参数化（n和d）如何影响安全性仍需进一步研究。将线性化技巧的安全性条件（多项式$\nu$-独立性和嵌套层数$\nu$）关联到具体的PIOP协议时，需要逐案分析，是否所有采用此优化的方案都能无缝适用尚需验证。此外，本文的工作主要基于AGM和RO模型，将结果推广到更弱的假设或标准模型是未来的重要方向。对于更复杂的PIOP结构，以及如何处理非KZG的其他多项式承诺方案中的类似优化，本文并未给出通用答案。

### 强关联论文

[FFK+23] Faonio et al. From Polynomial IOP and Commitments to Non-Malleable zkSNARKs. **TCC 2023** [Google Scholar](https://scholar.google.com/scholar?q=From+Polynomial+IOP+and+Commitments+to+Non-Malleable+zkSNARKs)

[KPT23] Kohlweiss et al. How to Compile Polynomial IOP into Simulation-Extractable SNARKs: A Modular Approach. **TCC 2023** [Google Scholar](https://scholar.google.com/scholar?q=How+to+Compile+Polynomial+IOP+into+Simulation-Extractable+SNARKs+A+Modular+Approach)

[GM17] Groth et al. Snarky Signatures: Minimal Signatures of Knowledge from Simulation-Extractable SNARKs. **CRYPTO 2017** [Google Scholar](https://scholar.google.com/scholar?q=Snarky+Signatures+Minimal+Signatures+of+Knowledge+from+Simulation-Extractable+SNARKs)

[LPS23] Lipmaa et al. Algebraic Group Model with Oblivious Sampling. **TCC 2023** [Google Scholar](https://scholar.google.com/scholar?q=Algebraic+Group+Model+with+Oblivious+Sampling)

[GWC19] Gabizon et al. PLONK: Permutations over Lagrange-bases for Oecumenical Noninteractive Arguments of Knowledge. **ePrint 2019** [Google Scholar](https://scholar.google.com/scholar?q=PLONK+Permutations+over+Lagrange-bases+for+Oecumenical+Noninteractive+Arguments+of+Knowledge)

[CHM+20] Chiesa et al. Marlin: Preprocessing zkSNARKs with Universal and Updatable SRS. **EUROCRYPT 2020** [Google Scholar](https://scholar.google.com/scholar?q=Marlin+Preprocessing+zkSNARKs+with+Universal+and+Updatable+SRS)

[CFF+21] Campanelli et al. Lunar: A Toolbox for More Efficient Universal and Updatable zkSNARKs and Commit-and-Prove Extensions. **ASIACRYPT 2021** [Google Scholar](https://scholar.google.com/scholar?q=Lunar+A+Toolbox+for+More+Efficient+Universal+and+Updatable+zkSNARKs+and+Commit-and-Prove+Extensions)


## 关键词

+ 零知识证明
+ 模拟可提取性
+ zkSNARK
+ PLONK
+ Marlin
+ 非交互式证明