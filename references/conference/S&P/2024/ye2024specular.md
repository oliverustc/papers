---
title: "Specular: Towards Secure, Trust-minimized Optimistic Blockchain Execution"
标题简称:
论文类型: conference
会议简称: S&P
发表年份: 2024
modified: 2025-04-08 23:07:02
---

## Specular: Towards Secure, Trust-minimized Optimistic Blockchain Execution

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/10646707)

## 作者

+ Zhe Ye
+ Ujval Misra
+ Jiajun Cheng
+ Wenyang Zhou
+ [Dawn Song](Dawn%20Song.md)

## 笔记

### 背景与动机

乐观Rollup通过将计算外包至无信任的L2链，并利用交互式欺诈证明协议解决状态声明分歧，为区块链扩容提供了一条可行路径。然而，当前主流的乐观Rollup方案如Arbitrum Nitro [5]和Optimism Bedrock [6]，其欺诈证明系统采用“编译式”设计——L1裁判直接仲裁特定L2客户端二进制文件的执行轨迹，而非抽象协议规范。这种方法将二进制文件与协议本身混为一谈，导致三个根本性缺陷：第一，放大了单一文化故障风险，因为它阻碍了无许可的N版本编程；第二，导致信任计算基过于庞大复杂，难以独立审计和形式化验证；第三，升级过程频繁且不透明，增加了审计负担并扩大了治理攻击面。本文旨在填补现有工作对于乐观Rollup中NVP与欺诈证明协议设计之间关系系统化研究的空白，提出一种直接仲裁L2语义的原生欺诈证明方案，以实现最小化信任计算基的、具备弹性的乐观Rollup。

### 相关工作

[1] Wood et al. Ethereum: A secure decentralised generalised transaction ledger. **Ethereum project yellow paper 2014** [Google Scholar](https://scholar.google.com/scholar?q=Ethereum%3A+A+secure+decentralised+generalised+transaction+ledger)
> 核心思路：定义了以太坊EVM的形式化状态转换模型和指令集。
> 局限与区别：本文将其作为L2执行语义的规范目标，直接在其基础上构建证明系统，而非编译至更低级ISA。

[2] Kalodner et al. Arbitrum: Scalable, private smart contracts. **USENIX Security 2018** [Google Scholar](https://scholar.google.com/scholar?q=Arbitrum%3A+Scalable%2C+private+smart+contracts)
> 核心思路：提出了首个基于交互式欺诈证明的乐观Rollup原型，采用定制AVM。
> 局限与区别：其原生AVM设计虽支持理论上的1-NVP，但实际需要从头开发独立客户端，工程成本极高；本文通过机会主义复用现有以太坊客户端规避此问题。

[5] Bousfield et al. Arbitrum Nitro: A second-generation optimistic rollup. **2022** [Google Scholar](https://scholar.google.com/scholar?q=Arbitrum+Nitro%3A+A+second-generation+optimistic+rollup)
> 核心思路：将EVM编译为WASM进行欺诈证明仲裁，支持更丰富的函数调用流程。
> 局限与区别：依赖编译工具链，导致TCB膨胀、NVP受限、升级不透明；本文直接仲裁EVM语义，TCB仅含L1裁判。

[6] Optimism Bedrock Explainer. **Optimism Docs 2023** [Google Scholar](https://scholar.google.com/scholar?q=Bedrock+explainer+%7C+optimism+docs)
> 核心思路：将EVM编译为MIPS进行欺诈证明，复用Geth作为L2客户端。
> 局限与区别：面临与Nitro相同的编译式路径固有缺陷；本文通过原生EVM证明系统实现机会主义NVP。

[8] Canetti et al. Refereed delegation of computation. **Information and Computation 2013** [Google Scholar](https://scholar.google.com/scholar?q=Refereed+delegation+of+computation)
> 核心思路：提出了两方非共谋服务器下的交互式二分搜索证明协议。
> 局限与区别：原始RDoC假设固定、非共谋的服务器委员会；本文将其拓展至无需许可的多方设置，并适配区块链的激励机制。

[12] Knight et al. An experimental evaluation of the assumption of independence in multiversion programming. **IEEE TSE 1986** [Google Scholar](https://scholar.google.com/scholar?q=An+experimental+evaluation+of+the+assumption+of+independence+in+multiversion+programming)
> 核心思路：实验证明NVP中独立开发程序的故障往往存在隐藏相关性，降低预期效益。
> 局限与区别：本文指出定制化NVP存在此问题，但机会主义复用现有成熟客户端可有效规避相关性风险。

[13] Breidenbach et al. Enter the hydra: Towards principled bug bounties and exploit-resistant smart contracts. **USENIX Security 2018** [Google Scholar](https://scholar.google.com/scholar?q=Enter+the+hydra%3A+Towards+principled+bug+bounties+and+%E2%80%89Exploit-Resistant%E2%80%89+smart+contracts)
> 核心思路：提出KNVP概念用于智能合约的安全决策。
> 局限与区别：该工作在合约层应用NVP；本文将其思想引入ORU的TCB最小化，并实现1-of-N特性。

[21] Hildenbrandt et al. KEVM: A complete formal semantics of the ethereum virtual machine. **CSF 2018** [Google Scholar](https://scholar.google.com/scholar?q=KEVM%3A+A+complete+formal+semantics+of+the+ethereum+virtual+machine)
> 核心思路：提供了EVM的完整形式化语义框架。
> 局限与区别：KEVM主要用于规范分析；本文将其作为验证L1裁判与规范一致性的潜在目标，以进一步缩小TCB。

[33] Canetti et al. Practical delegation of computation using multiple servers. **CCS 2011** [Google Scholar](https://scholar.google.com/scholar?q=Practical+delegation+of+computation+using+multiple+servers)
> 核心思路：提出了基于哈希函数的实用化RDoC协议，包括二分搜索和单步证明。
> 局限与区别：原始协议假设固定委员会；本文将其仲裁逻辑适配至EVM的复杂指令集和账户模型。

### 核心技术与方案

本文的核心贡献是提出并实现了一个“L2原生”的欺诈证明方案Specular，该方案的关键抽象在于将仲裁目标从客户端二进制提升至L2规范本身，即EVM的语义。这样做从根本上解锁了机会主义的1-of-N版本编程特性。

首先，在概念层面，本文区分了“编译式”与“原生式”两种设计范式。编译式方案将L2客户端源码编译为低级别ISA的二进制，L1裁判仲裁该二进制的执行轨迹。这导致二进制与协议耦合，阻碍了NVP。原生式方案则构建一个仅包含规范语义的抽象轨迹，L1裁判直接仲裁该轨迹上的状态转换。由于所有符合规范的L2客户端在该抽象轨迹上产生相同的执行过程，它们可以互操作。因此，只要有一个诚实节点运行正确的客户端，就能确保系统安全，而无需大多数客户端共同正确。这种1-of-N特性使得任何实现规范的客户端均可无许可参与，极大增强了系统的抗故障能力。

其次，在具体技术实现上，本文为EVM设计了一个简单的一步证明方案。该方案的核心是构建一个称为“一步状态”的认证数据结构。该结构封装了EVM的完整状态，但通过使用散列函数（如Merkle树）对其内部组件（如栈、内存、世界状态）进行承诺，使得证明者可以在不揭示全部状态的情况下，仅提供与当前指令相关的部分状态子证明。整个证明系统由一对算法Prover和Verifier定义。Prover输入当前一步状态和下一状态，输出一个包含所有必要子证明的证明π；Verifier输入π、初始状态承诺h和声称的最终状态承诺h‘，通过模拟单步执行来验证状态转换的正确性。具体而言，Verifier首先检查π中的状态揭示是否与h一致，然后使用π中的子证明（如栈证明、内存证明、世界状态证明等）来模拟指令执行，最后检查模拟得到的最终状态承诺是否等于h’。对内存和世界状态的访问，通过Merkle证明实现对数级别的揭示和更新。对于可能无限访问内存的指令（如KECCAK256），方案采用子步骤分解，将一次操作拆分为多个操作在固定大小内存块上的子步骤，以防止证明成本超出L1区块Gas限制。

该方案的安全性依赖于碰撞抵抗哈希函数。其完备性保证：对于正确的状态转换，诚实证明者总能生成一个能被验证者接受的证明。其可靠性保证：对于错误的状态转换，任何恶意证明者都无法伪造一个能通过验证的证明，因为找到碰撞伪造哈希路径在计算上是不可行的。系统的通信复杂度在正常运行期间为常量（仅发送状态承诺）；在争议期间，交互式二分搜索的轮数为状态执行步数的对数，单步证明的大小与访问的存储和内存量成线性关系。

### 核心公式与流程

**[一步状态哈希承诺结构，以合约内交易内状态为例]**
$$ \begin{aligned} \omega_{\text{intra}} &= \{ \text{batch}, \text{blockNumber}, \text{transactionIdx}, I_e, \mu_g, A_r, H_{\text{oss}}(\text{lastDepthState}), I_a, \sigma[I_a]_c, I_s, I_v, \text{callFlag}, \text{out}, \text{outSize}, \\ 
&\quad \mu_{pc}, I_b[\mu_{pc}], \text{size}(\mu_s), H_{\text{stack}}(\mu_s), \text{size}(\mu_m), r(\mu_m), \text{size}(I_d), r(I_d), \text{size}(\mu_o), r(\mu_o), r(\sigma), H(A_t), r(\text{accessList}), H(A_l) \} \end{aligned} $$
> 作用：定义了合约内一步状态的数据序列化结构，该散列是整个证明系统的核心绑定承诺。将栈、内存、世界状态等组件的根哈希（r(*)）或链式哈希（H(*)）纳入计算，使得验证者无需拥有完整状态即可验证。这些组件哈希在后续的单步指令证明中，可以通过提供Merkle证明或哈希链前缀来进行部分揭示和验证。

**[一步证明验证算法]**
```pseudo
procedure VERIFY(π, h, h')
    assert h == H_OSS(π_ω)       // 检查揭示的状态与承诺一致
    VERIFYDATA(π)                // 验证L1数据证明(如交易calldata)的一致性
    ω' ← EMULATE(π)             // 模拟单步状态转换
    assert h' == H_OSS(ω')       // 检查转换后状态的承诺
end procedure

procedure EMULATE(π)
    if next step is a consensus validation step then
        ω' ← EMULATECONSENSUSSTEP(π_ω, π_d)
    else
        for each component proof π_c in π_C do
            h_c ← corresponding commitment in π_ω
            authenticate π_c against h_c  // 验证组件的Merkle证明
        end for
        ω' ← EMULATEEXECSTEP(π_ω, π_d, π_C)  // 使用揭示的组件状态模拟指令执行
    end if
    return ω'
end procedure
```
> 作用：这是EVM单步证明验证的核心流程。验证者首先将证明π中的状态揭示π_ω进行哈希，确保其与双方已达成共识的初始状态承诺h一致。然后验证L1数据证明π_d（如用于获取交易上下文）。最后，验证者使用EMULATE函数，通过解释π中包含的子证明（如栈、内存、世界状态的Merkle证明）来模拟指令的执行，并计算新状态的承诺h’。如果模拟的结果与声称的最终承诺一致，则证明被接受。

### 实验结果

实验在一台配备Intel i9-13900K @ 5.80 GHz处理器、64 GB内存的桌面电脑上进行，运行Ubuntu Windows Subsystem for Linux。为评估一步证明性能，作者在与Uniswap V2、Ethereum Name Service和Ballot三个流行应用交互的300笔交易中，生成了约40万个执行步骤的单步证明。

在证明大小方面，平均一步证明大小为558字节，其中最小为323字节，最大为3684字节（不包含合约字节码）。当包含合约字节码后，平均大小增至约11.6 KB，最大可达29.6 KB。证明生成时间平均约为0.739毫秒，几乎可以忽略。

验证成本方面，不包含合约字节码时，平均Gas消耗约为109k Gas，最大约897k Gas。当包含合约字节码后，平均Gas消耗增至约629k Gas，最大可达1,874k Gas。由于以太坊合约字节码大小上限为24KB，作者估计最坏情况下的验证Gas消耗不会超过3,000k Gas，仅占以太坊区块Gas上限（约3,000万）的10%，因此验证成本在实际中是可行的。实验还展示了不同指令的验证成本分布，例如SSTORE由于其需要多个Merkle Patricia树证明，验证成本较高；KECCAK256由于子步骤分解，其验证成本分布呈现双峰特征。

对于机会主义NVP的验证，使用SpecErigon（基于Erigon的客户端）作为L2客户端生成的证明与SpecGeth（基于Geth）生成的证明是一致的，均能通过验证。虽然SpecErigon的平均证明生成时间为6.5毫秒，是SpecGeth的大约10倍，但这一延迟仍然可以忽略。

### 局限性与开放问题

本文的工作主要集中在安全性和弹性，未对欺诈证明的性能进行深度优化，其L1验证成本在包含合约字节码时平均约629k Gas，对于高频争议场景可能构成挑战。未来的工作可以设计一个双层证明系统，以更高效的证明系统（如SNARK）作为默认快路径，而以本文的简单系统作为更可信的失败回退，从而在不牺牲信任最小化特性的前提下大幅降低验证成本。此外，本文尚未对L2共识层客户端和证明者应用1-NVP，这是后续工作可以完善的方向。

### 强关联论文

[1] Wood et al. Ethereum: A secure decentralised generalised transaction ledger. **Ethereum project yellow paper 2014** [Google Scholar](https://scholar.google.com/scholar?q=Ethereum%3A+A+secure+decentralised+generalised+transaction+ledger)

[2] Kalodner et al. Arbitrum: Scalable, private smart contracts. **USENIX Security 2018** [Google Scholar](https://scholar.google.com/scholar?q=Arbitrum%3A+Scalable%2C+private+smart+contracts)

[5] Bousfield et al. Arbitrum Nitro: A second-generation optimistic rollup. **2022** [Google Scholar](https://scholar.google.com/scholar?q=Arbitrum+Nitro%3A+A+second-generation+optimistic+rollup)

[6] Optimism Bedrock Explainer. **Optimism Docs 2023** [Google Scholar](https://scholar.google.com/scholar?q=Bedrock+explainer+%7C+optimism+docs)

[8] Canetti et al. Refereed delegation of computation. **Information and Computation 2013** [Google Scholar](https://scholar.google.com/scholar?q=Refereed+delegation+of+computation)

[9] Our pragmatic path to decentralization. **Optimism Blog 2022** [Google Scholar](https://scholar.google.com/scholar?q=Our+pragmatic+path+to+decentralization)

[12] Knight et al. An experimental evaluation of the assumption of independence in multiversion programming. **IEEE TSE 1986** [Google Scholar](https://scholar.google.com/scholar?q=An+experimental+evaluation+of+the+assumption+of+independence+in+multiversion+programming)

[13] Breidenbach et al. Enter the hydra: Towards principled bug bounties and exploit-resistant smart contracts. **USENIX Security 2018** [Google Scholar](https://scholar.google.com/scholar?q=Enter+the+hydra%3A+Towards+principled+bug+bounties+and+%E2%80%89Exploit-Resistant%E2%80%89+smart+contracts)

[21] Hildenbrandt et al. KEVM: A complete formal semantics of the ethereum virtual machine. **CSF 2018** [Google Scholar](https://scholar.google.com/scholar?q=KEVM%3A+A+complete+formal+semantics+of+the+ethereum+virtual+machine)

[33] Canetti et al. Practical delegation of computation using multiple servers. **CCS 2011** [Google Scholar](https://scholar.google.com/scholar?q=Practical+delegation+of+computation+using+multiple+servers)


## 关键词

+ 乐观Rollup安全
+ 争议解决协议
+ EVM语义感知证明
+ 可信计算基最小化
+ 以太坊客户端多样性
+ 区块链二层扩展