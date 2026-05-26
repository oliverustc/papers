---
title: "Cryptographic oracle-based conditional payments"
标题简称:
论文类型: preprint
预印本简称: archive
发表年份: 2022
created: 2025-04-29 10:49:13
modified: 2025-04-29 10:50:01
---

## Cryptographic oracle-based conditional payments

## 发表信息

+ [原文链接](https://www.ndss-symposium.org/ndss-paper/cryptographic-oracle-based-conditional-payments/)

## 作者

+ Varun Madathil 
+ Sri AravindaKrishnan Thyagarajan 
+ Dimitrios Vasilopoulos 
+ Lloyd Fournier 
+ [Giulio Malavolta](Giulio%20Malavolta.md)
+ Pedro Moreno-Sanchez 

## 笔记

### 背景与动机

在去中心化金融的许多场景中，支付往往需要依赖于链外真实世界事件的发生，例如金融仲裁、预支付、交易对赌等。这类应用需要一个称为“预言机”的第三方实体来证明事件结果，并以此触发支付。这种“基于预言机的条件支付”是连接现实世界与区块链的核心组件，其应用范围远超加密货币本身。然而，设计一个安全、高效且不依赖双方信任的解决方案极具挑战：收款方Bob不能提前获得付款方Alice的签名，否则无论事件结果如何他都能取款；而Bob也不能依赖Alice事后提供签名，因为Alice可能离线。现有的解决方案，如Discreet Log Contracts (DLC)，虽然对比特币友好，但存在诸多瓶颈：它不支持高效的分布式信任（在多预言机场景下会导致指数级组合爆炸），要求预言机与Alice同步（需要预言机定期发布秘密值），并且缺乏正式的安全模型，容易遭受流氓密钥攻击和混搭攻击。相比之下，基于智能合约的方案虽然理论上可行，但会牺牲可扩展性、同质化，并产生高昂的链上成本。本文旨在填补这一空白，为基于预言机的条件支付提供一个形式化的密码学基础，并提出高效、可证明安全的构造，以解决现有方案在分布式信任、隐私和安全性方面的根本性缺陷。

### 相关工作

[21] T. Dryja. Discreet log contracts. **Technical Report 2020** [Google Scholar](https://scholar.google.com/scholar?q=Discreet+log+contracts)
> 核心思路：提出了DLC方案，利用适配器签名和预言机，在比特币网络上实现条件支付，无需智能合约。
> 局限与区别：DLC不支持高效的分布式信任（需要指数级组合），要求预言机同步，且缺乏形式化安全证明，易受攻击。本文的方案通过VweTS解决了所有这些问题，支持高效的阈值签名且无需同步。

[20] N. Döttling et al. Mcfly: Verifiable encryption to the future made practical. **Cryptology ePrint Archive 2022** [Google Scholar](https://scholar.google.com/scholar?q=McFly+Verifiable+encryption+to+the+future+made+practical)
> 核心思路：提出了一个基于阈值签名的见证加密方案，用于实现定时加密。
> 局限与区别：该方案不关心加密消息的结构（即不验证其是否为有效签名）。本文的技术核心在于高效地证明被加密消息的结构（即它是一个有效签名），并为此提出了新的批处理技术。

[38] F. Zhang et al. Town Crier: An authenticated data feed for smart contracts. **ACM CCS 2016** [Google Scholar](https://scholar.google.com/scholar?q=Town+Crier+An+authenticated+data+feed+for+smart+contracts)
> 核心思路：利用可信执行环境（TEE）来提供经认证的预言机数据。
> 局限与区别：该方案依赖TEE硬件假设，其安全性在实践中不明确，且仍需智能合约的支持。本文的方案无需可信硬件，完全基于密码学假设。

[39] F. Zhang et al. DECO: Liberating web data using decentralized oracles for TLS. **ACM CCS 2020** [Google Scholar](https://scholar.google.com/scholar?q=DECO+Liberating+web+data+using+decentralized+oracles+for+TLS)
> 核心思路：用去中心化预言机取代TEE，利用TLS协议证明数据来源。
> 局限与区别：该方案仍依赖于智能合约来最终执行逻辑。本文的方案在链下完成所有逻辑，链上仅需一次常规签名验证，无需智能合约。

[23] S. Eskandari et al. SoK: Oracles from the ground truth to market manipulation. **ACM AFT 2021** [Google Scholar](https://scholar.google.com/scholar?q=SoK+Oracles+from+the+ground+truth+to+market+manipulation)
> 核心思路：对预言机问题进行了系统化知识梳理，提出了模块化工作流。
> 局限与区别：该工作是系统化分析，未提出新的条件支付解决方案，与本文直接构造协议的目标正交。

[30] Y. Lindell and B. Riva. Cut-and-choose Yao-based secure computation in the online/offline and batch settings. **CRYPTO 2014** [Google Scholar](https://scholar.google.com/scholar?q=Cut-and-choose+Yao-based+secure+computation+in+the+online/offline+and+batch+settings)
> 核心思路：提出了针对混淆电路的批处理cut-and-choose技术，以摊销安全参数的代价。
> 局限与区别：该技术原本用于安全多方计算。本文借鉴其思想，将其创新性地应用于见证加密的验证中，实现了高效的“批处理式”可验证性。

### 核心技术与方案

本文的核心贡献是提出并构造了一个新的密码学原语——基于阈值签名的可验证见证加密（VweTS）。该原语允许Alice加密一个支付签名，并使其解密条件取决于从多个预言机处获得足够数量的、关于某个特定事件结果的签名。整个构造包含两个层次：首先是为单种情况设计的**基于适配器签名的基础方案**，然后是为应对大量事件结果而设计的**VweTS扩展方案**。

**1. 整体框架与核心思路**
VweTS方案的核心思路是将问题分解为两个部分：**消息加密**与**身份验证**。
- **消息加密**：Alice要加密的“消息”是她对支付的授权签名 $\sigma$。为了加密这个签名，Alice将见证加密（WES）与一个**适配器签名**（或直接使用BLS签名，取决于具体构造）结合。她首先生成一个预签名 $\hat{\sigma}$，该预签名本身不是有效签名，但可以和一个秘密值 $y$ 结合（“适配”）成一个完整签名 $\sigma$。
- **身份验证**：解密过程的关键是秘密值 $y$。Alice将 $y$ 进一步通过**阈值秘密共享**分解成 $N$ 份共享 $y_1, ..., y_N$，每个共享对应一个预言机。然后，利用**基于BLS签名的见证加密方案**（WES），她将每个共享 $y_i$ 加密成一个密文，该密文的解密条件是知道对应预言机在事件结果 $m$ 上的签名。
- **可验证性**：上述过程面临的核心挑战是：Bob需要在不持有任何预言机签名的情况下，相信Alice的密文确实包含了正确共享，并且这些共享能够用于恢复 $y$。为了解决这个问题，本文采用了**批处理Cut-and-Choose**技术。Alice生成大量冗余的WES密文，Bob随机要求Alice打开其中一部分以验证其正确性，而对于未被打开的部分，Bob通过概率论证确信至少有一个密文是诚实的。为了应对任意数量的预言机，该Cut-and-Choose过程被设计成“桶映射”的形式：未被打开的密文被随机映射到不同的“桶”中，每个桶对应一个预言机，只要每个桶内至少有一个诚实密文，安全就能得到保证。该过程通过Fiat-Shamir启发式改为非交互。

**2. 基于适配器签名的基础方案构造**
- **构造思路**：该方案利用适配器签名来封装支付签名 $\sigma$。首先，Alice为每个可能的事件结果 $j$ 生成一个预签名 $\hat{\sigma}_j$。预签名对应的秘密 $y_j$ 被阈值分享成 $y_{j,1},...,y_{j,N}$。
- **关键步骤**：
    1. **生成承诺**：Alice生成 $2NMB$ 个WES密文对 $c'_i$（基于一个随机密钥 $\overline{vk}^*$ 和随机消息 $\overline{m}^*$），每个密文加密一个随机数 $r_i$。同时计算 $R_i = g^{r_i}$。这些将用于之后的Cut-and-Choose。
    2. **生成承诺的参数**：Alice计算哈希 $H_2$ 来确定哪些密文对会被打开（$b_i=1$），以及剩余的 $NMB$ 个密文对被映射到哪个桶 $\Phi(i)=(\alpha, \beta)$。
    3. **处理未打开密文**：对于每个未被打开的密文对（索引 $i$ 且 $b_i=0$），Alice首先根据桶映射找到对应的预言机 $\beta$ 和事件结果 $\alpha$。然后，她为该桶生成另一个WES密文 $c_i$，该密文加密相同的随机数 $r_i$，但使用预言机 $\beta$ 的密钥和事件消息 $\overline{m}_\alpha$。同时，她计算 $s_i = r_i + y_{\alpha, \beta}$（其中 $y_{\alpha, \beta}$ 是 $y_\alpha$ 的一个共享），并生成一个NIZK证明 $\pi_i$ 来证明 $c_i$ 和 $c'_i$ 加密了同一个 $r_i$。
    4. **验证**：Bob通过随机打开（$b_i=1$）的密文检查Alice是否诚实地生成，并通过检查 $g^{s_i} = R_i \cdot Y_{\alpha,\beta}$ 来验证未打开密文中 $s_i$ 与 $y_{\alpha,\beta}$ 的一致性。
    5. **解密**：当Bob从 $\rho$ 个预言机处获得对事件 $\overline{m}_j$ 的签名后，他就能解密对应的WES密文，得到 $r_i$，从而计算出共享 $y_{\beta} = s_i - r_i$。拥有 $\rho$ 个共享后，Bob就能重构秘密 $y_j$，然后将预签名 $\hat{\sigma}_j$ 适配为完整签名 $\sigma_j$。
- **安全性直觉**：**One-wayness** 依赖于适配器签名的不可伪造性和WES的选择明文安全（IND-CPA），通过一系列混合论证，最终归约到敌手无法伪造适配器签名。**Verifiability** 依赖于Cut-and-Choose参数的正确选择（每个桶至少有B个密文，且 $B \ge \lambda / \log(MN) + 1$），确保至少有一个未被打开的密文是正确生成，并结合NIZK的可靠性，保证解密能恢复正确的签名共享。

**3. VweTS扩展方案**
- **构造思路**：为了降低对结果数量 $M$ 的依赖，该方案不再为每个结果都生成完整的Cut-and-Choose证明，而是将问题转化为证明“结果编号的每一位”。Alice将所有的秘密 $y_j$ 替换为一个由 $\mu = \log M$ 个随机数对组成的集合 $\{z_{0,i}, z_{1,i}\}_{i=1}^\mu$。每个结果 $j$ 对应的秘密 $y_j$ 变成了 $y_j = e_j - \sum_i z_{j[i], i}$，其中 $e_j$ 是Alice发布的一个公开值，$j[i]$ 是 $j$ 的第 $i$ 位。
- **关键步骤**：
    1. Alice为每个 $z_{b,i}$ 生成一个见证加密实例，条件是预言机证明事件结果的第 $i$ 位等于 $b$。
    2. 发起Cut-and-Choose时，总的WES密文数从与M线性相关变为与 $2\mu$ 线性相关，极大地节省了计算和通信开销。
    3. 解密时，Bob只需从预言机处获得 $\mu$ 个签名（每个对应一位），解密得到所有 $z_{j[i], i}$，即可计算出 $y_j$，再恢复支付签名。
- **安全性直觉**：在一个结果 $j$ 被揭露后，对应的 $z_{j[i], i}$ 可以被获知，但对于另一个结果 $j*$，至少有一位 $i*$ 使得 $j*[i*] \neq j[i*]$，因此 $z_{j*[i*], i*}$ 仍然是安全的。这个性质通过归约到离散对数问题得以证明。

### 核心公式与流程

**[BLS签名方案]**
$$ 
\begin{aligned}
&\text{KeyGen}(1^\lambda): \alpha \leftarrow \mathbb{Z}_q, vk := g_0^\alpha, sk := \alpha \\
&\text{Sign}(sk, m): \sigma := H(m)^{sk} \in \mathbb{G}_1 \\
&\text{Vf}(vk, m, \sigma): e(g_0, \sigma) = e(vk, H(m))
\end{aligned}
$$
> 作用：预言机BLS签名、支付方BLS签名以及WES加密函数的核心组件。

**[基于BLS签名的见证加密（WES）]**
$$ 
\begin{aligned}
\text{Enc}((\tilde{vk}, \tilde{m}), m): & \\
& r_1 \leftarrow \mathbb{Z}_q, r_2 \leftarrow \mathbb{G}_T \\
& c_1 := g_0^{r_1} \\
& c_2 := e(\tilde{vk}, H_0(\tilde{m}))^{r_1} \cdot r_2 \\
& c_3 := H_1(r_2) + m \\
\text{Dec}(\tilde{\sigma}, c): & \\
& r := c_2 \cdot e(c_1, \tilde{\sigma})^{-1} \\
& m := c_3 - H_1(r)
\end{aligned}
$$
> 作用：用于加密秘密值（如 $r_i$ 或 $y_{\alpha,\beta}$），解密需要对应的BLS签名。

**[VweTS核心验证方程（基于适配器签名方案）]**
$$ 
g^{s_i} = R_i \cdot Y_{\alpha, \beta}
$$
> 作用：在Cut-and-Choose过程中验证未打开密文中 $s_i$ 与适配器秘密共享 $y_{\alpha,\beta}$ 的一致性，是确保解密密文能恢复正确秘密的关键。

**[VweTS扩展方案的秘密恢复]**
$$ 
y_{j} = e_{j} - \sum_{i=1}^{\mu} z_{j[i], i}
$$
> 作用：将支付签名对应的秘密 $y_j$ 与结果编号的每一位上预言机的签名关联起来，实现了从线性依赖到对数依赖的转变。

### 实验结果

实验在配备四核Intel Core i7 2.3 GHz和16 GB RAM的机器上进行，所有操作在同一台机器上运行（通过localhost通信），实现语言为Rust。实验评估了两个系统参数：预言机数量/阈值和事件结果数量。核心性能数据显示，即使对于阈值4-of-7、事件结果数高达1024的场景，计算开销仍低于25秒，通信开销低于2.3 MB。当结果数提升至 $2^{15}$，在相同的4-of-7阈值下，计算时间升至约150秒，通信开销约15 MB。与Discreet Log Contracts (DLC) 的对比实验表明，在小结果数场景下DLC更快，但由于DLC的复杂度随预言机数量呈指数增长，VweTS在更多预言机（如5-of-9）或更多结果（如超过$2^{10}$）时性能明显优于DLC。实验还验证了通过单调函数编码（如范围证明）可以进一步减少所需密文数量。总体而言，VweTS在常见参数设置下在商品硬件上展现了良好的实用性，且可扩展性优于DLC。

### 局限性与开放问题

VweTS虽然在性能和安全性上优于DLC和智能合约方案，但仍存在一些局限。首先，该方案依赖于非交互零知识证明（NIZK）和双线性配对，这些密码学原语的效率影响整体性能，尤其是在移动设备或资源受限的环境下。其次，虽然VweTS支持分布式信任，但其安全性前提是预言机是半诚实的，抵抗合谋攻击的能力依赖于阈值设置（t-of-N），对有状态或自适应安全的预言机模型考虑不足。未来的工作可以探索如何将VweTS与更通用的属性基加密（ABE）结合，以实现更灵活的断言逻辑，或者研究在量子计算机威胁下的后量子版本。

### 强关联论文

[21] T. Dryja. Discreet log contracts. **Technical Report 2020** [Google Scholar](https://scholar.google.com/scholar?q=Discreet+log+contracts)

[30] Y. Lindell and B. Riva. Cut-and-choose Yao-based secure computation in the online/offline and batch settings. **CRYPTO 2014** [Google Scholar](https://scholar.google.com/scholar?q=Cut-and-choose+Yao-based+secure+computation+in+the+online/offline+and+batch+settings)

[10] L. Aumayr et al. Generalized channels from limited blockchain scripts and adaptor signatures. **International Conference on the Theory and Application of Cryptology and Information Security 2021** [Google Scholar](https://scholar.google.com/scholar?q=Generalized+channels+from+limited+blockchain+scripts+and+adaptor+signatures)

[12] D. Boneh and M. K. Franklin. Identity-based encryption from the Weil pairing. **CRYPTO 2001** [Google Scholar](https://scholar.google.com/scholar?q=Identity-based+encryption+from+the+Weil+pairing)

[13] D. Boneh, B. Lynn, and H. Shacham. Short signatures from the Weil pairing. **ASIACRYPT 2001** [Google Scholar](https://scholar.google.com/scholar?q=Short+signatures+from+the+Weil+pairing)

[24] S. Garg et al. Witness encryption and its applications. **ACM STOC 2013** [Google Scholar](https://scholar.google.com/scholar?q=Witness+encryption+and+its+applications)

[15] J. Camenisch and I. Damgård. Verifiable encryption, group encryption, and their applications to separable group signatures and signature sharing schemes. **ASIACRYPT 2000** [Google Scholar](https://scholar.google.com/scholar?q=Verifiable+encryption%2C+group+encryption%2C+and+their+applications+to+separable+group+signatures+and+signature+sharing+schemes)

[36] A. Shamir. How to share a secret. **Communications of the ACM 1979** [Google Scholar](https://scholar.google.com/scholar?q=How+to+share+a+secret)

[22] A. Erwig et al. Two-party adaptor signatures from identification schemes. **PKC 2021** [Google Scholar](https://scholar.google.com/scholar?q=Two-party+adaptor+signatures+from+identification+schemes)

[16] M. Chase. Multi-authority attribute based encryption. **TCC 2007** [Google Scholar](https://scholar.google.com/scholar?q=Multi-authority+attribute+based+encryption)


## 关键词

+ 基于预言机条件支付区块链
+ VweTS阈值签名可验证见证加密
+ 分布式信任ObC支付协议
+ 剪切选择批处理技术
+ Schnorr ECDSA BLS签名条件支付