---
title: "Fairness in an unfair world: Fair multiparty computation from public bulletin boards"
doi: 10.1145/3133956.3134092
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2017
created: 2025-04-29 10:33:21
modified: 2025-04-29 10:34:47
---
## Fairness in an unfair world: Fair multiparty computation from public bulletin boards

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3133956.3134092)

## 作者

+ [Arka Rai Choudhuri](Arka%20Rai%20Choudhuri.md)
+ [Matthew Green](Matthew%20Green.md)
+ [Abhishek Jain](Abhishek%20Jain.md)
+ Gabriel Kaptchuk 
+ [Ian Miers](Ian%20Miers.md)
## 笔记

### 背景与动机
安全多方计算允许互不信任的参与方在保护各自输入隐私的前提下共同计算一个函数。一个自然且重要的安全要求是公平性：要么所有参与方都获得输出，要么没有任何一方获得。该性质在电子拍卖、合同签署等场景中至关重要，例如参与方可能利用信息不对称获取不正当优势。Cleve 于 STOC 1986 证明了一个根本性的不可能结论 [25]：当不诚实参与方占多数时，即使借助可信设置，针对一般函数的公平MPC也是无法实现的。为绕过此障碍，现有研究大致分为两派：一是针对受限函数类在标准模型下实现公平性 [7-9, 45, 47]；二是通过增强模型或放宽公平性定义来为一般函数提供妥协方案，例如引入第三方恢复公平 [20]、实现 Δ-公平性 [13, 31, 34, 42, 59, 60] 或对违规方施加经济惩罚 [6, 17, 52, 53]。然而这些方案要么依赖难以寻觅的可信第三方，要么需要精确估计敌手的计算能力与动机，当输出价值极高时威慑力不足。本文旨在利用现有的公共公告板基础设施填补这一空白，在无需可信设置与敌手估值的前提下，首次为一般函数实现标准意义上的完全公平MPC。

### 相关工作
[25] Cleve et al. Limits on the Security of Coin Flips when Half the Processors Are Faulty. **STOC 1986** [Google Scholar](https://scholar.google.com/scholar?q=Limits+on+the+Security+of+Coint+Flips+when+Half+the+processors＋Are+Faulty)
> 核心思路：证明当超过一半参与方不诚实时，公平的通用多方计算是不可能的。
> 局限与区别：该结论是本文努力克服的理论瓶颈，而本文通过引入公告板模型来绕过这一不可能结果。

[6] Andrychowicz et al. Secure Multiparty Computations on Bitcoin. **IEEE S&P 2014** [Google Scholar](https://scholar.google.com/scholar?q=Secure+Multiparty+Computations+on+Bitcoin)
> 核心思路：利用比特币脚本实现带惩罚的公平MPC，违约方需支付罚金。
> 局限与区别：其目标仅为公平性惩罚而非标准公平性；当违约方评估输出价值高于罚金时，威慑失效。

[17] Bentov et al. How to Use Bitcoin to Design Fair Protocols. **CRYPTO 2014** [Google Scholar](https://scholar.google.com/scholar?q=How+to+Use+Bitcoin+to+Design+Fair+Protocols)
> 核心思路：系统性地用区块链实现公平交换与MPC的惩罚机制。
> 局限与区别：同样只保障“公平惩罚”而非完全公平，且依赖于参与者对惩罚成本与输出价值的比较。

[59] Pass et al. Formal Abstractions for Attested Execution Secure Processors. **EUROCRYPT 2017** [Google Scholar](https://scholar.google.com/scholar?q=Formal+Abstractions+for+Attested+Execution+Secure+Processors)
> 核心思路：在配备安全时钟的安全硬件模型中实现 Δ-公平性，确保诚实方至晚在Δ倍于敌手的时间内获得输出。
> 局限与区别：Δ 值由敌手控制，实际中可被设置得极大；本文虽也使用安全硬件，但无需安全时钟，且实现的是完全公平。

[39] Gentry et al. Witness Encryption from Instance Independent Assumptions. **CRYPTO 2014** [Google Scholar](https://scholar.google.com/scholar?q=Witness+Encryption+from+Instance+Independent+Assumptions)
> 核心思路：提出基于实例独立假设的见证加密构造。
> 局限与区别：本文将其用作理论构造的底层组件，但现有见证加密方案效率极低，仅作为可行性证明。

### 核心技术与方案
本文提出两种基于公共公告板的公平MPC方案，均采用运行一个（可能不公平的）MPC协议来计算一个加密函数输出的方式，再设计一个特殊的解密过程确保解密权对双方是相等的。关键洞察在于：公告板提供了一种公开、不可伪造的发布机制，使得任何一方获得解密所需的信息时，另一方也能从公告板上获取相同信息。

**方案一：基于见证加密的理论构造。**
该方案将公告板建模为提供不可伪造证明（通过唯一签名或证明机制）的公共账本，并支持撤销（rewind）操作。方案使用了填充参数 $\Delta t$ 定义语言 $L_{WE, \Delta t}$，其中语句包含函数值 $\{y_i\}_{i \in [n]}$ 和一个截止轮次 $T$，见证由秘密值 $\{\rho_i\}_{i \in [n]}$、公告板上的时间戳 $t \in \{T, \dots, T+\Delta t\}$ 以及对应的认证标签 $\sigma$ 组成。由于 $f$ 是单射单向函数且签名唯一，每个语句的见证集合规模为 $\Delta t + 1$，是一个多项式语言，从而标准的见证加密蕴含可提取见证加密。协议流程分为两个阶段：第一阶段，各方运行一个 $\mathcal{F}'_{\Delta t}$ 理想函数，该函数计算所有秘密值的单向函数值并提供关于输出 $F(x_1,\dots,x_n)$ 的见证加密密文；第二阶段，各方交换秘密值 $\rho_i$，若所有值都正确则将其发布到公告板上，任何一方都能从板上获取见证并解密。诚实方在截止时间 $T+\Delta t$ 之前监视公告板，一旦发现有效发布即获取输出。安全证明要求模拟器支持重绕（rewind）公告板以估计敌手的中止概率，从而在预期多项式时间内成功强制输出。假设包括单射单向函数、唯一签名和见证加密的安全性；当使用标准签名或权益证明时，需采用更强的可提取见证加密。

**方案二：基于安全硬件的实用构造。**
该方案使用 Intel SGX 等安全处理器替代见证加密。每个参与方的 SGX 芯片安装程序 $\text{prog}_{\text{fair}}$，该程序实现一个条件解密引擎。协议首先由 SGX 执行密钥交换生成密钥 $K$，并为每个参与方分配密钥份额 $k_i$ 和释放令牌份额 $\rho_i$，同时输出对这些份额的承诺。随后参与方以各自输入 $x_i$、密钥份额 $k_i$、随机数 $r_i$ 和承诺为输入运行一个标准 MPC（文中采用 SPDZ-2 实现），该 MPC 验证所有提交份额与承诺的一致性，若一致则输出函数值在密钥 $K$ 下的认证加密密文。此后各方交换 $\rho_i$ 并能将其发布到公告板上。解密时，需向本地 SGX 提供密文、释放令牌（已发布或收到的）及其公告板证明，SGX 验证 $f(\rho)=y$ 和时间戳 $t$ 在窗口 $[T, T+\Delta t]$ 内，若通过则用 $K$ 解密输出。由于模拟器可以观察并干预敌手对 SGX 的查询，可在敌手试图解密时再向理想函数查询真实输出并直接编程 SGX 的输出，因此无需重绕，公告板可建模为全局功能。安全性基于单向函数、存在性不可伪造签名、认证加密的 INT-CTXT 和语义安全、承诺的隐藏与绑定性以及 DDH 假设。该方案完全脱离了低效的多线性映射，可直接使用现有硬件和密码库实现。

### 核心公式与流程
**[语言 $L_{WE,\Delta t}$ 的定义（方案一）]**
$$L_{WE,\Delta t} = \left\{( \{y_i\}_{i\in[n]}, T) \mid \exists (t, \sigma, \{\rho_i\}_{i\in[n]}) \text{ s.t. } \forall i\in[n], y_i = f(\rho_i) \land t \in \{T,\dots,T+\Delta t\} \land \text{Verify}_{BB}\big((t||\rho_1||\dots||\rho_n), \sigma\big) = 1 \right\}$$
> 作用：定义了方案一中见证加密所绑定的语句。语句包含图像值集合和一个截止时间，见证是秘密值、时间戳和公告板签名的组合。利用单射单向函数和唯一签名保证每个语句仅有 $\Delta t+1$ 个多项式个见证，从而标准见证加密蕴含可提取安全。

**[理想函数 $\mathcal{F}'_{\Delta t}$ 的功能（方案一）]**
$$\mathcal{F}'_{\Delta t}\big((x_1,\rho_1,t_1),\dots,(x_n,\rho_n,t_n)\big) = \big(c, \{f(\rho_i)\}_{i\in[n]}, T\big)$$
其中 $T=\max(t_1,\dots,t_n)$ 且 $c = \text{WE.Enc}\big(x_{WE}, \mathcal{F}(x_1,\dots,x_n)\big)$，语句 $x_{WE} = (\{f(\rho_i)\}_{i\in[n]}, T)$。
> 作用：定义了方案一中第一阶段 MPC 需要计算的混合世界理想函数。该函数接收每个参与方的输入、随机令牌和当前公告板计数器，输出所有令牌的单向函数值、截止时间 $T$，以及一个关于函数真实输出的见证加密密文。

**[SGX 解密条件（方案二）]**
$$t \in \{T, T+1, \dots, T+\Delta t\} \land f(\rho) = y \land \text{Ver}_{BB}(t, \rho, \sigma) = 1$$
> 作用：规定了方案二中 SGX 条件解密的三个必要条件：当前公告板时间戳在有效窗口内，发布的值 $\rho$ 的单向函数值等于 MPC 阶段已公开的 $y$，且公告板签名的认证通过。

**[安全游戏不可区分性定义]**
$$
\operatorname{IDEAL}_{\operatorname{Sim},F}(1^\lambda, \vec{x}, z) \approx_c \operatorname{REAL}_{\mathcal{A},\Pi}(1^\lambda, \vec{x}, z)
$$
> 作用：定义了完全公平安全多方计算的标准安全模型：对于任意实际敌手，存在一种理想世界模拟器，使得两个实验的输出在计算上不可区分。

### 实验结果
论文实现了基于安全硬件的方案，实验设置如下：公告板使用比特币 Testnet；MPC 采用 SPDZ-2 框架，并实现了基于 3 轮 AES 的认证加密来生成密文；SGX 部分基于 Obscuro 项目改造为条件解密器，运行在 Intel i5-6600K 3.5GHz 处理器上。实验针对线性搜索（n=100,500,1000）测试了两方设置。公平性引入的 MPC 开销极低：线性搜索 100、500、1000 条目时，公平性开销（额外 AES 加密时间）分别为 0.08s、0.07s、0.06s，而 MPC 在线总运行时间分别为 0.03s、0.30s、0.66s——加密部分占比极少，当问题规模增大时开销更加微不足道。SGX 性能方面，初始化（含密钥发行、秘密分发）平均耗时 1.180s（master）、0.002s（minion）；条件解密（包括验证公告板签名和 AES 解密）平均仅需 0.039s（master）、0.037s（minion），均在实用范围内。MPC 在线运行 AES 组件的时间随参与方数量增加而线性增长，2 方时为 0.07s，6 方时为 0.21s，仍保持在十分之几秒量级，证明了方案的可扩展性。

### 局限性与开放问题
本文基于见证加密的理论方案依赖低效的多线性映射构造，仅具可行性价值；能否从哈希证明系统等更简单的假设构造针对特定语言的见证加密是一个重要开放问题。基于安全硬件的方案虽然实用，但其安全性依赖于 Intel SGX 等硬件的抗攻击假设，近期 SGX 侧信道攻击可能构成威胁。此外，两个方案的安全性证明都假定了公告板目录不可伪造，实际部署时需要谨慎选择公告板实现并评估信任假设。

### 强关联论文

[25] Cleve et al. Limits on the Security of Coin Flips when Half the Processors Are Faulty. **STOC 1986** [Google Scholar](https://scholar.google.com/scholar?q=Limits+on+the+Security+of+Coin+Flips+when+Half+the+Processors+Are+Faulty)

[6] Andrychowicz et al. Secure Multiparty Computations on Bitcoin. **IEEE S&P 2014** [Google Scholar](https://scholar.google.com/scholar?q=Secure+Multiparty+Computations+on+Bitcoin)

[17] Bentov et al. How to Use Bitcoin to Design Fair Protocols. **CRYPTO 2014** [Google Scholar](https://scholar.google.com/scholar?q=How+to+Use+Bitcoin+to+Design+Fair+Protocols)

[59] Pass et al. Formal Abstractions for Attested Execution Secure Processors. **EUROCRYPT 2017** [Google Scholar](https://scholar.google.com/scholar?q=Formal+Abstractions+for+Attested+Execution+Secure+Processors)

[39] Gentry et al. Witness Encryption from Instance Independent Assumptions. **CRYPTO 2014** [Google Scholar](https://scholar.google.com/scholar?q=Witness+Encryption+from+Instance+Independent+Assumptions)

[19] Boyle et al. On Extractability Obfuscation. **TCC 2014** [Google Scholar](https://scholar.google.com/scholar?q=On+Extractability+Obfuscation)

[20] Cachin et al. Optimistic Fair Secure Computation. **CRYPTO 2000** [Google Scholar](https://scholar.google.com/scholar?q=Optimistic+Fair+Secure+Computation)

[34] Garay et al. Resource Fairness and Composability of Cryptographic Protocols. **TCC 2006** [Google Scholar](https://scholar.google.com/scholar?q=Resource+Fairness+and+Composability+of+Cryptographic+Protocols)

[46] Gordon et al. On Complete Primitives for Fairness. **TCC 2010** [Google Scholar](https://scholar.google.com/scholar?q=On+Complete+Primitives+for+Fairness)

[29] Damgard et al. Practical Covertly Secure MPC for Dishonest Majority – or: Breaking the SPDZ Limits. **ePrint 2012** [Google Scholar](https://scholar.google.com/scholar?q=Practical+Covertly+Secure+MPC+for+Dishonest+Majority+–+or+Breaking+the+SPDZ+Limits)


## 关键词

+ 公平多方计算
+ 见证加密
+ 可信硬件
+ 公告板
+ 区块链