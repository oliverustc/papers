---
title: "Sok: Distributed randomness beacons"
标题简称:
论文类型: conference
会议简称: S&P
发表年份: 2023
created: 2025-04-28 16:48:01
modified: 2025-04-28 16:49:10
---

## Sok: Distributed randomness beacons

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/10179419)

## 作者

+ Kevin Choi 
+ Aathira Manoj 
+ [[Joseph Bonneau]] 

## 笔记

### 背景与动机
分布式随机数信标是众多去中心化应用的核心基础设施，例如彩票、电子投票、区块链协议中的领导者选举以及分片等场景均依赖公开可验证的随机性。Rabin 最早形式化了理想随机信标的概念，但现实中不存在完全可信的第三方，而中心化方案如 NIST 或 random.org 面临单点被攻破或作恶的风险，且用户无法验证其安全性，攻击者甚至可以设计出具有陷门的“看起来随机”的输出。另一类隐式信标（如基于比特币或股票市场数据）虽在实践中有一定安全性，但缺乏正式的安全模型，易受内部人员操纵。为了在去除单点信任的同时提供形式化的安全保证，分布式随机信标应运而生，它通过多方协议在存在部分恶意参与者的前提下产生不可偏倚、不可预测且具有活性的随机输出。尽管已有大量 DRB 协议被提出，它们基于不同的设置、假设和密码学原语，具有独特的安全特点与性能权衡，但缺乏一个统一的、深入的分析框架来比较其设计维度和安全性。本文正是为了填补这一空白，系统化地梳理了现有 DRB 的设计空间，并提出了一种通用的比较框架，以帮助实践者和研究者理解各类协议的内在逻辑与适用场景。

### 相关工作

[21]  Blum.  Coin flipping by telephone a protocol for solving impossible problems. **ACM SIGACT News 1983** [Google Scholar](https://scholar.google.com/scholar?q=Coin+flipping+by+telephone+a+protocol+for+solving+impossible+problems)
> 核心思路：最早提出了基于承诺的抛币协议，是分布式随机性的奠基性工作。
> 局限与区别：基本协议在异步网络下存在最后揭示者攻击，无法保证活性。

[23]  Boneh, Bonneau, Bünz, and Fisch.  Verifiable delay functions. **CRYPTO 2018** [Google Scholar](https://scholar.google.com/scholar?q=Verifiable+delay+functions)
> 核心思路：提出可验证延迟函数 (VDF) 的概念，该函数需要固定时间的顺序计算才能求值，但验证极快。
> 局限与区别：VDF 需要专门硬件和对延迟下界的合理估计，尚未被大规模实践验证。

[27]  Boneh and Naor.  Timed commitments. **CRYPTO 2000** [Google Scholar](https://scholar.google.com/scholar?q=Timed+commitments)
> 核心思路：提出定时承诺，允许在约定时间后强制打开承诺值，从而解决承诺协议中的发送者停发问题。
> 局限与区别：该工作仅提出概念，本文详述了如何将其用于构建 Bicorn 此类优化型 DRB。

[39]  Cherniaeva, Shirobokov, and Shlomovits.  Homomorphic Encryption Random Beacon. **Cryptology ePrint Archive 2019** [Google Scholar](https://scholar.google.com/scholar?q=Homomorphic+Encryption+Random+Beacon)
> 核心思路：利用阈值加密（ElGamal 同态性质）实现共享密文的单次拉格朗日插值重构，避免多次插值。
> 局限与区别：HERB 依赖 DKG 初始化，当参与者动态变化时需要重新运行成本高昂的 DKG。

[34]  Cascudo and David.  SCRAPE: Scalable randomness attested by public entities. **Applied Cryptography and Network Security 2017** [Google Scholar](https://scholar.google.com/scholar?q=SCRAPE+Scalable+randomness+attested+by+public+entities)
> 核心思路：提出高效的 PVSS 方案，用于在 DRB 中公开可验证地分发和恢复秘密份额。
> 局限与区别：乐观情况下通信复杂度 $O(n^3)$，最坏情况下需额外恢复轮次。

[83]  Qian.  RANDAO: Verifiable Random Number Generation. **2017** [Google Scholar](https://scholar.google.com/scholar?q=RANDAO+Verifiable+Random+Number+Generation)
> 核心思路：用经济押金惩罚机制来威慑参与者在揭示阶段停发，本质是承诺-揭示-惩罚。
> 局限与区别：需要参与者锁定高额押金且依赖区块链平台，对诚实故障不具包容性。

[32]  Camenisch et al.  Internet computer consensus. **ACM PODC 2022** [Google Scholar](https://scholar.google.com/scholar?q=Internet+computer+consensus)
> 核心思路：提出 Dfinity DVRF，利用阈值 BLS 签名构建无边际熵的 PRG 信标，输出 $\Omega_\tau = H(\text{Sign}_{sk}(\tau \parallel \Omega_{\tau-1}))$。
> 局限与区别：无边际熵意味着一旦密钥泄露，所有未来输出可预测（最大损害为预测）。

[61]  Gilad et al.  Algorand: Scaling Byzantine Agreements for Cryptocurrencies. **SOSP 2017** [Google Scholar](https://scholar.google.com/scholar?q=Algorand+Scaling+Byzantine+Agreements+for+Cryptocurrencies)
> 核心思路：使用 VRF 进行私有抽签选委员会，并利用 VRF 输出作为信标。
> 局限与区别：私有抽签存在囤积攻击可能性，且要求秘密密钥事先承诺以防止掏空攻击。

[89]  Schindler et al.  HydRand: Practical Continuous Distributed Randomness. **IEEE S&P 2020** [Google Scholar](https://scholar.google.com/scholar?q=HydRand+Practical+Continuous+Distributed+Randomness)
> 核心思路：使用 PVSS 进行秘密共享，结合上一个信标输出和前一次循环中预承诺的熵来生成新输出。
> 局限与区别：采用轮循或随机选择的单一熵提供者，导致最大损害为偏倚（而非仅预测）。

### 核心技术与方案

本文提出一个统一的框架，将 DRB 协议解耦为两个核心设计维度：熵提供者的选择和信标输出的生成。

对于熵提供者的选择，协议可分为全节点参与和委员会参与两类。全节点方案中所有 $n$ 个节点每轮都提供边际熵，这在小规模网络中直接可行，但扩展到更大规模时通信成本会快速上升。为改善可扩展性，委员会方案先通过一个选举过程来确定每轮的熵提供者委员会，之后只由委员会执行输出生成。委员会选举又分为公开选举（可使用轮循、随机选择或领导者选择）和私有选举（通过 VRF 或哈希链等私密抽签确定获奖者）。公开选举的好处是确定性或可验证性，但可能受拒绝服务攻击；私有选举提供更好的抗拒绝服务能力和较低通信开销，但引入囤积攻击风险。

信标输出生成根据熵的来源可分为三类：来自所有提供者的新鲜边际熵、结合上一个输出和预承诺的边际熵、以及完全不依赖边际熵的伪随机生成。新鲜边际熵的生成方法覆盖承诺-揭示、承诺-揭示-惩罚、和承诺-揭示-恢复三种子类，其中恢复机制又可分为基于阈值秘密共享和基于阈值加密两种分支。基于阈值秘密共享的承诺-揭示-恢复方法如 Scrape，每个参与者需在承诺阶段向所有人分发 PVSS 份额，若对象在揭示阶段停发则其他节点通过拉格朗日插值恢复其暗含的随机值。该方法在乐观情况下只需一轮揭示，在最坏情况下需要额外一轮恢复和 $O(n)$ 次拉格朗日插值。基于阈值加密的 HERB 则将每个节点的加密熵同态聚合为一个密文，然后由至少 $t+1$ 个节点共同进行一次解密（单次拉格朗日插值）即可得到聚合结果，这避免了多次插值的开销。而基于 VRF/DVRF 的无边际熵方案则完全由密码学伪随机性驱动，效率最高但面临密钥泄露后未来输出被预言的致命风险。

延迟类协议是另一个独特分支，利用可验证延迟函数或定时承诺来阻止最后揭示者攻击。Unicorn++ 先收集所有节点的熵值后送入 VDF 计算，由于 VDF 的不可加速性，任何人无法在提交其熵前预测 VDF 的输出，因此能容忍最恶劣的 $n-1$ 个恶意节点。Bicorn 则用定时承诺替代普通承诺，在乐观情况下没有延迟（如同基本承诺-揭示），只在节点停发时启动强制打开流程，从而保证了活性和效率的平衡。RandRunner 利用带陷门的 VDF 构造确定性链，每个周期的领导者可用陷门快速输出，恶意领导者则迫使所有节点执行慢速顺序计算，这使得系统在最坏情况下的通信复杂度从 $O(n)$ 增至 $O(n^2)$。

### 核心公式与流程

**协议 Strawman（理想同步）**
$$
\Omega = \sum_{i=1}^{n} e_i
$$
> 作用：展示在完美同步下分布式随机性的朴素构造，但因异步网络下最后揭示攻击而不安全。

**安全游戏 Gamble（Unbiasability）**
$$
\text{Pr}[\Omega_\tau \in Y] \leq \frac{|Y|}{2^{\ell_{\Omega_\tau}(\lambda)}} + \text{negl}(\lambda)
$$
> 作用：定义无偏性、活性和不可预测性的形式化游戏模型，区分 Intra-unpredictability 和 Inter-unpredictability。

**Unicorn++（VDF-based DRB）**
$$
x_\tau = H(e_1,\ldots,e_n), \quad y_\tau,\pi_\tau = \text{VDF.Eval}(pp,x_\tau), \quad \Omega_\tau = H(y_\tau)
$$
> 作用：利用VDF延迟保证任何节点无法在提交熵后及时计算输出，从而防止偏倚；容忍任意 $n-1$ 个恶意节点。

**Dfinity-DVRF（无边际熵 DRB）**
$$
\Omega_\tau = H(\text{Sign}_{sk}(\tau \parallel \Omega_{\tau-1}))
$$
> 作用：阈值 BLS 签名链实现的纯伪随机信标，单次 Lagrange 插值 $O(n^2)$ 验签成本，但密钥泄露后所有未来输出可预测。

**HERB（Threshold Encryption DRB）**
$$
c_i = \text{Enc}_{pk}(e_i), \quad C = \prod c_i, \quad \Omega_\tau = \text{Dec}_{sk}(C)
$$
> 作用：利用 ElGamal 同态性和阈值解密，只进行一次 Lagrange 插值即恢复输出，避免多个秘密重构的通信开销。

**PVSS Reconstruction（Recover 过程）**
$$
h^{s} = \prod_{i\in A} (h^{p(i)})^{\lambda_{0,i,A}}
$$
> 作用：指数上的 Lagrange 插值恢复秘密而不直接泄露秘密值，用于 Scrape 等协议的恢复步骤。

### 实验结果

本文未提供实验数据，但通过 Table I 对 30 余种 DRB 协议进行了综合比较。表中列出了每个协议的免疫囤积性、容错阈值、$\alpha$-代内不可预测性（一般为 $O(\Delta)$）、$\beta$-代间不可预测性（多数为1）、通信复杂度（乐观/最坏案例）、验证者复杂度、最大损害（预测或偏倚）以及恢复成本等关键指标。

在非延迟类中，无边际熵协议（如 Dfinity）验证者复杂度最低 $O(1)$，但它们的最大损害都是完整预测（一旦密钥泄露，输出可完全预测）。相比之下，基于新鲜边际熵的协议（如 Scrape、HERB）在乐观情况下通信复杂度分别为 $O(n^3)$ 和 $O(n^2)$，验证者复杂度为 $O(n^2)$ 和 $O(n)$，而最大损害仅限偏倚（除非攻击者采用快速对手模型并拥有策略截断能力）。VDF类协议在容错能力上达到理论上限（可容忍 $n-1$ 个恶意节点），验证者复杂度可通过快速验证降低至 $O(\log T)$（Pietrzak VDF）。

对于委员会协议，私有抽签类（如 Algorand）具有最低的乐观通信复杂度 $O(n)$，但最大损害仍为偏倚（因囤积攻击）。委员会协议的共同问题是恢复成本较高（$O(n^3)$ 至 $O(n^4)$，取决于是否使用 DKG），这反映了它们面对动态参与者和密钥轮换时的性能瓶颈。

### 局限性与开放问题
本文明确指出 VDF 在实际部署中的核心挑战：硬件实现需要提供确信延迟下限的可靠估计，而 VDF 假设仍相对较新，未得到充分实践验证。私有抽签协议的囤积攻击问题虽可通过 SSLE 检测，但追溯囤积者的身份仍是一个开放方向。几乎所有非 VDF 类 DRB 都假设许可设置和同步通信，如何在无许可、异步环境下构造安全的 DRB 是关键难题。此外，形式化安全证明多采用基于游戏的模型，向 UC 安全模型的扩展还有很大空间。最后，将传统的随机数提取器理论与当前的密码学假设结合，以生产更高质量的信标输出，也是一条值得探索的道路。

### 强关联论文

[23] Boneh, Bonneau, Bünz, and Fisch. Verifiable delay functions. **CRYPTO 2018** [Google Scholar](https://scholar.google.com/scholar?q=Verifiable+delay+functions)

[27] Boneh and Naor. Timed commitments. **CRYPTO 2000** [Google Scholar](https://scholar.google.com/scholar?q=Timed+commitments)

[39] Cherniaeva, Shirobokov, and Shlomovits. Homomorphic Encryption Random Beacon. **Cryptology ePrint Archive 2019** [Google Scholar](https://scholar.google.com/scholar?q=Homomorphic+Encryption+Random+Beacon)

[34] Cascudo and David. SCRAPE: Scalable randomness attested by public entities. **Applied Cryptography and Network Security 2017** [Google Scholar](https://scholar.google.com/scholar?q=SCRAPE+Scalable+randomness+attested+by+public+entities)

[32] Camenisch et al. Internet computer consensus. **ACM PODC 2022** [Google Scholar](https://scholar.google.com/scholar?q=Internet+computer+consensus)

[61] Gilad et al. Algorand: Scaling Byzantine Agreements for Cryptocurrencies. **SOSP 2017** [Google Scholar](https://scholar.google.com/scholar?q=Algorand+Scaling+Byzantine+Agreements+for+Cryptocurrencies)

[89] Schindler et al. HydRand: Practical Continuous Distributed Randomness. **IEEE S&P 2020** [Google Scholar](https://scholar.google.com/scholar?q=HydRand+Practical+Continuous+Distributed+Randomness)

[88] Schindler et al. RandRunner: Distributed Randomness from Trapdoor VDFs with Strong Uniqueness. **Cryptology ePrint Archive 2020** [Google Scholar](https://scholar.google.com/scholar?q=RandRunner+Distributed+Randomness+from+Trapdoor+VDFs+with+Strong+Uniqueness)

[21] Blum. Coin flipping by telephone a protocol for solving impossible problems. **ACM SIGACT News 1983** [Google Scholar](https://scholar.google.com/scholar?q=Coin+flipping+by+telephone+a+protocol+for+solving+impossible+problems)

[83] Qian. RANDAO: Verifiable Random Number Generation. **2017** [Scholar](https://scholar.google.com/scholar?q=RANDAO+Verifiable+Random+Number+Generation)


## 关键词

+ 分布式随机信标
+ 可公开验证随机性
+ 不可偏差性
+ 不可预测性
+ 区块链随机性
+ 密码学构建块