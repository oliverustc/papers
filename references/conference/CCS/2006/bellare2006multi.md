---
title: "Multi-signatures in the plain public-key model and a general forking lemma"
标题简称:
论文类型: conference
会议简称: CCS
发表年份: 2006
---

## Multi-signatures in the plain public-key model and a general forking lemma

## 发表信息

+ [原文链接](https://dl.acm.org/doi/abs/10.1145/1180405.1180453)

## 作者

+ [Mihir Bellare](Mihir%20Bellare.md) 
+ Gregory Neven 


## 笔记

### 背景与动机
多签名方案允许一组签名者针对同一文件生成一个紧凑的联合签名，在合同签署、联合背书和证书机构分布式管理等场景具有重要应用价值。然而，现有方案存在严重的关键管理瓶颈。Micali、Ohta 与 Reyzin 的方案 [31] 要求在签名前所有潜在签名者必须参与一个专用的交互式密钥生成协议，这一方面迫使签名者集合是静态固定的、无法动态增加成员，另一方面协议本身计算开销大、公钥尺寸随组规模 N 线性增长。Boldyreva 的方案 [11] 和 Lu、Ostrovsky、Sahai、Shacham、Waters 的方案 [29] 虽然免去了专用密钥生成，但采用了知识秘密钥假设，在模型中要求攻击者在提供任意公钥时附上对应的秘密钥。该假设实质上对应于 CA 在证书颁发时必须实施可并发抽取的零知识知识证明，但当前业界标准（如 PKCS#10 和 RFC 4210/4211）仅包含签名式证据，并不满足可抽取性要求，甚至导致已知攻击 [9]。这意味着现有方案若要安全部署，必须大幅修改 CA 的运作方式和客户软件。本文的贡献在于提出了一个在“普通公钥模型”下可证明安全的多签名方案 MS-BN，它不要求专用密钥生成协议，也不依赖知识秘密钥假设，同时签名长度、签名验证速度均不逊于甚至优于现有方案，基于标准的离散对数假设并在随机谕言模型中可证明安全。文中还提出了一个一般性的分叉引理，该引理不依赖签名语境，纯粹刻画算法输出行为的概率性质，可独立应用于其他协议的安全证明。

### 相关工作

[31] Micali, Ohta, Reyzin. Accountable-subgroup multisignatures. **ACM CCS 2001** [Google Scholar](https://scholar.google.com/scholar?q=Accountable-subgroup+multisignatures)
> 核心思路：要求预定义签名者集合执行交互式密钥生成以确保密钥间独立性，签名和验证均仅需一次指数运算。
> 局限与区别：集合静态不可扩展，公钥尺寸依赖组大小 N，本文通过动态公开密钥注册解决了此静态约束。

[11] Boldyreva. Threshold signatures, multisignatures and blind signatures based on the gap-Diffie-Hellman-group signature scheme. **PKC 2003** [Google Scholar](https://scholar.google.com/scholar?q=Threshold+signatures+multisignatures+and+blind+signatures+based+on+the+gap-Diffie-Hellman-group+signature+scheme)
> 核心思路：采用知识秘密钥假设，基于双线性对的 Gap-Diffie-Hellman 群构建签名。
> 局限与区别：依赖双线性对（配对）运算，验证耗时比本文高一个数量级；签名长度虽为 160 比特，本文为 320 比特，但验证更快；关键是需要 KOSK 假设，本文免除此假设。

[29] Lu, Ostrovsky, Sahai, Shacham, Waters. Sequential aggregate signatures and multisignatures without random oracles. **EUROCRYPT 2006** [Google Scholar](https://scholar.google.com/scholar?q=Sequential+aggregate+signatures+and+multisignatures+without+random+oracles)
> 核心思路：在标准模型下基于双线性对构造，不依赖随机谕言，安全假设为 (co)CDH。
> 局限与区别：公钥尺寸 960 比特，系统参数极大（25,920 比特），签名 1120 比特，计算开销高；同样需要 KOSK 假设，本文在各方面均有显著效率优势且随机谕言模型的可证明安全已足够。

[12] Boneh, Gentry, Lynn, Shacham. Aggregate and verifiably encrypted signatures from bilinear maps. **EUROCRYPT 2003** [Google Scholar](https://scholar.google.com/scholar?q=Aggregate+and+verifiably+encrypted+signatures+from+bilinear+maps)
> 核心思路：聚合签名方案，要求消息互异以确保安全，在消息相同的多签名场景下存在脆弱性。
> 局限与区别：即使采用增强消息“公钥||消息”也不能免疫公钥重放攻击（敌手将自身的公钥设为诚实用户相同值），故该方案不能直接作为普通公钥模型下的多签名方案使用；本文通过每个公钥设置独立哈希值加以防范。

[40] Pointcheval, Stern. Security arguments for digital signatures and blind signatures. **Journal of Cryptology 2000** [Google Scholar](https://scholar.google.com/scholar?q=Security+arguments+for+digital+signatures+and+blind+signatures)
> 核心思路：提出经典分叉引理，通过重放攻击者从成功伪造中获得两个可接受的对话，从而提取秘密钥。
> 局限与区别：该引理专门针对 Fiat-Shamir 转换得到的标准签名方案，难以应用于多签名等复杂场景；本文的通用分叉引理剥离了签名上下文，纯粹刻画任意算法的输出概率，扩展性更强。

[8] Bellare, Palacio. GQ and Schnorr identification schemes: Proofs of security against impersonation under active and concurrent attacks. **CRYPTO 2002** [Google Scholar](https://scholar.google.com/scholar?q=GQ+and+Schnorr+identification+schemes+Proofs+of+security+against+impersonation+under+active+and+concurrent+attacks)
> 核心思路：提出 Reset 引理用于身份识别协议的安全证明，通过双次运行提取秘密信息。
> 局限与区别：本文的通用分叉引理可视作 Reset 引理的推广，且证明方法更简洁，同时提供最坏情况时间保证（而非期望时间）。

### 核心技术与方案

**方案构造思路。** MS-BN 方案基于 Schnorr 签名 [42]。设 G 为素数阶 p 的循环群，g 为生成元。经典 Schnorr 签名对消息 m、公钥 X 的输出为 (R, s)，满足 g^s = RX^c，其中 c = H(R || m)。直接扩展为多签名的朴素想法是令签名 (R, s) 满足 g^s = R∏_{i=1}^n X_i^{c}，但该方案受到经典作恶密钥攻击：敌手可以令自己的公钥 X_1 = g^{x_1}·∏_{i=2}^n X_i^{-1}，从而独立为群组 L 伪造签名。

**对抗作恶密钥攻击。** 本文的关键改进在于令每个公钥 X_i 对应一个独立的哈希值 c_i = H_1(X_i || R || ⟨L⟩ || m)。验证方程变为：
$$g^s = R \prod_{i=1}^{n} X_i^{c_i}.$$
即使敌手令其公钥与其他用户的公钥存在函数依赖关系，由于 c_i 依赖于 X_i 自身，无法再通过上述抵消技巧消除非目标公钥的贡献。安全证明利用通用分叉引理，从敌手的两次成功伪造中提取目标公钥 X^* 的离散对数：通过将验证方程相除，得到 g^{s-s'} = (X^*)^{n^*(h-h')}，从而计算出 x^* = (s-s')/(n^*(h-h')) mod p。

**并发签名的仿真。** 签名协议包含四轮交互。第一轮每个签名者提交份额承诺 t_i = H_0(R_i)（其中 R_i = g^{r_i}），第二轮广播 R_i 并验证承诺。模拟器（归约算法）在不知道目标私钥的情况下可以这样仿真：它选择随机值 c_1 并令 s_1 ←$ Z_p，然后通过 R_1 = g^{s_1}·X_1^{-c_1} 反向计算 R_1。由于模拟器在敌手广播 R_i 之前已经通过 H_0 的查询看到了敌手的承诺，它可以提取 R_i 值并计算全局 R，从而正确设置 c_1 并得出 s_1。如果敌手在承诺阶段提前查询 H_0 导致冲突，模拟器中止。

**通用分叉引理。** 令 H 为大小为 h 的集合。给定算法 A，它以输入 x 和 q 个哈希值 h_1,…,h_q 返回 (J, σ)，其中 J ∈ {0,…,q}。定义接受概率 acc = Pr[J ≥ 1]。分叉算法 F_A 对 X 运行 A 两次：第一次获得 (I, σ)，若 I=0 则中止；否则，保持前 I-1 个哈希值不变、重选后续哈希值 h'_I,…,h'_q 并再次运行 A。若第二次输出的 I'=I 且 h_I ≠ h'_I，则成功。引理断言分叉成功的概率满足：
$$ \text{frk} \ge \text{acc}\cdot\left(\frac{\text{acc}}{q} - \frac{1}{h}\right), \quad \text{或等价地} \quad \text{acc} \le \frac{q}{h} + \sqrt{q\cdot\text{frk}}.$$
该引理不依赖签名方案或随机谕言，仅基于概率分析（利用 Jensen 不等式和 Cauchy-Schwarz 型不等式），因此可直接用于多签名等复杂场景，且提供最坏情况时间保证而非期望时间。

**安全性概要。** 若存在敌手 F 以时间 t 发起 q_S 次签名查询、q_H 次哈希查询、涉及最多 N 个公钥的攻击，以概率 ε 成功伪造，则存在算法 B 以概率 ε' 求解离散对数问题：
$$ \epsilon' \ge \frac{\epsilon^2}{q_H+q_S} - \frac{2q_H+16N^2q_S}{2^{l_0}} - \frac{8Nq_S}{2^k} - \frac{1}{2^{l_1}}, $$
运行时间 t' = 2t + q_S·t_{exp} + O((q_S+q_H)(1+q_H+Nq_S))。归约依赖于随机谕言和离散对数假设，不需要知识秘密钥假设。

**复杂度。** 签名者需执行 1 次指数运算（含多指数化为单指数等价），验证也需 1 次指数运算；签名大小 320 比特，公钥 160 比特，系统参数 160 比特；协议需要 4 轮交互，支持并发签名会话。

### 核心公式与流程

**[验证方程]**
$$g^{s} = R \prod_{i=1}^{n} X_{i}^{c_{i}}, \quad c_i = H_1(X_i \| R \| \langle L \rangle \| m)$$
> 通过为每个公钥分配独立哈希值，防止作恶密钥攻击；敌手无法通过抵消的方式将多个公钥的贡献合并。

**[分叉引理概率不等式]**
$$\mathrm{frk} \ge \mathrm{acc} \cdot \left(\frac{\mathrm{acc}}{q} - \frac{1}{h}\right)$$
> 从单次接受概率 acc 导出两次分叉成功概率 frk 的下界；用于从伪造者提取目标秘密钥。

**[离散对数提取公式]**
$$x^* = \frac{s - s'}{n^*(h - h')} \bmod p$$
> 从分叉获得的两个有效签名 (R,s) 和 (R,s') 中提取目标公钥 X^* 的离散对数；要求两次签名中目标公钥对应的哈希值不同。

**[签名协议（四轮）]**
第1轮：签名者 i 选择 r_i ←$ Z_p，计算 R_i = g^{r_i}，t_i = H_0(R_i)，广播 t_i。
第2轮：广播 R_i。
第3轮：验证 t_i = H_0(R_i)，计算 R = ∏_i R_i，c_i = H_1(X_i || R || ⟨L⟩ || m)，s_i = x_i·c_i + r_i mod p，广播 s_i。
第4轮：计算 s = ∑_i s_i mod p，输出签名 σ = (R, s)。
> 增加承诺轮次允许模拟器通过 H_0 查询提取敌手的 R_i、预先计算 R 并正确编程 H_1，实现并发签名仿真。

### 实验结果
由于该论文是理论性方案设计，未提供实际系统实验部署或数据集上的运行时间测量。但在表 1 中给出了与三种可证明安全的多签名方案的性能对比（基于 160 比特椭圆曲线群和 1024 比特 RSA 安全水平）。MS-BN 的签名验证仅需 1 次指数运算，而基于配对的 MS-Bo [11] 需要 2 次配对运算（约等于 12-40 次指数运算），MS-LOSSW [29] 需要 2 次配对运算且签名长度为 1120 比特。MS-BN 的公钥尺寸仅为 160 比特，而 MS-Bo 为 960 比特、MS-LOSSW 为 960 比特。签名生成成本均为 1 次指数运算，与 MS-MOR [31] 无异但 MS-MOR 的密钥生成协议开销巨大且公钥依赖组大小 N。因此，MS-BN 在证明复杂度、签名/验证计算量和公钥尺寸方面均具有明显优势。该方案适用于任意规模的消息和签名者群组，安全性紧度优于 MS-MOR 但非完全紧归约，实际安全级别高于理论估计。

### 局限性与开放问题
尽管 MS-BN 显著降低了密钥管理开销，但其安全性归约并非紧的（公式 (4) 中的 ε' 包含 O(ε²/(q_H+q_S)) 的劣化），且整体证明依赖随机谕言模型，未在标准模型下给出安全性。协议需要四轮交互，虽然常数轮，但在某些低时延环境中仍可能成为瓶颈。开放问题包括：能否构造普通公钥模型下紧归约的多签名方案？标准模型下是否存在同等高效的构造？能否将通用分叉引理进一步推广到更多交互式协议（如身份识别或可否认认证）的安全性证明中？

### 强关联论文

[31] Micali, Ohta, Reyzin. Accountable-subgroup multisignatures. **ACM CCS 2001** [Google Scholar](https://scholar.google.com/scholar?q=Accountable-subgroup+multisignatures)

[11] Boldyreva. Threshold signatures, multisignatures and blind signatures based on the gap-Diffie-Hellman-group signature scheme. **PKC 2003** [Google Scholar](https://scholar.google.com/scholar?q=Threshold+signatures+multisignatures+and+blind+signatures+based+on+the+gap-Diffie-Hellman-group+signature+scheme)

[29] Lu, Ostrovsky, Sahai, Shacham, Waters. Sequential aggregate signatures and multisignatures without random oracles. **EUROCRYPT 2006** [Google Scholar](https://scholar.google.com/scholar?q=Sequential+aggregate+signatures+and+multisignatures+without+random+oracles)

[12] Boneh, Gentry, Lynn, Shacham. Aggregate and verifiably encrypted signatures from bilinear maps. **EUROCRYPT 2003** [Google Scholar](https://scholar.google.com/scholar?q=Aggregate+and+verifiably+encrypted+signatures+from+bilinear+maps)

[9] Bellare, Ristenpart, Yilek. Work in progress, 2006. **未公开发表** [Google Scholar](https://scholar.google.com/scholar?q=Bellare+Ristenpart+Yilek+2006+proof+of+possession+attack) — 此处因原文为工作进展且非正式发表，无标准索引，但为理解 KOSK 假设的攻击不可或缺。

[40] Pointcheval, Stern. Security arguments for digital signatures and blind signatures. **Journal of Cryptology 2000** [Google Scholar](https://scholar.google.com/scholar?q=Security+arguments+for+digital+signatures+and+blind+signatures)

[8] Bellare, Palacio. GQ and Schnorr identification schemes: Proofs of security against impersonation under active and concurrent attacks. **CRYPTO 2002** [Google Scholar](https://scholar.google.com/scholar?q=GQ+and+Schnorr+identification+schemes+Proofs+of+security+against+impersonation+under+active+and+concurrent+attacks)

[42] Schnorr. Efficient signature generation by smart cards. **Journal of Cryptology 1991** [Google Scholar](https://scholar.google.com/scholar?q=Efficient+signature+generation+by+smart+cards)

[5] Bellare, Goldreich. On defining proofs of knowledge. **CRYPTO 1992** [Google Scholar](https://scholar.google.com/scholar?q=On+defining+proofs+of+knowledge)

[30] Lysyanskaya, Micali, Reyzin, Shacham. Sequential aggregate signatures from trapdoor permutations. **EUROCRYPT 2004** [Google Scholar](https://scholar.google.com/scholar?q=Sequential+aggregate+signatures+from+trapdoor+permutations)


## 关键词

+ 多重签名
+ 普通公钥模型
+ 分叉引理
+ 数字签名
+ 密钥管理