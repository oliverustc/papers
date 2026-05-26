---
title: "Efficient Fully Structure-Preserving Signatures and Shrinking Commitments"
标题简称:
论文类型: journal
期刊简称: Journal of Cryptology
发表年份: 2019
created: 2025-05-12 09:13:24
modified: 2025-05-12 09:15:41
---

## Efficient Fully Structure-Preserving Signatures and Shrinking Commitments

## 发表信息

+ [原文链接]()

## 作者

+ Masayuki Abe
+ [Jens Groth](Jens%20Groth.md)
+ [Markulf Kohlweiss](Markulf%20Kohlweiss.md)
+ Miyako Ohkubo
+ Mehdi Tibouchi

## 笔记

### 背景与动机

在基于双线性对的密码学中，结构保持密码学起初要求公钥、消息和签名等公开分量均为源群元素，这使得它们能够与Groth-Sahai证明系统等工具平滑组合，从而构造出复杂的隐私保护协议。然而，现有结构保持签名方案（SPS）的私钥通常是指数形式的标量值，这带来了一个根本性的瓶颈：当需要证明对私钥的拥有时，必须使用Groth-Sahai证明系统逐比特地分解该标量值，导致证明规模与安全参数对数线性增长。例如，方案 [2] 的私钥包含 4 个标量值，对其知识证明需要超过 61,000 个群元素，这在实际应用中是禁止性的。本文旨在填补这一空白，首次提出**完全结构保持签名**（FSPS）的概念，要求私钥本身也由群元素组成，从而允许使用Groth-Sahai证明系统进行高效、在线可提取（无需重绕）的私钥知识证明。

### 相关工作

[2] Abe et al. Constant-size structure-preserving signatures: Generic constructions and simple assumptions. **J. Cryptology 2016** [Google Scholar](https://scholar.google.com/scholar?q=Constant-size+structure-preserving+signatures%3A+Generic+constructions+and+simple+assumptions)
> 核心思路：提出了部分一次性签名（POS）和xRMA安全的FSPS作为构建块。
> 局限与区别：其FSPS仅满足弱安全模型（扩展随机消息攻击），且签名需要知道消息的离散对数，限制了可用性。

[3] Abe et al. Structure-preserving signatures and commitments to group elements. **J. Cryptology 2016** [Google Scholar](https://scholar.google.com/scholar?q=Structure-preserving+signatures+and+commitments+to+group+elements)
> 核心思路：奠定了结构保持密码学的基础，提出了第一个SPS和SPTC方案。
> 局限与区别：所有SPTC都是扩展的（承诺长度大于消息长度），并未针对完全结构保持进行设计。

[8] Abe et al. Group to group commitments do not shrink. **EUROCRYPT 2012** [Google Scholar](https://scholar.google.com/scholar?q=Group+to+group+commitments+do+not+shrink)
> 核心思路：证明了在标准定义下，结构保持承诺（SPTC）不可能实现压缩。
> 局限与区别：该不可能性依赖于完全绑定安全性；本文通过放松为“选择消息目标抗碰撞性”（CMTCR）来规避该结果。

[28] Damgård et al. Non-interactive and reusable non-malleable commitment schemes. **STOC 2003** [Google Scholar](https://scholar.google.com/scholar?q=Non-interactive+and+reusable+non-malleable+commitment+schemes)
> 核心思路：提出了“诚实发送者绑定”这一弱化绑定概念。
> 局限与区别：本文将其扩展为多会话的CMTCR概念，并证明其对于构造安全签名足够。

[29] Escala et al. Fine-tuning Groth-Sahai proofs. **PKC 2014** [Google Scholar](https://scholar.google.com/scholar?q=Fine-tuning+Groth-Sahai+proofs)
> 核心思路：优化了Groth-Sahai证明系统的效率，特别是关于多标量乘法的证明。
> 局限与区别：本文利用该优化来计算FSPS中私钥知识证明的具体开销。

[38] Groth et al. Efficient noninteractive proof systems for bilinear groups. **SIAM J. Comput. 2012** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+noninteractive+proof+systems+for+bilinear+groups)
> 核心思路：提出了Groth-Sahai NIWI/NIZK证明系统，是处理双线性群上方程的基础工具。
> 局限与区别：用于证明时，若私钥为标量值，则需逐比特处理；FSPS使其能直接处理群元素私钥。

[50] Wang et al. How to obtain fully structure-preserving (automorphic) signatures from structure-preserving ones. **ASIACRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=How+to+obtain+fully+structure-preserving+(automorphic)+signatures+from+structure-preserving+ones)
> 核心思路：改进了本文的框架，提出了更短签名但更长私钥的FSPS变体。
> 局限与区别：在效率权衡上有所不同，验证了本文框架的通用性。

### 核心技术与方案

本文的技术核心是构建一个满足**选择消息目标抗碰撞性**（CMTCR）的**压缩结构保持陷门承诺方案**（SPTC），并以此为基础构造第一个基于标准假设的FSPS方案（FSP2），以及在通用群模型中构造一个效率更高的组合FSPS方案（EFSP1）。

**1. 压缩 SPTC 的构造**
为绕过 [8] 的不可能性结果（要求完全绑定），本文定义了CMTCR安全性，该安全性保证敌手无法对诚实生成的承诺找到不同的有效打开。构造分两步：首先，提出一个**消息转置承诺**（MTC），将标量消息 $m \in \mathbb{Z}_p^\ell$ 承诺为一个群元素 $\tilde{G}_u = \tilde{G}^\zeta \prod_{i=1}^\ell \tilde{X}_i^{m_i}$，其打开为 $R = G^\zeta$。该MTC的安全性直接基于双配对（DBP）假设。然而，MTC不是结构保持的，因为消息是标量。为了使其结构保持，本文将MTC与部分一次性签名（POS）结合。具体地，对一个由 $k$ 个群元素组成的消息向量 $M$，签名者先生成POS的长期密钥对 $(sk_{pos}, vk_{pos})$ 和 $k$ 个一次性密钥对 $(osk_{pos}^{(j)}, ovk_{pos}^{(j)})$，并用 $sk_{pos}$ 和 $osk_{pos}^{(j)}$ 对每个消息块 $M^{(j)}$ 生成POS签名 $\sigma_{pos}^{(j)}$。然后，使用MTC对**所有POS私钥**（一个标量向量 $(sk_{pos}, osk_{pos}^{(1)}, \dots, osk_{pos}^{(k)})$）进行承诺。由于POS的公钥是其私钥在特定基下的指数，MTC的打开 $open_{mtc}$ 可以包含这些公钥 $\gamma(sk_{pos}, \dots) = (vk_{pos}, ovk_{pos}^{(1)}, \dots)$。最终，整个TC的承诺就是MTC的承诺（单个群元素），而打开则包含MTC的打开、$vk_{pos}$、所有 $ovk_{pos}^{(j)}$ 和所有的POS签名。验证时，检查MTC的验证方程和所有POS签名的验证方程。该TC的CMTCR安全性可规约到MTC的目标抗碰撞性和POS的多密钥一次性非自适应选择消息攻击（MK-OT-NACMA）安全性。

**2. 基于 SPTC 的 FSPS 构造（FSP2）**
给定一个CMTCR安全的SPTC和一个UF-XRMA安全的FSPS（记为xSIG），构造FSP2。FSP2的签名过程为：对消息 $M$，运行TC.Com生成 $(com_{tc}, open_{tc})$，然后用xSIG的私钥对 $com_{tc}$ 进行签名得到 $\sigma_{xsig}$。最终签名为 $\sigma = (\sigma_{xsig}, open_{tc}, com_{tc})$。安全性证明的核心是：若敌手输出合法伪造，则要么 $com_{tc}^\dagger$ 从未在签名查询中出现过（此时可攻破xSIG的UF-XRMA安全），要么 $com_{tc}^\dagger$ 出现过但伪造消息不同（此时可攻破TC的CMTCR安全）。由于xSIG只在由TC.SimCom随机生成的群元素（承诺）上签名，这满足xRMA的攻击模型。该构造实现了UF-CMA安全。在具体实例化中，xSIG的私钥为 $(K_1, K_2, K_3, K_4)$ 共4个 $\mathbb{G}$ 元素，使得FSP2也是FSPS。

**3. 高效的组合 FSPS 构造（EFSP1）**
在通用群模型中，本文构造了签名大小为 $\Omega(\sqrt{L})$ 的EFSP1，其验证密钥仅为单个群元素 $V = G^v$。构造思想是让签名者自己选取向量 $U = G^u \in \mathbb{G}^{\ell-1}$ 作为临时公钥并包含在签名中，从而在签名算法中能使用 $u$ 进行线性运算。对消息 $\tilde{M} \in \tilde{\mathbb{G}}^{\ell \times k}$，签名算法选取随机数 $z$ 和 $u$，计算：
$$R = G^{1/z}, \quad \tilde{S} = (\tilde{Y}_1 \tilde{X}^u \tilde{G}^v)^z$$
$$\tilde{T}_j = \left( \prod_{i=1}^{\ell-1} \tilde{M}_{(i,j)}^{u_i} \cdot \tilde{M}_{(\ell,j)} \cdot \tilde{Y}_j^v \cdot (\tilde{Y}_1^v \prod_{i=1}^{\ell-1} (\tilde{X}_i^v)^{u_i} \tilde{G}^{v^2})^{b z} \right)^z$$
其中 $b=0$ 表示随机化签名，$b=1$ 表示强不可伪造签名。验证方程为：
$$e(R, \tilde{S}) = e(G, \tilde{Y}_1) \prod_i e(U_i, \tilde{X}_i) e(V, \tilde{G})$$
$$e(R, \tilde{T}_j) = \prod_i e(U_i, \tilde{M}_{(i,j)}) e(G, \tilde{M}_{(\ell,j)}) e(V, \tilde{Y}_j) e(V, \tilde{S})^b$$
安全性通过在通用群模型中将签名元素视为关于未知标量 $(v, u_i, x_i, y_j, z_i)$ 的劳伦多项式来证明。分析表明，敌手只能通过复制先前查询中 $b$ 类型相同的消息-签名对来满足验证方程。

**效率对比**：FSP2的私钥大小为4个 $\mathbb{G}$ 元素，验证密钥需约 $10+3k+3\ell$ 个元素；EFSP1的私钥大小为 $k+\ell+1$ 个 $\tilde{\mathbb{G}}$ 元素，验证密钥仅为1个 $\mathbb{G}$ 元素。签名大小上，FSP2为 $(7+k+\ell, 4+2k)$，EFSP1为 $(\ell, 1+k)$。两者签名大小均满足理论下界 $\kappa + \sigma \ge \sqrt{L}$。

### 核心公式与流程

**[MTC承诺生成]**
$$\tilde{G}_u := \tilde{G}^\zeta \prod_{i=1}^\ell \tilde{X}_i^{m_i}, \quad R := G^\zeta$$
> 作用：将标量消息向量 $m \in \mathbb{Z}_p^\ell$ 压缩承诺为一个 $\tilde{\mathbb{G}}$ 元素，打开为一个 $\mathbb{G}$ 元素，是构建压缩SPTC的核心。

**[FSP2签名算法]**
$$(com_{tc}, open_{tc}) \gets \mathsf{TC.Com}(ck_{tc}, M); \quad \sigma_{xsig} \gets \mathsf{xSIG.Sign}(sk_{xsig}, com_{tc})$$
$$\sigma := (\sigma_{xsig}, open_{tc}, com_{tc})$$
> 作用：利用CMTCR安全的SPTC打破消息与xSIG签名之间的直接消息依赖性，使得xSIG只需对随机群元素（承诺）签名，从而将xRMA安全提升为CMA安全。

**[EFSP1验证方程（随机化模式，$b=0$）]**
$$e(R, \tilde{S}) = e(G, \tilde{Y}_1) \prod_{i=1}^{\ell-1} e(U_i, \tilde{X}_i) e(V, \tilde{G})$$
$$e(R, \tilde{T}_j) = \prod_{i=1}^{\ell-1} e(U_i, \tilde{M}_{(i,j)}) e(G, \tilde{M}_{(\ell,j)}) e(V, \tilde{Y}_j), \quad \forall j$$
> 作用：第一条方程固定签名结构，第二条方程将消息向量 $\tilde{M}$ 和签署者选择的临时公钥 $U$ 绑定。随机化可通过 $(U, R, \tilde{S}, \tilde{T}) \to (U R^\alpha, R^{1/\beta}, (\tilde{S} \prod \tilde{X}_i^{\alpha_i})^\beta, (\tilde{T}_j \prod \tilde{M}_{(i,j)}^{\alpha_i})^\beta)$ 实现。

**[EFSP1签名大小下界]**
$$\kappa + \sigma \ge \sqrt{L}$$
> 作用：表明对于任意在非对称双线性群上的（一次性）SPS，其验证密钥大小 $\kappa$ 与签名大小 $\sigma$ 之和必须至少与消息长度 $L$ 的平方根成正比。这证明了本文EFSP1构造在常数级验证密钥（$\kappa=1$）下的签名大小 $\sigma \approx \sqrt{L}$ 是渐进最优的。

### 实验结果

论文本身未提供软件实验数据，而是从方案的理论效率进行评估，并与现有方案进行对比。核心数值来源于表1、表2和表4：

- **FSP1（基础构造）**：对于 $L=100$ 的消息，签名大小为 $(7, 307)$，即7个 $\mathbb{G}$ 元素和307个 $\tilde{\mathbb{G}}$ 元素，验证方程数为 $7+2L=207$。该方案效率较低，由于签名包含OTS的验证密钥，导致签名大小随消息长度线性增长。
- **FSP2（基于SPTC的主构造）**：通过设置 $k=\ell=10$（即 $L=100$），签名大小优化为 $(27, 24)$，即27个 $\mathbb{G}$ 元素和24个 $\tilde{\mathbb{G}}$ 元素，验证方程数为 $5+k=15$。相比FSP1，签名大小和验证开销均有显著降低，特别是 $\tilde{\mathbb{G}}$ 元素数量减少了12.8倍。
- **EFSP1（通用群模型下的高效构造）**：对于 $L=100$ 的消息，设置 $\ell = k = 10$，签名大小为 $(10, 11)$，即10个 $\mathbb{G}$ 元素和11个 $\tilde{\mathbb{G}}$ 元素，验证方程仅为 $1+k=11$ 个。验证密钥仅需1个 $\mathbb{G}$ 元素，这已是最优。EFSP1在签名大小和验证成本上均远优于前两者。
- **私钥知识证明的开销**（表3）：对于FSP2，证明私钥仅需(10, 10, 2)个元素；而证明一个签名需要 $(28 + 6k + 2\ell, 18 + 8k, 2)$ 个元素。当 $L=100, k=\ell=10$ 时，约为(108, 98, 2)个元素。这远优于现有方案（如对[2]的方案进行FO证明需要超过61,000个元素）。

这些对比清晰地展示了本文构造的优势：FSP2和EFSP1均实现了 $\sqrt{L}$ 量级的签名大小，且私钥知识证明的开销远小于标量分解的方法。EFSP1在牺牲标准模型安全性（依赖通用群模型）的情况下，获得了最优的效率。

### 局限性与开放问题

本文的FSP2依赖xRMA安全的xSIG，而xSIG的构造本身依赖较为复杂的交互假设（DDH2, XDLIN1, co-CDH2），且存在3倍的消息扩展因子。如何构造一个基于更简单标准假设且无消息扩展的xRMA安全的FSPS，是潜在的改进方向。另外，Theorem 11的下界 $\kappa + \sigma \ge \sqrt{L}$ 意味着，若要保持常数级验证密钥，签名大小必然随 $\sqrt{L}$ 增长。一个重要的开放问题是能否构造签名大小为常数（与 $L$ 无关）而验证密钥大小随 $L$ 增长的方案，这可能在带宽受限的应用中更有优势。

### 强关联论文

[2] Abe et al. Constant-size structure-preserving signatures: Generic constructions and simple assumptions. **J. Cryptology 2016** [Google Scholar](https://scholar.google.com/scholar?q=Constant-size+structure-preserving+signatures%3A+Generic+constructions+and+simple+assumptions)

[3] Abe et al. Structure-preserving signatures and commitments to group elements. **J. Cryptology 2016** [Google Scholar](https://scholar.google.com/scholar?q=Structure-preserving+signatures+and+commitments+to+group+elements)

[8] Abe et al. Group to group commitments do not shrink. **EUROCRYPT 2012** [Google Scholar](https://scholar.google.com/scholar?q=Group+to+group+commitments+do+not+shrink)

[28] Damgård et al. Non-interactive and reusable non-malleable commitment schemes. **STOC 2003** [Google Scholar](https://scholar.google.com/scholar?q=Non-interactive+and+reusable+non-malleable+commitment+schemes)

[29] Escala et al. Fine-tuning Groth-Sahai proofs. **PKC 2014** [Google Scholar](https://scholar.google.com/scholar?q=Fine-tuning+Groth-Sahai+proofs)

[38] Groth et al. Efficient noninteractive proof systems for bilinear groups. **SIAM J. Comput. 2012** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+noninteractive+proof+systems+for+bilinear+groups)

[50] Wang et al. How to obtain fully structure-preserving (automorphic) signatures from structure-preserving ones. **ASIACRYPT 2016** [Google Scholar](https://scholar.google.com/scholar?q=How+to+obtain+fully+structure-preserving+(automorphic)+signatures+from+structure-preserving+ones)


## 关键词

+ 完全结构保持签名
+ 双线性群密码构造
+ 收缩结构保持陷门承诺
+ 非交互式知识证明
+ 通用双线性群模型
+ 可随机化签名方案