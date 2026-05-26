---
title: "Sweep-uc: Swapping coins privately"
标题简称:
论文类型: conference
会议简称: S&P
发表年份: 2024
created: 2025-05-09 14:39:35
modified: 2025-05-09 14:41:26
---

## Sweep-uc: Swapping coins privately

## 发表信息

+ [原文链接](https://ieeexplore.ieee.org/abstract/document/10646880)
+ [archive](https://eprint.iacr.org/2022/1605)

## 作者

+ [Lucjan Hanzlik](Lucjan%20Hanzlik.md)
+ Julian Loss Sri
+ AravindaKrishnan Thyagarajan
+ Benedikt Wagner

## 笔记

### 背景与动机
公平交换（原子交换）是加密货币的基本操作，但现有方案大多缺乏链上隐私，使得交易历史公开，损害了货币的可互换性。基于哈希时间锁合约（HTLC）的协议 [2,3] 虽然功能强大，却要求底层区块链支持特定脚本，导致与 Monero 等无脚本系统的不可兼容性，并且脚本交易费用远高于普通签名验证交易，也使被交换的硬币易于被追踪。另一些协议依赖中间方（如 Tumblebit [13]、A^2L [14] 系列）来提供隐私和引导问题，但 Tumblebit 仍需要 HTLC，而 A^2L 及后续 A^2L+ [26] 和 BlindHub [15] 要么安全性证明有漏洞或依赖过于理想化的模型，要么需要通用两方计算（GP-2PC）或通用零知识证明（GP-ZK），导致效率低下。此外，这些协议大多只能支持适配器签名，无法覆盖使用唯一签名（如 BLS [30]）的区块链。本文旨在构造第一个同时满足效率、最小化脚本、广泛兼容（同时支持适配器签名和唯一签名）、且在 UC 框架下安全可证明的 bootstrapped 隐私交换协议。

### 相关工作

[13] Heilman 等. TumbleBit: An untrusted bitcoin-compatible anonymous payment hub. **NDSS 2017** [Google Scholar](https://scholar.google.com/scholar?q=TumbleBit+An+untrusted+bitcoin-compatible+anonymous+payment+hub)
> 核心思路：使用中间方（tumbler）和盲签名实现不可链接的原子交换。
> 局限与区别：依赖 HTLC 脚本，导致兼容性差、交易费用高、可追踪性差；本文完全不需要 HTLC，仅依赖签名验证脚本。

[14] Tairi 等. A^2L: Anonymous atomic locks for scalability in payment channel hubs. **IEEE S&P 2021** [Google Scholar](https://scholar.google.com/scholar?q=A^2L+Anonymous+atomic+locks+for+scalability+in+payment+channel+hubs)
> 核心思路：使用适配器签名实现无需脚本的原子交换。
> 局限与区别：后续工作 [26] 发现其安全性证明存在漏洞；本文首次在 UC 框架下提供完整证明，且不依赖适配器签名独家支持。

[26] Glaeser 等. Foundations of coin mixing services. **ACM CCS 2022** [Google Scholar](https://scholar.google.com/scholar?q=Foundations+of+coin+mixing+services)
> 核心思路：修复 A^2L 的安全问题，提出 A^2L+（仅理想模型安全）和 A^2L^UC（需 GP-2PC）。
> 局限与区别：A^2L^UC 因使用通用两方计算而效率极低；本文采用 cut-and-choose 技术避免了 GP-2PC，同时在 UC 框架下安全。

[15] Qin 等. BlindHub: Bitcoin-compatible privacy-preserving payment channel hubs supporting variable amounts. **ePrint 2022/1735** [Google Scholar](https://scholar.google.com/scholar?q=BlindHub+Bitcoin-compatible+privacy-preserving+payment+channel+hubs+supporting+variable+amounts)
> 核心思路：支持可变金额的隐私支付通道枢纽，使用适配器签名和通用零知识证明。
> 局限与区别：仅 BlindChannel 部分有 UC 证明，其余依赖 LOE 模型；本文不需要 GP-ZK，且支持唯一签名。

[10] Thyagarajan 等. Universal atomic swaps: Secure exchange of coins across all blockchains. **IEEE S&P 2022** [Google Scholar](https://scholar.google.com/scholar?q=Universal+atomic+swaps+Secure+exchange+of+coins+across+all+blockchains)
> 核心思路：提出仅需签名验证的最小脚本可支持任意区块链的原子交换。
> 局限与区别：效率在无适配器签名支持的区块链上很差（如 Monero）；本文通过 cut-and-choose 技术使唯一签名方案也能高效实现。

### 核心技术与方案

**整体框架**：Sweep-UC 采用电子现金范式（Chaum 1982 [31]）。用户 Alice 与中间方 sweeper W 交互，分为三个步骤：(1) 注册（Register）：Alice 选择一个随机 nonce sn，W 锁定自己的硬币，并发送一个 promise 消息（通过 redeem 协议生成）；(2) 添加支付（AddPayment）：Alice 通过匿名通道发起盲签名交互（BS 为 BLS 盲签名），嵌套在 exchange 协议中，以支付给 W 为条件获得盲签名 σ_BS；(3) 获取支付（GetPayment）：Alice 使用 σ_BS 从 promise 中赎回 W 的签名，从而获得 W 的硬币。交换的原子性和不可链接性通过 exchange 协议和 redeem 协议保证，盲签名的不可滥用性由 one-more unforgeability 保证。

**Exchange 协议**：用于左边（Alice 付给 W 以换取盲签名）。定义算法 Setup、Buy、Sell、Get。安全性分为恶意卖家安全（确保卖家无法在未收到买家签名前获得有用信息）和恶意买家安全（确保买家只有在卖家获得有效签名后才能学到盲签名）。文中给出基于 cut-and-choose 的实例化（如图 2 左侧），针对 BLS 签名方案。核心思想：卖家将盲签名响应 bsm2 和交易签名 σ_s 进行秘密共享，并使用 cut-and-choose 让买家验证部分共享的正确性，从而避免将随机预言机当电路使用。安全性依赖 BLS 的 EUF-CMA 安全性。

**Redeem 协议**：用于右边（Alice 用盲签名换取 W 的签名）。定义算法 Promise、VerPromise、Redeem。安全性分为恶意用户安全（模拟性与可提取性）和恶意服务安全（确保 promise 能正确兑换）。文中给出基于 cut-and-choose 的实例化（如图 2 右侧），同样针对 BLS 签名。核心思路：卖家将盲签名 σ_BS 的私钥 sk_BS 和另一个随机数 s_0 进行秘密共享，然后将每个共享分量 σ_j 加密为 ct_j，通过 cut-and-choose 使 Alice 验证 λ 个打开实例的一致性。最终，Alice 可以用完整的 σ_BS 重构所有 σ_j，从而恢复加密密钥并得到 σ_s。安全性依赖 BLS 的唯一性假设和 DDH 假设。

**安全证明策略**：在 UC 框架下，定义理想功能 F_ux，包含 Register、AddPayment、GetPayment 以及一个额外的 ChangePayment 接口（解决盲签名中接收公钥无法提取的问题）。Sweep-UC 的 UC 安全性通过基于 exchange 和 redeem 协议的游戏安全性的黑盒归约得到证明。模拟器在遇到恶意用户时，利用 blind signature 的模拟器构造 promise 和 exchange 消息，并在收到用户颁发的交易签名后通过 extractor 提取盲签名以恢复善意。关键假设：BS 的弱盲性、one-more 不可伪造性，以及 BLS 的 EUF-CMA、DDH。

**复杂度**：通信复杂度为 O(λ) 个群元素（约 64–78 KB，λ=128）；计算复杂度中，seller 侧算法（Setup、Promise）耗时 < 1 秒，buyer 侧验证 cut-and-choose（Buy、VerPromise）约 5 秒，而 Redeem 和 Get 在最坏情况下约 13–25 秒（并行后可优化）。总体而言，实际可行。

### 核心公式与流程

**Exchange 协议 (图 2 左侧，BLS cut-and-choose)**

Setup 算法：生成多项式 f, f'，计算共享盲签名 bsm2,j 和共享交易签名 σ_j，加密为 ct_j = H(σ_j) ⊕ bsm2,j，通过挑战 b_j 确定打开集合并返回 xm1。

Buy 算法：验证 λ 个打开实例的重合多项式承诺和签名，若通过则返回自己的签名 σ_b。

Get 算法：利用 σ_s 和 λ 个打开的 σ_j 重构未打开的 σ_?，验证配对并重构 bsm2。

**Redeem 协议 (图 2 右侧，BLS cut-and-choose)**

Promise 算法：生成 ct0 = h^{s0} · σ_s，以及各分量加密 ct_j = Ĥ(sn, σ_j) · h^{s_j}，附加零知识证明（用于 ct0 的良构性），通过 cut-and-choose 确定打开集合并返回 prom。

VerPromise 算法：验证打开实例的盲签名和多项式承诺，以及 ct0 的零知识证明。

Redeem 算法：使用完整 σ_BS 重构所有 σ_j，解密 ct_j 得到 h^{s_j}，再插值得到 h^{s0}，最终获得 σ_s = ct0 / h^{s0}。

**核心安全引理**

Lemma 1：若 BLS 签名 EUF-CMA 安全，则 EXC_BLS^cc 对恶意卖家安全。

Lemma 2：若 BLS 签名 EUF-CMA 安全，则 EXC_BLS^cc 对恶意买家安全。

Lemma 3：若 BS 是唯一盲签名，则 RP_BLS^cc 对恶意服务安全。

Lemma 4：若 BLS 签名 EUF-CMA 安全且 DDH 假设在 G1 中成立，则 RP_BLS^cc 对恶意用户安全。

### 实验结果

实验使用 MacbookPro Intel i7 @2.3 GHz 四核，16GB RAM，Python 实现（调用 Chia-Network BLS12-381 库），参数 λ=128，使用 16 个 worker 并行。结果来自表2，各算法平均执行时间（秒）：
EXC.Setup 0.82, EXC.Buy 5.3, EXC.Get（HC 诚实情况）0.35, EXC.Get（WC 恶意卖家最坏情况）13.5;
RP.Promise 0.53, RP.VerPromise 5.16, RP.Redeem（HC）0.21, RP.Redeem（WC）25.5。
实验表明 sweeper 侧算法 < 1 秒，用户侧验证 cut-and-choose 约 5 秒，最终化约 1 秒，证明方案实际可行。当前实现未优化，预计在更强大服务器上可进一步降低。

### 局限性与开放问题
目前 Sweep-UC 仅支持固定金额的交换，限制了匿名集大小；尚需考虑不当注册的拒绝服务攻击（可通过盲注册缓解但会增加复杂度）。将来可以探索支持不同面额的扩展，以及为其他后量子签名方案实例化 exchange 和 redeem 协议。此外，完整的端到端实现和链上评估有待完成。

### 强关联论文

[10] S. A. K. Thyagarajan, G. Malavolta, and P. Moreno-Sanchez. Universal atomic swaps: Secure exchange of coins across all blockchains. **IEEE S&P 2022** [Google Scholar](https://scholar.google.com/scholar?q=Universal+atomic+swaps+Secure+exchange+of+coins+across+all+blockchains)

[13] E. Heilman, L. Alshenibr, F. Baldimtsi, A. Scafuro, and S. Goldberg. TumbleBit: An untrusted bitcoin-compatible anonymous payment hub. **NDSS 2017** [Google Scholar](https://scholar.google.com/scholar?q=TumbleBit+An+untrusted+bitcoin-compatible+anonymous+payment+hub)

[14] E. Tairi, P. Moreno-Sanchez, and M. Maffei. A2L: Anonymous atomic locks for scalability in payment channel hubs. **IEEE S&P 2021** [Google Scholar](https://scholar.google.com/scholar?q=A2L+Anonymous+atomic+locks+for+scalability+in+payment+channel+hubs)

[15] X. Qin, S. Pan, A. Mirzaei, Z. Sui, O. Ersoy, A. Sakzad, M. F. Esgin, J. K. Liu, J. Yu, and T. H. Yuen. BlindHub: Bitcoin-compatible privacy-preserving payment channel hubs supporting variable amounts. **ePrint 2022/1735** [Google Scholar](https://scholar.google.com/scholar?q=BlindHub+Bitcoin-compatible+privacy-preserving+payment+channel+hubs+supporting+variable+amounts)

[26] N. Glaeser, M. Maffei, G. Malavolta, P. Moreno-Sanchez, E. Tairi, and S. A. K. Thyagarajan. Foundations of coin mixing services. **ACM CCS 2022** [Google Scholar](https://scholar.google.com/scholar?q=Foundations+of+coin+mixing+services)

[30] D. Boneh, B. Lynn, and H. Shacham. Short signatures from the Weil pairing. **ASIACRYPT 2001** [Google Scholar](https://scholar.google.com/scholar?q=Short+signatures+from+the+Weil+pairing)

[31] D. Chaum. Blind signatures for untraceable payments. **CRYPTO 1982** [Google Scholar](https://scholar.google.com/scholar?q=Blind+signatures+for+untraceable+payments)


## 关键词

+ 公平交换原子交换
+ 隐私保护跨链交换
+ UC安全框架
+ 链上隐私
+ 可替代性加密货币
+ 模块化子协议设计