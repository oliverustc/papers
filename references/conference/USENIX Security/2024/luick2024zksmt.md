---
title: "ZKSMT: A VM for Proving SMT Theorems in Zero Knowledge"
标题简称:
论文类型: conference
会议简称: USENIX Security
发表年份: 2024
modified: 2025-04-11 10:21:54
---

## ZKSMT: A VM for Proving SMT Theorems in Zero Knowledge

## 发表信息

+ [原文链接](https://www.usenix.org/conference/usenixsecurity24/presentation/luick)

## 作者

+ Daniel Luick
+ John C. Kolesar
+ [Timos Antonopoulos](Timos%20Antonopoulos.md)
+ William R. Harris
+ James Parker
+ [Ruzica Piskac](Ruzica%20Piskac.md)
+ [Eran Tromer](Eran%20Tromer.md)
+ [Xiao Wang](Xiao%20Wang.md)
+ [Ning Luo](Ning%20Luo.md)

## 笔记

### 背景与动机
程序安全验证通常可归约为可满足性模理论（SMT）公式的不可满足性判定，但传统的验证过程要求所有信息完全公开，这阻碍了包含知识产权的私有程序的验证。零知识证明允许验证者在不泄露公式或证明本身的前提下确认SMT公式的有效性，是实现隐私保护程序安全证明的关键构件。然而，现有零知识协议如ZKUNSAT仅支持纯布尔逻辑，无法处理程序验证中广泛使用的一阶理论与线性整数算术等更丰富的理论。另一方面，将通用零知识虚拟机如Cheesecloth运行SMT证明验证器，其开销极大：最短的基准测试（仅6步）耗时接近两小时，因为通用VM需模拟冯·诺依曼架构、支持随机访存且无法利用理论特定的优化。因此，亟需一个紧凑、可扩展且与零知识优化兼容的框架，能够模块化地支持多种SMT理论，并允许为不同规则定制高效的零知识协议。

### 相关工作

[42] Luo et al. Proving UNSAT in zero knowledge. **CCS 2022** [Google Scholar](https://scholar.google.com/scholar?q=Proving+UNSAT+in+zero+knowledge)
> 核心思路：提出了ZKUNSAT，一个在零知识中验证命题逻辑不可满足性的协议，仅支持合取范式下的一种解析规则。
> 局限与区别：ZKUNSAT严格限于命题逻辑，无法处理一阶理论如等式与线性算术；本文ZKSMT扩展至一阶逻辑，支持多规则、动态表达式表，并利用多项式承诺实现高效的多重集检查。

[15] Cuéllar et al. Cheesecloth: Zero-Knowledge proofs of real world vulnerabilities. **USENIX Security 2023** [Google Scholar](https://scholar.google.com/scholar?q=Cheesecloth+Zero-Knowledge+proofs+of+real+world+vulnerabilities)
> 核心思路：Cheesecloth是一个通用零知识证明工具，将LLVM程序编译为ZKP电路进行验证。
> 局限与区别：通用VM需对所有指令和内存操作进行混淆执行，开销巨大；本文ZKSMT针对SMT验证设计专用VM，避免通用性损失，实现了三个数量级的加速。

[6] Baum et al. Mac’n’cheese: Zero-knowledge proofs for boolean and arithmetic circuits with nested disjunctions. **Crypto 2021** [Google Scholar](https://scholar.google.com/scholar?q=Mac%27n%27cheese+Zero-knowledge+proofs+for+boolean+and+arithmetic+circuits+with+nested+disjunctions)
> 核心思路：提出基于VOLE的零知识证明系统，支持布尔与算术电路，并允许嵌套析取。
> 局限与区别：该协议作为底层后端用于Cheesecloth；本文ZKSMT使用同类VOLE-ZK协议，但通过分组检查等定制优化实现更高效率。

[22] Galois, Inc. swanky: A suite of rust libraries for secure computation. 2019 [Google Scholar](https://scholar.google.com/scholar?q=swanky+A+suite+of+rust+libraries+for+secure+computation)
> 核心思路：实现了Diet Mac’n’cheese等零知识证明库。
> 局限与区别：本文ZKSMT在评估中将其作为baseline的一部分，但最终采用EMP-toolkit实现。

[14] Christ et al. SMTInterpol: An interpolating SMT solver. **SPIN 2012** [Google Scholar](https://scholar.google.com/scholar?q=SMTInterpol+An+interpolating+SMT+solver)
> 核心思路：SMTInterpol是一个支持插值生成的SMT求解器，可输出证明证书。
> 局限与区别：本文使用SMTInterpol生成命题证明，并编译为ZKSMT格式；SMTInterpol本身不提供零知识属性。

[32] Hoenicke and Schindler. A simple proof format for SMT. **SMT Workshop 2022** [Google Scholar](https://scholar.google.com/scholar?q=A+simple+proof+format+for+SMT)
> 核心思路：提出一种简化的SMT证明格式，供SMTInterpol使用。
> 局限与区别：本文利用该格式作为桥梁，将SMTInterpol输出转换为ZKSMT输入。

[5] Barnett et al. Boogie: A modular reusable verifier for object-oriented programs. **FMCO 2005** [Google Scholar](https://scholar.google.com/scholar?q=Boogie+A+modular+reusable+verifier+for+object-oriented+programs)
> 核心思路：Boogie是一个程序验证工具链，可生成SMT验证条件。
> 局限与区别：本文使用Boogie测试套件生成的SMT公式作为基准，但Boogie本身不涉及零知识。

[1] SMT-LIB: The Satisfiability Modulo Theories Library - Benchmarks [Google Scholar](https://scholar.google.com/scholar?q=SMT-LIB+The+Satisfiability+Modulo+Theories+Library+Benchmarks)
> 核心思路：SMT-LIB提供标准化的SMT基准测试集。
> 局限与区别：本文使用其中Wisconsin Safety Analyzer子集进行压力测试。

### 核心技术与方案

**整体架构**  
ZKSMT 的核心是一个专门为 SMT 证明验证设计的虚拟机。它将 SMT 公式的所有 AST 节点存储在只读的表达式表 $M_e$ 中，将证明步骤存储在只读的步骤表 $M_p$ 中。主验证循环按检查顺序（可以是逻辑顺序的任意排列）迭代处理每个证明步骤，依次执行五个阶段：步骤获取、结论获取、前提获取、规则检查、循环检查（确保前提 StepID 小于当前 StepID）。校验通过后，将 StepID 记录在数组 $D$ 中，最后对 $D$ 进行置换检查，确保所有步骤都被恰好验证一次。这种结构类似于冯·诺依曼处理器，但指令集（规则检查指令）是针对 SMT 理论定制的。

**表达式与证明的编码**  
每个表达式通过 NodeID（操作符）、ImmAddr（常量和变量名）以及 IndAddr（子表达式索引列表）表示，长度固定为 $\alpha$（通过填充）。每个证明步骤包含 StepID、RuleID、Premises（前提步骤ID列表，长度固定为 $\mu$）以及 Result（结论在 $M_e$ 中的索引）。这种编码方式使得表达式引用可以在零知识中通过索引相等来判断，而非遍历整个 AST。

**零知识实例化**  
ZKSMT 使用 read-only memory (ROM) 协议 [17,20,30] 来从 $M_e$ 和 $M_p$ 中根据承诺的地址读取数据。为保证隐私，采用分组检查（Group Checking）：所有使用同一规则的证明步骤被集中验证，从而避免了对不同规则进行多路复用，仅调用对应的检查指令。分组检查会泄露每种规则的使用次数，但隐藏了具体应用顺序。置换检查通过 Schwartz-Zippel 引理高效实现，确保所有步骤均被验证。

**规则检查的多项式方法**  
对于需要多重集操作的规则（如 Resolution 和 DeDup），ZKSMT 将多重集编码为多项式。给定编码函数 $\Psi: \Sigma \to \mathbb{F}$，多重集 $\langle\langle \ell \rangle\rangle$ 对应的多项式为  
$$\gamma_\Psi(\langle\langle \ell \rangle\rangle) = \prod_{i} (X - \Psi(\ell_i)).$$  
子集关系 ($\subseteq$) 可通过证明一个多项式整除另一个多项式来检验。对于不考虑多重性的子集关系 ($\mathrm{subset}_d$)，使用双变量多项式 $\alpha$ 和 $\beta$ 进行验证，其中 $\alpha$ 编码两个列表的混合产物，$\beta$ 编码合并列表的顺序一致性。具体地，对于 $\langle\langle \ell^{\mathrm{sub}}\rangle\rangle \subseteq_d \langle\langle \ell^{\mathrm{sup}}\rangle\rangle$，验证者检查 $\alpha_\Psi(\langle\langle \bar{\ell}^{\mathrm{sub}}\rangle\rangle, \langle\langle \bar{\ell}^{\mathrm{sup}}\rangle\rangle) = \beta_\Psi(\langle\langle \bar{\ell}\rangle\rangle)$ 以及相应的单项式多项式等式，其中 $\bar{\ell}$ 是适当排序后的合并列表。

**检查指令示例**  
- **Resolution**：前提 $\bigvee A$ 和 $\bigvee B$，结论 $\bigvee C$，需满足 $\langle\langle A\rangle\rangle \subseteq \langle\langle C\rangle\rangle \uplus \langle\langle p\rangle\rangle$ 且 $\langle\langle B\rangle\rangle \subseteq \langle\langle C\rangle\rangle \uplus \langle\langle \neg p\rangle\rangle$。通过检查两个多项式整除关系实现。  
- **DeDup**：检查 $\langle\langle A\rangle\rangle$ 是 $\langle\langle B\rangle\rangle$ 的 $\mathrm{subset}_d$，使用双变量多项式协议。  
- **ExclMid**：简单模式匹配：结论必须为 $\bigvee\{\neg a, a\}$。  
- **Congruence**：检查结论是析取式，且包含函数应用相等与对应参数不等的子句。  
- **MulDist**：遍历 AST 检查乘法分配律。  
- **Farkas**：检查前提为等式，结论为析取的负不等式，且系数满足线性关系。

**安全性与正确性**  
论文证明了 ZKSMT 的完备性和可靠性（Theorem 1,2，证明见附录 B）。核心思想是将 ZKSMT 格式的证明与标准推导树之间建立双向转换：从 ZKSMT 的每一步可构造一棵标准推导树（注意重复使用结论的步骤需复制），反之将标准推导树转化为 ZKSMT 格式（合并相同 AST 节点）。由于 ZKSMT 执行了严格的置换检查和类型检查，转换后证明的每一步在原始理论下均有效。渐进复杂度方面，ZKSMT 的通信量和计算量与证明步骤数 $\pi$ 和最大列表长度 $\alpha$ 大致呈线性关系，实际测量证实了这一点。

### 核心公式与流程

**[表达式编码]**  
每个表达式映射为一个整数向量：  
$$
\left\{\varepsilon_I(\text{NodeID})\right\} \| \left\{\varepsilon_{\mathcal{A}_{\text{imm}}}(\text{ImmAddr})\right\} \| \left\{\varepsilon_{\mathcal{A}_{\text{ind}}}(\text{IndAddr})\right\}
$$
> 作用：将 AST 节点统一编码为定长整数向量以便承诺与零知识处理。

**[多项式编码多重集]**  
给定编码 $\Psi: \Sigma \to \mathbb{F}$，多重集 $\langle\langle \ell \rangle\rangle$ 的多项式表示为：  
$$
\gamma_\Psi(\langle\langle \ell \rangle\rangle) = \prod_{i=0}^{d-1} (X - \Psi(\ell_i))
$$
> 作用：将多重集运算化为多项式整除性问题，适用于子集关系检测。

**[子集检测多项式]**  
对于 $\mathrm{subset}_d$ 检测，使用双变量多项式：
$$
\alpha_\Psi(\langle\langle \bar{\ell}^{\text{sub}}\rangle\rangle, \langle\langle \bar{\ell}^{\text{sup}}\rangle\rangle) = (1+X)^{d'} \cdot \prod_{i=0}^{d'-1} (Y + \Psi(\bar{\ell}_i^{\text{sub}})) \cdot \prod_{i=0}^{d-2} (Y\cdot(1+X) + \Psi(\bar{\ell}_i^{\text{sup}}) + X\cdot \Psi(\bar{\ell}_{i+1}^{\text{sup}}))
$$
$$
\beta_\Psi(\langle\langle \bar{\ell}\rangle\rangle) = \prod_{i=0}^{d'+d-1} ((1+X)\cdot Y + \Psi(\bar{\ell}_i) + \Psi(\bar{\ell}_{i+1})\cdot X)
$$
> 作用：通过 $\alpha = \beta$ 的双变量多项式等式判定 $\bar{\ell}^{\text{sub}}$ 中的每个不同元素在 $\bar{\ell}^{\text{sup}}$ 中出现，同时保持顺序一致性。

**[Resolution 侧条件]**  
前提 $\bigvee A$ 和 $\bigvee B$，结论 $\bigvee C$，要求：  
$$
\langle\langle A\rangle\rangle \subseteq \langle\langle C\rangle\rangle \uplus \langle\langle p\rangle\rangle,\quad \langle\langle B\rangle\rangle \subseteq \langle\langle C\rangle\rangle \uplus \langle\langle \neg p\rangle\rangle
$$
> 作用：利用多项式整除检查实现规则的零知识验证。

**[Farkas 规则]**  
前提 $\sum_{i=0}^{n}(m_i * a_i) + (-m_i * b_i) = c$，结论 $\bigvee_{i=0}^{n}\{ \neg (a_i \leq_i b_i) \}$，要求 $m_i \geq 0$ 且 $c>0$ 或 $c=0$ 且至少一个 $\leq_i$ 是 $<$。
> 作用：将线性不等式的得出转化为对系数和模式的模式匹配。

### 实验结果

实验使用 AWS r5b.4xlarge 实例（128 GB 内存，16 vCPUs，10 Gbps 网络），配置 8 线程。  
1. **Boogie 测试集**：ZKSMT 能在数秒内验证大多数 Boogie 验证条件，最大基准（约 3000 步）耗时 39 秒。运行时间与证明步骤数大致呈线性关系。  
2. **与通用 zkVM 对比**：在最短的 Boogie 基准（6 步）上，Cheesecloth + Diet Mac’n’cheese 耗时 1 小时 51 分钟，而 ZKSMT 仅需 2 秒，加速比达 3330×。对 190 个可处理的基准，Cheesecloth 的估计时间比 ZKSMT 慢 1100 倍至 54000 倍以上。  
3. **压力测试**：使用 Wisconsin Safety Analyzer 基准，ZKSMT 能处理最大包含 20 万步、38 万表达式、最大列表长度 $\alpha=97$ 的证明，耗时约 3 小时，涉及 229 亿次 $\mathbb{F}_2$ 乘法和 3.36 亿次 $\mathbb{F}_{2^{128}}$ 乘法。更大的证明会因内存不足而失败。  
4. **规则分解**：对 Lock、Houdini、McCarthy 三个基准，类型检查、Resolution 和其他规则的时间占比显示 Resolution 是最耗时的单个规则，但所有规则均线性缩放。  
5. **参数影响**：最大列表长度 $\alpha$ 与运行时间成正比（$R^2>0.99$），表达式表大小 $\chi$ 和项列表数 $\eta$ 对运行时间影响不显著（因 ROM 访问时间恒定）。  
6. **证明膨胀**：从 SMTInterpol 原始证明编译为 ZKSMT 格式，步骤数增加 1 至 7 倍，但 ZKSMT 仍远快于通用 zkVM。

### 局限性与开放问题

当前 ZKSMT 仅支持量化自由的一阶理论，未涵盖数组理论和位向量理论，而这些在符号执行（如 KLEE）中频繁使用。核心逻辑可扩展至含全称和存在量词的公式，但需要设计新的量化规则。另一个挑战是将 ZKSMT 的证明与程序翻译验证（如编译等价性）结合，以实现完整的零知识程序安全验证流水线。此外，当前实现中最大列表长度 $\alpha$ 的填充策略会导致极端情况下的效率损失，未来可分解大型列表规则以消除影响。

### 强关联论文

[1] SMT-LIB: The Satisfiability Modulo Theories Library - Benchmarks [Google Scholar](https://scholar.google.com/scholar?q=SMT-LIB+The+Satisfiability+Modulo+Theories+Library+Benchmarks)

[5] Mike Barnett, Bor-Yuh Evan Chang, Robert DeLine, Bart Jacobs, and K Rustan M Leino. Boogie: A modular reusable verifier for object-oriented programs. **FMCO 2005** [Google Scholar](https://scholar.google.com/scholar?q=Boogie+A+modular+reusable+verifier+for+object-oriented+programs)

[6] Carsten Baum, Alex J. Malozemoff, Marc B. Rosen, and Peter Scholl. Mac’n’cheese: Zero-knowledge proofs for boolean and arithmetic circuits with nested disjunctions. **Crypto 2021** [Google Scholar](https://scholar.google.com/scholar?q=Mac%27n%27cheese+Zero-knowledge+proofs+for+boolean+and+arithmetic+circuits+with+nested+disjunctions)

[14] Jürgen Christ, Jochen Hoenicke, and Alexander Nutz. SMTInterpol: An interpolating SMT solver. **SPIN 2012** [Google Scholar](https://scholar.google.com/scholar?q=SMTInterpol+An+interpolating+SMT+solver)

[15] Santiago Cuéllar, Bill Harris, James Parker, Stuart Pernsteiner, and Eran Tromer. Cheesecloth: Zero-Knowledge proofs of real world vulnerabilities. **USENIX Security 2023** [Google Scholar](https://scholar.google.com/scholar?q=Cheesecloth+Zero-Knowledge+proofs+of+real+world+vulnerabilities)

[22] Galois, Inc. swanky: A suite of rust libraries for secure computation. 2019 [Google Scholar](https://scholar.google.com/scholar?q=swanky+A+suite+of+rust+libraries+for+secure+computation)

[32] Jochen Hoenicke and Tanja Schindler. A simple proof format for SMT. **SMT Workshop 2022** [Google Scholar](https://scholar.google.com/scholar?q=A+simple+proof+format+for+SMT)

[42] Ning Luo, Timos Antonopoulos, William R. Harris, Ruzica Piskac, Eran Tromer, and Xiao Wang. Proving UNSAT in zero knowledge. **CCS 2022** [Google Scholar](https://scholar.google.com/scholar?q=Proving+UNSAT+in+zero+knowledge)


## 关键词

+ ZKSMT零知识SMT定理证明
+ 虚拟机SMT有效性验证ZK
+ 可满足性模理论零知识
+ 程序安全验证隐私保护
+ 线性整数算术ZK证明
+ Boogie软件验证工具集成
