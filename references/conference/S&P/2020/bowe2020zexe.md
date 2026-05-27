---
title: "Zexe: Enabling decentralized private computation"
doi: 10.1109/sp40000.2020.00050
标题简称:
论文类型: conference
会议简称: S&P
发表年份: 2020
---
## Zexe: Enabling decentralized private computation

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/9152634)

## 作者

+ [Sean Bowe](Sean%20Bowe.md)
+ [Alessandro Chiesa](Alessandro%20Chiesa.md)
+ [Matthew Green](Matthew%20Green.md)
+ [Ian Miers](Ian%20Miers.md)
+ [Pratyush Mishra](Pratyush%20Mishra.md)
+ Howard Wu 


## 笔记

### 背景与动机
分布式账本技术在金融、治理和数据共享等领域展现出巨大潜力，但其公共可审计性也带来了严重的隐私问题，任何参与方都可以读取账本上所有事件的历史 [Nak09]。在比特币这类支付系统中，交易会暴露发送方、接收方和金额，不仅泄露个人财务细节，还破坏了货币的“可互换性”这一基本经济属性。当转向以太坊等智能合约系统时，问题更为严峻，因为交易不仅要暴露应用内部的函数调用历史，应用的内部状态也必须是公开的 [Woo17]。与此同时，公共可审计性还带来了可扩展性问题：所有节点都需要通过重新执行计算来验证状态转换，导致网络中算力最弱的节点成为瓶颈，并催生了“验证者困境” [LTK+15]。先前的方案，如 Zerocash [BCG+14] 和 Hawk [KMS+16]，虽然实现了数据隐私，但都局限于隐藏状态转换的输入和输出，而未能隐藏正在执行的转换函数本身，即无法实现“函数隐私”。Zexe 旨在填补这一空白，构建一个同时提供数据隐私、函数隐私和验证简洁性的分布式账本系统。

### 相关工作

[BCG+14] Ben-Sasson 等. Zerocash: Decentralized Anonymous Payments from Bitcoin. **SP 2014** [Google Scholar](https://scholar.google.com/scholar?q=Zerocash%3A+Decentralized+Anonymous+Payments+from+Bitcoin)
> 核心思路：使用简洁非交互式零知识证明（zkSNARK）在账本上实现隐私支付，通过承诺和序列号隐藏交易金额和用户身份。
> 局限与区别：仅支持单一硬编码的货币价值转移功能，无法处理用户自定义函数或实现函数隐私。

[KMS+16] Kosba 等. Hawk: The Blockchain Model of Cryptography and Privacy-Preserving Smart Contracts. **SP 2016** [Google Scholar](https://scholar.google.com/scholar?q=Hawk%3A+The+Blockchain+Model+of+Cryptography+and+Privacy-Preserving+Smart+Contracts)
> 核心思路：结合 Zerocash 和多方计算的评估者-证明者概念，使各方能进行离线计算并通过密码学证明报告结果，保护私有输入。
> 局限与区别：保护了计算输入的隐私，但未能隐藏执行的是哪种计算，即不提供函数隐私。

[TR17] Teutsch 等. A scalable verification solution for blockchains. **2017** [Google Scholar](https://scholar.google.com/scholar?q=A+scalable+verification+solution+for+blockchains)
> 核心思路：用户报告计算结果但不提供密码学证明，而是通过激励机制（如挑战-应答游戏）来保证正确性。
> 局限与区别：基于理性经济假设，仅对抗理性且高效的攻击者，而非所有恶意的对手；且不提供强隐私保证。

[MS18] Meckler 等. Coda: Decentralized cryptocurrency at scale. **2018** [Google Scholar](https://scholar.google.com/scholar?q=Coda%3A+Decentralized+cryptocurrency+at+scale)
> 核心思路：使用任意深度的递归 SNARK 组合，使区块链节点能快速验证当前区块链状态。
> 局限与区别：系统目标是与 Zexe 正交的可扩展性问题；Zexe 使用深度为 2 的递归组合以确保所有交易验证成本相等，而 Coda 聚焦于状态证明的压缩。

[NVV18] Narula 等. zkLedger: Privacy-Preserving Auditing for Distributed Ledgers. **NSDI 2018** [Google Scholar](https://scholar.google.com/scholar?q=zkLedger%3A+Privacy-Preserving+Auditing+for+Distributed+Ledgers)
> 核心思路：通过同态承诺和 Schnorr 证明，在少数特权方之间实现匿名支付。
> 局限与区别：隐私性以交易验证时间随匿名集大小线性增长为代价；Zexe 中验证时间与匿名集大小呈对数关系。

[BAZ+19] Bünz 等. Zether: Towards Privacy in a Smart Contract World. **2019** [Google Scholar](https://scholar.google.com/scholar?q=Zether%3A+Towards+Privacy+in+a+Smart+Contract+World)
> 核心思路：使公开的智能合约能够在零知识中推理同态承诺，以此隐藏交易金额，但不隐藏交易双方的身份。
> 局限与区别：除不隐藏身份外，验证成本与匿名集大小线性相关；Zexe 提供更强的身份隐私和更优的验证复杂度。

### 核心技术与方案

Zexe 系统的核心技术是实现一种新的密码学原语——“去中心化私有计算”方案（DPC）。DPC 方案支持一种基于“记录”的简洁编程模型，其中每份数据记录都绑定了一个“诞生谓词”和一个“消亡谓词”，分别控制该记录的创建和消费条件。这些谓词与一个共享的“记录纳核”（RNK）执行环境共同运作，为构建应用提供基础。RNK 的核心规则是，在一个有效交易中，所有被消费记录的消亡谓词和所有新创建记录的诞生谓词必须同时被满足。

为了同时实现数据隐私、函数隐私和验证简洁性，Zexe 的 DPC 构建方案采用了以下方法：首先，基于 Zerocash 的架构，将交易数据（记录）通过隐蔽的承诺发布到账本，其序列号（SN）由伪随机函数评估得出，确保交易不泄露除输入输出记录数以外的任何信息。为了实现函数隐私，DPC 方案允许用户选择任意函数作为记录谓词，并通过零知识证明确保这些函数的执行和谓词的满足情况，从而隐藏具体函数内容。为了解决“恶意函数”可能破坏系统的问题，DPC 通过让每个谓词都能“看到”整个交易的本地数据，特别是其他记录的谓词类型，从而使一个记录能保护自己免受与“坏”记录交互的影响。

在技术实现上，为了高效实现 NP 关系 $\mathcal{R}_e$ 的证明，Zexe 采用了递归证明组合技术。核心思想是，将 $\mathcal{R}_e$ 的证明分解为两层：第一层使用高效的椭圆曲线 $E_\textsf{BLS}$ 上的 zkSNARK 证明谓词（谓词本身可能复杂）的满足性；第二层使用另一个配对友好曲线 $E_\textsf{CP}$ 上的 zkSNARK 来验证第一层证明的有效性以及其它全局检查（如默克尔树路径验证）。通过使用 Cocks-Pinch 方法构造的曲线链，使得第二层 SNARK 能高效地验证第一层 SNARK 的证明，同时将复杂的非证明检查（如承诺打开）转移到更高效的 $E_\textsf{BLS}$ 曲线上进行。最终，交易验证时间与离线计算的复杂度无关，实现“简洁性”。

系统的根本安全性依赖于底层密码学假设，包括离散对数假设和伪随机函数的安全性。零知识证明系统（具体为 Groth-Maller [GM17] 的模拟可提取 zkSNARK）保证了完备性、可靠性和完美零知识性质。证明策略是通过将 DPC 方案的安全性归约到理想功能，并使用模拟器来证明在现实世界中，敌手从交易中获取的信息不包含除了输入输出记录数界限之外的任何信息。渐进复杂度上，交易大小固定为 32m+32n+840 字节，验证时间约为几十毫秒，均独立于离线计算的实际复杂度。

### 核心公式与流程

**DPC 执行 NP 关系 $\mathcal{R}_e$**
$$\mathbf{x}_e = (\mathsf{st_L}, [\mathsf{sn}_i]_1^m, [\mathsf{cm}_j]_1^n, \mathsf{memo}) \quad \text{and} \quad \mathbf{w}_e = ([\mathbf{r}_i]_1^m, [\mathbb{w}_{\mathbf{L},i}]_1^m, [\mathsf{ask}_i]_1^m, [\mathbf{r}_j]_1^n, \mathsf{aux})$$
> 作用：定义了交易零知识证明的实例（public statement）和见证（private witness）。实例包含账本摘要、序列号集合、承诺集合和备忘录；见证包含记录的详细内容、默克尔树证据、地址私钥和辅助输入。

**交易大小**
$$\text{tx size} = 32m + 32n + 840 \text{ bytes}$$
> 作用：以字节为单位给出交易大小的计算公式，其中 $m$ 和 $n$ 分别是输入和输出记录的数量。常数 840 字节包含两个 zkSNARK 证明和其他固定元数据。

**构建 DPC 方案的算法**
$$\begin{aligned}
&\text { DPC.Setup}(1^\lambda) \rightarrow \mathsf{pp} \\
&\text { DPC.GenAddress}(\mathsf{pp}) \rightarrow (\mathsf{apk}, \mathsf{ask}) \\
&\text { DPC.Execute}^L(\mathsf{pp}, [\mathbf{r}_i]_1^m, [\mathsf{ask}_i]_1^m, [\mathsf{apk}_j]_1^n, [\mathsf{payload}_j]_1^n, [\Phi_{\mathsf{b},j}]_1^n, [\Phi_{\mathsf{d},j}]_1^n, \mathsf{aux}, \mathsf{memo}) \rightarrow ([\mathbf{r}_j]_1^n, \mathsf{tx}) \\
&\text { DPC.Verify}^L(\mathsf{pp}, \mathsf{tx}) \rightarrow b
\end{aligned}$$
> 作用：描述 DPC 方案的四个核心算法。Setup 生成公共参数；GenAddress 创建地址密钥对；Execute 产生证明谓词满足性和记账规则一致性的交易；Verify 验证交易有效性。

### 实验结果
实验在一台配备 Intel Xeon 6136 CPU (3.0 GHz) 和 252 GB 内存的机器上进行。对于 2 个输入记录和 2 个输出记录的典型配置，DPC.Setup 耗时 109.62 秒，DPC.Execute 耗时 52.5 秒（均使用 12 线程），而 DPC.Verify 仅需 46 毫秒（单线程）。交易大小为 968 字节，无论离线计算的复杂度如何。系统使用的椭圆曲线包括 BLS 族曲线 $E_\textsf{BLS}$（377位基域）和 Cocks-Pinch 曲线 $E_\textsf{CP}$（782位基域），以及对应的 Edwards 曲线 $E_\textsf{Ed/BLS}$ 和 $E_\textsf{Ed/CP}$ 用于高效密码原语。对于用户自定义资产和去中心化交易所等应用，额外产生的约束数少于 35000，证明生成时间只需几十毫秒，与基础 DPC Execute 的数十秒成本相比可忽略。总体而言，Zexe 在实现数据隐私、函数隐私和简洁性的高目标下，实现了可容忍的效率，交易生成和验证成本与现存同类系统（如 Zerocash、Hawk）相当。

### 局限性与开放问题
Zexe 的主要成本在于生成包含在交易中的密码学证明，虽然可控制在约一分钟以内（加上随离线计算增长的部分），但对于更复杂的计算来说成本仍然很高。系统依赖于具有可信设置的配对基础 zkSNARK，虽然可以通过安全多方计算来缓解，但仍需所有用户信任“主参数”的生成过程。未来工作可以将系统扩展为完整的智能合约框架，并探索使用最新提出的通用设置 SNARK（如 Marlin 或 PLONK）来替代当前方案，以进一步减轻可信设置负担。

### 强关联论文

[BCG+14] Ben-Sasson 等. Zerocash: Decentralized Anonymous Payments from Bitcoin. **SP 2014** [Google Scholar](https://scholar.google.com/scholar?q=Zerocash%3A+Decentralized+Anonymous+Payments+from+Bitcoin)

[KMS+16] Kosba 等. Hawk: The Blockchain Model of Cryptography and Privacy-Preserving Smart Contracts. **SP 2016** [Google Scholar](https://scholar.google.com/scholar?q=Hawk%3A+The+Blockchain+Model+of+Cryptography+and+Privacy-Preserving+Smart+Contracts)

[GM17] Groth 等. Snarky Signatures: Minimal Signatures of Knowledge from Simulation-Extractable SNARKs. **CRYPTO 2017** [Google Scholar](https://scholar.google.com/scholar?q=Snarky+Signatures%3A+Minimal+Signatures+of+Knowledge+from+Simulation-Extractable+SNARKs)

[TR17] Teutsch 等. A scalable verification solution for blockchains. **2017** [Google Scholar](https://scholar.google.com/scholar?q=A+scalable+verification+solution+for+blockchains)

[MS18] Meckler 等. Coda: Decentralized cryptocurrency at scale. **2018** [Google Scholar](https://scholar.google.com/scholar?q=Coda%3A+Decentralized+cryptocurrency+at+scale)

[NVV18] Narula 等. zkLedger: Privacy-Preserving Auditing for Distributed Ledgers. **NSDI 2018** [Google Scholar](https://scholar.google.com/scholar?q=zkLedger%3A+Privacy-Preserving+Auditing+for+Distributed+Ledgers)

[BCT+17] Ben-Sasson 等. Scalable Zero Knowledge Via Cycles of Elliptic Curves. **Algorithmica 2017** [Google Scholar](https://scholar.google.com/scholar?q=Scalable+Zero+Knowledge+Via+Cycles+of+Elliptic+Curves)

[Nak09] Nakamoto. Bitcoin: a peer-to-peer electronic cash system. **2009** [Google Scholar](https://scholar.google.com/scholar?q=Bitcoin%3A+a+peer-to-peer+electronic+cash+system)

[Woo17] Wood. Ethereum: A Secure Decentralised Generalised Transaction Ledger. **2017** [Google Scholar](https://scholar.google.com/scholar?q=Ethereum%3A+A+Secure+Decentralised+Generalised+Transaction+Ledger)

[BAZ+19] Bünz 等. Zether: Towards Privacy in a Smart Contract World. **2019** [Google Scholar](https://scholar.google.com/scholar?q=Zether%3A+Towards+Privacy+in+a+Smart+Contract+World)


## 关键词

+ 去中心化私有计算（DPC）
+ 简洁零知识证明
+ 隐私保护智能合约
+ 递归证明组合
+ 恒定大小交易
+ 账本型系统