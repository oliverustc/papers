---
title: "On defining proofs of knowledge"
标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 1992
modified: 2025-04-08 18:35:36
---

## On defining proofs of knowledge

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/3-540-48071-4_28)

## 作者

+ 

## 笔记

### 背景与动机

知识证明（Proof of Knowledge）的概念由 Goldwasser、Micali 和 Rackoff 在开创性工作中引入，旨在形式化地刻画一个交互式证明系统中证明者“知道”某个秘密（如 NP 语言的见证）而非仅仅声称其存在。然而，该文献并未给出正式定义。后续被广泛引用的形式化定义，即 Feige、Fiat 和 Shamir 的定义 [6] 以及 Tompa 和 Woll 的定义 [18]，存在严重缺陷：它们仅在证明者以“非可忽略”（non‑negligible）概率使验证者接受时才要求知识提取器成功，而对概率既不非可忽略也不可忽略的情形（如概率为 \(n^{-k}\) 且 \(k\) 与输入长度相关）则不作任何要求。这种处理不仅概念上不完善，更在实际应用中造成问题——当知识证明被用作更大协议的子协议时（例如在抗选择密文攻击的加密方案中作为“解密模块”），无法证明协议的安全性，因为模拟器在面对概率既不非可忽略也不可忽略的证明者时无法完成提取。本文旨在指出这些缺陷的根源，并提出一个更完善的定义，该定义统一地要求知识提取器的期望运行时间与 \(p(x)-\kappa(x)\) 成反比，其中 \(p(x)\) 是验证者接受的概率，\(\kappa(x)\) 是知识误差函数，从而消除了对不同概率区间的割裂处理。

### 相关工作

[6] Feige, Fiat, Shamir. Zero-Knowledge Proofs of Identity. **J. Cryptology 1988** [Google Scholar](https://scholar.google.com/scholar?q=Zero-Knowledge+Proofs+of+Identity)
> 核心思路：定义知识证明时要求知识提取器仅对成功概率非可忽略的证明者有输出，且提取器需严格多项式时间。
> 局限与区别：未处理概率既不非可忽略也不可忽略的情形，且提取器需要证明者的辅助输入和描述，过于强依赖证明者内部信息。本文引入概率自适应的提取时间，并取消对证明者计算能力的限制。

[18] Tompa, Woll. Random Self-Reducibility and Zero-Knowledge Interactive Proofs of Possession of Information. **FOCS 1987** [Google Scholar](https://scholar.google.com/scholar?q=Random+Self-Reducibility+and+Zero-Knowledge+Interactive+Proofs+of+Possession+of+Information)
> 核心思路：允许验证者运行任意长时间，提取器以多项式时间（关于输入长度和验证者运行时间）工作，输入包含证明者的完全视图。
> 局限与区别：同样只对成功概率大于固定常数 \(\epsilon\) 的情形要求提取。本文指出其组成引理仅适用于 BPP 关系，且并行重复提升知识误差的证明困难。

[7] Feige, Shamir. Witness Indistinguishability and Witness Hiding Protocols. **STOC 1990** [Google Scholar](https://scholar.google.com/scholar?q=Witness+Indistinguishability+and+Witness+Hiding+Protocols)
> 核心思路：定义知识提取器为期望多项式时间，输出见证的概率至多比验证者接受概率低一个可忽略量（即 \(\Pr[\text{accept}] > \Pr[\text{extract}] - |x|^{-b}\)）。
> 局限与区别：该定义在统一处理所有概率方面优于 [6,18]，但仍要求知识提取器获得证明者的辅助输入 \(k\)，且无法处理超多项式时间证明者。本文去除对辅助输入的依赖，并允许提取器仅依赖公共输入和预言机访问。

[14] Goldwasser, Micali, Rackoff. The Knowledge Complexity of Interactive Proof Systems. **SIAM J. Comput. 1989** [Google Scholar](https://scholar.google.com/scholar?q=The+Knowledge+Complexity+of+Interactive+Proof+Systems)
> 核心思路：提出知识证明的概念雏形，通过知识提取器刻画“知识”。
> 局限与区别：未给出形式定义，后续 [6,18] 的形式化有缺陷。本文继承其提取器思想并加以完善。

[5] Brassard, Crépeau, Laplante, Léger. Computationally Convincing Proofs of Knowledge. **STACS 1991** [Google Scholar](https://scholar.google.com/scholar?q=Computationally+Convincing+Proofs+of+Knowledge)
> 核心思路：研究计算上可靠的知识证明，考虑仅对多项式时间证明者有效的提取器，提取时间与作弊概率成反比，知识误差设为 \(2^{-k}\)。
> 局限与区别：未给出正式定义，且主要针对特定轮结构协议。本文给出一般性定义并讨论“参数”（arguments）情况下的适应性调整。

[12] Goldreich, Micali, Wigderson. Proofs that Yield Nothing but Their Validity or All Languages in NP Have Zero-Knowledge Proof Systems. **J. ACM 1991** [Google Scholar](https://scholar.google.com/scholar?q=Proofs+that+Yield+Nothing+but+Their+Validity+or+All+Languages+in+NP+Have+Zero-Knowledge+Proof+Systems)
> 核心思路：提出图同构的原子知识证明（知识误差 1/2）以及图非同构的零知识证明。
> 局限与区别：[12] 未用模块化方式证明非同构协议，而是依赖整体分析。本文指出其子协议需要知识定义才能模块化，并展示新定义如何支持模块化模拟。

### 核心技术与方案

本文的核心贡献是给出知识证明的系统性定义（定义 3），并围绕该定义进行扩展与证明。

**定义框架**：给定二元关系 \(R\subseteq\{0,1\}^*\times\{0,1\}^*\)（通常为 NP 关系），交互函数 \(V\)（可多项式时间计算）称为关系 \(R\) 的知识验证器（knowledge verifier），知识误差为 \(\kappa:\{0,1\}^*\to[0,1]\)，需满足：

- **非平凡性**：存在一个交互函数 \(P^*\)，使得对所有 \(x\in L_R\)，\(P^*\) 与 \(V\) 的交互总是接受（即完备性概率为 1）。
- **有效性（validity）**：存在常数 \(c>0\) 和一个概率预言机（oracle）机器 \(K\)（称为通用知识提取器），使得对任意交互函数 \(P\) 和任意 \(x\in L_R\)，若  
  \[
  p(x)\triangleq \Pr[\mathrm{tr}_{P,V}(x)\in\mathrm{ACC}_V(x)] > \kappa(x),
  \]
  则 \(K\) 以预言机方式访问 \(P_x\)，输入 \(x\)，在期望步骤数不超过 \(|x|^c/(p(x)-\kappa(x))\) 内输出一个 \(y\in R(x)\)。

**关键创新**：

1. **概率自适应的提取时间**：提取器的期望运行时间与 \(1/(p(x)-\kappa(x))\) 成比例，而非仅在 \(p(x)\) 非可忽略时才要求提取。这统一处理了任意概率区间，包括了既不非可忽略也不可忽略的情形。
2. **知识误差函数 \(\kappa(\cdot)\)**：反映了验证者可能在没有真实知识的情况下接受的概率上限。典型例子是原子图同构知识证明的知识误差为 1/2；通过顺序重复可将其降低至 \((1+1/\mathrm{poly}(\cdot))\kappa(\cdot)^{m(\cdot)}\)（定理 4）。对于知识误差可忽略的情形，若存在指数时间搜索算法，则可进一步将误差降至 0（命题 5）。
3. **提取器不依赖证明者的内部信息**：仅依赖公共输入 \(x\) 和预言机 \(P_x\)（即证明者关于 \(x\) 的交互函数），而不同于 [6,18] 需要证明者的辅助输入或完全视图。这使得定义更符合“从交互中可得的知识”这一直觉。
4. **更强的通用性**：定义不限制证明者的计算能力，因此可应用于超多项式时间证明者（例如 Shamir 的 PSPACE 交互证明中的证明者），并可谈论其“知识”（§7.2）。同时定义去掉了对声音性（soundness）的内置要求，将声音性视为可选的附加性质，从而更准确地刻画只需在 \(x\in L_R\) 上保证知识提取的应用（如基于二次剩余的身份识别）。

**有效性条件的等价形式**（§6）：提出另一种表述，即存在期望多项式时间的提取器 \(K\) 使得 \(\Pr[K^{P_x}(x)\in R(x)] \ge p(x)-\kappa(x)\)，并且 \(K^{P_x}(x)\in R(x)\cup\{\bot\}\)。该形式在模拟和证明中更方便。

**知识误差降低的证明概要**（附录 C.1）：对于知识验证器 \(V\)，定义 \(V_m\) 为顺序重复 \(m(x)\) 次。构造提取器 \(K_m\)：通过分析部分转录的接受概率，找到一个轮次 \(i\) 使得第 \(i+1\) 次迭代的条件成功概率足够高，然后利用原提取器 \(K\) 在该部分转录下进行提取。通过并行运行多个拷贝，最终期望时间被控制在 \(\mathrm{poly}(x)/(p_m(x)-\kappa_m(x))\) 内，其中 \(\kappa_m(x)=(1+1/\mathrm{poly}(x))\kappa(x)^{m(x)}\)。

**应用示例**（§7）：
- **图非同构的零知识证明模块化**：使用图同构原子知识证明（知识误差 1/2）作为子协议。模拟器利用知识提取器从接受转录中提取同构，从而完美模拟证明者的步骤。由于提取时间与子协议接受概率成反比，而子协议仅在模拟器需要时才被调用，总期望时间为多项式。
- **PSPACE 交互证明的知识**：Shamir 的 IP=PSPACE 协议中，证明者可通过算术化方法传递满足性赋值。本文构造知识提取器通过多项式插值获取中间配置，证明该协议是关系 \(R_L\)（输入与中间配置）的知识证明。

**复杂度**：验证器 \(V\) 的运行时间为多项式；通用提取器 \(K\) 的期望运行时间为 \(\mathrm{poly}(|x|)/(p(x)-\kappa(x))\)。对于重复协议，\(V_m\) 的通信量增加 \(m\) 倍，提取时间相应调整。

### 核心公式与流程

**[知识验证器定义（Def. 3）]**
\[
\begin{aligned}
&\text{非平凡性: } \exists P^*\ \forall x\in L_R:\ \Pr[\mathrm{tr}_{P^*,V}(x)\in\mathrm{ACC}_V(x)]=1.\\
&\text{有效性: } \exists c>0,\ \text{预言机机器 }K:\ \forall P,\forall x\in L_R,\\
&\quad\text{若 }p(x)=\Pr[\mathrm{tr}_{P,V}(x)\in\mathrm{ACC}_V(x)]>\kappa(x),\\
&\quad\text{则 }K^{P_x}(x)\text{ 在期望 }\frac{|x|^c}{p(x)-\kappa(x)}\text{ 步内输出 }y\in R(x).
\end{aligned}
\]
> 作用：给出知识证明的形式化定义，核心是将提取时间与成功概率差成反比。

**[有效性等价形式（§6）]**
\[
\exists\ \text{期望多项式时间预言机机器 }K:\ \forall P,\forall x\in L_R,\\
\Pr[K^{P_x}(x)\in R(x)] \ge p(x)-\kappa(x),\quad K^{P_x}(x)\in R(x)\cup\{\bot\}.
\]
> 作用：提供另一种便于模拟器使用的表述，确保提取器能以概率 \(p(x)-\kappa(x)\) 成功输出见证，否则输出 \(\bot\)。

**[顺序重复知识误差降低（定理 4）]**
\[
\kappa_m(x) = (1+1/\mathrm{poly}(|x|))\cdot\kappa(x)^{m(x)}.
\]
> 作用：表明通过顺序重复可将知识误差指数级降低，证明基于部分转录的统计分析和并行提取子程序。

**[原子协议：图同构知识证明（附录 E）]**
\[
\begin{aligned}
&\text{输入：图 }H,G\text{（同构）。}\\
&\text{步骤 p1: 证明者选 }t=n^2\text{ 个随机同构副本 }K_1,\ldots,K_t\text{ 发送。}\\
&\text{步骤 v1: 验证者随机选子集 }S\subseteq\{1,\ldots,t\}\text{ 发送。}\\
&\text{步骤 p2: 对 }i\in S\text{ 发送 }a_i=\pi_i\text{（ }H\to K_i\text{ 的同构）；}\\
&\qquad\quad\ \ \text{对 }i\notin S\text{ 发送 }a_i=\pi_i\circ\psi\text{（ }G\to H\text{ 的同构通过 }K_i\text{）。}\\
&\text{步骤 v2: 验证 }a_i\text{ 正确，若全部正确则接受。}\\
&\text{知识误差：}1/2^t\text{（但可降为零误差，因 }t\text{ 使} s=1\text{ 时穷举可行）。}
\end{aligned}
\]
> 作用：展示原子知识证明的构造，其提取器通过寻找另一接受子集 \(S'\neq S\) 来提取同构，期望时间与接受概率的倒数成正比。

**[PSPACE 证明中的知识提取（§7.2）]**
\[
\begin{aligned}
&\text{思路：通过选择随机 }r_1,\ldots,r_{i-1}\in Z_N\text{ 向证明者询问第 }i\text{ 个变量的多项式 }p_i,\\
&\text{然后利用多项式插值（使用 }2t\text{ 个随机点）恢复 }c_{i,j}(\sigma_1,\ldots,\sigma_{i-1})\text{ 系数，}\\
&\text{从而找到使得 }p_i(\mu_i)\not\equiv0\pmod N\text{ 的 }\mu_i\in\{0,1\}。
\end{aligned}
\]
> 作用：说明超多项式时间证明者的知识同样可被形式化定义，提取器通过算术化方法获取量子位满足性赋值。

### 实验结果

本文是理论定义与概念澄清工作，未提供实验评估。所有讨论均基于形式化定义的逻辑分析、构造性证明以及已知协议（如图同构、图非同构、PSPACE 交互证明）的重新解释。文中通过两个具体应用（图非同构的模块化零知识证明、PSPACE 证明的知识意义）展示了新定义在解决先前定义无法处理的案例中的有效性，但未涉及实际计算实验或性能测量。该工作的核心贡献在于提供了正确且统一的形式化基础，使得后续协议的安全证明（如抗选择密文攻击的加密方案）能够基于严格定义而非“手摇”论证。

### 局限性与开放问题

本文定义依赖一个已知的知识误差函数 \(\kappa(\cdot)\)，但在某些应用中 \(\kappa\) 的具体取值可能需要基于计算复杂性假设（如整数离散对数问题的难解性）来设定，如何系统地从假设推导出合理的 \(\kappa\) 仍是一个开放问题。对于并行重复降低知识误差的情形，本文仅给出针对特定类知识验证器的部分结果，未能提供一个通用的并行复合定理，这限制了在通信效率敏感场景下的应用。此外，本文明确将声音性与知识验证分离，但在许多经典应用中两者需同时满足，如何平衡两者并设计同时满足的协议仍需要更多研究。

### 强关联论文

[6] Feige, Fiat, Shamir. Zero-Knowledge Proofs of Identity. **J. Cryptology 1988** [Google Scholar](https://scholar.google.com/scholar?q=Zero-Knowledge+Proofs+of+Identity)

[7] Feige, Shamir. Witness Indistinguishability and Witness Hiding Protocols. **STOC 1990** [Google Scholar](https://scholar.google.com/scholar?q=Witness+Indistinguishability+and+Witness+Hiding+Protocols)

[12] Goldreich, Micali, Wigderson. Proofs that Yield Nothing but Their Validity or All Languages in NP Have Zero-Knowledge Proof Systems. **J. ACM 1991** [Google Scholar](https://scholar.google.com/scholar?q=Proofs+that+Yield+Nothing+but+Their+Validity+or+All+Languages+in+NP+Have+Zero-Knowledge+Proof+Systems)

[14] Goldwasser, Micali, Rackoff. The Knowledge Complexity of Interactive Proof Systems. **SIAM J. Comput. 1989** [Google Scholar](https://scholar.google.com/scholar?q=The+Knowledge+Complexity+of+Interactive+Proof+Systems)

[18] Tompa, Woll. Random Self-Reducibility and Zero-Knowledge Interactive Proofs of Possession of Information. **FOCS 1987** [Google Scholar](https://scholar.google.com/scholar?q=Random+Self-Reducibility+and+Zero-Knowledge+Interactive+Proofs+of+Possession+of+Information)

[5] Brassard, Crépeau, Laplante, Léger. Computationally Convincing Proofs of Knowledge. **STACS 1991** [Google Scholar](https://scholar.google.com/scholar?q=Computationally+Convincing+Proofs+of+Knowledge)

[17] Shamir. IP=PSPACE. **FOCS 1990** [Google Scholar](https://scholar.google.com/scholar?q=IP=PSPACE)


## 关键词

+ 知识证明
+ 形式化定义
+ 密码协议
+ 提取器
+ 挑战-应答