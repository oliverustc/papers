---
title: "Election verifiability or ballot privacy: Do we need to choose"
标题简称:
论文类型: conference
会议简称: ESORICS
发表年份: 2013
---

## Election verifiability or ballot privacy: Do we need to choose

## 发表信息

+ [原文链接](https://link.springer.com/chapter/10.1007/978-3-642-40203-6_27)

## 作者

+ Edouard Cuvelier 
+ Olivier Pereira 
+ Thomas Peters 


## 笔记

### 背景与动机

在电子投票系统中，正确性与隐私性这两个基本属性之间存在天然冲突：提供可公开验证的审计线索（audit trail）以保障选举正确性，往往会因为审计信息的泄露而削弱选票的长期隐私。大多数现有的通用可验证投票方案（如 Helios [3]、Scantegrity II [11]）发布的审计信息是建立在计算安全假设之上的加密数据：一旦未来计算能力提升或出现密码分析突破，这些密文就可能被破解，从而暴露个人投票行为。这种对“未来隐私丧失”的担忧不仅可能使选民产生恐惧而被胁迫，而且削弱了引入可验证技术的正当性——方案用计算性隐私换取正确性，但突破后两者皆失。

极少数提供完美隐私（everlasting privacy）的方案，如基于盲签名 [22] 或秘密共享 [15, 33] 的方法，要么要求选民工作量与受托机构数量线性相关，要么依赖不可实用的安全信道或低效的 cut-and-choose 证明。因此，如何在保持与 Cramer、Gennaro、Schoenmakers [16] 相同最优效率（即选民工作量与选民数及受托人数无关）的同时，提供一种审计线索本身具备完美隐私（即使面对无限计算能力的对手也能保护隐私）的方案，是一个未解决的关键问题。本文提出的承诺一致加密（CCE）原语正是旨在填补这一空白：它使得在传统投票方案基础上添加可验证性成为一种纯收益——在不对隐私造成任何妥协的前提下，实现与原始系统同等高效的可验证性。

### 相关工作

[15] Cramer 等. A secure and optimally efficient multi-authority election scheme. **EUROCRYPT 1997** [Google Scholar](https://scholar.google.com/scholar?q=A+secure+and+optimally+efficient+multi-authority+election+scheme)
> 核心思路：提出第一个选民工作量与受托人数无关的通用可验证投票方案，基于 ElGamal 加密和零知识证明。
> 局限与区别：审计线索（加密的选票）仅提供计算性隐私，一旦加密被破解将泄露投票关系；本文通过 CCE 原语将审计线索替换为完美隐藏承诺，在同样效率水平下实现完美隐私。

[22] Fujioka 等. A practical secret voting scheme for large scale elections. **AUSCRYPT 1992** [Google Scholar](https://scholar.google.com/scholar?q=A+practical+secret+voting+scheme+for+large+scale+elections)
> 核心思路：基于盲签名和匿名信道实现投票，审计线索仅含匿名信息，可提供完美隐私。
> 局限与区别：依赖可靠的匿名信道，在大规模选举中部署极具挑战；本文不依赖任何特殊信道，属于“阈值加密选票”范式。

[33] Moran & Naor. Receipt-free universally-verifiable voting with everlasting privacy. **CRYPTO 2006** [Google Scholar](https://scholar.google.com/scholar?q=Receipt-free+universally-verifiable+voting+with+everlasting+privacy)
> 核心思路：通过秘密共享将选票分发给多个受托机构，实现永恒隐私。
> 局限与区别：选民在选票准备阶段的工作量与受托机构数量线性相关，不适合大规模选举；本文方案中选民工作量与受托人数无关。

[16] Cramer 等. A secure and optimally efficient multi-authority election scheme. **EUROCRYPT 1997** [Google Scholar](https://scholar.google.com/scholar?q=A+secure+and+optimally+efficient+multi-authority+election+scheme)
> 核心思路：提出“最优效率”概念，即选民工作量与选民总数和受托人数无关，计票方工作量线性于选民数。该文方案采用计算性审计线索。
> 局限与区别：本文在保持该最优效率下将其推广至完美隐私审计线索，且未引入昂贵的 cut-and-choose 技术。

[20] Demirel 等. Improving Helios with everlasting privacy towards the public. **EVT/WOTE 2012** [Google Scholar](https://scholar.google.com/scholar?q=Improving+Helios+with+everlasting+privacy+towards+the+public)
> 核心思路：基于 Pedersen 承诺与 Paillier 加密的组合，试图为 Helios 增加永恒隐私。
> 局限与区别：该方案依赖于 cut-and-choose 零知识证明，在可比安全级别下比本文慢约 4 个数量级，且密钥生成需要复杂的安全多方计算协议；本文的方案不使用 cut-and-choose，指数运算次数与安全参数无关。

[4] Arapinis 等. Practical everlasting privacy. **POST 2013** [Google Scholar](https://scholar.google.com/scholar?q=Practical+everlasting+privacy)
> 核心思路：用符号模型对 everlasting privacy 进行形式化建模。
> 局限与区别：该工作偏向于形式化分析与建模，不提供具体的加密原语构造；本文则提供具体的可实例化的 CCVA 加密方案及其安全性证明。

### 核心技术与方案

**1. 整体框架：从 CCE 到 CCVAE 再到 Minivoting 方案**

本文构造的核心是**承诺一致加密（CCE）**及其**有效性增强版本（CCVAE）**。一个 CCE 方案给出了六元算法（Gen, Enc, Dec, DeriveCom, Open, Verify），其核心特征是：从任何 CCE 密文 $c$ 中，可使用 DeriveCom 算法导出一个对消息 $m$ 的承诺 $d$；同时，私钥 $sk$ 可用于 Open 算法产生该承诺的打开信息 $a$。正确性要求满足：$\text{Verify}(pk, \text{DeriveCom}(pk,c), \text{Dec}(sk,c), \text{Open}(sk,c)) = 1$。

在实际投票中，选民对选票 $v$ 运行 $c \leftarrow \text{Enc}(pk, v)$，然后将 $c$（可能带有有效性证明）发送给计票机构。计票机构将 $\text{DeriveCom}(pk, c)$ 发布在公开告示板 PB 上，而将密文 $c$ 存储在秘密告示板 SB 上。因为从 DeriveCom 输出的承诺 $d$ 是完美隐藏的（即其分布独立于消息 $v$），任何仅能访问 PB 的对手（即使拥有无限计算能力）都无法从 $d$ 恢复 $v$，从而实现了永久隐私（PPAT）。而真实选票 $c$（以及后续的各步骤数据）仅在 SB 上由受托机构处理，SB 数据的隐私保护依赖于计算安全的加密方案。这个 Minivoting 方案 Enc2Vote($\Pi,\rho$) 的安全性由两个定理保障：若 DeriveCom 完美隐藏，则方案具有 PPAT（定理性 1）；若底层的 CCVAE 方案是 NM-CPA 安全的，则方案具有 Ballot Privacy（定理 2，源自 [9]）。

**2. 有效性增强（Validity Augmentation）**

仅靠 CCE 不足以防止恶意选民产生“不一致”的密文——即密文的 Dec 输出与承诺的打开不一致，导致计票过程受阻。因此，本文引入 CCVAE：在 CCE 之上增加一个有效性证明 $\sigma_{cc}$，通过 Valid 算法验证；再通过 Strip 算法去除该证明后恢复成标准的 CCE 密文，以支持同态运算等高阶操作。

**3. 具体构造一：PPATS（适用于同态计票的简单选票）**

PPATS 方案的底层 CCE 密文为
$$c = (d, c_1, c_2) = (h^r h_1^m,\ g^s,\ g^r g_1^s)$$
其中 $d$ 是对 $m$ 的完美隐藏承诺（TC2 承诺 [1]），$(c_1, c_2) = (g^s, g^r g_1^s)$ 是对底数 $g^r$ 的 ElGamal 加密，而 $g^r$ 正好是 $d$ 打开所需的辅助值。私钥 $sk = x_1$ 满足 $g_1 = g^{x_1}$，解密时通过计算 $m$ 满足 $e(c_1^{x_1}/c_2, h)\cdot e(g, d) = e(g, h_1)^m$ 来恢复 $m$（需要穷举搜索，限制于小结果空间）。有效性证明采用标准的 Schnorr 型 Sigma 协议（在随机谕言模型下是零知识的）。因为同态性保持，计票时可将所有选票的多成分分别相乘得到单个结果密文。

**4. 具体构造二：PPATC（适用于混网计票的复杂选票）**

PPATC 方案对消息 $m \in \mathbb{G}_1$ 的加密为
$$c = (c_1, c_2, c_3, d_1, d_2) = (g^{r_1},\ g^{r_2},\ g_1^r g_2^{r_2},\ h^r h_1^{r_1},\ m g_1^{r_1})$$
其中 $(d_1, d_2)$ 是完美隐藏承诺（将 $m$ 埋入 $d_2$），解密通过 $m = d_2 / c_1^{x_1}$ 直接计算，无需穷举搜索。有效性证明类似地基于 Sigma 协议，验证密文各成分间的关系正确。该方案适合混网（shuffle）：先对密文进行置换和重新随机化（利用同态性质），再逐份解密并公开打开信息。open $a = c_3 / c_2^{x_2} = g_1^r$。

**5. 渐进复杂度**

两个方案中，选民的准备工作（计算一个 CCVA 密文）在 SXDH 曲线上仅需常数次（PPATS 为 6 个 $\mathbb{G}_1$ 标量乘、6 个 $\mathbb{G}_2$ 标量乘；PPATC 为 9 个 $\mathbb{G}_1$ 标量乘、4 个 $\mathbb{G}_2$ 标量乘，具体见表 1），与选民总数和受托机构数无关。计票方的工作量线性于选民数（对 PPATS 是逐积相乘，对 PPATC 是混网操作并以 n 为规模执行线性次配对验证）。相比先前提供完美隐私的方案（如 PPATP，基于 Paillier 和 Pedersen 承诺），PPATS 和 PPATC 快约 40 倍。

### 核心公式与流程

**[PPATS 加密]**
$$c = (d, c_1, c_2) = (h^r h_1^m,\ g^s,\ g^r g_1^s)$$
> 作用：密文由三部分组成：$d$ 是一个完美隐藏的 TC2 承诺（绑定于消息 $m$ 和随机数 $r$），$(c_1, c_2)$ 是对 $g^r$ 的 ElGamal 加密（随机数 $s$）。解密时通过双线性对运算求解 $m$ 使得 $e(c_1^{x_1}/c_2, h) \cdot e(g, d) = e(g, h_1)^m$。Open 输出 $a = g^r = c_2/c_1^{x_1}$。

**[PPATC 加密]**
$$c = (c_1, c_2, c_3, d_1, d_2) = (g^{r_1},\ g^{r_2},\ g_1^r g_2^{r_2},\ h^r h_1^{r_1},\ m g_1^{r_1})$$
> 作用：密文包含五个元素。$d_2$ 是消息 $m$ 被 $g_1^{r_1}$ 盲化后的值，$d_1$ 是 $h^r h_1^{r_1}$ 形式的承诺（对 $(r, r_1)$ 的 Pedersen 承诺），$c_1, c_2, c_3$ 用于在解密时恢复 $g_1^{r_1}$（解密：$m = d_2/c_1^{x_1}$）以及打开辅助值 $a = c_3/c_2^{x_2} = g_1^r$。验证如下成立：$e(g, d_1) = e(a, h)e(d_2/m, h_1)$。

**[有效性证明（Sigmal 协议用于 PPATS）]**
$$\begin{align*}
& \text{证明者：}(m, r, s), \ \text{随机数：}(t, u, v)\\
& c' \leftarrow \text{Enc}_S(pk, (t, u, v)) = (h^u h_1^t,\ g^v,\ g^u g_1^v)\\
& \nu_{cc} \leftarrow \mathcal{H}(pk, c, c')\\
& z \leftarrow (z_m, z_r, z_s) = (t + \nu_{cc} m, u + \nu_{cc} r, v + \nu_{cc} s)\\
& \text{验证者：} c' \stackrel{?}{=} \text{Enc}_S(pk, z) \cdot c^{-\nu_{cc}}
\end{align*}$$
> 作用：使用 Fiat-Shamir 变换的非交互式零知识证明，证明密文 $c$ 是已知 $(m, r, s)$ 下诚实生成的，从而保证 Valid 检查通过后密文的 Strip 版本与 Dec 和 Open 一致。

### 实验结果

实验评估基于 SXDH 双线性群设定：选择 $\mathbb{G}_1$ 为 256 位素数域上的椭圆曲线群，$\mathbb{G}_2$ 为同一域的二次扩域上的群。表 1 给出了生成一个 CCVA 密文（含有效性证明）的计算开销，以 256 位整数乘法为单位。基线方案 PPATP（基于 Paillier 加密 + Pedersen 承诺）在 0/1 投票场景下总成本约为 4,202,496 单位，256 位选票下降低至 3,809,280 单位，依然很高。作为对比，PPATS（0/1 投票）总成本仅 115,200 单位，约为 PPATP 的 1/36；PPATC（256 位选票）总成本 96,000 单位，约为 PPATP 的 1/40。效率提升的主要原因在于 PPATS 和 PPATC 运行在更短的素数阶群上且避免了模 $N^2$ 的大指数运算。论文还指出，使用 JSBN 库在 Chrome 浏览器中仅需不到 1 秒即可计算编码 256 位选票的 PPATC 密文，表明该方案可以流畅在 JavaScript 环境如 Helios 中运行。

### 局限性与开放问题

尽管 PPATS 和 PPATC 方案极大提升效率并提供了完美的审计线索隐私，它们仍有局限性。首先，PPATS 因其解密依赖对消息空间的穷举搜索，仅适用于结果空间较小的选举（如简单赞成计数），而无法支持需要高熵结果的复杂计票规则。PPATC 虽支持任意消息格式且解密高效，但基于混网的计票流程会揭示比同态计票更多的信息（如各选票之间的对应关系经重排后依然公开了选票本身的统计分布）。其次，本文末节提到，将方案集成到现有系统如 Helios 时，会在 accountability（问责性）分析中引入新的困难：Validate 过程不可公开验证，导致 voter 与 authorities 之间的责任分配不明确——这些问题需要更完整的可验证性/问责性形式化模型来刻画。最后，本文未专门解决持摄影设备在投票间内的强迫/收买等更广泛的 coercion 问题。

### 强关联论文

[16] Cramer et al. A secure and optimally efficient multi-authority election scheme. **EUROCRYPT 1997** [Google Scholar](https://scholar.google.com/scholar?q=A+secure+and+optimally+efficient+multi-authority+election+scheme)

[15] Cramer et al. Multi-authority secret-ballot elections with linear work. **EUROCRYPT 1996** [Google Scholar](https://scholar.google.com/scholar?q=Multi-authority+secret-ballot+elections+with+linear+work)

[1] Abe et al. Signing on elements in bilinear groups for modular protocol design. **IACR Cryptology ePrint Archive 2010** [Google Scholar](https://scholar.google.com/scholar?q=Signing+on+elements+in+bilinear+groups+for+modular+protocol+design)

[7] Benaloh. Verifiable Secret-Ballot Elections. **PhD thesis, Yale University 1987** [Google Scholar](https://scholar.google.com/scholar?q=Verifiable+Secret-Ballot+Elections)

[22] Fujioka et al. A practical secret voting scheme for large scale elections. **AUSCRYPT 1992** [Google Scholar](https://scholar.google.com/scholar?q=A+practical+secret+voting+scheme+for+large+scale+elections)

[33] Moran & Naor. Receipt-free universally-verifiable voting with everlasting privacy. **CRYPTO 2006** [Google Scholar](https://scholar.google.com/scholar?q=Receipt-free+universally-verifiable+voting+with+everlasting+privacy)

[33] Moran & Naor. Split-ballot voting: Everlasting privacy with distributed trust. **ACM Trans. Inf. Syst. Secur. 2010** [Google Scholar](https://scholar.google.com/scholar?q=Split-ballot+voting:+Everlasting+privacy+with+distributed+trust)

[20] Demirel et al. Improving Helios with everlasting privacy towards the public. **EVT/WOTE 2012** [Google Scholar](https://scholar.google.com/scholar?q=Improving+Helios+with+everlasting+privacy+towards+the+public)

[4] Arapinis et al. Practical everlasting privacy. **POST 2013** [Google Scholar](https://scholar.google.com/scholar?q=Practical+everlasting+privacy)

[9] Bernhard et al. How not to prove yourself: Pitfalls of the fiat-shamir heuristic and applications to Helios. **ASIACRYPT 2012** [Google Scholar](https://scholar.google.com/scholar?q=How+not+to+prove+yourself:+Pitfalls+of+the+fiat-shamir+heuristic+and+applications+to+Helios)


## 关键词

+ 承诺一致性加密
+ 完美隐私审计轨迹
+ 通用可验证投票
+ 永久隐私
+ 高效加密构造