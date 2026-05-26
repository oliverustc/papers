---
title: "zkCross: A novel architecture for Cross-ChainPrivacy-Preserving auditing"
标题简称:
论文类型: conference
会议简称: USENIX Security
发表年份: 2024
---

## ZkCross: A novel architecture for Cross-ChainPrivacy-Preserving auditing

## 发表信息

+ [原文链接](https://www.usenix.org/conference/usenixsecurity24/presentation/guo-yihao)

## 作者

+ Yihao Guo 
+ Minghui Xu 
+ Xiuzhen Cheng 
+ Dongxiao Yu 
+ Wangjie Qiu 
+ Gang Qu 
+ Weibing Wang 
+ Mingming Song 


## 笔记

### 背景与动机
跨链技术是实现区块链间互操作性的重要手段，但现有跨链协议 [2] 普遍侧重于通用性、安全性和效率，忽视了隐私保护与审计这两个相互冲突的需求。隐私保护要求数据保密与最小化暴露，而审计则要求透明性与数据可访问性，这使得两者在单链系统中已难以兼得 [4, 7, 9, 34, 37]。在跨链场景下，这一矛盾因“信息孤岛”而进一步加剧：审计方无法直接获取异源链的全部交易数据，若在每条被审计链上注册全节点则需 TB 级存储，极不现实。本文首次系统性地识别了跨链隐私审计的三个核心挑战：跨链链接性暴露问题、隐私与审计的不兼容问题以及全审计低效问题。为填补这一空白，作者提出了 zkCross——一种新颖的双层跨链架构，通过三个基于零知识证明的协议，在无需可信第三方的前提下，同时实现跨链转账与交换的隐私保护以及高效的全审计。

### 相关工作

[1] Baldimtsi et al. Anonymous Sidechains. **DPM 2021** [Google Scholar](https://scholar.google.com/scholar?q=Anonymous+Sidechains)
> 核心思路：基于 Monero 平台设计匿名侧链方案。
> 局限与区别：隐私保护能力依赖底层链（如 Monero、Zcash），无法推广至其他区块链系统。

[6] Deshpande et al. Privacy-Preserving Cross-Chain Atomic Swaps. **FC 2020** [Google Scholar](https://scholar.google.com/scholar?q=Privacy-Preserving+Cross-Chain+Atomic+Swaps)
> 核心思路：基于 Schnorr 签名为 HTLC 添加隐私保护。
> 局限与区别：要求交互双方信任同一个秘密，这在互不信任的对手间难以达成；且方案仅支持跨链交换，不支持跨链转账。

[21] Yuxian Li et al. ZeroCross: A Sidechain-based Privacy-Preserving Cross-Chain Solution for Monero. **JPDC 2022** [Google Scholar](https://scholar.google.com/scholar?q=ZeroCross)
> 核心思路：基于 Monero 的隐私侧链方案。
> 局限与区别：同 [1]，方案与底层链强耦合，不具有通用性。

[30] Thyagarajan et al. Universal Atomic Swaps: Secure Exchange of Coins Across All Blockchains. **IEEE S&P 2022** [Google Scholar](https://scholar.google.com/scholar?q=Universal+Atomic+Swaps)
> 核心思路：使用可验证定时签名替代时间锁，实现通用原子交换。
> 局限与区别：属于桥接方案，依赖第三方组件，存在单点故障风险；未考虑隐私保护。

[31] Tsabary et al. MAD-HTLC: Because HTLC is Crazy-Cheap to Attack. **IEEE S&P 2021** [Google Scholar](https://scholar.google.com/scholar?q=MAD-HTLC)
> 核心思路：利用区块链激励机制抵御针对 HTLC 的激励操纵攻击。
> 局限与区别：仅关注 HTLC 的安全性，未涉及隐私保护或审计。

[36] Xie et al. zkBridge: Trustless Cross-Chain Bridges Made Practical. **CCS 2022** [Google Scholar](https://scholar.google.com/scholar?q=zkBridge)
> 核心思路：提出 deVirgo 证明系统以提升跨链桥的验证效率。
> 局限与区别：属于桥接方案，中心化风险较高；未考虑隐私保护。

[40] Yin et al. Bool Network: An Open, Distributed, Secure Cross-Chain Notary Platform. **IEEE TIFS 2022** [Google Scholar](https://scholar.google.com/scholar?q=Bool+Network)
> 核心思路：结合安全硬件与密码学技术增强公证人平台的安全性。
> 局限与区别：依赖于公证人这一第三方实体，存在单点故障风险。

[33] Xiaoyi Wang et al. A Supervisory and Governance Mechanism for Power Master-Slave Chain Architecture. **ICETCI 2021** [Google Scholar](https://scholar.google.com/scholar?q=Supervisory+and+Governance+Mechanism+for+Power+Master-Slave+Chain)
> 核心思路：提出“以链治链”的监管思路，用于电力系统主从链架构。
> 局限与区别：审计效率低，属于中继式全审计，复杂度为 O(k×m×n)。

### 核心技术与方案

**整体架构**：zkCross 采用双层架构，下层为多条可独立交互的普通链，上层为由审计节点构成的审计链。审计链的状态树以各普通链的状态树根作为叶子节点，建立层级关联。该架构将审计过程与下层跨链交互协议解耦，使得下层协议的设计更加灵活。

**协议 Θ（隐私保护跨链转账）**：针对 CLE 问题，Θ 协议通过隐藏接收方地址与转账金额来切断交易双方的链接性。金额隐藏采用固定面额机制（如将大额转账拆分为若干标准面额交易），从而在匿名集中产生等额交易。接收方地址通过哈希函数和零知识证明隐藏。具体流程为：
1.  **Burn**：发送方 $\mathcal{S}^I$ 在链 I 上构造并发送交易 $Tx_{Burn}$，包含转账金额 $v_{\mathcal{S}}$ 以及哈希值 $h(\widetilde{pk}_{\mathcal{R}^{II}}, r, sn)$，其中 $\widetilde{pk}_{\mathcal{R}^{II}}$ 为接收方公钥，$r$ 和 $sn$ 为随机数，$sn$ 随后用作该交易的唯一序列号以防止双花。发送方将资产锁定在合约 $\xi^I$ 中并设置超时 $T_3$。
2.  **Transmit**：共识后，发送方通过链下通道将 $r$、$sn$ 以及 $Tx_{Burn}$ 的 Merkle 证明（$h_{Burn}, root_{Burn}$）发送给接收方 $\mathcal{R}^{II}$。
3.  **Mint**（成功路径）：接收方构造电路 $\Lambda_{\Theta}$（包含哈希函数和 Merkle 证明验证逻辑），调用零知识证明算法得到 $\pi_{\Theta}$。证明公开输入为 $(\widetilde{pk}_{\mathcal{R}^{II}}, sn, v_{\mathcal{S}}, root_{Burn})$，私密输入为 $(\widetilde{pk}_{\mathcal{S}^I}, addr_{\xi^I}, r, h_{Burn})$。接收方将 $(\pi_{\Theta}, \widetilde{pk}_{\mathcal{R}^{II}}, sn, v_{\mathcal{S}}, root_{Burn})$ 打包为 $Tx_{Mint}$ 发送至链 II 的合约 $\xi^{II}$，合约验证 $\pi_{\Theta}$ 后向接收方发放资产。
4.  **Redeem**（超时路径）：若接收方超时未 Mint，发送方可构造类似证明（此时 $\widetilde{pk}_{\mathcal{R}^{II}}$ 变为私密输入），赎回被锁资产。

**协议 Φ（隐私保护跨链交换）**：针对 CLE 问题，Φ 协议的核心在于隐藏 HTLC 中的原像（preimage）。传统 HTLC 要求双方使用同一原像，导致可链接性。Φ 协议通过零知识证明证明两个独立原像间的关联，同时确保原子性。流程为：
1.  **Prepare**：发送方 $\mathcal{S}$ 生成两个原像 $(pre^I, pre^{II})$、两个随机序列号 $(sn^I, sn^{II})$ 和一个 256 位整数 $Z_{256}$，满足 $sn^I \oplus Z_{256} = sn^{II}$。发送方构造电路 $\Lambda_{\Phi}^{off}$，计算哈希值 $h(pre^I, sn^I)$ 和 $h(pre^{II}, sn^{II})$，生成证明 $\pi_{\Phi}^{off}$。证明与 $Z_{256}$、两哈希值、两原像通过链下发送给接收方。
2.  **Lock**：发送方在链 I 使用 $h(pre^I, sn^I)$ 锁定资产 $v_{\mathcal{S}}$，接收方在链 II 使用 $h(pre^{II}, sn^{II})$ 锁定资产 $v_{\mathcal{R}}$。双方设置时间锁 $T_1 > T_2$。
3.  **Unlock**（成功路径）：发送方 $\mathcal{S}^{II}$ 构造电路 $\Lambda_{\Phi}^{on}$（逻辑类似 $\Lambda_{\Theta}$），以 $sn^{II}$、$v_{\mathcal{R}}$、$root_{Lock}^{II}$ 为公开输入，以 $\widetilde{pk}_{\mathcal{R}^{II}}$、$pre^{II}$ 等为私密输入，生成证明 $\pi_{\Phi}^{II}$ 并提交，解锁接收方锁定的资产。接收方获得 $sn^{II}$ 后通过 XOR 运算得到 $sn^I$，构造类似证明 $\pi_{\Phi}^{I}$ 解锁发送方锁定的资产。
4.  **Refund**（超时路径）：若发送方超时未提交 $\pi_{\Phi}^{II}$，接收方无法获得 $sn^I$，双方资产均自动退还。

**协议 Ψ（高效跨链审计）**：针对 IPA 和 FAI 问题，Ψ 协议将交易聚合与审计功能压缩至一个零知识电路中，审计方只需验证聚合后的证明即可完成全审计。核心在于电路 $\Lambda_{\Psi}$，包含四个功能模块：
*   **审计功能**：根据具体任务（如检查地址是否在黑名单中）判断单笔交易或聚合交易的合法性。
*   **签名验证功能**：验证交易签名的正确性。
*   **状态转换功能**：验证交易执行前后状态树根的正确转换。
*   **根验证功能**：通过重算状态树根，确保承诺的新旧状态根与链上区块一致。
流程为：提交者从下层链收集一组已共识的交易，作为私密输入；以旧状态根和新状态根为公开输入，生成证明 $\pi_{\Psi}$，并提交至审计链。审计方调用 $\Pi.Verify$ 验证 $\pi_{\Psi}$，通过后更新状态根。基于 zk-SNARK 的简洁性，审计复杂度从传统全审计的 $O(k \times m \times n)$ 降至 $O(k \times m)$，效率提升约 $n$ 倍，同时交易内容不向审计方泄露，解决了 IPA 问题。

### 核心公式与流程

**[Θ.Burn交易定义]**
$$Tx_{Burn} \stackrel{{\text def}}{{=}} (From: \mathcal{S}; To: \xi; v_{\mathcal{S}}, h(\widetilde{pk}_{\mathcal{R}}, r, sn))$$
> 作用：定义跨链转账协议中的销毁交易，其中接收方地址通过哈希隐藏。

**[Θ.Mint交易定义]**
$$Tx_{\text{Mint}} \stackrel{{\text def}}{{=}} (From: \mathcal{R}; To: \xi; \pi, \widetilde{pk}_{\mathcal{R}}, sn, v, root_{\text{Burn}})$$
> 作用：定义跨链转账协议中的铸造交易，包含零知识证明 $\pi$ 用于验证 Burn 交易的存在性及金额、序列号等信息的正确性。

**[Φ.Lock交易定义]**
$$Tx_{\text{Lock}} \stackrel{{\text def}}{{=}} (From: \mathcal{S}/\mathcal{R}; To: \xi; v, h(\text{pre}, sn))$$
> 作用：定义跨链交换协议中的锁定交易，使用独立原像与序列号生成的哈希锁代替传统 HTLC 中的统一原像哈希。

**[Ψ.Commit交易定义]**
$$Tx_{\text{Commit}} \stackrel{{\text def}}{{=}} (From: \mathcal{C}_{\mathcal{T}}; To: \xi; \vec{x}, \pi)$$
> 作用：定义审计协议中的提交交易，包含状态根等公开输入 $\vec{x}$ 和证明 $\pi$，使审计方可在不获取交易内容的情况下验证状态转换的正确性。

### 实验结果
实验在云服务器（50 个 ecs.g6.3xlarge 实例，每实例 12 vCPU，48GB RAM）和本地服务器上展开，使用 Go-Ethereum 构建 200 节点的 PoW 区块链网络，采用 Groth16 算法和 xjsnark 库实现 zk-SNARK，用 Solidity 编写智能合约。隐私保护协议方面，随着节点数从 20 增至 100，Θ 协议中 $Tx_{Burn}$ 延迟从约 2.5 秒增至 5.5 秒，吞吐量从 72 TPS 降至 47 TPS；Φ 协议中 $Tx_{Lock}$ 延迟从约 2.0 秒增至 5.5 秒，吞吐量从 75 TPS 降至 49 TPS。Gas 消耗方面，Θ 协议为 494,000 Gas（约 1.72 美元），Φ 协议为 901,472 Gas（约 3.13 美元）。审计协议 Ψ 方面，当聚合 250 笔交易时，证明大小仅 127 字节，验证时间约 16.4 毫秒，远低于传统全审计的 35 秒；当交易数增至 10,000 时，Ψ 的审计时间仅约 40 秒，而传统方案需 3.15 小时，效率提升近 284 倍。与 zk-Rollup 相比，Ψ 在内部增加电路约束的同时，将公开输入和验证密钥的大小减少约 15 KB，节约约 1000 万 Gas。

### 局限性与开放问题
本文方案目前仅支持双层审计，未来可扩展到多层架构以支持更复杂的跨链场景。此外，系统在抵抗针对零知识证明本身（如适用于 Groth16 的恶意证明者攻击）或共识层面的攻击方面，仍有提升空间。zkCross 现假设至少存在一个诚实的提交者，该假设在现实多链环境中可能面临挑战，如何在不依赖此假设的前提下保证审计可靠性值得进一步研究。最后，协议中涉及的固定面额机制可能降低资金利用效率，设计更灵活的匿名值方案将是后续方向。

### 强关联论文

[6] Apoorvaa Deshpande, Maurice Herlihy. Privacy-Preserving Cross-Chain Atomic Swaps. **FC 2020** [Google Scholar](https://scholar.google.com/scholar?q=Privacy-Preserving+Cross-Chain+Atomic+Swaps)

[13] Jens Groth. On the Size of Pairing-Based Non-Interactive Arguments. **EUROCRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=On+the+Size+of+Pairing-Based+Non-Interactive+Arguments)

[21] Yuxian Li, Jian Weng, Ming Li, Wei Wu, Jiasi Weng, Jia-Nan Liu, Shun Hu. ZeroCross: A Sidechain-based Privacy-Preserving Cross-Chain Solution for Monero. **JPDC 2022** [Google Scholar](https://scholar.google.com/scholar?q=ZeroCross)

[30] Sri AravindaKrishnan Thyagarajan, Giulio Malavolta, Pedro Moreno-Sanchez. Universal Atomic Swaps: Secure Exchange of Coins Across All Blockchains. **IEEE S&P 2022** [Google Scholar](https://scholar.google.com/scholar?q=Universal+Atomic+Swaps)

[31] Itay Tsabary, Matan Yechieli, Alex Manuskin, Ittay Eyal. MAD-HTLC: Because HTLC is Crazy-Cheap to Attack. **IEEE S&P 2021** [Google Scholar](https://scholar.google.com/scholar?q=MAD-HTLC)

[32] Florian Tschorsch, Björn Scheuermann. Bitcoin and Beyond: A Technical Survey on Decentralized Digital Currencies. **IEEE COMST 2016** [Google Scholar](https://scholar.google.com/scholar?q=Bitcoin+and+Beyond)

[35] Gavin Wood. Polkadot: Vision for a Heterogeneous Multi-Chain Framework. **White Paper 2016** [Google Scholar](https://scholar.google.com/scholar?q=Polkadot)

[36] Tiancheng Xie, Jiaheng Zhang, Zerui Cheng, Fan Zhang, Yupeng Zhang, Yongzheng Jia, Dan Boneh, Dawn Song. zkBridge: Trustless Cross-Chain Bridges Made Practical. **CCS 2022** [Google Scholar](https://scholar.google.com/scholar?q=zkBridge)

[40] Zeyuan Yin, Bingsheng Zhang, Jingzhong Xu, Kaiyu Lu, Kui Ren. Bool Network: An Open, Distributed, Secure Cross-Chain Notary Platform. **IEEE TIFS 2022** [Google Scholar](https://scholar.google.com/scholar?q=Bool+Network)

[44] Yushu Zhang, Jiajia Jiang, Xuewen Dong, Liangmin Wang, Yong Xiang. BeDCV: Blockchain-Enabled Decentralized Consistency Verification for Cross-Chain Calculation. **IEEE TCC 2022** [Google Scholar](https://scholar.google.com/scholar?q=BeDCV)


## 关键词

+ zkCross跨链隐私保护审计
+ 双层跨链架构协议
+ 跨链关联性暴露防御
+ 零知识证明跨链隐私
+ 区块链信息孤岛问题
+ 隐私与审计兼容性