---
title: "Anonymous credentials light"
doi: 10.1145/2508859.2516687
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2013
created: 2025-05-09 11:02:29
modified: 2025-05-09 11:03:47
---
## Anonymous credentials light

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/2508859.2516687)

## 作者

+ [Foteini Baldimtsi](Foteini%20Baldimtsi.md)
+ [Anna Lysyanskaya](Anna%20Lysyanskaya.md)

## 笔记

### 背景与动机
匿名凭证是隐私保护身份管理的核心构件，允许用户在不泄露额外信息的前提下证明持有凭证。Chaum 最早提出这一概念 [17]，Camenisch 和 Lysyanskaya 给出了首个完整实现 [13]。然而，现有所有可证明安全的匿名凭证系统均依赖 RSA 群或双线性配对群，安全参数选择导致在移动设备、智能卡和 RFID 上效率过低——例如 CL 凭证在 Java 卡上执行一次凭证展示需超过 16 秒 [6]。相比之下，Brands 提出的 UProve 系统 [8, 9] 基于离散对数困难群（可选椭圆曲线），仅需少量指数运算，但其凭证不支持不可链接的重用，且一直缺乏可证明安全性；Baldimtsi 和 Lysyanskaya 后续甚至证明了其底层的 Brands 盲签名方案在随机预言机模型下无法被证明安全 [4]。因此，如何构造一个既能支持属性、又能在椭圆曲线群上高效实现且具备可证明安全性的匿名凭证系统，成为亟待解决的开放问题。

### 相关工作

[1] Abe. A secure three-move blind signature scheme for polynomially many signatures. **EUROCRYPT 2001** [Google Scholar](https://scholar.google.com/scholar?q=A+secure+three-move+blind+signature+scheme+for+polynomially+many+signatures)
> 核心思路：提出一个三轮盲签名方案，通过 OR-proof 技术实现签名者的不可区分性。
> 局限与区别：原始方案仅支持无属性消息的盲签名，且其安全证明后被修正为仅适用于成功概率压倒性高的敌手，后续仅给出通用群模型证明；本文在其基础上引入属性承诺并修改 z₁ 的构造，使签名能编码用户属性。

[8] Brands. Untraceable off-line cash in wallets with observers. **CRYPTO 1993** [Google Scholar](https://scholar.google.com/scholar?q=Untraceable+off-line+cash+in+wallets+with+observers)
> 核心思路：提出基于离散对数假设的盲签名，并用于构建可链接的匿名凭证（UProve 的前身）。
> 局限与区别：该方案缺乏可证明安全性，且凭证不可匿名重用；本文在保持类似效率的同时给出了可证明安全构造。

[13] Camenisch and Lysyanskaya. An efficient system for non-transferable anonymous credentials with optional anonymity revocation. **EUROCRYPT 2001** [Google Scholar](https://scholar.google.com/scholar?q=An+efficient+system+for+non-transferable+anonymous+credentials+with+optional+anonymity+revocation)
> 核心思路：基于 RSA 假设给出了第一个完整的匿名凭证系统，支持多次匿名使用。
> 局限与区别：需要 RSA 群或双线性配对，在轻量设备上性能不足；本文基于 DDH 假设大大降低了计算开销。

[4] Baldimtsi and Lysyanskaya. On the security of one-witness blind signature schemes. **ePrint 2012** [Google Scholar](https://scholar.google.com/scholar?q=On+the+security+of+one-witness+blind+signature+schemes)
> 核心思路：证明所有已知方法均无法在随机预言机模型下证明 Brands 型盲签名方案的安全性。
> 局限与区别：该负面结果直接促使本文需要设计新的可证明安全的盲签名属性方案，而非修补 Brands 方案。

[33] Ohkubo and Abe. Security of three-move blind signature schemes reconsidered. **SCIS 2003** [Google Scholar](https://scholar.google.com/scholar?q=Security+of+three-move+blind+signature+schemes+reconsidered)
> 核心思路：指出 Abe 原始盲签名方案安全证明中的缺陷，并证明其在并发组合下仅对成功概率压倒性高的敌手成立。
> 局限与区别：本文仅考虑顺序组合，并成功给出了 DDH 假设下的证明，同时保留了 Abe 方案的基本结构。

[6] Bichsel et al. Anonymous credentials on a standard java card. **CCS 2009** [Google Scholar](https://scholar.google.com/scholar?q=Anonymous+credentials+on+a+standard+java+card)
> 核心思路：在 Java 卡上实现了 CL 凭证，利用 RSA 硬件加速器。
> 局限与区别：展示一个凭证仍需超过 16 秒，不适用于多数应用；本文在椭圆曲线上仅需数百毫秒。

[35] Paquin. U-prove cryptographic specification v1.1. **Microsoft Technical Report 2011** [Google Scholar](https://scholar.google.com/scholar?q=U-prove+cryptographic+specification+v1.1)
> 核心思路：提供 Brands 方案的具体规范（UProve），强调椭圆曲线群上的高效性。
> 局限与区别：缺乏安全证明，且凭证不可匿名重用；本文提供可证明安全的替代方案。

### 核心技术与方案

本文首先形式化定义了“带属性的盲签名”（Blind Signatures with Attributes），作为构造可链接匿名凭证的模块。该定义要求：用户和签名者共同输入对用户属性的承诺 C；协议输出一个新的、不可链接的承诺 $\tilde{C}$ 以及对 $(m, \tilde{C})$ 的签名，其中 m 是用户选择的消息。盲性保证签名者无法将签名与执行实例链接；不可伪造性保证用户无法产生比所执行协议次数更多的签名，且输入承诺的多重集与输出承诺的多重集必须匹配。

基于该定义，构造的具体方案 ACL 由三条子协议组成：注册、准备和验证。注册阶段仅需执行一次，用户向签名者证明他知道承诺 C 的开（由零知识证明 $\pi_1$ 实现）。准备阶段：签名者选择随机数 rnd，构造一次性标签公钥 $z_1 = C g^{\text{rnd}}$、$z_2 = z / z_1$（z 是系统公钥）；用户验证 rnd 后，随机选择 $\gamma\in\mathbb{Z}_q^*$ 盲化得到 $\zeta = z^\gamma$、$\zeta_1 = z_1^\gamma$、$\zeta_2 = \zeta / \zeta_1$，并选择 $\tau$ 计算 $\eta = z^\tau$。验证阶段执行 OR-proof：签名者使用 y 侧（真实密钥 x）和一个模拟的 z 侧（使用随机 $c', r'$）生成 $a = g^u$ 和 $a'$；用户将其盲化为 $\alpha$ 和 $\alpha'$，计算挑战 $\varepsilon = \mathcal{H}(\zeta, \zeta_1, \alpha, \alpha', \eta, m)$ 并发送 $e = (\varepsilon - t_2 - t_4) \bmod q$；签名者计算 $c = e - c'$、$r = u - c x$，返回 $(c, r, c', r')$；用户解盲得到完整签名 $\sigma = (m, \zeta, \zeta_1, \rho, \omega, \rho'_1, \rho'_2, \omega', \mu)$，其中 $\zeta_1$ 即为输出的盲化承诺 $\tilde{C}$。

验证算法：检查 $\zeta \neq 1$ 且满足
$$\omega + \omega' = \mathcal{H}(\zeta, \zeta_1, g^\rho y^\omega, g^{\rho'_1} \zeta_1^{\omega'}, h^{\rho'_2} \zeta_2^{\omega'}, z^\mu \zeta^{\omega'}, m) \bmod q.$$

安全性方面，定理 3 证明盲性成立：通过混合论证将真实游戏与混合游戏（一个正确签名+一个伪造签名）和伪造游戏（两个伪造签名）进行等价，利用 DDH 假设证明相邻游戏不可区分。定理 4 证明顺序组合下的 $( \ell, \ell+1 )$-不可伪造性：先证引理 1（协议是证人不可区分的，因此可用 z 侧模拟器替换 y 侧），引理 2（限制性盲化引理，保证 $\log_z \zeta = \log_{z_1} \zeta_1$ 以不可忽略概率成立），引理 3（不与签名者交互无法生成有效签名）；然后通过重放攻击和分叉引理，从 $ \ell+1$ 个签名中提取出离散对数。安全性依赖离散对数假设和随机预言机模型，但非紧致归约——损失因子 $\binom{q_h}{2} \approx q_h^2$，因此推荐 576 位椭圆曲线群以对抗 $2^{80}$ 次哈希查询，对应的 128 位安全。

### 核心公式与流程

**盲化 Pedersen 承诺**
$$ \text{Commit}^B(L_1,\dots,L_n; R, \gamma) = (z^\gamma,\; \text{Commit}(L_1,\dots,L_n;R)^\gamma) $$
> 作用：在 ACL 中 $\tilde{C} = (\zeta, \zeta_1)$ 实际上是用户属性的盲化 Pedersen 承诺，其中 $\zeta = z^\gamma$，$\zeta_1 = z_1^\gamma = (C g^{\text{rnd}})^\gamma$，保证了在签名中编码属性。

**OR-proof 中用户盲化步骤**
$$ \alpha = a g^{t_1} y^{t_2}, \quad \alpha'_1 = (a'_1)^\gamma g^{t_3} \zeta_1^{t_4}, \quad \alpha'_2 = (a'_2)^\gamma h^{t_5} \zeta_2^{t_4} $$
$$ e = \mathcal{H}(\zeta,\zeta_1,\alpha,\alpha',\eta,m) - t_2 - t_4 $$
> 作用：用户对签名者发送的 $\Sigma_y$ 和 $\Sigma_z$ 第一消息进行盲化，并用盲化因子隐藏挑战，使签名者看到的 $e$ 不泄露真实哈希值。

**签名解盲**
$$ \rho = r + t_1,\; \omega = c + t_2,\; \rho'_1 = \gamma r'_1 + t_3,\; \rho'_2 = \gamma r'_2 + t_5,\; \omega' = c' + t_4,\; \mu = \tau - \omega'\gamma $$
> 作用：用户将签名者返回的应答解盲，得到完整的签名元组 $\sigma = (m, \zeta, \zeta_1, \rho, \omega, \rho'_1, \rho'_2, \omega', \mu)$。

**验证方程**
$$ \omega + \omega' = \mathcal{H}(\zeta,\zeta_1,\; g^\rho y^\omega,\; g^{\rho'_1} \zeta_1^{\omega'},\; h^{\rho'_2} \zeta_2^{\omega'},\; z^\mu \zeta^{\omega'},\; m) $$
> 作用：验证者通过重算哈希确认签名的 OR-proof 结构完整性。

### 实验结果

论文未报告自主实验数据，但引用了同组作者在独立工作 [28] 中基于 ACL 的 NFC 智能手机实现：使用 BlackBerry Bold 9900（NFC 功能）及 160 位椭圆曲线群（作为概念验证）。签名/凭证发行总时间（包括终端、通信与智能手机执行）约为 300 毫秒；花费/验证时间（即签名验证）约为 380 毫秒，其中需揭示 2 个属性；若无属性揭示则耗时更少。这些数字是在非优化参数（160 位群，对应约 80 位安全等级）下测得的，但充分说明了 ACL 在轻量设备上的实用性。与 CL 凭证在 Java 卡上 16 秒以上的展示时间 [6] 相比，ACL 展现了压倒性优势。

### 局限性与开放问题

本文安全证明仅适用于顺序组合的不可伪造性，将扩展至并发自组合留作开放问题。证明是非紧致的，损失因子约 $q_h^2$，导致推荐群位宽较大（576 位椭圆曲线对应 128 位安全），若采用更紧致归约可进一步降低开销。另外，本文仅实现了“可链接”的匿名凭证（单次使用），而非完全不可链接的多用凭证；若要支持多次匿名使用，需用户每次重新执行发行协议，可能引入额外的通信开销。

### 强关联论文

[1] M. Abe. A secure three-move blind signature scheme for polynomially many signatures. **EUROCRYPT 2001** [Google Scholar](https://scholar.google.com/scholar?q=A+secure+three-move+blind+signature+scheme+for+polynomially+many+signatures)

[4] F. Baldimtsi and A. Lysyanskaya. On the security of one-witness blind signature schemes. **ePrint 2012** [Google Scholar](https://scholar.google.com/scholar?q=On+the+security+of+one-witness+blind+signature+schemes)

[6] P. Bichsel, J. Camenisch, T. Groß, and V. Shoup. Anonymous credentials on a standard java card. **CCS 2009** [Google Scholar](https://scholar.google.com/scholar?q=Anonymous+credentials+on+a+standard+java+card)

[8] S. Brands. Untraceable off-line cash in wallets with observers. **CRYPTO 1993** [Google Scholar](https://scholar.google.com/scholar?q=Untraceable+off-line+cash+in+wallets+with+observers)

[13] J. Camenisch and A. Lysyanskaya. An efficient system for non-transferable anonymous credentials with optional anonymity revocation. **EUROCRYPT 2001** [Google Scholar](https://scholar.google.com/scholar?q=An+efficient+system+for+non-transferable+anonymous+credentials+with+optional+anonymity+revocation)

[17] D. Chaum. Blind signatures for untraceable payment. **CRYPTO 1982** [Google Scholar](https://scholar.google.com/scholar?q=Blind+signatures+for+untraceable+payment)

[33] M. Ohkubo and M. Abe. Security of three-move blind signature schemes reconsidered. **SCIS 2003** [Google Scholar](https://scholar.google.com/scholar?q=Security+of+three-move+blind+signature+schemes+reconsidered)

[35] C. Paquin. U-prove cryptographic specification v1.1. **Microsoft Technical Report 2011** [Google Scholar](https://scholar.google.com/scholar?q=U-prove+cryptographic+specification+v1.1)


## 关键词

+ 匿名凭证
+ 盲签名
+ 椭圆曲线
+ DDH假设
+ 隐私保护