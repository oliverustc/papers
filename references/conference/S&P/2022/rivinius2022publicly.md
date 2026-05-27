---
title: "Publicly accountable robust multi-party computation"
doi: 10.1109/sp46214.2022.9833608
标题简称:
论文类型: conference
会议简称: S&P
发表年份: 2022
created: 2025-05-23 01:09:23
modified: 2025-05-23 01:09:40
---
## Publicly accountable robust multi-party computation

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/9833608)

## 作者

+ Marc Rivinius
+ Pascal Reisert
+ [Daniel Rausch](Daniel%20Rausch.md)
+ [Ralf Küsters](Ralf%20K%C3%BCsters.md)
## 笔记

### 背景与动机
在客户端-服务器模型的大规模应用中，如隐私保护云计算、电子投票和拍卖，安全多方计算（MPC）协议需要满足严苛的安全要求：计算结果应可公开验证，任何恶意方应能被识别并追究责任，且恶意方不应能破坏计算、强制协议重启或阻止诚实方获得正确结果。现有高效的SPDZ类两阶段协议大多仅提供中止安全性（输出正确或协议中止），而缺乏对公开可验证性、强公开可问责性和鲁棒性的同时支持。Cunningham等人的协议 [14] 是唯一具备强公开可识别中止的SPDZ类协议，但不具备鲁棒性。将具有可识别中止的协议与“两全其美”（BoBW）通用转换 [41], [42] 结合，虽可提供鲁棒性，但会引入高达O(n)的性能损失，且要求客户端在每次重启时重新提供输入，这在高信任场景（如选举）中不可接受。因此，本文旨在填补这一空白：构建首个同时满足强公开可问责性（含公开可验证性）和鲁棒性，且无需协议重启的高效两阶段MPC协议。

### 相关工作

[10] Baum, C. et al. Publicly Auditable Secure Multi-Party Computation. **SCN 2014**
> 核心思路：提出了一个具有公开可审计性的SPDZ类协议。
> 局限与区别：该协议不具备鲁棒性，且其公开可验证性仅针对部分恶意方（非强性质）。本文需要更强、更全面的组合安全属性。

[11] Baum, C. et al. Efficient Secure Multiparty Computation with Identifiable Abort. **TCC 2016-B**
> 核心思路：实现了具有可识别中止的高效MPC。
> 局限与区别：该协议不具备强公开可识别中止（其安全性在敌手控制所有服务器时失效），也未考虑鲁棒性。本文的目标是更强的、对所有服务器都适用的可问责性。

[14] Cunningham, R. K. et al. Catching MPC Cheaters: Identification and Openability. **ICITS 2017**
> 核心思路：提出了第一个具有强公开可识别中止的SPDZ类协议，使用Pedersen承诺。
> 局限与区别：该协议不具备鲁棒性，无法阻止恶意方中止计算。本文将其扩展为具有鲁棒性的协议，并改用格基承诺以获得更好的协同效应和参数效率。

[28] Baum, C. et al. Efficient Constant-Round MPC with Identifiable Abort and Public Verifiability. **CRYPTO 2020**
> 核心思路：实现了常数轮、具有可识别中止和公开可验证性的MPC。
> 局限与区别：同 [11]，不具备强安全性质，且不提供鲁棒性。本文的协议在实现更强安全属性的同时，提供了更好的渐近复杂度（例如在线通信复杂度为n·|f|对n²·|f|）。

[41] Hirt, M. et al. A Dynamic Tradeoff between Active and Passive Corruptions in Secure Multi-Party Computation. **CRYPTO 2013**
> 核心思路：提出了“两全其美”的通用框架，可将具有可识别中止的协议转换为具有鲁棒性的协议。
> 局限与区别：该框架基于协议迭代，会带来O(n)的性能损失并要求客户端重新输入，本文通过阈值秘密共享避免了这种开销。

[42] Patra, A. et al. Beyond Honest Majority: The Round Complexity of Fair and Robust Multi-party Computation. **ASIACRYPT 2019**
> 核心思路：另一个“两全其美”协议，针对超过半数的敌手进行优化。
> 局限与区别：同 [41]，依赖协议迭代。本文的协议无需迭代，因此在线效率更高且适用于不允许重启的场景。

[45] Baum, C. et al. More Efficient Commitments from Structured Lattice Assumptions. **SCN 2018**
> 核心思路：提出了高效的基于结构化格（Module-SIS/LWE）的承诺方案（BDLOP）。
> 局限与区别：该方案原始的加法同态性不足以支持SPDZ协议中的一次Beaver乘法后的安全运算。本文对其进行了推广，通过使用两个独立模数来解决此问题，从而为在线阶段提供足够的安全性和同态能力。

[15] Keller, M. et al. Overdrive: Making SPDZ Great Again. **EUROCRYPT 2018**
> 核心思路：提出了Overdrive系列协议中的LowGear，一种高效的基于BGV加密的SPDZ离线阶段方案。
> 局限与区别：LowGear不具备公开可验证性或可问责性。本文的离线阶段借鉴了其思想，但通过添加承诺和可验证的NIZKP来实现可问责性，并设计了新的密文乘法协议。

[16] Baum, C. et al. Using TopGear in Overdrive: A More Efficient ZKPoK for SPDZ. **SAC 2019**
> 核心思路：提出了TopGear，通过聚合所有参与方的零知识证明来提高SPDZ离线阶段的效率。
> 局限与区别：其聚合技术使得识别单个恶意方变得困难，因此不适用于本文的公开可问责目标。本文采用了不同的证明聚合策略，并首次在这种设置下结合了经典聚合 [49] 和拒绝采样 [50] 技术。

### 核心技术与方案

本文提出的协议是一个SPDZ类两阶段协议，由在线阶段、离线阶段和设置阶段组成，其核心思想是扩展SPDZ协议以支持阈值秘密共享，并与一个改进的同态承诺方案相结合，从而实现鲁棒性和公开可问责性。

**在线阶段**：其核心在于使用一个改进的格基公开承诺方案（基于BDLOP [45]），对每个参与方的秘密共享份额进行承诺，形成视图。通过公开这些承诺和对应的打开信息，任何外部审计者或参与方都能验证计算的正确性。对于乘法操作，采用Beaver技术，通过预计算三元组将所需操作转化为线性运算，这些线性运算直接在视图上执行，而承诺方案的同态性确保了这些线性运算后的承诺仍然有效。为了在不依赖统计隐藏承诺和可提取性的情况下获得模拟安全性，对于最终输出，协议不是直接打开原始份额的承诺，而是通过一个零知识证明（NIZKP）来证明新承诺与旧承诺承诺了相同的值，然后打开新承诺。这避免了传统方法中为达到正确分布而需要可提取性和统计隐藏性，从而显著减小了承诺参数的大小并提高了效率。鲁棒性来源于阈值秘密共享：只要至少有t个份额是有效的，即使部分参与方失效或恶意，输出仍然可以被重构，从而避免了协议重启。

**离线阶段**：负责生成在线阶段所需的视图和Beaver三元组，同样需要保证可问责性和鲁棒性。其构造基于BGV加密方案，通过让每个参与方生成自己的“承诺性密文”（即对同一明文同时生成加密和承诺），并使用NIZKP证明其正确性。通过这些承诺性密文，可以安全地构造出份额的密文和承诺，从而生成视图。为生成三元组的c分量，协议提供了两种选择：1) 使用BGV的某种同态加密功能直接计算；2) 使用一个新颖的、仅依赖线性同态加密的乘法子协议。该子协议的工作方式是每个参与方将其份额与b的加密相乘并加上噪声进行再加密，然后通过NIZKP证明其正确性，最后重构出c的密文。此方法有助于引导密钥生成，并避免了选择性失败攻击。为了实现高效，离线阶段采用了结合经典聚合 [49] 和拒绝采样 [50] 的NIZKP技术，这在SPDZ类协议中是首次具体分析，并取得了良好的参数效果。

**设置阶段**：负责生成承诺参数和BGV的阈值公钥。密钥生成协议基于Asharov等人的方案 [67]，并利用承诺方案和NIZKPs提高了效率。通过使用全阈值密钥共享和针对每个参与方密钥份额的承诺，实现了鲁棒性和可问责性。特别地，为了生成范围证明以确保密钥足够小，本文结合了现有的NIZKPs [45], [54], [69]，设计了一种新的构造，将R_q中的元素用比特表示并证明其比特的乘积和和为0，从而证明其无穷范数有界。

安全性证明在通用可组合（UC）框架下进行，协议各自实现一个理想功能，这些理想功能天然满足鲁棒性和公开可问责性的定义。证明依赖于BGV加密方案的CPA安全性、承诺方案的计算绑定性和隐藏性，以及NIZKP的模拟可靠性和零知识性。协议实现了强性质，即即使所有计算方（服务器）都被腐化，公开可问责性仍然成立。协议的在线通信、计算和轮复杂度为O(n·|f|)（|f|为乘法门数量），优于或等于其他可识别中止协议，而离线通信复杂度略高，为O(n²·|f|)，但换来了更强的鲁棒性。

### 核心公式与流程

**[视图定义]** 对于共享值x，参与方P_i的视图⟨x⟩_i由以下部分组成：
$$
\langle x \rangle_i := ( [x]_i, \mathsf{R_C}([x]_i), \mathsf{Com}([x]_1), \dots, \mathsf{Com}([x]_n) )
$$
> 作用：每个参与方持有自己的份额、打开随机性，以及所有参与方份额的公开承诺。

**[Beaver乘法操作]** 使用三元组⟨a⟩_i, ⟨b⟩_i, ⟨c⟩_i (其中c = a·b) 来安全地计算x·y：
$$
\langle x \cdot y \rangle_i := \langle c \rangle_i + u \cdot \langle a \rangle_i + v \cdot \langle b \rangle_i + u \cdot v
$$
其中u = x - b, v = y - a是打开的掩码值。
> 作用：将非线性乘法转化为线性操作，所有操作在承诺的视图上执行，保持了承诺的结构。

**[广义BDLOP承诺]** 对明文x的承诺c = (c[0], c[1])^T：
$$
c = \binom{c[0]}{c[1]} = \binom{\mathbf{A}_0 \cdot r\ (\text{mod}\ p')}{\mathbf{A}_1 \cdot r + x\ (\text{mod}\ p)}
$$
其中A_0, A_1是公共参数矩阵，r是小随机噪声。
> 作用：通过使用两个独立模数p'和p(p|p')，可以在不增加明文模数p的前提下提高绑定性和同态性，从而安全支持Beaver乘法中的噪声增长。

**[BGV加密]** 对明文x的加密c = (c[0], c[1])^T：
$$
\mathsf{Enc}_k(x, (v, \mathbf{e})^\mathrm{T}) := \binom{k[1] \cdot v + p \cdot \mathbf{e}[0] + x}{k[0] \cdot v + p \cdot \mathbf{e}[1]}
$$
其中k = (k[0], k[1])是公钥，v, e是加密随机性噪声。
> 作用：作为离线阶段的核心加密原语，其同态性质用于生成共享和计算乘法三元组。

### 实验结果
实验设置：所有协议使用单线程实现（AMD EPYC 7443 CPU），带宽限制为1 Gbit/s，网络延迟模拟为0 ms和100 ms。统计安全参数为40 bit，计算安全参数为128 bit。评估的算术电路为“网络A”（118016个加法门，118272个乘法门），批量大小b = N = 32768。对比基线为SPDZ [7], [8] 和 Cunningham等人的协议 [14]（作为BoBW[14]的非重启近似）。在线阶段，无网络延迟时，本文协议每次评估网络A的摊还运行时间为2.0秒，相比SPDZ（0.1秒）慢约20倍，但优于Cunningham协议（0.5秒）在需识别错误时的表现（86秒）。当存在错误导致重启时，BoBW[14]（有1次重启）的摊还时间飙升至1000秒，而本文协议无此问题。离线阶段，本文协议为300秒，高于SPDZ（100秒）但低于Cunningham协议（1300秒）。在线通信方面，每参与方每乘法门，本文协议（log p=128, η=40）为1240 bit，高于SPDZ的256 bit和Cunningham的1008 bit。离线通信方面，本文协议每参与方每乘法门约为25-60 MiB（取决于n和t），高于SPDZ（8 MiB）和Cunningham（30 MiB）。对于网络A的完全评估，本文协议总通信量为在线17.48 MiB，离线2.58 GiB，均处于实用范围内。使用可提取性变体将导致在线阶段慢约4倍。结果表明，本文协议通过适度的性能开销（相比于SPDZ）换取了强大的安全属性，且在恶意方导致中断时，比基于重启的方案（BoBW）具有决定性的性能优势。

### 局限性与开放问题
本文协议的主要开销来自于格基承诺和零知识证明，这导致了在线和离线阶段的通信和计算量均高于基础SPDZ。对于未使用批量处理的电路，协议的效率会因参数未针对小电路优化而降低。未来工作需要研究更高效的承诺方案或零知识证明系统，以缩小与不含可问责性协议的效率差距。此外，尽管本协议具有后量子安全的潜力，但文中并未对后量子安全性进行详细分析，这是下一步值得探究的方向。对于需要高隐私性（即t接近n）的场景，鲁棒性阈值n-t+1会变得很小，限制了协议在容忍少数腐化方故障方面的能力。

### 强关联论文

[7] Damgård, I. et al. Multiparty Computation from Somewhat Homomorphic Encryption. **CRYPTO 2012**

[8] Damgård, I. et al. Practical Covertly Secure MPC for Dishonest Majority - Or: Breaking the SPDZ Limits. **ESORICS 2013**

[10] Baum, C. et al. Publicly Auditable Secure Multi-Party Computation. **SCN 2014**

[11] Baum, C. et al. Efficient Secure Multiparty Computation with Identifiable Abort. **TCC 2016-B**

[14] Cunningham, R. K. et al. Catching MPC Cheaters: Identification and Openability. **ICITS 2017**

[15] Keller, M. et al. Overdrive: Making SPDZ Great Again. **EUROCRYPT 2018**

[16] Baum, C. et al. Using TopGear in Overdrive: A More Efficient ZKPoK for SPDZ. **SAC 2019**

[41] Hirt, M. et al. A Dynamic Tradeoff between Active and Passive Corruptions in Secure Multi-Party Computation. **CRYPTO 2013**

[42] Patra, A. et al. Beyond Honest Majority: The Round Complexity of Fair and Robust Multi-party Computation. **ASIACRYPT 2019**

[45] Baum, C. et al. More Efficient Commitments from Structured Lattice Assumptions. **SCN 2018**


## 关键词

+ 安全多方计算（MPC）
+ 公共问责制
+ SPDZ协议
+ 格基承诺方案
+ 鲁棒MPC
+ 可公开验证性