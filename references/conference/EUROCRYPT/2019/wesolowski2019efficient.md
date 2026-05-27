---
title: "Efficient verifiable delay functions"
doi: 10.1007/978-3-030-17659-4_13
标题简称:
论文类型: conference
会议简称: EUROCRYPT
发表年份: 2019
created: 2025-04-28 16:45:56
modified: 2025-04-28 16:46:28
---
## Efficient verifiable delay functions

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-030-17659-4_13)

## 作者

+ Benjamin Wesolowski 

## 笔记

### 背景与动机
Verifiable delay function（VDF）是一种在指定顺序时间 Δ 内可计算、但结果能被高效验证的函数，在去中心化系统（如可信随机信标、资源高效区块链）中具有关键应用。然而，Boneh 等人 [4] 提出的早期 VDF 构造存在明显瓶颈：要么需要 polylog(Δ) 规模的并行性才能达到 Δ 的并行时间，要么在面对大量预计算时不安全，必须定期更新设置。Lenstra 和 Wesolowski [15] 提出的 sloth 函数仅达到常数因子的验证加速，未能实现指数级验证–计算差距。因此，构造一个严格满足 Δ 顺序性、验证复杂度 polylog(Δ)，且不依赖可信设置或大规模并行的 VDF 成为开放问题。本文基于 Rivest–Shamir–Wagner [18] 的时间锁谜题，通过引入一个公开随机的简洁论证，首次实现了输出和证明各为单个群元素、验证仅需两次指数运算的高效 VDF。

### 相关工作

[4] Boneh, D. et al. Verifiable delay functions. **CRYPTO 2018** [Google Scholar](https://scholar.google.com/scholar?q=Verifiable+delay+functions)
> 核心思路：首次形式化定义 VDF，并给出基于重复平方和未知阶群的构造思路。
> 局限与区别：其中一个构造需要 polylog(Δ) 并行性，另一个构造需要频繁更新设置；本文提供了无需并行、无需预计算的安全方案。

[15] Lenstra, A.K. et al. Trustworthy public randomness with sloth, unicorn and trx. **Int. J. Appl. Cryptol. 2016** [Google Scholar](https://scholar.google.com/scholar?q=Trustworthy+public+randomness+with+sloth+unicorn+and+trx)
> 核心思路：提出 sloth 慢速哈希函数用于随机信标。
> 局限与区别：验证仅比计算快常数因子，不具备指数级加速；本文实现了指数级验证–计算差距。

[18] Rivest, R.L. et al. Time-lock puzzles and timed-release crypto. **Technical report 1996** [Google Scholar](https://scholar.google.com/scholar?q=Time-lock+puzzles+and+timed-release+crypto)
> 核心思路：提出基于 RSA 组的顺序平方计算作为时间锁谜题。
> 局限与区别：该谜题本身无法直接验证结果正确性；本文在其基础上添加了公开可验证的简洁证明。

[16] Pietrzak, K. Simple verifiable delay functions. **ITCS 2019** [Google Scholar](https://scholar.google.com/scholar?q=Simple+verifiable+delay+functions)
> 核心思路：独立提出另一种 VDF，基于相同时间锁谜题，证明长度为 O(log Δ) 个群元素。
> 局限与区别：证明较长（10KB vs 0.25KB），验证需要 O(log Δ) 次指数运算；本文证明仅一个群元素，验证仅需两次指数运算。

[6] Boneh, D. et al. Efficient generation of shared RSA keys. **CRYPTO 1997** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+generation+of+shared+RSA+keys)
> 核心思路：通过安全多方计算生成 RSA 模数以避免单点信任。
> 局限与区别：需要假设参与方不共谋；本文使用类群实现无需可信设置的公开参数。

[9] Buchmann, J. et al. A key-exchange system based on imaginary quadratic fields. **J. Cryptol. 1988** [Google Scholar](https://scholar.google.com/scholar?q=A+key-exchange+system+based+on+imaginary+quadratic+fields)
> 核心思路：提出基于虚二次域类群的密码系统，其阶的计算被认为是困难的。
> 局限与区别：本文将其作为 VDF 中未知阶群的实例，避免 RSA 模数所需的可信生成过程。

[7] Boneh, D. et al. Timed commitments. **CRYPTO 2000** [Google Scholar](https://scholar.google.com/scholar?q=Timed+commitments)
> 核心思路：引入定时承诺，可在预定时间内强制打开。
> 局限与区别：与 VDF 不同，它涉及承诺的强制打开而非函数的可验证延迟计算。

[17] Rabin, M.O. Transaction protection by beacons. **J. Comput. Syst. Sci. 1983** [Google Scholar](https://scholar.google.com/scholar?q=Transaction+protection+by+beacons)
> 核心思路：提出随机信标用于产生可公开验证的随机数。
> 局限与区别：原方案依赖于可信第三方；VDF 可实现无偏且不可预测的去中心化随机数生成。

[1] Bellare, M. et al. Encapsulated key escrow. **Technical report 1996** [Google Scholar](https://scholar.google.com/scholar?q=Encapsulated+key+escrow)
> 核心思路：引入时间胶囊用于密钥托管，防止早期恢复。
> 局限与区别：属于时间敏感性密码学早期工作，与 VDF 的计算–验证特性不同。

### 核心技术与方案
本文构造了一个**陷门 VDF**，进而可转化为标准 VDF。方案基于一个有限群 $G$（其阶是秘密陷门），例如 RSA 群 $( \mathbf { Z } / N \mathbf { Z } ) ^ { \times } / \{ \pm 1 \}$ 或虚二次域类群。输入 $x$ 被哈希到群元素 $g = H_G(x)$，输出为 $y = g^{2^t}$，其中 $t$ 是时间参数。陷门持有者可利用群阶快速计算 $y$，其他人则只能通过 $t$ 次顺序平方计算得到相同结果。  
为了支持公开验证，构造了一个公开硬币简洁论证：给定 $(G, g, y, t)$，验证者均匀选取一个 2k 比特的素数 $\ell$，证明者计算 $\pi = g^{\lfloor 2^t/\ell \rfloor}$，验证者检查 $y = \pi^\ell \cdot g^{r}$，其中 $r = 2^t \bmod \ell$。该协议通过 Fiat-Shamir 转化为非交互式：$\ell = H_{\mathrm{prime}}(\mathrm{bin}(g) ||| \mathrm{bin}(y))$。  
**正确性直觉**：若 $y = g^{2^t}$，则 $\pi^\ell g^r = g^{\lfloor 2^t/\ell \rfloor \cdot \ell} \cdot g^r = g^{2^t} = y$。  
**完备性**：陷门持有者能通过群阶计算 $\pi$，任何人通过顺序平方计算 $y$ 后也可用算法（如 Algorithm 5）在 $O(t/\log t)$ 群操作内得到 $\pi$。  
**可靠性（Soundness）**：在随机预言模型下，若对手能输出虚假 $(y',\pi')$ 使验证通过，则可构造一个求解根查找问题（在群 $G$ 中，给定 $u \neq 1$，求 $v$ 使 $v^\ell = u$）的算法，该问题在 RSA 和类群中被认为困难。具体地，通过引理 1，对手获胜概率 $p_{\mathrm{win}}$ 可转化为以 $p_{\mathrm{win}}/(q+1)$ 概率赢得根查找游戏。注意在 RSA 设置中，工作空间为 $( \mathbf { Z } / N \mathbf { Z } ) ^ { \times } / \{ \pm 1 \}$ 以避免 $\pm 1$ 带来的平凡攻击。  
**顺序性（Sequentiality）**：在随机预言模型下，若对手能在时间 $< t\delta$ 内赢得求值竞赛，则可将其转化为针对时间锁假设的对手，因此方案是 $t\delta$-顺序的。  
**渐进复杂度**：  
- 输出 $y$ 为一个群元素，证明 $\pi$ 为一个群元素（可选传输 $(\ell,\pi)$ 以压缩带宽）。  
- 验证：计算 $\ell = H_{\mathrm{prime}}(\cdot)$，一次模幂 $g^{2^t}$（实际上只需计算 $g^r$ 和 $\pi^\ell$ 并进行一次群乘），共约两次指数运算（指数比特长 2k）。  
- 求值：$t$ 次顺序平方计算 $y$，外加 $O(t/\log t)$ 群操作计算 $\pi$，后者可高度并行化。  
- 聚合：对于多个输入 $(x_i)$，可利用随机线性组合生成单个聚合证明 $\tilde\pi = (\prod g_i^{\alpha_i})^{\lfloor 2^t/\ell\rfloor}$，验证方程为 $\tilde\pi^\ell \cdot (\prod g_i^{\alpha_i})^r = \prod y_i^{\alpha_i}$，安全性通过重随机化和 Cauchy–Schwarz 论证归约到根查找问题。  
- 水印：将身份 id 嵌入哈希计算 $\ell = H_{\mathrm{prime}}(\mathrm{id} ||| \mathrm{bin}(g) ||| \mathrm{bin}(y))$，使得每个证明与特定身份绑定，防止他人冒充。

### 核心公式与流程

**验证方程（基础构造）**
$$
\pi^\ell \cdot g^r = y
$$
> 作用：验证者检查 $\pi$ 和 $y$ 是否满足关系，其中 $r = 2^t \bmod \ell$。

**挑战生成（Fiat-Shamir）**
$$
\ell = H_{\mathrm{prime}}(\mathrm{bin}(g) \,|||\, \mathrm{bin}(y))
$$
> 作用：将交互式协议转换为非交互式，输出素数 $\ell$ 作为挑战。

**聚合验证方程**
$$
\tilde\pi^\ell \cdot \left(\prod_{i=1}^n g_i^{\alpha_i}\right)^r = \prod_{i=1}^n y_i^{\alpha_i}
$$
> 作用：用一个群元素 $\tilde\pi$ 同时证明所有 $n$ 个输出 $y_i = g_i^{2^t}$。

**水印证明**
$$
\ell = H_{\mathrm{prime}}(\mathrm{id} \,|||\, \mathrm{bin}(g) \,|||\, \mathrm{bin}(y))
$$
> 作用：将挑战绑定到证明者身份 id，防止证明被他人重用。

**根查找困难性**
$$
\text{给定 } u \neq 1_G,\ \text{求 } v \text{ 使得 } v^\ell = u
$$
> 作用：可靠性证明的核心假设——在未知阶群中提取 $\ell$ 次根是困难的。

**证明 $\pi$ 的计算（算法 5 核心思路）**
$$
g^{\lfloor 2^t/\ell\rfloor} = \prod_{b=0}^{2^\kappa-1} \left(\prod_{i\in I_b} g^{2^{\kappa i}}\right)^b
$$
> 作用：通过基 $2^\kappa$ 分解指数，利用预计算值在 $O(t/\kappa + \kappa 2^\kappa)$ 群操作内完成，取 $\kappa = \log t/3$ 得到 $O(3t/\log t)$。

### 实验结果
本论文为纯理论密码学构造，未提供实验数据。文中仅给出理论复杂度分析：在 RSA 组（2048 比特模数）和时间参数 $\Delta = 2^{40}$ 顺序平方时，输出和证明各为 0.25KB（对比 Pietrzak [16] 方案 10KB）；验证需两次指数运算（指数比特长约为 256 比特，即安全级别）；证明计算开销约为 $O(\Delta/\log \Delta)$ 群操作，折算为相对于求值时间 $T$ 的约 5% 额外开销（$\omega \approx 20$）。文中还讨论了实际时序估计的挑战，并提及 Ethereum Foundation 和 Protocol Labs 正在开发专用硬件以实现精确的时序基准。

### 局限性与开放问题
1. 安全性依赖于两种不同的假设：顺序性基于时间锁假设（对于 RSA 组等），而可靠性基于根查找问题假设，后者尚未被严格归约到标准困难问题如大整数分解或 RSA 问题。  
2. 在类群设置中，序列的选择（如判别式的大素数性）直接影响安全性，且类群运算可能不如 RSA 乘法快速，实际性能需进一步评估。  
3. 证明的计算虽可并行化，但总计算量仍超出顺序求值约 5%，对于某些对延迟极度敏感的应用，可能需要采用分段预处理方案（Section 4.3）来降低开销，但会增加证明长度。

### 强关联论文

[4] Boneh, D. et al. Verifiable delay functions. **CRYPTO 2018** [Google Scholar](https://scholar.google.com/scholar?q=Verifiable+delay+functions)

[15] Lenstra, A.K. et al. Trustworthy public randomness with sloth, unicorn and trx. **Int. J. Appl. Cryptol. 2016** [Google Scholar](https://scholar.google.com/scholar?q=Trustworthy+public+randomness+with+sloth+unicorn+and+trx)

[18] Rivest, R.L. et al. Time-lock puzzles and timed-release crypto. **Technical report 1996** [Google Scholar](https://scholar.google.com/scholar?q=Time-lock+puzzles+and+timed-release+crypto)

[16] Pietrzak, K. Simple verifiable delay functions. **ITCS 2019** [Google Scholar](https://scholar.google.com/scholar?q=Simple+verifiable+delay+functions)

[6] Boneh, D. et al. Efficient generation of shared RSA keys. **CRYPTO 1997** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+generation+of+shared+RSA+keys)

[9] Buchmann, J. et al. A key-exchange system based on imaginary quadratic fields. **J. Cryptol. 1988** [Google Scholar](https://scholar.google.com/scholar?q=A+key-exchange+system+based+on+imaginary+quadratic+fields)

[7] Boneh, D. et al. Timed commitments. **CRYPTO 2000** [Google Scholar](https://scholar.google.com/scholar?q=Timed+commitments)

[17] Rabin, M.O. Transaction protection by beacons. **J. Comput. Syst. Sci. 1983** [Google Scholar](https://scholar.google.com/scholar?q=Transaction+protection+by+beacons)

[1] Bellare, M. et al. Encapsulated key escrow. **Technical report 1996** [Google Scholar](https://scholar.google.com/scholar?q=Encapsulated+key+escrow)


## 关键词

+ 可验证延迟函数
+ 陷门VDF
+ 未知阶群
+ RSA群
+ 去中心化随机性