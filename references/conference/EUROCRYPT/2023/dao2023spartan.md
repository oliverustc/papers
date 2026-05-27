---
title: "Spartan and bulletproofs are simulation-extractable for free"
doi: 10.1007/978-3-031-30617-4_18
标题简称:
论文类型: conference
会议简称: EUROCRYPT
发表年份: 2023
modified: 2025-04-13 17:49:05
---
## Spartan and bulletproofs are simulation-extractable (for free !)

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-30617-4_18)

## 作者

+ Quang Dao 
+ [Paul Grubbs](Paul%20Grubbs.md)
## 笔记

### 背景与动机
零知识简洁非交互式知识论证（zkSNARKs）在实践中，尤其是在区块链和加密货币系统中，面临着两类严峻的安全威胁：适应性正确性攻击和可塑性攻击。前者允许攻击者在生成证明后选择公共输入以证明虚假陈述；后者允许攻击者将一个有效证明篡改为另一个不同的有效证明。标准的安全属性如非适应性知识可靠性和零知识无法保证对这些攻击的防御，而模拟可提取性（SIM-EXT）则能同时蕴含这两者，为部署的系统提供更强的安全保证。现有工作[29, 30]证明了部分基于结构化参考字符串（SRS）的zkSNARK（如PlonK, Marlin, Sonic）在代数群模型（AGM）下满足SIM-EXT。然而，这些结果不适用于像Spartan和Bulletproofs这样的透明zkSNARK，因为它们依赖不同的构建模块（如Sumcheck和Inner Product Argument），并且依赖于更强的AGM假设。本文旨在填补这一空白，证明在随机预言机模型（ROM）和标准离散对数假设下，Spartan和Bulletproofs自身就满足SIM-EXT，这一性质是“免费”得来的。

### 相关工作

[2] Attema, T., Fehr, S., Klooß, M. Fiat-Shamir Transformation of Multi-Round Interactive Proofs. **TCC 2021** [Google Scholar](https://scholar.google.com/scholar?q=Fiat-Shamir+Transformation+of+Multi-Round+Interactive+Proofs)
> 核心思路：提出了一个树构建器，可以从多轮协议的Fiat-Shamir变换后的NIZK中提取接受证明的树，从而证明知识可靠性。
> 局限与区别：该树构建器仅适用于完善特殊可靠性的协议，且要求验证者挑战仅需要满足“互异性”。本文将其推广，支持计算特殊可靠性，并允许挑战满足更复杂的谓词（如线性无关）。

[16] Bünz, B., et al. Bulletproofs: Short Proofs for Confidential Transactions and More. **IEEE S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Bulletproofs+Short+Proofs+for+Confidential+Transactions+and+More)
> 核心思路：提出了Bulletproofs协议，包括聚合范围证明和算术电路可满足性证明，其安全性基于离散对数假设。
> 局限与区别：该论文仅证明了标准的知识可靠性，未证明非可塑性（SIM-EXT）。本文首次证明其FS变换版本在ROM中满足SIM-EXT。

[29] Ganesh, C., et al. What Makes Fiat-Shamir zkSNARKs (Updatable SRS) Simulation Extractable? **SCN 2022** [Google Scholar](https://scholar.google.com/scholar?q=What+Makes+Fiat-Shamir+zkSNARKs+Updatable+SRS+Simulation+Extractable)
> 核心思路：建立了一般化的SIM-EXT定理，一个Fiat-Shamir编译的NIZK满足SIM-EXT，如果它同时满足知识可靠性、k-零知识（k-ZK）和k-唯一响应（k-UR）。
> 局限与区别：该定理主要针对基于SRS的协议，且证明中使用了AGM，不直接适用于透明zkSNARK。本文采用了类似的定理框架，但将其适配到透明设置（无SRS更新），并完全在ROM中证明所有性质。

[30] Ganesh, C., et al. Fiat-Shamir Bulletproofs are Non-Malleable (in the Algebraic Group Model). **EUROCRYPT 2022** [Google Scholar](https://scholar.google.com/scholar?q=Fiat-Shamir+Bulletproofs+are+Non-Malleable+in+the+Algebraic+Group+Model)
> 核心思路：在AGM中证明了Bulletproofs的FS变换版本满足SIM-EXT。
> 局限与区别：该工作的证明依赖于AGM，本文的核心目标之一就是移除对AGM的依赖，仅基于标准DL假设和ROM证明Bulletproofs的SIM-EXT。

[54] Setty, S. Spartan: Efficient and General-Purpose zkSNARKs without Trusted Setup. **CRYPTO 2020** [Google Scholar](https://scholar.google.com/scholar?q=Spartan+Efficient+and+General-Purpose+zkSNARKs+without+Trusted+Setup)
> 核心思路：提出了Spartan协议，通过Sumcheck和多项式承诺技术构造了透明zkSNARK，其安全基于离散对数假设。
> 局限与区别：该论文主要证明了标准的知识可靠性和零知识，未涉及SIM-EXT。本文首次为Spartan的两个变种（线性验证器NIZK和次线性验证器SNARK）建立了SIM-EXT的证明。

### 核心技术与方案
本文采用[29]的通用SIM-EXT定理框架。对于一个由$(2r+1)$轮公开币交互协议$\Pi$转换而来的非交互协议$\pi_{\mathsf{FS}}$，只要满足以下三个性质，它就满足SIM-EXT：(1) 适应性知识可靠性 (KS)，(2) 完美的$k$-零知识 ($k$-ZK)，以及(3) 对于同一个轮次$k$，满足$k$-唯一响应 ($k$-UR)。本文的核心工作是为Spartan和Bulletproofs的各个变种分别验证这三个性质。

**1. 知识可靠性（通过计算特殊可靠性）**

知识可靠性是证明中最富技术挑战的部分。本文通过一个标准的两步路径来证明：首先证明交互协议$ \Pi $满足计算特殊可靠性（Computational Special Soundness），然后利用推广的树构建器（Tree Builder）建立知识可靠性。

**关于树构建器的推广：** 现有树构建器[2]要求每个节点的子节点对应的验证者挑战必须互异。但Spartan和Bulletproofs的可靠性依赖于更强的关系，例如Spartan的Sumcheck子协议要求挑战向量线性无关，而Bulletproofs要求标量挑战非零且互逆。本文引入“划分谓词”的概念，将挑战空间划分为若干块，并要求子节点的挑战来自不同的划分块。例如，对于Bulleproofs，挑战来自$\mathbb{F}^*$，划分块为$\{x, -x\}$；对于Spartan的Sumcheck，挑战来自$\mathbb{F}^2$，划分块要求两个向量线性无关。本文证明存在一个高效的树构建器（Theorem 4.4），能够从成功的恶意证明者$ \mathcal{P}^*$处，以不低于$\epsilon(\mathcal{P}^*) - \frac{Q(Q-1)/2 + (Q+1)(\sum_i n_i - r)}{C}$的概率，生成满足特定划分谓词的$(\phi, \mathbf{n})$-树，其中$Q$是随机谕言查询次数，$C$是划分块的最小大小。

**各协议的特殊可靠性证明：**
- **Spartan-NIZK (Lemma 5.6):** 其信息论核心Spartan-Core的可靠性有$ (6\mu+1)/|\mathbb{F}|$的错误概率。树提取器通过级联方式工作：提取Sumcheck多项式（需要$(1, 2_{\text{li}}, 2)$-树），提取$\Sigma$-协议子例程（ProdPf, OpenPf, EqPf）的声明，提取多项式承诺$\mathsf{PC}_{\mathsf{Multi}}.\mathsf{Open}$的见证（需要$(4_\pm, \ldots, 4_\pm, 2)$-树）。最终，若所有子提取器成功，则输出R1CS见证；否则，存在一个攻击离散对数关系（DL-REL）的对手。
- **Spartan-SNARK (Lemma 5.13):** 核心逻辑与NIZK类似，但额外包含一个对稀疏多项式承诺$\mathsf{PC}_{\mathsf{SparseMulti}}.\mathsf{Open}$的提取。由于后者涉及更多轮次和更大的树结构，其可靠性损失更大，且提取器时间复杂度更高：$O(Q \cdot m^{7.5} \cdot (m+n)^3)$。
- **Bulletproofs (Lemma 6.1):** BP-ARP需要$(m \cdot n, m+2, 3, 2, \underbrace{4_{\pm}, \ldots, 4_{\pm}}_{\log(mn)})$ -树。其核心是Inner Product Argument (BP-IPA)的提取，最终将KS的可靠性归约到DL-REL假设。

**2. $k$-零知识 ($k$-ZK) 模拟器**

$k$-ZK要求存在一个模拟器，它只允许在第$k$轮编程随机谕言。这比标准的NIZK模拟器（通常可以编程所有轮）要求更强。
- **Spartan (Theorem 5.8):** $k$等于协议的最后一轮减一。模拟器利用Spartan的结构特点：除了最后一个子协议，所有其他子协议（如Sumcheck、$\Sigma$-protocols）都可以通过使用有效见证（而不需要真实见证）来诚实生成，这些见证可随机采样得到，保证模拟的统计不可区分性。模拟器只需在最后的相等证明（EqPf）子协议中，调用其模拟器，这正好是第$k$轮，需要编程随机谕言。这种延迟编程的策略使其能完美满足$k$-ZK。
- **Bulletproofs (Lemma 6.2):** $k=2$。模拟器在第2轮之后编程挑战$x$。通过在第2轮后采样$x$并计算所有依赖于$x$的值（如$ \hat{t}, \mu $），然后倒推出$T_2$以满足验证方程，从而生成一个与诚实证明分布完全相同的模拟证明。该方法确保了模拟的完美性。

**3. $k$-唯一响应 ($k$-UR)**

$k$-UR要求对手不能为两个不同的证明输出相同的第$k$轮之前的部分和相同的第$k$轮挑战。这是本文在移除AGM方面的核心创新。
- **Spartan (Lemma 5.9):** Spartan的最后一轮是一个经典的$\Sigma$-协议（EqPf），对于给定的挑战，响应（scalar $z$）由验证方程$h^z = (C_1/C_2)^c \cdot \alpha$唯一确定。因此，它天然满足$k$-UR，不需要任何额外假设。
- **Bulletproofs (Lemma 6.3):** 这是一个难点。本文提出了一个新的证明策略，完全替代了[30]中依赖AGM的方法。核心思想是用提取替换AGM。给定一个输出两个不同证明的$k$-UR对手（它们在第二轮挑战$x$之前相同，但之后不同），首先从中提取出BP-IPA的见证$(\mathbf{l}, \mathbf{r})$。然后通过分析三种不同情况得到矛盾：
  1. 如果$\hat{t} \neq \hat{t}'$或$\beta_x \neq \beta_x'$，则两个等式$g^{\hat{t}} h^{\beta_x} = \text{constant}$提供一个非平凡的离散对数关系。
  2. 如果$(\hat{t}, \beta_x) = (\hat{t}', \beta_x')$但$\mu \neq \mu'$，则两个验证IPA的等式提供一个离散对数关系。
  3. 如果除了最后的IPA证明外全相同，则利用BP-IPA证明的唯一性（可归约到DL-REL）得到矛盾。
该归约通过一系列混合论证完成，将$k$-UR的安全性归约到DL-REL假设和BP-IPA的KS安全性。

最终，通过定理3.4，将以上三个性质组合起来，给出了Spartan和Bulletproofs各变种的完整SIM-EXT优势上界（Theorem 5.10, 5.14, 6.4, 6.5）。

### 核心公式与流程

**[划分谓词定义]**
对于挑战空间Ch的一个划分$\mathcal{P} = \mathsf{Ch}^{(1)} \sqcup \cdots \sqcup \mathsf{Ch}^{(C)}$，对应的划分谓词$\phi_{\mathcal{P}, n}: \mathsf{Ch}^n \to \{0,1\}$定义为：$\phi_{\mathcal{P}, n}(c_1, \dots, c_n) = 1$当且仅当$c_1, \dots, c_n$属于不同的划分块。
> 作用：定义了比简单“互异性”更强的挑战关系，是泛化树构建器的核心。

**[Spartan-NIZK知识可靠性 (Theorem 5.7)]**
存在提取器$\mathcal{E}_{\text{Spartan-NIZK}_{\text{FS}}}$，对任何PPT对手$\mathcal{P}^*$，存在EPT对手$\mathcal{B}$攻击DL-REL，使得：
$$
\begin{aligned}
\mathbf{Adv}_{\text{Spartan-NIZK}_{\text{FS}}}^{\text{KS}} (\mathcal{E}, \mathcal{P}^*) \leq &\frac{Q(Q-1) + (Q+1)(13\mu + 10) + 2(6\mu+1)}{|\mathbb{F}| - 1} \\
&+ \mathbf{Adv}_{\mathbb{G}, \sqrt{m}+2}^{\text{DL-REL}}(\mathcal{B})
\end{aligned}
$$
其中$\mu = \log m$，$m$是R1CS矩阵维度。
> 作用：给出了Spartan-NIZK FS版本知识可靠性的具体安全边界，表明其归约到DL-REL。

**[Bulletproofs BP-ARP的2-唯一响应 (Lemma 6.3)]**
对于任何攻击2-UR的对手$\mathcal{A}$，存在一个对手$\mathcal{B}$攻击DL-REL，使得：
$$
\mathbf{Adv}_{\text{BP-ARP}_{\text{FS}}}^{\text{2-UR}}(\mathcal{A}) \leq 2 \cdot \frac{Q(Q-1) + 6(Q+1)\log(mn)}{|\mathbb{F}|-1} + 3 \cdot \mathbf{Adv}_{\mathbb{G}, 2mn+3}^{\text{DL-REL}}(\mathcal{B})
$$
> 作用：在不依赖AGM的情况下，给出了Bulletproofs FS版本唯一响应性质的安全归约。

**[SIM-EXT定理 (Theorem 3.4)]**
对于一个FS编译的NIZK$\pi_{\text{FS}}$，如果它满足KS，并存在一个完美的$k$-ZK模拟器$\mathcal{S}_{\text{FS},k}$和$k$-UR性质，则它满足SIM-EXT。其优势满足：
$$
\mathbf{Adv}^{\text{SIM-EXT}}(\mathcal{E}_{\text{SE}}, \mathcal{P}^*) \leq \mathbf{Adv}^{\text{KS}}(\mathcal{E}, \mathcal{P}_{\text{KS}}^*) + \mathbf{Adv}^{k-\text{UR}}(\mathcal{A}) + 2/|\mathsf{Ch}_k|
$$
> 作用：建立了SIM-EXT与KS、$k$-ZK和$k$-UR之间的充分条件关系，是本文所有证明的顶层框架。

### 实验结果
本文不涉及实验，而专注于理论安全性分析。然而，在第7章中，作者对其证明的紧致性（concrete security bounds）进行了定量讨论。为了评估安全边界，作者计算了在典型参数下的位安全强度（bit security）。对于Bulletproofs的单值范围证明（$m=1, n=64$），作者的基于“重绕”（rewinding）的KS分析得到约22位的安全强度，而基于AGM的分析[33]达到了约164位。这种巨大的差距源于两个因素：第一，重绕技术导致了对随机谕言查询次数$Q$的二次依赖（$O(Q^2)$），而AGM下是线性依赖$O(Q)$；第二，归约到DL-REL的对手是期望多项式时间（EPT），根据[42]的结果，这会导致额外的“平方根”级别的安全性损失。对于Spartan，由于其树状结构更庞大（$O(m^6)$），其仿真时间更长，导致可证明的安全强度更低。作者承认这种紧致性差距是当前工作的主要局限性，并期望未来的工作能改进重绕技术的紧致性。

### 局限性与开放问题
本文的证明虽然理论意义重大，但在紧致性方面存在显著不足。基于重绕的提取器导致安全边界对查询次数$Q$有二次依赖，且提取器运行时间为$O(Q \cdot N)$，这使得在典型参数下，可证明的位安全强度远低于标准要求（例如22位对比于AGM下的164位）。未来工作一个重要的开放问题是，能否为Spartan和Bulletproofs设计出更紧致的、基于重绕的知识可靠性归约。此外，本文的证明针对特定协议，期待能将这一分析框架泛化，抽象出一个适用于其他基于Sumcheck或多项式IOP的透明zkSNARK的通用SIM-EXT证明理论。最后，本文的安全性依赖于离散对数假设，会被量子计算机攻击，在未来后量子密码学的语境下，这些协议的安全性需要重新评估。

### 强关联论文

[2] Attema, T., Fehr, S., Klooß, M. Fiat-Shamir Transformation of Multi-Round Interactive Proofs. **TCC 2021**

[16] Bünz, B., et al. Bulletproofs: Short Proofs for Confidential Transactions and More. **IEEE S&P 2018**

[29] Ganesh, C., et al. What Makes Fiat-Shamir zkSNARKs (Updatable SRS) Simulation Extractable? **SCN 2022**

[30] Ganesh, C., et al. Fiat-Shamir Bulletproofs are Non-Malleable (in the Algebraic Group Model). **EUROCRYPT 2022**

[33] Ghoshal, A., Tessaro, S. Tight State-Restoration Soundness in the Algebraic Group Model. **CRYPTO 2021**

[54] Setty, S. Spartan: Efficient and General-Purpose zkSNARKs without Trusted Setup. **CRYPTO 2020**

[57] Wahby, R.S., et al. Doubly-Efficient zkSNARKs without Trusted Setup. **IEEE S&P 2018**


## 关键词

+ 模拟可提取性
+ Spartan
+ Bulletproofs
+ 离散对数假设
+ 零知识证明安全性