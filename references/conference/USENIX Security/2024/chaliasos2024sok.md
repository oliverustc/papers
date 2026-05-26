---
title: "SoK: What Dont We Know Understanding Security Vulnerabilities in SNARKs"
标题简称:
论文类型: conference
会议简称: USENIX Security
发表年份: 2024
modified: 2025-04-17 13:44:34
created: 2025-04-13 14:50:49
---

## SoK: What Dont We Know Understanding Security Vulnerabilities in SNARKs

## 发表信息

+ [原文链接](https://www.usenix.org/conference/usenixsecurity24/presentation/chaliasos)

## 作者

+ Stefanos Chaliasos 
+ [Jens Ernstberger](Jens%20Ernstberger.md) 
+ David Theodore 
+ David Wong 
+ Mohammad Jahanara 
+ Benjamin Livshits 

## 笔记

### 背景与动机
零知识证明（ZKP）从复杂理论中的概念演变为现代密码学的核心组件，尤其是 SNARK 作为其最具实用价值的变体，已在区块链扩容（如 zkSync、Polygon zkEVM）、隐私交易（如 Zcash、Tornado Cash）以及可验证计算等场景中大规模部署。然而，现有研究高度集中在设计更高效的 SNARK 系统和提供其理论安全证明上，普遍隐含一种“SNARK 只是数学”的假设——即被数学证明正确的东西在实践中也是安全的。这种认知导致对实际系统实现中端到端安全性的系统性评估严重缺失。本文填补了这一空白：通过对 141 个真实 SNARK 漏洞的深入分析，建立了一个涵盖电路层、前端层、后端层和集成层的系统化模型，并提出了首个针对 SNARK 系统的威胁模型和漏洞分类学，揭示了跨层交互带来的复杂安全隐患，指出现实世界的 SNARK 系统绝非“只是数学”。

### 相关工作

[29] Alessandro Chiesa, Yuncong Hu, Mary Maller, Pratyush Mishra, Noah Vesely, and Nicholas Ward. Marlin: Preprocessing zksnarks with universal and updatable srs. **EUROCRYPT 2020** [Google Scholar](https://scholar.google.com/scholar?q=Marlin%3A+Preprocessing+zksnarks+with+universal+and+updatable+srs)
> 核心思路：提出了一种支持通用且可更新参考字符串的预处理 SNARK。
> 局限与区别：Marlin 侧重于协议层面的理论设计，而本文专注于分析实际部署中实现的漏洞，而非协议本身的安全性证明。

[56] Jens Groth. On the size of pairing-based noninteractive arguments. **EUROCRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=On+the+size+of+pairing-based+noninteractive+arguments)
> 核心思路：Groth16 是证明最短、验证最快的 SNARK，基于 PCP 和椭圆曲线配对。
> 局限与区别：Groth16 在实践中被广泛使用，但其非通用可组合性（non-UC）和安全实现中的陷阱是本文研究的关键对象之一。

[46] Ariel Gabizon, Zachary J Williamson, and Oana Ciobotaru. Plonk: Permutations over lagrange-bases for oecumenical noninteractive arguments of knowledge. **CRYPTO 2019** [Google Scholar](https://scholar.google.com/scholar?q=Plonk%3A+Permutations+over+lagrange-bases+for+oecumenical+noninteractive+arguments+of+knowledge)
> 核心思路：Plonk 采用了通用设置和 Plonkish 算术化。
> 局限与区别：Plonk 的理论描述不完整导致了“Frozen Heart”漏洞，本文分析了该漏洞如何从描述缺陷演变为实现中的致命错误。

[85] Shankara Pailoor, Yanju Chen, Franklyn Wang, Clara Rodríguez, Jacob Van Geffen, Jason Morton, Michael Chu, Brian Gu, Yu Feng, and Işıl Dillig. Automated detection of under-constrained circuits in zero-knowledge proofs. **PLDI 2023** [Google Scholar](https://scholar.google.com/scholar?q=Automated+detection+of+under-constrained+circuits+in+zero-knowledge+proofs)
> 核心思路：提出了 Picus 方法，通过符号执行检测 Circom 电路中的欠约束问题。
> 局限与区别：Picus 仅针对 Circom 语言，且依赖 SMT 求解器在有限域算术上存在性能瓶颈；本文则覆盖了整个 SNARK 栈的多种语言和漏洞类型。

[105] Hongbo Wen, Jon Stephens, Yanju Chen, Kostas Ferles, Shankara Pailoor, Kyle Charbonnet, Isil Dillig, and Yu Feng. Practical security analysis of zero-knowledge proof circuits. **Cryptology ePrint Archive 2023** [Google Scholar](https://scholar.google.com/scholar?q=Practical+security+analysis+of+zero-knowledge+proof+circuits)
> 核心思路：提出了 ZKAP 工具，通过静态分析识别 Circom 电路中的常见漏洞。
> 局限与区别：ZKAP 的检测范围受限于预定义规则，且同样仅适用于 Circom；本文的漏洞分类更全面，覆盖了前端编译器和后端协议实现层。

[60] Miguel Isabel, Clara Rodríguez-Núñez, and Albert Rubio. Scalable verification of zero-knowledge protocols. **SP 2024** [Google Scholar](https://scholar.google.com/scholar?q=Scalable+verification+of+zero-knowledge+protocols)
> 核心思路：提出了 CIVER，基于变换和演绎规则进行模块化验证。
> 局限与区别：CIVER 主要针对 Circom 电路的前置和后置条件，本文则分析了集成层和协议层的漏洞，而这些层是形式化验证工具的盲区。

[36] Quang Dao, Jim Miller, Opal Wright, and Paul Grubbs. Weak fiat-shamir attacks on modern proof systems. **ePrint 2023** [Google Scholar](https://scholar.google.com/scholar?q=Weak+fiat-shamir+attacks+on+modern+proof+systems)
> 核心思路：系统化了“Frozen Heart”攻击，即 Fiat-Shamir 变换中因遗漏部分公开输入而产生的漏洞。
> 局限与区别：该工作聚焦于攻击的通用模式；本文将其作为后端和证明系统层漏洞的典型案例，并提供了更广泛的漏洞数据集。

[84] Alex Ozdemir, Riad S Wahby, Fraser Brown, and Clark Barrett. Bounded verification for finite-field-blasting (in a compiler for zero knowledge proofs). **ePrint 2023** [Google Scholar](https://scholar.google.com/scholar?q=Bounded+verification+for+finite-field-blasting+(in+a+compiler+for+zero+knowledge+proofs))
> 核心思路：部分验证了 CirC 编译器中的关键编译 pass，以防范编译器引入漏洞。
> 局限与区别：该工作仅针对编译器前端的一个有限子集，而本文揭示了前端和编译层缺陷的多样性。

[82] Alex Ozdemir, Fraser Brown, and Riad S Wahby. Circ: Compiler infrastructure for proof systems, software verification, and more. **SP 2022** [Google Scholar](https://scholar.google.com/scholar?q=Circ%3A+Compiler+infrastructure+for+proof+systems%2C+software+verification%2C+and+more)
> 核心思路：CirC 提供了一个语言无关的中间表示（IR），支持多种 DSL 编译到此 IR。
> 局限与区别：CirC 本身是基础设施，不提供漏洞检测；本文强调了基于此 IR 进行跨 DSL 静态分析的潜力，并指出了当前工具的不足。

[50] Rosario Gennaro, Craig Gentry, Bryan Parno, and Mariana Raykova. Quadratic span programs and succinct nizks without pcps. **EUROCRYPT 2013** [Google Scholar](https://scholar.google.com/scholar?q=Quadratic+span+programs+and+succinct+nizks+without+pcps)
> 核心思路：提出了 R1CS 算术化及基于 QSP 的 SNARK。
> 局限与区别：该工作奠定了 SNARK 的数学基础，本文则探讨了这些基础在实际实现中如何被误用或错误实现。

### 核心技术与方案

本文的核心贡献在于建立了一个 SNARK 系统安全性分析的系统化框架，而非提出一个新的 SNARK 协议。该框架由三个相互关联的维度构成：系统模型、威胁模型和漏洞分类。

**系统模型**将典型的 SNARK 应用自顶向下划分为四个层次。电路层使用 DSL（如 Circom）或 eDSL（如 gnark）描述待证明的计算逻辑，开发者必须区分“赋值”与“约束”，这是欠约束漏洞的根源。前端层由编译器和算术化模块组成，将高层电路描述编译为 R1CS、Plonkish 或 AIR 等中间表示。后端层实现了具体的证明系统算法，执行 Setup、Prove 和 Verify 三个核心函数。集成层涵盖与 SNARK 交互的应用逻辑，如智能合约对公共输入的验证、nullifier 管理等。

**威胁模型**定义了三种对抗角色：网络对抗者 $R_1$ 能窃听公开消息并利用证明的可延展性；恶意用户 $R_2$ 拥有对证明器的预言机访问，可尝试拒绝服务攻击；恶意证明者 $R_3$ 掌握所有输入并试图破坏可靠性。漏洞的影响被分为三类：打破可靠性、打破完备性、打破零知识。该模型的一个关键洞察是，可靠性漏洞的严重性最高，因为恶意证明者可以利用其生成伪造证据，导致系统产生灾难性后果。

**漏洞分类与根因分析**基于对 141 个漏洞数据的统计，揭示了电路层是漏洞最密集的层次，占 99 个（70.2%），其中 95 个打破可靠性。电路层最主要的漏洞类型是欠约束，其根因包括“已赋值但未约束”（14 个）、“缺失输入约束”（25 个）、“不安全重用电路模板”（9 个）以及“逻辑到约束的错误转换”（32 个）。特别地，后者源于将传统编程逻辑翻译为有限域 $\mathbb{F}_p$ 上的算术电路时，开发者因不熟悉无分支、无类型约束的编程范式而遗漏关键约束。例如，实现条件分支时使用选择器（multiplexer）若未约束所有分支输出，则攻击者可输入任意值。集成层漏洞（13 个）主要源于传递未检查数据，即电路期望的隐式约束在应用端未被强制执行。后端层漏洞（23 个）以“不安全验证器”为主（16 个），通常源于 Fiat-Shamir 变换实现不全（如省略部分公开输入）或椭圆曲线点校验缺失。

**防御分析**评估了现有工具：Picus 通过符号执行检测欠约束但限于 Circom 且受 SMT 求解器性能限制；Circomspect 和 ZKAP 依赖静态分析规则，检测范围有限；CIVER 的模块化验证方法有潜力但尚未覆盖整个栈。重要的发现是：在调查的 75 份审计报告中，仅有 5 份使用了 SNARK 专用工具，说明了防御工具的覆盖率严重不足。

### 核心公式与流程

**[SNARK 三元组定义]**
$$Setup(pp) \to (pk, vk)$$
$$Prove(pk, x, w) \to \pi$$
$$Verify(vk, x, \pi) \to \{0, 1\}$$
> 作用：定义了 SNARK 系统的三个核心算法，是后续所有安全性讨论的基础。Setup 基于公共参数生成证明密钥和验证密钥，Prove 由证明者使用私密输入生成证据，Verify 由验证者验证证据的有效性。

**[欠约束漏洞的数学表现]**
$$C(x, w) = y \quad \text{但} \quad C'(x, w') = y \quad \forall w' \neq w$$
> 作用：描述了欠约束漏洞的实质——电路约束方程组存在自由度，使得攻击者可在不改变公共输出的前提下任意选择私密赋值。图中关于 MiMC 哈希模板的示例展示了这种漏洞的典型代码模式：赋值操作 `<-` 未伴随约束操作 `===`，导致信号未被纳入 R1CS 方程。

**[Frozen Heart 攻击的根因数学表达]**
$$challenge = H(partial\_transcript) \quad \text{而非} \quad H(full\_transcript)$$
> 作用：描述了一种特定的 Fiat-Shamir 实现错误——哈希函数只对部分协议交互记录进行摘要，使得攻击者可以调整未哈希的部分进行重放攻击，从而伪造证明。该漏洞源于理论描述中省略了“全部公开输入”这一关键细节。

### 实验结果

本文的实验并非传统意义上的性能基准测试，而是对 141 个漏洞数据的统计分析。主要结果如下：电路层漏洞数量最多（99 个，占 70.2%），其中 95 个（96%）破坏可靠性。在这 95 个可靠性漏洞中，根因分布为：已赋值但未约束 14 个、缺失输入约束 25 个、不安全重用电路模板 9 个、逻辑翻译错误 32 个、算术域错误 8 个。集成层漏洞共 13 个，其中缺失验证输入占 10 个。后端层漏洞共 23 个，不安全验证器占 16 个。在漏洞来源方面，安全审计报告贡献了 101 个漏洞，漏洞披露报告 16 个，问题跟踪器 24 个。防御工具覆盖率极低——在 75 份审计报告中仅 5 份使用了专用工具。所有漏洞都来自 2018 年至 2024 年间公开的系统，包括 zkSync、Polygon zkEVM、Scroll、Zcash、Tornado Cash、Aztec 等主流 SNARK 项目。实验结论强有力地证实了 SNARK 系统安全问题的普遍性和严重性，尤其是电路层的欠约束漏洞构成了最大威胁。

### 局限性与开放问题
本文的漏洞数据完全依赖于公开可获得的报告，可能存在选择的系统性偏差：更容易被发现和公开的漏洞（如欠约束）被过度代表，而一些难以检测或未被发现的漏洞类别可能被低估。此外，对于许多报告的漏洞，缺乏概念验证利用代码，导致难以精确评估其实际的可利用性和严重性。跨层交互引发的复杂漏洞（如集成层中因传递未检查数据而绕过后端安全性质的漏洞）目前几乎没有有效的自动化检测工具，这是一个重要的开放研究方向。

### 强关联论文

[46] Ariel Gabizon, Zachary J Williamson, and Oana Ciobotaru. Plonk: Permutations over lagrange-bases for oecumenical noninteractive arguments of knowledge. **EUROCRYPT 2019** [Google Scholar](https://scholar.google.com/scholar?q=Plonk%3A+Permutations+over+lagrange-bases+for+oecumenical+noninteractive+arguments+of+knowledge)

[56] Jens Groth. On the size of pairing-based noninteractive arguments. **EUROCRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=On+the+size+of+pairing-based+noninteractive+arguments)

[29] Alessandro Chiesa, Yuncong Hu, Mary Maller, Pratyush Mishra, Noah Vesely, and Nicholas Ward. Marlin: Preprocessing zksnarks with universal and updatable srs. **EUROCRYPT 2020** [Google Scholar](https://scholar.google.com/scholar?q=Marlin%3A+Preprocessing+zksnarks+with+universal+and+updatable+srs)

[85] Shankara Pailoor, Yanju Chen, Franklyn Wang, Clara Rodríguez, Jacob Van Geffen, Jason Morton, Michael Chu, Brian Gu, Yu Feng, and Işıl Dillig. Automated detection of under-constrained circuits in zero-knowledge proofs. **PLDI 2023** [Google Scholar](https://scholar.google.com/scholar?q=Automated+detection+of+under-constrained+circuits+in+zero-knowledge+proofs)

[36] Quang Dao, Jim Miller, Opal Wright, and Paul Grubbs. Weak fiat-shamir attacks on modern proof systems. **ePrint 2023** [Google Scholar](https://scholar.google.com/scholar?q=Weak+fiat-shamir+attacks+on+modern+proof+systems)

[50] Rosario Gennaro, Craig Gentry, Bryan Parno, and Mariana Raykova. Quadratic span programs and succinct nizks without pcps. **EUROCRYPT 2013** [Google Scholar](https://scholar.google.com/scholar?q=Quadratic+span+programs+and+succinct+nizks+without+pcps)

[82] Alex Ozdemir, Fraser Brown, and Riad S Wahby. Circ: Compiler infrastructure for proof systems, software verification, and more. **SP 2022** [Google Scholar](https://scholar.google.com/scholar?q=Circ%3A+Compiler+infrastructure+for+proof+systems%2C+software+verification%2C+and+more)

[105] Hongbo Wen, Jon Stephens, Yanju Chen, Kostas Ferles, Shankara Pailoor, Kyle Charbonnet, Isil Dillig, and Yu Feng. Practical security analysis of zero-knowledge proof circuits. **ePrint 2023** [Google Scholar](https://scholar.google.com/scholar?q=Practical+security+analysis+of+zero-knowledge+proof+circuits)

[60] Miguel Isabel, Clara Rodríguez-Núñez, and Albert Rubio. Scalable verification of zero-knowledge protocols. **SP 2024** [Google Scholar](https://scholar.google.com/scholar?q=Scalable+verification+of+zero-knowledge+protocols)

[84] Alex Ozdemir, Riad S Wahby, Fraser Brown, and Clark Barrett. Bounded verification for finite-field-blasting (in a compiler for zero knowledge proofs). **ePrint 2023** [Google Scholar](https://scholar.google.com/scholar?q=Bounded+verification+for+finite-field-blasting+(in+a+compiler+for+zero+knowledge+proofs))


## 关键词

+ SNARKs安全漏洞分类
+ 零知识证明实现安全
+ SNARK实现端到端安全
+ 141漏洞分析分类体系
+ ZKP系统威胁模型
+ SNARK防御机制评估
