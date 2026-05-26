---
title: "Definitions and properties of zero-knowledge proof systems"
标题简称:
论文类型: journal
期刊简称: Journal of Cryptology
发表年份: 1994
modified: 2025-04-08 18:38:12
---

## Definitions and properties of zero-knowledge proof systems

## 发表信息

+ [原文链接](https://link.springer.com/article/10.1007/BF00195207)

## 作者

+ [Oded Goldreich](Oded%20Goldreich.md)
+ Yair Oren

## 笔记

### 背景与动机

零知识证明由 Goldwasser、Micali 和 Rackoff 在 [GMR1] 中提出，其核心思想是证明者能使验证者相信某个断言的正确性，同时验证者除了该断言本身的正确性之外学不到任何额外知识。然而，原始的 [GMR1] 定义在应用于密码学协议时存在严重缺陷。一方面，该定义下的零知识不满足顺序组合封闭性，即多个零知识子协议的串联可能不再保持零知识性质，这与“零点之和仍为零”的直观相悖。另一方面，在大型密码协议中，恶意的验证者往往基于先前阶段获取的信息（即辅助输入）来构造其消息，而 [GMR1] 定义未考虑验证者拥有此类先验信息的情况，因此无法保证在这种场景下协议的安全性。本文旨在填补这些空白，引入更适用于密码学应用的零知识定义，并系统研究零知识证明系统必须拥有的本质属性。

### 相关工作

[GMR1] Goldwasser 等人. The knowledge complexity of interactive proof systems. **STOC 1985** [Google Scholar](https://scholar.google.com/scholar?q=The+knowledge+complexity+of+interactive+proof+systems)
> 核心思路：首次提出零知识交互证明的概念，定义了知识复杂性。
> 局限与区别：该定义未考虑验证者拥有辅助输入的情况，且不满足顺序组合封闭性，无法直接用于大型密码协议的设计。

[GMW1] Goldreich 等人. Proofs that yield nothing but their validity and a methodology of cryptographic protocol design. **FOCS 1986** [Google Scholar](https://scholar.google.com/scholar?q=Proofs+that+yield+nothing+but+their+validity+and+a+methodology+of+cryptographic+protocol+design)
> 核心思路：展示了零知识证明在密码协议设计中的广泛应用，例如图同构的零知识证明。
> 局限与区别：该工作中的协议均基于黑盒模拟证明，其零知识性质在何种定义下成立尚待形式化分析。

[GMW2] Goldreich 等人. How to play any mental game or a completeness theorem for protocols with honest majority. **STOC 1987** [Google Scholar](https://scholar.google.com/scholar?q=How+to+play+any+mental+game+or+a+completeness+theorem+for+protocols+with+honest+majority)
> 核心思路：提出了一种编译器，可将弱攻击模型下的安全协议转化为强攻击模型下的安全协议，其安全性依赖于NP语言的零知识证明。
> 局限与区别：该编译器依赖于零知识证明的组合性质，而原始 [GMR1] 定义无法证明这一性质，因此需要一个更强的定义（即辅助输入零知识）。

[FS] Feige 和 Shamir. 个人通信.
> 核心思路：指出了 [GMR1] 零知识定义不满足组合封闭性的问题。
> 局限与区别：该工作仅指出了问题，并未提出解决方案或新的定义。

[GK] Goldreich 和 Krawczyk. On the composition of zero-knowledge proof systems. **ICALP 1990** [Google Scholar](https://scholar.google.com/scholar?q=On+the+composition+of+zero-knowledge+proof+systems)
> 核心思路：系统研究了零知识证明的并发组合问题，展示了 [GMR1] 定义下并发组合可能破坏零知识性。
> 局限与区别：该工作证明了并发组合的困难性，而本文关注的顺序组合对于辅助输入零知识是成立的。

[GMS] Goldreich 等人. Interactive proof systems: provers that never fail and random selection. **FOCS 1987** [Google Scholar](https://scholar.google.com/scholar?q=Interactive+proof+systems:+provers+that+never+fail+and+random+selection)
> 核心思路：研究了具有完美可靠性的交互证明系统（Las Vegas 证明），指出此类语言属于NP。
> 局限与区别：本文在此基础上进一步证明了具有Las Vegas零知识的语言必然属于RP，揭示了错误概率的必要性。

[AH1] Aiello 和 Hastad. Perfect zero-knowledge languages can be recognized in two rounds. **FOCS 1987** [Google Scholar](https://scholar.google.com/scholar?q=Perfect+zero-knowledge+languages+can+be+recognized+in+two+rounds)
> 核心思路：证明了完美零知识语言可以在两轮交互中识别。
> 局限与区别：该工作依赖于原始 [GMR1] 定义或更强的定义，而本文在两轮协议平凡性证明中利用了辅助输入零知识的更强要求，因而得到了不同结论。

[AH2] Aiello 和 Hastad. Relativized perfect zero-knowledge is not BPP. **Information and Computation 1992** [Google Scholar](https://scholar.google.com/scholar?q=Relativized+perfect+zero-knowledge+is+not+BPP)
> 核心思路：通过相对化证明，展示了相对于某个预言机，存在非BPP语言的两轮完美零知识证明。
> 局限与区别：该结果适用于 [GMR1] 定义，而本文证明在辅助输入零知识定义下，两轮协议必然是平凡的，因此该结果不矛盾。

[BCC] Brassard 等人. Minimum disclosure proofs of knowledge. **J. Comput. System Sci. 1988** [Google Scholar](https://scholar.google.com/scholar?q=Minimum+disclosure+proofs+of+knowledge)
> 核心思路：引入了零知识论证的概念，其可靠性的要求从无条件安全放宽为计算安全性。
> 局限与区别：本文的部分平凡性结果可扩展到零知识论证，因为构造的“欺骗证明者”是有效的。

### 核心技术与方案

本文的核心贡献分为两部分：新定义体系的建立与性质研究，以及零知识证明系统必要性质的证明。

在第一部分，文章首先引入**辅助输入零知识**的定义。该定义要求，对于任意概率多项式时间验证者 $V^*$ ，存在一个概率多项式时间模拟器 $M_{V^*}$ ，使得对于任意公共输入 $x \in L$ 和任意辅助输入 $y \in \{0,1\}^*$ ，分布族 $\{\langle P(x), V^*(x, y) \rangle\}_{x; y}$ 和 $\{M_{V^*}(x, y)\}_{x; y}$ 是多项式时间不可区分的。相比于原始 [GMR1] 定义，该定义明确考虑了验证者拥有先验知识的情况，并要求模拟器在输入辅助输入 $y$ 时也能产生与真实交互不可区分的输出。然后，文章引入**黑盒模拟零知识**的定义，其要求存在一个通用的概率多项式时间模拟器 $M_u$ ，对于任意验证者 $V^*$ ， $M_u$ 能够通过黑盒方式（即仅需调用 $V^*$ 的输入输出功能）模拟 $V^*$ 与证明者 $P$ 的交互。文章的关键定理是证明了 $Cl(\text{blackbox-simulation}) \subseteq Cl(\text{auxiliary-input})$ ，证明策略是利用黑盒模拟器 $M_u$ 来构建特定验证者 $V^*$ 的模拟器 $M_{V^*}$ 。具体地，对于给定的 $V^*$ 和辅助输入 $y$ ，构造一个将 $y$ 内嵌的验证者 $V_y^*$ ，然后运行 $M_u$ 并给予其黑盒访问 $V_y^*$ 的权限，最后在输出中添加 $y$ 。该构造的核心保障是，若 $M_u$ 能模拟任何黑盒验证者，则 $M_{V^*}$ 能模拟任何拥有辅助输入的特定验证者。基于此定理，所有已知的黑盒模拟零知识协议（如[GMR1]和[GMW1]中的协议）自动成为辅助输入零知识，从而可以安全地用于密码学协议组合。

文章进一步证明了辅助输入零知识在顺序组合下是封闭的。其证明思路是：对于 $k$ 个子协议的顺序组合，模拟器 $M_{V^*}$ 通过迭代调用每个子协议的模拟器 $M_{V'}^i$ 来构建整体模拟。关键在于构造一个“有状态的”验证者 $V'$ ，它能够接收前一步的历史描述作为辅助输入，从而恢复出验证者 $V^*$ 在该时刻的状态。通过混合参数论证，如果某个区分器能够区分整体模拟和真实交互，则必然存在一个 $i$ 使得该区分器能区分第 $i$ 个子协议的模拟，从而导出矛盾。

在第二部分，文章证明了零知识证明系统的一系列必要性质，即若缺少某些性质，则语言必然属于BPP，从而证明是平凡的。定理4.1证明具有Las Vegas零知识（即从不接受 $x \notin L$ 的实例）的语言必然属于RP。核心思想是，对于 $x \notin L$ ，不存在任何接受的历史；对于 $x \in L$ ，模拟器 $M_V$ 必须以极高概率产生接受的历史；因此，一个简单的算法（运行 $M_V$ 并检查是否输出接受历史）就能在 $x \in L$ 时高概率接受，在 $x \notin L$ 时永不接受，满足RP的定义。定理4.2将此结果推广到具有确定性验证者的零知识证明，通过展示可以将此类协议修改为Las Vegas形式。定理4.3证明一轮零知识协议是平凡的，通过用随机的新随机数替换模拟器生成的随机数，利用协议的可靠性来保证对 $x \notin L$ 的拒绝，并利用零知识性质保证对 $x \in L$ 的接受。

定理4.4是两轮辅助输入零知识协议的平凡性证明，这是对一轮结果的推广。其证明策略与一轮类似，但利用了辅助输入的定义来向模拟器隐藏验证者的随机数 $r$ 。构造的BPP机器随机选择一个 $r$ 并计算 $\beta^* = V(x, r)$ ，然后运行模拟器 $M_{V^*}(x, \beta^*)$ 来获得证明者的回答 $\alpha$ 。由于模拟器不知道 $r$ ，其产生的 $\alpha$ 必须与真实证明者一样，仅基于 $\beta^*$ 产生。协议的可靠性保证了对于 $x \notin L$ ，任何有效的 $\alpha$ 使得 $\rho(x, r, \alpha)$ 接受的概率极低；完备性保证了对于 $x \in L$ ，模拟器产生的 $\alpha$ 能以高概率使得 $\rho(x, r, \alpha)$ 接受。该证明依赖于非均匀多项式不可区分性，以便区分器能够利用真实的随机数 $r$ 作为辅助输入来检测模拟的失败。文章指出，由于该证明相对化，且[AH2]证明了存在相对化的预言机使得两轮[GMR1]零知识不等于BPP，因此本结果不适用于原始[GMR1]定义。

定理4.5证明具有确定性证明者的辅助输入零知识协议是平凡的。证明策略是利用确定性带来的“唯一性”：给定 $x$ 和随机数 $r$ ，整个交互由 $r$ 唯一确定。BPP机器通过迭代构造对话：先获得 $\alpha_0$ ，然后计算 $\beta_1 = V(x, r, \alpha_0)$ ，再将 $[\beta_1]$ 作为辅助输入给一个构造的验证者 $V^*$ ，利用其模拟器获得 $\alpha_1$ ，并确保此 $\alpha_1$ 与之前基于 $r$ 的唯一 $\alpha_1$ 一致（这由“单元素引理”保证，该引理说明若一个分布族高度集中于一个元素，则其多项式不可区分的分布族也必然高度集中于同一元素）。重复此过程即可重建整个唯一对话，从而判断接受与否。该证明同样相对化，因此不适用于[GMR1]定义。

### 核心公式与流程

**[辅助输入零知识定义]**
概率多项式时间算法 $V^*$  和 $M_{V^*}$ ，使得 $\forall x \in L, \forall y \in \{0,1\}^*$，分布族 $\{\langle P(x), V^*(x, y) \rangle\}_{x; y}$ 与 $\{M_{V^*}(x, y)\}_{x; y}$ 多项式时间不可区分。
> 作用：定义了满足密码学应用需求的零知识性质，允许验证者拥有任意先验知识，并支持顺序组合。

**[黑盒模拟零知识定义]**
存在概率多项式时间机器 $M_u$，使得 $\forall$ 概率多项式时间 $V^*$，分布族 $\{\langle P(x), V^*(x) \rangle\}_x$ 与 $\{M_u^{V^*}(x)\}_x$ 多项式时间不可区分（区分器可黑盒访问 $V^*$）。
> 作用：形式化了所有已知零知识协议的证明方法，即通过一个通用模拟器对所有验证者进行黑盒模拟。

**[两轮辅助输入零知识协议平凡性证明算法]**
$$M(x): \\
1.\ r \leftarrow_R \{0,1\}^{l_r(|x|)};\ \beta^* := V(x, r)\\
2.\ \text{运行 } M_{V^*}(x, \beta^*); \text{ 若产生合法历史 } [x, \beta^*, r', (\beta^*, \alpha)], \text{ 则转3; 否则拒绝}\\
3.\ \text{输出 } \rho(x, r, \alpha)$$
> 作用：通过向模拟器隐藏随机数 $r$，将模拟器视为证明者，利用原协议的可靠性保证对非语言的拒绝，利用零知识性质保证对语言的接受。

**[单元素引理]**
设 $\{\pi_1^x\}$ 与 $\{\pi_2^x\}$ 多项式时间不可区分，且 $\pi_1^x(\sigma_x) \geq 1 - \varepsilon$，$\{\pi_2^x\}$ 可在多项式时间内抽样。则对几乎所有 $x$，$\pi_2^x(\sigma_x) > 1 - 2\varepsilon$。
> 作用：用于确定性证明者的协议平凡性证明，保证模拟器产生的唯一对话与真实协议中由随机数 $r$ 确定的唯一对话相同。

### 实验结果

本文为纯粹的理论研究工作，不包含实验验证。所有结论均基于数学证明，包括定义之间的关系证明（如定理3.2和3.3）、以及多个平凡性定理（定理4.1至4.5），这些证明均以构造性方法给出，不涉及数值模拟或基准测试。

### 局限性与开放问题

本文建立的理论框架虽然深刻，但依赖于非均匀多项式不可区分性假设（在两轮和确定性证明者的平凡性证明中），这在实际应用中可能是一个较强的假设。此外，文章未解决辅助输入零知识与黑盒模拟零知识之间是否完全等价的问题，仅证明了前者包含于后者。关于并发组合是否适用于辅助输入零知识，文章仅提到了[GK]的负结果，未给出自己的解决方案。对于随机数在零知识中的必要性，文章虽然证明了确定性证明者的协议是平凡的，但并未完全排除在更强的计算假设下存在非平凡此类协议的可能性。

### 强关联论文

[GMR1] Goldwasser 等人. The Knowledge Complexity of Interactive Proof Systems. **STOC 1985** [Google Scholar](https://scholar.google.com/scholar?q=The+Knowledge+Complexity+of+Interactive+Proof+Systems)

[GMW1] Goldreich 等人. Proofs that Yield Nothing but their Validity and a Methodology of Cryptographic Protocol Design. **FOCS 1986** [Google Scholar](https://scholar.google.com/scholar?q=Proofs+that+Yield+Nothing+but+their+Validity+and+a+Methodology+of+Cryptographic+Protocol+Design)

[GMW2] Goldreich 等人. How to Play any Mental Game or a Completeness Theorem for Protocols with Honest Majority. **STOC 1987** [Google Scholar](https://scholar.google.com/scholar?q=How+to+Play+any+Mental+Game+or+a+Completeness+Theorem+for+Protocols+with+Honest+Majority)

[GK] Goldreich 等人. On the Composition of Zero-Knowledge Proof Systems. **ICALP 1990** [Google Scholar](https://scholar.google.com/scholar?q=On+the+Composition+of+Zero-Knowledge+Proof+Systems)

[GMS] Goldreich 等人. Interactive Proof Systems: Provers that Never Fail and Random Selection. **FOCS 1987** [Google Scholar](https://scholar.google.com/scholar?q=Interactive+Proof+Systems:+Provers+that+Never+Fail+and+Random+Selection)

[AH1] Aiello 等人. Perfect Zero-Knowledge Languages Can Be Recognized in Two Rounds. **FOCS 1987** [Google Scholar](https://scholar.google.com/scholar?q=Perfect+Zero-Knowledge+Languages+Can+Be+Recognized+in+Two+Rounds)

[AH2] Aiello 等人. Relativized Perfect Zero-Knowledge Is Not BPP. **Information and Computation 1992** [Google Scholar](https://scholar.google.com/scholar?q=Relativized+Perfect+Zero-Knowledge+Is+Not+BPP)

[BCC] Brassard 等人. Minimum Disclosure Proofs of Knowledge. **J. Comput. System Sci. 1988** [Google Scholar](https://scholar.google.com/scholar?q=Minimum+Disclosure+Proofs+of+Knowledge)


## 关键词

+ 零知识证明安全性定义
+ 辅助输入零知识
+ 黑盒模拟零知识
+ 密码学协议组合安全
+ 零知识平凡性分类
+ 交互证明系统基础