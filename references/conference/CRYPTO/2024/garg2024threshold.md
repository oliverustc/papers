---
title: "Threshold encryption with silent setup"
doi: 10.1007/978-3-031-68394-7_12

标题简称:
论文类型: conference
会议简称: CRYPTO
发表年份: 2024
created: 2025-04-17 10:50:10
modified: 2025-04-29 16:32:17
---
## Threshold encryption with silent setup

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-031-68394-7_12)
+ [code](https://github.com/tangle-network/silent-threshold-encryption-gadget)

## 作者

+ [Sanjam Garg](Sanjam%20Garg.md) 
+ [Dimitris Kolonelos](Dimitris%20Kolonelos.md)
+ [Guru-Vamsi Policharla](Guru-Vamsi%20Policharla.md)
+ [Mingyuan Wang](Mingyuan%20Wang.md) 

## 笔记

### 背景与动机
阈值加密允许加密方生成一个简洁的密文，使得任意 $t$ 个参与方可以解密，而任何少于 $t$ 方的合谋无法获得消息。然而，几乎所有现有方案都依赖于一个昂贵的交互式分布式密钥生成（DKG）协议来建立共享密钥 [44,73]，这导致了高昂的通信与计算开销。此外，传统 DKG 假设同步网络，而异步 DKG 不仅成本更高，且最多只能容忍 $< 1/3$ 的恶意节点 [2,21,22,55,56]。DKG 的交互性质还使得系统难以支持多元宇宙（multiverse）——即一次设置后，无需额外交互即可为不同的委员会集合生成加密密钥——以及动态阈值（dynamic threshold）——即加密方可以为每个密文自由选择不同的阈值。尽管存在一些尝试实现后两种属性的工作，但它们要么需要一个可信的私钥生成器 [27,50]，要么密文大小与委员会规模线性相关 [24,25]。唯一一个具有常数大小密文的方案 [67] 依赖于不可区分混淆（indistinguishability Obfuscation，iO）或针对所有 NP 语言的见证加密（witness encryption） [40]。本文填补的空白是：构建第一个实用的、基于配对群的且无需交互式设置的阈值加密方案，同时保持常数大小的密文和非交互式解密。

### 相关工作

[13] Boneh 等. Short signatures from the Weil pairing. **ASIACRYPT 2001** [Google Scholar](https://scholar.google.com/scholar?q=Short+signatures+from+the+Weil+pairing)
> 核心思路：BLS 签名方案，其验证方程为线性等式 $e(g, \sigma) = e(pk, H(\text{msg}))$，这是本文构建签名基础见证加密的基础。
> 局限与区别：BLS 签名本身不具有阈值性，也不支持静默设置。

[43] Garg 等. Hints: threshold signatures with silent setup. **IEEE S&P 2024** [Google Scholar](https://scholar.google.com/scholar?q=Hints%3A+threshold+signatures+with+silent+setup)
> 核心思路：提出了 hinTS，一种静默设置的阈值签名方案，其中每个参与方独立生成 BLS 密钥对并通过发布“提示”来支持后续的签名聚合。
> 局限与区别：hinTS 的验证方程包含一个非线性的阶数检查（用于证明 $B$ 是二进制向量），无法直接用于构建线性可验证的见证加密。本文通过引入度检查（degree-check）替代该非线性验证，构建了一个完全线性可验证的静默阈值签名。

[13] 和 [43] 在参考文献中编号不同，但这里[43]是本文核心参考的静默阈值签名方案。

[53] Kate 等. Constant-size commitments to polynomials and their applications. **ASIACRYPT 2010** [Google Scholar](https://scholar.google.com/scholar?q=Constant-size+commitments+to+polynomials+and+their+applications)
> 核心思路：KZG 多项式承诺方案，用于高效地承诺向量（多项式）并提供常数大小的证明。
> 局限与区别：KZG 承诺本身不提供加密功能。本文利用 KZG 承诺作为向量承诺，来构建聚合签名及其证明。

[12] Boneh 等. Identity-based encryption from the Weil pairing. **CRYPTO 2001** [Google Scholar](https://scholar.google.com/scholar?q=Identity-based+encryption+from+the+Weil+pairing)
> 核心思路：Boneh-Franklin IBE 方案，其加密方式可以看作一种特殊的签名基础见证加密，给定一个身份对应的签名（即私钥）即可解密。
> 局限与区别：IBE 需要一个全局的私钥生成器来分发密钥，而本文的方案是完全分布式的，不需要任何可信中心。

[24] Daza 等. CCA2-secure threshold broadcast encryption with shorter ciphertexts. **ProvSec 2007** [Google Scholar](https://scholar.google.com/scholar?q=CCA2-secure+threshold+broadcast+encryption+with+shorter+ciphertexts)
> 核心思路：提出了一种门限广播加密方案，但其密文长度与接收者集合的大小线性相关。
> 局限与区别：本文方案实现了常数大小的密文，不随委员会规模增长。

[27] Delerablée 等. Dynamic threshold public-key encryption. **CRYPTO 2008** [Google Scholar](https://scholar.google.com/scholar?q=Dynamic+threshold+public-key+encryption)
> 核心思路：提出了动态阈值公钥加密，允许加密时自由选择阈值。
> 局限与区别：该方案依赖于一个可信的私钥生成器（Private Key Generator）来分发密钥，而本文的静默设置完全消除了对任何可信第三方的依赖。

[57] Kolonelos 等. Distributed broadcast encryption from bilinear groups. **ePrint 2023** [Google Scholar](https://scholar.google.com/scholar?q=Distributed+broadcast+encryption+from+bilinear+groups)
> 核心思路：基于配对群构建了分布式广播加密（DBE）方案，即静默设置的广播加密（$t=1$ 的特例）。
> 局限与区别：本文的方案是更一般化的门限方案（任意 $t$），并且通过相同的技术框架支持灵活广播加密（FBE）等扩展。

[37] Freitag 等. How to use (plain) witness encryption: registered ABE, flexible broadcast, and more. **CRYPTO 2023** [Google Scholar](https://scholar.google.com/scholar?q=How+to+use+(plain)+witness+encryption%3A+registered+ABE%2C+flexible+broadcast%2C+and+more)
> 核心思路：引入了灵活广播加密（FBE）概念，并从通用见证加密构建。
> 局限与区别：该方案不提供具体的高效实例化。本文首次从配对群给出了 FBE 的一个具体、高效的构造，且公钥大小为常数。

[31] Drijvers 等. Pixel: multi-signatures for consensus. **USENIX Security 2020** [Google Scholar](https://scholar.google.com/scholar?q=Pixel%3A+multi-signatures+for+consensus)
> 核心思路：Pixel 是一种前向安全的聚合签名方案。
> 局限与区别：本文讨论如何将 Pixel 的验证线性化，并将其与静默设置框架结合，以构建前向安全的静默阈值加密方案。

### 核心技术与方案

本文的整体框架分为两个层次：首先构建一个具有线性验证的静默阈值签名方案（Silent Threshold Signature，STS），然后基于该 STS 构建静默阈值加密方案（Silent Threshold Encryption，STE）。核心思路是利用签名基础见证加密：将密文设计为对“存在一个有效签名”这一声明的见证加密，而阈值签名本身则作为解密密钥。

#### 层次一：构建具有线性验证的静默阈值签名

本文的 STS 方案是对 hinTS [43] 的一个修改，使其验证方程完全线性。线性验证是指验证方程可以表示为矩阵 $A$ 与签名向量 $w$ 的配对运算：$A \circ w = b$，其中 $A$ 和 $b$ 是公开信息，$w$ 是签名。

**关键步骤：**

1.  **静默设置：** 每个参与方 $i$ 独立生成 BLS 密钥对 $(sk_i, pk_i = [sk_i]_1)$，并发布公钥 $pk_i$ 和一组“提示” $hint_i$。提示包括 $[sk_i \cdot \tau^j]_1$ 等形式，用于支持后续的聚合计算，其中 $\tau$ 是 KZG 承诺的随机陷门，由 CRS 提供。

2.  **签名与聚合：** 给定一个消息（或标签）$[\gamma]_2$，每个参与方 $i$ 生成部分签名 $\sigma_i = sk_i \cdot [\gamma]_2$。聚合方收集 $t$ 个部分签名后，计算：
    *   聚合公钥 $\text{aPK}$ 和一个多项式 $B(x)$，该多项式通过插值定义在选定参与方的索引上（值为 1）和其他位置（值为 0）。
    *   使用 Sumcheck 原理 [9,66] 计算多项式 $Q_x(x)$ 和 $Q_Z(x)$，使得 $SK(x) \cdot B(x) = \frac{\text{aSK}}{M+1} + Q_Z(x) Z(x) + Q_x(x) x$，其中 $SK(x) = \sum sk_i L_i(x)$。
    *   生成最终的聚合签名 $w$，包含 $[B(\tau)]_2, \text{aPK}, [Q_Z(\tau)]_1, [Q_x(\tau)]_1, [\hat{Q}_x(\tau)]_1, \sigma^*$ 等元素。

3.  **线性验证：** 验证方通过以下五个配对方程检查签名的有效性，这些方程全部是线性的（即每个方程都是形如 $[x]_1 \circ [y]_2 = [x']_1 \circ [y']_2$ 的线性组合）：
    *   **Sumcheck 验证：** $[SK(\tau)]_1 \circ [B(\tau)]_2 = [1]_2 \circ \text{aPK} + [Z(\tau)]_2 \circ [Q_Z(\tau)]_1 + [\tau]_2 \circ [Q_x(\tau)]_1$
    *   **度检查 1：** $[\tau]_2 \circ [Q_x(\tau)]_1 = [1]_2 \circ [\hat{Q}_x(\tau)]_1$ （确保 $Q_x$ 的度数正确）
    *   **签名验证：** $[\gamma]_2 \circ \text{aPK} = [1]_1 \circ \sigma^*$
    *   **度检查 2：** $[\tau^t]_1 \circ [B(\tau)]_2 = [1]_2 \circ [\hat{B}(\tau)]_1$ （确保 $B$ 有至少 $t+1$ 个非零点，即满足阈值 $t$）
    *   **虚拟参与方检查：** $[1]_1 \circ [B(\tau)]_2 = [\tau-1]_2 \circ [Q_0(\tau)]_1 + 1$ （确保 $B$ 非零）

#### 层次二：从 STS 构建 STE

给定上述具有线性验证的 STS 方案，可以通过签名基础见证加密通用框架构建 STE。

**构造思路：** 令 STS 的验证方程为 $A \circ w = b$，其中 $A$ 是一个 $u \times v$ 的矩阵（由公共信息和加密时选择的随机标签 $[\gamma]_2$ 生成），$w$ 是 $v$ 个群元素组成的签名（即解密所需的证据），$b$ 是 $u$ 个目标群元素。注意 $A$ 和 $b$ 完全公开。

**加密过程：** 加密方随机选择向量 $s = (s_1, \dots, s_u) \in \mathbb{Z}_p^u$，并计算：
*   密文第一部分：$\text{ct}_2 = s^\top \cdot A$ （结果为 $v$ 个群元素）
*   密文第二部分：$\text{ct}_3 = s^\top \cdot b + \text{msg}$ （结果为 1 个目标群元素）
*   将标签 $[\gamma]_2$ 作为密文的一部分公开。

**解密过程：** 收集 $t$ 个有效的部分解密 $\sigma_i = sk_i \cdot [\gamma]_2$（即 STS 的部分签名）。通过聚合这些部分签名和公开的“提示”计算出一个有效的签名向量 $w$。然后，通过以下运算恢复消息：
$ \text{msg} = \text{ct}_3 - \text{ct}_2 \circ w $
正确性源于恒等式 $s^\top A \circ w = s^\top (A \circ w) = s^\top b$。

**安全证明策略：** 证明在通用群模型（GGM）[59,71] 下进行。直觉上，如果敌手能够通过察看密文和部分解密获得关于消息的任何信息，则它必须能够通过通用群操作计算出一个新的群元素。这意味着它能够构造一个有效的签名 $w$，这构成了对 STS 方案的伪造。由于 STS 方案被证明在 GGM 下是不可能的，因此敌手无法获得任何信息，保证了语义安全性。

**系统复杂度：**
*   **通信量（群元素个数）：** 公钥和提示大小：$O(M)$，其中 $M$ 是最大委员会大小；加密密钥（ek）：常数（2个元素）；每个部分解密 $\sigma_i$：常数（1个元素）；密文：常数（9个群元素，即 768 字节）。
*   **计算量：** 加密和部分解密均为常数时间（为例 7ms 和 1ms）；解密聚合时间与委员会大小成线性关系（约为 $O(n)$，但对于 n=1024 约为 200ms）。

### 核心公式与流程

**[加密密钥 ek 的计算]**
$$ \text{ek} = (C, Z) = \left( \left[ \sum_{i \in V} sk_i L_i(\tau) \right]_1, [Z(\tau)]_2 \right) $$
> 作用：加密密钥由聚合的公钥承诺 $C$ 和循环多项式 $Z(\tau)$ 组成，用于生成密文。

**[密文生成（Enc 算法核心）]**
$$ \boldsymbol{A} = \begin{pmatrix} C & [1]_2 & Z & [\tau]_2 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & [\tau]_2 & [1]_2 & 0 & 0 & 0 \\ 0 & [\gamma]_2 & 0 & 0 & 0 & [1]_1 & 0 & 0 \\ [\tau^t]_1 & 0 & 0 & 0 & 0 & 0 & [1]_2 & 0 \\ [1]_1 & 0 & 0 & 0 & 0 & 0 & 0 & Z_0 \end{pmatrix} $$
$$ \boldsymbol{b} = ([0]_T, [0]_T, [0]_T, [0]_T, [1]_T)^\top $$
> 作用：矩阵 $\boldsymbol{A}$ 和向量 $\boldsymbol{b}$ 定义了 STS 的线性验证系统。加密方随机选择向量 $\boldsymbol{s} \in \mathbb{Z}_p^5$，计算 $\text{ct}_2 = \boldsymbol{s}^\top \cdot \boldsymbol{A}$ 和 $\text{ct}_3 = \boldsymbol{s}^\top \cdot \boldsymbol{b} + \text{msg}$。

**[解密聚合（DecAggr 核心步骤）]**
1.  **计算 $B(x)$**：通过插值计算，使得 $B(\omega^i)=1$ 对于所有提供部分解密的 $i \in S_v$ 和虚拟参与方 0；否则 $B(\omega^i)=0$。
2.  **计算聚合公钥**：$\text{aPK} = \frac{1}{M+1} \left( \sum_{i\in S_v} B(\omega^i) pk_i + [1]_1 \right)$。
3.  **计算多项式 $Q_x(x)$ 和 $Q_Z(x)$**：根据 Sumcheck 原理计算。
4.  **计算聚合签名**：$ \text{w} = ([B(\tau)]_2, -\text{aPK}, [-Q_Z(\tau)]_1, [Q_x(\tau)]_1, [\hat{Q}_x(\tau)]_1, \sigma^*, [\hat{B}(\tau)]_1, [-Q_0(\tau)]_1)^\top $。
5.  **恢复消息**：$\text{msg}^* = \text{ct}_3 - \text{ct}_2 \circ \text{w}$。
> 作用：聚合合法的部分解密，计算出满足线性验证系统（$A\circ w=b$）的签名向量 $w$，然后利用配对运算去除掩码，恢复消息。

### 实验结果

实验环境为 2019 年款 MacBook Pro，配备 2.4 GHz Intel Core i9 处理器和 16 GB DDR4 RAM，单线程运行。方案使用 BLS12-381 配对友好曲线实现。核心性能数据如下：加密时间小于 7 毫秒，不依赖于委员会规模；部分解密时间小于 1 毫秒，仅需一次群操作；对于最大委员会规模 1024 方，解密聚合时间约为 200 毫秒。密文大小为 9 个群元素（768 字节），约为标准 ElGamal 密文的 8 倍。部分解密的大小仅为 1 个群元素（96 字节）。一次性密钥生成时间对于 1024 方约为 28 秒（由于当前的实现未优化，预计在优化后会有显著降低）。与需要昂贵交互设置的传统阈值加密方案相比，本文方案在设置阶段彻底消除了交互，使得委员会规模可以轻松扩展。与同类型的分布式广播加密方案 [57]（用于 $t=1$ 情况）相比，本文方案的效率具有可比性。

### 局限性与开放问题
本文方案的安全性证明依赖于通用群模型，这是一个启发式模型，不排除存在针对具体椭圆曲线群的高级攻击。虽然方案实现了常数大小的密文，但公钥和提示的大小随最大委员会规模 $M$ 线性增长。一个开放问题是如何基于更标准的假设（如 $q$-型假设或标准对称性假设）构建静默阈值加密，而非依赖 GGM。另一个方向是研究如何进一步降低解密聚合的计算复杂度，使其完全达到 $O(\log n)$ 或常数时间，以适应超大规模委员会的场景。

### 强关联论文

[13] Boneh, D., Lynn, B., Shacham, H. Short signatures from the Weil pairing. **ASIACRYPT 2001** [Google Scholar](https://scholar.google.com/scholar?q=Short+signatures+from+the+Weil+pairing)

[43] Garg, S., Jain, A., Mukherjee, P., Sinha, R., Wang, M., Zhang, Y. Hints: threshold signatures with silent setup. **IEEE S&P 2024** [Google Scholar](https://scholar.google.com/scholar?q=Hints%3A+threshold+signatures+with+silent+setup)

[53] Kate, A., Zaverucha, G.M., Goldberg, I. Constant-size commitments to polynomials and their applications. **ASIACRYPT 2010** [Google Scholar](https://scholar.google.com/scholar?q=Constant-size+commitments+to+polynomials+and+their+applications)

[12] Boneh, D., Franklin, M. Identity-based encryption from the Weil pairing. **CRYPTO 2001** [Google Scholar](https://scholar.google.com/scholar?q=Identity-based+encryption+from+the+Weil+pairing)

[24] Daza, V., Herranz, J., Morillo, P., Ràfols, C. CCA2-secure threshold broadcast encryption with shorter ciphertexts. **ProvSec 2007** [Google Scholar](https://scholar.google.com/scholar?q=CCA2-secure+threshold+broadcast+encryption+with+shorter+ciphertexts)

[27] Delerablée, C., Pointcheval, D. Dynamic threshold public-key encryption. **CRYPTO 2008** [Google Scholar](https://scholar.google.com/scholar?q=Dynamic+threshold+public-key+encryption)

[57] Kolonelos, D., Malavolta, G., Wee, H. Distributed broadcast encryption from bilinear groups. **ePrint 2023** [Google Scholar](https://scholar.google.com/scholar?q=Distributed+broadcast+encryption+from+bilinear+groups)

[37] Freitag, C., Waters, B., Wu, D.J. How to use (plain) witness encryption: registered ABE, flexible broadcast, and more. **CRYPTO 2023** [Google Scholar](https://scholar.google.com/scholar?q=How+to+use+(plain)+witness+encryption%3A+registered+ABE%2C+flexible+broadcast%2C+and+more)

[31] Drijvers, M., Gorbunov, S., Neven, G., Wee, H. Pixel: multi-signatures for consensus. **USENIX Security 2020** [Google Scholar](https://scholar.google.com/scholar?q=Pixel%3A+multi-signatures+for+consensus)

[67] Reyzin, L., Smith, A., Yakoubov, S. Turning HATE into LOVE: compact homomorphic ad hoc threshold encryption for scalable MPC. **CSCML 2021** [Google Scholar](https://scholar.google.com/scholar?q=Turning+HATE+into+LOVE%3A+compact+homomorphic+ad+hoc+threshold+encryption+for+scalable+MPC)


## 关键词

+ 无声设置门限加密确定性公钥
+ 见证加密门限签名配对构造
+ 异步设置动态门限多世界支持
+ 通用群模型门限加密安全证明
+ 分布式广播加密配对替代构造