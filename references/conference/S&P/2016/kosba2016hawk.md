---
title: "Hawk: The blockchain model of cryptography and privacy-preserving smart contracts"
doi: 10.1109/sp.2016.55
标题简称:
论文类型: conference
会议简称: S&P
发表年份: 2016
---
## Hawk: The blockchain model of cryptography and privacy-preserving smart contracts

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/7546538)

## 作者

+ [Ahmed Kosba](Ahmed%20Kosba.md)
+ [Andrew Miller](Andrew%20Miller.md) 
+ [Elaine Shi](Elaine%20Shi.md)
+ Zikai Wen 
+ [Charalampos Papamanthou](Charalampos%20Papamanthou.md) 


## 笔记

### 背景与动机
区块链和智能合约系统（如比特币 [48] 和以太坊 [57]）允许互不信任的参与方在没有可信第三方的情况下安全交易，依靠去中心化共识保证正确性和可用性，且区块链内置的离散时钟可在合约中止时实现财务公平（通过没收押金惩罚作弊方）。然而，现有系统完全缺乏事务隐私：所有交易（包括金额和伪名间的资金流动）都公开记录在区块链上，且已有图分析攻击可去除伪名匿名性 [42][52]。尽管 Zerocash [11] 等隐私加密货币提供了匿名转账，但它们放弃了可编程性，无法支持智能合约中的复杂逻辑（如拍卖、金融衍生品）。Hawk 首次在同一个系统中同时实现了事务隐私与可编程性：程序员无需实现密码学即可编写隐私智能合约，编译器自动生成基于零知识证明的密码协议，使合约参与方与区块链交互时，资金的流通和金额对公众隐藏。

### 相关工作

[11] Ben-Sasson et al. Zerocash: Decentralized Anonymous Payments from Bitcoin. **S&P 2014** [Google Scholar](https://scholar.google.com/scholar?q=Zerocash+Decentralized+Anonymous+Payments+from+Bitcoin)
> 核心思路：使用零知识证明（zk-SNARK）实现匿名数字货币交易，通过 mint 和 pour 操作隐藏发送方、接收方和金额。
> 局限与区别：不具备可编程性，无法支持智能合约；且其安全定义是基于区分性（indistinguishability）而非模拟安全性，难以直接嵌入 UC 框架。

[57] Wood. Ethereum: A Secure Decentralized Transaction Ledger. **2014** [Google Scholar](https://scholar.google.com/scholar?q=Ethereum+A+Secure+Decentralized+Transaction+Ledger)
> 核心思路：首个图灵完备的区块链智能合约平台，允许用户编写任意程序并在区块链上执行。
> 局限与区别：所有交易数据在区块链上公开，无事务隐私保障；Hawk 通过其私有合约部分隐藏了数据与金额。

[49] Parno et al. Pinocchio: Nearly Practical Verifiable Computation. **S&P 2013** [Google Scholar](https://scholar.google.com/scholar?q=Pinocchio+Nearly+Practical+Verifiable+Computation)
> 核心思路：提出高效的 zk-SNARK 系统，用于验证任意计算，证明大小和验证时间与计算规模无关。
> 局限与区别：原始 SNARK 不满足模拟可提取性，无法直接用于 UC 协议；Hawk 采用 Kosba 等 [38] 的提升变换使其具备 UC 安全性。

[7] Andrychowicz et al. Secure Multiparty Computations on Bitcoin. **S&P 2013** [Google Scholar](https://scholar.google.com/scholar?q=Secure+Multiparty+Computations+on+Bitcoin)
> 核心思路：利用 Bitcoin 脚本实现公平的模 n 安全多方计算，通过押金和超时实现财务公平。
> 局限与区别：无法隐藏交易金额和资金流向；仅针对特定应用（如抽奖），缺乏通用平台；依赖 Bitcoin 有限的脚本语言。

[17] Bentov and Kumaresan. How to Use Bitcoin to Design Fair Protocols. **CRYPTO 2014** [Google Scholar](https://scholar.google.com/scholar?q=How+to+Use+Bitcoin+to+Design+Fair+Protocols)
> 核心思路：利用 Bitcoin 的“claim-or-refund”原语构建公平协议，保证在作弊或中止时诚实方获得补偿。
> 局限与区别：同样缺乏事务隐私；其 on-chain 开销为 O(N²) 轮和 O(N²) 笔交易，而 Hawk 在通用区块链模型下可实现 O(N) on-chain 成本。

[40] Kumaresan and Bentov. How to Use Bitcoin to Incentivize Correct Computations. **CCS 2014** [Google Scholar](https://scholar.google.com/scholar?q=How+to+Use+Bitcoin+to+Incentivize+Correct+Computations)
> 核心思路：使用 Bitcoin 的“multi-lock”抽象为可验证计算提供经济激励，保证诚实计算。
> 局限与区别：事务公开，且协议复杂度高；Hawk 通过零知识证明既验证计算又隐藏输入输出。

[12] Ben-Sasson et al. SNARKs for C: Verifying Program Executions Succinctly and in Zero Knowledge. **CRYPTO 2013** [Google Scholar](https://scholar.google.com/scholar?q=SNARKs+for+C+Verifying+Program+Executions+Succinctly+and+in+Zero+Knowledge)
> 核心思路：将 C 程序编译为 SNARK 电路，支持通用计算的简洁零知识证明。
> 局限与区别：SNARK 需要可信设置和电路相关的公共参考串，且不提供模拟可提取性；Hawk 在最终化阶段使用普通 SNARK（不需要提取），在冻结和计算阶段使用提升后的 SNARK。

[38] Kosba et al. How to Use SNARKs in Universally Composable Protocols. **ePrint 2015** [Google Scholar](https://scholar.google.com/scholar?q=How+to+Use+SNARKs+in+Universally+Composable+Protocols)
> 核心思路：提出高效变换使 SNARK 满足模拟可提取性，适用于 UC 框架。
> 局限与区别：该变换本身增加一定开销；Hawk 采纳此变换用于 freeze 和 compute 操作，但 finalize 由于可跳过提取而直接使用普通 SNARK 以节省开销。

[53] Szabo. Formalizing and Securing Relationships on Public Networks. **First Monday 1997** [Google Scholar](https://scholar.google.com/scholar?q=Formalizing+and+Securing+Relationships+on+Public+Networks)
> 核心思路：提出智能合约概念，强调用密码学和协议实现合同自动执行。
> 局限与区别：未涉及区块链的具体实现；Hawk 是首个将智能合约与匿名数字货币结合的实用系统。

### 核心技术与方案

Hawk 的整体协议由两个层次组成：底层是私有钱币系统（Private Cash），类似 Zerocash 的 mint/pour 操作，实现匿名转账；上层是 Hawk 特定原语 freeze、compute 和 finalize，将私有钱币与可编程逻辑绑定。系统依赖一个称为“管理器”的辅助方，管理器可以看到用户的输入（因此被信任不会泄露隐私），但即使管理器恶意或与用户合谋，也无法影响合约结果的正确性，因为所有关键步骤都通过零知识证明保证。

**私有钱币系统**：区块链维护一个币集合 Coins，每个币是形如 $(\mathcal{P}, \text{coin}:= \text{Comm}_s(\$val))$ 的承诺。mint 操作将公开账本资金转入私有池，产生一个新币。pour 操作将两个输入币（来自同一用户 $\mathcal{P}$）转换为两个输出币（可指向不同接收方 $\mathcal{P}_1, \mathcal{P}_2$），并保持总金额守恒。为证明合法性，用户构造零知识证明 $\pi$ 满足关系 $\mathcal{L}_{\text{POUR}}$：输入币存在于 Merkle 树（其根为 MT.root）、序列号 $sn_i = \text{PRF}_{sk_{\text{prf}}}(\mathcal{P}||\text{coin}_i)$ 未被用过、输出币是正确承诺且金额守恒。该证明隐藏了具体花费了哪些币以及金额（零知识性质），从而实现了事务隐私。

**Hawk 特有原语**：每个 Hawk 合约包含私有部分 $\phi_{\text{priv}}$ 和公共部分 $\phi_{\text{pub}}$。协议步骤如下：
1. **Freeze**（冻结）：用户 $\mathcal{P}_i$ 选择一个私有钱币 $(\mathcal{P}_i, \text{coin})$，计算序列号 $sn$，并生成承诺 $cm = \text{Comm}_{s'}(\$val || in || k)$，其中 $in$ 为私有输入，$k$ 为对称密钥。然后提交零知识证明 $\pi$ 满足 $\mathcal{L}_{\text{FREEZE}}$：存在一个币在 Coins 中且其值与 $cm$ 中的 $\$val$ 相等，$sn$ 计算正确。区块链验证证明后将 $sn$ 加入 SpentCoins（防止双花），记录 $cm$。此时资金被冻结在合约中。
2. **Compute**（计算）：用户在时间 $T_1$ 到 $T_2$ 之间将输入打开给管理器：加密 $(\$val || in || k || s')$ 到管理器的公钥下，并附带零知识证明 $\mathcal{L}_{\text{COMPUTE}}$ 证明 $cm$ 确实承诺了这些值。管理器解密后获得所有用户的输入，计算 $\phi_{\text{priv}}$ 得到输出金额 $\{\$val'_i\}$ 和公共输出 $out$。
3. **Finalize**（最终化）：管理器为每个接收方生成新币 $coin'_i = \text{Comm}_{s'_i}(\$val'_i)$ 并用对称密钥 $k_i$ 加密 $(s'_i || \$val'_i)$，然后提交零知识证明 $\mathcal{L}_{\text{FINALIZE}}$：所有 $cm_i$（缺失用户的视为 (0,⊥,⊥)）与输入一致，$\phi_{\text{priv}}$ 计算正确，输出币金额总和等于输入币金额总和，且每个 $coin'_i$ 是正确承诺。区块链验证证明后，将新币添加到 Coins，并将密文发送给各用户，用户用自己的 $k_i$ 解密获得新币。

**安全直觉**：通过零知识证明，区块链（公众）只能看到冻结时公开的 $cm$ 和序列号，但看不到金额和输入数据；管理器看到所有输入，但它无法伪造证明（因为证明需要正确的 $s, \$val, in$ 等）。利用 SNARK 的模拟可提取性（freeze 和 compute 阶段）和普通 SNARK（finalize 阶段），可以证明整个协议 UC 安全地模拟了理想功能 $\mathcal{F}(\text{IdealP}_{\text{hawk}})$。所需假设：Merkle 树哈希抗碰撞、承诺完美绑定且计算隐藏、NIZK 计算零知识且模拟可提取、加密语义安全、PRF 安全。

**复杂度**：用户侧（pour/freeze/compute）证明时间约 $20s$ 量级，独立于参与方数；管理器侧 finalize 证明时间随参与方数线性增长，100 个参与方时用 4 核约 $2.85$ 分钟；区块链验证时间极短（约 10–20 ms）。On-chain 存储方面，全局现金协议验证密钥 23 KB，每个 Hawk 合约额外需 13–114 KB（与参与方数相关）。

### 核心公式与流程

**[冻结关系 LFREEZE]**
$$
( \text{statement}, \text{witness}) \in \mathcal{L}_{\text{FREEZE}} \\
\text{statement} = (\mathcal{P}, \text{MT.root}, \text{sn}, \text{cm}) \\
\text{witness} = (\text{coin}, \text{sk}_{\text{prf}}, \text{branch}, s, \$val, \text{in}, k, s') \\
\text{coin} = \text{Comm}_s(\$val) \land \text{MerkleBranch}(\text{MT.root}, \text{branch}, (\mathcal{P} \|\text{coin})) \\
\land \mathcal{P}.\text{pk}_{\text{prf}} = \text{PRF}_{\text{sk}_{\text{prf}}}(0) \land \text{sn} = \text{PRF}_{\text{sk}_{\text{prf}}}(\mathcal{P} \|\text{coin}) \\
\land \text{cm} = \text{Comm}_{s'}(\$val \| \text{in} \| k)
$$
> 作用：零知识证明用户冻结的币确实存在于私有池中，序列号正确，且承诺的金额与币值一致。

**[计算关系 LCOMPUTE]**
$$
( \text{statement}, \text{witness}) \in \mathcal{L}_{\text{COMPUTE}} \\
\text{statement} = (\mathcal{P}_{\mathcal{M}}, \text{cm}, \text{ct}) \\
\text{witness} = (\$val, \text{in}, k, s', r) \\
\text{cm} = \text{Comm}_{s'}(\$val \| \text{in} \| k) \land \text{ct} = \text{ENC}(\mathcal{P}_{\mathcal{M}}.\text{epk}, r, (\$val \| \text{in} \| k \| s'))
$$
> 作用：证明用户打开的密文与冻结时的承诺一致，即正确将输入发送给了管理器。

**[最终化关系 LFINALIZE]**
$$
( \text{statement}, \text{witness}) \in \mathcal{L}_{\text{FINALIZE}} \\
\text{statement} = (\text{in}_{\mathcal{M}}, \text{out}, \{\text{cm}_i, \text{coin}'_i, \text{ct}_i\}_{i\in[N]}) \\
\text{witness} = (\{s_i, \$val_i, \text{in}_i, s'_i, k_i\}_{i\in[N]}) \\
(\{\$val'_i\}_{i\in[N]}, \text{out}) = \phi_{\text{priv}}(\{\$val_i, \text{in}_i\}_{i\in[N]}, \text{in}_{\mathcal{M}}) \\
\sum_{i\in[N]} \$val_i = \sum_{i\in[N]} \$val'_i \\
\forall i: ( \text{cm}_i = \text{Comm}_{s_i}(\$val_i \| \text{in}_i \| k_i) ) \lor (\$val_i, \text{in}_i, k_i, s_i, \text{cm}_i) = (0, \bot, \bot, \bot, \bot)\\
\land \text{ct}_i = \text{SENC}_{k_i}(s'_i \| \$val'_i) \land \text{coin}'_i = \text{Comm}_{s'_i}(\$val'_i)
$$
> 作用：证明管理器最终计算的输出正确，金额守恒，每个输出币被正确密文加密给相应接收方。

### 实验结果

实验在 Amazon EC2 r3.8xlarge 虚拟机上执行，支持 80 位和 112 位安全级别。对于用户侧操作（pour、freeze、compute），80 位安全级别下：pour 证明时间 12.4 秒（4核）或 27.5 秒（单核），freeze 证明时间 8.4 秒（4核）或 20.7 秒（单核），compute 证明时间 9.3 秒（4核）或 22.5 秒（单核）。112 位安全级别下相应时间增加约 50%。验证时间极短，均在 10 ms 左右。管理器侧 finalize 操作：对于密封拍卖合约，10 个竞拍者时证明时间 15.4 秒（4核），100 个竞拍者时 169.3 秒（约 2.85 分钟），验证时间仅 10–20 ms。SNARK 公共参考字符串（CRS）中只有验证密钥需上链：全局现金协议 23 KB，每个 Hawk 合约 13–114 KB（10–100 用户）。采用 SNARK 友好的密码学实现（Ajtai 哈希、Speck 对称加密等）比朴素实现节省 2.0–2.6 倍运算量。协议优化（finalize 中跳过模拟可提取 SNARK、用对称加密代替公钥加密）共带来 10 倍加速。所有情况下管理器计算成本对应 EC2 费用低于 \$0.14（100 用户时）。

### 局限性与开放问题
管理器虽然不需要被完全信任，但它能看到所有用户的输入，因此用户依赖于管理器不泄露事后隐私。若希望完全去除对管理器的信任，可引入安全多方计算或可信硬件（如 Intel SGX），但复杂度会大幅增加。SNARK 的公共参考串需要可信设置，且每个合约需生成独立的 CRS，当前使用可复用 MPC 或硬件辅助设置，但仍是部署障碍。此外，合约参与方数量存在上限（需预先声明），这可通过递归 SNARK 缓解但性能开销更高。最后，如何设计经济学激励（如入场费防女巫攻击）和更高效的 on-chain 验证仍是开放问题。

### 强关联论文

[11] E. Ben-Sasson, A. Chiesa, C. Garman, M. Green, I. Miers, E. Tromer, and M. Virza. Zerocash: Decentralized anonymous payments from Bitcoin. **S&P 2014** [Google Scholar](https://scholar.google.com/scholar?q=Zerocash+Decentralized+anonymous+payments+from+Bitcoin)

[49] B. Parno, C. Gentry, J. Howell, and M. Raykova. Pinocchio: Nearly practical verifiable computation. **S&P 2013** [Google Scholar](https://scholar.google.com/scholar?q=Pinocchio+Nearly+practical+verifiable+computation)

[57] G. Wood. Ethereum: A secure decentralized transaction ledger. **2014** [Google Scholar](https://scholar.google.com/scholar?q=Ethereum+A+secure+decentralized+transaction+ledger)

[7] M. Andrychowicz, S. Dziembowski, D. Malinowski, and L. Mazurek. Secure Multiparty Computations on Bitcoin. **S&P 2013** [Google Scholar](https://scholar.google.com/scholar?q=Secure+Multiparty+Computations+on+Bitcoin)

[17] I. Bentov and R. Kumaresan. How to Use Bitcoin to Design Fair Protocols. **CRYPTO 2014** [Google Scholar](https://scholar.google.com/scholar?q=How+to+Use+Bitcoin+to+Design+Fair+Protocols)

[40] R. Kumaresan and I. Bentov. How to Use Bitcoin to Incentivize Correct Computations. **CCS 2014** [Google Scholar](https://scholar.google.com/scholar?q=How+to+Use+Bitcoin+to+Incentivize+Correct+Computations)

[38] A. Kosba, Z. Zhao, A. Miller, H. Chan, C. Papamanthou, R. Pass, abhi shelat, and E. Shi. How to use SNARKs in universally composable protocols. **ePrint 2015** [Google Scholar](https://scholar.google.com/scholar?q=How+to+use+SNARKs+in+universally+composable+protocols)

[12] E. Ben-Sasson, A. Chiesa, D. Genkin, E. Tromer, and M. Virza. SNARKs for C: verifying program executions succinctly and in zero knowledge. **CRYPTO 2013** [Google Scholar](https://scholar.google.com/scholar?q=SNARKs+for+C+verifying+program+executions+succinctly+and+in+zero+knowledge)

[48] S. Nakamoto. Bitcoin: A Peer-to-Peer Electronic Cash System. **2009** [Google Scholar](https://scholar.google.com/scholar?q=Bitcoin+A+Peer-to-Peer+Electronic+Cash+System)

[53] N. Szabo. Formalizing and securing relationships on public networks. **First Monday 1997** [Google Scholar](https://scholar.google.com/scholar?q=Formalizing+and+securing+relationships+on+public+networks)


## 关键词

+ 隐私保护智能合约
+ 零知识证明
+ 区块链形式化模型
+ 去中心化交易隐私
+ 自动密码协议生成