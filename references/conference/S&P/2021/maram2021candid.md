---
title: "Candid: Can-do decentralized identity with legacy compatibility, sybil-resistance, and accountability"
标题简称:
论文类型: conference
会议简称: S&P
发表年份: 2021
modified: 2025-05-09 10:53:12
created: 2025-04-13 13:55:10
---

## Candid: Can-do decentralized identity with legacy compatibility, sybil-resistance, and accountability

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/9519473)

## 作者

+ [Deepak Maram](Deepak%20Maram.md)
+ Harjasleen Malvai
+ Fan Zhang
+ Nerla Jean-Louis
+ Alexander Frolov
+ Tyler Kell
+ Tyrone Lobban
+ Christine Moy
+ Ari Juels
+ [Andrew Miller](Andrew%20Miller.md)

## 笔记

### 背景与动机
去中心化身份（DID）本应让用户自主管理凭证，但现有方案存在严重制约：首先，它们假设一个现成的凭证发行生态，却未指明如何从零构建，面临冷启动难题；其次，用户需自行保管私钥，丢失密钥的风险极高，这已成为加密货币行业数亿美元损失的根源 [58]；再次，现有系统普遍缺乏抗女巫攻击能力，无法保证每用户只有唯一身份——而在匿名投票、空投分发[14]等场景中这一性质至关重要；最后，隐私保护与法规遵从（如 KYC/AML、制裁名单筛查）之间存在矛盾，如何在隐藏用户真实身份的同时识别并封禁违规用户尚未被有效解决。针对上述痛点，本文提出 CanDID 平台，通过引入预言机技术（DECO [82] 或 Town Crier [81]）从现有、未改动的网络服务中安全地导入身份数据，实现遗留兼容；利用安全多方计算（MPC）在保护隐私的前提下完成基于唯一标识符的去重，提供抗女巫攻击能力；设计新的隐私保护模糊匹配协议，支持基于制裁名单的问责；基于秘密共享与现有网络认证流程，提供用户友好的密钥恢复机制。

### 相关工作

[10] uPort: Open identity system for the decentralized web, 2020. [Google Scholar](https://scholar.google.com/scholar?q=uPort+Open+identity+system+for+the+decentralized+web)
> 核心思路：基于区块链的去中心化身份实现，允许用户自主管理 DID 与凭证。
> 局限与区别：未解决自举问题，即需要已有凭证发行者；缺乏抗女巫攻击设计；密钥恢复依赖用户自行保管助记词。

[32] Decentralized Identity Foundation. 2020. [Google Scholar](https://scholar.google.com/scholar?q=Decentralized+Identity+Foundation)
> 核心思路：制定 DID 与可验证凭证的行业标准，推动互操作性。
> 局限与区别：标准本身不涉及如何从现有 web 服务导入数据；未提供内置的密钥恢复方案；未处理用户去重。

[66] Sonnino A. 等. Coconut: Threshold issuance selective disclosure credentials with applications to distributed ledgers. **arXiv 2018** [Google Scholar](https://scholar.google.com/scholar?q=Coconut+Threshold+issuance+selective+disclosure+credentials+with+applications+to+distributed+ledgers)
> 核心思路：基于阈值签名的匿名凭证方案，支持选择性披露。
> 局限与区别：Coconut 侧重于凭证的匿名性撤销与可选择性，但同样假定密钥管理问题已解决，且未涉及基于遗留系统的凭证生成与去重。

[81] Zhang F. 等. Town Crier: An authenticated data feed for smart contracts. **ACM CCS 2016** [Google Scholar](https://scholar.google.com/scholar?q=Town+Crier+An+authenticated+data+feed+for+smart+contracts)
> 核心思路：利用 Intel SGX 等 TEE 提供经 TLS 认证的数据源，证明网页内容的真实性。
> 局限与区别：Town Crier 本身是预言机，CanDID 将其作为底层组件用于凭证生成；但 CanDID 亦支持 DECO 以避免 TEE 信任假设。

[82] Zhang F. 等. DECO: Liberating web data using decentralized oracles for TLS. **ACM CCS 2020** [Google Scholar](https://scholar.google.com/scholar?q=DECO+Liberating+web+data+using+decentralized+oracles+for+TLS)
> 核心思路：通过三方 TLS 会话与 MPC，让证明者向验证者证明特定 TLS 响应内容满足某一谓词，而不泄露数据。
> 局限与区别：DECO 专注于隐私保护的数据证明，CanDID 将其扩展到完整的身份凭证系统，并叠加去重与问责功能。

[23] Borge M. 等. Proof-of-personhood: Redemocratizing permissionless cryptocurrencies. **IEEE EuroS&PW 2017** [Google Scholar](https://scholar.google.com/scholar?q=Proof+of+personhood+Redemocratizing+permissionless+cryptocurrencies)
> 核心思路：通过定期线下会议实现“每人一票”式的人格证明。
> 局限与区别：依赖物理集会，可扩展性受限；CanDID 则完全通过线上 MPC 实现基于唯一标识符的去重。

[71] W3C. Decentralized Identifiers (DIDs) v0.11, 2018. [Google Scholar](https://scholar.google.com/scholar?q=Decentralized+Identifiers+DIDs+v0+11)
> 核心思路：提出 DID 的数据模型与语法，推荐使用可信托管方组成的仲裁方进行密钥恢复。
> 局限与区别：未给出具体实现；未讨论隐私保护下的去重与制裁名单筛查。

[77] Wüst K. 等. PRcash: Centrally-issued digital currency with privacy and regulation. **IACR ePrint 2018** [Google Scholar](https://scholar.google.com/scholar?q=PRcash+Centrally+issued+digital+currency+with+privacy+and+regulation)
> 核心思路：在数字货币中实现交易隐私与中央监管能力。
> 局限与区别：其隐私保护下的问责技术面向的是交易而非身份凭证，且未考虑遗留兼容。

[58] Roberts J. J. 等. Nearly 4 million Bitcoins lost forever, new study says. **Fortune 2017** [Google Scholar](https://scholar.google.com/scholar?q=Nearly+4+million+Bitcoins+lost+forever+new+study+says)
> 核心思路：报告因密钥丢失导致的巨额加密货币损失。
> 局限与区别：证实密钥恢复问题是现实痛点，CanDID 正是为应对该痛点而设计。

[18] Bagherzandi A. 等. Password-protected secret sharing. **ACM CCS 2011** [Google Scholar](https://scholar.google.com/scholar?q=Password+protected+secret+sharing)
> 核心思路：通过密码保护秘密共享，即使所有委员会节点合谋也无法获取密钥。
> 局限与区别：若用户忘记密码则永久丢失密钥；CanDID 的密钥恢复基于现有 web 账户，对用户更友好。

### 核心技术与方案

CanDID 整体由身份子系统和密钥恢复子系统构成，共享同一委员会 $C$，共 $n$ 个节点，容忍 $t < n/3$ 个静态主动腐败。委员会持有阈值签名密钥 $(sk^{\mathcal{C}}, pk^{\mathcal{C}})$。

**1. 凭证模型**：凭证格式仿照 W3C 可验证凭证 [76]，包含用户标识符 $pk^U$、上下文 $ctx$、一组声明 $\{claim_i\}$ 以及委员会签名 $\sigma$。每个声明包含属性名 $a_i$、值 $v_i$（可能是承诺形式）和可选的来源提供方 $P_i$。为支持抗女巫攻击，每个凭证自动包含一条“dedupOver”声明，指明用于去重的属性集。

**2. 预凭证生成**：用户利用 DECO [82] 或 Town Crier [81] 从现有 web 服务生成预凭证 $PC=(claim, pk^U, \pi)$。$\pi$ 是委员会（DECO 版）或 TEE（Town Crier 版）对声明与公钥的签名。该步骤确保凭证的真实性与隐私性：委员会仅获知声明承诺，不知底层数据值。

**3. 主凭证发行与抗女巫攻击**：委员会维护一个秘密共享的表格 IDTable，存储用户去重属性（如 SSN）的伪随机值 $\tilde{v} = PRF(sk^{\mathcal{C}}_{prf}, v)$。新用户提交预凭证后，委员会通过 MPC 计算 $\tilde{v}$ 并检查是否已存在。若不存在，则向用户签发主凭证。MPC 协议步骤：
- 用户接收盲因子 $[b]$，计算 $v' = b+v$ 并附零知识证明 $\pi^{blind}$ 证明盲化正确。
- 委员会恢复 $[v]$ 并联合计算 $PRF([sk^{\mathcal{C}}_{prf}], [v])$，输出 $\tilde{v}$。
- 各节点验证 $\tilde{v} \notin IDTable$ 后将 $(\tilde{v}, pk^U)$ 加入 IDTable，并生成阈值部分签名。
该协议保证了抵抗性即每人至多一个主凭证，且隐私性即属性值 $v$ 对委员会隐藏。

**4. 上下文凭证发行**：用户可基于主凭证申请针对特定应用 $ctx$ 的上下文凭证。为证明新声明属于同一用户，用户提供零知识证明（基于编辑距离的模糊匹配）表明新声明与主凭证中的链接属性（如姓名）一致。委员会维护每个上下文的已颁发集合 $Issued_{ctx}$，确保每个主凭证对每个 $ctx$ 只颁发一次。该设计实现应用间的不可链接性（定理7）：在假设委员会诚实的条件下，不同应用收到的凭证 $pk^U_{new}$ 彼此独立。

**5. 问责与制裁名单模糊匹配**：系统通过 MPC 实现隐私保护的模糊字符串匹配，支持筛选和撤销违规用户。具体方法基于 c-shingles 和编辑距离：
- 预计算每个名字的二元字母集 $sh_2(name)$。
- 在线时，计算输入串 $x$ 的 $sh_2(x)$，与数据库中各串 $y$ 的 $sh_2(y)$ 比较集合差异来筛选候选，再在限定数量（实验取15）内精确计算编辑距离。
- 该过程实为算术电路，可在 SNARK（用于注册时证明）或 MPC（用于定期筛查）中运行。安全依赖于对 $t<n/3$ 腐败的容忍以及电路门数的合理近似。

**6. 密钥恢复**：用户将私钥 $sk^U$ 秘密分享给委员会，并指定恢复策略（如使用 2/3 的 legacy 账户认证）。用户提供针对账户标识符的预凭证（通过 DECO/Town Crier 生成）。恢复时，委员会通过 MPC 计算 $pid = PRF(sk^{\mathcal{C}}_{prf}, id_P^U)$ 以查找存储的密钥份额，并在满足策略后合并还原。该过程保证委员会和认证提供商均无法获知用户的真实身份标识符。

### 核心公式与流程

**凭证结构**
$$ cred = \{ pk^U, ctx, \mathcal{CS}, \sigma \} $$
其中 $\mathcal{CS} = \{claim_i\}_{i=1}^k$，$claim_i = (a_i, v_i, P_i)$，$v_i$ 可以是明文或承诺，$\sigma = Sig_{sk^{\mathcal{C}}}(pk^U, ctx, \mathcal{CS})$。
> 作用：定义了 CanDID 凭证的完整格式，包含去重声明“dedupOver”。

**去重协议中的 PRF 计算与查表**
$$ \tilde{v} = PRF(sk^{\mathcal{C}}_{prf}, v) $$
$$ \tilde{v} \notin \text{IDTable} \Rightarrow \text{insert } (\tilde{v}, pk^U) $$
> 作用：基于唯一标识符的隐私保护去重核心，通过对标识符进行伪随机映射并查表实现。

**预凭证生成（DECO 版）**
$$ \pi_i = Sig_{sk_i}(claim, pk^U) $$
$$ \pi = Combine(\{\pi_i\}_{i=1}^t) $$
> 作用：用户从委员会得到阈值签名，证明声明源自某 web 服务。

**上下文凭证发行的 ZK 链接证明**
$$ ZKPoK\{r, r', v, v' : C_v = com(v, r) \land C_{v'} = com(v', r') \land \Delta(v, v') \le \delta_{a_{link}} \} $$
> 作用：在隐藏具体值的同时，证明新声明与主凭证在链接属性上匹配（容差 $\delta$ 内）。

**模糊匹配的 c-shingles 近似**
$$ sh_c(w) = \{ \text{所有长度为 c 的连续子串} \} $$
$$ dist(sh_c(w), sh_c(w')) = |sh_c(w)\setminus sh_c(w')| + |sh_c(w')\setminus sh_c(w)| \le (2c-1) \cdot edit(w, w') $$
> 作用：利用 c-shingles 作为过滤步骤，大幅降低编辑距离比较的计算量。

**密钥恢复中的身份表征**
$$ pid^U_P = PRF([sk^{\mathcal{C}}_{prf}], [id^U_P]) $$
> 作用：将用户的 legacy 账户标识符映射为隐私保护的伪标识，用于查询存储的密钥份额。

### 实验结果

实验使用四台 AWS t2.2xlarge 节点作为委员会，用户端为 ThinkPad x270（4.7Mbps 上行）。预凭证生成：DECO 在线阶段 8.61 s（SSA）、10.10 s（RentCafe）；Town Crier 仅需 0.39 s 和 1.01 s。主凭证发行总时长：DECO 线上 18.76 s；含制裁名单检查时飙升至约 1500 s（25 min），其中模糊匹配 SNARK 证明主导（估计约 2.8e7 乘法门，涉及 25511 条名单项）。MPC 远程计算能力：单次乘法 41.8 μs（四节点），估算对百万级数据库进行完整模糊匹配需 155 h。链接名称的 ZK 证明用时 0.94 s。去重 PRF 运行仅 0.01 s（MP-SPDZ 中 MiMC 电路 322 门）。对于定期筛查，电路规模随数据库大小线性增长，在 256K 条目时 3500 门，1M 时 13500 门。实验表明 CanDID 在实际网络条件下可正常运行，但制裁模糊匹配仍是瓶颈。

### 局限性与开放问题
当前模糊匹配基于编辑距离与 c-shingles 的近似，对制裁名单筛查更慢且可能误判；更高效的模糊匹配方案或改用 TEE 是可能的改进方向。此外，当前的抗女巫攻击依赖政府颁发的唯一标识符（如 SSN），并非全球人口都有此条件；基于模糊属性（如姓名+地址）的去重虽可在原则上使用相同 MPC 方法，但开销巨大，是重要的未来工作。密钥恢复假设用户至少能访问一个被允许的 web 账户，若所有账户同时丢失，则系统仍面临密钥不可恢复风险。

### 强关联论文

[81] Zhang F. 等. Town Crier: An authenticated data feed for smart contracts. **ACM CCS 2016** [Google Scholar](https://scholar.google.com/scholar?q=Town+Crier+An+authenticated+data+feed+for+smart+contracts)

[82] Zhang F. 等. DECO: Liberating web data using decentralized oracles for TLS. **ACM CCS 2020** [Google Scholar](https://scholar.google.com/scholar?q=DECO+Liberating+web+data+using+decentralized+oracles+for+TLS)

[66] Sonnino A. 等. Coconut: Threshold issuance selective disclosure credentials with applications to distributed ledgers. **arXiv 2018** [Google Scholar](https://scholar.google.com/scholar?q=Coconut+Threshold+issuance+selective+disclosure+credentials+with+applications+to+distributed+ledgers)

[23] Borge M. 等. Proof-of-personhood: Redemocratizing permissionless cryptocurrencies. **IEEE EuroS&PW 2017** [Google Scholar](https://scholar.google.com/scholar?q=Proof+of+personhood+Redemocratizing+permissionless+cryptocurrencies)

[76] World Wide Web Consortium (W3C). Verifiable credentials data model implementation report 1.0. **W3C 2019** [Google Scholar](https://scholar.google.com/scholar?q=Verifiable+credentials+data+model+implementation+report+1+0)

[71] W3C. Decentralized identifiers (DIDs) v0.11, 2018. [Google Scholar](https://scholar.google.com/scholar?q=Decentralized+Identifiers+DIDs+v0+11)

[32] Decentralized Identity Foundation. 2020. [Google Scholar](https://scholar.google.com/scholar?q=Decentralized+Identity+Foundation)

[10] uPort: Open identity system for the decentralized web, 2020. [Google Scholar](https://scholar.google.com/scholar?q=uPort+Open+identity+system+for+the+decentralized+web)

[18] Bagherzandi A. 等. Password-protected secret sharing. **ACM CCS 2011** [Google Scholar](https://scholar.google.com/scholar?q=Password+protected+secret+sharing)

[58] Roberts J. J. 等. Nearly 4 million Bitcoins lost forever, new study says. **Fortune 2017** [Google Scholar](https://scholar.google.com/scholar?q=Nearly+4+million+Bitcoins+lost+forever+new+study+says)


## 关键词

+ 去中心化身份
+ 女巫攻击防护
+ 遗留系统兼容
+ 密钥恢复
+ 去中心化节点委员会
+ 隐私保护凭证