---
title: "Sharp: Short relaxed range proofs"
doi: 10.1145/3548606.3560628
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2022
modified: 2025-04-15 16:44:32
created: 2025-04-11 11:49:07
---
## Sharp: Short relaxed range proofs

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/3548606.3560628)

## 作者

+ [Geoffroy Couteau](Geoffroy%20Couteau.md)
+ Dahmun Goudarzi 
+ Michael Klooß
+ [Michael Reichle](Michael%20Reichle.md)
## 笔记

### 背景与动机
零知识范围证明允许证明者向验证者证明一个秘密值落在公开区间内，而不泄露该值，它是匿名凭证、电子投票、匿名加密货币等众多应用的核心构件。现有范围证明主要分为两个范式：基于 $n$ 进制分解的方案 [13][14][32] 与基于平方分解的方案 [10][23][31][36]。其中，Bulletproofs [13] 是 $n$ 进制分解范式的代表，它实现了对数级的证明尺寸和透明的公共参考串，成为实际应用中最常用的方案。然而，Bulletproofs 的计算开销较大，特别是在需要批量证明时，其计算复杂度优势会变得不那么显著。平方分解范式利用 Lagrange 四平方定理将非负性证明转化为平方和证明，避免了 $n$ 进制分解。Couteau 等人 (Eurocrypt '21) [22] 提出的 CKLR 方案复兴了这一范式，通过构造有界整数承诺方案并基于离散对数群实例化，获得了比 Bulletproofs 更短的证明和更少的群运算。但 CKLR 的核心缺陷在于：它需要非标准的大群（例如 352 或 416 比特的椭圆曲线）来达到 128 位安全，这导致其实际计算效率远不如标准 256 位曲线上的 Bulletproofs；同时，CKLR 缺乏有效的批处理能力，且依赖于新引入的有界整数承诺方案，该方案的松弛打开性质限制了它在标准应用中的直接替换性。本文旨在填补 CKLR 在实际可用性上的空白，提出一个在通信、计算和灵活性上全面超越 Bulletproofs 和 CKLR 的优化范围证明家族 Sharp。

### 相关工作

[13] Benedikt Bünz, Jonathan Bootle, Dan Boneh, Andrew Poelstra, Pieter Wuille, and Greg Maxwell. Bulletproofs: Short Proofs for Confidential Transactions and More. **IEEE S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Bulletproofs+Short+Proofs+for+Confidential+Transactions+and+More)
> 核心思路：基于 $n$ 进制分解和内积论证，证明尺寸随范围比特数对数增长，支持高效的批处理。
> 局限与区别：计算开销高，尤其对证明者；本文 Sharp 方案在标准 256 位曲线上实现 10 倍以上的证明者加速。

[22] Geoffroy Couteau, Michael Klooß, Huang Lin, and Michael Reichle. Efficient Range Proofs with Transparent Setup from Bounded Integer Commitments. **EUROCRYPT 2021** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+Range+Proofs+with+Transparent+Setup+from+Bounded+Integer+Commitments)
> 核心思路：引入有界整数承诺，将平方分解范式实例化于 DLOG 群，证明尺寸优于 Bulletproofs。
> 局限与区别：需非标准大群、缺乏批处理、承诺具松弛性；本文 Sharp 通过群切换、批短测试 (RAST) 和多项式分解证明克服这些局限。

[23] Geoffroy Couteau, Thomas Peters, and David Pointcheval. Removing the Strong RSA Assumption from Arguments over the Integers. **EUROCRYPT 2017** [Google Scholar](https://scholar.google.com/scholar?q=Removing+the+Strong+RSA+Assumption+from+Arguments+over+the+Integers)
> 核心思路：在隐藏阶群中实现平方分解范围证明，不依赖强 RSA 假设。
> 局限与区别：使用大 RSA 群（约 2048 位），通信和计算开销大；本文 Sharp_RSA 仅添加一个隐藏阶群元素，实现 77% 的尺寸缩减。

[25] Ivan Damgård and Eiichiro Fujisaki. A Statistically-Hiding Integer Commitment Scheme Based on Groups with Hidden Order. **ASIACRYPT 2002** [Google Scholar](https://scholar.google.com/scholar?q=A+Statistically-Hiding+Integer+Commitment+Scheme+Based+on+Groups+with+Hidden+Order)
> 核心思路：提出 Damgård-Fujisaki 整数承诺方案，在隐藏阶群中支持整数承诺和平方分解。
> 局限与区别：隐藏阶群效率低；本文用隐藏阶群仅增强松弛性质，不主导证明。

[10] Fabrice Boudot. Efficient Proofs that a Committed Number Lies in an Interval. **EUROCRYPT 2000** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+Proofs+that+a+Committed+Number+Lies+in+an+Interval)
> 核心思路：最早基于平方分解的范围证明之一，使用隐藏阶群。
> 局限与区别：通信和计算复杂度高；本文 Sharp 在 DLOG 群中的优化使其更实用。

[14] Jan Camenisch, Rafik Chaabouni, and abhi shelat. Efficient Protocols for Set Membership and Range Proofs. **ASIACRYPT 2008** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+Protocols+for+Set+Membership+and+Range+Proofs)
> 核心思路：基于 $n$ 进制分解和签名的高效范围证明。
> 局限与区别：依赖配对群，计算较慢；本文 Sharp 在椭圆曲线群上更高效。

[31] Jens Groth. Non-interactive Zero-Knowledge Arguments for Voting. **ASIACRYPT 2005** [Google Scholar](https://scholar.google.com/scholar?q=Non-interactive+Zero-Knowledge+Arguments+for+Voting)
> 核心思路：在隐藏阶群中实现非交互范围证明用于投票。
> 局限与区别：证明尺寸大；本文 Sharp_RSA 尺寸缩减 77%。

[34] Max Hoffmann, Michael Klooß, Markus Raiber, and Andy Rupp. Black-Box Wallets: Fast Anonymous Two-Way Payments for Constrained Devices. **PoPETs 2020** [Google Scholar](https://scholar.google.com/scholar?q=Black-Box+Wallets+Fast+Anonymous+Two-Way+Payments+for+Constrained+Devices)
> 核心思路：在隐私支付中利用范围证明保证余额非负，使用 CKLR 型方案。
> 局限与区别：CKLR 效率低；Sharp 可作为更高效的 drop-in 替换。

[12] Benedikt Bünz, Shashank Agrawal, Mahdi Zamani, and Dan Boneh. Zether: Towards Privacy in a Smart Contract World. **FC 2020** [Google Scholar](https://scholar.google.com/scholar?q=Zether+Towards+Privacy+in+a+Smart+Contract+World)
> 核心思路：在智能合约上实现匿名支付，使用 Bulletproofs 作为范围证明。
> 局限与区别：Bulletproofs 计算开销大；Sharp 提供 10 倍以上加速。

### 核心技术与方案

Sharp 方案的核心思想是将 CKLR 的松弛性从承诺重新解释为范围证明的松弛性：它证明 Pedersen 承诺中的值是一个落在区间内的有理数（而非整数），从而使用标准的 Pedersen 承诺，便于集成。在此基础上，Sharp 通过三个核心技术实现全面优化：多项式基分解证明 (PoDec)、批短测试 (RAST) 和隐藏阶群增强。

**1. 多项式基分解证明 (PoDec) 与群切换**
Sharp 将范围证明分解为短开证明 (PoSO) 和分解证明 (PoDec) 两个独立模块。PoDec 证明存在四个短整数满足平方分解方程。为证明等式 $x(B-x) \equiv_p \sum_{j=1}^4 y_j^2$ 在 $\mathbb{Z}_p$ 上成立，Sharp 利用多项式技术：从 PoSO 中得到掩码后的响应 $z = \gamma x + \tilde{x}$ 和 $z_j = \gamma y_j + \tilde{y}_j$，计算多项式
$$ f = z(\gamma B - z) - \sum_{j=1}^4 z_j^2 = \alpha_1 \gamma + \alpha_0. $$
若分解成立，则 $f$ 是 $\gamma$ 的一次多项式（二次项系数 $\alpha_2=0$）。证明者承诺系数 $\alpha_1, \alpha_0$，挑战 $\gamma$ 后，验证者通过检查 $f \equiv_q \alpha_1 \gamma + \alpha_0$ 来保证分解正确性。这一多项式技术允许使用 Pedersen 多承诺 (MPed) 实现一个证明证明多个值的分解，将 CKLR 中每个值所需的单独承诺合并，从而节省通信。更重要的是，PoSO 和 PoDec 所需的群大小不同：PoSO 仅需 $p \ge 2 (B\Gamma^2+1)L$ 来保证有理数表示的唯一性，而 PoDec 要求 $q \ge 18K^2$（$K = (B\Gamma+1)L$）来确保平方分解方程在整数上成立。Sharp 的模块化设计允许对 PoSO 和 PoDec 使用不同大小的群，即群切换，从而避免 CKLR 中单一群尺寸的妥协——例如 PoSO 可用 256 位群，PoDec 用稍大的群。

**2. 批短测试 (RAST) 与优化 PoSO**
Sharp 的核心技术贡献在于构造一个批量的“分数短测试”。在 CKLR 中，每个短开证明 (PoSO) 需要单独执行，且需多次重复以达到所需安全参数，导致通信开销大。Sharp 观察到，一个随机线性组合的测试可以批量检查多个 $x_i$ 是否共享一个短分母 $d$。具体地，证明者计算 $\zeta_k = \sum_{i,j} \gamma_{i,j}^{(k)} y_{i,j} + \mu_k$（其中 $\mu_k$ 是掩码），并发送 $\zeta_k$。RAST 测试的核心定理（定理 3.3）保证：如果不存在一个 $d \in [1,\Gamma]$ 使得对所有 $x_i$ 都有 $d \cdot x_i \in [-K', K']_{\mathbb{Z}_p}$，则测试接受的概率最多为 $8/(\Gamma+1)$。因此，使用 $\Gamma$ 比特的挑战空间，只需 $R = \lceil \lambda / \log(\Gamma+1) \rceil$ 次重复即可达到 $\lambda$ 位安全，且每次重复仅需发送两个短整数（$\zeta_k$ 和掩码响应 $\tau_k$），而 CKLR 每次重复需发送大量群元素和标量。这一优化使得 Sharp 在标准 256 位曲线（如 secp256k1）上即可高效运行，无需使用非标准大群。

**3. 隐藏阶群增强与完全安全性**
针对松弛可靠性（仅保证有理数在区间内）在部分应用（如匿名交易）中的不足，Sharp 提出使用一个隐藏阶群元素来增强安全性。具体地，在 DLOG 群承诺 $C_x$ 之外，额外在隐藏阶群 H 中添加一个承诺 $C'_x$，并证明其打开与 $C_x$ 一致。通过利用隐藏阶群的“2-fROOT”或“1-fROOT”假设，可以强制分母为特定形式：在类群中分母为 2 的幂，从而将有理数限制为二进有理数；在 RSA 群中分母必须为 1，即整数，从而获得完全可靠性。该增强仅增加一个群元素和少量标量，因为挑战和响应可以通过综合计算（$\gamma' = \sum \gamma_k (\Gamma+1)^{k-1}$）避免额外重复，因此开销极小，却实现了从松弛到完全的跨越。

**安全性总结**：
- **承诺绑定**：基于 DLOG 假设。
- **承诺隐藏**：基于 SEI/子群不可区分性假设，参数 $S = 2^{2\lambda}$。
- **游荡可靠性**：SharpGS 和 SharpSO 提供松弛可靠性，知识误差为 $(2/(\Gamma+1))^R$ 和 $(2+8^R)/(\Gamma+1)^R$，提取关系为 $[x_i]_\mathbb{Q} \in [0, B]_\mathbb{Q}$。
- **非中断 SHVZK**：基于 SEI 假设和拒绝采样掩码，模拟器通过将掩码中的真实值替换为 0 来生成不可区分副本。

**渐进复杂度**：
- **通信**：SharpGS 证明大小为 $O((R + N) \log p)$ 比特，其中 $R$ 是重复次数，$N$ 是批量大小。与 CKLR 相比，群元素数量减少约 50%。SharpSO 进一步优化为 $O(R + N)$ 短整数 + $O(N)$ 群元素，通信量几乎与 $N$ 线性增长。
- **计算**：证明者主导为 $O(N \cdot \text{multiexp} + R \cdot \text{scalar\_op})$，验证者主导为 $O(N \cdot \text{multiexp} + R \cdot \text{scalar\_op})$。与 Bulletproofs 的 $O(\log B)$ 次多指数运算相比，Sharp 在 $N$ 较大时优势更明显，且多指数大小固定（约 4-5 个基）。

### 核心公式与流程

**[Lagrange 四平方分解]**
$$4x(B-x) + 1 = \sum_{j=1}^{3} y_{i,j}^2$$
> 作用：将非负性条件 $x \in [0, B]$ 的证明转化为存在三个短整数 $y_j$ 满足平方和等式，这是 Sharp 平方分解范式的基础。

**[RAST 批短测试定理 (定理 3.3 简化)]**
给定向量 $\vec{x} \in \mathbb{Z}_p^N$，若不存在单个 $d \in [1, D]$ 使得 $d \vec{x} \in [-K', K']_{\mathbb{Z}_p}^N$，则随机线性测试 $\mu + \sum \gamma_i x_i \in [0, K]_{\mathbb{Z}_p}$ 接受的概率不超过 $8/(D+1)$。
> 作用：保证批量短测试的安全性，即若各 $x_i$ 不共享一个小分母，则测试几乎必然拒绝，这是 SharpSO 减少重复次数的核心。

**[SharpGS 多项式分解验证方程]**
$$D_{k,*} + \gamma_k C_{k,*} = t_k^* H_0 + \sum_{i=1}^N f_{k,i}^* H_i$$
其中 $f_{k,i}^* = 4z_{k,i}(\gamma_k B - z_{k,i}) + \gamma_k^2 - \sum_{j=1}^3 z_{k,i,j}^2$
> 作用：证明分解多项式 $f$ 是 $\gamma$ 的一次多项式，从而保证平方分解方程在 $\mathbb{Z}_q$ 上成立。

**[SharpSO 最终验证方程]**
$F_x = D_x$, $F_y = D_y$, $F_* = D_*$, 且 $f_k = d_k$ for $k \in [1,R]$
其中 $F_x = -\gamma C_x + t_x G_0 + \sum z_i G_i$
> 作用：综合验证短开证明的线性关系、PoSO 响应与分解的正确性，构成五轮协议中 Phase 2 的最终验证。

### 实验结果

**实验设置**：在配备 2.3 GHz Intel Core i7 处理器的 MacBook Pro 上运行，使用 libsecp256k1 [43] 库（256 位椭圆曲线）。SharpSO 为单线程非优化实现，Bulletproofs 为使用同一库的优化参考实现 [13]。

**核心性能数值**（来自表 2）：
- **单证明 ($N=1$, $\lambda=128$, $\log B=64$)**：证明者时间：SharpSO 1.17 ms vs Bulletproofs 20.6 ms（**$11.6\times$ 加速**）；验证者时间：SharpSO 0.75 ms vs Bulletproofs 2.55 ms（**$3.4\times$ 加速**）。
- **批量证明 ($N=8$, $\lambda=128$, $\log B=64$)**：证明者时间：SharpSO 7.47 ms vs Bulletproofs 157 ms（**$21\times$ 加速**）；验证者时间：SharpSO 3.88 ms vs Bulletproofs 12.1 ms（**$3.1\times$ 加速**）。
- **32 位范围 ($\lambda=128$, $\log B=32$)**：单证明加速 $10.8\times$ (证明者) 和 $2.0\times$ (验证者)；批量证明加速 $11.9\times$ (证明者) 和 $2.0\times$ (验证者)。

**对比基线**：
- **与 CKLR 对比**：SharpGS 证明尺寸缩减约 34% ($N=1$) 至 75% ($N=8$)；SharpSO 缩减约 29% 至 74%。且在标准 256 位群上即可运行，避免 CKLR 对非标准大群的需求。
- **与 RSA 方案 [23] 对比**：SharpRSA 证明尺寸缩减 77% ($N=1$) 至 92% ($N=8$)。
- **与 Bulletproofs 对比**：通信上，SharpGS 单证明比 Bulletproofs 短 42-50%；批量 $N=8$ 时仅大 1.1-1.3 倍，但计算加速 10-20 倍。

**适用规模**：Sharp 在 32-64 位范围、单证明或中小批量 ($N \le 16$) 时性能最优。对超高批量 (如 $N>100$)，Bulletproofs 的对数通信可能更优，但 Sharp 的计算加速仍具吸引力。

### 局限性与开放问题
Sharp 的主要局限在于其松弛可靠性在部分应用（如匿名交易）中不能作为直接替换使用，而需要借助隐藏阶群增强或预先保证值足够短。此外，RAST 测试的安全性分析（定理 3.3）依赖于一个非平凡的论据，其紧致性可能不是最优的，探索更紧的界或更简单的证明是开放问题。最后，Sharp 尚未在配对群或后量子环境下进行系统优化，将其迁移到这些设置中并评估其性能是未来有价值的方向。

### 强关联论文

[22] Geoffroy Couteau, Michael Klooß, Huang Lin, and Michael Reichle. Efficient Range Proofs with Transparent Setup from Bounded Integer Commitments. **EUROCRYPT 2021** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+Range+Proofs+with+Transparent+Setup+from+Bounded+Integer+Commitments)

[13] Benedikt Bünz, Jonathan Bootle, Dan Boneh, Andrew Poelstra, Pieter Wuille, and Greg Maxwell. Bulletproofs: Short Proofs for Confidential Transactions and More. **IEEE S&P 2018** [Google Scholar](https://scholar.google.com/scholar?q=Bulletproofs+Short+Proofs+for+Confidential+Transactions+and+More)

[23] Geoffroy Couteau, Thomas Peters, and David Pointcheval. Removing the Strong RSA Assumption from Arguments over the Integers. **EUROCRYPT 2017** [Google Scholar](https://scholar.google.com/scholar?q=Removing+the+Strong+RSA+Assumption+from+Arguments+over+the+Integers)

[10] Fabrice Boudot. Efficient Proofs that a Committed Number Lies in an Interval. **EUROCRYPT 2000** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+Proofs+that+a+Committed+Number+Lies+in+an+Interval)

[14] Jan Camenisch, Rafik Chaabouni, and abhi shelat. Efficient Protocols for Set Membership and Range Proofs. **ASIACRYPT 2008** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+Protocols+for+Set+Membership+and+Range+Proofs)

[31] Jens Groth. Non-interactive Zero-Knowledge Arguments for Voting. **ASIACRYPT 2005** [Google Scholar](https://scholar.google.com/scholar?q=Non-interactive+Zero-Knowledge+Arguments+for+Voting)

[25] Ivan Damgård and Eiichiro Fujisaki. A Statistically-Hiding Integer Commitment Scheme Based on Groups with Hidden Order. **ASIACRYPT 2002** [Google Scholar](https://scholar.google.com/scholar?q=A+Statistically-Hiding+Integer+Commitment+Scheme+Based+on+Groups+with+Hidden+Order)

[40] Torben P. Pedersen. Non-Interactive and Information-Theoretic Secure Verifiable Secret Sharing. **CRYPTO 1992** [Google Scholar](https://scholar.google.com/scholar?q=Non-Interactive+and+Information-Theoretic+Secure+Verifiable+Secret+Sharing)


## 关键词

+ 范围证明
+ 零知识证明
+ 离散对数
+ 群论
+ 密码学