---
title: "Fiat-Shamir Security of FRI and Related SNARKs"
标题简称:
论文类型: conference
会议简称: ASIACRYPT
发表年份: 2023
modified: 2025-04-10 16:40:26
---

## Fiat-Shamir Security of FRI and Related SNARKs

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-981-99-8724-5_1)

## 作者

+ [Alexander R. Block](Alexander%20R.%20Block.md)
+ Albert Garreta
+ [Jonathan Katz](Jonathan%20Katz.md)
+ [Justin Thaler](Justin%20Thaler.md)
+ Pratyush Ranjan Tiwari
+ Michał Zając

## 笔记

### 背景与动机
Fiat-Shamir变换是将交互式协议转化为非交互式随机预言机模型下安全证明的标准工具，广泛用于构建SNARK等密码学原语。然而，该变换对多轮交互协议的安全性并非普遍成立，在最坏情况下，安全比特损失与协议轮数呈线性关系，大幅削弱实际部署的安全保障。特别地，FRI协议（一种高效的对数轮交互式预言机近似证明）及其在Plonky2、ethSTARK等实际系统中的派生方案，虽然被广泛应用并承载了数亿美元资产，但其在Fiat-Shamir变换下的安全性此前缺乏正式证明。现有分析通常仅针对交互版本，或隐含依赖于许多轮子协议本身是Fiat-Shamir安全的假设。本文旨在填补这一关键空白，通过建立FRI及其相关协议的逐轮（知识）可靠性，为这些协议在随机预言机模型下的Fiat-Shamir安全性提供第一个正式证明。

### 相关工作
[4] Ben-Sasson等. Fast Reed-Solomon Interactive Oracle Proofs of Proximity. **ICALP 2018** [Google Scholar](https://scholar.google.com/scholar?q=Fast+Reed-Solomon+Interactive+Oracle+Proofs+of+Proximity)
> 核心思路：提出了FRI协议，一个对数轮交互式预言机近似证明。
> 局限与区别：仅分析了交互版本的安全性，未证明其在Fiat-Shamir变换下的安全性。

[9] Ben-Sasson等. Interactive Oracle Proofs. **TCC 2016** [Google Scholar](https://scholar.google.com/scholar?q=Interactive+Oracle+Proofs)
> 核心思路：引入了交互式预言机证明（IOP）的概念和BCS变换，将IOP编译为非交互式论证。
> 局限与区别：其安全性依赖于状态恢复可靠性，本文的工作是证明特定协议满足更强的逐轮可靠性，从而可直接应用BCS变换。

[22] Canetti等. Fiat-Shamir: from practice to theory. **STOC 2019** [Google Scholar](https://scholar.google.com/scholar?q=Fiat-Shamir:+from+practice+to+theory)
> 核心思路：提出了逐轮（RBR）可靠性的概念，作为分析Fiat-Shamir安全性的工具。
> 局限与区别：为分析提供了理论基础，但未对FRI等复杂多轮协议给出具体的RBR可靠性证明。

[6] Ben-Sasson等. Proximity gaps for Reed-Solomon codes. **FOCS 2020** [Google Scholar](https://scholar.google.com/scholar?q=Proximity+gaps+for+Reed-Solomon+codes)
> 核心思路：给出了FRI协议目前已知的最佳可证明可靠性界。
> 局限与区别：这些界是针对交互版本的，本文的RBR可靠性分析直接利用了这些结果。

[60] Polygon Zero Team. Plonky2: Fast recursive arguments with plonk and FRI.
> 核心思路：提出了一种结合Plonk和FRI的高效递归论证系统。
> 局限与区别：仅分析了交互版本，本文将其作为实例，使用所开发的工具证明了其Fiat-Shamir安全性。

[65] StarkWare. ethSTARK Documentation. **ePrint 2021** [Google Scholar](https://scholar.google.com/scholar?q=ethSTARK+Documentation)
> 核心思路：提出了基于FRI的ethSTARK协议。
> 局限与区别：其安全性分析未正式建立RBR可靠性，且文中知识可靠性界有多余因子，本文的方法提供了更优的界。

### 核心技术与方案
本文的核心技术路线分为三个层次：首先，证明FRI协议及其变体Batched FRI的逐轮（RBR）可靠性。其次，提出一个称为 **δ相关IOP** 的通用框架，并证明如果基础协议在敌手总是发送低阶多项式时是RBR可靠的，则它在一般敌手（敌手发送接近低阶多项式的函数）下也是RBR可靠的，且仅有一个可控的损失因子。最后，将上述工具应用于Plonk-like协议（抽象为 **OPlonky**），证明其0相关形式的RBR可靠性，并结合Batched FRI的RBR可靠性，确立其最终的Fiat-Shamir安全性。

**FRI的RBR可靠性证明**：证明的关键在于定义“厄运”状态。对于FRI的折叠阶段，如果当前函数 $G_i$ 远离RS码，则协议处于厄运状态。当敌手在新一轮中发送函数 $G_{i+1}'$ 时，协议离开厄运状态的概率等于敌手“侥幸成功”的概率，即 $G_{i+1}' = G_{i+1}$（诚实计算的结果）且 $G_{i+1}$ 恰好是δ接近RS码的。这个概率被上界为 $\varepsilon_1 = O(2^{2n}/(\rho^{3/2}|\mathbb{F}|))$。对于查询阶段，如果所有查询检查都通过，协议离开厄运状态的概率是 $(1-\delta)^\ell$。因此，整个FRI协议的RBR可靠性误差为 $\max\{\varepsilon_1, (1-\delta)^\ell\}$。RBR知识可靠性的证明类似：如果敌手能以高于该误差的概率使状态离开厄运，则必然可以从中提取出有效的低阶近似函数。

**δ相关IOP与RBR可靠性的传递**：本文定义了δ相关IOP，其中验证者有一个用于检查一组函数是否在某个共同大子集上与低阶多项式一致的预言机。关键的定理是：如果一个0相关IOP是RBR可靠的，那么构造一个δ相关IOP，其RBR可靠性误差为 $\varepsilon_0 / (2\sqrt{\rho}\eta)$，其中 $\delta = 1 - \sqrt{\rho} - \eta$。证明思路如下：如果当前状态在δ相关IOP中是厄运的，则所有与之δ相关的低阶状态在0相关IOP中都是厄运的。通过Johnson界，这样的低阶状态数量不超过 $1/(2\sqrt{\rho}\eta)$。因此，如果敌手能以高于该损失因子的概率使状态离开厄运，则必然存在一个低阶状态能以高于 $\varepsilon_0$ 的概率离开其厄运状态，这与0相关IOP的RBR可靠性矛盾。随后，将δ相关预言机替换为一个RBR可靠的IOPP（如Batched FRI），得到的编译后IOP的可靠性误差为 $\max\{\varepsilon_{RBR}, \varepsilon_{CA}\}$。

**Plonk-like协议（OPlonky）的RBR可靠性**：本文将Plonk-like协议抽象为一个δ相关IOP，称为OPlonky。其核心是构造0相关形式（OPlonky(0)）的RBR可靠性。通过对协议每个轮次定义厄运状态（如发送多项式度数不对、复制约束不成立、主多项式在H上不消失等），并分析每个轮次中协议离开厄运状态的最大概率，证明其可靠性误差主要来源于三个部分：轮1中的随机挑战与多项式的插值偶然成立的概率 $\varepsilon_1$，轮2中随机挑战α使所有约束多项式恰好同时在H上消失的概率 $\varepsilon_2$，以及轮3中随机点z恰好是方程 $q(X)Z_H(X) - d(X) = 0$ 的根的概率 $\varepsilon_3$。总误差为 $\max\{\varepsilon_1, \varepsilon_2, \varepsilon_3\}$。结合之前的结果，可以导出OPlonky与Batched FRI编译后的SNARK的Fiat-Shamir安全性。

### 核心公式与流程

**[FRI协议的折叠方程]**
$$G_1(s) = (x_0 - s')(s'' - s')^{-1} G_0(s'') + (x_0 - s'')(s' - s'')^{-1} G_0(s')$$
> 作用：定义了FRI协议折叠阶段的核心操作，将大域上的函数 $G_0$ 线性投影到小域上的函数 $G_1$。

**[FRI的RBR可靠性误差]**
$$\varepsilon_{\mathrm{rbr}}^{\mathrm{FRI}} = \max\left\{O\left(\frac{2^{2n}}{\rho^{3/2}|\mathbb{F}|}\right), (1-\delta)^\ell\right\}$$
> 作用：给出了FRI协议在交互阶段的逐轮可靠性误差上界，是后续Fiat-Shamir安全性分析的基础。第一个项对应折叠阶段的失败概率，第二个项对应查询阶段的失败概率。

**[Batched FRI的RBR可靠性误差]**
$$\varepsilon_{\mathrm{rbr}}^{\mathrm{bFRI}} = \max\left\{O\left(\frac{2^{2n}}{\rho^{3/2}|\mathbb{F}|}\right), (1-\delta)^\ell\right\}$$
> 作用：与普通FRI的RBR可靠性误差形式相同，表明批次处理多个函数并不增加额外的可靠性损失（在适当假设下）。

**[δ相关IOP到一般IOP的RBR可靠性传递]**
$$\varepsilon_{\mathrm{compiled}} = \max\left\{\frac{\varepsilon_0}{2\sqrt{\rho}\eta}, \varepsilon_{\mathrm{CA}}\right\}$$
> 作用：核心定理之一，表明一个在0相关假设下RBR可靠的协议，在引入δ相关IOP和RBR可靠的IOPP后，编译后的整体协议的RBR可靠性误差是其组合的最大值，且包含一个由Johnson界导出的损失因子。

**[Plonk-like协议（OPlonky）的RBR可靠性误差（0相关形式）]**
$$\varepsilon = \max\left\{\left(\frac{3n(r'+u)}{|\mathbb{F}|}\right)^t, \left(\frac{|\mathcal{P}| + (s+2)t - 1}{|\mathbb{F}|}\right)^t, \frac{n \cdot \max\{\deg(P_j), u+1\}}{|\mathbb{K} \setminus D|}\right\}$$
> 作用：这是对Plonk-like协议的一个通用分析结果，给出了其在敌手发送低阶多项式条件下的RBR可靠性误差，其中三个项分别对应三个主要轮次的失败概率。

### 实验结果
论文本身是理论性工作，没有进行数值实验。然而，它通过严谨的理论分析展示了其方法的适用性和优越性。分析表明，FRI的RBR可靠性误差与已知的最佳交互式可靠性上界“[6]”紧密匹配，因此应用Fiat-Shamir变换后，预计不会引入超过协议轮数乘数的额外安全损失，这与定理中 $Q \cdot \varepsilon_{\mathrm{rbr}}$ 的形式一致。对于Plonk-like协议，以Plonky2为例，其设计指标是提供约100-bit的计算安全性。本文的分析显示，通过选择适当的参数（如并行重复次数 $t$），可以精确达到该目标，特别是在使用较小域（如64-bit Goldilocks域）时。相比之下，本文的方法避免了在某些先前工作中出现的如 $\ell^m$ 的误差项（其中 $m$ 是预言机数量，在Plonky2中可超过130），从而显著降低了安全裕度的不确定性。此外，论文指出，其分析能够改进ethSTARK协议[65]的知识可靠性界，将原先的 $\ell^2$ 因子降低为 $\ell$，这一改进已在后续的总结性工作中被确认“[39]”。这些理论结果直接为实际部署建议提供了严谨依据，例如指导协议设计者如何设置重复轮数以在效率和安全性之间取得平衡。

### 局限性与开放问题
本文的分析框架专门针对使用FRI作为低阶测试工具的协议，不适用于使用KZG等多项式承诺方案的Plonk变体。分析主要侧重于Fiat-Shamir安全性，并未完全解决交互协议的已知可靠性界与最佳已知攻击之间的差距问题，在某些参数下仍存在安全裕度的不确定性。对于ethSTARK和RISC Zero等协议，本文仅提供了RBR可靠性证明的策略性概述或部分分析，缺乏完整的形式化证明。未来的工作可以探索将这些结果扩展到KZG结合方案，并完成对更多实际协议（如RISC Zero）的完整安全性分析。

### 强关联论文

[4] Ben-Sasson, E., Bentov, I., Horesh, Y., Riabzev, M. Fast reed-solomon interactive oracle proofs of proximity. **ICALP 2018**

[9] Ben-Sasson, E., Chiesa, A., Spooner, N. Interactive oracle proofs. **TCC 2016**

[22] Canetti, R., et al. Fiat-Shamir: from practice to theory. **STOC 2019**

[6] Ben-Sasson, E., Carmon, D., Ishai, Y., Kopparty, S., Saraf, S. Proximity gaps for reed-solomon codes. **FOCS 2020**

[60] Polygon Zero Team. Plonky2: Fast recursive arguments with plonk and FRI.

[65] StarkWare. ethstark documentation. **ePrint 2021**

[44] Kattis, A.A., Panarin, K., Vlasov, A. RedShift: transparent SNARKs from list polynomial commitments. **ACM CCS 2022**

[26] Chiesa, A., Ojha, D., Spooner, N. Fractal: post-quantum and transparent recursive proofs from holography. **EUROCRYPT 2020**

[25] Chiesa, A., Manohar, P., Spooner, N. Succinct arguments in the quantum random oracle model. **TCC 2019**


## 关键词

+ FRI协议
+ Fiat-Shamir变换
+ 零知识证明
+ 多项式测试
+ 可靠性证明