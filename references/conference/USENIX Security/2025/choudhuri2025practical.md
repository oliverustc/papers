---
title: Practical mempool privacy via one-time setup batched threshold encryption
标题简称: 
论文类型: conference
会议简称: USENIX Security
发表年份: 2025
created: 2025-04-28 11:34:05
modified: 2025-04-28 16:05:21
---

## Practical mempool privacy via one-time setup batched threshold encryption

## 发表信息

+ [archive链接](https://eprint.iacr.org/2024/1516)
+ [code](https://github.com/guruvamsi-policharla/batched-threshold-pp)

## 作者

+ [Arka Rai Choudhuri](Arka%20Rai%20Choudhuri.md)
+ [Sanjam Garg](Sanjam%20Garg.md) 
+ [Guru-Vamsi Policharla](Guru-Vamsi%20Policharla.md)
+ [Mingyuan Wang](Mingyuan%20Wang.md) 

## 笔记

### 背景与动机
在去中心化金融（DeFi）生态系统中，客户端提交的交易在内存池（mempool）中公开可见，这使其极易受到抢跑、尾随等市场操纵行为的影响，即矿工可提取价值（MEV）问题 [DGK+20]。除了避免市场操纵，客户端还可能出于在交易中包含敏感时效信息等原因，希望交易内容在执行前保持私密，即拥有待处理交易隐私（pending transaction privacy）。因此，设计一种实用的内存池隐私方案至关重要 [CGPP24]。现有的密码学方案存在明显瓶颈：传统阈值公钥加密 [DF90, DDFY94] 需为每批 B 笔交易广播 O(nB) 信息；一些细粒度加密方案 [DHMW23, Shu21] 虽将通信降至 O(n)，却无法保证待处理交易隐私，即未选中交易的信息也会泄露；最近的工作 [CGPP24] 虽同时具备 O(n) 通信和待处理交易隐私，但其代价是昂贵的初始多方计算（MPC）设置以及额外的每周期（per-epoch）设置。本文旨在构造第一个实用的方案，仅需一次性轻量级分布式密钥生成（DKG）设置，即可同时实现 O(1) 的单方通信开销、常量大小的密文和完整的待处理交易隐私。

### 相关工作

[ElG86, BO22, PNS23] 使用传统的阈值公钥加密方案.
> 核心思路：客户端使用系统公钥加密，解密服务器使用密钥份额进行阈值解密。
> 局限与区别：解密每批 B 笔交易需要 O(nB) 的通信量，当交易量增大时难以扩展。

[DHMW23, MGZ22, Shu21] 提出了更高效的方案，例如 McFly [DHMW23] 和 Shutter 网络 [Shu21].
> 核心思路：允许客户端针对特定周期加密，使得解密通信量降低至 O(n)，且初始设置仅需 DKG。
> 局限与区别：这些方案不支持待处理交易隐私。一旦解密了某个周期，所有加密到该周期的交易（包括未被选中的）都会被解密，违反了核心隐私要求。

[CGPP24] 正式定义了内存池隐私所需的安全属性，并构造了批量阈值加密原语.
> 核心思路：利用 KZG 多项式承诺 [KZG10] 和配对产品方程（PPE）构造可证安全的方案，通过一个可解释的承诺实现批量解密，通信量为 O(n)，并保证了待处理交易隐私。
> 局限与区别：该方案需要一个基于通用 MPC 的昂贵初始设置，并且每周期都需要一个额外的 epoch 设置。本文仅需一次性 DKG 设置，回避了复杂的 MPC 协议。

### 核心技术与方案

本文的核心思想是构建一个基于配对产品方程（PPE）的批处理阈值加密方案，其安全性依赖于一个新引入的交互式假设 i-kzg。整体框架包含设置（Setup）、加密（Enc）、批量解密（BatchDec）和组合（Combine）四个算法。

**构造思路**：方案的核心是让客户端加密一个“声明”，该声明包含两个配对产品方程，这两个方程必须同时满足才能解密。
1.  **移位的 BLS 签名 (Shifted BLS)**: 为消除对每周期新鲜承诺（commitment）的需要，并防止攻击者随意构造欺骗性见证（witness），委员会不直接签名承诺本身，而是签名一个经过公开随机群元素“移位”后的值。具体而言，委员会需要生成一个 BLS 签名 σ 作用于 `H(eid)/com`，其中 `com` 是由委员会最终选定的多项式承诺。这使得攻击者要么需要伪造 BLS 签名，要么需要打破 KZG 承诺的绑定性质，在代数群模型（AGM）下可归约到离散对数困难问题。
2.  **承诺作为见证 (Commitment as Witness)**: 客户端加密时，将 KZG 承诺 `com` 也作为见证的一部分。客户端证明自己知道一个 KZG 打开证明 π，可以在点 x̂ 处打开某一承诺 com 得到值 tg，并且知道一个 BLS 签名 σ 作用于 `H(eid)/com`。这样，在设置阶段就不再需要预先抽样一个随机的承诺。

**关键协议流程**：
用户加密时，选择一个随机点 x̂ ∈ Ω，以及随机数 s 和 α, β。计算 S = g^s, tg = H_F(S)。密文包含四个群元素 (`ct^(1)`, `ct^(2)`, `ct^(3)`, `ct^(4)`)，一个值 S，点 x̂ 和一个 NIZK 证明 Φ。
- 批量解密时，委员会首先从选中的 B 个密文中提取 (x̂, tg) 对。他们插值出一个 B-1 次的多项式 p(X) 以计算承诺 `com = g^(p(τ))`。接着，每个服务器 j 广播其部分签名 `σ_j = (H_G(eid)/com)^([sk]_j)`。
- 组合时，任何方都可以通过拉格朗日插值恢复出完整的签名 σ。然后，使用从 `com` 计算出的 KZG 打开证明 π 和签名 σ，结合密文中包含的 `ct^(2)`, `ct^(3)`, `ct^(4)`，通过一系列配对运算和哈希，即可恢复出明文 M。

**安全性证明直觉**：安全性证明在代数群模型的可编程随机预言机（ROM）下进行。证明的关键在于论证新引入的 i-kzg 假设的困难性，并将其归约到更为标准的 (B-1)-dlog 假设（Lemma 4）。安全证明的结构（Theorem 5）构建了一系列混合论证（hybrid argument），从真实世界逐步过渡到理想世界，模拟器（Simulator）能够在不泄露任何信息的情况下，通过编程随机预言机来描述解密过程，从而证明协议能安全地模拟理想功能。

**渐进复杂度**：
- **通信量**：解密一个批次 B 笔交易，每个解密服务器仅需广播一个 G_1 群元素（常量为 48 字节），总通信量为 O(n)，与 B 无关。
- **计算量**：
    - 客户端加密：O(1) 时间，独立于委员会大小和批次大小。
    - 服务器批量解密：O(B log B) 时间，主要用于计算 KZG 打开证明。
    - 消息恢复：O(B log B) 时间，同样主要受限于 KZG 证明验证和计算。

### 核心公式与流程

**[配对产品方程 (PPEs) 系统]**
$$ e(\text{com} \cdot g^{-\text{tg}}, h) = e(\pi , h^{(\tau - \hat{x})}) $$
$$ e(H(\text{eid}) \cdot \text{com}^{-1}, \text{pk}) = e(\sigma , h) $$
> 作用：构成客户端加密的“声明”。第一个方程验证 KZG 承诺 `com` 在点 x̂ 打开到值 tg（证明为 π）。第二个方程验证签名 σ 是对 `H(eid)/com` 的有效 BLS 签名。`com`, `π`, `σ` 是见证，`tg`, `x̂`, `eid` 是公共声明的一部分。

**[用户加密流程 (Enc)]**
客户端执行：
1. 抽样随机数 $\hat{x} \in \Omega$, $s \xleftarrow{\$} \mathbb{F}$, 计算 $S = g^s$, $\text{tg} = H_F(S)$。
2. 抽样随机数 $\alpha, \beta \xleftarrow{\$} \mathbb{F}$。
3. 计算密文群元素：
   $\text{ct}^{(1)} := H(e(H_G(\text{eid}) \cdot g^{-\text{tg}}, h)^\alpha) \oplus M$
   $\text{ct}^{(2)} := h^{\alpha(\tau - \hat{x})}$
   $\text{ct}^{(3)} := h^\alpha \text{pk}^\beta$
   $\text{ct}^{(4)} := h^\beta$
4. 生成 NIZK 证明 Φ，声明知道 $\alpha, \beta, s$ 使得上述关系成立。
> 作用：这是客户端加密交易的详细步骤。见证是 $\alpha, \beta, s$，通过 NIZK 证明这些值被正确使用。

**[批量解密与组合流程 (BatchDec & Combine)]**
- **BatchDec**: 委员会对选中的 B 个密文 $( \text{ct}_1, \ldots, \text{ct}_B )$，计算多项式 $p(X)$（满足 $p(\text{ct}_i.\hat{x}) = \text{tg}_i$），生成承诺 $\text{com} = g^{p(\tau)}$。每个服务器 j 广播部分签名 $\sigma_j = (H_G(\text{eid}) / \text{com})^{[\text{sk}]_j}$。
- **Combine**: 验证并插值部分签名得到完整签名 $\sigma$（满足 $e(H_G(\text{eid})/\text{com}, \text{pk}) = e(\sigma, h)$）。计算 KZG 打开证明 $\pi_i$（$q_i(X) = (p(X) - \text{tg}_i)/(X - \text{ct}_i.\hat{x})$）。解密每个密文：
  $m_i = \text{ct}_i^{(1)} \oplus H(e(\pi_i, \text{ct}_i^{(2)}) \cdot e(\delta, \text{ct}_i^{(3)}) \cdot e(\sigma^{-1}, \text{ct}_i^{(4)}))$
> 作用：这是委员会如何以 O(1) 通信量实现批量解密，以及任意方如何恢复出所有明文的完整步骤。关键点在于，只需要广播一个签名 $\sigma$（由部分签名重构），所有选中的交易都可被解密。

### 实验结果

实验使用 Rust 编程语言实现，基于 arkworks 密码学库 [ac22] 和 BLS12-381 配对友好曲线，在单核 2.4 GHz Intel Core i9 处理器上运行。为进行公平比较，本文与最相关的工作 [CGPP24] 进行了直接对比。
- **加密性能**：加密一笔交易约需 8.5 毫秒，与委员会规模无关；密文大小约为 466 字节，比 [CGPP24] 的方案（约 35% 的密文大小增加）略大。这是为大幅简化设置所付出的合理代价。
- **批量解密性能**：
    - 对于约 500 笔交易的一个区块（类似以太坊），每个委员会成员计算部分解密约需 3.2 秒，重构所有消息约需 3.0 秒。
    - 部分解密的大小仅为 48 字节（一个 G_1 元素），比 [CGPP24] 小 40%。
    - 虽然计算时间比 [CGPP24] 慢约 20%，但最大的改进在于：本文仅需一次性 DKG 设置，而 [CGPP24] 需要昂贵的基于 MPC 的设置和每周期设置。
- **与传统方案对比**：
    - 相比传统阈值方案（其部分解密总大小为 O(nB)），本文的通信效率有显著提升（例如，n=128, B=512 时，传统方案约 3 MB，本文仅 6 KB）。
    - 相比不提供待处理交易隐私的方案（如 [Shu21]），本文在类似通信开销下提供了更强的安全性。
- **委员会变更**：委员会成员的加入/离开可以通过主动秘密共享（Proactive Secret Sharing）技术处理，根据 [CGPP24] 的基准测试，在 64 人委员会和模拟的广域网环境下，这一过程可以在 10 秒内完成。

### 局限性与开放问题
1. 方案的安全性基于随机预言机模型和代数群模型，并引入了一个新的交互式假设（i-kzg）。虽然在论文中证明其可归约到标准 (B-1)-dlog 假设，但实际部署时需要一个不需要信任可编程随机预言机的标准模型方案。
2. 协议依赖于一个 NIZK 证明系统来处理密文的不可延展性（CCA2 安全性），虽然可以使用高效的 Sigma 协议，但这增加了加密方的计算开销（占用了绝大部份的加密时间）和密文大小。
3. 设置阶段虽然只需要一次性的 DKG，但仍然假定了一个可信任的密钥生成方或一个去中心化的密钥生成协议。对于大规模部署，委员会的密钥生成和成员轮换过程中的活跃秘密共享步骤仍需在实际网络条件下进一步验证其效率。

### 强关联论文

[CGPP24] Arka Rai Choudhuri, Sanjam Garg, Julien Piet, and Guru-Vamsi Policharla. Mempool privacy via batched threshold encryption: Attacks and defenses. **USENIX Security 2024** [Google Scholar](https://scholar.google.com/scholar?q=Mempool+Privacy+via+Batched+Threshold+Encryption+Attacks+and+Defenses)

[DHMW23] Nico Döttling, Lucjan Hanzlik, Bernardo Magri, and Stella Wohnig. McFly: Verifiable encryption to the future made practical. **FC 2023** [Google Scholar](https://scholar.google.com/scholar?q=McFly+Verifiable+encryption+to+the+future+made+practical)

[Shu21] Shutter Network contributors. The shutter network. **2021** [Google Scholar](https://scholar.google.com/scholar?q=Shutter+Network)

[BO22] Joseph Bebel and Dev Ojha. Ferveo: Threshold decryption for mempool privacy in BFT networks. **ePrint 2022** [Google Scholar](https://scholar.google.com/scholar?q=Ferveo+Threshold+Decryption+for+Mempool+Privacy+in+BFT+Networks)

[ElG86] Taher ElGamal. On computing logarithms over finite fields. **CRYPTO 1985** [Google Scholar](https://scholar.google.com/scholar?q=On+computing+logarithms+over+finite+fields)

[DGKS20] Philip Daian, Steven Goldfeder, Tyler Kell, Yunqi Li, Xueyuan Zhao, Iddo Bentov, Lorenz Breidenbach, and Ari Juels. Flash boys 2.0: Frontrunning in decentralized exchanges, miner extractable value, and consensus instability. **IEEE S&P 2020** [Google Scholar](https://scholar.google.com/scholar?q=Flash+Boys+2.0+Frontrunning+in+Decentralized+Exchanges+Miner+Extractable+Value+and+Consensus+Instability)


## 关键词

+ 内存池隐私保护
+ 一次性DKG批量阈值加密
+ 待处理交易隐私
+ 抗前置交易攻击
+ DeFi隐私保护机制
+ 分布式密钥生成协议