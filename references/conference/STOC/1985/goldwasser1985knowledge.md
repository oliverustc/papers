---
title: "The knowledge complexity of interactive proof-systems"
doi: 10.1145/22145.22178
标题简称:
论文类型: conference
会议简称: STOC
发表年份: 1985
modified: 2025-04-30 16:57:23
created: 2025-04-08 11:10:12
---
## The knowledge complexity of interactive proof-systems

## 发表信息

最早发表于1985年，有多个版本

+ [1985年 发表于STOC的extended abstract链接](https://dl.acm.org/doi/10.1145/22145.22178)
+ [1989年发表于SICOMP链接](https://epubs.siam.org/doi/10.1137/0218012)
+ [2019年重制版](https://dl.acm.org/doi/pdf/10.1145/3335741.3335750)

## 作者

+ [Shafi Goldwasser](Shafi%20Goldwasser.md)
+ [Silvio Micali](Silvio%20Micali.md)
+ Charles Rackoff

## 笔记

### 背景与动机
传统的NP证明系统要求证明者将整个证明“写在书里”，验证者只需被动阅读即可完成验证。这种模式虽然简洁，却往往迫使证明者披露远超待证命题本身的知识。例如，为证明一个图是哈密顿的，NP证明需要展示一条完整的哈密顿回路，这比仅仅确认“存在哈密顿回路”这一比特信息包含了多得多的结构信息。一个重要的问题是：对于证明一个定理，究竟需要传递多少“额外”知识？作者引入“知识复杂度”这一计算复杂性度量，旨在量化交互式证明过程中泄露的额外知识量。特别地，作者关注能否在证明过程中泄露的附加知识本质上为零，即实现“零知识”证明。该工作填补了理论空白：传统模型无法刻画交互行为对知识泄露的抑制作用，而本文通过引入交互式证明系统首次形式化了这一可能性。

### 相关工作

[1] S. Cook. The Complexity of Theorem-Proving Procedures. **STOC 1971** [Google Scholar](https://scholar.google.com/scholar?q=The+Complexity+of+Theorem-Proving+Procedures)
> 核心思路：形式化了NP的概念，定义了通过确定性多项式时间验证器即可检查的证明。
> 局限与区别：NP证明系统是非交互的，证明者必须一次性写出完整证据，这往往导致大量额外知识泄露。本文引入交互，允许验证者主动提问，从而可以显著降低知识泄露。

[2] L. Babai. Trading Group Theory for Randomness. **STOC 1985** [Google Scholar](https://scholar.google.com/scholar?q=Trading+Group+Theory+for+Randomness)
> 核心思路：提出了Arthur-Merlin交互式证明模型（公开抛币模型），并证明了常数轮交互即可捕捉全部能力。
> 局限与区别：Arthur-Merlin模型中，验证者的随机币对证明者是公开的。本文的交互式证明系统（IP）允许验证者拥有私有随机币，作者认为这能带来更强的表达能力，且是分析零知识的必要模型。

[3] M. Blum. Coin flipping by telephone. **IEEE COMPCON 1982** [Google Scholar](https://scholar.google.com/scholar?q=Coin+flipping+by+telephone)
> 核心思路：提出了通过电话进行抛币的密码学协议，为构造零知识证明提供了基础工具（如可承诺的比特）。
> 局限与区别：原文并未直接构建零知识证明，而是提供了一个关键原语。本文的零知识证明系统在构造中隐式地依赖于类似随机性掩码和承诺的思想，以确保证明者无法作弊。

[4] M. O. Rabin. How to Exchange Secrets by Oblivious Transfer. **Technical Report TR-81, Aiken Computation Laboratory, Harvard University 1981** [Google Scholar](https://scholar.google.com/scholar?q=How+to+Exchange+Secrets+by+Oblivious+Transfer)
> 核心思路：提出了不经意传输（OT）的概念，允许发送方以1/2的概率传递秘密（如大整数的分解），且发送方不知道接收方是否收到。
> 局限与区别：本文指出Rabin的原始OT协议缺少一个严格的安全性证明，无法证明恶意接收方不能以超过1/2的概率获得分解。本文的研究（与[FMR]合作）通过让接收方先进行一个零知识证明，证明自己知道某数的平方根，从而修复了这一缺陷，使得协议的正确性可归约到因式分解的困难性。

[5] Fagin, Halpern, Vardi. A model-theoretic analysis of knowledge. **FOCS 1984** [Google Scholar](https://scholar.google.com/scholar?q=A+model-theoretic+analysis+of+knowledge)
> 核心思路：从模型论角度分析“知识”的概念，假设参与者具有无限计算能力，关注逻辑上的知识蕴含。
> 局限与区别：该模型不适用于密码学场景。本文采用了计算复杂性框架下的知识概念，认为知识是相对于特定计算资源（多项式时间）而言的，只有在参与者无法自行计算时才构成“知识”。

[6] S. Goldwasser, S. Micali. Probabilistic Encryption. **JCSS 1984** [Google Scholar](https://scholar.google.com/scholar?q=Probabilistic+Encryption)
> 核心思路：提出“语义安全”的概率加密概念，其安全性基于计算不可区分性（computational indistinguishability）。
> 局限与区别：该工作主要解决加密问题。本文直接借鉴并扩展了“计算不可区分性”这一概念，用来定义“知识复杂度”，即两个概率分布的不可区分性。这也是判定零知识证明的核心工具。

[7] Halpern, Moses. Knowledge and Common Knowledge in a Distributed Environment. **PODC 1984** [Google Scholar](https://scholar.google.com/scholar?q=Knowledge+and+Common+Knowledge+in+a+Distributed+Environment)
> 核心思路：在分布式系统中形式化“知识”与“公共知识”，同样基于无限计算能力假设。
> 局限与区别：与本文的计算性知识定义不同，该工作未考虑计算资源限制。本文提出，在密码学中，接收方“知道”某事当且仅当其能够通过多项式时间算法独立计算出来。

[8] C. Papadimitriou. Games against nature. **FOCS 1983** [Google Scholar](https://scholar.google.com/scholar?q=Games+against+nature)
> 核心思路：提出了PSPACE的一个优雅刻画，即“对抗自然的游戏”。
> 局限与区别：Papadimitriou的模型虽然涉及概率和交互，但并不是一种高效的证明方法（验证者可能仍需指数时间），而本文定义的IP要求验证者为多项式时间，并且证明者可以具有无限能力。

[9] Dolev, Broder. Flipping Coins in Many Pockets. **FOCS 1984** [Google Scholar](https://scholar.google.com/scholar?q=Flipping+Coins+in+Many+Pockets)
> 核心思路：提出了多方抛币协议。
> 局限与区别：本文在应用部分指出，该协议可能泄露过多秘密知识。对协议的知识复杂度进行分析可以发现其潜在弱点，并最终被[j]的分析所证实（该协议在使用低指数RSA或Rabin函数时可被攻破）。

### 核心技术与方案

**整体框架**。本文提出了一个两层次的理论框架。第一层定义了交互式证明系统，作为NP的推广。第二层定义了知识复杂度，用以量化交互式证明中泄露的额外知识量。核心贡献是构造了一个具体的交互式零知识证明协议，证明了语言L = { (m, y) | y 是模 m 的二次非剩余} 具有知识复杂度0（即零知识）。

**交互式证明系统定义**。一个交互式证明系统由一对图灵机 (A, B) 组成。A是证明者，具有无限的计算能力；B是验证者，是多项式时间的概率图灵机。该对机器共享输入x，通过一个交互式图灵机模型进行通信，其中B主动发起并控制计算过程。系统需满足两个性质：
1.  **完备性**：若 x ∈ L，则存在一个诚实证明者A，使得B以压倒性概率（如 $1 - 1/n^k$）接受。
2.  **可靠性**：对任意（可能作弊的）证明者 A* 和 x ∉ L，B接受的概率是可忽略的（如 $1/n^k$）。

**知识复杂度与模拟器**。知识复杂度是衡量信息泄露的核心概念。直观上，如果存在一个多项式时间模拟器M，能够仅在不与证明者交互的情况下，生成与真实协议交互文本计算不可区分的概率分布，那么证明者就没有泄露知识。准确地说，对于语言L的证明系统 (A, B)，若对于所有多项式时间验证者 B'，存在一个多项式时间模拟器 M，使得两个概率分布族 $(A,B')[x]$ 和 $M[x]$（对 x ∈ L）是 (1 - 1/2^{f(n)})-可区分的，则称L的知识复杂度为 f(n)。特别地，f(n) = 0 意味着零知识。

**零知识证明协议：二次非剩余**。该协议的核心思想是，验证者B需要向证明者A证明他知道自己发送的每个数的“类型”（是随机平方还是平方乘以y）。这通过对B要求其提供“平方根”证据来实现。若y确实是二次非剩余，则A可以区分这两种类型。全协议分为多轮迭代。下面针对Jacobi符号为1的输入 (y,m) ∈ L 描述单轮交互（注：步数编号与原文4.2节一致，此处稍作简化以说明核心逻辑）：
1.  B随机选择 r0 ∈ Z_m*，抛硬币 Cx。若Cx=0，设 x = r0^2 mod m；若 Cx=1，设 x = y·r0^2 mod m。B发送x。然后，B选取两个大小为 n = log m 的随机集合T = {t_i = r_i^2 mod m} 和 S = {t_{n+i} = y·r_{n+i}^2 mod m}，并将 T∪S 中的元素随机排列后发送给A。
2.  A随机选择一个大小为n的子集 Z ⊆ T∪S 发送给B。
3.  B 披露所有 z∈Z 对应的随机数 r（表明其是平方或 y·平方）。对于剩余集合，B计算并发送一组“核对”数，使得A能够确信B确实知道这些数对应的平方根关系。B最终保留下两个集合X和Y。
4.  A检查B的回应是否一致，并确认所提供的“核对”数正确。若检查通过，A发送 v = Q_m(x)（即x的二次剩余性，0表示是平方，1表示非平方）。
5.  B验证 v 是否等于 Cx。若全部 n 轮迭代均正确，B接受。

**安全性论证**。
*   **完备性 (Completeness)**：若 (y,m) ∈ L，则A可以正确区分T中的元素（二次剩余）和S中的元素（二次非剩余），因此总是能正确回答v = Cx。证明者执行完全部n轮的概率趋近于1。
*   **可靠性 (Soundness)**：若 (y,m) ∉ L，即y是二次剩余，则所有ti和x都是随机平方，它们在分布上不可区分。即使A*拥有无限计算能力，其对Cx猜测的正确概率也精确为1/2。经过n轮后，A*成功欺骗B的概率仅为(1/2)^n。
*   **零知识 (Zero-Knowledge)**：这是证明的核心难点。对于任意的作弊验证者B'，模拟器M通过“重绕”B'来提取B'对平方根的知识。M首先以B'的随机带运行一次B'，得到第一轮交互的所有信息。然后，M使用相同的随机带重新运行B'，并让证明者（实际上是M自身）在第二步选择另一个不同的随机子集Z'。利用B'在两次运行中披露的数学关系（例如，若某个元素在第一次被揭示为某个数，在第二次被揭示为另一个数），M可以通过代数运算计算出B“知道”的某个秘密平方根，从而自己就能计算出Q_m(x)。这就避免了A（即M）直接计算Q_m(x)的困难。M可以完美模拟诚实证明者的行为，除了一个可忽略的事件（如两次选择相同子集）。因此，产生的分布与真实协议计算不可区分。

**渐近复杂度**。通信量（交互的比特数）与安全性参数n的多项式成正比。证明者A的计算能力需要能判定二次剩余（无限或条件多项式时间），验证者B的计算为多项式时间。

### 核心公式与流程

**[交互式证明系统定义]**
$$
\begin{aligned}
&\text{完备性: } \forall x \in L, \Pr[B \text{ 接受} \mid \text{诚实 A}] \ge 1 - \frac{1}{n^k}\\
&\text{可靠性: } \forall x \notin L, \forall A^*, \Pr[B \text{ 接受} \mid \text{任意 }A^*] \le \frac{1}{n^k}
\end{aligned}
$$
> 作用：定义了交互式证明系统必须满足的两个核心概率性质。

**[知识复杂度定义（模拟器描述）]**
$$
\exists \text{ PPT M, s.t. } \forall \text{ PPT }B', \{M[x]\}_{x\in L} \equiv^{\text{comp}} \{(A,B')[x]\}_{x\in L}
$$
> 作用：形式化了零知识的概念，即存在一个模拟器，能在不与证明者交互的情况下，生成与真实交互计算不可区分的文本分布。

**[二次非剩余零知识证明协议的核心发生器]**
$$ 
x = 
\begin{cases} 
r_0^2 \bmod m, & \text{if } C_x = 0 \\
y \cdot r_0^2 \bmod m, & \text{if } C_x = 1
\end{cases}
$$
> 作用：验证者B生成挑战数x，其类型（是否是平方）由秘密币C_x决定，这是证明者需要回答的问题。

**[证明可靠性的关键等式（Claim 1）]**
当$(y,m) \notin L$时，对于$C_x=0$和$C_x=1$，B发送给A的“核对”数分别满足：
- 若 $C_x=0$：对于 $t_i \in X$，B发送 $\sqrt{x \cdot t_i} = r_0 r_i$；对于 $t_i \in Y$，B发送 $\sqrt{x \cdot y \cdot t_i} = y r_0 r_i$。
- 若 $C_x=1$：对于 $t_i \in X$，B发送 $\sqrt{x \cdot y \cdot t_i} = y r_0 r_i$；对于 $t_i \in Y$，B发送 $\sqrt{x \cdot t_i} = r_0 r_i$。
在这两种情况下，A收到的都是随机平方的随机平方根，A无法区分$C_x$的值。
> 作用：严格证明当y是二次剩余时，所有挑战和响应在分布上对A完全不可区分，从而A*猜测C_x的概率精确为1/2，保证了可靠性。

**[零知识证明的模拟器策略（核心步骤）]**
M两次运行B'，得到两个不同的随机子集Z和Z'。然后M在X（B'第一次运行中披露的集合）和X'（B'第二次运行中披露的集合）的交集中寻找一个元素$t_i$，使得 $t_i \in (T-X') \cap \tilde{X}$。利用B'两次提供的关于$t_i$的不同平方根，M可通过代数运算计算出$r_0$，从而获得$Q_m(x)$。
> 作用：描述了模拟器如何解决判定二次剩余的困难问题。通过重绕B'，M能从B'的矛盾信息中自己计算出正确答案，从而在不依赖A的情况下完美模拟A的行为。

### 实验结果
该论文未提供任何实验结果。本文是完全的理论性工作，专注于定义和证明概念，如交互式证明系统、知识复杂度和零知识证明。其核心贡献在于提出了新的计算复杂性度量标准和具体的协议构造，并对其正确性、可靠性和零知识性质进行了数学证明。该工作并未模拟或实现任何系统，也没有对协议的具体运行时间或通信开销进行实验性测量。因此，不存在与传统方案的实验性基线对比，也没有关于适用规模或参数范围的实验数据。所有结论均建立在严格的数学推理之上，而非实证测试。

### 局限性与开放问题
本文在结论部分明确提出了多个开放性问题，这本身也揭示了其工作的局限和未涉及之处。首先，NP是否严格包含于IP？虽然本文引入了IP，但并未证明其与NP的关系。其次，知识复杂度为0的语言类KC(0)是否包含于NP？这是关于零知识证明表达能力的一个基本问题。此外，IP的超多项式轮交互是否是必要的？即交互层次IP[k]是否随k的增加而严格递增？最后，是否存在NP-完全语言具有多项式甚至线性知识复杂度？这些开放问题指出了该理论框架下需要进行大量后续研究的方向。

### 强关联论文

[1] S. Cook. The Complexity of Theorem-Proving Procedures. **STOC 1971** [Google Scholar](https://scholar.google.com/scholar?q=The+Complexity+of+Theorem-Proving+Procedures)

[2] L. Babai. Trading Group Theory for Randomness. **STOC 1985** [Google Scholar](https://scholar.google.com/scholar?q=Trading+Group+Theory+for+Randomness)

[3] M. Blum. Coin flipping by telephone. **IEEE COMPCON 1982** [Google Scholar](https://scholar.google.com/scholar?q=Coin+flipping+by+telephone)

[5] Fagin, Halpern, Vardi. A model-theoretic analysis of knowledge. **FOCS 1984** [Google Scholar](https://scholar.google.com/scholar?q=A+model-theoretic+analysis+of+knowledge)

[6] S. Goldwasser, S. Micali. Probabilistic Encryption. **JCSS 1984** [Google Scholar](https://scholar.google.com/scholar?q=Probabilistic+Encryption)

[7] Halpern, Moses. Knowledge and Common Knowledge in a Distributed Environment. **PODC 1984** [Google Scholar](https://scholar.google.com/scholar?q=Knowledge+and+Common+Knowledge+in+a+Distributed+Environment)

[8] C. Papadimitriou. Games against nature. **FOCS 1983** [Google Scholar](https://scholar.google.com/scholar?q=Games+against+nature)

[9] Dolev, Broder. Flipping Coins in Many Pockets. **FOCS 1984** [Google Scholar](https://scholar.google.com/scholar?q=Flipping+Coins+in+Many+Pockets)


## 关键词

+ 零知识证明奠基论文
+ 交互证明系统知识复杂性
+ 二次剩余零知识证明
+ 计算复杂性知识理论
+ 零知识定义
+ 密码学协议基础
