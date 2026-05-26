---
title: "Traceable ring signature"
标题简称:
论文类型: conference
会议简称: PKC
发表年份: 2007
created: 2025-05-12 08:37:37
modified: 2025-05-12 08:44:38
---

## Traceable ring signature

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-540-71677-8_13)
+ [archive](https://eprint.iacr.org/2006/389)

## 作者

+ Eiichiro Fujisaki
+ Koutarou Suzuki

## 笔记

### 背景与动机
数字签名中的匿名性并非总是有益的。环签名 [24] 允许签名者在一组自选的“环”中匿名签署消息，无需群管理员，且支持动态群组形成，但其匿名性是绝对的，这为恶意或不负责任的签名者留下了可乘之机。例如，在BBS的匿名投票中，该机制无法阻止同一人多次投票。群签名 [10] 虽然提供了可追踪性，但需要一个拥有撤销匿名特权的群管理员，这违反了“无托管”的初衷。本文旨在填补环签名与群签名之间的缺口，提出一种具有“温和”匿名限制的环签名方案。该方案在保留环签名灵活性的同时，引入“公共可追踪性”和“标签可链接性”的概念，以约束“过度匿名”。具体来说，若同一签名者使用同一标签对两个不同消息签名，其身份将被公开追踪；若对同一消息重复签名，则两个签名会被链接。

### 相关工作

[2] Au, Chow, Susilo, Tsang等. Short linkable ring signatures revisited. **EUROPKI 2006**
> 核心思路：提出短可链接环签名，关注签名链接性。
> 局限与区别：该工作主要解决链接性，未涉及本文所定义的公共可追踪性（即揭示签名者身份）；本文方案同时满足了链接性与身份追踪。

[4] Bender, Katz, Morselli等. Ring signatures: stronger definitions, and constructions without random oracles. **TCC 2006**
> 核心思路：形式化了环签名的更强安全性定义，特别是针对恶意密钥选择和子群攻击。
> 局限与区别：本文的安全模型直接继承并扩展了 [4] 的定义，但在可追踪环签名语境下，将匿名性定义为一种较弱的版本，因为最强的匿名性（即使所有其他密钥泄露也能保持匿名）与公共可追踪性无法共存。

[5] Brands. Untraceable off-line cash in wallet with observers. **CRYPTO 1993**
> 核心思路：提出了受限盲签名，具有“双重花费”时可追踪用户的特性。
> 局限与区别：受限盲签名需要一个在线签名者（类似群管理员）来发行“硬币”，不支持无特设管理员的临时群组形成，而本文的环签名允许签名者自主选择环。

[17] Liu, Wei, Wong等. Linkable spontaneous anonymous group signature for ad hoc groups. **ACISP 2004**
> 核心思路：提出首个可链接环签名，允许链接同一签名者的两次签名。
> 局限与区别：该方案未考虑“免陷害性”攻击，即一个恶意签名者可以陷害诚实用户。本文方案通过引入基于多项式的构造，从设计上防止了这种陷害。

[24] Rivest, Shamir, Tauman等. How to leak a secret. **Asiacrypt 2001**
> 核心思路：首次形式化定义了环签名，展示了如何利用陷门置换构造环签名。
> 局限与区别：该经典方案不具备任何链接性或可追踪性，是本文方案的起点但非终点。本文在其基础上增加了对“标签”的依赖和可追踪性机制。

[25] Teranishi, Furukawa, Sako等. k-times anonymous authentication. **Asiacrypt 2004**
> 核心思路：允许用户在k次内匿名认证，超过k次则暴露身份。
> 局限与区别：该工作需要一个发行方，且不支持临时群组选择。本文指出，任何可追踪环签名可转化为其变体，但反之则不然。

### 核心技术与方案

本文的核心构造基于离散对数假设和DDH假设，在随机预言机模型下证明安全。方案的核心思想是将签名者的身份信息嵌入到一种基于**拉格朗日插值**的线性关系中。

**构造思路**：对于标签L（包含问题描述和环成员公钥集）和消息m，签名者i首先计算一个固定的锚点 $A_0 = H'(L, m)$。然后，决定一条穿过点 $(0, \log_h A_0)$ 和点 $(i, x_i)$ 的直线，其中 $x_i$ 是签名者的私钥，$h = H(L)$。该直线的斜率 $A_1$ 通过 $A_1 = (\sigma_i / A_0)^{1/i}$ 计算，其中 $\sigma_i = h^{x_i}$。对于环中所有其他成员j，该直线在横坐标j处的纵坐标即为伪造的签名元素 $\sigma_j = A_0 \cdot (A_1)^j$。由于 $\log_h \sigma_j$ 与成员j的私钥 $x_j$ 无关，任何试图陷害用户j的攻击者都必须猜测或同时解决离散对数问题。

**签名与验证**：签名者生成一个关于合取语言的非交互零知识证明（基于Fiat-Shamir变换），该语言证明环中存在某个索引i，使得 $\log_g y_i = \log_h \sigma_i$。为了高效证明，签名者使用 [11] 的“1-out-of-n”零知识证明技术，但巧妙地利用上述构造，使得该证明可以简化为一个简单的Sigma协议，证明者只需为真正的签名者i提供一个有效的响应，而其他位置的值可随机选取。最终签名为 $(A_1, c_N, z_N)$，其中 $c_N$ 和 $z_N$ 是证明的挑战和响应。

**追踪算法**：输入两个同一标签下的签名，接收方计算两个签名中的所有 $\sigma_i$ 和 $\sigma_i'$。如果存在唯一索引i使得 $\sigma_i = \sigma_i'$，则输出相应的公钥 $pk_i$，揭示该签名者。如果所有 $\sigma_i = \sigma_i'$，则输出“linked”（链接）。如果无相等，则输出“indep”（独立）。这利用了插值的性质：同一条直线上的点，在横坐标i处有相同的纵坐标当且仅当这条直线由同一个签名者定义。

**安全性直觉**：
- **标签可链接性**：如果一个敌手对于n个成员的环生成了n+1个有效的签名，且所有签名相互独立（追踪算法输出“indep”），则根据鸽巢原理和拉格朗日插值的唯一性，必然存在两个签名由同一人产生，导致矛盾。这保证了不能再造一张新椅子。
- **匿名性**：匿名性依赖于DDH假设。如果DDH成立，那么模拟器可以在不知道真正签名者私钥的情况下，通过随机抽取数值并控制随机预言机H和H'来完美模拟签名。由于模拟的签名与真实签名不可区分，敌手无法判断是哪个用户签的名。
- **免陷害性**：如果敌手不想被陷害，必须伪造一个针对受害者 $pk_i$ 的签名。根据引理3，如果敌手能够使得追踪算法输出 $pk_i$，那么有压倒性概率，敌手已经成功伪造了用户i的签名（即 $\sigma_i$ 是用 $x_i$ 产生的）。这可以规约为离散对数问题：通过重绕技术，从敌手的两次运行中提取出私钥 $x_i$。

**复杂度**：签名大小为 $O(n)$，包含一个群元素 $A_1$ 和n个Zq元素 $(c_i, z_i)$。验证耗时为 $O(n)$，需要n次指数运算生成 $\sigma_i$ 和验证n个等式。与经典的 [17] 等方案相比，该方案在通信和计算量上具有竞争力，但主要优势在于其简洁性以及同时满足公共可追踪性、标签可链接性和免陷害性。

### 核心公式与流程

**[签名生成 - 线性插值]**
$$\sigma_i = h^{x_i}, \quad A_0 = H'(L, m), \quad A_1 = \left(\frac{\sigma_i}{A_0}\right)^{1/i}, \quad \sigma_j = A_0 \cdot (A_1)^j \text{ for } j \neq i$$
> 作用：将签名者i的真实签名 $\sigma_i$ 与一个由标签和消息决定的锚点$A_0$ 线性组合，生成整个环的伪造签名 $\sigma_j$，使得它们共线。

**[非交互零知识证明 - 1-out-of-n Sigma协议]**
1. 证明者选择随机数 $w_i$，计算 $a_i = g^{w_i}, b_i = h^{w_i}$。
2. 对 $j \neq i$，选择随机数 $z_j, c_j$，计算 $a_j = g^{z_j} y_j^{c_j}, b_j = h^{z_j} \sigma_j^{c_j}$。
3. 计算 $c = H''(L, m, A_0, A_1, a_N, b_N)$。
4. 计算 $c_i = c - \sum_{j \neq i} c_j \pmod{q}$, $z_i = w_i - c_i x_i \pmod{q}$。
5. 输出 $(c_N, z_N) = ((c_1,...,c_n), (z_1,...,z_n))$。
> 作用：证明至少存在一个i使得 $\log_g y_i = \log_h \sigma_i$，而无需暴露哪个i。这是一个标准的Sigma协议证明技巧，通过在挑战c上分配来隐藏真实签名者。

**[追踪算法]**
对环中每个i，比较两个签名中的 $\sigma_i$ 和 $\sigma_i'$：
- 如果存在唯一的i使得 $\sigma_i = \sigma_i'$，则输出 $pk_i$。
- 如果所有i都相等，输出“linked”。
- 否则输出“indep”。
> 作用：利用插值直线的唯一性，通过比较横坐标i上的纵坐标值来追踪签名者。如果两签名来自同一人对不同消息的签名，则只有一个点重合；如果是对同一消息的签名，则所有点重合；如果是不同人，则无点重合。

### 实验结果
本文是理论性方案设计，未提供具体实验代码或数据集。然而，通过分析其计算复杂度可评估性能。签名算法主要开销在于生成n次模指数运算（用于计算所有 $\sigma_j$）和证明过程中的约n+1次指数运算。验证算法需要约2n次指数运算（用于计算每个成员的a_i和b_i）。通信开销方面，签名由1个群元素 $A_1$ 和2n个 $\mathbb{Z}_q$ 元素组成，大小约为 $|G| + 2n|q|$。相比 [26] 中基于累加器的短签名方案，本文方案的签名长度线性增长于环的大小，但在群元素足够小（如256位）时，对于典型规模的群（如数百人），通信量是可行的。与 [27] 相比，本文方案在结构和证明上更简单，更易于实现。

### 局限性与开放问题
本文方案的安全性依赖于随机预言机模型（ROM），这是理论密码学中的一个理想化模型，虽然高效但不如标准模型（Standard Model）安全。另外，签名的长度随环的大小线性增长，对于超大规模环（如万人以上），通信和计算开销可能成为瓶颈。未来的一个重要开放问题是构造具有常数大小签名的高效可追踪环签名方案，或在不依赖随机预言机的标准模型下实现类似功能。同时，本文的匿名性定义是较弱的版本，如何在不牺牲追踪性的前提下实现更强的匿名性（如抵抗非成员攻击）也是一个难题。

### 强关联论文

[4] Bender, Katz, Morselli等. Ring signatures: stronger definitions, and constructions without random oracles. **TCC 2006**

[5] Brands. Untraceable off-line cash in wallet with observers. **CRYPTO 1993**

[10] Chaum, Van Heyst等. Group signatures. **EUROCRYPT 1991**

[11] Cramer, Damgård, Schoenmakers等. Proofs of partial knowledge and simplified design of witness hiding protocols. **CRYPTO 1994**

[17] Liu, Wei, Wong等. Linkable spontaneous anonymous group signature for ad hoc groups. **ACISP 2004**

[24] Rivest, Shamir, Tauman等. How to leak a secret. **Asiacrypt 2001**

[25] Teranishi, Furukawa, Sako等. k-times anonymous authentication. **Asiacrypt 2004**

[27] Tsang, Wei, Chan, Au, Liu, Wong等. Separable linkable threshold ring signatures. **INDCRYPT 2004**


## 关键词

+ 可追踪环签名
+ 环签名
+ 匿名性限制
+ 双重签名检测
+ 匿名投票
+ 过度匿名防护